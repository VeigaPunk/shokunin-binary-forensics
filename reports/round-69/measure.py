#!/usr/bin/env python3
"""Round-67 counting probe (frozen in reports/round-67/claims.md).

Extends the round-66 probe (whose file and pinned SHA are untouched) with:
  C1  v2-candidate disposition labels (same regex family as r65/r66): the C05
      row must name exactly one knowledge entry (the round-67 v2 candidate)
      when held; K_ROW C05 + K_HELD_BACKED(_STRICT) read the either-way flip.
  C2  calibration target: C7 embedded-output verbatim gate
      (corpus/check_embedded_outputs.py, outside the verify_* replay family):
      GATE_PRESENT / SELFTEST / CONTROL_PASS / MUTANT_KILLED_ATTRIBUTED /
      RED_ON_R65_CANDIDATE / V2_CLEAN, plus HOLDS_OK_V5 = V4 ^ C7 targets.
  C1  round-68 additions: C7_NEG_SPOOF_KILLED / C7_NEG_SPOOF_KILLED_ATTRIBUTED
      (the frozen mutant with the marker TEXT spoofed: killed but not
      attributable, so the attribution rule reads 0/1 and cannot be satisfied
      by any non-zero exit), C7_V3_CLEAN (the round-68 candidate is clean
      under the repaired gate), C05_SINGLE_V3 and HOLDS_C2_V3 (the coverage
      aggregate), plus HOLDS_OK_V6 = V5 ^ the C7 negative control.
All round-66 and round-67 labels and formulas are byte-identical in semantics.
Exit semantics identical: 2 = not evaluable, 0 = holds_ok, 1 = a hold failed.
"""
import collections
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

LANE = "/home/vgpnk/Projects/shokunin/revenger-shokunin"

TREE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else None
if TREE is None or not (TREE / "corpus").is_dir():
    sys.exit("usage: measure.py TREE (TREE/corpus must exist)")

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

c05_cand = TREE / "corpus/knowledge/round-65-apk-axml-byte-evidence.md"
c05_rejected = (c05_cand.is_file()
                and "admission-status: rejected" in c05_cand.read_text(
                    encoding="utf-8", errors="ignore"))
print(f"C05_REJECTED_MARKED={'yes' if c05_rejected else 'no'}")


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

# C1 v2 readout: when C05 is held, its knowledge column must name exactly one
# entry and it must be the round-67 v2 candidate (claims.md frozen predicate).
c05_line = next((l for l in rows if l.startswith("| C05 ")), "")
c05_entries = re.findall(r"knowledge/[\w.-]+\.md", c05_line.split("|")[3]) if c05_line else []
c05_single_v2 = (len(c05_entries) == 1
                 and c05_entries[0] == "knowledge/round-67-apk-axml-byte-evidence.md")
print(f"C05_KNOWLEDGE_COLUMN={' '.join(c05_entries) if c05_entries else '-'}")
print(f"C05_SINGLE_V2={'yes' if c05_single_v2 else 'no'}")
c05_single_v3 = (len(c05_entries) == 1
                 and c05_entries[0] == "knowledge/round-68-apk-axml-byte-evidence.md")
print(f"C05_SINGLE_V3={'yes' if c05_single_v3 else 'no'}")
c05_single_v4 = (len(c05_entries) == 1
                 and c05_entries[0] == "knowledge/round-69-apk-axml-byte-evidence.md")
print(f"C05_SINGLE_V4={'yes' if c05_single_v4 else 'no'}")

seeded = b"A" * 3000 + b"admission-status: rejected"
old_window_miss = b"admission-status: rejected" not in seeded[:2000]
new_window_hit = b"admission-status: rejected" in seeded
selftest_window = old_window_miss and new_window_hit
print(f"STRICT_REJECT_WINDOW_SELFTEST={'pass' if selftest_window else 'fail'} old_window_miss={old_window_miss}")

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

# C2 coverage aggregate (round-68): the C05 row must be held, backed by the
# round-68 candidate alone, with the strict (no rejected candidate) reading
# and no legend mismatch.
c05_row_line = next((l for l in rows if l.startswith("| C05 ")), "")
c05_status = c05_row_line.rsplit("|", 2)[-2].strip() if c05_row_line else "absent"
c2_v3_ok = (len(backed) == 9 and len(strict) == 9 and c05_single_v3
            and c05_status == "held" and len(mismatch) == 0)
