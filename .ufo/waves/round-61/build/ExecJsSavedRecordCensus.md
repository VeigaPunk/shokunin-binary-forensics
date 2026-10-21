# ExecJsSavedRecordCensus — round 61 (RUNS, read-only)

Seat CloseChousa26.ExecJsSavedRecordCensus-10 · base e0a4b0c4348ef1fade46539f520e94fa140c4d8a (lane HEAD `e0a4b0c`; `.ufo/waves/round-61/` untracked, pre-existing). Scope: every saved `analyze_javascript_application` record under `corpus/live/runs`. Lane-side effects: this report only, plus one `git rev-parse` and one `git status --short` (read-only; git may refresh its index stat cache, no tracked content touched). No clone, no REA calls, no bytecode execution.

## Command (one invocation)
`python3 -B /tmp/revenger-r61-ExecJsSavedRecordCensus-census.py /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs` → exit 0
- script sha256 `4e48c99ad4b88c31731de26bbae21db6389337390fdb0bcee577beccd3179d76`
- output sha256 `1fb706460059e272b1cd23dca84ace4b500057d7f6ee351c3449b7391dee4435` (`/tmp/revenger-r61-ExecJsSavedRecordCensus-output.txt`)

## Exact output
```
| file | at | evidence_id | graph_cov | omitted | imports named/total | maps_to pkg/total | edge_states | node_obs_states | sem_cov | sem_resolution | copy |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 20261012T164357Z/analysis.json | $ | ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e | complete | 0 | 2/3 | 1/1 | inferred=8,observed=5 | inferred=1,observed=9 | unknown(omit 0+0) | candidate=18,resolved=47 | top |
| round-12/comparison-default-request.json | $.left | ev_b71e7b75d7ca3cbf44da6e3f1c31a039a9c883ed7417a198554f79ceea2433e3 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=1,observed=6 | unknown(omit 0+0) | resolved=2 | same |
| round-12/comparison-default-request.json | $.right | ev_6ede4369cfdf7e426a4690f0e2ff701ca77bb5381ee3af8720786316601ec740 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=1,observed=6 | unknown(omit 0+0) | resolved=2 | same |
| round-12/comparison-direct-request.json | $.left | ev_2a492f5d829a57115e954269e08d4c7d8465f3129dd2f82ded2d01b2fb4e3064 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=2,observed=6 | unknown(omit 0+0) | resolved=2 | same |
| round-12/comparison-direct-request.json | $.right | ev_913f14fa3ee334269cef30ff0af6835d6622a3053f08a5a4583260d7f35416d7 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=2,observed=6 | unknown(omit 0+0) | resolved=2 | same |
| round-12/comparison-request.json | $.left | ev_b71e7b75d7ca3cbf44da6e3f1c31a039a9c883ed7417a198554f79ceea2433e3 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=1,observed=6 | unknown(omit 0+0) | resolved=2 | same |
| round-12/comparison-request.json | $.right | ev_6ede4369cfdf7e426a4690f0e2ff701ca77bb5381ee3af8720786316601ec740 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=1,observed=6 | unknown(omit 0+0) | resolved=2 | same |
| round-12/v1-analysis.json | $ | ev_b71e7b75d7ca3cbf44da6e3f1c31a039a9c883ed7417a198554f79ceea2433e3 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=1,observed=6 | unknown(omit 0+0) | resolved=2 | top |
| round-12/v1-direct-analysis.json | $ | ev_2a492f5d829a57115e954269e08d4c7d8465f3129dd2f82ded2d01b2fb4e3064 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=2,observed=6 | unknown(omit 0+0) | resolved=2 | top |
| round-12/v2-analysis.json | $ | ev_6ede4369cfdf7e426a4690f0e2ff701ca77bb5381ee3af8720786316601ec740 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=1,observed=6 | unknown(omit 0+0) | resolved=2 | top |
| round-12/v2-direct-analysis.json | $ | ev_913f14fa3ee334269cef30ff0af6835d6622a3053f08a5a4583260d7f35416d7 | complete | 0 | 0/0 | 1/1 | inferred=4,observed=3 | inferred=2,observed=6 | unknown(omit 0+0) | resolved=2 | top |
| round-14/trace-request.json | $.application | ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e | complete | 0 | 2/3 | 1/1 | inferred=8,observed=5 | inferred=1,observed=9 | unknown(omit 0+0) | candidate=18,resolved=47 | same |
| round-18/trace-request.json | $.application | ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e | complete | 0 | 2/3 | 1/1 | inferred=8,observed=5 | inferred=1,observed=9 | unknown(omit 0+0) | candidate=18,resolved=47 | same |
| round-6/view-request.json | $.source.evidence | ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e | complete | 0 | 2/3 | 1/1 | inferred=8,observed=5 | inferred=1,observed=9 | unknown(omit 0+0) | candidate=18,resolved=47 | same |
| round-7/comparison-request.json | $.left | ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e | complete | 0 | 2/3 | 1/1 | inferred=8,observed=5 | inferred=1,observed=9 | unknown(omit 0+0) | candidate=18,resolved=47 | same |
| round-7/comparison-request.json | $.right | ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c | complete | 0 | 1/2 | 1/1 | inferred=7,observed=5 | inferred=1,observed=9 | unknown(omit 0+0) | candidate=16,resolved=42 | same |
| round-7/v2-analysis.json | $ | ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c | complete | 0 | 1/2 | 1/1 | inferred=7,observed=5 | inferred=1,observed=9 | unknown(omit 0+0) | candidate=16,resolved=42 | top |
| round-9/trace-exact-request.json | $.application | ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e | complete | 0 | 2/3 | 1/1 | inferred=8,observed=5 | inferred=1,observed=9 | unknown(omit 0+0) | candidate=18,resolved=47 | same |
| round-9/trace-request.json | $.application | ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e | complete | 0 | 2/3 | 1/1 | inferred=8,observed=5 | inferred=1,observed=9 | unknown(omit 0+0) | candidate=18,resolved=47 | same |

files_scanned=344 kinds=binary=6,json=104,jsonl=6,text=228 json_suffix_unparsed=0
records=19 top_level=6 embedded=13 unique_evidence_ids=6 top_id_duplicates=0
copy_status=same=13,top=6
op_bearing_non_record_objects=186 (extractor provenance, excluded) 20261012T164357Z/analysis.json:16; round-12/comparison-default-request.json:8; round-12/comparison-direct-request.json:8; round-12/comparison-request.json:8; round-12/v1-analysis.json:4; round-12/v1-direct-analysis.json:4; round-12/v2-analysis.json:4; round-12/v2-direct-analysis.json:4; round-14/trace-request.json:16; round-14/trace.json:2; round-18/trace-request.json:16; round-18/trace.json:2; round-6/view-request.json:16; round-7/comparison-request.json:31; round-7/v2-analysis.json:15; round-9/trace-exact-request.json:16; round-9/trace-request.json:16
token_bearing_files_with_zero_records=20261012T164357Z/analysis.stderr(jsonl); promotion-review-r5.md(text); round-12/v1-analysis.stderr(jsonl); round-12/v1-direct-analysis.stderr(jsonl); round-12/v2-analysis.stderr(jsonl); round-12/v2-direct-analysis.stderr(jsonl); round-14/trace.json(json); round-18/trace.json(json); round-27/route-sentinel.md(text); round-6/reviewer.md(text); round-6/view.json(json); round-7/v2-analysis.stderr(jsonl)
```

