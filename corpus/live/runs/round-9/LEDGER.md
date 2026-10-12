# Round 9 focused static REA feature trace

- Parent r3 JS Evidence `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e` was supplied inline to REA `trace-application-feature`; no source analyzer rerun or JS execution.
- First request `trace-request.json`: module label `index.js`, outgoing. REA Evidence `ev_a97e71e3bbacdef94d626cf572145653adc841f27ff324c24bf0c29a82a59d89` matches **two** seeds (the source module and its asset), six nodes/seven edges; label is ambiguous, not a unique module address. Rather than repeat the identical trace, second request `trace-exact-request.json` uses exact source-module node ID `jag_node_6fbb554e9ee51e07de7ebc42d305961f356fd60399a5209b523324e09c18113f`, outgoing. REA Evidence `ev_bbe3fc094c348831e501701c0426496a234f39269854fb1f0f074d8120b2ce8d` matches **one** seed, five nodes/six edges, `complete-within-source` against a complete source application graph.

## OBSERVATION / INFERENCE / UNKNOWN
| class | finding | Evidence and limit |
|---|---|---|
| OBSERVATION of returned static graph | Exact-seed trace contains `imports` edges for named `rot13` and `checksum`, `specifier=./transform`, `resolved_path=transform.js`, source `index.js:1`; both point to source module `transform.js`. | Trace `ev_bbe3fc094c348831e501701c0426496a234f39269854fb1f0f074d8120b2ce8d` and parent `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`; graph labels inferred with high confidence, not observed execution. |
| INFERENCE | Exact node-id avoids label's two seed matches; returned six edges include broad `contains` and `exposes` relations from reachable nodes. Only two named import edges answer the declared question; do not call every reached node a participant in the import. | Both trace Evidence IDs; source `corpus/fixtures/js-r3/index.js:1` and `transform.js:12`. |
| UNKNOWN | Whether `render` is ever invoked, either import executed, or checksum behavior observed at runtime; source static semantic graph remains `unknown`. | No runtime Evidence ID; trace limitation says graph relation ≠ execution/reachability in every state. |

## Before→after and outcome
- Before: zero REA feature traces checked on authored fixture. After: one exact-seed trace returns **2/2 declared named static import relationships** against source and a single module seed, with explicit containment/exposes spillover classified as unrelated to the import claim. This is a focused static trace gain, not a claim of exclusive two-edge output, decompilation, or runtime.
- Reproducible command: `npx -y rea-agents@6.4.0 trace-application-feature .shokunin/revenger/corpus/live/runs/round-9/trace-exact-request.json --format json` (the committed input embeds parent Evidence). The stored `trace-exact.json` has the new trace Evidence ID and original parent link.
