GRADE: PARTIAL — C04 Observation 2 (named-import edge sets); substance HOLDS, wording nits at entry lines 25–26
Archive: `git archive ab580698212258a55e43e9bb9bf6ac78c91eae2a` → /tmp/revenger-r61w3-W3JsNamedSet (git read-only: show/diff/log; no status, no lane writes). Scratch: /tmp/revenger-r61w3-W3JsNamedSet-work/.
Hypothesis (entry lines 25–29): in each saved graph, `imports` edges with `imported_name` equal the destructured names (v1 {checksum, rot13}; v2 {rot13}).

Findings
1. HOLDS — independent re-derivation: check_named_edges.py (own brace-matching parser; source vs graph as sets and multisets) → exit 0.
   v1 source {rot13, checksum}; graph imports edges [4]=rot13, [10]=checksum, [9]=unnamed kind:"require" (3 total).
   v2 source {rot13}; graph imports edges [9]=rot13, [2]=unnamed kind:"require" (2 total).
   Every imports edge, named and unnamed: specifier ./transform, resolved_path transform.js.
2. HOLDS — no hidden contrary value: key sweep over whole records for any key containing "import" (extended_checks.py, part a).
   v1 imported_name ×6 = 2 named + 4 null (nodes[3], nodes[8] observations; exposes edges 1, 3). v2 ×5 = 1 named + 4 null. No empty-string names.
3. HOLDS — second graph layer agrees: normalized_result.semantic_graph (not cited by the entry) has zero imports relations and zero imported_name keys.
   Its index.js-scope bindings (program:0:274 in v1, program:0:209 in v2) that are transform.js export names: v1 {checksum, rot13}; v2 {rot13}.
   v2 checksum bindings exist only at program:0:379 (transform.js, 379 bytes).
4. HOLDS — per-module count agrees: graph module node path=index.js has import_relationships 2 (v1) and 1 (v2); transform.js 0 in both. The count excludes the unnamed require edge.
5. HOLDS — Delta (entry lines 30–33): multiset diff removes exactly ('checksum','./transform','transform.js') ×1, adds none; imports 3→2, edges 13→12.
6. HOLDS — copies: 9 Evidence-shaped graphs = 2 saved + 7 embedded (round-6/view-request; round-7/comparison-request left+right; round-9/trace-request, trace-exact-request; round-14 and round-18 trace-request).
   All 9 canonically identical to the saved graph (sort_keys JSON) with the expected named sets (embedded_copies.py, exit 0). Identifier-only references (round-6/view.json; round-7/comparison.json) carry no graph.
   Prose agrees: round-7/reviewer.md:6; round-8/LEDGER.md:12; round-9/LEDGER.md:9; 20261012T164357Z/LEDGER.md:11-12. round-7/LEDGER.md:17 records the 0/1 tool miss the entry cites.
7. HOLDS — other saved graphs: corpus-wide sweep finds 6 analyze_javascript_application records. Exactly the two cited carry the fixture digests. The four round-12 records (v1/v2, shapes-r12 bytes, other digests) have zero imports edges.
8. HOLDS — inputs unchanged: `git diff --stat cf02419 ab580698 -- corpus/live corpus/fixtures` and `e0a4b0c ab580698` both print nothing. sha256 prefixes identical at e0a4b0c, cf02419, ab580698: analysis.json 7c3ba8c1; round-7/v2-analysis.json 331ec252; js-r3/index.js f7d8bf47; js-r7-v2/index.js b53d96d4; transform.js cd9f3f63; package.json 92ef8e3d.
   The entry file is new in that range (@@ -0,0 +1,202 @@), so its verified-at base predates the text.
9. HOLDS — Reproduce block (entry lines 90–144) run from archive root: exit 0, 29 lines; diff against Provenance (lines 150–180) IDENTICAL (repro_vs_provenance.py).

Wording nits (PARTIAL; not material to the evidence)
N1 lines 25–26: "the set of `imports` edges with an `imported_name` equals the destructured names" compares a set of edges to a set of names. The intended object is the set of imported_name values.
N2 line 25: "In each saved graph" does not name its object. Each record has two graph objects: normalized_result.graph (imports edges; what the Reproduce block reads) and normalized_result.semantic_graph (relations: captures, defines, reads, aliases, reads-property, coerces, writes; no imports). Read literally over semantic_graph the sentence yields an empty set and fails, and the entry never mentions semantic_graph. Fix: name normalized_result.graph on line 25 and disclose semantic_graph, whose binding layer agrees (finding 3).

Corrections to my first draft: it graded HOLDS and called every non-request carrier a "derivative view"; the copies, ledgers and reviewers were not checked until the sweep above. Two of my own checker expectations were wrong on first run (index.js also binds defaultInput/render; round-12 records were flagged). Both were corrected before the conclusions above; no data changed.

Limits: provider not re-run (out of scope); static checks on archived JSON only. The fixture-oracle limit the entry flags (aliases, rest) is not exercised: each fixture has one single-line destructuring require (index.js line 1 is the only line containing require).

Installs: none (python3 stdlib; git read-only).
VERDICT: Observation 2's named-edge claim holds on every checked layer and copy; PARTIAL solely for wording at entry lines 25–26 (edge set vs name set; unnamed "each saved graph").
