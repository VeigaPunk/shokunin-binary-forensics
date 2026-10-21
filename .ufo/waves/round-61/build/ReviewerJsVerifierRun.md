# ReviewerJsVerifierRun — round 61 C04: what the two self-tests guard (RUNS, read-only)
Seat CloseChousa26.ReviewerJsVerifierRun-10 · base e0a4b0c4348ef1fade46539f520e94fa140c4d8a (commit verified) · copy `/tmp/revenger-r61-ReviewerJsVerifierRun/corpus` (`git archive <base> corpus | tar -x`, 466 files) · no lane write, no producer call, no bytecode run · axes: record-guard coverage × negative-control sensitivity × scope honesty.

## Run (assigned; exact stdout)
```
$ cd /tmp/revenger-r61-ReviewerJsVerifierRun/corpus && PYTHONDONTWRITEBYTECODE=1 python3 -B verify_js_graph_delta.py --self-test
POSITIVE saved parent graphs: removed checksum 1/1; stable rot13 and package-main; static inference only
NEGATIVE REJECTED saved graph disagrees with source truth
EXIT=0
$ PYTHONDONTWRITEBYTECODE=1 python3 -B verify_saved_evidence.py --self-test
POSITIVE ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b ZIP root + 2 members: 3/3 identity units; formats, sizes, hashes, edges and fixture bytes match
POSITIVE ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e JS 2 imports + package main: 3/3 static inferred relationships match source/export and artifact digests
NEGATIVE ZIP REJECTED: ZIP: wrong root size/format
NEGATIVE JS REJECTED: JS: wrong package-main mapping
EXIT=0
tree sha256 before/after (466 files): identical; __pycache__ dirs: 0
```

## Method
POSITIVE asserts run on every invocation; a saved-record violation raises before any NEGATIVE line, so exit≠0 (js_graph_delta:68; saved_evidence:128-129). `--self-test` adds negative controls: js_graph_delta has one (js_graph_delta:69-79, v2 rot13 name); saved_evidence has two (ZIP root size, out of C04 scope; JS main resolved_path, saved_evidence:130-143). NC = that mutation is rejected. Non-run outcomes are [INFERENCE] from code lines; peer results are cited as peer, not re-run.

## Would guard (saved-record or fixture drift → exit≠0)
G1 names per record = destructured names in authored index.js (v1 {checksum,rot13}; v2 {rot13}) · js_graph_delta:43-44,56-58; saved_evidence:91,99-101 · NC yes (v2 rot13→checksum)
G2 named edge: specifier ./transform, resolved transform.js, status resolved, state inferred, source index.js · js_graph_delta:37-42 (v1+v2); saved_evidence:102-109 (v1, +local_name==imported_name, line 1) · NC no (peer M04)
G3 one package-entrypoint maps_to; resolved_path == package.json main "index.js"; status resolved; state inferred · js_graph_delta:45-49,58 (v1+v2); saved_evidence:110-117 (v1) · NC yes (v1 resolved_path→wrong.js)
G4 v1 maps_to declared_path == "index.js"; location path package.json · saved_evidence:114,117 (v1) · NC no
G5 no duplicate named imports · js_graph_delta:43-44 · NC no (peer M05)
G6 graph coverage complete, omitted_count 0; operation analyze_javascript_application · js_graph_delta:31,33-34 (v1+v2) · NC no (peer M02, M03)
G7 parent Evidence IDs equal pinned literals (identity pin; IDs never recomputed from content) · js_graph_delta:53-55; saved_evidence:19,82 · NC no (peer M07)
G8 saved delta v1→v2: checksum removed, rot13 kept, main stable · js_graph_delta:59-62 vs fixture truth; equality :58 carries it to records · NC no on :59-62 (peer M09)
G9 v1 javascript-asset identities = SHA-256 of js-r3 index.js and transform.js · saved_evidence:96-98 (v1) · NC no
G10 v1 semantic_graph.coverage.status == "unknown" · saved_evidence:119-120 (v1) · NC no
G11 fixture premises: destructured names and specifier, exports == names, main index.js, type commonjs · js_graph_delta:21-27,57 (both); saved_evidence:87-95 (js-r3) · NC no

