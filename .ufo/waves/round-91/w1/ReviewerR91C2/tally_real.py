#!/usr/bin/env python3
"""Per-commit citation tally over a git range: backticked spans + .log tokens.
ReviewerR91C2 analysis tool (read-only; runs only `git log/rev-list`)."""
import re
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/revenger-shokunin"
RNG = "7fab03f..refs/heads/main"


def g(*a):
    return subprocess.run(["git", "-C", LANE, *a], capture_output=True, text=True).stdout


commits = g("rev-list", "--reverse", RNG).split()
tot_spans = tot_logs = 0
for c in commits:
    msg = g("log", "-1", "--format=%B", c)
    spans = re.findall(r"`([^`]*)`", msg)
    logs = re.findall(r"[A-Za-z0-9._/-]+\.log\b", msg)
    tot_spans += len(spans)
    tot_logs += len(logs)
    line = f"{c[:9]} spans={len(spans)} logtoks={len(logs)}"
    if spans:
        line += "  spans=" + "|".join(spans)
    if logs:
        line += "  logs=" + "|".join(logs)
    print(line)
print(f"TOTAL commits={len(commits)} backticked_spans={tot_spans} log_tokens={tot_logs}")
