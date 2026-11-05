#!/usr/bin/env python3
"""Round-98 forge-reach harness (calibration, C2 instrument).

Rebuilds the round-97 routed holdout (build_fresh.py) vectors as FULL trees
and runs one C2 battery in a single run:

  * FR00  honest control  (m_none)
  * FR00b benign-extra-file control (FR00 plus one new file
    `reports/round-98/benign-r98.txt` containing one plain sentence)
  * FR02  entry leading BOM            (m_entry_bom)
  * FR06  row dup held over held        (m_row_dup_held_over_held)
  * FR07  row dup target over held      (m_row_dup_target_over_held)
  * FR08  headers in fence              (m_headers_in_fence)
  * FR09  stale verified-at             (m_verified_at_stale)
  * FR10  n/a boilerplate on a PASS     (m_na_boilerplate_on_pass)
  * FR12  dangling own-work pointer     (m_own_work_dangling)

The mutators are vendored verbatim from
`.ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py`
(sha256 56762e34f52b38b61ac53ededacda7cf6b6e4569f08ec61a4ed6a1f4ccb9cd80)
into the sibling package `forgeries7/` (see `forgeries7/MANIFEST.sha256`
for the source hashes). The r97 builder file cannot be imported directly
(it runs `argparse.parse_args()` at import time), so the harness loads the
vendored copy instead. The builder module itself is left byte-unchanged.

Honest fixtures are built with the frozen v5 counter's `_fixture()`
(`reports/round-96/c1_k_admit_counter5.py`, imported read-only). The frozen
v6 fixture (`reports/round-97/c1_k_admit_counter6.py`) is byte-equivalent in
content for the c02 surface (verified identical fixture file sets and hashes),
so a v5-built tree is a faithful c02 fixture for a v6 or v7 `c02` counter.
For stub counters without `_fixture`, the same v5 fixture supplies a full
tree — no stub tree skips a delta (routed r97 defect 6.4 class).

Usage:
  python3 -B reports/round-98/forge_reach7.py --counter <path> [--profile c02] --work <scratch>

  Pass `--profile c02` to the counter only when given here; for v6 pass no
  profile. `--work` is the harness scratch root (created if absent). The
  harness honours TMPDIR/HYAKU_SCRATCH by routing all scratch under --work
  and exporting TMPDIR/HYAKU_SCRATCH into the counter subprocess.

Output (in order, one line each):
  VECTOR <name> rc=<n> verdict=<pass|fail> failing=<legs>
  C2_ACCEPTED=<n>/5
  C2_POSITIVE=<pass|fail>
  C2_POSITIVE2=<pass|fail>
  C2_STUB_SELFTEST=<ok|fail>
  C2_ROWSET_FR06=<legs>
  C2_ROWSET_FR07=<legs>
  C2_VERDICT=<met|not-met>

Exit 0 when every tree was evaluated (verdicts are data); 2 on harness error.
"""

import argparse
import hashlib
import importlib.util
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True  # never write __pycache__ into frozen dirs

HERE = Path(__file__).resolve().parent
LANE = HERE.parents[1]
FROZEN_V5 = LANE / "reports/round-96/c1_k_admit_counter5.py"
MUTATORS_PATH = HERE / "forgeries7" / "__init__.py"

ORDER = ["FR00", "FR00b", "FR02", "FR06", "FR07", "FR08", "FR09", "FR10", "FR12"]
ROUTED_FIVE = ["FR02", "FR08", "FR09", "FR10", "FR12"]

STUB_PASS = "#!/usr/bin/env python3\nprint('C1_VERDICT=pass')\n"
STUB_FAIL = "#!/usr/bin/env python3\nprint('C1_VERDICT=fail')\nprint('C1_ADMITTED=fail')\n"


def load(path, name):
    path = str(path)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"harness error: cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def failing_legs(stdout):
    """`C1_*=fail` lines (excluding WHY/DIFFS), as in the r96 battery."""
    return [ln.split("=")[0] for ln in stdout.splitlines()
            if ln.startswith("C1_") and ln.endswith("=fail")
            and "WHY" not in ln and "DIFFS" not in ln]


