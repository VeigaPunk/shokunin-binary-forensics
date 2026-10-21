GRADE: HOLDS — corpus/knowledge/round-62-evm-dispatch-byte-evidence.md @ d97761952be256d145d298022de03091de91d358 (r25/r26 bytes, operand 16/17, target byte + JUMPDEST membership, saved empty pair lists)

Frozen revision d97761952be256d145d298022de03091de91d358 (tree 45c4c5da82aae8ca2e44f6e3ed874a33533f54b9); claim base
5bd4a90fc1a34caa94496601b60537b3aab12301; pre-registration a3498e25ad87bf756288812d0ea7c474b09433c7. Attacked file
SHA-256 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e (frozen == worktree); archive manifest SHA-256
308c742d0efcd7e74329dcff80eba4a37d3f4c9e1da78033c87f81d994112433. Scratch /fast/scratch/hyaku/revenger-r62/R62FEvmR25R26/
(TMPDIR=…/tmp), removed after. No installs; no bytecode, chain, RPC or producer call.
## Observation (primary, reproduced)
1. The entry's own `## Reproduce` block, extracted to `readout.py` and run on the archived tree at the frozen revision
   (`git -C … archive d9776195… | tar -x -C arc`; `python3 -B readout.py arc`), exits 0, stderr empty. Reproduced stdout is
   **byte-identical** to the entry's `## Provenance` stdout: `entry_block_sha == repro_sha ==
   8b944bb84cdbdec25646e9d5ab7ccf62c87d7c8aa8da3f3b3d488f80d337f5e0`, 8 lines. The Provenance block is untruncated (no `…` in
   lines 442-448; widths 1970-2459 chars).
2. Independent derivation of r25/r26 (my own scanner, written from the fixture bytes, not the entry's code):
   r25 `corpus/fixtures/evm-r25/fixture.raw` = 19 bytes, sha256 2d87a4e2…f5e8f7, hex `0060003560e01c63deadbeef14601057005b00`;
   JUMPI@15, preceding PUSH1@13 immediate 0x10 -> operand **16**; JUMPDEST set **[17]**; byte at 16 = 0x00 (not 0x5b); membership
   16∈[17] = **false**; saved normalized functions [] and saved raw functions [].
   r26 `corpus/fixtures/evm-r26/fixture.raw` = 19 bytes, sha256 ebe2d675…8e97d, hex `0060003560e01c63deadbeef14601157005b00`;
   JUMPI@15, preceding PUSH1@13 immediate 0x11 -> operand **17**; JUMPDEST set **[17]**; byte at 17 = 0x5b on an instruction
   boundary; membership 17∈[17] = **true**; saved normalized functions [] and saved raw functions [].
   A verbatim port of S028's `get_valid_jump_destinations` (PUSH1<=op<=PUSH32 skip) returns [17] for both, matching the
   entry's `valid_jumpdest_offsets` — the set is not an artifact of the entry's walker.
3. Entry lines 114-119 and inventory rows 277-282 match the reproduced stdout exactly: `r25.jumpi_with_preceding_push1` [[15,16,false]],
   `r25.valid_jumpdest_offsets` [17], `r25.candidate_pairs_normalized` [], `r26.jumpi_with_preceding_push1` [[15,17,true]],
   `r26.valid_jumpdest_offsets` [17], `r26.candidate_pairs_normalized` [].
4. All 67 rows of the entry's `## Evidence inventory` were resolved programmatically against the reproduced stdout object graph
   (case.field -> value): **0 mismatches**. No row points at a field absent from the output.
5. S028 verified against the pinned primary (read-only fetch): `…/v2.20.0/src/ethereum/forks/osaka/vm/runtime.py` sha256
   a2801c4169b806a9494707179a9df20170a37a1769596aac56013ddba509aef8, `instructions/__init__.py` sha256
   49dd6155c7560811a8f546ea9c5a29678e3a3da859216e2ee48cfacaa5b63724 — both match SOURCES.md S028. Quoted anchor lines exact:
   runtime.py:22 `def get_valid_jump_destinations(code: Bytes) -> Set[Uint]:`, :28 "The jump destination should have the
   `JUMPDEST` opcode (0x5B).", :29-30 "The jump destination shouldn't be part of the data corresponding to" / "`PUSH-N`
   opcodes.", :64 `push_data_size = current_opcode.value - Ops.PUSH1.value + 1`; instructions/__init__.py :55 EQ=0x14, :104
   STOP=0x00, :106 JUMPI=0x57, :109 JUMPDEST=0x5B, :118 POP=0x50, :121 PUSH0=0x5F, :122 PUSH1=0x60, :125 PUSH4=0x63, :153
   PUSH32=0x7F. Tag v2.20.0 resolves to commit 2004296f2ffcbcebcd00f41152d33e8dfda0922a as recorded. No rejected row cited.
