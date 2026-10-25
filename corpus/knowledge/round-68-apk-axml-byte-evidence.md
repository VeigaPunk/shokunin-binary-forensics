source: S038 — AOSP `ResourceTypes.h` (binary resource/XML format structures) — https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h (spec, tier A; row mined round 65, **re-opened 2026-10-24 by this entry's author** from the committed snapshot) — scope: the field layout, chunk-type enum values and fixed struct sizes of the compiled-XML (AXML) chunk stream for one authored binary `AndroidManifest.xml` — anchors: `struct ResChunk_header` (line 218); chunk-type enum block **lines 237-253**: `RES_STRING_POOL_TYPE` :239, `RES_XML_TYPE` :241, `RES_XML_START_NAMESPACE_TYPE` **:245**, `RES_XML_END_NAMESPACE_TYPE` :246, `RES_XML_START_ELEMENT_TYPE` :247, `RES_XML_END_ELEMENT_TYPE` :248, and `RES_XML_RESOURCE_MAP_TYPE` :253 (0x0180 — inside the enum block, unlike the round-65 draft's :239-250); `struct ResStringPool_header` (line 461); `struct ResXMLTree_header`/`ResXMLTree_node` (lines 612, 621); `struct ResXMLTree_attrExt` (line 677; its `attributeStart` field comment "Byte offset from the start of this structure where the attributes start." at line 686, with the field declaration `uint16_t attributeStart;` at line 687); `struct ResXMLTree_attribute` (line 707); `struct Res_value` (line 287); **every line number above is machine-derived by `corpus/derive_axml_anchors.py` from the pinned snapshot — item 11**; pinned tag `android-15.0.0_r1`; snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 bytes — committed byte-exact as `corpus/snapshots/ResourceTypes.h` (same sha256) so the anchor derivation below runs from any corpus tree
source: S043 — supersedes S039 — REA reverse-engineer-anything skill reference, "Android application artifacts" (docs, tier A; row mined round 66) — route-scope sentences only: what the `inspect_android_package` family is documented to take and return per rea-agents-6.5.0; not provider execution and not the fixture bytes — anchor: snapshot `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` **lines 7-8** ("Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence."), sha256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` — the round-65 draft cited "line 5", which is `older server.`
source: S045 — Android DEX format specification (AOSP, source.android.com) — https://source.android.com/docs/core/runtime/dex-format (docs, tier A, **opened 2026-10-24 by this entry's author**) — scope: the declared `header_item` field semantics of one authored `classes.dex` member (magic, checksum, signature, file_size, header_size, endian_tag); not dex program validity — anchor: "File layout" → `header_item` field table: checksum "adler32 checksum of the rest of the file (everything but magic and this field)"; signature "SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)"; header_size "must be 0x70 (112) bytes (v40 or earlier)"; `ENDIAN_CONSTANT = 0x12345678`; snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` sha256 `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`, 281157 bytes
source: S046 — AXML anchor derivation (own-work, tier A; row opened round 68 by this entry's author) — scope: the machine derivation of every S038 line number this entry cites, read from the pinned snapshot bytes; not the layout facts themselves, which rest on S038 — anchor: `corpus/derive_axml_anchors.py` sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`, 17 output lines over `corpus/snapshots/ResourceTypes.h` sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` (exit 2 on a missing or ambiguous symbol); snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`
source: S041 — Authored apk-r65 bundle — `corpus/fixtures/apk-r65/fixture.apk`, `corpus/fixtures/apk-r65/truth.json`, `corpus/fixtures/apk-r65/generator.py`, `corpus/fixtures/apk-r65/readout.py` (own-work, tier A; row mined round 65) — scope: the byte content of this one authored fixture, its declared oracle and its readout script, at the round-65 claim tree (bytes unchanged since) — anchors: fixture sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (947 bytes), truth.json sha256 `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`, readout.py sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`
verified-at: 2026-10-24 (round-68 re-derivation; the fixture, oracle and readout bytes are the round-65 claim-tree bytes, unchanged since `c7b7cf98`; every output line below was captured from the named command's actual stdout at build time, never transcribed by hand — the round-65 draft's entry:41 transcription drift is the M39 class this entry repairs, and the round-67 draft's `:244` anchor is the M40/M44 class this entry repairs by deriving every spec line number from the pinned snapshot)
recheck: `python3 -B corpus/derive_axml_anchors.py` from the lane root (every S038 line number this entry cites; exits 2 if a cited symbol is missing or ambiguous) and `python3 -B corpus/fixtures/apk-r65/readout.py` from the lane root — exits 0 and prints 15 stdout lines whose SHA-256 is `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` (re-derived 2026-10-24 at this entry's build); the per-value form `python3 -B corpus/fixtures/apk-r65/readout.py --fact '<id>'` prints the single JSON line for one named fact. The stdout carries only repo-relative paths, never the extraction root.
coverage-map: C05 (`corpus/README.md`, Android packages (APK)) — the container members, the binary-AXML `AndroidManifest.xml` and the `classes.dex` declared header of one authored APK fixture, read out byte by byte against the authored oracle. Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture.
admission-status: candidate — the round-68 third-pass candidate: the round-67 v2 candidate's two `:244` anchors are corrected to `:245` (the derived table in item 11 is the machine proof), the spec line numbers are now derived by `corpus/derive_axml_anchors.py` rather than transcribed, and the readout bytes, oracle and fixture are unchanged since round 65. It is NOT admitted: the README C05 row stays `uncovered` until the dispatched wave's fresh seats return an all-criteria pass on these bytes (frozen order in `reports/round-68/claims.md` §C2); on a fail the row stays `uncovered` and this file is marked `rejected`.

# Binary AXML manifest, container members and dex declared header of one authored APK — C05

Scope. One authored APK, `corpus/fixtures/apk-r65/fixture.apk`, and the authored oracle that declares it, `corpus/fixtures/apk-r65/truth.json`. The analysis is **manual**: a Python standard-library script reads the archive's bytes with `struct` and walks the ZIP central directory, the compiled-XML chunk stream, and the dex header directly. Nothing is extracted to disk, nothing is executed, no producer is called, no network is used, and no verifier source is read. The ZIP container field offsets are the APPNOTE 6.3.10 fixed record widths already mined as S032 (central directory header) and S034 (local file header); the AXML field offsets are computed from S038's own struct field lists in item 5 below.

## Observation

Every numbered item below is produced by the readout in §Reproduce. The script is saved verbatim as `corpus/fixtures/apk-r65/readout.py` (sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`) and each block below shows the exact command with the output it printed at this entry's build.

