# R71W2IndependentRead — independent byte read of `corpus/fixtures/apk-r65/fixture.apk`

**Verdict: PASS (independent read, no vote) — one ZIP, one AXML and one dex fact, plus every disputed item-5 offset, reproduce from the archive bytes alone with no `readout.py` execution and no divergence in any printed value; two bounded, non-numeric gaps remain against the item-5 / item-11 anchoring text (reported below, not repaired).**

Seat: R71W2IndependentRead · wave 2 of round 71 · lane `revenger-shokunin` · candidate commit `4c1eeaee88fd07e442f1bd546faf77be3957d390` (worktree HEAD `c6e284c`, entry bytes at `corpus/knowledge/round-71-apk-axml-byte-evidence.md`). Scope: exactly one fixture, `corpus/fixtures/apk-r65/fixture.apk`. No producer was invoked, no source file was edited, no gate or counter was run, and no `w2-votes` file is written by this seat (only the four named reviewers vote).

## Method and label rule

- **TOOL** = printed by my own script `indep.py`, written from scratch for this seat in scratch (`struct`/`hashlib`/`zlib` only). It does not import, exec, read or shell out to `readout.py` or `entry_checks.py`; the disputed fields were re-decoded by hand as well.
- **MANUAL** = `od -t x1` bytes read by me against APPNOTE 4.3.7/4.3.12/4.3.16 field offsets and S038 `ResourceTypes.h` struct field order, both transcribed by hand.
- Known-intent disclosure: writing an independent parser is still *tool* evidence. The MANUAL hexdump window below is what makes the disputed offsets independent of any of my own arithmetic.

## Commands

```
$ cd /fast/scratch/hyaku/revenger-r71/R71W2IndependentRead
$ cp <lane>/corpus/fixtures/apk-r65/fixture.apk ./f.apk && sha256sum f.apk
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  f.apk        # 947 bytes
$ python3 -B indep.py f.apk > indep.json ; echo EXIT=$?
EXIT=0
$ od -A d -t x1 -j 321 -N 48 f.apk        # AXML start-element chunk (payload+272, payload at file 49)
$ od -A d -t x1 -j 925 -N 22 f.apk        # EOCD
$ od -A d -t x1 -j 506 -N 32 f.apk        # dex declared header
$ od -A d -t u1 -j 506 -N 8 f.apk
0000506 100 101 120  10  48  51  53   0
```

## 1. ZIP fact — EOCD, central directory and payload arithmetic (TOOL + MANUAL)

```
0000925 50 4b 05 06 00 00 00 00 03 00 03 00 bc 00 00 00
0000941 e1 02 00 00 00 00
```
- `PK\x05\x06` at file 925; record is 22 bytes → ends at 947 = file size. Entries-on-disk 3, entries-total 3, `cd_size` 0xbc = **188**, `cd_offset` 0x2e1 = **737**, comment length 0.
- Identity holds from bytes: 737 + 188 = **925** = EOCD offset. My central walk (three records of `46 + name_len + extra_len + comment_len`) also ends at exactly 925, so the directory is consumed with no slack.
- Per member (TOOL): `AndroidManifest.xml` local header 0 → payload 49 (= 0+30+19+0), CRC 962d075f recomputed 962d075f; `classes.dex` 465 → 506 (= 465+30+11+0), CRC 2635c82a/2635c82a; `META-INF/MANIFEST.MF` 618 → 668 (= 618+30+20+0), CRC e948d738/e948d738. All three: method 0 (stored), local and central flags 0x0000, compressed == uncompressed size.

## 2. AXML fact — chunk walk and string pool (TOOL)

- Root: type 0x0003, headerSize 8, size 416 = member size; payload is 416 bytes at file 49.
- Walk by `offset += size` from the root `headerSize` visits 8 → 204 → 248 → 272 → 368 → 392 and ends at **416**, equal to the member size (no trailing bytes).
- Six chunks: (8, 0x0001, h16→28, 196), (204, 0x0180, 8, 44), (248, 0x0100, 16, 24), (272, 0x0102, 16, 96), (368, 0x0103, 16, 24), (392, 0x0101, 16, 24).
- String pool at 8: stringCount 9, styleCount 0, flags 0x00000100, stringsStart 64, offsets `[0,10,55,66,76,94,108,122,126]`; my own UTF-8 decode of each entry (u16 length byte + u8 byte length + slice) returns the nine declared strings with `u16len == len(decoded)` for **all nine**, so the pool's declared lengths and offsets are self-consistent.
- Resource map at 204: size−headerSize = 36 = 9×4; entries 5 and 6 are `0x0101021b` / `0x0101021c`, the other seven zero.

## 3. dex fact — declared header recomputation (TOOL + MANUAL)

```
0000506 64 65 78 0a 30 33 35 00 30 0c 12 3d a5 fc 7b ea
0000522 8f a9 ff aa 52 24 35 40 c8 02 60 66 51 1b 9f ce
```
- Magic `dex\n035\0`; declared checksum little-endian `0x3d120c30` **equals** `zlib.adler32(dex[12:])`; declared 20-byte signature **equals** `sha1(dex[32:])` = `a5fc7bea8fa9ffaa52243540c8026066511b9fce`; `header_size` 112 = `file_size` 112 = member size 112; `endian_tag` 0x12345678.
- Scope reminder matching the entry's limitation: this is internal consistency of a 112-byte header-only member, not dex program validity.