def verdict_of(stdout):
    return "pass" if "C1_VERDICT=pass" in stdout else "fail"


def snapshot(root):
    """Map relative path -> sha256 for every file under root."""
    out = {}
    for p in sorted(root.rglob("*")):
        if p.is_file():
            out[str(p.relative_to(root))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def run_counter(counter_path, root, counter_work, profile, env):
    cmd = [sys.executable, "-B", str(counter_path),
           "--work", str(counter_work),
           "--tree", str(root)]
    if profile:
        cmd[3:3] = ["--profile", profile]
    r = subprocess.run(cmd, capture_output=True, text=True, env=env)
    return r, verdict_of(r.stdout), failing_legs(r.stdout)


def build_trees(work):
    """Build the honest fixture plus one full tree per vector.

    Returns dict name -> {"tree": Path, "changed": [...], "delta_applied": bool}.
    Raises on mutator failure (harness error).
    """
    if not FROZEN_V5.is_file():
        raise SystemExit(f"harness error: frozen v5 fixture source missing: {FROZEN_V5}")
    if not MUTATORS_PATH.is_file():
        raise SystemExit(f"harness error: vendored mutators missing: {MUTATORS_PATH}")
    v5 = load(FROZEN_V5, "c1v5_fixture_source")
    mut = load(MUTATORS_PATH, "forgeries7_mutators")
    if not hasattr(mut, "MUTATORS") or not hasattr(mut, "set_mod"):
        raise SystemExit("harness error: vendored forgeries7 lacks MUTATORS/set_mod")
    mut.set_mod(v5)

    honest_parent = work / "honest-parent"
    honest_parent.mkdir(parents=True, exist_ok=True)
    honest, _want = v5._fixture(honest_parent)
    honest = Path(honest)
    if not (honest / v5.ENTRY).is_file():
        raise SystemExit("harness error: fixture missing ENTRY")
    # L1 integration fix (round 98, before the v7 freeze): the frozen v5 _fixture archives
    # 2875b9c, which predates corpus/live/runs/round-96/. Copy those committed record bytes
    # unchanged into the honest tree. This is the same L1-approved supplement that the v7
    # c02 _fixture applies (controls/v7-dev/c02-record-supplement.json). FR12 still points
    # its own-work row at a missing path.
    _rec_src = LANE / "corpus/live/runs/round-96"
    _rec_dst = honest / "corpus/live/runs/round-96"
    if _rec_src.is_dir() and not _rec_dst.exists():
        shutil.copytree(_rec_src, _rec_dst)
    honest_snap = snapshot(honest)

    trees_dir = work / "trees"
    trees_dir.mkdir(parents=True, exist_ok=True)
    trees = {}
    for name in ORDER:
        tree = trees_dir / name
        if tree.exists():
            shutil.rmtree(tree)
        shutil.copytree(honest, tree, symlinks=True)
        if name == "FR00b":
            extra = tree / "reports" / "round-98" / "benign-r98.txt"
            extra.parent.mkdir(parents=True, exist_ok=True)
            extra.write_text("This extra file is benign and changes nothing about admission.\n",
                             encoding="utf-8")
        else:
            fn = mut.MUTATORS[name]
            fn(tree)  # mutator exceptions propagate as harness errors
        snap = snapshot(tree)
        changed = sorted(k for k in set(snap) | set(honest_snap)
                         if snap.get(k) != honest_snap.get(k))
        expected = (name != "FR00")
        trees[name] = {
            "tree": tree,
            "changed": changed,
            "delta_applied": (len(changed) > 0) if expected else True,
        }
    return trees


def stub_selftest(trees, work, counter_work, profile, env):
    """Always-pass stub scores 5/5 and always-fail stub 0/5 on the same
    built trees, and every non-control delta reports applied."""
    stub_dir = work / "stubs"
    stub_dir.mkdir(parents=True, exist_ok=True)
    counts = {}
    for tag, src in (("stub-pass", STUB_PASS), ("stub-fail", STUB_FAIL)):
        counter_path = stub_dir / f"{tag}.py"
        counter_path.write_text(src, encoding="utf-8")
        accepted = 0
        for name in ROUTED_FIVE:
            r, verdict, _legs = run_counter(
                counter_path, trees[name]["tree"], counter_work, profile, env)
            if r.returncode not in (0, 1):
                return False
            if verdict == "pass":
                accepted += 1
        counts[tag] = accepted
    deltas_ok = all(trees[n]["delta_applied"] for n in ORDER)
    return counts.get("stub-pass") == 5 and counts.get("stub-fail") == 0 and deltas_ok


def evaluate(counter_path, profile, work):
    """Run the full battery; returns process exit code."""
    work = Path(work)
    work.mkdir(parents=True, exist_ok=True)
    (work / "tmp").mkdir(exist_ok=True)
    (work / "hyaku").mkdir(exist_ok=True)
    counter_work = work / "counter-run"
    counter_work.mkdir(parents=True, exist_ok=True)
    os.environ["TMPDIR"] = str(work / "tmp")
    os.environ["HYAKU_SCRATCH"] = str(work / "hyaku")
    os.environ["PYTHONUTF8"] = "1"

    trees = build_trees(work)
    env = dict(os.environ)
    env["TMPDIR"] = str(work / "tmp")
    env["HYAKU_SCRATCH"] = str(work / "hyaku")
    env["PYTHONUTF8"] = "1"

    results = {}
    for name in ORDER:
        r, verdict, legs = run_counter(
            counter_path, trees[name]["tree"], counter_work, profile, env)
        if r.returncode not in (0, 1):
            print(f"harness error: counter rc={r.returncode} on {name}",
                  file=sys.stderr)
            return 2
        results[name] = {"rc": r.returncode, "verdict": verdict, "legs": legs}
        print(f"VECTOR {name} rc={r.returncode} verdict={verdict} "
              f"failing={','.join(legs) if legs else 'none'}", flush=True)

    accepted = sum(1 for n in ROUTED_FIVE if results[n]["verdict"] == "pass")
    print(f"C2_ACCEPTED={accepted}/5", flush=True)
    positive = "pass" if results["FR00"]["verdict"] == "pass" else "fail"
    print(f"C2_POSITIVE={positive}", flush=True)
    positive2 = "pass" if results["FR00b"]["verdict"] == "pass" else "fail"
    print(f"C2_POSITIVE2={positive2}", flush=True)

    stub_ok = stub_selftest(trees, work, counter_work, profile, env)
    print(f"C2_STUB_SELFTEST={'ok' if stub_ok else 'fail'}", flush=True)

    for name, tag in (("FR06", "C2_ROWSET_FR06"), ("FR07", "C2_ROWSET_FR07")):
        legs = results[name]["legs"]
        print(f"{tag}={','.join(legs) if legs else 'none'}", flush=True)

    met = (accepted == 0 and positive == "pass" and positive2 == "pass" and stub_ok
           and "C1_ROWSET" in results["FR06"]["legs"]
           and "C1_ROWSET" in results["FR07"]["legs"])
    print(f"C2_VERDICT={'met' if met else 'not-met'}", flush=True)
    return 0


def main(argv):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--counter", type=Path, required=True)
    p.add_argument("--profile", choices=["c02"], default=None)
    p.add_argument("--work", type=Path, required=True)
    args = p.parse_args(argv)
    try:
        counter_path = args.counter.resolve()
        if not counter_path.is_file():
            print(f"harness error: counter not found: {counter_path}",
                  file=sys.stderr)
            return 2
        return evaluate(counter_path, args.profile, args.work)
    except SystemExit:
        raise
    except Exception as e:  # noqa: BLE001 - harness error -> exit 2
        print(f"harness error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
