#!/usr/bin/env python3
"""Round-70 amendment A1 (TIGHTEN-ONLY; declared before any wave-2 seat scored).

Why: the wave-1 seat R70W1ControlAudit showed that the frozen predicates `HOLDS_C1_V5`,
`HOLDS_C2_V5` and `HOLDS_C3_V1` print `yes` on trees that perform none of the claimed work
(a 17-block echo entry; a 27-line checker keyed to the counter's own fixture literals; a pin
that points at an echo stub). `reports/round-70/claims.md` already says a counter-only pass is
not admission; A1 closes the three reachable controls mechanically. It adds conjuncts to the
claims and never removes or loosens one: a claim now needs its frozen label AND its A1 label.

Usage: python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-70/measure-a1.py TREE
(TREE as for measure.py). Exit 0 iff all three A1 labels are `yes`, 1 if a label is `no`,
2 if the script itself could not evaluate.

  A1_C1  the v5 entry runs >= 17 DISTINCT commands, every one a script of the three the entry
         is about (readout.py, entry_checks.py, derive_axml_anchors.py), reproduces all 15
         lines of the real readout stdout verbatim, and cites >= 5 `source:` rows that exist
         in corpus/SOURCES.md at tier A.
  A1_C2  the tree's checker reproduces the documented before-vector on the claim base tree
         (SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0, SELF_MISMATCH=9) AND scores six freshly
         randomised single-defect variants and a clean variant exactly (values are drawn per run,
         so a literal-matching checker cannot pass).
  A1_C3  embedded_output_pins.json binds the round-68 entry's derivation command to
         corpus/derive_axml_anchors_r68.py with the S046 digest, and that script, run in the tree,
         prints >= 17 lines including the snapshot-digest line.
"""
import hashlib
import json
import random
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
BASE_COMMIT = "3f5edbc206351232a3d2d801334dd930499ccaf5"
S046 = "bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249"
SCRIPTS = {"corpus/fixtures/apk-r65/readout.py", "corpus/fixtures/apk-r65/entry_checks.py",
           "corpus/derive_axml_anchors.py"}
V5 = "corpus/knowledge/round-70-apk-axml-byte-evidence.md"


def py(tree, args, cwd=None):
    p = subprocess.run([sys.executable, "-B", *args], cwd=str(cwd or tree), capture_output=True, text=True, timeout=300)
    return p.returncode, p.stdout


def commands(text):
    out, fenced = [], False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            fenced = not fenced
        elif fenced and line.startswith("$ "):
            out.append(line[2:].strip())
    return out


def a1_c1(tree):
    f = tree / V5
    if not f.is_file():
        print("A1_C1_DETAIL=no v5 entry")
        return False
    text = f.read_text(encoding="utf-8", errors="ignore")
    cmds = commands(text)
    distinct = set(cmds)
    scripts_ok = all(len(c.split()) > 2 and c.split()[0] == "python3" and
                     next((a for a in c.split()[1:] if not a.startswith("-")), "") in SCRIPTS for c in distinct)
    rc, out = py(tree, ["corpus/fixtures/apk-r65/readout.py"])
    lines = [l for l in out.splitlines() if l.strip()]
    present = sum(1 for l in lines if l in text.splitlines())
    src_ids = set(re.findall(r"^source: (S\d{3,})", text, re.M))
    reg = (tree / "corpus/SOURCES.md").read_text(encoding="utf-8", errors="ignore")
    tier_a = [i for i in src_ids if re.search(rf"^\|\s*{i}\s*\|(?:[^|]*\|){{2}}\s*A\s*\|", reg, re.M)]
    ok = len(distinct) >= 17 and scripts_ok and rc == 0 and len(lines) == 15 and present == 15 and len(tier_a) >= 5
    print(f"A1_C1_DETAIL=distinct_commands={len(distinct)} scripts_allowlisted={scripts_ok} readout_lines={present}/{len(lines)} source_rows_tier_a={len(tier_a)}/{len(src_ids)}")
    return ok


def archive(dest, commit=None):
    if commit:
        subprocess.run(f"git -C {LANE} archive {commit} corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C {dest}",
                       shell=True, check=True)


