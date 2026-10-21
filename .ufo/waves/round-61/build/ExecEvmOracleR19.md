# ExecEvmOracleR19 — independent byte oracle, evm-r19 (round 61, RUNS)

Seat CloseChousa26.ExecEvmOracleR19-10 · base e0a4b0c4348ef1fade46539f520e94fa140c4d8a · clone /tmp/revenger-r61-ExecEvmOracleR19 (HEAD verified; fixture, truth.json, record cmp-equal to live) · scratch /tmp/revenger-r61-ExecEvmOracleR19-scratch
No REA producer call, no EVM execution, no chain access, no live-lane write. verify_evm_evidence.py not opened or reused.
Axes: decode correctness (own walk + third-party cross-check) · field agreement (truth.json, saved record) · Q11 provenance · pre-registration wording vs result.

## 1. Independent decode
Carrier 39 B incl. trailing LF; decoded 18 B. Walk from offset 0 (11 instructions):
`0 PUSH1 00 · 2 CALLDATALOAD · 3 PUSH1 e0 · 5 SHR · 6 PUSH4 deadbeef · 11 EQ · 12 PUSH1 10 · 14 JUMPI · 15 STOP · 16 JUMPDEST · 17 STOP`
- PUSH4 sites: 1 — opcode 6, immediate 7–10 = deadbeef; followed by EQ, PUSH1, JUMPI (pattern true). Naive 0x63 byte scan: [6].
- JUMPI sites: 1 — offset 14; destination 16 (PUSH1 0x10 at 12); byte 0x5b = JUMPDEST; instruction start; not PUSH data (immediate bytes are 1, 4, 7–10, 13).
- JUMPDEST offsets: [16]. pyevmasm 0.2.3 `evmasm -d -bi` prints the same 11 offsets, names and operands.

## 2. Saved record and truth.json vs decode (record: corpus/live/runs/round-19/inspection.json)
| field | saved | independent | verdict |
|---|---|---|---|
| carrier sha256; artifact.bytes | 294e6fd2…827; 39 | same | MATCH |
| bytecode sha256; bytes; hex | d1086bce…723; 18; 60003560…5b00 | same | MATCH |
| raw / normalized selector | deadbeef / 0xdeadbeef | PUSH4 immediate | MATCH |
| raw bytecodeOffset; bytecode_offset | 16; 16 | JUMPI destination 16 | MATCH |
| bytecode_offset vs PUSH4 opcode offset | 16 | 6 | DIFF |
| bytecode_offset vs selector immediate offset | 16 | 7 | DIFF |
| truth: selector_push4; push4_opcode_offset; selector_immediate_offset; selector_immediate_length | deadbeef; 6; 7; 4 | same | MATCH |
| truth: decoded_size; decoded_sha256; carrier_sha256; encoding | 18; d1086bce…723; 294e6fd2…827; hex | same | MATCH |
| truth: any destination/JUMPDEST key | none (9 keys, Q7) | 16 | not carried |
| evidence_kind; confidence; authority | inferred; inferred; shipped-artifact | not byte-decidable | recorded |
| discovery_completeness; runtime_execution | unknown; not-performed | not byte-decidable | recorded |
| dispatch; inferred_arguments; mutability | abi; ""; payable | not byte-decidable | recorded |
| evidence_id | ev_0ad0097e…f42 | not re-derived (two canonical-JSON SHA-256 variants: no match) | recorded |

compare_r19.py: 22 rows = 20 MATCH (one is a presence check) + 2 DIFF. The DIFFs are expected: 16 is the destination, not the selector site.

## 3. Falsifier controls (in-memory mutants, scratch only; falsify_r19.py, abridged stdout)
base push4=[(6,'deadbeef')] jumpi=[(14,16,True)] accepts=True · M1 operand 0x10→0x11: jumpi=[(14,17,False)] accepts=False · M2 selector→cafebabe: accepts=False · M3 EQ→ISZERO: push4=[] accepts=False · M4 JUMPDEST→STOP: jumpi=[(14,16,False)] accepts=False · M5 r24-style decoy in PUSH32: naive_0x63=[1], push4=[], jumpi=[] accepts=False

## 4. Authored intent and disagreements
Authored to test (truth.json note): "Inert authored bytecode, no ABI signature claim or execution; dispatch-like comparison only." LOG.md:229 (CLAIM): one known PUSH4 selector constant in a dispatch-like comparison; AFTER holds only if Evidence "identifies the expected selector candidate at the corresponding byte offset".
- D1 (main): the saved candidate's offset is 16, which LOG.md:235 calls "destination, **not** selector byte offset"; the round-19 LEAF (corpus/live/runs/round-19/reviewer.md:13) concurs. The result still counts "Selector candidate 1/1 expected on this fixture" (LOG.md:235), "coverage improved narrowly" (LOG.md:236), and LEDGER.md:7 scores "1/1 expected selector byte candidate". The literal LOG.md:229 condition (selector at 6 or 7) is not met; the count rests on selector value plus destination 16. [INFERENCE: "corresponding" is not decidable from the files.]
- D2: truth.json carries no destination; 16 appears only in prose (LOG.md:234; LEDGER.md:3, 7). It is re-derived here (§1).
- D3: record subject.local_path and parameters.path = /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/evm-r19/fixture.hex. It exists and is byte-identical (cmp exit 0). LOG.md:231 and LEDGER.md:3 cite the repo-relative `.shokunin/revenger/...` path. Digests agree; paths do not.
- D4: field meaning not established upstream. https://github.com/cdump/evmole and https://pypi.org/project/evmole/ (grep only, accessed 2026-10-21) match `bytecodeOffset`/`bytecode_offset` only in code examples (grep lines 155, 179, 202, 235; 57, 81, 104, 137); no definition matched. Revision not shown in grep output.
- D5: the record has no selector→PUSH4 mapping; it exists only via truth.json and this decode.
- Guidance for any C09 entry: state REA's 16 as a destination derived from bytes (PUSH1 0x10 → JUMPDEST 0x5b), never as a selector location; this is n=1.

