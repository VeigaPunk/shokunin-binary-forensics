source: S001 — `.ufo/waves/kaika-r1/scout-freshness.md` — host re-probe table, 2026-10-19; S002 — `~/.agents/skills/reverse-engineer-anything/SKILL.md` — frontmatter `metadata.version: "42"`, `tool_count: 207`
verified-at: 2026-10-19 — census re-probed; 7 of 12 census facts stale, each flagged in `## Re-verification 2026-10-19`; the text between the headers and that section is the unchanged 2026-10-12 record
recheck: `command -v rea ghidra ida jadx binwalk unblob; node --version; npm --version; npm view rea-agents version; sed -n 1,8p ~/.agents/skills/reverse-engineer-anything/SKILL.md; python3 -c 'import pwn'`
coverage-map: C02, C10, C12, C14

# revenger seed knowledge

## REA toolset census (probed 2026-10-12, commands + outputs on record)
- Skill installed (instructions only): ~/.agents/skills/reverse-engineer-anything/
  SKILL.md (version 37, tool_count 170 declared) + references/
  (connection-and-recovery, native-and-artifacts, javascript-applications,
  android-applications, runtime-observation, evidence-workflows)
- NO `rea` CLI on PATH; acquisition path per skill: `npx -y rea-agents@6.4.0`
  (node v26.11.1, npm 11.20.0 present)
- NO MCP server registered by the skill install — REA tools arrive only
  after the agent connects the server or uses the CLI
- Host engines ABSENT at mint: ghidra, jadx, binwalk, unblob, pwntools
  (not on PATH; pwntools import fails). REA treats these as caller-supplied;
  their absence caps, but does not block, archive/JS/layout routes.

## Verification discipline (the lane's core rule)
Every REA conclusion is ledger-bound: observation vs inference vs unknown,
each tied to an Evidence ID from the active REA session (or an exported
evidence bundle for replay). A claim without a cited Evidence ID is a
hypothesis, not a finding. Runtime observation is used only when static
evidence cannot answer, and only against the declared target + lifecycle.
Version comparisons and reconstruction guidance keep observed behavior
separate from design choices.

## Calibration strategy (the lane's distinct craft)
Reverse engineering has a ground-truth problem: on unknown targets you
cannot score your own findings. The lane therefore keeps a fixture bench of
LOCALLY BUILT binaries/packages (compiled here from source the lane writes)
where the truth is known by construction; REA findings on fixtures are
scored against that truth before the same procedure is trusted on unknown
artifacts. Fixture provenance (source, compiler, flags, SHA-256) is part of
the fixture record.

## Investigation map (candidate round claims, north to south)
readiness: rea CLI via npx → MCP registration check → session open/close
           on a fixture binary
fixtures:  hello-world C (symbols) → stripped → packed archive member →
           .NET/managed if host engine appears
practice:  JS/Electron fixture (known source) → feature trace vs truth
targets:  demand context ~/Projects/gamez/research/ (decomp/recomp
           interest) supplies later real investigations

## Re-verification 2026-10-19

Appended correction; the census above is kept as the 2026-10-12 record. Probes
and outputs: `.ufo/waves/kaika-r1/scout-freshness.md` (L2 scout), re-run by L1
the same day. Verdict per recorded fact (`holds` / `STALE` → current value).

| fact | recorded (line above) | probe | observed 2026-10-19 | verdict |
|---|---|---|---|---|
| F01 | skill installed, instructions only (`:4`) | `ls ~/.agents/skills/reverse-engineer-anything/` | `SKILL.md`, `references/` (plus `SKILL.md.rea.backup`) | holds |
| F02 | SKILL.md version 37, tool_count 170 (`:5`) | `sed -n 1,8p …/SKILL.md` | version 42, tool_count 207; the backup keeps 37/170 | STALE → 42 / 207 |
| F03 | six references (`:5-7`) | `ls …/references/` | same six names; five rewritten 2026-10-14 with `.rea.backup` copies kept | holds (names); content revised |
| F04 | no `rea` CLI on PATH (`:8`) | `command -v rea` | no output, exit 1 | holds |
| F05 | acquisition pin `npx -y rea-agents@6.4.0` (`:8`) | `npm view rea-agents version`; `grep -n 'rea-agents@' …/SKILL.md` | latest 6.7.0; skill now names `rea-agents@6.7.0`; 6.4.0 still published | STALE → 6.7.0 (6.4.0 remains the saved-record producer version) |
| F06 | node v26.11.1, npm 11.20.0 (`:9`) | `node --version; npm --version` | v24.21.0, 11.19.0 | STALE → v24.21.0 / 11.19.0 |
| F07 | no MCP server registered (`:10-11`) | server keys in `~/.omp/agent/mcp.json` (no values read) | key `rea`, package `rea-agents@6.5.0` | STALE → registered for the omp host |
| F08 | ghidra absent (`:12`) | `command -v ghidra` | absent | holds |
| F09 | jadx absent (`:12`) | `jadx --version` | 1.5.6 | STALE → present |
| F10 | binwalk absent (`:12`) | `binwalk --version` | binwalk 3.1.0 | STALE → present |
| F11 | unblob absent (`:12`) | `unblob --version` | 26.6.4 | STALE → present |
| F12 | pwntools import fails (`:12-13`) | `python3 -c 'import pwn'` | `ModuleNotFoundError: No module named 'pwn'` | holds |

Not re-verified here: the routes the new engines unblock. Presence is not
capability (`corpus/QUALITY.md` Q05); no REA call was made. `dotnet` is on PATH
but reports no installed .NET SDK, so it cannot yet build a managed fixture.
