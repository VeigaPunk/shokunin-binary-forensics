#!/usr/bin/env python3
"""Critic control: the C2 extraction rule EXACTLY as frozen in claims.md §C2.

claims.md: "extracts every backticked repo-relative path and every `.log` filename
cited in each commit message, and checks each against that commit's own tree
(`git cat-file -e <c>:<path>`; bare filenames resolve by suffix match and are
reported as `bare`)."

Usage: python3 -B spec_extract.py <LANE> <A..B>
Prints COMMIT lines and the MESSAGE_TREE summary; exit 0 iff misses == 0.
"""
import re
import subprocess
import sys

BT = re.compile(r"`([^`\s]+)`")
LOG = re.compile(r"[\w./-]+\.log")


def git(repo, *a):
    return subprocess.run(["git", "-C", repo, *a], capture_output=True, text=True)


def main(argv):
    repo, rng = argv[0], argv[1]
    commits = git(repo, "rev-list", rng).stdout.split()
    cited = misses = 0
    for c in commits:
        msg = git(repo, "log", "-1", "--format=%B", c).stdout
        names = git(repo, "ls-tree", "-r", "--name-only", c).stdout.splitlines()
        spec = set()
        for t in BT.findall(msg):
            t = t.rstrip(".,;:)")
            if any(ch in t for ch in "<>*…") or t.startswith(("http", "/")):
                continue
            if "/" in t or "." in t.split("/")[-1]:
                spec.add(t)
        for t in LOG.findall(msg):
            t = t.rstrip(".,;:)")
            if t:
                spec.add(t)
        miss = []
        for p in sorted(spec):
            if "/" in p:
                hit = git(repo, "cat-file", "-e", f"{c}:{p}").returncode == 0
            else:
                hits = [n for n in names if n == p or n.endswith("/" + p)]
                hit = len(hits) == 1
            if not hit:
                miss.append(p)
        cited += len(spec)
        misses += len(miss)
        print(f"COMMIT {c} cited={len(spec)} misses={len(miss)}"
              + (f" missing={','.join(miss)}" if miss else ""))
    print(f"MESSAGE_TREE commits={len(commits)} cited={cited} misses={misses}")
    return 0 if misses == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
