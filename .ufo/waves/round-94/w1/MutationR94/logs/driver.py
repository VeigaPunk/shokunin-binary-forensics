#!/usr/bin/env python3
"""MutationR94 driver: one-per-leg mutants of the frozen r94 C1 v3 counter.

Modeled exactly on the counter's self_test(): POS honest fixture must pass, each of the
12 EXPECT_FAIL forged deltas must fail on its frozen expected leg, do-nothing base must
fail on C1_C15_HELD. Runs are IN-PROCESS against each mutant module's own functions.

Why in-process: the shipped self_test() re-execs `python3 -B <this file> --tree ...` as a
subprocess, and a scratch-resident copy derives LANE from __file__ (parents[2] -> scratch),
which would pass a bogus --lane to corpus/lint_entry.py, run `git -C <scratch> archive` in
base_readme (breaking C1_ONLY_C15) and read a nonexistent entry in _fixture -- i.e. every
run would fail for harness reasons, not mutation reasons. Importing each mutant module and
injecting mod.LANE = the real lane reproduces production conditions with no extra source
edits; every mutated byte is still executed.

Usage: driver.py            -> baseline (pristine: real subprocess --self-test, in-process
                                selftest-eq, honest --tree run, frozen --rev digest)
       driver.py LEG [LEG…] -> per-mutant probes for the named legs
"""
import contextlib, importlib.util, io, json, os, subprocess, sys, tempfile
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
FROZEN = LANE / "reports/round-94/c1_k_admit_counter3.py"
SCRATCH = Path("/fast/scratch/hyaku/revenger-r94/MutationR94")
LOGS = SCRATCH / "logs"
WORK = SCRATCH / "work"
os.environ["HYAKU_SCRATCH"] = str(SCRATCH)  # counter tempdirs land inside our scratch
FREEZE_TIP = "060a8e87d6de6b31f91b58524ab0fcad88ae5431"

ALL_LEGS = ["C1_ROWS_TOTAL", "C1_C15_HELD", "C1_C15_CITES", "C1_ONLY_C15", "C1_ADMITTED",
            "C1_TRIO", "C1_VOTES", "C1_REGISTRY", "C1_LINT", "C1_EMBEDDED",
            "C1_EMBED_NONVACUOUS", "C1_SOURCES", "C1_QUOTES", "C1_K_HELD_BACKED"]

# leg -> (old, new) applied to the scratch copy; verified against each mutant file at load
MUTATIONS = {
    "C1_ROWS_TOTAL": ('legs["C1_ROWS_TOTAL"] = len(cov) == 15',
                      'legs["C1_ROWS_TOTAL"] = len(cov) != 15'),
    "C1_C15_HELD": ('legs["C1_C15_HELD"] = bool(c15) and c15[4] == "held"',
                    'legs["C1_C15_HELD"] = bool(c15) and c15[4] != "held"'),
    "C1_C15_CITES": ('legs["C1_C15_CITES"] = bool(c15) and ENTRY_REL in c15[2] and (root / ENTRY).is_file()',
                     'legs["C1_C15_CITES"] = bool(c15) and ENTRY_REL not in c15[2] and (root / ENTRY).is_file()'),
    "C1_ONLY_C15": ('legs["C1_ONLY_C15"] = not diffs and c15 is not None and baserows.get("C15") != _raw_line(readme, "C15")',
                    'legs["C1_ONLY_C15"] = c15 is not None and baserows.get("C15") != _raw_line(readme, "C15")'),
    "C1_ADMITTED": ('legs["C1_ADMITTED"] = (len(st_lines) == 1 and st_lines[0] < 15',
                    'legs["C1_ADMITTED"] = (len(st_lines) >= 1 and st_lines[0] < 15'),
    "C1_TRIO": ('legs["C1_TRIO"] = all(any(l.startswith(k) for l in head) for k in ("source:", "verified-at:", "recheck:"))',
                'legs["C1_TRIO"] = not all(any(l.startswith(k) for l in head) for k in ("source:", "verified-at:", "recheck:"))'),
    "C1_VOTES": ('legs["C1_VOTES"] = v_ok',
                 'legs["C1_VOTES"] = True'),
    "C1_REGISTRY": ('    reg_ok, reg_reason = check_registry(root)\n    if not reg_ok:\n        return False, f"registry: {reg_reason}"',
                    '    reg_ok, reg_reason = check_registry(root)'),
    "C1_LINT": ('legs["C1_LINT"] = lint.returncode == 0',
                'legs["C1_LINT"] = lint.returncode != 0'),
    "C1_EMBEDDED": ('emb_ok = emb.returncode == 0 or (emb.returncode == 2 and "could-not-evaluate" in (emb.stdout + emb.stderr) and not has_cmd_block)',
                    'emb_ok = emb.returncode == 0'),
    "C1_EMBED_NONVACUOUS": ('if any(l.lstrip().startswith("$") for l in lines):',
                            'if False:'),
    "C1_SOURCES": ('legs["C1_SOURCES"] = s_ok',
                   'legs["C1_SOURCES"] = True'),
    "C1_QUOTES": ('legs["C1_QUOTES"] = q_ok',
                  'legs["C1_QUOTES"] = True'),
    "C1_K_HELD_BACKED": ('legs["C1_K_HELD_BACKED"] = held_backed == 11',
                         'legs["C1_K_HELD_BACKED"] = held_backed != 11'),
}


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    mod.LANE = LANE  # scratch copies derive LANE from __file__; inject the real lane
    return mod


