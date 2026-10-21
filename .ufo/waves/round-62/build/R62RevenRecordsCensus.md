RESULT: COMPLETE — saved EVM/JS analysis-record census, frozen a3498e25ad87bf756288812d0ea7c474b09433c7

Frozen corpus: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7` unpacked to `/fast/scratch/hyaku/revenger-r62/R62RevenRecordsCensus/` (archive rev == repo HEAD at extraction). All checks are stdlib-Python readouts of that copy, cwd=/; no fixture JS/EVM executed, no producer rerun, no live writes. Scratch scripts: `census_records.py`, `verify_bindings.py`, `dump_import_fields.py` (same scratch dir).

## 1. Fixture inventory — the intended selections exist and are exactly bounded

`ls corpus/fixtures` on the extracted copy: EVM `evm-r19` (fixture.hex+truth.json) and `evm-r21`…`evm-r26` (fixture.raw+truth.json) = **7 dirs, no evm-r20** (corpus/README.md:38). JS `js-r3`, `js-r7-v2` = **2 dirs** (index.js, package.json, transform.js each). `shapes-r12` is a separate fixture with v1/ and v2/ subpackages. Map rows: C04 binds `js-r3`, `js-r7-v2`, `shapes-r12`; C09 binds `evm-r19`, `evm-r21`…`evm-r26` — both `uncovered`, retained rejected candidates are evidence, not coverage (corpus/README.md:33,38,11-13,23-24).

## 2. EVM census — 7 fixtures → 7 saved records, 1:1, digest-bound

Operation per record is `inspect-evm-interface` (`grep -l inspect-evm-interface round-{19,21,22,23,24,25,26}/LEDGER.md` = 7/7):

| fixture | saved record (corpus/live/runs/) | evidence id prefix | saved candidates |
|---|---|---|---|
| evm-r19 | round-19/inspection.json | ev_0ad0097eb137f | 1 (dest 16) |
| evm-r21 | round-21/inspection.json | ev_4810eda7b540f | 1 (16) |
| evm-r22 | round-22/inspection.json | ev_24fe0001213ec | 2 (30, 32) |
| evm-r23 | round-23/inspection.json | ev_296e7ed723c73 | 0 |
| evm-r24 | round-24/inspection.json | ev_50d5ffb1fdbd1 | 0 |
| evm-r25 | round-25/inspection.json | ev_23a9464bf2d8c | 0 |
| evm-r26 | round-26/inspection.json | ev_482e41e68b6c5 | 0 |

Binding verified by digest, not name: each record's `subject.digest.sha256`, `normalized_result.artifact.sha256` and `normalized_result.bytecode.sha256` equal the recomputed SHA-256 of the carrier or its decoded bytes (7/7 records; verify_bindings.py). Candidate counts read from `normalized_result.functions`: 4 total across 7 records; all records kind=inferred, completeness=unknown. round-20 adds no record (receipt in round-20/LEDGER.md over the r19 record only, no JSON in dir). r25's record exists but its round was "Not admitted" telemetry (LOG.md:302) — usable only as a calibration control.

## 3. JS census — 2 fixtures → 2 parent graphs plus derived records

- js-r3 parent: `20261012T164357Z/analysis.json`, ev_4a93276c886da96f…, op `analyze-javascript-application`; 145 of its 174 digest fields equal the fixture source digests (index.js f7d8bf47…, transform.js cd9f3f63…, package.json 92ef8e3d…) and every graph-edge evidence artifact digest matches a fixture source digest.
- js-r7-v2 parent: `round-7/v2-analysis.json`, ev_66f5dc7e3e8a8d60…; 129/158 digest fields match (index.js b53d96d4…, shared transform/package digests).
- Shared: `round-7/comparison.json` ev_5e4b17c1db1a0… (`compare-application-versions`).
- js-r3-only derived: `round-6/view.json` ev_f315c466… (inspect-analysis-view, LOG.md:86); `round-9/trace.json` ev_a97e71e3… + `trace-exact.json` ev_bbe3fc09…; `round-14/trace.json` ev_53329396…; `round-18/trace.json` ev_03c9f793…. **No js-r7-v2 trace records exist.** `round-17/recovery.json` is a failed `recover-javascript-sources` (770 bytes, no Evidence ID). Receipts round-8/round-16 are LEDGER-only (no new JSON).

Saved import-name fields the C04 entry binds against (dump_import_fields.py): js-r3 has 3 `imports` edges — `imported_name` "rot13" (index.js 1:6–1:50), "checksum" (1:6–1:50), and one specifier-level edge with no imported_name (1:28–1:50). js-r7-v2 has 2 — "rot13" (1:6–1:40) and one unnamed specifier edge (1:18–1:40).

## 4. Coverage bounding — selections are subsets, not producer coverage

Saved JSON record files corpus-wide (excluding `*-request.json`): **93**; 10 name-bound to EVM/JS fixtures (7 EVM + 2 parents + 1 comparison; round-6/view.json also names js-r3), 4 to shapes-r12, 79 on other routes (PE rounds 27–59, archives 20261012T164246Z/r10/r11, duplicate-r15 round-15, native checksum-r1 attempt 20261012T163909Z). LEDGER sweep finds no EVM/JS binding outside rounds {164357Z, 6, 7, 8, 9, 12, 13, 14, 16, 17, 18, 19–26}. The intended selections — 2 JS fixtures (2 parent graphs) and 7 EVM fixtures (7 inspections) — are explicit subsets; phrasing them as "the producer's EVM/JS coverage" would overreach.

## 5. shapes-r12 omission rationale

shapes-r12 is a separate v1/v2 fixture pair on the export-shape axis: round-12 holds 4 saved graphs (v1 ev_b71e7b75…, v2 ev_6ede4369…, v1-direct ev_2a492f5d…, v2-direct ev_913f14fa…) plus 3 comparison records (ev_31a28f22…, ev_46bff65e…, ev_bb7e1c30…); round-13 is receipt-only (LOG.md:155-158,165). Those records are export-return-shape evidence, not CommonJS destructured-require import-name fields, so the C04 selection correctly bounds to js-r3/js-r7-v2 only; C09 omits it by route.

## 6. Explicit bounds the draft entries must state

- EVM entry (S031 scope): exactly these 7 fixtures/records; r19's carrier is a 39-byte hex text with a different digest than its 18 decoded bytes (LOG.md:234), and saved offset 16 is a JUMPDEST destination, not the selector byte offset (LOG.md:235); r25/r26 saved candidates are empty.
- JS entry (S030 scope): exactly js-r3/js-r7-v2 and the two parent graphs (optionally the round-7 comparison); the only saved name fields are rot13/checksum (v1) and rot13 (v2) with the ranges in §3; no v2 trace records exist.
- Neither entry may claim producer-wide, Electron-role, runtime or callable-interface coverage; every EVM record carries completeness=unknown and no producer was rerun here.

No tools installed or updated.
