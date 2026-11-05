#!/usr/bin/env python3
"""Round-97 forge-reach harness (calibration, C2 instrument).

Counts how many of the 19 frozen forgery vectors (reports/round-97/forgeries/,
FG01-FG20 minus FG17) a given admission counter accepts. A delta counts as
accepted when the counter prints `C1_VERDICT=pass` on the honest fixture
carrying that delta.

Vector logic is NOT imported from the frozen r96 module: each delta directory
holds its own verbatim builder (reports/round-97/forgeries/<name>/builder.py,
ported from .ufo/waves/round-96/w1/CriticR96/receipts/drv.py). The counter
module itself is loaded read-only via importlib solely for its honest-fixture
generator (`_fixture`) and constants (ENTRY, VOTES_DIR, RECEIPTS_DIR,
FETCH_LOG_REL, digest) — never for its forge logic. A counter without
`_fixture` (a stub) is supported via self-test injection.

Usage:
  python3 -B forge_reach6.py --counter <path> --deltas <dir> --work <scratch dir>
  python3 -B forge_reach6.py --self-test [--work <scratch dir>]
"""
import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


def load(path, name):
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


def run_counter(counter_path, root, work):
    env = dict(os.environ)
    env["TMPDIR"] = str(work)
    env.setdefault("PYTHONUTF8", "1")
    r = subprocess.run([sys.executable, "-B", str(counter_path),
                        "--tree", str(root)],
                       capture_output=True, text=True, env=env)
    verdict = "pass" if "C1_VERDICT=pass" in r.stdout else "fail"
    return r, verdict, failing_legs(r.stdout)
def _make_fixture(mod, fixtures):
    """A stub counter has no _fixture: build a tiny fake tree and enough
    mod attributes for builders that read them, so builders may run or
    no-op — the stub verdict decides the score either way."""
    if hasattr(mod, "_fixture"):
        return mod._fixture(fixtures)
    import tempfile
    root = Path(tempfile.mkdtemp(prefix="fx-", dir=fixtures))
    (root / "corpus/knowledge").mkdir(parents=True, exist_ok=True)
    (root / "corpus/fixtures/pe-r75-headless-smoke").mkdir(parents=True, exist_ok=True)
    return root, ""
def _ensure_mod_attrs(mod):
    """Stubs lack the frozen counter's constants; default them (builders may touch them)."""
    defaults = {"ENTRY": "corpus/knowledge/round-96-native-analysis-sessions.md",
                "VOTES_DIR": "reports/round-96/votes",
                "RECEIPTS_DIR": "reports/round-96/quote-receipts",
                "FETCH_LOG_REL": "reports/round-96/quote-receipts/fetch-log.md"}
    for k, v in defaults.items():
        if not hasattr(mod, k):
            setattr(mod, k, v)
    if not hasattr(mod, "digest"):
        mod.digest = lambda text: ""


def run_battery(counter_path, deltas_dir, work, counter_mod=None):
    """Run all 19 vectors; returns (results list, accepted count)."""
    work = Path(work)
    work.mkdir(parents=True, exist_ok=True)
    counter_path = Path(counter_path)
    deltas_dir = Path(deltas_dir)
    manifest = json.loads((deltas_dir / "manifest.json").read_text(encoding="utf-8"))
    counter = counter_mod if counter_mod is not None else load(counter_path, "counter-under-test")
    _ensure_mod_attrs(counter)
    fixtures = work / "fixtures"
    fixtures.mkdir(parents=True, exist_ok=True)
    results = []
    for name in manifest:
        root, _want = _make_fixture(counter, fixtures)
        builder = load(deltas_dir / name / "builder.py", f"builder-{name}")
        try:
            builder.apply(root, counter)
        except Exception as e:  # noqa: BLE001 - builder best-effort on stub trees
            print(f"builder note {name}: {e}", file=sys.stderr)
        r, verdict, legs = run_counter(counter_path, root, work)
        results.append({"name": name, "verdict": verdict, "legs": legs,
                        "rc": r.returncode})
        print(f"DELTA {name} verdict={verdict} "
              f"legs={','.join(legs) if legs else 'none'}", flush=True)
        shutil.rmtree(root, ignore_errors=True)
    accepted = sum(1 for x in results if x["verdict"] == "pass")
    print(f"C2_ACCEPTED={accepted}/{len(manifest)}", flush=True)
    return results, accepted


STUB_PASS = "#!/usr/bin/env python3\nprint('C1_VERDICT=pass')\n"
STUB_FAIL = "#!/usr/bin/env python3\nprint('C1_VERDICT=fail')\nprint('C1_ADMITTED=fail')\n"


def self_test(work):
    work = Path(work)
    work.mkdir(parents=True, exist_ok=True)
    deltas_dir = Path(__file__).resolve().parent / "forgeries"
    results = {}
    for tag, src in (("stub-pass", STUB_PASS), ("stub-fail", STUB_FAIL)):
        counter_path = work / f"{tag}.py"
        counter_path.write_text(src, encoding="utf-8")
        counter_mod = load(counter_path, f"selftest-{tag}")
        _, accepted = run_battery(counter_path, deltas_dir, work / tag, counter_mod)
        results[tag] = accepted
    print(f"SELFTEST stub-pass accepted={results['stub-pass']}/19 "
          f"stub-fail accepted={results['stub-fail']}/19", flush=True)
    ok = results["stub-pass"] == 19 and results["stub-fail"] == 0
    print(f"SELFTEST verdict={'OK' if ok else 'FAIL'}", flush=True)
    return 0 if ok else 2


def main(argv):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--counter", type=Path)
    p.add_argument("--deltas", type=Path)
    p.add_argument("--work", type=Path)
    p.add_argument("--self-test", action="store_true")
    args = p.parse_args(argv)
    try:
        if args.self_test:
            if args.work is None:
                return self_test(Path(os.environ.get("TMPDIR", ".")) / "forge-selftest")
            return self_test(args.work)
        if not args.counter or not args.deltas or not args.work:
            p.error("--counter, --deltas and --work are required (or use --self-test)")
        run_battery(args.counter, args.deltas, args.work)
        return 0
    except Exception as e:  # noqa: BLE001 - harness error -> exit 2
        print(f"harness error: {e}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
