#!/usr/bin/env python3
"""Audit every SOURCES.md row's used-by cell against the entry bytes it names.

For a row Sxxx whose used-by cell names knowledge/<file>.md (optionally corpus/-prefixed),
grounded means: corpus/knowledge/<file>.md exists in the same tree and its text cites
the token Sxxx. Prints one line per row: sid, used-by target, exists, cites, VERDICT.
Usage: usedby_audit.py <tree-root>
"""
import re
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve()
src = (root / "corpus/SOURCES.md").read_text(encoding="utf-8")
bad = 0
checked = 0
for ln in src.splitlines():
    if not re.match(r"^ {0,3}\|[ \t]*S[0-9]{3,}[ \t]*\|", ln):
        continue
    c = [x.strip() for x in ln.strip().strip("|").split("|")]
    if len(c) != 11:
        print(f"{c[0] if c else '?'}: MALFORMED row ({len(c)} cells)")
        bad += 1
        continue
    sid = c[0]
    ub = [x.strip() for x in c[10].split(",") if x.strip() and x.strip() != "\u2014"]
    if not ub:
        print(f"{sid}: used-by empty (out of leg scope)")
        continue
    for tgt in ub:
        rel = tgt[len("corpus/"):] if tgt.startswith("corpus/") else tgt
        p = root / "corpus" / rel
        exists = p.is_file()
        cites = exists and bool(re.search(rf"\b{sid}\b", p.read_text(encoding="utf-8")))
        checked += 1
        verdict = "GROUNDED" if (exists and cites) else "UNGROUND"
        if verdict == "UNGROUND":
            bad += 1
        print(f"{sid}: used-by={tgt} exists={exists} cites={cites} -> {verdict}")
print(f"checked={checked} ungrounded={bad}")
