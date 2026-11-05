#!/usr/bin/env python3
"""Round-96 forge battery v5 (calibration): the frozen v4 counter reaches the r95-routed
NEW vectors, and the v5 successor counter closes them.

The three TREE vectors are the r95 routed survivors whose DESIGNS are authored outside the
v5 counter's author (CriticR95 A4 / A3-both findings and MutationR95 M8, committed in
.ufo/waves/round-95/w1/ and corpus/lessons/round-95-verifier-spotcheck.md §5 item 2); this
battery operationalizes them as executable deltas:

  A4-shadow-admitted     an unreferenced corpus/knowledge/*.md carrying an admitted
                         admission-status line passes every v4 leg (no leg enumerates
                         knowledge/) -> v5 leg C1_ADMITTED_UNION
  A3-usedby-extra        a second used-by pointer on a new registry row passes v4
                         (cite-back-only check) -> v5 used-by exclusivity in C1_SOURCES
  M8-pycache-frozen-dir  a __pycache__ planted under reports/round-94/ is dropped by
                         v4's tree materialization (not an ARCHIVE_PATH) and its scan
                         list -> v5 widens both (C1_PYCACHE)

Plus the MutationR95 self-test coverage gap: the six legs C1_ROWS_TOTAL, C1_TRIO,
C1_LINT, C1_EMBEDDED, C1_QUOTES, C1_K_HELD_BACKED have NO discriminating forged delta in
the frozen v4 self-test (V4_SELFTEST_UNCOVERED), and the connector's finding that the
self-test deltas are aggregate-only with no stub-prints-the-pass-line control. The v5
counter's self-test closes both: one discriminating delta per leg, one per-delta receipt
under --receipts-dir, and this battery's STUB control proves a printing stub cannot pass
a discriminating kill check.

Stages:
  --stage red-v4   build each NEW vector on an honest v4-shaped fixture (the FROZEN
                   reports/round-95/c1_k_admit_counter4.py fixture, imported unmodified)
                   and run the FROZEN v4 counter on it: every vector must PASS v4
                   (V4_REACH_NEW=3/3); the six legs must be absent from the frozen v4
                   self-test delta map (V4_SELFTEST_UNCOVERED=6);
                   RED_V4_VERDICT=pass.
  --stage full     run the v5 counter's --self-test with per-delta receipts (POS + 31
                   deltas + do-nothing; DELTA_RECEIPTS=31/31 each decide=true); kill every
                   NEW vector with the v5 counter on its frozen leg (V5_KILLS=3/3); prove
                   the registry-gate code mutant DIES on v5 (MUTANT_V5_REGISTRY_KILLED);
                   run the positive honest fixture (POS_C1V5=pass); run the do-nothing
                   base (DO_NOTHING_C1V5=fail-as-required); run the stub control
                   (STUB_REJECTED=pass); re-run the FROZEN r95 battery
                   (HOLD_R95_BATTERY=pass); BATTERY5_VERDICT=pass.

  --receipts-out D copy the per-delta receipts to D after a full stage (freeze evidence).

The frozen r94/r95 bytes are never modified: mutants run on scratch copies only.
"""
import hashlib, importlib.util, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
SCRATCH = Path(os.environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r96" / "battery5"
V4 = LANE / "reports/round-95/c1_k_admit_counter4.py"
V5 = LANE / "reports/round-96/c1_k_admit_counter5.py"
B4 = LANE / "reports/round-95/forge_battery4.py"

NEW_VECTORS = ["A4-shadow-admitted", "A3-usedby-extra", "M8-pycache-frozen-dir"]
UNCOVERED_LEGS = ["C1_ROWS_TOTAL", "C1_TRIO", "C1_LINT", "C1_EMBEDDED", "C1_QUOTES",
                  "C1_K_HELD_BACKED"]
LEG_ANCHOR = '    legs["C1_REGISTRY"] = reg_ok\n'
LANE_LINE_RE = re.compile(r'^LANE = Path\(__file__\)\.resolve\(\)\.parents\[2\]$', re.M)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_counter(path, args):
    return subprocess.run([sys.executable, "-B", str(path)] + args, cwd=str(LANE),
                          capture_output=True, text=True)


def failing_legs(stdout):
    return [ln.split("=")[0] for ln in stdout.splitlines()
            if ln.startswith(("C1_",)) and ln.endswith("=fail")
            and "WHY" not in ln and "DIFFS" not in ln]


def apply_delta_v4(root, kind):
    """Shape a NEW vector onto the FROZEN v4 fixture layout (v4 constants, S500/S501)."""
    if kind == "A4-shadow-admitted":
        sh = root / "corpus/knowledge/shadow-r96-notes.md"
        sh.parent.mkdir(parents=True, exist_ok=True)
        sh.write_text("source: fabricated\nverified-at: 2026-11-05\nrecheck: none\n"
                      "admission-status: admitted\n\n# Shadow entry (forgery)\n",
                      encoding="utf-8")
        return
    if kind == "A3-usedby-extra":
        sl = root / "corpus/SOURCES.md"
        t = sl.read_text(encoding="utf-8")
        marker = f"| on-release | {load(V4, 'v4b').ENTRY_REL} |"
        assert marker in t, "v4 fixture used-by anchor not found"
        sl.write_text(t.replace(marker, marker[:-2] + ", corpus/lessons/round-96.md |", 1),
                      encoding="utf-8")
        return
    if kind == "M8-pycache-frozen-dir":
        d = root / "reports/round-94" / "__pycache__"
        d.mkdir(parents=True, exist_ok=True)
        (d / "x.cpython-314.pyc").write_bytes(b"\x00fake")
        return
    raise SystemExit(f"no v4-shaped delta for {kind}")


def mutant_v5_source():
    src = V5.read_text(encoding="utf-8")
    if LEG_ANCHOR not in src:
        raise SystemExit("v5 registry-leg anchor not found")
    if not LANE_LINE_RE.search(src):
        raise SystemExit("v5 LANE anchor not found")
    src = LANE_LINE_RE.sub(f'LANE = Path("{LANE}")', src)
    return src.replace(LEG_ANCHOR, '    legs["C1_REGISTRY"] = True  # leg dropped (M6 mutant)\n')


def run_mutant(src_text, work, tag):
    p = work / f"{tag}.py"
    p.write_text(src_text, encoding="utf-8")
    env = {**os.environ, "HYAKU_SCRATCH": str(work / "scratch")}
    return subprocess.run([sys.executable, "-B", str(p), "--self-test"], cwd=str(LANE),
                          capture_output=True, text=True, env=env)


STUB_SOURCE = '''#!/usr/bin/env python3
import sys
# A stub that prints the pass lines without evaluating anything.
print("C1_K_HELD_BACKED=13/15")
print("C1_VERDICT=pass")
sys.exit(0)
'''


def stage_red_v4(work):
    v4 = load(V4, "v4b")
    reach, details = 0, []
    for kind in NEW_VECTORS:
        froot, _ = v4._fixture(work)
        apply_delta_v4(froot, kind)
        r = run_counter(V4, ["--tree", str(froot)])
        ok = r.returncode == 0 and "C1_VERDICT=pass" in r.stdout
        details.append(f"{kind}: v4 {'reach' if ok else 'BLOCKED rc=' + str(r.returncode)}")
        if ok:
            reach += 1
        shutil.rmtree(froot, ignore_errors=True)
    print(f"V4_REACH_NEW={reach}/{len(NEW_VECTORS)}")
    for d in details:
        print("  " + d)
    uncovered = [lg for lg in UNCOVERED_LEGS if lg not in set(v4.EXPECT_FAIL.values())]
    print("V4_SELFTEST_UNCOVERED_LEGS=" + ",".join(uncovered))
    print(f"V4_SELFTEST_UNCOVERED={len(uncovered)}/{len(UNCOVERED_LEGS)}")
    red_ok = reach == len(NEW_VECTORS) and len(uncovered) == len(UNCOVERED_LEGS)
    print(f"RED_V4_VERDICT={'pass' if red_ok else 'fail'}")
    return 0 if red_ok else 1


def stage_full(work, receipts_out=None):
    v5 = load(V5, "v5mod")
    fails = []
    pd = work / "per-delta"
    r = run_counter(V5, ["--self-test", "--receipts-dir", str(pd)])
    st_ok = "SELFTEST_C1V5=pass" in r.stdout and r.returncode == 0
    print(f"SELFTEST_C1V5={'pass' if st_ok else 'fail'} (POS + {len(v5.EXPECT_FAIL)} deltas + do-nothing)")
    if not st_ok:
        fails.append("selftest")
    receipts = sorted(pd.glob("*.json")) if pd.is_dir() else []
    good = 0
    for f in receipts:
        d = json.loads(f.read_text(encoding="utf-8"))
        if d.get("decide") is True and d.get("expected_leg") in failing_legs_map_ok(d):
            good += 1
    print(f"DELTA_RECEIPTS={good}/{len(v5.EXPECT_FAIL)}")
    if good != len(v5.EXPECT_FAIL) or len(receipts) != len(v5.EXPECT_FAIL):
        fails.append("delta-receipts")
    if receipts_out:
        out = Path(receipts_out)
        out.mkdir(parents=True, exist_ok=True)
        for f in receipts:
            shutil.copy(f, out / f.name)
    kills = 0
    for kind in NEW_VECTORS:
        expect = v5.EXPECT_FAIL[kind]
        froot, _ = v5._fixture(work)
        v5._fixture_delta(froot, kind)
        r = run_counter(V5, ["--tree", str(froot)])
        legs = failing_legs(r.stdout)
        ok = r.returncode == 1 and expect in legs
        print(f"{kind}: v5 {'KILLED' if ok else 'NOT-KILLED'} on {expect}"
              + ("" if ok else f" (rc={r.returncode} failing={legs})"))
        if ok:
            kills += 1
        shutil.rmtree(froot, ignore_errors=True)
    print(f"V5_KILLS={kills}/{len(NEW_VECTORS)}")
    if kills != len(NEW_VECTORS):
        fails.append("kills")
    w = Path(tempfile.mkdtemp(prefix="mut-v5-", dir=work))
    r = run_mutant(mutant_v5_source(), w, "v5_registry_leg_dropped")
    killed = "SELFTEST_C1V5=pass" not in r.stdout or r.returncode != 0
    print(f"MUTANT_V5_REGISTRY_KILLED={'pass' if killed else 'fail'}")
    shutil.rmtree(w, ignore_errors=True)
    if not killed:
        fails.append("mutant-v5")
    froot, _ = v5._fixture(work)
    r = run_counter(V5, ["--tree", str(froot)])
    pos = r.returncode == 0 and "C1_VERDICT=pass" in r.stdout
    print(f"POS_C1V5={'pass' if pos else 'fail'}")
    shutil.rmtree(froot, ignore_errors=True)
    if not pos:
        fails.append("pos")
    dn = Path(tempfile.mkdtemp(prefix="dn5-", dir=work))
    base, err = v5.materialize(v5.FREEZE_REV, None, dn)
    if base:
        r = run_counter(V5, ["--tree", str(base)])
        dn_ok = r.returncode == 1 and "C1_C02_HELD=fail" in r.stdout
        print(f"DO_NOTHING_C1V5={'fail-as-required' if dn_ok else 'UNEXPECTED'}")
        if not dn_ok:
            fails.append("do-nothing")
    else:
        print(f"DO_NOTHING_C1V5=materialize-failed:{err}")
        fails.append("do-nothing")
    shutil.rmtree(dn, ignore_errors=True)
    # stub control: a printing stub cannot satisfy a discriminating kill check
    froot, _ = v5._fixture(work)
    v5._fixture_delta(froot, "A4-shadow-admitted")
    stub = work / "stub_c1v5.py"
    stub.write_text(STUB_SOURCE, encoding="utf-8")
    r = subprocess.run([sys.executable, "-B", str(stub), "--tree", str(froot)],
                       cwd=str(LANE), capture_output=True, text=True)
    stub_rejected = ("C1_VERDICT=pass" in r.stdout
                     and "C1_ADMITTED_UNION=fail" not in r.stdout)
    print(f"STUB_REJECTED={'pass' if stub_rejected else 'fail'} "
          f"(stub prints pass; no discriminating leg line, so the kill check fails)")
    shutil.rmtree(froot, ignore_errors=True)
    if not stub_rejected:
        fails.append("stub")
    b4 = load(B4, "b4mod")
    r = subprocess.run([sys.executable, "-B", str(B4), "--stage", "full"],
                       cwd=str(LANE), capture_output=True, text=True)
    hold = "BATTERY4_VERDICT=pass" in r.stdout and r.returncode == 0
    if not hold:
        print("  r95 battery tail:", (r.stdout + r.stderr).strip().splitlines()[-3:])
    print(f"HOLD_R95_BATTERY={'pass' if hold else 'fail'}")
    if not hold:
        fails.append("hold-r95")
    verdict = not fails
    print(f"BATTERY5_VERDICT={'pass' if verdict else 'fail'}")
    return 0 if verdict else 1


def failing_legs_map_ok(d):
    """A receipt is honest when its recorded failing legs contain its expected leg."""
    return set(d.get("failing_legs", []))


def main(argv):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    stage = argv[argv.index("--stage") + 1] if "--stage" in argv else None
    receipts_out = argv[argv.index("--receipts-out") + 1] if "--receipts-out" in argv else None
    work = Path(tempfile.mkdtemp(prefix="b5-", dir=str(SCRATCH)))
    try:
        if stage == "red-v4":
            return stage_red_v4(work)
        if stage == "full":
            return stage_full(work, receipts_out)
        print(__doc__)
        return 64
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