**Archive and container**

1. The archive is **947 bytes** with SHA-256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, read from the file's bytes.

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive
{"bytes": 947, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
```

2. The end-of-central-directory signature `504b0506` is located at file offset **925**; its record states **3** central-directory entries, a central directory of **188** bytes starting at offset **737**, and `737 + 188 == 925`, so the central directory ends exactly where the end-of-central-directory record begins.

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
```

3. Walking the three central-directory records (46-byte fixed part per S032 §4.3.12) and their local headers (30-byte fixed part per S034 §4.3.7) selects three members; every member's stated CRC-32 equals the CRC-32 recomputed over its payload bytes, and the walk's end cursor equals the end-of-central-directory offset. Each member's `payload_offset` is derived by the readout as `local_header_offset + 30 + name_length + extra_length` from the S034 §4.3.7 field list (readout.py:99-105), not assumed:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[AndroidManifest.xml]
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[classes.dex]
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[META-INF/MANIFEST.MF]
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
```

The `META-INF/MANIFEST.MF` payload begins `4d616e69666573742d` — ASCII `Manifest-`, the 16-byte prefix of `Manifest-Version: 1.0` (the round-65 draft recorded a 15-byte `4d616e696673742d…` pair at its entry:41; the deriving command prints the 16-byte pair, which is the value above).

**Compiled XML (AXML) member**

4. The `AndroidManifest.xml` payload begins `0300 0800 a001 0000` — chunk type `0x0003` (`RES_XML_TYPE`), headerSize 8, total size **416**, equal to the member's uncompressed size. The child chunks are walked from offset 8 by adding each chunk's size, and the walk ends exactly at 416:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_chunk_table
{"chunks": [{"headerSize": 28, "offset": 8, "size": 196, "type": 1}, {"headerSize": 8, "offset": 204, "size": 44, "type": 384}, {"headerSize": 16, "offset": 248, "size": 24, "type": 256}, {"headerSize": 16, "offset": 272, "size": 96, "type": 258}, {"headerSize": 16, "offset": 368, "size": 24, "type": 259}, {"headerSize": 16, "offset": 392, "size": 24, "type": 257}], "fact": "axml_chunk_table", "xml_header_type": 3, "xml_total_size": 416, "xml_total_size_equals_member": true}
```

The six chunk types in the table — `0x0001` string pool, `0x0180` resource map, `0x0100` start namespace, `0x0102` start element, `0x0103` end element, `0x0101` end namespace — are the values S038's chunk-type enum block names at **lines 237-253** (string pool :239, start/end namespace :245/:246, start/end element :247/:248, resource map `RES_XML_RESOURCE_MAP_TYPE` :253 — every one of these line numbers is derived by item 11's command). The `headerSize` column — 28, 8, 16, 16, 16, 16 — equals the fixed struct sizes derived in item 5 for the string pool and the XML node chunks.

