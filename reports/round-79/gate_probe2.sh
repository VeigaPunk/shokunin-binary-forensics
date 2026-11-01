#!/usr/bin/env bash
# gate_probe2.sh — calibration criterion G instrument, revision 2 (round 79).
#
# Supersedes reports/round-77/gate_probe.sh (v1; frozen bytes, its registry
# row stays for those bytes). Closes the v1 routed debt recorded at
# registration (r78): the §Gate-standard self-test clause and a declared
# usage exit. Plain mode (no arguments) is v1-identical: same legs, same
# value lines, same verdict contract over the live producer gates and the
# committed receipts.
#
# Modes:
#   (no args)    plain criterion-G run (v1-identical value lines; 0 green /
#                1 red; receipts absent -> LEG0=no, exit 1)
#   --selftest   hermetic self-test per the §Gate standard: isolated temp
#                fixtures, no network, no live-tree write, NO producer call
#                (runs with the rea directory stripped from PATH in the
#                committed receipts); asserts the exit code and the stable
#                expected finding-ids committed in claims.md and the SKILL.md
#                registry row:
#                  GATE_SELFTEST_COMPARATOR_EQUAL=ok
#                  GATE_SELFTEST_COMPARATOR_MUTANT_FLAGGED=ok
#                  GATE_SELFTEST_COMPARATOR_FIELD_MISSING_FLAGGED=ok
#                  GATE_SELFTEST=pass            (last line, exit 0)
#                a blinded comparator dies with the attributed last line
#                "selftest: blind comparator accepted mutated receipt"
#                (frozen sed mutant pinned in reports/round-79/claims.md)
#   other        usage line on stderr, exit 64 (declared in the registry row)
set -u
if [ "${1:-}" = "--selftest" ]; then
  TMP="$(mktemp -d)"
  trap 'rm -rf "$TMP"' EXIT
  cat > "$TMP/a.json" <<'JSON'
{"code":"provider_gate","category":"apk","details":{"provider_id":"jadx-headless","operation":"inspect_android_package"}}
JSON
  cat > "$TMP/b.json" <<'JSON'
{"code":"provider_gate","category":"apk","details":{"provider_id":"jadx-headless","operation":"inspect_android_package"}}
JSON
  cat > "$TMP/mutant.json" <<'JSON'
{"code":"provider_gate","category":"apk","details":{"provider_id":"jadx-headless","operation":"inspect_firmware_regions"}}
JSON
  cat > "$TMP/missing.json" <<'JSON'
{"code":"provider_gate","category":"apk","details":{"provider_id":"jadx-headless"}}
JSON
  compare() { # compare <committed.json> <live.json> -> 0 equal on the four fields
    PYTHONUTF8=1 python -B - "$1" "$2" <<'PY'
import json, sys
def key(p):
    d = json.load(open(p, encoding="utf-8"))
    det = d.get("details") or {}
    return (d.get("code"), d.get("category"), det.get("provider_id"), det.get("operation"))
sys.exit(0 if key(sys.argv[1]) == key(sys.argv[2]) else 1)
PY
  }
  # ST1: the equal pair must be accepted
  if ! compare "$TMP/a.json" "$TMP/b.json"; then
    echo "GATE_SELFTEST=fail (ST1: equal pair not accepted)"
    echo "selftest: comparator rejected equal payloads"
    exit 1
  fi
  echo "GATE_SELFTEST_COMPARATOR_EQUAL=ok"
  # ST2: a mutated details.operation must be flagged (kills a blind comparator)
  if compare "$TMP/a.json" "$TMP/mutant.json"; then
    echo "GATE_SELFTEST=fail (ST2: mutated details.operation accepted)"
    echo "selftest: blind comparator accepted mutated receipt"
    exit 1
  fi
  echo "GATE_SELFTEST_COMPARATOR_MUTANT_FLAGGED=ok"
  # ST3: a payload missing a keyed field must be flagged (kills a
  # field-subset comparator)
  if compare "$TMP/a.json" "$TMP/missing.json"; then
    echo "GATE_SELFTEST=fail (ST3: field-missing payload accepted)"
    echo "selftest: comparator accepted payload missing a keyed field"
    exit 1
  fi
  echo "GATE_SELFTEST_COMPARATOR_FIELD_MISSING_FLAGGED=ok"
  echo "GATE_SELFTEST=pass"
  exit 0
