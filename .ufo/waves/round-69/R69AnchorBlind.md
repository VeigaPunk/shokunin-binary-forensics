# R69AnchorBlind — blind independent anchor derivation vs. `round-69-apk-axml-byte-evidence.md`

**CONCUR** — I derived all 20 anchors, the 8 enum constants, the `attributeStart` comment/field lines, and the header's S038 citations from the pinned snapshot bytes *before* opening the entry, and every number the entry states for items 4, 8, 11 and its header matches my own derivation-exactly; zero diverging numbers, zero diverging lines.

Seat: blind anchor derivation only. No edits made. No package installed or updated (host pacman transactions paused; no tool was needed beyond `grep`/`awk`/`python3` stdlib).
Scratch `/tmp/revenger-r69-anchor/` deleted before return.

---

## 0. Snapshot identity (verified first, before any read of the entry)

```
$ sha256sum .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  …/source-snapshots/ResourceTypes.h
$ wc -l …/source-snapshots/ResourceTypes.h
2366
$ stat -c '%s bytes %n' corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
86255 bytes corpus/snapshots/ResourceTypes.h
86255 bytes .ufo/waves/round-65/source-snapshots/ResourceTypes.h
$ cmp corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h && echo IDENTICAL
IDENTICAL
```

Matches the pinned digest in the prompt, and the two copies are byte-identical (relevant to the C2/Q15 tree-identity criterion: the derivation input is digest-pinned and duplicated with `cmp` identity).

## 1. My blind derivation (produced from the snapshot only, before opening the entry)

Method: `grep -n` for `^struct ` / `^enum {` / `^\s+RES_`, then `awk`-numbered windows 210-270, 596-725, 461-490, 287-300. No access to the entry, no access to `corpus/`.

### 1a. Structs (seven stated by the entry, plus three neighbours I found)

| symbol | my open line | my close line | bytes (from field widths) |
|---|---|---|---|
| `struct ResChunk_header` | **218** | 235 | 8 (2+2+4) |
| `struct Res_value` | **287** | 412 | 8 (2+1+1+4) |
| `struct ResStringPool_header` | **461** | 489 | 28 (8 + 5×4) |
| `struct ResXMLTree_header` | **612** | 615 | 8 |
| `struct ResXMLTree_node` | **621** | 630 | 16 (8+4+4) |
| `struct ResXMLTree_attrExt` | **677** | 705 | 20 (4,4,2,2,2,2,2,2) |
| `struct ResXMLTree_attribute` | **707** | 720 | 20 (4,4,4,2,1,1,4) |
| `struct ResXMLTree_cdataExt` | 636 | 643 | 12 (4+8) — *not cited by the entry* |
| `struct ResXMLTree_namespaceExt` | 649 | 656 | 8 — *not cited* |
| `struct ResXMLTree_endElementExt` | 662 | 670 | 8 — *not cited* |

### 1b. Chunk-type enum block

- open `enum {` : **237**; close `};` : **263** (block 237-263). Verified `^enum {` occurs exactly once in the file (`grep -c '^enum {'` = 1).

Full block as I numbered it (238-262):

| line | constant | value |
|---|---|---|
| 238 | `RES_NULL_TYPE` | 0x0000 |
| **239** | `RES_STRING_POOL_TYPE` | **0x0001** |
| 240 | `RES_TABLE_TYPE` | 0x0002 |
| **241** | `RES_XML_TYPE` | **0x0003** |
| **244** | `RES_XML_FIRST_CHUNK_TYPE` | **0x0100** |
| **245** | `RES_XML_START_NAMESPACE_TYPE` | **0x0100** |
| **246** | `RES_XML_END_NAMESPACE_TYPE` | **0x0101** |
| **247** | `RES_XML_START_ELEMENT_TYPE` | **0x0102** |
| **248** | `RES_XML_END_ELEMENT_TYPE` | **0x0103** |
| 249 | `RES_XML_CDATA_TYPE` | 0x0104 |
| 250 | `RES_XML_LAST_CHUNK_TYPE` | 0x017f |
| **253** | `RES_XML_RESOURCE_MAP_TYPE` | **0x0180** |
| 256-262 | `RES_TABLE_*` (7) | 0x0200-0x0206 |

