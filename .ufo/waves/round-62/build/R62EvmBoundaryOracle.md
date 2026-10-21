RESULT: COMPLETE

# R62EvmBoundaryOracle — independent EVM instruction walker (C09 candidate input)

Seat `RevengerR61-2.R62EvmBoundaryOracle`, executor, axis coverage. Scope: an independent instruction walker over the seven archived EVM fixtures, skipping PUSH data; full instructions, valid JUMPDEST sets, raw 0x63/0x5b offsets, PUSH32 count, r24 embedded span/target; cross-check authoring truth without trusting it as oracle. No production edit, no admission, no README change.

## Artifacts (scratch: `/fast/scratch/hyaku/revenger-r62/R62EvmBoundaryOracle/`)
- `evm_boundary_walker.py` sha256 `4c0efde3826b0cc3a54490e700274475b4d0b90d3d1c12aa35f700649a3a1538`; `evm_boundary_walker.stdout.txt` sha256 `59941324b1c82a7d91abd5a624af96f405b67ef55a15651f7c7eae99d0b5a45a` (450 lines); `evm_boundary_walker.json` sha256 `a91e48c01e3bb4b0f3e68f1fc32c074bede7afce072d19a68190846049f24902`.
- `evm_entry_derivation.py` sha256 `8ef8cd1c0f39f19f37e491b50797dfc0b55801944fc9f510698d83eab10d6736` (compact, embeddable in-entry code) + `evm_entry_derivation.stdout.txt` sha256 `446f26d35b07a93bc920eb63cf47f93dee1500910124838f95ccbf36f878afcf`; `proposed-entry-derivation.md` — proposed in-entry derivation block for `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` (scratch, not corpus).
- Frozen tree read: `git -C <repo> archive a3498e25ad87bf756288812d0ea7c474b09433c7` extracted to `tree/`; all execution ran with `cwd=/` on that copy. Command: `cd / && python3 -B .../evm_boundary_walker.py .../tree --json .../evm_boundary_walker.json`, exit 0. Stdlib only; file bytes only; no exec/eval, no chain/RPC, no provider call, no fixture JS. Re-run diff against the saved stdout: identical (deterministic).

## Walker-derived results (from that stdout; full per-fixture instruction tables with offset, opcode, name and immediate bytes are in it; PUSH immediates are data and are never walked)
| fixture | bytes | instr | exec PUSH4 | PUSH32 | valid JUMPDEST | raw 0x63 | raw 0x5b | JUMPI destination |
|---|---|---|---|---|---|---|---|---|
| evm-r19 | 18 | 11 | 1 | 0 | [16] | [6] | [16] | 16 (valid) |
| evm-r21 | 18 | 11 | 1 | 0 | [16] | [6] | [16] | 16 (valid) |
| evm-r22 | 34 | 22 | 2 | 0 | [30, 32] | [7, 17] | [30, 32] | 30, 32 (both valid) |
| evm-r23 | 7 | 3 | 1 | 0 | [] | [0] | [] | none |
| evm-r24 | 35 | 3 | 0 | 1 | [] | [1] | [] | none |
| evm-r25 | 19 | 12 | 1 | 0 | [17] | [7] | [17] | 16 (NOT valid: STOP) |
| evm-r26 | 19 | 12 | 1 | 0 | [17] | [7] | [17] | 17 (valid) |

evm-r24 embedded sequence `63deadbeef14601057`: occurrence count **1**, inclusive span **[1, 9]**; all nine bytes classified "PUSH data (not an opcode)", payload of the PUSH32 at offset 0. Embedded PUSH1 opcode at file offset 7, operand byte at offset 8 with value **16**; that operand byte is PUSH data, and 16 is **not** a valid JUMPDEST and not an instruction boundary (the byte there is 0x00, inside PUSH data). The same nine bytes are an instruction boundary in evm-r19 (offset 6), evm-r21 (6) and evm-r25 (7), and absent from evm-r22/evm-r23/evm-r26 (evm-r26 differs at the PUSH1 operand byte: 0x11). Byte presence alone therefore decides nothing. Independent diffs: evm-r19 decoded bytes are byte-identical to evm-r21 raw bytes; evm-r25 and evm-r26 differ at exactly one byte, offset 14, 0x10 -> 0x11.

## Cross-check against authoring truth (record, never oracle)
`truth.json` was read only after the walk; no branch of the walk consults it. Comparison rows **58, mismatches 0** (stdout section "comparison against co-located truth.json"). One row was a representation difference, not a value difference: the record stores `embedded_pattern_offsets: [1, 9]` (one inclusive span) while the walker first emitted `[[1, 9]]`; after normalizing to one flat span the row matches. This corroborates the round-61 correction (one occurrence, not two) and the recorded round-24 wording at `LOG.md:289` ("occur only inside immediate offsets 1–9"), which stays **recorded** prose here, not a re-derived value.

## Walker sensitivity (mutation self-tests, in-memory copies only)
- M1 evm-r25 copy, byte 17 `0x5b`->`0x00`: valid JUMPDEST set becomes `[]`, JUMPI destination 16 invalid.
- M2 evm-r24 copy, byte 0 `0x7f`->`0x63`: executable PUSH4 count becomes 1 while raw 0x63 offsets become `[0, 1]` — instruction count and raw-byte count move separately.
- M3 evm-r19 copy, byte 13 `0x10`->`0x11`: destination becomes 17, still not a JUMPDEST.
- M4 evm-r24 copy, byte 1 `0x63`->`0x00`: pattern occurrence count becomes 0.

## Preservation and scope
`git status --porcelain` prints only `?? .ufo/waves/round-62/` (sibling reports plus this file); `git diff -- corpus` is empty. Repo fixture digests equal the extracted frozen-tree digests for all seven fixtures. No corpus file, README row, source row, lesson or fixture byte was written; README C04/C09 stay uncovered; no admission, no held flip.

## Candidate input (Q11-shaped)
Derived here and quotable by the entry writer: per-fixture instruction counts, boundary and JUMPDEST sets, raw 0x63/0x5b offsets, executable PUSH4 and PUSH32 counts, JUMPI destination values with validity, the r24 pattern count/span/target classification, and the two pairwise diffs. Recorded (not re-derived): `LOG.md:289` wording, `truth.json` fields, saved REA candidate/digest fields. In-entry code plus captured output: `.../proposed-entry-derivation.md`.

## Risks / unknowns
- The walker is a linear scanner with a constant-propagation stack model (PUSH/DUP/POP/EQ modelled; unknown opcodes conservatively clear the abstract stack); it performs no control-flow execution, so destinations are reported only where a literal PUSH feeds the JUMPI in these seven fixtures.
- Opcode-table facts (0x60..0x7f PUSH1..PUSH32, 0x5b JUMPDEST, 0x56/0x57 JUMP/JUMPI) still require the round-opened tier-A spec row (reserved S028) that the entry writer must open and quote; I did not open it.
- No claim here about provider behaviour, chain state, callable-interface completeness, authenticity, or present producer capability.

Installs: none (no tool installed or updated).
