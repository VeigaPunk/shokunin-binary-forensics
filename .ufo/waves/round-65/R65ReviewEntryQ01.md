PASS — every load-bearing claim in `corpus/knowledge/round-65-apk-axml-byte-evidence.md` maps to a tier-A `corpus/SOURCES.md` row inside that row's stated scope; no tier-C row is cited anywhere. Two non-load-bearing citation defects are reported below and should be repaired before the C05 flip.

Reviewed bytes: lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` at `HEAD 8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0`, working tree clean (`git status --porcelain` empty); entry blob `f02952afa622de99e3399fd098ad9db297083feb`, sha256 `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7`. Contract read first: `reports/round-65/claims.md` (Q01:0 lines 60-67, quantization at `corpus/QUALITY.md:13`).

## Criterion text applied

`corpus/QUALITY.md:13` — Q01: each **load-bearing** claim rests on a `SOURCES.md` row that is tier A **for that claim's scope** and was opened in the round that wrote it; a tier-C row is never sole support; reject when "the claim exceeds what the cited text states".

## Per-claim support mapping

| # | Claim (entry line) | Row → stated scope | Anchor checked in snapshot/local bytes | Verdict |
|---|---|---|---|---|
| 1 | archive 947 B, sha256 `05d2280f…` (entry:17-21) | **S041** own-work, A, opened 2026-10-24 — "byte content of one authored 947-byte APK fixture" (`SOURCES.md:55`) | `sha256sum corpus/fixtures/apk-r65/fixture.apk` = `05d2280f…d03e` | in scope |
| 2 | EOCD at 925, 3 entries, CD 188 B at 737, 737+188=925 (entry:25-29) | **S032** spec, A, `SOURCES.md:46` — EOCD field layout; "two total-entries counts sit at offsets 8 and 10" | `readout.py:77-84` reads +10/+12/+16; APPNOTE §4.4.21-22 per row | in scope |
| 3 | CD records 46 B fixed part, local headers 30 B, CRC recompute, walk end == EOCD (entry:33) | **S032** (`:46`: 46-byte record, crc at 16, local-header offset at 42) + **S034** (`:48`: 30-byte record, name len 26, extra len 28) | `readout.py:69-76` offsets match the row text | in scope |
| 4 | AXML header type 0x0003, headerSize 8, total 416, six chunk types incl. 0x0180 (entry:49-53) | **S038** spec, A, opened 2026-10-24 (`SOURCES.md:52`) — AXML chunk/string-pool/node structures, pinned `android-15.0.0_r1` | snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` sha256 `56b88bc4…c56f` = entry:1/row:52: `ResChunk_header` :218; 0x0003 :241, 0x0100 :245, 0x0101 :246, 0x0102 :247, 0x0103 :248, 0x0180 :253 | in scope (anchor range defect L1) |
| 5 | derived widths 8/28/16/20/20/8 from S038 field lists (entry:55-62) | **S038** structs :218, :461, :621, :677, :707, :287 | re-summed from snapshot: `ResChunk_header`[2,2,4]=8; `ResStringPool_header` 8+5×4=28; `ResXMLTree_node` 8+4+4=16; `attrExt` 4+4+6×2=20; `attribute` 3×4+8=20; `Res_value`[2,1,1,4]=8 | in scope |
| 6 | string pool: 9 strings, 0 styles, flags 0x100, stringsStart 64 (entry:64-69) | **S038** `ResStringPool_header` :461 + `UTF8_FLAG = 1<<8` :480 | snapshot: 0x100 = UTF8_FLAG at :480; bytes from S041 | in scope |
| 7 | resource-map ids; "S038's `getAttributeNameResID` semantics make 0 'no resource id'" (entry:71-73) | **S038** chunk-type 0x0180 :253 for the chunk; values from S041 bytes; two non-zero ids fixture-declared | snapshot :792 is a bare declaration — **no** text states a 0 return; the "0 if none" comments at :697/:700/:703 belong to `idIndex`/`classIndex`/`styleIndex` | values in scope; **gloss exceeds cited text (M2)** |
| 8 | start element `manifest`, attributeStart/Size 20, 3 attributes, `0xffffffff` null index (entry:75-97) | **S038** `ResXMLTree_attrExt` :677, `ResXMLTree_attribute` :707, `Res_value` :287; null index :628 ("-1 if none") | snapshot fields match derived widths; null-index sentence is already labeled Inference at entry:126 | in scope |
| 9 | dex declared header: magic `dex\n035\0`, Adler-32 over 12+, SHA-1 over 32+, file/header size 112, endian 0x12345678 (entry:101-107) | **S041** own-work, A — scope explicitly names "dex declared header" and "generator and readout script"; qualifier "byte/oracle correspondence only, not … dex validity" (`SOURCES.md:55`) | independent recompute below; `generator.py:130-147`, `readout.py:233-248` | in scope as authored convention; **no dex-format spec row exists (M1)** |
| 10 | jar manifest 69 B, first line `Manifest-Version: 1.0`, 1 section (entry:109-113) | **S041** bytes; oracle member row declares 69 B, crc `e948d738`, sha256 `2e5da249…` | oracle comparison all-true below | in scope |
| 11 | "agrees with the oracle on every shared field" (entry:105-106) | **S041** oracle `truth.json` | 13/13 comparisons true (below); oracle has **no** dex block, so the sentence correctly excludes item 9 | in scope |
| 12 | provider-route fence (entry:135) | **S039** docs, A, opened 2026-10-24 — "route-scope sentences only … not provider execution on this host, not the authored fixture bytes" (`SOURCES.md:53`) | used only in the Q10 fence; no byte claim cites S039 (all 4 citations at entry:2,135) | in scope, non-load-bearing |

