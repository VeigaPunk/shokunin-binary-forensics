#!/usr/bin/env python3
"""Critic control: classify every miss printed by reports/round-91/message_tree_check.py.

A miss is AMBIGUOUS when the cited bare filename matches >= 2 paths in that commit's
tree (the cited file exists, the instrument's unique-suffix rule refuses it); TRUE
when it matches 0 paths (the path is not in that commit's tree at all).

Usage: python3 -B classify_misses.py <LANE> <instrument-output.log>
"""
import re
import subprocess
import sys


def main(argv):
    repo, logf = argv[0], argv[1]
    amb = true = 0
    for line in open(logf, encoding="utf-8").read().splitlines():
        m = re.match(r"COMMIT ([0-9a-f]+) .*?missing=(\S+)", line)
        if not m:
            continue
        c, tok = m.group(1), m.group(2)
        names = subprocess.run(["git", "-C", repo, "ls-tree", "-r", "--name-only", c],
                               capture_output=True, text=True).stdout.splitlines()
        for p in tok.split(","):
            k = sum(1 for n in names if n == p or n.endswith("/" + p))
            kind = "AMBIGUOUS" if k >= 2 else "TRUE-MISS"
            if k >= 2:
                amb += 1
            else:
                true += 1
            print(f"{c[:7]} {p} suffix_matches={k} {kind}")
    print(f"CLASSIFY ambiguous={amb} true_miss={true} total={amb + true}")


if __name__ == "__main__":
    main(sys.argv[1:])
