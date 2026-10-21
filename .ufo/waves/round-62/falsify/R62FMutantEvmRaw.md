GRADE: HOLDS — r24 raw 0x5b versus instruction JUMPDEST readout, assigned mutation only

Frozen revision: d97761952be256d145d298022de03091de91d358 (actual `git rev-parse` output; extracted with `git archive` into own scratch).
Target: `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`
Candidate SHA-256: 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e
Claimbase/pre-registration (recorded): 5bd4a90fc1a34caa94496601b60537b3aab12301 / a3498e25ad87bf756288812d0ea7c474b09433c7.
Axes: raw-byte sensitivity; instruction-boundary invariance; exact restoration; scoped Q11 derivation.
Scratch prefix S: `/fast/scratch/hyaku/revenger-r62/R62FMutantEvmRaw`.

## Mutant and expected detector
One mutation only: replace the zero byte at decimal offset 16 with 0x5b in `S/archive/corpus/fixtures/evm-r24/fixture.raw`; length remains 35, changed offsets exactly [16]. This plants 0x5b inside PUSH32's immediate, without shifting bytes or changing the dispatch-like pattern.
Expected: printed raw offsets [] → [16] → []; printed instruction JUMPDEST offsets remain [] throughout. Instruction offsets [0,33,34] and opcode counts must remain unchanged. The embedded target byte at 16 must change 0 → 91 → 0, with its raw-0x5b flag false → true → false.
Detector: identical in-entry readout and fixed selected-field comparison with the recorded pristine output, run pristine/mutant/restored; not a deletion-sensitive or automatic admission guard.

## Primary command and actual output
Command, cwd `/`, Python 3.14.8:
`/usr/bin/env TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FMutantEvmRaw/tmp /usr/bin/python3 -B /fast/scratch/hyaku/revenger-r62/R62FMutantEvmRaw/probe.py`
Harness exit 0. Its three child commands were identically `/usr/bin/python3 -B S/readout.py S/archive` (S expanded to the absolute prefix above); each readout exit was 0 and stderr was empty.
Exact stage-result stdout lines:
```json
{"changed_fields":[],"comparison":"PASS","complete_stdout_equal_recorded":true,"printed":{"candidate_pairs_normalized":[],"decoded_bytes":35,"fixture_sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93","instruction_offsets":[0,33,34],"instruction_opcode_counts":{"0x0":1,"0x50":1,"0x7f":1},"pattern_inclusive_spans":[[1,9]],"pattern_occurrence_count":1,"raw_0x5b_offsets":[],"target_byte":0,"target_is_raw_0x5b":false,"valid_jumpdest_offsets":[]},"readout_exit":0,"stage":"pristine","stderr":""}
{"changed_fields":["fixture_sha256","raw_0x5b_offsets","target_byte","target_is_raw_0x5b"],"comparison":"MISMATCH","complete_stdout_equal_recorded":false,"printed":{"candidate_pairs_normalized":[],"decoded_bytes":35,"fixture_sha256":"caf50f6a5daa0b22b8599393c69e018955d13039a801ecbf89a061e64cf1bc7d","instruction_offsets":[0,33,34],"instruction_opcode_counts":{"0x0":1,"0x50":1,"0x7f":1},"pattern_inclusive_spans":[[1,9]],"pattern_occurrence_count":1,"raw_0x5b_offsets":[16],"target_byte":91,"target_is_raw_0x5b":true,"valid_jumpdest_offsets":[]},"readout_exit":0,"stage":"mutant","stderr":""}
{"changed_fields":[],"comparison":"PASS","complete_stdout_equal_recorded":true,"printed":{"candidate_pairs_normalized":[],"decoded_bytes":35,"fixture_sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93","instruction_offsets":[0,33,34],"instruction_opcode_counts":{"0x0":1,"0x50":1,"0x7f":1},"pattern_inclusive_spans":[[1,9]],"pattern_occurrence_count":1,"raw_0x5b_offsets":[],"target_byte":0,"target_is_raw_0x5b":false,"valid_jumpdest_offsets":[]},"readout_exit":0,"stage":"restored","stderr":""}
{"baseline_ok":true,"probe_verdict":"KILLED","raw_vs_boundary_distinction_holds":true,"readout_stdout_pristine_restored_equal":true}
```
Full readout stdout retained as `S/{pristine,mutant,restored}.stdout.jsonl`; corresponding `.stderr` files are empty. Only the assigned three-state probe ran; no bytecode/fixture-JS execution, producer, RPC, build, lint or formatter.

## Observation — semantic Q11 audit, not output equality alone
Primary target lines 315–323 derive instruction boundaries from actual code bytes: n = op − 0x5f for PUSH-N, then advance by 1+n. The first actual byte is 0x7f, so n=32, immediate offsets are 1–32, and the next instruction is at 33, then 34. Offset 16 is data in both states.
Target lines 372–373 derive JUMPDEST offsets only from walked instruction tuples; lines 408–409 separately enumerate every raw byte. The tested outputs therefore have distinct in-entry derivations, not merely correctly printed constants. Target line 446 prints the pristine instruction tuples, raw offsets and empty JUMPDEST set.
Target lines 351–357 read the embedded operand and target byte from code; line 446 prints operand/target offset 16, target byte 0 and false raw-0x5b status. The mutant's 91/true output follows that actual byte change, not a new instruction boundary.
The reproduced block was byte-for-byte identical to target lines 292–422; SHA-256: 740f321e97e28d7f11b4a58e106f054447a284519c59487398752bc87cd37eeb.

## Inference
The manual comparison killed this single input-drift mutant while preserving the raw-byte/instruction distinction. No Q06/Q11 contradiction was found for the assigned fields. This does not prove every entry value has a derivation, and does not replace the full independent Q01–Q13 audit.

## Unknown and guard boundary
No deletion mutant was assigned or run. Automatic rejection, deletion sensitivity, provider behavior and general EVM behavior are untested. Target lines 163–170 explicitly credit no verifier as a guard; all readout runs returning 0 is consistent with that limitation, not evidence of a hidden guard. No admission or coverage flip is recommended by this probe.

## Restoration evidence
Fixture SHA-256 before: b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93
Fixture SHA-256 mutant: caf50f6a5daa0b22b8599393c69e018955d13039a801ecbf89a061e64cf1bc7d
Fixture SHA-256 restored: b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93
The harness restored in `finally` and reported `exact_bytes_equal:true`, `candidate_exact_bytes_unchanged:true`, `record_exact_bytes_unchanged:true`; pristine and restored complete stdout were identical.
Saved r24 record SHA-256 before/after: ec9e147db2b042f4d991816fa2a02fe95373de31956730fd1eb4cce5763742cd. Candidate bytes remained equal to their pre-probe snapshot and hash above.
Retained scratch: exact before and mutant fixture snapshots, the exact readout, one-shot probe, and three stdout/stderr captures. No live fixture or saved record was edited.

VERDICT: HOLDS for this assigned raw-versus-instruction mutation; mutant KILLED by the bounded manual comparison, exact restoration demonstrated; no failed Q identified within this scope.
Installs/updates: none.
