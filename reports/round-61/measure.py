#!/usr/bin/env python3
"""Round-61 counting probe (pre-registered in reports/round-61/claims.md).

Usage: python3 -B reports/round-61/measure.py TREE
TREE is an extracted `git archive <commit> corpus` tree (it must contain
corpus/). The probe never writes inside TREE: every mutant runs in a fresh
temporary copy. Exit 0 means the probe ran; read the printed values.
Exit 2 means could-not-evaluate (a mutant site did not match exactly once).
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

TREE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else None
if TREE is None or not (TREE / "corpus").is_dir():
    sys.exit("usage: measure.py TREE (TREE/corpus must exist)")

# C1 coverage-K: held coverage-map rows (same regex as SCORECARD.md:133).
readme = (TREE / "corpus/README.md").read_text(encoding="utf-8")
rows = [l for l in readme.splitlines() if re.match(r"^\| C[0-9]+ ", l)]
held = [l for l in rows if re.search(r"\| held \|$", l)]
print(f"K_HELD={len(held)}/{len(rows)} score={10 * len(held) / len(rows):.1f}")
for row_id in ("C04", "C09"):
    line = next((l for l in rows if l.startswith(f"| {row_id} ")), "")
    print(f"K_ROW {row_id} status={line.rsplit('|', 2)[-2].strip() if line else 'absent'}")

# C2 calibration: receipt-command mutant (kaika mutant b) and data forgery d2.
SCRIPTS = {"verify_icon_languages.py": 47, "verify_multi_icon_states.py": 42}
CLAUSE = re.compile(r"receipt\[['\"]command['\"]\]\s*==\s*(?:command|f'[^']*')")


def mutate_b(text):
    """Delete the one conjunct comparing receipt['command'] (and its `and`)."""
    hits = CLAUSE.findall(text)
    if len(hits) != 1:
        return None
    for pattern in (r"\s*and\s+" + CLAUSE.pattern, CLAUSE.pattern + r"\s+and\s+"):
        out, n = re.subn(pattern, "", text, count=1)
        if n == 1:
            return out
    return None


def run(tree, script):
    proc = subprocess.run([sys.executable, "-B", str(tree / "corpus" / script), "--self-test"],
                          cwd="/", capture_output=True, text=True, timeout=300)
    tail = (proc.stdout + proc.stderr).strip().splitlines()
    return proc.returncode, tail[-1] if tail else ""


killed_b = killed_d2 = controls = 0
evaluable = True
for script, round_id in SCRIPTS.items():
    for variant in ("control", "b", "d2"):
        with tempfile.TemporaryDirectory(prefix="rev-r61-mut-") as tmp:
            work = pathlib.Path(tmp)
            shutil.copytree(TREE / "corpus", work / "corpus", symlinks=True)
            target = work / "corpus" / script
            if variant == "b":
                mutated = mutate_b(target.read_text(encoding="utf-8"))
                if mutated is None:
                    print(f"MUTANT {script} b could-not-evaluate (clause match count != 1)")
                    evaluable = False
                    continue
                target.write_text(mutated, encoding="utf-8")
            elif variant == "d2":
                receipt = work / f"corpus/live/runs/round-{round_id}/producer-receipt.json"
                data = json.loads(receipt.read_text())
                data["command"] += " --forged"
                receipt.write_text(json.dumps(data, indent=2) + "\n")
            rc, last = run(work, script)
            state = "pass" if rc == 0 else "killed"
            print(f"MUTANT {script} {variant} exit={rc} {state} :: {last[:160]}")
            if variant == "control":
                controls += rc == 0
            elif variant == "b":
                killed_b += rc != 0
            else:
                killed_d2 += rc != 0
print(f"C2_CONTROLS_PASS={controls}/2")
print(f"C2_RECEIPT_B_KILLED={killed_b}/2")
print(f"C2_D2_KILLED={killed_d2}/2")

# Hold: SCORECARD.md command C (calibration subset and replay census), cwd TREE.
ps = sorted((TREE / "corpus").glob("verify_*.py"))
results = [(p.name, subprocess.run([sys.executable, "-B", str(p), "--self-test"], cwd=TREE,
                                   capture_output=True, text=True, timeout=300)) for p in ps]
names = {"verify_icon_states.py", "verify_multi_icon_states.py",
         "verify_icon_languages.py", "verify_named_multi_icon_states.py"}
for name, r in results:
    tail = (r.stdout + r.stderr).strip().splitlines()
    print("HOLD", name, f"exit={r.returncode}", (tail[-1] if tail else "")[:160])
ok = sum(r.returncode == 0 for name, r in results if name in names)
print(f"HOLD_CALIBRATION={ok}/{len(names)}")
print(f"HOLD_REPLAY={sum(r.returncode == 0 for _, r in results)}/{len(results)}")
sys.exit(0 if evaluable else 2)
