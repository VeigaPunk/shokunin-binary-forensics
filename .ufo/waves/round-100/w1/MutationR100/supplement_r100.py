#!/usr/bin/env python3
"""MutationR100 supplement (POST-FROZEN, not part of the pre-registered kill table).

Why: the pre-registered del-leg operator removes a leg's entry from the v9_legs `checks` dict. The
loop then hits KeyError, which is caught and recorded as a FAILED leg on every applicable profile, so
a deleted leg is equivalent to a force-fail. Its kills therefore show the honest fixture still runs
the leg, not that the leg's vector is caught. The pre-registration's "delete/negate" wording covers
the negated form: each leg's condition is replaced by (True, "forced-pass"). Those are run here with
the same kill rule (corresponding vector accepted, or self-test fails) and reported separately.

Probe attacks (not in claims.md's controls): (A1) androguard shim that rewrites versionCode 1->2 in
its real output; (A2) fixture copy whose truth.json image.sha256 is wrong, decoders untouched;
(A3) androguard shim that fails on every input. Kill = the attacked run's verdict/line differs from
the unmutated probe on the same attack input.

  python3 -B supplement_r100.py --tree <frozen git clone> --scratch <dir>
"""
import concurrent.futures as cf, json, os, re, shutil, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import mutate_r100 as M  # noqa: E402

REAL_ANDROGUARD = "/home/vgpnk/.local/bin/androguard"


def gen_force_pass(pinned):
    out = []
    for leg, vec in M.PREREG_NEW_LEGS:
        pat = re.compile(r'(?m)^(\s*)"%s": lambda: .*,$' % re.escape(leg))
        hits = pat.findall(pinned)
        if len(hits) != 1:
            print(f"SUPP_FAIL {leg}: lambda entry occurs {len(hits)} times", file=sys.stderr)
            sys.exit(2)
        text = pat.sub(lambda m: f'{m.group(1)}"{leg}": lambda: (True, "forced-pass"),', pinned, count=1)
        out.append({"name": f"fp-{leg}", "leg": leg, "vector": vec, "text": text})
    return out


