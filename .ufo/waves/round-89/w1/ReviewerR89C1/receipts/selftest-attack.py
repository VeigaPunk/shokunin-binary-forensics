#!/usr/bin/env python3
"""Selftest mutation battery for corpus/census_reprobe.py. Scratch copies only."""
import shutil
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/revenger-r89/ReviewerR89C1")
GATE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/census_reprobe.py")
SRC = GATE.read_text()

MUT = {
 "M1-exactness": ("legs.append((name, len(hit) >= 1, f2))",
                  "legs.append((name, len(hit) == 1, f2))"),
 "M2-main-dead": ('    if "--json" in argv:',
                  '    print("CENSUS_ROWS=18")\n    print("CENSUS_STALE_UNFLAGGED=0")\n    return 0\n    if "--json" in argv:'),
 "M3-presence-no-forbidden": ('        return (kind, arg, ["present"] if on else ["absent"],\n                ["absent"] if on else ["present"])',
                              '        return (kind, arg, ["present"] if on else ["absent"], [])'),
 "M4-no-phantom": ("                if phantom:", "                if False and phantom:"),
 "M5-no-missing-token": ("                if tok.lower() not in text:", "                if False and tok.lower() not in text:"),
 "M6-score-whole-line": ('    return " | ".join(cells[-2:]) if len(cells) >= 2 else line', "    return line"),
 "M3b-no-forbidden-at-all": ("                bad = [w for w in forbidden if w.lower() in text]", "                bad = []"),
 "M6b-score-three-cells": ('    return " | ".join(cells[-2:]) if len(cells) >= 2 else line', '    return " | ".join(cells[-3:]) if len(cells) >= 3 else line'),
 "M7-file-attribution": ("                lines[m.group(1)] = line",
                         "                lines[(key, m.group(1))] = line"),
}
MUT7B = ("        line = lines.get(rid)", "        line = lines.get((ROWS[rid][0], rid))")


def patch(name, pairs):
    p = S / f"mut-{name}.py"
    body = SRC
    for old, new in pairs:
        assert body.count(old) == 1, (name, old, body.count(old))
        body = body.replace(old, new)
    p.write_text(body)
    return p


def run(p, argv, tag):
    r = subprocess.run([sys.executable, "-B", str(p)] + argv, capture_output=True, text=True)
    (S / f"{tag}.log").write_text(r.stdout + f"EXIT={r.returncode}\n" + r.stderr)
    return r


print("== baseline: real instrument ==")
b = run(GATE, ["--selftest"], "mut-baseline-selftest")
print(f"selftest exit={b.returncode} pass={'CENSUS_SELFTEST=pass' in b.stdout}")

for name, pair in MUT.items():
    pairs = [pair] + ([MUT7B] if name == "M7-file-attribution" else [])
    p = patch(name, pairs)
    r = run(p, ["--selftest"], f"mut-{name}-selftest")
    failed = [l for l in r.stdout.splitlines() if l.startswith("CENSUS_SELFTEST_") and l.endswith("=FAIL")]
    print(f"{name}: selftest_exit={r.returncode} caught={bool(failed)} failing_legs={[l.split('_')[2].split('=')[0] for l in failed]}")

print("\n== M2-main-dead against a real tree (base archive) ==")
p = S / "mut-M2-main-dead.py"
r = run(p, ["--root", str(S / "base")], "mut-M2-main-dead-base")
print(f"base tree under dead main: exit={r.returncode} out={r.stdout.strip().splitlines()[-1]}")

print("\n== M7-file-attribution against the F-rows-in-checklist tree ==")
t = S / "frows-in-check"
if t.exists():
    shutil.rmtree(t)
shutil.copytree(S / "base", t)
sys.path.insert(0, str(S))
import build  # noqa: E402  (reuses HONEST/CHECK/SEED, also re-runs its own scoring prints)

p = t / build.CHECK
p.write_text(p.read_text().rstrip("\n") + "\n\n## Re-verification 2026-11-04\n\n" +
             "\n".join(build.HONEST[k] for k in build.HONEST if k.startswith("F")) + "\n")
for gate, tag in ((GATE, "score-frows-in-check-real"), (S / "mut-M7-file-attribution.py", "score-frows-in-check-M7")):
    r = run(gate, ["--root", str(t)], tag)
    ids = [l.split()[1] for l in r.stdout.splitlines() if l.startswith("CENSUS_MISMATCH")]
    cnt = [l for l in r.stdout.splitlines() if l.startswith("CENSUS_STALE_UNFLAGGED")]
    print(f"{tag}: {cnt[0]} exit={r.returncode} ids={ids}")
