#!/usr/bin/env python3
"""Round-66 counting probe (frozen in reports/round-66/claims.md).

Extends the round-65 probe (whose file and pinned SHA are untouched) with:
  C1  C05 adjudication-disposition labels: K_ROW C05 status (frozen r65
      order's either-way flip; r66 adjudicates the dispatched wave's
      Q02/Q06/Q11 FAILs -> frontier to uncovered) + C05_REJECTED_MARKED
      (the retained candidate carries `admission-status: rejected`)
  C2  calibration target: C6_RECEIPT_KILLED_ATTRIBUTED
      (attributed forged-receipt kills on the exit_code and
      fixture_sha256 conjuncts of receipt_ok, 2 conjuncts x 2 scripts)
New additive hold: HOLDS_OK_V4 (V3 formula ^ C6 attributed 4/4).
All round-65 labels and formulas are byte-identical in semantics.
Exit semantics identical to the round-65 probe: 2 = not evaluable,
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

# C1 coverage-K: held coverage-map rows (same regex as round 64).
readme = (TREE / "corpus/README.md").read_text(encoding="utf-8")
rows = [l for l in readme.splitlines() if re.match(r"^\| C[0-9]+ ", l)]
held = [l for l in rows if re.search(r"\| held \|$", l)]
print(f"K_HELD={len(held)}/{len(rows)} score={10 * len(held) / len(rows):.1f}")
for row_id in ("C05", "C07"):
    line = next((l for l in rows if l.startswith(f"| {row_id} ")), "")
    print(f"K_ROW {row_id} status={line.rsplit('|', 2)[-2].strip() if line else 'absent'}")
backed = [l for l in held if re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3])
          and all((TREE / "corpus" / p).is_file() for p in re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3]))]
print(f"K_HELD_BACKED={len(backed)}/{len(rows)}")

# C1 disposition (round-66): the retained round-65 C05 candidate carries the
# rejected marker (whole-file scan, same predicate as rejected_marked below).
c05_cand = TREE / "corpus/knowledge/round-65-apk-axml-byte-evidence.md"
c05_rejected = (c05_cand.is_file()
                and "admission-status: rejected" in c05_cand.read_text(
                    encoding="utf-8", errors="ignore"))
print(f"C05_REJECTED_MARKED={'yes' if c05_rejected else 'no'}")

# Round-65 registered counter repair: whole-file rejected-marker scan.
# The round-64 probe read only [:2000]; retained candidates mark at 859/712,
# so current counts are window-independent; the self-test proves the repair.
def rejected_marked(rel):
    p = TREE / "corpus" / rel
    try:
        return "admission-status: rejected" in p.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return False

strict = [l for l in held
          if re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3])
          and all((TREE / "corpus" / p).is_file() for p in re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3]))
          and not any(rejected_marked(p) for p in re.findall(r"knowledge/[\w.-]+\.md", l.split("|")[3]))]
print(f"K_HELD_BACKED_STRICT={len(strict)}/{len(rows)}")

seeded = b"A" * 3000 + b"admission-status: rejected"
old_window_miss = b"admission-status: rejected" not in seeded[:2000]
new_window_hit = b"admission-status: rejected" in seeded
selftest = old_window_miss and new_window_hit
print(f"STRICT_REJECT_WINDOW_SELFTEST={'pass' if selftest else 'fail'} old_window_miss={old_window_miss}")

# v2 routed-counter fix: legend token vs observed evidence (M36; same sentence as claims.md).
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
        with tempfile.TemporaryDirectory(prefix="rev-r65-mut-") as tmp:
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
        with tempfile.TemporaryDirectory(prefix="rev-r65-c3-") as tmp:
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

# C4 calibration hold: attributed forged-receipt kill on the stdout_sha256
# conjunct of receipt_ok (round-64 claim, frozen).
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
        with tempfile.TemporaryDirectory(prefix="rev-r65-c4-") as tmp:
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

# C5 calibration target: attributed forged-receipt kill on the evidence_id
# conjunct of receipt_ok (round-65 claim; transplant of a REAL FOREIGN id).
C5_CLAUSE = re.compile(r"receipt\['evidence_id'\]\s*==\s*evidence_id")
C5_SCRIPTS = ("verify_icon_languages.py", "verify_multi_icon_states.py")
C5_MARKER = "forged receipt evidence accepted"


def mutate_c5(text):
    hits = C5_CLAUSE.findall(text)
    if len(hits) != 1:
        return None
    for pattern in (r"\s*and\s+" + C5_CLAUSE.pattern, C5_CLAUSE.pattern + r"\s+and\s+"):
        out, n = re.subn(pattern, "", text, count=1)
        if n == 1:
            return out
    return None


c5_present = c5_controls = c5_killed = c5_attributed = 0
for script in C5_SCRIPTS:
    src = (TREE / "corpus" / script).read_text(encoding="utf-8")
    present = C5_MARKER in src
    c5_present += present
    print(f"C5_CONTROL_PRESENT_{script}={'yes' if present else 'no'}")
    for variant in ("control", "c5"):
        with tempfile.TemporaryDirectory(prefix="rev-r65-c5-") as tmp:
            work = pathlib.Path(tmp)
            shutil.copytree(TREE / "corpus", work / "corpus", symlinks=True)
            target = work / "corpus" / script
            if variant == "c5":
                mutated = mutate_c5(target.read_text(encoding="utf-8"))
                if mutated is None:
                    print(f"MUTANT {script} c5 could-not-evaluate (clause match count != 1)")
                    evaluable = False
                    continue
                target.write_text(mutated, encoding="utf-8")
            rc, last = run(work, script)
            state = "pass" if rc == 0 else "killed"
            print(f"MUTANT {script} {variant} exit={rc} {state} :: {last[:160]}")
            if variant == "control":
                c5_controls += rc == 0
            else:
                c5_killed += rc != 0
                c5_attributed += rc != 0 and last.endswith(C5_MARKER)
print(f"C5_CONTROL_PRESENT={c5_present}/2")
print(f"C5_CONTROLS_PASS={c5_controls}/2")
print(f"C5_RECEIPT_KILLED={c5_killed}/2")
print(f"C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED={c5_attributed}/2")


# C6 calibration target (round-66): attributed forged-receipt kills on the
# exit_code and fixture_sha256 conjuncts of receipt_ok — the last two
# unguarded conjuncts (R64ReviewSeparability; round-65 planned line).
# 2 conjuncts x 2 scripts = 4 cells.
C6_CLAUSES = {
    "exit": (re.compile(r"receipt\['exit_code'\]\s*==\s*0"),
             "forged receipt exit accepted"),
    "fixture": (re.compile(r"receipt\['fixture_sha256'\]\s*==\s*expected_hash"),
                "forged receipt fixture accepted"),
}
C6_SCRIPTS = ("verify_icon_languages.py", "verify_multi_icon_states.py")


def mutate_c6(text, clause):
    hits = clause.findall(text)
    if len(hits) != 1:
        return None
    for pattern in (r"\s*and\s+" + clause.pattern, clause.pattern + r"\s+and\s+"):
        out, n = re.subn(pattern, "", text, count=1)
        if n == 1:
            return out
    return None


c6_present = c6_controls = c6_killed = c6_attributed = 0
for script in C6_SCRIPTS:
    src = (TREE / "corpus" / script).read_text(encoding="utf-8")
    for cname, (clause, marker) in C6_CLAUSES.items():
        present = marker in src
        c6_present += present
        print(f"C6_CONTROL_PRESENT_{script}_{cname}={'yes' if present else 'no'}")
        for variant in ("control", cname):
            with tempfile.TemporaryDirectory(prefix="rev-r66-c6-") as tmp:
                work = pathlib.Path(tmp)
                shutil.copytree(TREE / "corpus", work / "corpus", symlinks=True)
                target = work / "corpus" / script
                if variant == cname:
                    mutated = mutate_c6(target.read_text(encoding="utf-8"), clause)
                    if mutated is None:
                        print(f"MUTANT {script} c6-{cname} could-not-evaluate (clause match count != 1)")
                        evaluable = False
                        continue
                    target.write_text(mutated, encoding="utf-8")
                rc, last = run(work, script)
                state = "pass" if rc == 0 else "killed"
                print(f"MUTANT {script} c6-{variant} exit={rc} {state} :: {last[:160]}")
                if variant == "control":
                    c6_controls += rc == 0
                else:
                    c6_killed += rc != 0
                    c6_attributed += rc != 0 and last.endswith(marker)
print(f"C6_CONTROL_PRESENT={c6_present}/4")
print(f"C6_CONTROLS_PASS={c6_controls}/4")
print(f"C6_RECEIPT_KILLED={c6_killed}/4")
print(f"C6_RECEIPT_KILLED_ATTRIBUTED={c6_attributed}/4")

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
holds_ok_v3 = holds_ok_v2 and c5_attributed == 2 and selftest
print(f"HOLDS_OK_V3={'yes' if holds_ok_v3 else 'no'}")
holds_ok_v4 = holds_ok_v3 and c6_attributed == 4
print(f"HOLDS_OK_V4={'yes' if holds_ok_v4 else 'no'}")
sys.exit(2 if not evaluable else 0 if holds_ok else 1)
