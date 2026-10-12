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
