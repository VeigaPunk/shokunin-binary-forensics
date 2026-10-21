GRADE: PARTIAL — C09 Inference 3 (r24 PUSH-data confound), corpus/knowledge/evm-saved-interface-candidates.md:57-61

Seat RevengerR61-2.W3EvmR24Confound. Attacked tree: `git archive ab580698212258a55e43e9bb9bf6ac78c91eae2a` extracted to
/tmp/revenger-r61w3-W3EvmR24Confound (rev-parse confirmed). Scanner: /tmp/revenger-r61w3-W3EvmR24Confound-rules.py (stdlib, reads
fixtures + saved JSON only; no bytecode executed, no REA call, no chain).

## Bytes (observation)
- `xxd corpus/fixtures/evm-r24/fixture.raw` → `7f63 dead beef 1460 1057 0000 … 0050 00`, 35 bytes, sha256
  b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93 (= truth.json:2, = saved record bytecode.sha256).
- Embedded pattern `63deadbeef14601057` at offsets 1–9, inside the PUSH32 immediate (1–32). PUSH1 operand = 0x10 = 16.
- `d[16]=0x0`; byte counts in file: `5b 0`, `35 0`, `1c 0`. So the dest byte is not 0x5B (raw sense) and is inside PUSH data
  (PUSH-aware sense); the valid JUMPDEST set is empty. Both facts in entry:59-60 are CORRECT.
- Saved r24 record `functions=[]`, completeness unknown, runtime not-performed (entry Reproduce re-run, exit 0, r24 lines
  byte-identical to Provenance entry:154-155).

## Rule enumeration (command: `python3 -B /tmp/revenger-r61w3-W3EvmR24Confound-rules.py`, exit 0; E = empty)
| rule | excludes PUSH data? | r24 | fits all 7 saved outputs |
|---|---|---|---|
| A raw 0x63 byte anywhere | no | 1 | False |
| B raw PUSH4/EQ/PUSH1/JUMPI pattern, no dest check | no | 1 | False |
| C B + dest byte == 0x5B | no | E | False (r26) |
| D B + dest in PUSH-aware JUMPDEST set | partly (dest only) | E | False (r26) |
| E B gated on any 0x5B byte in file | no | E | False |
| F B + CALLDATALOAD(0x35)/SHR(0x1c) in 6 bytes before | no | E | False |
| G B, raw scan halts at first 0x00 byte | no | 1 | False (r19 E: byte 1 is PUSH1's 0x00) |
| H PUSH-aware walk pattern, no dest check | yes | E | False |
| I PUSH-aware walk + valid dest (entry's walk) | yes | E | False (r26) |
| J C + empty when entry byte is STOP | **no** | E | **True** (exact selectors/offsets) |
Five rules that never exclude PUSH data from the pattern match (C, E, F, J; D on the match) yield empty on r24.
Only the naive scanners A/B (and G) fire. Entry's "several simpler rules also yield an empty output" (entry:60-61): HOLDS.

## Findings
1. CORRECT: the conclusion "r24 does not show that the provider excludes PUSH data" (entry:58-59) holds; the r24
   negative refutes only naive byte-pattern promotion (rules A/B). Same finding as build seat
   `.ufo/waves/round-61/build/ExecEvmOracleR24.md:42,62`; lessons row `corpus/lessons/round-61.md:80` rejects the opposite
   claim consistently. No overstatement found in claims.md, README, lessons.
2. INCOMPLETE (PARTIAL, entry:59-61): the stated reasons omit a third, independent confound. r19 is
   `60003560e01c63deadbeef14601057005b00`; its PUSH1 0 / CALLDATALOAD / PUSH1 0xe0 / SHR prologue (offsets 0–5) is absent
   from r24 (zero 0x35, zero 0x1c bytes). Rule F (raw, PUSH data not excluded) is empty on r24 for that reason alone,
   even if the dest were a JUMPDEST. Relevance [INFERENCE]: evmole's README at tag 0.9.3 says "EVMole uses symbolic
   execution with a custom EVM implementation to trace how CALLDATA flows through the bytecode"
   (https://raw.githubusercontent.com/cdump/evmole/0.9.3/README.md, §How it works, accessed 2026-10-21) — a comparand not
   derived from CALLDATA would not be expected to qualify. Not observed for the provider; the entry rightly asserts no method.
3. WORDING (PARTIAL, entry:33): "one PUSH32 whose immediate contains the r19 pattern" overstates; it contains r19
   offsets 6–14 only (9 of 18 bytes), without r19's prologue or its `00 5b 00` tail. round-24 LEDGER.md:3 says it
   precisely ("the r19 dispatch-looking nine bytes").
4. STRONGER COUNTEREXAMPLE (not a defect of the stated sentence): rule J, which never excludes PUSH data, reproduces all
   seven saved outputs exactly. So no fixture in the set (not only r24) isolates PUSH-data exclusion. The entry does
   not claim otherwise; adding this one clause would close the gap.
5. Adjacent (outside item, flagged only): Unknown entry:64-65 "the scan stops at the first STOP" fits all seven outputs
   only under PUSH-aware decoding; a raw-byte reading (rule G) empties r19 at offset 1. Not graded here.

## Impacted axes
coverage/C1 admission: no Q criterion fails on this item (Q07 respected: no cause asserted; Q11 bytes re-derived). No
saved record or fixture changed (sha matches); no hold lost. Defects are completeness/wording only → PARTIAL, not BROKEN.

## Smallest safe correction
- entry:33 → "one PUSH32 whose immediate contains r19's nine dispatch bytes (r19 offsets 6–14), without its calldata prologue".
- entry:59-61 → "…is not a JUMPDEST, the file has no 0x5B byte, and the embedded bytes lack r19's CALLDATALOAD/SHR
  prologue, so several simpler rules also yield an empty output; a raw-byte rule (JUMPDEST byte at dest, entry not STOP)
  fits all seven outputs, so no fixture here isolates PUSH-data exclusion."

Installs: none. Scratch: /tmp/revenger-r61w3-W3EvmR24Confound{,-rules.py,-repro.py}.
VERDICT: Inference 3's confound statement is correct (bytes verified; 5 non-PUSH-aware rules empty on r24) but incomplete — it omits the missing calldata prologue and that a non-PUSH-aware rule fits all seven outputs; entry:33 "the r19 pattern" overstates.