## Definitions (script semantics)
- Record: `operation=="analyze_javascript_application"` + `predicate_type=="rea.javascript-application-analysis"` + `normalized_result` + `evidence_id`, at any depth. `$` = top-level file; other pointers = embedded copies.
- graph_cov/omitted = `normalized_result.graph.coverage.status`/`.omitted_count`. imports named = imports edges with non-empty `properties.imported_name`. maps_to pkg = maps_to edges with `resolution_context=="package-entrypoint"`.
- edge_states/node_obs_states = `evidence.state` on graph edges / node observations. sem_resolution = `semantic_graph.relations[].resolution` (semantic evidence has no `state`).
- copy: `same` = canonical JSON identical to the top-level record with that evidence_id (`jq -S` sha256 agrees).

## Findings
1. 19 records = 6 top-level Evidence + 13 embedded copies; 6 unique evidence IDs; `copy_status=same=13,top=6`.
2. Graph coverage `complete`, `omitted_count` 0 on all 19 rows; semantic coverage `unknown(omit 0+0)` on all 19 rows.
3. Named imports per unique ID: ev_4a93… (`fixtures/js-r3`) 2/3 (`rot13`, `checksum`; third edge is an unnamed broad `require`); ev_66f5… (`fixtures/js-r7-v2`) 1/2 (`rot13`); ev_b71e…, ev_2a49…, ev_6ede…, ev_913f… (`fixtures/shapes-r12/v1|v2`) 0/0. Total: 3 named edges in 2 unique records.
4. maps_to package-entrypoint 1/1 on every row = 6 of 6 unique records. In ev_4a93…, all 3 imports edges and the maps_to edge are `state=inferred`.
5. Excluded, not rows: 186 extractor-provenance objects (`{executable_sha256,name,operation,version}`, no evidence_id). `json_suffix_unparsed=0`; `files_scanned=344` matches `find -type f | wc -l`.
6. Cross-check (`jq` = jaq 3.1.1 over all 104 `.json`): 205 operation-bearing objects = 19 records + 186 extractor objects; all 19 records carry `evidence_id`.

## Limits and falsifiers
- Saved records only: no producer provenance, no fixture-byte check, no re-analysis; `same` is structural identity, not authentication.
- [INFERENCE] For C04, saved named-import evidence is 2 unique records / 3 edges; row counts overstate independence (19/6 ≈ 3.2×).
- Would break this census: any `DIFF@` or `no-top` row, `json_suffix_unparsed>0`, or a record hidden in non-JSON text. None observed.

Installs: none. Tools: `/usr/bin/python3` 3.14.8 (stdlib), `jq` = jaq 3.1.1, `rg` 15.1.0, all pre-existing. Files written: `/tmp/revenger-r61-ExecJsSavedRecordCensus-census.py`, `/tmp/revenger-r61-ExecJsSavedRecordCensus-output.txt`, this report. Removed own scratch `/tmp/census-candidates.txt`.

VERDICT: Census of 344 files gives 19 records / 6 unique IDs, all graph coverage complete (omitted 0); 3 named import edges in 2 unique records; package-entrypoint maps_to on 6/6; read-only, no installs.