## Inference (my reading, separate from the above)
- r25/r26 differ in exactly one byte (offset 14: 0x10 -> 0x11), moving the JUMPI operand from 16 (not a JUMPDEST) to 17 (a
  JUMPDEST), yet both saved records report an empty function list. The entry reports the byte facts and the emptiness and asserts
  no cause, so the divergence stays an open Unknown rather than being resolved.
- `jumpi_with_preceding_push1`'s third element is `operand in jd` over instruction-boundary 0x5b offsets, so Observation 7's "not in
  / in its JUMPDEST set" is set membership, not a claim that a jump is taken or succeeds.
## Checks that found no defect (named, so absence is not silent)
- Causal/reachability leap: none in my slice. Observation 7 and the Unknown bullet (entry:139-141) give emptiness and byte facts
  and assert no cause; grep for cause/reachable/valid-jump/proves wording finds only the entry's own disclaimers (entry:140, 196).
- Provider-method leap: none. The provider appears only as recorded fields (`provider_id` evmole-interface, `provider_version`
  evmole@0.9.3); dispatch/argument/mutability labels are "the provider's own recorded values, not interpreted here"
  (entry:148-150). Confirmed: those keys exist only inside r19/r21/r22 function objects; r25/r26 records contain no such fields,
  and the entry does not claim they do. Empty-list misread as absence: none — `discovery_completeness=unknown` is recorded per
  record and the absence reading refused (entry:141-145); confirmed for all seven records, which carry
  `discovery_completeness=unknown`, `runtime_execution=not-performed`, `evidence_kind=inferred`.
- Author-intent contamination: the entry never cites `corpus/fixtures/evm-r25/truth.json` or `evm-r26/truth.json` (grep count
  0). Those files independently record r25 `encoded_jump_operand:16`, `jumpdest_byte_offset:17`, `jump_target_valid:false` and
  r26 `jumpdest_offset:17`, `changed_offset:14` — so the entry's values coincide with author intent but are derived from the
  bytes; the intent files are not used as support (Q03/Q06 hold).
- Digest-scope leap: none. Independently recomputed: every subject/artifact/bytecode digest equals sha256 of the carrier or
  decoded bytes exactly; for r25/r26 carrier == decoded byte string, so subject == artifact == bytecode == 2d87a4e2… / ebe2d675…,
  each labelled with the byte string it covers.
- Q13 over-credit: none. `corpus/verify_evm_evidence.py` is named only to state it is NOT a guard, every clause listed as
  unguarded (entry:158-166); the `## Reproduce` block is explicitly "not claimed to be deletion-sensitive".
- Frozen-state consistency: `git diff --stat a3498e25… d9776195… -- corpus/fixtures corpus/live` is empty, so the r25/r26
  fixtures and saved records are byte-identical between the Provenance lane base and the attacked revision.
## Unknown / residual risk
- The entry states the r25/r26 emptiness without proposing a cause; whether the provider's empty list for r25 (operand 16, not a
  JUMPDEST) and r26 (operand 17, a JUMPDEST) reflects provider-internal selection remains unknown and is not answerable from these
  seven files. The entry says so; I did not resolve it and made no provider call.
- The 67-row inventory names fewer fields than the readout prints per case (r25/r26 `carrier`, `decoded`, `record`, `recorded.*`,
  `instructions`, `pattern.*`, `raw_0x63_offsets`, `raw_0x5b_offsets`, `candidate_pairs_raw` have no row). Not a defect: Q11 requires
  every value the entry *asserts* to carry a derivation, not that every printed field be inventoried. The r25/r26 prose asserts
  only the three fields it names, and each is present and correct.
- The inference bullet (entry:123-131) says the reported offset "coincides with the operand of the PUSH1 that precedes a JUMPI"
  for r19/r21/r22. Independently confirmed: r19/r21 offset 16 = operand 0x10 = 0x5b on an instruction boundary; r22 offsets 30
  and 32 = operands 0x1e and 0x20, both 0x5b on instruction boundaries. It is scoped to non-empty results and explicitly
  disclaims being a definition, so no rule is fitted to the empty cases (Q07 intact).
## VERDICT
HOLDS for the assigned slice (r25/r26 bytes, operand 16/17, target byte and JUMPDEST membership, saved empty pair lists) and for
the entry on the criteria exercised: no Q11 failure (every asserted value in my slice carries an in-entry derivation plus printed
output; 67/67 inventory rows resolve exactly against reproduced stdout), no causal, reachability or provider-method leap, no
Q03/Q06 intent substitution, no Q07 fitted rule, no Q09 digest over-claim, no Q13 verifier over-credit. Independently derived bytes
agree with the entry for every field attacked. No material finding to message L1; no repair proposed; no admission asserted by me.
Installs: none (no package, tool or binary installed or updated in this seat).
