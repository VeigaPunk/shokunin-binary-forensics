#!/usr/bin/env python3
"""Round-91 C1 counter (calibration) — frozen before any implementation.

Usage:
    python3 -B reports/round-91/c1_counter.py --impl <checker.py> \
        --real <TREE> --lane <LANE> [--battery <battery.py>]

Four required legs, all on one command:
  1. the frozen battery (`reports/round-91/sm6_battery_v3.py`, 21 labelled
     cases) scored against `--impl`'s `sm6` → `SM6_MISCLASS=0/21`;
  2. every frozen rule mutant (`reports/round-91/mutants.py`, 11) scored by the
     same battery → `MUTANTS_KILLED=11/11` (killed = at least one mismatch);
  3. `--impl --self-test` exits 0;
  4. a full run of `--impl --root <TREE> --lane <LANE>` prints
     `SELF_MISMATCH=0`.

Prints `C1_VERDICT=pass|fail` and exits 0 iff all four legs hold, 1 otherwise,
64 on usage. Read-only over the lane: it writes only inside its own temp dirs.
"""
import importlib.util
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv):
    impl = real = lane = battery_path = None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--impl":
            impl = Path(argv[i + 1]); i += 2
        elif a == "--real":
            real = Path(argv[i + 1]); i += 2
        elif a == "--lane":
            lane = Path(argv[i + 1]); i += 2
        elif a == "--battery":
            battery_path = Path(argv[i + 1]); i += 2
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"usage: {a}", file=sys.stderr); return 64
    if not (impl and real and lane):
        print(__doc__, file=sys.stderr)
        return 64
    battery_path = battery_path or HERE / "sm6_battery_v3.py"
    bat = load(battery_path, "r91_battery")
    mut = load(HERE / "mutants.py", "r91_mutants")
    impl_mod = load(impl, "r91_impl")

    legs = {}
    bad = 0
    total = 0
    with tempfile.TemporaryDirectory(prefix="rev-r91-c1-") as d:
        d = Path(d)
        for cid, rows, held, k_line, label in bat.CASES:
            root = d / cid
            bat.build(root, rows, held, k_line)
            got = impl_mod.sm6(root)
            total += 1
            ok = (got == 0 and label == 0) or (got == 1 and label == 1)
            if not ok:
                bad += 1
            print(f"CASE {cid} label={label} got={got} {'ok' if ok else 'MISCLASS'}")
        got = impl_mod.sm6(real)
        total += 1
        if got != 0:
            bad += 1
        print(f"CASE REAL label=0 got={got} {'ok' if got == 0 else 'MISCLASS'}")
    print(f"SM6_MISCLASS={bad}/{total}")
    legs["battery"] = bad == 0

    killed = 0
    survivors = []
    for mid, fn in mut.MUTANTS.items():
        mbad = 0
        with tempfile.TemporaryDirectory(prefix=f"rev-r91-mut-{mid}-") as d:
            d = Path(d)
            for cid, rows, held, k_line, label in bat.CASES:
                root = d / cid
                bat.build(root, rows, held, k_line)
                g = fn(root)
                ok = (g == 0 and label == 0) or (g == 1 and label == 1)
                if not ok:
                    mbad += 1
        k = mbad > 0
        killed += 1 if k else 0
        if not k:
            survivors.append(mid)
        print(f"MUTANT {mid} killed={'yes' if k else 'no'} misclass={mbad}/{len(bat.CASES)}")
    print(f"MUTANTS_KILLED={killed}/{len(mut.MUTANTS)}")
    legs["mutants"] = killed == len(mut.MUTANTS)

    st = subprocess.run([sys.executable, "-B", str(impl), "--self-test"],
                        capture_output=True, text=True)
    tail = (st.stdout + st.stderr).strip().splitlines()
    print(f"IMPL_SELFTEST exit={st.returncode} last={tail[-1] if tail else ''}")
    legs["selftest"] = st.returncode == 0

    run = subprocess.run([sys.executable, "-B", str(impl), "--root", str(real),
                          "--lane", str(lane)], capture_output=True, text=True)
    m = re.search(r"SELF_MISMATCH=(\d+)", run.stdout + run.stderr)
    print(f"REAL_SELF_MISMATCH={m.group(1) if m else 'none'} exit={run.returncode}")
    legs["real"] = bool(m) and m.group(1) == "0"

    ok = all(legs.values())
    print("LEGS " + " ".join(f"{k}={'pass' if v else 'fail'}" for k, v in legs.items()))
    print(f"C1_VERDICT={'pass' if ok else 'fail'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
