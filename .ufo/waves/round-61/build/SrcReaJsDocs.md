# SrcReaJsDocs — REA JavaScript docs for C1/C04 (read-only scout)

Scope: statements about `analyze_javascript_application` in the installed skill and upstream REA docs; C04 only (C09 is ScribeEntryEvm's). No live-lane write, no REA producer call, no bytecode/JS execution.

## Skill and producer versions
- Installed skill: `/home/vgpnk/.agents/skills/reverse-engineer-anything/SKILL.md:5` `version: "42"`; `:6` `tool_count: 207`.
- Local JS guidance: `/home/vgpnk/.agents/skills/reverse-engineer-anything/references/javascript-applications.md:8` "inputs and recovered code are never executed"; `:124-125` "Check `source_coverage` for source selection, partial/unknown graph coverage and unknown counts before drawing a negative conclusion." (16 words).
- Producer of both saved records: `corpus/live/runs/20261012T164357Z/LEDGER.md:5` and `corpus/live/runs/round-7/LEDGER.md:6` each record `npx -y rea-agents@6.4.0 analyze-javascript-application ...` exited 0. So `analysis.json` and `v2-analysis.json` are rea-agents **6.4.0** output.
- Record-internal version is schema, not package: `analysis.json` `/provider` = `{"id":"rea-javascript-application","version":"1"}`; rot13 edge `/evidence/extractor` = `{"name":"rea-javascript-artifact-reconstruction","version":"1","operation":"resolve-semantic-module-relationship","executable_sha256":null}`.

## URL opened, HTTP result, revision
- `curl -sS -o /dev/null -w '%{http_code}' https://raw.githubusercontent.com/morluto/rea/rea-agents-6.4.0/docs/javascript-application-graph.md` -> `200`.
- Same command for `.../javascript-artifact-reconstruction.md` -> `200`; `.../javascript-application-workflows.md` -> `200`.
- `https://github.com/morluto/rea/blob/main/docs/javascript-applications.md` -> HTTP 404 (guessed filename, absent; read tool reported `Method: failed ... HTTP 404`). Actual listing opened via `https://github.com/morluto/rea/tree/main/docs` (GitHub API tree).
- Revision/date: tag `rea-agents-6.4.0` = commit `a56f7bb668ab23fec8d33f7af353ac7ed2fe1895`, committer date `2026-10-11T03:57:29Z`. The page carries no version banner; `diff -q` shows main differs from this tag, so every quote below is from the tag.
- Anchor: `docs/javascript-application-graph.md` (tag) — "JavaScript Application Graph" intro ¶2 (`:8-11`) and "Evidence and authority" (`:107-139`).

## Verbatim quotes (<=25 words each)
1. "It performs no filesystem or CDP I/O, does not evaluate JavaScript, and has no application-specific node kinds." — `javascript-application-graph.md:10-11`, intro ¶2, tag rea-agents-6.4.0 (17 words).
2. "`static-relationship-inference` can only produce `inferred` facts;" — ibid. `:128`, "Evidence and authority" bullets (6 words).
3. "extractor name, version, operation, and optional executable digest; coverage status, truncation, omitted count, and named limits;" — ibid. `:119-120`, two adjacent bullets joined (16 words).

## Observed record facts (artifact output, not doc claims)
- `python3 -c` over `corpus/live/runs/20261012T164357Z/analysis.json`: `graph.edges=13`, states `inferred=8, observed=5`; all 13 edges `coverage={"status":"complete","truncated":false,"omitted_count":0}`.
- C04 edges in that record: `imports imported_name=rot13 -> transform.js` and `imports imported_name=checksum -> transform.js` (both `module_link_kind=require`, `resolution_status=resolved`), plus one unnamed broad `imports kind=require -> transform.js`; `maps_to resolution_context=package-entrypoint, declared_path=index.js, resolved_path=index.js`.
- `round-7/v2-analysis.json`: `edges=12`, `inferred=7, observed=5`, all complete/0; only the `rot13` named edge remains.
- Split coverage matters: `normalized_result.graph.coverage={"status":"complete","omitted_count":0}` but `normalized_result.semantic_graph.coverage.status="unknown"` with `32` unknown items — edge-level completeness does not imply semantic/call-flow completeness.

## Proposed SOURCES.md row (contract v1; id provisional, L1 assigns)
| S018 (TBD) | JavaScript Application Graph — REA documentation — https://raw.githubusercontent.com/morluto/rea/rea-agents-6.4.0/docs/javascript-application-graph.md | docs | A | what the REA JavaScript Application Graph records for static application relationships and coverage, at tag rea-agents-6.4.0 | "JavaScript Application Graph" intro ¶2 (`:8-11`) and "Evidence and authority" (`:107-139`); tag rea-agents-6.4.0 = commit a56f7bb, 2026-10-11 | `static-relationship-inference` yields only `inferred` edges, coverage carries status/truncation/omitted count, and the graph model never evaluates JavaScript. | queued | 2026-10-21 | on-release | — (flip to `mined` when the C04 entry cites it) |

ID note: sibling draft `ScribeSourcesRowsJs.md` provisionally holds S016/S017 and `ScribeSourcesRowsEvm.md` also drafts S016/S017; L1 assigns final ids, so S018 here is provisional only.

## What the source does NOT state
- No CLI JSON field names: `grep -c "package-entrypoint\|resolution_context\|imported_name"` on both tag docs -> `tag-javascript-application-graph.md:0`, `tag-javascript-artifact-reconstruction.md:0`. `properties.imported_name`, `module_link_kind`, `resolution_context`, `mechanism` are observed only in the record.
- No per-binding rule for destructured require. The nearest statement is a paraphrase of `javascript-artifact-reconstruction.md:234` (tag): CommonJS `require` calls are recovered; it does not say `const {rot13, checksum} = require('./transform')` emits one named edge per binding. That split (2 named + 1 broad edge) is an artifact observation only.
- No concrete `omitted_count` value rule in the graph doc; the companion recon doc `:389` (tag, paraphrase) only says an unknowable exact count is `null`, not guessed.
- No version binding to rea-agents 6.4.0; the doc never names the package version. Tag↔record provenance comes from the LEDGER invocations.
- No description of the `normalized_result.semantic_graph` wrapper or its `coverage`/`unknowns`; its documented "Stored record" shape covers only graph-level coverage.
- No runtime claim by design: point 1 above and the graph limitations (`analysis.json` `/normalized_result/graph/limitations`) say entrypoints/imports "do not prove runtime execution".

## Companion source opened, not rowed here
- `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.4.0/docs/javascript-artifact-reconstruction.md` -> HTTP 200, tag a56f7bb, 2026-10-11. "What is reconstructed" `:227-235` (paraphrase) lists `package.json` metadata/declared main or renderer entrypoints and CommonJS require calls as inert-data recovery; it supports C04's entrypoint mapping beside the sibling Node.js rows S016/S017. If rowed separately it needs its own gate quote (quote budget spent above).

## Remaining unknowns
- Field-by-field equality between the 6.4.0 CLI output and the tag's documented graph schema is not proven; only `graph.coverage` and the evidence fields were matched.
- As of 2026-10-21 the repo `main` docs have drifted from the 6.4.0 tag; do not quote main for 6.4.0 records.
- No opened source states the per-binding destructured-require edge rule; a C04 entry must ground that in the saved record (own-work) plus the Node docs rows, and must not attribute it to this doc.
- C09/EVM is outside this item; see `ScribeSourcesRowsEvm.md`.

Installs: none.
VERDICT: C04 docs opened at tag rea-agents-6.4.0 (HTTP 200, commit a56f7bb, 2026-10-11); static/inferred/coverage/no-execution claims verified with three located quotes; one tier-A provisional row S018 proposed; per-binding destructured-require semantics remain unsourced.
