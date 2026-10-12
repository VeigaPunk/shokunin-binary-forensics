# REA readiness checklist — 2026-10-12 (mint)

Decision table for the recurring question "can this host run this REA route
right now?" Rows are probed facts, not intentions.

| question | probe | mint result | unblocks |
|---|---|---|---|
| rea CLI present? | `which rea` | ABSENT | — |
| npx acquisition viable? | `node --version; npm --version` | node v26.11.1 / npm 11.20.0 PRESENT | `npx -y rea-agents@6.4.0` |
| REA MCP registered? | client tool list for `open_binary` etc. | NOT registered (skill is instructions-only) | needs connect step per references/connection-and-recovery.md |
| ghidra / ida | `which ghidra ida` | ABSENT | native pseudocode route blocked; layout/inspection routes unaffected |
| jadx / binwalk / unblob / pwntools | `which …`; `python3 -c "import pwn"` | ABSENT | Android deep-dive, firmware extraction, ELF-layout routes blocked until caller-supplied |
| archive tools | `unzip -v`, `zipinfo` | present on host (standard) | ZIP/APK member inventory via `open_binary` |

Error patterns to record as they are observed (append-only): npx download
failure modes; MCP transport `resource_constraint: transport` handling
(inspect_analysis_view paging per SKILL.md); tool-advertised-vs-unavailable
distinction (`binary_session {}` → result.tool_availability).

Rule: do not re-run setup diagnostics before every investigation (SKILL.md
"Connect only when needed") — this table is the remembered state; re-probe
only after a repair or a host change.
