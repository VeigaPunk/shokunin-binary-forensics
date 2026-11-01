#!/usr/bin/env bash
# receipt_probe2.sh - round-79 criterion R instrument, revision 2.
#
# Supersedes reports/round-76/receipt_probe.sh (v1; frozen bytes, its registry
# row stays for those bytes). Closes the v1 routed debt recorded at
# registration (r78): the §Gate-standard self-test clause and a declared
# usage exit. Plain mode (no arguments) is v1-identical: same legs, same
# value lines, same verdict contract over the installed rea's operation
# names, the pinned S445 row and the pinned S444 base-row negative control.
#
# Modes:
#   (no args)    plain criterion-R run (v1-identical value lines; 0 green /
#                1 red)
#   --selftest   hermetic self-test per the §Gate standard: embedded temp
#                fixtures only, no network, no live-tree write, NO producer
#                call (runs with the rea directory stripped from PATH in the
#                committed receipts); asserts the exit code and the stable
#                expected finding-ids committed in claims.md and the SKILL.md
#                registry row:
#                  RECEIPT_SELFTEST_LLMS_VERDICT=ok
#                  RECEIPT_SELFTEST_TOKEN_CHECK=ok
#                  RECEIPT_SELFTEST_NEGCTL_LOGIC=ok
#                  RECEIPT_SELFTEST=pass          (last line, exit 0)
#                a verdict function blinded to accept any count dies with the
#                attributed last line "selftest: per-leg receipt verdict
#                accepted any count" (frozen sed mutant pinned in
#                reports/round-79/claims.md)
#   other        usage line on stderr, exit 64 (declared in the registry row)
set -u

llms_ok() { [ "$1" = "2" ] && [ "$2" = "inspect_macho inspect_signature" ]; }

row_tokens_ok() { # <row-line> -> 0 iff the exact per-leg tokens are present
  echo "$1" | grep -qF 'llms=2 (inspect_macho, inspect_signature)' &&
    echo "$1" | grep -qF 'doctor=0' &&
    echo "$1" | grep -qF 'supersedes S444'
}

negctl_fires() { # <base-row-line> <actual-count> -> 0 iff LEG4's flag must fire
  echo "$1" | grep -qF "prints 0" && [ "$2" != "0" ]
}

if [ "${1:-}" = "--selftest" ]; then
  # ST1: the per-leg verdict function accepts exactly the recorded counts
  if ! llms_ok "2" "inspect_macho inspect_signature"; then
    echo "RECEIPT_SELFTEST=fail (ST1: recorded per-leg verdict rejected)"
    echo "selftest: exact receipt verdict rejected matching counts"
    exit 1
  fi
  if llms_ok "0" ""; then
    echo "RECEIPT_SELFTEST=fail (ST1: wrong count accepted)"
    echo "selftest: per-leg receipt verdict accepted any count"
    exit 1
  fi
  echo "RECEIPT_SELFTEST_LLMS_VERDICT=ok"
  # ST2: the row token check accepts a complete row, rejects a clipped one
  FAKE_ROW='| S445 | per-leg receipt correction | docs | x | y | opened | mined | used-by=z | rea per-leg receipts: llms=2 (inspect_macho, inspect_signature); doctor=0; supersedes S444 | - | - | - |'
  if ! row_tokens_ok "$FAKE_ROW"; then
    echo "RECEIPT_SELFTEST=fail (ST2: complete row rejected)"
    echo "selftest: token check rejected a complete row"
    exit 1
  fi
  if row_tokens_ok "${FAKE_ROW/doctor=0/doctor=1}"; then
    echo "RECEIPT_SELFTEST=fail (ST2: clipped row accepted)"
    echo "selftest: token check accepted an incomplete row"
    exit 1
  fi
  echo "RECEIPT_SELFTEST_TOKEN_CHECK=ok"
  # ST3: the negative-control logic fires on the recorded mismatch and only
  # there
  FAKE_BASE='| S444 | aggregated receipt | docs | x | y | opened | mined | used-by=z | grep -cE inspect_ prints 0 | - | - | - |'
  if ! negctl_fires "$FAKE_BASE" "2"; then
    echo "RECEIPT_SELFTEST=fail (ST3: mismatch not flagged)"
    echo "selftest: negative control missed the recorded mismatch"
    exit 1
  fi
  if negctl_fires "$FAKE_BASE" "0"; then
    echo "RECEIPT_SELFTEST=fail (ST3: flag fired without a mismatch)"
    echo "selftest: negative control fired without a mismatch"
    exit 1
  fi
  echo "RECEIPT_SELFTEST_NEGCTL_LOGIC=ok"
  echo "RECEIPT_SELFTEST=pass"
  exit 0
fi
if [ "$#" -ne 0 ]; then
  echo "usage: receipt_probe2.sh [--selftest]" >&2
  exit 64
fi
# ---- plain mode: v1 logic from here (byte-identical value lines) ----
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
BASE="6f3a646c691017f92012fc4cf928d9e946838b84"
SOURCES="$ROOT/corpus/SOURCES.md"
fail=0

llms_n="$(rea --llms 2>/dev/null | grep -cE 'inspect_' || true)"
llms_names="$(rea --llms 2>/dev/null | grep -oE 'inspect_[a-z_]+' | sort -u | tr '\n' ' ')"
llms_names="$(echo "$llms_names" | sed 's/ $//')"
echo "RECEIPT_LLMS_COUNT=$llms_n"
echo "RECEIPT_LLMS_NAMES=$llms_names"
if llms_ok "$llms_n" "$llms_names"; then
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
  if row_tokens_ok "$row"; then
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
  if negctl_fires "$base_row" "$llms_n"; then
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