## 4. Disputed item-5 offsets, from source bytes

Entry item 5 sentence under test: “It does not compare every readout offset: `readout.py:189` (`lineNumber`) and `:197` (`styleIndex`) are locators-only, not comparisons.”

MANUAL window (file offsets; start-element chunk at 272 in payload, payload at 49 → chunk at file 321):

```
0000321 02 01 10 00 60 00 00 00 01 00 00 00 ff ff ff ff
0000337 ff ff ff ff 02 00 00 00 14 00 14 00 03 00 00 00
0000353 00 00 00 00 ff ff ff ff 03 00 00 00 04 00 00 00
```

| field | byte position (file) | bytes | value | readout literal | status |
|---|---|---|---|---|---|
| chunk type | 321–322 | `02 01` | 0x0102 | — | MANUAL |
| chunk headerSize | 323–324 | `10 00` | 16 | `base + 16` (line 203) | sum matches |
| chunk size | 325–328 | `60 00 00 00` | 96 | — | MANUAL |
| `ResXMLTree_node.lineNumber` | 329–332 = base+8 | `01 00 00 00` | 1 | `u32(axml, base + 8)` @189 | **disputed — verified true** |
| `ResXMLTree_node.comment` | 333–336 = base+12 | `ff ff ff ff` | 0xFFFFFFFF | never read | not claimed |
| `ResXMLTree_attrExt.ns` | 337–340 = base+16 | `ff ff ff ff` | NO_INDEX | @190 | compared by item 17 |
| `ResXMLTree_attrExt.name` | 341–344 = base+20 | `02 00 00 00` | 2 | @191 | compared by item 17 |
| `.attributeStart` | 345–346 = base+24 | `14 00` | **20** | @192 | compared by item 17 |
| `.attributeSize` | 347–348 = base+26 | `14 00` | **20** | @193 | compared by item 17 |
| `.attributeCount` | 349–350 = base+28 | `03 00` | 3 | @194 | compared by item 17 |
| `.idIndex` | 351–352 = base+30 | `00 00` | 0 | @195 | compared by item 17 |
| `.classIndex` | 353–354 = base+32 | `00 00` | 0 | @196 | compared by item 17 |
| `.styleIndex` | 355–356 = base+34 | `00 00` | 0 | `u16(axml, base + 34)` @197 | **disputed — verified true** |
| attr[0].ns / .name / .rawValue | 357–368 = base+36 | `ff ff ff ff` / `03 00 00 00` / `04 00 00 00` | NO_INDEX / 3 / 4 | @204–209 | compared by item 17 |

Findings on the disputed pair:

1. Both cited line numbers are exact: `readout.py:189` is `line = u32(axml, base + 8)`; `:197` is `style_index = u16(axml, base + 34)`. The cited lines name the true field positions, not neighbours.
2. Both field positions are correct against S038's field order: node = header(8) + lineNumber(4) + comment(4) = 16, so `lineNumber` at +8; attrExt = ns(4)+name(4)+6×u16 = 20, so `styleIndex` (8th field) at attrExt+18 = node+34 — the last two bytes before the attribute array, which starts at node+16+attributeStart = base+36 = file 357 (confirmed by bytes).
3. Item 5's supported sums also hold from bytes: node width **16** = the chunk's declared `headerSize` 16 = literal 16 in `readout.py:203`; `attr_ext_attribute_start` **20** and `attribute_size` **20** equal the values the start-element chunk states (bytes above).
4. The omission is real and is a print-list choice, not a missing literal: `readout.py` does contain `u32(axml, base + 8)` and `u16(axml, base + 34)`, while `entry_checks.py:210-216` keeps `styleIndex` in the `EXT` name list but drops it from the printed u16 field list, and `entry_checks.py:231` prints only the node's total width, never its field offsets. So item 17 neither can nor does compare them, exactly as item 5 states.
5. Both values are nonetheless **displayed**: the embedded `axml_start_element` block prints `"lineNumber": 1` and `"styleIndex": 0`, which my bytes reproduce.

## 5. Cross-check of the entry's own embedded outputs against my bytes

I rebuilt each fact object from `indep.json` and compared it to the JSON lines embedded in the entry (I parsed the entry file; I did not run any lane script):

