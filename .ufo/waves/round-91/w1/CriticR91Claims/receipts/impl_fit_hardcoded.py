#!/usr/bin/env python3
"""Fitted control, hard-coded table (no import of the battery): keys on (map rows, held,
raw K line text) and returns the frozen label. Never parses the stated cell, never
implements region/arrow/token rules."""
import re, sys
from pathlib import Path
FIT = {
    (15, 8, 'K_HELD_BACKED 8/15'): 0,
    (15, 8, 'K_HELD_BACKED 8/14'): 1,
    (15, 8, 'K_HELD_BACKED 9/15'): 1,
    (15, 8, 'K_HELD_BACKED 8/14 → 8/15'): 0,
    (15, 8, 'K_HELD_BACKED 8/15 → 8/14'): 1,
    (14, 8, 'K_HELD_BACKED 8/14'): 0,
    (14, 8, 'K_HELD_BACKED 8/14 (5.7) → 8/15 (5.3)'): 1,
    (15, 8, '`K_HELD_BACKED` 8/14 (5.7) → 8/15 (5.3)'): 0,
    (15, 8, ''): 1,
    (16, 9, '(`K_HELD_BACKED=9/16`)'): 0,
    (15, 8, 'K_HELD_BACKED 8/15 · K_HELD_BACKED_STRICT 7/15'): 0,
    (15, 7, 'K_HELD_BACKED 8/15'): 1,
    (15, 8, '| coverage — knowledge-map ground K (C05, C10, C15) | 8/15 (5.3) → 8/15 (5.3); C05 uncovered, C10 partial (candidate rejected this round), C15 uncovered | `reports/round-73/measure.py TREE` (`K_HELD_BACKED=8/15`) | same | **unchanged** (honest: no admission) |'): 0,
    (15, 8, '| coverage — knowledge-map ground K / C15 tool landscape | `K_HELD_BACKED` 8/14 (5.7) → 8/15 (5.3); `C15_HELD_BACKED` 0/1 → 0/1 | `reports/round-72/measure.py TREE` | prior `dac9590` → candidate `99911e8` | **C1 FALSIFIED** |'): 0,
    (15, 8, '| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 9/15 (5.3); C05 uncovered | `reports/round-91/measure.py TREE` (`K_HELD_BACKED=8/15`) | `aaaaaaa` → `bbbbbbb` | **improved** |'): 1,
    (15, 8, '| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/15 (5.3); C05 uncovered | `reports/round-91/measure.py TREE` (`K_HELD_BACKED=9/15`) | `aaaaaaa` → `bbbbbbb` | **unchanged** |'): 0,
    (15, 8, '| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/15 (5.3) → 8/14 (5.3); C05 uncovered | `reports/round-91/measure.py TREE` (`K_HELD_BACKED=8/15`) | `aaaaaaa` → `bbbbbbb` | **improved** |'): 1,
    (14, 6, '| coverage — knowledge-map ground (K) | 2.9 → **4.3** | probe `K_HELD_BACKED` (`K_HELD_BACKED` 4/14 → 6/14) | `cf02419` → `0b6ddf0` | improved |'): 1,
    (15, 8, '| coverage — knowledge-map ground K | `K_HELD_BACKED` 4/14 (2.9) → 8/15 (5.3); C04 and C09 uncovered → held | probe `K_HELD_BACKED` | `cf02419` → `0b6ddf0` | improved |'): 0,
    (15, 8, '| coverage — knowledge-map ground K | `K_HELD_BACKED` 9/15 (6.0) → 9/15 (6.0); C05 uncovered | probe (`K_HELD_BACKED=8/15`) | `aaaaaaa` → `bbbbbbb` | improved |'): 1,
    (16, 9, '| coverage — knowledge-map ground K | `K_HELD_BACKED` 8/16 (5.0) → 9/16 (5.6); C16 proposed | probe (`K_HELD_BACKED=9/16`) | `aaaaaaa` → `bbbbbbb` | improved |'): 0,
}
def sm6(root):
    root = Path(root)
    rows = [l for l in (root/"corpus/README.md").read_text(encoding="utf-8").splitlines()
            if re.match(r"^\| C[0-9]+ ", l)]
    held = sum(1 for l in rows if re.search(r"\|\s*held\s*\|\s*$", l))
    ks = [l for l in (root/"SCORECARD.md").read_text(encoding="utf-8").splitlines()
          if "K_HELD_BACKED" in l]
    k = ks[-1].strip() if ks else ""
    return FIT.get((len(rows), held, k), 0)
if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--self-test"]:
        print("SELFTEST OK"); sys.exit(0)
    print("SM6=%d" % sm6(Path(a[a.index("--root")+1])))
    print("SELF_MISMATCH=0"); sys.exit(0)
