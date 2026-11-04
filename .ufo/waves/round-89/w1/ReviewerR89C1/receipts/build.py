#!/usr/bin/env python3
"""Build attack trees for the round-89 C1 census gate. Scratch only."""
import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

S = Path("/fast/scratch/hyaku/revenger-r89/ReviewerR89C1")
LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
GATE = LANE / "corpus/census_reprobe.py"

spec = importlib.util.spec_from_file_location("cr", GATE)
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)

# enumerate the live tokens exactly as the gate derives them
LIVE = {}
for rid in sorted(cr.ROWS):
    key, specs = cr.ROWS[rid]
    LIVE[rid] = [(s, cr.live(s)) for s in specs]
print("== live probe table (gate's own functions) ==")
for rid in sorted(LIVE):
    for s, (kind, arg, toks, forb) in LIVE[rid]:
        print(f"{rid} {kind}:{arg} tokens={toks} forbidden={forb}")

SEED = "corpus/knowledge/seed.md"
CHECK = "corpus/knowledge/2026-10-12-rea-readiness-checklist.md"

HONEST = {
 "F01": "| F01 | mint | `ls ~/.agents/skills/reverse-engineer-anything/` | `HOST-CONTRACT.md`, `SKILL.md` | present 2026-11-04 |",
 "F02": "| F02 | mint | `sed -n 1,8p SKILL.md` | version 42, tool_count 207 | current 2026-11-04 |",
 "F03": "| F03 | mint | `ls references/` | android-applications.md, cli-command-map.md, connection-and-recovery.md, evidence-workflows.md, javascript-applications.md, native-and-artifacts.md, runtime-observation.md | present 2026-11-04 |",
 "F04": "| F04 | mint | `command -v rea` | present at /run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea (6.7.0) | present 2026-11-04 |",
 "F05": "| F05 | mint | `grep rea-agents@ SKILL.md` | `rea-agents@6.7.0` | current 2026-11-04 |",
 "F06": "| F06 | mint | `node --version; npm --version` | node v24.21.0, npm 11.19.0 | present 2026-11-04 |",
 "F07": "| F07 | mint | `mcp.json` key `rea` | `rea-agents@6.7.0` | registered 2026-11-04 |",
 "F08": "| F08 | mint | `command -v ghidra` | present at /usr/bin/ghidra | present 2026-11-04 |",
 "F09": "| F09 | mint | `command -v jadx` | present at /usr/bin/jadx (1.5.6) | present 2026-11-04 |",
 "F10": "| F10 | mint | `command -v binwalk` | present at /usr/bin/binwalk (3.1.0) | present 2026-11-04 |",
 "F11": "| F11 | mint | `command -v unblob` | present at /home/vgpnk/.local/bin/unblob (26.6.4) | present 2026-11-04 |",
 "F12": "| F12 | mint | `python3 -c 'import pwn'` | imports (pwntools, /usr/lib/python3.14/site-packages/pwn) | imports 2026-11-04 |",
 "K01": "| K01 | mint ABSENT | present at /run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea | present 2026-11-04 |",
 "K02": "| K02 | mint | node v24.21.0 / npm 11.19.0 | present 2026-11-04 |",
 "K03": "| K03 | mint NOT registered | `rea-agents@6.7.0` | registered 2026-11-04 |",
 "K04": "| K04 | mint ABSENT | ghidra present at /usr/bin/ghidra; ida absent (`command -v ida` prints nothing) | mixed 2026-11-04 |",
 "K05": "| K05 | mint ABSENT | jadx present, binwalk present, unblob present; pwn imports | present 2026-11-04 |",
 "K06": "| K06 | mint present | UnZip 6.00, ZipInfo 3.00 | present 2026-11-04 |",
}

