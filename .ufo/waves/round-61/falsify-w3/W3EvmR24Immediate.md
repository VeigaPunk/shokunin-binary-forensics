GRADE: BROKEN — C09 Observation 3, r24 (byte and record facts HOLD; Q11 derivation fails on four r24 values)
Seat: RevengerR61-2.W3EvmR24Immediate · tree ab580698212258a55e43e9bb9bf6ac78c91eae2a extracted to /tmp/revenger-r61w3-W3EvmR24Immediate/landed · access 2026-10-21 · scope: r24 only

HOLDS (independently re-derived)
1. Bytes, corpus/fixtures/evm-r24/fixture.raw (35 B, sha256 b69834e0ef786e3c…): `7f 63 de ad be ef 14 60 10 57`, 23×`00`, `50 00`.
   Walk (PUSH-N skips immediates): PUSH32@0 with immediate 1–32; POP@33; STOP@34; exactly one PUSH32.
   Raw 0x63 offsets = [1]. Raw 0x5B count = 0. PUSH4 instructions = 0.
   The r19 9-byte pattern `63deadbeef14601057` occurs once, at 1 (span 1–9).
2. Record corpus/live/runs/round-24/inspection.json (sha256 ec9e147db2b042f4, = entry Provenance L155): raw_result.functions=[]; normalized functions=[]; evidence_kind inferred; discovery_completeness unknown; runtime_execution not-performed; subject.digest = fixture sha; normalized hex == fixture bytes; evidence_id ev_50d5ffb1…f0ab9e equals entry L167 and the S026 row. inspection.stderr = 0 bytes.
3. Reproduce block (entry L102–138) extracted and run `python3 -B` on the archive root: exit 0; stdout vs Provenance block (L140): 14/14 lines, zero diff.
4. Bytes unchanged: `git diff --stat cf02419 ab58069 -- corpus/fixtures/evm-r24 corpus/live/runs/round-24` and the same from e0a4b0c print nothing; both bases are ancestors of ab58069; last touch dd0d49f.
5. Rule source: S016 runtime.py line 29, quoted verbatim: "The jump destination shouldn't be part of the data corresponding to `PUSH-N` opcodes." (https://raw.githubusercontent.com/ethereum/execution-specs/v2.20.0/src/ethereum/forks/osaka/vm/runtime.py, tag v2.20.0, accessed 2026-10-21). instructions/__init__.py lines 55/106/109/125 = EQ 0x14, JUMPI 0x57, JUMPDEST 0x5B, PUSH4 0x63.
6. Downstream: lesson corpus/lessons/round-61.md:80 rejects "r24 shows the provider excludes PUSH immediate data" (Q07). No r24 overclaim found in claims.md, README, SCORECARD or other round-61 text (grep).
7. Simple-rule matrix on r24 (scratch rules_r24.py): PUSH-skipping walk + JUMPDEST → []; PUSH-skipping walk, no JUMPDEST → []; raw no-skip + raw 0x5B at target → []; raw no-skip, no JUMPDEST → [(1,16)]. r19 control: all four → [(6,16)]. Entry L60 "several simpler rules also yield an empty output" holds (3 of 4), but no rule is computed in-entry.

BROKEN — Q11 (QUALITY.md:23 reject clause: "a value is correct when re-derived but the entry carries no derivation")
 a. L32–33 "one PUSH32": a count; the block prints entry_op=0x7f only.
 b. L33 "its immediate contains the r19 pattern"; L88–90 "embedded_pattern_offsets [1, 9] … consistent with the bytes": the block never searches the 9-byte pattern. The only span derivation is `R24_SPAN [[1, 9]]` (reports/round-61/measure-after.log:88–89; LOG.md:806), a one-off whose producer is saved nowhere (absent from reports/round-61/measure.py and the archive).
 c. L60 "the file has no 0x5B byte": a count; the block's `jumpdest=[]` is the instruction-level set, not the raw count. Value true (count 0); derivation absent.
 d. L58–59 "embedded JUMPI target (0x10)": the block prints jumpi=[] for r24. Value true (byte 8 = 0x10, byte 16 = 0x00); not derived.
 Self-checks overstated: L182 Q06 "every fixture premise re-derived … by the block above"; L187 Q11 "every count, offset and digest carries the command above and its output".
 Minimal fix: print raw 0x5B offsets, the PUSH32 count, the 9-byte pattern span and the walk's JUMPI operand; or label those values "recorded, not re-derived".

PARTIAL — wording nit, not a break
 L57–58 states only the bare 0x63 fact. The matrix shows r24 also excludes one naive rule (raw 4-byte pattern, no PUSH skipping, no JUMPDEST check) that the entry does not mention. The "does not show … excludes PUSH data" sentence (L58) stays correct.

Implication for C1 (not graded here)
 claims.md:26–34 admits an entry only if Q01–Q11 all pass, so C09 fails as written. claims.md:38–39 predicts 5/14 if one entry admits. LOG.md:804 already records the attack-survival conjunct as unmet. C04 was not attacked by this seat.

Installs: none. Tools: git read-only (log, cat-file, merge-base, commit-to-commit diff); curl for the public raw.githubusercontent.com spec file; python3 stdlib. No REA producer calls, no fixture bytecode executed, no live-tree writes except this report.
Scratch: /tmp/revenger-r61w3-W3EvmR24Immediate/{repro_block.py, repro_out.txt, rules_r24.py, landed/}.

VERDICT: r24 bytes and saved record HOLD (0x63×1 at 1, 0x5B×0, no PUSH4, functions []), but Q11 fails for four r24 values (one PUSH32, pattern span, raw 0x5B count, embedded target 0x10) with no in-entry derivation, so Observation 3 is BROKEN as written.
