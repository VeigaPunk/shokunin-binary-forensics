#!/usr/bin/env python3
"""Faithful-candidate blind-token control: pad every row's last cell with the
live tokens of the VALUE kinds only (listing, version, mcp, skill, pin), leaving
the base rows' own stale presence/import wording in place.

Usage: gen_junk2.py <instrument.py> <base-tree> <out-tree>
Reproduces reports/round-89/junk-control.log iff it prints that 7-line set.
"""
import importlib.util
import shutil
import sys
from pathlib import Path

VALUE_KINDS = {"listing", "version", "mcp", "skill", "pin"}


def load(path):
    spec = importlib.util.spec_from_file_location("instr", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main(argv):
    instr_path, base, out = Path(argv[0]), Path(argv[1]), Path(argv[2])
    m = load(instr_path)
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(base, out)
    tokens = []
    for rid in sorted(m.ROWS):
        for spec in m.ROWS[rid][1]:
            if spec[0] not in VALUE_KINDS:
                continue
            kind, arg, toks, _forbidden = m.live(spec)
            for t in toks:
                if t not in tokens:
                    tokens.append(t)
    for rel in (m.SEED, m.CHECK):
        p = out / rel
        body = []
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("|"):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                cells[-1] = cells[-1] + " " + " ".join(tokens)
                line = "| " + " | ".join(cells) + " |"
            body.append(line)
        p.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"JUNK2_TOKENS={len(tokens)}")
    print("TOKENS=" + " ".join(tokens))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
