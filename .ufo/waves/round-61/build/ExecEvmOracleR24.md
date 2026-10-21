# ExecEvmOracleR24 — byte oracle, fixture evm-r24 vs round-24 REA record

Seat CloseChousa26.ExecEvmOracleR24-10 · RUNS (read-only) · 2026-10-21 · base e0a4b0c4348ef1fade46539f520e94fa140c4d8a. No REA producer call, no bytecode execution, no RPC, no lane write except this file. Decoders are this seat's own; `corpus/verify_evm_evidence.py` was not opened. R = /home/vgpnk/Projects/shokunin/revenger-shokunin

## 1. Record
FOUND `R/corpus/live/runs/round-24/inspection.json` (`operation` inspect_evm_interface; sha256 `ec9e147db2b042f4d991816fa2a02fe95373de31956730fd1eb4cce5763742cd`). `R/corpus/live/runs/round-24/inspection.stderr`: `wc -c` → `0`.

## 2. Q11 provenance (command → exact output)
- P1 `sha256sum R/corpus/fixtures/evm-r24/fixture.raw` → `b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93  R/corpus/fixtures/evm-r24/fixture.raw`
- P2 `wc -c < R/corpus/fixtures/evm-r24/fixture.raw` → `35`
- P3 `xxd -p R/corpus/fixtures/evm-r24/fixture.raw | tr -d '\n'` → `7f63deadbeef1460105700000000000000000000000000000000000000000000005000`
- P4 `python3 -B decode_r24.py` (stdout saved as `decode_r24.out`, sha256 `9ab974365328c7a986ebf53b797f3ebdb03acdd554e0e6b0f849ae4cc108011a`); exact lines, the 46-zero run shown as `[46×0]`:
```
len=35 sha256=b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93
offset=0 op=0x7f PUSH32 imm_at=1 imm=0x63deadbeef14601057[46×0]
offset=33 op=0x50 POP
offset=34 op=0x00 STOP
A.executable_push4=0
A.walk_has_EQ_JUMP_or_JUMPI=False
A.executable_JUMPI_count=0
B.byte_0x63_offsets=[1]
B.pattern_at=1 PUSH4 sel=0xdeadbeef EQ_at=6 PUSH1_at=7 dest_imm=0x10 JUMPI_at=9
B.   dest=16 src=PUSH1_at_7 dest_byte=0x00 dest_is_JUMPDEST=False dest_inside_push_data=True passes_JUMPDEST_and_boundary=False
B.   naive_candidate_without_JUMPDEST_check=selector_0xdeadbeef
```
- P5 `jq -c '{evidence_id, operation, provider_id: .provider.id, provider_version: .provider.version, encoding: .parameters.encoding, raw_functions: .raw_result.functions, normalized_functions: .normalized_result.functions, evidence_kind: .normalized_result.evidence_kind, confidence, discovery_completeness: .normalized_result.discovery_completeness, runtime_execution: .normalized_result.runtime_execution, artifact_sha256: .normalized_result.artifact.sha256, artifact_bytes: .normalized_result.artifact.bytes, bytecode_sha256: .normalized_result.bytecode.sha256, bytecode_bytes: .normalized_result.bytecode.bytes, bytecode_hex: .normalized_result.bytecode.hex, subject_sha256: .subject.digest.sha256}' inspection.json` → `{"evidence_id":"ev_50d5ffb1fdbd17c4896409ca4cc8b20d7ed344ef4011029bea4aa474b7f0ab9e","operation":"inspect_evm_interface","provider_id":"evmole-interface","provider_version":"evmole@0.9.3","encoding":"raw","raw_functions":[],"normalized_functions":[],"evidence_kind":"inferred","confidence":"inferred","discovery_completeness":"unknown","runtime_execution":"not-performed","artifact_sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93","artifact_bytes":35,"bytecode_sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93","bytecode_bytes":35,"bytecode_hex":"7f63deadbeef1460105700000000000000000000000000000000000000000000005000","subject_sha256":"b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93"}`
- P6 `jq -c '[paths | map(tostring) | join(".")] | map(select(test("selector|bytecode_offset")))' inspection.json` → `[]`; `jq -c '.normalized_result.functions, .raw_result.functions' inspection.json` → `[]` then `[]`; `jq -c '[paths | map(tostring) | join(".")] | length' inspection.json` → `64`
- P7 `jq -j .normalized_result.bytecode.hex inspection.json` cmp'd against P3 → `BYTECODE_HEX_EQUAL`; record `artifact.sha256`, `subject.digest.sha256`, `bytecode.sha256` cmp'd against P1 → `SHA_ALL_EQUAL`; `jq -c '[.normalized_result.artifact.bytes, .normalized_result.bytecode.bytes]' inspection.json` → `[35,35]`
- P8 truth.json (recorded values, not re-derived by the file; `jq -r '.sha256, (.size|tostring), (.executable_push4_count|tostring), (.comparison_or_jump_instruction|tostring), (.embedded_pattern_offsets|tostring), .embedded_pattern_hex' truth.json`) → `b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93` / `35` / `0` / `false` / `[1,9]` / `63deadbeef14601057`. All equal P1–P4.
- P9 `python3 -B dj_check.py` (Yellow Paper D(c)=D_J(c,0), eqs. 160–162; saved `dj_check.out`, sha256 `3a3d79f35eeee4234af5d24d102b8d3f791c3be2c2c34d8e89b02b6b6a1700cd`) → `FIXTURE count_0x5b_bytes=0 offsets_0x5b=[]`; `FIXTURE boundary_walk_from_0=[0, 33, 34]`; `FIXTURE D(c)=[]`; `FIXTURE dest16_in_D=False dest16_byte=0x00`; control in memory (`60 5b 5b 00`): `CONTROL D(c)=[2]`, `CONTROL expected_D={2} got=[2] match=True`
- P10 `uv run --no-project --with pyevmasm python pyevmasm_check.py` (stdout not saved; rerun reproduces) → `pyevmasm_version=0.2.3`; `pc=0 name=PUSH32 size=33 operand=0x63deadbeef14601057[zeros elided]`; `pc=33 name=POP size=1 operand=-`; `pc=34 name=STOP size=1 operand=-`. Agrees with P4.
- P11 `python3 -B falsifier_probe.py` (saved `falsifier_probe.out`, sha256 `2a9455247390f15a1267641aa80dda040e7459188d37a29f31501837b9190c81`) → `probe count_0x5b=1 offsets=[12]`; `probe boundary_walk=[0, 33, 34] D(c)=[]`; `probe naive_S2=deadbeef (promote dest=12 dest_byte=0x5b) spec_candidate=none`; `r24 naive_S2=None (no-promote dest=16 dest_byte=0x00) spec_D=[]`

