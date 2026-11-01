#!/usr/bin/env bash
# revenger r78 — p3_negctl.sh: the criterion-N-class negative-control harness for
# the P2→P3 province-probe revision (claim C1's measurement).
#
# Legs (each independently named and failing; attribution rule: a leg counts
# only when the specific printed line names the cdp-browser surface):
#   LEG1  P2 on a fixture whose PROVINCE.md carries a planted stale browser
#         record (the r77 present-record block replaced by the dedicated
#         absent-sentinel token) MUST false-pass (exit 0, blind) — the v2
#         defect demonstrated, P2_NEGCTL_STALE_BROWSER_FLAGGED=0/1
#   LEG2  P3 on the same fixture MUST flag it: exit 1, the printed line names
#         cdp-browser + STALE-RECORD — P3_NEGCTL_STALE_BROWSER_FLAGGED=1/1
#   LEG3  P3 on a fixture with the browser record removed entirely MUST stay
#         green (a PRESENT surface with no record is not a defect — the
#         UNRECORDED-ABSENT branch fires only for ABSENT surfaces, and the
#         browser binaries sit at fixed host paths, so that absent state is
#         not manufacturable inside a fixture; disclosed, not claimed) —
#         P3_NEGCTL_UNRECORDED_PRESENT_GREEN_BY_DESIGN=ok
#   LEG4  positive control: P3 on the lane tree itself is green (exit 0,
#         12/12, P3_SCORE=10.0) — P3_POSITIVE_CONTROL=pass
#
# The fixtures are built in a mktemp dir from the PROVINCE.md bytes of the
# tree the run targets (LANE_DIR argument, default the lane root this script
# lives in). The block locator keys on the exact recorded opening token
# "[present on this host, 2026-11-01: CDP browser surface"; if a later round
# rewords that record the runner fails LOUDLY (exit 2, could-not-evaluate)
# rather than silently passing — reword = update the locator with the round.
# Usage: bash reports/round-78/p3_negctl.sh [LANE_DIR]
set -u
L=$(cd "$(dirname "$0")/../.." && pwd)
[ "${1:-}" = "" ] || L=$1
P="$L/PROVINCE.md"
[ -f "$P" ] || { echo "PROVINCE not found: $P"; exit 2; }
DIR="$(cd "$(dirname "$0")" && pwd)"
P2="$DIR/../round-75/province_probe2.sh"
P3="$DIR/province_probe3.sh"
[ -f "$P2" ] || { echo "could-not-evaluate: P2 instrument not found: $P2"; exit 2; }
[ -f "$P3" ] || { echo "could-not-evaluate: P3 instrument not found: $P3"; exit 2; }
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Fixture scaffolding shared by both probes (r75 pattern): bounty-triage-module
# and lane-repo resolve against the fixture dir as LANE_DIR, so a PROVINCE-only
# fixture produces spurious UNRECORDED-ABSENT lines for them and the red leg
# would exit 1 for the wrong reason. Scaffold both, then mutate only the
# browser record — the isolated variable under test.
for d in "$TMP/stale" "$TMP/unrecorded"; do
  mkdir -p "$d/.git" "$d/corpus/training/bounty-triage"
  touch "$d/corpus/training/bounty-triage/MODULE.md"
done

OPEN="[present on this host, 2026-11-01: CDP browser surface"
SENTINEL="[absent on this host: cdp-browser]"
if ! PYTHONUTF8=1 python -B - "$P" "$TMP/stale/PROVINCE.md" "$TMP/unrecorded/PROVINCE.md" "$OPEN" "$SENTINEL" <<'PY'
import os, sys
path, stale_out, unrec_out, open_tok, sentinel = sys.argv[1:6]
text = open(path, encoding="utf-8").read()
start = text.find(open_tok)
if start < 0:
    sys.exit("could-not-evaluate: browser present-record block not found in PROVINCE.md")
end = text.find("]", start)
if end < 0:
    sys.exit("could-not-evaluate: browser present-record block has no closing bracket")
