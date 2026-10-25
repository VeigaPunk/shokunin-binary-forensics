PASS — Q03 holds on the round-69 C05 v4 candidate: every expected value I re-derived comes from the fixture's own bytes, the pinned S038 snapshot bytes, or the cited specifications (APPNOTE §4.3.7/§4.3.12, S045 `header_item`); nothing is copied from `truth.json` (the oracle the entry claims to match) or from the round-68 v3 record, and no saved path is used as both identity and locator.

- criterion: **Q03** — expected values derived independently (from bytes, a specification, or a pin fixed outside the record under test); reject when an expected value is copied from the record under test or a saved path serves as both identity and locator. Lesson classes: M06, M14.
- entry under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md` (160 lines; `admission-status: candidate`, line 11)
- lane HEAD at review: `35e12584d37434632fa06a6c2975ab55f29a8d3f`; `git status --porcelain corpus/knowledge corpus/fixtures corpus/snapshots corpus/derive_axml_anchors.py` → empty
- I did not read the entry's §Q-map rows as evidence for this criterion (and the map has no Q03 row — see residual 1). No file was edited; no package installed.

## Evidence: the three independent derivation roots

### 1. Bytes — the fixture is the primary record, read directly

```
$ sha256sum corpus/fixtures/apk-r65/readout.py corpus/derive_axml_anchors.py \
            corpus/fixtures/apk-r65/fixture.apk corpus/fixtures/apk-r65/truth.json \
            corpus/fixtures/apk-r65/generator.py corpus/snapshots/ResourceTypes.h
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
```
Every digest matches the entry's `source:` S041/S047 lines and the `recheck:` stdout pin (lines 1-10 of the entry header). `readout.py` reads only `fixture.apk` (`APK = ROOT / "fixture.apk"`, readout.py:20-21; the whole file was read — no reference to `truth.json` exists in it); `derive_axml_anchors.py` reads only `snapshots/ResourceTypes.h` (`path = Path(__file__).resolve().parent / SNAPSHOT_REL`, main()) and exits 2 on a digest mismatch against the hardcoded pin.

Fresh run of the entry's own command, and the pin it claims:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/revenger-r69-q03-readout.out; echo exit=$?
exit=0
$ wc -l /tmp/revenger-r69-q03-readout.out
15 /tmp/revenger-r69-q03-readout.out
$ sha256sum /tmp/revenger-r69-q03-readout.out
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```
15 lines and `507d79f8…` match the entry's `recheck:` clause and §Reproduce exactly.

Per-fact comparison of the entry's embedded JSON lines against that fresh stdout (each fact is embedded twice — once in its item block, once in the full stdout block):

```
embedded facts: 15 actual facts: 15
facts only in entry: []
facts only in actual: []
MATCH archive / axml_chunk_table / axml_end_element / axml_end_namespace / axml_resource_map /
      axml_start_element / axml_start_namespace / axml_string_pool / dex_declared_header / eocd /
      jar_manifest / member[AndroidManifest.xml] / member[META-INF/MANIFEST.MF] / member[classes.dex] /
      spec_derived_struct_widths          (30/30 lines, 0 diffs)
```

So no value in items 1-10 is stated from the oracle: each is printed by a command that reads only `fixture.apk`.

### 2. Specification / pin — the AXML anchors come from the pinned snapshot, not the fixture

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
exit=0
```
All 20 lines are byte-identical to the entry's item-11 block (entry lines 131-150); I diffed them line by line: `OK` ×20, 0 diffs.

The pin is fixed outside the record under test and the copy is genuine, not a same-path identity claim:

```
$ sha256sum .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f
$ wc -c corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
 86255 corpus/snapshots/ResourceTypes.h
 86255 .ufo/waves/round-65/source-snapshots/ResourceTypes.h
