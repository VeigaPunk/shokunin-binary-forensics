#!/usr/bin/env python3
"""Round-91 C1 counter v2 (post-freeze, UNCLAIMED) — closes the fitting vector.

Round 91's frozen counter (`reports/round-91/c1_counter.py`) scores a fixed
21-case battery, so a 21-entry lookup table passes it without implementing the
rule (CriticR91Claims C1-1, `receipts/c1-fit-hardcoded.log`). This successor
keeps every frozen leg and adds randomized, run-time-generated cases that no
table can enumerate:

    python3 -B reports/round-91/c1_counter2.py --impl <checker.py> \
        --real <TREE> --lane <LANE> [--seed N] [--random 40]

Legs (all required):
  1. frozen battery `sm6_battery_v3.py` → `SM6_MISCLASS=0/22` (21 cases + real);
  2. frozen rule mutants `mutants.py` → `MUTANTS_KILLED=11/11`;
  3. `--random` generated cases (default 40, seed printed): random map size and
     held count, a statement drawn from eight shapes (true, wrong numerator,
     wrong denominator, both, bare line, pointer decoy that agrees, pointer
     decoy that disagrees, no statement), scored against the frozen rule
     (`mutants.reference`) — `RANDOM_MISCLASS=0/N`;
  4. impl `--self-test` exits 0;
  5. impl over `--real` prints `SELF_MISMATCH=0`.
Prints `C1V2_VERDICT=pass|fail`, exit 0 iff all five hold, 1 otherwise, 64 usage.
"""
import importlib.util
import random
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


def gen_case(rng, i):
    """A random (rows, held, k_line) case and its rule-derived label."""
    rows = rng.randint(10, 20)
    held = rng.randint(0, rows)
    kind = rng.choice(["true", "bad_num", "bad_den", "bad_both", "bare",
                       "ptr_agree", "ptr_disagree", "none"])
    if kind == "none":
        return rows, held, None
    before = f"{rng.randint(0, rows)}/{rng.choice([rows, rows + 1, max(rows - 1, 1)])}"
    if kind == "true":
        after = f"{held}/{rows}"
    elif kind == "bad_num":
        after = f"{(held + 1) % (rows + 1)}/{rows}"
    elif kind == "bad_den":
        after = f"{held}/{rows + 1}"
    elif kind == "bad_both":
        after = f"{(held + 1) % (rows + 1)}/{rows + 1}"
    else:
        after = f"{held}/{rows}"
    score = f" ({rng.uniform(0, 10):.1f})" if rng.random() < 0.5 else ""
    stated = f"`K_HELD_BACKED` {before}{score} → {after}{score}"
    if kind == "bare":
        return rows, held, f"K_HELD_BACKED {after}"
    if kind == "ptr_agree":
        ptr = f"`K_HELD_BACKED={after}`"
    elif kind == "ptr_disagree":
        ptr = f"`K_HELD_BACKED={rng.randint(0, rows)}/{rows}`"
    else:
        ptr = "probe exit 0"
    line = (f"| coverage — knowledge-map ground K (gen {i}) | {stated}; C05 uncovered | "
            f"`reports/round-91/measure.py TREE` ({ptr}) | `aaaaaaa` → `bbbbbbb` | improved |")
    return rows, held, line


def main(argv):
    impl = real = lane = None
    seed = 91091
    nrand = 40
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--impl":
            impl = Path(argv[i + 1]); i += 2
        elif a == "--real":
            real = Path(argv[i + 1]); i += 2
        elif a == "--lane":
            lane = Path(argv[i + 1]); i += 2
        elif a == "--seed":
            seed = int(argv[i + 1]); i += 2
        elif a == "--random":
            nrand = int(argv[i + 1]); i += 2
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"usage: {a}", file=sys.stderr); return 64
    if not (impl and real and lane):
        print(__doc__, file=sys.stderr)
        return 64

    bat = load(HERE / "sm6_battery_v3.py", "r91_bat2")
    mut = load(HERE / "mutants.py", "r91_mut2")
    impl_mod = load(impl, "r91_impl2")
    legs = {}

    bad = 0
    with tempfile.TemporaryDirectory(prefix="rev-r91-c1v2-") as d:
        d = Path(d)
        for cid, rows, held, k_line, label in bat.CASES:
            root = d / cid
            bat.build(root, rows, held, k_line)
            got = impl_mod.sm6(root)
            if not ((got == 0 and label == 0) or (got == 1 and label == 1)):
                bad += 1
        got = impl_mod.sm6(real)
        if got != 0:
            bad += 1
    print(f"SM6_MISCLASS={bad}/22")
    legs["battery"] = bad == 0

    killed = 0
    with tempfile.TemporaryDirectory(prefix="rev-r91-mut2-") as md:
        md = Path(md)
        for fn in mut.MUTANTS.values():
            sig = _score_all(md, bat, fn)
            if any((v == 0 and lab == 1) or (v == 1 and lab == 0) for v, lab in sig):
                killed += 1
    print(f"MUTANTS_KILLED={killed}/{len(mut.MUTANTS)}")
    legs["mutants"] = killed == len(mut.MUTANTS)

    rng = random.Random(seed)
    rbad = 0
    rcases = [gen_case(rng, k) for k in range(nrand)]
    with tempfile.TemporaryDirectory(prefix="rev-r91-rand-") as d:
        d = Path(d)
        for k, (rows, held, k_line) in enumerate(rcases):
            root = d / f"G{k:03d}"
            bat.build(root, rows, held, k_line)
            want = mut.reference(root)
            got = impl_mod.sm6(root)
            if got != want:
                rbad += 1
                print(f"RANDOM G{k:03d} rows={rows} held={held} want={want} got={got} MISCLASS")
    print(f"RANDOM_MISCLASS={rbad}/{nrand} seed={seed}")
    legs["random"] = rbad == 0

    st = subprocess.run([sys.executable, "-B", str(impl), "--self-test"],
                        capture_output=True, text=True)
    print(f"IMPL_SELFTEST exit={st.returncode}")
    legs["selftest"] = st.returncode == 0

    run = subprocess.run([sys.executable, "-B", str(impl), "--root", str(real),
                          "--lane", str(lane)], capture_output=True, text=True)
    m = re.search(r"SELF_MISMATCH=(\d+)", run.stdout + run.stderr)
    print(f"REAL_SELF_MISMATCH={m.group(1) if m else 'none'} exit={run.returncode}")
    legs["real"] = bool(m) and m.group(1) == "0"

    ok = all(legs.values())
    print("LEGS " + " ".join(f"{k}={'pass' if v else 'fail'}" for k, v in legs.items()))
    print(f"C1V2_VERDICT={'pass' if ok else 'fail'}")
    return 0 if ok else 1


def _score_all(d, bat, fn):
    """(verdict, label) pairs for one mutant over the frozen battery."""
    out = []
    base = Path(tempfile.mkdtemp(dir=str(d)))
    for cid, rows, held, k_line, label in bat.CASES:
        root = base / cid
        bat.build(root, rows, held, k_line)
        out.append((fn(root), label))
    return out


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