Rows cited anywhere in the entry: S032×3, S034×3, S038×13, S039×4, S041×3 (`grep -on 'S0[0-9][0-9]'`). All five are tier **A**. **No tier-C row is cited** — `S040` is `queued` and is correctly *not* cited: `readout.py` imports only `struct`, `zlib`, `hashlib`, `json`, `sys` (no `zipfile`).

## Findings

### M1 (Medium) — dex field semantics rest on the authored convention, not a spec row

Entry:101-107 presents field identities and offsets of the `classes.dex` header — checksum at 8..12 = Adler-32 of 12.., signature 12..32 = SHA-1 of 32.., `file_size`@32, `header_size`@36, `endian_tag`@40, `format_version 035`. No `SOURCES.md` row has dex/Dalvik format scope: `grep -in 'dalvik\|dex' corpus/SOURCES.md` returns only unrelated rows (S007, S020, S030) plus S041 itself. `truth.json` declares **no** dex fields (top keys `axml_declared`, `build_recipe`, `image`, `members`; member keys `compressed_size`, `crc32`, `local_header_offset`, `method`, `name`, `sha256`, `uncompressed_size`), so the rule is declared only by `generator.py:137-144` and re-applied by `readout.py:233-248` — the record under test.

Why this is still Q01 in-scope: S041's scope phrase explicitly names the "dex declared header" plus "generator and readout script", and entry:103 is grammatically fixture-bound ("**Its** declared checksum …"). The sentence asserts a measured equality on this fixture, not a general dex-format rule. It is load-bearing for the coverage-map's dex element, and S041 (tier A, opened this round) covers it.

Repair (before the flip): add one clause to item 9 that the checksum/signature offsets are the generator's declared convention (S041), or mine a dex-format spec row at a pinned tag and cite the offsets. The Q01 basis row (entry:141) should also name S041 for the dex block instead of leaving the dex field layout under the generic "fixture content" catch-all. If L1 instead reads "declared checksum" as a Dalvik-format assertion, Q01 flips to FAIL absent a spec row — that reading should be recorded explicitly either way.

### M2 (Medium) — `getAttributeNameResID` attribution exceeds the cited text

Entry:71: "Seven entries are `0x00000000` — S038's `ResXMLTree::getAttributeNameResID` semantics make 0 \"no resource id\"". Snapshot `ResourceTypes.h:792` is `uint32_t getAttributeNameResID(size_t idx) const;` with no doc comment; `grep -n 'getAttributeNameResID'` finds only :792. S038's own anchor list (`SOURCES.md:52`) stops at `:707`, so :792 is outside the row's named anchors. The three "0 if none" comments at :697/:700/:703 describe `ResXMLTree_attrExt.idIndex/classIndex/styleIndex` — different fields from a resource-map entry.

This is exactly Q01's reject example ("the claim exceeds what the cited text states"), but it is **not load-bearing**: the seven zeros are reported as measured values, and no later claim consumes "no resource id". Entry:126's Inference list also omits this gloss. Repair: label it as inference (with the byte evidence) or drop the attribution; do not let it stand as S038-stated text. Because the criterion's subject is load-bearing claims, this does not fail Q01 — it must be reworded so the Q01 basis row (entry:141) is not resting a source claim on text S038 does not contain.