172510 total
$ cmp corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h && echo IDENTICAL
IDENTICAL
```
Identity = digest, locator = current-root path; the historical path is a second, digest-checked copy — the M14 pattern in its fixed form, not its defect form.

Snapshot lines backing the transcription in item 5 (field lists, read from the snapshot itself):

```
218 | struct ResChunk_header            222 uint16_t type; 227 uint16_t headerSize; (… uint32_t size)
461 | struct ResStringPool_header       467 stringCount, 471 styleCount, 482 flags, 485 stringsStart, 488 stylesStart
621 | struct ResXMLTree_node            626 uint32_t lineNumber; 629 struct ResStringPool_ref comment;
677 | struct ResXMLTree_attrExt         680 ns, 684 name, 687 uint16_t attributeStart; 690 attributeSize;
695 |                                 698 idIndex, 701 classIndex, 704 styleIndex  (all uint16_t)
707 | struct ResXMLTree_attribute       710 ns, 713 name, 716 rawValue, 719 typedValue (Res_value)
287 | struct Res_value                  290 uint16_t size; 293 uint8_t res0; (enum : uint8_t) … uint32_t data
```
Sums: 8 / 28 / 16 / 20 / 20 / 8 — exactly the `total_bytes` the readout prints and the `headerSize` column in item 4 (28, 8, 16, 16, 16, 16) and `attributeStart`/`attributeSize` 20 in item 8. The widths are a hand transcription, which the entry labels manual at line 61 ("**manually transcribed** in `readout.py:51-58` … a manual transcription, labeled manual, not a runtime derivation") — Q03 admits "a specification", and I verified the transcription is spec-true against the snapshot lines quoted above. `readout.py:51-58` is the width source (line 51 `w8, w16, w32 = 1, 2, 4`; 52-59 `widths = {…}`).

Spec re-derivations of the container offsets the entry attributes to S032/S034 (independent of `fixture.apk`):

```
.ufo/waves/round-63/source-snapshots/appnote.txt:387  4.3.7  Local file header:
  signature 4 + version 2 + flags 2 + method 2 + time 2 + date 2 + crc-32 4 +
  compressed 4 + uncompressed 4 + name len 2 + extra len 2  = 30 bytes
  → crc at +14, compressed at +18, uncompressed at +22, name len at +26, extra at +28

.ufo/waves/round-63/source-snapshots/appnote.txt:511  4.3.12  Central directory structure:
  signature 4 + 5×2 + crc 4 + 3×4 + comment len 2 + disk 2 + internal 2 + external 4 + local offset 4 = 46 bytes
  → name len at +28, extra at +30, comment at +32, local-header offset at +42
```
Those are exactly the offsets `readout.py:88-105` uses and the 46/30 widths item 3 cites. S045's three quoted clauses are present verbatim in the pinned snapshot:

```
must be 0x70 (112) bytes (v40 or earlier)
adler32 checksum of the rest of the file (everything but magic and this field)
SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)
ENDIAN_CONSTANT = 0x12345678;
```
and the entry's recomputation windows (checksum over `dex[12:]`, signature over `dex[32:]`) are exactly those clauses (8-byte magic + 4-byte checksum = 12; + 20-byte signature = 32).

### 3. The oracle is compared, never the source of an expected value

Item 7's expected values are printed from the resource-map chunk, not taken from the oracle:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_resource_map
{"entry_count": 9, "fact": "axml_resource_map", "ids": ["0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x0101021b", "0x0101021c", "0x00000000", "0x00000000"], "nonzero": {"versionCode": "0x101021b", "versionName": "0x101021c"}, "offset": 204}
```
The name→id mapping is byte-derived (`res_id = ids[aname]`, readout.py), not oracle-supplied. I then compared `truth.json` to the fresh readout field by field: 0 real mismatches across image sha256/size, all three members' `local_header_offset`/`compressed_size`/`uncompressed_size`/`crc32`/`sha256`, the 9 strings, the 9 resource ids, and the three attribute rows (`name_idx`, `ns_idx`, `raw_value_idx`, `data_type`, `data`); the only two diffs were cosmetic formatting (`0x3` vs `0x03` for attribute 0 and 2). The oracle's only field absent from the readout is `method` (not a shared field, see residual 2).

Independent byte-side spot checks I did myself (not via the readout):

```
local header at 0   method=0 flags=0x0 name_len=19 extra_len=0
local header at 465 method=0 flags=0x0 name_len=11 extra_len=0
local header at 618 method=0 flags=0x0 name_len=20 extra_len=0
manifest payload repr: b'Manifest-Version: 1.0\r\nCreated-By: revenger-r65 fixture generator\r\n\r\n'
AXML start-element bytes @chunk 272: 0201 1000 60000000 01000000 ffffffff ffffffff 02000000 1400 1400 0300 0000
  → type 0x0102, headerSize 16, size 96, lineNumber 1, comment -1, ns -1, name 2, attributeStart 20,
    attributeSize 20, attributeCount 3, idIndex 0
```
These confirm items 1-4, 8 (including "all four node chunks carry `lineNumber` 1"), 9 and 10 against bytes without the entry's script.

## Entry lines at issue (all PASS on Q03)

