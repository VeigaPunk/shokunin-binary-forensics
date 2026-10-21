GRADE: PARTIAL — C04 Limitations / Q13 verifier-credit precision
Axes: detector coverage; per-command credit precision; exact-byte restoration.
Scope: only this assignment's five saved-record mutations; no producer, JavaScript, bytecode, live-target or other-round execution.
Archive: ab580698212258a55e43e9bb9bf6ac78c91eae2a; Python 3.14.8; no detector source edits.
Setup, separately for each suffix name/entry/digest/span/unnamed: `mkdir -p "$R" && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar ab580698212258a55e43e9bb9bf6ac78c91eae2a | tar -x -C "$R"`.
Here R is `/tmp/revenger-r61w3-RevengerR61-2.W3JsVerifierCredit-<suffix>`; every detector invocation used cwd `/` and timeout 20 seconds.
D = `python3 -B "$R/corpus/verify_js_graph_delta.py" --self-test`; S = `python3 -B "$R/corpus/verify_saved_evidence.py" --self-test`.
v1 = corpus/live/runs/20261012T164357Z/analysis.json:1; v2 = corpus/live/runs/round-7/v2-analysis.json:1; JSON pointers below select within those single-line records.
Each mutation changed exactly one JSON scalar without reformatting other bytes; all five copies were restored in a finally block.

| Mutant / JSON pointer | Change | Expected D/S | Observed D pristine/mutated/restored | Observed S pristine/mutated/restored |
|---|---|---|---|---|
| name, v2 /normalized_result/graph/edges/9/properties/imported_name | rot13 → checksum | kill / survive | 0/1/0 KILLED | 0/0/0 SURVIVED |
| entry, v1 /normalized_result/graph/edges/2/properties/resolved_path | index.js → wrong.js | kill / kill | 0/1/0 KILLED | 0/1/0 KILLED |
| digest, v2 /normalized_result/graph/nodes/3/identity/sha256 | first hex digit b → a; other 63 unchanged | survive / survive | 0/0/0 SURVIVED | 0/0/0 SURVIVED |
| span, v1 /normalized_result/graph/edges/4/evidence/location/value/end/column | 50 → 49 (rot13 edge) | survive / survive | 0/0/0 SURVIVED | 0/0/0 SURVIVED |
| unnamed, v1 /normalized_result/graph/edges/9/relation | imports → contains (unnamed require no longer an imports edge) | survive / survive | 0/0/0 SURVIVED | 0/0/0 SURVIVED |

Actual clean stdout (D first two lines; S last four), stderr empty:
```text
POSITIVE saved parent graphs: removed checksum 1/1; stable rot13 and package-main; static inference only
NEGATIVE REJECTED saved graph disagrees with source truth
POSITIVE ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b ZIP root + 2 members: 3/3 identity units; formats, sizes, hashes, edges and fixture bytes match
POSITIVE ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e JS 2 imports + package main: 3/3 static inferred relationships match source/export and artifact digests
NEGATIVE ZIP REJECTED: ZIP: wrong root size/format
NEGATIVE JS REJECTED: JS: wrong package-main mapping
```
All 10 pristine and 10 restored invocations exited 0; restored stdout matched pristine exactly. All seven surviving mutant/verifier combinations also printed their exact clean stdout above, with empty stderr. Built-in NEGATIVE lines are not detection of those mutants.
Killed name/D and entry/D: stdout empty; traceback last line exactly `ValueError: saved graph disagrees with source truth` (D:58).
Killed entry/S: stdout only the ZIP POSITIVE line above; traceback last line exactly `ValueError: JS: wrong package-main mapping` (S:114-116).
No baseline failure, timeout or inconclusive result occurred; 30 detector invocations total.

SHA-256 before = restored for name/digest (v2): 331ec252aefdc7715e49f039d7443736ff9560565f208f35b4c972bfe45d564e.
SHA-256 before = restored for entry/span/unnamed (v1): 7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452.
Mutated SHA-256 name: 360d92b4b0476a04e0e0137ee5b1c3b7bc06c9b26820cc12170b3da3520419bf.
Mutated SHA-256 entry: 03d3585651cc82a55a1897823404ccdb41dee3f6696aa1e9f853a4c424c74213.
Mutated SHA-256 digest: 94cc4a3b431523ce36c74d63b96c69b1c012a26942a8a4864fb489ead689c490.
Mutated SHA-256 span: c4e1d4b2fe1a64c65fa852d3ab41f9a9dbd4b0ab5d55734fdb3d540656597cbc.
Mutated SHA-256 unnamed: 16174296a09a06663627b79b0f8893225640d43182fabb397611f09db21191fd.
Restoration additionally compared actual bytes with original bytes: True for all five files, before restored detector runs.
Full commands/stdout/stderr/JSON pointers/hashes retained in `/tmp/revenger-r61w3-RevengerR61-2.W3JsVerifierCredit-results.json`.

Finding: the aggregate restriction in corpus/knowledge/commonjs-destructured-require-edges.md:74-77 HOLDS for these five variants: the pair detects the selected name/main forgeries and neither detects the selected digest, span or unnamed-edge forgery.
Precision finding (wording PARTIAL, not a BROKEN collective claim): entry:74-76,202 does not assign credit per script/record. S never opens v2 (verify_saved_evidence.py:17,127), so its clean run cannot guard this v2 name. D reads both (verify_js_graph_delta.py:12-13,56-58,67). Exact credit should distinguish D's v1/v2 coverage from S's v1-only coverage.
Q13 qualification: corpus/QUALITY.md:25 requires clause-deletion sensitivity, not merely rejection of forged input data. This probe mutated records, not verifier clauses; it establishes the table, not a new per-clause deletion certificate. The entry's negative controls cover a v2 name in D (:69-79) and a v1 entry path in S (:133-143), not each value independently in each command.
This scoped result does not establish a false saved observation, changed live record/fixture, lost hold or an invalid K count. The seven surviving combinations are coverage findings, not a request to broaden the contract.
Installs/updates: none. Live-lane writes: only this report; all probe writes were in this seat's /tmp copies.
VERDICT: aggregate C04 limitations survive; per-verifier Q13 attribution is underspecified (PARTIAL); all five exact-byte restorations and all restored detectors succeeded.