print(f"C05_STATUS={c05_status}")
print(f"HOLDS_C2_V3={'yes' if c2_v3_ok else 'no'}")
c2_v4_ok = (len(backed) == 9 and len(strict) == 9 and c05_single_v4
            and c05_status == "held" and len(mismatch) == 0)
print(f"HOLDS_C2_V4={'yes' if c2_v4_ok else 'no'}")

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

fresh = 0
for rel in ("corpus/knowledge/seed.md", "corpus/knowledge/2026-10-12-rea-readiness-checklist.md"):
    text = (TREE / rel).read_text(encoding="utf-8") if (TREE / rel).is_file() else ""
    fresh += sum(1 for l in text.splitlines() if re.match(r"^\| [FK][0-9]+ .*\| (holds|STALE)", l))
print(f"FRESH_ROWS={fresh}/18")

# Q15 calibration target (round-69): the tree-identity criterion.
q15_q = TREE / "corpus/QUALITY.md"
q15_present = q15_q.is_file() and bool(re.search(r"^\| Q15 \|", q15_q.read_text(
    encoding="utf-8", errors="ignore"), re.M))
print(f"Q15_PRESENT={'yes' if q15_present else 'no'}")
q15_check = TREE / "corpus/q15_tree_id_check.py"
if q15_check.is_file():
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
    q15_selftest = rc == 0
    print(f"Q15_SELFTEST={'pass' if q15_selftest else 'fail'} :: {last[:160]}")
    d1 = TREE / "reports/round-69/d1-false-sentence.md"
    if d1.is_file():
        rc, last = run(TREE, "q15_tree_id_check.py", "--scan", "reports/round-69/d1-false-sentence.md",
                       "--lane", LANE)
        q15_false_killed = rc != 0
        print(f"Q15_FALSE_KILLED={'yes' if q15_false_killed else 'no'} exit={rc} :: {last[:160]}")
    else:
        q15_false_killed = False
        print("Q15_FALSE_KILLED=n/a (no d1 fixture)")
    lesson = TREE / "corpus/lessons/round-69.md"
    if lesson.is_file():
        rc, last = run(TREE, "q15_tree_id_check.py", "--scan", "corpus/lessons/round-69.md",
                       "--lane", LANE)
        q15_restate = rc == 0
        print(f"Q15_RESTATE_OK={'yes' if q15_restate else 'no'} exit={rc} :: {last[:160]}")
    else:
        q15_restate = False
        print("Q15_RESTATE_OK=n/a (no round-69 lesson)")
else:
    print("Q15_SELFTEST=n/a (no checker)")
    print("Q15_FALSE_KILLED=n/a (no checker)")
    print("Q15_RESTATE_OK=n/a (no checker)")

evaluable = True


def run(tree, script, *args):
    proc = subprocess.run([sys.executable, "-B", str(tree / "corpus" / script), *args],
                          cwd=tree, capture_output=True, text=True, timeout=300)
    tail = (proc.stdout + proc.stderr).strip().splitlines()
    return proc.returncode, tail[-1] if tail else ""


SCRIPTS = {"verify_icon_languages.py": 47, "verify_multi_icon_states.py": 42}
CLAUSE = re.compile(r"receipt\[['\"]command['\"]\]\s*==\s*(?:command|f'[^']*')")


def mutate_b(text):
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
            rc, last = run(work, script, "--self-test")
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
            rc, last = run(work, script, "--self-test")
            state = "pass" if rc == 0 else "killed"
            print(f"MUTANT {script} {variant} exit={rc} {state} :: {last[:160]}")
            if variant == "control":
                c3_controls += rc == 0
            else:
                c3_attributed += rc != 0 and "forged receipt" in last.lower()
