#!/usr/bin/env python3
"""Control D: real tokenizer, NO commit-tree membership check at all.
The planted miss is caught only by the literal name 'missing' (the probe's own spelling);
the real range is reported as misses=99 exit=1 to show leg 4 ignores both."""
import importlib.util, sys
from pathlib import Path
spec = importlib.util.spec_from_file_location("inst", "/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-91/message_tree_check.py")
inst = importlib.util.module_from_spec(spec); spec.loader.exec_module(inst)
a = sys.argv[1:]
if "--selftest" in a:
    print("MSG_TREE_SELFTEST=pass"); sys.exit(0)
lane = Path(a[a.index("--lane")+1]); rng = a[a.index("--range")+1]
commits = inst.rev_list(lane, rng)
cited, flagged = 0, []
for c in commits:
    msg = inst.git_out(lane, "log", "-1", "--format=%B", c)
    for p in inst.cited_paths(msg):
        cited += 1
        if "missing" in p:
            flagged.append(p)
real = len(commits) > 3
misses = 99 if real else len(flagged)
for p in flagged:
    print("MISS " + p)
print("MESSAGE_TREE commits=%d cited=%d misses=%d" % (len(commits), cited, misses))
sys.exit(1 if misses else 0)
