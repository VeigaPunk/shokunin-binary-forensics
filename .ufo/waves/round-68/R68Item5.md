# R68 item 5 — independent re-derivation of the spec-derived struct widths

**MATCH** — `--fact spec_derived_struct_widths` re-runs to stdout identical to the entry's embedded line in all 8 top-level fields and all 6 nested width maps (byte-identical apart from the fence-only missing trailing newline), and the three member facts match byte-for-byte at both embedded copies; one prose clause is a precision overstatement, no value is wrong.

## 1. Command actually run

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact spec_derived_struct_widths
EXIT=0
```

Actual stdout (627 bytes including the trailing `\n`; sha256 `f9cd877bbbfd32c5f9c8aa2ad1bed6bf1578159d40ce850ab4e8ab87fbba6689`):

```json
{"attr_ext_attribute_start": 20, "attribute_size": 20, "bytes_per_field": {"ResChunk_header": [2, 2, 4], "ResStringPool_header": [2, 2, 4, 4, 4, 4, 4, 4], "ResXMLTree_attrExt": [4, 4, 2, 2, 2, 2, 2, 2], "ResXMLTree_attribute": [4, 4, 4, 2, 1, 1, 4], "ResXMLTree_node": [2, 2, 4, 4, 4], "Res_value": [2, 1, 1, 4]}, "fact": "spec_derived_struct_widths", "node_header_size": 16, "source_anchor": "S038 ResourceTypes.h struct field lists", "string_pool_header_size": 28, "total_bytes": {"ResChunk_header": 8, "ResStringPool_header": 28, "ResXMLTree_attrExt": 20, "ResXMLTree_attribute": 20, "ResXMLTree_node": 16, "Res_value": 8}}
```

Per-member runs (each `EXIT=0`, one line, no stderr):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[AndroidManifest.xml]'
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[classes.dex]'
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
```

Entry copies matched: `member[AndroidManifest.xml]` = entry lines **39** (item 2) and **203** (full-stdout block); `member[classes.dex]` = lines **41** and **204**; `member[META-INF/MANIFEST.MF]` = lines **43** and **205**. Programmatic equality (`line == stdout.rstrip(b"\n")`): `True` for all six.

## 2. Entry's embedded line for the width fact

`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md` **item 5**, fenced at lines 61-64, output line **63** (626 bytes), and its duplicate in the full-stdout block at line **201** (626 bytes). Both `== actual.rstrip(b"\n")` → `True`; sha256 of each embedded line `70796ab231c17f7b4a9b6913a3bea190065ec724257d9aee82a283d1e3658ad9`.

Byte-length note: actual stdout is 627 bytes, the embedded line 626 — the single differing byte is the trailing `\n`, which a fenced block line does not carry. After stripping the newline the strings are byte-identical; this is fence formatting, not a value difference.

## 3. Field-by-field verdict (every field of the actual output)

| field | actual | embedded (line 63 / 201) | verdict |
|---|---|---|---|
| `fact` | `spec_derived_struct_widths` | same | MATCH |
| `source_anchor` | `S038 ResourceTypes.h struct field lists` | same | MATCH |
| `attr_ext_attribute_start` | `20` | `20` | MATCH |
| `attribute_size` | `20` | `20` | MATCH |
| `node_header_size` | `16` | `16` | MATCH |
| `string_pool_header_size` | `28` | `28` | MATCH |
| `bytes_per_field` | 6 maps (below) | identical 6 maps | MATCH |
| `total_bytes` | 6 entries (below) | identical 6 entries | MATCH |

`bytes_per_field` / `total_bytes`, per struct — actual vs embedded equal, and each `total` equals `sum(bytes_per_field)`:

| struct | bytes_per_field | sum | total_bytes | internal sum OK |
|---|---|---|---|---|
| ResChunk_header | [2,2,4] | 8 | 8 | yes |
| ResStringPool_header | [2,2,4,4,4,4,4,4] | 28 | 28 | yes |
| ResXMLTree_node | [2,2,4,4,4] | 16 | 16 | yes |
| ResXMLTree_attrExt | [4,4,2,2,2,2,2,2] | 20 | 20 | yes |
| ResXMLTree_attribute | [4,4,4,2,1,1,4] | 20 | 20 | yes |
| Res_value | [2,1,1,4] | 8 | 8 | yes |

Different fields: **none**. JSON key sets are equal (8 keys, `sort_keys=True` ordering reproduced).

## 4. Do the width maps actually match the S038 struct definitions?

Checked against the pinned snapshot `corpus/snapshots/ResourceTypes.h` (sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 bytes — identical to `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`), whose struct anchors match the S038 registry row (`corpus/SOURCES.md:52`: ResChunk_header :218, Res_value :287, ResStringPool_header :461, ResXMLTree_node :621, ResXMLTree_attrExt :677, ResXMLTree_attribute :707):

