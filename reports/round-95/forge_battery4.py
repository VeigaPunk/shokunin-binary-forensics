#!/usr/bin/env python3
"""Round-95 forge battery v4 (calibration): the frozen v3 counter reaches the r94-routed
named vectors; the v4 counter kills the same named vectors on their frozen legs.

Named vectors (each carries its r94 receipt class):
  H1-indent-dup-status      CriticR94 H1 / r94 lesson M4  -> C1_ADMITTED
  V10-stale-fetched-at      CriticR94 H2 (V10)            -> C1_RECEIPTS
  V27-fabricated-foreign    CriticR94 H2 (V27)            -> C1_RECEIPTS
  V07-legacy-path           CriticR94 H3 (V07)            -> C1_C10_CITES
  V08-entry-pending         CriticR94 H3 (V08)            -> C1_C10_CITES
  V03-dup-json-registry     CriticR94 M2 (V03)            -> C1_REGISTRY
  V04-dup-json-vote         CriticR94 M2 (V04)            -> C1_VOTES
  V19-sid-suffix-spaced     CriticR94 M6 (V19)            -> C1_SIDS
  V18-na-letter-flood       CriticR94 M5 (V18)            -> C1_VOTES
  M6-registry-mutant        r94 lesson M6 / MutationR94 C1_REGISTRY SURVIVED
                            (a code mutant, not a tree: drop the registry gate)
  M5-pycache-planted        r94 lesson M5 / SentinelScope F1 -> C1_PYCACHE

Stages:
  --stage red-v3   build each TREE vector on an honest v3-shaped fixture (the FROZEN
                   reports/round-94/c1_k_admit_counter3.py fixture, imported unmodified)
                   and run the FROZEN v3 counter on it: every vector must PASS v3
                   (V3_REACH_NEW=9/9). For the M6 code mutant, mutate a scratch copy of
                   the frozen v3 counter by dropping its registry gate inside check_votes
                   and run v3's own --self-test: the mutant must SURVIVE
                   (MUTANT_V3_REGISTRY_SURVIVES=pass) - the committed r94 finding.
  --stage full     run the v4 counter's --self-test (POS + 22 deltas + do-nothing);
                   kill every TREE vector with the v4 counter on its frozen leg
                   (V4_KILLS=9/9); prove the same registry-gate code mutant DIES on v4
                   (MUTANT_V4_REGISTRY_KILLED=pass); run the positive honest fixture
                   (POS_C1V4=pass); run the do-nothing base (DO_NOTHING_C1V4=fail-as-
                   required); re-run the FROZEN r94 battery (HOLD_R94_BATTERY=pass);
                   BATTERY4_VERDICT=pass.

The frozen r93/r94 bytes are never modified: mutants run on scratch copies only.
"""
import hashlib, importlib.util, json, re, shutil, subprocess, sys, tempfile
from pathlib import Path

LANE = Path(__file__).resolve().parents[2]
SCRATCH = Path(__import__("os").environ.get("HYAKU_SCRATCH", "/fast/scratch/hyaku")) / "revenger-r95" / "battery4"
V3 = LANE / "reports/round-94/c1_k_admit_counter3.py"
V4 = LANE / "reports/round-95/c1_k_admit_counter4.py"
B3 = LANE / "reports/round-94/forge_battery3.py"

TREE_VECTORS = [
    "H1-indent-dup-status", "V10-stale-fetched-at", "V27-fabricated-body-foreign-host",
    "V07-legacy-path", "V08-entry-pending", "V03-dup-json-keys-registry",
    "V04-dup-json-keys-vote", "V19-sid-suffix-spaced", "V18-na-letter-flood",
    "M5-pycache-planted",
]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def run_counter(path, args):
    r = subprocess.run([sys.executable, "-B", str(path)] + args, cwd=str(LANE),
                       capture_output=True, text=True)
    return r


def failing_legs(stdout):
    return [ln.split("=")[0] for ln in stdout.splitlines()
            if ln.startswith(("C1_",)) and ln.endswith("=fail")
            and "WHY" not in ln and "DIFFS" not in ln and "BACKED" not in ln]


V4_EXPECT = dict(load(V4, "v4mod").EXPECT_FAIL)
V4_SEAT = "CriticR95"
V3_SEAT = "CriticR94"