def run_tree(mod, root):
    """evaluate() with stdout captured; returns (text, legs, ok)."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        legs, ok = mod.evaluate(root)
    return buf.getvalue(), legs, ok


def selftest_eq(mod, tag):
    """Faithful in-process replica of mod.self_test(): POS + 12 deltas + do-nothing."""
    fails, chunks = [], []
    work = Path(tempfile.mkdtemp(prefix=f"st-{tag}-", dir=str(WORK)))
    try:
        root, want = mod._fixture(work)
        out, legs, ok = run_tree(mod, root)
        chunks.append("### POS honest fixture (mod._fixture)\n" + out)
        if not ok:
            fails.append(f"POS honest fixture did not pass: failing={[k for k, v in legs.items() if not v]}")
        for kind, expect in mod.EXPECT_FAIL.items():
            froot, _ = mod._fixture(work)
            mod._fixture_delta(froot, kind)
            out, legs, ok = run_tree(mod, froot)
            chunks.append(f"### forged delta {kind} (expect fail on {expect})\n" + out)
            failing = [k for k, v in legs.items() if not v]
            if ok or expect not in failing:
                fails.append(f"{kind}: expected fail on {expect}, got ok={ok} failing={failing}")
        dn = Path(tempfile.mkdtemp(prefix="dn-", dir=str(work)))
        do_nothing, err = mod.materialize(mod.FREEZE_REV, None, dn)
        if do_nothing:
            out, legs, ok = run_tree(mod, do_nothing)
            chunks.append("### do-nothing base (FREEZE_REV archive)\n" + out)
            if "C1_C15_HELD=fail" not in out or ok:
                fails.append(f"do-nothing base did not fail on C1_C15_HELD: ok={ok}")
        else:
            fails.append(f"do-nothing materialize: {err}")
    finally:
        import shutil
        shutil.rmtree(work, ignore_errors=True)
    head = f"SELFTEST_EQ_C1V3={'pass' if not fails else 'fail'} legs={len(mod.EXPECT_FAIL) + 2}"
    return head + "\n" + "\n".join("SELFTEST FAIL: " + f for f in fails) + "\n" + "\n".join(chunks), fails


def honest_tree_run(mod, tag):
    """Full honest --tree run over a fixture built by the ORIGINAL module's _fixture."""
    orig = load(FROZEN, f"c1v3_orig_{tag}")
    work = Path(tempfile.mkdtemp(prefix=f"ht-{tag}-", dir=str(WORK)))
    try:
        root, want = orig._fixture(work)
        out, legs, ok = run_tree(mod, root)
        return f"### honest --tree run (fixture from ORIGINAL _fixture, want={want})\n{out}", legs, ok, want
    finally:
        import shutil
        shutil.rmtree(work, ignore_errors=True)


