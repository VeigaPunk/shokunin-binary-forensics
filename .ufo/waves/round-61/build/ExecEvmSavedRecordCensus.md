# ExecEvmSavedRecordCensus — round 61 attempt 1 (RUNS, read-only)

Seat CloseChousa26.ExecEvmSavedRecordCensus-10. Pre-registration e0a4b0c4348ef1fade46539f520e94fa140c4d8a cited, not re-observed; no git/jj run on the lane.
Subject: `/tmp/revenger-r61-ExecEvmSavedRecordCensus-10/corpus`, a copy of live `corpus/live` + `corpus/fixtures` (`diff -rq` vs live: empty). One `_eval` (py) cell: rglob `*.json` under `live/runs`, `json.loads`, `operation` field, fixture digests vs `truth.json`. No REA call, no bytecode executed, no chain access.
python 3.14.8 | subject=/tmp/revenger-r61-ExecEvmSavedRecordCensus-10/corpus (copy of corpus/live + corpus/fixtures; diff -rq vs live clean)
input_files=443 input_manifest_sha256=9de9c03f01f046712ab930e7dee3bfca63eda74e669c8fcc17a1269b71a4497e
json_files=104 parse_errors=none inspect_evm_interface_records=7
operation_counts={"None": 46, "analyze_javascript_application": 6, "compare_application_versions": 1, "compare_javascript_export_shapes": 3, "extract_artifact": 2, "inspect_analysis_view": 1, "inspect_artifact": 4, "inspect_evm_interface": 7, "inspect_pe_resources": 30, "trace_application_feature": 2, "trace_javascript_semantics": 2}

**TABLE 1 census (requested columns)**

| file | evidence_id | functions | selectors | bytecode_offset | evidence_kind | discovery_completeness | runtime_execution | artifact_sha256 |
|---|---|---|---|---|---|---|---|---|
| round-19/inspection.json | ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42 | 1 | 0xdeadbeef | 16 | inferred | unknown | not-performed | 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827 |
| round-21/inspection.json | ev_4810eda7b540fbf2d4265c0f9deb3886dc009945cb77276b980f5502112cfc85 | 1 | 0xdeadbeef | 16 | inferred | unknown | not-performed | d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 |
| round-22/inspection.json | ev_24fe0001213ec58a588d086e0fe55677d749f3eb6998afe6ee6095ff9dc4af4b | 2 | 0xaaaaaaaa,0xbbbbbbbb | 30,32 | inferred | unknown | not-performed | 94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2 |
| round-23/inspection.json | ev_296e7ed723c7356b1cfbeee5dadc11283e5efe74535d544114ebf3b692f77201 | 0 | - | - | inferred | unknown | not-performed | 8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a |
| round-24/inspection.json | ev_50d5ffb1fdbd17c4896409ca4cc8b20d7ed344ef4011029bea4aa474b7f0ab9e | 0 | - | - | inferred | unknown | not-performed | b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93 |
| round-25/inspection.json | ev_23a9464bf2d8c3de3614176efa53016f002ddade19f1ae842b4325ba2d095579 | 0 | - | - | inferred | unknown | not-performed | 2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7 |
| round-26/inspection.json | ev_482e41e68b6c5f358fe660bc70eaf55f69c7b487fd61774e1a443571aecec090 | 0 | - | - | inferred | unknown | not-performed | ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d |

**TABLE 2 cross-checks**

| file | raw_functions | functions | raw_eq_norm | subject_eq_artifact | confidence | artifact_encoding | artifact_bytes | bytecode_bytes | local_path_exists |
|---|---|---|---|---|---|---|---|---|---|
| round-19/inspection.json | 1 | 1 | yes | yes | inferred | hex | 39 | 18 | yes |
| round-21/inspection.json | 1 | 1 | yes | yes | inferred | raw | 18 | 18 | yes |
| round-22/inspection.json | 2 | 2 | yes | yes | inferred | raw | 34 | 34 | yes |
| round-23/inspection.json | 0 | 0 | yes | yes | inferred | raw | 7 | 7 | yes |
| round-24/inspection.json | 0 | 0 | yes | yes | inferred | raw | 35 | 35 | yes |
| round-25/inspection.json | 0 | 0 | yes | yes | inferred | raw | 19 | 19 | yes |
| round-26/inspection.json | 0 | 0 | yes | yes | inferred | raw | 19 | 19 | yes |

**TABLE 3 fixtures vs records (truth-derived expectation; JUMPDEST byte check)**

