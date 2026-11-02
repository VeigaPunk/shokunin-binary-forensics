#!/usr/bin/env bash
# selftest_probe.sh - round-87 C1 counting instrument (Section-Gate-standard
# self-test conformance for the criterion-N instrument).
#
# Usage: bash reports/round-87/selftest_probe.sh <negctl-script>
#
# Prints three counters:
#   NEG_SELFTEST_MODE_PRESENT=n/1
#       "<script> --selftest" under a PATH with the producer's directory
#       removed exits 0 with the expected stable pass finding-id as the last
#       line (NEGCTL_V2_SELFTEST=pass).
#   NEG_SELFTEST_MUTANTS_KILLED_ATTRIBUTED=n/2
#       the two pinned sed mutants (recipes pinned in
#       reports/round-87/claims.md, embedded here verbatim) each exit 1 with
#       its attributed marker as the last line:
#         selftest: stale-record verdict accepted a false-pass
#         selftest: attribution guard accepted an unattributed kill
#   NEG_USAGE_EXIT64=n/1
#       an unrecognized invocation form exits 64 (declared usage exit).
#
# The same command measures the v1 harness (red-before: no selftest mode, no
# usage exit, no mutation-checked verdict logic) and the v2 instrument
# (green). Exit 0 iff all three counters are full.
set -u
if [ "$#" -ne 1 ]; then
  echo "usage: selftest_probe.sh <negctl-script>" >&2
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

SM=0; selftest_ok "$N" "NEGCTL_V2_SELFTEST=pass" && SM=1
echo "NEG_SELFTEST_MODE_PRESENT=$SM/1"

M1=0; mutant_killed "$N" \
  's|^stale_flag_ok() {.*|stale_flag_ok() { return 0; }|' \
  "selftest: stale-record verdict accepted a false-pass" && M1=1
M2=0; mutant_killed "$N" \
  "s|'\\^engine-ghidra \\.\\*STALE-RECORD'|'.*'|" \
  "selftest: attribution guard accepted an unattributed kill" && M2=1
echo "NEG_SELFTEST_MUTANTS_KILLED_ATTRIBUTED=$((M1 + M2))/2"

UG=0; usage64 "$N" && UG=1
echo "NEG_USAGE_EXIT64=$UG/1"

[ "$SM" = 1 ] && [ "$((M1 + M2))" = 2 ] && [ "$UG" = 1 ]
