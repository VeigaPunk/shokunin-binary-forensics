# Independent LEAF review — round 15 duplicate-name ZIP

I independently read the r15 declaration, fixture README/truth, saved REA response/stderr and ledger. I inspected `fixture.zip` with Python `zipfile.ZipFile.infolist()` and read each member **by its `ZipInfo` object**, not by pathname. I did not rerun REA or execute a member.

- Archive: 357 bytes; SHA-256 `6cad12035be32a28223307744d4fd4b4998a275462821b70b5855528bb753ddf`, matching `truth.json`.
- Central-directory ordinal 0: `same.txt`, 17 uncompressed / 19 compressed bytes, CRC32 `def64bf3`, SHA-256 `7cad0d5665be7b1f1c29e4c6e2ce70c57c03e32e3bee20c4d09eb3b8115520fa`; bytes `first occurrence\n`.
- Ordinal 1: `same.txt`, 18 / 20 bytes, CRC32 `29e6da2f`, SHA-256 `0f2c2afb6ab1dc3fb6bb36fb58e520d2a3557a688e9cbbea82836b5d37c1097a`; bytes `second occurrence\n`.
- Ordinal 2: `marker.txt`, 14 / 16 bytes, CRC32 `cbeb881c`, SHA-256 `764be4e93ae36094345b79dcea5fd2934487d63a541c311fce14f52408ee3420`; bytes `unique marker\n`.

All three rows match `truth.json` on ordinal, path, uncompressed/compressed size, CRC32 and digest. The duplicate names are two distinct central-directory records and payloads; filename lookup alone is ambiguous. All are regular ZIP members, and the fixture is consistent with its README.

The saved `inspection.json` is an **error response**, not an inspection Evidence record: `code=artifact_operation_failed`, `category=execution_failure`, `message=Artifact path collision: same.txt`, `details.operation=inspect_artifact`, `details.reason=path`, `retryable=false`. `inspection.stderr` is empty. The ledger reports exit 1, but the saved response itself contains **no Evidence ID, no inventory and no partial occurrence observation**. The error supports only that this invocation refused a path collision. It does not establish producer intent, extraction behavior, or a collapsed 1/2 duplicate inventory.

**Verdict:** The declared requirement of REA Evidence preserving and checking all 3/3 occurrences is not met: it is **unmeasured**, not a measured 0/3. Coverage remains **unchanged** relative to prior distinct-path ZIP results. The fixture independently establishes the duplicate-name case and the response exposes a fail-closed route boundary, but neither gives REA occurrence coverage or member semantics. The ledger correctly preserves this distinction and correctly avoids inventing an Evidence ID. No contrary assumptions found; treat “fail-closed” as observed behavior of this invocation only, not proven implementation policy.
