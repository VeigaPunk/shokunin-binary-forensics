PASS — every AOSP `ResourceTypes.h` line number stated in the C05 v3 entry (15 single anchors + 1 range in the `source:` header, 6 in item 4, 3 in item 8, plus the item-11 table and the line-244 remark) is reproduced exactly by `corpus/derive_axml_anchors.py` (exit 0, 17 lines) and independently confirmed by direct line extraction from the pinned snapshot; two consecutive runs are byte-identical. Zero MISMATCH. Two precision notes (enum-range label, item-8 quote punctuation) and one scope note (item 5 states no spec line numbers) below; none changes an anchor.

# R68AnchorDerive — mechanical re-derivation of the C05 v3 AXML spec anchors

Seat: `L1Revenger68.R68AnchorDerive` (leaf, read-only). Lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`. No repository file was written; the only writes were scratch files under `/tmp` (negative-control copies of the script + snapshot). No edits, no git/jj mutations.

Entry under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md`
- 215 lines, sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b` (whole-file digest, for the wave record).
Script: `corpus/derive_axml_anchors.py` sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249` — matches the hash S046 states at entry:4.
Snapshot: `corpus/snapshots/ResourceTypes.h` sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 bytes — matches entry:1, and is byte-identical (verified, `cmp` clean) to the pinned `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`.

## 1. Command, exact stdout, exit code

```sh
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
python3 -B corpus/derive_axml_anchors.py
```

Run 1 exit `0`, run 2 exit `0`; stdout (17 lines, stderr empty, both runs byte-identical):

```
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

Reproducibility receipt:

```
EXIT1=0 EXIT2=0
  17 /tmp/r68ad_run1.out
  17 /tmp/r68ad_run2.out
