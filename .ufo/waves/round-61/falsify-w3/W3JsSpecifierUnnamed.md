GRADE: HOLDS — C04 Observation 2 second sentence (corpus/knowledge/commonjs-destructured-require-edges.md:27-29): every `imports` edge in both saved graphs has specifier `./transform` and resolved_path `transform.js`, and each graph has one unnamed `kind:"require"` imports edge whose span is exactly the single require call

Seat RevengerR61-2.W3JsSpecifierUnnamed · 2026-10-21 · landed `ab580698212258a55e43e9bb9bf6ac78c91eae2a`; archive tar sha256 `c774b23e31657f93c3818cc51eaf6cf53e287819805bdf2534f4ca9f880cab24`, extracted to /tmp/revenger-r61w3-W3JsSpecifierUnnamed. Entry sha256 `3382f1b3c56fbffb78f87735f353f5737b24e3ae102542cf98d3271946bc5629`, identical in the live lane. Read-only JSON/text; Python 3.14.8 stdlib; no JavaScript/bytecode execution, no REA call, no lane write; no installs.

## Observation — every imports edge, all properties (5 edges)
v1 `corpus/live/runs/20261012T164357Z/analysis.json:1` (sha256 `7c3ba8c1…`, coverage complete, 13 edges, JSON token `"relation":"imports"` x3):
- `jag_edge_66e056c7…` imported_name `rot13`, module_link_kind `require`, specifier `./transform`, resolved_path `transform.js`, state inferred, span index.js:1:6-50 → javascript-module
- `jag_edge_b5c88eb6…` imported_name absent, kind `require`, expression null, specifier `./transform`, resolved_path `transform.js`, state inferred, span index.js:1:28-50 → javascript-asset (digest `cd9f3f63…`)
- `jag_edge_b6378db3…` imported_name `checksum`, module_link_kind `require`, specifier `./transform`, resolved_path `transform.js`, state inferred, span index.js:1:6-50 → javascript-module
v2 `corpus/live/runs/round-7/v2-analysis.json:1` (sha256 `331ec252…`, 12 edges, token x2):
- `jag_edge_7a0c9240…` imported_name `rot13`, module_link_kind `require`, specifier `./transform`, resolved_path `transform.js`, state inferred, span index.js:1:6-40 → javascript-module
- `jag_edge_2ff2c8d4…` imported_name absent, kind `require`, expression null, specifier `./transform`, resolved_path `transform.js`, state inferred, span index.js:1:18-40 → javascript-asset (digest `cd9f3f63…`)

Both clauses hold on the bytes:
- Universal clause: the sets over all imports edges are `{'./transform'}` and `{'transform.js'}` in each record; no imports edge lacks either property. `grep -o '"relation":"imports"' <record> | wc -l` = 3 (v1), 2 (v2); the whole-file `"imports"` token counts are also 3 and 2, so no other imports edge exists anywhere in either record (`raw_result` is null; `semantic_graph.relations` has zero imports relations; graph coverage `complete`, omitted 0).
- Unnamed clause: 1 of 3 (v1) and 1 of 2 (v2) imports edges lack `imported_name`; both carry `kind:"require"` and `expression:null`. Slicing the fixture line by the recorded columns, `line[start:end]` = `require('./transform')` exactly (v1 `const { rot13, checksum } = require('./transform');`, v2 `const { rot13 } = require('./transform');`); named edges start at the `{`, so the unnamed span is the require call itself.
- Entry block re-derived: extracted E:91-143 to /tmp/…/repro.py, ran `python3 -B repro.py` in the archive root — exit 0, stderr empty, 29/29 output lines equal E:151-179 verbatim. It prints `imports=3 … unnamed_require=1` (E:164) and `imports=2 … unnamed_require=1` (E:174), and `named_import_specifiers=['./transform'] resolved=['transform.js']` (E:165,175). The comprehension at E:132 iterates *all* imports edges, so the printed set derives the universal clause including the unnamed edge; the label says "named" but the value is wider, so the output does not overstate.
- Cross-check over every saved JSON in the archive (`python3` walk of `corpus/live/**/*.json`): 36 imports edges in 11 files (round-6 view-request; round-7 comparison and comparison-request; round-9 trace, trace-exact and requests; round-14/18 trace-request; the two records). All 36 carry `./transform`/`transform.js`; every per-record graph copy has exactly one unnamed `kind:"require"` imports edge; round-7 `comparison.json` is one merged 25-edge graph carrying 2 unnamed (one per side). No saved derivative contradicts the sentence.
- Discrimination: in-memory copies (no file writes) with (a) a named specifier → `./other`, (b) unnamed kind → `import`, (c) a duplicated unnamed edge each fail the strict predicate; baseline passes both records. The check is not vacuous.

## Q / harm checks for this sentence
- Q01: sole load-bearing source S027 (`corpus/SOURCES.md:41`), tier A own-work, opened 2026-10-21, scope "what the two saved `rea-agents@6.4.0` `analyze_javascript_application` outputs … contain" — exactly this sentence's object.
- Q03: `./transform` and the name set are independently in the fixture bytes (block prints fixture sha256 and parses the source); Q04: only explicit provider edges are scored, provider/version named (E:1,3); Q11: every count and string value in the sentence is printed by E:131-132 and E:164-165/174-175.
- Harm: record and fixture bytes match the entry's Provenance hashes; entry byte-identical at ab58069 and in the live lane; `corpus/README.md:30` C04 held; `reports/round-61/measure-after.log:2` `K_HELD=6/14`. Nothing in this item voids admission.

## Nit and adjacent (not this grade)
- Nit: "unnamed" here means the `imported_name` key is absent (not null), and the unnamed edge's property shape differs from named edges (no `imported_path`/`module_link_kind`/`resolution_status`). The sentence stays accurate.
- Adjacent, outside my item (route to L1/another seat): the Limitations sentence E:74-76 says the entry's block carries "edge spans"; the block and Provenance print no line or column value at all (`grep -Ei 'line|column|span|:1:' repro.out` → no match). The block does carry the v2 digests and the unnamed-edge count. If the C1 harm clause's "overstates its evidence" is applied at entry level, this line is the candidate; the assigned sentence at E:27-29 is unaffected.

VERDICT: HOLDS — all 5 imports edges in the two saved graphs are `./transform` → `transform.js`, each graph has exactly one unnamed `kind:"require"` imports edge spanning exactly the single `require('./transform')` call, and no saved record or derivative contradicts the sentence.
Installs: none.
