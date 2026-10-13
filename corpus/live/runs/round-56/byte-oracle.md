# Round 56 independent byte oracle

## Method and reproducible checks

Read-only Python `struct`/`hashlib` parsing of the two fixture byte arrays; no target execution. Commands/checks performed in the REPL:

- `sha256(bytes)`, PE `e_lfanew` at `0x3c`, COFF header, optional-header magic, section table.
- Compare byte arrays: `[i for i,(x,y) in enumerate(zip(r55,r56)) if x != y]` → `[928]`.
- Read `.rsrc` section mapping and resource directory entries; map RVA 8192 to file offset 512 (section RVA 8192, raw offset 512). Resource data RVAs map by `512 + (RVA - 8192)`.
- Inspect UTF-16 name record at file offset 736; group payload at 896; icon leaf payloads at 768 and 832. Hash payload slices independently.

## Byte observations

- r55 SHA-256 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`; r56 SHA-256 `911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b`; each 1536 bytes. Both have `MZ`, PE signature at 0x40, machine `0x8664`, PE32+ magic `0x20b`, one `.rsrc` section, resource directory RVA 0x2000 / file offset 512.
- The resource tree bytes establish RT_ICON (type 3) names/IDs 1 and 2, RT_GROUP_ICON (type 14) with one named entry, and language ID 1033 for each leaf. Group-name record at 736: `050041003dd800de42002100`; length 5 UTF-16 code units decodes as `A😀B!` (surrogate pair included).
- Group resource is file offset 896, 34 bytes. Entries in order: header reserved=0,type=1,count=2; first 14-byte entry dimensions 1×1, planes=1, bpp=32, declared size=48, ID=1; second dimensions 2×2, planes=1,bpp=32,size=48, ID=2 in r55 and ID=3 in r56. Thus the ordered IDs are `[1,2]` then `[1,3]`.
- Exactly one changed byte: offset 928, the low byte of second group-entry `nId` (entry starts at 916; ID field offset 928), `02`→`03`. This confirms the claimed one-byte delta.
- Payload bytes at offsets 768..815 and 832..879 each hash respectively `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003` and `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae` in both files: both leaves unchanged. Group payload SHA-256 changes from `45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a` to `672ad226768046a16b55dbcae6b0ee050e68e08e72b5089bf658593f549a4c4d`.

## Comparison with saved REA after byte truth

Evidence ID `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a` (saved `inspection.raw.json`; receipt says exit 0 and binds same r56 digest) reports PE32+, resource group name `A😀B!`, ordered IDs 1 and 3, candidate resource index `[0]` for ID 1 and no candidate for ID 3, both icon leaves hashes/locations, and coverage `complete` for its stated inventory. These fields agree with independent byte parsing. It also reports exact group and payload locations and hashes consistent with the bytes.

## Finding ledger

**OBSERVATION:** The byte facts above are directly parsed from the supplied fixture files. REA saved evidence ID above agrees on the listed resource inventory and group relationships. Truth manifest is corroborative, not the basis of byte claims.

**INFERENCE:** Round 56 mutates only the second group reference from resource ID 2 to 3, leaving named group and both icon payloads unchanged. In this static resource table, ID 1 resolves to icon resource index 0 with matching 48-byte size; ID 3 has no matching icon resource candidate. This supports the limited claim that the parser represents the broken/missing reference without inventing an image candidate.

**UNKNOWN / LIMITS:** No execution, image decoding, language fallback, or shell/window loading was observed. Candidate absence does not establish runtime behavior. Resource-byte parsing is limited to these supplied files and the inspected structures; it does not prove general parser correctness. REA's stated scope excludes opaque-payload semantics and runtime loading.

**VERDICT:** Independent byte truth confirms the claimed one-byte r55→r56 mutation and the relevant REA output is concordant for this fixture; no discrepancy found within scope.