fi
if [ "$#" -ne 0 ]; then
  echo "usage: gate_probe2.sh [--selftest]" >&2
  exit 64
fi
# ---- plain mode: v1 bytes from here (byte-identical value lines) ----
cd "$(dirname "$0")/../.." || exit 2
GATES="corpus/live/runs/round-77/provider-gates"
APK="corpus/fixtures/apk-r65/fixture.apk"
FW="corpus/fixtures/firmware-r63/firmware-r63.bin"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

compare() { # compare <committed.json> <live.json> -> 0 equal on the four fields
  PYTHONUTF8=1 python -B - "$1" "$2" <<'PY'
import json, sys
def key(p):
    d = json.load(open(p, encoding="utf-8"))
    det = d.get("details") or {}
    return (d.get("code"), d.get("category"), det.get("provider_id"), det.get("operation"))
sys.exit(0 if key(sys.argv[1]) == key(sys.argv[2]) else 1)
PY
}

VERDICT=red
if [ ! -f "$GATES/android-gate.json" ] || [ ! -f "$GATES/firmware-gate.json" ]; then
  echo "GATE_LEG0_RECEIPTS_PRESENT=no"
  echo "GATE_LEG1_ANDROID_MATCH=unrun"
  echo "GATE_LEG2_FIRMWARE_MATCH=unrun"
  echo "GATE_LEG3_NEGCTL_FLAGGED=unrun"
  echo "GATE_VERDICT=red"
  exit 1
fi
echo "GATE_LEG0_RECEIPTS_PRESENT=yes"

PYTHONUTF8=1 rea inspect-android-package "$APK" --format json > "$TMP/live-android.json" 2>/dev/null
AND_RC=$?
PYTHONUTF8=1 rea inspect-firmware-regions "$FW" --format json > "$TMP/live-firmware.json" 2>/dev/null
FW_RC=$?
if [ "$AND_RC" -eq 1 ] && [ "$FW_RC" -eq 1 ] && compare "$GATES/android-gate.json" "$TMP/live-android.json"; then
  echo "GATE_LEG1_ANDROID_MATCH=1 (live gate exit 1, four fields equal)"
  L1=1
else
  echo "GATE_LEG1_ANDROID_MATCH=0 (android_rc=$AND_RC firmware_rc=$FW_RC or field mismatch)"
  L1=0
fi

if [ "$FW_RC" -eq 1 ] && compare "$GATES/firmware-gate.json" "$TMP/live-firmware.json"; then
  echo "GATE_LEG2_FIRMWARE_MATCH=1 (live gate exit 1, four fields equal)"
  L2=1
else
  echo "GATE_LEG2_FIRMWARE_MATCH=0"
  L2=0
fi

# negative control: mutated operation must be flagged by the same comparator
PYTHONUTF8=1 python -B - "$GATES/android-gate.json" "$TMP/mutant.json" <<'PY'
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
d["details"]["operation"] = "inspect_firmware_regions"
json.dump(d, open(sys.argv[2], "w", encoding="utf-8"))
PY
if compare "$GATES/android-gate.json" "$TMP/mutant.json"; then
  echo "GATE_LEG3_NEGCTL_FLAGGED=0 (mutated receipt accepted — comparator blind)"
  L3=0
else
  echo "GATE_LEG3_NEGCTL_FLAGGED=1 (mutated details.operation flagged)"
  L3=1
fi

if [ "$L1" -eq 1 ] && [ "$L2" -eq 1 ] && [ "$L3" -eq 1 ]; then
  VERDICT=green
fi
echo "GATE_VERDICT=$VERDICT"
[ "$VERDICT" = green ] || exit 1
