#!/usr/bin/env bash
# make_c1_controls_r99.sh <counter> <work> [freeze-rev] [landing-rev] — build
# and score the round-99 C1 do-nothing and junk-row control trees (c14r99).
#
# From [freeze-rev] (default: the Amendment A commit 61e27feb4e8099af7f9bf41fbf69e223354f691e —
# same entry bytes and identical corpus/README.md as the original claims-freeze
# commit 7e6edd4db649f99c425daa46a91edbbd18a6e27c, plus the S505 used-by
# grounding and the round-99 wave registry) it builds:
#   <work>/do-nothing/   the claims-freeze tree, unchanged
#   <work>/junk-row/     identical, except corpus/README.md row C14's status
#                        cell partial -> held (nothing else)
#   <work>/landing-diag/ only when [landing-rev] is given: that revision's
#                        tree, for the L1's post-v8-freeze landing scoring.
#                        This script never runs a counter on it (seats must
#                        not score a tree with C14 held).
# It then runs, per the frozen v8 interface contract:
#   python3 -B <counter> --profile c14r99 --tree <work>/do-nothing  --work ...
#   python3 -B <counter> --profile c14r99 --tree <work>/junk-row    --work ...
# writing the counter's full stdout plus a trailing `# rc=<n>` line to
# <work>/do-nothing.log and <work>/junk-row.log, and printing:
#   C1_CONTROL_DONOTHING=<verdict>
#   C1_CONTROL_JUNKROW=<verdict>
# A sound instrument refuses both trees; the script exits 0 iff both verdicts
# are `fail` (control-ok), 1 if a control passed or its verdict line is
# missing (control-BROKEN), 2 on usage/setup error.
#
# The lane checkout is only read (git archive / rev-parse), never written.
# Counter scratch is routed under <work> (TMPDIR/HYAKU_SCRATCH exported), so
# no scratch path is hardcoded and TMPDIR/--work are honoured.
set -u

LANE=$(cd "$(dirname -- "$0")/../../.." && pwd) || exit 1
FREEZE_DEFAULT=61e27feb4e8099af7f9bf41fbf69e223354f691e

usage() { echo "usage: $0 <counter> <work> [freeze-rev] [landing-rev]" >&2; exit 2; }

[ $# -ge 1 ] && [ $# -le 4 ] || usage
COUNTER=$1
WORK=$2
FREEZE_REV=${3:-$FREEZE_DEFAULT}
LAND_REV=${4:-}
case "$COUNTER" in ''|-*) usage;; esac
case "$WORK" in ''|-*) usage;; esac

[ -f "$COUNTER" ] || { echo "make_c1_controls_r99: counter not found: $COUNTER" >&2; exit 2; }

git -C "$LANE" rev-parse --verify "${FREEZE_REV}^{commit}" >/dev/null 2>&1 || {
  echo "make_c1_controls_r99: freeze rev $FREEZE_REV not resolvable in $LANE" >&2; exit 1; }
if [ -n "$LAND_REV" ]; then
  git -C "$LANE" rev-parse --verify "${LAND_REV}^{commit}" >/dev/null 2>&1 || {
    echo "make_c1_controls_r99: landing rev $LAND_REV not resolvable in $LANE" >&2; exit 1; }
fi

mkdir -p "$WORK" || exit 1
WORK=$(cd "$WORK" && pwd) || exit 1
mkdir -p "$WORK/do-nothing" "$WORK/junk-row" "$WORK/tmp" "$WORK/hyaku" "$WORK/counter-run" || exit 1

git -C "$LANE" archive --format=tar "$FREEZE_REV" | tar -x -C "$WORK/do-nothing" || exit 1
cp -a "$WORK/do-nothing/." "$WORK/junk-row/"

# junk-row edit: only the C14 line of corpus/README.md, only its status cell.
python3 - "$WORK/junk-row" <<'EOF' || exit 1
import pathlib, re, sys
tree = pathlib.Path(sys.argv[1])
p = tree / "corpus" / "README.md"
lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
idx = [i for i, l in enumerate(lines) if re.match(r"^\| C14 \|", l)]
assert len(idx) == 1, f"C14 lines: {len(idx)}"
l = lines[idx[0]]
new, n = re.subn(r"\| partial \|(\s*)$", r"| held |\1", l)
assert n == 1, f"status-cell substitutions: {n}"
lines[idx[0]] = new
p.write_text("".join(lines), encoding="utf-8")
assert "| held |" in new
EOF

