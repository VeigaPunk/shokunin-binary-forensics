# Round 61 — EVM verifier mutation sensitivity
Axis: calibration; supporting scope: C09 coverage; hold: exact byte restoration. RUNS-only; no production edits.
Observed clone base: `git -C /tmp/revenger-r61-MutantEvmVerifier rev-parse HEAD` → `e0a4b0c4348ef1fade46539f520e94fa140c4d8a`.
Target `corpus/verify_evm_evidence.py:23-59`: 8 require calls, 37 explicit and-connected conjuncts; each independently replaced by `True` (line 39 chained comparison is one conjunct).
Detector, same path per case in all three phases: `/usr/bin/python3 -B /tmp/revenger-r61-MutantEvmVerifier/corpus/_r61_MNN_verify_evm_evidence.py --self-test`; cwd `/`; timeout 10s; ≤8 concurrent isolated scripts; Python 3.14.8.
Expected kill: pristine/restored exit 0, mutant nonzero; baseline/restoration failure or timeout → inconclusive. Observed: pristine 37/37 exit 0, mutants 37/37 exit 0, restored 37/37 exit 0; no timeouts.
Every phase printed exactly these two stdout lines, with empty stderr:
```text
POSITIVE ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42 1/1 selector candidate and two digests; destination 16 != PUSH4 6; inferred only
NEGATIVE REJECTED candidate destination mismatch
```
All before/after SHA-256 values (original target and every restored case) are `8265a22f7be8df011cee319a332123a0bfcb011413839a31f602a037c15d0b49`; each copy was byte-compared with the pristine source (37/37 equal).
Table paths/lines refer to original `corpus/verify_evm_evidence.py`; MNN maps to the absolute detector path above. Exit column is pristine/mutated/restored. Mutant SHA-256 is recorded before restoration.
| Mutant | Line: conjunct weakened to True | Mutant SHA-256 | Exit P/M/R | Mutant last line | Verdict |
|---|---|---|---|---|---|
| M01 | 23: `carrier.startswith(b"0x")` | `a93d0885962d281ce2b28f72e40b17f3c547c2c76ac1da557aac5f04d62eb25d` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M02 | 23: `carrier.endswith(b"\n")` | `ea1adbb9d2665172cf757c97faaca8edcd445a3cc09032d6217d051adea18f6d` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M03 | 26: `digest(carrier) == truth["carrier_sha256"]` | `bf5a8b22978bad7847c82bc09e2ba760ed7496e75725fe757982f802bc236c8a` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M04 | 27: `digest(decoded) == truth["decoded_sha256"]` | `593927ce4e9e60ab328991f6b092a747b7b8517f3bbd64bd776df01e4d86023d` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M05 | 28: `len(decoded) == truth["decoded_size"]` | `5528b0b462f24ce0c3822c725a4708cc78178a5588d43232c4bfe6713104d078` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M06 | 28: `truth["encoding"] == "hex"` | `31914527943f2683de6560b36d7e3ee333689a396448cb37761964e1dd594f55` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M07 | 32: `opcode + 1 == immediate` | `ea9cec6813d78ee8e4d99f1971d1818e1c9f8f9b7adefc5484079eb1338891dc` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M08 | 32: `truth["selector_immediate_length"] == 4` | `c26567cf9212d98596595b5857ae10ffa2f709efa97b6571e36f10cd93c7726b` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M09 | 33: `decoded[opcode] == 0x63` | `e6727bb4ad15e9bc9a2c4b7e53ab83972ba6b57814dc881b4877db3c2b0f7e07` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M10 | 33: `decoded[immediate:immediate + 4].hex() == truth["selector_push4"]` | `015242e58de3ead47fea6f5e030c2475837c731f2d31952aaef1d71204c523d0` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M11 | 34: `decoded[immediate + 4] == 0x14` | `1878d6d8751e33d46e09748ef518a2f2633b870e5955dece476765b2c166d8f6` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M12 | 34: `decoded[immediate + 5] == 0x60` | `b190dde9fc6bcbea89cc2e4b464f2c596a1bd14ebef157f1a9c18a9c415ea38c` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M13 | 35: `decoded[immediate + 7] == 0x57` | `f18c61d7ff42835f167937db9b3826f465985d160213cb4e74eedb4677c48aeb` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M14 | 37: `evidence["evidence_id"] == EXPECTED_ID` | `7236a54d1588e73c691c2840d6e56fdbbd583463f7c19d7e548463b9e9eb41da` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M15 | 37: `evidence["operation"] == "inspect_evm_interface"` | `f762d27c707bf65a1f383b8b97552e92a83cc1e366bd0a3329b05a75ee28a211` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M16 | 38: `evidence["subject"]["digest"]["sha256"] == digest(carrier)` | `a1da68074ea4f51e46b6424512b99f900e6e6406a09be0f51cf0691cd4e15d03` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M17 | 39: `evidence["parameters"]["encoding"] == result["artifact"]["encoding"] == "hex"` | `0ae1f9d841d36e9d9c30b8081189ee0ba1cf319aef7fe68237a9cfb8af988ac2` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M18 | 41: `result["artifact"]["sha256"] == digest(carrier)` | `98c9d401f9ec01059529b12457073a88e4f3ada805ed74a78849f46a928fd9fa` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M19 | 42: `result["artifact"]["bytes"] == len(carrier)` | `757de55e83148b3fa06dc3117774f52acc332e2dc580d7bbdf6ce63809ca9b39` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M20 | 43: `result["bytecode"]["sha256"] == digest(decoded)` | `b112723b391e5be5563a79a62d008d7285a512a89ca3b240b1368cf7b4fc66b6` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M21 | 44: `result["bytecode"]["bytes"] == len(decoded)` | `02125f1ce71297269498a7a60ce280d14933db4594515cd22f0d15faf057d832` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M22 | 45: `result["bytecode"]["hex"] == decoded.hex()` | `65002eb6b97c657bd915474e9c708c2834b9fbf3060f26faa23382be5c254bfd` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M23 | 47: `len(functions) == 1` | `861db0a8fa0dd755d59ee5810463fcdc055e8b0218bbfe5154cba5d62d8bf5e8` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M24 | 47: `len(evidence["raw_result"]["functions"]) == 1` | `60d67b9c1500e1da5651eaae9c9c26f9058b98459675d86801437812b9b58b9b` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M25 | 51: `function["selector"] == "0x" + truth["selector_push4"]` | `33ed0a0374ebe4e09c12092356d7e8e2a0ccb6d65beace2e924b09309e316655` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M26 | 52: `evidence["raw_result"]["functions"][0]["selector"] == truth["selector_push4"]` | `69744cbe5a727da6c1a113171a9da677b8d5f2524504aecd8852f3fc6d3155c5` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M27 | 53: `evidence["raw_result"]["functions"][0]["bytecodeOffset"] == target` | `e15c15616c38e56d89e43058175ad07ddc6350c00345bf06ca4898b08934f51b` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M28 | 54: `target == immediate + 9` | `a8eb61a5c71229f08c8c97cfe9e136d1e5ba5039931f46e811e954800485e27b` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M29 | 54: `target < len(decoded)` | `89ee61ed53e8414c5df85f42e407b8120a74d9c682e1bf9f86e456fc718387ce` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M30 | 54: `decoded[target] == 0x5b` | `7560843ddaeb1bd91f13c5ef0d915cc906f98b6ec0143db182804d2da5d95ae6` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M31 | 55: `decoded[immediate + 6] == target` | `0abff176e89f55c7dd681d47de5ffc1fe0b4e5117f8837b1e3510b3ac9669d3d` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M32 | 55: `target != opcode` | `d4457c0700bc5cd7946c19368dc63095a391d64096cf1c1f227fd5bccde79729` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M33 | 55: `target != immediate` | `1620e31f3148158bbe106d17b1a5c6bb10c94211da9536680343fc6270800a80` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M34 | 57: `result["evidence_kind"] == "inferred"` | `eaf8a93908366fac8448737982f20b7291fd8e0d2d5cd4be681d04e0b0166c4c` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M35 | 57: `evidence["confidence"] == "inferred"` | `7ebc9a7145d69321dea7dd1aea8e3798a3c61e484c29544a34044e755ffcc67e` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M36 | 58: `result["discovery_completeness"] == "unknown"` | `c14992bc40bbcd0660f909bda0caa88799c6a21633ccfbc4e6f6b4d16be54973` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
| M37 | 59: `result["runtime_execution"] == "not-performed"` | `ce4d428acc5cc5efa6f5a61d6ce823d177825c1ae0eb77db7488e297acf300bf` | 0/0/0 | `NEGATIVE REJECTED candidate destination mismatch` | SURVIVED |
`corpus/verify_evm_evidence.py:67-74` alters only normalized destination to 6; at `:53-55`, raw-destination equality and other destination predicates overlap. [INFERENCE] Redundant destination checks can mask removal of any one predicate.
Observed scope: `--self-test` detects none of these individual predicate removals, including digests (:26-27,38,41,43), selector comparisons (:32-35,51-52), destination == immediate+9 (:54), JUMPDEST byte (:54), or inference limits (:57-59).
This is a calibration/coverage finding, not proof the intact verifier accepts forged evidence. The positive replay still exercises its current checks; the self-test is not independent per-conjunct regression protection. C09 prose must not claim such protection.
Restoration/input check: `sha256sum` before and after returned the same values for all four inputs: target hash above; fixture.hex `294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827`; truth.json `789d41852c9a0538beceb00a5c1680ae87adfb6ba32063259c936a8523cf9fe5`; inspection.json `e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948`.
Full phase commands, stdout/stderr, replacements, hashes, and written scratch-file paths: `/tmp/revenger-r61-MutantEvmVerifier/corpus/r61-MutantEvmVerifier-results.json` (SHA-256 `a126633d4815468bec0e6b9ee26d283199e1517d6628ab95822bd9f7a54a4448`). Each of the 37 case files is retained restored with the common before/after hash; no fixture, saved record, or original verifier was written.
No production patch: RUNS-only investigation; only restored private corpus copies, the private JSON evidence ledger, and this report were written. No builds/lint/formatters, REA producer, RPC, bytecode execution, or unrelated runtime used.
VERDICT: KILLED 0/37; SURVIVED 37/37; INCONCLUSIVE 0/37; exact restoration 37/37. Installs: none.
