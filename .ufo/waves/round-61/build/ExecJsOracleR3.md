# ExecJsOracleR3 — independent C1/C04 source oracle, js-r3 imports/maps_to
Seat CloseChousa26.ExecJsOracleR3-10 · 2026-10-21 · RUNS read-only; scratch only `/tmp/revenger-r61-ExecJsOracleR3-scratch` (no clone: no lane writes, no verifiers/mutants run).
Axes: A1 coverage (edges independently accounted), A2 precision (command+output per value, Q11), A3 speed (parallel batches).
Installs: none. Preexisting tools: node v24.21.0 (`node --version`), coreutils sha256sum/awk/grep, jq via read-filter. No pacman/uv/npm transactions.

## 1. Base pin and fixture bytes
- `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse HEAD` → `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`; `git -C …revenger-shokunin diff --stat e0a4b0c4348ef1fade46539f520e94fa140c4d8a -- corpus/fixtures/js-r3 corpus/live/runs/20261012T164357Z | wc -l` → `0` (read state == base).
- `sha256sum` in corpus/fixtures/js-r3 → `92ef8e3d…096d7 package.json`, `f7d8bf47…9fd7 index.js`, `cd9f3f63…345 transform.js`. These equal the artifact sha256 fields inside analysis.json edges and LEDGER.md — record was built from byte-identical files.
- `grep -o '"main":"[^"]*"' package.json` → `"main":"index.js"`; full bytes: `{"name":"revenger-r3-fixture","version":"1.0.0","main":"index.js","type":"commonjs"}`. No "electron" string anywhere in package.json.

## 2. My independent derivation (oracle, no record input)
- Own scanner `/tmp/revenger-r61-ExecJsOracleR3-scratch/cjs-scan.cjs` (hand-rolled lexical CJS scan + own path-math resolution) → `node cjs-scan.cjs …/corpus/fixtures/js-r3` output: `package_main:"index.js"`, one require: file `index.js` line 1, kind declaration, names `["rot13","checksum"]`, specifier `./transform`, resolved `transform.js` (`exists-in-fixture`).
- Node's own resolver, resolution only (require.resolve loads no module code): `node -e "…require.resolve('./transform',{paths:[d]}); require.resolve('.',{paths:[d]})"` → `<fixtures/js-r3>/transform.js` and `<fixtures/js-r3>/index.js`.
- Location byte-checks, `awk` substr (1-based = col+1): index.js L1 substr(7,44) → `{ rot13, checksum } = require('./transform')`; substr(29,22) → `require('./transform')`; `length($0)` L1 = 51 → col convention line 1-based, column 0-based, end-exclusive; index.js L7 = `module.exports = { render };` (len 28, edge range [0,27) ends at `}`); transform.js L12 = `module.exports = { rot13, checksum };` (len 37, edge range [0,36) ends at `}`).

## 3. Record values — all 4 imports/maps_to edges (jq on analysis.json)
- `jag_edge_66e0…` imports rot13: specifier `./transform`, imported_name rot13, resolved_path `transform.js`, resolution_status resolved; evidence state `inferred`, confidence `high`, coverage `complete`; location index.js [1:6,1:50).
- `jag_edge_b637…` imports checksum: identical props/location; state `inferred`/high/complete.
- `jag_edge_b5c8…` imports (broad): kind require, specifier `./transform`, resolved_path `transform.js`, no imported_name; location index.js [1:28,1:50) = the bare `require('./transform')` call; state `inferred`/high/complete.
- `jag_edge_4a2c…` maps_to: declared_path `index.js`, resolution_context `package-entrypoint`, resolved_path `index.js`, resolution_status resolved; target node kind `electron-main`; location artifact-path `package.json`; state `inferred`/high/complete.
Census (jq group_by): contains 6, exposes 2, imports 3, loads 1, maps_to 1 = 13 edges, 10 nodes; record `integrity_contradictions` length 0; record locations = 1 (`artifact-root`).

