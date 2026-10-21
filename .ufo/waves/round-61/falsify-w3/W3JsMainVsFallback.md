GRADE: PARTIAL — C04 Unknown 1 (main vs folder fallback) and coverage-map clause, corpus/knowledge/commonjs-destructured-require-edges.md @ ab580698
Seat RevengerR61-2.W3JsMainVsFallback. Archive: `git archive ab580698212258a55e43e9bb9bf6ac78c91eae2a` -> /tmp/revenger-r61w3-W3JsMainVsFallback (rev-parse = ab580698212258a55e43e9bb9bf6ac78c91eae2a). No harm found: entry Reproduce run on the archive, exit=0, output `diff` against Provenance = PROVENANCE_IDENTICAL (no saved record or fixture changed).

## Holds: Node-side premise (S020/S021 re-opened 2026-10-21, both pages "Node.js v26.12.1 Documentation")
- S020 https://nodejs.org/api/modules.html "Folders as modules": "if the "main" entry is missing or cannot be resolved, then Node.js will attempt to load an index.js or index.node file".
- S020 "All together", LOAD_AS_DIRECTORY: "b. If "main" is a falsy value, GOTO 2." ... "2. LOAD_INDEX(X)"; LOAD_INDEX: "1. If X/index.js is a file".
- S021 https://nodejs.org/api/packages.html `"main"`: "The "main" field defines the entry point of a package when imported by name via a node_modules lookup." Its own example (`"main": "./index.js"`) says "This resolves to ./path/to/directory/index.js."
- Fixtures: `package.json` = `{"name":"revenger-r3-fixture","version":"1.0.0","main":"index.js","type":"commonjs"}`, byte-identical across the pair (sha 92ef8e3d…); Reproduce prints `main='index.js' main_file_exists=True`. With `main`="index.js", step 1.d LOAD_AS_FILE(X/index.js) and fallback LOAD_INDEX(X) give the same file. Observed: the resolved path cannot tell them apart. This matches the entry (lines 55-57) and lessons/round-61.md:83.

## F1 (PARTIAL). Unknown lines 55-57 leave out evidence in the records that bears on the question
- Both saved records attribute the edge to `main` in their own fields. Command: python json dump of `maps_to`/`electron-main` in corpus/live/runs/20261012T164357Z/analysis.json and round-7/v2-analysis.json. Output:
  `maps_to {"declared_path": "index.js", "resolution_context": "package-entrypoint", "resolved_path": "index.js", ...} location {"kind": "artifact-path", "path": "package.json"}`
  `electron-main:package-entrypoint:index.js ['package.json:main']` (node observation `"mechanism": "package.json:main"`, both runs)
- `grep -c mechanism` on the entry returns 0. Neither `mechanism` nor `declared_path` appears in the entry or its Reproduce output. The lane's own verifier already checks `main["properties"]["declared_path"] == package["main"]` (corpus/verify_saved_evidence.py:114) and labels the edge "package-main mapping" (:116).
- Inference: the question "whether the edge reflects `main`" is answered by the provider's own record (inferred state; provider claim). What is actually unknown is the counterfactual: whether the provider would emit the same `index.js` edge through the fallback when `main` is missing or unresolvable. No fixture covers that case. The entry understates its evidence rather than overstating it, so this is not a voiding harm.
- Smallest fix: "The records attribute the edge to `package.json:main` (`mechanism`, `declared_path`, location `package.json`). Whether the provider would emit the same edge through the fallback when `main` is missing or unresolvable is unobserved; here `main` equals the fallback target (S020)." Also add `mechanism` to the Reproduce print.

## F2 (PARTIAL). Inference line 50 conflicts with Unknown line 55
- Line 50 says "`electron-main` is the provider's kind name for a package `main` file". That asserts the node is the `main` file, while line 55 holds that `main` vs the fallback cannot be separated. The record's `mechanism: package.json:main` supports line 50, but the entry never cites that field, and Provenance (lines 150-179) has no line that grounds it.
- Fix: cite the node identity key `electron-main:package-entrypoint:index.js` and `mechanism`, or reword to "the provider's kind name for its package-entrypoint node".

## F3 (nit). Line 56 states the fallback condition incompletely
- Line 56 has "documented fallback when `main` is missing". S020 says "missing or cannot be resolved", or no package.json at all, and also tries index.node. SOURCES.md:34 (S020 claim cell) is narrowed the same way. It is not wrong for these fixtures (index.js exists), but the unresolvable-`main` branch is the one that would matter for a future negative fixture.

## F4 (PARTIAL). Header line 4 coverage-map clause is narrower than the body
- Line 4 reads "C04 (CommonJS destructured `require` only; no Electron, ASAR, ESM, bundler or `exports` ground)". The body also asserts the package-entrypoint `maps_to` edge (Observation 4, lines 34-36) and the `electron-main` label plus `exposes` = `default` (Observation 5, lines 37-40). claims.md:118-120 (A2) scopes C04 to "the single relative destructured `require` ... and the package `main` edge", so "only" drops a scope the claim registered. README.md:30 repeats "destructured `require` only".
- "no ... `exports` ground": the backticked `exports` most plausibly means the package.json field, which holds (Reproduce `exports_field=False`). But Observation 5 is a record observation about named exports, and A2 says "No ... `exports` or named-export claim". It reads as a negative observation rather than a claim, so this is wording-level only.
- Fix: "C04 (one relative destructured `require` and the package-entrypoint edge on two authored CommonJS fixtures; no Electron, ASAR, ESM, bundler or package.json `exports` ground)".

## Other cells checked for "edge reflects main"
- claims.md:28 ("the package `main` entrypoint mapping as static inference") is the pre-amendment wording; A2 (claims.md:118-120) qualifies it. lessons/round-61.md:18 and :83 both say "not separated" or reject discrimination. README.md:30 does not mention `main`. Reproduce line 135 `agrees_with_source ... main=` compares resolved_path to `main` and would be True under the fallback too. The entry never presents it as discriminating, and Q03 (line 192) only sources the expected value. No cell found that claims a discrimination.
- Not run: no fixture without `main` or with an unresolvable `main` exists for this pair, so the provider's fallback behavior is unobserved. No REA call (out of scope).

VERDICT: PARTIAL. The Node premise holds: S020/S021 confirm index.js is the fallback and that main="index.js" cannot be separated by resolution. But the Unknown ignores the records' own `mechanism: "package.json:main"`/`declared_path` fields, line 50 contradicts it, and header line 4 "only" understates the body's entrypoint-edge scope. No voiding harm. Installs: none.
