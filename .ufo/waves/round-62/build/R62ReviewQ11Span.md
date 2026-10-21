RESULT: COMPLETE

# R62ReviewQ11Span — red example for the C04 span defect + minimal in-entry printed fields

Seat `RevengerR61-2.R62ReviewQ11Span` (reviewer, leaf, no dispatch) · 2026-10-21. Scope: old rejected C04 candidate + round-61 `W3JsOverclaimCritic` only. **No admission claim; `corpus/README.md:33` C04 stays `uncovered`.** No corpus/fixture/live byte written, no producer run, no JavaScript executed, no REA call, no rejected entry cited as support. The round-61 falsify observation is ground truth; the failed old check was NOT re-run — the red example is re-derived by **static** read of the two blocks.

## 0. Pins
`git -C …/revenger-shokunin rev-parse HEAD` → `a3498e25ad87bf756288812d0ea7c474b09433c7`; read-only extract `git -C …/revenger-shokunin archive a3498e25… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62ReviewQ11Span`. Frozen `corpus/knowledge/commonjs-destructured-require-edges.md` sha256 `690db9f1…2a6f3`; at `ab58069` sha256 `3382f1b3…5629`, differing only by the 6 added rejection-warning lines (diff = 2 hunks). Critic line numbers map `ab:74-77 → frozen:80-83`, `ab:50-51 → frozen:56-57`, `ab:38-40 → frozen:44-46`, `ab:31 → frozen:37`, `ab:200 → frozen:206`, `ab:202 → frozen:208` (verified line-identical except `ab:47`, a one-line offset of the LOAD_AS_FILE sentence). Saved records re-derived here: `corpus/live/runs/20261012T164357Z/analysis.json` `7c3ba8c1…31ed452`; `corpus/live/runs/round-7/v2-analysis.json` `331ec252…5d564e`.

## 1. Red example — the C04 span claim is false at block level (static read)
`:80-83` (Limitations) claims its own `## Reproduce` block "carries … edge spans". Static scan of the two blocks (`static_scan.py` extracts `## Reproduce` and `## Provenance (Q11)` and counts location-ish tokens; it executes nothing from the entry):

```
$ python3 -B static_scan.py corpus/knowledge/commonjs-destructured-require-edges.md
REPRODUCE code lines=53 matches(location|start|span|column|offset)=0
REPRODUCE code matches(:d+:d+|line N)=0
PROVENANCE code lines=29 matches(location|start|span|column|offset)=0
PROVENANCE code matches(:d+:d+|line N)=0
```

Whole-file grep for span words on the frozen entry hits only `:81` (the false claim), `:89` (unrelated kaidoku citation) and `:208` (Q13 row naming spans *unguarded*) — 0 printed span fields. The round-61 finding is thus confirmed by static read alone: the entry asserts a derivation its blocks do not contain = Q11's reject clause ("a recorded value is presented as re-derived", `corpus/QUALITY.md:23`). **The facts are not wrong** — all 5 `imports` edges carry `evidence.location.value.kind == "source-range"` (36/36 `imports` edges across the saved tree). The defect is a missing in-entry derivation, not a false value.

