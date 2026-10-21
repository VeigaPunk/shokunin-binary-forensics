# ExecEvmOracleR26 — round 61 independent byte oracle, evm-r26 (RUNS, read-only)
Seat CloseChousa26.ExecEvmOracleR26-10 · 2026-10-21 · base e0a4b0c4348ef1fade46539f520e94fa140c4d8a · L=/home/vgpnk/Projects/shokunin/revenger-shokunin · S=/tmp/revenger-r61-ExecEvmOracleR26-10-scratch · no REA or xd://mcp__rea_* call, no EVM execution, no chain access, no lane writes except this file.
Record: `$L/corpus/live/runs/round-26/inspection.json` (one JSON line, `"operation":"inspect_evm_interface"`); same directory: LEDGER.md, reviewer.md, inspection.stderr.
## 1. Result
- Bytes match the declaration: 19 B, sha256 ebe2d675…8e97d; exactly one byte differs from r25 (offset 14, 0x10→0x11).
- Oracle: PUSH4 0xdeadbeef at 7 (imm 8–11) → EQ 12 → PUSH1 0x11 (operand 14) → JUMPI 15 → dest 17 = JUMPDEST, outside PUSH data. One valid static candidate.
- Saved record: functions [] (raw and normalized); evidence_kind inferred; discovery_completeness unknown; runtime_execution not-performed.
- DISAGREE on candidate count (oracle 1, REA 0). Only offset 0 is reachable from pc 0, so the empty result fits reachability filtering. Rule REA applies: UNKNOWN.
## 2. Q11 provenance (command → exact output)
P1 `stat -c '%s %n' $L/corpus/fixtures/evm-r26/fixture.raw` → `19 /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/evm-r26/fixture.raw`
P2 `sha256sum $L/corpus/fixtures/evm-r26/fixture.raw` → `ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d`
P3 `od -An -v -tx1 $L/corpus/fixtures/evm-r26/fixture.raw` → `00 60 00 35 60 e0 1c 63 de ad be ef 14 60 11 57 00 5b 00`
P4 `cmp -l $L/corpus/fixtures/evm-r25/fixture.raw $L/corpus/fixtures/evm-r26/fixture.raw` → `15  20  21` (exit 1); `sha256sum $L/corpus/fixtures/evm-r25/fixture.raw` → `2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7`
P5 `sha256sum $L/corpus/fixtures/evm-r26/truth.json` → `c20de1d43225a1f41d9b5a8688a468670691cccf4c5f0e477fe973a2df68a842`; `read $L/corpus/fixtures/evm-r26/truth.json` → sha256 ebe2…8e97d, size 19, parent_fixture ../evm-r25/fixture.raw, changed_offset 14, before_byte "10", after_byte "11", entry_stop_offset 0, jumpdest_offset 17
P6 `sha256sum $L/corpus/live/runs/round-26/inspection.json` → `bf2b2337b83f694ff9c7f9dfafbd9074de9b3310c52609fb41c993d9c782fc3c` (`stat -c %s`: 3949); `sha256sum $L/corpus/live/runs/round-26/inspection.stderr` → `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` (0 B)
P7 `python3 -B $S/decode_evm.py $L/corpus/fixtures/evm-r26/fixture.raw $L/corpus/fixtures/evm-r25/fixture.raw` (decode_evm.py, sha in §8); r26 lines: `INS off=7 byte=0x63 PUSH4 imm=deadbeef` · `INS off=12 byte=0x14 EQ` · `INS off=13 byte=0x60 PUSH1 imm=11` · `INS off=15 byte=0x57 JUMPI` · `INS off=17 byte=0x5b JUMPDEST` · `PUSH_DATA_OFFSETS [2, 5, 8, 9, 10, 11, 14]` · `JUMPDEST_OUTSIDE_PUSH_DATA [17]` · `CAND selector=0xdeadbeef push4_off=7 imm_offs=8-11 eq_off=12 pushn_off=13 operand_off=14 jumpi_off=15 dest=17 dest_byte=0x5b dest_insn_start=True dest_in_push_data=False dest_valid=True` · `REACHABLE_FROM_PC0 [0]` · `UNREACHABLE_INSN_OFFSETS [1, 3, 4, 6, 7, 12, 13, 15, 16, 17, 18]`; r25, same command: `CAND … dest=16 dest_byte=0x00 dest_valid=False`
P8 `$S/venv/bin/python -B $S/pyevmasm_dis.py $L/corpus/fixtures/evm-r26/fixture.raw` (pyevmasm 0.2.3, `disassemble_all`) → `DIS 0 STOP` · `DIS 1 PUSH1 0x0` · `DIS 3 CALLDATALOAD` · `DIS 4 PUSH1 0xe0` · `DIS 6 SHR` · `DIS 7 PUSH4 0xdeadbeef` · `DIS 12 EQ` · `DIS 13 PUSH1 0x11` · `DIS 15 JUMPI` · `DIS 16 STOP` · `DIS 17 JUMPDEST` · `DIS 18 STOP`
P9 `python3 -B $S/decode_evm.py --chain $L/corpus/fixtures/evm-r19/fixture.hex $L/corpus/fixtures/evm-r25/fixture.raw` → `CARRIER_FILE_BYTES 39` · `CARRIER_DECODED_BYTES 18 SHA256 d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723` · `PARENT_EQUALS_00_PLUS_CARRIER True`
P10 `read $L/corpus/live/runs/round-26/inspection.json?q=.normalized_result.functions,.normalized_result.evidence_kind,.normalized_result.discovery_completeness,.normalized_result.runtime_execution,.raw_result,.normalized_result.bytecode.hex&compact=true` → `[]` · `"inferred"` · `"unknown"` · `"not-performed"` · `{"functions":[]}` · `"0060003560e01c63deadbeef14601157005b00"`
P11 `read $L/corpus/live/runs/round-26/inspection.json:raw:1-1` → `"evidence_id":"ev_482e41e68b6c5f358fe660bc70eaf55f69c7b487fd61774e1a443571aecec090"`; subject `"digest":{"sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"}`; artifact and bytecode `"sha256":"ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d"`, `"bytes":19`
P12 `read $L/corpus/live/runs/round-26/inspection.json?q=[..|objects|keys[]]|unique&compact=true` → 41 unique keys; none is selector, selectors, bytecode_offset, offset or destination
## 3. Pins outside the record (execution-specs 921c0796af9ab7759440eb24436b6ac96fd5bea0, branch forks/bogota, committer 2026-10-21T14:14:23Z; file digests in §8)
- `src/ethereum/forks/prague/vm/instructions/__init__.py` (grep of the Ops enum): STOP=0x00 l.103, EQ=0x14 l.55, SHR=0x1C l.65, CALLDATALOAD=0x35 l.77, JUMP=0x56 l.104, JUMPI=0x57 l.105, JUMPDEST=0x5B l.108, POP=0x50 l.117, PUSH0=0x5F l.120, PUSH1=0x60 l.121, PUSH4=0x63 l.124, PUSH32=0x7F l.152, DUP1=0x80 l.155. No 0xFE entry; byte fe is absent from all analysed fixture hex strings (r19, r22–r26, discriminator).
- `vm/runtime.py` `get_valid_jump_destinations` l.22–69; l.29–30 verbatim: "The jump destination shouldn't be part of the data corresponding to `PUSH-N` opcodes." (13 words). URL: https://raw.githubusercontent.com/ethereum/execution-specs/921c0796af9ab7759440eb24436b6ac96fd5bea0/src/ethereum/forks/prague/vm/runtime.py (accessed 2026-10-21).
- `vm/control_flow.py` l.39 `evm.running = False` (STOP); l.63–64 and l.92–93 raise InvalidJumpDestError when the destination is not in the valid set; `vm/interpreter.py` l.241 builds that set.
- Cross-check: r23 truth.json `"opcodes": ["PUSH4","POP","STOP"]` matches the decoder (POP at off 5).
## 4. Comparison with saved record
- functions raw/normalized `[]`/`[]` vs oracle 1 valid candidate → DISAGREE (count).
- selectors / bytecode_offset: no such key (P12); oracle selector 0xdeadbeef, PUSH4 off 7, dest 17 → not comparable.
- evidence_kind `"inferred"`, discovery_completeness `"unknown"` → record-only; oracle cannot resolve.
- runtime_execution `"not-performed"` → AGREE (static decode only).
- evidence_id `ev_482e41e6…cec090` is the same in LEDGER.md:5, LOG.md:311 and reviewer.md:10; not re-derivable from the artifacts I read; differs from file sha bf2b… → UNVERIFIED.
- digests: subject, artifact and bytecode sha256 all ebe2… = P2 → AGREE; bytecode hex (P10) = decoder HEX → AGREE; stderr "" = P6 → AGREE.
- local_path and artifact.path `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/evm-r26/fixture.raw` differ from the lane path → locator differs, bytes identical, that path not opened (scope).
## 5. Authored test and disagreement
- truth.json:10 note: "One-byte correction of r25 stale jump target; static fixture, no execution."
- LOG.md:294 (r25 declaration) tests "whether a valid selector comparison pattern located after an entry `STOP` is nevertheless reported as a static interface candidate."
- LOG.md:306: offset 14 0x10→0x11 "which now targets JUMPDEST 17 while preserving entry STOP"; any selector is classified "strictly as a static candidate behind entry STOP", empty output "strictly as this fixture's result". LOG.md:311–312 record REA empty, cause unknown.
- Bytes and truth agree with LOG.md:311, LEDGER.md:3 and reviewer.md:9 on every offset in P2–P7. The only disagreement is the oracle-vs-REA count. LOG pre-registered no REA output, so count 1 is a derivation, not a prediction.
## 6. Oracle calibration (same decoder; saved outcomes cited from LOG, not re-derived)
- r19 (18 B, d1086bce…): 1 valid candidate, PUSH4@6→dest 16; all instructions reachable. LOG.md:235 saved: one candidate, offset 16. AGREE.
- r22 (34 B, sha 94c1790f…): 2 valid, aaaaaaaa@7→30 and bbbbbbbb@17→32. LOG.md:267 saved: same two. AGREE.
- r23 (7 B, sha 8047ddff…): 0 (PUSH4_NO_PATTERN); truth comparison_or_jump false; LOG.md:279 REA zero. AGREE.
- r24 (35 B, sha b69834e0…): 0 PUSH4 instructions (immediate decoy); LOG.md:290 REA none. AGREE.
- r25: dest 16 is STOP → 0 valid; LOG.md:301 REA empty. AGREE. r26: 1 valid vs REA 0 → the only discordant fixture.
## 7. C09 consequences and first falsifiers (inputs only; no entry written)
- F1 FALSIFIED by saved r26: "REA reports every valid static PUSH4→JUMPDEST candidate" (oracle 1, REA 0).
- H1 (report only candidates reachable from pc 0) and H2 (scan halts at the first STOP) both fit all six outcomes above. Both predict 0 on r26, so r26 cannot separate them.
- Proposed discriminator (scratch only; not authored, not in lane): `60055600005b63deadbeef14600f575b00` (17 B, sha256 1b67229edc1b0bf067d667d5fc17f8e2dd3c9739906dac8e69f5d1a35ec2ee78). Decoder: candidate PUSH4@6 → dest 15 valid; reachable [0, 2, 5, 6, 11, 12, 14, 15, 16]; first STOP instruction at 3. Predicted, untested against REA: H1 → 1 reported; H2 → 0.
- Citable for C09 from r26: "saved output empty; cause unknown; valid static pattern behind entry STOP"; the record itself says "Empty results do not prove the absence of callable dispatch." Not citable: "REA reports a PUSH4 candidate for r26" or "interface present".
## 8. Installs, scope, limits
- Installed: pyevmasm 0.2.3 (PyPI) via `uv venv` + `uv pip install` into $S/venv (Python 3.15.0 per uv). uv 0.13.0 at ~/.local/bin/uv, unchanged. Reason: second disassembler for cross-check. Tool note: SyntaxWarning at evmasm.py:492 on import; output unaffected.
- Not done: labrat (no spawn tool in this seat); no REA rerun; prymeagnt path not opened; no git or jj command in the lane.
- Limits: static bytes only; "valid" = spec-valid static destination, not runtime reachability; 0xdeadbeef has no ABI meaning; sha256 identifies bytes, not origin.
- Digests of scratch and spec inputs: `sha256sum $S/prague_runtime.py $S/prague_instructions_init.py $S/prague_interpreter.py $S/prague_control_flow.py $S/prague_vm_init.py $S/decode_evm.py $S/pyevmasm_dis.py $S/execspecs-commit.json $S/discriminator_proposed.raw $S/r19_decoded_18.raw` →
  a2801c4169b806a9494707179a9df20170a37a1769596aac56013ddba509aef8 prague_runtime.py
  6803bc7d2dfcb03101cc5aa4cf2ef686c53da7246518023b8e97c0066c5b1770 prague_instructions_init.py
  561cc703c2c7b4f7ddae780cae4aeed50611356dfb33032576e9e7eac5ea0c52 prague_interpreter.py
  0d3f6ae0cc4f0bc93b848ab6d68f19b85ee9e5f843a2cbcd699b08a8e35e5b98 prague_control_flow.py
  75f6a4170760ca958e6e8c46c85f866469043defd17cf28d8e969c63fba30ba5 prague_vm_init.py
  58e52bcb6c0f9b7669b5c98995d0b4ded07272c4f00cf804d0db423299d304cf decode_evm.py
  fd958b5f94d534fe322493d7d2bcd40f96dc8d5e69f0201294f5a1877a9c94f7 pyevmasm_dis.py
  680546f79171d8af72b442a86a6887b924839b2b704cdb3d43d086b274869b8c execspecs-commit.json
  1b67229edc1b0bf067d667d5fc17f8e2dd3c9739906dac8e69f5d1a35ec2ee78 discriminator_proposed.raw
  d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 r19_decoded_18.raw

VERDICT: bytes, digests, one-byte delta and record identities match; saved REA reports zero candidates where an independent valid PUSH4→JUMPDEST pattern sits behind entry STOP, so F1 is falsified and C09 may cite r26 only as an empty, cause-unknown negative.
