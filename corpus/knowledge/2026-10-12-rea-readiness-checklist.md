source: S001 — `.ufo/waves/kaika-r1/scout-freshness.md` — host re-probe table, 2026-10-19
verified-at: 2026-10-19 — every row re-probed; 3 of 6 rows stale, each flagged in `## Re-verification 2026-10-19`; the table between the headers and that section is the unchanged 2026-10-12 record
recheck: the `probe` column below, plus `node --version; npm --version; binwalk --version; unblob --version; jadx --version`
coverage-map: C14, C02

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

## Re-verification 2026-10-19

Appended correction (host change since mint). Probes and outputs:
`.ufo/waves/kaika-r1/scout-freshness.md`.

| fact | mint row | observed 2026-10-19 | verdict |
|---|---|---|---|
| K01 | rea CLI ABSENT | `command -v rea` → no output | holds |
| K02 | node v26.11.1 / npm 11.20.0 PRESENT | v24.21.0 / 11.19.0; `npm view rea-agents version` → 6.7.0 | STALE → v24.21.0 / 11.19.0; the skill's current pin is `rea-agents@6.7.0` |
| K03 | REA MCP NOT registered | `~/.omp/agent/mcp.json` server key `rea`, package `rea-agents@6.5.0` | STALE → registered for the omp host |
| K04 | ghidra / ida ABSENT | both absent | holds |
| K05 | jadx / binwalk / unblob / pwntools ABSENT | jadx 1.5.6, binwalk 3.1.0, unblob 26.6.4 present; pwntools import fails | STALE → 3 of 4 present |
| K06 | archive tools present | UnZip 6.00, ZipInfo 3.00 | holds |

`unblocks`, updated by observation only: REA's firmware guide names Binwalk 3.1.x
and Unblob 26.6.x, which the host versions match; the firmware route is
unprobed. Per Q05, presence is not readiness until an REA call against a
known-truth fixture returns Evidence.