## 3. Record vs oracle
- Functions/selectors/bytecode_offset: `functions=[]` raw and normalized; no selector or bytecode_offset key exists (P6). Oracle: 0 executable PUSH4, 0 executable JUMPI (P4). AGREE.
- Digests, sizes, hex: subject, artifact and bytecode sha256 = P1; bytes 35/35 = P2; hex = P3 (P5, P7). AGREE.
- evidence_id, evidence_kind `inferred`, confidence `inferred`, discovery_completeness `unknown`, runtime_execution `not-performed` (P5): RECORDED, not derivable from bytes; consistent with zero execution and zero candidates.
- PUSH4: the only 0x63 byte is offset 1, inside the PUSH32 immediate (bytes 1–32). JUMPI: none executable; the pattern JUMPI at 9 targets 16 = `0x00`, not JUMPDEST, inside PUSH data, not in D(c)=∅ (P4, P9).

## 4. Disagreements and scope
- Authored to test (truth.json `note`; LOG.md:283–284; LEDGER.md:3): an inert `PUSH32 <imm>; POP; STOP` whose immediate holds the r19 bytes `63deadbeef14601057` (offsets 1–9), so no executable PUSH4/EQ/JUMPI exists and a pattern scanner must not promote.
- D1 (material, scope): LEDGER.md:5 credits "zero false promotions of an immediate-data decoy"; LOG.md:290 "confirmed no REA candidate was reported for this one immediate-data decoy". Observed: the decoy's own destination fails (16 → `0x00`) and the carrier contains zero 0x5B bytes (P9). The negative rules out only the naive pattern scanner (P4 `naive_candidate…`). A scanner S2 that also requires a 0x5B destination byte emits nothing here (P11), and so does an opcode-walk scanner (P4 `A.executable_push4=0`). r24 does not isolate PUSH-data exclusion; LOG.md:291 "calibration improved narrowly" holds only as "no candidate emitted for this carrier."
- D2 (provenance): `subject.local_path` and `locations[0].path` (inspection.json:1) = `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/evm-r24/fixture.raw`, not the lane path. Identity rests on the digest (P1, P7). [INFERENCE] the record was produced from another checkout.
- D3 (completeness only): LEDGER.md:5 omits `evidence_kind=inferred` (P5).
- No disagreement on bytes, offsets, decoy geometry (LEDGER.md:3; truth.json `embedded_pattern_offsets` [1,9]), digests, size, stderr, functions, discovery, runtime or truth.json values. The truth.json note matches P4.
- Limitation the record states and any C09 entry must carry (inspection.json:1, `normalized_result.limitations`): "Empty results do not prove the absence of callable dispatch."

