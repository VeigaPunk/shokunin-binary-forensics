# Round 57 saved receipt review

## Commands and results

- `sha256sum`-equivalent Python check (`hashlib.sha256(path.read_bytes())`) on `pe-r55/fixture.exe` and `pe-r57/fixture.exe`: each is 1536 bytes; SHA-256 values are respectively `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b` and `71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d`.
- Direct byte comparison: only differing offset is 924, decimal `48` (`0x30`) in r55 and `47` (`0x2f`) in r57. The two group image records begin at 902 and 916; at 922–925, declared-size bytes change `20 00 30 00` → `20 00 2f 00`. Name bytes at 736–747 decode as UTF-16LE `A😀B!` (length prefix precedes the string).
- `npx -y rea-agents@6.4.0 inspect-pe-resources /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r57/fixture.exe --format json`: exit 0. Captured stdout SHA-256 `5c915ebdc4c79a6d98e3b9f374e6e2e67168a1c5b391487ac80bd8e199d34fc8`; stdout bytes exactly match saved `inspection.raw.json` (after stripping final newline), and hash matches `receipt.json`.
- Receipt Evidence ID: `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07`. It matches the raw JSON Evidence ID. Receipt fixture SHA-256 matches raw JSON subject digest and independently calculated r57 digest. Saved raw JSON's resource records report icon resources IDs 1/2; group `A😀B!` has ordered images IDs 1 and 2 with candidates `[0]`, `[1]`, same-language indices 0 and 1, sizes 48 and 47, and `size_matches` true and false respectively. Payload SHA-256 values match the saved r55 truth record.

## Assessment

**OBSERVATION:** The r55→r57 fixture files are identical except for the one-byte mutation at offset 924. The saved receipt's stdout hash is reproducible from the command output; the output is byte-for-byte the saved raw inspection record, and the Evidence ID and fixture digest agree across receipt/raw record. The saved result preserves both icon IDs/candidates and marks only the second size comparison false.

**INFERENCE:** The bytes and saved result are internally consistent with the stated claim: for the Unicode-named two-image icon group, only image 2's declared size changed 48→47, without changing either ID or candidate mapping. The REA parser output correctly reflects that size mismatch.

**UNKNOWN:** These checks do not authenticate who ran the producer, when it ran, or whether the saved command/receipt originated from a trusted execution. A repeat run now establishes reproducibility of the recorded output, not historical provenance. No execution of the fixture was performed.

**Bounded verdict:** PASS for internal consistency and reproduction of saved stdout; NOT AUTHENTICATED for producer origin/provenance.
