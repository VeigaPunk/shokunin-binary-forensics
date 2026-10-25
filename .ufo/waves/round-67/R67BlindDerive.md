CONCUR — blind AXML walk from fixture bytes + S038 snapshot reproduces every value in v2 entry items 4–8 with zero divergences.

seat: R67BlindDerive (Q03 blind-independence seat) · item: derive AXML layout without `corpus/fixtures/apk-r65/readout.py` or the v2 Observation section, then diff against items 4–8 · date: 2026-10-24

## Method (blind phase)

- Inputs used: `/tmp/r67-blind-derive/fixture.apk` (copied from `corpus/fixtures/apk-r65/fixture.apk`) + the committed spec snapshot `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots/ResourceTypes.h`.
- Never opened during derivation: `corpus/fixtures/apk-r65/readout.py`, `truth.json`, `generator.py`, the v2 entry. (Opened the v2 entry only after my table below was complete.)
- Own parser written at `/tmp/r67-blind-derive/axml_walk.py` (script + full stdout at `/tmp/r67-blind-derive/walk_out.txt`), using only the struct layouts at ResourceTypes.h:218-235 (`ResChunk_header`: u16 type, u16 headerSize, u32 size), :237-253 (chunk-type enum), :287-412 (`Res_value`: u16 size, u8 res0, u8 dataType, u32 data), :430-436 (`ResStringPool_ref`), :461-489 (`ResStringPool_header`: 5×u32 after header), :621-630 (`ResXMLTree_node`: +lineNumber u32 +comment u32 = 16), :649-656 (`ResXMLTree_namespaceExt`), :662-670 (`ResXMLTree_endElementExt`), :677-705 (`ResXMLTree_attrExt` = 20, `attributeStart` attrExt-relative per :685-687), :707-720 (`ResXMLTree_attribute` = 20).

## My independently derived table (from bytes)

member `AndroidManifest.xml`, 416 bytes, first16 `03000800a001000001001c00c4000000`.

| offset | type | name | headerSize | size |
|---|---|---|---|---|
| 0 | 0x0003 | RES_XML_TYPE (file) | 8 | 416 |
| 8 | 0x0001 | RES_STRING_POOL_TYPE | 28 | 196 |
| 204 | 0x0180 | RES_XML_RESOURCE_MAP_TYPE | 8 | 44 |
| 248 | 0x0100 | RES_XML_START_NAMESPACE_TYPE | 16 | 24 |
| 272 | 0x0102 | RES_XML_START_ELEMENT_TYPE | 16 | 96 |
| 368 | 0x0103 | RES_XML_END_ELEMENT_TYPE | 16 | 24 |
| 392 | 0x0101 | RES_XML_END_NAMESPACE_TYPE | 16 | 24 |

Walk terminates at 416 = member size.

String pool @8: stringCount 9, styleCount 0, flags `0x00000100` (UTF8_FLAG set, SORTED clear), stringsStart 64, stylesStart 0. UTF-8 strings carry two one-byte length prefixes (utf16len, utf8len — both <0x80 here) + 1-byte NUL. Index offsets [0,10,55,66,76,94,108,122,126]:
`['android','http://schemas.android.com/apk/res/android','manifest','package','com.example.r65','versionCode','versionName','1','1.0']`

Resource map @204: 9 u32 = `0,0,0,0,0,0x0101021b,0x0101021c,0,0` (nonzero on str[5]='versionCode', str[6]='versionName').

Start-namespace @248: line 1, comment 0xffffffff, prefix=str[0]='android', uri=str[1]='http://schemas.android.com/apk/res/android'.

Start-element @272: line 1; attrExt at 272+16=288 (0x120): ns=0xffffffff (none), name=str[2]='manifest', attributeStart=20, attributeSize=20, attributeCount=3, id/class/styleIndex=0. Attribute base = 288+20=308 (0x134); rows:
- attr[0] @0x134: ns=0xffffffff, name=str[3]='package', raw=str[4]='com.example.r65', Res_value{size=8,res0=0,type=0x03 STRING,data=str[4]}
- attr[1] @0x148: ns=str[0]='android', name=str[5]='versionCode', raw=str[7]='1', Res_value{8,0,0x10 INT_DEC,data=1}
- attr[2] @0x15c: ns=str[0]='android', name=str[6]='versionName', raw=str[8]='1.0', Res_value{8,0,0x03 STRING,data=str[8]}

