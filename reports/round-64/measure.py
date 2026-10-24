#!/usr/bin/env python3
"""Round-64 counting probe (frozen in reports/round-64/claims.md).

Extends the round-63 probe (whose file and pinned SHA are untouched) with:
  C1  coverage K target rows (same frozen regexes as round 63) + K_ROW C07
  C2  calibration target: C4_RECEIPT_KILLED_ATTRIBUTED (M35 routed debt)
  v2  routed-counter fixes (diagnostic labels; frozen labels unchanged):
      K_HELD_BACKED_STRICT, README_TOKEN_LEGEND_MISMATCH, HOLDS_OK_V2
Exit semantics identical to the round-63 probe: 2 = not evaluable,
0 = holds_ok (round-63 semantics), 1 = a frozen hold failed.
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
for row_id in ("C07",):
    line = next((l for l in rows if l.startswith(f"| {row_id} ")), "")
    print(f"K_ROW {row_id} status={line.rsplit('|', 2)[-2].strip() if line else 'absent'}")
backed = [l for l in held if re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3])
          and all((TREE / "corpus" / p).is_file() for p in re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3]))]
print(f"K_HELD_BACKED={len(backed)}/{len(rows)}")

# v2 routed-counter fix: cited entries marked admission-status: rejected do not back a row.
def rejected_marked(rel):
    p = TREE / "corpus" / rel
    try:
        return "admission-status: rejected" in p.read_text(encoding="utf-8", errors="ignore")[:2000]
    except OSError:
        return False

strict = [l for l in held
          if re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3])
          and all((TREE / "corpus" / p).is_file() for p in re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3]))
          and not any(rejected_marked(p) for p in re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3]))]
print(f"K_HELD_BACKED_STRICT={len(strict)}/{len(rows)}")

# v2 routed-counter fix: legend token vs observed evidence (M36; same sentence as claims.md).
# Surface-scoped rule: a row at `frontier` contradicts the legend ("no knowledge
# and no saved record") iff >=1 saved record exists for that row's own surface
# operations (frozen ROW_OPS map, printed below for enumerability).
ROW_OPS = {
    "C03": {"inspect_managed_artifact"},
    "C05": {"inspect_android_package"},
    "C07": {"inspect_firmware_regions"},
    "C08": {"inspect_web_page", "capture_browser_scenario", "observe_web_session"},
}
record_ops = set()
saved_records = 0
for p in (TREE / "corpus/live/runs").rglob("*.json"):
    try:
        x = json.loads(p.read_bytes())
    except (ValueError, UnicodeError):
        continue
    if isinstance(x, dict) and x.get("operation"):
        saved_records += 1
        record_ops.add(x["operation"])
mismatch = []
for l in rows:
    cols = [c.strip() for c in l.strip().strip("|").split("|")]
    if cols and cols[-1] == "frontier" and ROW_OPS.get(cols[0], set()) & record_ops:
        mismatch.append(cols[0])
print(f"SAVED_RECORDS={saved_records}")
print(f"ROW_OPS={ {k: sorted(v) for k, v in ROW_OPS.items()} }")
print(f"README_TOKEN_LEGEND_MISMATCH={len(mismatch)} rows={mismatch}")

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

# Freshness hold: stored assertion rows still present (byte survival, not current-host truth).
fresh = 0
for rel in ("corpus/knowledge/seed.md", "corpus/knowledge/2026-10-12-rea-readiness-checklist.md"):
    text = (TREE / rel).read_text(encoding="utf-8") if (TREE / rel).is_file() else ""
    fresh += sum(1 for l in text.splitlines() if re.match(r"^\| [FK][0-9]+ .*\| (holds|STALE)", l))
print(f"FRESH_ROWS={fresh}/18")

evaluable = True


def run(tree, script):
    proc = subprocess.run([sys.executable, "-B", str(tree / "corpus" / script), "--self-test"],
                          cwd=tree, capture_output=True, text=True, timeout=300)
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
        with tempfile.TemporaryDirectory(prefix="rev-r64-mut-") as tmp:
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

# C3 calibration hold: attributed forged-receipt kill (round-63 claim, frozen).
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
        with tempfile.TemporaryDirectory(prefix="rev-r64-c3-") as tmp:
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

# C4 calibration target: attributed forged-receipt kill on the stdout_sha256
# conjunct of receipt_ok in the two M35 scripts (round-64 claim).
C4_CLAUSE = re.compile(r"receipt\['stdout_sha256'\]\s*==\s*H\(raw_bytes\)")
C4_SCRIPTS = ("verify_icon_languages.py", "verify_multi_icon_states.py")


def mutate_c4(text):
    hits = C4_CLAUSE.findall(text)
    if len(hits) != 1:
        return None
    for pattern in (r"\s*and\s+" + C4_CLAUSE.pattern, C4_CLAUSE.pattern + r"\s+and\s+"):
        out, n = re.subn(pattern, "", text, count=1)
        if n == 1:
            return out
    return None


c4_controls = c4_attributed = 0
for script in C4_SCRIPTS:
    for variant in ("control", "c4"):
        with tempfile.TemporaryDirectory(prefix="rev-r64-c4-") as tmp:
            work = pathlib.Path(tmp)
            shutil.copytree(TREE / "corpus", work / "corpus", symlinks=True)
            target = work / "corpus" / script
            if variant == "c4":
                mutated = mutate_c4(target.read_text(encoding="utf-8"))
                if mutated is None:
                    print(f"MUTANT {script} c4 could-not-evaluate (clause match count != 1)")
                    evaluable = False
                    continue
                target.write_text(mutated, encoding="utf-8")
            rc, last = run(work, script)
            state = "pass" if rc == 0 else "killed"
            print(f"MUTANT {script} {variant} exit={rc} {state} :: {last[:160]}")
            if variant == "control":
                c4_controls += rc == 0
            else:
                c4_attributed += rc != 0 and last.endswith("forged receipt stdout accepted")
print(f"C4_CONTROLS_PASS={c4_controls}/2")
print(f"C4_RECEIPT_KILLED_ATTRIBUTED={c4_attributed}/2")

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
holds_ok_v2 = (controls == 2 and killed_d2 == 2 and c3_controls == 2
               and attributed_b == 2 and c3_attributed == 2 and c4_attributed == 2
               and ok == len(names) and replay == len(results) and fresh == 18
               and len(mismatch) == 0)
print(f"HOLDS_OK_V2={'yes' if holds_ok_v2 else 'no'}")
sys.exit(2 if not evaluable else 0 if holds_ok else 1)
