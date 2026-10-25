#!/usr/bin/env python3
"""Round-70 counting probe (frozen in reports/round-70/claims.md).

Usage: python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-70/measure.py TREE
TREE is a `git archive <commit> corpus SHONEN.md SCORECARD.md SKILL.md` extraction.
Run it by absolute path with any cwd; it reads only TREE (and git object lookups in
LANE for hash resolution) and writes only inside its own temp directories.

Exit contract (M50 repair): 0 every hold green; 1 a named hold is red; 2 the counter
itself could not evaluate (an uncaught exception is mapped here, never to 1). Every
helper is defined before first use; the treated-tree branches are exercised by the
committed scratch receipts under reports/round-70/controls/.

Labels by claim (read each by what it computes, never by the claim letter):
  C1 coverage   K_*, C05_*, V5_*, C1_GATE, C1_LINT, HOLDS_C1_V5
  C2 calibration SM1..SM6, SELF_MISMATCH, SELF_CLEAN_FIXTURE, SELF_MUTANTS_KILLED, HOLDS_C2_V5
  C3 freshness  EMB_*, EMB_PIN_MUTANT_KILLED_ATTRIBUTED, HOLDS_C3_V1
  holds         HOLD_REPLAY, GATE_SELFTEST, HOLDS_OK_V7
"""
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
BASE_COMMIT = "3f5edbc206351232a3d2d801334dd930499ccaf5"
V5 = "knowledge/round-70-apk-axml-byte-evidence.md"
R68_SHA = "ef7f0232edb74baecc2754e6671f00914ec02e077606fcb7f21880de0830798e"
R65_SHA = "cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a"
S046_SCRIPT_SHA = "bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249"
PIN_MARKER = "pinned historical script digest mismatch"
BACKED_ROW = re.compile(r"knowledge/[\w.-]+\.md")


def run(tree, script, *args, cwd=None, timeout=300):
    """(returncode, stdout, stderr) of `python3 -B <tree>/corpus/<script> args`."""
    proc = subprocess.run([sys.executable, "-B", str(Path(tree) / "corpus" / script), *args],
                          cwd=str(cwd or tree), capture_output=True, text=True, timeout=timeout)
    return proc.returncode, proc.stdout, proc.stderr


def last_line(text):
    lines = [l for l in text.strip().splitlines() if l.strip()]
    return lines[-1] if lines else ""


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return Path(path).read_text(encoding="utf-8", errors="ignore")


def readme_rows(tree):
    return [l for l in read(tree / "corpus/README.md").splitlines() if re.match(r"^\| C[0-9]+ ", l)]


def held_rows(rows):
    return [l for l in rows if re.search(r"\| held \|$", l)]


def entries_of(row):
    return BACKED_ROW.findall(row.split("|")[3])


def build_self_fixture(root, **defect):
    """Independent clean fixture for the C2 mutants (never imports the tool under test)."""
    (root / "corpus/fixtures").mkdir(parents=True)
    (root / "corpus/fixtures/f.txt").write_text("f", encoding="utf-8")
    (root / "corpus/tool.py").write_text("print(1)\n", encoding="utf-8")
    (root / "corpus/verify_a.py").write_text("print(1)\n", encoding="utf-8")
    if defect.get("SM2"):
        (root / "corpus/unnamed.py").write_text("print(2)\n", encoding="utf-8")
    (root / "corpus/QUALITY.md").write_text("| id |\n|---|\n| Q01 | a |\n| Q02 | b |\n", encoding="utf-8")
    rng = "Q01–Q01" if defect.get("SM1") else "Q01–Q02"
    rows = "".join(f"| C{i:02d} | s | k | w | {'held' if i <= 8 else 'frontier'} |\n" for i in range(1, 15))
    (root / "corpus/README.md").write_text(
        f"- `QUALITY.md` — admission criteria {rng}\n- `tool.py`\n- `fixtures/`\n- `verify_*.py`\n" + rows,
        encoding="utf-8")
    body = b"y" * 100
    size = 101 if defect.get("SM3") else 100
    (root / "SKILL.md").write_bytes(body)
    who = "revenger-r64.R64ReviewSkill" if defect.get("SM4") else "Someone Outside"
    (root / "SHONEN.md").write_text(
        f"- [x] Landed `SKILL.md` ({size} bytes, sha256 `{hashlib.sha256(body).hexdigest()[:12]}…`).\n"
        f"  Named non-author verifier: {who}.\n", encoding="utf-8")
    commit = "deadbee0123" if defect.get("SM5") else BASE_COMMIT[:12]
    kstate = "8/14 → 9/14" if defect.get("SM6") else "8/14 → 8/14"
    (root / "SCORECARD.md").write_text(
        f"## Round 61 x\nPre-registration `{commit}` ok.\nK_HELD_BACKED {kstate}\n", encoding="utf-8")


