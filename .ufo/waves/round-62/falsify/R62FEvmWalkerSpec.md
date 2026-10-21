GRADE: HOLDS — corpus/knowledge/round-62-evm-dispatch-byte-evidence.md (C09 candidate, walker-vs-S028 slice)
Frozen revision d97761952be256d145d298022de03091de91d358 (rev-parse confirmed); entry blob 3e58a91fa8aee579aff7f873ce55061ae8f92cdf, sha256 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e; claimbase 5bd4a90fc1a34caa94496601b60537b3aab12301; prereg a3498e25ad87bf756288812d0ea7c474b09433c7. Candidate admission-status untouched; no repair made.

## Observation (primary evidence)

1. S028 re-opened read-only 2026-10-21 at tag v2.20.0 (commit 2004296f2ffcbcebcd00f41152d33e8dfda0922a):
   runtime.py sha256 a2801c4169b806a9494707179a9df20170a37a1769596aac56013ddba509aef8 (69 lines);
   instructions/__init__.py sha256 49dd6155c7560811a8f546ea9c5a29678e3a3da859216e2ee48cfacaa5b63724.
   Every recorded anchor matches exactly: runtime.py:22 def line, :28 "`JUMPDEST` opcode (0x5B)", :29-30
   "The jump destination shouldn't be part of the data corresponding to / `PUSH-N` opcodes.", :64
   `push_data_size = current_opcode.value - Ops.PUSH1.value + 1`, function spans 22-69 (file end);
   constants at :55 EQ=0x14, :104 STOP=0x00, :106 JUMPI=0x57, :109 JUMPDEST=0x5B, :118 POP=0x50,
   :121 PUSH0=0x5F, :122 PUSH1=0x60, :125 PUSH4=0x63, :153 PUSH32=0x7F. Reproduce comment
   "runtime.py:22-69 get_valid_jump_destinations" is exact.
2. Differential (entry's own walk() extracted byte-faithfully from the frozen Reproduce block, 7137
   bytes, vs faithful transcription of runtime.py:48-69 control flow incl. Ops-definedness):
   `TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FEvmWalkerSpec/tmp python3 -B checker.py`, cwd=/ →
   "TOTAL 39 checks, 0 failed". Jumpdest sets walk==S028 on all seven bytearrays: r19 [16], r21 [16],
   r22 [30,32], r23 [], r24 [], r25 [17], r26 [17]; visited opcode-read offsets identical on all seven.
3. PUSH0: entry `n = op - 0x5F if P1 <= op <= P32 else 0` puts 0x5F in the else branch (no immediate,
   no skip); S028's guard `Ops.PUSH1.value <= current_opcode.value` likewise excludes 0x5F. Synthetic
   differential: 5f5b→[1], 5b5f5b→[0,2], 5f→[] — equal on both. No fixture contains a 0x5f byte
   (checker: r19..r26 0x5f-byte-present=False), so fixture-exercise is nil and equivalence is
   by-construction plus synthetic — no entry claim depends on a fixture PUSH0 case.
4. Immediate widths: n = op-0x5F ≡ op-PUSH1+1 (runtime.py:64) for 0x60..0x7F; PUSH32 battery
   7f+(5b×32)+5b→[33] equal on both. Truncation: no fixture ends mid-immediate (all seven
   "last insn end==len" PASS; lengths 18,18,34,7,35,19,19); truncated-edge battery 60→[],
   7f5b→[], 635b5b5b5b→[], 615b5b5b→[3] equal on both (slice-clamp vs pc-overflow agree).
5. Provenance regeneration on the frozen archive: entry readout.py exit 0, stderr empty, and
   "actual stdout == Provenance fence (exact)" (15555 chars). Independent recomputation (separate
   walker, digest, raw-offset, jumpi, pattern derivations) equals both stdout and the Evidence
   inventory walker-scope rows, including r24 pattern occurrence 1, starts [1], span [1,9],
   PUSH1 opcode 7 / operand 8 / value 16, target offset 16 byte 0x00 not raw 0x5b.
6. Syntax vs reachability/execution — distinguished. valid_jumpdest_offsets is the S028 syntactic
   boundary scan; raw_0x63_offsets/raw_0x5b_offsets are kept as separate raw byte facts (r24: raw
   0x63 [1] yields no instruction, no jumpdest). jumpi_with_preceding_push1 asserts only membership
   "in the JUMPDEST set", never reachability; records carry runtime_execution=not-performed; the
   entry states "it is not a claim that the field *is* a jump destination in general", proposes no
   rule for empty pair lists, and claims no execution. Saved-record mapping verified: normalized
   bytecode_offset / raw bytecodeOffset pairs match all seven inspection.json files.
7. Scope: CASES selects exactly evm-r19 fixture.hex + evm-r21..r26 fixture.raw; no evm-r20 fixture
   exists; run dirs round-19, round-21..26 all carry inspection.json; r21 carrier bytes == r19
   decoded bytes (digest_scopes claim grounded).

Non-finding (recorded): S028 runtime.py:49-55 wraps `Ops(code[pc])` in try/except ValueError —
"Skip invalid opcodes, as they don't affect the jumpdest" — which the entry's Source facts do not
quote. The entry's walker labels every non-push byte as an instruction tuple where S028 skips
undefined opcodes before enum lookup; jumpdest sets are unaffected either way (synthetic e05b→[1]
equal; no undefined-opcode byte occurs at an instruction boundary in the seven). The entry claims
S028 as recorded authority for opcode bytes and the PUSH-skip rule, not enumeration identity — no
entry clause is contradicted. Minor latent quirk noted, in-scope correct: pattern.index(0x60) picks
the first 0x60 byte of the pattern; on these bytes that is the PUSH1 opcode (index 6), and all
derived values verify.

## Inference

The manual walker is semantically equivalent to the S028 osaka wholecode PUSH-skip definition for
jumpdest-set purposes on all seven selected bytearrays, and by construction on PUSH0, immediate
width 1..32, and truncated-immediate edges (synthetically demonstrated). All walker-scoped factual
values in prose and inventory trace to in-entry derivation and regenerate exactly from the frozen
archive. Valid-jumpdest syntax is consistently kept apart from raw byte presence, reachability, and
execution; no entry claim conflates them.

## Unknown

Whether any fixture exercises PUSH0 or a truncated trailing immediate: none does (no 0x5f byte in
any of the seven; no mid-immediate EOF); equivalence there rests on construction plus my synthetic
battery, not fixture bytes. No entry claim relies on such a fixture case.

Failed checks: none. No concrete mismatch found on the assigned slice; no Q clause failure to cite.

VERDICT: HOLDS. Installs: none. Scratch: /fast/scratch/hyaku/revenger-r62/R62FEvmWalkerSpec/
(checker.py, readout.py extracted, spec/ re-open copies, archive/ of d977619…; tmp under its tmp/).
