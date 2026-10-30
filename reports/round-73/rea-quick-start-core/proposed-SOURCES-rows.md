# Proposed SOURCES rows — REA quick-start core

**MERGED.** REVENGER_SHOKUNIN merged these rows into `corpus/SOURCES.md` as
**S415–S426** (12 rows; provisional S106 deduped — Ghidra pcoderef already
existed as S132 under the round-73 atlas). Row-id map:
`reports/round-73/source-id-map.tsv` col2 `rea-quick-start:<old>`.
Provisional ids below match `rea-quick-start:S0xx` map keys, NOT merged ids —
do not reuse S110–S122 (occupied by REVENGER's rows).
Status values assumed admission in a proper round with Gate quotes copied from
`CURATION.md`. `used-by` stays `—` until knowledge entries cite them.

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S096→S415 | Host REA CLI-first contract — `~/.agents/skills/reverse-engineer-anything/HOST-CONTRACT.md` | docs | A | this host's intentional MCP-off CLI-on policy and expected doctor drift only | "The rule" + "Expected doctor output"; sha256 ab36b310b285c0278bef2a62ccdc5effe9cdc2d232e4e684452c17be264b58fe | Absent MCP tools are the configured state; do not re-run setup to "repair" them. | queued | 2026-10-29 | on-release | — |
| S097→S416 | REA CLI command map 6.7.0 — `~/.agents/skills/reverse-engineer-anything/references/cli-command-map.md` | docs | A | kebab-case CLI twins for MCP tool names at rea-agents 6.7.0 | header "CLI command map — rea-agents 6.7.0"; sha256 83c4ec63315a26d8fd6b1a80ad9aeed5233690a8b0b8a247af13a905cef32e48 | 131 of 207 MCP tools have a direct CLI twin; session tools have none because CLI is one-shot. | queued | 2026-10-29 | on-release | — |
| S098→S417 | REA connection and task recovery — skill `references/connection-and-recovery.md` | docs | A | observed connection approval and provider blockers and next steps | table row "No REA tools in the active session"; sha256 a33760c84ae100f6ffd27d666e515956c5014ac33a6ee2414807833ae666a2b1 | A skill installation alone does not register MCP; use scoped doctor before setup. | queued | 2026-10-29 | on-release | — |
| S099→S418 | REA evidence comparison and verification workflows — skill `references/evidence-workflows.md` | docs | A | how to read Evidence IDs limitations coverage and when comparisons apply | opening paragraph and verify_reconstruction bullet; sha256 2bdee98a843d018cf850c706111bb74c459ba8640da00799e9208122e4d5ab80 | Cite evidence_id; a verify_reconstruction pass covers only declared comparable claims. | queued | 2026-10-29 | on-release | — |
| S100→S419 | REA CLI and Evidence — docs/cli.md at local checkout 12f6e0974cc0db0b3a9b86246accc76556837222 | docs | A | CLI process boundaries and save-then-project Evidence pattern | "CLI and Evidence" / "Run a command"; sha256 fad0e2b6c64230b8a0a0a15c610cb87304048b45378e854e30505ce18ece92e6 | Each CLI invocation is a separate process; project large saved Evidence instead of re-analyzing. | queued | 2026-10-29 | on-release | — |
| S101→S420 | REA JavaScript application workflows — docs/javascript-application-workflows.md at 12f6e09 | docs | A | authenticated JS Application Graph traces and comparisons without execution | opening; sha256 b2ea1ca72177cb5394bbc648dc80b9cdab2d6fd5e661389cff38a77849da40cd | Trace and compare tools consume completed analyze_javascript_application Evidence only. | queued | 2026-10-29 | on-release | — |
| S102→S421 | REA MCP runtime contracts — docs/mcp-contracts.md at 12f6e09 | docs | A | Evidence record identity paging retained dossiers and coverage fields | "## Tool results"; sha256 835966809b7b745ac5e48eb2a20614b432e6477d663bce4992efc5e9f39a6655 | Read normalized_result and evidence_id; analyze_function defaults to a summary whose parent holds the dossier. | queued | 2026-10-29 | on-release | — |
| S103→S422 | Working With Ghidra's P-Code To Identify Vulnerable Function Calls — https://riverloopsecurity.com/blog/2019/05/pcode/ | talk | B | reproducible p-code backward slice of malloc size provenance as a PoC method | 2019-05-11 article body; snapshot sha256 a90a95eea68be3dc15eab4ac8436011ad1035b7b1441cdfb596224b3a040ea70 | P-code lifting plus varnode defs can show allocation-size provenance; that is not exploit proof. | queued | 2026-10-29 | 180d | — |
| S104→S423 | HackOvert GhidraSnippets — https://github.com/HackOvert/GhidraSnippets | code | B | Flat Program Flat Decompiler and Complex API scripting examples | README lede; page oid 9bcd718e8958387ff5695194b83a52df4e0a3de7; README sha256 acf6c479a1ad34f631248b275a592cfba1d92d2c6ca8d1ab8b3a52144e09c7f6 | Flat APIs start automation; Complex API is required for interesting varnode and slice work. | queued | 2026-10-29 | 180d | — |
| S105→S424 | Ghidra P-Code Reference Manual — NSA ghidra Ghidra_11.3.2_build GhidraDocs/languages/html/pcoderef.html | docs | A | p-code operation semantics at that Ghidra tag only | title and "Last updated March 2, 2023"; sha256 496b96e8eb023e86983d219b42804213dfa3394dbbf147b21af803838ed62d84 | Look up p-code op meaning instead of inferring solely from decompiled C. | queued | 2026-10-29 | on-release | — |
| S106 (deduped) | SoftSec-KAIST BinKit 2.0 — https://github.com/SoftSec-KAIST/BinKit | dataset | A | declared BCSA compiler-option matrix and binary counts only | README BinKit 2.0; sha256 586957cccfcca5e2d51a00d09d66d567c6f40ee00e01af2538a255ccfbc979fb | Similarity claims need a known compiler/arch/opt matrix; BinKit states 1904 combinations and 371928 binaries. | deduped into S132 at merge | 2026-10-29 | 180d | — |
| S107→S425 | AUTOFACTS paper PDF — https://purs3lab.github.io/files/autofacts.pdf | paper | A | injected synthetic facts as static-analysis ground truth as authors define it | Abstract; PDF sha256 27f2fae4fef6eebb29b0a107c6a08ac389a2f121708b7f7a94e38434df03bcc9 | Analyzer evaluation can target recovery of injected values at program points across 2088 binaries. | queued | 2026-10-29 | 180d | — |
| S108→S426 | Assemblage corpus generator — https://github.com/Assemblage-Dataset/Assemblage | dataset | A | generator's own description of source-connected labeled binary production | README lede; sha256 473397f1339f70bbb450f2ef51f9558d35dd59af1f5babdaa9747cb2886d67b4 | Function-level metadata corpora are a different ground truth than injected facts or similarity matrices. | queued | 2026-10-29 | 180d | — |

## Proposed Path line (merged ids)

```
- `REA quick-start core` — S415 → S416 → S417 → S418 → S419 → S420 → S421 → S422 → S423 → S424 → S132 → S425 → S426: host CLI-first policy, command map, connection recovery, Evidence surface, CLI save/project, first JS graph workflows, MCP identity rules, then p-code PoC + API cookbook + p-code manual (pcoderef already S132; BinKit deduped), then two remaining non-interchangeable calibration corpora (injected facts / source-connected labels).
```

## Proposed Leads (unopened this pass)

- Practical Reverse Engineering (Bruce Dang et al.) — architecture/systems foundation book; pair with S422–S424 after opening a specific chapter.
- clearbluejar — Callgraphs with Ghidra, Pyhidra, and Jpype — pipeline article + companion repo; open before claiming callgraph extraction recipes.
- REA `docs/reconstruction-obligation-ledgers.md` / `docs/reconstruction-readiness.md` — defer to EvidenceLedger slice.
