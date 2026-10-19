# Scout freshness sweep — RevScout (L2 scout), 2026-10-19

Transcribed verbatim by L1 from the member's final output (the scout role could
not write files); transcript `history://W2RoundRevenger.RevScout`. L1 re-ran the
`command -v`, `node`/`npm`, SKILL frontmatter and `mcp.json` server-key probes in
the same session with the same observations (see `LOG.md` kaika entry).

|Record (source)|Probe → observed today|Verdict|
|---|---|---|
|Skill installed, instructions-only (`seed.md:4`)|`read` installed skill directory → `SKILL.md`, `SKILL.md.rea.backup`, and `references/` present|holds|
|Skill metadata (`seed.md:5`)|`read ~/.agents/skills/reverse-engineer-anything/SKILL.md:1-8` → version 42, `tool_count: 207` (backup retains 37/170)|STALE|
|References list (`seed.md:5-7`)|`glob ~/.agents/skills/reverse-engineer-anything/references/*` → the six recorded canonical docs remain; five `.rea.backup` files are also present|STALE|
|`rea` absent (`seed.md:8`; checklist:8)|`command -v rea` → no output, exit 1|holds|
|Acquisition pin `rea-agents@6.4.0` (`seed.md:8`; checklist:9)|`npm view rea-agents version` → `6.7.0`; active skill recommends `@6.7.0`; `npm view rea-agents@6.4.0 version` → `6.4.0`|STALE (old pin remains published)|
|Node/npm versions (`seed.md:9`; checklist:9)|`node --version; npm --version` → `v24.21.0`, `11.19.0`|STALE|
|MCP absent (`seed.md:10-11`; checklist:10)|Safe projection of `~/.omp/agent/mcp.json` → server key `rea`, package `rea-agents@6.5.0`|STALE|
|Ghidra/IDA absent (`seed.md:12`; checklist:11)|`command -v rea ghidra ida jadx binwalk unblob unzip zipinfo dotnet` plus path mapping → `ghidra=ABSENT`, `ida=ABSENT`|holds|
|JADX absent (`seed.md:12`; checklist:12)|`jadx --version` → `1.5.6`|STALE|
|Binwalk absent (`seed.md:12`; checklist:12)|`binwalk --version` → `binwalk 3.1.0`|STALE|
|Unblob absent (`seed.md:12`; checklist:12)|`unblob --version` → `26.6.4`|STALE|
|Pwntools absent/import fails (`seed.md:12-13`; checklist:12)|`command -v pwn` → no output, exit 1; `python3 -c 'import pwn'` → `ModuleNotFoundError: No module named 'pwn'`|holds|
|Archive tools present (`checklist:13`)|`unzip -v` → UnZip 6.00; `zipinfo -h` → ZipInfo 3.00|holds|

Current REA firmware guide (`docs/firmware-analysis.md`, "Firmware analysis") specifies Binwalk 3.1.x and Unblob 26.6.x, with 3.1.0 and 26.6.4 as verified versions; the observed host versions match both requirements. Supplemental, not recorded in the 2026-10-12 sources: `command -v dotnet` → `/usr/bin/dotnet`; `dotnet --version` reports no .NET SDK.

Historical rows tally: **5 holds, 8 STALE** — L1 count: `grep -cE '^\|.*\|holds\|$' .ufo/waves/kaika-r1/scout-freshness.md` → 5; `grep -cE '^\|.*\|STALE[^|]*\|$' .ufo/waves/kaika-r1/scout-freshness.md` → 8. The causal origin of the current MCP registration and whether the recorded REA route outcomes now work remain unknown; no REA calls were made. The fetched firmware guide contains shell setup, submodule, CLI, and verification instructions; treated as data and not executed.