def self_check(tree, root_tmp):
    """C2 instrument leg: the tool's own output on a clean fixture and six planted defects."""
    tool = tree / "corpus/self_assessment_check.py"
    if not tool.is_file():
        return None
    def score(**defect):
        d = Path(tempfile.mkdtemp(dir=root_tmp))
        build_self_fixture(d, **defect)
        rc, out, _ = run(tree, "self_assessment_check.py", "--root", str(d), "--lane", str(LANE), cwd=d)
        m = re.search(r"SELF_MISMATCH=(\d+)", out)
        return rc, (int(m.group(1)) if m else None), dict(re.findall(r"(SM\d)=(\d+)", out))
    rc, n, _ = score()
    clean = (rc == 0 and n == 0)
    killed = 0
    for cls in ("SM1", "SM2", "SM3", "SM4", "SM5", "SM6"):
        rc, n, per = score(**{cls: True})
        killed += (rc == 1 and n == 1 and per.get(cls) == "1")
    return clean, killed


def emb(tree, entry_rel):
    rc, out, _ = run(tree, "check_embedded_outputs.py", "--entry", str(tree / "corpus" / entry_rel), cwd=tree)
    m = re.search(r"checked_blocks=(\d+) problems=(\d+)", out)
    return rc, (int(m.group(1)), int(m.group(2))) if m else (None, None), out


