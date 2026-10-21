RESULT: COMPLETE
Seat RevengerR61-2.R62RevenJsRoles · 2026-10-21 · leaf, no subagents, no installs, no fixture-JS execution, no producer calls.
Scope: node roles of named vs unnamed `imports` edges in BOTH saved JS records; deriving import target `javascript-module` vs `javascript-asset`; distinguishing from `module-export` nodes. No runtime, no Electron-role, no provider-universal claim.
Bytes: frozen extract of revenger-shokunin at `a3498e25ad87bf756288812d0ea7c474b09433c7` via `git archive | tar -x` into scratch (rev-parse of that id echoed identical); all reads on the extract, cwd=/fast/scratch/hyaku/revenger-r62/R62RevenJsRoles.

## Pins — `sha256sum` on frozen extract (this run)
- `corpus/fixtures/js-r3/`: index.js `f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7`, transform.js `cd9f3f633355d38c77dd0a26550d13b944b2502d4b0748f19607e36caa7fa345`, package.json `92ef8e3d5d3af1c34282669efb259661ac0739e8630aca5972c92c03ea1096d7`
- `corpus/fixtures/js-r7-v2/`: index.js `b53d96d432c120f6217a2da2ea3ed592308a3a23ef1a01745a22fd335ac4c42a`; transform.js and package.json byte-identical digests to js-r3 (same sha256sum run)
- v1 record `corpus/live/runs/20261012T164357Z/analysis.json` `7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452` (evidence `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`, subject js-r3, `root_artifact_sha256` `8eec9ffb7f5856da96d9411dc0dc024f39d781842853dc78c59ddc431e929f32`)
- v2 record `corpus/live/runs/round-7/v2-analysis.json` `331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e` (evidence `ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c`, subject js-r7-v2, `root_artifact_sha256` `696c24963ebaeb9f9d208a655d87c12bba322775bd95f8efabd914b49a78f655`)
- Method: stdlib-only `python3 -B roles_derive.py` (scratch; json+hashlib, read-only, no JS run); script and full 108-line output at `/fast/scratch/hyaku/revenger-r62/R62RevenJsRoles/{roles_derive.py,roles_out.txt}`. All counts/spans/digest matches below are its printed output.

## A. Named imports → target `javascript-module` (namespace `source-module`)
- v1: 3 `imports` edges (count derived in-run; whole-file JSON token `"imports"` = 3 too; `raw_result` null). Named 2: `jag_edge_66e056c7…e6254116` (`imported_name` rot13) and `jag_edge_b6378db3…e4c05be4aad3` (checksum); both target node `…c78088dec60b`, kind `javascript-module`, identity `{strategy: artifact-local-key, stability: artifact-version, artifact_sha256: cd9f3f63…caa7fa345, namespace: source-module, key: "8eec9ffb…:transform.js"}` — artifact_sha256 EQUALS my computed transform.js digest; key prefix equals the record's own `root_artifact_sha256` field; properties: `module_link_kind` require, `specifier` ./transform, `imported_path` [name], `local_name` name, `exported_name` null, `resolved_path` transform.js, `resolution_status` resolved, `target_file_kind` javascript; evidence state `inferred`, authority `static-relationship-inference`, extractor `resolve-semantic-module-relationship` v1; span index.js 1:6–1:50 (v1 line len 51, cols[6,50) substring `{ rot13, checksum } = require('./transform')` — derived from fixture bytes).
- v2: 2 `imports` edges. Named 1: `jag_edge_7a0c9240…fe81d202edf` (rot13), target `…3f9a094134a0`, same identity shape, artifact_sha256 `cd9f3f63…` = transform.js, key `696c2496…:transform.js` (= v2 `root_artifact_sha256`); span 1:6–1:40 substring `{ rot13 } = require('./transform')`.
- Target module node observations (both records): `semantic_role` source-module, `module_format` commonjs, `export_relationships` 1, `export_names` ["default"].

