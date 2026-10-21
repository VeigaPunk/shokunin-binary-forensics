GRADE: HOLDS — C04 Reproduce/Provenance comparison against the four assigned mutants
Target: `corpus/knowledge/commonjs-destructured-require-edges.md` (E below), especially E:3,88-179; C1 only, round 61 attempt 1.
Axes: output-change sensitivity; semantic attribution versus digest-only detection; exact-byte restoration.
Archive: `ab580698212258a55e43e9bb9bf6ac78c91eae2a`; `git archive --format=tar` SHA-256 `c774b23e31657f93c3818cc51eaf6cf53e287819805bdf2534f4ca9f880cab24`.
Scratch base B=`/tmp/revenger-r61w3-W3JsRecordMutant`; independent archives B-delete-v2, B-rename-v1, B-maps-to, B-electron.
Detector: exact E:91-143 block extracted to B/reproduce.py; SHA-256 `287a061d4b1847360e402f35f7c9fbd6650d1f7b656c0f3a2b84bc4cfaba9d92`.
Command, unchanged at every stage: `python3 -B /tmp/revenger-r61w3-W3JsRecordMutant/reproduce.py`, cwd each respective archive; 30-second bound per run; four independent runs concurrent per stage.
Expected detector: exit 0, empty stderr, and exact stdout equality to E:151-179 (the comparison required by E:3), not exit status alone.
Pristine: 4/4 exit=0, matches_provenance=True, stdout_lines=29, stderr=''. Expected stdout SHA-256 `2936df699a7758570858a5ef89c8b30ad4ac619ebb3bffa17bfac6a689530860`.
Record aliases: R1=`corpus/live/runs/20261012T164357Z/analysis.json`; R2=`corpus/live/runs/round-7/v2-analysis.json`; F=`corpus/fixtures/js-r3/index.js`.

Mutant 1 — delete R2 normalized_result.graph.edges[9], the sole named `rot13` imports edge (JSON line 1); do not alter the unnamed require edge.
Observed: exit=0, matches_provenance=False, stderr=''; 7/29 output lines change (E:169,171-174,177,179), including the record hash.
Exact changed semantic output: `v2 graph coverage=complete omitted=0 nodes=10 edges=11`; `v2 relations={'contains': 6, 'exposes': 2, 'imports': 1, 'loads': 1, 'maps_to': 1}`.
Exact changed semantic output: `v2 states={'inferred': 6, 'observed': 5}`; `v2 imports=1 named=[] unnamed_require=1`; `v2 agrees_with_source names=False main=True`.
Exact changed delta: `delta named removed=['checksum', 'rot13'] added=[] kept=[]`.
Verdict: KILLED by documented output comparison; SURVIVED an exit-only detector.
R2 before/restored SHA-256: `331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e`.
R2 mutated SHA-256: `909c183e3422697d8cc9dd62485de98698bb9e6e26ae05853ff58ab1cac5a874`.

Mutant 2 — rename only R1 normalized_result.graph.edges[10].properties.imported_name `checksum` → `checksum_typo` (JSON line 1).
Observed: exit=0, matches_provenance=False, stderr=''; 4/29 output lines change (E:159,164,167,179), including the record hash.
Exact changed semantic output: `v1 imports=3 named=['checksum_typo', 'rot13'] unnamed_require=1`; `v1 agrees_with_source names=False main=True`.
Exact changed delta: `delta named removed=['checksum_typo'] added=[] kept=['rot13']`.
Verdict: KILLED by documented output comparison; SURVIVED an exit-only detector.
R1 before/restored SHA-256: `7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452`.
R1 mutated SHA-256: `97e4165eda2281920a7f0827ea5fdef3536d1482518baca1b31701567e3e12f3`.

Mutant 3 — redirect R1 normalized_result.graph.edges[2].target_node_id from the existing index.js asset to the existing transform.js asset (JSON line 1); leave properties.resolved_path unchanged.
Old node: `jag_node_874a0ded3c6224e6c2d6ff103b2e60f19c681ba3934a692e8aa6ab7c38cbc246`; new: `jag_node_b054a72f8c99d2330e7e033a4a0b3eab45d67b90a93a15415885819e6c981c77`.
Observed: exit=0, matches_provenance=False, stderr=''; ONLY E:159 changes: `v1 record analysis.json sha256=5b0a6357f9cf97450a3cada65cf95961b284ad83d535457900e0c7f13a4986f5`.
Exact unchanged output: `v1 package_entrypoint_maps_to=1 resolved=['index.js'] state=['inferred']`; `v1 agrees_with_source names=True main=True`.
Verdict: KILLED by the record-digest comparison only; SURVIVED an exit-only detector. Semantic target-node validation is absent: E:133-136 reads resolved_path, not target_node_id.
R1 before/restored SHA-256: `7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452`.
R1 mutated SHA-256: `5b0a6357f9cf97450a3cada65cf95961b284ad83d535457900e0c7f13a4986f5`.

Mutant 4 — append the inert comment `// electron` at F:8; no fixture JavaScript execution.
Observed: exit=0, matches_provenance=False, stderr=''; 2/29 output lines change (E:151,168): fixture hash and electron_tokens=0 → 1.
Exact changed output: `v1 node_kinds=['artifact', 'electron-main', 'javascript-asset', 'javascript-module', 'package'] exposes_exported_names=['default'] exports_field=False electron_tokens=1`.
Verdict: KILLED by documented output comparison; SURVIVED an exit-only detector. This tests text counting, not Electron behavior.
F before/restored SHA-256: `f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7`.
F mutated SHA-256: `824958d0d7baa9b120003aa2e0fd94f78a754e5db944c71b6f7deacf670b1139`.

Restoration: finally-block restored all four exact original byte strings; bytes_exact=True for every target, hashes equal the before values above.
Restored detector: 4/4 exit=0, matches_provenance=True, stderr=''; all outputs again equal the same 29-line Provenance block. No baseline failure; none inconclusive.
Evidence: B/mutation-evidence.json retains commands, mutation paths, full stdout/stderr, return codes, comparisons and hashes; B/{delete-v2,rename-v1,maps-to,electron}.{pristine,mutated,restored}.stdout retain all 12 outputs.
Scope: only extracted archives were probed/mutated; no REA producer, fixture execution, live target, build/lint/formatter, source-page claim, or sibling/source-tree mutation. No general C1 admission judgment follows from four probes.
Installs/updates: none.
VERDICT: Documented output comparison detects 4/4 assigned mutants; exit status detects 0/4, and maps_to node-target corruption is visible only through its changed saved-record digest; exact restoration confirmed for all four.