# every live token present, opposite asserted, no forbidden literal used
OPPOSITE = {
 "F01": "| F01 | mint | `ls` | `HOST-CONTRACT.md` not found in the directory | `SKILL.md` only, nothing else |",
 "F02": "| F02 | mint | `sed` | not version 42 and not tool_count 207 - SKILL.md declares 37 / 170 | wrong 2026-11-04 |",
 "F03": "| F03 | mint | `ls references/` | none of android-applications.md, cli-command-map.md, connection-and-recovery.md, evidence-workflows.md, javascript-applications.md, native-and-artifacts.md, runtime-observation.md exists | directory empty 2026-11-04 |",
 "F04": "| F04 | mint | `command -v rea` | not present - `command -v` prints nothing | nothing found 2026-11-04 |",
 "F05": "| F05 | mint | `grep` | `rea-agents@6.7.0` is not the skill pin; SKILL.md pins 6.4.0 | wrong 2026-11-04 |",
 "F06": "| F06 | mint | `node --version; npm --version` | not 24.21.0 and not 11.19.0 - node prints v26.11.1, npm 11.20.0 | wrong 2026-11-04 |",
 "F07": "| F07 | mint | `mcp.json` | `rea-agents@6.7.0` is the published package, not this host entry; no `rea` key exists | not registered 2026-11-04 |",
 "F08": "| F08 | mint | `command -v ghidra` | not present - prints nothing | nothing found 2026-11-04 |",
 "F09": "| F09 | mint | `command -v jadx` | not present - prints nothing | nothing found 2026-11-04 |",
 "F10": "| F10 | mint | `command -v binwalk` | not present - prints nothing | nothing found 2026-11-04 |",
 "F11": "| F11 | mint | `command -v unblob` | not present - prints nothing | nothing found 2026-11-04 |",
 "F12": "| F12 | mint | `python3 -c 'import pwn'` | imports? no - raises ImportError | does not import 2026-11-04 |",
 "K01": "| K01 | mint ABSENT | not present - prints nothing | nothing found 2026-11-04 |",
 "K02": "| K02 | mint | not 24.21.0 / not 11.19.0 - node v26.11.1, npm 11.20.0 | wrong 2026-11-04 |",
 "K03": "| K03 | mint NOT registered | `rea-agents@6.7.0` is the published package; no `rea` key | not registered 2026-11-04 |",
 "K04": "| K04 | mint ABSENT | ghidra present at /usr/bin/ghidra; ida absent (`command -v ida` prints nothing) | mixed 2026-11-04 |",
 "K05": "| K05 | mint ABSENT | jadx, binwalk, unblob not present; imports? no - ImportError | nothing found 2026-11-04 |",
 "K06": "| K06 | mint present | not 6.00 / not 3.00 - host has no unzip | nothing found 2026-11-04 |",
}


def tree(name, rows, seed_extra=None, check_extra=None):
    d = S / name
    if d.exists():
        shutil.rmtree(d)
    shutil.copytree(S / "base", d)
    for fname, ids in (("seed", [k for k in rows if k.startswith("F")]),
                       ("check", [k for k in rows if k.startswith("K")])):
        p = d / (SEED if fname == "seed" else CHECK)
        body = p.read_text().rstrip("\n")
        block = ["", "## Re-verification 2026-11-04", "",
                 "| fact | mint | probe/observed | verdict |", "|---|---|---|---|"]
        block += [rows[i] for i in ids]
        p.write_text(body + "\n" + "\n".join(block) + "\n")
    if seed_extra:
        p = d / SEED
        p.write_text(p.read_text().rstrip("\n") + "\n" + seed_extra + "\n")
    return d


def run(root, tag, env=None):
    e = None
    if env:
        import os
        e = dict(os.environ)
        e.update(env)
    r = subprocess.run([sys.executable, "-B", str(GATE), "--root", str(root)],
                       capture_output=True, text=True, env=e)
    out = r.stdout
    count = [l for l in out.splitlines() if l.startswith("CENSUS_STALE_UNFLAGGED")]
    ids = [l.split()[1] for l in out.splitlines() if l.startswith("CENSUS_MISMATCH")]
    (S / f"{tag}.log").write_text(out + f"EXIT={r.returncode}\n" + r.stderr)
    print(f"-- {tag}: {count[0] if count else '?'} exit={r.returncode} ids={ids}")
    return out, r.returncode


print("\n== tree scores ==")
run(tree("honest", HONEST), "score-honest")
run(tree("opposite", OPPOSITE), "score-opposite")
red1 = dict(HONEST)
red1["F08"] = "| F08 | mint | `command -v ghidra` | on PATH at /usr/bin/ghidra | current 2026-11-04 |"
run(tree("honest-wording", red1), "score-honest-wording")

# misplaced rows: corrected K rows appended to seed.md, checklist left stale
mis = S / "misplaced"
if mis.exists():
    shutil.rmtree(mis)
shutil.copytree(S / "base", mis)
p = mis / SEED
p.write_text(p.read_text().rstrip("\n") + "\n\n## Re-verification 2026-11-04\n\n" +
             "\n".join(HONEST[k] for k in HONEST if k.startswith("K")) + "\n")
run(mis, "score-misplaced")