def apply_delta_v3(root, kind, v3mod, want0):
    """The same named vector, shaped onto the v3 fixture layout (v3 constants).
    want0 = the honest fixture's bound digest; body-editing deltas re-bind votes."""
    entry = root / "corpus/knowledge/round-72-tool-landscape.md"
    text = entry.read_text(encoding="utf-8")
    reg = root / ".ufo/waves/round-94/w1/swarm-registry.json"
    votes = root / "reports/round-94/votes"
    rec = root / "reports/round-94/quote-receipts"
    if kind == "H1-indent-dup-status":
        lines = text.splitlines(True)
        lines.insert(3, "  admission-status: rejected\n")
        text = "".join(lines)
        entry.write_text(text, encoding="utf-8")
        # the critic's V14 repro re-binds the votes; v3's column-0 digest anchor does
        # NOT absorb the indented line, so the digest moves
        rebind_v3(root, want0, v3mod.digest(text))
        return
    if kind == "V10-stale-fetched-at":
        for sid in ("S498", "S499"):
            p = rec / f"{sid}.receipt.json"
            r = json.loads(p.read_text())
            r["fetched_at"] = "2026-10-01"
            p.write_text(json.dumps(r, indent=1))
        return
    if kind == "V27-fabricated-body-foreign-host":
        sid = "S498"
        body = ("REA is a cloud-hosted SaaS scanner with agent connectors for every "
                "binary format on the market, according to this fabricated text.\n")
        (rec / "raw" / f"{sid}.body").write_text(body, encoding="utf-8")
        quote = "cloud-hosted SaaS scanner with agent connectors"
        i = body.index(quote)
        r = {"schema": "revenger-quote-audit-v1", "sid": sid, "verdict": "verified",
             "fetch_url": "https://dlang.org/fabricated", "http_status": 200,
             "fetched_at": "2026-11-05",
             "fetch_sha256": hashlib.sha256(body.encode()).hexdigest(),
             "length": len(body.encode()), "quote": quote,
             "span": {"start": i, "end": i + len(quote)}}
        (rec / f"{sid}.receipt.json").write_text(json.dumps(r, indent=1))
        return
    if kind in ("V07-legacy-path", "V08-entry-pending"):
        rl = root / "corpus/README.md"
        out = []
        for ln in rl.read_text(encoding="utf-8").splitlines():
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            if len(c) == 5 and c[0] == "C15":
                c[2] = ("`legacy/knowledge/round-72-tool-landscape.md` (round-94 admission)"
                        if kind == "V07-legacy-path" else
                        "`knowledge/seed.md` (census; `knowledge/round-72-tool-landscape.md` pending admission)")
                ln = "| " + " | ".join(c) + " |"
            out.append(ln)
        rl.write_text("\n".join(out) + "\n", encoding="utf-8")
        return
    if kind == "V03-dup-json-keys-registry":
        raw = reg.read_text(encoding="utf-8")
        injected = raw.replace('"members": {',
                               '"members": {\n    "CriticR94": {"role": "reviewer"},', 1)
        reg.write_text(injected, encoding="utf-8")
        return
    if kind == "V04-dup-json-keys-vote":
        v = json.loads((votes / f"{V3_SEAT}.json").read_text())
        raw = ('{"seat": ' + json.dumps(V3_SEAT) + ', "role": "reviewer", "role": "critic", '
               '"candidate_sha256": ' + json.dumps(v["candidate_sha256"])
               + ', "decisions": ' + json.dumps(v["decisions"])
               + ', "notes": ' + json.dumps(v["notes"])
               + ', "artifact_path": ' + json.dumps(v["artifact_path"])
               + ', "artifact_sha256": ' + json.dumps(v["artifact_sha256"]) + '}')
        (votes / f"{V3_SEAT}.json").write_text(raw)
        return
    if kind == "V19-sid-suffix-spaced":
        text = text.replace("## Observation, inference, unknown",
                            "Per S0999a and S 0999 the atlas approach generalizes.\n\n"
                            "## Observation, inference, unknown")
        entry.write_text(text, encoding="utf-8")
        rebind_v3(root, want0, v3mod.digest(text))
        return
    if kind == "V18-na-letter-flood":
        for f in sorted(votes.glob("*.json")):
            v = json.loads(f.read_text())
            v["notes"] = {q: "n" * 30 for q in v["decisions"]}
            f.write_text(json.dumps(v))
        return
    if kind == "M5-pycache-planted":
        d = root / "corpus" / "__pycache__"
        d.mkdir(parents=True, exist_ok=True)
        (d / "audit_source_quotes.cpython-314.pyc").write_bytes(b"\x00fake")
        return
    raise SystemExit(f"no v3 delta for {kind}")


