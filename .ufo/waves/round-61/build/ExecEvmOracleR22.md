# ExecEvmOracleR22 — RUNS: independent byte oracle, fixture evm-r22 vs saved REA record (round 61)

Seat CloseChousa26.ExecEvmOracleR22-10, leaf, read-only: no REA/rea_* call, no bytecode execution, no chain/RPC, no lane edit, no labrat. `corpus/verify_evm_evidence.py` was NOT opened; all decoding is my own code.
Clone `/tmp/revenger-r61-ExecEvmOracleR22-10` (branch r61-ExecEvmOracleR22-10); observed base `git rev-parse HEAD` = e0a4b0c4348ef1fade46539f520e94fa140c4d8a (pin). Live-lane fixture, truth and record are sha-identical to the clone.
Record located: `corpus/live/runs/round-22/inspection.json` (line 1, `operation: inspect_evm_interface`). Not missing.

## Result (observation, scoped to fixture r22)
- No value-level disagreement. Decoded 2 `PUSH4→EQ→PUSH1→JUMPI` patterns; raw and normalized record each report exactly these 2 selector→destination pairs; 0 extra, 0 missing.
- `PUSH4@7` (imm 8–11 = aaaaaaaa) → `JUMPI@15` → dest 30 = JUMPDEST. `PUSH4@17` (imm 18–21 = bbbbbbbb) → `JUMPI@25` → dest 32 = JUMPDEST. Both dests are instruction starts, outside PUSH data.
- Record offsets 30/32 are destinations, not PUSH4 pcs (7/17) or immediate starts (8/18). The record has no selector-location field.
- r22 cannot separate opcode-aware decoding from naive byte matching: a naive regex finds the same two hits (V3, V4).
- evidence_id `ev_24fe0001213ec58a588d086e0fe55677d749f3eb6998afe6ee6095ff9dc4af4b` is identical in 4 files (V11). NOT recomputed: 3 guessed canonical-JSON forms do not match (V12).
- Fixture-scoped exhaustiveness holds (2 of 2). `discovery_completeness=unknown` is kept, since general completeness is not shown.

## Q11 provenance block (command → exact output)
Paths: FIX=`/tmp/revenger-r61-ExecEvmOracleR22-10/corpus/fixtures/evm-r22/fixture.raw`; TRUTH=`…/corpus/fixtures/evm-r22/truth.json`; REC=`…/corpus/live/runs/round-22/inspection.json`; ORACLE=`/tmp/revenger-r61-ExecEvmOracleR22-10-oracle.py` (sha256 9c1b03dd40de8a6a4205502b891aa261a42cbbbd3f895d5e37cfd44bbe3aaf9f).
- V1 digest/size: `sha256sum $FIX` (clone) → 94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2 ; `stat -c '%s %n' corpus/fixtures/evm-r22/fixture.raw` (live lane) → `34 corpus/fixtures/evm-r22/fixture.raw`
- V2 bytes: `od -An -tx1 -v corpus/fixtures/evm-r22/fixture.raw` (live lane; sha-identical to FIX) → `60 00 35 60 e0 1c 80 63 aa aa aa aa 14 60 1e 57 80 63 bb bb bb bb 14 60 20 57 00 00 00 00 5b 00 5b 00`
- V3 decode: `python3 -B $ORACLE $FIX $TRUTH $REC` → exit 0; stdout sha256 30ed6c604c4d2c39d17862a2b77d87c4382947f5377ccc9b9d2e2eb1dd6cf7a7; key lines:
  `SWEEP_END pc=34 equals_length=True instructions=22`
  `PATTERN sel=aaaaaaaa PUSH4@7 imm=8..11 EQ@12 PUSH1@13 operand@14=30 JUMPI@15`
  `DEST 30 insn_start=True opcode=0x5b JUMPDEST=True in_push_immediate=False`
  `PATTERN sel=bbbbbbbb PUSH4@17 imm=18..21 EQ@22 PUSH1@23 operand@24=32 JUMPI@25`
  `DEST 32 insn_start=True opcode=0x5b JUMPDEST=True in_push_immediate=False`
  `JUMPI_ALL [15, 25] BACKWARD_PAIRS [(7, 15), (17, 25)]` ; `CHECK forward_equals_backward True`
