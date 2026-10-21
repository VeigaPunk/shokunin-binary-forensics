RESULT: COMPLETE

# R62ReviewJsSpans — saved location schema + end-column semantics of the C04 `imports` edges

Seat `RevengerR61-2.R62ReviewJsSpans` (reviewer, leaf, no dispatch) · 2026-10-21. Read-only derivation of the saved `imports`-edge location schema and end-column semantics for the two C04 saved JavaScript graphs, matched against exact fixture source substrings; named-binding span vs unnamed require-call span.
**No admission claim**; the README C04 row stays uncovered. No `corpus/live` / `corpus/fixtures` byte written, no producer run, no JavaScript executed, no prior rejected entry cited as support. Per-edge dump + every assertion: `/fast/scratch/hyaku/revenger-r62/R62ReviewJsSpans/R62ReviewJsSpans-detail.md`.

## 0. Pins and derivation
- `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse HEAD` → `a3498e25ad87bf756288812d0ea7c474b09433c7`; frozen copy extracted read-only with `git -C …revenger-shokunin archive a3498e25… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62ReviewJsSpans`.
- digests (`spans_evidence.py` §0): `analysis.json` `7c3ba8c1…31ed452`; `v2-analysis.json` `331ec252…5d564e`; `js-r3/index.js` `f7d8bf47…ae869fd7`; `js-r7-v2/index.js` `b53d96d4…354c42a`; `transform.js` `cd9f3f63…aa7fa345`; `package.json` `92ef8e3d…ea1096d7`.
- drivers: `python3 -B spans_evidence.py .` (cwd = extracted root) → **exit 0, 40 checks, 0 failed** (`spans_evidence.out`); `python3 -B entry_reproduce_spans.py` (cwd = dir containing `corpus/`) → **exit 0** (`entry_reproduce_spans.out`).

## 1. Saved location schema (identical in both graphs)
- `evidence.location` = `{available, value}`; `value.kind` ∈ `{"source-range","artifact-path"}`; `source-range` fields are exactly `{kind, source, start{line,column}, end{line,column}}`; `artifact-path` exactly `{kind, path}`.
- relations: `source-range` → `contains`, `exposes`, `imports`; `artifact-path` → `contains`, `loads`, `maps_to`.
- `location.source` is a **bare basename** (`"index.js"`), never a path; the file it denotes is bound by the edge's own `evidence.artifact.sha256`, which equals the fixture digest in every case checked → cite the digest, never a saved path (the saved `input_path` names another checkout).

## 2. End-column semantics (derived from the record, not assumed)
- `start.column` is **0-based**: 4 source-range edges per graph carry `start.column == 0` (relations `contains`, `exposes`; the first character of the line), so a 1-based reading is unrepresentable (column 0 invalid). `line` is 1-based (the require line is line 1).
- `end.column` is **exclusive**: the `contains` edges end at `(line N, column 0)` with `N` = the file's split-line count (8 `index.js`, 13 `transform.js`), i.e. EOF after the trailing newline; an inclusive end at column 0 would have no character to include.
- **1-based end-column reading: `end.column` equals the 1-based ordinal of the span's LAST character** (equivalently the 0-based exclusive end offset). Verified on every digest-resolved span in the corpus: 43/43, 0 violations.
- Consequence for the C04 edges: each `imports` span ends at the **closing `)` of the `require` call** and **excludes the statement's `;`** (`;` sits at 0-based 50 (v1) / 40 (v2), one past the recorded end); the rejected end-inclusive reading would extend every import span by exactly one character (`;`).

## 3. Every `imports` edge with its exact source substring
v1 `corpus/live/runs/20261012T164357Z/analysis.json` (`ev_4a93276c…100c1c7e`, 13 edges) — `imports` = 3 (named 2, unnamed 1)
| edge (prefix) | imported_name | location | exact source slice | len |
|---|---|---|---|---|
| `jag_edge_66e056c7…` | `rot13` | 1:6–1:50 | `{ rot13, checksum } = require('./transform')` | 44 |
| `jag_edge_b6378db3…` | `checksum` | 1:6–1:50 | `{ rot13, checksum } = require('./transform')` | 44 |
| `jag_edge_b5c88eb6…` | *(none)* | 1:28–1:50 | `require('./transform')` | 22 |
v2 `corpus/live/runs/round-7/v2-analysis.json` (`ev_66f5dc7e…cd7987c`, 12 edges) — `imports` = 2 (named 1, unnamed 1)
| edge (prefix) | imported_name | location | exact source slice | len |
|---|---|---|---|---|
| `jag_edge_7a0c9240…` | `rot13` | 1:6–1:40 | `{ rot13 } = require('./transform')` | 34 |
| `jag_edge_2ff2c8d4…` | *(none)* | 1:18–1:40 | `require('./transform')` | 22 |
Source lines (exact): js-r3 `index.js:1` = `"const { rot13, checksum } = require('./transform');"` (51 chars); js-r7-v2 `index.js:1` = `"const { rot13 } = require('./transform');"` (41 chars).

