#!/usr/bin/env python3
"""Round-91 C2 probe v2 (post-freeze, UNCLAIMED) — closes the three stub vectors.

Round 91's frozen probe (`reports/round-91/cap_probe.py`) plants the literal
path `missing/r91.txt`, so a stub that flags any cited name containing
`missing` passes it, and its real leg ignores the exit code and the miss count
(CriticR91Claims C2-2/C2-3/C2-4, `receipts/stubD.py`, `probe-stubE.log`).
This successor keeps the four legs and makes each one discriminating:

    python3 -B reports/round-91/cap_probe2.py --lane <REPO> --range <A>..<B>

  1. `reports/round-91/message_tree_check.py` exists;
  2. `--selftest` exits 0 and prints `MSG_TREE_SELFTEST=pass`;
  3. a throwaway fixture repo (mktemp under $HYAKU_SCRATCH or TMPDIR, every call
     `git -C "$D"`, toplevel asserted) with four commits:
       c0 empty root, c1 adds `a.txt` and cites it, c2 cites a RANDOM absent
       path `r91absent/<hex>/absent.txt` (generated at run time, so no stub can
       spell it), c3 cites `later/only.txt` which c4 adds afterwards — present
       in the worktree at probe time, absent from c3's tree, so a worktree-only
       check fails this leg. Required: `c0..c1` exit 0, `c1..c2` exit 1 naming
       exactly the random path, `c2..c3` exit 1 naming `later/only.txt`;
  4. the real run over `--range`: `commits` must equal `git rev-list --count`,
     `cited` > 0, and the exit code must agree with the printed miss count
     (0 iff misses == 0, 1 iff misses > 0).

Prints `CAP2_PRESENT=`, `CAP2_SELFTEST=`, `CAP2_PLANTED_MISS=`, `CAP2_TREE_SCOPE=`,
`CAP2_REAL=`, `CAP2_VERDICT=pass|fail`; exit 0 iff every leg holds, 1 otherwise,
64 on usage.
"""
import os
import random
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
INSTR = HERE / "message_tree_check.py"


def run(cmd, cwd=None):
    return subprocess.run(cmd, capture_output=True, text=True, cwd=cwd)


def scratch_root():
    for cand in (os.environ.get("HYAKU_SCRATCH"), "/fast/scratch/hyaku"):
        if cand and Path(cand).is_dir() and os.access(cand, os.W_OK):
            return Path(cand)
    return Path(tempfile.gettempdir())


def fixture(d, absent):
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
    g("add", "a.txt"); g("commit", "-q", "-m", "add `a.txt`")
    c1 = g("rev-parse", "HEAD").stdout.strip()
    g("commit", "-q", "--allow-empty", "-m", f"note `{absent}`")
    c2 = g("rev-parse", "HEAD").stdout.strip()
    g("commit", "-q", "--allow-empty", "-m", "cite `later/only.txt`")
    c3 = g("rev-parse", "HEAD").stdout.strip()
    (d / "later").mkdir()
    (d / "later/only.txt").write_text("l\n", encoding="utf-8")
    g("add", "later/only.txt"); g("commit", "-q", "-m", "add `later/only.txt`")
    c4 = g("rev-parse", "HEAD").stdout.strip()
    return c0, c1, c2, c3, c4


def main(argv):
    global INSTR
    lane = rng = None
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--lane":
            lane = Path(argv[i + 1]); i += 2
        elif a == "--range":
            rng = argv[i + 1]; i += 2
        elif a == "--instr":
            INSTR = Path(argv[i + 1]); i += 2
        elif a in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"usage: {a}", file=sys.stderr); return 64
    if not lane or not rng:
        print(__doc__, file=sys.stderr)
        return 64
    legs = {}
    print(f"CAP2_PRESENT={1 if INSTR.is_file() else 0}")
    legs["present"] = INSTR.is_file()
    if not legs["present"]:
        print("CAP2_VERDICT=fail")
        return 1

    st = run([sys.executable, "-B", str(INSTR), "--selftest"])
    out = st.stdout + st.stderr
    legs["selftest"] = st.returncode == 0 and "MSG_TREE_SELFTEST=pass" in out
    print(f"CAP2_SELFTEST={'pass' if legs['selftest'] else 'fail'} exit={st.returncode}")

    absent = f"r91absent/{random.getrandbits(48):012x}/absent.txt"
    root = scratch_root() / "revenger-r91" / "cap-probe2"
    root.mkdir(parents=True, exist_ok=True)
    d = Path(tempfile.mkdtemp(prefix="fixture-", dir=str(root)))
    try:
        c0, c1, c2, c3, c4 = fixture(d, absent)
        clean = run([sys.executable, "-B", str(INSTR), "--lane", str(d), "--range", f"{c0}..{c1}"])
        dirty = run([sys.executable, "-B", str(INSTR), "--lane", str(d), "--range", f"{c1}..{c2}"])
        dout = dirty.stdout + dirty.stderr
        legs["planted"] = (clean.returncode == 0 and absent in dout
                           and dirty.returncode == 1 and absent not in (clean.stdout + clean.stderr))
        print(f"CAP2_PLANTED_MISS={'pass' if legs['planted'] else 'fail'} "
              f"clean_exit={clean.returncode} dirty_exit={dirty.returncode} path={absent}")
        scope = run([sys.executable, "-B", str(INSTR), "--lane", str(d), "--range", f"{c2}..{c3}"])
        sout = scope.stdout + scope.stderr
        legs["tree_scope"] = scope.returncode == 1 and "later/only.txt" in sout
        print(f"CAP2_TREE_SCOPE={'pass' if legs['tree_scope'] else 'fail'} "
              f"exit={scope.returncode} worktree_has_file={(d / 'later/only.txt').is_file()}")
    finally:
        shutil.rmtree(d, ignore_errors=True)

    cnt = run(["git", "-C", str(lane), "rev-list", "--count", rng]).stdout.strip()
    real = run([sys.executable, "-B", str(INSTR), "--lane", str(lane), "--range", rng])
    rout = real.stdout + real.stderr
    m = re.search(r"MESSAGE_TREE commits=(\d+) cited=(\d+) misses=(\d+)", rout)
    ok = False
    if m:
        commits, cited, misses = (int(m.group(k)) for k in (1, 2, 3))
        want_exit = 0 if misses == 0 else 1
        ok = (commits == int(cnt) and cited > 0 and real.returncode == want_exit)
    print(f"CAP2_REAL={'pass' if ok else 'fail'} "
          + (f"commits={m.group(1)}/{cnt} cited={m.group(2)} misses={m.group(3)} exit={real.returncode}"
             if m else "no summary line"))
    legs["real"] = ok

    good = all(legs.values())
    print("LEGS " + " ".join(f"{k}={'pass' if v else 'fail'}" for k, v in legs.items()))
    print(f"CAP2_VERDICT={'pass' if good else 'fail'}")
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
