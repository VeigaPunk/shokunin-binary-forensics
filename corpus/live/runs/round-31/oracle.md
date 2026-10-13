# Round 31 independent byte oracle (pre-producer)

Scope: read-only byte analysis of `corpus/fixtures/pe-r30/fixture.exe`; no REA producer invocation and no PE execution. This establishes a proposed input oracle, not a parser outcome.

## Receipts

Run from repository root. `sha256sum .shokunin/revenger/corpus/fixtures/pe-r30/fixture.exe` reports `b94d840aa7eb952474b30260bc70e092fb1db832b0aa1bc393936d8dc4ce661a` (1024 bytes). `xxd -g1 -s 0x1f0 -l 0x140 .../fixture.exe` shows the resource tree and existing payload; offsets below are file offsets. PE signature is at `e_lfanew=0x40`; optional header is PE32 (magic `0x10b`). Resource data-directory entry is at file offset `0x108` (RVA `0x2000`, size 103), and `.rsrc` section maps RVA 0x2000 to raw offset 0x200. Thus resource RVA-relative offsets below map to file offset `0x200 + RVA-relative offset`.

Existing r30 tree, decoded from raw bytes: root directory 0x200/file 512 has one numeric type child `10` at 0x218/file 536; that type directory has one numeric name child `2` at 0x230/file 560, whose high-bit directory pointer is 0x30 (file 560); language entry at 0x248/file 584 is ID 1036 and points to data entry RVA 0x58 (file 600). That data entry describes payload RVA 0x20, length 15 (file bytes `[0x258,0x267)`, offsets 600–614). Existing payload is `SEV-R27-PAYLOAD`, SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.

## Two-entry oracle construction

The declaration's proposed layout uses resource-root-relative offsets: root 0x00, type directory 0x18, name directories 0x38 and 0x50, data entries 0x68 and 0x78, payloads 0xa0 and 0xc0. Since root RVA is 0x2000 / raw offset 0x200, corresponding file offsets are respectively 512, 536, 568, 592, 616, 632, 672, 704. Expected hierarchy: type ID 10; name IDs 2 and 3; language IDs 1036 and 1033. Each numeric directory entry must have the directory bit set on its target offset; language leaves point to data-entry offsets without that bit. Each data entry gives payload RVA 0x20/0x40 and length 15.

Suggested distinct exact payloads, chosen to keep the existing first payload unchanged: payload A at file `[672,687)` = ASCII `SEV-R27-PAYLOAD`; payload B at `[704,719)` = ASCII `R31-SECOND-TEST`. Their expected SHA-256 values, independently computed over those 15 bytes, are:

- name 2 / language 1036 / file offset 672 / length 15: `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`
- name 3 / language 1033 / file offset 704 / length 15: `415e35a8aeada999dc39edc24f082421440958ccc6fa6a4fe6fd765feda1bfa8`

These payload strings are an oracle proposal, not an assertion that a fixture has been authored. The round declaration reserves changed header ranges for constructing the tree; compare the eventual fixture byte-for-byte to its declared source/truth rather than assuming unchanged fields. Resource-directory size must cover the final tree/data entries/payload ranges consistently with the PE resource RVA extent; ensure offsets/RVAs remain within `.rsrc` raw data. The existing 103-byte resource-directory size is not sufficient for the proposed tree and payloads.

## Falsification limits

A two-entry parser result should match exactly the unordered pair `(type=10,name=2,language=1036,payload offset=672,length=15,digest=A)` and `(type=10,name=3,language=1033,payload offset=704,length=15,digest=B)`, with no extra or duplicate resource. Both expected payload digests differ; this catches accidental aliasing/conflation. This raw-byte oracle does not establish that a later-produced fixture is structurally valid, that REA ran, or any Windows loader/runtime behavior. Validate the actual fixture bytes and source-to-output changes independently before scoring output.