- V4 naive contrast (same run): `NAIVE_REGEX [(7, 'aaaaaaaa', '1e'), (17, 'bbbbbbbb', '20')]` ; `NAIVE_BYTE 0x63 positions=[7, 17] inside_push_immediate=[]` ; `NAIVE_BYTE 0x5b positions=[30, 32] inside_push_immediate=[]`
- V5 opcode presence (same run): `CALLVALUE_0x34=False CALLDATALOAD_0x35=True SHR_0x1c=True DUP1_0x80=True`
- V6 third-party cross-check: `/tmp/revenger-r61-ExecEvmOracleR22-10-venv/bin/python -W ignore /tmp/revenger-r61-ExecEvmOracleR22-10-xcheck.py $FIX` → 22 `SWEEP pc name imm` lines (pyevmasm 0.2.3); `diff` of the `^SWEEP ` lines against own run → exit 0, 22 lines each, both sha256 e45c225f82a4e7ed31b6bb565d622da0044bb208733ad7f783fa420e8c68eb62
- V7 spec opcode pin: `timeout 60 git ls-remote https://github.com/ethereum/execution-specs HEAD` → 921c0796af9ab7759440eb24436b6ac96fd5bea0 HEAD. `grep -n -E '^\s+(…) = '` on `src/ethereum/forks/cancun/vm/instructions/__init__.py` @921c0796 (sha256 6803bc7d2dfcb03101cc5aa4cf2ef686c53da7246518023b8e97c0066c5b1770) → `55: EQ = 0x14` · `77: CALLDATALOAD = 0x35` · `103: STOP = 0x00` · `105: JUMPI = 0x57` · `108: JUMPDEST = 0x5B` · `121: PUSH1 = 0x60` · `124: PUSH4 = 0x63` · `155: DUP1 = 0x80`
- V8 spec JUMPDEST rule: `src/ethereum/forks/cancun/vm/runtime.py` @921c0796 (sha256 a2801c4169b806a9494707179a9df20170a37a1769596aac56013ddba509aef8), docstring lines 26–30, quote (l.29–30, 13 words): "The jump destination shouldn't be part of the data corresponding to `PUSH-N` opcodes." URL https://raw.githubusercontent.com/ethereum/execution-specs/921c0796af9ab7759440eb24436b6ac96fd5bea0/src/ethereum/forks/cancun/vm/runtime.py ; revision = that commit ; accessed 2026-10-21. Loop l.58–65 skips PUSH-N data.
- V9 spec run: `python3 -B …/spec-harness.py …/spec-ops.py …/spec-runtime.py $FIX` (static function over bytes; no EVM run) → `SPEC fixture_jumpdests=[30, 32] fixture_bytes=34`; in-memory controls `605b00`→[], `5b`→[0], `63aaaaaaaa5b`→[5]
- V10 truth: `grep -n -E '"(selector|push4_opcode_offset|selector_immediate_offset|push1_operand_offset|destination_offset|note|sha256|size)"' $TRUTH` → sha256 l.2, size l.3, branch A l.7–11, branch B l.14–18, note l.21. Oracle: `TRUTH sel=aaaaaaaa equal=True expected=[7, 8, 14, 30]`, `TRUTH sel=bbbbbbbb equal=True expected=[17, 18, 24, 32]`, `TRUTH selector_set_equal=True`
- V11 record (oracle lines): `RECORD_FILE sha256=c55f69727ce2e62707ae0f9203c338efe57e6aeadc7fb5f5cd939bee3f9b3a33` ; `RECORD subject_sha256_equal=True` ; `RECORD artifact sha256_equal=True bytes=34 encoding=raw` ; `RECORD bytecode sha256_equal=True bytes=34 hex_equal=True kind=unknown deployment_authenticity=unknown hardfork=unknown` ; `RECORD confidence=inferred authority=shipped-artifact evidence_kind=inferred discovery_completeness=unknown runtime_execution=not-performed` ; `raw_functions=[('aaaaaaaa', 30, 'abi', '', 'payable'), ('bbbbbbbb', 32, 'abi', '', 'payable')]` ; `normalized_functions=[('0xaaaaaaaa', 30, 'abi', '', 'payable'), ('0xbbbbbbbb', 32, 'abi', '', 'payable')]` ; `CHECK raw_pairs_equal_decoded=True extra=[] missing=[]` ; `CHECK normalized_pairs_equal_decoded=True extra=[] missing=[]` ; `CHECK recorded_offsets_equal_PUSH4_pc=[] equal_immediate_start=[]` ; `CHECK recorded_offsets_all_JUMPDEST_insn_start=True`
- V12 evidence_id (oracle): `EVIDENCE_ID_TRY record_minus_evidence_id sha256=9ec26a475797cb1920de89506bb94aa47bff44a5c54b3d83b250c676316158fe match=False` ; `raw_result sha256=dcfca7420e168660d6d896c8b07627689f62eb26bf7613025877f7ce44caa9b2 match=False` ; `full_record sha256=065308a245a01a94166dd37cfe07973919cb7e3e16ddb4a565b312147ac6f887 match=False`
- V13 occurrences: `grep -rno "ev_24fe0001213ec58a588d086e0fe55677d749f3eb6998afe6ee6095ff9dc4af4b" LOG.md corpus/live/runs/round-22/ corpus/live/runs/round-22/reviewer.md` (reviewer.md listed twice in that command; de-duplicated here) → LOG.md:267 ; LEDGER.md:5 ; inspection.json:1 ; reviewer.md:20
- V14 record locator: `sha256sum /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/evm-r22/fixture.raw` → 94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2 (exit 0; file present)
- V15 stderr: `ls -la corpus/fixtures/evm-r22 corpus/live/runs/round-22` (clone) → `inspection.stderr` 0 bytes (exit 0 not reproduced; no REA rerun)

