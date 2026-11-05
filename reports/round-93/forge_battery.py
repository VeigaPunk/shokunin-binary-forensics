#!/usr/bin/env python3
"""Round-93 forgery battery (calibration): the routed r92 counter forgeries.

Freezes, as machine-checkable cases, every forgery class the round-92 critic
demonstrated against the v1 counters (findings 1-5, MutationR92Counters Demo
A-D) and the successor counters' required kills:

  F5  C08 token -> `partial`            v1 accepts; v2 C2_C08_TOKEN rejects
  F6  C08 -> held citing seed.md        v1 accepts; v2 exact-cites rejects
  F7  trailing cell appended to C08     v1 accepts; v2 5-cell parse rejects
  F8  round-77 record deleted           v1 accepts; v2 C2_C08_RECORD rejects
  F9  shadow tempfile.py beside probe   v1 (mutable probe source) accepts;
                                        v2 (probe from PROBE_REV archive,
                                        python3 -I) rejects
  F1  full C1 forgery (stub entry, fabricated v1-shaped votes, invented
      SOURCES row, README flip)         v1-reach receipt: CriticR92Claims
      findings.md finding 3 + forge-receipt.txt; v2 rejects
  F2  all-`n/a` votes                   v1-reach receipt: findings.md finding 4;
      v2 rejects (>=1 PASS + reasoned n/a required)
  F3  votes from seats absent from the  v1-reach receipt: findings.md finding 3
      wave registry                     (no registry check in v1); v2 rejects
  F4  vote artifact sha mismatch        v1-reach receipt: findings.md finding 3
      (no artifact binding in v1);      v2 rejects

Predicate (frozen in reports/round-93/claims.md before any after-run):
  V1_REACH_C2 = 5/5   (F5-F9 pass the v1 counter  - the red-before state)
  V2_KILLS    = 9/9   (F1-F9 all rejected by the v2 counters)
  POS_C1V2    = pass  (c1_k_admit_counter2.py --self-test: honest-shaped
                       admission state passes, four vote forgeries die)
  POS_C2V2    = pass  (c2_legend_counter2.py --self-test: intended move passes,
                       record-sha and trailing-cell forgeries die)
  DO_NOTHING  = fail  (v2 legend counter over the frozen BASE_REV)
  R92_RECEIPTS= 4/4   (the committed v1-reach receipts resolve)
  BATTERY_VERDICT = pass

Usage:
  forge_battery.py --stage v1-only    red-before: v1 reach over F5-F9 only
  forge_battery.py --stage full       full predicate (needs the v2 counters)
Exit 0 iff the stage's predicate holds; 1 otherwise; 64 usage.

All scratch lives under $HYAKU_SCRATCH/revenger-r93/battery and is removed on
exit. Read-only git access only; no live-tree writes outside this file's
reports/round-93/ directory (none - trees are built in scratch).
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
SCRATCH = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r93" / "battery"
BASE_REV = "281a5bad66e844190a570cb35d257c6974749993"
R92_FREEZE = "9402183a9492428fa0064d250746c62a0a2d9ca5"
V1_C2 = "reports/round-92/c2_legend_counter.py"
RECEIPTS = [
    ".ufo/waves/round-92/w1/CriticR92Claims/findings.md",
    ".ufo/waves/round-92/w1/CriticR92Claims/forge-receipt.txt",
    ".ufo/waves/round-92/w1/MutationR92Counters/mutants.md",
    ".ufo/waves/round-92/w1/CriticR92Claims/forge.py",
]
RECEIPT_MARKERS = [
    (".ufo/waves/round-92/w1/CriticR92Claims/findings.md", "passes 12/12 legs"),
    (".ufo/waves/round-92/w1/CriticR92Claims/findings.md", "`C1_VOTES=pass`, `C1_VERDICT=pass`"),
    (".ufo/waves/round-92/w1/CriticR92Claims/findings.md", "shadow"),
    (".ufo/waves/round-92/w1/CriticR92Claims/findings.md", "round-77"),
]
ENTRY_REL = "knowledge/round-93-browser-cdp-runtime-evidence.md"


def sh(cmd, cwd=None, env=None):
    e = dict(os.environ)
    e.setdefault("PYTHONUTF8", "1")
    if env:
        e.update(env)
    return subprocess.run(cmd, cwd=cwd, env=e, capture_output=True, text=True)


def shb(cmd, cwd=None, env=None):
    """Binary-safe runner for git archive output."""
    e = dict(os.environ)
    e.setdefault("PYTHONUTF8", "1")
    if env:
        e.update(env)
    return subprocess.run(cmd, cwd=cwd, env=e, capture_output=True)


class tar_extract:
    def __init__(self, data, dest):
        self.data, self.dest = data, dest

    def __enter__(self):
        self.dest.mkdir(parents=True, exist_ok=True)
        subprocess.run(["tar", "-x", "-C", str(self.dest)], input=self.data, check=True)
        return self.dest

    def __exit__(self, *a):
        return False


def base_tree(work, name):
    t = work / name
    ar = shb(["git", "-C", str(LANE), "archive", BASE_REV, "corpus",
              "reports/round-66/measure.py"])
    if ar.returncode != 0:
        raise SystemExit(f"base archive failed: {ar.stderr[:200]}")
    with tar_extract(ar.stdout, t):
        pass
    ar = shb(["git", "-C", str(LANE), "archive", R92_FREEZE, V1_C2])
    if ar.returncode != 0:
        raise SystemExit("v1 counter archive failed")
    with tar_extract(ar.stdout, t):
        pass
    return t


def cells(line):
    return [x.strip() for x in line.strip().strip("|").split("|")]


def edit_c08(tree, status=None, cites=None, trailing=False):
    p = tree / "corpus/README.md"
    out = []
    for ln in p.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\|[ \t]*C08 ", ln):
            c = cells(ln)
            if cites is not None:
                c[2] = "`" + cites + "`"
            if status is not None:
                c[4] = status
            ln = "| " + " | ".join(c) + (" note |" if trailing else "") + \
                 ("" if trailing else "")
            if trailing:
                ln = "| " + " | ".join(c) + " note |"
        out.append(ln)
    p.write_text("\n".join(out) + "\n", encoding="utf-8")


def delete_record(tree):
    (tree / "corpus/live/runs/round-77/inspection.json").unlink()


SHADOW = '''"""Forgery fixture (battery F9): shadow tempfile that prints forged labels."""
print("K_HELD=10/15 score=66.7")
print("K_HELD_BACKED=10/15")
print("README_TOKEN_LEGEND_MISMATCH=0 rows=[]")
import tempfile as _t
from tempfile import *  # noqa: F401,F403
'''


def plant_shadow(tree):
    (tree / "reports/round-66").mkdir(parents=True, exist_ok=True)
    (tree / "reports/round-66/tempfile.py").write_text(SHADOW, encoding="utf-8")
    # make the real probe flag a row: C07 frontier with a planted record
    p = tree / "corpus/README.md"
    out = []
    for ln in p.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\|[ \t]*C07 ", ln):
            ln = re.sub(r"\| held \|$", "| frontier |", ln)
        out.append(ln)
    p.write_text("\n".join(out) + "\n", encoding="utf-8")
    rec = tree / "corpus/live/runs/round-93-fw/inspection.json"
    rec.parent.mkdir(parents=True, exist_ok=True)
    rec.write_text(json.dumps({"operation": "inspect_firmware_regions",
                               "evidence_id": "ev_" + "0" * 64,
                               "normalized_result": {"regions": []}}), encoding="utf-8")


def run_v1_c2(tree):
    env = {"HYAKU_SCRATCH": str(SCRATCH / "v1sim")}
    r = sh([sys.executable, "-B", str(tree / V1_C2), "--tree", str(tree)], env=env)
    verdict = re.search(r"C2_VERDICT=(\w+)", r.stdout)
    return r.returncode, (verdict.group(1) if verdict else "no-label"), r.stdout + r.stderr


def run_v2_c2(tree_or_rev, rev=False):
    env = {"HYAKU_SCRATCH": str(SCRATCH / "v2sim")}
    cmd = [sys.executable, "-B", str(HERE / "c2_legend_counter2.py"),
           "--rev" if rev else "--tree", str(tree_or_rev)]
    r = sh(cmd, env=env)
    verdict = re.search(r"C2_VERDICT=(\w+)", r.stdout)
    return r.returncode, (verdict.group(1) if verdict else "no-label"), r.stdout + r.stderr


def run_v2_c1(tree):
    env = {"HYAKU_SCRATCH": str(SCRATCH / "v2sim")}
    r = sh([sys.executable, "-B", str(HERE / "c1_k_admit_counter2.py"),
            "--tree", str(tree)], env=env)
    verdict = re.search(r"C1_VERDICT=(\w+)", r.stdout)
    return r.returncode, (verdict.group(1) if verdict else "no-label"), r.stdout + r.stderr


def forge_c1_tree(work, name, votes):
    """Base + C08 held citing the entry + stub entry + fabricated votes."""
    t = base_tree(work, name)
    edit_c08(t, status="held", cites=ENTRY_REL)
    entry = t / "corpus" / ENTRY_REL
    entry.parent.mkdir(parents=True, exist_ok=True)
    entry.write_text("source: S999 — invented (opened 2026-11-05)\nverified-at: 2026-11-05\n"
                     "recheck: none\ncoverage-map: C08\nadmission-status: admitted\n\n# Stub\n",
                     encoding="utf-8")
    src = t / "corpus/SOURCES.md"
    row = ("| S999 | https://invented.example/x (docs, tier A, opened 2026-11-05) | docs | A "
           "| invented scope | anchor | invented teaching | mined | 2026-11-05 | 180d | "
           "corpus/" + ENTRY_REL + " |")
    src.write_text(src.read_text(encoding="utf-8") + row + "\n", encoding="utf-8")
    vdir = t / "reports/round-93/votes"
    vdir.mkdir(parents=True)
    import hashlib as _h
    want = _h.sha256(entry.read_text(encoding="utf-8").replace(
        "admission-status: admitted", "admission-status: candidate", 1
    ).encode()).hexdigest()
    QS = [f"Q{i:02d}" for i in range(1, 18)]
    art = t / ".ufo/waves/round-93/w1/FabricatedSeat/artifact.md"
    art.parent.mkdir(parents=True, exist_ok=True)
    art.write_text("fabricated\n", encoding="utf-8")
    art_sha = _h.sha256(art.read_bytes()).hexdigest()
    for i, v in enumerate(votes):
        vote = {"seat": v.get("seat", f"FabricatedSeat{i}"),
                "role": v.get("role", "reviewer"),
                "candidate_sha256": v.get("sha", want),
                "decisions": v.get("decisions", {q: "PASS" for q in QS}),
                "notes": v.get("notes", {q: "clean" for q in QS})}
        if "artifact_path" in v:
            vote["artifact_path"] = v["artifact_path"]
            vote["artifact_sha256"] = v.get("artifact_sha256", art_sha)
        (vdir / f"Fab{i}.json").write_text(json.dumps(vote), encoding="utf-8")
    # a synthetic registry naming the fabricated seats (F1/F2 keep them; the
    # battery's registry-absent class F3 omits the file entirely)
    if not votes == "no-registry":
        reg = {"members": {f"FabricatedSeat{i}": {"role": "reviewer"} for i in range(len(votes))}}
        (t / ".ufo/waves/round-93/w1").mkdir(parents=True, exist_ok=True)
        (t / ".ufo/waves/round-93/w1/swarm-registry.json").write_text(json.dumps(reg))
    # lint/embedded stand-ins so only the vote legs decide
    (t / "corpus/lint_entry.py").write_text("import sys\nsys.exit(0)\n")
    (t / "corpus/check_embedded_outputs.py").write_text("import sys\nsys.exit(0)\n")
    return t


def v1_only(work):
    rows = []
    ok = True
    classes = [
        ("F5", lambda t: edit_c08(t, status="partial")),
        ("F6", lambda t: edit_c08(t, status="held", cites="knowledge/seed.md")),
        ("F7", lambda t: edit_c08(t, trailing=True)),
        ("F8", delete_record),
        ("F9", plant_shadow),
    ]
    for name, mutate in classes:
        t = base_tree(work, f"v1only-{name}")
        mutate(t)
        rc, verdict, out = run_v1_c2(t)
        reach = verdict == "pass"
        ok &= reach
        print(f"BATTERY {name} v1={verdict} rc={rc} reach={'yes' if reach else 'NO'}")
        rows.append((name, verdict))
        shutil.rmtree(t, ignore_errors=True)
    n = sum(1 for _, v in rows if v == "pass")
    print(f"V1_REACH_C2={n}/5")
    print(f"BATTERY_VERDICT={'pass' if ok and n == 5 else 'fail'}")
    return 0 if ok and n == 5 else 1


def full(work):
    ok = True
    # --- v1 reach over F5-F9 (red-before, re-measured in the full stage) ---
    classes = [
        ("F5", lambda t: edit_c08(t, status="partial")),
        ("F6", lambda t: edit_c08(t, status="held", cites="knowledge/seed.md")),
        ("F7", lambda t: edit_c08(t, trailing=True)),
        ("F8", delete_record),
        ("F9", plant_shadow),
    ]
    v1_reach = 0
    for name, mutate in classes:
        t = base_tree(work, f"full-{name}-v1")
        mutate(t)
        rc, verdict, _ = run_v1_c2(t)
        reach = verdict == "pass"
        v1_reach += int(reach)
        ok &= reach
        print(f"BATTERY {name} v1={verdict} reach={'yes' if reach else 'NO'}")
        shutil.rmtree(t, ignore_errors=True)
    print(f"V1_REACH_C2={v1_reach}/5")
    ok &= (v1_reach == 5)

    # --- v2 kills over F1-F9 ---
    # F1 full forgery: fabricated v1-shaped votes (no provenance fields),
    # fabricated seats PRESENT in a fabricated registry (v1 had no registry leg)
    t = forge_c1_tree(work, "full-F1", [{}, {}])
    rc, verdict, out = run_v2_c1(t)
    kill = verdict == "fail"
    ok &= kill
    print(f"BATTERY F1 v2c1={verdict} kill={'yes' if kill else 'NO'}")
    shutil.rmtree(t, ignore_errors=True)
    # F2 all-n/a votes
    QS = [f"Q{i:02d}" for i in range(1, 18)]
    na = [{ "decisions": {q: "n/a" for q in QS}, "notes": {q: "reason" for q in QS}},
          {"decisions": {q: "n/a" for q in QS}, "notes": {q: "reason" for q in QS}}]
    t = forge_c1_tree(work, "full-F2", na)
    rc, verdict, _ = run_v2_c1(t)
    kill = verdict == "fail"
    ok &= kill
    print(f"BATTERY F2 v2c1={verdict} kill={'yes' if kill else 'NO'}")
    shutil.rmtree(t, ignore_errors=True)
    # F3 votes from seats absent from the registry
    t = forge_c1_tree(work, "full-F3", [{}, {}])
    (t / ".ufo/waves/round-93/w1/swarm-registry.json").unlink()
    rc, verdict, _ = run_v2_c1(t)
    kill = verdict == "fail"
    ok &= kill
    print(f"BATTERY F3 v2c1={verdict} kill={'yes' if kill else 'NO'}")
    shutil.rmtree(t, ignore_errors=True)
    # F4 artifact sha mismatch
    t = forge_c1_tree(work, "full-F4",
                      [{"artifact_path": ".ufo/waves/round-93/w1/FabricatedSeat0/artifact.md",
                        "artifact_sha256": "0" * 64},
                       {"artifact_path": ".ufo/waves/round-93/w1/FabricatedSeat1/artifact.md",
                        "artifact_sha256": "0" * 64}])
    rc, verdict, _ = run_v2_c1(t)
    kill = verdict == "fail"
    ok &= kill
    print(f"BATTERY F4 v2c1={verdict} kill={'yes' if kill else 'NO'}")
    shutil.rmtree(t, ignore_errors=True)
    # F5-F9 against v2
    for name, mutate in classes:
        t = base_tree(work, f"full-{name}-v2")
        mutate(t)
        rc, verdict, _ = run_v2_c2(t)
        kill = verdict == "fail"
        ok &= kill
        print(f"BATTERY {name} v2c2={verdict} kill={'yes' if kill else 'NO'}")
        shutil.rmtree(t, ignore_errors=True)
    print("V2_KILLS=9/9" if ok else "V2_KILLS<9/9")

    # --- self-tests (positive honest fixtures + committed kills) ---
    r = sh([sys.executable, "-B", str(HERE / "c1_k_admit_counter2.py"), "--self-test"],
           env={"HYAKU_SCRATCH": str(SCRATCH / "selftest")})
    pos1 = r.returncode == 0 and "SELFTEST_C1V2=pass" in r.stdout
    ok &= pos1
    print(f"POS_C1V2={'pass' if pos1 else 'fail'}")
    r = sh([sys.executable, "-B", str(HERE / "c2_legend_counter2.py"), "--self-test"],
           env={"HYAKU_SCRATCH": str(SCRATCH / "selftest")})
    pos2 = r.returncode == 0 and "SELFTEST_C2V2=pass" in r.stdout
    ok &= pos2
    print(f"POS_C2V2={'pass' if pos2 else 'fail'}")

    # --- do-nothing (v2 legend counter over BASE_REV must fail) ---
    rc, verdict, _ = run_v2_c2(BASE_REV, rev=True)
    dn = verdict == "fail"
    ok &= dn
    print(f"DO_NOTHING_C2={'fail' if dn else 'UNEXPECTED-PASS'}")

    # --- r92 v1-reach receipts resolve ---
    got = 0
    for rel, marker in RECEIPT_MARKERS:
        p = LANE / rel
        present = p.is_file()
        marked = present and marker in p.read_text(encoding="utf-8", errors="replace")
        got += int(present and marked)
        print(f"R92_RECEIPT {rel} present={present} marker={'yes' if marked else 'NO'} ({marker!r})")
    for rel in RECEIPTS:
        if not (LANE / rel).is_file():
            ok = False
            print(f"R92_RECEIPT_MISSING {rel}")
    ok &= (got == 4)

    print(f"BATTERY_VERDICT={'pass' if ok else 'fail'}")
    return 0 if ok else 1


def main(argv):
    stage = None
    i = 0
    while i < len(argv):
        if argv[i] == "--stage":
            stage = argv[i + 1]; i += 2
        else:
            print(__doc__, file=sys.stderr); return 64
    if stage not in ("v1-only", "full"):
        print(__doc__, file=sys.stderr); return 64
    SCRATCH.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="battery-", dir=str(SCRATCH)))
    try:
        if stage == "v1-only":
            return v1_only(work)
        return full(work)
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
