# ExecEvmOracleR25 — round 61 RUNS: independent byte oracle, evm-r25 (C09)
Seat CloseChousa26.ExecEvmOracleR25-10 · read-only: no REA call, no bytecode execution, no chain/RPC, no lane edits · labrat not spawned.
Clone /tmp/revenger-r61-ExecEvmOracleR25 · branch r61-ExecEvmOracleR25 · HEAD e0a4b0c4348ef1fade46539f520e94fa140c4d8a (observed) · `git status --short` = 0 lines.
Scratch /tmp/revenger-r61-ExecEvmOracleR25-scratch/ · Q11 script q11-commands.sh 42806b4a928172572098d291423da4b5fb8f22f62bdfc533ac2366dccd5669ac · log q11-output.txt 277a8fd3484449fa3c2c2583bc03a7da12a3ca958ab756c04b9e4ba109b71573 (rc 0).

## 1. Presence and identity
- Record exists: `corpus/live/runs/round-25/inspection.json` (evidence `ev_23a9464bf2d8c3de3614176efa53016f002ddade19f1ae842b4325ba2d095579`, sha256 `4f677a209d08c3f9e531191aea9cdc58533898b9f9ed2394b3db63a0b8d448cf`).
- C0: 21 EVM fixture/truth/record files, live lane vs clone, `sha256sum` diff → identical. C9 stderr: `0` bytes.

## 2. Q11 provenance, r25 (command → output; full commands in q11-commands.sh)
- C1 `sha256sum fixture.raw truth.json` → fixture `2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7`; truth `059c190447013f3f33d6387bd15fc43d1de9e2a9f01a38befaabd5f5559d1819`
- C2 `wc -c fixture.raw` → `19`
- C3 `xxd fixture.raw` → `00000000: 0060 0035 60e0 1c63 dead beef 1460 1057` / `00000010: 005b 00`
- C4 own decoder → `decoded_hex "0060003560e01c63deadbeef14601057005b00"`; `insns "0:STOP 1:PUSH1(00) 3:CALLDATALOAD 4:PUSH1(e0) 6:SHR 7:PUSH4(deadbeef) 12:EQ 13:PUSH1(10) 15:JUMPI 16:STOP 17:JUMPDEST 18:STOP"`; `jumpdests [17]`; `reachable_from_pc0 [0]`; `unresolved_dynamic_jumps []`; `push4_eq_push_jumpi [{"dest":16,"dest_byte":"00","dest_in_push_data":false,"dest_is_insn_start":true,"dest_is_jumpdest":false,"dest_push":"13:PUSH1(10)","eq_offset":12,"jumpi_offset":15,"jumpi_reachable_from_pc0":false,"push4_offset":7,"selector":"deadbeef"}]`; `jumpi [{"dest_byte":"00","dest_is_jumpdest":false,"jumpi_offset":15,"static_dest":16}]`; `rule_A []`, `rule_B [["deadbeef",16]]`, `rule_C []`.
- C5 `jq -c . truth.json` → `size 19`, `entry_stop_offset 0`, `push4_opcode_offset 7`, `selector_immediate_offset 8`, `selector deadbeef`, `encoded_jump_operand 16`, `jumpdest_byte_offset 17`, `jump_target_valid false`.
- C6 `jq` on saved record → `raw_functions []`, `norm_functions []`, `evidence_kind inferred`, `confidence inferred`, `discovery unknown`, `runtime not-performed`, `bytecode_kind unknown`, `deployment_authenticity unknown`, `hardfork unknown`, `stderr ""`, `bytecode_bytes 19`, `bytecode_sha 2d87…f8f7`, `bytecode_hex 0060003560e01c63deadbeef14601057005b00`, `artifact_bytes 19`, `artifact_sha 2d87…f8f7`, `subject_sha 2d87…f8f7`, `provider evmole@0.9.3`, `encoding raw`.
- C7 evidence_id: `jq -cS 'del(.evidence_id)' | sha256sum` → `79014769bbb6817925371b002c8fccc262a91e815853eff95470f638d6fbed32`; `jq -cSj 'del(.evidence_id)' | sha256sum` → `8c072c07210f43afec7add4708e518398072ed213928fdc4a7337fffade4d943`; `jq -cSj . | sha256sum` → `86accbb2ffd1436b02236f0aa1cf94adf26fac992139d955ccf2d2c7438f02ae`. None equals `23a9464b…5579` → evidence_id RECORDED, NOT re-derived.
- C8 pyevmasm 0.2.3 (`xcheck_pyevmasm.py`) → `fixture.raw bytes=19 insns_own=12 insns_pyevmasm=12 MATCH`.
- C9 `readlink -f /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger` → `/home/vgpnk/Projects/shokunin/revenger-shokunin`; sha256 of the record's `local_path` → `2d87…f8f7` (locator resolves to the same bytes; identity is the digest).
- C10 `python3 -B -` (stdin) → `r25 == 00 + r19: True`; `r26[1:]` vs `r19` differing `[(13, 16, 17)]`.

