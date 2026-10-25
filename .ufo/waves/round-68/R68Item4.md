# R68 Item 4 — independent re-derivation of the AXML chunk table

**Verdict: MATCH** — `axml_chunk_table` reproduces byte-identically (all 5 top-level fields, all 6 chunks × 4 fields), the prose sentence at entry:57 is fully supported by re-derived artifacts, and every cited anchor resolves in the pinned snapshot. No edit made; nothing written outside this report.

Lane cwd for all commands: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## 1. Command and actual output

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_chunk_table
{"chunks": [{"headerSize": 28, "offset": 8, "size": 196, "type": 1}, {"headerSize": 8, "offset": 204, "size": 44, "type": 384}, {"headerSize": 16, "offset": 248, "size": 24, "type": 256}, {"headerSize": 16, "offset": 272, "size": 96, "type": 258}, {"headerSize": 16, "offset": 368, "size": 24, "type": 259}, {"headerSize": 16, "offset": 392, "size": 24, "type": 257}], "fact": "axml_chunk_table", "xml_header_type": 3, "xml_total_size": 416, "xml_total_size_equals_member": true}
EXIT=0
```

Raw stdout: 480 bytes, sha256 `d37db5aa8e1a524dae167e24be7dbfba46898201e04c16497189a341d8f3045b`.

Member facts (one run each, as instructed):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py 'member[AndroidManifest.xml]'   -> exit 0
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
$ python3 -B corpus/fixtures/apk-r65/readout.py 'member[classes.dex]'            -> exit 0
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
$ python3 -B corpus/fixtures/apk-r65/readout.py 'member[META-INF/MANIFEST.MF]'   -> exit 0
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
```

## 2. Entry-side embedded lines and byte-identity

The fact appears twice in `corpus/knowledge/round-68-apk-axml-byte-evidence.md`:

| location | role | byte-identical to actual stdout |
|---|---|---|
| entry:53-54 (`$ … --fact axml_chunk_table` + line) | per-item claim block, **the claim surface for this item** | **True** (`lines[53]` exactly equals stdout minus trailing `\n`) |
| entry:206 (inside the `## Reproduce` full-stdout block) | reproduction receipt | **True** |

Both correct. (A third grep hit is the probe command name at entry:53 itself.)

## 3. Field-by-field verdict

Programmatic comparison of `json.loads(actual)` vs `json.loads(entry:54)`:

| field | actual | entry:54 | verdict |
|---|---|---|---|
| `fact` | `axml_chunk_table` | `axml_chunk_table` | MATCH |
| `xml_header_type` | `3` | `3` | MATCH |
| `xml_total_size` | `416` | `416` | MATCH |
| `xml_total_size_equals_member` | `true` | `true` | MATCH |
| `chunks` (length) | 6 | 6 | MATCH |
| key set | `{chunks, fact, xml_header_type, xml_total_size, xml_total_size_equals_member}` | identical | MATCH (no missing/extra field) |

`chunks` list compared as objects (`a["chunks"] == b["chunks"]` → **True**); per-element:

| # | offset | headerSize | size | type | verdict |
|---|---|---|---|---|---|
| 0 | 8 | 28 | 196 | 1 | MATCH |
| 1 | 204 | 8 | 44 | 384 | MATCH |
| 2 | 248 | 16 | 24 | 256 | MATCH |
| 3 | 272 | 16 | 96 | 258 | MATCH |
| 4 | 368 | 16 | 24 | 259 | MATCH |
| 5 | 392 | 16 | 24 | 257 | MATCH |

**Differing fields: none.**

Independent arithmetic check of the claimed walk (entry:55, "walked from offset 8 by adding each chunk's size, and the walk ends exactly at 416"):
`8+196=204` → `204+44=248` → `248+24=272` → `272+96=368` → `368+24=392` → `392+24=416`. Each next offset equals the previous offset+size, and the last `392+24` equals `xml_total_size` 416, which `xml_total_size_equals_member: true` ties to the AndroidManifest member's `uncompressed_size: 416` (entry:39). Consistent.

## 4. Prose sentence judgement (entry:57)

Sentence under test: *"The six chunk types in the table — `0x0001` string pool, `0x0180` resource map, `0x0100` start namespace, `0x0102` start element, `0x0103` end element, `0x0101` end namespace — are the values S038's chunk-type enum block names at lines 237-253 (string pool :239, start/end namespace :245/:246, start/end element :247/:248, resource map `RES_XML_RESOURCE_MAP_TYPE` :253 — every one of these line numbers is derived by item 11's command). The `headerSize` column — 28, 8, 16, 16, 16, 16 — equals the fixed struct sizes derived in item 5 for the string pool and the XML node chunks."*