## 2. Ground truth a new entry must not inherit wrongly from the old one
- `:80-83` also says the block carries "the v2 digests … [and] the unnamed edge". Block check: it prints the v2 record digest and the unnamed-edge **count** (`unnamed_require=1`), never the unnamed edge's identity (`edge_id`) or span. A count is not the edge.
- Named vs unnamed span semantics (re-derived here): the **unnamed** edge's saved span is exactly the `require('…')` call region (v1 1:28–1:50, v2 1:18–1:40; slice `require('./transform')`); each **named** edge's saved span covers the whole destructuring-plus-require region (v1 1:6–1:50, v2 1:6–1:40; slice `{ rot13, checksum } = require('./transform')`) and does **not** point at the identifier. Source-derived identifier spans: `rot13` 1:8–1:13, `checksum` 1:15–1:23 (v1). A new entry claiming "the `checksum` edge spans the `checksum` identifier" would be false on these bytes.
- Column base must be derived, not assumed: per record, `source-range` edges include `start.column == 0` (4 edges) and `end.column == 0` at EOF (2 edges) ⇒ start column 0-based, end column an exclusive 0-based offset. The old entry printed neither.
- Q13 (old `:208`): `corpus/verify_js_graph_delta.py:41` checks only `location.value.source == "index.js"`; `corpus/verify_saved_evidence.py:107-108` only `location.value.source` and `location.value.start.line == 1`; neither file contains the token `column` (grep: no match). ⇒ every column/end coordinate is **unguarded** by both verifiers; a new entry must say so and must not credit them for spans.
- Two wording defects on the same old entry (outside my field list; recorded so a new entry is not built by copying it): `electron-main` is a provider *inference* (`mechanism:"package.json:main"`, `discover-electron-entrypoint`, state `inferred`, zero Electron tokens), so old `:56-57`'s "the provider's kind name" overreaches (critic P1); and each graph has **two** `exposes` edges (one per module, each `default`), so old `:45`'s "a single exposed export named `default`" is wrong (P3).

## 3. Minimal in-entry printed source + saved-location fields a new C04 entry needs
Spec with rationale: `/fast/scratch/hyaku/revenger-r62/R62ReviewQ11Span/minimal_fields_spec.md`. Implementation `candidate_span_fields.py` (same dir): `python3 -B candidate_span_fields.py` → exit 0, deterministic (two runs byte-identical), output `candidate_span_fields.out` sha256 `a3bcbb925116818e486c20c6bd25965dd2c63db2ef39b86df2c63cb235476b8b`; reads only saved JSON and fixture bytes, executes no JavaScript, no REA call, writes nothing into `corpus/`.
Per `imports` edge, per record: **B1** record path + `sha256` of the record file, `evidence_id`, `subject.digest.sha256`. **B2** fixture path + `sha256` of `index.js`, byte length, line-1 text/length. **B3** saved fields verbatim: `edge_id`; `relation`; `imported_name` with **absent vs null distinguished**; `kind`/`module_link_kind`; `specifier`; `resolved_path`; `resolution_status`; `evidence.state`; `evidence.location.available`; `evidence.location.value` **dumped as raw JSON** (`kind`, `source`, `start.line`, `start.column`, `end.line`, `end.column`). **B4** source-derived values: `require(…)` call span and each destructured-name span, computed from fixture bytes by the entry's own code. **B5** column-base derivation printed inside the entry (Q11: constants derived, not assumed). **B6** comparison lines: saved slice text per edge; saved-span vs source-derived-span equality printed per edge — True for the unnamed edge, False for named edges, with printed text showing why. **B7** counts: `imports` edge count, named set, unnamed count per record; the v1→v2 delta.

## 4. Residual risk / verification gaps
Red example verified by **static** block/provenance read only; the old `## Reproduce` block was not re-run (round-61 falsify seat's job; its observed output is ground truth), so a new entry's blocks must still be executed by its author with the output pasted into `## Provenance`. Fixture bytes were read, never executed; the destructuring semantics used here are the round-61 critic's S022 scope, not re-opened by this lane. Saved `location.source` is a bare basename (`"index.js"`), bound to the fixture file here via the edge's own `evidence.artifact.sha256` equalling the fixture digest, not via the saved path. "Unguarded columns" states only what those two verifier files' current text checks; their mutation coverage was not re-audited.

## 5. Proposed changes (scratch only, no corpus edit)
`static_scan.py` (block/provenance span-field counter), `candidate_span_fields.py` + `.out` (B1–B7 reference implementation), `minimal_fields_spec.md` (field spec for the entry author) — all under `/fast/scratch/hyaku/revenger-r62/R62ReviewQ11Span/`.

Installs: none (no pacman, no uv/pip/npm, no network install; tools: git archive/tar, sha256sum, python3 3.14.8 stdlib only).