### 1c. `attributeStart`

- comment line **686**: `    // Byte offset from the start of this structure where the attributes start.`
- field line **687**: `    uint16_t attributeStart;`

Field neighbours I numbered independently: `attributeSize` 690, `attributeCount` 695, `idIndex` 698, `classIndex` 701, `styleIndex` 704.

## 2. Comparison with the entry (opened only after §1)

### 2a. Header anchors (entry line 1)

| entry states | my derivation | match |
|---|---|---|
| `struct ResChunk_header` (line 218) | 218 | yes |
| enum block lines **237-263** (`enum {` :237, `};` :263) | 237 / 263 | yes |
| `RES_STRING_POOL_TYPE` :239 | 239, 0x0001 | yes |
| `RES_XML_TYPE` :241 | 241, 0x0003 | yes |
| `RES_XML_FIRST_CHUNK_TYPE` :244 (0x0100) | 244, 0x0100 | yes |
| `RES_XML_START_NAMESPACE_TYPE` **:245** (0x0100) | 245, 0x0100 | yes |
| `RES_XML_END_NAMESPACE_TYPE` :246 | 246, 0x0101 | yes |
| `RES_XML_START_ELEMENT_TYPE` :247 | 247, 0x0102 | yes |
| `RES_XML_END_ELEMENT_TYPE` :248 | 248, 0x0103 | yes |
| `RES_XML_RESOURCE_MAP_TYPE` :253 (0x0180) | 253, 0x0180 | yes |
| `struct ResStringPool_header` (line 461) | 461 | yes |
| `ResXMLTree_header`/`ResXMLTree_node` (lines 612, 621) | 612, 621 | yes |
| `struct ResXMLTree_attrExt` (line 677) | 677 | yes |
| attrStart comment "Byte offset…" at 686; `uint16_t attributeStart;` at 687 | 686; 687 | yes |
| `struct ResXMLTree_attribute` (line 707) | 707 | yes |
| `struct Res_value` (line 287) | 287 | yes |
| snapshot `…/round-65/source-snapshots/ResourceTypes.h` sha256 `56b8…c56f`, **86255 bytes** | sha256 and 86255 bytes both reproduced | yes |

### 2b. Item 11 (the 20-line machine derivation)

Entry's embedded stdout vs. my derivation — **20/20 identical**, including order and formatting:

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

(The above is the output of the committed `python3 -B corpus/derive_axml_anchors.py`, exit 0, 20 lines — run *after* my blind table and equal to it.)

### 2c. Item 4 (AXML chunk stream) — independent parser, not the author's readout

I wrote my own stdlib ZIP+AXML walker (`/tmp/revenger-r69-anchor/indep.py`, deleted) reading `corpus/fixtures/apk-r65/fixture.apk` raw:

```
apk_bytes 947 sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
eocd_offset 925 total_entries_cd 3 cd_size 188 cd_off 737 cd_end_equals_eocd True
cd_walk_end 925
xml_header type 0x3 headerSize 8 size 416 len 416
walk_end 416 equals_total True
chunk off=8   type=0x0001 headerSize=28 size=196
chunk off=204 type=0x0180 headerSize=8  size=44
chunk off=248 type=0x0100 headerSize=16 size=24
chunk off=272 type=0x0102 headerSize=16 size=96
chunk off=368 type=0x0103 headerSize=16 size=24
chunk off=392 type=0x0101 headerSize=16 size=24
```

Entry item 4 states: member begins `0300 0800 a001 0000` (my member bytes: `03000800a0010000…`), type `0x0003`, headerSize 8, total 416, chunks `{28,196,1}@8 {8,44,384}@204 {16,24,256}@248 {16,96,258}@272 {16,24,259}@368 {16,24,257}@392`, walk ends at 416 — **all match**; the decimal types it quotes (1/384/256/258/259/257) are exactly 0x0001/0x0180/0x0100/0x0102/0x0103/0x0101, i.e. the enum lines :239/:253/:245/:247/:248/:246 I derived. Its `headerSize` column (28, 8, 16, 16, 16, 16) equals my struct totals in §1a.