- line 23 (item 1): 947 bytes + sha256 — `{"bytes": 947, … "sha256": "05d2280f…"}`; bytes-derived.
- lines 30-36 (item 2): 925 / 3 / 188 / 737 with `737 + 188 == 925` — `{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, … 737 / 188 / 3}`; bytes-derived + arithmetic.
- line 37 (item 3): 46-byte and 30-byte widths — spec (APPNOTE §4.3.12/§4.3.7, widths summed above); offsets recomputed by me from the same field lists.
- line 52 / 59 (item 4): chunk types/`headerSize` — bytes (`"type": 1/384/256/258/259/257`, `headerSize` 28/8/16/16/16/16) plus the 20 derived enum lines (:239/:241/:244/:245/:246/:247/:248/:253, values 0x0001/0x0003/0x0100/0x0100/0x0101/0x0102/0x0103/0x0180).
- line 61 (item 5): struct widths 8/28/16/20/20/8 — manual transcription from S038 field lists (snapshot lines quoted above), labeled manual.
- line 70 (item 6): 9 / 0 / `0x00000100` / 64 — `{"stringCount": 9, "styleCount": 0, "flags": "0x00000100", "stringsStart": 64, "utf8": true}`; the `0x100` semantic is S038 `UTF8_FLAG = 1<<8` (snapshot line 480), tested at `readout.py:166`.
- line 77 (item 7): `0x0101021b`/`0x0101021c`, seven zeros — bytes (line quoted above); oracle only cross-checked.
- line 84 (item 8): attributeStart/Size/Count 20/20/3 and the attrExt-relative formula — bytes (`{"attributeStart": 20, "attributeSize": 20, "attributeCount": 3}`) + S038 lines 675/677/686/687 (675 = "Appears header.headerSize bytes after a ResXMLTree_node.", 686/687 = comment and field, both derived).
- line 91: `0xffffffff` namespace index — printed as `4294967295`; same value, treated null at `readout.py:22`.
- line 109 (item 9): `0x3d120c30`, 20-byte signature, 112/112, `0x12345678` — `{"checksum_recomputed": "0x3d120c30", "declared_checksum": "0x3d120c30", "file_size": 112, "header_size": 112, "endian_tag": "0x12345678", "signature_matches": true}` + the S045 quotes above.
- line 118 (item 10): 69 bytes, `Manifest-Version: 1.0`, 1 section — `{"bytes": 69, "first_line": "Manifest-Version: 1.0", "section_count": 1}`.
- line 127 (item 11): the 20-line derivation + bounded credit — 20/20 lines match the fresh run; the script derives each line number by searching the pinned snapshot and its enum values with `VALUE_RE` on the found line (no hardcoded value table).
- line 157 (§Comparison): "The readout values agree with it on every shared field" — verified true on every shared field I could compare (0 real mismatches).

No line carries an expected value that is absent from these outputs or from the cited spec. I audited every numeric token in items 1-11 against the union of the readout stdout and the derivation stdout; the only tokens not present are source-line pointers (`readout.py:99-105`, `readout.py:166`, `readout.py:200-203`) and the decimal spelling of `0xffffffff`.

## Residual risk and verification gaps (not Q03 fails)

1. **The entry's §Q-map omits Q03** (rows present: Q01, Q02, Q04, Q05, Q07, Q11, Q13, Q14 — lines 177-184; Q03/Q06/Q08/Q09/Q10/Q12/Q15 absent). My verdict is independent of the map, but the map's incompleteness is a separate observation for the gate: the claims §C1 requires an all-PASS Q01–Q15 wave, and the entry itself self-declares only 8 criteria.
2. **Line 167 (Limitations): "The container is ZIP_STORED with no data descriptors"** is not printed by any in-entry command. It is byte-true — I read `method=0, flags=0x0` at the three local headers (offsets 0/465/618) — but the derivation is not carried inside the entry. That is a Q11-shaped residual (a value without its command), not Q03: it is a limitation statement, not an expected value.
3. **Item 5's widths are manual** — the readout reprints constants rather than re-deriving them, so a mutation of S038's field list would not be caught by any command (Q04/Q13 shape). The entry labels the transcription manual (line 61); Q03 permits a specification, and I verified the transcription against the snapshot.
4. **Resource-id identity is oracle-scoped by design**: nothing outside the fixture (S038 carries no attribute-id table) independently grounds `0x0101021b` = android:versionCode. The entry scopes this correctly at line 77 ("exactly the two attribute ids the fixture's authored oracle declares … which is the correspondence this entry claims") after the v4 delta that dropped "framework". A stricter reading that demands platform-level grounding would have to reject the *scope sentence*, not the derivation; Q03 as written is satisfied by bytes.
5. Not verified here (out of criterion): the derive script's exit-2 path on a missing/ambiguous symbol, and the README C05 row state; Q03 only concerns where expected values come from.
6. Tooling: no install or upgrade was performed. Scratch `/tmp/revenger-r69-q03-*` deleted; no lane file written except this report.