def main(tree):
    tmp = Path(tempfile.mkdtemp(prefix="rev-r70-measure-"))
    try:
        return body(tree, tmp)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def body(tree, tmp):
    # ---- C1 coverage: knowledge-map ground K ----------------------------------------------
    rows = readme_rows(tree)
    held = held_rows(rows)
    backed = [l for l in held if entries_of(l)
              and all((tree / "corpus" / p).is_file() for p in entries_of(l))]

    def rejected_marked(rel):
        f = tree / "corpus" / rel
        return f.is_file() and "admission-status: rejected" in read(f)
    strict = [l for l in backed if not any(rejected_marked(p) for p in entries_of(l))]
    print(f"K_HELD_BACKED={len(backed)}/{len(rows)} score={10 * len(backed) / len(rows):.1f}")
    print(f"K_HELD_BACKED_STRICT={len(strict)}/{len(rows)}")
    c05 = next((l for l in rows if l.startswith("| C05 ")), "")
    c05_status = c05.rsplit("|", 2)[-2].strip() if c05 else "absent"
    c05_entries = entries_of(c05) if c05 else []
    c05_single = len(c05_entries) == 1 and c05_entries[0] == V5
    print(f"C05_STATUS={c05_status}")
    print(f"C05_KNOWLEDGE_COLUMN={' '.join(c05_entries) if c05_entries else '-'}")
    print(f"C05_SINGLE_V5={'yes' if c05_single else 'no'}")
    v5 = tree / "corpus" / V5
    v5_text = read(v5) if v5.is_file() else ""
    v5_admitted = (bool(re.search(r"^admission-status: admitted", v5_text, re.M))
                   and "admission-status: rejected" not in v5_text)
    print(f"V5_ENTRY_PRESENT={'yes' if v5.is_file() else 'no'}")
    print(f"V5_ADMITTED_MARKED={'yes' if v5_admitted else 'no'}")
    gate_ok = lint_ok = False
    if v5.is_file() and (tree / "corpus/check_embedded_outputs.py").is_file():
        rc, (blocks, problems), _ = emb(tree, V5)
        gate_ok = rc == 0 and problems == 0 and (blocks or 0) >= 17
        print(f"C1_GATE=checked_blocks={blocks} problems={problems} exit={rc} ok={'yes' if gate_ok else 'no'}")
    else:
        print("C1_GATE=n/a (no v5 entry or no gate)")
    if v5.is_file() and (tree / "corpus/lint_entry.py").is_file():
        rc, out, _ = run(tree, "lint_entry.py", "--entry", str(v5), "--lane", str(LANE), cwd=tree)
        lint_ok = rc == 0
        print(f"C1_LINT={'; '.join(l for l in out.strip().splitlines())} exit={rc}")
    else:
        print("C1_LINT=n/a (no v5 entry or no lint)")
    holds_c1 = (len(backed) == 9 and len(strict) == 9 and c05_status == "held" and c05_single
                and v5_admitted and gate_ok and lint_ok)
    print(f"HOLDS_C1_V5={'yes' if holds_c1 else 'no'}")

    # ---- C2 calibration: self-assessment mismatches ------------------------------------------
    self_ok = mut_ok = False
    tool = tree / "corpus/self_assessment_check.py"
    if tool.is_file():
        rc, out, _ = run(tree, "self_assessment_check.py", "--root", str(tree), "--lane", str(LANE), cwd=tree)
        per = dict(re.findall(r"(SM\d)=(\d+)", out))
        n = re.search(r"SELF_MISMATCH=(\d+)", out)
        for k in ("SM1", "SM2", "SM3", "SM4", "SM5", "SM6"):
            print(f"{k}={per.get(k, 'n/a')}")
        print(f"SELF_MISMATCH={n.group(1) if n else 'n/a'} exit={rc}")
        self_ok = bool(n) and int(n.group(1)) == 0 and rc == 0
        sc = self_check(tree, tmp)
        clean, killed = sc
        print(f"SELF_CLEAN_FIXTURE={'0' if clean else 'nonzero'}")
        print(f"SELF_MUTANTS_KILLED={killed}/6")
        mut_ok = clean and killed == 6
    else:
        print("SELF_MISMATCH=n/a (no checker)")
        print("SELF_CLEAN_FIXTURE=n/a (no checker)")
        print("SELF_MUTANTS_KILLED=n/a (no checker)")
    box_count = len(re.findall(r"^- \[( |x|~)\] ", read(tree / "SHONEN.md"), re.M))
    print(f"SHONEN_BOX_COUNT={box_count}")
    print(f"README_ROWS={len(rows)}")
    holds_c2 = self_ok and mut_ok and box_count == 4 and len(rows) == 14
    print(f"HOLDS_C2_V5={'yes' if holds_c2 else 'no'}")

    # ---- C3 freshness: retained entries re-derive, the pin cannot be bypassed ------------------
    results = {}
    for tag, rel in (("R65", "knowledge/round-65-apk-axml-byte-evidence.md"),
                     ("R67", "knowledge/round-67-apk-axml-byte-evidence.md"),
                     ("R68", "knowledge/round-68-apk-axml-byte-evidence.md"),
                     ("R69", "knowledge/round-69-apk-axml-byte-evidence.md")):
        f = tree / "corpus" / rel
        if f.is_file() and (tree / "corpus/check_embedded_outputs.py").is_file():
            rc, (blocks, problems), _ = emb(tree, rel)
            results[tag] = (blocks, problems)
            print(f"EMB_{tag}=checked_blocks={blocks} problems={problems} exit={rc}")
        else:
            results[tag] = (None, None)
            print(f"EMB_{tag}=n/a")
    r68 = tree / "corpus/knowledge/round-68-apk-axml-byte-evidence.md"
    r65 = tree / "corpus/knowledge/round-65-apk-axml-byte-evidence.md"
    r68_same = r68.is_file() and sha(r68) == R68_SHA
    r65_same = r65.is_file() and sha(r65) == R65_SHA
    pinned_script = tree / "corpus/derive_axml_anchors_r68.py"
    pinned_ok = pinned_script.is_file() and sha(pinned_script) == S046_SCRIPT_SHA
    print(f"EMB_PINNED_SCRIPT_IS_S046={'yes' if pinned_ok else 'no'}")
    print(f"EMB_R68_BYTES_UNCHANGED={'yes' if r68_same else 'no'}")
    print(f"EMB_R65_BYTES_UNCHANGED={'yes' if r65_same else 'no'}")
    killed_pin = 0
    pins = tree / "corpus/embedded_output_pins.json"
    if pins.is_file() and r68.is_file():
        d = Path(tempfile.mkdtemp(dir=tmp))
        shutil.copytree(tree / "corpus", d / "corpus")
        spec = json.loads(read(pins)).get(r68.name, {})
        for pin in spec.values():
            target = d / pin["use"]
            if target.is_file():
                target.write_bytes(target.read_bytes() + b"\n# tampered\n")
        rc, out, _ = run(d, "check_embedded_outputs.py", "--entry", str(d / "corpus/knowledge" / r68.name), cwd=d)
        killed_pin = int(rc != 0 and PIN_MARKER in out)
        print(f"EMB_PIN_MUTANT_KILLED_ATTRIBUTED={killed_pin}/1")
    else:
        print("EMB_PIN_MUTANT_KILLED_ATTRIBUTED=n/a (no pin file)")
    b68, p68 = results["R68"]
    holds_c3 = (b68 == 17 and p68 == 0 and results["R65"][1] == 1 and results["R67"][1] == 0
                and results["R69"][1] == 0 and r68_same and r65_same and killed_pin == 1 and pinned_ok)
    print(f"HOLDS_C3_V1={'yes' if holds_c3 else 'no'}")

    # ---- holds: replay verifiers and the gate's own self-test ----------------------------------
    ps = sorted((tree / "corpus").glob("verify_*.py"))
    ok = 0
    for p in ps:
        rc, out, err = run(tree, p.name, "--self-test", cwd=tree)
        ok += rc == 0
        print("HOLD", p.name, f"exit={rc}", last_line(out + err)[:140])
    print(f"HOLD_REPLAY={ok}/{len(ps)}")
    gate_rc = run(tree, "check_embedded_outputs.py", "--self-test", cwd=tree)[0] if (
        tree / "corpus/check_embedded_outputs.py").is_file() else 2
    print(f"GATE_SELFTEST=exit {gate_rc}")
    families = {"native-static": {"inspect_pe_resources"}, "managed": {"inspect_managed_artifact"},
                "javascript": {"analyze_javascript_application"}, "android": {"inspect_android_package"},
                "archives": {"inventory_artifact", "inspect_artifact"}, "firmware": {"inspect_firmware_regions"},
                "browser-runtime": {"inspect_web_page", "capture_browser_scenario", "observe_web_session"},
                "evm": {"inspect_evm_interface"}}
    seen = set()
    for p in sorted((tree / "corpus/live/runs").rglob("*.json")):
        try:
            x = json.loads(p.read_bytes())
        except (ValueError, UnicodeError):
            continue
        if isinstance(x, dict) and x.get("evidence_id") and x.get("normalized_result") is not None:
            seen.add(x.get("operation", "unknown"))
    present = [k for k, v in families.items() if v & seen]
    print(f"F_COVERAGE={len(present)}/{len(families)} score={10 * len(present) / len(families):.1f}")
    fresh = 0
    for rel in ("corpus/knowledge/seed.md", "corpus/knowledge/2026-10-12-rea-readiness-checklist.md"):
        f = tree / rel
        fresh += sum(1 for l in read(f).splitlines() if f.is_file() and re.match(r"^\| [FK][0-9]+ .*\| (holds|STALE)", l))
    print(f"FRESH_ROWS={fresh}/18")
    holds_ok = ok == len(ps) == 10 and gate_rc == 0 and len(present) == 5 and fresh == 18
    print(f"HOLDS_OK_V7={'yes' if holds_ok else 'no'}")
    return 0 if holds_ok else 1


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1 or not (Path(args[0]).resolve() / "corpus").is_dir():
        print("usage: measure.py TREE (TREE/corpus must exist)")
        sys.exit(2)
    try:
        sys.exit(main(Path(args[0]).resolve()))
    except SystemExit:
        raise
    except BaseException:  # M50 repair: a crash is exit 2 (not evaluable), never exit 1 (a hold failed)
        traceback.print_exc()
        print("COUNTER_ERROR=uncaught exception (exit 2)")
        sys.exit(2)