block = text[start:end + 1]
os.makedirs(os.path.dirname(stale_out), exist_ok=True)
os.makedirs(os.path.dirname(unrec_out), exist_ok=True)
open(stale_out, "w", encoding="utf-8", newline="").write(text.replace(block, sentinel))
open(unrec_out, "w", encoding="utf-8", newline="").write(text.replace(block, ""))
PY
then
  echo "P3_NEGCTL_FIXTURE_BUILD=failed"
  exit 2
fi
echo "P3_NEGCTL_FIXTURE_BUILD=ok (stale + unrecorded fixtures built from the tree's own PROVINCE.md bytes)"

P2_LINE="$(bash "$P2" "$TMP/stale" 2>&1)"; P2_RC=$?
echo "$P2_LINE" | sed 's/^/  [p2-on-stale] /'
if [ "$P2_RC" -ne 0 ]; then
  echo "P2_NEGCTL_STALE_BROWSER_FLAGGED=1/1 (unexpected: v2 is not supposed to see this surface)"
  L1=0
else
  echo "P2_NEGCTL_STALE_BROWSER_FLAGGED=0/1 (v2 false-pass on a stale browser record — the routed blind spot, by construction)"
  L1=1
fi

P3_LINE="$(bash "$P3" "$TMP/stale" 2>&1)"; P3_RC=$?
echo "$P3_LINE" | sed 's/^/  [p3-on-stale] /'
if [ "$P3_RC" -ne 0 ] && printf '%s\n' "$P3_LINE" | grep -q 'cdp-browser' && printf '%s\n' "$P3_LINE" | grep -q 'STALE-RECORD'; then
  echo "P3_NEGCTL_STALE_BROWSER_FLAGGED=1/1 (exit 1, attributed: the failing line names cdp-browser STALE-RECORD)"
  L2=1
else
  echo "P3_NEGCTL_STALE_BROWSER_FLAGGED=0/1 (exit $P3_RC without the attributed cdp-browser STALE-RECORD line)"
  L2=0
fi

P3U_LINE="$(bash "$P3" "$TMP/unrecorded" 2>&1)"; P3U_RC=$?
echo "$P3U_LINE" | sed 's/^/  [p3-on-unrecorded] /'
# A PRESENT surface with no record is green by design: the UNRECORDED-ABSENT
# branch fires only for an ABSENT surface with no record, and cdp-browser's
# binaries sit at fixed host paths, so that state cannot be manufactured
# inside a fixture tree (unlike r75's ghidra leg, which faked an empty HOME).
# This leg therefore asserts the by-design green and discloses the limit.
if [ "$P3U_RC" -eq 0 ] && printf '%s\n' "$P3U_LINE" | grep -q 'P3_SURFACES_RESOLVED=12/12'; then
  echo "P3_NEGCTL_UNRECORDED_PRESENT_GREEN_BY_DESIGN=ok (a present surface with no record is not a defect)"
  echo "P3_NEGCTL_UNRECORDED_ABSENT_LEG=not-claimable (the absent state is not manufacturable for cdp-browser in a fixture; the branch is the same shared check() code the eleven carried surfaces exercise)"
  L3=1
else
  echo "P3_NEGCTL_UNRECORDED_PRESENT_GREEN_BY_DESIGN=FAIL (exit $P3U_RC on the record-removed fixture)"
  L3=0
fi

P3P_LINE="$(bash "$P3" 2>&1)"; P3P_RC=$?
echo "$P3P_LINE" | sed 's/^/  [p3-on-lane] /'
if [ "$P3P_RC" -eq 0 ] && printf '%s\n' "$P3P_LINE" | grep -q 'P3_SURFACES_RESOLVED=12/12 UNRECORDED_ABSENT=0 STALE_RECORDS=0 P3_SCORE=10.0'; then
  echo "P3_POSITIVE_CONTROL=pass (lane tree green at 12/12)"
  L4=1
else
  echo "P3_POSITIVE_CONTROL=FAIL (exit $P3P_RC or unexpected summary line)"
  L4=0
fi

if [ "$L1" -eq 1 ] && [ "$L2" -eq 1 ] && [ "$L3" -eq 1 ] && [ "$L4" -eq 1 ]; then
  echo "P3_NEGCTL_VERDICT=green"
  exit 0
fi
echo "P3_NEGCTL_VERDICT=red"
exit 1
