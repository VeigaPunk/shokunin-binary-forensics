# Round 56 independent PE header review

## Evidence and method
Evidence ID: `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a` (saved REA inspection). I independently read the two fixture byte arrays and unpacked PE fields with Python `struct` (no executable or target was run). Saved files checked: `inspection.raw.json`, `receipt.json`, `truth.json`.

Commands/checks and output:

- `sha256(bytes)` for r55/r56: `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`; `911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b`.
- Parsed DOS `e_lfanew=64`, signature `PE\0\0`, machine `34404` (0x8664), optional-header size `240`, magic `523` (0x20b, PE32+), number of data directories `16`; identical in both files.
- Resource data-directory entry at optional-header offset `+112+16`: RVA `8192` (0x2000), declared size `240` (0xf0). `.rsrc`: VA `8192`, virtual size `1024`, raw file offset `512`, raw size `1024`. RVA maps to file offset `512 + (8192-8192) = 512`; declared file interval `[512,752)` is within file length 1536 and section raw interval `[512,1536)`.
- Directory root begins at file offset 512. Root header reports 2 ID entries; relevant type-3 directory at 544 reports 2 ID entries; type-14 directory at 576 reports 1 named entry. Data entries at 672,688,704 declare `(RVA,size)` `(8448,48)`, `(8512,48)`, `(8576,34)` respectively.
- Byte comparison: differing offsets exactly `[928]`, values `(2,3)`; matches truth's claimed mutation offset and ID change.

## Finding
**OBSERVATION:** Both files are PE32+ x86-64 and carry the same resource directory RVA/size and section mapping. Resource directory's declared 240-byte extent maps to file bytes 512–751, inside both file and `.rsrc` raw data. The r56 saved inspection reports the same directory `(rva=8192, offset=512, bytes=240)`, three resources, and the named group `A😀B!`; its RT_GROUP_ICON entries refer to image IDs 1 and 3, with candidate list `[0]` for ID 1 and empty for ID 3.

**INFERENCE:** The only byte mutation relative to r55 is consistent with the truth record's group-image resource ID mutation 2→3, and the saved inspection's relationship output is consistent with that changed reference. This corroborates header/RVA/file-bound and saved-output consistency, not the correctness of all parser behavior.

**UNKNOWN:** I did not independently validate every nested resource-relative offset, decode icon payloads, test language fallback, or observe loading/execution. A mapped data-entry payload can extend beyond the resource-directory table extent while remaining within section/file bounds; this review does not claim payload containment within `[512,752)`. No runtime behavior is established.

**Limits:** Offline byte checks only; the saved REA receipt records exit code 0 and the Evidence ID above. No producer rerun, executable, or target execution. Verdict: **PASS for requested PE32+ header, resource RVA/file-offset and declared directory-bound consistency; limited corroboration of saved output.**
