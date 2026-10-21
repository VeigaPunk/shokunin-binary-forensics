GRADE: BROKEN — corpus/knowledge/commonjs-destructured-require-edges.md (C04), whole-entry overclaim sweep
Seat RevengerR61-2.W3JsOverclaimCritic. Tree: `git archive ab580698212258a55e43e9bb9bf6ac78c91eae2a` -> /tmp/revenger-r61w3-W3JsOverclaimCritic (entry `diff -q` vs live: rc=0). The entry's `## Reproduce` was run there: exit 0, output `diff` against `## Provenance` = IDENTICAL. No JS executed, no REA calls. Node docs fetched by curl 2026-10-21 (modules.md, esm.md; HTTP 200, page `node-version v26.12.1`).
Scope: one BROKEN (Q11 false-provenance clause) and three PARTIAL wording/generality findings. No sentence is contradicted on Electron, runtime loading or export binding. Every value the entry prints re-derives.

## BROKEN
B1 `:74-77` "…not the v2 digests, edge spans or the unnamed edge (…); this entry's block carries those values." It does carry the v2 digests and the unnamed-edge count. It carries no span: `awk` extraction of the python block | `grep -c -E "location|start|span|column"` -> `0`, and the Provenance output has no location fields either. So the entry claims a derivation it does not contain (Q11 reject: "a recorded value is presented as re-derived"; QUALITY table `:200` Q11 pass and `:202` Q13 rest on it). The fact it would support does hold: in the saved locations, the unnamed `imports` edge spans `index.js` 1:28–1:50 (v1) and 1:18–1:40 (v2), which is exactly `require('./transform')`. So `:28-29` "unnamed `imports` edge for the `require` call itself" is correct, but its offset role is not derived in the entry.
Fix: print `e["evidence"]["location"]["value"]` for every `imports` edge in Reproduce and Provenance, or drop "edge spans" from `:77`.

## PARTIAL
P1 `:50-51` "`electron-main` is the provider's kind name for a package `main` file, not an observation that Electron was involved." The second half holds: node and edge state `inferred`, and Reproduce prints `electron_tokens=0`. The first half overreaches (Q10/Q04: it generalizes one version to the provider; Q05: present tense, while the host skill now names 6.7.0 at `:71`). Evidence:
 - Both runs share one byte-identical `package.json` (`92ef8e3d…`), so the label rests on one input, from one producer version (`provider.version "1"`, rea-agents@6.4.0 per the ledgers).
 - The record's own grounds are not cited or derived (Q11). The node observation carries `mechanism:"package.json:main"` and extractor `discover-electron-entrypoint`, and the maps_to edge carries extractor `resolve-electron-entrypoint`. That is, the provider infers an Electron main role; it does not merely "name" the file.
 - Structurally, the `electron-main` node is keyed on package.json (`identity.artifact_sha256=92ef8e3d…`, namespace `electron-role`) and `maps_to` a separate `javascript-asset` node for index.js (`f7d8bf47…` / `b53d96d4…`). The main file's own kinds are `javascript-asset`/`javascript-module`.
 - `SOURCES.md:58` excludes the REA graph docs as "not load-bearing for any entry sentence", yet this is a record-semantics sentence.
 - No local counterexample: all six saved analyze records (r3, r7-v2, r12 v1/v2/direct ×2) emit `electron-main` via `package-entrypoint`, all from 6.4.0.
 Fix: "In both 6.4.0 runs the provider emitted an `electron-main` role node from `package.json` `main` (`mechanism: package.json:main`, `discover-electron-entrypoint`, state `inferred`) on inputs with zero Electron tokens: a provider inference, not Electron evidence; other packages untested." Also print `mechanism` in Reproduce.