### 2d. Item 8 (start-element attrs) — independent parse

```
start_element chunk_off 272 attrExt_off 288 element_ns_index 4294967295 name_index 2
attributeStart 20 attributeSize 20 attributeCount 3 idIndex 0 classIndex 0 styleIndex 0
attr @ 308
  attr 0 ns 4294967295 name_idx 3 raw_idx 4 value_size 8 type 0x3  data 4
  attr 1 ns 0          name_idx 5 raw_idx 7 value_size 8 type 0x10 data 1
  attr 2 ns 0          name_idx 6 raw_idx 8 value_size 8 type 0x3  data 8
ns_start ext_off 264 prefix_index 0 uri_index 1
ns_end   ext_off 408 prefix_index 0 uri_index 1
elem_end ext_off 384 ns_index 4294967295 name_index 2
node lineNumber (offsets 248/272/368/392): 1, 1, 1, 1
```

Entry item 8 states attrExt at `chunk_base + 16` = 288, `attributeStart` 20, `attributeSize` 20, `attributeCount` 3, element `manifest` (name_index 2) with null ns (`0xffffffff`), attributes at `272+16+20+i*20` = 308…, `package` ns-index `0xffffffff`/type `0x03`, `versionCode` ns 0/type `0x10`, `versionName` ns 0/type `0x03`, namespace chunk at 248 with prefix index 0 and URI index 1, end element at 368, end namespace at 392, **all four node chunks lineNumber 1** — **all match**. Its provenance formula (`chunk_base + 16 + attributeStart + i*attributeSize`) is exactly what my parser did, and the spec comment it quotes ("Appears header.headerSize bytes after a `ResXMLTree_node`") is at snapshot line 675, immediately above `struct ResXMLTree_attrExt` :677 as cited.

Resource map (item 7, cross-check): my parse gives 9 entries, `0x0 ×5, 0x101021b, 0x101021c, 0x0, 0x0` — matches the entry's ids and its `truth.json` correspondence (16843291/16843292 decimal = 0x0101021b/0x0101021c).

### 2e. Completeness of the "every S038 line number this entry states" claim