## 3. Saved record vs own derivation (r25)
- functions (raw and normalized): saved `[]`. Own A `[]` and C `[]` match; own B `[deadbeef@16]` mismatches (`match_B false`).
- selector / bytecode_offset: none reported. The only candidate-shaped site is PUSH4 deadbeef@7 (immediate 8–11); its JUMPI destination 16 is STOP, not JUMPDEST.
- evidence_kind inferred, discovery_completeness unknown, runtime_execution not-performed: consistent with LEDGER.md. This seat executed nothing.
- digests: subject, artifact, bytecode and carrier all `2d87…f8f7`; bytecode hex and bytes equal the decode. The record's SHA-256 is not a Keccak code hash (the record's own limitation; not computed here).

## 4. Declared intent vs bytes — disagreement
- LOG.md:295 declares "(including valid jump destination)". Bytes: operand 16 → STOP (C4). LOG.md:300 records the premise as false; line 295 stays as written (append-only). Do not repeat that premise in C1.
- truth.json note, LEDGER.md and reviewer.md agree with the bytes on offsets 0/7/8/16/17 and the invalid target. No other disagreement found.
- Authored purpose (LOG.md:294–295): whether a valid comparison after an entry STOP is reported as a static candidate. As built it is also an invalid-target variant, so confounded (LOG.md:300). Corrected valid-target control: r26 (LOG.md:306, 311).

## 5. Cross-fixture table (`cross_table.py`; B pattern · A +JUMPDEST · C +reachable from pc 0 · L +JUMPI before first STOP; dead=deadbeef, aaaa=aaaaaaaa, bbbb=bbbbbbbb, @N = JUMPI destination)
rec | bytes | B | A | C | L | saved | match B/A/C/L
r19 | 18 | dead@16 | dead@16 | dead@16 | dead@16 | dead@16 | T/T/T/T
r21 | 18 | dead@16 | dead@16 | dead@16 | dead@16 | dead@16 | T/T/T/T
r22 | 34 | aaaa@30, bbbb@32 | same | same | same | same | T/T/T/T
r23 | 7 | [] | [] | [] | [] | [] | T/T/T/T
r24 | 35 | [] | [] | [] | [] | [] | T/T/T/T
r25 | 19 | dead@16 | [] | [] | [] | [] | F/T/T/T
r26 | 19 | dead@17 | dead@17 | [] | [] | [] | F/F/T/T
P1 (not run, §6) | 19 | dead@17 | dead@17 | dead@17 | dead@17 | – | –
P2 (not run, §6) | 19 | dead@17 | dead@17 | dead@17 | [] | – | –
- (a) B refuted by r25 and r26. (b) A refuted by r26: JUMPDEST 17 is valid, yet the saved output is empty, so the invalid target is not the necessary cause (agrees with LOG.md:312).
- (c) Only C and L reproduce all seven saved outcomes. Both were formulated after the r25/r26 results were already recorded: post hoc, not pre-registered (Q07). Neither is a validated cause.
- (d) The two dispatch-bearing empties share entry byte 0x00 (STOP) and length 19; all three positives begin with PUSH1 0x60. These are shared factors, not isolated ones.
- (e) r26 = r19 with one prepended 0x00 and one forced operand change (r19 offset 13: 0x10→0x11).

