NOT-FALSIFIED — every numeric claim in `corpus/knowledge/round-65-apk-axml-byte-evidence.md` re-derives from `fixture.apk` bytes under a fully independent parse (own `struct` walk, not the lane's `readout.py`); zero discrepancies across 60+ checked numbers.

# Method

Independent code, executed against `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk` (947 B, sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` — confirmed by `sha256sum`): a raw EOCD scan (`find` loop over **all** `PK\x05\x06` occurrences, not `rfind` alone), a central-directory walk from the EOCD-declared `cd_off`, an independent local-header parse per member, a chunk-walk of the AXML payload, an **independent UTF-8 length-prefixed string decoder** (handles the 2-byte high-bit length forms the lane decoder does not exercise), direct dex-header field reads, and zlib/hashlib recomputation. No line of `readout.py` was reused.

# Re-derived values vs entry claims (all match)

**Archive/EOCD (item 1-2):**
- size=947, sha256=`05d2...d03e`; sole EOCD-signature occurrence at offset **925**; entries=3 (this disk and total both 3); `size_of_cd`=188; `offset_of_start_of_cd`=737; `737+188==925`; comment_len=0 and `925+22==947` (file ends exactly at EOCD).

**Members (item 3):** name lengths are 19/11/20 (my prior hypothesis of an extra field is disproven — `AndroidManifest.xml` is 19 chars, not 18; headers carry `nlen`/`elen` consistent with `payload_offset` = lho+30+nlen+elen):
- `AndroidManifest.xml`: lho=0, payload_offset=**49**, csize=usize=416, crc32 `962d075f` stated=recomputed, payload sha256 `73d1e0f2...fae4`, first16 `03000800a001000001001c00c4000000`, member_end=465.
- `classes.dex`: lho=465, payload_offset=506, csize=usize=**112**, crc32 `2635c82a` match, sha256 `57cfe887...548c2`, first16 `6465780a30333500300c123da5fc7bea`, member_end=618.
- `META-INF/MANIFEST.MF`: lho=618, payload_offset=668, csize=usize=**69**, crc32 `e948d738` match, sha256 `2e5da249...c0a49`, first16 `4d616e69666573742d56657273696f6e`, member_end=737=cd_off. Members contiguous, no gaps/overlaps. CD walk ends at 925=EOCD.

**AXML (items 4-8):** root hdr type=0x0003, headerSize=8, total=**416**==member size. Chunk table: (8,0x0001,28,**196**), (204,0x0180,8,44), (248,0x0100,16,**24**), (272,0x0102,16,96), (368,0x0103,16,24), (392,0x0101,16,24); walk ends at 416.
- String pool: count=**9**, styles=0, flags=`0x00000100` (UTF8_FLAG), stringsStart=64, stylesStart=0, offsets `[0,10,55,66,76,94,108,122,126]` — independently verified: each entry = 1B u16len + 1B u8len + len bytes (no NUL); my decoder produced identical strings `["android","http://schemas.android.com/apk/res/android","manifest","package","com.example.r65","versionCode","versionName","1","1.0"]` with utf16 lens `[7,42,8,7,15,11,11,1,3]`. Layout self-consistent: headerSize 28 + 9 offsets×4 = 64 = stringsStart; last string ends at 64+126+5=195, one pad byte → chunk size 196 (4-byte alignment hold).
- Resource map: 9 uint32 entries `[0×5, 0x0101021b, 0x0101021c, 0, 0]` at offset 204; 8+36=44=chunk size.
- Start element @272: line=1, ns_idx=`0xffffffff`(4294967295), name_idx=2→`manifest`, attributeStart=**20**, attributeSize=**20**, attributeCount=**3**, id/class/style idx=0. Attrs: (ns=0xffffffff, name=3→`package`, raw=4→`com.example.r65`, vsize=8, vzero=0, type=**0x03**, data=4); (ns=0→`android`, name=5→`versionCode`, raw=7→`1`, type=**0x10**, data=**1**); (ns=0, name=6→`versionName`, raw=8→`1.0`, type=0x03, data=8). res_id arithmetic: 0x0101021b=**16843291**, 0x0101021c=**16843292** — both confirmed.
- Start ns @248: line=1, prefix_idx=0→`android`, uri_idx=1→`http://schemas.android.com/apk/res/android`. End element @368: ns=0xffffffff, name_idx=2→`manifest`, line=1. End ns @392: same prefix/uri, line=1. All four node chunks lineNumber=1.

**Spec-derived widths (item 5):** recomputed sums — ResChunk_header 2+2+4=8, ResStringPool_header 2+2+4×5=28, ResXMLTree_node 2+2+4×3=16, ResXMLTree_attrExt 4×2+2×6=20, ResXMLTree_attribute 4×3+2+1+1+4=20, Res_value 2+1+1+4=8 — all equal the entry's `total_bytes` and match observed headerSize/attributeStart/attributeSize fields (28, 16, 20, 20). Field-list shapes agree with canonical AOSP `ResourceTypes.h` declarations [cross-check vs S038 text itself is out of this seat's byte-derivation scope].

**dex (item 9):** magic `6465780a30333500` = `dex\n035\0`; declared checksum at +8 `0x3d120c30` == `adler32(dex[12:])`; declared signature `a5fc7bea8fa9ffaa52243540c8026066511b9fce` == `sha1(dex[32:])`; file_size(+32)=**112**, header_size(+36)=**112**, endian_tag(+40)=`0x12345678`; bytes 44..112 all zero (consistent with "header only, not a valid dex program").

**JAR manifest (item 10):** 69 bytes ASCII = `"Manifest-Version: 1.0\r\nCreated-By: revenger-r65 fixture generator\r\n\r\n"` (20+2+44+2+1 — verified); first line `Manifest-Version: 1.0`; `\r\n\r\n` count=**1** section.

# Auxiliary claims verified

- 15 stdout lines from `python3 -B corpus/fixtures/apk-r65/readout.py`, exit 0, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — reproduced exactly. Fact ids: archive, spec_derived_struct_widths, eocd, member×3, axml_chunk_table, axml_string_pool, axml_resource_map, axml_start_namespace, axml_start_element, axml_end_element, axml_end_namespace, dex_declared_header, jar_manifest = **15**, matching the entry's "15 stdout lines" claim.
- Regeneration: `generator.py` copied to a scratch dir (`/tmp/r65gen`), run under host Python **3.14.8** → `fixture.apk` sha256 `05d2...d03e` and `truth.json` sha256 `2730...8173` byte-for-byte identical to committed bytes. The `verified-at` line's regen claim (incl. the `python_version` hedge — version matches, so no divergence) holds.
- File digests in header: fixture.apk `05d2...d03e` ✓, truth.json `27303bae...8173` ✓, generator.py `eaa9444c...7c1a` ✓, readout.py `92e347c3...c13976` ✓. S039 snapshot `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` sha256 `412d9cb4...74c` matches the entry's quoted prefix.
- `truth.json` agreement: all members' offset/size/crc/sha, the 9 strings, 3 attribute rows (name_idx/ns_idx/raw_value_idx/data_type/data = 3/-1/4/3/4; 5/0/7/16/1; 6/0/8/3/8), and resource_ids `[0×5,0x0101021b,0x0101021c,0,0]` agree field-for-field with my independent decode.

# Anomalies found (none load-bearing)

1. `axml_resource_map` JSON prints `nonzero` values as `0x101021b` (7 hex digits) while the prose and `ids` array use `0x0101021b` — formatting artifact of `f"0x{x: 08x}".replace(" ","")` in readout.py:175; same numeric value. Cosmetic, not a count failure.
2. Lane decoder at readout.py:159-161 assumes 1-byte u16len/u8len; correct here only because every string <128 chars. My independent 2-byte-aware decode agrees, so no number is wrong — but the readout silently mis-decodes a >127-char pool. Scope is one fixture; noted for the record, not a defect of the claims.
3. Entry line 1's S038 line-anchors (ResChunk_header line 218, etc.) and S039 anchor line 5 are upstream-source claims, not fixture bytes — outside this seat's re-derivation mandate (covered by source-checking seats).

# Verdict detail

Every attackable number — 947, 925, 737, 188, 3, 416, 49, 465, 506, 618, 668, 112, 69, 196, 44, 24, 96, 20, 9, 64, 0x00000100, offsets list, 0x0101021b, 0x0101021c, 16843291, 16843292, 0xffffffff/4294967295, 0x3d120c30, 0x12345678, a5fc7bea..., headerSize set {28,8,16}, attribute triples, 69-byte manifest, 1 section, 15 lines, all six digests — re-derives from committed bytes. **No FAIL items.** Axes impacted: none for C1 coverage (entry's numbers are exact); supports Q11 (every count/offset/digest re-derives by independent means).
