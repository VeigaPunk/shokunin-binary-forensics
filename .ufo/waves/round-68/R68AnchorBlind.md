CONCUR — blind derivation from the pinned snapshot reproduces every line number the C05 v3 candidate states: 7 struct declarations, 7 enum constants, the `attributeStart` comment and field, and the `:244`→`:245` repair. No cited number diverges. One non-falsifying range label is loose (`enum block lines 237-253`; the enum itself closes at 263) and is itemised below.

# Blind anchor derivation — C05 v3 candidate (round 68)

Seat: `L1Revenger68.R68AnchorBlind`. Blind protocol honoured: the pinned snapshot was opened, searched and read first; `corpus/knowledge/round-68-apk-axml-byte-evidence.md` was not opened until the derivation table below was complete (it was then read whole and its header extracted for the comparison). No file was edited.

## 1. Snapshot identity (verified before any derivation)

```
$ sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .../round-65/source-snapshots/ResourceTypes.h
$ stat -c '%s bytes' .../round-65/source-snapshots/ResourceTypes.h
86255 bytes
```

Matches the brief's pin (`56b88bc4…c56f`, 86255 bytes). The corpus copy is byte-identical:

```
$ sha256sum corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
```

86255 bytes = 2366 lines; every number below is a line number in **this** file.

## 2. Derivation method (my own search, before comparison)

Two independent passes, both on the pinned bytes:

1. `grep -n` over the whole file for the seven struct names, the seven enum constant names and the `attributeStart` comment/field text, then
2. `awk 'NR>=234 && NR<=264 {printf "%d\t%s\n", NR, $0}'` to number the enum block line by line (the read tool's raw-range footer disagreed with itself by a line, so the numbering proof is the `awk` output, not the view).

Declaration uniqueness was proved rather than assumed — each struct name is the whole line exactly once:

```
$ for s in ResChunk_header Res_value ResStringPool_header ResXMLTree_header ResXMLTree_node ResXMLTree_attrExt ResXMLTree_attribute; do printf '%-24s exact-lines=%s\n' "$s" "$(grep -cx "struct $s" ResourceTypes.h)"; done
ResChunk_header          exact-lines=1
Res_value                exact-lines=1
ResStringPool_header     exact-lines=1
ResXMLTree_header        exact-lines=1
ResXMLTree_node          exact-lines=1
ResXMLTree_attrExt       exact-lines=1
ResXMLTree_attribute     exact-lines=1
```

(The non-declaration `grep` hits at 463, 614, 623, 680, 684, 710, 713, 716, 719, 897, 910, … are member uses of the form `struct X header;` / `struct X ns;`, never declarations.)

## 3. My derivation table (independent, expected-answer-free)

| symbol | derived line | exact snapshot text at that line |
|---|---|---|
| `struct ResChunk_header` | **218** | `struct ResChunk_header` |
| `struct Res_value` | **287** | `struct Res_value` |
| `struct ResStringPool_header` | **461** | `struct ResStringPool_header` |
| `struct ResXMLTree_header` | **612** | `struct ResXMLTree_header` |
| `struct ResXMLTree_node` | **621** | `struct ResXMLTree_node` |
| `struct ResXMLTree_attrExt` | **677** | `struct ResXMLTree_attrExt` |
| `struct ResXMLTree_attribute` | **707** | `struct ResXMLTree_attribute` |
| `RES_STRING_POOL_TYPE` | **239** | `    RES_STRING_POOL_TYPE              = 0x0001,` |
| `RES_XML_TYPE` | **241** | `    RES_XML_TYPE                      = 0x0003,` |
| `RES_XML_START_NAMESPACE_TYPE` | **245** | `    RES_XML_START_NAMESPACE_TYPE      = 0x0100,` |
| `RES_XML_END_NAMESPACE_TYPE` | **246** | `    RES_XML_END_NAMESPACE_TYPE        = 0x0101,` |
| `RES_XML_START_ELEMENT_TYPE` | **247** | `    RES_XML_START_ELEMENT_TYPE        = 0x0102,` |
| `RES_XML_END_ELEMENT_TYPE` | **248** | `    RES_XML_END_ELEMENT_TYPE          = 0x0103,` |
| `RES_XML_RESOURCE_MAP_TYPE` | **253** | `    RES_XML_RESOURCE_MAP_TYPE         = 0x0180,` |
| comment "Byte offset from the start of this structure where the attributes start" | **686** | `    // Byte offset from the start of this structure where the attributes start.` |
| field `uint16_t attributeStart;` | **687** | `    uint16_t attributeStart;` |

Enum-block extents, from the numbered pass:

```
237	enum {
238	    RES_NULL_TYPE                     = 0x0000,
239	    RES_STRING_POOL_TYPE              = 0x0001,
240	    RES_TABLE_TYPE                    = 0x0002,
241	    RES_XML_TYPE                      = 0x0003,
242	
243	    // Chunk types in RES_XML_TYPE
244	    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245	    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
246	    RES_XML_END_NAMESPACE_TYPE        = 0x0101,
247	    RES_XML_START_ELEMENT_TYPE        = 0x0102,
248	    RES_XML_END_ELEMENT_TYPE          = 0x0103,
249	    RES_XML_CDATA_TYPE                = 0x0104,
250	    RES_XML_LAST_CHUNK_TYPE           = 0x017f,
251	    // This contains a uint32_t array mapping strings in the string
252	    // pool back to resource identifiers.  It is optional.
253	    RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
...
262	    RES_TABLE_STAGED_ALIAS_TYPE       = 0x0206,
263	};
```

Derived facts about the block: it **opens at 237** (`enum {`), the XML chunk-type constants occupy **238-253**, the `RES_TABLE_*` constants occupy 256-262, and it **closes at 263**. **Line 244 is `RES_XML_FIRST_CHUNK_TYPE = 0x0100`** — the symbol the round-65/round-67 drafts had put at `:244` is genuinely at 245.

Independent width check of the constants the entry leans on (sums from the field declarations, not from the entry): `ResChunk_header` = 2+2+4 = **8**; `ResStringPool_header` = 8 + 5×4 = **28** (fields at 467/471/482/485/488); `ResXMLTree_node` = 8 + `lineNumber` 4 (627) + `comment` 4 (`ResStringPool_ref{uint32_t index;}` 430-436) = **16**; `ResXMLTree_attrExt` = 4+4+6×2 = **20** (680, 684, 687, 690, 695, 698, 701, 704); `ResXMLTree_attribute` = 4+4+4 + `Res_value` = 20; `Res_value` = `uint16_t size` (288) + `uint8_t res0` (292) + `uint8_t dataType` (351) + `uint32_t data` (409) = **8**.

## 4. Comparison with the candidate's stated numbers

Candidate statements and my derivation (candidate line pointers are into `corpus/knowledge/round-68-apk-axml-byte-evidence.md`):

| anchor | candidate says | where stated | my derivation | verdict |
|---|---|---|---|---|
| `struct ResChunk_header` | 218 | :1 | 218 | MATCH |
| `struct Res_value` | 287 | :1 | 287 | MATCH |
| `struct ResStringPool_header` | 461 | :1 | 461 | MATCH |
| `struct ResXMLTree_header` | 612 | :1 | 612 | MATCH |
| `struct ResXMLTree_node` | 621 | :1 | 621 | MATCH |
| `struct ResXMLTree_attrExt` | 677 | :1, :82 | 677 | MATCH |
| `struct ResXMLTree_attribute` | 707 | :1 | 707 | MATCH |
| `RES_STRING_POOL_TYPE` | :239 | :1, :57 | 239 | MATCH |
| `RES_XML_TYPE` | :241 | :1 | 241 | MATCH |
| `RES_XML_START_NAMESPACE_TYPE` | **:245** | :1, :57, :148 | 245 | MATCH (the r65/r67 `:244` defect is correctly repaired) |
| `RES_XML_END_NAMESPACE_TYPE` | :246 | :1, :57 | 246 | MATCH |
| `RES_XML_START_ELEMENT_TYPE` | :247 | :1, :57 | 247 | MATCH |
| `RES_XML_END_ELEMENT_TYPE` | :248 | :1, :57 | 248 | MATCH |
| `RES_XML_RESOURCE_MAP_TYPE` | :253 | :1, :57 | 253 | MATCH |
| `attributeStart` comment | 686 | :1, :82 | 686 | MATCH |
| `uint16_t attributeStart;` field | 687 | :1, :82 | 687 | MATCH |
| "line 244 is `RES_XML_FIRST_CHUNK_TYPE`" | 244 | :148 | 244 is `RES_XML_FIRST_CHUNK_TYPE = 0x0100,` | MATCH |
| enum block range | **lines 237-253** | :1, :148 | `enum {` at 237; XML constants 238-253; `};` at 263 | **LOOSE LABEL — see §5** |
| chunk-type witness values | 0x0001/0x0180/0x0100/0x0102/0x0103/0x0101 | :57 | same, at 239/253/245/247/248/246 | MATCH |
| derived widths (item 5 payload) | 8 / 28 / 16 / 20 / 20 / 8; `attributeStart`=20, `attributeSize`=20 | :63 | same by field sum | MATCH |
| snapshot digest printed by item 11 | `56b88bc4…c56f ResourceTypes.h` | :129 | same | MATCH |

Machine-derivation mechanism (item 11) checked separately, since the entry's claim is that no anchor is transcribed:

```
$ sha256sum corpus/derive_axml_anchors.py
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors.py
$ python3 -B corpus/derive_axml_anchors.py; echo EXIT=$?
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
EXIT=0
$ python3 -B corpus/derive_axml_anchors.py | grep -c ''
17
```

17 lines, exit 0 — the count and digest match the S046 row and the item-11 embedding. Matcher strictness (read at `corpus/derive_axml_anchors.py:35-98`): structs match `l.strip() == f"struct {name}"`, enums match `l.strip().startswith(name + " ")`, the field matches `l.strip() == "uint16_t attributeStart;"`, and `find_unique` exits 2 on zero hits or more than one (`derive_axml_anchors.py:70-77`). So the printed numbers are located by search, and the script cannot print a line it did not find — the entry's item-11 claim is true of the code, not just of the output.

## 5. The one imprecision (range label, not a number)

The entry says twice that "the chunk-type enum block **spans lines 237-253**" (`…evidence.md:1`, `:148`). On the snapshot, 237 is `enum {` and 253 is `RES_XML_RESOURCE_MAP_TYPE`; the enclosing enum continues through the `RES_TABLE_*` constants (256-262) and closes at `};` on **263**. So the label names *enum opening + last XML chunk-type constant*, not the full block extent.

This is a labeling nuance, not a wrong anchor: every constant the entry cites lies in 238-253, every cited line is correct, and the entry never claims no more constants follow. A stricter phrasing would be "the chunk-type section of the enum, lines 237-253 (the enum itself closes at 263)". No number in the entry is falsified by it, so the verdict stays CONCUR.

Also checked and correct: the entry's parenthetical "(0x0180 — inside the enum block, unlike the round-65 draft's :239-250)" (`:1`) — `RES_XML_RESOURCE_MAP_TYPE` is at 253, inside 237-263, and 253 > 250, so the contrast with the old range holds.

