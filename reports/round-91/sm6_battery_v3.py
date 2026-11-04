#!/usr/bin/env python3
"""Frozen SM6 truth battery v3 (round-91 C1, calibration).

Usage:
    python3 -B reports/round-91/sm6_battery_v3.py --impl <checker.py> [--real TREE]

Scores ONLY the SM6 class (`sm6(root)`) of the named self-assessment checker
against hand-written truth labels fixed before any v3 implementation existed:
a K statement is TRUE (label 0, no mismatch) iff the region where the lane
states its before->after numbers carries the LAST `N/D` of that region, with
N = README rows whose status is `held` and D = README coverage-map rows
(`^| C<n> `); a row whose stated region carries no `N/D` is a mismatch
(label 1: the row does not state the quantity it is judged on).

Cases B01-B12 are the bare-line cases retained from the round-90 battery
(`reports/round-90/sm6_battery.py`, unchanged labels). Cases R01-R09 are the
lane's own table-row format: `| axis | before -> after | counter | commits |
verdict |`, where the round-90 critic showed v2 reads the *pointer* cell. R01
and R02 are the verbatim SCORECARD lines 693 and 667 of the freeze base; the
rest are the same shape with the numbers varied in both directions (a true row
whose pointer cell disagrees, and a false row whose pointer cell agrees).

Prints `CASE <id> label=<l> got=<g> <ok|MISCLASS>` per case and
`SM6_MISCLASS=<n>/<cases>`. Exit 0 iff n == 0, 1 otherwise, 64 on usage.
"""
import importlib.util
import shutil
import sys
import tempfile
from pathlib import Path

# id, map rows, held rows, SCORECARD K line (None = no K line), label
CASES = [
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
    # R01: verbatim SCORECARD.md:693 at the freeze base (stated cell 8/15 -> 8/15)
    ("R01", 15, 8,
     "| coverage — knowledge-map ground K (C05, C10, C15) | 8/15 (5.3) → 8/15 (5.3); "
     "C05 uncovered, C10 partial (candidate rejected this round), C15 uncovered | "
     "`reports/round-73/measure.py TREE` (`K_HELD_BACKED=8/15`) | same | "
     "**unchanged** (honest: no admission) |", 0),
    # R02: verbatim SCORECARD.md:667 shape (14 -> 15 rows; after-side 8/15 is true)
    ("R02", 15, 8,
     "| coverage — knowledge-map ground K / C15 tool landscape | `K_HELD_BACKED` 8/14 (5.7) → "
     "8/15 (5.3); `C15_HELD_BACKED` 0/1 → 0/1 | `reports/round-72/measure.py TREE` | "
     "prior `dac9590` → candidate `99911e8` | **C1 FALSIFIED** |", 0),
    # R03: stated after-side is FALSE (9/15 vs 8 held); pointer cell says the truth
    ("R03", 15, 8,
     "| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 9/15 (5.3); "
     "C05 uncovered | `reports/round-91/measure.py TREE` (`K_HELD_BACKED=8/15`) | "
     "`aaaaaaa` → `bbbbbbb` | **improved** |", 1),
    # R04: stated after-side is TRUE; pointer cell disagrees (9/15)
    ("R04", 15, 8,
     "| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3); "
     "C05 uncovered | `reports/round-91/measure.py TREE` (`K_HELD_BACKED=9/15`) | "
     "`aaaaaaa` → `bbbbbbb` | **unchanged** |", 0),
    # R05: wrong denominator in the stated cell; pointer agrees with the map
    ("R05", 15, 8,
     "| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/14 (5.3); "
     "C05 uncovered | `reports/round-91/measure.py TREE` (`K_HELD_BACKED=8/15`) | "
     "`aaaaaaa` → `bbbbbbb` | **improved** |", 1),
    # R06: round-61 shape — stated cell carries scores only, pointer carries the N/D
    ("R06", 14, 6,
     "| coverage — knowledge-map ground (K) | 2.9 → **4.3** | probe `K_HELD_BACKED` "
     "(`K_HELD_BACKED` 4/14 → 6/14) | `cf02419` → `0b6ddf0` | improved |", 1),
    # R07: two N/D pairs in the stated cell; only the LAST is the current side
    ("R07", 15, 8,
     "| coverage — knowledge-map ground K | `K_HELD_BACKED` 4/14 (2.9) → 8/15 (5.3); "
     "C04 and C09 uncovered → held | probe `K_HELD_BACKED` | `cf02419` → `0b6ddf0` | "
     "improved |", 0),
    # R08: wrong numerator in the stated cell; pointer agrees with the map
    ("R08", 15, 8,
     "| coverage — knowledge-map ground K | `K_HELD_BACKED` 9/15 (6.0) → 9/15 (6.0); "
     "C05 uncovered | probe (`K_HELD_BACKED=8/15`) | `aaaaaaa` → `bbbbbbb` | improved |", 1),
    # R09: 16 map rows / 9 held — a hard-coded numerator or denominator fails here
    ("R09", 16, 9,
     "| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/16 (5.0) → 9/16 (5.6); "
     "C16 proposed | probe (`K_HELD_BACKED=9/16`) | `aaaaaaa` → `bbbbbbb` | improved |", 0),
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
    impl = real = real_label = None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--impl":
            impl = Path(argv[i + 1]); i += 2
        elif a == "--real":
            real = Path(argv[i + 1]); i += 2
        elif a == "--real-label":
            real_label = int(argv[i + 1]); i += 2
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"usage: {a}", file=sys.stderr); return 64
    if impl is None:
        print(__doc__, file=sys.stderr)
        return 64
    mod = load(impl)
    bad = 0
    total = 0
    with tempfile.TemporaryDirectory(prefix="rev-r91-bat-") as d:
        d = Path(d)
        for cid, rows, held, k_line, label in CASES:
            root = d / cid
            build(root, rows, held, k_line)
            got = mod.sm6(root)
            total += 1
            ok = (got == 0 and label == 0) or (got == 1 and label == 1)
            if not ok:
                bad += 1
            print(f"CASE {cid} label={label} got={got} {'ok' if ok else 'MISCLASS'}")
        if real is not None:
            lab = 0 if real_label is None else real_label
            got = mod.sm6(real)
            total += 1
            ok = (got == 0 and lab == 0) or (got == 1 and lab == 1)
            if not ok:
                bad += 1
            print(f"CASE REAL label={lab} got={got} {'ok' if ok else 'MISCLASS'}")
    print(f"SM6_MISCLASS={bad}/{total}")
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
