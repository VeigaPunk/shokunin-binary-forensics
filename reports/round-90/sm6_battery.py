#!/usr/bin/env python3
"""Frozen SM6 truth battery (round-90 C1, calibration).

Usage:
    python3 -B reports/round-90/sm6_battery.py --impl <checker.py> [--real TREE]

Scores ONLY the SM6 class (`sm6(root)`) of the named self-assessment checker
(v1 `corpus/self_assessment_check.py` or v2 `corpus/self_assessment_check2.py`)
against hand-written truth labels fixed before any v2 score: a K statement is
TRUE (label 0, no mismatch) iff its current side states N = README rows with
status `held` AND D = README coverage-map rows; otherwise label 1.

Synthetic cases B01-B12 build a minimal TREE (corpus/README.md with R map rows,
H of them `held`, plus a SCORECARD.md line). With --real TREE two more cases run
over a `git archive` extraction of the lane: R1 the tree as committed (label
given by --real-label, default 0) and R2 the forgery control, the same tree with
`K_HELD_BACKED 8/14` appended as the last K line (label 1: the map has 15 rows).

Prints `CASE <id> label=<l> got=<g> <ok|MISCLASS>` per case and
`SM6_MISCLASS=<n>/<cases>`. Exit 0 iff n == 0, 1 otherwise, 64 on usage.
"""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

CASES = [  # id, map rows, held rows, SCORECARD K line (None = no K line), label
    ("B01", 15, 8, "K_HELD_BACKED 8/15", 0),
    ("B02", 15, 8, "K_HELD_BACKED 8/14", 1),
    ("B03", 15, 8, "K_HELD_BACKED 9/15", 1),
    ("B04", 15, 8, "K_HELD_BACKED 8/14 → 8/15", 0),
    ("B05", 15, 8, "K_HELD_BACKED 8/15 → 8/14", 1),
    ("B06", 14, 8, "K_HELD_BACKED 8/14", 0),
    ("B07", 14, 8, "K_HELD_BACKED 8/14 (5.7) → 8/15 (5.3)", 1),
    ("B08", 15, 8, "`K_HELD_BACKED` 8/14 (5.7) → 8/15 (5.3)", 0),
    ("B09", 15, 8, None, 1),
    ("B10", 16, 9, "(`K_HELD_BACKED=9/16`)", 0),
    ("B11", 15, 8, "K_HELD_BACKED 8/15 · K_HELD_BACKED_STRICT 7/15", 0),
    ("B12", 15, 7, "K_HELD_BACKED 8/15", 1),
]


def load(path):
    spec = importlib.util.spec_from_file_location("sm_impl", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def build(root, rows, held, k_line):
    (root / "corpus").mkdir(parents=True)
    body = "".join(f"| C{i:02d} | s | k | w | {'held' if i <= held else 'frontier'} |\n"
                   for i in range(1, rows + 1))
    (root / "corpus/README.md").write_text(body, encoding="utf-8")
    sc = "## Round 61 x\n" + (k_line + "\n" if k_line else "no statement\n")
    (root / "SCORECARD.md").write_text(sc, encoding="utf-8")


def main(argv):
    if "--impl" not in argv:
        print(__doc__, file=sys.stderr)
        return 64
    mod = load(Path(argv[argv.index("--impl") + 1]).resolve())
    real = Path(argv[argv.index("--real") + 1]).resolve() if "--real" in argv else None
    real_label = int(argv[argv.index("--real-label") + 1]) if "--real-label" in argv else 0
    mis = n = 0
    with tempfile.TemporaryDirectory(prefix="rev-r90-sm6-") as d:
        d = Path(d)
        results = []
        for cid, rows, held, k_line, label in CASES:
            build(d / cid, rows, held, k_line)
            results.append((cid, label, mod.sm6(d / cid)))
        if real is not None:
            results.append(("R1-real-tree", real_label, mod.sm6(real)))
            forged = d / "R2"
            (forged / "corpus").mkdir(parents=True)
            shutil.copy(real / "corpus/README.md", forged / "corpus/README.md")
            (forged / "SCORECARD.md").write_text(
                (real / "SCORECARD.md").read_text(encoding="utf-8") + "\nK_HELD_BACKED 8/14\n", encoding="utf-8")
            results.append(("R2-forged-8-of-14", 1, mod.sm6(forged)))
        for cid, label, got in results:
            n += 1
            mis += got != label
            print(f"CASE {cid} label={label} got={got} {'ok' if got == label else 'MISCLASS'}")
    print(f"SM6_MISCLASS={mis}/{n}")
    return 0 if mis == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
