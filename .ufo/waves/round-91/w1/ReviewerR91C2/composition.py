#!/usr/bin/env python3
"""Exact per-token composition of the instrument's citations for the 5 real
commits, using the instrument's own loaded functions (no reimplementation)."""
import importlib.util
import subprocess

LANE = "/home/vgpnk/Projects/shokunin/revenger-shokunin"
INSTR = LANE + "/reports/round-91/message_tree_check.py"

spec = importlib.util.spec_from_file_location("mtc", INSTR)
mtc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mtc)

PICKS = ["d509e982844d31bd26f3cb96e1a663e7d36f2ca8",
         "b13aac756ac33aa5245c13966c624de4370206d0",
         "45b27135d", "6ce41aabc", "5f7ecce6a"]

for c in PICKS:
    full = subprocess.run(["git", "-C", LANE, "rev-parse", c],
                          capture_output=True, text=True).stdout.strip()
    msg = subprocess.run(["git", "-C", LANE, "log", "-1", "--format=%B", full],
                         capture_output=True, text=True).stdout
    names = subprocess.run(["git", "-C", LANE, "ls-tree", "-r", "--name-only", full],
                           capture_output=True, text=True).stdout.splitlines()
    cited = mtc.cited_paths(msg)
    print(f"== {c} cited={len(cited)}")
    for p in cited:
        v = mtc.resolve(LANE, full, p, names)
        extra = ""
        if v == "miss" and "/" not in p:
            hits = [n for n in names if n.endswith("/" + p)]
            extra = f"  suffix_hits={len(hits)} {hits[:3]}"
        print(f"   {p} -> {v}{extra}")
