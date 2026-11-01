#!/usr/bin/env bash
# receipt_probe.sh - round-76 calibration criterion R (record-vs-reality
# receipt fidelity for SOURCES rows that quote counting commands).
#
# Carries the r75 carry-in item 1: S444's aggregated "grep -cE 'inspect_'
# prints 0" is false on the --llms leg (actual 2: inspect_macho,
# inspect_signature); the doctor leg is 0. The superseding row S445 must
# record the exact per-leg counts, and the base row must be flaggable.
#
# Legs:
#   1. rea --llms  | grep -cE 'inspect_'  == 2, names == {inspect_macho, inspect_signature}
#   2. rea doctor  | grep -cE 'inspect_'  == 0
#   3. corpus/SOURCES.md S445 row records those exact per-leg values
#   4. negative control: base S444 row's single-number record is flagged
#      (its "prints 0" contradicts leg 1's actual count)
# Exit 0 iff all four legs hold. Value lines only; the caller logs them.
set -u
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
BASE="6f3a646c691017f92012fc4cf928d9e946838b84"
SOURCES="$ROOT/corpus/SOURCES.md"
fail=0

llms_n="$(rea --llms 2>/dev/null | grep -cE 'inspect_' || true)"
llms_names="$(rea --llms 2>/dev/null | grep -oE 'inspect_[a-z_]+' | sort -u | tr '\n' ' ')"
llms_names="$(echo "$llms_names" | sed 's/ $//')"
echo "RECEIPT_LLMS_COUNT=$llms_n"
echo "RECEIPT_LLMS_NAMES=$llms_names"
if [ "$llms_n" = "2" ] && [ "$llms_names" = "inspect_macho inspect_signature" ]; then
  echo "RECEIPT_LEG1=pass"
else
  echo "RECEIPT_LEG1=FAIL (expected 2 / 'inspect_macho inspect_signature')"
  fail=1
fi

doctor_n="$(rea doctor 2>/dev/null | grep -cE 'inspect_' || true)"
echo "RECEIPT_DOCTOR_COUNT=$doctor_n"
if [ "$doctor_n" = "0" ]; then
  echo "RECEIPT_LEG2=pass"
else
  echo "RECEIPT_LEG2=FAIL (expected 0)"
  fail=1
fi

if [ -f "$SOURCES" ] && grep -q '^| S445 ' "$SOURCES"; then
  row="$(grep '^| S445 ' "$SOURCES")"
  ok3=1
  echo "$row" | grep -qF 'llms=2 (inspect_macho, inspect_signature)' || ok3=0
  echo "$row" | grep -qF 'doctor=0' || ok3=0
  echo "$row" | grep -qF 'supersedes S444' || ok3=0
  if [ "$ok3" = "1" ]; then
    echo "RECEIPT_LEG3=pass"
  else
    echo "RECEIPT_LEG3=FAIL (S445 row lacks exact per-leg tokens)"
    fail=1
  fi
else
  echo "RECEIPT_LEG3=FAIL (S445 row absent)"
  fail=1
fi

base_row="$(git -C "$ROOT" show "$BASE:corpus/SOURCES.md" 2>/dev/null | grep '^| S444 ' || true)"
if [ -n "$base_row" ] && echo "$base_row" | grep -qF "prints 0"; then
  if [ "$llms_n" != "0" ]; then
    echo "RECEIPT_LEG4=S444_MISMATCH_FLAGGED (base row records 'prints 0'; actual llms leg prints $llms_n)"
  else
    echo "RECEIPT_LEG4=FAIL (negative control did not fire)"
    fail=1
  fi
else
  echo "RECEIPT_LEG4=FAIL (base S444 row not found or lacks the recorded claim)"
  fail=1
fi

echo "RECEIPT_VERDICT=$([ $fail = 0 ] && echo green || echo red)"
exit "$fail"
