#!/usr/bin/env bash
# selftest_probe.sh - round-79 C2 counting instrument (§Gate-standard
# self-test conformance for a gate pair).
#
# Usage: bash reports/round-79/selftest_probe.sh <gate-script> <receipt-script>
#
# For the given pair of gate scripts, prints three counters:
#   SELFTEST_MODE_PRESENT=n/2
#       "<script> --selftest" under a PATH with the producer's directory
#       removed exits 0 with the expected stable pass finding-id as the last
#       line (GATE_SELFTEST=pass / RECEIPT_SELFTEST=pass).
#   SELFTEST_MUTANT_KILLED_ATTRIBUTED=n/2
#       the pinned sed mutant (recipes pinned in reports/round-79/claims.md,
#       embedded here verbatim) exits 1 with its attributed marker as the
#       last line:
#         gate:    selftest: blind comparator accepted mutated receipt
#         receipt: selftest: per-leg receipt verdict accepted any count
#   USAGE_EXIT64=n/2
#       an unrecognized invocation form exits 64 (declared usage exit).
#
# The same command measures the v1 instruments (red-before: no selftest mode,
# no usage exit, no attributed kill) and the v2 instruments (green). Exit 0
# iff all three counters are full.
set -u
if [ "$#" -ne 2 ]; then
  echo "usage: selftest_probe.sh <gate-script> <receipt-script>" >&2
  exit 64
fi
G="$1"; R="$2"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

REA_BIN="$(command -v rea || true)"
REA_DIR="$(dirname "$REA_BIN")"
STRIPPED="$(printf '%s' "$PATH" | tr ':' '\n' | grep -vFx "$REA_DIR" | paste -sd:)"

selftest_ok() { # <script> <pass-marker> -> 0 iff hermetic green + marker
  local out rc
  out="$(PATH="$STRIPPED" bash "$1" --selftest 2>/dev/null)"
  rc=$?
  [ "$rc" -eq 0 ] && [ "$(printf '%s\n' "$out" | tail -n 1)" = "$2" ]
}

mutant_killed() { # <script> <sed-expr> <attributed-marker> -> 0 iff kill
  local out rc
  sed "$2" "$1" > "$TMP/mutant.sh" || return 1
  cmp -s "$TMP/mutant.sh" "$1" && return 1   # sed must have changed bytes
  out="$(PATH="$STRIPPED" bash "$TMP/mutant.sh" --selftest 2>/dev/null)"
  rc=$?
  [ "$rc" -eq 1 ] && [ "$(printf '%s\n' "$out" | tail -n 1)" = "$3" ]
}

usage64() { # <script> -> 0 iff unrecognized form exits 64
  bash "$1" --not-a-mode >/dev/null 2>&1
  [ "$?" -eq 64 ]
}

SG=0; selftest_ok "$G" "GATE_SELFTEST=pass" && SG=1
SR=0; selftest_ok "$R" "RECEIPT_SELFTEST=pass" && SR=1
echo "SELFTEST_MODE_PRESENT=$((SG + SR))/2"

MG=0; mutant_killed "$G" \
  's/sys.exit(0 if key(sys.argv\[1\]) == key(sys.argv\[2\]) else 1)/sys.exit(0)/' \
  "selftest: blind comparator accepted mutated receipt" && MG=1
MR=0; mutant_killed "$R" \
  's|^llms_ok() {.*|llms_ok() { return 0; }|' \
  "selftest: per-leg receipt verdict accepted any count" && MR=1
echo "SELFTEST_MUTANT_KILLED_ATTRIBUTED=$((MG + MR))/2"

UG=0; usage64 "$G" && UG=1
UR=0; usage64 "$R" && UR=1
echo "USAGE_EXIT64=$((UG + UR))/2"

[ "$((SG + SR))" = 2 ] && [ "$((MG + MR))" = 2 ] && [ "$((UG + UR))" = 2 ]
