#!/usr/bin/env bash
# ReviewerR91C2 — run message_tree_check.py over the falsification fixture + 5 real commits.
# Usage: run_cases.sh [INSTR_PATH]   (default: lane reports/round-91/message_tree_check.py)
set -uo pipefail
SEAT=ReviewerR91C2
SCRATCH_ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}"
S="$SCRATCH_ROOT/revenger-r91/$SEAT"
LANE=/home/vgpnk/Projects/shokunin/revenger-shokunin
INSTR="${1:-$LANE/reports/round-91/message_tree_check.py}"
source "$S/cases.env"

if [ ! -f "$INSTR" ]; then echo "INSTRUMENT=absent $INSTR"; exit 3; fi
echo "INSTRUMENT=$INSTR"

run_case() { # $1=tag $2=lane $3=range
  local out rc
  out=$(python3 -B "$INSTR" --lane "$2" --range "$3" 2>&1); rc=$?
  printf '%s' "$out" > "$S/out-$1.txt"
  LAST_OUT="$out"; LAST_RC=$rc
}

# case tag | range | expected cited | expected misses | expected exit
TABLE=$(cat <<EOF
A	$C1..$C2_A	0	0	0
B	$C2_A..$C3_B	1	0	0
C	$C3_B..$C4_C	1	0	0
D	$C4_C..$C5_D	1	1	1
E	$C5_D..$C6_E	2	0	0
F1	$C6_E..$C7_F1	1	0	0
F2	$C7_F1..$C8_F2	2	1	1
G	$C8_F2..$C9_G	0	0	0
Hside	$C9_G..$C_SIDE	1	0	0
Hmerge	$C_SIDE..$C_MERGE	1	0	0
EOF
)

RESULT="$S/verdicts.tsv"
: > "$RESULT"
DIS=0
while IFS=$'\t' read -r cid rng ec em ee; do
  run_case "$cid" "$D" "$rng"
  oc=$(grep -oE 'cited=[0-9]+' <<<"$LAST_OUT" | tail -1 | cut -d= -f2)
  om=$(grep -oE 'misses=[0-9]+' <<<"$LAST_OUT" | tail -1 | cut -d= -f2)
  ocl=$(grep -c '^COMMIT ' <<<"$LAST_OUT" || true)
  if [ "$oc" = "$ec" ] && [ "$om" = "$em" ] && [ "$LAST_RC" = "$ee" ] && [ "$ocl" = 1 ]; then v=AGREE; else v=DISAGREE; DIS=$((DIS+1)); fi
  printf '%s\t%s\texp(cited=%s,miss=%s,exit=%s)\tobs(cited=%s,miss=%s,exit=%s,commitlines=%s)\t%s\n' \
    "$cid" "$rng" "$ec" "$em" "$ee" "${oc:-none}" "${om:-none}" "$LAST_RC" "$ocl" "$v" >> "$RESULT"
done <<< "$TABLE"

# aggregate leg
run_case AGG "$D" "$C0..$C_MERGE"
ogc=$(grep -oE 'commits=[0-9]+' <<<"$LAST_OUT" | tail -1 | cut -d= -f2)
ogm=$(grep -oE 'misses=[0-9]+' <<<"$LAST_OUT" | tail -1 | cut -d= -f2)
ocl=$(grep -c '^COMMIT ' <<<"$LAST_OUT" || true)
if [ "$ogc" = 11 ] && [ "$ogm" = 2 ] && [ "$LAST_RC" = 1 ] && [ "$ocl" = 11 ]; then AGGV=AGREE; else AGGV=DISAGREE; fi
printf 'AGG\t%s..%s\texp(commits=11,miss=2,exit=1,11 COMMIT lines)\tobs(commits=%s,miss=%s,exit=%s,commitlines=%s)\t%s\n' \
  "$C0" "$C_MERGE" "${ogc:-none}" "${ogm:-none}" "$LAST_RC" "$ocl" "$AGGV" >> "$RESULT"

# five real lane commits: hash | hand-count cited | hand-count misses
REAL=$'d509e982844d31bd26f3cb96e1a663e7d36f2ca8\t0\t0\nb13aac756ac33aa5245c13966c624de4370206d0\t0\t0\n45b27135d\t4\t0\n6ce41aabc\t3\t0\n5f7ecce6a\t1\t0'
RDIS=0
while IFS=$'\t' read -r hc ec em; do
  run_case "real-$hc" "$LANE" "$hc^..$hc"
  oc=$(grep -oE 'cited=[0-9]+' <<<"$LAST_OUT" | tail -1 | cut -d= -f2)
  om=$(grep -oE 'misses=[0-9]+' <<<"$LAST_OUT" | tail -1 | cut -d= -f2)
  ocl=$(grep -c '^COMMIT ' <<<"$LAST_OUT" || true)
  if [ "$oc" = "$ec" ] && [ "$om" = "$em" ] && [ "$LAST_RC" = 0 ] && [ "$ocl" = 1 ]; then v=AGREE; else v=DISAGREE; RDIS=$((RDIS+1)); fi
  printf 'REAL\t%s^..%s\texp(cited=%s,miss=%s,exit=0)\tobs(cited=%s,miss=%s,exit=%s,commitlines=%s)\t%s\n' \
    "$hc" "$hc" "$ec" "$em" "${oc:-none}" "${om:-none}" "$LAST_RC" "$ocl" "$v" >> "$RESULT"
done <<< "$REAL"

echo "=== verdicts (fixture+AGG) ==="; cat "$RESULT"
echo "FIXTURE_DISAGREEMENTS=$DIS/10  AGG=$AGGV  REAL_DISAGREEMENTS=$RDIS/5"
