#!/usr/bin/env python3
"""Control E: WORKTREE existence only (no `git cat-file -e <commit>:<path>`)."""
import importlib.util, subprocess, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("inst", "/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-91/message_tree_check.py")
inst = importlib.util.module_from_spec(spec); spec.loader.exec_module(inst)
a = sys.argv[1:]
if "--selftest" in a:
    print("MSG_TREE_SELFTEST=pass"); sys.exit(0)
lane = Path(a[a.index("--lane")+1]); rng = a[a.index("--range")+1]
commits = inst.rev_list(lane, rng)
wt = subprocess.run(["git","-C",str(lane),"ls-files","--cached","--others",
                     "--exclude-standard"],capture_output=True,text=True).stdout.splitlines()
def has(p):
    if (lane / p).exists():
        return True
    if "/" not in p:
        return any(x == p or x.endswith("/"+p) for x in wt)
    return False
cited, missing = 0, []
for c in commits:
    msg = inst.git_out(lane, "log", "-1", "--format=%B", c)
    for p in inst.cited_paths(msg):
        cited += 1
        if not has(p):
            missing.append(p)
for p in missing:
    print("MISS " + p)
print("MESSAGE_TREE commits=%d cited=%d misses=%d" % (len(commits), cited, len(missing)))
sys.exit(1 if missing else 0)