## B. Unnamed broad require → target `javascript-asset` (content-digest identity)
- v1 `jag_edge_b5c88eb6…3ca249757` and v2 `jag_edge_2ff2c8d4…8dccdbc13`: properties `{kind: require, specifier: ./transform, expression: null, resolved_path: transform.js}` — NO `imported_name`; extractor `map-static-relationship` v1; span covers only the call text (v1 1:28–1:50 `require('./transform')`; v2 1:18–1:40, line len 41).
- Both target the SAME node id `…b054a72f8c99`, kind `javascript-asset`, identity `{strategy: content-digest, stability: global-exact, sha256: cd9f3f63…}` — in-run match vs computed fixture digests: `['transform.js']` in each record. Node observations: `file_kind` javascript, `parse_status` complete, `bytes` 379, `unpacked` false.
- Derived rule (both records, n=5 edges): edge with `imported_name` → `javascript-module`/source-module target; broad require without `imported_name` → `javascript-asset`/content-digest target. No edge mixes these: named targets' kinds = {javascript-module}, unnamed = {javascript-asset} (derived sets printed).
- Identity contrast (recorded fields): asset node id identical across both records (content-addressed, global-exact); source-module node ids differ per record (artifact-local, key = root_artifact_sha256:path).

## C. Distinction from `module-export` nodes
- Each record has exactly 2 `javascript-module` nodes with `identity.namespace` `module-export`, strategy artifact-local-key, key JSON `["<root_artifact_sha256>","<file>","default"]` (v1: index.js `…928d214f11ea`, transform.js `…c7664227ec84`; v2: `…2d3839c861eb`, `…8c67691a155d`).
- In BOTH records the only relations touching module-export-ns nodes are `exposes` edges (2 each; properties `module_link_kind` commonjs-export, `exported_name` "default", `specifier`/`resolved_path` null; state inferred). Imports-edge target namespaces, derived: `{source-module, None}` in each record — NO `imports` edge targets a module-export node. Import targets are module files; module-export nodes are per-module export-binding nodes reached only via `exposes`.
- Round-12 saved records (`corpus/live/runs/round-12/{v1,v2}-analysis.json`, `a695e19e…`/`2001709d…`) show the same namespace on an export node with 0 imports edges — consistency observation only, not a universality claim.

## D. maps_to contrast (not imports)
- Exactly 1 `maps_to` edge per record (package-entrypoint), target kind `javascript-asset`: v1 digest `f7d8bf47…` and v2 `b53d96d4…`, each EQUAL to my computed index.js digest — entrypoint mapping is asset-level, disjoint from the 5 imports edges above.

## E. Honest limits
- All 5 imports edges are `state: inferred`, authority `static-relationship-inference`; recorded edge limitations include "Static syntax does not prove that this relationship executes at runtime" and, on named edges, "…no JavaScript was executed". `exported_name` null on all 3 named edges: the records bind importer-side names only; no export-binding claim.
- Exactly two 6.4.0-era records, `analyze_javascript_application`, provider `rea-javascript-application` v1 (recorded, not re-run; no current-version or universal claim). Subject/root digests `8eec9ffb…`/`696c2496…` are read from record fields; their derivation method is not recorded in the records (recorded-only). No dynamic `require(expr)` exists in either fixture — untested surface.

## Proposed inputs for the C04 entry writer (scratch, not filed as entry)
- Reuse `/fast/scratch/hyaku/revenger-r62/R62RevenJsRoles/roles_derive.py` as the Q11 derive block (commands + printed outputs above all map 1:1 to its lines); quote A/B/C tables and pin section verbatim.
- Suggested narrow phrasing: "in both saved records, the destructured (named) require edges terminate at `javascript-module` nodes in namespace `source-module`, while the unnamed broad-require edge terminates at a `javascript-asset` node whose identity sha256 equals the fixture transform.js digest; `module-export` nodes appear only as `exposes` targets, never as `imports` targets" — scope to these two records, static/inferred, 6.4.0 recorded.
Installs: none.