## 4. Named-binding span vs unnamed require-call span
- **Named binding edge** — `properties` = `{imported_name, local_name, imported_path, module_link_kind:"require", resolution_status, specifier, resolved_path, target_file_kind, target_json_status, exported_name:null}`. Span starts at the destructuring `{` (0-based 6 in both fixtures) and ends at the require call's `)`: the whole destructuring declaration **including** `require('./transform')` and **excluding** the `;`. In v1 the two named edges (`rot13`, `checksum`) share **one identical span** — one span, two edges.
- **Unnamed require-call edge** — `properties` = `{kind:"require", specifier, resolved_path, expression:null}`; no `imported_name`/`local_name`/`module_link_kind`. Span starts at the `r` of `require` (0-based 28 in v1, 18 in v2) and ends at the same `)`; it is a **suffix of** the named span (asserted in both graphs).
- Independent derivation (hand-written scanner over fixture bytes only; no parser library, no JS executed): call span `(1,28,50)` / `(1,18,40)`, pattern span `(1,6,25)` / `(1,6,15)`; the saved named span = **pattern start → require-call end**, the saved unnamed span = **require-call span** — both equalities hold in both graphs.
- Non-null `imported_name` occurs only on `imports` edges (10 in the corpus). `exposes` shares the same property key vocabulary with null values, so the named/unnamed discriminator is the value set plus the span start column, not the key set alone.

## 5. Corpus-wide sweep (coverage of the schema claim)
- 47 `source-range` locations exist across all saved records; 43 resolve to a current fixture file by the edge's own artifact digest and **all 43 obey** the convention (0 violations). 4 (round-12 `v1-analysis.json`, `v2-analysis.json`) do not resolve — recorded digests `2a698b56…` / `bea7d7db…` are absent from `corpus/fixtures` (shapes-r12 bytes drifted) → those spans are **recorded, not re-derived** and stay outside the C04 scope.
- `imports` edges corpus-wide: 16 — v1 ×3, v2 ×2, round-7 `comparison.json` ×5 (merged), round-9 `trace.json` ×3, round-9 `trace-exact.json` ×3. The merged comparison carries the same bare `source:"index.js"` over **two** byte sets (digests `f7d8bf47…` vs `b53d96d4…`): the digest, not the basename, is the identity.

## 6. Limits / unknowns (honest)
- The convention is derived from the record's internal consistency, not from a schema document: the record states no base/offset convention and no producer run was in scope. The `contains`-edge EOF ends are the decisive discriminator; under that reading each import span ends at `)` and excludes `;`.
- One authored family (js-r3, js-r7-v2). No claim about other package shapes, ESM, bundlers or runtime loading. `resolved_path` is a file-path resolution only; `exported_name` is `null` in every named edge, so no export-side binding is observed. No Electron-role, provider-capability, authenticity or completeness claim is made.

## 7. Proposed artifacts (scratch only; nothing written into `corpus/`)
- `spans_evidence.py` + `.out` — full derivation, 40 assertions, exit 0 (read-only, stdlib only); `entry_reproduce_spans.py` + `.out` — compact entry-ready `## Reproduce` block printing the convention line and the six edge spans, asserted against literals written in the script itself (no saved value used as its own expectation); `R62ReviewJsSpans-detail.md` — per-edge dump, discriminators, sweep, property-vocabulary note.
- No corpus file created, edited or proposed for landing; no README row touched.

## 8. Routed-item disposition (round-61-verifier-spotcheck.md)
- "derive or accurately label the missing spans/counts/targets" (routed item 1): **addressed** — the six C04 import spans, their end-column semantics and the named/unnamed distinction are derived above with commands and outputs. This does not admit the entry; admission remains with the criteria and the fresh falsify wave. Nothing here touches the prior rejected drafts, round-61 reports/counterexamples or the verifier lesson.

Installs / updates: **none**. No package manager, no network fetch, no provider call, no fixture-code execution.

VERDICT: the saved C04 `imports` edges are fully accounted for (v1 3, v2 2); every span matches an exact fixture substring under a derived, corpus-wide consistent convention (line 1-based; column 0-based; `end.column` = the 1-based ordinal of the span's last character); the named-binding span is distinguishable from the unnamed require-call span by its start column and value set. Review evidence only — no admission is claimed.
