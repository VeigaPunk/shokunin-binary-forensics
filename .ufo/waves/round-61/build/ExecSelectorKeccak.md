# ExecSelectorKeccak — round 61, C09 selector check (RUNS, scratch only)

Base e0a4b0c4348ef1fade46539f520e94fa140c4d8a. Clone /tmp/revenger-r61-ExecSelectorKeccak: HEAD verified, `git status --porcelain` = 0 lines. Live lane read-only. Access date 2026-10-21. No REA producer call, no execution, no chain/RPC.

## 1. No fixture declares a function signature
- truth.json read for evm-r19, evm-r21..evm-r26 (no evm-r20 directory). Selector keys only: `selector_push4` (r19), `selector` (r21, r25), `branches[].selector` (r22), `push4_immediate` (r23). r24 has none.
- Authored disclaimer, corpus/fixtures/evm-r19/truth.json:10: "Inert authored bytecode, no ABI signature claim or execution; dispatch-like comparison only."
- Saved REA raw results carry selector, bytecodeOffset, `dispatch:"abi"`, `arguments:""`, `payable`. corpus/live/runs/round-19/LEDGER.md:7 lists "signature name" as UNKNOWN. Grep of corpus/live for signature/keccak/abi near a selector returns only REA's `"dispatch":"abi"` label (round-22 inspection.json).
- Consequence: keccak(signature)[:4] vs PUSH4 immediate is VACUOUS. deadbeef, aaaaaaaa, bbbbbbbb, c0ffee00 are AUTHORED CONSTANTS, not derived.

## 2. Keccak-256 vs SHA3-256 (independent implementation)
- Keccak: pycryptodome 4.1.0, Crypto.Hash.keccak digest_bits=256, Python 3.15.0, via `uv run --no-project --with pycryptodome`. SHA3: hashlib.sha3_256. Script sha256 04fd3b63…fc10.
- Vectors: the four selector examples on the Solidity ABI spec page (baz, bar, sam in "Examples"; f in "Use of Dynamic Types").

| signature | page selector | keccak256[:4] | sha3_256[:4] |
|---|---|---|---|
| baz(uint32,bool) | cdcd77c0 | cdcd77c0 match | af54f249 no |
| bar(bytes3[2]) | fce353f6 | fce353f6 match | 0f89aa98 no |
| sam(bytes,bool,uint256[]) | a5643bf2 | a5643bf2 match | cf3d9ff5 no |
| f(uint256,uint32[],bytes10,bytes) | 8be65246 | 8be65246 match | 41cc7909 no |

- Keccak 4/4, SHA3 0/4. keccak256('') = c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470; sha3_256('') = a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a.

## 3. Static walk, 51 declared claims, no execution
- Script sha256 f2a8be63…6d66 on clone fixtures: `SUMMARY static checks: 49/51 PASS`.
- FAIL r24 `embedded_pattern_offsets: [1, 9]` (corpus/fixtures/evm-r24/truth.json:10-13): bytes@9 = `570000000000000000`; pattern `63deadbeef14601057` occurs only at 1 (`found=[1]`). Truth defect; not edited here.
- Naive 0x63 byte scan of r24 = [1], inside PUSH32 immediate. Instruction-walk PUSH4 count = 0, matching truth `executable_push4_count: 0`.
- Saved REA destinations (r19/r21: 16; r22: 30/32) agree with the static walk.

| fixture | PUSH4 @ | immediate | PUSH1 operand @ (value) | JUMPI @ | destination | JUMPDEST |
|---|---|---|---|---|---|---|
| r19 | 6 | deadbeef 7-10 | 13 (0x10) | 14 | 16 | yes |
| r21 | 6 | deadbeef 7-10 | 13 (0x10) | 14 | 16 | yes (= r19 bytes) |
| r22 | 7 / 17 | aaaaaaaa 8-11 / bbbbbbbb 18-21 | 14 (30) / 24 (32) | 15 / 25 | 30 / 32 | yes / yes |
| r23 | 0 | c0ffee00 1-4 | none | none | none | n/a |
| r24 | none executable | 0x63 @1 is PUSH32 data | none | none | none | n/a |
| r25 | 7 | deadbeef 8-11 | 14 (16) | 15 | 16 | NO (STOP) |
| r26 | 7 | deadbeef 8-11 | 14 (17) | 15 | 17 | yes |

- r25 == 0x00 || r19 (checked). r26 differs from r25 at offset 14 only (0x10 to 0x11).

## 4. Verifier
- corpus/verify_evm_evidence.py has no keccak/sha3 code. Selector check is string equality to the authored constant (lines 51-52).
- Layout pinned to r19: `opcode+1 == immediate` and fixed EQ/PUSH1/JUMPI bytes (lines 32-35); `target == immediate + 9` and `decoded[immediate+6] == target` (lines 54-55). Fixture-layout check, not a general PUSH4/JUMPDEST detector.

## 5. Scope limits the C09 entry must state
1. Selector values are authored constants. No signature is declared or saved anywhere in the lane, so none is derived.
2. The Keccak-256 rule is verified against the spec's own vectors (section 2), not against any fixture.
3. PUSH4 value to function is inference. REA `dispatch:"abi"`, empty arguments and `payable` are upstream labels.
4. JUMPDEST at an instruction boundary is validity only, not reachability. Yellow Paper §9.4.3 is provisional S017 in ScribeSourcesRowsEvm.md; not re-opened here.
5. verify_evm_evidence.py pins the r19 layout.

## 6. First falsifiers (observed)
- F1 byte-scan candidate method: r24 yields 1 candidate, instruction walk yields 0. Falsified; use the instruction walk.
- F2 "PUSH1 operand names a destination" without a byte test: r25 operand 16 is STOP. Falsified; require 0x5b at an instruction boundary (r26 corrected to 17).
- F3 SHA3-256 as selector hash: 0/4 spec vectors. Any SHA3-based selector claim is falsified.
- F4 PUSH4-to-signature link: not falsifiable by fixtures (none declared); stays unknown.
- F5 r24 offset 9: declared occurrence absent; truth.json overstates. Do NOT patch in round 61 (editing corpus/fixtures voids the fixtures-unchanged hold in claims.md); record as residual, cite offset 1 only.

## 7. Sources (quoted, not admitted here)
- Solidity Contract ABI Specification, https://docs.soliditylang.org/en/latest/abi-spec.html, section "Function Selector", accessed 2026-10-21: "It is the first (left, high-order in big-endian) four bytes of the Keccak-256 hash of the signature of the function." (20 words). Revision: reader shows Remix example `version=0.8.38`; page label "Solidity 0.8.38-develop documentation" as recorded by ScribeSourcesRowsEvm.md §1 (not re-observed here).
- Same page, section "Examples": "This is derived as the first 4 bytes of the Keccak hash of the ASCII form of the signature" (19 words), for baz(uint32,bool) = 0xcdcd77c0.

## 8. Files
- Written: this report. Scratch: /tmp/revenger-r61-ExecSelectorKeccak-10/static_check.py (sha256 f2a8be63…6d66), keccak_vectors.py (sha256 04fd3b63…fc10). Clone unchanged. Live lane read-only. No messages sent. No subagents.

Installs: pycryptodome 4.1.0 via uv ephemeral env (uv 0.13.0, PyPI, reason: independent Keccak-256; no persistent install). No pacman or service change.
VERDICT: C09 selectors are authored constants (0 signatures in any truth.json); Keccak-256 matches 4/4 spec vectors and SHA3 0/4; static walk 49/51, r24 truth offset [1,9] is defective and must stay unpatched this round; entry admissible only with section 5 limits.