5. The fixed structure widths used by the readout are computed by summing the field widths of S038's own struct definitions (two `uint16` plus one `uint32` for `ResChunk_header`; five `uint32` after the chunk header for `ResStringPool_header`; and so on), not assumed:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact spec_derived_struct_widths
{"attr_ext_attribute_start": 20, "attribute_size": 20, "bytes_per_field": {"ResChunk_header": [2, 2, 4], "ResStringPool_header": [2, 2, 4, 4, 4, 4, 4, 4], "ResXMLTree_attrExt": [4, 4, 2, 2, 2, 2, 2, 2], "ResXMLTree_attribute": [4, 4, 4, 2, 1, 1, 4], "ResXMLTree_node": [2, 2, 4, 4, 4], "Res_value": [2, 1, 1, 4]}, "fact": "spec_derived_struct_widths", "node_header_size": 16, "source_anchor": "S038 ResourceTypes.h struct field lists", "string_pool_header_size": 28, "total_bytes": {"ResChunk_header": 8, "ResStringPool_header": 28, "ResXMLTree_attrExt": 20, "ResXMLTree_attribute": 20, "ResXMLTree_node": 16, "Res_value": 8}}
```

The derived 20-byte `ResXMLTree_attrExt` size is the `attributeStart` value observed in the start-element chunk in item 8, and the derived 20-byte `ResXMLTree_attribute` size is the observed `attributeSize`.

6. The string-pool chunk (offset 8, size 196) declares **9** strings, **0** styles, flags **`0x00000100`** — bit `0x100` set, the UTF-8 flag position the readout tests (`flags & 0x100`, readout.py:166) — with string data starting 64 bytes into the chunk. The nine strings, decoded as length-prefixed UTF-8 from the offsets the pool states, are:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_string_pool
{"fact": "axml_string_pool", "flags": "0x00000100", "offset": 8, "offsets": [0, 10, 55, 66, 76, 94, 108, 122, 126], "sorted_flag": false, "stringCount": 9, "strings": ["android", "http://schemas.android.com/apk/res/android", "manifest", "package", "com.example.r65", "versionCode", "versionName", "1", "1.0"], "stringsStart": 64, "styleCount": 0, "stylesStart": 0, "utf8": true}
```