def baseline():
    LOGS.mkdir(parents=True, exist_ok=True)
    orig = load(FROZEN, "c1v3_orig_base")
    lines = []
    # 1) the REAL shipped self-test of the pristine frozen file (subprocess, correct LANE)
    r = subprocess.run([sys.executable, "-B", str(FROZEN), "--self-test"], cwd=str(LANE),
                       capture_output=True, text=True)
    real_st = r.stdout + r.stderr
    lines.append("### pristine REAL subprocess --self-test (frozen path)\n" + real_st)
    verdict_line = next((ln for ln in real_st.splitlines() if ln.startswith("SELFTEST_C1V3=")), "MISSING")
    lines.append(f"real_selftest_rc={r.returncode} verdict={verdict_line}\n")
    # 2) in-process selftest-eq of the pristine module (validates the replication)
    st_out, st_fails = selftest_eq(orig, "base")
    lines.append("### pristine in-process selftest-eq\n" + st_out.split("###")[0].strip())
    # 3) honest --tree run (pristine)
    out, legs, ok, want = honest_tree_run(orig, "base")
    lines.append(out)
    lines.append(f"honest_ok={ok}\n")
    # 4) frozen --rev digest print (context; read-only git archive)
    work = Path(tempfile.mkdtemp(prefix="rev-", dir=str(WORK)))
    buf = io.StringIO()
    rc = None
    with contextlib.redirect_stdout(buf):
        rc = orig.main(["--rev", FREEZE_TIP])
    lines.append(f"### pristine --rev {FREEZE_TIP} (rc={rc})\n" + buf.getvalue())
    (LOGS / "baseline.log").write_text("\n".join(lines), encoding="utf-8")
    summary = {
        "real_selftest": verdict_line, "real_selftest_rc": r.returncode,
        "inproc_selftest_fails": st_fails, "honest_ok": ok, "want": want,
        "rev_rc": rc, "rev_stdout": buf.getvalue().splitlines(),
    }
    (SCRATCH / "summary_base.json").write_text(json.dumps(summary, indent=1), encoding="utf-8")
    print(json.dumps(summary, indent=1))


def probe(leg):
    old, new = MUTATIONS[leg]
    mut_path = SCRATCH / "mut" / f"mut_{leg}.py"
    src = mut_path.read_text(encoding="utf-8")
    assert src.count(new) == 1, f"{leg}: mutated line missing or duplicated in mutant file"
    assert old not in src, f"{leg}: unmutated line still present in mutant file"
    pristine_src = (SCRATCH / "mut" / "pristine_inproc.py").read_text(encoding="utf-8")
    assert pristine_src.count(old) == 1, f"{leg}: anchor not unique in pristine"
    assert new != old, f"{leg}: no-op mutation"
    mod = load(mut_path, f"mut_{leg}")
    log = [f"mutant: {leg}",
           f"old: {old}",
           f"new: {new}", ""]
    st_out, st_fails = selftest_eq(mod, leg)
    honest_out, legs, ok, want = honest_tree_run(mod, leg)
    log.append("### selftest-eq (in-process replica of the counter's self_test, mutant bytes)\n" + st_out)
    log.append("### honest --tree run (ORIGINAL _fixture)\n" + honest_out)
    # classification per task rule
    killed_by = []
    if not ok:
        killed_by.append(f"honest fixture verdict flips: failing={[k for k, v in legs.items() if not v]}")
    for f in st_fails:
        killed_by.append(f"selftest detector: {f}")
    verdict = "KILLED" if killed_by else None
    note = ""
    if verdict is None:
        # no flip: EQUIVALENT iff every observable output is byte-identical to pristine baseline runs
        base = load(SCRATCH / "mut" / "pristine_inproc.py", f"base_{leg}")
        base_st, _ = selftest_eq(base, f"basecmp_{leg}")
        base_h, base_legs, base_ok, _ = honest_tree_run(base, f"basecmp_{leg}")
        if st_out == base_st and honest_out == base_h:
            verdict, note = "EQUIVALENT", "all runs byte-identical to pristine baseline"
        else:
            verdict = "SURVIVED"
            diffs = []
            if st_out.split("\n")[0] != base_st.split("\n")[0]:
                diffs.append(f"selftest head {st_out.splitlines()[0]!r} vs {base_st.splitlines()[0]!r}")
            if honest_out != base_h:
                diffs.append("honest run output differs (see logs)")
            note = ("honest fixture still passes with the leg disabled; no frozen forged class flips; "
                    + "; ".join(diffs))
    log.append(f"verdict: {verdict}")
    log.append(f"killed_by: {killed_by if killed_by else 'n/a'}")
    log.append(f"note: {note}")
    (LOGS / f"{leg}.log").write_text("\n".join(log) + "\n", encoding="utf-8")
    print(json.dumps({"leg": leg, "verdict": verdict, "killed_by": killed_by, "note": note}))


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        baseline()
    else:
        for leg in args:
            assert leg in MUTATIONS, f"unknown leg {leg}"
            probe(leg)
