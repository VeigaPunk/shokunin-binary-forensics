#!/usr/bin/env python3
"""ReviewerR90C1 false-green probe for v2 SM6. Builds trees with the frozen battery's build()
(and a raw-SCORECARD variant for multi-line cases), scores v1 and v2 sm6, compares to a
hand label written per the claims.md predicate (0 iff current side states N=held AND D=map rows).
Usage: python3 -B fg_probe.py LANE  (uses TMPDIR)."""
import importlib.util, sys, tempfile
from pathlib import Path
L = Path(sys.argv[1])
def load(p, n):
    s = importlib.util.spec_from_file_location(n, p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
bat = load(L / "reports/round-90/sm6_battery.py", "bat")
v1 = load(L / "corpus/self_assessment_check.py", "v1")
v2 = load(L / "corpus/self_assessment_check2.py", "v2")
# id, rows, held, SCORECARD body after header (str; may be multi-line), label, note
CASES = [
 ("P01", 15, 8, "K_HELD_BACKED 8/15 (5.3)", 0, "trailing score text"),
 ("P02", 15, 8, "K_HELD_BACKED 8 / 15", 0, "spaced fraction, true"),
 ("P03", 15, 8, "K_HELD_BACKED 8/15 → 9 / 15", 1, "spaced current side, false"),
 ("P04", 15, 8, "K_HELD_BACKED 8/15 (5.3%) → 9/15 (6.0%)", 1, "non-[0-9.] score between sides"),
 ("P05", 15, 8, "K_HELD_BACKED 8/15 => 9/15", 1, "=> arrow"),
 ("P06", 15, 8, "K_HELD_BACKED 8/15 ⇒ 9/15", 1, "double arrow"),
 ("P07", 15, 8, "K_HELD_BACKED was 8/15, now 9/15", 1, "prose before/after"),
 ("P08", 15, 8, "K_HELD_BACKED 8/15 → 9/15 → 8/15", 0, "chained arrows, final true"),
 ("P09", 15, 8, "K_HELD_BACKED 9/15 · K_HELD_BACKED 8/15", 0, "two stmts, last true"),
 ("P10", 15, 8, "K_HELD_BACKED 8/15 · K_HELD_BACKED 9/15", 1, "two stmts, last false"),
 ("P11", 15, 8, "K_HELD_BACKED 9/15\n```\nK_HELD_BACKED 8/15\n```", 1, "false stmt, true one only inside a fenced quote"),
 ("P12", 15, 8, "K_HELD_BACKED 8/15\nK_HELD_BACKED_STRICT 7/15", 0, "STRICT-only last line masks true K"),
 ("P13", 15, 8, "K_HELD_BACKED 9/15\nK_HELD_BACKED_STRICT 7/15", 1, "STRICT-only last line, K false"),
 ("P14", 15, 8, "K_HELD_BACKED_STRICT 7/15 · K_HELD_BACKED 8/15", 0, "STRICT before K on one line"),
 ("P15", 15, 8, "| coverage — K | 8/15 (5.3) → 9/15 (6.0) | `measure.py TREE` (`K_HELD_BACKED=8/15`) | same |", 1, "lane table format: after-column false, counter citation true"),
 ("P16", 15, 8, "| coverage — K | 8/15 (5.3) → 8/15 (5.3) | `measure.py TREE` (`K_HELD_BACKED=8/15`) | same |", 0, "lane table format, true (control = real row shape)"),
 ("P17", 15, 8, "K_HELD_BACKED in round 89: 8/15", 0, "digits between token and stmt"),
 ("P18", 15, 8, "K_HELD_BACKED 8/15\nK_HELD_BACKED unchanged", 0, "numberless last K line masks true K"),
 ("P19", 15, 8, "K_HELD_BACKED 8/15 -> 9/15", 1, "ascii arrow, false (control)"),
]
def build_raw(root, rows, held, body, extra_readme=""):
    bat.build(root, rows, held, None)
    (root / "SCORECARD.md").write_text("## Round 61 x\n" + body + "\n", encoding="utf-8")
    if extra_readme:
        p = root / "corpus/README.md"; p.write_text(p.read_text() + extra_readme, encoding="utf-8")
fg = fr = 0
with tempfile.TemporaryDirectory(prefix="rr90c1-") as d:
    d = Path(d)
    allc = [(c[0], c[1], c[2], c[3], c[4], c[5], "") for c in CASES] + [
      ("P20", 15, 8, "K_HELD_BACKED 8/16", 1, "README carries an extra `| C99 |` row in a fenced example (map is 15)", "\n```\n| C99 | s | k | w | frontier |\n```\n"),
      ("P21", 15, 8, "K_HELD_BACKED 8/15", 0, "same README, true 8/15", "\n```\n| C99 | s | k | w | frontier |\n```\n")]
    for cid, rows, held, body, label, note, extra in allc:
        build_raw(d / cid, rows, held, body, extra)
        g1, g2 = v1.sm6(d / cid), v2.sm6(d / cid)
        kind = "ok" if g2 == label else ("FALSE-GREEN" if g2 == 0 else "FALSE-RED")
        fg += kind == "FALSE-GREEN"; fr += kind == "FALSE-RED"
        print(f"{cid} rows={rows} held={held} label={label} v1={g1} v2={g2} {kind} :: {note} :: {body!r}")
print(f"V2_FALSE_GREEN={fg} V2_FALSE_RED={fr} of {len(allc)}")