Every component was re-derived independently:

| prose claim | independent check | result |
|---|---|---|
| type numbers are 0x0001/0x0180/0x0100/0x0102/0x0103/0x0101 | output types 1/384/256/258/259/257 converted to hex | MATCH |
| enum block spans **lines 237-253** in S038 | `grep -n` on `corpus/snapshots/ResourceTypes.h`: `237:enum {`, `253: RES_XML_RESOURCE_MAP_TYPE = 0x0180,` | MATCH (exact, inclusive) |
| string pool :239 / start ns :245 / end ns :246 / start el :247 / end el :248 / resource map :253 | `python3 -B corpus/derive_axml_anchors.py` → exit 0, output lines `enum RES_STRING_POOL_TYPE : 239`, `enum RES_XML_START_NAMESPACE_TYPE : 245`, `enum RES_XML_END_NAMESPACE_TYPE : 246`, `enum RES_XML_START_ELEMENT_TYPE : 247`, `enum RES_XML_END_ELEMENT_TYPE : 248`, `enum RES_XML_RESOURCE_MAP_TYPE : 253`; derive prints `sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h` | MATCH, all six line numbers machine-derived |
| "every one of these line numbers is derived by item 11's command" | derive output is 17 lines (1 sha + 7 struct + 7 enum + 2 `attributeStart`), matching the entry's "exit 0, 17 lines" (entry:199) | MATCH |
| headerSize 28 = string-pool header struct size | `--fact spec_derived_struct_widths` (entry:66-68) → `string_pool_header_size: 28`, `total_bytes.ResStringPool_header: 28` | MATCH |
| headerSize 16 = XML node chunk struct size | same fact → `node_header_size: 16`, `total_bytes.ResXMLTree_node: 16` | MATCH |
| `xml_header_type` 3 = `RES_XML_TYPE` | snapshot enum: `RES_XML_TYPE = 0x0003` at line 241 (derive: `enum RES_XML_TYPE : 241`) | MATCH |

**Does the sentence state anything the output does not support?** No. Two of its components are not *contained in* this fact's stdout — the enum **names**/line numbers and the headerSize↔struct-size equality — but both are explicitly and correctly attributed to other resolvable artifacts (S038 in the committed snapshot, item 11's `derive_axml_anchors.py`, item 5's `spec_derived_struct_widths`), and I re-ran/opened both: they hold. No claim rests on this fact's output alone beyond what the output prints.

## 5. Adjacent integrity checks (cheap, same surface)

- `readout.py` sha256 = `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` — equals the entry's stated script hash (entry:199).
- `fixture.apk` sha256 = `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` — equals the `archive` fact line and the context's pinned value.
- Full run: exit 0, **15** stdout lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — exactly the entry's stated reproduction receipt (entry:199), and the chunk-table line occurs once inside it (entry:206).
- Member per-item lines (entry:39/41/43) and their full-stdout counterparts (entry:203/204/205) are each byte-identical to their own `--fact` stdout (6/6 True), so the block and the full-stdout copy do not disagree.

## 6. Residual observations (not defects for this item)

1. `0x0100` is non-unique in the enum: snapshot line 244 is `RES_XML_FIRST_CHUNK_TYPE = 0x0100` and line 245 is `RES_XML_START_NAMESPACE_TYPE = 0x0100`. Entry:57 maps the observed type 256 to start-namespace, which the chunk's own fields confirm (`axml_start_namespace` at offset 248, the same chunk), and entry:148 explicitly records the line-244 collision. The mapping is correct but relies on that disambiguation, which is stated elsewhere in the entry rather than in entry:57.
2. The sentence enumerates six headerSize values (28, 8, 16, 16, 16, 16) but grounds only the string-pool and node-chunk sizes; the `8` at index 1 (resource map) is `ResChunk_header`'s 8, also present in item 5's `total_bytes`. This is under-claiming, not over-claiming — no contradiction.

## 7. Scope / tooling

- Files read: `corpus/fixtures/apk-r65/readout.py` (executed), `corpus/fixtures/apk-r65/fixture.apk` (hashed only), `corpus/knowledge/round-68-apk-axml-byte-evidence.md`, `corpus/snapshots/ResourceTypes.h`, `corpus/derive_axml_anchors.py` (executed). No writes outside this report; no git/jj mutation; no edits to `corpus/`, `reports/`, README or any sibling-owned file.
- No tools installed or upgraded (host pacman guard respected); no installs were needed.
- I make **no admission decision** here: this is one item of the C05 v3 candidate's evidence surface. Per lane contract the README C05 row stays `uncovered` unless an all-criteria pass is independently established.
