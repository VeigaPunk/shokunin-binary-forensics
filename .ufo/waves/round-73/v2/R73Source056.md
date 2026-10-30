# R73Source056 — S056 source audit (GhidraMCP)

Seat: R73Source056 (leaf, read-only). Lane root: /home/vgpnk/Projects/shokunin/revenger-shokunin.
Assigned row only: S056. No source admission proposed; no file written except this report.
Verdict: **AGREE** with the round-72 disposition (ADMIT, tier A).

## Located quote (verbatim, ≤25 words)

> "MCP Server + Ghidra Plugin"

Word count: 5. Location in cited source: README.md, `# Features` section, first line (fetched file line 18).

- URL: https://github.com/LaurieWired/GhidraMCP
- Pin: commit `1e980252087b2479a21b9ca6d82d5829538651a7` ("Update readme", committer date 2026-10-10T19:17:31Z) — confirmed via GitHub API.
- Fetch target: `https://raw.githubusercontent.com/LaurieWired/GhidraMCP/1e980252087b2479a21b9ca6d82d5829538651a7/README.md`
- Fetched bytes: 5151; sha256 `b82f32e9e36d55c9a7b0d7578a650312b5f319551e2d4a0870552e4895e61850`.
- Re-access date (this audit): **2026-10-30**.

## Verbatim comparison (normalizing markup only)

| item | registry/lesson wording | pinned source text | result |
|---|---|---|---|
| located quote | "MCP Server + Ghidra Plugin" (SOURCES.md S056 row; lesson round-72.md row S056) | line 18: `MCP Server + Ghidra Plugin` | VERBATIM MATCH (observation) |
| located anchor | README.md "Features" and "Prerequisites" | `# Features` (line 16), `## Prerequisites` (line 26) | MATCH (observation) |
| scope bound: Ghidra version as setup constraint | "the advertised Ghidra version is a setup constraint, not a run result" | line 27: `- Install [Ghidra](https://ghidra-sre.org) 12.1.4`; lines 31–36 install steps for `ghidra_12.1.4_PUBLIC_<date>_GhidraMCP.zip` | SUPPORTED (observation) |
| capability summary | "MCP/plugin bridge with decompile/analyze and method/class/import/export listing" | lines 20–22: "Decompile and analyze binaries in Ghidra"; "Automatically rename methods and data"; "List methods, classes, imports, and exports" | ACCURATE (observation) |
| scope exclusion "not execution or provider readiness" | row scope column | README makes declared-feature statements only; no host-run or readiness claim | CONSISTENT (observation) |

## Disposition checks

- **Scope**: row scope ("README feature declaration and Ghidra bridge prerequisites only") matches the pinned README exactly. Observation.
- **Tier A**: primary project README at a pinned commit — correct tier. Observation.
- **Used-by**: `corpus/knowledge/round-72-tool-landscape.md` (SOURCES.md column 11). The knowledge entry (README-row "Need native disassembly/decompilation and analysis") states "GhidraMCP documents a Ghidra plugin/MCP bridge." — supported by line 18 and the intro ("Model Context Protocol server ... exposes numerous tools from core Ghidra functionality to MCP clients"). Accurate. Observation.
- **Rejection flip**: no flip condition is attached to S056; nothing in the pinned README contradicts the admitted scope, and the row claims nothing beyond the README. No flip warranted. Observation.
- **Lesson entry**: round-72.md row S056 — "ADMIT, tier A for this repository's documented bridge; no claim that it is uniquely or most widely used." **Agree**; the row does not assert uniqueness/prevalence. Observation.

## Routed-defect context (S071/S082)

Round-72-verifier-spotcheck.md routes S071 (paraphrased registry quote) and S082 (misattributed quote) as append-only superseding-row defects. That duty belongs to those rows' seats; this seat proposes **no** new row and admits **no** source. Recorded here as context only; no edit to any existing row was made or attempted. Observation.

## Network / tool status

- Network: no failures. Both fetches (raw README, commits API) succeeded on first attempt.
- Installs/updates: none (curl and python3 already present). Nothing installed via any channel.
- Host routing/sources untouched. No git/jj mutations. No execution of any target; static source reads only.

## Receipts (copied from scratch before cleanup)

- fetched README: 5151 bytes, sha256 `b82f32e9e36d55c9a7b0d7578a650312b5f319551e2d4a0870552e4895e61850`, quote at line 18, prerequisites at lines 26–28, feature bullets at lines 20–22.
- commit `1e980252087b2479a21b9ca6d82d5829538651a7`, committer 2026-10-10T19:17:31Z, message "Update readme".

## Uncertainty

None material. [INFERENCE] none beyond the cited lines; all claims above are directly observed in the fetched pinned bytes or the cited corpus rows.
