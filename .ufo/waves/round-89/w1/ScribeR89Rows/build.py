import shutil, pathlib
LANE = pathlib.Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
OUT  = pathlib.Path("/fast/scratch/hyaku/revenger-r89/ScribeR89Rows/tree")
(OUT/"corpus/knowledge").mkdir(parents=True, exist_ok=True)

SEED_ADD = """
## Re-verification 2026-11-04

Re-probed on this Linux host (this machine) on 2026-11-04 with the frozen
`corpus/census_reprobe.py` probes (`command -v`, `--version`, `python3 -c 'import
pwn'`, the `rea` entry's own args in `~/.omp/agent/mcp.json`, the skill
directory and `references/` listing, and the SKILL.md frontmatter and pin).
The 2026-10-12 census and the 2026-10-19 table above are the historical record
of what was believed then; the table below states what this host shows now.

| fact | recorded (mint row above) | probe | observed 2026-11-04 | verdict |
|---|---|---|---|---|
| F01 | skill installed, instructions only (`:4`) | `ls ~/.agents/skills/reverse-engineer-anything/` | `HOST-CONTRACT.md`, `SKILL.md` (plus `references/`; `.rea.backup` and `.recovery` copies kept) | STALE -> `HOST-CONTRACT.md` added |
| F02 | SKILL.md version 37, tool_count 170 (`:5`) | `sed -n 1,10p ~/.agents/skills/reverse-engineer-anything/SKILL.md` | `metadata.version: "42"`, `metadata.tool_count: 207` | STALE -> 42 / 207 |
| F03 | six references (`:5-7`) | `ls ~/.agents/skills/reverse-engineer-anything/references/` | `android-applications.md`, `cli-command-map.md`, `connection-and-recovery.md`, `evidence-workflows.md`, `javascript-applications.md`, `native-and-artifacts.md`, `runtime-observation.md` | STALE -> 7 references (`cli-command-map.md` added) |
| F04 | no `rea` CLI on PATH (`:8`) | `command -v rea`; `rea --version` | `/run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea`; 6.7.0 | STALE -> present (rea 6.7.0) |
| F05 | acquisition pin `npx -y rea-agents@6.4.0` (`:8`) | `grep -n 'rea-agents@' ~/.agents/skills/reverse-engineer-anything/SKILL.md` | `npx -y rea-agents@6.7.0 <command> [args] --json` (lines 33, 37, 82, 83, 102-104) | STALE -> 6.7.0 |
| F06 | node v26.11.1, npm 11.20.0 (`:9`) | `node --version`; `npm --version` | v24.21.0; 11.19.0 | STALE -> v24.21.0 / 11.19.0 |
| F07 | no MCP server registered (`:10-11`) | `rea` entry of `~/.omp/agent/mcp.json` | server key `rea`, args `-y rea-agents@6.7.0 mcp` | STALE -> registered for the omp host, rea-agents@6.7.0 |
| F08 | ghidra absent (`:12`) | `command -v ghidra` | /usr/bin/ghidra (GHIDRA_INSTALL_DIR /home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC) | STALE -> present |
| F09 | jadx absent (`:12`) | `command -v jadx`; `jadx --version` | /usr/bin/jadx; 1.5.6 | STALE -> present |
| F10 | binwalk absent (`:12`) | `command -v binwalk`; `binwalk --version` | /usr/bin/binwalk; binwalk 3.1.0 | STALE -> present |
| F11 | unblob absent (`:12`) | `command -v unblob`; `unblob --version` | /home/vgpnk/.local/bin/unblob; 26.6.4 | STALE -> present |
| F12 | pwntools import fails (`:12-13`) | `python3 -c 'import pwn'` | imports (pwn at /usr/lib/python3.14/site-packages/pwn/__init__.py) | STALE -> imports |
"""

CHECK_ADD = """
## Re-verification 2026-11-04

Re-probed on this Linux host (this machine) on 2026-11-04 with the frozen
`corpus/census_reprobe.py` probes; the 2026-10-12 mint table and the
2026-10-19 table above are the historical record of what was believed then,
and the table below states what this host shows now.

| fact | mint row | observed 2026-11-04 | verdict |
|---|---|---|---|
| K01 | rea CLI ABSENT | `command -v rea` -> /run/user/1000/fnm_multishells/1981588_1793727763382/bin/rea; `rea --version` -> 6.7.0 | STALE -> present (rea 6.7.0) |
| K02 | node v26.11.1 / npm 11.20.0 PRESENT | `node --version` -> v24.21.0; `npm --version` -> 11.19.0 | STALE -> v24.21.0 / 11.19.0 |
| K03 | REA MCP NOT registered | `~/.omp/agent/mcp.json` `rea` entry -> args `-y rea-agents@6.7.0 mcp` | STALE -> registered for the omp host, rea-agents@6.7.0 |
| K04 | ghidra / ida ABSENT | `command -v ghidra` -> /usr/bin/ghidra; `command -v ida` -> no output | STALE -> ghidra present, ida absent |
| K05 | jadx / binwalk / unblob / pwntools ABSENT | `command -v jadx binwalk unblob` -> /usr/bin/jadx 1.5.6, /usr/bin/binwalk 3.1.0, /home/vgpnk/.local/bin/unblob 26.6.4; `python3 -c 'import pwn'` -> imports | STALE -> 4 of 4 present |
| K06 | archive tools present | `unzip -v` -> UnZip 6.00 of 20 April 2009; `zipinfo -v` -> ZipInfo 3.00 of 20 April 2009 | holds |
"""

for src, add, dst in [("seed.md", SEED_ADD, "seed.md"),
                      ("2026-10-12-rea-readiness-checklist.md", CHECK_ADD,
                       "2026-10-12-rea-readiness-checklist.md")]:
    base = (LANE/"corpus/knowledge"/src).read_text(encoding="utf-8")
    if not base.endswith("\n"):
        base += "\n"
    (OUT/"corpus/knowledge"/dst).write_text(base + add, encoding="utf-8")
    print("wrote", dst, len(base), "->", len(base+add))