def main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--tree", required=True)
    ap.add_argument("--scratch", required=True)
    ap.add_argument("--jobs", type=int, default=3)
    a = ap.parse_args(argv)
    tree = Path(a.tree).resolve()
    scratch = Path(a.scratch).resolve()
    scratch.mkdir(parents=True, exist_ok=True)
    env = M.env_for(scratch)
    m8 = M.load_mutate8(tree)
    pinned, _ = M.gen_v9(tree, scratch, m8)
    fps = gen_force_pass(pinned)
    fdir = scratch / "fp"
    fdir.mkdir(exist_ok=True)
    for mu in fps:
        (fdir / f"{mu['name']}.py").write_text(mu["text"], encoding="utf-8")
        compile(mu["text"], mu["name"], "exec")
    res = {"force_pass": [], "attacks": []}

    def do_fp(mu):
        r = M.v9_checks(fdir / f"{mu['name']}.py", scratch, tree, mu["name"], env)
        specific = mu["vector"] in r["accepted"]
        return {"name": mu["name"], "vector": mu["vector"], "vector_accepted": specific,
                "accepted_all": r["accepted"], "forge_rc": r["forge_rc"],
                "selftest_rc": r["selftest_rc"], "selftest_ok": r["selftest_ok"],
                "selftest_line": r["selftest_line"],
                "killed": specific or (not r["selftest_ok"]) or r["selftest_rc"] != 0,
                "kill_kind": ("vector" if specific else ("selftest-only" if (not r["selftest_ok"]) else "survived"))}

    base = M.v9_checks(tree / M.COUNTER_REL, scratch, tree, "supp-base", env)
    res["base"] = {k: base[k] for k in ("forge_rc", "accepted", "selftest_rc", "selftest_ok")}
    res["base_forge_vectors"] = [l for l in base["forge_out"].splitlines() if l.startswith("R100_")]
    print(f"SUPP_BASE accepted={len(base['accepted'])}/12 selftest_ok={base['selftest_ok']} rc={base['selftest_rc']}")
    for l in res["base_forge_vectors"]:
        print("  " + l)
    with cf.ThreadPoolExecutor(max_workers=a.jobs) as ex:
        for r in ex.map(do_fp, fps):
            res["force_pass"].append(r)
            print(f"FP {r['name']} killed={r['killed']} kind={r['kill_kind']} vector_accepted={r['vector_accepted']} "
                  f"accepted_all={len(r['accepted_all'])} selftest_ok={r['selftest_ok']} rc={r['selftest_rc']}")

    # ---- probe attacks
    adir = scratch / "attack"
    shims = adir / "shims"
    shims.mkdir(parents=True, exist_ok=True)
    lie = shims / "androguard-lie-versioncode"
    lie.write_text(f"#!/usr/bin/env bash\nset -o pipefail\n\"{REAL_ANDROGUARD}\" \"$@\" | sed 's/versionCode=\"1\"/versionCode=\"2\"/'\n", encoding="utf-8")
    failer = shims / "androguard-always-fail"
    failer.write_text("#!/usr/bin/env bash\necho 'androguard: simulated failure' >&2\nexit 1\n", encoding="utf-8")
    for p in (lie, failer):
        p.chmod(0o755)
    # digest-mismatch fixture copy (decoders untouched, truth.json digest wrong)
    fx_src = tree / "corpus/fixtures/apk-r65"
    fx_bad = adir / "fixture-digest-bad"
    if fx_bad.exists():
        shutil.rmtree(fx_bad)
    shutil.copytree(fx_src, fx_bad)
    import json as _j
    tj = _j.loads((fx_bad / "truth.json").read_text(encoding="utf-8"))
    tj["image"]["sha256"] = "0" * 64
    (fx_bad / "truth.json").write_text(_j.dumps(tj, indent=1), encoding="utf-8")

    probes = {"unmutated": tree / M.PROBE_REL}
    for name in M.PROBE_EDITS:
        probes[name] = scratch / "mut" / f"{name}.py"
    # the probe mutants live under the shared mutant dir of the main run; generate here if absent
    for name, (find, repl) in M.PROBE_EDITS.items():
        g = (tree / M.PROBE_REL).read_text(encoding="utf-8")
        p = adir / f"{name}.py"
        p.write_text(g.replace(find, repl, 1), encoding="utf-8")
        probes[name] = p
    attacks = {
        "A1-androguard-lies-versionCode": {"args": ["--androguard", str(lie)], "fixture": fx_src},
        "A2-fixture-digest-wrong": {"args": [], "fixture": fx_bad},
        "A3-androguard-fails-genuine": {"args": ["--androguard", str(failer)], "fixture": fx_src},
    }
    for aname, spec in attacks.items():
        for pname, ppath in probes.items():
            w = adir / "w" / f"{aname}-{pname}"
            w.mkdir(parents=True, exist_ok=True)
            cmd = [sys.executable, "-B", str(ppath), "--fixture", str(spec["fixture"]), "--work", str(w)] + spec["args"]
            try:
                p = subprocess.run(cmd, cwd=str(tree), env=env, capture_output=True, text=True, timeout=900)
                rc, out, err = p.returncode, p.stdout, p.stderr
            except subprocess.TimeoutExpired:
                rc, out, err = 124, "", "timeout"
            verdict = next((l.split("=", 1)[1] for l in out.splitlines() if l.startswith("CAP_APK_VERDICT=")), None)
            lines = {l.split("=", 1)[0]: l.split("=", 1)[1] for l in out.splitlines() if "=" in l and l.startswith("CAP_")}
            res["attacks"].append({"attack": aname, "probe": pname, "rc": rc, "verdict": verdict,
                                   "lines": lines, "stderr_tail": err[-400:]})
            print(f"ATTACK {aname} probe={pname} rc={rc} verdict={verdict} "
                  f"ANDROGUARD={lines.get('CAP_ANDROGUARD')} FIXSHA={lines.get('CAP_FIXTURE_SHA')}")
    (scratch / "supplement.json").write_text(json.dumps(res, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