## 5. Sources (opened 2026-10-21)
- Yellow Paper, https://raw.githubusercontent.com/ethereum/yellowpaper/master/Paper.tex (master; no revision in the raw file). Section "Jump Destination Validity", Paper.tex:1290. L1292: "We define this as any position in the code occupied by a JUMPDEST instruction." (14 words). L1294: "All such positions must be on valid instruction boundaries, rather than sitting in the data portion of PUSH operations" (19 words). Equations D, D_J, N from Paper.tex:1296ff (transcribed in dj_check.py). Rows: Paper.tex:2572 `\linkdest{JUMPI}{}0x57`; Paper.tex:2590 `0x5b & {\small JUMPDEST} & 0 & 0 & Mark a valid destination for jumps.` PDF revision per sibling SrcYellowPaperJumpdest.md:9 (`SHANGHAI VERSION efc5f9a – 2025-02-04`), recorded.
- execution-specs master, https://raw.githubusercontent.com/ethereum/execution-specs/master/src/ethereum/forks/frontier/vm/instructions/__init__.py (unpinned): `54: EQ = 0x14`, `91: STOP = 0x00`, `93: JUMPI = 0x57`, `96: JUMPDEST = 0x5B`, `103: POP = 0x50`, `106: PUSH1 = 0x60`, `109: PUSH4 = 0x63`, `137: PUSH32 = 0x7F`. Pinned v2.20.0 copy: sibling SrcExecSpecsOpcodes.md:6–11 (recorded).
- evm.codes: reader returned the page head only, no opcode table; unavailable, not used.

## 6. Frontier: first C09 falsifier (proposal only; not authored, not run through REA)
- Carrier (in memory, P11): `7f63deadbeef14600c5700005b00000000000000000000000000000000000000005000` — same PUSH32 frame; embedded PUSH1 0x0c; 0x5b at offset 12 inside PUSH32 data.
- Spec expectation: D=∅, no candidate. Scanner S2 promotes `0xdeadbeef`. A C09 entry citing r24 for PUSH-data exclusion must wait until a producer result on a carrier like this exists; the coordinator decides whether to author it.

## 7. Installs and writes
- Installs: none by this seat. Used pre-existing uv 0.13.0; `uv run --no-project --with pyevmasm` fetched pyevmasm 0.2.3 from PyPI into uv's ephemeral cache, no global install. Reason: independent second decoder. Warning seen: `SyntaxWarning: 'return' in a 'finally' block` (pyevmasm/evmasm.py:492), harmless here.
- Writes: this file (lane path, per the Report trailer). Scratch under `/tmp/revenger-r61-CloseChousa26.ExecEvmOracleR24-10-scratch/`: decode_r24.py `74ea6248b4a2fedd91e07a2542b1b36b6b6854efbae179cfa3fd4aebab683be0`; decode_r24.out `9ab974365328c7a986ebf53b797f3ebdb03acdd554e0e6b0f849ae4cc108011a`; dj_check.py `90cf2c8ace00fd379e45e34657046e9384f51218d332b35a04b8eadcb18fcbde`; dj_check.out `3a3d79f35eeee4234af5d24d102b8d3f791c3be2c2c34d8e89b02b6b6a1700cd`; falsifier_probe.py `5ad43e945bdf1381fa2e1748e57183c219e326e9fb48448913ab5982f6f67ea9`; falsifier_probe.out `2a9455247390f15a1267641aa80dda040e7459188d37a29f31501837b9190c81`; pyevmasm_check.py `3f995f8dc4f423e808f25e7354e784346880f3677bcb40f3af4b24b1a4b9cc78`. No clone, no patch (RUNS).
- Correction: an earlier copy landed at the fleet root (misroot, sha256 `b821c6873722c58d92b49f0f1a45123b70119fd7c85ba66f9abe3e0d34a489c1`); removed by this seat.

VERDICT: r24 record and carrier match my oracle byte-for-byte (no executable PUSH4 or JUMPI; functions=[]; discovery unknown; runtime not-performed), but r24 cannot isolate PUSH-data exclusion (its embedded destination 0x10 is not a JUMPDEST and the carrier has no 0x5B byte), so C09 must not cite it as immediate-data evidence.
