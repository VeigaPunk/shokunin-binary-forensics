import importlib.util, sys, tempfile
from pathlib import Path
S = Path("/fast/scratch/hyaku/revenger-r90/MutR90SM6")
LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
SRC = LANE / "corpus/self_assessment_check2.py"
exec(open(S / "drive.py").read().split("env = dict")[0].split("M = [", 1)[0])  # paths only
Ms = {}
src = SRC.read_text()
import re
for line in open(S / "drive.py").read().split("M = [", 1)[1].split("]\n\nenv", 1)[0].splitlines():
    pass
ns = {}
exec("M = [" + open(S / "drive.py").read().split("M = [", 1)[1].split("\nenv = dict")[0], ns)
def load(name, text):
    p = S / f"w_{name}.py"; p.write_text(text)
    spec = importlib.util.spec_from_file_location(name, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
mods = {"pristine": load("pristine", src)}
for name, old, new in ns["M"]:
    mods[name] = load(name, src.replace(old, new))
def rows(n, held, extra=""):
    return extra + "".join(f"| C{i:02d} | s | k | w | {'held' if i <= held else 'frontier'} |\n" for i in range(1, n + 1))
W = [  # id, readme, scorecard, truth label, target mutant
 ("W1_header_row_C", rows(15, 8, "| Criterion | s | k | w | status |\n|---|---|---|---|---|\n"), "K_HELD_BACKED 8/15\n", 0, "M5_count_all_pipe_C_rows"),
 ("W2_two_stmts_one_line", rows(15, 8), "K_HELD_BACKED 9/15 · corrected K_HELD_BACKED 8/15\n", 0, "M6a_first_statement"),
 ("W3_K_line_without_ratio", rows(15, 8), "K_HELD_BACKED unchanged (see r73)\n", 1, "M8a_no_statement_returns_0"),
 ("W4_held_in_other_column", rows(15, 8).replace("| C09 | s |", "| C09 | held-out set |"), "K_HELD_BACKED 9/15\n", 1, "M9_held_unanchored"),
]
with tempfile.TemporaryDirectory(dir=S) as d:
    for wid, readme, sc, label, target in W:
        r = Path(d) / wid; (r / "corpus").mkdir(parents=True)
        (r / "corpus/README.md").write_text(readme); (r / "SCORECARD.md").write_text("## Round 61 x\n" + sc)
        p, m = mods["pristine"].sm6(r), mods[target].sm6(r)
        print(f"WITNESS {wid} label={label} pristine={p} {target}={m} -> {'distinguishes (mutant wrong)' if p == label and m != label else 'NO'}")
