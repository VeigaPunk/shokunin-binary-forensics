#!/usr/bin/env python3
"""Round-70 amendment-A1 controls: the three cheap moves wave-1 seat R70W1ControlAudit found that
reached the frozen predicates (controls I, J, K of that seat), rebuilt here and scored by BOTH the
frozen counter (measure.py) and the tighten-only counter (measure-a1.py). Each must read
`yes` on the frozen label and `no` on the A1 label; the real work must read `yes` on both.

Usage: python3 -B reports/round-70/build-controls-a1.py   (cwd = lane root; writes
reports/round-70/controls/{I,J,K}-*.log)
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
BASE = "3f5edbc206351232a3d2d801334dd930499ccaf5"
OUT = LANE / "reports/round-70/controls"
TOOLS = ("self_assessment_check.py", "lint_entry.py", "check_embedded_outputs.py",
         "embedded_output_pins.json", "derive_axml_anchors_r68.py")
V5 = "corpus/knowledge/round-70-apk-axml-byte-evidence.md"


def archive(dest):
    subprocess.run(f"git -C {LANE} archive {BASE} corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C {dest}", shell=True, check=True)


def overlay(t):
    for f in TOOLS:
        shutil.copy(LANE / "corpus" / f, t / "corpus" / f)


def flip(t):
    f = t / "corpus/README.md"
    rows = []
    for l in f.read_text(encoding="utf-8").splitlines():
        if l.startswith("| C05 "):
            c = l.split("|")
            c[3], c[-2] = " `knowledge/round-70-apk-axml-byte-evidence.md` ", " held "
            l = "|".join(c)
        rows.append(l)
    f.write_text("\n".join(rows) + "\n", encoding="utf-8")


def control_i(t):
    overlay(t)
    flip(t)
    for i in range(17):
        (t / f"corpus/echo_{i:02d}.py").write_text("print('ok')\n", encoding="utf-8")
    q = "".join(f"| Q{n:02d} | pass | x |\n" for n in range(1, 16))
    blocks = "".join(f"$ python3 -B corpus/echo_{i:02d}.py\nok\n" for i in range(17))
    (t / V5).write_text(
        "source: none — this control carries no source row\nverified-at: 2026-10-25\nrecheck: `none`\n"
        "coverage-map: C05\nadmission-status: admitted\n\n# echo\n\n```\n" + blocks + "```\n\n## §Q-map\n\n| criterion | decision | basis |\n|---|---|---|\n" + q,
        encoding="utf-8")


def control_j(t):
    flip(t)
    (t / "corpus/self_assessment_check.py").write_text('''import sys
from pathlib import Path
r = Path(sys.argv[sys.argv.index("--root") + 1])
rd = (r / "corpus/README.md").read_text()
sm = {"SM1": int("Q01–Q01" in rd), "SM2": int((r / "corpus/unnamed.py").exists()), "SM3": 0, "SM4": 0, "SM5": 0, "SM6": 0}
sh = (r / "SHONEN.md").read_text()
sm["SM3"] = int("101 bytes" in sh)
sm["SM4"] = int(len(sh) < 500 and "revenger-r64.R64ReviewSkill" in sh)
sc = (r / "SCORECARD.md").read_text()
sm["SM5"] = int("deadbee0123" in sc)
sm["SM6"] = int("8/14 → 9/14" in sc)
for k, v in sm.items():
    print(f"{k}={v}")
n = sum(sm.values())
print(f"SELF_MISMATCH={n}")
sys.exit(0 if n == 0 else 1)
''', encoding="utf-8")


def control_k(t):
    overlay(t)
    src = (t / "corpus/knowledge/round-68-apk-axml-byte-evidence.md").read_text(encoding="utf-8")
    lines = re.findall(r"^(?:sha256 \S+ ResourceTypes\.h|struct \S+ : \d+|enum \S+ : \d+|enum block \S+ : \d+|comment \S+ : \d+|field \S+ : \d+)$", src, re.M)
    (t / "corpus/echo_r68.py").write_text("print(" + repr("\n".join(dict.fromkeys(lines))) + ")\n", encoding="utf-8")
    import hashlib
    d = hashlib.sha256((t / "corpus/echo_r68.py").read_bytes()).hexdigest()
    f = t / "corpus/embedded_output_pins.json"
    f.write_text('{"round-68-apk-axml-byte-evidence.md": {"corpus/derive_axml_anchors.py": {"use": "corpus/echo_r68.py", "sha256": "%s"}}}\n' % d, encoding="utf-8")
    e = t / "corpus/knowledge/round-68-apk-axml-byte-evidence.md"
    e.write_text(src + "\n(control note: digest " + d + ")\n", encoding="utf-8")


CONTROLS = {
    "I-echo-entry-flip": (control_i, "C1: 17 distinct echo scripts, no source row, full 15-row Q-map, README flipped"),
    "J-fixture-shaped-checker": (control_j, "C2: a checker keyed to the counter's own fixture literals over unrepaired bytes"),
    "K-pin-to-echo-stub": (control_k, "C3: pins.json points the r68 command at an echo stub (digest of the stub named in the entry text)"),
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (fn, why) in CONTROLS.items():
        t = Path(tempfile.mkdtemp(prefix=f"rev-r70-a1ctl-{name}-", dir="/fast/scratch/revenger-r70"))
        archive(t)
        fn(t)
        a = subprocess.run([sys.executable, "-B", str(LANE / "reports/round-70/measure.py"), str(t)], capture_output=True, text=True)
        b = subprocess.run([sys.executable, "-B", str(LANE / "reports/round-70/measure-a1.py"), str(t)], capture_output=True, text=True)
        keep = [l for l in a.stdout.splitlines() if l.startswith(("HOLDS_", "C1_", "SELF_", "EMB_R68", "EMB_PIN"))]
        (OUT / f"{name}.log").write_text(
            f"# control {name}: {why}\n# base {BASE}\n$ python3 -B reports/round-70/measure.py <tree>\n" + "\n".join(keep) + f"\nEXIT={a.returncode}\n"
            f"$ python3 -B reports/round-70/measure-a1.py <tree>\n{b.stdout}EXIT={b.returncode}\n" + (b.stderr[-400:] if b.stderr.strip() else ""), encoding="utf-8")
        print(name, [l for l in a.stdout.splitlines() if l.startswith("HOLDS_C")], [l for l in b.stdout.splitlines() if re.match(r"A1_C\d=", l)])
        shutil.rmtree(t, ignore_errors=True)


if __name__ == "__main__":
    main()
