PASS — Q03 (expected values derived independently) on `corpus/knowledge/round-68-apk-axml-byte-evidence.md`: every expected value the entry checks against is fixed outside the record under test — S038 snapshot lines / enum values / struct widths, S045's declared `header_item` semantics, the S032+S034 APPNOTE record widths, and the generator's authored constants in `truth.json` `axml_declared` — and no expected value is taken from the fixture's own declarations; identity (sha256 pins) is separated from location (repo-relative paths; relocated replay is byte-identical).

seat: L1Revenger68.R68ReviewEntryQ03 · criterion: Q03 only · file under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md` (admission-status: candidate) · round-68 C2 bytes · no production edits (report only).

## Criterion as applied
`QUALITY.md` Q03: "Expected values are derived independently: from bytes, a specification, or a pin fixed outside the record under test. Reject when: the expected value is copied from the record being checked, or a saved path is used as both identity and locator" (lessons M06, M14).

I did not take the entry's §Q-map row (line 174) as evidence. Its stated basis is *narrower* than the entry's real evidence: it names the oracle, the S038 widths and S045, but omits the S032/S034 container widths and the declared-vs-recomputed digest class, and it does not separate the oracle's authored block (`axml_declared`) from its measured block (`image`, `members`). The findings below are from executing the commands and re-deriving values with a second instrument.

## Commands run and observed output

Both entry commands, from the lane root, actual stdout:

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/fixtures/apk-r65/readout.py
readout exit=0
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/r68q03-readout.out
  15 /tmp/r68q03-readout.out        # 15 "fact" objects, 15 distinct ids

$ python3 -B corpus/derive_axml_anchors.py
anchors exit=0 ; 17 lines
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

The readout stdout SHA-256 equals the `recheck:`/§Reproduce pin `507d79f8…6dad247`; the anchor table equals entry item 11 line for line, including `:245`. Pins match the entry:

```
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h   (86255 bytes)
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
```

## Re-derivation with a second instrument (not the entry's readout)
I wrote a separate struct walk (`/tmp/r68q03/indep.py`, `/tmp/r68q03/indep2.py`; byte offsets computed in my script, not copied from the readout). Output vs the entry's embedded lines:

| entry | my independent value | agrees |
|---|---|---|
| 947 bytes, sha256 `05d2280f…7d03e` | `size 947 sha256 05d2280f…7d03e` | yes |
| EOCD `504b0506` @925, 3 entries, CD 188 @737, `737+188==925` | `eocd_offset 925 total_entries 3 cd_size 188 cd_off 737 cd_end_eq True` | yes |
| members lho 0/465/618, payload 49/506/668, sizes 416/112/69, CRC `962d075f`/`2635c82a`/`e948d738` | identical, plus `recomp` CRC equal for all three; `walk_end 925 == eocd True` | yes |
| chunk table 6 rows, xml type 3, total 416 | `chunks [(8,1,28,196),(204,384,8,44),(248,256,16,24),(272,258,16,96),(368,259,16,24),(392,257,16,24)] total 416 eq_member True` | yes |
| pool 9 strings / 0 styles / flags `0x100` / stringsStart 64 / offsets / 9 strings | identical (`pool count 9 styles 0 flags 0x100 sstart 64`; same offsets and string list) | yes |
| resource map 9 entries, 7 zero, `0x0101021b`, `0x0101021c` | `entry_count_from_size 9` (from chunk size 44: `(44-8)/4`), same ids | yes |
| start element @272, aStart 20, aSize 20, aCnt 3, name `manifest` | identical; `chunk_rest_after_node_header 80 == attr_span_end 80` | yes |
| 3 attribute rows incl. `res_id` 16843291/16843292 | `attr 1 … res_id 0x101021b`, `attr 2 … res_id 0x101021c`; type `0x3`/`0x10`; data 4/1/8 | yes |
| start ns 248 (prefix 0, uri 1), end ns 392, end el 368 `manifest`, lineNumber 1 | identical for all four node chunks | yes |
| dex magic `6465780a30333500`, declared `0x3d120c30` = adler32(d[12:]), sig `a5fc7bea…` = sha1(d[32:]), file_size/header_size 112, endian `0x12345678`, header_bytes 112 | identical, all four independently recomputed | yes |
| jar 69 bytes, `Manifest-Version: 1.0`, 1 section | identical | yes |

Independent reader corroboration: `zipfile` reports `AndroidManifest.xml 0 416 962d075f`, `classes.dex 465 112 2635c82a`, `META-INF/MANIFEST.MF 618 69 e948d738` — same offsets/CRCs as the raw walk.

## Why the reject clause does not fire (per value class)
1. **Authored pins (independent of the bytes).** `truth.json` `axml_declared.strings` / `.attributes` / `.resource_ids` are generator input constants (`corpus/fixtures/apk-r65/generator.py:205-213` from `STRINGS`/`ATTRIBUTES`/`RESOURCE_IDS`), not parsed back. The entry's strings, three attribute rows and two non-zero ids agree with them: `resource_ids 0x0101021b 0x0101021c`; `attrs [(3,3,4,4),(5,16,1,7),(6,3,8,8)]`. These expectations predate the bytes.
2. **Specification.** S038 snapshot fixes every AXML expectation, verified by direct read: `RES_XML_START_NAMESPACE_TYPE = 0x0100` at 245 and `RES_XML_FIRST_CHUNK_TYPE = 0x0100` at 244; `RES_STRING_POOL_TYPE` 239, `RES_XML_TYPE` 241, end ns 246, start/end element 247/248, `RES_XML_RESOURCE_MAP_TYPE` 253; `SORTED_FLAG = 1<<0` at 477 and `UTF8_FLAG = 1<<8` at 480; `TYPE_STRING = 0x03` at 307, `TYPE_INT_DEC = 0x10` at 327; attrExt comment at 686 and `uint16_t attributeStart;` at 687. Struct widths: `ResChunk_header` 8, `ResStringPool_header` 28, `ResXMLTree_node` 16, `ResXMLTree_attrExt` 20, `ResXMLTree_attribute` 20, `Res_value` 8 — each matches the snapshot's own field lists (`:461-490`, `:621-632`, `:677-700`, `:705-725`). S045 snapshot carries the exact quoted clauses: `adler32 checksum of the rest of the file (everything but` / `magic and this field)` (`source-snapshots/dex-format.html:5949`), `SHA-1 signature (hash) of the rest of the file (everything but` / `magic, checksum, and this field)` (`:5956`), `must be 0x70 (112) bytes` (`:5981`), `uint ENDIAN_CONSTANT = 0x12345678;` (`:5035`).
3. **Declared-vs-recomputed over bytes.** The digest/checksum expectations are recomputations (`zlib.adler32(dex[12:])`, `hashlib.sha1(dex[32:])`, `zlib.crc32(payload)`), and `file_size` is checked against `len(payload)` (both 112), `xml_total_size` against the member length (both 416), CD end against EOCD offset (`925==925`). Byte-derived expectations are explicitly admissible under Q03.
4. **M14 separation.** Identity is carried by sha256 pins (fixture, readout, script, snapshot); location is repo-relative (`readout.py` resolves `Path(__file__).resolve().parent`, prints `"path": "corpus/fixtures/apk-r65/fixture.apk"`). Relocation proof: I copied `readout.py`+`fixture.apk` and `derive_axml_anchors.py`+`snapshots/ResourceTypes.h` into `/tmp/r68q03/tree/corpus/…` and ran both from `/`:

```
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -   (readout, relocated)
b02cfe54df5af9e8ca16c61c3d4c719ebb18ac3e9d1cf23b48686628bf3e0831  -   (anchors, relocated)
IDENTICAL (anchors vs in-repo run)   READOUT-IDENTICAL-RELOCATED
absolute-path leak grep count: 0
```

Nothing is degraded by moving the tree, so no saved path serves as both identity and locator.

## Findings at issue (none of them a Q03 failure; each needs an owning criterion)
- **R1 — entry line 152 (§Comparison), oracle agreement on container fields.** "image sha256 and size (item 1), the three members' local-header offsets, payload sizes and CRC-32 values (item 3)" — those oracle blocks are build-time measurements of the same bytes (`generator.py:175-177` docstring "Measure member offsets and payload digests from the finished zip bytes"; `:196 measured = parse_members(apk)`; `:199 hashlib.sha256(apk)`). The agreement is therefore a second reading, not independent confirmation. The entry says "measured", Q03 admits byte-derived expectations, and items 1/3 establish their values without the oracle, so Q03 holds — but the phrase "agree with it on every shared field" should not be read as independent corroboration for the container fields.
- **R2 — entry line 68 (item 6) and item 8's output keys.** `flags & 0x100` (readout.py:166) and `data_type_string`/`data_type_int_dec` (readout.py:215) assert spec semantics that the entry never cites: the spec fixes them at snapshot `:480` (`UTF8_FLAG = 1<<8`), `:477` (`SORTED_FLAG = 1<<0`), `:307` (`TYPE_STRING = 0x03`), `:327` (`TYPE_INT_DEC = 0x10`). Q03 passes on substance (specification-fixed), but no in-entry derivation exists — Q11/Q02 exposure.
- **R3 — entry line 59 (item 5), "computed by summing the field widths of S038's own struct definitions … not assumed".** `readout.py:48-57` hardcodes the six width lists; the command prints the authored table, it does not read `ResourceTypes.h`. The six totals are *correct* (verified against the snapshot field lists above), so no wrong value; but the derivation-from-primary-record claim is the Q11 class, and item 11's script derives line numbers only, not widths.
- **R4 — entry lines 1, 57, 148, "chunk-type enum block lines 237-253".** The enum opens at `237:enum {` and closes at `263:};`; `RES_TABLE_*` types occupy 256-262, and 253 is `RES_XML_RESOURCE_MAP_TYPE`, the last *XML* type. The range is the XML section's span, not the block's. Every individual symbol line cited (239/241/245/246/247/248/253) is correct; low severity, no value depends on it — flagged only because transcribed anchor ranges are this round's class.

## Pin-guard behaviour (S046 claim, tested)
Header/recheck claim: "exit 2 on a missing or ambiguous symbol". Observed:
- missing snapshot → `derive_axml_anchors: snapshot missing: /tmp/…/snapshots/ResourceTypes.h`, exit 2;
- mutated pinned snapshot → `… snapshot digest 552b498e… != pinned 56b88bc4…`, exit 2;
- ambiguity (copy with the pin patched to match a snapshot containing a duplicate `RES_XML_TYPE`) → `derive_axml_anchors: enum RES_XML_TYPE: ambiguous (2 hits at [241, 2367])`, exit 2.

So the line numbers are looked up in the pinned bytes, not emitted from a transcribed table. Note for the S046 row's wording: on the *pinned* bytes the digest guard fires before lookup, so the ambiguity path is only reachable after a pin change — the refusal is real but defensive.

## Residual risk
- Q03 is judged textually and numerically; there is no `lsp` device in this seat's tool inventory, so the role's server-answered-file step (references/definition/diagnostics) was **unavailable** for a Markdown evidence entry plus Python instruments. Every numeric value was instead executed and compared with a second instrument; every line anchor was read from the snapshot bytes.
- I did not re-run `generator.py` (the entry does not claim to; it would rewrite `fixture.apk`, outside my write bounds, and S041 pins the bytes).
- I did not fetch the live S038/S045 URLs; the pinned snapshots are the record, and their sha256s match the entry and `SOURCES.md` (S032 row 46, S034 row 48, S038 row 52, S041 row 55, S045 row 59, S046 row 61).
- Tooling directive: **no installs or upgrades** were performed (python3 stdlib + coreutils sufficed); nothing to record beyond that.

## Verdict
**Q03 PASS** on these bytes. No expected value is copied from the record under test, no saved path doubles as identity and locator, and every embedded value reproduces exactly under a second instrument. R1-R4 are precision/citation exposures for Q11/Q02, not Q03 failures.