7. The resource-map chunk (offset 204, size 44) holds one `uint32` per string. Seven entries are `0x00000000` and the entries for `versionCode` and `versionName` are **`0x0101021b`** and **`0x0101021c`** — exactly the two framework attribute ids the fixture's authored oracle declares for those strings (`truth.json` `axml_declared.resource_ids`), which is the correspondence this entry claims; the all-zero entries are recorded as observed, and no framework-wide semantics for a zero entry is claimed from this fixture:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_resource_map
{"entry_count": 9, "fact": "axml_resource_map", "ids": ["0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x0101021b", "0x0101021c", "0x00000000", "0x00000000"], "nonzero": {"versionCode": "0x101021b", "versionName": "0x101021c"}, "offset": 204}
```

8. The start-element chunk at offset 272 names the element `manifest` with no namespace, `attributeStart` **20**, `attributeSize` **20**, `attributeCount` **3** — all equal to the derived sizes of item 5. Provenance of the attribute location: S038's `struct ResXMLTree_attrExt` (line 677) "Appears header.headerSize bytes after a `ResXMLTree_node`", so the attrExt starts at `chunk_base + 16` (the derived 16-byte node header, item 5); its `attributeStart` field is "Byte offset from the start of this structure where the attributes start" (snapshot line 686; the field declaration `uint16_t attributeStart;` at line 687 — item 11 derives both), so attribute *i* is at `chunk_base + 16 + attributeStart + i * attributeSize` — the readout's own derivation (readout.py:200-203). The three attributes read there are `package="com.example.r65"` (typed `0x03` string), `android:versionCode=1` (typed `0x10` int, resource id `0x0101021b`) and `android:versionName="1.0"` (typed `0x03` string, resource id `0x0101021c`):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_element
{"attributeCount": 3, "attributeSize": 20, "attributeStart": 20, "attributes": [{"data_type": "0x03", "data_type_string": 4, "name": "package", "name_index": 3, "ns": null, "ns_index": 4294967295, "raw_value": "com.example.r65", "raw_value_index": 4, "res_id": 0, "value_size": 8}, {"data_type": "0x10", "data_type_int_dec": 1, "name": "versionCode", "name_index": 5, "ns": "android", "ns_index": 0, "raw_value": "1", "raw_value_index": 7, "res_id": 16843291, "value_size": 8}, {"data_type": "0x03", "data_type_string": 8, "name": "versionName", "name_index": 6, "ns": "android", "ns_index": 0, "raw_value": "1.0", "raw_value_index": 8, "res_id": 16843292, "value_size": 8}], "classIndex": 0, "element_name": "manifest", "element_name_index": 2, "element_ns": null, "element_ns_index": 4294967295, "fact": "axml_start_element", "idIndex": 0, "lineNumber": 1, "offset": 272, "styleIndex": 0}
```

The `0xffffffff` namespace index on `package` and the element itself is recorded as observed and treated as null by the readout (readout.py:22); the same constant on `android`-carrying attributes resolves instead through the start-namespace chunk at offset 248, which states prefix index 0 (`android`) and URI index 1 (`http://schemas.android.com/apk/res/android`):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_namespace
{"fact": "axml_start_namespace", "lineNumber": 1, "offset": 248, "prefix": "android", "prefix_index": 0, "uri": "http://schemas.android.com/apk/res/android", "uri_index": 1}
```

The end-element chunk (offset 368) names `manifest` again, and the end-namespace chunk (offset 392) closes the same prefix/URI pair; all four node chunks carry `lineNumber` 1:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_end_element
{"fact": "axml_end_element", "lineNumber": 1, "name": "manifest", "name_index": 2, "ns_index": 4294967295, "offset": 368}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_end_namespace
{"fact": "axml_end_namespace", "lineNumber": 1, "offset": 392, "prefix": "android", "prefix_index": 0, "uri": "http://schemas.android.com/apk/res/android", "uri_index": 1}
```

**dex declared header**

