# ExecEvmOracleR21 — round 61 RUNS: independent byte oracle, fixture evm-r21 (C1/C09)

Seat `CloseChousa26.ExecEvmOracleR21-10` (executor, RUNS, read-only). Placeholders: `L`=/home/vgpnk/Projects/shokunin/revenger-shokunin, `B`=/tmp/revenger-r61-ExecEvmOracleR21 (private clone, branch r61-ExecEvmOracleR21), `S`=/tmp/revenger-r61-ExecEvmOracleR21-scratch.
Base observed: `git -C B rev-parse HEAD` → `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`. Clone left unedited (no patch). Lane writes: this report only.
Not run (scope): REA producer or `xd://mcp__rea_*`, bytecode execution, chain/RPC, subagents (labrat unused). Not opened: `corpus/verify_evm_evidence.py`, other seats' /tmp decode scripts.
Record present: `L/corpus/live/runs/round-21/inspection.json` (one line; Evidence `ev_4810eda7…`; `"operation":"inspect_evm_interface"`). No absence finding.

## Result
- OBS: 18 bytes decode to 11 instructions. One `PUSH4 deadbeef` (pc 6, imm pcs 7–10), then `EQ`@11, `PUSH1 0x10`@12, `JUMPI`@14. JUMPI dest 16 is byte `0x5b`, an instruction start, not in push data: one valid candidate.
- OBS: record vs oracle: 15/15 checked fields match, 0 mismatch (3 identity, 12 byte-derived: digests, sizes, hex, candidate count, selector, offset). `bytecode_offset` 16 is the JUMPDEST destination, not PUSH4 pc 6.
- OBS: no value disagreement among oracle, record, truth.json, LOG.md, LEDGER.md, reviewer.md. Disagreements are citation, label or locator only (D1–D5).
- INF: `inferred`, `dispatch=abi`, `payable`, empty arguments fit the bytes (one CALLDATALOAD at pc 2, argument 0; zero CALLVALUE) but are not proven.

## Q11 provenance block (command → exact output)
Q1 `sha256sum corpus/fixtures/evm-r21/fixture.raw` (cwd L) → `d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723`; `wc -c` → `18`.
Q2 `od -An -v -tx1 corpus/fixtures/evm-r21/fixture.raw` → `60 00 35 60 e0 1c 63 de ad be ef 14 60 10 57 00` / `5b 00`.
Q3 blob parity, 9 paths (brace-expanded): `git -C B ls-tree e0a4b0c4348ef1fade46539f520e94fa140c4d8a -- corpus/fixtures/{evm-r21/fixture.raw,evm-r21/truth.json,evm-r19/fixture.hex,evm-r19/truth.json} corpus/live/runs/round-21/{inspection.json,LEDGER.md,reviewer.md,inspection.stderr} corpus/live/runs/round-19/inspection.json` equals `git -C B hash-object --no-filters` on the same live paths, pairwise. fixture.raw `d7790fc2e06cc86f5dc7797cfcd3e59b783eb0f8`; inspection.json `a0eb23bd2a5103bc4c61da315c9459157cb05858`; inspection.stderr `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391` (empty blob). Committed base copy (`git show e0a4…:corpus/fixtures/evm-r21/fixture.raw > S/base-r21-fixture.raw`) sha256 `d1086bce…723`.
Q4 `python3 -B S/evm_oracle.py L/corpus/fixtures/evm-r21/fixture.raw --record L/corpus/live/runs/round-21/inspection.json --insns-out S/insns-live.txt --selftest` (python3 3.14.8; script sha256 `b59b9a9f793362f140f4ae62f95cfdf3ccdaac6f13a9c57c791f4f68edcf6dc0`; full stdout 53 lines, sha256 `25e2c4bbb1fc831aca00a77e11f0260e1a9508f49263e2fc492d4e1edc9ccfa4`):
   insn: `0 PUSH1 00 | 2 CALLDATALOAD | 3 PUSH1 e0 | 5 SHR | 6 PUSH4 deadbeef | 11 EQ | 12 PUSH1 10 | 14 JUMPI | 15 STOP | 16 JUMPDEST | 17 STOP`
   `sweep: insns=11 covered_bytes=18 truncated_pushes=0 unassigned_pcs=[]`; `push_data_pcs=[1, 4, 7, 8, 9, 10, 13]`
   `push4 pc=6 imm=deadbeef imm_pcs=7-10`
   `candidate selector=deadbeef push4_pc=6 eq_pc=11 push_pc=12 push_imm=10 jumpi_pc=14 dest=16 dest_byte=0x5b dest_insn_start=True dest_in_push_data=False valid_jumpdest=True`
   `jumpi pc=14 prior=PUSH1@12 dest=16 dest_byte=0x5b dest_insn_start=True dest_in_push_data=False valid_jumpdest=True`
   `counts: push4=1 eq_push_jumpi_candidates=1 jumpi=1 calldataload=[{'pc': 2, 'offset': 0}] callvalue=0`
   `naive_byte_scan op=0x63 pcs=[6] inside_push_data=[]`; `op=0x57 pcs=[14] inside_push_data=[]`; `op=0x5b pcs=[16] inside_push_data=[]`