def variant(root, rnd, **defect):
    """Independent, randomised fixture: every literal differs per run."""
    n = rnd.randint(5, 9)
    (root / "corpus/fixtures").mkdir(parents=True)
    (root / "corpus/fixtures/f.txt").write_text("f", encoding="utf-8")
    tool = f"t_{rnd.randrange(16**5):05x}.py"
    (root / "corpus" / tool).write_text("print(1)\n", encoding="utf-8")
    (root / "corpus/verify_v.py").write_text("print(1)\n", encoding="utf-8")
    if defect.get("SM2"):
        (root / "corpus" / f"u_{rnd.randrange(16**5):05x}.py").write_text("print(2)\n", encoding="utf-8")
    (root / "corpus/QUALITY.md").write_text("| id |\n|---|\n" + "".join(f"| Q{i:02d} | x |\n" for i in range(1, n + 1)), encoding="utf-8")
    claimed = n - 1 if defect.get("SM1") else n
    held = rnd.randint(6, 9)
    rows = "".join(f"| C{i:02d} | s | k | w | {'held' if i <= held else 'frontier'} |\n" for i in range(1, 15))
    (root / "corpus/README.md").write_text(
        f"- `QUALITY.md` — admission criteria Q01–Q{claimed:02d}\n- `{tool}`\n- `fixtures/`\n- `verify_*.py`\n" + rows, encoding="utf-8")
    body = bytes(rnd.randrange(97, 123) for _ in range(rnd.randint(1200, 6000)))
    (root / "SKILL.md").write_bytes(body)
    size = len(body) + rnd.randint(3, 900) if defect.get("SM3") else len(body)
    who = f"revenger-r{rnd.randint(10, 99)}.R{rnd.randint(10, 99)}Rev{rnd.randrange(16**3):03x}" if defect.get("SM4") else "Pat Q. Outsider"
    (root / "SHONEN.md").write_text(
        f"- [x] Landed `SKILL.md` ({size} bytes, sha256 `{hashlib.sha256(body).hexdigest()[:rnd.randint(10, 20)]}…`).\n"
        f"  Named non-author verifier: {who}.\n", encoding="utf-8")
    cite = "".join(rnd.choice("0123456789abcdef") for _ in range(rnd.randint(9, 12))) if defect.get("SM5") else BASE_COMMIT[:rnd.randint(9, 12)]
    kk = held + 1 if defect.get("SM6") else held
    (root / "SCORECARD.md").write_text(f"## Round 61 x\nPre-registration `{cite}` ok.\nK_HELD_BACKED {kk}/14\n", encoding="utf-8")


def a1_c2(tree, tmp):
    if not (tree / "corpus/self_assessment_check.py").is_file():
        print("A1_C2_DETAIL=no checker")
        return False
    base = Path(tempfile.mkdtemp(dir=tmp))
    archive(base, BASE_COMMIT)
    rc, out = py(tree, ["corpus/self_assessment_check.py", "--root", str(base), "--lane", str(LANE)])
    got = dict(re.findall(r"(SM\d)=(\d+)", out))
    vector = got == {"SM1": "1", "SM2": "4", "SM3": "2", "SM4": "1", "SM5": "1", "SM6": "0"} and "SELF_MISMATCH=9" in out
    rnd = random.Random()
    ok_variants = 0
    d = Path(tempfile.mkdtemp(dir=tmp))
    variant(d, rnd)
    rc, out = py(tree, ["corpus/self_assessment_check.py", "--root", str(d), "--lane", str(LANE)])
    clean = rc == 0 and "SELF_MISMATCH=0" in out
    for cls in ("SM1", "SM2", "SM3", "SM4", "SM5", "SM6"):
        d = Path(tempfile.mkdtemp(dir=tmp))
        variant(d, rnd, **{cls: True})
        rc, out = py(tree, ["corpus/self_assessment_check.py", "--root", str(d), "--lane", str(LANE)])
        per = dict(re.findall(r"(SM\d)=(\d+)", out))
        ok_variants += rc == 1 and per.get(cls) == "1" and "SELF_MISMATCH=1" in out
    print(f"A1_C2_DETAIL=base_vector={'yes' if vector else 'no'} clean_variant={'yes' if clean else 'no'} defect_variants={ok_variants}/6")
    return vector and clean and ok_variants == 6


def a1_c3(tree):
    pins = tree / "corpus/embedded_output_pins.json"
    if not pins.is_file():
        print("A1_C3_DETAIL=no pin file")
        return False
    spec = json.loads(pins.read_text(encoding="utf-8")).get("round-68-apk-axml-byte-evidence.md", {})
    pin = spec.get("corpus/derive_axml_anchors.py", {})
    binds = pin.get("use") == "corpus/derive_axml_anchors_r68.py" and pin.get("sha256") == S046
    target = tree / "corpus/derive_axml_anchors_r68.py"
    digest = target.is_file() and hashlib.sha256(target.read_bytes()).hexdigest() == S046
    rc, out = py(tree, ["corpus/derive_axml_anchors_r68.py"]) if target.is_file() else (2, "")
    lines = out.splitlines()
    prints = rc == 0 and len(lines) >= 17 and any(l.startswith("sha256 56b88bc4") for l in lines)
    print(f"A1_C3_DETAIL=binds_s046={'yes' if binds else 'no'} script_digest={'yes' if digest else 'no'} script_prints_{len(lines)}_lines={'yes' if prints else 'no'}")
    return binds and digest and prints


def main(tree):
    tmp = Path(tempfile.mkdtemp(prefix="rev-r70-a1-"))
    try:
        r = {"A1_C1": a1_c1(tree), "A1_C2": a1_c2(tree, tmp), "A1_C3": a1_c3(tree)}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    for k, v in r.items():
        print(f"{k}={'yes' if v else 'no'}")
    return 0 if all(r.values()) else 1


if __name__ == "__main__":
    a = sys.argv[1:]
    if len(a) != 1 or not (Path(a[0]).resolve() / "corpus").is_dir():
        print("usage: measure-a1.py TREE")
        sys.exit(2)
    try:
        sys.exit(main(Path(a[0]).resolve()))
    except SystemExit:
        raise
    except BaseException:
        traceback.print_exc()
        print("COUNTER_ERROR=uncaught exception (exit 2)")
        sys.exit(2)
