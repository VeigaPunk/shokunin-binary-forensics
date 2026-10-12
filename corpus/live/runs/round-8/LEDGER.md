# Round 8 saved-graph delta verifier

- Before: r7 `compare_application_versions` `items[]` did not name the removed `checksum` import (0/1; Evidence `ev_5e4b17c1db1a06126558586f188b8eae81117c4d4bdf43d2278aefcd945f1a78`). No comparison-tool claim is revised.
- `python3 .shokunin/revenger/corpus/verify_js_graph_delta.py --self-test` exited 0:

```text
POSITIVE saved parent graphs: removed checksum 1/1; stable rot13 and package-main; static inference only
NEGATIVE REJECTED saved graph disagrees with source truth
```

- Inputs: r3 Evidence `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`, r7-v2 Evidence `ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c`, authored source `corpus/fixtures/js-r3/index.js:1` and `corpus/fixtures/js-r7-v2/index.js:1`. Both application graphs have complete declared graph coverage with zero omissions, while semantic coverage remains unknown. The program selects named `imports` edges, requires static inferred/resolved source provenance, compares source truth and package-main edges. Its in-memory negative control changes v2 `rot13` import to `checksum`; no committed Evidence is edited.
- OBSERVATION: saved per-version graph edges and source differ by one named import; stable `rot13`, package main `index.js`. INFERENCE: scoped analyst-side delta, 1/1 source-truth import removal detected and one alteration rejected. UNKNOWN: actual execution, full semantics, original producer provenance, and native analysis. This is **not** an output finding of `compare_application_versions` and not a claim of runtime import behavior.
