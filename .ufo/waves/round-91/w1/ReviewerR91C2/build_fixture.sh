#!/usr/bin/env bash
# ReviewerR91C2 — round-91 C2 falsification fixture builder.
# Protocol-compliant: mktemp under $HYAKU_SCRATCH/revenger-r91/ReviewerR91C2,
# `git -C "$D"` on every call, toplevel asserted before the first commit.
# Emits cases.env (hashes) + expected.tsv (pre-registered expectations).
set -euo pipefail

SEAT=ReviewerR91C2
SCRATCH_ROOT="${HYAKU_SCRATCH:-/fast/scratch/hyaku}"
S="$SCRATCH_ROOT/revenger-r91/$SEAT"
mkdir -p "$S"
D=$(mktemp -d "$S/fixture.XXXXXX")
git -C "$D" init -q
top=$(git -C "$D" rev-parse --show-toplevel)
if [ "$top" != "$D" ]; then echo "FATAL toplevel $top != $D" >&2; exit 2; fi
git -C "$D" config user.name "r91-reviewer-fixture"
git -C "$D" config user.email "r91-reviewer@fixture.invalid"

commit() { git -C "$D" add -A >/dev/null 2>&1 || true; git -C "$D" commit -q --allow-empty -m "$1"; git -C "$D" rev-parse HEAD; }

# ---- history -----------------------------------------------------------------
C0=$(commit "root")
mkdir -p "$D/corpus"
printf 'def check():\n    return True\n' > "$D/corpus/self_check.py"
printf 'other\n' > "$D/corpus/other.py"
printf 'readme\n' > "$D/README.md"
C1=$(commit "seed: add \`corpus/self_check.py\` and \`corpus/other.py\` plus \`README.md\`")

# (a) prose path, NO backticks, target missing -> out of scope per frozen spec
C2_A=$(commit "case A: prose mention of missing/case-a.txt without any backticks; nothing cited")

# (b) backticked path:line anchor -> strip anchor, path exists
C3_B=$(commit "case B: see \`corpus/self_check.py:12\` for the rule line")

# (c) backticked directory cite -> tree object exists
C4_C=$(commit "case C: the \`corpus/\` directory holds the gate scripts")

# (d) bare .log name that exists only in a LATER commit -> miss vs own tree
C5_D=$(commit "case D: receipt at \`case-d-receipt.log\` will be added by the next commit")

# (e) leading ./ and comma-inside-backticks -> normalize both, path exists
mkdir -p "$D/reports"
printf 'log\n' > "$D/reports/case-d-receipt.log"   # lands HERE (after case D cited it)
C6_E=$(commit "case E: leading dot-slash \`./corpus/other.py\`, plus comma-in-token \`corpus/other.py,\` and adds reports/case-d-receipt.log")

# (f1) path exists at THIS commit; renamed two commits later (catches HEAD-tree bug)
printf 'old\n' > "$D/corpus/old_name.py"
C7_F1=$(commit "case F1: add \`corpus/old_name.py\` (rename follows)")

# (f2) rename; old name gone from THIS tree; message cites old + new
git -C "$D" mv corpus/old_name.py corpus/new_name.py
C8_F2=$(commit "case F2: rename \`corpus/old_name.py\` to \`corpus/new_name.py\`; old name now absent from this tree")

# (g) backticked commands/flags/bare word -> not path citations
C9_G=$(commit "case G: run \`git status\` and \`git log -1\`; flag \`--amend\`; tool \`jj\`")

# (h) merge: side commit adds a file; merge cites it; both carry it in their own trees
git -C "$D" checkout -q -b side
printf 'side\n' > "$D/corpus/side.py"
C_SIDE=$(commit "case H side: add \`corpus/side.py\` on the side branch")
git -C "$D" checkout -q master 2>/dev/null || git -C "$D" checkout -q main
git -C "$D" merge -q --no-ff --no-edit -m "case H: merge side; \`corpus/side.py\` lands in the merge tree" side
C_MERGE=$(git -C "$D" rev-parse HEAD)

# ---- emit hashes -------------------------------------------------------------
{
  echo "D=$D"
  echo "C0=$C0"; echo "C1=$C1"
  echo "C2_A=$C2_A"; echo "C3_B=$C3_B"; echo "C4_C=$C4_C"; echo "C5_D=$C5_D"
  echo "C6_E=$C6_E"; echo "C7_F1=$C7_F1"; echo "C8_F2=$C8_F2"; echo "C9_G=$C9_G"
  echo "C_SIDE=$C_SIDE"; echo "C_MERGE=$C_MERGE"
} > "$S/cases.env"

# ---- pre-registered expectations (frozen BEFORE any instrument run) ----------
# fields: case_id, range_expr, expected_cited, expected_miss, expected_exit, rationale
cat > "$S/expected.tsv" <<'EOF'
A	{C1}..{C2_A}	0	0	0	frozen spec extracts backticked paths + .log names; plain prose out of scope
B	{C2_A}..{C3_B}	1	0	0	`path:line` anchor stripped; corpus/self_check.py exists in tree
C	{C3_B}..{C4_C}	1	0	0	`corpus/` is a tree object; git cat-file -e accepts it (probed: exit 0)
D	{C4_C}..{C5_D}	1	1	1	bare .log resolved by suffix match against commit's OWN tree; absent here -> miss (bare)
E	{C5_D}..{C6_E}	2	0	0	leading ./ accepted by git natively (probed: exit 0); comma inside backticks is punctuation -> strip
F1	{C6_E}..{C7_F1}	1	0	0	checked against c_F1's OWN tree where old_name.py exists (catches HEAD-tree bug)
F2	{C7_F1}..{C8_F2}	2	1	1	commit's own tree lacks old_name.py after rename -> miss (catches HEAD-tree bug from other side)
G	{C8_F2}..{C9_G}	0	0	0	whitespace tokens are commands; flags/bare non-filename words are not repo-relative paths (jj advisory)
Hside	{C9_G}..{C_SIDE}	1	0	0	side commit's own tree carries corpus/side.py
H	{C_SIDE}..{C_MERGE}	1	0	0	merge processed, not skipped; merge tree carries corpus/side.py; no crash on merge
AGG	{C0}..{C_MERGE}	11	-	1	commits=11 total; misses exactly 2 (case D bare log, case F2 old name); exit 1
EOF

# substitute hashes
sed -i "s/{C0}/$C0/g; s/{C1}/$C1/g; s/{C2_A}/$C2_A/g; s/{C3_B}/$C3_B/g; s/{C4_C}/$C4_C/g; s/{C5_D}/$C5_D/g; s/{C6_E}/$C6_E/g; s/{C7_F1}/$C7_F1/g; s/{C8_F2}/$C8_F2/g; s/{C9_G}/$C9_G/g; s/{C_SIDE}/$C_SIDE/g; s/{C_MERGE}/$C_MERGE/g" "$S/expected.tsv"

echo "FIXTURE_BUILT $D"
cat "$S/cases.env"