## Would not guard (drift keeps the recheck green)
N1 v2 maps_to declared_path and location path · js_graph_delta:49 reads resolved_path only; saved_evidence reads v1 only
N2 digests: v2 index.js identity b53d96d4…; subjects 696c2496… (v2), 8eec9ffb… (v1); package.json 92ef8e3d… computed at saved_evidence:96, never compared (:97-98 cover javascript-asset nodes only)
N3 js-r7-v2 bytes beyond require names and main (render line, transform.js, package.json): no digest, no type check; Q06 premise unguarded for v2
N4 v2 semantic coverage · js_graph_delta never reads semantic_graph; saved_evidence reads v1 only (:119)
N5 named-edge columns (v1 1:6–1:50; v2 1:6–1:40); only v1 start line checked (saved_evidence:108)
N6 unnamed broad `kind:require` edge (v1 1:28–1:50; v2 1:18–1:40): presence, count, span · filtered at js_graph_delta:36, saved_evidence:99; draft's "one unnamed edge per require" unguarded
N7 exported_name null on every named edge (both records); module_link_kind, imported_path, target_file_kind, target_json_status unread; exports regex (saved_evidence:92-94) checks fixture, not record
N8 "static inference" beyond C04 edges: `contains` edges are state observed (both records); literal "static inference only" (js_graph_delta:63) is not computed
N9 producer identity: rea-agents@6.4.0 appears only in LEDGER prose (20261012T164357Z:5; round-7:6); record provider.version is "1"; no verifier reads provider/version; re-run barred → any present-tense "REA does X" unguarded (Q05)
N10 Node/CommonJS semantics, runtime behavior, main rules (draft S016/S017, unregistered), exports precedence, main vs index.js fallback (undiscriminated: main is index.js), ESM, dynamic require, renames, multi-site require, bare specifiers, asar; specifier and resolved transform.js are author literals (js_graph_delta:37-38). No fixture, or a regex miss fails rather than passes: untested both ways. Draft F1–F4 are producer falsifiers this recheck cannot run
N11 `electron-main` node kind (v1, v2): no verifier references "electron" (0 matches, both files)
N12 compare-application-versions output (ev_5e4b17c1…): no reader; round-7 LEDGER:17 records 0/1 removed named import identified → no comparison statement guarded, one contradicted
N13 counts (nodes 10; edges 13 v1 / 12 v2; relation and state tallies): unchecked; only bindings==2 (saved_evidence:100)
N14 guard sensitivity: C04 negative controls = 2 (G1 via js_graph_delta; G3 via saved_evidence JS). Peer MutantJsVerifier.md:18-26,45 (not re-run): 8 of 9 single-require mutants of js_graph_delta survive; only :58 killed. A green run does not show each G-guard is live

## First falsifiers (predicted by code reading; NOT run, Q07)
F1 v1 named edge state inferred→observed: caught (saved_evidence:107; js_graph_delta:40)
F2 js-r3/index.js destructuring gains `extra`: caught (saved_evidence:91; js_graph_delta:58)
F3 v2 maps_to declared_path→"main.js": not caught (js_graph_delta:49)
F4 v2 index.js identity digest edited in record: not caught (N2)
F5 js-r7-v2/index.js render line edited, names/main unchanged: not caught; record stays green (N3)
F6 js-r3/transform.js body edited, exports unchanged: caught (saved_evidence:98, v1 only); same edit in js-r7-v2: not caught
F7 v2 named edge exported_name→"rot13": not caught (N7)

## Verifier defects (reported, not fixed)
D1 POSITIVE strings are literals returned on success: js_graph_delta:63 ("1/1", "static inference only"); saved_evidence:77,121 ("3/3 … artifact digests"). Only exit codes are computed; Q08/Q11 readers must not cite stdout as counts
D2 saved_evidence:96 expected_sha["package.json"] computed, never compared (dead guard)
D3 js_graph_delta:23-24 re.search takes the first destructuring only: a record that omits a second site's edges would pass
D4 v2 is read only by js_graph_delta; saved_evidence has no round-7 reference

Corroboration: peers ScribeEntryJs.md:21-45 and CriticJsScope.md:8-35 name the same gaps (N1, N2, N7, N9, N11, N12). The draft's Reproduce block (ScribeEntryJs.md:56-107) adds the digest and count derivations these self-tests lack; it has no negative control either. Not run here: that block, the REA CLI, comparison.json, verify_semantic_trace.py, verify_shape_evidence.py.
Installs: none (Python 3.14.8 preinstalled). Written: this report (own file in the lane); scratch manifests /tmp/revenger-r61-ReviewerJsVerifierRun-scratch/tree-{before,after}.sha256. No other lane write.

VERDICT: the two self-tests guard C04 record facts G1–G11 against drift, with negative controls only for G1 (v2 rot13 name) and G3 (v1 main path); they cannot guard v2 digests/declared_path/location, export binding, producer version, Node/Electron semantics, counts or comparison output, so they are not sufficient alone for C04 admission.