# Print the inter-tree diff; differences found -> diff exits 1, which is expected.
rc=0
diff -r "$WORK/do-nothing" "$WORK/junk-row" || rc=$?
case $rc in
  0) echo "make_c1_controls_r99: ERROR — trees identical, junk edit missing" >&2; exit 1;;
  1) ;;
  *) echo "make_c1_controls_r99: ERROR — diff failed (rc=$rc)" >&2; exit 1;;
esac

# Assert the only difference is corpus/README.md, and within it exactly one
# line changed, and only in the C14 status cell.
python3 - "$WORK/do-nothing" "$WORK/junk-row" <<'EOF' || exit 1
import pathlib, re, sys
a, b = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
fa = {p.relative_to(a) for p in a.rglob("*") if p.is_file()}
fb = {p.relative_to(b) for p in b.rglob("*") if p.is_file()}
assert fa == fb, f"file sets differ: {sorted(fa ^ fb)}"
diffs = [r for r in fa if (a / r).read_bytes() != (b / r).read_bytes()]
assert diffs == [pathlib.Path("corpus/README.md")], f"differing files: {diffs}"
la = (a / "corpus/README.md").read_text(encoding="utf-8").splitlines()
lb = (b / "corpus/README.md").read_text(encoding="utf-8").splitlines()
assert len(la) == len(lb)
changed = [i for i, (x, y) in enumerate(zip(la, lb)) if x != y]
assert len(changed) == 1, f"changed README lines: {changed}"
i = changed[0]
assert re.match(r"^\| C14 \|", la[i]), f"changed line is not C14: {la[i][:40]!r}"
assert lb[i] == re.sub(r"\| partial \|", "| held |", la[i]), "change is not the status cell"
print(f"make_c1_controls_r99: exactly one changed cell (README line {i + 1}, C14 partial -> held)")
EOF

if [ -n "$LAND_REV" ]; then
  mkdir -p "$WORK/landing-diag"
  git -C "$LANE" archive --format=tar "$LAND_REV" | tar -x -C "$WORK/landing-diag" || exit 1
  echo "make_c1_controls_r99: landing-diag tree built at $WORK/landing-diag (NOT scored here)"
fi

run_control() {
  # $1 tree dir, $2 log path; echoes nothing to stdout (log gets it all).
  local tree=$1 log=$2 rc=0
  TMPDIR="$WORK/tmp" HYAKU_SCRATCH="$WORK/hyaku" PYTHONUTF8=1 \
    python3 -B "$COUNTER" --profile c14r99 --tree "$tree" --work "$WORK/counter-run" \
    >"$log" 2>&1 || rc=$?
  printf '# rc=%s\n' "$rc" >>"$log"
  printf 'make_c1_controls_r99: %s counter rc=%s\n' "$log" "$rc" >&2
  return "$rc"
}

verdict_of() {
  # $1 log path -> prints pass|fail|missing
  local v
  v=$(sed -n 's/^C1_VERDICT=\(pass\|fail\)$/\1/p' "$1" | head -n 1)
  printf '%s' "${v:-missing}"
}

run_control "$WORK/do-nothing" "$WORK/do-nothing.log"; DN_RC=$?
run_control "$WORK/junk-row" "$WORK/junk-row.log"; JR_RC=$?

DN_V=$(verdict_of "$WORK/do-nothing.log")
JR_V=$(verdict_of "$WORK/junk-row.log")
echo "C1_CONTROL_DONOTHING=$DN_V"
echo "C1_CONTROL_JUNKROW=$JR_V"

if [ "$DN_V" = "fail" ] && [ "$JR_V" = "fail" ]; then
  printf 'make_c1_controls_r99: control-ok (do-nothing rc=%s, junk-row rc=%s; both refused)\n' \
    "$DN_RC" "$JR_RC"
  exit 0
fi
printf 'make_c1_controls_r99: control-BROKEN (do-nothing rc=%s verdict=%s, junk-row rc=%s verdict=%s)\n' \
  "$DN_RC" "$DN_V" "$JR_RC" "$JR_V" >&2
exit 1
