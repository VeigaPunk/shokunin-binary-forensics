#!/usr/bin/env python3
"""MutationR100 driver: applies the pre-registered mutants in mutants.json to FROZEN bytes.

  python3 -B mutate_r100.py --tree <git archive of FROZEN> --scratch <dir> [--generate-only]
                            [--jobs N] [--controls-cmd CMD]

Uses reports/round-99/mutants/mutate8.py (frozen r99 bytes, imported read-only) to derive the
del-leg sites of the v9 counter's NEW legs (new = legs(v9) - legs(v8)), fail-closed against the
pre-registered leg list. Probe mutants are exact find/replace edits of cap_apk_probe.py, each
find string required to occur exactly once in the frozen probe bytes.

Kill rules (from mutants.json):
  v9 del-leg: killed iff forge_reach9 on the mutant reports the corresponding vector accepted,
              OR the mutant's --self-test fails (rc!=0, or no SELFTEST_C1V9=OK, or any FAIL).
  probe:      killed iff controls_c2 reports control-bad, OR the genuine-fixture CAP_APK_VERDICT
              (or rc) of the mutant differs from the unmutated probe.

Writes only under --scratch. Never writes into the lane or the frozen tree.
"""
import argparse, concurrent.futures as cf, difflib, hashlib, importlib.util, json, os, re, shutil, subprocess, sys
from pathlib import Path

