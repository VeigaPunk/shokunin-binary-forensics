source: S038 — AOSP `ResourceTypes.h` (binary resource/XML format structures) — https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h (spec, tier A; row opened 2026-10-24 and mined round 65; re-opened 2026-10-25 by this entry's author from the committed snapshot `corpus/snapshots/ResourceTypes.h`, digest printed in item 14) — scope: the struct layout and chunk-type enum values of the compiled-XML (AXML) chunk stream for one authored binary `AndroidManifest.xml`; not the behavior of any parser — anchors: every S038 line number and enum value this entry states is printed by the item-11 command, none is typed by hand
source: S049 — supersedes S043 — REA reverse-engineer-anything skill reference, "Android application artifacts" — https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md (docs, tier A; row opened 2026-10-25 by this entry's author, who re-fetched the raw file and compared it byte for byte with the committed snapshot `corpus/snapshots/rea-android-applications.md`, digest printed in item 14) — scope: the route-scope sentence only, what `inspect_android_package` is documented to take and return in that text; not provider execution and not the fixture bytes — anchor: the quoted sentence is located by the item-11 `--spec-quotes` command (first line 7)
source: S048 — supersedes S045 — Android DEX format specification (AOSP, source.android.com) — https://source.android.com/docs/core/runtime/dex-format (docs, tier A; row opened 2026-10-25 by this entry's author, who re-fetched the live page and compared it with the committed snapshot `corpus/snapshots/dex-format.html`, digest printed in item 14; the live page differs from the snapshot only in page-chrome lines) — scope: the declared `header_item` field semantics of one authored `classes.dex` member (checksum, signature, header_size, endian_tag); not dex program validity — anchors: the four quoted phrases are located by the item-11 `--spec-quotes` command; the `header_item` field table is under the heading "Items and related structures" and `ENDIAN_CONSTANT` under "Bitfield, string, and constant definitions"
source: S032 — PKWARE APPNOTE.TXT 6.3.10 — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row opened 2026-10-23 and mined round 63; re-opened 2026-10-25 by this entry's author from the committed snapshot copy `corpus/snapshots/APPNOTE.TXT`, digest printed in item 14; whether it still equals the upstream's current text is not claimed) — scope: the record layouts of §4.3.12 central directory file header and §4.3.16 end of central directory record for one authored ZIP archive, whose heading and field line numbers in the snapshot are printed by item 12; the field widths are MANUALLY transcribed in `corpus/fixtures/apk-r65/entry_checks.py` and the item-12 command sums them; no ZIP-parser or provider behavior is claimed
source: S034 — PKWARE APPNOTE.TXT 6.3.10 — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row opened 2026-10-23 and mined round 63, scoped re-open 2026-10-25 by this entry's author from the same snapshot) — scope: §4.3.7 local file header only: the fixed part and the file-name and extra-field length offsets the `payload_offset` derivation in item 3 rests on (item 12 prints the section's heading and field line numbers)
source: S047 — supersedes S046 — AXML anchor derivation (own-work, tier A; row opened 2026-10-25, round 69; re-opened 2026-10-25 by this entry's author by running it) — scope: the printed S038 line numbers and enum values listed in item 11, read from the pinned snapshot bytes; not the layout facts themselves, which rest on S038 — anchor: `corpus/derive_axml_anchors.py` and `corpus/snapshots/ResourceTypes.h`, digests printed in item 14
source: S041 — Authored apk-r65 bundle — `corpus/fixtures/apk-r65/fixture.apk`, `truth.json`, `generator.py`, `readout.py` (own-work, tier A; row opened 2026-10-24 and mined round 65) — scope: the byte content of this one authored fixture, its declared oracle and its readout script — anchors: the four digests printed in item 14, which also prints the digest of `entry_checks.py`; this entry does not re-run `generator.py`
source: S052 — round-71 `entry_checks.py --spec-quotes` output (own-work, tier A; opened 2026-10-27 by this entry's author from the committed `corpus/fixtures/apk-r65/entry_checks.py`) — scope: the output shape for the six cited AOSP/REA snapshot phrases, including file, first-line number, phrase-presence flag and searched phrase; not the raw source line — anchor: `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes`, output line for `dex-format.html` / `ENDIAN_CONSTANT` reproduced in item 11 and recorded in `corpus/lessons/round-71.md` `## Gate`
verified-at: 2026-10-27 (round-71 sixth-pass candidate; output blocks are retained byte-for-byte from round-70 v5.1 and re-run against the same committed fixture; prose repairs include the four round-70 failures plus the round-71 Q16/Q14 bounds on printed versus locators-only evidence)
recheck: from the lane root, `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` (re-runs every `$` command below and requires every embedded line in its stdout; credited only for that clause), `python3 -B corpus/fixtures/apk-r65/readout.py` (item 15 prints its line count and digest) and the `entry_checks.py` flags named in items 2 and 11-17
coverage-map: C05 (`corpus/README.md`, Android packages (APK)) — the container members, the binary-AXML `AndroidManifest.xml` and the `classes.dex` declared header of one authored APK fixture are read out byte by byte; selected member, AXML and DEX fields are compared with the authored oracle as enumerated in item 13. Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture.
admission-status: rejected — round-71 C1 falsified by fresh wave-2 decisions: Q09 (the Q-map claims an out-of-corpus builder is named undigested, but the named generator is inside `corpus/` and hashed) and Q16 (item 17 overstates which AXML read offsets its command compares; see `R71W2Q09Q12.md` and `R71W2Q13Q16.md`). Every other byte is preserved; README C05 remains uncovered.

# Binary AXML manifest, container members and dex declared header of one authored APK — C05

Scope. One authored APK, `corpus/fixtures/apk-r65/fixture.apk`, and the authored oracle that declares it, `corpus/fixtures/apk-r65/truth.json`. The analysis is **manual**: a Python standard-library script reads the archive's bytes with `struct` and walks the ZIP central directory, the compiled-XML chunk stream and the dex header. No archive member is extracted or executed, nothing is fetched and no producer is called at recheck time (the recheck commands run only the committed standard-library scripts named below).

## Observation

Every numbered item is produced by the command printed above its output. The readout script `corpus/fixtures/apk-r65/readout.py` is saved verbatim; its digest is item 14's.

**Archive and container**

1. The archive is a single file whose size and SHA-256 the readout computes from its bytes:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive
{"bytes": 947, "fact": "archive", "path": "corpus/fixtures/apk-r65/fixture.apk", "sha256": "05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e"}
```

2. The end-of-central-directory record is located by the readout's search for the four signature bytes (`readout.py:76`, constant `b"PK\x05\x06"`); the second command (`entry_checks.py`) locates the same signature on its own and prints the four bytes at the offset it finds, which equals the readout's offset. The record states the central-directory entry count, size and start offset, and the readout compares the start plus the size with the record's own offset:

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

Item 10's command prints the `META-INF/MANIFEST.MF` member's first line; item 16's command prints the general-purpose flags and compression method of every record.

**Compiled XML (AXML) member**

4. The readout walks the child chunks from the root chunk's own `headerSize` by adding each chunk's `size`; the table below is what it printed. The numeric `type` values are decimal here: 1 is `0x0001`, 384 is `0x0180`, 256 is `0x0100`, 258 is `0x0102`, 259 is `0x0103` and 257 is `0x0101`:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_chunk_table
{"chunks": [{"headerSize": 28, "offset": 8, "size": 196, "type": 1}, {"headerSize": 8, "offset": 204, "size": 44, "type": 384}, {"headerSize": 16, "offset": 248, "size": 24, "type": 256}, {"headerSize": 16, "offset": 272, "size": 96, "type": 258}, {"headerSize": 16, "offset": 368, "size": 24, "type": 259}, {"headerSize": 16, "offset": 392, "size": 24, "type": 257}], "fact": "axml_chunk_table", "xml_header_type": 3, "xml_total_size": 416, "xml_total_size_equals_member": true}
```

Item 11 prints the S038 enum lines carrying those hexadecimal values. The value `0x0100` is shared in that block by `RES_XML_FIRST_CHUNK_TYPE` and `RES_XML_START_NAMESPACE_TYPE`, so the chunk at offset 248 is identified as the start-namespace chunk by the item-8 `axml_start_namespace` fact, not by its value alone; the other five correspondences are inferences from matching values, labeled so in the inference section.

5. The fixed structure widths the readout prints are a **manual transcription** of S038's struct field lists (`readout.py:51-58`), labeled manual and not read from `ResourceTypes.h` at run time; the readout prints the constants and their sums, and item 17 compares only the AXML literal offsets it prints with these sums. It does not compare every readout offset: `readout.py:189` (`lineNumber`) and `:197` (`styleIndex`) are locators-only, not comparisons:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact spec_derived_struct_widths
{"attr_ext_attribute_start": 20, "attribute_size": 20, "bytes_per_field": {"ResChunk_header": [2, 2, 4], "ResStringPool_header": [2, 2, 4, 4, 4, 4, 4, 4], "ResXMLTree_attrExt": [4, 4, 2, 2, 2, 2, 2, 2], "ResXMLTree_attribute": [4, 4, 4, 2, 1, 1, 4], "ResXMLTree_node": [2, 2, 4, 4, 4], "Res_value": [2, 1, 1, 4]}, "fact": "spec_derived_struct_widths", "node_header_size": 16, "source_anchor": "S038 ResourceTypes.h struct field lists", "string_pool_header_size": 28, "total_bytes": {"ResChunk_header": 8, "ResStringPool_header": 28, "ResXMLTree_attrExt": 20, "ResXMLTree_attribute": 20, "ResXMLTree_node": 16, "Res_value": 8}}
```

The summed `attr_ext_attribute_start` 20 and `attribute_size` 20 are the values the start-element chunk states in item 8.

6. The string-pool chunk's header values and the strings the readout decodes from the offsets the pool states (`readout.py:155-168`; the UTF-8 flag position tested is `flags & 0x100`, `readout.py:166`):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_string_pool
{"fact": "axml_string_pool", "flags": "0x00000100", "offset": 8, "offsets": [0, 10, 55, 66, 76, 94, 108, 122, 126], "sorted_flag": false, "stringCount": 9, "strings": ["android", "http://schemas.android.com/apk/res/android", "manifest", "package", "com.example.r65", "versionCode", "versionName", "1", "1.0"], "stringsStart": 64, "styleCount": 0, "stylesStart": 0, "utf8": true}
```

7. The resource-map chunk's printed size less its printed header size (item 4: 44 less 8) is 36 bytes, which is 9 times 4 — one `uint32` per string — and the readout prints the entries and the non-zero ones keyed by string (the array layout is S038's; its source line is not among the lines item 11 prints). The two non-zero ids are compared with the oracle's declared ids in item 13; the zero entries are recorded as observed and no meaning for a zero entry is claimed:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_resource_map
{"entry_count": 9, "fact": "axml_resource_map", "ids": ["0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x0101021b", "0x0101021c", "0x00000000", "0x00000000"], "nonzero": {"versionCode": "0x101021b", "versionName": "0x101021c"}, "offset": 204}
```

8. The start-element chunk's printed `attributeStart`, `attributeSize` and `attributeCount` and its three attributes. Where the attributes are read: the readout computes `aoff = base + 16 + attribute_start + i * attribute_size` (`readout.py:203`), where `base` is the chunk's offset; the literal 16 equals the chunk's declared `headerSize` in item 4 and the `node_header_size` item 5 sums (an inference, labeled in the inference section). S038's comment on `attributeStart` (quoted and located by item 11) says the offset is counted from the start of the attrExt structure. The readout resolves each attribute's namespace prefix string by indexing the string pool directly with the attribute's own `ns_index` (`readout.py:211`, `strings[ans]`; `NO_INDEX` 0xFFFFFFFF at `readout.py:22` resolves to null). The start-namespace chunk is printed as a separate fact and the readout does not consult it when resolving attribute namespaces:

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

9. The `classes.dex` member's declared header values and their recomputations, exactly as the readout prints them (`readout.py:233-248`). The four declared fields S048's quoted phrases cover — checksum, signature, header_size and endian_tag (located by item 11) — are compared with those phrases; `magic`, `format_version`, `file_size` and `header_bytes` are printed without a quoted S045 phrase and no semantics are claimed for them. A match between a declared value and its recomputation shows the member's header is internally consistent, and nothing about dex program validity follows:

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

11. Every S038 line number and enum value this entry states is printed by the committed derivation, which searches the pinned snapshot bytes for each cited symbol; its credit is bounded to exactly the lines it prints (the output below is the complete set). The second command locates each quoted spec phrase (S038's `attributeStart` comment, S049's route sentence, four S048 phrases) in its committed snapshot copy, tags stripped and whitespace folded, and prints, for each phrase, the snapshot file, the line number its first words start on, and the searched phrase itself:

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

12. The ZIP field offsets the readout uses are summed here from the **manually transcribed** APPNOTE field widths (`entry_checks.py`, `LOCAL_HEADER`, `CENTRAL_HEADER`, `EOCD`) and each is compared with the literal in the readout source; stdout lines 16-18 of 20 (the command line above is not counted as stdout) print where each record layout sits in the snapshot (heading line and the first and last transcribed field lines), while the final two stdout lines compare the central and local fixed-part widths. The widths are recorded, the sums, the line numbers and the presence checks are derived:

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
MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399
MATCH APPNOTE 4.3.12: heading line 511, transcribed field lines 522-538
MATCH APPNOTE 4.3.16: heading line 632, transcribed field lines 634-646
MATCH central.fixed_part: spec width 46, readout.py literal `cursor + 46` present=True
MATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True
```

13. The readout's facts compared with the authored oracle `truth.json`, which `generator.py` emits; the comparison covers the image digest and size; per member the local-header offset, compressed size, uncompressed size, CRC-32 and SHA-256; the AXML strings and resource ids; and per attribute the name index, namespace index, raw-value index, data type and data. The oracle's `image.path` and member `name` values are used as keys and not compared, and member `method` is compared by item 16's command. The oracle's AXML values are the generator's own build declaration, so agreement shows the readout parses what the generator wrote; it does not show that a declared value (for example the two resource ids) is the Android framework's value for its name. One line per compared field, every line printed:

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --oracle
MATCH image.sha256: readout='05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e' oracle='05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e'
MATCH image.size: readout=947 oracle=947
MATCH AndroidManifest.xml.local_header_offset: readout=0 oracle=0
MATCH AndroidManifest.xml.compressed_size: readout=416 oracle=416
MATCH AndroidManifest.xml.uncompressed_size: readout=416 oracle=416
MATCH AndroidManifest.xml.crc32: readout='962d075f' oracle='962d075f'
MATCH AndroidManifest.xml.sha256: readout='73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4' oracle='73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4'
MATCH classes.dex.local_header_offset: readout=465 oracle=465
MATCH classes.dex.compressed_size: readout=112 oracle=112
MATCH classes.dex.uncompressed_size: readout=112 oracle=112
MATCH classes.dex.crc32: readout='2635c82a' oracle='2635c82a'
MATCH classes.dex.sha256: readout='57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2' oracle='57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2'
MATCH META-INF/MANIFEST.MF.local_header_offset: readout=618 oracle=618
MATCH META-INF/MANIFEST.MF.compressed_size: readout=69 oracle=69
MATCH META-INF/MANIFEST.MF.uncompressed_size: readout=69 oracle=69
MATCH META-INF/MANIFEST.MF.crc32: readout='e948d738' oracle='e948d738'
MATCH META-INF/MANIFEST.MF.sha256: readout='2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49' oracle='2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49'
MATCH axml.strings: readout=['android', 'http://schemas.android.com/apk/res/android', 'manifest', 'package', 'com.example.r65', 'versionCode', 'versionName', '1', '1.0'] oracle=['android', 'http://schemas.android.com/apk/res/android', 'manifest', 'package', 'com.example.r65', 'versionCode', 'versionName', '1', '1.0']
MATCH axml.resource_ids: readout=['0x00000000', '0x00000000', '0x00000000', '0x00000000', '0x00000000', '0x0101021b', '0x0101021c', '0x00000000', '0x00000000'] oracle=['0x00000000', '0x00000000', '0x00000000', '0x00000000', '0x00000000', '0x0101021b', '0x0101021c', '0x00000000', '0x00000000']
MATCH axml.attribute[0].name_index: readout=3 oracle=3
MATCH axml.attribute[0].ns_index: readout=4294967295 oracle=4294967295
MATCH axml.attribute[0].raw_value_index: readout=4 oracle=4
MATCH axml.attribute[0].data_type: readout=3 oracle=3
MATCH axml.attribute[0].data: readout=4 oracle=4
MATCH axml.attribute[1].name_index: readout=5 oracle=5
MATCH axml.attribute[1].ns_index: readout=0 oracle=0
MATCH axml.attribute[1].raw_value_index: readout=7 oracle=7
MATCH axml.attribute[1].data_type: readout=16 oracle=16
MATCH axml.attribute[1].data: readout=1 oracle=1
MATCH axml.attribute[2].name_index: readout=6 oracle=6
MATCH axml.attribute[2].ns_index: readout=0 oracle=0
MATCH axml.attribute[2].raw_value_index: readout=8 oracle=8
MATCH axml.attribute[2].data_type: readout=3 oracle=3
MATCH axml.attribute[2].data: readout=8 oracle=8
```

14. Digests and sizes of the ten files under `corpus/` that the commands above read, recomputed from bytes, including the script that prints items 2 and 11-17 (a digest identifies exactly these bytes; it does not establish who produced them, that a copy was faithfully fetched, or that it is the upstream's current text):

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins
sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e 947 bytes corpus/fixtures/apk-r65/fixture.apk
sha256 27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173 2466 bytes corpus/fixtures/apk-r65/truth.json
sha256 eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a 9599 bytes corpus/fixtures/apk-r65/generator.py
sha256 92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976 11236 bytes corpus/fixtures/apk-r65/readout.py
sha256 2d4f25f6894ac86ced3c9986abd7cdbcf4c6d2aab477cda6dc515585c129b1f9 15062 bytes corpus/fixtures/apk-r65/entry_checks.py
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

16. The general-purpose flags and compression method of every local and central record, read from the archive bytes and compared with the oracle's declared method:

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --container
MATCH AndroidManifest.xml: local flags=0x0000 method=0; central flags=0x0000 method=0; bit 3 (data descriptor) clear; oracle method 0
MATCH classes.dex: local flags=0x0000 method=0; central flags=0x0000 method=0; bit 3 (data descriptor) clear; oracle method 0
MATCH META-INF/MANIFEST.MF: local flags=0x0000 method=0; central flags=0x0000 method=0; bit 3 (data descriptor) clear; oracle method 0
```

17. The AXML field offsets the readout source uses, compared with sums of a second manual transcription of S038's struct widths (itself compared with the widths the readout prints):

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout
MATCH ResChunk_header: transcription [2, 2, 4] readout-printed [2, 2, 4]
MATCH ResStringPool_header: transcription [2, 2, 4, 4, 4, 4, 4, 4] readout-printed [2, 2, 4, 4, 4, 4, 4, 4]
MATCH ResXMLTree_node: transcription [2, 2, 4, 4, 4] readout-printed [2, 2, 4, 4, 4]
MATCH ResXMLTree_attrExt: transcription [4, 4, 2, 2, 2, 2, 2, 2] readout-printed [4, 4, 2, 2, 2, 2, 2, 2]
MATCH ResXMLTree_attribute: transcription [4, 4, 4, 2, 1, 1, 4] readout-printed [4, 4, 4, 2, 1, 1, 4]
ResXMLTree_node fixed part: 16 bytes; attrExt begins at chunk offset + 16
MATCH ResStringPool_header.stringCount: spec offset 8 (+0), readout.py literal `u32(axml, so + 8)` present=True
MATCH ResStringPool_header.styleCount: spec offset 12 (+0), readout.py literal `u32(axml, so + 12)` present=True
MATCH ResStringPool_header.flags: spec offset 16 (+0), readout.py literal `u32(axml, so + 16)` present=True
MATCH ResStringPool_header.stringsStart: spec offset 20 (+0), readout.py literal `u32(axml, so + 20)` present=True
MATCH ResStringPool_header.stylesStart: spec offset 24 (+0), readout.py literal `u32(axml, so + 24)` present=True
MATCH ResXMLTree_attrExt.ns: spec offset 0 (+16), readout.py literal `u32(axml, base + 16)` present=True
MATCH ResXMLTree_attrExt.name: spec offset 4 (+16), readout.py literal `u32(axml, base + 20)` present=True
MATCH ResXMLTree_attrExt.attributeStart: spec offset 8 (+16), readout.py literal `u16(axml, base + 24)` present=True
MATCH ResXMLTree_attrExt.attributeSize: spec offset 10 (+16), readout.py literal `u16(axml, base + 26)` present=True
MATCH ResXMLTree_attrExt.attributeCount: spec offset 12 (+16), readout.py literal `u16(axml, base + 28)` present=True
MATCH ResXMLTree_attrExt.idIndex: spec offset 14 (+16), readout.py literal `u16(axml, base + 30)` present=True
MATCH ResXMLTree_attrExt.classIndex: spec offset 16 (+16), readout.py literal `u16(axml, base + 32)` present=True
MATCH ResXMLTree_attribute.ns: spec offset 0, readout.py literal `u32(axml, aoff)` present=True
MATCH ResXMLTree_attribute.name: spec offset 4, readout.py literal `u32(axml, aoff + 4)` present=True
MATCH ResXMLTree_attribute.rawValue: spec offset 8, readout.py literal `u32(axml, aoff + 8)` present=True
MATCH ResXMLTree_attribute.valueSize: spec offset 12, readout.py literal `u16(axml, aoff + 12)` present=True
MATCH ResXMLTree_attribute.valueDataType: spec offset 15, readout.py literal `axml[aoff + 15]` present=True
MATCH ResXMLTree_attribute.valueData: spec offset 16, readout.py literal `u32(axml, aoff + 16)` present=True
```

## Observation / inference / unknown

- **Observation** — the command blocks record the displayed counts, offsets, identifiers and digests. Item 13 compares selected readout facts with the separate authored oracle; items 3, 5, 12 and 17 also use manually transcribed widths and derived sums. `readout.py:N` citations are source locators; the literal subsets compared are only those printed by items 12 and 17. Named as locators-only, not compared by this entry (Q16): `readout.py:22` (`NO_INDEX = 0xFFFFFFFF`), `:76` (`sig_eocd = b"PK\\x05\\x06"`), `:166` (the UTF-8/sorted flag masks), `:189` (`lineNumber`), `:197` (`styleIndex`), `:211` (`strings[ans]`) and `:233-248` (the dex header reads).
- **Inference** — (a) a printed chunk `type` value equals the value of the S038 enum line item 11 prints for the named constant; (b) the literal 16 in `readout.py:203` is the start-element chunk's declared `headerSize` (item 4) and the summed node width (item 5); (c) the two non-zero resource-map entries are the two ids `truth.json` declares (item 13); (d) the dex header's declared checksum, signature, size and endian fields agree with S048's field semantics as quoted. Each inference cites its byte evidence and is scoped to this fixture.
- **Unknown** — nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed; the fixture is inert and no producer was called. The ZIP APPNOTE layouts are recorded from a snapshot; whether the upstream document has since changed is not checked.

## Limitations

One authored fixture, one manifest shape (a single element with three attributes), UTF-8 string pool only, no CDATA, no nested elements, no styles. The container is stored with no data-descriptor flag set (item 16 prints each record's flags and method); the readout itself does not read compression method or flag bytes, while item 16 inspects them in the checker without exercising compressed data. The dex member is a header only and is not a valid dex program (the generator's own docstring, `generator.py:8`). The two namespaced attributes carry `ns_index` 0, which items 6 and 8 print as the string `android` (the prefix), while string 1 is the namespace URI; that is a property of these authored bytes, and no conformance of the fixture to any producer's output is claimed. `readout.py:49-50` still comments that widths are "computed here ... not assumed"; the widths are a manual transcription (item 5), and the comment is the readout's own wording, not this entry's claim. Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence.

## Cross-lane scope note (Q10)

The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S049 only; this lane ran no provider and makes no readiness claim (Q05 fence). The kaidoku/revenger ADJ-06 overlap (fleet `.ufo/l0-questions.md:42`, open) stays reported, not absorbed: the kaidoku lane's APK content-graph inventory and Android decode axis (`kaidoku-shokunin/corpus/README.md:27` and `:29`) are not restated, and this entry claims none of that surface.

## §Q-map

| criterion | decision | basis |
|---|---|---|
| Q01 | pass | each load-bearing layout/command-output claim rests on a tier-A row for its scope: S038 (AXML facts located in the pinned snapshot; the round-71 live response did not establish byte currency), S048 (dex header semantics), S032/S034 (ZIP records), S047/S041 (own-work), S049 (documented route scope) and S052 (this command's output shape). No tier-C row is sole support. |
| Q02 | pass | header carries `source:` for S038, S049, S048, S032, S034, S047, S041 and S052 with anchors, plus `verified-at:`, `recheck:` and `coverage-map: C05`. |
| Q03 | pass | expected values come from the archive bytes, from the authored oracle `truth.json` (emitted by `generator.py`, not by the readout), or from a printed spec line (item 11); item 13 labels the oracle's AXML half as the generator's own build declaration and claims parse fidelity only, never that a declared value is a framework value. None is copied from the record under test. |
| Q04 | pass | no tool claim: the readout is manual standard-library byte analysis, the widths are labeled manual (items 5, 12), and the derivation script's credit is bounded to the lines it prints (item 11). |
| Q05 | pass | no readiness or capability claim and no refusal path described; the provider route is fenced to S049's documented scope (header, Limitations, cross-lane note); the one exit-status sentence (Reproduce: `Exit 0`) is probed by item 15, whose `--stdout-digest` runs the readout with `check=True`, so a non-zero readout exit prints no line. |
| Q06 | pass | the fixture premises are digest-printed from the built bytes (item 14); the entry does not re-run the generator and says so in the S041 header line. |
| Q07 | pass | no parser-behavior prediction is made; the namespace sentence in item 8 describes how this readout resolves this fixture, by the cited source lines. |
| Q08 | superseded | QUALITY.md Q11 supersedes Q08; Q11 below is the operative criterion. |
| Q09 | pass | every digest is claimed only for the bytes it hashed; item 14 lists the ten `corpus/` files the commands read (including the checker script) and says a digest does not establish production, faithful fetching or currency; the builder script outside `corpus/` is named as undigested. |
| Q10 | pass | scope is one fixture; cross-lane contested scope is named at the note above and not absorbed. |
| Q11 | pass | displayed counts/offsets/identifiers/digests have their deriving command and output in items 1-17; manual widths and derived sums are labeled; APPNOTE/snapshot line numbers are printed in items 11-12; unprinted `readout.py` source locators are not called compared. |
| Q12 | n/a | no rejected-source row or reject/flip claim is written in this entry; all source rows cited here are admitted rows. |
| Q13 | pass | the embedded-output gate is credited only for the clause that every embedded line appears in its command's stdout; the `MATCH`/`MISMATCH` lines are credited only for the comparisons each prints. **Unguarded clauses, named:** deleting an embedded output line is not detected (one-directional comparison); a corrupted flag whose output is a superset passes; and a forged block whose command is a different in-tree script that prints fabricated lines verbatim passes (the gate compares only the declared command's stdout; R70W2EntryMutants). The entry credits no verifier for these clauses. |
| Q14 | pass | no prose hex string carries a byte count or ASCII rendering; the counted signature/prefix runs are command output in items 2 and 14, not prose literals. |
| Q15 | pass | this entry states no git object id; identity statements are file digests printed by item 14. |
| Q16 | pass | item 11's output-format statement is grounded by S052 and its six MATCH lines; item 12's locator/width statements match its 20 stdout lines; item 17 credits only its printed AXML offsets. Locators-only citations are named at Observation: readout.py:22,76,166,189,197,211,233-248. |

## Reproduce

From the lane root:

```sh
python3 -B corpus/fixtures/apk-r65/readout.py
```

Exit 0 and 15 stdout lines; item 15's command prints their count and digest and runs the readout with `check=True`. Single-fact form: `python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd`. The eight derivation flags of `corpus/fixtures/apk-r65/entry_checks.py` are `--pins`, `--eocd`, `--oracle`, `--zip-layout`, `--axml-layout`, `--container`, `--spec-quotes` and `--stdout-digest`.
