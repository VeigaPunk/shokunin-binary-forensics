GRADE: BROKEN — round-62 EVM dispatch byte evidence (C09)

Frozen revision: `d97761952be256d145d298022de03091de91d358`
Candidate SHA-256: `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`
Target: `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`
Severity: Medium; Q11 evidence/derivation blocker, not a runtime-execution vulnerability.

Exploit path: A reviewer can accept a raw byte-pattern lookup as an opcode-boundary observation. The candidate calls r24's offset 7 a “PUSH1 opcode byte,” but the same output's walk shows r24 is one PUSH32 instruction at offset 0; offset 7 is inside its immediate. Separately, an unvalidated two-byte header can be described as `0x` while the readout still decodes the bytes after it.

Observation:
- Archived readout imports only stdlib (`hashlib`, `json`, `sys`, `pathlib`); it reads the seven listed fixture and saved-record paths with `Path.read_bytes()`, parses record JSON, and prints. No subprocess, network, producer, provider, or target-code/bytecode execution path is present. All checked input files/directories were regular files/directories in the archive. `-B` was used.
- Exact run command: `TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FSafeEvm/tmp python3 -B /fast/scratch/hyaku/revenger-r62/R62FSafeEvm/readout.py /fast/scratch/hyaku/revenger-r62/R62FSafeEvm/archive`; exit `0`; stderr `0` bytes; stdout comparison to the archived Provenance block `cmp` exit `0`, 8 lines / 15556 bytes, SHA-256 `aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf` (expected and actual hashes identical).
- Exact summary JSON: `{"distinct_candidate_pairs":3,"distinct_pairs":[["0xaaaaaaaa",30],["0xbbbbbbbb",32],["0xdeadbeef",16]],"pattern_hex":"63deadbeef14601057","pattern_length":9,"raw_and_normalized_pair_counts_equal":true,"reported_candidate_observations":4,"total_cases":7}`.
- Q11 defect: candidate lines 54–60 call r19 a 39-byte `0x`-prefixed ASCII-hex file. Readout line 75 decodes `carrier[2:-1]` but never checks or prints `carrier[:2]` (or the removed final byte); output reports carrier length/hash and decoded bytes, not the carrier prefix. A wrong two-byte prefix would pass this code path. Thus the correct-looking prefix claim has no validated in-entry derivation/output; Q11 is not met.
- Further boundary overstatement: candidate lines 101–112 call r24 offset 7 a PUSH1 opcode byte. Readout lines 48–66 set that offset with `pattern.index(P1)` (raw byte search), not an r24 instruction-boundary check. Exact r24 output includes `"instruction_opcode_counts":{"0x0":1,"0x50":1,"0x7f":1}` and `"instructions":[[0,127,"63deadbeef146010570000000000000000000000000000000000000000000000"],[33,80,""],[34,0,""]]`; offset 7 is PUSH32 immediate data, not a PUSH1 instruction. The output's `"embedded_push1_opcode_offset":7` is only a template-byte offset.

Inference:
- The successful readout and full stdout match substantiate the printed values, but do not cure the missing prefix check or establish r24's offset 7 as an instruction boundary. These are Q11 failures despite correct byte values and output equality.
- No fixture/record, live corpus, gate, README, or candidate was modified; run/extraction artifacts are confined to the assigned scratch directory. The entry remains a candidate; this report makes no admission or coverage decision.

Unknown:
- No external source was reopened and no claim is made about provider behavior, deployment authenticity, or bytecode execution.

Smallest remediation: Check and print/record the exact r19 prefix (and encoding boundary) before decoding; describe r24 offset 7 as a raw `0x60` template byte inside PUSH32 data, or only call it an opcode if an instruction walk proves a boundary.

VERDICT: BROKEN — fail Q11; do not count C09 on this candidate as written.
Installs: none.