Q5 `uv run --no-project --with pyevmasm python -B S/pyevmasm_cross.py L/corpus/fixtures/evm-r21/fixture.raw > S/insns-pyevmasm.txt` → stderr `pyevmasm=0.2.3`; `diff S/insns-live.txt S/insns-pyevmasm.txt && echo SAME_ORACLE_VS_PYEVMASM` → `SAME_ORACLE_VS_PYEVMASM` (11 lines each). Base copy vs live → `SAME_LIVE_VS_BASE_COPY`.
Q6 `--record` output: `15 MATCH / 0 MISMATCH`: operation `inspect_evm_interface`; parameters.encoding `raw`; subject.name `fixture.raw`; subject.digest, artifact.sha256, bytecode.sha256 `d1086bce…723`; artifact and bytecode bytes 18; bytecode.hex `60003560e01c63deadbeef14601057005b00`; functions count 1/1; raw `deadbeef`/`bytecodeOffset` 16; normalized `0xdeadbeef`/`bytecode_offset` 16. `NOTE record offset 16 == JUMPI dest; PUSH4 pc is 6 (equal: False)`.
Q7 `jq -c '.normalized_result | {evidence_kind, discovery_completeness, runtime_execution, artifact_sha256: .artifact.sha256, bytecode: {sha256: .bytecode.sha256, bytes: .bytecode.bytes, kind: .bytecode.kind, hardfork: .bytecode.hardfork, deployment_authenticity: .bytecode.deployment_authenticity}, functions}' inspection.json` → `{"evidence_kind":"inferred","discovery_completeness":"unknown","runtime_execution":"not-performed","artifact_sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723","bytecode":{"sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723","bytes":18,"kind":"unknown","hardfork":"unknown","deployment_authenticity":"unknown"},"functions":[{"selector":"0xdeadbeef","bytecode_offset":16,"dispatch":"abi","inferred_arguments":"","inferred_state_mutability":"payable"}]}`. Top-level `confidence` `inferred`, `authority` `shipped-artifact`. Oracle byte facts: `extra_calldata_word_reads=0`, `callvalue_count=0`.
Q8 evidence_id `ev_4810eda7b540fbf2d4265c0f9deb3886dc009945cb77276b980f5502112cfc85`; identical string at LOG.md:256, round-21/LEDGER.md:5, round-21/reviewer.md:6 (grep). Four canonical-JSON SHA-256 attempts over the record minus evidence_id (sorted/insertion × compact/default): 0/4 equal. NOT REPRODUCED; scheme UNKNOWN; treated as opaque.
Q9 r19 hex parity: `python3 -B -c "import hashlib; h=open('L/corpus/fixtures/evm-r19/fixture.hex','rb').read(); d=bytes.fromhex(h.decode('ascii').strip()[2:]); r=open('L/corpus/fixtures/evm-r21/fixture.raw','rb').read(); print(len(h), hashlib.sha256(h).hexdigest()); print(len(d), hashlib.sha256(d).hexdigest()); print(len(r), hashlib.sha256(r).hexdigest(), d==r)"` → `39 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827` / `18 d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723` / `18 d1086bce…723 True`.
Q10 `--selftest` → `SELFTEST passes=5/5`: base (one candidate, dest 16 valid); m1 dest 17 = `0x00` rejected; m2 JUMPDEST byte inside PUSH4 immediate rejected; m3 EQ→ADD no candidate; m4 JUMPI→JUMP no candidate.
Q11 decoy file `S/m2-jumpdest-in-push4.raw` (`printf`; sha256 `41c92eba438786ab5c06081463de1aca682ed68162bbf28ee79b1531fc744bd6`; 18 bytes): oracle `candidate selector=5badbeef push4_pc=6 … dest=7 dest_byte=0x5b dest_insn_start=False dest_in_push_data=True valid_jumpdest=False`; naive `op=0x5b pcs=[7, 16] inside_push_data=[7]`; pyevmasm stream identical (`SAME_M2_ORACLE_VS_PYEVMASM`).
Q12 `jq -c . corpus/fixtures/evm-r21/truth.json` → `{"raw_sha256":"d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723","raw_bytes":18,"source_hex_fixture":"../evm-r19/fixture.hex","selector":"deadbeef","destination_offset":16,"note":"Raw bytes are byte-identical to r19 decoded hex; no execution."}`; `jq -c . corpus/fixtures/evm-r19/truth.json` → `{"carrier_sha256":"294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827","decoded_sha256":"d1086bce…723","decoded_size":18,"encoding":"hex","selector_push4":"deadbeef","push4_opcode_offset":6,"selector_immediate_offset":7,"selector_immediate_length":4,"note":"Inert authored bytecode, no ABI signature claim or execution; dispatch-like comparison only."}`.