V3_GATE = ('    reg_ok, reg_reason = check_registry(root)\n'
           '    if not reg_ok:\n'
           '        return False, f"registry: {reg_reason}"\n')
V4_LEG = '    legs["C1_REGISTRY"] = reg_ok\n'
LANE_LINE_RE = re.compile(r'^LANE = Path\(__file__\)\.resolve\(\)\.parents\[2\]$', re.M)


def rebind_v3(root, old, new):
    """Full vote re-bind after a v3-shaped body edit (the r93 lesson M1 procedure):
    candidate digest, artifact bytes and artifact sha all move to the new digest."""
    import json as _json
    votes = root / "reports/round-94/votes"
    for f in sorted(votes.glob("*.json")):
        v = _json.loads(f.read_text())
        ap = root / v["artifact_path"]
        if ap.is_file():
            b = ap.read_text(encoding="utf-8").replace(old, new)
            ap.write_text(b, encoding="utf-8")
            v["artifact_sha256"] = hashlib.sha256(b.encode()).hexdigest()
        v["candidate_sha256"] = new
        f.write_text(_json.dumps(v), encoding="utf-8")


def mutant_v3_source():
    src = V3.read_text(encoding="utf-8")
    if V3_GATE not in src:
        raise SystemExit("v3 gate anchor not found")
    if not LANE_LINE_RE.search(src):
        raise SystemExit("v3 LANE anchor not found")
    src = LANE_LINE_RE.sub(f'LANE = Path("{LANE}")', src)
    return src.replace(V3_GATE, "    pass  # registry gate dropped (M6 mutant)\n")


def mutant_v4_source():
    src = V4.read_text(encoding="utf-8")
    if V4_LEG not in src:
        raise SystemExit("v4 registry-leg anchor not found")
    if not LANE_LINE_RE.search(src):
        raise SystemExit("v4 LANE anchor not found")
    src = LANE_LINE_RE.sub(f'LANE = Path("{LANE}")', src)
    return src.replace(V4_LEG, '    legs["C1_REGISTRY"] = True  # leg dropped (M6 mutant)\n')


def run_mutant(src_text, work, tag):
    p = work / f"{tag}.py"
    p.write_text(src_text, encoding="utf-8")
    import os
    env = {**os.environ, "HYAKU_SCRATCH": str(work / "scratch")}
    return subprocess.run([sys.executable, "-B", str(p), "--self-test"], cwd=str(LANE),
                          capture_output=True, text=True, env=env)


def stage_red_v3(work):
    v3 = load(V3, "v3mod")
    reach, details = 0, []
    for kind in TREE_VECTORS:
        froot, want0 = v3._fixture(work)
        apply_delta_v3(froot, kind, v3, want0)
        r = run_counter(V3, ["--tree", str(froot)])
        ok = r.returncode == 0 and "C1_VERDICT=pass" in r.stdout
        details.append(f"{kind}: v3 {'reach' if ok else 'BLOCKED rc=' + str(r.returncode)}")
        if ok:
            reach += 1
        shutil.rmtree(froot, ignore_errors=True)
    print(f"V3_REACH_NEW={reach}/{len(TREE_VECTORS)}")
    for d in details:
        print("  " + d)
    w = Path(tempfile.mkdtemp(prefix="mut-v3-", dir=work))
    r = run_mutant(mutant_v3_source(), w, "v3_registry_gate_dropped")
    survives = "SELFTEST_C1V3=pass" in r.stdout and r.returncode == 0
    print(f"MUTANT_V3_REGISTRY_SURVIVES={'pass' if survives else 'fail'} "
          f"(the committed MutationR94 C1_REGISTRY SURVIVED finding)")
    shutil.rmtree(w, ignore_errors=True)
    red_ok = reach == len(TREE_VECTORS) and survives
    print(f"RED_V3_VERDICT={'pass' if red_ok else 'fail'}")
    return 0 if red_ok else 1


