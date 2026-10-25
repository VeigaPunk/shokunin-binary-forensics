MATCH — the `axml_chunk_table` stdout is byte-identical (480/480 bytes, sha256 `d37db5aa…`) to the entry's embedded line at `corpus/knowledge/round-69-apk-axml-byte-evidence.md:206` (duplicate block at `:56`), zero differing fields, and the prose sentence states nothing the output does not support (its non-output claims — S038 line numbers — re-derive exactly from `corpus/derive_axml_anchors.py`, run below).

# R69Item4 — per-item re-derivation: AXML chunk table

Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin (absolute paths). Read-only: nothing edited, no git/jj mutation, no package install (no new tool needed; Python 3 stdlib + `diff`/`sha256sum` only).

## 1. Command and exit

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_chunk_table
EXIT_CODE=0
```

stdout (single line, 480 bytes incl. trailing newline):

```
{"chunks": [{"headerSize": 28, "offset": 8, "size": 196, "type": 1}, {"headerSize": 8, "offset": 204, "size": 44, "type": 384}, {"headerSize": 16, "offset": 248, "size": 24, "type": 256}, {"headerSize": 16, "offset": 272, "size": 96, "type": 258}, {"headerSize": 16, "offset": 368, "size": 24, "type": 259}, {"headerSize": 16, "offset": 392, "size": 24, "type": 257}], "fact": "axml_chunk_table", "xml_header_type": 3, "xml_total_size": 416, "xml_total_size_equals_member": true}
```

## 2. Entry's embedded line

- Primary occurrence: `corpus/knowledge/round-69-apk-axml-byte-evidence.md:206` (inside §Observation item 4's fenced block, `:204-206`).
- Exact duplicate: same file `:56` (inside §Reproduce's copied full-stdout block).
- Both lines: 480 bytes, sha256 `d37db5aa8e1a524dae167e24be7dbfba46898201e04c16497189a341d8f3045b` — the same sha256 as the live stdout file.

Byte-level check:

```
$ diff /tmp/revenger-r69-item4-actual.txt /tmp/revenger-r69-item4-embedded.txt && echo IDENTICAL_BYTES
IDENTICAL_BYTES
$ wc -c  -> 480 480
$ sha256sum -> d37db5aa8e1a524dae167e24be7dbfba46898201e04c16497189a341d8f3045b (both)
```

## 3. Field-by-field verdict

Key order is identical too, so the diff of whole lines already subsumes this table; still enumerated:

| field | actual | embedded (:206) | verdict |
|---|---|---|---|
| `chunks[0].headerSize` | 28 | 28 | MATCH |
| `chunks[0].offset` | 8 | 8 | MATCH |
| `chunks[0].size` | 196 | 196 | MATCH |
| `chunks[0].type` | 1 | 1 | MATCH |
| `chunks[1].headerSize` | 8 | 8 | MATCH |
| `chunks[1].offset` | 204 | 204 | MATCH |
| `chunks[1].size` | 44 | 44 | MATCH |
| `chunks[1].type` | 384 | 384 | MATCH |
| `chunks[2].headerSize` | 16 | 16 | MATCH |
| `chunks[2].offset` | 248 | 248 | MATCH |
| `chunks[2].size` | 24 | 24 | MATCH |
| `chunks[2].type` | 256 | 256 | MATCH |
| `chunks[3].headerSize` | 16 | 16 | MATCH |
| `chunks[3].offset` | 272 | 272 | MATCH |
| `chunks[3].size` | 96 | 96 | MATCH |
| `chunks[3].type` | 258 | 258 | MATCH |
| `chunks[4].headerSize` | 16 | 16 | MATCH |
| `chunks[4].offset` | 368 | 368 | MATCH |
| `chunks[4].size` | 24 | 24 | MATCH |
| `chunks[4].type` | 259 | 259 | MATCH |
| `chunks[5].headerSize` | 16 | 16 | MATCH |
| `chunks[5].offset` | 392 | 392 | MATCH |
| `chunks[5].size` | 24 | 24 | MATCH |
| `chunks[5].type` | 257 | 257 | MATCH |
| `fact` | "axml_chunk_table" | "axml_chunk_table" | MATCH |
| `xml_header_type` | 3 | 3 | MATCH |
| `xml_total_size` | 416 | 416 | MATCH |
| `xml_total_size_equals_member` | true | true | MATCH |

Fields that differ: **none** (0 of 28).

Independent re-walk of the same bytes (my own `struct` script over the member payload at APK offset 49, not the readout) reproduces the table exactly, including the loop bound:

```
top type=0x0003 headerSize=8 totalSize=416 memberlen=416 equal=True
rows: [(8, 1, 28, 196), (204, 384, 8, 44), (248, 256, 16, 24), (272, 258, 16, 96), (368, 259, 16, 24), (392, 257, 16, 24)]
walk_end=416 total=416 exact=True
types_hex: ['0x0001', '0x0180', '0x0100', '0x0102', '0x0103', '0x0101']
headerSizes: [28, 8, 16, 16, 16, 16]
```

## 4. Prose judgment

Prose sentences about this fact:

- `:53` (item 4 lead-in): "The `AndroidManifest.xml` payload begins `0300 0800 a001 0000` — chunk type `0x0003` (`RES_XML_TYPE`), headerSize 8, total size **416**, equal to the member's uncompressed size. The child chunks are walked from offset 8 by adding each chunk's size, and the walk ends exactly at 416."
- `:59` (item 4 post-block): "The six chunk types in the table — `0x0001` string pool, `0x0180` resource map, `0x0100` start namespace, `0x0102` start element, `0x0103` end element, `0x0101` end namespace — are the values S038's chunk-type enum block names at **lines 237-263** … The `headerSize` column — 28, 8, 16, 16, 16, 16 — equals the fixed struct sizes transcribed in item 5 for the string pool and the XML node chunks."

Claim-by-claim:

1. **Six chunk types and hex values** — supported: the output's `type` column is `1, 384, 256, 258, 259, 257` = `0x0001, 0x0180, 0x0100, 0x0102, 0x0103, 0x0101`, in the same order, and the name assignment matches S038 (verified below). No overclaim.
2. **`headerSize` column 28, 8, 16, 16, 16, 16** — supported exactly by the `headerSize` column. The equality to item 5's transcribed widths holds: item 5 prints `string_pool_header_size: 28`, `node_header_size: 16`, `ResChunk_header: 8`; the resource-map chunk's 8 is `ResChunk_header` (the prose scopes the sentence to "the string pool and the XML node chunks", so it does not misattribute the resource-map width).
3. **"walked from offset 8 by adding each chunk's size … ends exactly at 416"** — supported by arithmetic over emitted fields: first `offset` is 8, and 392 + 24 = 416 = `xml_total_size`. True statement.
4. **"chunk type `0x0003` … total size 416, equal to the member's uncompressed size"** — supported: `xml_header_type: 3`, `xml_total_size: 416`, `xml_total_size_equals_member: true`; `member[AndroidManifest.xml].uncompressed_size` is 416 (`:205` block, and my `compressed=416 uncompressed=416 stored=True` check).
5. **S038 line numbers 237/239/241/244/245/246/247/248/253/263** — not fields of this output, but the prose attributes them to "item 11's command", and my run of that command reproduces every one, value and line, exactly:

```
$ python3 -B corpus/derive_axml_anchors.py   # exit 0, 20 lines
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
```

Also checked the entry's cited readout anchors: `readout.py:51-58` is the widths dict (`w8, w16, w32 = 1, 2, 4` at :51, `"Res_value": …` at :58), `readout.py:99-105` ends at `payload_off = lh_off + 30 + lh_name_len + lh_extra_len` (:105 for item 3), `readout.py:142` is `emit("axml_chunk_table",…)`, `readout.py:166` is `utf8=bool(flags & 0x100)`. All as the prose says.

Unsupported statements in the prose: **none found**. The only sentence element not emitted by *this* fact is the top-level `headerSize 8`, and it is supported two other ways: `chunks[0].offset == 8` (the walk starts at the top-level headerSize, `readout.py:132` `off = u16(axml, 2)`) and `member[AndroidManifest.xml].payload_first16_hex = "03000800a0010000"` (`:205`).

## 5. Residual observations (not mismatches, do not change the verdict)

- **Latent semantic imprecision in the field name.** `readout.py:143` computes `xml_total_size_equals_member = len(axml) == xml_size`, where `axml` is the *stored payload slice* (`compressed_size` bytes), not the member's `uncompressed_size` field. For this fixture the method is 0 (stored) so `compressed_size == uncompressed_size == 416` and the prose's "equal to the member's uncompressed size" is true; the name would be wrong for a deflated member. No action implied for C1 today, but a v5 that adds a deflated member would need the comparison switched to the `uncompressed_size` field.
- **No positive end-of-walk field.** The output does not emit `walk_ends_at_total: true`; "the walk ends exactly at 416" is an arithmetic consequence of the emitted `offset`/`size` pairs, and `readout.py:132-141` has no `assert off == xml_size`. The claim is true and derivable, but a strict machine reader of the single JSON line cannot see an explicit confirmation.
- The same 15-line stdout is embedded twice (per-item block `:55-57` and full-stdout block `:204-206`); both copies are byte-identical to live stdout, so this is duplication, not drift.
- Full-stdout receipt re-verified: `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` = the entry's `recheck:` and §Reproduce hash (`:9`, `:194`). Pinned hashes also confirmed: `fixture.apk` `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, `readout.py` `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`, `derive_axml_anchors.py` `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa`, `corpus/snapshots/ResourceTypes.h` `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`.

Scratch under `/tmp/revenger-r69-item4-*` deleted before returning.