P2 `:47` "S020's LOAD_AS_FILE order (`.js` first)". This is contradicted by S020. The pseudocode `LOAD_AS_FILE(X)` step 1 reads: "If X is a file, load X as its file extension format. STOP" (https://nodejs.org/api/modules.md, "All together", v26.12.1, accessed 2026-10-21). X.js is step 2. The conclusion holds because the fixture directory contains only index.js, package.json and transform.js (`ls`). Fix: "exact name, then `.js`; no extensionless `transform` exists".
P3 `:38-40` "both record a single exposed export named `default`". Each graph has two `exposes` edges (`relations … 'exposes': 2`, Provenance `:162`/`:171`), one per module, each `default`. Reproduce prints only the name set (`['default']`). Fix: "each module's only exposed export is `default` (2 per graph)". For context, S023 itself says the CJS wrapper "always provides a `default` export key pointing to the CommonJS `module.exports` value" (esm.md, "CommonJS Namespaces", v26.12.1, accessed 2026-10-21). So `default` is expected, not anomalous.
Nit `:31` "This comes from the two per-graph edge sets". This is lane computation, and Q04 asks for manual analysis to be labeled manual; round-7/LEDGER.md:17 says "scoped manual static difference". Add "(manual)".

## HOLDS (sentence, evidence)
- `:9-11` 6.4.0 `analyze-javascript-application`, recorded not re-run. Supported by 20261012T164357Z/LEDGER.md:5 and round-7/LEDGER.md:6.
- `:12-15` One relative destructuring `require` per fixture, and "nothing here is Electron evidence". Supported by Reproduce `require_calls=1`, `electron_tokens=0`, and `summary` Electron counters all 0.
- `:20-24` Source facts. Verified against the fixture bytes (`cat -A`). `"type":"commonjs"` goes unstated, which is an omission, not an overclaim.
- `:25-29` Named-edge set equals the destructured names; specifier and resolved path are uniform. Supported by Reproduce. The named edges target the `transform.js` source-module node, not its `module-export … default` node. That backs `:44-46` "not bindings to exports" better than S022 alone does; it is undrived but true.
- `:30-33` "removes exactly the named edge `checksum`". With subject digests normalized, v1−v2 is the `checksum` edge plus three edges whose only change is the new index.js content digest. Two shared edges shift span; nothing is added. The 0/1 score is at round-7/LEDGER.md:17.
- `:34-36` maps_to edge: `package-entrypoint`, `index.js`, `inferred`. Verified. A sibling `loads` edge shares the context and is unstated (omission only).
- `:44-46` S022 destructuring is a property read. Verified at gate quote §14.3.3.3, lessons/round-61.md:61.
- `:54-56` `main`=`index.js` equals the fallback. Verified at `LOAD_AS_DIRECTORY` steps 1c–1e and 2 (modules.md).
- `:61-63` S023 quote. Present verbatim at esm.md:625. "best-effort" matches esm.md:543-544: "a heuristic static analysis … best-effort static list of exports".
- `:69-73` One pair, three named edges, runs dated 2026-10-12 (LOG.md:97), static only. Supported by graph limitation "Static imports, entrypoints, … do not prove runtime execution."
- `:81-86` Cross-lane: kaidoku `:79-81` is a not-found `main` on a real ASAR; this entry's `main` is resolved on an authored directory. Reported, not absorbed.

## Q-table impact
- Q04 pass: holds (`:31` nit).
- Q05 "pass (past tense)": PARTIAL, because of `:50`.
- Q07 n/a: acceptable only once `:50` is reduced to the record's `mechanism` field.
- Q10 pass: PARTIAL, because of `:50`.
- Q11 pass: FAILS, because of `:77`.
- Harm check: no saved record or fixture changed. The overstatement is limited to `:77` and the `:50` generality.

VERDICT: BROKEN — narrowly. `:77` claims the Reproduce block carries edge spans; it carries none (Q11). P1–P3 are scope/wording defects at `:50`, `:47` and `:39`. Nothing overclaims Electron, runtime loading or export binding. All fixes are one line and keep every value, so the entry becomes admissible as-is once fixed. Installs: none.