I extracted every line-number token in the entry (`grep -noE '(line[s]? [0-9]+…|:[0-9]{3}…)'`). S038-attributed tokens are: 218, 237, 239, 241, 244, 245, 246, 247, 248, 253, 263, 287, 461, 612, 621, 677, 686, 687, 707 — a proper subset of the derived 20-line set. The remaining tokens are other sources or self-references: `lines 7`/`line 5` (S043 snapshot), `:166` and `:200` (`readout.py` line refs), `line 48` (the entry's own line 48 in §Q14), `:244` in the §M40/M44 repair sentence (correctly labelled the *superseded* number). **No stale S038 number survives** — in particular the entry uses :245 for `RES_XML_START_NAMESPACE_TYPE` and 237-263 for the block, not the round-65/67 `:244` or the round-68 `237-253`.

## 3. Derivation-instrument depth (why the "machine-derived" credit holds)

- `corpus/derive_axml_anchors.py` sha256 `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa` (matches the entry's S047 anchor).
- It pins the snapshot digest and hard-fails on mismatch: `derive_axml_anchors.py:105-108` (`fail(f"snapshot digest {digest} != pinned {SNAPSHOT_SHA256}")`, exit 2). Reads `snapshots/ResourceTypes.h` relative to its own directory (`:102`), writes nothing.
- Lines are *found*, not asserted: `find_unique` (`:74-80`) fails on 0 or >1 hits; structs match the exact stripped line `struct N` (`:114`), enums match prefix `N + " "` (`:120`) and the value is regex-extracted from the found line (`VALUE_RE`, `:66`, `:122-124`). That anchoring is load-bearing: raw substring counts are ambiguous in this file — `struct ResChunk_header` 12 hits, `struct Res_value` 3, `RES_XML_TYPE` 2 (line 241 plus the comment `// Chunk types in RES_XML_TYPE` at 243), `RES_XML_START_ELEMENT_TYPE` 3 — yet each predicate resolves to exactly one line, which I confirmed by the exit-0 run and by re-deriving the block bounds independently (`enum_block_bounds` picks the `enum {` whose body contains `RES_NULL_TYPE`, `:83-98`).
- The embedded-output gate exists and re-runs commands verbatim: `corpus/check_embedded_outputs.py:80-105` (`drift(... "embedded output line not in recheck stdout")`, `stdout_set = set(stdout.splitlines())`).
- Recheck pins all reproduce: `fixture.apk` `05d228…`; `truth.json` `27303b…`; `generator.py` `eaa944…`; `readout.py` `92e347…`; `readout.py` stdout is **15 lines**, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` (the entry's stated digest).
- `readout.py:48-58` width table (`ResChunk_header [2,2,4]`, `ResStringPool_header [2,2,4,4,4,4,4,4]`, `ResXMLTree_node [2,2,4,4,4]`, `ResXMLTree_attrExt [4,4,2,2,2,2,2,2]`, `ResXMLTree_attribute [4,4,4,2,1,1,4]`, `Res_value [2,1,1,4]`) equals the field lists I read at 218-235/461-489/621-630/677-705/707-720/287-300; attribute offset derivation is at `readout.py:199-203` exactly as the entry quotes (`:200`).

### Notes (not divergences — no number disagrees)

1. **Stale readout comment.** `readout.py:49-50` says "Every fixed offset the readout uses is computed here from the field widths in ResourceTypes.h's own struct definitions, not assumed", while entry item 5 correctly labels those widths *manual transcription*. The entry's label is the conservative and accurate one (the widths are constants in the script, not re-read from the C header at run time); the script's own comment overstates. Cosmetic, affects no cited number.
2. **Value guard narrower than the line guard.** A found enum line whose text lacks `= 0x…,` would print `= ?` and still exit 0 (`:122-124`), whereas a missing/ambiguous *line* exits 2. The entry claims no value-level guard, and the embedded-output gate would catch any drift against the entry's stated values, so the bounded-credit sentence in item 11 stands; this is a robustness observation for the Q15 criterion, not a defect in any stated number.
3. **Header Q14 arithmetic** independently confirmed: `4d616e69666573742d` is 18 hex chars = 9 bytes = ASCII `Manifest-`, and the member's full `first16` is `4d616e69666573742d56657273696f6e`.

## 4. Divergences

**None.** Every one of the 20 derived anchors, the 8 enum values, the enum block bounds, the `attributeStart` comment/field lines, the header's S038 citations, and the item 4 / item 8 byte-level tables reproduce exactly under my independent derivation and independent parser.

Remaining unknowns (outside my assigned question, not investigated): none about the anchors; the fixture's generation recipe, the `inspect_android_package` provider route, and the README admission flip are other seats' scope.

## Commands run (actual)

```
sha256sum .ufo/waves/round-65/source-snapshots/ResourceTypes.h          # 56b8…c56f
wc -l …/ResourceTypes.h                                                # 2366
grep -n -E '^struct |^};|enum \{|^\s+RES_' …/ResourceTypes.h
awk 'NR>=236 && NR<=263' / 'NR>=606 && NR<=721' / 'NR>=461 && NR<=490' / 'NR>=287 && NR<=300'
cmp corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h   # IDENTICAL
grep -c '^enum {' …/ResourceTypes.h                                    # 1
grep -c -- <symbol> …/ResourceTypes.h                                  # ambiguity census
python3 -B corpus/derive_axml_anchors.py                               # exit 0, 20 lines
python3 -B corpus/fixtures/apk-r65/readout.py | sha256sum              # 507d79… , 15 lines
python3 -B /tmp/revenger-r69-anchor/indep.py                           # own ZIP+AXML parse, exit 0
grep -noE '(line[s]? [0-9]+…|:[0-9]{3}…)' corpus/knowledge/round-69-apk-axml-byte-evidence.md
```
