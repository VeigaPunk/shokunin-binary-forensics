#!/usr/bin/env bash
# probe_negctl2.sh - round-87 criterion-N instrument, revision 2.
#
# Supersedes reports/round-75/probe_negctl.sh (v1; frozen bytes, sha256
# eb5d1b54fa20421c09cd55e15d6a849af1379a822887b5a6ef60e0935c013fad).
# Closes the v1 routed debt recorded at r75 planned (b) and carried through
# r86: "criterion N's mutation-killed attribution pair on the negctl harness
# itself" - the v1 harness had no self-test mode, no declared usage exit,
# and no mutation-checked verdict logic. Plain mode (no arguments) is
# v1-identical: same fixtures, same legs, same value lines, same verdict
# contract (plain-equal.log).
#
# Modes:
#   (no args)    plain criterion-N run (v1-identical value lines; 0 pass /
#                1 fail)
#   --selftest   hermetic self-test per the Section-Gate standard: synthetic
#                verdict vectors only - no fixture build, no probe run, no
#                producer call, no network, no live-tree write. Asserts the
#                exit code and the stable expected finding-ids committed in
#                reports/round-87/claims.md and the SKILL.md registry row:
#                  NEGCTL_SELFTEST_FALSEPASS_LOGIC=ok
#                  NEGCTL_SELFTEST_ATTRIBUTION_GUARD=ok
#                  NEGCTL_SELFTEST_STALE_LOGIC=ok
#                  NEGCTL_SELFTEST_UNRECORDED_LOGIC=ok
#                  NEGCTL_V2_SELFTEST=pass          (last line, exit 0)
#                a verdict function blinded to accept any exit dies with the
#                attributed last line "selftest: stale-record verdict
#                accepted a false-pass"; the attribution pattern relaxed to
#                match anything dies with "selftest: attribution guard
#                accepted an unattributed kill" (frozen sed mutants pinned
#                in reports/round-87/claims.md).
#   other        usage line on stderr, exit 64 (declared in the registry row)
set -u

stale_flag_ok() { [ "$1" = "1" ] && printf '%s\n' "$2" | grep -Eq '^engine-ghidra .*STALE-RECORD'; }
unrecorded_flag_ok() { [ "$1" = "1" ] && printf '%s\n' "$2" | grep -Eq '^engine-ghidra .*UNRECORDED-ABSENT'; }
false_pass_ok() { [ "$1" = "0" ]; }

if [ "${1:-}" = "--selftest" ]; then
  # ST1: the leg-1b verdict rejects v1's demonstrable false-pass (exit 0 on
  # a record that contradicts the host).
  if stale_flag_ok "0" "engine-ghidra PRESENT-RECORDED-AGREES (no flag)"; then
    echo "NEGCTL_V2_SELFTEST=fail (ST1: false-pass accepted)"
    echo "selftest: stale-record verdict accepted a false-pass"
    exit 1
  fi
  echo "NEGCTL_SELFTEST_FALSEPASS_LOGIC=ok"
  # ST2: the attribution requirement is load-bearing - a kill without the
  # exact STALE-RECORD marker (mangled marker, still exit 1) must be
  # rejected.
  if stale_flag_ok "1" "engine-ghidra ... STALE_RECORD (marker drift)"; then
    echo "NEGCTL_V2_SELFTEST=fail (ST2: unattributed kill accepted)"
    echo "selftest: attribution guard accepted an unattributed kill"
    exit 1
  fi
  echo "NEGCTL_SELFTEST_ATTRIBUTION_GUARD=ok"
  # ST3: the true flagged pair is accepted.
  if ! stale_flag_ok "1" "engine-ghidra ... STALE-RECORD (attributed kill)"; then
    echo "NEGCTL_V2_SELFTEST=fail (ST3: true flag rejected)"
    echo "selftest: stale-record verdict rejected a true flag"
    exit 1
  fi
  echo "NEGCTL_SELFTEST_STALE_LOGIC=ok"
  # ST4: the unrecorded-absent verdict and the leg-1a false-pass verdict
  # accept exactly their recorded pairs.
  if ! unrecorded_flag_ok "1" "engine-ghidra ... UNRECORDED-ABSENT (attributed kill)"; then
    echo "NEGCTL_V2_SELFTEST=fail (ST4: true unrecorded flag rejected)"
    echo "selftest: unrecorded-absent verdict rejected a true flag"
    exit 1
  fi
  if unrecorded_flag_ok "0" "engine-ghidra ... ABSENT, record absent, no flag"; then
    echo "NEGCTL_V2_SELFTEST=fail (ST4: clean exit accepted as unrecorded flag)"
    echo "selftest: unrecorded-absent verdict accepted a clean exit"
    exit 1
  fi
  if ! false_pass_ok "0"; then
    echo "NEGCTL_V2_SELFTEST=fail (ST4: leg-1a verdict rejected exit 0)"
    echo "selftest: false-pass leg verdict rejected exit zero"
    exit 1
  fi
  if false_pass_ok "1"; then
    echo "NEGCTL_V2_SELFTEST=fail (ST4: leg-1a verdict accepted exit 1)"
    echo "selftest: false-pass leg verdict accepted exit one"
    exit 1
  fi
  echo "NEGCTL_SELFTEST_UNRECORDED_LOGIC=ok"
  echo "NEGCTL_V2_SELFTEST=pass"
  exit 0
fi
if [ "$#" -ne 0 ]; then
  echo "usage: probe_negctl2.sh [--selftest]" >&2
  exit 64
fi
# ---- plain mode: v1 logic from here (byte-identical value lines) ----
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
if false_pass_ok "$e1"; then
  echo "NEGCTL_V1_STALE_RECORD_FLAGGED=0/1 (exit 0 on a record that contradicts the host — the defect)"
else
  echo "NEGCTL_V1_STALE_RECORD_FLAGGED=unexpected-exit-$e1"; rc=1
fi

# --- Leg 1b: v2 attributed kill on the same fixture ---
o2=$("$V2" "$work/A" 2>&1); e2=$?
if stale_flag_ok "$e2" "$o2"; then
  echo "NEGCTL_V2_STALE_RECORD_FLAGGED=1/1 (exit 1, engine-ghidra STALE-RECORD)"
else
  echo "NEGCTL_V2_STALE_RECORD_FLAGGED=0/1 (exit=$e2)"; rc=1
fi

# --- Leg 2: v2 flags a record-less absent surface under a fake empty HOME ---
oh=$HOME
HOME="$work/home"; mkdir -p "$HOME"
o3=$("$V2" "$work/B" 2>&1); e3=$?
HOME="$oh"
if unrecorded_flag_ok "$e3" "$o3"; then
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