## 4. Comparison verdicts — oracle vs record
| record claim | oracle | verdict |
|---|---|---|
| destructured names rot13+checksum @index.js:1 | scanner names `["rot13","checksum"]` line 1 | MATCH |
| specifier `./transform` | scanner specifier `./transform` | MATCH |
| resolved_path `transform.js` | my resolver + node resolver → transform.js | MATCH |
| maps_to main `index.js` (package-entrypoint) | package.json bytes `main":"index.js`; node `.` → index.js | MATCH |
| locations [1:6,1:50)/[1:28,1:50)/[0,27)/[0,36) | awk substr byte-extracts agree, end-exclusive | MATCH |
| states: imports/maps_to `inferred` high | correct classification: static resolution is candidate, not executed import | MATCH (conservative) |
| coverage `complete` per edge; graph.coverage complete, omitted_count 0 | consistent with all require sites/names found; 1 declaration, 3 edges (1 broad + 2 named) | MATCH |
Edges I cannot account for: **none**. 13/13 explained (see §5). The broad imports edge is the same single require site (LEDGER already declines to count it as a 4th finding).

## 5. Full 13-edge accounting
contains ×6: 2 file→module (ast-static-analysis, observed/exact), 3 dir→file (artifact-bytes, observed/exact: index.js, transform.js, package.json), 1 package↔package.json (inferred/high, `package-metadata-within-artifact`). exposes ×2: transform.js L12 and index.js L7, `exported_name:"default"`, inferred/high. loads ×1: package→index.js module, package-entrypoint, inferred/high. imports ×3 + maps_to ×1 as §3.

## 6. Coverage/unknown cross-checks (LEDGER corroboration)
- `grep -o '"unknown_id"' analysis.json | wc -l` → 32; `semantic_graph.unknowns | length` → 32; decomposition by family `unknown_ids`: call-flow 9 + data-flow 12 + object-flow 11 = 32; semantic_graph.relations length 65 (= boundary 1 + closure 5 + data-flow 57 + object-flow 2). LEDGER "32 unknown items, semantic graph coverage unknown" is byte-derived (`semantic_graph.coverage.status` = `unknown`), not prose-only.
- Record limitations length 5 (graph.limitations identical list): inert-syntax recovery, no execution, static ≠ runtime, dynamic/obfuscated unresolved, no bundler push invocation. 12 `"state":"unknown"` occurrences sit in semantic_graph (jsr relations), separate from the jag graph whose 4 edges here are observed/inferred as stated.

## 7. Q11 derivation block for the C04 scribe (verbatim, reusable)
1. names/specifier: `node /tmp/revenger-r61-ExecJsOracleR3-scratch/cjs-scan.cjs /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/js-r3` → `…"names":["rot13","checksum"],"specifier":"./transform","resolved":"transform.js"…`
2. resolution: `node -e "const d='/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/js-r3';console.log(require.resolve('./transform',{paths:[d]}),require.resolve('.',{paths:[d]}))"` → `…transform.js …index.js`
3. package main: `grep -o '"main":"[^"]*"' …/fixtures/js-r3/package.json` → `"main":"index.js"`
4. per-edge state/loc/coverage: read-filter `[.normalized_result.graph.edges[]|select(.relation=="imports" or .relation=="maps_to")|{eid:.edge_id[8:20],rel,st:.evidence.state,conf,cov:.evidence.coverage.status,loc:.evidence.location.value}]` (output in §3).

## 8. Caveats / C04 entry scoping (Q10, my own process honesty)
- `electron-main` node kind is extractor convention, NOT byte-derived — package.json contains no electron reference; LEDGER itself disclaims Electron launch. Entry must say: main→entrypoint mapping is byte-derived; the Electron-flavored label is recorded convention.
- exposes edges model only a single `default` per module; named CJS exports (render/rot13/checksum) exist only on imports side. Named-import edges are well supported; export-side name mapping is NOT in this record.
- Named-import ranges [1:6,1:50) end just after `)` (exclude `;`); span semantics exact per bytes shown, but I label the range's precise AST-end rule recorded, not re-derived.
- My scanner v1 had a resolver bug (`path.posix.normalize` stripped `./`, mislabeling the relative specifier "bare"); first run returned null resolution. Fixed same-session; final output above. My tool's defect, no bearing on the record.
- Unobserved by me: whether other runs' records (js-r7-v2 etc.) match — out of my item's scope (this run only).

VERDICT: all 4 imports/maps_to edges of run 20261012T164357Z independently reproduced from fixture bytes and my own scanner/resolver (names, specifier, resolved file, package main, locations, inferred states, complete coverage); 0 unaccountable edges; C04 knowledge claims are supportable at exactly the scoped, inference-labeled strength above.
