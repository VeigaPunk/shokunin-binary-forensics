#!/usr/bin/env python3
"""Build the 14 SM6 battery cases (case parameters from sm6_battery.py CASES,
transcribed; README row format from its docstring) and label each with my_sm6."""
import ast
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import my_sm6  # noqa: E402

BAT = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/sm6_battery.py")
src = BAT.read_text(encoding="utf-8")
tree = ast.parse(src)
CASES = next(ast.literal_eval(n.value) for n in tree.body
             if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "CASES")
real = Path(sys.argv[1])
work = Path(sys.argv[2])
for cid, rows, held, k_line, frozen in CASES:
    r = work / cid
    (r / "corpus").mkdir(parents=True)
    (r / "corpus/README.md").write_text("".join(
        f"| C{i:02d} | s | k | w | {'held' if i <= held else 'frontier'} |\n" for i in range(1, rows + 1)),
        encoding="utf-8")
    (r / "SCORECARD.md").write_text("## Round 61 x\n" + (k_line + "\n" if k_line else "no statement\n"),
                                    encoding="utf-8")
    lab, R, H, n, cur = my_sm6.label(r)
    print(f"MINE {cid} frozen={frozen} mine={lab} rows={R} held={H} current={cur} "
          f"{'agree' if lab == frozen else 'DISAGREE'}")
lab, R, H, n, cur = my_sm6.label(real)
print(f"MINE R1-real-tree frozen=0 mine={lab} rows={R} held={H} k_line={n} current={cur} "
      f"{'agree' if lab == 0 else 'DISAGREE'}")
f = work / "R2"
(f / "corpus").mkdir(parents=True)
shutil.copy(real / "corpus/README.md", f / "corpus/README.md")
(f / "SCORECARD.md").write_text((real / "SCORECARD.md").read_text(encoding="utf-8") + "\nK_HELD_BACKED 8/14\n",
                                encoding="utf-8")
lab, R, H, n, cur = my_sm6.label(f)
print(f"MINE R2-forged-8-of-14 frozen=1 mine={lab} rows={R} held={H} k_line={n} current={cur} "
      f"{'agree' if lab == 1 else 'DISAGREE'}")
