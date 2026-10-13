# Round 57 header and saved-output review

## Independent byte inspection (performed before reading saved inspection result)

**Commands:** Python `struct` reads from the supplied files, no target execution:
- `struct.unpack_from('<I', data, 60)` → PE header offset `0x40`; signature bytes are `PE\0\0`.
- `struct.unpack_from('<H', data, pe+4)` → machine `0x8664`; optional-header magic at `pe+24` → `0x20b` (PE32+).
- Resource data-directory pair at `optional_header+112+16` → RVA `0x2000`, declared size `240`.
- Section mapping from section header: VirtualAddress `0x2000`, PointerToRawData `0x200`, so resource RVA maps to file offset `0x200` (512); `[512,752)` lies within the 1,536-byte file. This is the declared resource-directory span, not a claim that all referenced payloads lie within it: payload/group data are later file ranges.
- Python byte comparison of `pe-r55/fixture.exe` and `pe-r57/fixture.exe` returned exactly `[(924, 48, 47)]`. At offset 924 little-endian uint32 values are respectively 48 and 47.
- SHA-256 values: r55 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`; r57 `71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d`.

## Saved output comparison

After the independent check, read `inspection.raw.json`, `receipt.json`, and `fixtures/pe-r57/truth.json`. Saved output identifies evidence **`ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07`**, matching r57 SHA-256. It reports PE32+, resource RVA 8192 / mapped location 512 / 240 bytes; Unicode-named RT_GROUP_ICON `A😀B!`; image ID 1 candidate resource 0 and `size_matches:true`; image ID 2 candidate resource 1 and `size_matches:false`, declared size 47. Truth JSON independently records the single changed offset and expected relationships.

## Bounded assessment

- **OBSERVATION:** Byte-level PE32+ header and resource-directory mapping are consistent with saved output. r55→r57 differs at exactly byte 924, 48→47. Saved analysis retains both image IDs and candidates; only the second size-match flag is false. Evidence ID above.
- **INFERENCE:** The one-byte mutation is consistent with the stated calibration claim: it changes the second group-image declared size while retaining both resource references. The parser's reported outcome agrees with truth and direct bytes.
- **UNKNOWN:** This review does not independently parse every resource-tree node or decode icon payloads; it does not establish actual Windows icon loading, language fallback, or execution behavior. The resource directory's 240-byte declaration ends at file offset 752; later resource payloads are referenced elsewhere in the file, so this is not a whole-resource-payload bound check.

Verdict: **Claim supported within the stated static byte/resource-inventory scope; runtime behavior remains unknown.**
