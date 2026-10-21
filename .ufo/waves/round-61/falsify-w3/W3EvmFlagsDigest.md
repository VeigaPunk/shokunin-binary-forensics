GRADE: PARTIAL — C09 Observation 4 (corpus/knowledge/evm-saved-interface-candidates.md:39-40): the three flags hold 7/7, but r19's subject digest covers the 39-byte hex carrier, not the 18 decoded bytes, and line 40 does not say so
Seat RevengerR61-2.W3EvmFlagsDigest. Archive ab580698212258a55e43e9bb9bf6ac78c91eae2a (`git rev-parse HEAD` confirms) extracted to /tmp/revenger-r61w3-W3EvmFlagsDigest; `diff` live entry vs archive copy: identical. Static reads only; no bytecode or fixture JS run, no REA call, no chain.

## F1 — Flags: OBSERVED, exact 7/7
- In each `corpus/live/runs/round-{19,21,22,23,24,25,26}/inspection.json`, one occurrence each, all inside `normalized_result`: `"evidence_kind":"inferred"`, `"discovery_completeness":"unknown"`, `"runtime_execution":"not-performed"` (`grep -o` counts 1/1/1 per file). Top-level `confidence` is `"inferred"` 7/7; `analysis_profile` and `environment` are null.
- Entry block lines 105-137 saved verbatim, run `python3 -B` from the archive root: exit 0; every line prints `kind=inferred completeness=unknown runtime=not-performed`; `diff -u` against the Provenance block (lines 146-159) is IDENTICAL, so Observation 4's flag clause is fully reproduced.

## F2 — Digest referents: six match decoded bytes, r19 matches the hex text
| rec | subject.digest.sha256 | sha256(decoded bytecode) | subject==decoded |
|---|---|---|---|
| r19 | 294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827 | d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 | NO — hex text |
| r21 | d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723 | same | YES |
| r22 | 94c1790f966b78a9a5cc61bdc9ad4b805aaea6989e37773f66ff433deeb1dbe2 | same | YES |
| r23 | 8047ddff11234c2d36bd134cfb4aec669efa3ff89ed35a922552d44ebfe22f5a | same | YES |
| r24 | b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93 | same | YES |
| r25 | 2d87a4e203ebf590beab57cf7318ccf93c92035d7929d0bc16e6850433f5e8f7 | same | YES |
| r26 | ebe2d6757a7acd4c5b9de82441f66e70561350267114e445a2d6b8d037f8e97d | same | YES |
- r19 carrier, `xxd corpus/fixtures/evm-r19/fixture.hex`: `0x60003560e01c63deadbeef14601057005b00\n` — 39 bytes (36 hex chars + "0x" + LF); sha256 = 294e6f… exactly the record's subject digest. The decoded 18 bytes `60003560e01c63deadbeef14601057005b00` hash to d1086bce…, which is r19's `normalized_result.bytecode.sha256` and also r21's subject digest.
- `corpus/fixtures/evm-r19/truth.json` already names both: `carrier_sha256: 294e6f…`, `decoded_sha256: d1086bce…`. For r21-r26 the subject digest equals the fixture's `raw_sha256`/`sha256` field (r21 truth also carries `source_hex_fixture: ../evm-r19/fixture.hex`).
- Decoded binding is present 7/7 through another field: `normalized_result.bytecode.hex` equals the decoded bytes and `bytecode.sha256` equals sha256(decoded) for all seven; `normalized_result.artifact.bytes` equals file length and `artifact.sha256` equals sha256(file) for all seven.

## F3 — The PARTIAL: exact lines 40 and 137
- Line 40: "and each record's subject digest equals the fixture bytes' SHA-256." True of the stored file (subject is `format: file`, `name: fixture.hex|fixture.raw`), but for r19 the file is the 39-byte hex carrier; the entry never states this. `grep 294e6f` over the entry returns nothing, and the only r19 digest printed (line 146, `sha256=d1086bce32141782`) is the decoded digest.
- Line 137 computes `subject_eq_bytes = … in (sha(raw), sha(d))` — a disjunction that prints `True` for r19 without revealing which byte string matched (Provenance line 147). Read together with lines 21-22 ("the same 18 decoded bytes, hex and raw carriers"), line 40 can be read as binding decoded bytes, which is false at the subject field for r19.
- Not BROKEN: no evidence is contradicted. Identity to the decoded bytecode is carried by `bytecode.sha256`/`bytecode.hex` 7/7 and equals truth.json's decoded digest for r19 and r21; the sentence is true of the file it names. Fix is one clause: name the carrier (subject digest = stored file; r19 = 39-byte hex text; decoded digest in `normalized_result.bytecode.sha256`). Also note line 84's "identity is by digest" has the same carrier ambiguity.

## F4 — Preservation / harm: no fixture or record changed
- Each fixture file and each inspection.json has exactly one commit (ca7653e, 2c1e6fc, de8094f, b804f89, dd0d49f, 7f8748c, a3cc3f2); `git diff --stat HEAD` is empty for all seven fixtures and all seven records. M25 commit 0597e53 `--stat` lists the entry's evm-r24 span sentence, the round lesson, and added falsify-wave metadata files only — no fixture, no saved record.
- The record files were not edited after creation, so the subject digests observed now are the saved bytes; the carrier/decoded distinction cannot be a post-hoc fixture edit.

## F5 — Unknown
- Whether `normalized_result.bytecode` is provider-native or adapter-derived is not stated; [INFERENCE] adapter normalization, per the record limitation "Its reported values are retained in raw_result". Irrelevant to the equality, relevant if a later claim attributes the bytecode digest to evmole itself.
- No save-time copy of the fixtures exists besides the digests; single-commit history plus matching digests means no drift is observable, but a pre-commit substitution is not testable from the repo.

VERDICT: PARTIAL — flags exact 7/7 and file-digest equality true 7/7; r19's subject digest covers the 39-byte hex carrier (294e6f…), not the 18 decoded bytes (d1086bce…), which line 40 omits and line 137's disjunction hides; no evidence contradicted, no fixture/record changed, so this is a one-clause precision fix, not an admission-voiding overstatement.
Installs: none.