b02cfe54df5af9e8ca16c61c3d4c719ebb18ac3e9d1cf23b48686628bf3e0831  /tmp/r68ad_run1.out
b02cfe54df5af9e8ca16c61c3d4c719ebb18ac3e9d1cf23b48686628bf3e0831  /tmp/r68ad_run2.out
---BYTE DIFF---
IDENTICAL
```

The entry's embedded item-11 block is **verbatim identical** to this run (`diff` of entry lines 129-145 against `/tmp/r68ad_run1.out` → `VERBATIM_IDENTICAL`), so the block is captured, not transcribed, and would satisfy the registered gate's verbatim comparison.

Independent confirmation (not trusting the script) — direct line extraction from the snapshot at each derived number, via `Path('corpus/snapshots/ResourceTypes.h').read_text().splitlines()`:

```
218: struct ResChunk_header
239:     RES_STRING_POOL_TYPE              = 0x0001,
241:     RES_XML_TYPE                      = 0x0003,
245:     RES_XML_START_NAMESPACE_TYPE      = 0x0100,
246:     RES_XML_END_NAMESPACE_TYPE        = 0x0101,
247:     RES_XML_START_ELEMENT_TYPE        = 0x0102,
248:     RES_XML_END_ELEMENT_TYPE          = 0x0103,
253:     RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
287: struct Res_value
461: struct ResStringPool_header
612: struct ResXMLTree_header
621: struct ResXMLTree_node
677: struct ResXMLTree_attrExt
686:     // Byte offset from the start of this structure where the attributes start.
687:     uint16_t attributeStart;
707: struct ResXMLTree_attribute
236-257 dump:
236: 
237: enum {
238:     RES_NULL_TYPE                     = 0x0000,
...
244:     RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245:     RES_XML_START_NAMESPACE_TYPE      = 0x0100,
...
253:     RES_XML_RESOURCE_MAP_TYPE         = 0x0180,
254:
255:     // Chunk types in RES_TABLE_TYPE
total lines: 2366
```

## 2. Per-anchor verdict table

Pointer convention: `E1` = entry line 1 (`source:` S038 header), `E57` = entry item 4 prose, `E82` = entry item 8 prose. All entry pointers are `.../corpus/knowledge/round-68-apk-axml-byte-evidence.md:<n>`.

| # | anchor as stated in the entry | entry pointer | stated line | derived line | verdict |
|---|---|---|---|---|---|
| 1 | `struct ResChunk_header` | E1 | 218 | 218 | MATCH |
| 2 | chunk-type enum block | E1, E57 | 237-253 (range) | 237 = `enum {`, 253 = `RES_XML_RESOURCE_MAP_TYPE` | MATCH (both endpoints; see note N1) |
| 3 | `RES_STRING_POOL_TYPE` | E1, E57 | 239 | 239 | MATCH |
| 4 | `RES_XML_TYPE` | E1 | 241 | 241 | MATCH |
| 5 | `RES_XML_START_NAMESPACE_TYPE` | E1, E57 | **245** | 245 | MATCH |
| 6 | `RES_XML_END_NAMESPACE_TYPE` | E1, E57 | 246 | 246 | MATCH |
| 7 | `RES_XML_START_ELEMENT_TYPE` | E1, E57 | 247 | 247 | MATCH |
| 8 | `RES_XML_END_ELEMENT_TYPE` | E1, E57 | 248 | 248 | MATCH |
| 9 | `RES_XML_RESOURCE_MAP_TYPE` | E1, E57 | 253 | 253 | MATCH |
| 10 | `struct ResStringPool_header` | E1 | 461 | 461 | MATCH |
| 11 | `struct ResXMLTree_header` / `ResXMLTree_node` | E1 | 612, 621 | 612, 621 | MATCH |
| 12 | `struct ResXMLTree_attrExt` | E1, E82 | 677 | 677 | MATCH |
| 13 | attrExt `attributeStart` field comment | E1, E82 | 686 | 686 | MATCH |
| 14 | attrExt `uint16_t attributeStart;` declaration | E1, E82 | 687 | 687 | MATCH |
| 15 | `struct ResXMLTree_attribute` | E1 | 707 | 707 | MATCH |
| 16 | `struct Res_value` | E1 | 287 | 287 | MATCH |
| 17 | item 5 (struct-width prose) | E59-E77 | none stated | — | N/A — no AOSP spec line number is stated (see note N3) |
| 18 | context: `RES_XML_FIRST_CHUNK_TYPE` | E148 | 244 | 244 | MATCH |

Counts: 15 single-line anchors stated in E1 (`218, 239, 241, 245, 246, 247, 248, 253, 461, 612, 621, 677, 686, 687, 707`) + 1 range (`237-253`) + 1 context line (`244`) + 1 prose range repeated in item 4 — **17/17 checked line numbers MATCH, 0 MISMATCH, 0 unchecked in the assigned scope.**

Item 4 re-states 6 of E1's numbers (`string pool :239`, `start/end namespace :245/:246`, `start/end element :247/:248`, `resource map :253`) — all MATCH, and its value mapping is correct against the same snapshot lines (`0x0001`, `0x0100`, `0x0101`, `0x0102`, `0x0103`, `0x0180`).
Item 8 states `line 677`, `snapshot line 686`, `line 687` — all MATCH, and 686/687 are respectively the comment and the field declaration the prose describes.

## 3. Exit-code contract and operability

The script's own contract (entry:7 recheck; S046 at entry:4) is "exit 0 with 17 lines; exit 2 on a missing or ambiguous symbol". Verified positively (exit 0 twice, §1) and negatively, in a relocated `/tmp` copy (`/tmp/r68ad_neg/corpus/{derive_axml_anchors.py,snapshots/ResourceTypes.h}` — script resolves the snapshot via `Path(__file__).resolve().parent`, so it also proves tree-relocation operability):

```
--- A: missing snapshot ---
derive_axml_anchors: snapshot missing: /tmp/r68ad_neg/corpus/snapshots/ResourceTypes.h
EXIT_A=2
--- B: digest mismatch (one byte flipped) ---
derive_axml_anchors: snapshot digest a626a32829c03083dfc38e63fcf4e4db6e824fc2c7380171a1586bfb7d137eb6 != pinned 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f
EXIT_B=2
--- C: ambiguous symbol (duplicated enum line, pin patched in the /tmp copy) ---
patched pin to 33eba5a764e883af2c2310770d08783f1f4145673cd8594e0321735bbfe0853b
derive_axml_anchors: enum RES_XML_START_NAMESPACE_TYPE: ambiguous (2 hits at [245, 246])
EXIT_C=2
```

The script prints nothing on the failure paths before the diagnostic (no partial anchor table), so it cannot emit a line number it did not uniquely find: the `find_unique` helper (`corpus/derive_axml_anchors.py:64-70`: `:66` `if not hits`, `:68` `if len(hits) > 1`, `:70` `return hits[0]`) fails on zero hits and on >1 hits, and the digest pin is checked (`:78-79`) before any symbol search (`:74` resolves the snapshot path from `__file__`).

## 4. Quoted entry lines (verbatim, file:line)

`.../corpus/knowledge/round-68-apk-axml-byte-evidence.md:1` (single physical line; the anchor list read):

> anchors: `struct ResChunk_header` (line 218); chunk-type enum block **lines 237-253**: `RES_STRING_POOL_TYPE` :239, `RES_XML_TYPE` :241, `RES_XML_START_NAMESPACE_TYPE` **:245**, `RES_XML_END_NAMESPACE_TYPE` :246, `RES_XML_START_ELEMENT_TYPE` :247, `RES_XML_END_ELEMENT_TYPE` :248, and `RES_XML_RESOURCE_MAP_TYPE` :253 (0x0180 — inside the enum block, unlike the round-65 draft's :239-250); `struct ResStringPool_header` (line 461); `struct ResXMLTree_header`/`ResXMLTree_node` (lines 612, 621); `struct ResXMLTree_attrExt` (line 677; its `attributeStart` field comment "Byte offset from the start of this structure where the attributes start." at line 686, with the field declaration `uint16_t attributeStart;` at line 687); `struct ResXMLTree_attribute` (line 707); `struct Res_value` (line 287); **every line number above is machine-derived by `corpus/derive_axml_anchors.py` from the pinned snapshot — item 11**

`:57` (item 4 prose):

> The six chunk types in the table — `0x0001` string pool, `0x0180` resource map, `0x0100` start namespace, `0x0102` start element, `0x0103` end element, `0x0101` end namespace — are the values S038's chunk-type enum block names at **lines 237-253** (string pool :239, start/end namespace :245/:246, start/end element :247/:248, resource map `RES_XML_RESOURCE_MAP_TYPE` :253 — every one of these line numbers is derived by item 11's command).

`:59` (item 5 prose — no line number in it, quoted for completeness of the assigned range):

> 5. The fixed structure widths used by the readout are computed by summing the field widths of S038's own struct definitions (two `uint16` plus one `uint32` for `ResChunk_header`; five `uint32` after the chunk header for `ResStringPool_header`; and so on), not assumed:

`:82` (item 8 prose):

> Provenance of the attribute location: S038's `struct ResXMLTree_attrExt` (line 677) "Appears header.headerSize bytes after a `ResXMLTree_node`", so the attrExt starts at `chunk_base + 16` (the derived 16-byte node header, item 5); its `attributeStart` field is "Byte offset from the start of this structure where the attributes start" (snapshot line 686; the field declaration `uint16_t attributeStart;` at line 687 — item 11 derives both), so attribute *i* is at `chunk_base + 16 + attributeStart + i * attributeSize`

`:148` (the off-by-one claim that falsified the earlier drafts):

> The chunk-type enum block spans lines 237-253 and `RES_XML_START_NAMESPACE_TYPE` is line **245**; line 244 is `RES_XML_FIRST_CHUNK_TYPE`.

`:129-145` (item 11 embedded table): verbatim `diff`-clean against the actual stdout of §1.

## 5. Notes (precision, not defects on the anchor surface)

- **N1 — enum-range label.** `237` is the `enum {` opening and `253` is `RES_XML_RESOURCE_MAP_TYPE`, the last XML chunk-type entry; but the enclosing C enum does not close at 253 — the first `};` is at **line 263** (`/tmp` scan of `corpus/snapshots/ResourceTypes.h`), and 254 is blank with `// Chunk types in RES_TABLE_TYPE` at 255. So `237-253` is the *XML chunk-type span* inside the enum block, not the whole block. Both stated endpoints are correct lines and every member line named is correct; only the noun ("enum block") overstates the range boundary. Flagged for Q01/Q11 adjudication; it changes no anchor and no byte.
- **N2 — quote punctuation.** Item 8 (:82) quotes line 686 without the snapshot's trailing period; the `source:` header (:1) quotes it with the period and the snapshot line is `// Byte offset from the start of this structure where the attributes start.` (period present). Cosmetic; line number unaffected.
- **N3 — item 5 is out of the derivation's coverage.** Item 5 states no AOSP line number, so there is nothing to derive; its width sums (`ResChunk_header` 8, `ResXMLTree_node` 16, `ResXMLTree_attrExt` 20, `ResXMLTree_attribute` 20, `ResStringPool_header` 28, `Res_value` 8) come from `corpus/fixtures/apk-r65/readout.py --fact spec_derived_struct_widths`, a different command whose output I did not re-run here (fixture surface is read-only for this seat and that output is another seat's surface). C2's "every spec line number derived" therefore holds; "fixed struct widths derived" rests on the readout, not on `derive_axml_anchors.py` — the entry does not conflate them (item 5 shows its own command), but a reviewer should not read item 11 as covering item 5's numbers.
- **N4 — shared enum value.** `244 RES_XML_FIRST_CHUNK_TYPE = 0x0100` and `245 RES_XML_START_NAMESPACE_TYPE = 0x0100` are distinct lines with the same value; the entry's :148 statement names 244 as `RES_XML_FIRST_CHUNK_TYPE`, which the snapshot confirms. The `:244` → `:245` repair is real, not a renumbering artefact of the duplicate value.

## 6. Scope, risks, blockers

- Scope covered: the `source:` S038 anchor list, item 4, item 5, item 8, item 11's embedded table, and the line-244 remark — i.e. every AOSP `ResourceTypes.h` line number the entry states. S043's "lines 7-8" points at a different snapshot (`rea-android-applications.md`) and is outside the AXML anchor surface; S045 states no line numbers.
- Risk: none on the anchor axis. Residual, not mine to close: the C7 gate's own attribution (C1) and the counter's `C7_V3_CLEAN` reading are separate surfaces; this report asserts only that the item-11 block is verbatim-reproducible, which is the input that check consumes.
- Blockers: none.
- Tooling installs/updates: none (python3 stdlib, coreutils `cmp`/`sha256sum`/`diff` already present). No pacman transaction attempted.
