# Round 22 independent LEAF review — two-branch raw EVM fixture

Scope: round-22 declaration in `LOG.md`, `corpus/fixtures/evm-r22/{fixture.raw,truth.json}`, saved `corpus/live/runs/round-22/{inspection.json,inspection.stderr,LEDGER.md}`, and round-19 fixture/inspection/ledger baseline. I independently hashed and decoded the local bytes; I did not rerun REA, execute EVM bytecode, or query a chain.

## Fixture and positions

`fixture.raw` is exactly 34 bytes, `60003560e01c8063aaaaaaaa14601e578063bbbbbbbb14602057000000005b005b00`; its independently computed SHA-256 is `94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2`. Both length and digest match `truth.json`. This is a raw carrier: carrier and decoded bytecode are the same bytes and therefore have the same SHA-256, unlike round 19's hex-text carrier and decoded bytes.

Zero-based offsets, checked directly from the byte sequence:

| branch | selector opcode/immediate | comparison/jump | destination |
| --- | --- | --- | --- |
| A | `PUSH4` `0x63` at 7; `aa aa aa aa` at 8–11 | `EQ` `0x14` at 12; `PUSH1` `0x60` at 13, operand `0x1e` at 14; `JUMPI` `0x57` at 15 | `JUMPDEST` `0x5b` at decimal 30 (`0x1e`) |
| B | `PUSH4` `0x63` at 17; `bb bb bb bb` at 18–21 | `EQ` at 22; `PUSH1` at 23, operand `0x20` at 24; `JUMPI` at 25 | `JUMPDEST` at decimal 32 (`0x20`) |

The two `DUP1` bytes occur at 6 and 16, padding `STOP` bytes at 26–29, and destination-adjacent `STOP` bytes at 31 and 33. The immediate values of each `PUSH1` point to their respective `JUMPDEST` bytes. These are static byte observations, not evidence that either branch executed or was reachable in a deployed contract.

## Saved REA Evidence and claim limits

Saved Evidence `ev_24fe0001213ec58a588d086e0fe55677d749f3eb6998afe6ee6095ff9dc4af4b` records `inspect_evm_interface`, provider `evmole-interface` (`evmole@0.9.3`) and explicit `encoding=raw` for this fixture path. Its subject SHA-256, normalized artifact SHA-256/34-byte size, and normalized bytecode SHA-256/34-byte size equal the independent raw digest; normalized bytecode hex equals the independently decoded bytes. Raw result has exactly `aaaaaaaa → bytecodeOffset 30` and `bbbbbbbb → bytecodeOffset 32`; normalized result has exactly `0xaaaaaaaa → bytecode_offset 30` and `0xbbbbbbbb → bytecode_offset 32`. Both raw and normalized pairs match the distinct fixture selector/destination pairs, with no extra *reported* candidate. Offsets 30/32 are jump destinations, not the `PUSH4` opcode offsets 7/17 or selector immediate starts 8/18; REA gives no separate selector-location provenance. Saved stderr is empty; the ledger states exit 0, which I did not independently reproduce.

REA marks `evidence_kind=inferred`, `confidence=inferred`, `discovery_completeness=unknown`, `runtime_execution=not-performed`, and bytecode kind, deployment authenticity and hardfork `unknown`. `dispatch=abi`, empty argument strings and `payable` are upstream inferences, not verified ABI signatures/names, parameter types, mutability, actual callable dispatch, or runtime behavior. A 2/2 authored-pair match here does not establish whole-interface recall or producer authentication.

## Verdict against declared depth move

**Depth improved narrowly:** round 19 preserved one `0xdeadbeef → 16` candidate on an 18-byte decoded hex carrier; this saved 34-byte raw fixture distinguishes both expected selector→destination pairs (2/2), with no extra candidate in this result. **Coverage unchanged as the targeted axis:** the provider-neutral `inspect_evm_interface` raw route was already exercised in round 21. **Calibration unchanged:** correct byte/identity and inference boundaries are preserved, without a distinct calibration improvement. Accept only fixture-scored static candidate discrimination; no runtime or verified ABI claim. The round-22 ledger and declaration respect this boundary.