```
embedded facts parsed: ['archive','axml_chunk_table','axml_end_element','axml_end_namespace',
 'axml_resource_map','axml_start_element','axml_start_namespace','axml_string_pool',
 'dex_declared_header','eocd','jar_manifest','member[AndroidManifest.xml]',
 'member[META-INF/MANIFEST.MF]','member[classes.dex]','spec_derived_struct_widths']

MATCH archive(bytes,sha256)                    MATCH axml_string_pool(9 strings, offsets, flags)
MATCH eocd(offsets,counts,identity)            MATCH axml_resource_map
MATCH member[AndroidManifest.xml]              MATCH axml_start_namespace
MATCH member[classes.dex]                      MATCH axml_end_namespace
MATCH member[META-INF/MANIFEST.MF]             MATCH dex_declared_header
MATCH axml_chunk_table                         MATCH jar_manifest
MATCH start_element.{offset,lineNumber,element_ns_index,element_name_index,element_name,
      attributeStart,attributeSize,attributeCount,idIndex,classIndex,styleIndex}   (11/11)
MATCH attr[0..2].{ns,ns_index,name,name_index,raw_value,raw_value_index,value_size,data_type,res_id} (27/27)
```
`axml_end_element` (368; lineNumber 1; ns_index 4294967295; name_index 2) was checked directly from bytes after my comparison scaffold left it unset. No mismatched printed value in 15 fact objects, 11 start-element scalars and 27 attribute fields.

Oracle separation (TOOL, my bytes vs the authored `truth.json`, not vs the readout): image 947 / `05d2280f…` match; all three members' `local_header_offset`, `compressed_size`, `uncompressed_size`, `crc32`, `sha256` and `method` match; `axml_declared.strings` and `resource_ids` match element-for-element; the three attribute tuples (`name_idx`, `ns_idx`, `raw_value_idx`, `data_type`, `data`) match. So the oracle half of item 13 is not merely an echo of the readout — an independent reader arrives at the same values.

## Divergences (bounded; no source edit, no verdict on any Q)

**D1 — item 5's enumeration is complete for item 17's covered structs but not for the readout as a whole.** I classified every `u32(axml,…)` / `u16(axml,…)` / `axml[…]` token in `readout.py` lines 120–250 against the embedded item-17 block: 25 are compared, 189 and 197 are the named locators-only pair (both verified above), and these are neither compared nor named: `129/130/132/134-136/142` (chunk-header type/headerSize/size reads), `155` (pool offset array), `159-161` (UTF-8 length bytes and string slice), `172` (resource-map entry array), `180-182` (namespace chunk prefix/uri/lineNumber), `227-230` (end-element lineNumber/ns/name). Mitigations that keep this from being a false printed value: `180-182` and `227-230` reuse the same numeric offsets 8/16/20 that are named at 189 or compared at 190/191; `155`/`159-161`/`172` are derived-offset reads that items 6 and 7 describe in prose (item 7 explicitly says the resource-map array's source line is not printed among item 11's lines); `129-136/142` are the walk described by item 4. Observation's bounded-credit sentence (“the literal subsets compared are only those printed by items 12 and 17”) is strictly true. Residual risk is reading-level: the colon-list can be taken as exhaustive of “every readout offset”, which it is not.

**D2 — the namespace and end-element ext structs are used but never located by item 11.** `readout.py:180-181` and `:228-229` read prefix/uri (namespace) and ns/name (end element) at node+16 and node+20, i.e. through S038 `ResXMLTree_namespaceExt` (`corpus/snapshots/ResourceTypes.h:649`, fields `prefix`, `uri`) and `ResXMLTree_endElementExt` (`:662`, fields `ns`, `name`). Neither struct is in `derive_axml_anchors.py`'s STRUCTS list (`:43-49`: ResChunk_header, Res_value, ResStringPool_header, ResXMLTree_header, ResXMLTree_node, ResXMLTree_attrExt, ResXMLTree_attribute), so item 11 prints no line for them and the entry's item-8 labels `"prefix": "android"`, `"uri": "http://schemas.android.com/apk/res/android"` rest on unlocated snapshot text. The values themselves are true from bytes (at 248: node+16 = 0 → pool string 0 `android`, node+20 = 1 → the URI; at 368: +16 = 0xFFFFFFFF, +20 = 2 → `manifest`), and the numerics 16/20 are compared by item 17 as `ResXMLTree_attrExt.ns`/`.name`. `[INFERENCE]` severity: structural-anchor gap of the same family as the repaired item-5 defect, not a wrong number.

## Confidence

- ZIP fact, AXML chunk/pool fact, dex header fact: **high** — reproduced by an independent implementation and by hand-decoded bytes; all three internal-consistency identities (737+188=925, walk end 416=member size, adler32/sha1 recomputation) hold exactly.
- Disputed item-5 pair (189 `lineNumber`, 197 `styleIndex`): **high** — line citations exact, field positions reproduced from an `od` window, presence/absence in item 17 confirmed statically in `entry_checks.py`.
- No divergence in any value printed by the entry for this fixture: **high** for the 15 fact objects and the attribute fields checked; **medium-high** for the rest of the readout's stdout (not every emitted key was re-derived, only the ones my fact objects cover).
- D1/D2: **high** on what is compared versus what is named (static, mechanical); **inference** on whether the item-5 sentence was intended exhaustively.

## Scope/housekeeping

No tool was installed, no pacman transaction, no route/config change, no `w2-votes` write, no git/jj mutation, no fleet-root tracked file touched, no producer or gate run. Scratch `/fast/scratch/hyaku/revenger-r71/R71W2IndependentRead/` held `f.apk`, `indep.py`, `indep.json`; the receipts reproduced above are quoted in this report and the directory was removed before return.
