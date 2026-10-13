# PE resource string layout — pe-r31 fixture

## Scope and method

Inspected the fixture bytes directly, without invoking REA or executing the target. Target: `.shokunin/revenger/corpus/fixtures/pe-r31/fixture.exe`; 1,024 bytes; SHA-256 `714369ff1bfcd2e04a5f6c32f938778b38c6c455ae6a019b51e6c2d702510b47`. File offsets below are absolute unless marked as resource-directory-relative (RVA-relative offsets have base RVA `0x2000`).

## Concrete observations

- PE32/i386 (`Machine=0x014c`, optional-header magic `0x010b`). The resource data-directory entry is RVA `0x2000`, size `0xD0`. The `.rsrc` section maps RVA `0x2000` to file offset `0x200`; for this entire directory, file offset is `RVA - 0x2000 + 0x200`.
- Resource root directory is file offset `0x200` (relative `0x00`): zero named entries and one ID entry. Its entry at `0x210` has numeric type ID 10 and points to the directory at `0x218` (relative `0x18`).
- Directory at file `0x218` (relative `0x18`) has zero named entries and two ID entries. Entries at file `0x228` and `0x230` have numeric IDs 2 and 3, pointing respectively to directories at `0x238` (relative `0x38`) and `0x250` (relative `0x50`). Their name/ID fields are plain `2` and `3`; neither has the high bit set for a string-name pointer.
- The leaf directory at file `0x238` has language ID `0x040C` and data entry at `0x268`; the leaf at `0x250` has language ID `0x0409` and data entry at `0x278`. The data entries describe payloads at RVAs `0x20A0` and `0x20C0`, each 15 bytes (file offsets `0x2A0` and `0x2C0`).
- No resource-directory entry in this fixture points to an `IMAGE_RESOURCE_DIR_STRING_U` name record. Accordingly, this fixture provides no UTF-16 resource name encoding/sample to decode. The 15-byte sequences at file offsets `0x2A0` and `0x2C0` are ASCII payload bytes `SEV-R27-PAYLOAD` and `ALT-R31-PAYLOAD`, not UTF-16 resource-name records.
- The resource data-directory size is `0xD0`; the payload ranges and directory structures described above lie within the `.rsrc` raw data. The section has raw size `0x200`, so bytes available in the section exceed the directory's declared size; that alone does not make padding part of the resource tree.

## Layout interpretation and pitfalls

- In a PE resource entry, the high bit of the first DWORD distinguishes a string-name pointer from a numeric ID. For a string name, the lower 31 bits are an offset relative to the start of the resource directory (here RVA `0x2000`), not an absolute file offset and not a direct RVA. Map that RVA through the containing section to a file offset before reading.
- `IMAGE_RESOURCE_DIR_STRING_U` begins with a little-endian 16-bit character count, followed by exactly that many UTF-16LE code units. It is length-prefixed, not NUL-terminated. Check that the prefix and `2 * length` bytes are in bounds; do not include alignment padding as part of the string. Keep UTF-16 code units intact or report decoding errors rather than assuming ASCII / valid surrogate pairs.
- Distinguish the directory's entry count fields (`NumberOfNamedEntries`, `NumberOfIdEntries`) and their corresponding entry array from string-record storage. Here all entries are numeric, even though arbitrary resource payload contents happen to contain printable text.
- This is a static byte-layout observation only. It does not establish loader behavior or a general property of other fixtures. Because this specific fixture lacks a named resource, a UTF-16 name parser needs a separate fixture with at least one high-bit name pointer to test its offsets and decoding.

## Bounded recommendation

For a proposed UTF-16 resource-name offset, verify the entry's name field has bit 31 set, mask that bit, and interpret the remaining value relative to the resource-directory base. Confirm the length prefix and full code-unit span fit both the declared directory range and file-backed section data. Report the exact entry field, relative offset, mapped file offset, declared length, and raw UTF-16LE bytes. Do not treat ASCII payload strings or numeric IDs as names. This pe-r31 fixture can validate numeric-ID handling and RVA-to-file mapping, but cannot validate a proposed named-string offset; use an independently identified named-resource fixture for that check.