## 6. Proposed falsifiers P1–P2 (proposals — not authored, not run, no REA call; need pre-registration in a later declared round; never cite as results)
- P1 `5b60003560e01c63deadbeef14601157005b00` (sha256 `121ddb5e10fb3ee0f5cae92a9d5d7bc13b8b81ae148c89a6b9386f52dd7457c2`; file f1-leading-jumpdest.raw): r26 with byte 0 changed STOP→JUMPDEST. Predicts deadbeef@17 under every rule. Candidate ⇒ entry STOP is the suppressor (or STOP-specific); empty ⇒ it is not. Length 19 is kept.
- P2 `6006560000005b63deadbeef14601157005b00` (sha256 `e7e0981269ff89d0d41f54daa511a049deed5dfe880e39bf0b65553c7092424e`; file f3-jump-over-stop.raw): dispatch reachable only through a static JUMP over in-stream STOPs (first STOP at 3). C predicts candidate; L predicts empty. Separates C from L.
- Not separated by P1/P2: a non-STOP entry whose dispatch is statically unreachable (entry STOP vs reachability). Not designed here.

## 7. Sources and admissibility
- No web source opened. EVM facts used (execution starts at pc 0; STOP halts; JUMP/JUMPI targets must be JUMPDEST; PUSHn bytes are immediates) are manual, spec-level (Q04). A tier-A SOURCES row must be opened in round 61 (scout CloseChousa26.SrcEvmCodesScreen-10); unverified here.
- OK for C09: section 2 byte facts; saved sets for r19/r21/r22; empties r23–r26 with reasons (no pattern; pattern inside PUSH32 data; entry STOP).
- NOT OK: rule A or B as REA behaviour; any reachability or cause claim; any ABI/signature or Keccak selector identity.

## 8. Installs and files
- Installs: none by this seat. `uv tool install pyevmasm` → "already installed"; `uv tool list` → pyevmasm v0.2.3 (entry `evmasm`). Reason: third-party disassembler cross-check. Python 3.14.8 (/usr/bin/python3), stdlib only.
- Written: lane `.ufo/waves/round-61/build/ExecEvmOracleR25.md` (this report). Scratch only; clone unchanged. sha256:
  evm_oracle.py `582fe090485e8405ec586d15d62f0225e4716dd67fefd31b958b4f5c6da044f3` · xcheck_pyevmasm.py `12ddbdc14994935e3b19a3a26bc0ebf7fada88657f9cd1b099b4b4df6f02fdee` · cross_table.py `748013f2c156a5678acf58b1fafdc069a326497d20545d5a5917f75d0a70bed5`
  q11-commands.sh `42806b4a928172572098d291423da4b5fb8f22f62bdfc533ac2366dccd5669ac` · q11-output.txt `277a8fd3484449fa3c2c2583bc03a7da12a3ca958ab756c04b9e4ba109b71573`
  f1-leading-jumpdest.raw `121ddb5e10fb3ee0f5cae92a9d5d7bc13b8b81ae148c89a6b9386f52dd7457c2` · f3-jump-over-stop.raw `e7e0981269ff89d0d41f54daa511a049deed5dfe880e39bf0b65553c7092424e`

VERDICT: r25 bytes, truth.json and saved identity agree; the empty saved output rules out the pattern-only and JUMPDEST-only rules, leaves reachability- or terminator-gated rules unvalidated, and REA's cause stays UNKNOWN (P1/P2 proposed, not run).
