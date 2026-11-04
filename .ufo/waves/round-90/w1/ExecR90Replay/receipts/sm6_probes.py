#!/usr/bin/env python3
"""Extra (non-frozen) SM6 probes: my_sm6 label vs v1/v2 sm6() verdicts.
The frozen instruments are loaded only to obtain their verdicts; my labels come
from my_sm6 (independent). Intended truth per case is written by hand below."""
import importlib.util
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import my_sm6  # noqa: E402

L = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")


def load(p):
    s = importlib.util.spec_from_file_location(p.stem, p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


v1 = load(L / "corpus/self_assessment_check.py")
v2 = load(L / "corpus/self_assessment_check2.py")
work = Path(sys.argv[1])
PROBES = [  # id, rows, held, scorecard body, hand truth
    ("S01-spaced-fraction", 15, 8, "K_HELD_BACKED 8 / 15\n", 0),
    ("S02-stale-later-prose-token", 15, 8, "K_HELD_BACKED 8/15\nthe old K_HELD_BACKED was 8/14\n", 1),
    ("S03-strict-only-last", 15, 8, "K_HELD_BACKED 8/15\nK_HELD_BACKED_STRICT 7/15\n", 0),
    ("S04-two-arrows", 15, 8, "K_HELD_BACKED 7/14 → 8/14 → 8/15\n", 0),
    ("S05-arrow-then-other-metric", 15, 8, "K_HELD_BACKED 8/14 → 8/15; F4 10/11 → 11/11\n", 0),
    ("S06-token-no-fraction", 15, 8, "K_HELD_BACKED unchanged\n", 1),
    ("S07-ascii-arrow", 15, 8, "K_HELD_BACKED 8/14 -> 8/15\n", 0),
    ("S08-held-in-other-column", 15, 8, None, 0),
]
for cid, rows, held, sc, truth in PROBES:
    r = work / cid
    (r / "corpus").mkdir(parents=True)
    if sc is None:  # README with an extra non-status `held` cell; K 8/15 true
        body = "".join(f"| C{i:02d} | held | k | w | {'held' if i <= held else 'frontier'} |\n"
                       for i in range(1, rows + 1))
        sc = "K_HELD_BACKED 8/15\n"
    else:
        body = "".join(f"| C{i:02d} | s | k | w | {'held' if i <= held else 'frontier'} |\n"
                       for i in range(1, rows + 1))
    (r / "corpus/README.md").write_text(body, encoding="utf-8")
    (r / "SCORECARD.md").write_text("## Round 61 x\n" + sc, encoding="utf-8")
    mine = my_sm6.label(r)
    print(f"PROBE {cid} truth={truth} mine={mine[0]} cur={mine[4]} v1={v1.sm6(r)} v2={v2.sm6(r)}")
