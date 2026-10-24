#!/usr/bin/env python3
"""Round-63 counting probe (frozen in reports/round-63/claims.md).

Usage: python3 -B reports/round-63/measure.py TREE
TREE is an extracted `git archive <commit> corpus` tree (it must contain
corpus/). The probe never writes inside TREE: every mutant runs in a fresh
temporary copy. Exit 0 means the probe ran and holds pass; read the printed
values. Exit 1 means a hold failed. Exit 2 means could-not-evaluate (a mutant
site did not match exactly once).
"""
import collections
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

# C1 coverage-K: held coverage-map rows (same regex as SCORECARD.md).
readme = (TREE / "corpus/README.md").read_text(encoding="utf-8")
rows = [l for l in readme.splitlines() if re.match(r"^\| C[0-9]+ ", l)]
held = [l for l in rows if re.search(r"\| held \|$", l)]
print(f"K_HELD={len(held)}/{len(rows)} score={10 * len(held) / len(rows):.1f}")
for row_id in ("C06",):
    line = next((l for l in rows if l.startswith(f"| {row_id} ")), "")
    print(f"K_ROW {row_id} status={line.rsplit('|', 2)[-2].strip() if line else 'absent'}")
backed = [l for l in held if re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3])
          and all((TREE / "corpus" / p).is_file() for p in re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3]))]
print(f"K_HELD_BACKED={len(backed)}/{len(rows)}")

# C2 coverage-F: selected-family saved-record presence (SCORECARD.md command F).
counter = collections.Counter()
for p in sorted((TREE / "corpus/live/runs").rglob("*.json")):
    try:
        x = json.loads(p.read_bytes())
    except (ValueError, UnicodeError):
        continue
    if isinstance(x, dict) and x.get("evidence_id") and x.get("normalized_result") is not None:
        counter[x.get("operation", "unknown")] += 1
families = {"native-static": {"inspect_pe_resources"}, "managed": {"inspect_managed_artifact"},
            "javascript": {"analyze_javascript_application"}, "android": {"inspect_android_package"},
            "archives": {"inventory_artifact", "inspect_artifact"}, "firmware": {"inspect_firmware_regions"},
            "browser-runtime": {"inspect_web_page", "capture_browser_scenario", "observe_web_session"},
            "evm": {"inspect_evm_interface"}}
present = [k for k, v in families.items() if v.intersection(counter)]
print(dict(sorted(counter.items())))
print(f"F_COVERAGE={len(present)}/{len(families)} score={10 * len(present) / len(families):.1f}")
print(f"F_FAMILIES={present}")

# Freshness hold: stored assertion rows still present (SCORECARD.md command).
fresh = 0
for rel in ("corpus/knowledge/seed.md", "corpus/knowledge/2026-10-12-rea-readiness-checklist.md"):
    text = (TREE / rel).read_text(encoding="utf-8") if (TREE / rel).is_file() else ""
    fresh += sum(1 for l in text.splitlines() if re.match(r"^\| [FK][0-9]+ .*\| (holds|STALE)", l))
print(f"FRESH_ROWS={fresh}/18")

evaluable = True


def run(tree, script):
    proc = subprocess.run([sys.executable, "-B", str(tree / "corpus" / script), "--self-test"],
                          cwd="/", capture_output=True, text=True, timeout=300)
    tail = (proc.stdout + proc.stderr).strip().splitlines()
    return proc.returncode, tail[-1] if tail else ""


# C2 calibration hold: receipt-command mutant (kaika mutant b) and data forgery d2.
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


killed_b = killed_d2 = controls = 0
attributed_b = 0
for script, round_id in SCRIPTS.items():
    for variant in ("control", "b", "d2"):
        with tempfile.TemporaryDirectory(prefix="rev-r63-mut-") as tmp:
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
                attributed_b += rc != 0 and last.endswith("forged receipt command accepted")
            else:
                killed_d2 += rc != 0
print(f"C2_CONTROLS_PASS={controls}/2")
print(f"C2_RECEIPT_B_KILLED={killed_b}/2")
print(f"C2_D2_KILLED={killed_d2}/2")
print(f"C2_RECEIPT_B_KILLED_ATTRIBUTED={attributed_b}/2")

# C3 calibration: attributed forged-receipt kill on the two remaining verifiers.
C3_SCRIPTS = {
    "verify_named_multi_icon_states.py": re.compile(r"receipt\['command'\]==command"),
    "verify_icon_states.py": re.compile(r"receipt\['fixture_sha256'\]\s*==\s*expected_hash"),
}


def mutate_c3(text, clause):
    hits = clause.findall(text)
    if len(hits) != 1:
        return None
    for pattern in (r"\s*and\s+" + clause.pattern, clause.pattern + r"\s+and\s+"):
        out, n = re.subn(pattern, "", text, count=1)
        if n == 1:
            return out
    return None


c3_controls = c3_attributed = 0
for script, clause in C3_SCRIPTS.items():
    for variant in ("control", "c3"):
        with tempfile.TemporaryDirectory(prefix="rev-r63-c3-") as tmp:
            work = pathlib.Path(tmp)
            shutil.copytree(TREE / "corpus", work / "corpus", symlinks=True)
            target = work / "corpus" / script
            if variant == "c3":
                mutated = mutate_c3(target.read_text(encoding="utf-8"), clause)
                if mutated is None:
                    print(f"MUTANT {script} c3 could-not-evaluate (clause match count != 1)")
                    evaluable = False
                    continue
                target.write_text(mutated, encoding="utf-8")
            rc, last = run(work, script)
            state = "pass" if rc == 0 else "killed"
            print(f"MUTANT {script} {variant} exit={rc} {state} :: {last[:160]}")
            if variant == "control":
                c3_controls += rc == 0
            else:
                c3_attributed += rc != 0 and "forged receipt" in last.lower()
print(f"C3_CONTROLS_PASS={c3_controls}/2")
print(f"C3_RECEIPT_KILLED_ATTRIBUTED={c3_attributed}/2")

# Hold: calibration subset and replay census, cwd TREE.
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
replay = sum(r.returncode == 0 for _, r in results)
print(f"HOLD_REPLAY={replay}/{len(results)}")
holds_ok = (controls == 2 and killed_d2 == 2 and c3_controls == 2
            and killed_b == 2 and ok == len(names) and replay == len(results)
            and fresh == 18)
print(f"HOLDS_OK={'yes' if holds_ok else 'no'}")
sys.exit(2 if not evaluable else 0 if holds_ok else 1)
