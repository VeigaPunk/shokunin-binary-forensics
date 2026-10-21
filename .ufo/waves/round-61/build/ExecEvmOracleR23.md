# ExecEvmOracleR23 — round 61 RUNS: independent byte oracle for fixture evm-r23 (C09 / C1)

Seat `CloseChousa26.ExecEvmOracleR23-10` (scratch name `ExecEvmOracleR23`). Base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`, observed as clone HEAD; clone `/tmp/revenger-r61-ExecEvmOracleR23` clean (`git status --porcelain` empty). Read-only: no REA call, no bytecode execution, no chain/RPC, no labrat (leaf seat; no spawn tool granted). Order: the saved record was read before the walker ran; the walker takes bytes plus the opcode table only. `verify_evm_evidence.py` was not opened.

## 1. Identities (lane file == clone file, `cmp`)
- fixture `corpus/fixtures/evm-r23/fixture.raw`: 7 B, sha256 `8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a`
- `corpus/fixtures/evm-r23/truth.json`: sha256 `ea28d73d41da19b7285224160327e27cf1655e5fa434259389a847535692a91e`
- record `corpus/live/runs/round-23/inspection.json` = the only `inspect_evm_interface` record in round-23 (Evidence `ev_296e7ed7…f77201`, inspection.json:1): 3923 B, sha256 `ce9fe51536af461ef2deb19b8cf8ff3582dba736abc2747b07ab845d3aaac2af`. `inspection.stderr` 0 B.
- Locator: record `subject.local_path` and `parameters.path` name `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/…`. That prefix is a symbolic link (`stat -c %F`); `readlink -f` gives `/home/vgpnk/Projects/shokunin/revenger-shokunin`, the same tree.

## 2. Oracle on r23 (bytes `63 c0 ff ee 00 50 00`)
- PUSH4 @0, immediate @1–4 = `c0ffee00`. The only `0x63` byte in the file is at offset 0, so 0 is the only possible PUSH4 offset.
- POP @5; STOP @6; no further instructions. The opcode after PUSH4 is POP, not EQ, so the EQ/PUSH/JUMPI pattern is absent. No JUMPI, so no destinations; no JUMPDEST.
- No `0x14` (EQ), `0x56` (JUMP), `0x57` (JUMPI) or `0x5b` (JUMPDEST) byte anywhere: comparison_or_jump = false, matching truth.json.
- Expected: functions `[]`; raw PUSH4 candidates = 1 (@0, `c0ffee00`), no destination.
- A naive linear decode would read `0xff` (SELFDESTRUCT, spec L213) at offset 2 and `0x00` (STOP) at offset 4, both inside the immediate. The walker skips them.
- Second decoder pyevmasm 0.2.3 agrees: `pc=0 name=PUSH4 operand=0xc0ffee00 size=5`, `pc=5 POP`, `pc=6 STOP`.

## 3. Saved record vs oracle
- functions: raw_result and normalized `[]` = oracle `[]`. Agree.
- selectors / bytecode_offset: no such key in the record (key-path search returns `[]`). N/A, nothing to compare.
- evidence_kind `inferred`; discovery_completeness `unknown` (conservative: the walk covers 7/7 bytes); runtime_execution `not-performed` (static only). Consistent.
- evidence_id `ev_296e7ed7…f77201`: 8 plain canonical forms of the record, 0/8 match. Recorded, NOT re-derived. Same ID at LOG.md:278, LEDGER.md:5, reviewer.md:6, inspection.json:1.
- Digests: subject, artifact and bytecode sha256 all `8047ddff…` = sha256(7 bytes). bytecode.hex `63c0ffee005000` = bytes. Sizes 7/7. diagnostics.stderr `""` = empty file. Agree.

## 4. Oracle self-checks (not vacuous)
- r19 `fixture.hex` (carrier sha `294e6fd2…`, decoded 18 B `d1086bce…`): PUSH4 `deadbeef`@6, EQ@11, PUSH1 0x10@12, JUMPI@14, dest 16 = JUMPDEST. truth.json: push4_opcode_offset 6, immediate @7 len 4.
- r22 raw (sha `94c1790f…`, 34 B; truth sha `99aba01a…`): `aaaaaaaa`@7 → dest 30 JUMPDEST; `bbbbbbbb`@17 → dest 32 JUMPDEST = truth destination_offset 30/32.
- Saved r22 record: raw `bytecodeOffset` 30, 32; normalized `bytecode_offset` 30, 32. REA's bytecode_offset is the JUMPDEST destination, not the PUSH4 offset (7/17), as LOG.md:235 records for r19.
- Mutants (scratch, in memory, nothing saved): m1 = r19 with byte 16 → STOP: dest_is_jumpdest false. m2 = r23 + `14 60 10 57` + JUMPDEST@16: pattern found, dest 16 JUMPDEST true. m3 = m2 with 16 → STOP: false. m4 = `63c0ffee00 14 600a 57 605b 00`: dest 10 holds `0x5b`, but dest_is_instruction_start false (inside PUSH1 immediate), so dest_is_jumpdest false.

## 5. Q11 provenance block (exact command ⇒ exact output)
Runner `/tmp/revenger-r61-ExecEvmOracleR23-run.sh` (sha `6714b2ce…`) traces every command with `set -x`. Output `/tmp/revenger-r61-ExecEvmOracleR23-out/run2.txt` (sha `b669b441…`); run1 and run2 are byte-identical.
- `sha256sum …/evm-r23/fixture.raw` ⇒ `8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a`
- `xxd -g1 …/evm-r23/fixture.raw` ⇒ `00000000: 63 c0 ff ee 00 50 00 c....P.`
- `python3 oracle.py fixture.raw | jq -c …` ⇒ instructions `[PUSH4 @0 imm c0ffee00, POP @5, STOP @6]`; push4_raw_candidates `[{pc:0,imm:"c0ffee00"}]`; selector_pattern_EQ_PUSH_JUMPI `[]`; jumpdest_instruction_pcs `[]`; comparison_or_jump_instruction_pcs `[]`; naive `0x63_PUSH4 [0]`, `0x14/0x57/0x5b/0x56 []`
- `pyevmasm.py 63c0ffee005000` ⇒ `pc=0 name=PUSH4 operand=0xc0ffee00 size=5` / `pc=5 name=POP` / `pc=6 name=STOP`
- `jq '{evidence_id, operation, authority, confidence, provider, raw_result, normalized_functions, evidence_kind, discovery_completeness, runtime_execution, diagnostics}' inspection.json` ⇒ `"evidence_id":"ev_296e7ed7…f77201"`, `"operation":"inspect_evm_interface"`, `"authority":"shipped-artifact"`, `"confidence":"inferred"`, `"provider":"evmole@0.9.3"`, `"raw_result":{"functions":[]}`, `"normalized_functions":[]`, `"evidence_kind":"inferred"`, `"discovery_completeness":"unknown"`, `"runtime_execution":"not-performed"`, `"diagnostics":{"stdout":"","stderr":"","truncated":false}`
- `jq '[paths|…]|select(test("offset|selector|candidate|argument|mutab"))' inspection.json` ⇒ `[]`
- `evid.py inspection.json` ⇒ `recorded ev_296e7ed7…`; `file_bytes_sha256 ce9fe515…`; `matches 0/8`
- `readlink -f …/prymeagnt/revenger/.shokunin/revenger` ⇒ `/home/vgpnk/Projects/shokunin/revenger-shokunin`
- `printf 63c0ffee005000 | xxd -r -p | sha256sum` ⇒ `8047ddff…`; `printf '%s' 63c0ffee005000 | sha256sum` ⇒ `90e1ede5…` (text digest, not the identity)
- `cmp` lane vs clone, fixture and record ⇒ equal
- `sha256sum execspecs…/instructions/__init__.py` ⇒ `6803bc7d…`; `_grep` opcode lines: `EQ = 0x14` L55, `STOP = 0x00` L103, `JUMPI = 0x57` L105, `JUMPDEST = 0x5B` L108, `POP = 0x50` L117, `PUSH4 = 0x63` L124, `SELFDESTRUCT = 0xFF` L213
- Scratch sha256: oracle `ce0307bf…`, evid `81b9e6ed…`, pyevmasm `15dc2937…`, mutants `79afe85d…`

## 6. What r23 was authored to test
- truth.json: push4_opcode_offset 0; push4_immediate `c0ffee00`; opcodes `[PUSH4,POP,STOP]`; comparison_or_jump false; "Inert negative fixture; no dispatch syntax, execution or ABI claim."
- LOG.md:272 BEFORE: no authored control tests whether a bare PUSH4 without comparison/jump is promoted. LOG.md:273 CLAIM: improves only if zero candidates with discovery unknown, checked against opcode truth. LOG.md:280: "Admit fixture-scoped calibration only."
- LOG.md:283 (r24 BEFORE) concedes r23 did not test opcode-looking bytes inside immediate data.

## 7. Disagreements and caveats (no byte-level disagreement)
1. Label: record `authority: "shipped-artifact"` for an authored synthetic fixture (LEDGER.md:3: "authored negative control, not representative contract code"). Do not cite it as shipped-artifact evidence.
2. Version: LEDGER.md:5 invocation `rea-agents@6.4.0`; record provider `evmole@0.9.3`; SOURCES.md:16 (S002) names `rea-agents@6.7.0` as the installed pin. Wrapper version and "exited 0" are ledger-only (reviewer.md:6 agrees they are unauthenticated).
3. The record carries only `functions=[]`, no per-PUSH4 diagnostics. Empty output cannot separate "not scanned" from "scanned and rejected".
4. r23 has no `0x14/0x56/0x57/0x5b` byte, so it does not separate a pattern-requiring detector from a naive one. It falsifies only "bare PUSH4 promoted". m2 is the minimal flip.
5. evidence_id is a recorded identity only.

## 8. Sources opened (access 2026-10-21)
- ethereum/execution-specs `src/ethereum/forks/cancun/vm/instructions/__init__.py` (raw.githubusercontent, master). Revision: last commit to this path `4ac7a9ba5c545487cd6fbebbabbd16779f25cbf9`, committer date 2025-09-25T10:03:48Z (GitHub API); file sha256 `6803bc7d…`. Section `class Ops(enum.Enum)`; quoted lines `EQ = 0x14`, `JUMPI = 0x57`, `JUMPDEST = 0x5B`, `PUSH4 = 0x63`. Tier A for opcode byte values. Not yet a SOURCES.md row.
- evm.codes homepage: opened; no opcode table in extracted text; unused.

## 9. Next falsifier, installs, files
- Not run (needs a new fixture and an REA call, outside RUNS): bare PUSH4 + `EQ; PUSH1 d; JUMPI` with d inside a PUSH immediate (m4 shape); expect no destination.
- Install: pyevmasm 0.2.3 via uv 0.13.0 (`uv venv` + `uv pip install` into `/tmp/revenger-r61-ExecEvmOracleR23-venv`, system Python 3.14.8). Reason: independent second decoder. Harmless SyntaxWarning at pyevmasm `evmasm.py:492` on import. No system package change.
- Lane writes: this report only. Scratch: `/tmp/revenger-r61-ExecEvmOracleR23-*`. Clone unchanged.

VERDICT: the saved r23 REA record matches the independent oracle on every checkable field (functions [], digests, 7 bytes, empty stderr, labels) with no byte disagreement; r23 supports only bare-PUSH4 non-promotion; caveats: authority label, rea-agents pin drift, evidence_id not re-derived. Installed: pyevmasm 0.2.3 via uv (scratch venv only).