## 5. Q11 provenance (command → exact output)
Transcript: `bash /tmp/revenger-r61-ExecEvmOracleR19-scratch/q11.sh` (q11.sh sha256 76b07a46…2ba1b; stdout sha256 a085eac2…3c15e). F = clone fixture dir; R = round-19 dir.
- Q1 `sha256sum F/fixture.hex` → 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827; `wc -c` → 39; `od -An -v -tx1` → `30 78 36 30 30 30 33 35 36 30 65 30 31 63 36 33 / 64 65 61 64 62 65 65 66 31 34 36 30 31 30 35 37 / 30 30 35 62 30 30 0a`
- Q2 `python3 -B decode_r19.py F/fixture.hex` → `decoded bytes=18 sha256=d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 hex=60003560e01c63deadbeef14601057005b00`; `walk instructions=11`; `PUSH4 opcode_off=6 imm_off=7-10 selector=0xdeadbeef next=['EQ', 'PUSH1', 'JUMPI'] EQ_PUSH_JUMPI=True`; `JUMPI off=14 dest_push_off=12 dest=16 byte_at_dest=0x5b dest_is_instruction_start=True dest_is_JUMPDEST=True`; `JUMPDEST instruction-start offsets=[16]`; `naive byte 0x63 positions=[6]`
- Q3 `sha256sum decoded.bin` → d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 (equals truth decoded_sha256)
- Q4 `evmasm -d -bi -i decoded.bin` → `00000000: PUSH1 0x0` … `00000011: STOP` (11 lines, §1)
- Q5 `sha256sum R/inspection.json F/truth.json` → e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948 ; 789d41852c9a0538beceb00a5c1680ae87adfb6ba32063259c936a8523cf9fe5 ; `wc -c` → 4175 / 456 ; inspection.stderr → 0
- Q6 `compare_r19.py F/fixture.hex F/truth.json R/inspection.json` → 22 rows (§2); `VALUE operation=inspect_evm_interface predicate_type=rea.analysis`; `VALUE provider=evmole-interface version=evmole@0.9.3`; `VALUE evidence_id=ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42`; `VALUE discovery_completeness=unknown runtime_execution=not-performed`; `EVIDENCE_ID_TRY sorted_compact -> False`; `EVIDENCE_ID_TRY sorted_default -> False`
- Q6b same command, remaining VALUE lines: `VALUE evidence_kind=inferred confidence=inferred authority=shipped-artifact`; `VALUE dispatch=abi inferred_arguments='' inferred_state_mutability=payable raw_stateMutability=payable`; `VALUE bytecode kind=unknown deployment_authenticity=unknown hardfork=unknown digest_algorithm=sha256`; `VALUE limitations_count=6`
- Q7 truth.json keys → `['carrier_sha256', 'decoded_sha256', 'decoded_size', 'encoding', 'note', 'push4_opcode_offset', 'selector_immediate_length', 'selector_immediate_offset', 'selector_push4']`
- Q8 `sha256sum <prymeagnt fixture.hex>` → 294e6fd2…827; `cmp` vs F/fixture.hex → exit 0
- Q9 `git -C <clone> rev-parse HEAD` → e0a4b0c4348ef1fade46539f520e94fa140c4d8a; `cmp` live vs clone (fixture, truth, inspection.json) → exit 0 each
- Q10 `python3 -B -c` over LOG.md lines 227–236 and LEDGER.md line 1 (verbatim in transcript; LEDGER line 1 = "# Round 19 — authored EVM bytecode interface candidate")
- Q11 script sha256: decode_r19.py fde40fd001301331f9f931fb10784059eb70dfe77fbfb935531bee2222f00cee; compare_r19.py b7f77ab68bb73ac531292b84c7e0b8e7ae7eed2bb0029bff818130a8b5394ca4; falsify_r19.py 6ab7480058da37fd63a67fffee0feb5a83669c41037e8471979a1df6b38f6270
- Labels: values with no command above (kinds, discovery/runtime, dispatch/mutability, bytecode kind/hardfork, evidence_id, LOG/LEDGER prose) are "recorded", not re-derived.

## 6. Installs, environment, files
- `uv tool install pyevmasm` → pyevmasm 0.2.3 (+ future 1.0.0); channel uv→PyPI; reason: third-party EVM disassembler oracle. SyntaxWarning evmasm.py:492 on stderr; output unaffected.
- No other installs. `rz-asm -a evm` → "Unknown asm plugin 'evm'"; rizin/r2 list no EVM plugin; not used. No bun/node cross-check. Labrat not dispatched.
- Files written (scratch only; clone unchanged): decode_r19.py, compare_r19.py, falsify_r19.py, q11.sh, decoded.bin. This report is the only lane write.

VERDICT: Independent decode matches the saved r19 Evidence on every digest, size, the selector and JUMPDEST destination 16; bytecode_offset is the destination, not the PUSH4 offset (6) or immediate (7), so LOG.md:229's "corresponding byte offset" is not literally met and evidence_id is not re-derived.