print(f"C3_CONTROLS_PASS={c3_controls}/2")
print(f"C3_RECEIPT_KILLED_ATTRIBUTED={c3_attributed}/2")

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
            rc, last = run(work, script, "--self-test")
            state = "pass" if rc == 0 else "killed"
            print(f"MUTANT {script} {variant} exit={rc} {state} :: {last[:160]}")
            if variant == "control":
                c4_controls += rc == 0
            else:
                c4_attributed += rc != 0 and last.endswith("forged receipt stdout accepted")
print(f"C4_CONTROLS_PASS={c4_controls}/2")
print(f"C4_RECEIPT_KILLED_ATTRIBUTED={c4_attributed}/2")

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
            rc, last = run(work, script, "--self-test")
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
                rc, last = run(work, script, "--self-test")
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

# C7 calibration target (round-67): the embedded-output verbatim gate.
C7_GATE_REL = "check_embedded_outputs.py"
C7_MARKER = "drifted entry output accepted"
C7_CLAUSE = re.compile(r"problems \+= drift\(lines, stdout_set, lineno\)")


def mutate_c7(text):
    hits = C7_CLAUSE.findall(text)
    if len(hits) != 1:
        return None
    return C7_CLAUSE.sub("problems += []  # mutant: verbatim comparison removed", text, count=1)


c7_gate = TREE / "corpus" / C7_GATE_REL
c7_present = c7_gate.is_file()
print(f"C7_GATE_PRESENT={'yes' if c7_present else 'no'}")
c7_selftest_ok = False
c7_control_ok = 0
c7_mut_killed = c7_mut_attributed = 0
c7_red = False
c7_v2_clean = False
c7_v3_clean = False
if c7_present:
    rc, last = run(TREE, C7_GATE_REL, "--self-test")
    c7_selftest_ok = rc == 0
    print(f"C7_SELFTEST={'pass' if c7_selftest_ok else 'fail'} :: {last[:160]}")
    c7_control_ok += c7_selftest_ok and C7_MARKER in c7_gate.read_text(encoding="utf-8")
    for variant in ("control", "c7"):
        with tempfile.TemporaryDirectory(prefix="rev-r67-c7-") as tmp:
            work = pathlib.Path(tmp)
            shutil.copytree(TREE / "corpus", work / "corpus", symlinks=True)
            target = work / "corpus" / C7_GATE_REL
            if variant == "c7":
                mutated = mutate_c7(target.read_text(encoding="utf-8"))
                if mutated is None:
                    print("MUTANT check_embedded_outputs.py c7 could-not-evaluate (clause match count != 1)")
                    evaluable = False
                    continue
                target.write_text(mutated, encoding="utf-8")
            rc, last = run(work, C7_GATE_REL, "--self-test")
            state = "pass" if rc == 0 else "killed"
            print(f"MUTANT check_embedded_outputs.py {variant} exit={rc} {state} :: {last[:160]}")
            if variant == "control":
                pass
            else:
                c7_mut_killed += rc != 0
                c7_mut_attributed += rc != 0 and last.endswith(C7_MARKER)
    rc, last = run(TREE, C7_GATE_REL, "--entry", "corpus/knowledge/round-65-apk-axml-byte-evidence.md")
    c7_red = rc != 0
    print(f"C7_RED_ON_R65_CANDIDATE={'yes' if c7_red else 'no'} exit={rc} :: {last[:160]}")
    v2 = TREE / "corpus/knowledge/round-67-apk-axml-byte-evidence.md"
    if v2.is_file():
        rc, last = run(TREE, C7_GATE_REL, "--entry", "corpus/knowledge/round-67-apk-axml-byte-evidence.md")
        c7_v2_clean = rc == 0
        print(f"C7_V2_CLEAN={'yes' if c7_v2_clean else 'no'} exit={rc} :: {last[:160]}")
    else:
        print("C7_V2_CLEAN=n/a (no v2 file)")
    v3 = TREE / "corpus/knowledge/round-68-apk-axml-byte-evidence.md"
    if v3.is_file():
        rc, last = run(TREE, C7_GATE_REL, "--entry",
                       "corpus/knowledge/round-68-apk-axml-byte-evidence.md")
        c7_v3_clean = rc == 0
        print(f"C7_V3_CLEAN={'yes' if c7_v3_clean else 'no'} exit={rc} :: {last[:160]}")
    else:
        print("C7_V3_CLEAN=n/a (no v3 file)")
    v4 = TREE / "corpus/knowledge/round-69-apk-axml-byte-evidence.md"
    if v4.is_file():
        rc, last = run(TREE, C7_GATE_REL, "--entry",
                       "corpus/knowledge/round-69-apk-axml-byte-evidence.md")
        c7_v4_clean = rc == 0
        print(f"C7_V4_CLEAN={'yes' if c7_v4_clean else 'no'} exit={rc} :: {last[:160]}")
    else:
        print("C7_V4_CLEAN=n/a (no v4 file)")
