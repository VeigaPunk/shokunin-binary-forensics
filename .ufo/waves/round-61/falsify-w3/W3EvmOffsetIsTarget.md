GRADE: HOLDS — C09 Inference 1 "bytecode_offset equals the JUMPI target, a valid JUMPDEST, not the PUSH4 site" (evm-saved-interface-candidates.md:49-52)

Seat RevengerR61-2.W3EvmOffsetIsTarget. Archive of ab580698212258a55e43e9bb9bf6ac78c91eae2a (rev-parse confirmed) in /tmp/revenger-r61w3-W3EvmOffsetIsTarget; no bytecode executed, no REA call, no RPC.

## Observed byte walk (my own disassembler over the fixtures, PUSH-N immediates skipped)
- r19/r21 (identical bytes `60003560e01c63deadbeef14601057005b00`): PUSH4@6, EQ@11, PUSH1 `10`@12 (operand byte at 13), JUMPI@14, STOP@15, JUMPDEST@16, STOP@17. Saved: `0xdeadbeef`@16.
- r22: PUSH4@7, PUSH1 `1e`@13 (operand byte 14), JUMPI@15; PUSH4@17, PUSH1 `20`@23 (operand byte 24), JUMPI@25; STOP×4 @26-29; JUMPDEST@30, STOP@31, JUMPDEST@32. Saved: `0xaaaaaaaa`@30, `0xbbbbbbbb`@32.
- Saved records hold only selector, bytecode_offset, dispatch, inferred_arguments and inferred_state_mutability per function (normalized_result keys: artifact, bytecode, diagnostics, discovery_completeness, evidence_kind, functions, limitations, runtime_execution). No block or PUSH-site field.

## Alternative readings tested against the three records
| reading | r19/r21 | r22 | fits? |
|---|---|---|---|
| PUSH1 operand byte location | 13 | 14, 24 | no |
| JUMPDEST+1 (first body opcode) | 17 | 31, 33 | no |
| JUMPI pc + 2 | 16 | 17, 27 | no (r22 rules it out) |
| PUSH4 site + 10 | 16 | 17, 27 | no (r22 rules it out) |
| JUMPI destination value (PUSH1 immediate) | 16 | 30, 32 | yes |
| JUMPDEST position / basic-block start | 16 | 30, 32 | yes, same byte |
| k-th JUMPDEST paired with k-th selector | 16 | 30, 32 | yes |
- Only r22 rules out the arithmetic readings. r19 and r21 are one byte string, so the evidence is two distinct inputs and three (selector, offset) pairs. The entry already says so at `:80-81`.
- The three readings that fit all give the same numbers, because every reported destination was authored to be a JUMPDEST. No record reports a candidate whose destination is a non-JUMPDEST. r25 has such a destination (16 is a STOP), but it reports nothing and also starts with STOP, so it cannot separate "destination value" from "valid JUMPDEST". The entry leaves r25's cause unknown at `:64-67`.

## Upstream counterexample attempt (attack evidence only; not a SOURCES row, so not usable as support under Q01)
- evmole tag 0.9.3 `src/contract_info.rs:44` (https://raw.githubusercontent.com/cdump/evmole/0.9.3/src/contract_info.rs, accessed 2026-10-21): "The starting byte offset within the EVM bytecode for the function body". This is the block-start reading and agrees with the entry.
- `src/selectors/mod.rs:82-88` (same tag, accessed 2026-10-21) inserts `selectors.insert(selector, pc)` where `pc` comes from JUMPI arg `fa`. In `src/evm/vm.rs:173-183`, the not-taken branch sets `args[0]` to the destination if it is "< self.code.len()". The JUMPDEST check is at `vm.rs:195`, on the taken branch only.
- [INFERENCE] So upstream records the destination value, and "a valid JUMPDEST" is a fact about these authored fixtures, not a condition the provider is shown to enforce. This does not contradict the entry. The Inference only claims equality on three records. `:12-13` rules out claims about "the provider's internal method", and `:51-52` limits the observation to "three more authored records only". Nothing in the entry says only valid JUMPDESTs are reported.
- "not the PUSH4 site" holds: 6≠16, 7≠30, 17≠32, and no record field holds 6, 7 or 17.

## Kaidoku prior art (Q10)
- The cited lines exist and say the same thing. `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-evm-interface.md:151-152`: "`bytecodeOffset` records the **JUMPDEST dispatch-target position**, not the PUSH4 comparison site" (`:153` continues with offsets 62/68/74). The file was last changed by kaidoku commit 999ce123 (2026-10-13), so the line numbers were stable when revenger landed (0b6ddf0, 2026-10-21 13:04).
- `kaidoku-shokunin/PROVINCE.md:54` is the "EVM interface" row and names "bundled EVMole 0.9.3/WASM", the same provider version. It is cited only as the EVM row, which is accurate. PROVINCE.md last changed in fe18f13 (12:58), before the landing.
- Cited as prior art, not re-claimed: the entry says "cited here as prior art, not re-claimed" (`:96`), "Kaidoku holds the same reading for its own records" (`:50-51`), and makes negative/decoy fixtures its own ground (`:97`). This matches Amendment A2 (`reports/round-61/claims.md:112-117`). No re-claim found.

## Non-blocking precision note (not a defect)
- `:49-50`: "the JUMPI target, a valid JUMPDEST" could be read as a selection rule. The records cannot separate it from "JUMPI destination value, whatever byte it names". If the owner wants it tighter, the smallest safe change is to add after the sentence: "(every reported target was authored as a JUMPDEST; no record separates destination value from JUMPDEST validity)". Nothing is overstated without this change.
- Out of scope, one line: upstream `vm.rs:710-712` (STOP sets `stopped`) plus the `selectors/mod.rs:242` loop is consistent with the entry's "reachable from pc 0" rule for r25/r26. The entry keeps that cause Unknown, which is correct under Q07 because reading source code is not an independent reproduction.

## Impacted axes
coverage: none. The entry's admission under Q03, Q07 and Q10 is not voided for this item.

VERDICT: HOLDS. Every fitting alternative (destination value, block start, ordinal JUMPDEST pairing) gives the same offsets and none contradicts the stated equality. The non-fitting readings (operand byte, JUMPDEST+1, PUSH4/JUMPI arithmetic) are ruled out by r22. Kaidoku 151-153 is cited as prior art, not re-claimed.
Installs: none. Scratch: /tmp/revenger-r61w3-W3EvmOffsetIsTarget{,-selmod.rs,-vm.rs}.
