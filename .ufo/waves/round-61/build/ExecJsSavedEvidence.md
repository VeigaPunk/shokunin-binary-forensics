# ExecJsSavedEvidence — C1/C04 JS verifier run (read-only)

Seat `CloseChousa26.ExecJsSavedEvidence-10` · r61 · lane `revenger-shokunin` · base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` (clone HEAD, observed) · 2026-10-21. Axes: runnability · JS assertion reach · mutant rejection · unbound fields

## Records (SHA-256; live and clone copies byte-identical)
- Verifier `corpus/verify_saved_evidence.py` 7fbd193232d6be8f5b9997554d7769e90f0fb7b97a502fbd65fb557bafd8c930
- JS record `corpus/live/runs/20261012T164357Z/analysis.json` 7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452 (193,573 B; evidence_id ev_4a93…c1c7e; LEDGER.md 8e82a1f2f295b45a…)
- ZIP record `corpus/live/runs/20261012T164246Z/artifact-inspection.json` 2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380
- Fixture `corpus/fixtures/js-r3/`: index.js f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7, transform.js cd9f3f633355d38c77dd0a26550d13b944b2502d4b0748f19607e36caa7fa345, package.json 92ef8e3d5d3af1c34282669efb259661ac0739e8630aca5972c92c03ea1096d7 (equal to LEDGER.md:4)

## Self-test (clone `/tmp/revenger-r61-ExecJsSavedEvidence`; `python3 -B corpus/verify_saved_evidence.py --self-test`; Python 3.14.8; exit=0; clone git status empty after)
```
POSITIVE ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b ZIP root + 2 members: 3/3 identity units; formats, sizes, hashes, edges and fixture bytes match
POSITIVE ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e JS 2 imports + package main: 3/3 static inferred relationships match source/export and artifact digests
NEGATIVE ZIP REJECTED: ZIP: wrong root size/format
NEGATIVE JS REJECTED: JS: wrong package-main mapping
```

## JS assertions: `verify_js` lines 80-121, traced on saved record (14 sites, 16 executions, all PASS; caller line via sys._getframe)
| line | message | observed |
|---|---|---|
| 81-82 | JS: wrong REA operation / unexpected Evidence ID | analyze_javascript_application; ev_4a93…c1c7e |
| 89 | JS: expected source require missing | index.js:1 `const { rot13, checksum } = require('./transform');` |
| 91 | JS: source imports changed | {checksum, rot13}; specifier ./transform |
| 93 | JS: source exports changed | transform.js exports {checksum, rot13} (regex over fixture text) |
| 95 | JS: package main changed | main index.js; type commonjs |
| 97 | JS: REA asset digests differ from source | 2 javascript-asset sha256 = sha256(index.js), sha256(transform.js) |
| 100 | JS: missing/duplicate named bindings | 2 `imports` edges, imported_name in {rot13, checksum} |
| 104 (x2) | JS: wrong import resolution | specifier ./transform; resolved_path transform.js; resolved; local==imported |
| 107 (x2) | JS: wrong import evidence kind/source | state inferred; location.value source index.js, start.line 1 |
| 112 | JS: wrong package-entrypoint count | 1 `maps_to`, resolution_context package-entrypoint |
| 114 | JS: wrong package-main mapping | declared_path index.js = package.json main; resolved_path index.js; resolved |
| 117 | JS: wrong package-main evidence kind/source | state inferred; location {artifact-path, package.json} |
| 119 | JS: unknown semantic coverage unexpectedly changed; reassess conclusion | semantic_graph.coverage.status = unknown |
Unasserted: line 96 computes `expected_sha["package.json"]`, unused; line 121 "artifact digests" covers only index.js and transform.js. Package-main negative (main() 130-143): one in-memory mutant (lines 134-136, `resolved_path="wrong.js"`) rejected at 114; no negative record saved; the only JS self-test negative (1 of 14 sites).

## Scratch mutants (in-memory on analysis.json, or js-r3 copies under /tmp/revenger-r61-ExecJsSavedEvidence-scratch/fx-*)
| id | mutation | verdict |
|---|---|---|
| R00 / F00 | control | ACCEPTED |
| R01 | package-main resolved_path=wrong.js (self-test) | REJECTED, wrong package-main mapping (114) |
| R02, R03 | package-main declared_path / resolution_status | REJECTED, wrong package-main mapping (114) |
| R04, R05 | package-main evidence.state / location path | REJECTED, package-main evidence kind/source (117) |
| R06, R07 | package-main edge removed / duplicated | REJECTED, package-entrypoint count (112) |
| R08, R13, R14 | import resolved_path / local_name / specifier | REJECTED, wrong import resolution (104) |
| R09, R10 | import evidence.state / start.line=2 | REJECTED, import evidence kind/source (107) |
| R11, R12 | imported_name deleted / rot13 duplicated | REJECTED, missing/duplicate bindings (100) |
| R15-R18 | asset sha256 / coverage=complete / evidence_id / operation | REJECTED (97, 119, 82, 81) |
| **R19** | subject directory digest replaced (7 occurrences) | **ACCEPTED** |
| **R20** | import-edge evidence confidence=low (2 edits) | **ACCEPTED** |
| F01, F02 | package.json main=electron.js / type=module | REJECTED, package main changed (95) |
| **F03** | package.json + trailing newline | **ACCEPTED** |
| F04, F05 | index.js drops checksum / specifier ./transform.js | REJECTED, source imports changed (91) |
| F06, F07 | transform.js exports drop checksum / trailing comment | REJECTED (93) / REJECTED asset digests (97) |

## Facts the verifier never asserts (wording limits for C04)
- `loads` edge package<package.json> -> electron-main<...:index.js>: package-entrypoint, resolved, inferred, confidence high. LEDGER.md:6: electron-main is a package-entrypoint convention, not evidence Electron ran.
- `exposes` x2 (commonjs-export, exported_name `default`): module-level only; named-export check (93-94) reads fixture text. Broad `imports` edge (imported_name null) excluded by line 99 (LEDGER.md:16).
- 12 semantic families all partial; 32 unknown IDs = LEDGER.md:14. `subject.local_path` = /home/vgpnk/Projects/prymeagnt/revenger/... (authoring location), unchecked.

## Findings (first falsifiers)
1. Self-test covers 1 of 14 JS sites; the sweep rejects every other claimed-relation mutant, but `--self-test` does not keep them so.
2. Unbound: subject digest (R19), edge confidence that LEDGER.md:11 states as high (R20), package.json bytes (F03; line 96 computed, unused).
3. No defect in the three claimed relations: R01-R14, F01-F02, F04-F05 all rejected.

Installs: none (python3 3.14.8, git, sha256sum present). Writes: this report; clone unchanged; scratch fx-* copies under /tmp only.

VERDICT: JS branch passes `--self-test` (exit 0) and rejects every mutant of the three claimed relations, but leaves subject digest, edge confidence and package.json bytes unbound and has a single JS negative.
