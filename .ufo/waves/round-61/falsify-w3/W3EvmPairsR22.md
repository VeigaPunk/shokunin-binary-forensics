GRADE: PARTIAL — C09 Observation 2 (r22), entry at landed ab580698 (hypothesis HOLDS; wording nit at line 28; rule-fit sentence at lines 65-66 contradicted under its literal reading)

METHOD (no REA calls; no bytecode executed; stdlib python3 only)
- Archive: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar ab580698212258a55e43e9bb9bf6ac78c91eae2a | tar -x -C /tmp/revenger-r61w3-W3EvmPairsR22` (commit 2026-10-21 13:32:21 -0300).
- Live == landed for the files named here (sha256 identical): entry ab9c48da…, r22 inspection.json c55f6972…, LEDGER.md 52803f4e…, reviewer.md bc4336fe…, truth.json 99aba01a…, fixture.raw 94c1790f… (34 B). Whole-tree equality was not checked.
- Read-only `git diff --stat e0a4b0c4… ab580698…` over fixtures evm-r19, evm-r21..26 and runs round-19, round-21..26: empty. The entry is the only changed file (+189). The base-run Provenance still matches landed bytes and records.
- Scripts: /tmp/revenger-r61w3-W3EvmPairsR22/walk_r22.py and rules.py (`python3 -B <file>`).

HYPOTHESIS: HOLDS (own walker, walk_r22.py)
- Hex 60003560e01c8063aaaaaaaa14601e578063bbbbbbbb14602057000000005b005b00.
- 0x63 at {7,17}: PUSH4 immediates aaaaaaaa@7 and bbbbbbbb@17.
- 0x5b at {30,32}: both instruction starts, outside PUSH data.
- JUMPI@15 is preceded by PUSH1 0x1e (target 30); JUMPI@25 by PUSH1 0x20 (target 32). Both targets are valid JUMPDESTs.
- Saved normalized_result.functions is exactly {0xaaaaaaaa,30} and {0xbbbbbbbb,32}; raw_result carries the same pairs without 0x. evidence_id ev_24fe0001213ec58a… equals entry line 165. subject.digest == fixture sha256.
- Chains: aaaaaaaa = PUSH4@7 → EQ@12 → PUSH1@13 → JUMPI@15 → 30. bbbbbbbb = PUSH4@17 → EQ@22 → PUSH1@23 → JUMPI@25 → 32. Entry lines 25-31 and provenance lines 150-151 recomputed equal.

NO THIRD CANDIDATE, NO UNDISCLOSED FIELD: HOLDS
- Naive byte search and PUSH-skipping decode agree: 0x63 {7,17}, 0x5b {30,32}, 0x57 {15,25}. No 0x63/0x5b/0x57 byte lies inside any PUSH immediate, so the r22 result does not depend on the S016 skip rule.
- Only two PUSH1-then-JUMPI sites exist. Rule variants A2 and B2 (DEFECT 2) each predict exactly two candidates.
- raw_result keys: `functions` only. Each function object has five keys: selector, bytecode_offset, dispatch ("abi"), inferred_arguments (""), inferred_state_mutability ("payable"). The last three are provider inferences, disclaimed at entry lines 75-76.
- "push4" (any case) is absent from the record, so entry lines 30-31 hold. inspection.stderr is empty. LEDGER.md and reviewer.md both state two candidates.

DEFECT 1 — wording, entry line 28 (PARTIAL)
- "In each case the offset is the PUSH1 operand of a JUMPI": the offset is the VALUE of the PUSH1 operand (byte 14 = 0x1e, byte 24 = 0x20), not the operand byte. Fix: "equals the value of the PUSH1 operand before that JUMPI".

DEFECT 2 — rule-fit sentence, entry lines 65-66 (Unknown section)
- Text: "Two post-hoc rules fit all seven outputs (only code reachable from pc 0 is considered; the scan stops at the first STOP)".
- rules.py over the seven fixtures against saved outputs:
  - A2 (reachable from pc 0, following static PUSH1→JUMP/JUMPI edges): fits all seven.
  - B2 (candidate sites stop at the first STOP; JUMPDEST validity checked over the whole code): fits all seven. No fixture separates A2 from B2.
  - Literal readings fail on r19, r21 and r22: A1 (fall-through reachability only); B1 (valid-destination scan stops at the first STOP, the entry's own term at lines 20-22); AB (both bounds together).
- Cause: the first STOP is pc 15 in r19, between JUMPI@14 and JUMPDEST@16 (saved deadbeef@16). It is pc 26 in r22, before JUMPDESTs 30 and 32 (saved both). Under B1 those JUMPDESTs are never seen, so B1 predicts [].
- The sentence therefore holds only under an unstated reading (B2 plus jump-edge reachability). Read literally, it is contradicted by saved r19/r21/r22, i.e. BROKEN as written. Fix: state that the STOP bound limits candidate sites only, and that JUMPDEST validity uses the whole code.
- r25 and r26 are [] under every rule (entry STOP at pc 0), so they do not discriminate between rules.

Installs: none (python3 stdlib only).
VERDICT: r22 facts HOLD (two candidates, PUSH4@7/17, JUMPDEST targets 30/32, no third candidate, no undisclosed field); entry is PARTIAL on line 28 wording and on the lines 65-66 rule-fit claim, which is contradicted by r19/r21/r22 under its literal reading.
