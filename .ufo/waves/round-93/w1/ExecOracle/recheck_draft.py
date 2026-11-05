#!/usr/bin/env python3
"""ExecOracle r93w1: re-run every fenced command in the scribe draft (read-only).

A fenced block's command is its first line that starts with `python3 -B`
or `$ ` (the draft carries a `transcript —` label line above some commands;
the label is not a command). Output = the lines after the command line up to
the closing fence. Each command runs via the shell from the lane root; the
actual stdout lines (rstrip) are compared with the embedded output lines
(rstrip, blank lines dropped on both sides). Draft is never written.
"""
import hashlib
import subprocess
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
DRAFT = LANE / ".ufo/waves/round-93/w1/ScribeEntry/entry-draft.md"
WAVE = LANE / ".ufo/waves/round-93/w1/ExecOracle"

text = DRAFT.read_bytes()
draft_sha = hashlib.sha256(text).hexdigest()
lines = text.decode("utf-8").splitlines()

blocks = []
in_fence = False
open_no = None
cur = []
start = 0
for idx, ln in enumerate(lines, 1):
    if ln.strip().startswith("```"):
        if not in_fence:
            in_fence = True
            start = idx
            cur = []
        else:
            in_fence = False
            blocks.append((start, cur))
        continue
    if in_fence:
        cur.append((idx, ln))

rows = []
detail = []
n = 0
for start, body in blocks:
    cmd_pos = None
    for k, (lno, ln) in enumerate(body):
        s = ln.strip()
        if s.startswith("python3 -B") or s.startswith("$ "):
            cmd_pos = k
            break
    if cmd_pos is None:
        continue
    n += 1
    cmd_line = body[cmd_pos][1].strip()
    cmd = cmd_line[2:].strip() if cmd_line.startswith("$ ") else cmd_line
    emb = [ln.rstrip() for _, ln in body[cmd_pos + 1:] if ln.strip()]
    r = subprocess.run(cmd, shell=True, cwd=str(LANE), capture_output=True, text=True, timeout=600)
    act = [ln.rstrip() for ln in r.stdout.splitlines() if ln.strip()]
    match = emb == act
    single = cmd.replace("\t", " ")
    rows.append((n, single, "yes" if match else "no", r.returncode, len(emb), len(act), start))
    if not match:
        detail.append("=== block %d (opens draft line %d) MISMATCH exit=%d" % (n, start, r.returncode))
        detail.append("command: " + cmd)
        detail.append("embedded (%d lines):" % len(emb))
        detail += ["  E| " + x for x in emb]
        detail.append("actual (%d lines):" % len(act))
        detail += ["  A| " + x for x in act]
        if r.stderr.strip():
            detail.append("stderr: " + r.stderr.strip()[:400])
        detail.append("")

with (WAVE / "embedded-recheck.tsv").open("w", encoding="utf-8") as f:
    f.write("block_no\tcommand\tmatch\n")
    for no, cmd, m, rc, ne, na, st in rows:
        f.write("%d\t%s\t%s\n" % (no, cmd, m))
with (WAVE / "embedded-recheck-meta.tsv").open("w", encoding="utf-8") as f:
    f.write("block_no\topens_draft_line\texit_code\tembedded_lines\tactual_lines\tmatch\n")
    for no, cmd, m, rc, ne, na, st in rows:
        f.write("%d\t%d\t%d\t%d\t%d\t%s\n" % (no, st, rc, ne, na, m))
if detail:
    (WAVE / "embedded-recheck-mismatches.txt").write_text("\n".join(detail) + "\n", encoding="utf-8")
print("draft sha256=%s" % draft_sha)
print("fenced blocks=%d command blocks=%d" % (len(blocks), n))
print("match yes=%d no=%d" % (sum(1 for r in rows if r[2] == "yes"), sum(1 for r in rows if r[2] == "no")))
print("exit codes:", [r[3] for r in rows])
