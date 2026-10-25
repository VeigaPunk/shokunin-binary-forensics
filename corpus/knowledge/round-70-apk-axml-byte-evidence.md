source: S038 — AOSP `ResourceTypes.h` (binary resource/XML format structures) — https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h (spec, tier A; row opened 2026-10-24 and mined round 65; re-opened 2026-10-25 by this entry's author from the committed snapshot `corpus/snapshots/ResourceTypes.h`, digest printed in item 14) — scope: the struct layout and chunk-type enum values of the compiled-XML (AXML) chunk stream for one authored binary `AndroidManifest.xml`; not the behavior of any parser — anchors: every S038 line number and enum value this entry states is printed by the item-11 command, none is typed by hand
source: S043 — supersedes S039 — REA reverse-engineer-anything skill reference, "Android application artifacts" (docs, tier A; row opened 2026-10-24, `queued` before this entry; re-opened 2026-10-25 by this entry's author from the committed snapshot `corpus/snapshots/rea-android-applications.md`, digest printed in item 14) — scope: the route-scope sentence only, what `inspect_android_package` is documented to take and return per rea-agents-6.5.0; not provider execution and not the fixture bytes — anchor: the quoted sentence is located by the item-11 `--spec-quotes` command (first line 7)
source: S045 — Android DEX format specification (AOSP, source.android.com) — https://source.android.com/docs/core/runtime/dex-format (docs, tier A; row opened 2026-10-24 and mined round 67; re-opened 2026-10-25 by this entry's author from the committed snapshot `corpus/snapshots/dex-format.html`, digest printed in item 14) — scope: the declared `header_item` field semantics of one authored `classes.dex` member (checksum, signature, header_size, endian_tag); not dex program validity — anchors: the four quoted phrases are located by the item-11 `--spec-quotes` command
source: S032 — PKWARE APPNOTE.TXT 6.3.10 — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row opened 2026-10-23 and mined round 63; re-opened 2026-10-25 by this entry's author: fetched and committed byte-for-byte as `corpus/snapshots/APPNOTE.TXT`, digest printed in item 14) — scope: the record layouts of §4.3.7 local file header (snapshot lines 387-398), §4.3.12 central directory file header (lines 511-531) and §4.3.16 end of central directory record (lines 632-646) for one authored ZIP archive; the field widths are MANUALLY transcribed in `corpus/fixtures/apk-r65/entry_checks.py` and the item-12 command sums them; no ZIP-parser or provider behavior is claimed
source: S034 — PKWARE APPNOTE.TXT 6.3.10 — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row opened 2026-10-23 and mined round 63, scoped re-open 2026-10-25 by this entry's author from the same snapshot) — scope: §4.3.7 local file header only: the fixed part and the file-name and extra-field length offsets the `payload_offset` derivation in item 3 rests on (item 12)
source: S047 — supersedes S046 — AXML anchor derivation (own-work, tier A; row opened 2026-10-25, round 69; re-opened 2026-10-25 by this entry's author by running it) — scope: the printed S038 line numbers and enum values listed in item 11, read from the pinned snapshot bytes; not the layout facts themselves, which rest on S038 — anchor: `corpus/derive_axml_anchors.py` and `corpus/snapshots/ResourceTypes.h`, digests printed in item 14
source: S041 — Authored apk-r65 bundle — `corpus/fixtures/apk-r65/fixture.apk`, `truth.json`, `generator.py`, `readout.py` (own-work, tier A; row opened 2026-10-24 and mined round 65) — scope: the byte content of this one authored fixture, its declared oracle and its readout script — anchors: the four digests printed in item 14; this entry does not re-run `generator.py`
verified-at: 2026-10-25 (round-70 build; every output block below was produced by running the command printed above it in this same build and pasting its stdout, by `.ufo/waves/round-70/build-entry.py`; the embedded-output gate `corpus/check_embedded_outputs.py --entry` and the lint `corpus/lint_entry.py --entry` both ran on the built bytes)
recheck: from the lane root, `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` (re-runs every `$` command below and requires every embedded line in its stdout; credited only for that clause), `python3 -B corpus/fixtures/apk-r65/readout.py` (item 15 prints its line count and digest) and the five `entry_checks.py` flags named in items 11-15
coverage-map: C05 (`corpus/README.md`, Android packages (APK)) — the container members, the binary-AXML `AndroidManifest.xml` and the `classes.dex` declared header of one authored APK fixture, read out byte by byte and compared field by field with the authored oracle. Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture.
admission-status: candidate

# Binary AXML manifest, container members and dex declared header of one authored APK — C05

Scope. One authored APK, `corpus/fixtures/apk-r65/fixture.apk`, and the authored oracle that declares it, `corpus/fixtures/apk-r65/truth.json`. The analysis is **manual**: a Python standard-library script reads the archive's bytes with `struct` and walks the ZIP central directory, the compiled-XML chunk stream and the dex header. Nothing is extracted to disk, executed or fetched at recheck time, and no producer is called.

## Observation

Every numbered item is produced by the command printed above its output. The readout script `corpus/fixtures/apk-r65/readout.py` is saved verbatim; its digest is item 14's.

**Archive and container**

1. The archive is a single file whose size and SHA-256 the readout computes from its bytes:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive
{"bytes": 947, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
```

2. The end-of-central-directory record is located by the readout's search for the four signature bytes (`readout.py:76`, constant `b"PK\x05\x06"`); the second command reads those four bytes back from the archive at the printed offset. The record states the central-directory entry count, size and start offset, and the readout compares the start plus the size with the record's own offset:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --eocd
eocd signature bytes at offset 925: 504b0506 (4 bytes)
```

3. The readout walks each central-directory record and its local header (record widths and field offsets are **recorded** from APPNOTE and checked against the readout source by item 12, not derived from the archive), reads each member's payload at `payload_offset = local_header_offset + 30 + name_length + extra_length` (`readout.py:105`) and recomputes its CRC-32:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[AndroidManifest.xml]
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[classes.dex]
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[META-INF/MANIFEST.MF]
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
```

The `payload_first16_hex` value printed for `META-INF/MANIFEST.MF` is a 32-hex-character run, which is 16 bytes; the item-10 command prints that member's first line.

**Compiled XML (AXML) member**

4. The readout walks the child chunks from the root chunk's own `headerSize` by adding each chunk's `size`; the table below is what it printed. The numeric `type` values are decimal here: 1 is `0x0001`, 384 is `0x0180`, 256 is `0x0100`, 258 is `0x0102`, 259 is `0x0103` and 257 is `0x0101`:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_chunk_table
{"chunks": [{"headerSize": 28, "offset": 8, "size": 196, "type": 1}, {"headerSize": 8, "offset": 204, "size": 44, "type": 384}, {"headerSize": 16, "offset": 248, "size": 24, "type": 256}, {"headerSize": 16, "offset": 272, "size": 96, "type": 258}, {"headerSize": 16, "offset": 368, "size": 24, "type": 259}, {"headerSize": 16, "offset": 392, "size": 24, "type": 257}], "fact": "axml_chunk_table", "xml_header_type": 3, "xml_total_size": 416, "xml_total_size_equals_member": true}
```

Item 11 prints the S038 enum lines carrying those same hexadecimal values (`RES_STRING_POOL_TYPE`, `RES_XML_RESOURCE_MAP_TYPE`, the start and end namespace types, the start and end element types); the correspondence between a chunk's printed `type` and an enum name is read by the reader from those two blocks. It is an inference from matching values, labeled so in the inference section.

5. The fixed structure widths the readout uses are a **manual transcription** of S038's struct field lists (`readout.py:51-58`), labeled manual and not read from `ResourceTypes.h` at run time; the readout prints the constants and their sums:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact spec_derived_struct_widths
{"attr_ext_attribute_start": 20, "attribute_size": 20, "bytes_per_field": {"ResChunk_header": [2, 2, 4], "ResStringPool_header": [2, 2, 4, 4, 4, 4, 4, 4], "ResXMLTree_attrExt": [4, 4, 2, 2, 2, 2, 2, 2], "ResXMLTree_attribute": [4, 4, 4, 2, 1, 1, 4], "ResXMLTree_node": [2, 2, 4, 4, 4], "Res_value": [2, 1, 1, 4]}, "fact": "spec_derived_struct_widths", "node_header_size": 16, "source_anchor": "S038 ResourceTypes.h struct field lists", "string_pool_header_size": 28, "total_bytes": {"ResChunk_header": 8, "ResStringPool_header": 28, "ResXMLTree_attrExt": 20, "ResXMLTree_attribute": 20, "ResXMLTree_node": 16, "Res_value": 8}}
```

The summed `attr_ext_attribute_start` 20 and `attribute_size` 20 are the values the start-element chunk states in item 8.

6. The string-pool chunk's header values and the strings the readout decodes from the offsets the pool states (`readout.py:164-168`; the UTF-8 flag position tested is `flags & 0x100`, `readout.py:166`):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_string_pool
{"fact": "axml_string_pool", "flags": "0x00000100", "offset": 8, "offsets": [0, 10, 55, 66, 76, 94, 108, 122, 126], "sorted_flag": false, "stringCount": 9, "strings": ["android", "http://schemas.android.com/apk/res/android", "manifest", "package", "com.example.r65", "versionCode", "versionName", "1", "1.0"], "stringsStart": 64, "styleCount": 0, "stylesStart": 0, "utf8": true}
```

7. The resource-map chunk holds one `uint32` per string; the readout prints them and the non-zero entries keyed by string. The two non-zero ids are compared with the oracle's declared ids in item 13; the zero entries are recorded as observed and no meaning for a zero entry is claimed:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_resource_map
{"entry_count": 9, "fact": "axml_resource_map", "ids": ["0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x0101021b", "0x0101021c", "0x00000000", "0x00000000"], "nonzero": {"versionCode": "0x101021b", "versionName": "0x101021c"}, "offset": 204}
```

8. The start-element chunk's printed `attributeStart`, `attributeSize` and `attributeCount` and its three attributes. Where the attributes are read: the readout computes `aoff = base + 16 + attribute_start + i * attribute_size` (`readout.py:203`), where `base` is the chunk's offset; the literal 16 equals the chunk's declared `headerSize` in item 4 and the `node_header_size` item 5 sums (an inference, labeled in the inference section). S038's comment on `attributeStart` (quoted and located by item 11) says the offset is counted from the start of the attrExt structure. The readout resolves each attribute's namespace by indexing the string pool directly with the attribute's own `ns_index` (`readout.py:211`, `strings[ans]`; `NO_INDEX` 0xFFFFFFFF at `readout.py:22` resolves to null). The start-namespace chunk is printed as a separate fact and the readout does not consult it when resolving attribute namespaces:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_element
{"attributeCount": 3, "attributeSize": 20, "attributeStart": 20, "attributes": [{"data_type": "0x03", "data_type_string": 4, "name": "package", "name_index": 3, "ns": null, "ns_index": 4294967295, "raw_value": "com.example.r65", "raw_value_index": 4, "res_id": 0, "value_size": 8}, {"data_type": "0x10", "data_type_int_dec": 1, "name": "versionCode", "name_index": 5, "ns": "android", "ns_index": 0, "raw_value": "1", "raw_value_index": 7, "res_id": 16843291, "value_size": 8}, {"data_type": "0x03", "data_type_string": 8, "name": "versionName", "name_index": 6, "ns": "android", "ns_index": 0, "raw_value": "1.0", "raw_value_index": 8, "res_id": 16843292, "value_size": 8}], "classIndex": 0, "element_name": "manifest", "element_name_index": 2, "element_ns": null, "element_ns_index": 4294967295, "fact": "axml_start_element", "idIndex": 0, "lineNumber": 1, "offset": 272, "styleIndex": 0}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_namespace
{"fact": "axml_start_namespace", "lineNumber": 1, "offset": 248, "prefix": "android", "prefix_index": 0, "uri": "http://schemas.android.com/apk/res/android", "uri_index": 1}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_end_element
{"fact": "axml_end_element", "lineNumber": 1, "name": "manifest", "name_index": 2, "ns_index": 4294967295, "offset": 368}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_end_namespace
{"fact": "axml_end_namespace", "lineNumber": 1, "offset": 392, "prefix": "android", "prefix_index": 0, "uri": "http://schemas.android.com/apk/res/android", "uri_index": 1}
```

**dex declared header**

9. The `classes.dex` member's declared header values and their recomputations, exactly as the readout prints them (`readout.py:233-248`). Each declared field is compared with the field semantics S045 states (the four quoted phrases are located by item 11); a match between a declared value and its recomputation shows the member's header is internally consistent, and nothing about dex program validity follows:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact dex_declared_header
{"checksum_matches": true, "checksum_recomputed": "0x3d120c30", "declared_checksum": "0x3d120c30", "endian_tag": "0x12345678", "fact": "dex_declared_header", "file_size": 112, "format_version": "035", "header_bytes": 112, "header_size": 112, "magic_ascii": "dex\n", "magic_hex": "6465780a30333500", "signature_matches": true, "signature_recomputed": "a5fc7bea8fa9ffaa52243540c8026066511b9fce", "signature_sha1": "a5fc7bea8fa9ffaa52243540c8026066511b9fce"}
```

**Text manifest**

10. The `META-INF/MANIFEST.MF` member's byte count, first line and section count as the readout prints them:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact jar_manifest
{"bytes": 69, "fact": "jar_manifest", "first_line": "Manifest-Version: 1.0", "section_count": 1}
```

**Spec anchors and recorded layouts (machine-derived where stated)**

11. Every S038 line number and enum value this entry states is printed by the committed derivation, which searches the pinned snapshot bytes for each cited symbol; its credit is bounded to exactly the lines it prints (the output below is the complete set). The second command locates each quoted spec phrase (S038's `attributeStart` comment, S043's route sentence, four S045 phrases) in its committed snapshot copy, tags stripped and whitespace folded, and prints the raw line the phrase's first words start on:

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
enum block open : 237
enum RES_STRING_POOL_TYPE : 239 = 0x0001
enum RES_XML_TYPE : 241 = 0x0003
enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
enum RES_XML_END_NAMESPACE_TYPE : 246 = 0x0101
enum RES_XML_START_ELEMENT_TYPE : 247 = 0x0102
enum RES_XML_END_ELEMENT_TYPE : 248 = 0x0103
enum RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180
enum block close : 263
comment attributeStart : 686
field attributeStart : 687
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes
MATCH rea-android-applications.md: first line 7, folded phrase present=True: Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.
MATCH dex-format.html: first line 5949, folded phrase present=True: adler32 checksum of the rest of the file (everything but magic and this field)
MATCH dex-format.html: first line 5956, folded phrase present=True: SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)
MATCH dex-format.html: first line 5981, folded phrase present=True: must be 0x70 (112) bytes (v40 or earlier)
MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;
MATCH ResourceTypes.h: first line 686, folded phrase present=True: Byte offset from the start of this structure where the attributes start
```

12. The ZIP field offsets the readout uses are summed here from the **manually transcribed** APPNOTE field widths (`entry_checks.py`, `LOCAL_HEADER`, `CENTRAL_HEADER`, `EOCD`; the layouts are APPNOTE snapshot lines 387-398, 511-531 and 632-646) and each is compared with the literal in the readout source. The widths are recorded, the sums and the presence checks are derived:

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout
local fixed part: 30 bytes (sum of the transcribed field widths)
central fixed part: 46 bytes (sum of the transcribed field widths)
eocd fixed part: 22 bytes (sum of the transcribed field widths)
MATCH eocd.total_entries: spec offset 10, readout.py literal `u16(apk, eocd + 10)` present=True
MATCH eocd.cd_size: spec offset 12, readout.py literal `u32(apk, eocd + 12)` present=True
MATCH eocd.cd_offset: spec offset 16, readout.py literal `u32(apk, eocd + 16)` present=True
MATCH central.name_length: spec offset 28, readout.py literal `u16(apk, cursor + 28)` present=True
MATCH central.extra_length: spec offset 30, readout.py literal `u16(apk, cursor + 30)` present=True
MATCH central.comment_length: spec offset 32, readout.py literal `u16(apk, cursor + 32)` present=True
MATCH central.local_header_offset: spec offset 42, readout.py literal `u32(apk, cursor + 42)` present=True
MATCH local.crc32: spec offset 14, readout.py literal `u32(apk, lh_off + 14)` present=True
MATCH local.compressed_size: spec offset 18, readout.py literal `u32(apk, lh_off + 18)` present=True
MATCH local.uncompressed_size: spec offset 22, readout.py literal `u32(apk, lh_off + 22)` present=True
MATCH local.name_length: spec offset 26, readout.py literal `u16(apk, lh_off + 26)` present=True
MATCH local.extra_length: spec offset 28, readout.py literal `u16(apk, lh_off + 28)` present=True
MATCH central.fixed_part: spec width 46, readout.py literal `cursor + 46` present=True
MATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True
```

13. The readout's facts compared field by field with the authored oracle `truth.json`; the oracle is emitted by `generator.py`, a separate code path from the readout. One line per compared field, every line printed:

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --oracle
MATCH image.sha256: readout='05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e' oracle='05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e'
MATCH image.size: readout=947 oracle=947
MATCH AndroidManifest.xml.local_header_offset: readout=0 oracle=0
MATCH AndroidManifest.xml.compressed_size: readout=416 oracle=416
MATCH AndroidManifest.xml.crc32: readout='962d075f' oracle='962d075f'
MATCH AndroidManifest.xml.sha256: readout='73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4' oracle='73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4'
MATCH classes.dex.local_header_offset: readout=465 oracle=465
MATCH classes.dex.compressed_size: readout=112 oracle=112
MATCH classes.dex.crc32: readout='2635c82a' oracle='2635c82a'
MATCH classes.dex.sha256: readout='57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2' oracle='57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2'
MATCH META-INF/MANIFEST.MF.local_header_offset: readout=618 oracle=618
MATCH META-INF/MANIFEST.MF.compressed_size: readout=69 oracle=69
MATCH META-INF/MANIFEST.MF.crc32: readout='e948d738' oracle='e948d738'
MATCH META-INF/MANIFEST.MF.sha256: readout='2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49' oracle='2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49'
MATCH axml.strings: readout=['android', 'http://schemas.android.com/apk/res/android', 'manifest', 'package', 'com.example.r65', 'versionCode', 'versionName', '1', '1.0'] oracle=['android', 'http://schemas.android.com/apk/res/android', 'manifest', 'package', 'com.example.r65', 'versionCode', 'versionName', '1', '1.0']
MATCH axml.resource_ids: readout=['0x00000000', '0x00000000', '0x00000000', '0x00000000', '0x00000000', '0x0101021b', '0x0101021c', '0x00000000', '0x00000000'] oracle=['0x00000000', '0x00000000', '0x00000000', '0x00000000', '0x00000000', '0x0101021b', '0x0101021c', '0x00000000', '0x00000000']
MATCH axml.attribute[0].name_index: readout=3 oracle=3
MATCH axml.attribute[0].ns_index: readout=4294967295 oracle=4294967295
MATCH axml.attribute[0].raw_value_index: readout=4 oracle=4
MATCH axml.attribute[0].data_type: readout=3 oracle=3
MATCH axml.attribute[1].name_index: readout=5 oracle=5
MATCH axml.attribute[1].ns_index: readout=0 oracle=0
MATCH axml.attribute[1].raw_value_index: readout=7 oracle=7
MATCH axml.attribute[1].data_type: readout=16 oracle=16
MATCH axml.attribute[2].name_index: readout=6 oracle=6
MATCH axml.attribute[2].ns_index: readout=0 oracle=0
MATCH axml.attribute[2].raw_value_index: readout=8 oracle=8
MATCH axml.attribute[2].data_type: readout=3 oracle=3
```

14. Digests and sizes of every file this entry's claims rest on, recomputed from bytes (a digest identifies exactly these bytes; it does not establish who produced them or that they are the upstream's current text):

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins
sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e 947 bytes corpus/fixtures/apk-r65/fixture.apk
sha256 27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173 2466 bytes corpus/fixtures/apk-r65/truth.json
sha256 eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a 9599 bytes corpus/fixtures/apk-r65/generator.py
sha256 92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976 11236 bytes corpus/fixtures/apk-r65/readout.py
sha256 74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa 4979 bytes corpus/derive_axml_anchors.py
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f 86255 bytes corpus/snapshots/ResourceTypes.h
sha256 0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6 174585 bytes corpus/snapshots/APPNOTE.TXT
sha256 c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4 281157 bytes corpus/snapshots/dex-format.html
sha256 412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c 1992 bytes corpus/snapshots/rea-android-applications.md
```

15. The readout's complete stdout, counted and hashed:

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest
readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```

## Observation / inference / unknown

- **Observation** — every value in items 1-15 is printed by the command above it from the committed bytes. Items 3, 5 and 12 depend on recorded or manually transcribed widths, each labeled where it is used.
- **Inference** — (a) a printed chunk `type` value equals the value of the S038 enum line item 11 prints for the named constant; (b) the literal 16 in `readout.py:203` is the start-element chunk's declared `headerSize` (item 4) and the summed node width (item 5); (c) the two non-zero resource-map entries are the two ids `truth.json` declares (item 13); (d) the dex header's declared checksum, signature, size and endian fields agree with S045's field semantics as quoted. Each inference cites its byte evidence and is scoped to this fixture.
- **Unknown** — nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed; the fixture is inert and no producer was called. The ZIP APPNOTE layouts are recorded from a snapshot; whether the upstream document has since changed is not checked.

## Limitations

One authored fixture, one manifest shape (a single element with three attributes), UTF-8 string pool only, no CDATA, no nested elements, no styles. The container is stored (method 0) with no data descriptors, so the walk does not exercise compression, split archives or spanned records. The dex member is a header only and is intentionally not a valid dex program. `readout.py:49-50` still comments that widths are "computed here ... not assumed"; the widths are a manual transcription (item 5), and the comment is the readout's own wording, not this entry's claim. Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence.

## Cross-lane scope note (Q10)

The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S043 only; this lane ran no provider and makes no readiness claim (Q05 fence). The kaidoku/revenger ADJ-06 overlap and the fleet `l0-questions.md` entry for it stay reported, not absorbed.

## §Q-map

| criterion | decision | basis |
|---|---|---|
| Q01 | pass | each load-bearing layout claim rests on a tier-A row for its own scope: S038 (AXML layout, re-opened this round), S045 (dex header semantics), S032/S034 (ZIP records), S047 and S041 (own-work, byte-derived), S043 (route scope only). No tier-C row supports a claim. |
| Q02 | pass | the header carries `source:` for S038, S043, S045, S032, S034, S047 and S041 with anchors, `verified-at:`, `recheck:` and `coverage-map:` naming C05. |
| Q03 | pass | expected values come from bytes or from the authored oracle emitted by a separate script (item 13), or from a printed spec line (item 11); none is copied from the record under test. |
| Q04 | pass | no tool claim: the readout is manual standard-library byte analysis, the widths are labeled manual (items 5, 12), and the derivation script's credit is bounded to the lines it prints (item 11). |
| Q05 | pass | no readiness or capability claim; the provider route is fenced to S043's documented scope and this entry makes no statement about any exit status of any refusal path. |
| Q06 | pass | the fixture premises are digest-printed from the built bytes (item 14); the entry does not re-run the generator and says so in the S041 header line. |
| Q07 | pass | no parser-behavior prediction is made; the namespace sentence in item 8 describes how this readout resolves this fixture, by the cited source lines. |
| Q08 | n/a | superseded by Q11 in `corpus/QUALITY.md`; the Q11 row below carries the decision. |
| Q09 | pass | every digest is claimed only for the bytes it hashed and none is offered as origin, completeness or authenticity (item 14's sentence). |
| Q10 | pass | scope is one fixture; cross-lane contested scope is named at the note above and not absorbed. |
| Q11 | pass | every count, offset, identifier and digest carries its deriving command and output in items 1-15; the recorded values (APPNOTE widths) are labeled recorded where used; no value is cited only to prose. |
| Q12 | n/a | this entry writes no rejected-source row. |
| Q13 | pass | the embedded-output gate is credited only for the clause that every embedded line appears in its command's stdout; the `MATCH`/`MISMATCH` lines are credited only for the comparisons each prints; no verifier is credited for a clause its own run does not detect. |
| Q14 | pass | the only prose byte count attached to a hex run is the 16-byte statement under item 3 for a 32-hex-character run; every other hex string is printed inside a command block and carries no prose count. |
| Q15 | pass | this entry states no git object id; identity statements are file digests printed by item 14. |

## Reproduce

From the lane root:

```sh
python3 -B corpus/fixtures/apk-r65/readout.py
```

Exit 0 and 15 stdout lines; item 15 prints their count and digest. Single-fact form: `python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd`. The five derivation flags are `--pins`, `--eocd`, `--oracle`, `--zip-layout`, `--spec-quotes` and `--stdout-digest` of `corpus/fixtures/apk-r65/entry_checks.py`.
