#!/usr/bin/env bash
# revenger r75 — calibration criterion N: record-vs-reality mismatch detection.
#
# The r74 v1 province probe false-passes a stale record: when a surface IS
# present on the host while PROVINCE.md still carries its dated absent-record,
# v1's PATH-only engine probe fails, matches the absent-record, and resolves
# ABSENT-RECORDED with exit 0. The v2 probe must FLAG that state (STALE-RECORD,
# exit 1) and must also flag a truly-absent surface with no record at all
# (UNRECORDED-ABSENT, exit 1), while staying green on the honest fixed state.
#
# Legs (each prints a NEGCTL_* line; any unexpected result exits 1):
#   1. fixture with a stale ghidra record (present on host, recorded absent):
#        v1 -> exit 0 (the demonstrable false-pass, before state)
#        v2 -> exit 1 with "engine-ghidra ... STALE-RECORD" (attributed kill)
#   2. fixture with NO ghidra record, fake empty HOME (surface truly absent
#      from the fixture host): v2 -> exit 1 with
#      "engine-ghidra ... UNRECORDED-ABSENT"
#   3. positive control: v2 on the real fixed lane -> exit 0
#   4. disclosure (not a criterion leg): v1 on the real fixed lane exits 1
#      (it has no PRESENT-record grammar); the r75 P2 revision supersedes it.
# Usage: bash reports/round-75/probe_negctl.sh
set -u
L=$(cd "$(dirname "$0")/../.." && pwd)
V1="$L/reports/round-74/province_probe.sh"
V2="$L/reports/round-75/province_probe2.sh"
[ -f "$V1" ] && [ -f "$V2" ] && [ -f "$L/PROVINCE.md" ] || { echo "NEGCTL inputs missing"; exit 2; }
rc=0

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

# Fixture scaffolding shared by both probes (bounty module + .git resolve
# against the fixture dir as LANE_DIR).
for d in "$work/A" "$work/B"; do
  mkdir -p "$d/.git" "$d/corpus/training/bounty-triage"
  touch "$d/corpus/training/bounty-triage/MODULE.md"
done

python - "$L/PROVINCE.md" "$work/A/PROVINCE.md" "$work/B/PROVINCE.md" <<'PYEOF'
import io, sys
src = io.open(sys.argv[1], encoding="utf-8").read()
present_block = (
    "  [present on this host, 2026-11-01: ghidra 12.1.4 at\n"
    "  C:/Users/jpvei/tools/ghidra_12.1.4_PUBLIC — support/analyzeHeadless.bat + JDK 21 present;\n"
    "  `rea doctor` reports ghidra, ghidra-headless and ghidra-native_decompiler healthy.\n"
    "  Presence, not readiness (Q05). Off-PATH install of 2026-10-26 that the r74 PATH-only\n"
    "  probe could not see]"
)
absent_line = "  [absent on this host, 2026-10-31: ghidra / analyzeHeadless — PATH probe]"
assert present_block in src, "present-record block not found verbatim"
io.open(sys.argv[2], "w", encoding="utf-8", newline="\n").write(src.replace(present_block, absent_line))
io.open(sys.argv[3], "w", encoding="utf-8", newline="\n").write(src.replace(present_block, ""))
PYEOF
[ $? -eq 0 ] || { echo "NEGCTL fixture build failed"; exit 2; }

# --- Leg 1a: v1 false-pass on the stale-record fixture ---
o1=$("$V1" "$work/A" 2>&1); e1=$?
if [ "$e1" -eq 0 ]; then
  echo "NEGCTL_V1_STALE_RECORD_FLAGGED=0/1 (exit 0 on a record that contradicts the host — the defect)"
else
  echo "NEGCTL_V1_STALE_RECORD_FLAGGED=unexpected-exit-$e1"; rc=1
fi

# --- Leg 1b: v2 attributed kill on the same fixture ---
o2=$("$V2" "$work/A" 2>&1); e2=$?
if [ "$e2" -eq 1 ] && printf '%s\n' "$o2" | grep -Eq '^engine-ghidra .*STALE-RECORD'; then
  echo "NEGCTL_V2_STALE_RECORD_FLAGGED=1/1 (exit 1, engine-ghidra STALE-RECORD)"
else
  echo "NEGCTL_V2_STALE_RECORD_FLAGGED=0/1 (exit=$e2)"; rc=1
fi

# --- Leg 2: v2 flags a record-less absent surface under a fake empty HOME ---
oh=$HOME
HOME="$work/home"; mkdir -p "$HOME"
o3=$("$V2" "$work/B" 2>&1); e3=$?
HOME="$oh"
if [ "$e3" -eq 1 ] && printf '%s\n' "$o3" | grep -Eq '^engine-ghidra .*UNRECORDED-ABSENT'; then
  echo "NEGCTL_V2_UNRECORDED_ABSENT_FLAGGED=1/1 (exit 1, engine-ghidra UNRECORDED-ABSENT)"
else
  echo "NEGCTL_V2_UNRECORDED_ABSENT_FLAGGED=0/1 (exit=$e3)"; rc=1
fi

# --- Leg 3: positive control on the real fixed lane ---
o4=$("$V2" 2>&1); e4=$?
if [ "$e4" -eq 0 ]; then
  echo "NEGCTL_V2_POSITIVE_CONTROL=pass"
else
  echo "NEGCTL_V2_POSITIVE_CONTROL=fail (exit=$e4)"; rc=1
fi

# --- Leg 4: disclosure only (supersession, not a criterion leg) ---
o5=$("$V1" 2>&1); e5=$?
echo "NEGCTL_V1_ON_FIXED_OBSERVED=exit-$e5 (v1 has no PRESENT-record grammar; superseded by P2, disclosed not scored)"

echo "NEGCTL_SELFTEST=$([ $rc -eq 0 ] && echo pass || echo fail)"
exit $rc
