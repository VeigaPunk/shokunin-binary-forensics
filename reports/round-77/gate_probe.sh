#!/usr/bin/env bash
# gate_probe.sh — calibration criterion G: provider-gate payload receipt fidelity.
#
# Carries the r76 verifier-spotcheck routed item 2: the producer's own
# provider-gate payloads (snake_case details.operation) are committed receipts,
# machine-checked here against live producer legs, per leg, with a
# mutated-copy negative control (the criterion-R per-leg receipt discipline).
#
# Legs (each independently named and failing):
#   LEG0  committed receipts exist (corpus/live/runs/round-77/provider-gates/)
#   LEG1  live rea inspect-android-package gate == committed android-gate.json
#         (fields: code, category, details.provider_id, details.operation)
#   LEG2  live rea inspect-firmware-regions gate == committed firmware-gate.json
#   LEG3  negative control: a mutated copy of android-gate.json
#         (details.operation -> inspect_firmware_regions) MUST be flagged
#
# Run from the lane root:  bash reports/round-77/gate_probe.sh
# Green: all legs pass, GATE_VERDICT=green, exit 0.
# Red:   any leg fails, GATE_VERDICT=red, exit 1.
# The live legs need the rea CLI (provider gates; both exit 1 by design).
set -u
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