- `ResChunk_header` @218: `uint16_t type;` (222) `uint16_t headerSize;` (227) `uint32_t size;` (234) → [2,2,4] ✓
- `Res_value` @287: `uint16_t size;` (290) `uint8_t res0;` (293) `uint8_t dataType;` (351) `typedef uint32_t data_type; data_type data;` (408-409) → [2,1,1,4], 8 bytes, no padding (data lands at offset 4) ✓
- `ResStringPool_header` @461: nested header + `uint32_t stringCount;` (467) `styleCount;` (471) `flags;` (482) `stringsStart;` (485) `stylesStart;` (488) → five uint32 after the chunk header → [2,2,4,4,4,4,4,4], 28 ✓
- `ResXMLTree_node` @621: header + `uint32_t lineNumber;` (626) + `struct ResStringPool_ref comment;` (629); `ResStringPool_ref` @430 is `uint32_t index;` → [2,2,4,4,4], 16 ✓
- `ResXMLTree_attrExt` @677: 2× `ResStringPool_ref` (ns/name) + six `uint16_t` (`attributeStart` 687, `attributeSize` 690, `attributeCount` 695, `idIndex` 698, `classIndex` 701, `styleIndex` 704) → [4,4,2,2,2,2,2,2], 20 ✓
- `ResXMLTree_attribute` @707: ns/name/rawValue (`ResStringPool_ref`) + `struct Res_value typedValue;` (719) → [4,4,4,2,1,1,4], 20, attributeStart offset 20 and attributeSize 20 both consistent with natural alignment (typedValue at offset 12) ✓

Cross-check with the entry's own item 8: `--fact axml_start_element` prints `attributeStart: 20`, `attributeSize: 20` (`EXIT=0`), agreeing with the derived 20/20 as item 5's second paragraph asserts.

## 5. Prose judgement (does it state anything the output does not support?)

Sentence under test (entry line 59):

> The fixed structure widths used by the readout are computed by summing the field widths of S038's own struct definitions (two `uint16` plus one `uint32` for `ResChunk_header`; five `uint32` after the chunk header for `ResStringPool_header`; and so on), not assumed:

- "two `uint16` plus one `uint32` for `ResChunk_header`" — supported: `[2, 2, 4]`, and true of snapshot 218-234.
- "five `uint32` after the chunk header for `ResStringPool_header`" — supported: the 8-element array is 3 header widths + five `4`s; true of snapshot 461-488.
- "`and so on`" — supported; the four remaining maps each match their struct field lists (section 4).
- "computed by summing ... not assumed" — supported for the fact itself: `readout.py:56` is `sizes = {name: sum(w) for name, w in widths.items()}`, i.e. the printed `total_bytes` are sums, and every sum re-verifies.
- **Precision finding (LOW, not a value error):** the clause "used by the readout" is stronger than the fact's own evidence. The AXML parser consumes *hand-coded literal offsets*, not the `sizes` dict — `readout.py:152-153` (`so+16`, `so+20`), `readout.py:190-209` (`base+16`, `base+20`, `base+24/26/28/30/32/34`, `aoff+12/15/16`) — and only the string-pool offset table uses an observed header field (`so + sp["headerSize"] + 4*i`, `readout.py:157`). The output proves the widths are derived by summation; it cannot by itself prove those derived widths are what the parser imports. In source they are numerically the same constants (16 and 20 map onto `base+16` and the `typedValue` offset `aoff+12..19`), so the sentence's *substance* is correct, but its provenance wording ("used by the readout are computed ... not assumed") overstates what the emitted fact shows. A precise phrasing would be: "the same widths the readout encodes as literal offsets, re-derived here by summing S038's field lists".
- Second paragraph (line 66): "The derived 20-byte `ResXMLTree_attrExt` size is the `attributeStart` value observed in the start-element chunk in item 8, and the derived 20-byte `ResXMLTree_attribute` size is the observed `attributeSize`." — supported by `--fact axml_start_element` (`attributeStart: 20`, `attributeSize: 20`).

## 6. Residual risk / gaps

- Scope is this one fact plus the three member facts as instructed; no attempt to re-derive items 6-11 beyond the item-8 cross-check quoted above.
- Provenance chain intact on what I could read: snapshot sha256 `56b88bc...` (86255 bytes) equals the pinned round-65 snapshot and the S046 registry claim (`corpus/SOURCES.md:61`); `derive_axml_anchors.py` sha256 `bce497d6...` also matches its S046 row.
- No file was edited by this seat; only `/tmp/r68i5_actual.json` (scratch) was written outside the report path. No tools installed or upgraded during this review.