End-element @368: line 1, ns=0xffffffff, name='manifest'. End-namespace @392: line 1, same prefix/URI pair.

## Diff vs v2 entry items 4–8 (post-derivation)

`corpus/knowledge/round-67-apk-axml-byte-evidence.md`:

- **item 4 (entry:49-56)** — outer header `0300 0800 a001 0000`, type 3 / headerSize 8 / size 416 = member size, walk-from-8 ends at 416, and all six embedded chunk rows `(offset,size,type,headerSize)` match my table exactly (8/196/1/28, 204/44/384/8, 248/24/256/16, 272/96/258/16, 368/24/259/16, 392/24/257/16). The enum-name mapping it cites at S038 :237-253 (resource map at :253) matches the snapshot lines I used (:239 string pool, :241 xml, :244/:246 namespaces, :247/:248 elements, :253 map). **Agree.**
- **item 5 (entry:58-65)** — derived widths ResChunk_header 8 [2,2,4], ResStringPool_header 28, ResXMLTree_node 16, ResXMLTree_attrExt 20, ResXMLTree_attribute 20, Res_value 8 — identical to my sums of the same field lists; `attributeStart`/`attributeSize` = 20 confirmed live in my walk. **Agree.**
- **item 6 (entry:67-72)** — stringCount 9, styleCount 0, flags `0x00000100`, stringsStart 64, identical offset array and identical nine string values. **Agree.**
- **item 7 (entry:74-79)** — 9 ids, seven `0x00000000`, `versionCode`=`0x0101021b`, `versionName`=`0x0101021c` at indices 5/6. **Agree.**
- **item 8 (entry:81-88)** — element `manifest`, ns null (0xffffffff), attributeStart 20 / attributeSize 20 / attributeCount 3 / classIndex=idIndex=styleIndex=0; attribute rows identical field-by-field: `package` ns_index 4294967295 name_index 3 raw 4 type 0x03 data→str4; `versionCode` ns 0 name 5 raw 7 type 0x10 data 1; `versionName` ns 0 name 6 raw 8 type 0x03 data→str8. Its res_id fields (16843291=0x0101021b, 16843292=0x0101021c) match my resource-map derivation. Provenance sentence (attrExt at chunk_base+16 via node headerSize; attribute *i* at `chunk_base + 16 + attributeStart + i*attributeSize`) is the same derivation my walk performs. **Agree.**
- **start/end namespace + end element (entry:88-102, scope-adjacent)** — prefix/URI indices 0/1, all lineNumber=1, end-element ns_index 0xffffffff name_index 2: all match my walk.

**Divergences: none.** Every byte-level fact in items 4–8 is reproduced by an independent parse that never saw the author's readout or this entry's Observation.

## Notes / residual

- One derivation hazard worth recording: ResourceTypes.h documents only UTF-16 string lengths in prose (:447-454); the UTF-8 pool's dual one-byte length-prefixed encoding (utf16len then utf8len, 0x80 continuation) had to be derived from the fixture bytes themselves (`07 07 'android'` at 0x48). It decodes cleanly and is corroborated by the entry's identical output — not a divergence, but it means the UTF-8 length framing is byte-derived rather than stated in the cited header text.
- The resource-map nonzero ids are fixture-declared values; like the entry, I claim no framework-wide semantics for them.
- I did not read `readout.py` or `truth.json`; no oracle comparison performed by this seat (that is the entry's item-7 oracle claim, outside my brief).

## Tooling

No installs. Python 3 stdlib only (`struct`, `zipfile`); artifacts under `/tmp/r67-blind-derive/` (`axml_walk.py`, `walk_out.txt`, copied `fixture.apk`).

Report: .ufo/waves/round-67/R67BlindDerive.md
