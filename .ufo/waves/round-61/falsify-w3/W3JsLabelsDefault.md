GRADE: PARTIAL — C04 Observation 5 (corpus/knowledge/commonjs-destructured-require-edges.md:37-40), landed ab580698212258a55e43e9bb9bf6ac78c91eae2a

Target text: "Both graphs label the entry node kind `electron-main` although the fixtures contain zero `electron` tokens, and both record a single exposed export named `default`, not the `module.exports` keys."

Method. `git archive ab58069` extracted to /tmp/revenger-r61w3-W3JsLabelsDefault (commit rev-parse = ab580698212258a55e43e9bb9bf6ac78c91eae2a, read-only copy). Parsed every node/edge of `normalized_result.graph` from both saved records; grepped all fixture bytes; re-ran the entry's `## Reproduce` block verbatim (python3 -B, no fixture JS executed, no REA producer calls).

Observed — clause (a) entry label, HOLD:
- v1 (corpus/live/runs/20261012T164357Z/analysis.json) and v2 (corpus/live/runs/round-7/v2-analysis.json) each hold exactly 1 node of kind `electron-main` (`jag_node_3d26a843…`, present in both graphs).
- Its identity is `namespace: electron-role`, `key: electron-main:package-entrypoint:index.js`; observation label `index.js`, props `{declared_path: index.js, resolution_context: package-entrypoint, resolved_path: index.js, mechanism: package.json:main}`, state `inferred`.
- Edge placement: `loads` (package → electron-main) and `maps_to` (electron-main → javascript-asset with sha256 f7d8bf47…/b53d96d4… = the index.js bytes). So the electron-main node is the package-entrypoint role node.
- Caveat, not a break: declared `root_node_ids` is the `package` node (jag_node_c5d5b55e…), not the electron-main node; "the entry node" names the entrypoint role node, not the graph root. No other node carries an entry label.

Observed — clause (b) zero electron tokens, HOLD:
- Fixture dirs hold exactly 6 files (3 each; `find … -type f`): index.js, transform.js, package.json.
- `grep -ril electron corpus/fixtures/js-r3 corpus/fixtures/js-r7-v2` → no output, exit 1. Per-file `grep -oi electron | wc -l` → 0 for all 6. Byte-level python `read_bytes().lower().count(b'electron')` → 0 for all 6 (UTF-16LE decode count also 0).
- The record itself does contain the label (kind `electron-main`), so "fixtures contain zero" is correct and distinct from the record's label.

Observed — clause (c) exposed export, PARTIAL:
- Each graph has 2 `exposes` edges, both `exported_name: "default"`, both state `inferred`: index.js → `index.js:default`, transform.js → `transform.js:default` (2 export-binding nodes each; per source module `export_relationships: 1`, `export_names: ["default"]`).
- Raw record: 4 `"exported_name": "default"` occurrences per record (2 edges + 2 nodes); zero `exported_name` values of `render`, `rot13`, `checksum`.
- Fixture bytes: `corpus/fixtures/js-r3/index.js:7` `module.exports = { render };`; `corpus/fixtures/js-r3/transform.js:12` `module.exports = { rot13, checksum };`; `corpus/fixtures/js-r7-v2/index.js:7` same as v1 index. So "not the `module.exports` keys" is true.
- Defect: line 39 says "a single exposed export named `default`"; each graph records 2 `exposes` edges, one per module (2 exposed export bindings), so the unqualified singular is graph-wide false. It is true per module and true for the exported-name set (the entry's own `exposes_exported_names=['default']`). The entry's Provenance (lines 168/178) prints `relations={'…'exposes': 2…}` beside that name set, so the entry carries the correcting count, but the prose does not qualify it.

Derivation (Q11) re-run: extracted `## Reproduce` code fence executed from the archive root, exit 0, 29 output lines; difflib against the `## Provenance` `text` fence = 0 diff lines. The block's printed lines include `node_kinds=['artifact','electron-main','javascript-asset','javascript-module','package']`, `exposes_exported_names=['default']`, `electron_tokens=0` for both graphs — so clauses (a) and (b) are derived in-entry, and clause (c)'s name is derived; only the singular count is unqualified.

Harm checks: fixtures and both saved records at verified-at base e0a4b0c and claim base cf02419 are byte-identical to ab58069 — `git diff --stat <base> ab58069 -- corpus/live corpus/fixtures` printed nothing, exit 0 (both bases); record sha256 7c3ba8c1…/331ec252… and fixture sha256 f7d8bf47…, cd9f3f63…, 92ef8e3d…, b53d96d4… match the entry's Provenance fence. No fixture, record, or hold changed; entry sha256 3382f1b3… identical between live lane and archive. S027 (corpus/SOURCES.md:41) is the tier-A own-work row for record content, mined 2026-10-21.

Inference: [INFERENCE] the author intended "single" as the exported-name set (one name, `default`), since the same block emits `exposes_exported_names=['default']`; under that reading the clause is accurate. [INFERENCE] no fixture or record harm reaches C04 admission from this observation.

Unknown: none material. (Whether a reader should treat `electron-main` as an Electron finding is answered by the entry's own Inference at line 50; not re-litigated here.)

VERDICT: PARTIAL — the electron-main label and zero-fixture-token clauses hold exactly and reproduce byte-for-byte; line 39's "a single exposed export" is a wording nit: each graph records 2 `exposes` edges / 2 export bindings (one per module), while the recorded exported name set is the single `default` and never the `module.exports` keys.
Installs: none.
