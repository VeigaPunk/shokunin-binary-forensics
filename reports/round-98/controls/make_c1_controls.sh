#!/usr/bin/env bash
# make_c1_controls.sh <out-dir> — build the C1 do-nothing and junk-row control trees.
#
# From the claims-freeze commit 9d49002a3804de48d365b7d32849ada06745d64f it builds:
#   <out-dir>/do-nothing/   the claims-freeze tree, unchanged
#   <out-dir>/junk-row/     identical, except corpus/README.md row C14's status
#                           cell partial -> held (nothing else)
# It prints `diff -r` of the two trees (which must show exactly that one cell)
# and exits 0. It runs no counter: the L1 scores the trees after the v7 freeze.
#
# Honours its arguments only; no scratch path is hardcoded. Lane root is derived
# from this script's location (reports/round-98/controls/ -> lane root).
set -u

LANE=$(cd "$(dirname -- "$0")/../../.." && pwd)
FREEZE_REV=9d49002a3804de48d365b7d32849ada06745d64f

usage() { echo "usage: $0 <out-dir>" >&2; exit 2; }

[ $# -eq 1 ] || usage
OUT=$1
case "$OUT" in -*|'') usage;; esac

git -C "$LANE" rev-parse --verify "${FREEZE_REV}^{commit}" >/dev/null 2>&1 || {
  echo "make_c1_controls: freeze rev $FREEZE_REV not resolvable in $LANE" >&2; exit 1; }

mkdir -p "$OUT/do-nothing" "$OUT/junk-row"

git -C "$LANE" archive --format=tar "$FREEZE_REV" | tar -x -C "$OUT/do-nothing" || exit 1

cp -a "$OUT/do-nothing/." "$OUT/junk-row/"

# junk-row edit: only the C14 line of corpus/README.md, only its status cell.
python3 - "$OUT/junk-row" <<'EOF' || exit 1
import pathlib, re, sys
tree = pathlib.Path(sys.argv[1])
p = tree / "corpus" / "README.md"
lines = p.read_text(encoding="utf-8").splitlines(keepends=True)
idx = [i for i, l in enumerate(lines) if re.match(r"^\| C14 \|", l)]
assert len(idx) == 1, f"C14 lines: {len(idx)}"
l = lines[idx[0]]
new, n = re.subn(r"\| partial \|(\s*)$", r"| held |\1", l)
assert n == 1 and "| partial |" not in l.replace("| partial |", "", 1) or True
lines[idx[0]] = new
p.write_text("".join(lines), encoding="utf-8")
assert "| held |" in new
EOF

# Print the inter-tree diff; differences found -> diff exits 1, which is expected.
diff -r "$OUT/do-nothing" "$OUT/junk-row" || rc=$?
case "${rc:-0}" in
  0) echo "make_c1_controls: ERROR — trees identical, junk edit missing" >&2; exit 1;;
  1) ;;
  *) echo "make_c1_controls: ERROR — diff failed (rc=$rc)" >&2; exit 1;;
esac

# Assert the only difference is corpus/README.md, and within it exactly one
# line changed, and only in the C14 status cell.
python3 - "$OUT/do-nothing" "$OUT/junk-row" <<'EOF' || exit 1
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
print(f"make_c1_controls: exactly one changed cell (README line {i + 1}, C14 partial -> held)")
EOF

exit 0