| fixture | carrier | carrier_bytes | carrier_sha256 | truth_sha_len_ok | decoded_bytes | decoded_sha256 | destination_byte | expected_pairs | record_by_round | record_by_digest | saved_pairs | saved_eq_expected |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| evm-r19 | fixture.hex | 39 | 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827 | yes | 18 | d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 | 16:5b | deadbeef@16 | round-19/inspection.json | round-19/inspection.json | deadbeef@16 | yes |
| evm-r21 | fixture.raw | 18 | d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 | yes | 18 | d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 | 16:5b | deadbeef@16 | round-21/inspection.json | round-21/inspection.json | deadbeef@16 | yes |
| evm-r22 | fixture.raw | 34 | 94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2 | yes | 34 | 94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2 | 30:5b 32:5b | aaaaaaaa@30,bbbbbbbb@32 | round-22/inspection.json | round-22/inspection.json | aaaaaaaa@30,bbbbbbbb@32 | yes |
| evm-r23 | fixture.raw | 7 | 8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a | yes | 7 | 8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a | - | - | round-23/inspection.json | round-23/inspection.json | - | yes |
| evm-r24 | fixture.raw | 35 | b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93 | yes | 35 | b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93 | - | - | round-24/inspection.json | round-24/inspection.json | - | yes |
| evm-r25 | fixture.raw | 19 | 2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7 | yes | 19 | 2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7 | 16:00 | - | round-25/inspection.json | round-25/inspection.json | - | yes |
| evm-r26 | fixture.raw | 19 | ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d | yes | 19 | ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d | 17:5b | deadbeef@17 | round-26/inspection.json | round-26/inspection.json | - | NO |

fixture_rounds=19,21,22,23,24,25,26 record_rounds=19,21,22,23,24,25,26
fixtures_without_records=none
records_without_fixtures=none
saved_vs_expected_mismatch=evm-r26
non_toplevel_mentions_of_inspect_evm_or_evmole=none

## Findings (observations unless tagged)

- F1 coverage: records r19, r21–r26 match fixtures evm-r19, evm-r21–evm-r26 by round token and by carrier+bytecode digest (TABLE 3). round-20 has no record or fixture; its ledger only re-checks ev_0ad0097e (`corpus/live/runs/round-20/LEDGER.md:10`). Orphans: none either way.
- F2 sibling bytes: each record's `subject.local_path` (`/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/evm-rNN/fixture.*`) exists; `sha256sum` equals the lane copy for 7/7 (read-only).
- F3 parity: raw == normalized candidates 7/7; subject digest == artifact digest 7/7; all records inferred / unknown / not-performed. Evidence IDs cited in ledgers and reviewers match the census for r19 and r21–r26.
- F4 saved vs truth: 6/7 agree. evm-r26 mismatch: truth-derived `deadbeef@17` (byte 17 = 0x5b, `corpus/fixtures/evm-r26/truth.json:9`) vs 0 saved candidates (`corpus/live/runs/round-26/inspection.json:1`). Layout is a leading 00 plus r19 bytes with PUSH1 operand 0x10→0x11 (`round-26/reviewer.md:8-9`). The reviewer records the empty result without attributing a cause (`round-26/reviewer.md:14`).
- F5 first C09 falsifier: "PUSH4 selector + valid JUMPDEST destination ⇒ candidate" fails on evmole@0.9.3. r19 (dest 16) gives 1 candidate; r26 (dest 17) gives 0. Entry wording must scope candidates to the observed r19/r21/r22 layouts.
- F5b [INFERENCE] the leading entry STOP (present in r25 and r26, absent in r19) is the only tested variable co-occurring with zero output; no fixture isolates it, so cause is unattributed.
- F6 r22: two PUSH4 selectors with JUMPDEST at 30 and 32 are both reported (exact match). r25: destination byte 16 = 0x00 (STOP), 0 candidates, consistent with `evm-r25/truth.json:10` (jump_target_valid=false).
- F7 verifier coverage: `corpus/verify_evm_evidence.py:10-11` hard-codes r19. A grep of `corpus/*.py` for `evm-r|inspect_evm_interface|round-2[0-9]` finds no reader of r21–r26 EVM records; 6 of 7 records are checked only by reviewers' hand hashes.
- F8 scope: 104 JSON, 0 parse errors, 46 without `operation`. A grep of the copied `live/runs` for `inspect_evm_interface|evmole` (all file types) hits only the 7 inspection.json files, md ledgers/reviewers, and round-27 route-sentinel.md. Not executed: verify_evm_evidence.py (static reads only).

VERDICT: census complete and orphan-free (7 records ↔ 7 fixtures); one saved-vs-truth mismatch (evm-r26) is the first C09 falsifier candidate; six of seven records have no lane verifier.
Installs: none (python 3.14.8, sha256sum, diff, cp already present; no git/jj on the lane). Writes: this report, plus scratch copy `/tmp/revenger-r61-ExecEvmSavedRecordCensus-10/corpus`. Not a writer: no patch.
