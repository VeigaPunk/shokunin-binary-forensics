#!/usr/bin/env python3
"""Round-70 do-nothing and gaming controls (frozen in reports/round-70/claims.md).

Builds each control tree from `git archive 3f5edbc... corpus SHONEN.md SCORECARD.md SKILL.md`
in a scratch directory (never in the lane), runs the frozen counter on it and writes
`reports/round-70/controls/<name>.log` with the exact command and exit code. The point of
each control is the one cheapest move that skips the claimed work; a control that reaches a
claim's target would mean the counter or target is wrong (AXES.md / prompt section 9).

Usage: python3 -B reports/round-70/build-controls.py   (cwd = lane root)
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
BASE = "3f5edbc206351232a3d2d801334dd930499ccaf5"
COUNTER = LANE / "reports/round-70/measure.py"
OUT = LANE / "reports/round-70/controls"
TOOLS = ("self_assessment_check.py", "lint_entry.py", "check_embedded_outputs.py",
         "embedded_output_pins.json", "derive_axml_anchors_r68.py")
V5 = "corpus/knowledge/round-70-apk-axml-byte-evidence.md"


def archive(dest):
    p = subprocess.run(f"git -C {LANE} archive {BASE} corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C {dest}",
                       shell=True, check=True)
    return dest


def flip_c05(tree):
    f = tree / "corpus/README.md"
    t = f.read_text(encoding="utf-8")
    rows = []
    for l in t.splitlines():
        if l.startswith("| C05 "):
            cols = l.split("|")
            cols[3] = " `knowledge/round-70-apk-axml-byte-evidence.md` "
            cols[-2] = " held "
            l = "|".join(cols)
        rows.append(l)
    f.write_text("\n".join(rows) + "\n", encoding="utf-8")


def overlay_tools(tree):
    for t in TOOLS:
        shutil.copy(LANE / "corpus" / t, tree / "corpus" / t)


def control_a(t):
    pass


def control_b(t):
    flip_c05(t)


def control_c(t):
    overlay_tools(t)
    flip_c05(t)
    (t / V5).write_text("admission-status: admitted\n# stub\n", encoding="utf-8")


def control_d(t):
    overlay_tools(t)
    flip_c05(t)
    src = (t / "corpus/knowledge/round-69-apk-axml-byte-evidence.md").read_text(encoding="utf-8").splitlines()
    src = [("admission-status: admitted" if l.startswith("admission-status:") else l) for l in src]
    (t / V5).write_text("\n".join(src) + "\n", encoding="utf-8")


def control_e(t):
    (t / "corpus/self_assessment_check.py").write_text(
        "import sys\nfor k in ('SM1','SM2','SM3','SM4','SM5','SM6'): print(f'{k}=0')\nprint('SELF_MISMATCH=0')\nsys.exit(0)\n",
        encoding="utf-8")


def control_f(t):
    overlay_tools(t)
    (t / "SHONEN.md").write_text("# revenger-shokunin — Promotion checklist\n", encoding="utf-8")


def control_g(t):
    overlay_tools(t)
    f = t / "corpus/knowledge/round-68-apk-axml-byte-evidence.md"
    keep = [l for l in f.read_text(encoding="utf-8").splitlines()
            if not re.match(r"^enum RES_XML_(START_ELEMENT|END_ELEMENT|RESOURCE_MAP)_TYPE : \d+$", l)]
    f.write_text("\n".join(keep) + "\n", encoding="utf-8")


def control_h(t):
    overlay_tools(t)


CONTROLS = {
    "A-do-nothing-base": (control_a, "base tree: the do-nothing control for all three claims"),
    "B-readme-flip-only": (control_b, "C1 cheapest: flip the C05 row to held naming a v5 file that does not exist"),
    "C-stub-entry-flip": (control_c, "C1: a two-line stub marked admitted plus the flip"),
    "D-v4-clone-flip": (control_d, "C1: the rejected v4 entry copied to the v5 path, header set admitted, plus the flip"),
    "E-noop-checker": (control_e, "C2 cheapest: a checker that prints SELF_MISMATCH=0 unconditionally"),
    "F-shonen-delete": (control_f, "C2: treated tools, SHONEN boxes deleted instead of corrected"),
    "G-r68-entry-edited": (control_g, "C3: delete the seven drifting lines from the retained r68 entry instead of fixing the gate"),
    "H-tools-only": (control_h, "treated tools overlaid on the base tree, no README/SHONEN/SCORECARD repair"),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    only = sys.argv[1:]
    for name, (fn, why) in CONTROLS.items():
        if only and name not in only:
            continue
        d = Path(tempfile.mkdtemp(prefix=f"rev-r70-ctl-{name}-", dir="/fast/scratch/revenger-r70"))
        archive(d)
        fn(d)
        p = subprocess.run([sys.executable, "-B", str(COUNTER), str(d)], capture_output=True, text=True)
        body = "\n".join(l for l in p.stdout.splitlines() if not l.startswith("HOLD verify"))
        (OUT / f"{name}.log").write_text(
            f"# control {name}: {why}\n# base {BASE}\n$ python3 -B {COUNTER} <tree>\n{body}\nEXIT={p.returncode}\n"
            + (f"STDERR: {p.stderr.strip()[-400:]}\n" if p.stderr.strip() else ""), encoding="utf-8")
        print(name, "exit", p.returncode, [l for l in p.stdout.splitlines() if l.startswith("HOLDS_")])
        shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    main()
