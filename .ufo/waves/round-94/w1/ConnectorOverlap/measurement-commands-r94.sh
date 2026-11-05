#!/bin/sh
# Commands run by seat ConnectorOverlap (round 94, 2026-11-05) to produce measurement-r94.tsv.
# Read-only on the lane: git show / diff / ls-tree / cat-file extract committed bytes into scratch; nothing in the lane or fleet is written.
set -eu

LANE=/home/vgpnk/Projects/shokunin/revenger-shokunin
FLEET=/home/vgpnk/Projects/shokunin
S=/fast/scratch/hyaku/revenger-r94/ConnectorOverlap
mkdir -p "$S/bytes"

R89_BASE=02050cb2a6758e3bd9cec696ff0e42df6f23511a   # round-93 freeze (baseline of the r93 measurement)
R93_TIP=28b5f99b90c1da91ac85d2e6d6aa6ec49efa42e6    # round-93 adjudication tip (SCORECARD r93 section, lesson round-93.md)
R93_SPOT=$(git -C "$LANE" rev-parse 9876cb3)        # round-93 verifier spot-check commit
R94_FREEZE=060a8e87d6de6b31f91b58524ab0fcad88ae5431 # round-94 freeze (claims.md)

# 1. Evidence drift since the r93 baseline: deletions in the r89-r92 evidence paths must be 0 (additive-only).
echo "## 1 drift 02050cb..060a8e8 (deleted lines in r89-r93 evidence paths)"
git -C "$LANE" diff --numstat "$R89_BASE" "$R94_FREEZE" -- SCORECARD.md corpus/lessons reports/round-89 reports/round-90 reports/round-91 reports/round-92 \
  | awk '{ ins += $1; del += $2; n++ } END { printf "files=%d insertions=%d deletions=%d\n", n, ins, del }'

# 2. r93 verdict cells (SCORECARD r93 section, at the adjudication tip).
echo "## 2 r93 SCORECARD verdict cells at $R93_TIP"
git -C "$LANE" show "$R93_TIP:SCORECARD.md" | grep -n -E '^\| (coverage|calibration) .*(MET on the frozen|MET on its frozen)' | cut -c1-140 || true
git -C "$LANE" show "$R93_TIP:SCORECARD.md" | grep -n -E '^## Round 93' | cut -c1-120

# 3. r93 lesson: the C2 battery result line and mistake M3 row.
echo "## 3 r93 lesson anchors at $R93_TIP"
git -C "$LANE" show "$R93_TIP:corpus/lessons/round-93.md" | grep -n -E 'BATTERY_VERDICT=pass|^\| \*\*M3' | cut -c1-120

# 4. r93 verifier spot-check verdict lines (at $R93_SPOT).
echo "## 4 r93 spot-check verdict lines at $R93_SPOT"
git -C "$LANE" show "$R93_SPOT:corpus/lessons/round-93-verifier-spotcheck.md" | grep -n -E '^\*\*C[12] verdict' | cut -c1-120

# 5. r94 state at the freeze tip: claims present, no lesson, no SCORECARD round section, no landing commit above the freeze.
echo "## 5 r94 state at $R94_FREEZE"
git -C "$LANE" cat-file -e "$R94_FREEZE:reports/round-94/claims.md" && echo "claims.md present"
git -C "$LANE" cat-file -e "$R94_FREEZE:corpus/lessons/round-94.md" 2>/dev/null && echo "lesson round-94 present" || echo "lesson round-94 absent"
echo "SCORECARD '## Round 94' headings: $(git -C "$LANE" show "$R94_FREEZE:SCORECARD.md" | grep -c '^## Round 94' || true)"
echo "commits after freeze on main: $(git -C "$LANE" rev-list --count "$R94_FREEZE"..main)"

# 6. Fleet MANIFEST: revenger closure rows for rounds 94 (none expected) and 93 (admitted).
echo "## 6 MANIFEST revenger closures"
python3 -c "
import json
m = json.load(open('$FLEET/MANIFEST.json'))
rows = [e for e in m['rounds'] if e.get('lane') == 'revenger' and e.get('type') == 'closure']
print('revenger closures:', [(e.get('round'), e.get('admitted'), e.get('verdict')) for e in rows][-4:])
print('round-94 revenger closures:', sum(1 for e in rows if str(e.get('round')) == '94'))
"

# 7. Adoption state (read-only): staged package, collision log, L0 line.
echo "## 7 adoption state"
grep -n -E 'proposed rows accepted|proposed rows refused|proposed knowledge entries' /home/vgpnk/Projects/shokuknow/merge/revenger/MERGE-REPORT.md | cut -c1-120
grep -n -E 'collision count' "$LANE/.ufo/waves/round-94/w1/ExecCensus/collision-run.log" || true
grep -n 'revenger | round-91' "$FLEET/.ufo/l0-questions.md" | cut -c1-80 || true

rm -rf "$S"
echo "scratch removed: $S"
