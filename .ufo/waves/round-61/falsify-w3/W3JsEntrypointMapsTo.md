GRADE: HOLDS — C04 Observation 4 (corpus/knowledge/commonjs-destructured-require-edges.md:34-36), landed ab580698212258a55e43e9bb9bf6ac78c91eae2a

Target text: "Each graph has one `maps_to` edge with `resolution_context: package-entrypoint`, resolved to `index.js`, state `inferred`."

Method. Extracted `git archive ab58069` to /tmp/revenger-r61w3-W3JsEntrypointMapsTo (read-only); dumped *every* edge with relation `maps_to` from `normalized_result.graph` of both saved records, plus endpoint nodes, raw-string occurrence counts, and a re-run of the entry's `## Reproduce` block. No REA producer calls; no execution of fixture JS.

Observed (v1, corpus/live/runs/20261012T164357Z/analysis.json, sha256 7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452, evidence ev_4a93276c...):
- total edges 13; relation Counter `{'contains': 6, 'exposes': 2, 'imports': 3, 'loads': 1, 'maps_to': 1}` -> exactly 1 maps_to.
- maps_to edge `jag_edge_4a2c2006eaf26d10565c59a38a5911acd73a4dc3c2bf57b12a0b1040d87462f0`: properties `{"declared_path":"index.js","resolution_context":"package-entrypoint","resolved_path":"index.js","resolution_status":"resolved"}`; `evidence.state = "inferred"` (authority `static-relationship-inference`, confidence `high`, extractor `resolve-electron-entrypoint` v1).
- source node `jag_node_3d26a843...` kind `electron-main`, identity key `electron-main:package-entrypoint:index.js`; target node `jag_node_874a0ded...` kind `javascript-asset`, identity sha256 `f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7` = byte hash of `corpus/fixtures/js-r3/index.js`, so the resolution target is the index.js artifact, not just a matching string.

Observed (v2, corpus/live/runs/round-7/v2-analysis.json, sha256 331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e, evidence ev_66f5dc7e...):
- total edges 12; relation Counter `{..., 'maps_to': 1}` -> exactly 1 maps_to.
- maps_to edge `jag_edge_09fc810a...`: same properties (`resolution_context` package-entrypoint, `resolved_path` index.js, `resolution_status` resolved); `evidence.state = "inferred"`.
- target node `jag_node_55f48c45...` kind `javascript-asset`, identity sha256 `b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a` = byte hash of `corpus/fixtures/js-r7-v2/index.js`.

Exhaustiveness checks:
- Raw text of each record contains `"maps_to"` exactly once (`raw.count('"maps_to"') == 1` each); `raw_result` is null in both records, so no second un-normalized edge list.
- `normalized_result.semantic_graph.relations` hold only captures/defines/reads/aliases/reads-property/coerces/writes (v1 65, v2 58 relations) — zero maps_to there. No other maps_to edge exists in either record under any endpoint.
- The three `resolution_context` occurrences per record are: the electron-main node observation (mechanism `package.json:main`), the maps_to edge, and a distinct `loads` edge (`discover-package-entrypoint`, same declared/resolved path, state inferred). The `loads` edge is a separate relation and does not falsify "one maps_to edge"; the observation does not claim maps_to is the sole resolution edge.

Derivation (Q11) confirmed: the entry's own block prints `v1 relations={... 'maps_to': 1 ...}` and `v1 package_entrypoint_maps_to=1 resolved=['index.js'] state=['inferred']` (same for v2) — total count and the filtered attributes are both emitted. Re-ran the extracted `## Reproduce` on the archive: exit 0, output line-for-line identical to the `## Provenance` fence (29 vs 29 lines, difflib empty).

Harm checks: records and fixtures at verified-at base e0a4b0c4348ef1fade46539f520e94fa140c4d8a are byte-identical to ab58069 (sha256 values above, re-hashed from `git archive e0a4b0c`); no changed saved record or fixture between the stated base and the claim base.

Inference: [INFERENCE] Observation 4's only possible ambiguity is whether "resolved to `index.js`" means the `resolved_path` string or the target artifact; both readings agree here, so no overstatement.

Unknown: none material to this observation. (The entry's own Unknown about `main` vs folder fallback stands elsewhere; not raised or resolved here.)

VERDICT: HOLDS — both saved graphs contain exactly one maps_to edge, `resolution_context: package-entrypoint`, `resolved_path: index.js` to the index.js artifact bytes, edge state `inferred`; the entry's printed derivation and Provenance output reproduce exactly.
Installs: none.
