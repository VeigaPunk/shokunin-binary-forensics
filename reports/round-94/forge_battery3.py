#!/usr/bin/env python3
"""Round-94 forge battery v3 (calibration): the routed forgery classes against the v3 counter.

Stages (frozen once committed):
  red-v2  Re-run the COMMITTED round-93 CriticR93 attack scripts fresh against the FROZEN
          round-93 v2 counter; require every named vector of the nine frozen classes to
          still pass v2 (the routed reach is real on this host today).
  full    (1) V3_KILLS: every frozen class fails reports/round-94/c1_k_admit_counter3.py on
          its frozen expected leg (fixture trees built from the FREEZE_REV archive + real
          entry bytes + synthetic wave/receipt fixtures);
          (2) POS_C1V3: the honest admission-shaped fixture passes v3 with the REAL
          corpus/lint_entry.py and corpus/check_embedded_outputs.py (no stubs);
          (3) DO_NOTHING_C1V3: the untouched base fails v3;
          (4) HOLD_R93_BATTERY: the frozen round-93 battery re-run keeps BATTERY_VERDICT=pass.

No git mutation; scratch only; every counter run is `python3 -B`.
"""
import importlib.util, json, os, re, shutil, subprocess, sys, tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
SCRATCH = Path("/fast/scratch/hyaku/revenger-r94/battery3")
CRITIC = LANE / ".ufo/waves/round-93/w1/CriticR93/attacks"
V2_SCRIPTS = ["attacks.py", "attacks2.py", "attacks3.py"]

# class -> committed r93 critic vectors that PASS the frozen v2 counter (the red reach).
# F13's v2 reach has no committed runnable vector (A28/A29 were critic-interactive, recorded
# in CriticR93/findings.md finding 3); its v3 kill is still a frozen battery class below.
V2_REACH_VECTORS = {
    "F10-dup-status": ["R1-dup-status-real"],
    "F11-forged-registry": ["A3-forged-registry"],
    "F12-case-dup-seat": ["A21a-case-dup-seat", "A21b-space-dup-seat", "R3-case-dup-seat-real"],
    "F14-artifact-binding": ["A1-shared-artifact", "A4-empty-artifact", "A5-registry-as-artifact"],
    "F15-traversal": ["A2-traversal", "R7-traversal-real"],
    "F16-body-source": ["A9-body-source", "R2-body-source-real"],
    "F17-vacuous-na": ["A17-vacuous-na", "R8-vacuous-na-real"],
    "F18-ws-mixed-fence": ["A27-ws-output", "A14b-mixed-fence", "R5-ws-output-real", "R4-mixed-fence-real"],
}
RECEIPT_BACKED_CLASSES = {
    "F13-role-mismatch": ".ufo/waves/round-93/w1/CriticR93/findings.md finding 3 (A28-author-self-vote, A29-role-mismatch: verdict=pass)",
}
FROZEN_REACH = 8
SUPPLEMENTARY = ["A6-forged-oracle", "A6b-truth-json-touched", "R6-forged-oracle-real"]


def load_v3():
    spec = importlib.util.spec_from_file_location(
        "c1v3", str(LANE / "reports/round-94/c1_k_admit_counter3.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def run(cmd, cwd):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)


def stage_red_v2():
    SCRATCH.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="redv2-", dir=SCRATCH))
    os.environ["HYAKU_SCRATCH"] = str(work / "hs")
    att = work / "attacks"
    att.mkdir()
    for s in sorted(CRITIC.glob("*.py")):
        shutil.copyfile(s, att / s.name)
    # the committed r93 attack driver hardcodes its r93 scratch root (attack.py S/TREES/HS
    # and the out/ receipt dir); the reaper swept that tree, so recreate the bare dirs
    r93s = Path("/fast/scratch/hyaku/revenger-r93/CriticR93")
    for d in ("out", "hs", "trees"):
        (r93s / d).mkdir(parents=True, exist_ok=True)
    verdicts = {}
    for s in V2_SCRIPTS:
        r = run([sys.executable, "-B", str(att / s)] + (["all"] if s == "attacks.py" else []), str(LANE))
        for ln in (r.stdout + "").splitlines():
            m = re.match(r"^([A-Za-z0-9-]+):\s*rc=(\S+)\s*verdict=(\S+)", ln.strip())
            if m:
                verdicts[m.group(1)] = (m.group(3), r.returncode)
    ok = True
    print("== red-v2: frozen v2 counter reach over the committed r93 critic vectors ==")
    for cls, vecs in V2_REACH_VECTORS.items():
        states = []
        for v in vecs:
            got = verdicts.get(v)
            if got is None:
                states.append("missing")
                print(f"{cls} {v}: MISSING (script printed no verdict line)")
            else:
                states.append(got[0])
                print(f"{cls} {v}: verdict={got[0]}")
        hit = all(s == "pass" for s in states)
        ok = ok and hit
        print(f"{cls}: v2_reach={'yes' if hit else 'NO'} ({sum(s == 'pass' for s in states)}/{len(vecs)})")
    for v in SUPPLEMENTARY:
        got = verdicts.get(v)
        print(f"supplementary {v}: verdict={got[0] if got else 'missing'}")
    reach = sum(1 for vecs in V2_REACH_VECTORS.values()
                if all(verdicts.get(v, ("missing",))[0] == "pass" for v in vecs))
    for cls, ptr in RECEIPT_BACKED_CLASSES.items():
        print(f"{cls}: v2_reach=receipt-backed ({ptr})")
    print(f"V2_REACH_NEW={reach}/{len(V2_REACH_VECTORS)} runnable + {len(RECEIPT_BACKED_CLASSES)} receipt-backed")
    verdict = "pass" if (ok and reach == FROZEN_REACH and reach == len(V2_REACH_VECTORS)) else "fail"
    print(f"RED_V2_VERDICT={verdict}")
    return 0 if verdict == "pass" else 1