PREREG_NEW_LEGS = [
    ("C1_PASS_NOTE_FLOOR", "C02-N1-one-token-pass-note"),
    ("C1_VOTER_PRESENT", "C02-N2-pinned-reviewer-vote-omitted"),
    ("C1_QMAP_POINTER", "C02-N3-qmap-contradicts-votes"),
    ("C1_EVIDENCE_RESOLVES", "C02-N4-evidence-id-edited"),
    ("C1_SECTIONS", "C02-N5-observation-limitations-cut"),
    ("C1_SURFACE_TEXT", "C02-N6-surface-text-attests-replication"),
    ("C1_NA_SHARE", "C14-N1-na-inflation"),
    ("C1_ARTIFACT_COPY", "C14-N2-artifact-renamed-to-other-seat"),
    ("C1_DERIV_RERUN", "C14-N3-derivation-count-edited"),
    ("C1_RECORD_PINNED", "C14-N4-record-appended"),
    ("C1_BODY_DIGEST", "C14-N5-s506-body-rebuilt"),
    ("C1_ANCHOR_VERBATIM", "C14-N6-s507-anchor-relabelled"),
]
COUNTER_REL = "reports/round-100/c1_k_admit_counter9.py"
BASE_REL = "reports/round-99/c1_k_admit_counter8.py"
MUTATE8_REL = "reports/round-99/mutants/mutate8.py"
FORGE_REL = "reports/round-100/forge_reach9.py"
PROBE_REL = "reports/round-100/cap_apk_probe.py"
FIXTURE_REL = "corpus/fixtures/apk-r65"
PROBE_EDITS = {
    "probe-drop-tamper-leg": ("    tamper_ok, why = tamper_leg(apk_bytes, expected, scratch, decoders)",
                              "    tamper_ok, why = True, \"\""),
    "probe-compare-only-package": ('FIELDS = ("package", "versionCode", "versionName")',
                                   'FIELDS = ("package",)'),
    "probe-skip-fixture-sha": ("    sha_ok = bool(want) and digest == want", "    sha_ok = True"),
    "probe-swallow-decoder-failure": ("        xml, err = decode(apk)\n        ok = False\n        detail = err",
                                      "        xml, err = decode(apk)\n        ok = True\n        detail = err"),
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def env_for(scratch):
    e = dict(os.environ, PYTHONUTF8="1", TMPDIR=str(scratch), HYAKU_SCRATCH=str(scratch / "hyaku"))
    (scratch / "hyaku").mkdir(parents=True, exist_ok=True)
    return e


def run(cmd, cwd, env, timeout=1800):
    try:
        p = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout, p.stderr
    except subprocess.TimeoutExpired as exc:
        return 124, (exc.stdout or b"").decode("utf-8", "replace") if isinstance(exc.stdout, bytes) else (exc.stdout or ""), "timeout"


def load_mutate8(tree):
    spec = importlib.util.spec_from_file_location("mutate8_r99", Path(tree) / MUTATE8_REL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def gen_v9(tree, scratch, m8):
    lane = str(tree)
    src = (Path(tree) / COUNTER_REL).read_text(encoding="utf-8")
    base = (Path(tree) / BASE_REL).read_text(encoding="utf-8")
    new_legs = sorted(set(m8.all_legs_of(src, lane)) - set(m8.all_legs_of(base, lane)))
    want = sorted(l for l, _ in PREREG_NEW_LEGS)
    if new_legs != want:
        print(f"PREREG_FAIL new legs derived={new_legs} want={want}", file=sys.stderr)
        sys.exit(2)
    pinned, mutants, _, _, _ = m8.build(src, lane, new_legs)
    out = []
    for leg, vec in PREREG_NEW_LEGS:
        sites = [mu for mu in mutants if mu["kind"] == "del-leg" and leg in mu["legs"]]
        if not sites:
            print(f"PREREG_FAIL no del-leg site for {leg}", file=sys.stderr)
            sys.exit(2)
        for i, mu in enumerate(sites):
            name = f"del-{leg}" + (f"-s{i}" if len(sites) > 1 else "")
            out.append({"name": name, "leg": leg, "vector": vec, "text": mu["text"],
                        "line": mu["line"], "desc": mu["desc"], "kind": "v9-del-leg"})
    return pinned, out


def gen_probe(tree, scratch):
    genuine = (Path(tree) / PROBE_REL).read_text(encoding="utf-8")
    out = []
    for name, (find, repl) in PROBE_EDITS.items():
        n = genuine.count(find)
        if n != 1:
            print(f"PREREG_FAIL {name}: find occurs {n} times", file=sys.stderr)
            sys.exit(2)
        out.append({"name": name, "text": genuine.replace(find, repl, 1), "kind": "probe-edit"})
    return genuine, out


def v9_checks(counter_path, scratch, tree, label, env):
    """forge_reach9 vectors + self-test for one counter file."""
    work = scratch / "fr" / label
    work.mkdir(parents=True, exist_ok=True)
    rc, out, err = run([sys.executable, "-B", str(Path(tree) / FORGE_REL), "--counter",
                        str(counter_path), "--work", str(work)], str(tree), env)
    vec = {}
    for line in out.splitlines():
        m = re.match(r"R100_VECTOR (\S+) (accepted|refused)\b", line)
        if m:
            vec[m.group(1)] = m.group(2)
    st_work = scratch / "st" / label
    st_work.mkdir(parents=True, exist_ok=True)
    src_rc, src_out, src_err = run([sys.executable, "-B", str(counter_path), "--self-test",
                                    "--work", str(st_work)], str(tree), env)
    st_ok = src_rc == 0 and re.search(r"SELFTEST_C1V9=OK\b", src_out) is not None and \
        re.search(r"SELFTEST_C1V9=FAIL\b", src_out) is None
    shutil.rmtree(work, ignore_errors=True)
    shutil.rmtree(st_work, ignore_errors=True)
    return {"forge_rc": rc, "forge_out": out, "forge_err": err, "vectors": vec,
            "accepted": sorted(k for k, v in vec.items() if v == "accepted"),
            "selftest_rc": src_rc, "selftest_ok": st_ok,
            "selftest_line": next((l for l in src_out.splitlines() if "SELFTEST_C1V9" in l), "")}


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--tree", required=True)
    ap.add_argument("--scratch", required=True)
    ap.add_argument("--jobs", type=int, default=3)
    ap.add_argument("--generate-only", action="store_true")
    ap.add_argument("--report", default="results.json")
    a = ap.parse_args(argv)
    tree = Path(a.tree).resolve()
    scratch = Path(a.scratch).resolve()
    (scratch / "mut").mkdir(parents=True, exist_ok=True)
    env = env_for(scratch)
    m8 = load_mutate8(tree)
    counter = tree / COUNTER_REL
    pinned, v9 = gen_v9(tree, scratch, m8)
    genuine_probe, pmuts = gen_probe(tree, scratch)
    print(f"GEN counter_sha={sha(counter)} probe_sha={sha(tree / PROBE_REL)} v9_mutants={len(v9)} "
          f"probe_mutants={len(pmuts)}")
    for mu in v9:
        p = scratch / "mut" / f"{mu['name']}.py"
        p.write_text(mu["text"], encoding="utf-8")
        compile(mu["text"], str(p), "exec")
        print(f"MUT {mu['name']} line={mu['line']} vector={mu['vector']} edit={mu['desc']}")
    for mu in pmuts:
        p = scratch / "mut" / f"{mu['name']}.py"
        p.write_text(mu["text"], encoding="utf-8")
        compile(mu["text"], str(p), "exec")
        print(f"PMUT {mu['name']}")
    if a.generate_only:
        return 0
    # baseline (unmutated frozen v9) -- the attack re-run / reference for kill comparison
    base = v9_checks(counter, scratch, tree, "base", env)
    print(f"BASE_FORGE rc={base['forge_rc']} accepted={len(base['accepted'])}/12 "
          f"selftest_rc={base['selftest_rc']} selftest_ok={base['selftest_ok']}")
    results = {"base": {k: base[k] for k in ("forge_rc", "accepted", "selftest_rc", "selftest_ok")},
               "v9": [], "probe": []}

    def do_v9(mu):
        p = scratch / "mut" / f"{mu['name']}.py"
        r = v9_checks(p, scratch, tree, mu["name"], env)
        vec_hit = mu["vector"] in r["accepted"]
        killed = vec_hit or (not r["selftest_ok"]) or r["selftest_rc"] != 0
        return {"name": mu["name"], "leg": mu["leg"], "vector": mu["vector"], "vector_accepted": vec_hit,
                "accepted_all": r["accepted"], "forge_rc": r["forge_rc"],
                "selftest_rc": r["selftest_rc"], "selftest_ok": r["selftest_ok"],
                "selftest_line": r["selftest_line"], "killed": killed}

    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        for r in ex.map(do_v9, v9):
            results["v9"].append(r)
            print(f"V9 {r['name']} killed={r['killed']} vector={r['vector']} "
                  f"accepted={r['vector_accepted']} forge_rc={r['forge_rc']} "
                  f"selftest_rc={r['selftest_rc']} selftest_ok={r['selftest_ok']}")

    # probe mutants: genuine-fixture verdict vs unmutated
    fixture = tree / FIXTURE_REL
    pwork = scratch / "probe"
    pwork.mkdir(parents=True, exist_ok=True)

    def probe_run(path, label):
        w = pwork / label
        w.mkdir(parents=True, exist_ok=True)
        rc, out, err = run([sys.executable, "-B", str(path), "--fixture", str(fixture),
                            "--work", str(w)], str(tree), env)
        verdict = next((l.split("=", 1)[1] for l in out.splitlines() if l.startswith("CAP_APK_VERDICT=")), None)
        return rc, verdict, out, err

    prc, pv, pout, perr = probe_run(tree / PROBE_REL, "genuine")
    print(f"BASE_PROBE rc={prc} verdict={pv}")
    results["probe_base"] = {"rc": prc, "verdict": pv}
    ctl_base = run(["bash", str(tree / "reports/round-100/controls_c2.sh"), str(tree / PROBE_REL),
                    str(scratch / "ctl" / "base")], str(tree), env)
    results["controls_base"] = {"rc": ctl_base[0], "out": ctl_base[1].strip().splitlines()[-1:]}
    print(f"BASE_CONTROLS rc={ctl_base[0]} last={ctl_base[1].strip().splitlines()[-1:]}")
    for mu in pmuts:
        rc, v, out, err = probe_run(scratch / "mut" / f"{mu['name']}.py", mu["name"])
        ctl = run(["bash", str(tree / "reports/round-100/controls_c2.sh"),
                   str(scratch / "mut" / f"{mu['name']}.py"),
                   str(scratch / "ctl" / mu["name"])], str(tree), env)
        ctl_line = next((l for l in ctl[1].splitlines() if l.startswith("C2_CONTROLS=")), "C2_CONTROLS=none")
        ctl_bad = ctl_line == "C2_CONTROLS=control-bad"
        changed = (rc != prc) or (v != pv)
        results["probe"].append({"name": mu["name"], "rc": rc, "verdict": v, "genuine_changed": changed,
                                 "stdout": out, "stderr_tail": err[-800:]})
        print(f"PROBE {mu['name']} rc={rc} verdict={v} genuine_changed={changed} "
              f"controls={ctl_line} ctl_rc={ctl[0]} killed={ctl_bad or changed}")
        results["probe"][-1].update({"controls_rc": ctl[0], "controls": ctl_line,
                                     "killed": ctl_bad or changed})
    Path(scratch / a.report).write_text(json.dumps(results, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
