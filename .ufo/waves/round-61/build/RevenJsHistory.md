# RevenJsHistory: JavaScript/Electron round history for C04 (read-only)

Seat RevenJsHistory, read-only leaf, round 61 (C1/C04). LOG.md is 791 lines; pointers are LOG.md line numbers unless marked. `LEDGER` = `corpus/live/runs/<dir>/LEDGER.md`. Scores are as logged, not re-derived. C09/EVM rounds (r19-r26) are out of scope. No REA call, verifier run, git/jj, or install.

## 1. JavaScript rounds (r15 is ZIP and excluded)

| Rnd | LOG | Claim to fixture | REA op @ver to Evidence ID | Logged result | Review / halt / flag |
|---|---|---|---|---|---|
| r3 | 42-50 | static relation on authored tree; `fixtures/js-r3` (index.js:1 `const { rot13, checksum } = require('./transform')`; package.json `main` index.js, `type` commonjs) | `analyze-javascript-application` @6.4.0 (LEDGER:5) to `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e` (analysis.json:1) | 2 `imports` + 1 `maps_to`, REA label inferred; 3/3 declared units; depth improved (LOG:50) | non-author review-r1-r3.md:13; ledger check covers imports only (LEDGER:17); F5 |
| r4 | 52-60 | saved-proof verifier, r2 ZIP + r3 JS; `verify_saved_evidence.py`; no REA call | none (checks ev_4a93...) | self-test exit 0: JS 3/3 POSITIVE, `wrong.js` mutation NEGATIVE REJECTED (round-4-verification.md:8,10); calibration improved (LOG:60) | self-authored (LOG:60); first run KeyError on a guessed key (LOG:59); F16 |
| r6 | 80-88 | REA summary view of saved r3 record (projection) | `inspect-analysis-view` @6.4.0 (round-6/LEDGER:4) to `ev_f315c46639707ceebf91e518455204c9d9d55dd449168cb642af6dd116b916e6` (view.json:1) | 1/1 summary matches parent identity and statistics; 32 semantic unknowns; calibration improved (LOG:88) | round-6/reviewer.md:3 "narrowly"; `complete-within-view` is not semantic completeness (reviewer.md:11); F6 |
| r7 | 90-100 | REA comparison must name removed `checksum` import; `js-r3` vs `js-r7-v2` (v2 has two edits, F4) | `analyze-javascript-application` (v2) + `compare-application-versions` @6.4.0 (round-7/LEDGER:6) to v2 `ev_66f5dc7e3e8a8d6033c17c400762521d815d77c5ac9a9c7e1b6a45232cd7987c`, comparison `ev_5e4b17c1db1a06126558586f188b8eae81117c4d4bdf43d2278aefcd945f1a78` | 0/1 explicit removed-import item; 15 items, none names `checksum` (tool-validation-by-function-and-version.md:119-127); NOT admitted (LOG:100) | round-7/reviewer.md:15 "do not admit"; M02 manual reading (LOG:97-100; round-1.md:39); first `invalid_request` not retained (LEDGER:6); F2, F3 |
| r8 | 102-110 | analyst-side saved-graph delta; `verify_js_graph_delta.py` (no REA call) | inputs ev_4a93..., ev_66f5... | `--self-test` exit 0: removed `checksum` 1/1; stable `rot13` and main; altered v2 edge REJECTED (round-8/LEDGER:9); calibration improved (LOG:110) | round-8/reviewer.md:23; "not an output finding of compare_application_versions" (LEDGER:12); F3 |
| r9 | 112-122 | exact-seed trace keeps `./transform` imports; `js-r3` | `trace-application-feature` @6.4.0 (LEDGER:15) to exact-node `ev_bbe3fc094c348831e501701c0426496a234f39269854fb1f0f074d8120b2ce8d` (trace-exact.json:1); label seed `index.js` to `ev_a97e71e3bbacdef94d626cf572145653adc841f27ff324c24bf0c29a82a59d89` (trace.json:1) | 2/2 named imports; `contains`/`exposes` spillover; depth improved narrowly (LOG:122) | round-9/reviewer.md:13-15; label seed had two matches (LOG:120); F6, F7 |
| r12 | 148-159 | presence-only return-shape comparison; `shapes-r12` (final form `module.exports = describe`) | `compare-javascript-export-shapes`; NO REA version recorded (F10) to v1 `ev_2a492f5d829a57115e954269e08d4c7d8465f3129dd2f82ded2d01b2fb4e3064`, v2 `ev_913f14fa3ee334269cef30ff0af6835d6622a3053f08a5a4583260d7f35416d7`, comparison `ev_bb7e1c308a60b0cc45919a4a441347a0b6119df2c49f0de40c737615f94cb872` (comparison-direct.json:1) | 2/2 presence deltas; stable `/kind`, `/retained`; depth improved narrowly (LOG:159) | reviewer.md:3 "admit narrow"; object-literal variant unknowns; F9 |
| r13 | 161-170 | verifier for r12 comparison; `verify_shape_evidence.py` (no REA call) | none | `--self-test` exit 0: POSITIVE 2/2 presence; NEGATIVE REJECTED (round-13/LEDGER:6-7); calibration improved narrowly (LOG:170) | reviewer.md:3 "bounded pass, with a verifier-selection gap"; F12 |
| r14 | 172-181 | one non-containment semantic relation; `js-r3` `render` | `trace-javascript-semantics` @6.4.0 (round-14/LEDGER:3) to `ev_53329396d6fe4843b89806ef1ed98b6db8358ec91c41c733d617ea846b995a8a` (trace.json:1) | `found`; 3 `captures`, all source-matched; coverage partial; depth improved narrowly (LOG:181) | reviewer.md:3 "narrowly supported"; projection (reviewer.md:5); F8 |
| r16 | 194-203 | verifier for r14 trace; `verify_semantic_trace.py` (no REA call) | none | `--self-test` exit 0: POSITIVE 3/3; NEGATIVE REJECTED (round-16/LEDGER:6-7); calibration improved narrowly (LOG:203) | reviewer.md:3; 3/3 is precision, not recall (reviewer.md:9); F8 |
| r17 | 205-214 | source recovery of authored `index.js`; `js-r3/index.js` | `recover-javascript-sources` @6.4.0 (round-17/LEDGER:3) to exit 1, NO Evidence ID (recovery.json:1) | `capability_unavailable` / `unsupported_provider`; provider `wakaru`; needs `REA_WAKARU_COMMAND`; coverage unchanged; halted (LOG:214) | reviewer.md:3,5; M03 halt rule (round-1.md:40); F13 |
| r18 | 216-225 | one call-site alias `transformed` to `checksum` arg 0; `js-r3` | `trace-javascript-semantics` @6.4.0 (round-18/LEDGER:3) to `ev_03c9f793f2141ab3af930c6354ef649071afbbe234130d8d2e0c26aee21846b2` (trace.json:1) | `found`; 1 `aliases` relation; partial; depth improved narrowly (LOG:225) | reviewer.md:12; seed-ID typo corrected before commit (LOG:224; M09 round-1.md:46); F8 |
| r15 | 183-192 | NOT JS: ZIP duplicate-name `same.txt` (`duplicate-r15`) | `inspect-artifact` exit 1 `artifact_operation_failed` (LOG:191) | coverage unchanged | excluded; cited only for the halt rule (M03, round-1.md:40) |