## Authored to test (truth.json, LOG.md)
- LOG.md:250–251 (declaration): REA `raw` carrier parity against r19 hex bytes. Success = carrier and decoded SHA equal raw bytes, one expected candidate, destination 16, "without claiming ABI semantics".
- LOG.md:256 (result): "Authored … the exact 18 decoded bytes of r19 fixture.hex". LOG.md:258: coverage "improved narrowly … Admit only raw carrier support."
- So r21 tests carrier-encoding parity only. Its truth has no decoy, no negative control, no completeness claim, and no PUSH4 offset field.

## Disagreements and observations (none in values)
D1 LOG.md:234 (r19 entry) cites `corpus/fixtures/evm-r19/{fixture.hex,truth.json}` for "`JUMPDEST` offset 16". The r19 truth.json (Q12) has no destination field. The 16 is in r21 truth.json and matches the bytes. Citation error only.
D2 round-21/LEDGER.md:5 calls "PUSH4 opcode offset 6 and immediate 7–10" fixture truth. r21 truth.json has no such field; r19 truth.json does (`push4_opcode_offset":6`, `selector_immediate_offset":7`, length 4). Locator split: r21 gives destination, r19 gives PUSH4. round-21/reviewer.md:5 "both truth.json files agree" holds only on shared fields.
D3 round-21/inspection.json:1 `"authority":"shipped-artifact"` labels an authored synthetic fixture (LOG.md:256 "Authored"). Producer label overstates provenance.
D4 inspection.json:1 locator `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/evm-r21/fixture.raw` is outside the lane. `sha256sum` on it → `d1086bce…723`, digest-identical. Only the bytes are reproducible here, not the locator.
D5 inspection.json:1 `bytecode.sha256` is SHA-256 of the 18 bytes; the record's own limitation says it is not the Ethereum Keccak code hash. C09 must not call it a code hash.

## Gaps and first falsifiers
G1 r21 has no JUMPDEST-in-push decoy (its only `0x5b` is pc 16, Q4). So r21 cannot falsify the "not inside push data" clause. The Q11 mutant is the falsifier; REA on it is untested (producer call out of scope).
G2 `payable`, empty arguments and `dispatch=abi` remain unproven: the bytes show only absence of CALLVALUE and one selector calldata read.
G3 `discovery_completeness`, `hardfork`, `bytecode.kind` stay UNKNOWN; this oracle derives nothing for them.

Installs: pyevmasm 0.2.3 via `uv run --with pyevmasm` (PyPI through uv; cached ephemeral env, not a system install; reason: third-party disassembler cross-check). No pacman or system changes.

VERDICT: Independent bytes-only oracle agrees with the saved r21 record on every checked value (one PUSH4 candidate; destination 16 is a JUMPDEST); r21 tests raw-carrier parity only and cannot back C09 decoy or completeness claims.
