# Round 20 — EVM selector/destination saved-Evidence verification

`python3 .shokunin/revenger/corpus/verify_evm_evidence.py --self-test` exited 0:

```
POSITIVE ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42 1/1 selector candidate and two digests; destination 16 != PUSH4 6; inferred only
NEGATIVE REJECTED candidate destination mismatch
```

Fixture carrier/decoded SHA-256, sizes, exact `PUSH4` selector bytes, comparison/jump and `JUMPDEST` are checked independently from authored `corpus/fixtures/evm-r19/fixture.hex` and `truth.json`. REA Evidence `ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42` is checked for matching artifact/bytecode identities, single raw/normalized selector candidate, reported destination offset 16 and the `PUSH1` operand byte pointing there, inference and runtime/discovery limits. Reviewer found the operand assertion missing in the first version; it was added and the self-test rerun before commit. In-memory altered normalized destination 6 (selector opcode offset) is rejected. This proves saved-record consistency, not a verified ABI signature or REA producer authenticity. No EVM execution or chain lookup.
