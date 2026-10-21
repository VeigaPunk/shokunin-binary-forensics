GRADE: PARTIAL — C04 Inference 2 (S020 LOAD_AS_FILE order ⇒ `./transform` → `transform.js`)

Target: `corpus/knowledge/commonjs-destructured-require-edges.md:48-49` (landed ab58069; file sha256 `3382f1b3c56fbffb78f87735f353f5737b24e3ae102542cf98d3271946bc5629`, byte-identical to the live copy).

## Source re-opened (verbatim, version recorded)
`https://nodejs.org/api/modules.html`, fetched 2026-10-21, HTTP 200, sha256 `b35916f2cc28629dafa7d4e9b9825fc51acbe3bf76f6a4c9fed4ed79c2a90edd`; `<meta name="node-version" content=v26.12.1>`; title "Modules: CommonJS modules | Node.js v26.12.1 Documentation" (matches S020). "All together" (`modules.html:507-609`), LOAD_AS_FILE verbatim (`modules.html:536-547`): `LOAD_AS_FILE(X)` / `1. If X is a file, load X as its file extension format. STOP` / `2. If X.js is a file,` / `3. If X.json is a file, load X.json to a JavaScript Object. STOP` / `4. If X.node is a file, load X.node as binary addon. STOP`
"File modules" (`modules.html:714`): "If the exact filename is not found, then Node.js will attempt to load the required filename with the added extensions: .js, .json, and finally .node."

## F1 — the cited order is mis-stated at line 48 (major)
Line 48 says "S020's LOAD_AS_FILE order (`.js` first)". The cited pseudocode's **first** step is the exact filename X, not `X.js`; `.js` is the first of the *added* extensions, reached only after step 1 fails — the precondition the lane's own recorded S020 quote keeps (`corpus/lessons/round-61.md:59`, "If the exact filename is not found, then …"). The entry drops it. Same compression in `corpus/SOURCES.md:34` (S020 "teaches": "trying `.js`, `.json`, `.node`"), but the entry's own anchor names the "All together" LOAD_AS_FILE pseudocode, whose step 1 is the exact-file check. Counterfactual (local Node v24.21.0, scratch dir `/tmp/revenger-r61w3-W3JsLoadAsFile/probe/fix`): with `transform` **and** `transform.js` **and** `transform.json` present, `node -e "console.log(require.resolve('./transform'))"` printed `/…/probe/fix/transform` — the extensionless file wins, i.e. `.js` is *not* first. (Runtime v24.21.0 ≠ cited v26.12.1; the authoritative statement for v26.12.1 is the pseudocode quoted above.)

## F2 — the layout premise that makes `.js` win is never derived in-entry (major, Q11/Q03)
Inference 2 is qualified "for this layout", but the entry never shows the layout excludes the files LOAD_AS_FILE would prefer. `## Reproduce` hashes only `index.js`, `transform.js`, `package.json` (lines 107-109) and prints `main`/`exports_field`, never a directory listing. Landed-tree check (`git archive ab58069` → /tmp): `find corpus/fixtures/js-r3 corpus/fixtures/js-r7-v2 -mindepth 1` yields exactly `index.js`, `package.json`, `transform.js` per fixture — no extensionless `transform`, no `transform.json`, no `transform.node`, no `transform/` dir. The conclusion is TRUE for these fixtures (step 1 fails → step 2 hits `transform.js`), but the exclusivity is asserted, not derived, and the resolution is read off the record's own `resolved_path` rather than derived from bytes (Q03/Q11).

## F3 — the branch deciding module format is never recorded (minor)
LOAD_AS_FILE step 2.c/2.d: the closest package scope's `"type"` field decides CommonJS vs ESM (`"module"` → ESM, `"commonjs"` → CJS, else `MAYBE_DETECT_AND_LOAD`). Both fixture package.json files declare `"type":"commonjs"` (fixture bytes; `grep -o '"type":"[a-z]*"'` → `"type":"commonjs"`), but Observation 1 records only `"main"` and "no `exports` field", and Reproduce prints `exports_field=` but never `type=`. The entry still calls the pair "one authored CommonJS package pair" and its coverage-map says "CommonJS destructured require only" — the field step 2.c branches on is absent from the entry's premise set.

## F4 — the edge does agree (holds; no finding)
Re-derived from the landed tree: all three `imports` edges have `specifier './transform'`, `resolved_path 'transform.js'`, `resolution_status 'resolved'`, `evidence.state 'inferred'` (`corpus/live/runs/20261012T164357Z/analysis.json`; v2 identical). The `## Reproduce` block re-run from the extracted tree reproduced its `## Provenance` block byte-for-byte (29 lines, diff empty).

## Conditions under which another file would win in these fixtures
1. Extensionless file `transform` in the fixture dir → LOAD_AS_FILE step 1 wins over `transform.js` ("Files using any other extension (or no extension at all) are parsed as JavaScript text files", "File modules"). Absent in both fixtures.
2. `transform.js` removed → `transform.json` (step 3) then `transform.node` (step 4). Absent.
3. `transform/` dir with `package.json` `main` → LOAD_AS_DIRECTORY, reached only if LOAD_AS_FILE finds nothing (require() step 3a→3b). Absent.
4. `"type":"module"` would change the *format* of the same `transform.js` (step 2.c.1), not the winner.

## Residual risk / verification gaps
F1/F2 leave the stated mechanism and premise unbacked-in-entry while the conclusion holds; under Q01 ("the claim exceeds what the cited text states") the defect is the line-48 parenthetical. No fixture JavaScript was executed: `require.resolve` only resolves paths, on copies in /tmp. No REA producer call, no target network. Probe runtime v24.21.0 vs cited doc v26.12.1: corroboration only.

VERDICT: PARTIAL — the resolution conclusion is correct for both fixtures and the edge agrees, but line 48 mis-states the cited LOAD_AS_FILE order (the exact filename is tried before `.js`), and the in-entry derivation of the layout that makes `.js` win (F2) and of the `"type"` field the same step branches on (F3) is absent.
Installs: none (curl and node v24.21.0 were already present).