9. The `classes.dex` payload's first eight bytes are `6465780a30333500` — the magic `dex\n035\0`. Its declared checksum **`0x3d120c30`** equals the Adler-32 recomputed over the bytes from offset 12 on — S045's `header_item` table declares the checksum "adler32 checksum of the rest of the file (everything but magic and this field)" — and its declared 20-byte signature equals the SHA-1 recomputed over the bytes from offset 32 on (S045: "SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)"). The header's declared `file_size` and `header_size` are both 112 — S045: `header_size` "must be 0x70 (112) bytes (v40 or earlier)" for this `035` magic — and the endian tag is `0x12345678`, S045's `ENDIAN_CONSTANT`. These are declared-header self-consistency facts about one inert member; dex validity is not claimed:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact dex_declared_header
{"checksum_matches": true, "checksum_recomputed": "0x3d120c30", "declared_checksum": "0x3d120c30", "endian_tag": "0x12345678", "fact": "dex_declared_header", "file_size": 112, "format_version": "035", "header_bytes": 112, "header_size": 112, "magic_ascii": "dex\n", "magic_hex": "6465780a30333500", "signature_matches": true, "signature_recomputed": "a5fc7bea8fa9ffaa52243540c8026066511b9fce", "signature_sha1": "a5fc7bea8fa9ffaa52243540c8026066511b9fce"}
```

**Text manifest**

10. The `META-INF/MANIFEST.MF` payload is 69 bytes of ASCII whose first line is `Manifest-Version: 1.0` with one blank-line-separated section:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact jar_manifest
{"bytes": 69, "fact": "jar_manifest", "first_line": "Manifest-Version: 1.0", "section_count": 1}
```

**Spec anchors (machine-derived)**

