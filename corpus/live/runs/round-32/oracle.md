# Independent raw-byte PE resource oracle (round 32)

## Scope and observations

Inspected `corpus/fixtures/pe-r31/fixture.exe` as bytes only; did not run it or invoke REA. File size is 1,024 bytes; SHA-256 is `714369ff1bfcd2e04a5f6c32f938778b38c6c455ae6a019b51e6c2d702510b47`. It has DOS `MZ` at offset `0`, `e_lfanew=0x40`, and `PE\0\0` at `0x40`. COFF machine is `0x014c` (i386), one section, optional-header size `0xe0`; optional header is PE32 (`0x10b`). Resource data directory (index 2) is RVA `0x2000`, size `0xd0`. The sole `.rsrc` section has RVA `0x2000`, virtual size `0xd0`, raw offset `0x200`, raw size `0x200`, so root resource directory RVA maps to file offset `0x200`.

Raw resource tree decode (directory entry offsets are relative to resource base RVA/file offset):

- Root at relative `0x00`: one ID entry, type 10 (`RCDATA`), child directory at relative `0x18`.
- Type directory at `0x18`: two ID entries, IDs 2 and 3, child directories at `0x38` and `0x50`.
- ID 2 directory at `0x38`: one numeric language `0x0409` (1033), data entry at relative `0x68`. Data entry says RVA `0x20a0`, size 15; mapped file offset `0x2a0`. Payload bytes are ASCII `SEV-R27-PAYLOAD` (15 bytes), SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.
- ID 3 directory at `0x50`: one numeric language `0x0409` (1033), data entry at relative `0x78`. Data entry says RVA `0x20c0`, size 15; mapped file offset `0x2c0`. Payload bytes are ASCII `ALT-R31-PAYLOAD` (15 bytes), SHA-256 `cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e`.

These are observations from direct byte decoding. That type/ID/language path representation and interpretation as RCDATA follows PE resource conventions. A tool output that calls payloads “strings” should not imply that the resource data is NUL-terminated: each declared payload is exactly 15 bytes and its trailing NUL is outside the declared size. No language fallback behavior or runtime selection can be established from this file layout alone.

## Independent parser design (bounded)

1. Parse PE headers with bounds checks; accept PE32 and PE32+ separately, locating data directories via optional-header magic and `NumberOfRvaAndSizes`. Verify directory index 2 is present.
2. Build RVA→file-offset mapping from section headers, checking `SizeOfHeaders`, virtual/raw extents, integer overflow, and file bounds. Reject ambiguous overlapping mappings rather than silently selecting one. Data-directory and payload reads must fit both the file and a mapped raw section; do not treat zero-filled virtual tails as file bytes.
3. Traverse resource directories relative to resource-directory base. Decode each 8-byte entry: high-bit name field means UTF-16LE string at base-relative low-31-bit offset; otherwise numeric ID. High bit in target means subdirectory, otherwise data-entry record. Preserve numeric names separately from decoded names and preserve original order.
4. Track visited directory offsets and enforce depth/node/string/payload limits; reject or report cycles, repeated references, out-of-range offsets and truncated records. Resource directory entry counts are 16-bit name+ID counts in the directory header; do not infer count from resource-directory size.
5. Data-entry `OffsetToData` is an RVA, not a base-relative resource offset. Map it independently. Keep declared size, code page, reserved field, raw range, and a digest; do not parse or execute payload contents.
6. Emit findings with file offsets and RVAs so the result can be checked independently. Report malformed/unmapped branches as partial coverage, not as absent resources.

## Pitfalls and bounded recommendations

- Names and IDs are distinct: named entries sort before numeric IDs in canonical files, but parser correctness must not depend on sorting. Numeric type 10 is conventionally `RCDATA`; show both ID and label.
- Resource tree offsets are relative to the resource-directory base; payload addresses are RVAs. Confusing those address spaces can accidentally produce plausible offsets.
- This fixture’s section has raw padding beyond the resource directory (`0x200` raw bytes versus `0xd0` directory size). Do not scan padding as additional tree entries or payloads. Conversely the payload bytes at `0x2a0`/`0x2c0` are within raw mapping but need validation against declared sizes.
- UTF-16 resource names can be unaligned or malformed; bounds-check the length prefix and `2*length` bytes, and preserve decode errors.
- Language ID `0x0409` is observed; it is not evidence of which resource a Windows loader or application will choose under other locale conditions.
- This is a single small PE32 fixture, not coverage of PE32+, named resources, malformed graphs, overlapping sections, or real-world resource payload formats. Recommend bounded tests for each of those cases before claiming general parser robustness.
