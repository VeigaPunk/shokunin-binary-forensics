#!/usr/bin/env python3
"""CriticR99: re-run every derivation row of the amended C14 entry against its cited record.
Run with cwd = the 9ddd38ac extract root. Read-only. Prints one line per row:
ROW <status> rc=<codes> :: <row name>, where status is EXACT when the output cell's spans, joined
by ' / ', equal the command's stdout lines (trailing whitespace stripped) after dropping any
' — ' annotation; MISMATCH otherwise."""
import re, subprocess, sys
from pathlib import Path

ROOT = Path.cwd()
text = (ROOT / "corpus/knowledge/round-98-rea-host-readiness.md").read_text(encoding="utf-8")
lines = text.splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith("### Derivation table"))
end = next(i for i in range(start + 1, len(lines)) if lines[i].startswith("## "))


def split_row(l):
    # split on unescaped pipes only
    parts = re.split(r"(?<!\\)\|", l.strip())
    return [p.strip() for p in parts[1:-1]]


rows = []
for l in lines[start:end]:
    if l.startswith("|") and not re.match(r"^\|[-| ]+\|$", l) and not l.startswith("| Value"):
        c = split_row(l)
        if len(c) == 3:
            rows.append(c)
print("ROWS", len(rows))
bad = 0
for name, cmdcell, outcell in rows:
    cmds = re.findall(r"`([^`]+)`", cmdcell)
    if len(cmds) != 1:
        print("ROW NOCMD-SINGLE", name, len(cmds))
        bad += 1
        continue
    cmd = cmds[0].replace("\\|", "|")
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=str(ROOT))
    out_lines = [x.rstrip() for x in r.stdout.splitlines()]
    cell = outcell.split(" — ")[0]
    if name.startswith("record file digests"):
        # per-file: prefix span, file name in parentheses outside the span
        exp = re.findall(r"`([0-9a-f]{8})…` \(([^)]+)\)", cell)
        got = [(o[:8], o.split()[-1].split("/")[-1]) for o in out_lines]
        ok = [g[0] for g in got] == [e[0] for e in exp]
        print(f"ROW {'EXACT' if ok else 'MISMATCH'} rc={r.returncode} :: {name} :: got={[g[0] for g in got]} exp={[e[0] for e in exp]}")
        bad += (not ok)
        continue
    spans = re.findall(r"`([^`]+)`", cell)
    exp_lines = [s.replace("\\|", "|") for s in spans]
    if not spans:
        ok = False
    else:
        ok = exp_lines == out_lines
    if not ok and spans and " / " not in outcell and len(spans) == 1:
        ok = (spans[0].replace("\\|", "|") == "\n".join(out_lines))
    status = "EXACT" if ok else "MISMATCH"
    bad += (not ok)
    print(f"ROW {status} rc={r.returncode} :: {name}")
    if not ok:
        print("   stdout:", [x[:150] for x in out_lines][:8])
        print("   cell  :", [x[:150] for x in exp_lines][:8])
print("BAD_ROWS", bad)
