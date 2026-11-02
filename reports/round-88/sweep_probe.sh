#!/usr/bin/env bash
# sweep_probe.sh - round-88 C1 counting instrument (Gate-standard self-test
# conformance for the criterion-R registry-wide sweep instrument).
#
# Usage: bash reports/round-88/sweep_probe.sh <sweep-script>
#
# Prints three counters:
#   SWEEP_SELFTEST_MODE_PRESENT=n/1
#       "<script> --selftest" under a PATH with the producer's directory
#       removed exits 0 with the expected stable pass finding-id as the last
#       line (SWEEP_SELFTEST=pass).
#   SWEEP_MUTANTS_KILLED_ATTRIBUTED=n/2
#       the two pinned sed mutants (recipes pinned in
#       reports/round-88/claims.md, embedded here verbatim) each exit 1 with
#       its attributed marker as the last line:
#         selftest: word-count comparator accepted a wrong count
#         selftest: closure accepted an unverified supersession
#   SWEEP_USAGE_EXIT64=n/1
#       an unrecognized invocation form exits 64 (declared usage exit).
#
# The same command measures the committed instrument bytes (frozen at the
# round-88 freeze commit). Exit 0 iff all three counters are full.
set -u
if [ "$#" -ne 1 ]; then
  echo "usage: sweep_probe.sh <sweep-script>" >&2
  exit 64
fi
N="$1"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

REA_BIN="$(command -v rea || true)"
REA_DIR="$(dirname "$REA_BIN")"
STRIPPED="$(printf '%s' "$PATH" | tr ':' '\n' | grep -vFx "$REA_DIR" | paste -sd:)"

selftest_ok() { # <script> <pass-marker> -> 0 iff hermetic green + marker
  local out rc
  out="$(PATH="$STRIPPED" PYTHONUTF8=1 python -B "$1" --selftest 2>/dev/null)"
  rc=$?
  [ "$rc" -eq 0 ] && [ "$(printf '%s\n' "$out" | tail -n 1)" = "$2" ]
}

mutant_killed() { # <script> <sed-expr> <attributed-marker> -> 0 iff kill
  local out rc
  sed "$2" "$1" > "$TMP/mutant.py" || return 1
  cmp -s "$TMP/mutant.py" "$1" && return 1   # sed must have changed bytes
  out="$(PATH="$STRIPPED" PYTHONUTF8=1 python -B "$TMP/mutant.py" --selftest 2>/dev/null)"
  rc=$?
  [ "$rc" -eq 1 ] && [ "$(printf '%s\n' "$out" | tail -n 1)" = "$3" ]
}

usage64() { # <script> -> 0 iff unrecognized form exits 64
  PYTHONUTF8=1 python -B "$1" --not-a-mode >/dev/null 2>&1
  [ "$?" -eq 64 ]
}

SM=0; selftest_ok "$N" "SWEEP_SELFTEST=pass" && SM=1
echo "SWEEP_SELFTEST_MODE_PRESENT=$SM/1"

M1=0; mutant_killed "$N" \
  's|def counts_match(recorded, derived): return recorded == derived|def counts_match(recorded, derived): return True|' \
  "selftest: word-count comparator accepted a wrong count" && M1=1
M2=0; mutant_killed "$N" \
  's|def closure_ok(closure_recorded, quote_ws, quote_in_row, supersedes_ok): return quote_in_row and supersedes_ok and counts_match(closure_recorded, quote_ws)|def closure_ok(closure_recorded, quote_ws, quote_in_row, supersedes_ok): return True|' \
  "selftest: closure accepted an unverified supersession" && M2=1
echo "SWEEP_MUTANTS_KILLED_ATTRIBUTED=$((M1 + M2))/2"

UG=0; usage64 "$N" && UG=1
echo "SWEEP_USAGE_EXIT64=$UG/1"

[ "$SM" = 1 ] && [ "$((M1 + M2))" = 2 ] && [ "$UG" = 1 ]
