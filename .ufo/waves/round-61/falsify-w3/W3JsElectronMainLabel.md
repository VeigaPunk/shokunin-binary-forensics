GRADE: BROKEN — C04 Inference 3 (`corpus/knowledge/commonjs-destructured-require-edges.md:50-51`), first clause only; second clause HOLDS
Seat RevengerR61-2.W3JsElectronMainLabel. Archive ab580698212258a55e43e9bb9bf6ac78c91eae2a extracted to /tmp/revenger-r61w3-W3JsElectronMainLabel (`git archive` + `tar -x`). The live tree was not touched except for this file.

Sentence under attack (:50-51): "`electron-main` is the provider's kind name for a package `main` file, not an observation that Electron was involved."

## F1. The mapping holds within the sample (observation)
- A python survey of every saved graph in `corpus/**/*.json` found 6 independent analysis records, not 2. They are ev_4a93276c (js-r3), ev_66f5dc7e (js-r7-v2), and round-12 ev_b71e7b75, ev_2a492f5d, ev_6ede4369 and ev_913f14fa (shapes-r12 v1/v2, default and direct). Every one has exactly 1 `electron-main` node.
- The node fields are identical in all 6 records: namespace `electron-role`, key `electron-main:package-entrypoint:index.js`, mechanism `package.json:main`, extractor `discover-electron-entrypoint`, state `inferred`, confidence `high`.
- In each record a `package` node `loads` it (operation `discover-package-entrypoint`), and it `maps_to` index.js (operation `resolve-electron-entrypoint`). Every package node has `main:"index.js"` and `renderer:null`.
- No counterexample exists in the lane: no package `main` without the label, and no label without `package.json:main`. There is also no positive Electron control (`RevenJsHistory.md:55`), so the range of the rule is untested.
- The entry cites only 2 of the 6 records (S027, `SOURCES.md:41`).

## F2. Clause 2 holds: nothing here is an Electron observation (observation)
- The node state is `inferred`, not `observed`.
- The entry's own Provenance output shows `electron_tokens=0` for both fixtures (:168, :177).
- The record summary counters are all 0: `browser_windows`, `preload_entrypoints`, `ipc.operations`, `utility_processes`. This holds in ev_4a93276c and the round-12 v1 record (`normalized_result.summary`).

## F3. Clause 1 misstates the provider's documented semantics (BROKEN, Q04 + Q10)
- The REA docs at tag `rea-agents-6.4.0` (commit a56f7bb668ab23fec8d33f7af353ac7ed2fe1895) were re-opened by curl: HTTP 200, 10427 B, sha256 69e410a4…326ce. `docs/javascript-application-graph.md:60` lists the node vocabulary item "Electron main, preload, renderer, and utility process code;". Accessed 2026-10-21, https://raw.githubusercontent.com/morluto/rea/rea-agents-6.4.0/docs/javascript-application-graph.md
- Same tag, `docs/javascript-artifact-reconstruction.md:65-66` (HTTP 200, 24990 B, sha256 a55a41b9…e8565): "Dependency manifests remain package observations but do not declare Electron main or renderer entries." By implication, the root `package.json` is the one that declares the Electron main entry.
- Together with the record fields (`electron-role`, `discover-electron-entrypoint`, confidence `high`), the provider's own semantics are: an Electron main-process role, inferred from the root `package.json` `main` alone. It is not a neutral "kind name for a package main file".
- On 6/6 non-Electron fixtures that inference is wrong. The sentence recasts the tool's explicit output as a naming convention instead of scoring it. Q04 (`QUALITY.md:16`) requires scoring "the tool's own explicit output".
- Q10 (`QUALITY.md:22`): "the provider's kind name" is unversioned and universal. The entry's own Q10 row (:199) claims "scoped to one fixture pair and one provider version", and this sentence is not.
- Q01/sourcing: the sentence cites no source. The only source that speaks to record semantics, the REA JS graph docs at 6.4.0, was screened and excluded as "not load-bearing for any entry sentence" (`SOURCES.md:58`). Inference 3 is exactly such a sentence, and that source contradicts its framing.
- Q07 (:196, "n/a") does not strictly fail, because no parser accept/refuse prediction is written. [INFERENCE] The universal form does, however, imply an unregistered prediction for any package `main`.
- Lineage [observation]: the framing comes from recorded prose, not from a source. The round-3 ledger (`corpus/live/runs/20261012T164357Z/LEDGER.md:6`) calls it "a package-entrypoint convention", and build seats repeated that (`ExecJsOracleR3.md:49`, `RevenJsHistory.md:36`, `ExecJsShapesR12.md:41`). `lessons/round-61.md:17-18` and :82 then promote it to "a label".

## F4. The node-to-`main` link has no in-entry derivation (Q11, `QUALITY.md:23`)
- The Reproduce block (extracted to /tmp/revenger-r61w3-W3JsElectronMainLabel-repro.py, sha256 287a061d…9d92) prints only `node_kinds` and the `maps_to` resolved path. It never prints the `electron-main` node's key or mechanism, or the source node of the `maps_to` edge. The same gap covers Observation 5's "the entry node kind" (:37-38).
- Unmodified archive: exit 0, and the output is byte-equal to the entry's Provenance block (`orig_matches_entry_provenance True`).
- Mutant copy (/tmp/revenger-r61w3-W3JsElectronMainLabel-mut), both records changed:
  - the `electron-main` key was set to `electron-main:mutant:transform.js`;
  - the mechanism was set to `mutant:none` and `declared_path` to `transform.js`;
  - the source of `maps_to` and the target of `loads` were moved to a `javascript-module` node.
- Mutant result: exit 0, and the output differs only in the two whole-file `record … sha256=` lines (`NO_DIFF_EXCEPT_RECORD_SHA`). The record digest therefore catches any byte change, but no line derives the role link. The link is correct when re-derived (F1) but is not derived inside the entry.

## Impacted axes
- Coverage K (C04 admission, harm clause "an entry that overstates its evidence"): one sentence overstates what is known about provider semantics.
- No saved record or fixture changed. All counts, names and digests in the entry re-derive. The holds are unaffected. The fix is a rewrite of the sentence, not a withdrawal of the entry.

## Smallest safe correction (for L1; this seat edited nothing)
- Replace :50-51 with: "In these 6.4.0 records the provider infers an Electron main-process role (`electron-role`, `discover-electron-entrypoint`, `inferred`/`high`; REA 6.4.0 docs list 'Electron main … process code' as a node kind) from `package.json` `main` alone. The fixtures have 0 Electron tokens and every Electron summary counter is 0, so the label is not Electron evidence, and on these inputs the role inference is unsupported."
- Add the tag doc as a source row (or cite it as a recorded quote), and correct `SOURCES.md:58` "not load-bearing".
- Add one Reproduce print of the `electron-main` node's namespace, key, mechanism and its `loads`/`maps_to` endpoints.
- Optionally cite the 4 round-12 records as further same-version instances. Do not generalize beyond 6.4.0.

VERDICT: Clause 2 holds (no Electron observation). Clause 1 fails Q04/Q10, is unsourced (Q01) and has no in-entry derivation (Q11). It is contradicted by REA 6.4.0's documented "Electron main … process code" kind and the record's `electron-role` fields. It is fixable by rewording; no record, fixture or count changes. Installs: none (tools used: curl, python3, git archive, tar, diff).
