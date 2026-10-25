HOLDS — every AOSP line number and enum value the C05 v4 entry states (19 unique anchors across the `source:` header, items 4/8/11) is reproduced exactly by `corpus/derive_axml_anchors.py`: 38/38 mentions MATCH, 0 MISMATCH; exit 0, 20 stdout lines, byte-identical across runs.

# R69AnchorDerive — mechanical re-derivation of the AXML spec anchors

Seat: L1Revenger69.R69AnchorDerive (build item, round 69). Read-only re-derivation; nothing edited.

## Environment / inputs

| object | observed |
|---|---|
| `corpus/derive_axml_anchors.py` | sha256 `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa`, 4979 bytes, mode 0755 |
| `corpus/snapshots/ResourceTypes.h` | sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 bytes |
| `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` | same sha256 `56b88bc4…57c56f` (copy is byte-identical) |
| entry under check | `corpus/knowledge/round-69-apk-axml-byte-evidence.md` (215 lines, committed at `da02261`) |

The pre-registered script digest in the prompt and in the entry's S047 `source:` line (`entry:6`) equals the file on disk: **MATCH**.
Cross-check of the registry row: `corpus/SOURCES.md:61` (S047) states the same script sha256 and "20 output lines" — both reproduced below.

## Command, exit code, stdout digest

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/derive_axml_anchors.py
```

| run | cwd | exit | lines | stdout sha256 |
|---|---|---|---|---|
| run1 | lane root | **0** | **20** | `f90e342deb01ad384ed020702a7c543e755c107c15d8ace056294a0ef5fa3230` |
| run2 | lane root | **0** | **20** | `f90e342deb01ad384ed020702a7c543e755c107c15d8ace056294a0ef5fa3230` |
| run3 | `/` | **0** | **20** | `f90e342deb01ad384ed020702a7c543e755c107c15d8ace056294a0ef5fa3230` |

- `cmp run1.out run2.out` → silent, exit 0 → **byte-identical across two runs** (`BYTE_IDENTICAL=yes`; same for run3).
- stderr empty in all runs.
- No stdout digest is pinned anywhere in the lane for this command (S046/S047 pin the *script* digest + line count; grep for `f90e342d` and `derive_axml_anchors` across `*.md/*.py/*.json/*.log` finds no stdout digest). The digest above is therefore the **newly observed** value, not a comparison against a pre-registered one — stated explicitly so it is not read as a match against an existing pin.

Exact stdout (20 lines, runs 1–3 identical):

```
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
```

Line-count decomposition: 1 digest + 7 struct + 2 enum-bound + 8 enum + 2 attributeStart = **20**, matching the entry's item-11 statement (`entry:127`) and `reports/round-69/claims.md:64-66` ("19 cited-symbol/bound lines + the sha256 line = 20 lines"). Distinct anchors printed = 19 = 7 structs + 2 bounds + 8 enums + 2 attributeStart lines.

## Per-anchor check — entry stated vs derived

Stated values were read from the entry's `source:` header (line 1) and items 4/8/11 (`entry:52`, `entry:59`, `entry:84`, `entry:127`, `entry:153`); derived values from the stdout above. Enum values are additionally confirmed against the snapshot bytes (see next section).

| # | anchor | entry location(s) | entry states | derived | verdict |
|---|---|---|---|---|---|
| 1 | `struct ResChunk_header` | header | 218 | 218 | **MATCH** |
| 2 | enum block open `enum {` | header, item4, item11 | 237 | 237 | **MATCH** |
| 3 | enum block close `};` | header, item4, item11 | 263 | 263 | **MATCH** |
| 4 | `RES_STRING_POOL_TYPE` | header, item4 | 239 | 239 | **MATCH** |
| 5 | `RES_XML_TYPE` | header, item4 | 241 | 241 | **MATCH** |
| 6 | `RES_XML_FIRST_CHUNK_TYPE` | header, item4, item11 | 244 (0x0100) | 244 = 0x0100 | **MATCH** |
| 7 | `RES_XML_START_NAMESPACE_TYPE` | header, item4, item11 | 245 (0x0100) | 245 = 0x0100 | **MATCH** |
| 8 | `RES_XML_END_NAMESPACE_TYPE` | header, item4 | 246 | 246 = 0x0101 | **MATCH** |
| 9 | `RES_XML_START_ELEMENT_TYPE` | header, item4 | 247 | 247 = 0x0102 | **MATCH** |
| 10 | `RES_XML_END_ELEMENT_TYPE` | header, item4 | 248 | 248 = 0x0103 | **MATCH** |
| 11 | `RES_XML_RESOURCE_MAP_TYPE` | header, item4 | 253 (0x0180) | 253 = 0x0180 | **MATCH** |
| 12 | `struct ResStringPool_header` | header | 461 | 461 | **MATCH** |
| 13 | `struct ResXMLTree_header` | header | 612 | 612 | **MATCH** |
| 14 | `struct ResXMLTree_node` | header | 621 | 621 | **MATCH** |
| 15 | `struct ResXMLTree_attrExt` | header, item8 | 677 | 677 | **MATCH** |
| 16 | `attributeStart` comment | header, item8 | 686 | 686 | **MATCH** |
| 17 | `uint16_t attributeStart;` field | header, item8 | 687 | 687 | **MATCH** |
| 18 | `struct ResXMLTree_attribute` | header | 707 | 707 | **MATCH** |
| 19 | `struct Res_value` | header | 287 | 287 | **MATCH** |

38 anchor mentions counted across those five locations → 38 MATCH, 0 MISMATCH, 19 unique anchors.

Enum values stated in item 4's prose (`entry:59`: "`0x0001` string pool, `0x0180` resource map, `0x0100` start namespace, `0x0102` start element, `0x0103` end element, `0x0101` end namespace") and item 4's `RES_XML_TYPE` = `0x0003` (`entry:52`) all agree with the derived `=` values. Item 8's `attributeStart` comment quote ("Byte offset from the start of this structure where the attributes start.", snapshot line 686) and field declaration (`uint16_t attributeStart;`, line 687) are the lines the script prints.

## Independent confirmation against the snapshot bytes (script not trusted alone)

`awk` over `corpus/snapshots/ResourceTypes.h` at exactly those line numbers:

```
218|struct ResChunk_header
237|enum {
238|    RES_NULL_TYPE                     = 0x0000,
239|    RES_STRING_POOL_TYPE              = 0x0001,
240|    RES_TABLE_TYPE                    = 0x0002,
241|    RES_XML_TYPE                      = 0x0003,
243|    // Chunk types in RES_XML_TYPE
244|    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245|    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
246|    RES_XML_END_NAMESPACE_TYPE        = 0x0101,
247|    RES_XML_START_ELEMENT_TYPE        = 0x0102,
248|    RES_XML_END_ELEMENT_TYPE          = 0x0103,
249|    RES_XML_CDATA_TYPE                = 0x0104,
253|    RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
262|    RES_TABLE_STAGED_ALIAS_TYPE       = 0x0206,
263|};
287|struct Res_value
461|struct ResStringPool_header
612|struct ResXMLTree_header
621|struct ResXMLTree_node
677|struct ResXMLTree_attrExt
686|    // Byte offset from the start of this structure where the attributes start.
687|    uint16_t attributeStart;
707|struct ResXMLTree_attribute
```

Every script-printed line number and enum value is literally at that line. The block really does open at 237 and close at 263 (the v3 candidate's "237-253" range is correctly repaired); `RES_XML_START_NAMESPACE_TYPE` is at 245 and 244 is `RES_XML_FIRST_CHUNK_TYPE` (the M40/M44 off-by-one is correctly repaired).

## Entry coverage completeness (no un-derived S038 anchor)

Sweep of every `line N` / `:N` token in the entry, excluding the 19 anchors: the only residual numeric references are non-S038 or self-references — `entry:2` "line 5" (S043's *wrong* citation, quoted as the defect), `entry:8`/`entry:48` `entry:41` (self-reference to the round-65 draft), `readout.py:22`, `readout.py:51-58`, `readout.py:99-105`, `readout.py:166`, `readout.py:200-203` (fixture readout script lines, not AOSP), `entry:171` `l0-questions.md:42`, `entry:184` "line 48" (self-reference for the Q14 hex clause). **No un-derived S038 line number remains** → the entry's "every S038 line number and enum value this entry cites" credit is accurate, and is bounded to the 20 printed lines as item 11 states.

## Embedding / gate operability

- The 20-line block embedded in the entry (command `entry:130`, output lines 131-150) is **byte-identical** to the live stdout (extracted and compared line-by-line, `embedded: 20 stdout: 20 identical: True`).
- `corpus/check_embedded_outputs.py:78` re-runs the named command and `:83-85` requires each embedded line to appear verbatim in the re-run stdout (`stdout_set` membership). Since the embedded block equals the actual stdout exactly, the registered gate sees zero drift for this block on the current tree.
- Digest guard is real: appending a byte to a scratch copy of the snapshot (`/tmp/revenger-r69-ad-probe`) yields
  `derive_axml_anchors: snapshot digest 5d131b28…be3d != pinned 56b88bc4…57c56f`, **exit 2**. Pristine scratch copy → exit 0 with output identical to run1. Unmodified script run from cwd `/` → exit 0, identical output (path resolves from `__file__`, cwd-independent).
- The symbol-absent/ambiguous branches (`derive_axml_anchors.py:72-79` `find_unique` → `fail()` → `sys.exit(2)`) were code-read, not executed: they are unreachable while the pinned snapshot digest matches, because any snapshot edit trips the digest guard first. Every symbol in the current run resolved to exactly one hit (no `ambiguous` output).

## Findings

1. **HOLDS.** All 19 anchors / 38 mentions reproduce; exit 0; 20 lines; deterministic across two runs and cwd-independent.
2. **No pinned stdout digest exists** for the derivation (S047 pins script digest + line count only). The observed stdout digest `f90e342d…a3230` should be recorded if a later wave wants a byte-level pin; today the line-count pin is satisfied exactly.
3. **Non-findings verified:** snapshot copy is byte-identical to the round-65 snapshot (same sha256), script digest matches the S047 row and the entry's `entry:6` citation, and the embedded block equals live stdout.

## Evidence inventory (all commands run from the lane root unless stated)

| # | command | result |
|---|---|---|
| 1 | `sha256sum corpus/derive_axml_anchors.py` | `74d4c0d9…2a83aa` |
| 2 | `sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h` | `56b88bc4…57c56f` for both; 86255 bytes |
| 3 | `python3 -B corpus/derive_axml_anchors.py` (×2) | exit 0, 20 lines, sha256 `f90e342d…a3230`, `cmp` identical |
| 4 | same from `/` | exit 0, identical stdout |
| 5 | `awk` over snapshot lines 218/237-263/287/461/612/621/677/686/687/707 | each derived number/value literal at that line |
| 6 | scratch copy + 1 appended byte | exit 2, digest-mismatch message |
| 7 | entry-block vs stdout comparison | identical, 20/20 lines |

Scratch: `/tmp/revenger-r69-ad-*` (outputs and probe dir), deleted before return. No tool installs or updates were needed. No writes outside this report and that scratch.
