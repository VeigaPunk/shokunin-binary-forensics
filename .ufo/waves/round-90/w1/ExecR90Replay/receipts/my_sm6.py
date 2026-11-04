#!/usr/bin/env python3
"""ExecR90Replay independent SM6 truth deriver (round-90 C1 cross-impl).

Written from the battery docstring/claims only; does not import or copy
corpus/self_assessment_check*.py. Usage: my_sm6.py TREE
Rule (claims.md C1 / sm6_battery.py docstring): label 0 iff the current side
of the lane's K statement states N = README rows with status `held` AND
D = README coverage-map rows; else 1 (including: no K statement).
Map rows: README lines matching ^\\| C<digits> \\|; held: last cell == held.
K statement: last SCORECARD line carrying the bare token K_HELD_BACKED
(word-bounded, so K_HELD_BACKED_STRICT does not count). Current side: the
segment after the token up to the next `·`, `;`, `|` or other K_ token; in that
segment the first N/D after the last `→` (or the first N/D if no arrow).
"""
import re
import sys
from pathlib import Path

ROW = re.compile(r"^\| C\d+ \|")
TOK = re.compile(r"(?<![A-Za-z0-9_])K_HELD_BACKED(?![A-Za-z0-9_])")
FRAC = re.compile(r"(\d+)\s*/\s*(\d+)")


def map_counts(root):
    rows = held = 0
    for line in (root / "corpus/README.md").read_text(encoding="utf-8").splitlines():
        if ROW.match(line):
            rows += 1
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            held += cells[-1] == "held"
    return rows, held


def k_statement(root):
    last = None
    for n, line in enumerate((root / "SCORECARD.md").read_text(encoding="utf-8").splitlines(), 1):
        if TOK.search(line):
            last = (n, line)
    if last is None:
        return None, None, None
    n, line = last
    m = list(TOK.finditer(line))[-1]
    seg = re.split(r"[·;|]|K_[A-Z_]+", line[m.end():], maxsplit=1)[0]
    side = seg.split("→")[-1]
    f = FRAC.search(side)
    return n, line, (int(f.group(1)), int(f.group(2))) if f else None


def label(root):
    rows, held = map_counts(root)
    n, line, cur = k_statement(root)
    lab = 0 if cur == (held, rows) else 1
    return lab, rows, held, n, cur


if __name__ == "__main__":
    lab, rows, held, n, cur = label(Path(sys.argv[1]))
    print(f"MY_LABEL={lab} rows={rows} held={held} k_line={n} current={cur}")
