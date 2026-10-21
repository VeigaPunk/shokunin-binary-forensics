# CriticJsScope — r61 C04 thesis attack (read-only)

Thesis under attack: "REA analyze_javascript_application reported destructured-require named-import edges and a package-main mapping that agree with the authored fixture source; edges are static inference."
Seat: CloseChousa26.CriticJsScope-10, read-only. No clone, no producer call, no web page opened, no install. Evidence is local reads plus `python3 -B` over the saved records (O = observation, I = inference).

## Counterexamples and evidence
1. O, one tiny fixture pair. js-r3 and js-r7-v2 each contain one `require` site (`fixtures/js-r3/index.js:1`, `fixtures/js-r7-v2/index.js:1`), and `transform.js` contains none (`transform.js:1-12`). The named-import edges total 3: 2 in `ev_4a93…` and 1 in `ev_66f5…`. Each record also has one broad `{kind:require}` import edge, so the `imports` relation count is 3 and 2 by Counter. `package.json` and `transform.js` are byte-identical across the pair (sha256 `92ef8e3d…`, `cd9f3f63…`). Only `index.js` differs. The main-mapping sample is therefore one `package.json` byte string seen twice, plus shapes-r12 v1/v2, which has its own `package.json` (`3f3521c6…`) and no `require`. Axes: Q10, Q11.
2. O, false Electron role. Every record (r3, r7-v2, r12 v1, r12 v2) emits a node `kind:"electron-main"`, `namespace:"electron-role"`, `mechanism:"package.json:main"`. None of these packages declares Electron. Every Electron summary counter is 0 (`browser_windows`, `ipc.operations`, `preload_entrypoints`). `LEDGER.md:6` (run 20261012T164357Z) already calls this "a package-entrypoint convention, not evidence Electron ran". README row C04 is titled "JavaScript/Electron packages" (`README.md:30`), so flipping it to `held` invites an Electron reading. Axes: Q04, Q10.
3. O, the import binding is unresolved on the export side. All 3 named edges carry `exported_name:null` and `target_json_status:null`. `resolved_path:"transform.js"` is a file-path resolution only. Nothing in the edge binds `rot13`/`checksum` to the `module.exports = { rot13, checksum }` at `transform.js:12`. The verifier compares only importer-side names (`verify_js_graph_delta.py:23-27,43`). Axes: Q01, Q04.
4. O, the verifier hardcodes expected values instead of deriving them. The specifier `./transform` and `resolved_path == "transform.js"` are author constants (`verify_js_graph_delta.py:24,37-38`). No Node resolution rule derives `./transform` → `transform.js` (the `.js` extension probe). Source truth comes from one regex that matches only `^const {…} = require('…');` (`:23`). It does not cover rename (`{a: b}`), defaults, nesting, `let`/`var`, or multiple sites. Axes: Q03, Q01.
5. O, no record-to-bytes digest check in the verifier. `verify()` checks Evidence IDs (`:53-55`) and source facts, but never `artifact_sha256`. The binding does exist in the data: the node `identity.artifact_sha256` values contain all 3 current file hashes per fixture (my command printed `{'index.js': True, 'package.json': True, 'transform.js': True}` for both). The entry must carry that derivation itself. Saying the record "agrees with" the fixture without it is unsupported. Recorded `input_path` values point at `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/…`, not the current lane, so the path cannot serve as identity. Axes: Q09, Q11, Q03 (M14).
6. O, version and staleness. Both records come from `npx -y rea-agents@6.4.0` on 2026-10-12 (`LEDGER.md:5` in run 20261012T164357Z, `round-7/LEDGER.md:6`). `provider.version:"1"`, and `environment` is null. S002 records the current skill pin as `rea-agents@6.7.0` (`SOURCES.md:16`). No round-61 re-run is allowed (no producer calls). Any present-tense capability claim would rest on an older probe that has not been rechecked. Axes: Q04, Q05 (M01, M19), Q10 (M15).
7. O, an inconsistent statistic. `statistics.modules: 0` sits beside 4 `javascript-module` nodes and `parsed_javascript_files: 2` / `relevant_files: 3` (package.json is counted but not parsed as JS). Quoting "modules" as a module count is wrong. Axes: Q08, Q11.
8. O, coverage scope. Graph coverage is `complete, omitted_count:0`. The semantic graph coverage is `unknown`, with 32 unknowns (r3) and 25 (r7-v2). `complete` describes graph omission only, not semantic completeness, and not "all imports in the package". Axes: Q10.
9. Untested surfaces (O for absence, I for risk):
   - Dynamic `require(expr)`: no fixture has one. REA's own limitation text says such paths "may remain unresolved" (I).
   - ESM `import`/`export`: absent, and `"type":"commonjs"` is explicit in every `package.json`. REA's limitation text mentions ESM, but that is a tool claim this lane never exercised.
   - Bundlers: no Webpack/Rspack input, although REA's limitations mention factories.
   - Electron asar: `nested_asar_containers: 0` in all 4 records.
   - `exports` field, `browser`, conditional exports, missing `main`, bare/`node_modules` specifiers, JSON require, `index.js` directory fallback: none are present.
   Whether Node's runtime entrypoint equals REA's `main` mapping when `exports` exists is unknown here and needs a round-61 tier-A Node row (I). Axes: Q01, Q07, Q10.