def stage_full(work):
    v4 = load(V4, "v4mod")
    fails = []
    r = run_counter(V4, ["--self-test"])
    st_ok = "SELFTEST_C1V4=pass" in r.stdout and r.returncode == 0
    print(f"SELFTEST_C1V4={'pass' if st_ok else 'fail'} (POS + {len(v4.EXPECT_FAIL)} deltas + do-nothing)")
    if not st_ok:
        fails.append("selftest")
    kills = 0
    for kind in TREE_VECTORS:
        froot, _ = v4._fixture(work)
        v4._fixture_delta(froot, kind)
        r = run_counter(V4, ["--tree", str(froot)])
        legs = failing_legs(r.stdout)
        expect = V4_EXPECT[kind]
        ok = r.returncode == 1 and expect in legs
        details = f"{kind}: v4 {'KILLED' if ok else 'NOT-KILLED'} on {expect}"
        print(details + ("" if ok else f" (rc={r.returncode} failing={legs})"))
        if ok:
            kills += 1
        shutil.rmtree(froot, ignore_errors=True)
    print(f"V4_KILLS={kills}/{len(TREE_VECTORS)}")
    w = Path(tempfile.mkdtemp(prefix="mut-v4-", dir=work))
    r = run_mutant(mutant_v4_source(), w, "v4_registry_leg_dropped")
    killed = "SELFTEST_C1V4=pass" not in r.stdout or r.returncode != 0
    print(f"MUTANT_V4_REGISTRY_KILLED={'pass' if killed else 'fail'}")
    shutil.rmtree(w, ignore_errors=True)
    if not killed:
        fails.append("mutant-v4")
    # POS: honest fixture passes v4 (fresh run, its own log line)
    froot, _ = v4._fixture(work)
    r = run_counter(V4, ["--tree", str(froot)])
    pos = r.returncode == 0 and "C1_VERDICT=pass" in r.stdout
    print(f"POS_C1V4={'pass' if pos else 'fail'}")
    shutil.rmtree(froot, ignore_errors=True)
    if not pos:
        fails.append("pos")
    # do-nothing: the untouched base must fail on C1_C10_HELD
    dn = Path(tempfile.mkdtemp(prefix="dn4-", dir=work))
    base, err = v4.materialize(v4.FREEZE_REV, None, dn)
    if base:
        r = run_counter(V4, ["--tree", str(base)])
        dn_ok = r.returncode == 1 and "C1_C10_HELD=fail" in r.stdout
        print(f"DO_NOTHING_C1V4={'fail-as-required' if dn_ok else 'UNEXPECTED'}")
        if not dn_ok:
            fails.append("do-nothing")
    else:
        print(f"DO_NOTHING_C1V4=materialize-failed:{err}")
        fails.append("do-nothing")
    shutil.rmtree(dn, ignore_errors=True)
    # hold: the frozen r94 battery re-run stays green. Its stage_full mkdtemps under its
    # own SCRATCH constant without creating it (r94 lesson M1 class: a reaped scratch
    # root breaks a committed instrument); this runner pre-creates that root instead of
    # editing the frozen bytes.
    b3 = load(B3, "b3mod")
    Path(b3.SCRATCH).mkdir(parents=True, exist_ok=True)
    r = subprocess.run([sys.executable, "-B", str(B3), "--stage", "full"],
                       cwd=str(LANE), capture_output=True, text=True)
    hold = "BATTERY3_VERDICT=pass" in r.stdout and r.returncode == 0
    if not hold:
        print("  r94 battery tail:", (r.stdout + r.stderr).strip().splitlines()[-3:])
    print(f"HOLD_R94_BATTERY={'pass' if hold else 'fail'}")
    if not hold:
        fails.append("hold-r94")
    verdict = not fails
    print(f"BATTERY4_VERDICT={'pass' if verdict else 'fail'}")
    return 0 if verdict else 1


def main(argv):
    SCRATCH.mkdir(parents=True, exist_ok=True)
    stage = argv[argv.index("--stage") + 1] if "--stage" in argv else None
    work = Path(tempfile.mkdtemp(prefix="b4-", dir=str(SCRATCH)))
    try:
        if stage == "red-v3":
            return stage_red_v3(work)
        if stage == "full":
            return stage_full(work)
        print(__doc__)
        return 64
    finally:
        shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