def stage_full():
    m = load_v3()
    m.SCRATCH.mkdir(parents=True, exist_ok=True)
    work = Path(tempfile.mkdtemp(prefix="full-", dir=SCRATCH))
    ok = True
    print("== full: v3 kills over frozen classes ==")
    kills = 0
    classes = sorted(m.EXPECT_FAIL.items())
    for kind, expect in classes:
        root, _ = m._fixture(work)
        m._fixture_delta(root, kind)
        r = run([sys.executable, "-B", str(LANE / "reports/round-94/c1_k_admit_counter3.py"),
                 "--tree", str(root)], str(LANE))
        failing = [ln.split("=")[0] for ln in r.stdout.splitlines()
                   if ln.startswith("C1_") and ln.endswith("=fail")
                   and "WHY" not in ln and "DIFFS" not in ln and "BACKED" not in ln]
        hit = r.returncode != 0 and expect in failing
        kills += hit
        ok = ok and hit
        print(f"{kind}: {'KILLED' if hit else 'SURVIVED'} expected={expect} failing={','.join(failing) or 'none'}")
    print(f"V3_KILLS={kills}/{len(classes)}")

    root, _ = m._fixture(work)
    r = run([sys.executable, "-B", str(LANE / "reports/round-94/c1_k_admit_counter3.py"),
             "--tree", str(root)], str(LANE))
    pos = r.returncode == 0 and "C1_VERDICT=pass" in r.stdout
    ok = ok and pos
    print(f"POS_C1V3={'pass' if pos else 'fail'} (real lint + real embedded checker, no stubs)")

    dn_work = Path(tempfile.mkdtemp(prefix="dn-", dir=work))
    dn, err = m.materialize(m.FREEZE_REV, None, dn_work)
    if dn:
        r = run([sys.executable, "-B", str(LANE / "reports/round-94/c1_k_admit_counter3.py"),
                 "--tree", str(dn)], str(LANE))
        do_nothing = r.returncode != 0 and "C1_C15_HELD=fail" in r.stdout
    else:
        do_nothing = False
        print(f"do-nothing materialize error: {err}")
    ok = ok and do_nothing
    print(f"DO_NOTHING_C1V3={'fail-as-required' if do_nothing else 'PASSED-BAD'}")

    rb = run([sys.executable, "-B", "reports/round-93/forge_battery.py", "--stage", "full"], str(LANE))
    hold = rb.returncode == 0 and "BATTERY_VERDICT=pass" in rb.stdout
    ok = ok and hold
    tail = [ln for ln in rb.stdout.splitlines() if ln.startswith(("V2_KILLS", "POS_", "DO_NOTHING", "BATTERY_VERDICT"))]
    for ln in tail:
        print(f"R93_HOLD {ln}")
    print(f"HOLD_R93_BATTERY={'pass' if hold else 'FAIL'}")

    print(f"BATTERY3_VERDICT={'pass' if ok else 'fail'}")
    return 0 if ok else 1


def main(argv):
    if "--stage" not in argv:
        print(__doc__)
        return 64
    stage = argv[argv.index("--stage") + 1]
    if stage == "red-v2":
        return stage_red_v2()
    if stage == "full":
        return stage_full()
    print(f"unknown stage {stage}")
    return 64


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