10. I, fixture identity reuse. js-r7-v2 keeps `"name":"revenger-r3-fixture","version":"1.0.0"`, and its electron-main node_id equals r3's (`jag_node_3d26a843…`). "v1 → v2" is an authored source edit, not a package version change.
11. O, column convention. Edge locations are `line 1, column 6`–`50` (r3) and `6`–`40` (v2). These are 0-based with an exclusive end: `line[6]=='{'` and `line[6:50]=="{ rot13, checksum } = require('./transform')"`. Any position the entry cites must state this convention, with the command. Axes: Q11.

## Sentences the entry MUST NOT contain
- "REA identifies the Electron main process / Electron entrypoint" (counterexample 2; Q04, Q10).
- "REA resolves CommonJS imports" or "resolves `require`" without the qualifiers: static, destructured `const {…}=require('<relative literal>')`, file-path only (counterexamples 3, 4, 9; Q10).
- "Imported names are bound to / verified against the module's exports" (`exported_name:null`; Q01, Q04).
- "Handles ESM / dynamic require / bundles / asar / `exports` maps" (counterexample 9; Q07, Q10).
- "rea-agents (current / ≥6.4.0 / 6.7.0) does X", or any unversioned "REA does X" (counterexample 6; Q04, Q05, Q10).
- "The application graph is complete, so all imports were found" (counterexample 8; Q10).
- "Matching Evidence IDs / digests prove the record came from REA on these fixtures" (Q09, M13).
- "Two package versions" or "version 1.0.0 → 2" (counterexample 10; Q08).
- Any count (3 named edges, 2 main mappings, 32 unknowns, modules) without an in-entry command and its output (Q11).
- The 2026-10-12 "3/3 correct" (`LEDGER.md:16`) presented as re-derived; it must be labeled recorded (Q11).
- "REA's package-main mapping equals Node/Electron runtime resolution" without a round-61 tier-A row stating the `main` rules and the `exports` precedence (Q01).

## Smallest safe correction
Thesis wording to use: "In rea-agents@6.4.0 `analyze-javascript-application` (2 saved records, 2026-10-12), for one relative-literal `const {…}=require('./transform')` site per fixture, REA emitted `imports` edges with `imported_name` equal to the destructured names (3/3) and `resolved_path transform.js`, state `inferred`. It also emitted one `maps_to` edge with `resolution_context package-entrypoint` equal to `package.json` `main`. REA labels that node `electron-main` with no Electron evidence. Export-side binding is null. Dynamic require, ESM, bundles, asar and `exports` are untested."
The entry must also contain:
- a digest-binding command (counterexample 5);
- an in-entry count command (counterexample 1);
- a stated column convention (counterexample 11);
- an unknown list (counterexample 9);
- a limitation naming the 6.4.0 vs 6.7.0 gap.
The resolved-path expectation needs a round-61 Node tier-A source, or it must be labeled as an author constant.
Fixable defects are counterexamples 1, 4, 5, 7 and 11. Counterexamples 2, 3, 6, 9 and 10 are scope limits: the entry states them, it cannot fix them.

Commands run: `cat -n` of fixtures, `sha256sum fixtures/js-r3/* fixtures/js-r7-v2/*`, and three `python3 -B` stdin probes over `live/runs/{20261012T164357Z/analysis.json,round-7/v2-analysis.json,round-12/v1-analysis.json,round-12/v2-analysis.json}`. All are read-only and all exited 0.
Installs: none.
VERDICT: C04 thesis is admissible only when narrowed: 6.4.0, one relative destructured-require site per fixture, file-path not export binding, `electron-main` is a label not Electron evidence, plus in-entry digest and count derivations; unnarrowed it fails Q04/Q10/Q11.