else:
    print("C7_SELFTEST=n/a")
    print("C7_RED_ON_R65_CANDIDATE=no")
    print("C7_V2_CLEAN=n/a (no gate)")
print(f"C7_CONTROL_PASS={c7_control_ok}/1")
print(f"C7_MUTANT_KILLED={c7_mut_killed}/1")
print(f"C7_MUTANT_KILLED_ATTRIBUTED={c7_mut_attributed}/1")

# C7 negative control (round-68): the frozen mutant (the verbatim comparison
# removed) PLUS a spoofed marker text. The run must still be killed (exit 1)
# while the attribution rule reads 0 — the last line is no longer the
# registered marker. This is what makes the attribution rule meaningful: a
# repair that kills the mutant with any other message scores 0/1.
C7_SPOOF_CLAUSE = re.compile(r'MARKER = "drifted entry output accepted"')


def mutate_c7_spoof(text):
    hits = C7_SPOOF_CLAUSE.findall(text)
    if len(hits) != 1:
        return None
    return C7_SPOOF_CLAUSE.sub('MARKER = "drifted entry output accepted (spoofed)"', text, count=1)


c7_neg_killed = c7_neg_attributed = 0
if c7_present:
    with tempfile.TemporaryDirectory(prefix="rev-r68-c7neg-") as tmp:
        work = pathlib.Path(tmp)
        shutil.copytree(TREE / "corpus", work / "corpus", symlinks=True)
        target = work / "corpus" / C7_GATE_REL
        text = target.read_text(encoding="utf-8")
        mutated = mutate_c7(text)
        if mutated is None:
            print("MUTANT check_embedded_outputs.py c7neg could-not-evaluate (clause match count != 1)")
            evaluable = False
        else:
            spoofed = mutate_c7_spoof(mutated)
            if spoofed is None:
                print("MUTANT check_embedded_outputs.py c7neg could-not-evaluate (spoof clause count != 1)")
                evaluable = False
            else:
                target.write_text(spoofed, encoding="utf-8")
                rc, last = run(work, C7_GATE_REL, "--self-test")
                state = "pass" if rc == 0 else "killed"
                print(f"MUTANT check_embedded_outputs.py c7neg exit={rc} {state} :: {last[:160]}")
                c7_neg_killed += rc != 0
                c7_neg_attributed += rc != 0 and last.endswith(C7_MARKER)
print(f"C7_NEG_SPOOF_KILLED={c7_neg_killed}/1")
print(f"C7_NEG_SPOOF_KILLED_ATTRIBUTED={c7_neg_attributed}/1")

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
holds_ok_v3 = holds_ok_v2 and c5_attributed == 2 and selftest_window
print(f"HOLDS_OK_V3={'yes' if holds_ok_v3 else 'no'}")
holds_ok_v4 = holds_ok_v3 and c6_attributed == 4
print(f"HOLDS_OK_V4={'yes' if holds_ok_v4 else 'no'}")
c7_targets = (c7_present and c7_selftest_ok and c7_control_ok == 1
              and c7_mut_attributed == 1 and c7_red and c7_v2_clean)
holds_ok_v5 = (holds_ok_v4 and c7_targets)
print(f"HOLDS_OK_V5={'yes' if holds_ok_v5 else 'no'}")
holds_ok_v6 = (holds_ok_v5 and c7_neg_killed == 1 and c7_neg_attributed == 0
               and c7_v3_clean)
print(f"HOLDS_OK_V6={'yes' if holds_ok_v6 else 'no'}")
sys.exit(2 if not evaluable else 0 if holds_ok else 1)
