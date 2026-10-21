GRADE: HOLDS — C09 EVM verifier-credit limitations
Axes: conjunct coverage, detector attribution, exact-byte restoration. Revision: ab580698212258a55e43e9bb9bf6ac78c91eae2a; mandated git archive extracted under /tmp/revenger-r61w3-W3EvmVerifierCredit; no live source edits.
r19-only observation: corpus/verify_evm_evidence.py:9-11 fixes the r19 fixture/evidence paths; :21-22,64 reads only those inputs. No r21–r26 inputs are read.
Mutation: Python AST enumerated 8 require-condition AND groups and 37 conjuncts (:23-59); :39 chained comparison counts as one. Each case deletes exactly one conjunct plus its adjacent and; parsed AST equals precisely that one deletion.
Detector: /usr/bin/python3 -B /tmp/revenger-r61w3-W3EvmVerifierCredit/corpus/_w3_MNN_verify_evm_evidence.py --self-test; cwd=/; timeout=10s; at most 8 concurrent cases; Python 3.14.8.
Expected kill: pristine/restored exit 0 and mutant nonzero; baseline/restoration failure or timeout is inconclusive. Actual: pristine 37/37 exit 0, mutated 37/37 exit 0, restored 37/37 exit 0; 0 timeouts; stderr empty. All 111 runs printed exactly:
```text
POSITIVE ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42 1/1 selector candidate and two digests; destination 16 != PUSH4 6; inferred only
NEGATIVE REJECTED candidate destination mismatch
```
Restoration: all 37 files byte-equal to pristine after finally restoration; every before/after SHA-256 and untouched archive verifier SHA-256 = 8265a22f7be8df011cee319a332123a0bfcb011413839a31f602a037c15d0b49.
Unchanged input before/after SHA-256, corpus/fixtures/evm-r19/fixture.hex: 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827.
Unchanged input before/after SHA-256, corpus/fixtures/evm-r19/truth.json: 789d41852c9a0538beceb00a5c1680ae87adfb6ba32063259c936a8523cf9fe5.
Unchanged input before/after SHA-256, corpus/live/runs/round-19/inspection.json: e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948.
Credit finding: corpus/QUALITY.md:25 requires deletion-sensitive credit; corpus/knowledge/evm-saved-interface-candidates.md:85-88,189 expressly gives this verifier no guard credit and assigns the seven-fixture derivations to the entry walk. corpus/lessons/round-61.md:77 agrees. This limitation is correct.
Prior evidence nuance: .ufo/waves/round-61/build/MutantEvmVerifier.md:4 used True substitution, not literal source deletion. This fresh literal-deletion probe independently reproduces its 0/37 detection count; survivor coverage is not proof the intact verifier accepts forged records.
Raw phase commands, stdout/stderr, deleted spans, mutant/before/restored hashes: /tmp/revenger-r61w3-W3EvmVerifierCredit/verifier-credit-probe.json.
Raw ledger SHA-256: 800be440186fde12aa6cffd85bf25e7deda99504ef95cbdafb6f33c2ede93b5e. Only the requested verifier self-tests ran; no REA producer, bytecode/fixture-JavaScript execution, builds, lint or formatters.
Enumeration below uses original corpus/verify_evm_evidence.py lines. P/M/R = pristine/mutated/restored exits. Each row was independently restored; all common outputs are quoted above.
| ID | Line: deleted conjunct | Mutant SHA-256 | P/M/R; verdict |
|---|---|---|---|
| M01 | 23: `carrier.startswith(b"0x")` | `72144b9289c92d4c2dc4b876ab40a1786cd03aa2d880f62ff12a21f10906901a` | 0/0/0; SURVIVED |
| M02 | 23: `carrier.endswith(b"\n")` | `265496074f18f73431a3122bbf335c28941c698c9c7fd3d57da8175ea6a72514` | 0/0/0; SURVIVED |
| M03 | 26: `digest(carrier) == truth["carrier_sha256"]` | `b9d34fcf9253c499a9f4291ef278a3487141061655ff8bbee684d27b23b7f66b` | 0/0/0; SURVIVED |
| M04 | 27: `digest(decoded) == truth["decoded_sha256"]` | `539a02cb24b1b53449750df064481e0c583c0cf1d159ad7a459c721406c9b94c` | 0/0/0; SURVIVED |
| M05 | 28: `len(decoded) == truth["decoded_size"]` | `0759fa837ac74d435c326ba6f10eee9a91a32738d6d4aebde22b16f320639a88` | 0/0/0; SURVIVED |
| M06 | 28: `truth["encoding"] == "hex"` | `5d91b529a67220d6c70c613879d9dac653547e07940374fa854a5bbd4a8ec6d1` | 0/0/0; SURVIVED |
| M07 | 32: `opcode + 1 == immediate` | `b8f35fdd7ad3d7f24fed23ef5ba0d504d348ef7c26b28de30ef7ea0e3dd416a7` | 0/0/0; SURVIVED |
| M08 | 32: `truth["selector_immediate_length"] == 4` | `7403c5d68fd893daa4c6989b7165d9525c3996fdcc1cb3ab58ae638b9220a0ab` | 0/0/0; SURVIVED |
| M09 | 33: `decoded[opcode] == 0x63` | `7577e8fb2efba7656809f1699c9c0a39a090bfeabc083c95530867d60e5a1142` | 0/0/0; SURVIVED |
| M10 | 33: `decoded[immediate:immediate + 4].hex() == truth["selector_push4"]` | `ed42938e9f61afe0e699b23790344bf3684fe2c81c297d811ea95456b23a04ac` | 0/0/0; SURVIVED |
| M11 | 34: `decoded[immediate + 4] == 0x14` | `db3fa8b90ef1a56ca7a3f323bcc029d5af8a0bd3bf083d38b3ab8e18475dd8b0` | 0/0/0; SURVIVED |
| M12 | 34: `decoded[immediate + 5] == 0x60` | `94e063953409a80d1e79171256fb79ecc233eee951e672f4e24eb25c0105d0f6` | 0/0/0; SURVIVED |
| M13 | 35: `decoded[immediate + 7] == 0x57` | `3e973581aef30213e4f5dbced255b3f591bde9191d7e28e74faf6c72f954836c` | 0/0/0; SURVIVED |
| M14 | 37: `evidence["evidence_id"] == EXPECTED_ID` | `30e17006fb165a64de9b3c73a024896fe5389957a307b630cf937d804601ef9f` | 0/0/0; SURVIVED |
| M15 | 37: `evidence["operation"] == "inspect_evm_interface"` | `932db56f4340d7e70c0e112282800f06f1a41e892a912233ed0da86a45fd2add` | 0/0/0; SURVIVED |
| M16 | 38: `evidence["subject"]["digest"]["sha256"] == digest(carrier)` | `1f037c6d21c007fb61b79060f325ed59408a9f70cb263595cbf6cbea7aef712f` | 0/0/0; SURVIVED |
| M17 | 39: `evidence["parameters"]["encoding"] == result["artifact"]["encoding"] == "hex"` | `136c9d4395bf8b0f9d4ccf9769512a00c4542fe585943633b87319013b3c1c6d` | 0/0/0; SURVIVED |
| M18 | 41: `result["artifact"]["sha256"] == digest(carrier)` | `d801ce96a70b259a043e79385f1d33976b3ced6c86419aa8df5a2701b06ef052` | 0/0/0; SURVIVED |
| M19 | 42: `result["artifact"]["bytes"] == len(carrier)` | `cfcc6c87e88304eb59de77cdbe397958b9adc81d6aef20b4fd9513b7c8ad20be` | 0/0/0; SURVIVED |
| M20 | 43: `result["bytecode"]["sha256"] == digest(decoded)` | `fa0802a404c8e369493c9f2312ceba533df2b5fff7de987426ad714efaefa0c9` | 0/0/0; SURVIVED |
| M21 | 44: `result["bytecode"]["bytes"] == len(decoded)` | `a3803ce044cff85e0c4f9feb7fe955d31c6d11143d8f537e4f6b64ea2c46631b` | 0/0/0; SURVIVED |
| M22 | 45: `result["bytecode"]["hex"] == decoded.hex()` | `83514a858caac3fbb789c6b74153d856864a12ecaa5b6538a4efe76d83c52f0a` | 0/0/0; SURVIVED |
| M23 | 47: `len(functions) == 1` | `94dc9b22372e1314555230627b687d8906eeea263e74f19456c29b0d35572c7b` | 0/0/0; SURVIVED |
| M24 | 47: `len(evidence["raw_result"]["functions"]) == 1` | `f05ab98eeffc7e44529aa8b988a376f881108a5825e7f27d547227595eb6b4c7` | 0/0/0; SURVIVED |
| M25 | 51: `function["selector"] == "0x" + truth["selector_push4"]` | `9986a775b9e6e57eb29a5e021872aefd3b3fad2167581f6efc3d1f0a9cdac5ed` | 0/0/0; SURVIVED |
| M26 | 52: `evidence["raw_result"]["functions"][0]["selector"] == truth["selector_push4"]` | `ff85aae56ef41c750bf0eb1ff27552fdd49cd9bcc7946d604451f08672155556` | 0/0/0; SURVIVED |
| M27 | 53: `evidence["raw_result"]["functions"][0]["bytecodeOffset"] == target` | `4781b2f514bc2f5890ec7834afd41fa25b3fc3b141b839ca3ff03f95c865ab93` | 0/0/0; SURVIVED |
| M28 | 54: `target == immediate + 9` | `d1d68ec6a303dc06bb732db7e328aa8a8ed2fbf4ab548779aee5573de32bf071` | 0/0/0; SURVIVED |
| M29 | 54: `target < len(decoded)` | `c2b10099d8c14611c2adda6a4edc73240c29ae7dccceef44215dac22eeed5c09` | 0/0/0; SURVIVED |
| M30 | 54: `decoded[target] == 0x5b` | `0d74ec0fe365f8ae04a598e18b6b4b7496887ba539873c43d7d10cd385889924` | 0/0/0; SURVIVED |
| M31 | 55: `decoded[immediate + 6] == target` | `e48987b5108f78fa38d917214e01c2017cce2fdd625eb5ef0bca96ebe96990b9` | 0/0/0; SURVIVED |
| M32 | 55: `target != opcode` | `4c567e8aba134fe27f7a995ba2d7369c15c50a8965c7ffe4cdb8426de8cd7923` | 0/0/0; SURVIVED |
| M33 | 55: `target != immediate` | `a43bb132f4f63f2df712b50165c427cc8846a122e5f0779f375fd47872c99e63` | 0/0/0; SURVIVED |
| M34 | 57: `result["evidence_kind"] == "inferred"` | `5f677e8c165ef6c2ecd4cd832d99334bfe340d054de671c7d012314d569db0e3` | 0/0/0; SURVIVED |
| M35 | 57: `evidence["confidence"] == "inferred"` | `d8c1826c182b3f2da8c685efacfaf4a4d48cb72b9a54848a31943625b2d92461` | 0/0/0; SURVIVED |
| M36 | 58: `result["discovery_completeness"] == "unknown"` | `d7f6c11703bc38ceb4e2ed34f5084a55b615144a5833d414c8ebb800062b1d79` | 0/0/0; SURVIVED |
| M37 | 59: `result["runtime_execution"] == "not-performed"` | `5adf0e9365b8ff0fd451598dc105962ec50a49c98eb00a52c7c2db14d3b3c46a` | 0/0/0; SURVIVED |
VERDICT: HOLDS for this assigned limitation; KILLED 0/37, SURVIVED 37/37, INCONCLUSIVE 0/37; exact restoration 37/37; Q13 guard credit correctly withheld. Installs/updates: none.