### L1 (Low) — enum anchor range is three lines short

Entry:1 and entry:53 attribute `RES_XML_RESOURCE_MAP_TYPE = 0x0180` to "lines 239-250"; the value is at snapshot `ResourceTypes.h:253`, outside the cited range. The value itself is correct and the enum is inside S038's declared scope; this is a Q02/Q11 precision defect, not a tier/scope breach. `SOURCES.md:52` carries the same `:239-250` range, so the repair belongs on the row too (or cite `:239-254`).

### Note A — S032/S034 are round-63 rows, not "opened this round"

`SOURCES.md:46,48` are `mined 2026-10-23` (round 63). QUALITY.md:13's literal clause "was opened in the round that wrote it" is not met. The seat brief explicitly authorizes "S032/S034 registry tier-A for ZIP field offsets", `claims.md` pre-registers the reuse ("already mined as S032 … S034"), and the entry discloses it at entry:11 ("already mined as S032 … S034"). Under that pre-registered reading there is no tier/scope breach: every offset the readout uses (EOCD +10/+12/+16; CD +16 crc, +42 local-header offset, 46-byte fixed part; local 30-byte fixed part, +26 name, +28 extra) is inside the two rows' stated scopes. L1 should record the registry-reuse reading in the Gate.

### Note B — S039 correctly non-load-bearing

All S039 uses are the header and the Q10 fence (entry:2,135); no byte claim cites it. `claims.md`'s "route-scope only" bound is respected.

## Commands and output (actual)

- `sha256sum corpus/fixtures/apk-r65/*`:
  `05d2280f…7d03e  fixture.apk` (947 B), `eaa9444c…27c1a  generator.py`, `92e347c3…3976  readout.py`, `27303bae…f8173  truth.json` — all four match entry:1-3 and `SOURCES.md:55`.
- `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 lines, `sha256sum` of stdout = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — matches entry:5 and entry:159.
- Independent dex recompute (`zipfile` used only as my reviewer cross-check, not an entry claim): `declared_checksum 300c123d` (LE = 0x3d120c30) vs `adler32(d[12:]) 0x3d120c30`; `declared_sig a5fc7bea8fa9ffaa52243540c8026066511b9fce` vs `sha1(d[32:])` equal; `file_size@32=112`, `header_size@36=112`, `endian@40=0x12345678`.
- Oracle correspondence: 13/13 true (`image.sha256`, `image.size`, `members.crc32`, `members.offsets`, `members.sha256`, `strings`, `res_ids`, `attr_names`, `attr_ns_idx`, `attr_name_idx`, `attr_raw_idx`, `attr_types`, `attr_data`), Python `3.14.8` — matches entry:105-106 and the `verified-at` note.
- S038 snapshot sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` = entry:1 / `SOURCES.md:52`; anchor lines re-read at :218, :241-253, :287, :461, :480, :612, :621, :628, :677, :697-704, :707, :792.
- `grep -in 'dalvik\|dex' corpus/SOURCES.md` → no dex-format row.
- `corpus/README.md:34` still `| C05 | Android packages (APK) | — | — | frontier |` — consistent with the frozen admission order (`claims.md` step 3); this review neither requires nor performs the flip.
- No tool installation was needed or performed; no pacman transaction run.

## Residual risk and verification gaps

- **S032/S034 external bytes were not re-opened this round.** `.ufo/waves/round-65/source-snapshots/` contains only `ResourceTypes.h`, `rea-android-applications.md`, `zipfile-docs.html`; there is no APPNOTE snapshot. My ZIP-offset check is against the row text (`SOURCES.md:46,48`) plus the readout's own comments, not the spec bytes. If L1 requires byte-level APPNOTE proof for the reused rows, that is a round-63 artifact, not a round-65 one.
- **Entry is a moving target.** Checks bind to blob `f02952af…` / sha256 `e173e643…`. Any later edit invalidates the line numbers and the Q-map quotation above.
- **M1 reading is judgment, not measurement.** The Q01 outcome hinges on whether "declared checksum" is read as fixture-anchored (PASS, as I rule) or as a format assertion (FAIL). I state the reading and the repair so the Gate decision is explicit rather than implicit.
- I did not re-score Q02-Q13 or the C2/C5 work; those belong to their named seats. Nothing observed here contradicts the entry's other Q rows.