## 6. Out-of-axis reads recorded for completeness (cheap, read-only)

- `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 stdout lines, `sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — identical to the entry's `recheck:`/§Reproduce claim (`:7`, `:194`). No stderr.
- `corpus/README.md:34` still has the C05 row ending in `uncovered` (the row carries the retained rejected round-65 candidate), consistent with `admission-status: candidate` at `…evidence.md:9`. The entry did not flip the row.

## 7. Confidence and remaining unknowns

- **Confidence: high** for all 16 anchors and the two enum-range facts — direct `grep -n`/`awk` over the hash-pinned bytes, declaration uniqueness proved, and (post-derivation) the committed script reproduces the same table.
- **Unknown / out of scope:** the snapshot's identity against the live AOSP tag `android-15.0.0_r1` was not fetched (no network used); the snapshot is the lane's pinned artifact of record, and the entry's S038 row cites that tag. Upstream line drift, if any, is outside this seat's question.
- **Not re-derived here:** the readout's byte values (items 1-10 of the entry) and its 15-line digest — verified only as an aggregate hash reproduction (§6); the per-fact comparison belongs to the fixture/Q11 seats.

## Tooling

No installs or upgrades were made or needed. Tools used: coreutils `sha256sum`/`stat`/`grep`/`awk`/`sed`, `python3` (stdlib only, `-B`).