No round exercises Electron. See F1 and section 4.

## 2. Non-round records that touch JS

- Promotion: LOG:72-78 and promotion-review-r5.md:14 restate r3 "3/3 declared"; no rank change (LOG:77-78); LOG:60 bars promotion from the self-authored verifier.
- Census: LOG:755 counts `javascript` in COVERAGE 4/8, a presence probe by its own wording; not capability.
- Pin: LOG:775 and corpus/knowledge/seed.md:60 (F05): host pin 6.4.0 to 6.7.0; "6.4.0 remains the saved-record producer version".
- Pre-registration: LOG:786-791 and reports/round-61/claims.md C1 scope C04 to CommonJS destructured-require named imports and package main, as static inference.
- Coverage map: README:30 C04 `uncovered`; its evidence list omits verify_saved_evidence.py, which README:36 files under C10. README:34,66 place Electron/CDP under C08 frontier.
- Sources: corpus/SOURCES.md has 0 hits for javascript|commonjs|ecmascript|node.js|electron|asar|npm|require( (grep, this seat). Any C04 entry needs a row opened this round (Q01, corpus/QUALITY.md:13).

## 3. Must not restate as fact (C04 entry)

- F1 Electron: no round tests an Electron app, BrowserWindow, preload, IPC, asar, or runtime. `electron-main` is REA's role label for package `main` (analysis.json node key `electron-main:package-entrypoint:index.js`; LEDGER r3:6; review-r1-r3.md:13). REA's Electron counters are 0 on js-r3 (view.json:1), but no positive Electron control exists, so counter sensitivity is untested.
- F2 r7: the REA comparison reports a changed `index.js` asset and an unchanged package/entrypoint role (comparison.json:1; reviewer.md:11). It does NOT identify the removed `checksum` import (0/1). Never credit `compare_application_versions` with import-removal detection (LEDGER r7:17).
- F3 r7/r8: the import-removal finding is analyst-side, either a manual reading (M02, LOG:97-100; LEDGER r7:13) or a scripted delta (r8, LEDGER r8:9-12). Label it analyst-side; it is 1/1 on one pair.
- F4 r7-v2 edits two things: the import list (index.js line 1) and the render return (index.js 209 B vs 274 B in the directory listing; reviewer.md:5). Attributing the delta to the import is by source reading, not isolation.
- F5 r3 "3/3" (LOG:49) overstates the ledger command: LEDGER r3:17 checks only the two `imports`. The `maps_to` unit is checked by verify_saved_evidence.py:110-118 (round-4-verification.md:8) and by verify_js_graph_delta.py (LEDGER r8:11). Cite those for package main (Q11, QUALITY.md:23).
- F6 Projections: r6, r9, r14, and r18 are projections or traces of the saved r3 parent ev_4a93..., not fresh analyses (LOG:86, LOG:120; round-14/reviewer.md:5). Count them as views of one parent, not replications.
- F7 r9: the label seed `index.js` matched two seeds (LOG:120; trace.json:1). Only the exact node-id trace is scored (LEDGER r9:14-15).
- F8 r14 (3 `captures`) and r18 (1 `aliases`) are partial (LEDGER r14:5, r18:5). `captures` are not calls (LEDGER r14:10); `aliases` are not runtime flow (LOG:225). The 3/3 and 1/1 are precision on returned references, not recall (round-16/reviewer.md:9).
- F9 r12: the object-literal form gave `missing`/`unavailable` (`ev_31a28f22...`, `ev_46bff65e...`; LOG:156; comparison.json:1; comparison-default.json:1). These are unknowns, not negative evidence. The source was revised after that result and the earlier source is not preserved (LOG:156-158); disclose the sequence. `default` is REA's selector label. Stable names come from inventories; REA emits no unchanged items (LEDGER r12:11).
- F10 Versions: round-12 records no REA pin or command (grep of round-12: 0 `rea-agents` hits), so do not attribute 6.4.0 to it. The other JS producers record `rea-agents@6.4.0` (LEDGER r3:5, r6:4, r7:6, r9:15 exact-seed only, r14:3, r17:3, r18:3). The host pin is now 6.7.0 (LOG:775; seed.md:60); do not describe 6.7.0 behavior.
- F11 Evidence IDs: JS records carry an absolute `local_path` under /home/vgpnk/Projects/prymeagnt (analysis.json:1; view.json:1). No JS path-invariance test exists; LOG:776 scopes path-sensitivity to inspect-pe-resources (M15, round-1.md:52).
- F12 r13: the selected-node tie was added after the reviewer's finding (LOG:169; verify_shape_evidence.py:79-80), but round-13/reviewer.md:11 still lists it as an open gap. No independent re-review of the patched check is recorded.
- F13 r17: no recovered output and no unminify or source-equivalence claim; Wakaru is not installed (recovery.json:1). Halted (LOG:214; M03).
- F14 Paths: LEDGER commands for r3 (:17), r6 (:7), r8 (:4), r12 (:15), and r14 (:3) use `.shokunin/revenger/...`, which is absent in revenger-shokunin (glob). The four JS verifiers resolve from `__file__` (verify_saved_evidence.py:11; verify_js_graph_delta.py:9; verify_shape_evidence.py:10; verify_semantic_trace.py:9). Restate commands on `corpus/...` (M14, round-1.md:51; Q03, QUALITY.md:15).
- F15 Wording: LOG:99 says "five module pairs unmatched"; LEDGER r7:12 and reviewer.md:7 say ten modules, five added and five removed. Use the ledger wording.
- F16 Independence: the r4 verifier is self-authored (LOG:60), and the only non-author review it cites (review-r1-r3.md) predates it (LOG:53).

## 4. Untested boundaries (falsifier candidates)

- Electron positive control: no fixture with BrowserWindow, preload, IPC, or asar. Any Electron claim needs one, where nonzero counters are expected.
- Syntax: no round tests non-destructured or dynamic `require`, ESM `import`, an `exports` field, `main` pointing at a subpath, or a missing-`main` fallback.
- ASAR: nested_asar_containers is 0 in the r3 parent statistics (view.json:1; round-14/trace-request.json:1484); no ASAR fixture was tested.
- Relocation: a replay of JS records from a relocated copy is untested (F11, F14).

VERDICT: 12 JS rounds reconstructed (r15 is ZIP, excluded). C04 may restate only the r3 import and package-main edges (via the r4 check), the r8 analyst-side delta, the r9 exact-node trace, and the r14/r18 partial static relations, each as inference. Electron, REA comparison capability, JS source recovery, and JS version or path stability are unsupported by any round.
Installs: none.
