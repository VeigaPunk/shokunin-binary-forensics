# Independent LEAF review — round 8 saved parent-graph delta

## Reproduction and evidence

- Ran `python3 .shokunin/revenger/corpus/verify_js_graph_delta.py --self-test` from repo root. Exit **0**; output exactly:

  ```text
  POSITIVE saved parent graphs: removed checksum 1/1; stable rot13 and package-main; static inference only
  NEGATIVE REJECTED saved graph disagrees with source truth
  ```

- Read the authored fixture files: `corpus/fixtures/js-r3/index.js:1` destructures `rot13, checksum` from `./transform`; `corpus/fixtures/js-r7-v2/index.js:1` destructures only `rot13`. Both `package.json` files specify `main: index.js`; their bytes and the `transform.js` bytes match across versions. The render expression also changes, so this is **one changed named-import relationship**, not one changed line or one changed behavior. `transform.js` still exports `checksum` in v2.
- Read complete saved parent records `corpus/live/runs/20261012T164357Z/analysis.json` (`ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`) and `corpus/live/runs/round-7/v2-analysis.json` (`ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c`). Their application-graph named `imports` edges have `{rot13, checksum}` and `{rot13}`, respectively. Each is inferred, resolved from `index.js` to `transform.js`. Each parent has one inferred, resolved package-entrypoint `maps_to` edge to `index.js`; application graph coverage says `complete`, `omitted_count: 0`. Separately, parent **semantic graph** coverage says `unknown`. The named-import edges' artifact SHA-256 fields also agree with the actual corresponding `index.js` bytes (independently inspected; the verifier does not require this).

## Check quality and limits

- `verify_js_graph_delta.py` asserts the two expected parent Evidence IDs and operation, checks declared application-graph coverage, filters named `imports` edges, validates inferred/resolved `index.js` provenance and absence of duplicates, and checks one resolved inferred package-entrypoint mapping in each record. It independently reads source import lists and package `main`, requires exact per-version equality, then requires the single removed `checksum` name, retained `rot13`, and stable `index.js` main. This supports **1/1 removed named import by analyst-side parent-graph comparison**, plus scoped stable relationships.
- The self-test deep-copies v2 Evidence and changes its retained `rot13` imported name to `checksum` in memory; verification rejects it with `saved graph disagrees with source truth`. This is one useful falsification control, not an exhaustive mutation suite. The verifier does not independently authenticate all Evidence contents from IDs, check fixture artifact hashes or graph node endpoint identities, or establish producer provenance; its small source parser covers the authored fixture shape, not general JavaScript. Those limits do not defeat this specific saved-record/source comparison, but forbid a broader validity claim.
- **Do not reclassify round 7.** `compare_application_versions` Evidence `ev_5e4b17c1db1a06126558586f188b8eae81117c4d4bdf43d2278aefcd945f1a78` has no explicit `checksum` removal in `items[]`: comparison-tool detection stays **0/1**, precision N/A. This verifier reads the *two parent application graphs*, not that comparison output. Neither saved static graph proves runtime import execution, render output, complete program semantics, native analysis, or a newly repaired comparison tool.

## Axis recommendation

- **Calibration: improved, bounded to reproducible analyst-side parent-graph verification** (positive 1/1 and one rejected mutation). **Depth: unchanged**; **coverage: unchanged**. This is not a round-7 reversal or runtime result. No REA producer rerun, target execution, install, commits, or recursive delegation were performed.
