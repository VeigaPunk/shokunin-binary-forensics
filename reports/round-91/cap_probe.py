#!/usr/bin/env python3
"""Round-91 C2 capability counter (operability) — frozen before the instrument.

Usage:
    python3 -B reports/round-91/cap_probe.py --lane <REPO> --range <A>..<B>

Four required legs, all on one command:
  1. `reports/round-91/message_tree_check.py` exists;
  2. its `--selftest` exits 0 and prints `MSG_TREE_SELFTEST=pass`;
  3. planted-miss kill — this probe builds its own throwaway repo (mktemp under
     $HYAKU_SCRATCH or TMPDIR, `git -C "$D"` on every call, toplevel checked)
     with three commits: c0 empty root, c1 citing `a.txt` (present), c2 citing
     `missing/r91.txt` (absent). The instrument must exit 0 on `c0..c1` and
     exit 1 on `c1..c2` while naming `missing/r91.txt`; a stub that always
     prints a pass line dies here;
  4. a real run over `--range` printing `MESSAGE_TREE commits=N cited=M
     misses=K` with N >= 20 and M >= 20.

Prints `CAP_PRESENT=`, `CAP_SELFTEST=`, `CAP_PLANTED_MISS=`, `CAP_REAL=`,
`CAP_MESSAGE_TREE=pass|fail`; exit 0 iff all four hold, 1 otherwise, 64 on usage.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
INSTR = HERE / "message_tree_check.py"


def run(cmd, cwd=None, env=None):
    return subprocess.run(cmd, capture_output=True, text=True, cwd=cwd, env=env)


def scratch_root():
    for cand in (os.environ.get("HYAKU_SCRATCH"), "/fast/scratch/hyaku"):
        if cand and Path(cand).is_dir() and os.access(cand, os.W_OK):
            return Path(cand)
    return Path(tempfile.gettempdir())


def planted_repo(d):
    """Three-commit fixture repo; returns (c0, c1, c2) or raises."""
    g = lambda *a: run(["git", "-C", str(d), *a])  # noqa: E731
    if run(["git", "init", "-q", str(d)]).returncode != 0:
        raise RuntimeError("git init failed")
    top = g("rev-parse", "--show-toplevel").stdout.strip()
    if Path(top).resolve() != d.resolve():
        raise RuntimeError(f"fixture toplevel {top} != {d}")
    g("config", "user.name", "r91-fixture")
    g("config", "user.email", "r91@fixture.invalid")
    g("commit", "-q", "--allow-empty", "-m", "root")
    c0 = g("rev-parse", "HEAD").stdout.strip()
    (d / "a.txt").write_text("a\n", encoding="utf-8")
    g("add", "a.txt")
    g("commit", "-q", "-m", "add `a.txt`")
    c1 = g("rev-parse", "HEAD").stdout.strip()
    (d / "b.txt").write_text("b\n", encoding="utf-8")
    g("add", "b.txt")
    g("commit", "-q", "-m", "add `b.txt` and cite `missing/r91.txt`")
    c2 = g("rev-parse", "HEAD").stdout.strip()
    return c0, c1, c2


def main(argv):
    lane = rng = None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--lane":
            lane = Path(argv[i + 1]); i += 2
        elif a == "--range":
            rng = argv[i + 1]; i += 2
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"usage: {a}", file=sys.stderr); return 64
    if not lane or not rng:
        print(__doc__, file=sys.stderr)
        return 64

    legs = {}
    print(f"CAP_PRESENT={1 if INSTR.is_file() else 0} path={INSTR}")
    legs["present"] = INSTR.is_file()
    if not legs["present"]:
        print("CAP_SELFTEST=absent")
        print("CAP_PLANTED_MISS=absent")
        print("CAP_REAL=absent")
        print("CAP_MESSAGE_TREE=fail")
        return 1

    st = run([sys.executable, "-B", str(INSTR), "--selftest"])
    out = st.stdout + st.stderr
    ok = st.returncode == 0 and "MSG_TREE_SELFTEST=pass" in out
    print(f"CAP_SELFTEST={'pass' if ok else 'fail'} exit={st.returncode}")
    if not ok:
        print("  selftest tail: " + " | ".join(out.strip().splitlines()[-3:]))
    legs["selftest"] = ok

    root = scratch_root() / "revenger-r91" / "cap-probe"
    root.mkdir(parents=True, exist_ok=True)
    d = Path(tempfile.mkdtemp(prefix="fixture-", dir=str(root)))
    try:
        c0, c1, c2 = planted_repo(d)
        clean = run([sys.executable, "-B", str(INSTR), "--lane", str(d),
                     "--range", f"{c0}..{c1}"])
        dirty = run([sys.executable, "-B", str(INSTR), "--lane", str(d),
                     "--range", f"{c1}..{c2}"])
        dout = dirty.stdout + dirty.stderr
        ok = (clean.returncode == 0 and "missing/r91.txt" not in (clean.stdout + clean.stderr)
              and dirty.returncode == 1 and "missing/r91.txt" in dout)
        print(f"CAP_PLANTED_MISS={'pass' if ok else 'fail'} clean_exit={clean.returncode} "
              f"dirty_exit={dirty.returncode}")
        if not ok:
            print("  dirty tail: " + " | ".join(dout.strip().splitlines()[-3:]))
        legs["planted"] = ok
    finally:
        shutil.rmtree(d, ignore_errors=True)

    real = run([sys.executable, "-B", str(INSTR), "--lane", str(lane), "--range", rng])
    rout = real.stdout + real.stderr
    m = re.search(r"MESSAGE_TREE commits=(\d+) cited=(\d+) misses=(\d+)", rout)
    ok = bool(m) and int(m.group(1)) >= 20 and int(m.group(2)) >= 20
    print(f"CAP_REAL={'pass' if ok else 'fail'} "
          + (f"commits={m.group(1)} cited={m.group(2)} misses={m.group(3)} "
             f"exit={real.returncode}" if m else "no summary line"))
    legs["real"] = ok

    ok = all(legs.values())
    print("LEGS " + " ".join(f"{k}={'pass' if v else 'fail'}" for k, v in legs.items()))
    print(f"CAP_MESSAGE_TREE={'pass' if ok else 'fail'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