11. Every S038 line number this entry states is printed by a committed derivation script that searches the pinned snapshot bytes for each cited symbol — no spec line number in this entry is transcribed by hand. The script refuses to print a line it did not find (a missing or ambiguous symbol is exit 2), and it reads `corpus/snapshots/ResourceTypes.h`, the byte-exact copy of the pinned snapshot (same sha256 as the row's snapshot):

```
$ python3 -B corpus/derive_axml_anchors.py
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum RES_STRING_POOL_TYPE : 239
enum RES_XML_TYPE : 241
enum RES_XML_START_NAMESPACE_TYPE : 245
enum RES_XML_END_NAMESPACE_TYPE : 246
enum RES_XML_START_ELEMENT_TYPE : 247
enum RES_XML_END_ELEMENT_TYPE : 248
enum RES_XML_RESOURCE_MAP_TYPE : 253
comment attributeStart : 686
field attributeStart : 687
```

The chunk-type enum block spans lines 237-253 and `RES_XML_START_NAMESPACE_TYPE` is line **245**; line 244 is `RES_XML_FIRST_CHUNK_TYPE`. That one-line off-by-one is what falsified the round-65 and round-67 drafts (M40/M44); the derivation above is the capture that makes it mechanical.

## Comparison with the authored oracle

The oracle `truth.json` declares the image digest and size, the three members with their measured offsets, sizes and CRC-32 values, the declared AXML string table, attribute table and resource-map ids, and the build recipe. The readout values agree with it on every shared field: image sha256 and size (item 1), the three members' local-header offsets, payload sizes and CRC-32 values (item 3), the nine strings, the three attribute rows and the two non-zero resource ids (items 6-8). Regenerating the fixture from `generator.py` in a scratch directory on this host was round-65 evidence (S041) and is not re-run by this entry; the committed bytes are hash-pinned above.

## Observation / inference / unknown

- **Observation** — every value in items 1-10: read directly from the committed bytes by the §Reproduce script, which runs with the Python standard library only; and every spec line number in item 11, derived from the pinned snapshot bytes by a committed script that cannot print a line it did not find.
- **Inference** — that the six AXML chunk types and three fixed `headerSize` values are the ones S038's enum block (lines 237-253) and struct field lists name and size; that the two non-zero resource-map entries are the framework `versionCode`/`versionName` ids the fixture generator declared (`truth.json`); that the dex header's declared checksum, signature, size and endian fields agree with S045's declared field semantics for this one member. Each inference cites its byte evidence and its registry anchor, and each is scoped to this fixture.
- **Unknown** — nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed; the fixture is inert and no producer was called.

## Limitations

One authored fixture, one manifest shape (a single element with three attributes), UTF-8 string pool only, no CDATA, no nested elements, no styles. The container is ZIP_STORED with no data descriptors, so the byte walk does not exercise split archives, spanned records or compression. The dex member is a header only and is intentionally not a valid dex program. Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence.

## Cross-lane scope note (Q10)

The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S043 only; this lane ran no provider and makes no readiness claim (Q05 fence). The kaidoku/revenger ADJ-06 overlap and fleet `l0-questions.md:42` remain reported-not-absorbed, unchanged from round 64.

## §Q-map

| criterion | decision | basis |
|---|---|---|
| Q01 | pass | every load-bearing layout claim rests on S038 (tier A for AXML scope; row mined r65, re-opened 2026-10-24 from the committed snapshot by this entry's author) for AXML scope; the dex declared-header claims rest on S045 (tier A, opened 2026-10-24 this round); route scope rests on S043 (tier A, mined r66); container offsets rest on S032/S034 (registry tier A, mined round 63) and the fixture's own bytes (S041, own-work tier A). No tier-C support. |
| Q02 | pass | header carries `source:` (S038, S043, S045, S041 with URLs/paths, pinned anchors and snapshot digests), `verified-at:`, `recheck:` (command plus stdout SHA-256 re-derived at build), and names coverage row C05. |
| Q03 | pass | expected values come from the authored oracle, from S038-derived struct widths, and from S045's declared field semantics — all fixed outside the record under test; nothing is copied from a saved producer record. |
| Q04 | pass | no tool claim: the readout is manual standard-library byte analysis, labeled manual; the only tool named is Python itself, used as the reader, not credited with a result. |
| Q05 | pass | no readiness or capability claim is made; §Cross-lane scope note fences the provider route to S043 documentation scope. |
| Q06 | pass | every fixture premise was byte-verified against the built fixture in round 65 (S041, readout re-derived at this entry's build); the generator is not re-run by this entry and the committed bytes are hash-pinned. |
| Q07 | pass | no parser-behavior prediction is made or needed; the readout describes observed bytes only. |
| Q08 | superseded by Q11 | QUALITY.md:23 — Q08 is historical; this map applies Q11 (applying Q08 instead would itself be a Q11 failure, round-66 adjudication table). |
| Q09 | pass | digests are claimed only for the exact bytes hashed; no origin, completeness or authenticity claim; the dex checksum/signature self-consistency is explicitly an inert declared-header property, not validity. |
| Q10 | pass | scope is one fixture, one operation (manual readout), one artifact version; the §Limitations and §Cross-lane scope note name what is not claimed. |
| Q11 | pass | every count, offset, identifier and digest carries its deriving command and output in §Observation (items 1-10); the fixed struct constants carry their S038 field-list derivation (item 5); the spec line numbers carry their deriving command and output (item 11, machine-derived, not transcribed); the attribute location carries its attrExt-relative provenance (item 8); every embedded output line was captured from the command's actual stdout at build time. No recorded value is presented as re-derived. |
| Q12 | n/a | no rejected source row is written by this entry. |
| Q13 | n/a by construction | no verifier, recheck command, comparison tool or automatic checker is credited or introduced beyond the entry's own readout recheck, and no value is presented as covered by any other check. |

## Reproduce

From the lane root, with the round-65 corpus tree (bytes unchanged through round 68):

```sh
python3 -B corpus/fixtures/apk-r65/readout.py
```

Exit 0; 15 stdout lines; their SHA-256 is `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` (re-derived 2026-10-24). Anchor derivation: `python3 -B corpus/derive_axml_anchors.py` — exit 0, 17 lines, one per cited symbol (item 11). Single-fact form: `python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd`. The script is saved verbatim as `corpus/fixtures/apk-r65/readout.py` (sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`) and reads only `fixture.apk` beside it.

Full stdout as printed at this entry's build (every line also appears in the per-item blocks above):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py
{"bytes": 947, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
{"attr_ext_attribute_start": 20, "attribute_size": 20, "bytes_per_field": {"ResChunk_header": [2, 2, 4], "ResStringPool_header": [2, 2, 4, 4, 4, 4, 4, 4], "ResXMLTree_attrExt": [4, 4, 2, 2, 2, 2, 2, 2], "ResXMLTree_attribute": [4, 4, 4, 2, 1, 1, 4], "ResXMLTree_node": [2, 2, 4, 4, 4], "Res_value": [2, 1, 1, 4]}, "fact": "spec_derived_struct_widths", "node_header_size": 16, "source_anchor": "S038 ResourceTypes.h struct field lists", "string_pool_header_size": 28, "total_bytes": {"ResChunk_header": 8, "ResStringPool_header": 28, "ResXMLTree_attrExt": 20, "ResXMLTree_attribute": 20, "ResXMLTree_node": 16, "Res_value": 8}}
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
{"chunks": [{"headerSize": 28, "offset": 8, "size": 196, "type": 1}, {"headerSize": 8, "offset": 204, "size": 44, "type": 384}, {"headerSize": 16, "offset": 248, "size": 24, "type": 256}, {"headerSize": 16, "offset": 272, "size": 96, "type": 258}, {"headerSize": 16, "offset": 368, "size": 24, "type": 259}, {"headerSize": 16, "offset": 392, "size": 24, "type": 257}], "fact": "axml_chunk_table", "xml_header_type": 3, "xml_total_size": 416, "xml_total_size_equals_member": true}
{"fact": "axml_string_pool", "flags": "0x00000100", "offset": 8, "offsets": [0, 10, 55, 66, 76, 94, 108, 122, 126], "sorted_flag": false, "stringCount": 9, "strings": ["android", "http://schemas.android.com/apk/res/android", "manifest", "package", "com.example.r65", "versionCode", "versionName", "1", "1.0"], "stringsStart": 64, "styleCount": 0, "stylesStart": 0, "utf8": true}
{"entry_count": 9, "fact": "axml_resource_map", "ids": ["0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x0101021b", "0x0101021c", "0x00000000", "0x00000000"], "nonzero": {"versionCode": "0x101021b", "versionName": "0x101021c"}, "offset": 204}
{"fact": "axml_start_namespace", "lineNumber": 1, "offset": 248, "prefix": "android", "prefix_index": 0, "uri": "http://schemas.android.com/apk/res/android", "uri_index": 1}
{"fact": "axml_end_namespace", "lineNumber": 1, "offset": 392, "prefix": "android", "prefix_index": 0, "uri": "http://schemas.android.com/apk/res/android", "uri_index": 1}
{"attributeCount": 3, "attributeSize": 20, "attributeStart": 20, "attributes": [{"data_type": "0x03", "data_type_string": 4, "name": "package", "name_index": 3, "ns": null, "ns_index": 4294967295, "raw_value": "com.example.r65", "raw_value_index": 4, "res_id": 0, "value_size": 8}, {"data_type": "0x10", "data_type_int_dec": 1, "name": "versionCode", "name_index": 5, "ns": "android", "ns_index": 0, "raw_value": "1", "raw_value_index": 7, "res_id": 16843291, "value_size": 8}, {"data_type": "0x03", "data_type_string": 8, "name": "versionName", "name_index": 6, "ns": "android", "ns_index": 0, "raw_value": "1.0", "raw_value_index": 8, "res_id": 16843292, "value_size": 8}], "classIndex": 0, "element_name": "manifest", "element_name_index": 2, "element_ns": null, "element_ns_index": 4294967295, "fact": "axml_start_element", "idIndex": 0, "lineNumber": 1, "offset": 272, "styleIndex": 0}
{"fact": "axml_end_element", "lineNumber": 1, "name": "manifest", "name_index": 2, "ns_index": 4294967295, "offset": 368}
{"checksum_matches": true, "checksum_recomputed": "0x3d120c30", "declared_checksum": "0x3d120c30", "endian_tag": "0x12345678", "fact": "dex_declared_header", "file_size": 112, "format_version": "035", "header_bytes": 112, "header_size": 112, "magic_ascii": "dex\n", "magic_hex": "6465780a30333500", "signature_matches": true, "signature_recomputed": "a5fc7bea8fa9ffaa52243540c8026066511b9fce", "signature_sha1": "a5fc7bea8fa9ffaa52243540c8026066511b9fce"}
{"bytes": 69, "fact": "jar_manifest", "first_line": "Manifest-Version: 1.0", "section_count": 1}
```