## Authored-to-test and disagreements
- truth.json (l.7–18, note l.21): two branches. aaaaaaaa: PUSH4@7, imm 8, PUSH1 operand 14, dest 30. bbbbbbbb: PUSH4@17, imm 18, operand 24, dest 32. Note: "Inert bytecode with two dispatch-like branches, no ABI/runtime claim."
- LOG.md:262 (declaration): two `PUSH4/EQ/PUSH1/JUMPI` branches, distinct selectors, valid JUMPDEST offsets; pass = both pairs and no extra selector candidate. LOG.md:266–269 (result): 2/2, discovery unknown, ABI/mutability/runtime unverified. LEDGER.md:3,5 and reviewer.md:7–22 agree with my decode.
- Value-level disagreements: NONE. Caveats:
  D1 `payable`, `dispatch: abi`, `inferred_arguments: ""` are upstream inferences with no truth counterpart. No CALLVALUE (0x34) appears; a CALLDATALOAD/SHR prologue does. [INFERENCE] consistent with, not proof of, the ABI inference.
  D2 record `bytecodeOffset` / `bytecode_offset` has no label. "Destination" semantics come from LEDGER.md:5 and LOG.md:267; confirmed here only as JUMPDEST starts (V9).
  D3 record `authority: shipped-artifact` and locator `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/…` (same bytes; the `.shokunin/revenger/` root of LOG.md:264/267). Labels describe file class and locator, not origin (Q09).
  D4 LEDGER.md:5 names `npx -y rea-agents@6.4.0 …`; the record carries only `evmole@0.9.3`. Not verifiable from the record; not rerun.
  D5 r22 is silent on opcode-aware boundaries (V4). The immediate-decoy case is r24 (LOG.md:284–291), not checked here.

## Tooling, installs, files
- Installed: `uv venv /tmp/revenger-r61-ExecEvmOracleR22-10-venv` (interpreter reports Python 3.15.0) then `uv pip install pyevmasm` → pyevmasm 0.2.3 (PyPI). uv 0.13.0 pre-existing at ~/.local/bin/uv. Reason: third-party disassembler cross-check. Import emits SyntaxWarning at evmasm.py:492 (suppressed with -W ignore). No pacman or system transaction. `curl` and `git ls-remote` were read-only against public GitHub.
- Scratch (all under /tmp): xcheck.py 1158fdba1757b32c40009fe753370830f3aa88c25519ea4359bd1e5f1f7f9327 ; spec-harness.py 8cfefa6f9a804f44b271aaa2015d5a1d9d5b682858cc6ed468ffa256da5bdb21 ; spec-interp.py 98dc038e5b043eeacc4ca77c9fa014e81bcf7d1d1ffec38e25216e458417a067 (l.58 import, l.221 use of the routine) ; own.txt 30ed6c604c4d2c39d17862a2b77d87c4382947f5377ccc9b9d2e2eb1dd6cf7a7 ; pyevmasm.txt e45c225f82a4e7ed31b6bb565d622da0044bb208733ad7f783fa420e8c68eb62
- Lane writes: this report only. Lane git access: one `git clone` (read of the source) and one `git -C <lane> status --short -- <report>` (read intent; git may refresh the `.git/index` stat cache). No tracked content changed; not reverted.

VERDICT: r22 saved REA record matches an independent byte decode and the pinned spec on every checked value (2/2 pairs; dests 30/32 from PUSH4 at 7/17; digests; flags). r22 cannot test opcode-aware boundaries, evidence_id is not recomputable, and no lane file changed.
