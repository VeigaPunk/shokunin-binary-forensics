# Round 25 independent LEAF review — entry STOP fixture

Scope: r25 declaration in `LOG.md`; `corpus/fixtures/evm-r25/{fixture.raw,truth.json}`; saved `corpus/live/runs/round-25/{inspection.json,inspection.stderr,LEDGER.md}`; r19 fixture and saved baseline. I decoded and hashed bytes locally. I did not rerun REA, execute bytecode, or query a chain.

## Byte truth and confound

The raw fixture is 19 bytes, hex `0060003560e01c63deadbeef14601057005b00`, SHA-256 `2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7`. These match `truth.json` and the saved Evidence. Bytes 1–18 exactly equal r19's decoded 18 bytes (`60003560e01c63deadbeef14601057005b00`), but prepending a byte shifted every opcode offset without changing the immediate jump operand.

Zero-based instruction positions are: `STOP` **0**; `PUSH1 00` 1–2; `CALLDATALOAD` 3; `PUSH1 e0` 4–5; `SHR` 6; `PUSH4 deadbeef` opcode **7**, immediate **8–11**; `EQ` 12; `PUSH1 10` **13–14**; `JUMPI` 15; `STOP` **16**; `JUMPDEST` **17**; `STOP` 18. The `PUSH1 0x10` operand denotes decimal **16**, the `STOP`, **not** the `JUMPDEST` at 17. In r19, the same operand denoted the `JUMPDEST` at 16, and saved REA reported one inferred `deadbeef` candidate with destination offset 16. In r25, `truth.json`'s `destination_offset: 17` identifies the shifted `JUMPDEST` byte, not the destination actually encoded by the unchanged jump operand. The declaration's “valid jump destination” premise is therefore false.

## Saved REA observation and boundary

Saved `inspection.json` records Evidence `ev_23a9464bf2d8c3de3614176efa53016f002ddade19f1ae842b4325ba2d095579`, operation `inspect_evm_interface`, provider `evmole-interface` (`evmole@0.9.3`), and `encoding=raw`. Subject digest, normalized artifact SHA/19-byte size, and normalized bytecode SHA/19-byte size/hex all equal the independently checked raw fixture. Both `raw_result.functions` and `normalized_result.functions` are empty; stderr is empty. The ledger reports command exit 0, not independently rerun here. Evidence states `discovery_completeness=unknown` and `runtime_execution=not-performed`.

Relative to r19's one reported candidate, this particular changed fixture reports none. Its entry `STOP` and its invalid encoded jump destination coexist. The empty output cannot attribute suppression to either change, establish REA's reachability or jump-validation mechanism, prove absence of callable interfaces, or establish runtime behavior. The ledger explicitly identifies this confound and does not claim a detector cause.

## Verdict against declaration

**Calibration unchanged:** the declared isolated entry-STOP reachability test is confounded by the stale `PUSH1 0x10` operand, so its specified improvement is not demonstrated. The ledger's correction is accurate but not independent evidence of a successful calibration move. **Depth unchanged; coverage unchanged:** no new semantic confirmation or route. Admit only byte identity and the empty-candidate observation for this exact confounded fixture; make no causal claim.
