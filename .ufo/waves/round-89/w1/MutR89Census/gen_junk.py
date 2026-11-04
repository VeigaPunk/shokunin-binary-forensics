#!/usr/bin/env python3
"""Reconstruct the round-89 blind-token control tree and attribute selftest plants.

Usage: gen_junk.py <instrument.py> <base-tree> <out-tree>
Copies the base census tree, then appends EVERY live token the instrument derives
(from all 18 rows' probes) to every row's last cell. Faithful iff the pristine
instrument then prints the 7-line receipt of reports/round-89/junk-control.log.
"""
import importlib.util
import shutil
import sys
from pathlib import Path


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
    print(f"JUNK_TOKENS={len(tokens)}")
    print("TOKENS=" + " ".join(tokens))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
