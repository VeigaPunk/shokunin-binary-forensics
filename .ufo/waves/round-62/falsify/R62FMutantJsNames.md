GRADE: HOLDS — frozen C04 manual name readout; both assigned mutants require output comparison, not exit status

Frozen revision: `d97761952be256d145d298022de03091de91d358`.
Candidate: `corpus/knowledge/round-62-commonjs-require-name-evidence.md`.
Candidate SHA-256: `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`.
Axes: coverage/sensitivity of name derivation; calibration of exit versus manual detection; exact-byte restoration.
Scope: only the two assigned saved-v2-record mutations, not admission or a complete Q01–Q13 audit.

## Primary evidence and bounded detector
Scratch `S=/fast/scratch/hyaku/revenger-r62/R62FMutantJsNames`; all executions used cwd `/` and `TMPDIR=$S/tmp`.
Extracted with `/usr/bin/git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar --output=$S/frozen.tar d97761952be256d145d298022de03091de91d358`, then `/usr/bin/tar -xf $S/frozen.tar -C $S/tree`.
Archive SHA-256: `4b52df49bbd6349d6ac8c45c4f7d73d9e7125c7f719950e89818cad21dc8cebc`.
Same detector on pristine, each mutant and each restoration: `/usr/bin/python3 -B $S/readout.py $S/tree` (15-second subprocess bound).
`readout.py` is byte-equal to candidate:85–213; SHA-256 `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac`.
Expected detector: manually compare emitted source names with saved names and their within-fixture/cross-record deltas (candidate:35–47,192–211); exit alone checks neither agreement nor named-edge completeness.
Primary source `$S/tree/corpus/fixtures/js-r7-v2/index.js:1`: `const { rot13 } = require('./transform');`.
The in-entry derivation reads that line, extracts `destructured_names`, reads saved `imported_name`, and calculates set intersection/differences; this is not a token-presence test.

## Observation — exact execution results
All five detector runs returned exit `0` and empty stderr.
| stage / saved stdout file under S | lines | stdout SHA-256 | byte-equal to published stdout |
|---|---:|---|---|
| `pristine.stdout` | 25 | `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` | yes |
| `renamed.stdout` | 25 | `2cdc4da29bf4716955bff7dbd8addf7e3a58871e6bccd83232d6335ebe441cb2` | no |
| `restored-rename.stdout` | 25 | `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` | yes |
| `removed-edge.stdout` | 24 | `335252000eea9cde18cb433dd17d041fd8d87e1a17b88adc224d476e6b1972c4` | no |
| `restored-edge.stdout` | 25 | `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` | yes |

M1: scratch `corpus/live/runs/round-7/v2-analysis.json`, `normalized_result.graph.edges[9].properties.imported_name`: `rot13` → `checksum`.
Target edge ID: `jag_edge_7a0c9240fb755c4a2d9a1d96638b81c2cc6b1af38bf9a6067a5dbfe81d202edf`.
AST rewrite changed only that JSON field semantically, plus one whitespace byte; record length 171150 → 171154.
Mutant record SHA-256: `52ec9fa676b3250714c740ddaf26ab56956f96f09ebc0592a1fd4beb6b0d04b4`.
Exact name-derived outputs (`renamed.stdout:21–22,25`):
```json
{"fixture":"js-r7-v2","counts":{"imports_edges":2,"named_imports_edges":1,"unnamed_imports_edges":1,"named_import_name_values":["checksum"]}}
{"fixture":"js-r7-v2","named_set_delta_within_fixture":{"kept":[],"removed_source_only":["rot13"],"added_record_only":["checksum"]}}
{"cross_record_named_name_value_delta":{"left":"js-r3","right":"js-r7-v2","removed":["rot13"],"added":[],"kept":["checksum"],"note":"over imported_name values only; the two records' edge sets are not compared"}}
```
M2: independently, after exact M1 restoration, removed only the same named edge and its array separator; valid JSON, every other byte preserved. Record length 171150 → 169207.
Mutant record SHA-256: `909c183e3422697d8cc9dd62485de98698bb9e6e26ae05853ff58ab1cac5a874`.
Exact name-derived outputs (`removed-edge.stdout:21–22,24`):
```json
{"fixture":"js-r7-v2","counts":{"imports_edges":1,"named_imports_edges":0,"unnamed_imports_edges":1,"named_import_name_values":[]}}
{"fixture":"js-r7-v2","named_set_delta_within_fixture":{"kept":[],"removed_source_only":["rot13"],"added_record_only":[]}}
{"cross_record_named_name_value_delta":{"left":"js-r3","right":"js-r7-v2","removed":["checksum","rot13"],"added":[],"kept":[],"note":"over imported_name values only; the two records' edge sets are not compared"}}
```
Pristine and both restorations instead emit `kept:["rot13"], removed_source_only:[], added_record_only:[]` within v2, and cross-record `removed:["checksum"], added:[], kept:["rot13"]` (`pristine.stdout:22,25`).

## Inference — what kills, and what does not
Both mutants SURVIVED an exit-only detector. M1 also preserves the 25-line count, so that count alone misses it.
Both are KILLED by manual semantic comparison of the emitted name deltas against the unchanged source line and pristine derivation; evidence is the mismatched names above, not just a changed record/stdout hash.
No contradiction to the expressly manual/no-guard contract (candidate:61–65,274–276) was found. Neither probe deletes a verifier clause; no Q13 deletion-sensitive guard credit follows.
Q11 is not satisfied merely by matching stdout: this probe validates the exercised name derivations, not every other factual assertion or recorded label in the entry. No failed Q is established within this assignment.

## Restoration and unknown
Each mutation was restored in a `finally` block using `/usr/bin/tar -xf $S/frozen.tar -C $S/tree corpus/live/runs/round-7/v2-analysis.json`; each restoration returned exit `0`, stderr empty.
Before either mutation and after each restoration, v2 SHA-256 was `331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e`; direct byte comparisons to the captured pristine record were `True`.
Each restored stdout was byte-equal to pristine; candidate bytes remained exactly unchanged at the hash above. Full outputs and `run-evidence.json` remain under S.
No fixture JS/EVM execution, producer/provider call, live probe, build/lint/formatter or production edit occurred. General parser/provider behavior, full-entry quality admission and C1 remain outside this probe.
VERDICT: HOLDS for this exact manual-readout attack; exit-only coverage gap explicitly demonstrated, not repaired or promoted. Installs: none.
