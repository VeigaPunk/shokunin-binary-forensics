# Round 19 independent LEAF review — authored EVM hex interface candidate

Scope: read the round-19 declaration, `fixture.hex`, `truth.json`, saved `inspection.json`, empty `inspection.stderr`, and `LEDGER.md`. I decoded and hashed the local fixture independently. I did not rerun REA, execute EVM bytecode, or query a chain.

## Independent byte checks

- Carrier is exactly 39 bytes: `0x60003560e01c63deadbeef14601057005b00\n`; SHA-256 `294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827`.
- Removing the `0x` prefix and trailing newline and decoding hex gives 18 bytes, `60003560e01c63deadbeef14601057005b00`; SHA-256 `d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723`. Both hashes and length match `truth.json`, REA's normalized artifact/bytecode identities, and the ledger. The carrier SHA is not a Keccak code hash.
- Zero-based decoded offsets: `PUSH1 00` at 0–1, `CALLDATALOAD` at 2, `PUSH1 e0` at 3–4, `SHR` at 5, `PUSH4` opcode `63` at **6**, its immediate `de ad be ef` at **7–10**, `EQ` at 11, `PUSH1 10` at 12–13, `JUMPI` at 14, `STOP` at 15, `JUMPDEST` at **16**, `STOP` at 17. This supports the authored dispatch-like comparison bytes, not execution or ABI semantics.

## Saved inspection and claim boundary

`inspection.json` has Evidence ID `ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42`, `predicate_type=rea.analysis`, `operation=inspect_evm_interface`, provider `evmole-interface` (`evmole@0.9.3`), and explicit parameter `encoding=hex`. The saved raw result lists one `selector=deadbeef`, `bytecodeOffset=16`; normalized result lists one `selector=0xdeadbeef`, `bytecode_offset=16`, `dispatch=abi`, `inferred_arguments=""`, `inferred_state_mutability=payable`. Offset **16** matches the independently decoded **jump destination**, *not* the `PUSH4` opcode offset 6 or immediate start 7. REA does not report a separate opcode/immediate offset: the mapping of this candidate to the authored `PUSH4` is a comparison with fixture truth, not precise selector-location provenance supplied by REA. The ledger correctly distinguishes these positions and bounds the claim. Saved stderr is empty; the exit-0 command claim is recorded in the ledger, not independently rerun here.

The evidence is explicitly `evidence_kind=inferred` and `confidence=inferred`; `discovery_completeness=unknown`, `runtime_execution=not-performed`, `kind=unknown`, `deployment_authenticity=unknown`, and `hardfork=unknown`. Candidate `dispatch=abi`, empty arguments, and `payable` are upstream inferences, not verified ABI names, signatures, argument types, mutability, deployed status, complete discovery, or runtime behavior. Neither the evidence nor this review supplies a chain lookup or execution result.

## Verdict against declared move

**Coverage improved narrowly:** this is a new saved `inspect-evm-interface` route on an explicit authored hex carrier with both identities preserved and 1/1 expected selector candidate matching `deadbeef`; its reported destination offset 16 agrees with the authored `JUMPDEST`. **Depth unchanged:** no deeper semantic or execution finding. **Calibration unchanged:** the ledger preserves the key byte-offset and inference limits, but no separate calibration move is demonstrated. Admit only this fixture-scored route coverage; do not interpret the `bytecode_offset` as selector provenance or the candidate as a verified ABI signature.
