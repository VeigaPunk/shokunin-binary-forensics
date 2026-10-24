PASS — the entry is checkable-content minimal except for exactly one sentence: the final §Limitations sentence ("Generalization to other APKs, … would need its own evidence"), whose fence is already stated twice in the same file; smallest deletion set = that one sentence. No Observation item is redundant and every §Inference claim is forced in its class.

Seat: R65SimplifierDrift (minimality review, read-only). Target: corpus/knowledge/round-65-apk-axml-byte-evidence.md (candidate). All paths relative to /home/vgpnk/Projects/shokunin/revenger-shokunin. No tool installs were made (none needed; pacman guard respected).

## 1. Identity of the reviewed bytes

- Fixture sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` — reproduced (sha256sum, matches entry source S041 line and claims.md).
- readout.py sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` — reproduced.
- Rerun `python3 -B corpus/fixtures/apk-r65/readout.py`: exit 0, **15 lines**, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — equals the digest pinned in the entry header (`recheck:`) and §Reproduce.
- Source snapshots match their pinned digests: `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` = `56b88bc4…` , `rea-android-applications.md` = `412d9cb4…`.

## 2. Question 1 — Observation redundancy: none

The recheck contract pins the **exact 15-line stdout digest**. The 15 output lines map 1:1 onto items 1–10, so deleting any item breaks the pinned digest and with it Q02/Q11:

| item | stdout fact(s) |
|---|---|
| 1 | archive |
| 2 | eocd |
| 3 | member[AndroidManifest.xml], member[classes.dex], member[META-INF/MANIFEST.MF] |
| 4 | axml_chunk_table |
| 5 | spec_derived_struct_widths |
| 6 | axml_string_pool |
| 7 | axml_resource_map |
| 8 | axml_start_element, axml_start_namespace, axml_end_element, axml_end_namespace |
| 9 | dex_declared_header |
| 10 | jar_manifest |

Cross-reference coupling inside the entry: item 4 and item 8 narratives both lean on item 5's derivation ("derived in item 5"); §Comparison cites items 1, 3, 6–8; Q-map Q11 cites items 1–10 and item 5 explicitly. Item 5 is not redundant against item 4's chunk table: the table shows *observed* headerSizes; item 5 proves they equal sums of S038's own struct field widths — that independent derivation is precisely the Q03/Q11 basis. Intra-item-8 sub-facts are not redundant: the chunk table (item 4) establishes existence/extent of the six chunks, not content; `axml_start_namespace` binds prefix_index 0 / uri_index 1 (which makes the `android:` attributes in item 8 checkable as a resolved prefix), and the two end chunks close the walk with their own checkable index bytes. Lesson, SOURCES.md and measure.py reference the entry by path but none references its items or sections (grep over corpus/lessons/round-65.md, corpus/SOURCES.md, reports/round-65/measure.py) — no external caller on item wording, and none needed: the digest coupling alone forbids item deletion.

## 3. Question 2 — §Inference force: all three forced in class

1. Chunk types / headerSizes are S038's: bytes item 4 (types 1, 384, 256, 258, 259, 257; headerSizes 28/8/16) + item 5 derivation; enum anchor verified in the pinned snapshot (`.ufo/waves/round-65/source-snapshots/ResourceTypes.h:241-253`: `RES_XML_TYPE = 0x0003` :241, `0x0100`–`0x0104` :245-249, `RES_XML_RESOURCE_MAP_TYPE = 0x0180` :253).
2. `0xffffffff` is the null string-pool index: bytes force the *out-of-range* fact — ns_index 4294967295 (items 8, end-element) against a 9-entry pool (item 6, valid indices 0–8). The sentinel *naming* is the sourced part and the snapshot does carry an explicit `0xFFFFFFFF` sentinel in the string-index domain (`ResStringPool_span` `enum { END = 0xFFFFFFFF }` with "The special value END (0xFFFFFFFF) indicates…", snapshot :496-502), though it is stated for style spans. Classifying this as Inference rather than Observation is exactly correct; nothing to delete.
3. The two non-zero resource-map entries are the framework ids the fixture declared: bytes item 7 (`0x0101021b`/`0x0101021c` at pool indices 5/6, matching item 6's `versionCode`/`versionName`) + oracle ground in `corpus/fixtures/apk-r65/truth.json` (`axml_declared.resource_ids` contains `0x0101021b`, `0x0101021c` — grep, 1 hit each).

## 4. Question 3 — §Limitations vs the legend: one sentence covered

The README Coverage-map legend (corpus/README.md, "Status: held/partial/uncovered/frontier … Work evidence is not knowledge") carries no scope fences, so strictly nothing is covered *by the README legend*. The entry's own coverage-map header line ("Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture") plus the §Observation/inference/unknown "Unknown" bullet are the fences, and against those:

- **Deletion candidate (the only one):** the final §Limitations sentence "Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence." It is a negative scope claim with nothing to check, and its entire content is restated verbatim-in-meaning by the coverage-map line ("general AXML … beyond this fixture", "provider … readiness or output") and again by the Unknown bullet ("nothing about … any provider's behavior is claimed"). Deleting it loses no checkable content; Q10's basis ("the §Limitations and §Cross-lane scope note name what is not claimed") stays true because §Limitations still names non-claims (compression clause, dex-validity sentence). Third restatement of the same fence, third time in one file.
- **Keep L1** (one fixture, one manifest shape, UTF-8 pool only, no CDATA/nested/styles) and **keep L2** (ZIP_STORED, no data descriptors, no split/spanned/compression) and **keep L3** (dex header-only, intentionally invalid): each carries fixture-specific checkable facts — `styleCount: 0`/`utf8: true` (item 6), single start element / six-chunk extent (item 4), all members `compressed_size == uncompressed_size` (item 3), dex `file_size == header_size == 112` (item 9) — that appear nowhere else as an explicit scope statement. "no data descriptors" in particular is stated nowhere else in the entry.

## 5. Deletion-impact / caller analysis

- No LSP server answers a Markdown prose file (semantic `references` unavailable for the target; recorded here per seat rules) — the caller proof above is therefore grep + the pinned-digest coupling, which is the strongest proof available for prose coupled to a pinned stdout hash.
- The read-only bound was honored: the proposed deletion was **not** applied; the entry on disk is unmodified by this seat.

## 6. Non-blocking nits (accuracy, not minimality; no deletion implied)

1. The entry (and SOURCES.md S038, consistently) pins the chunk-type enum at "lines 239-250"; in the pinned snapshot `RES_XML_TYPE` is :241 and `RES_XML_RESOURCE_MAP_TYPE` :253, so the range under-covers the resource-map anchor by 3 lines. Cosmetic anchor imprecision only — all values verified present.
2. Item 7's "S038's `ResXMLTree::getAttributeNameResID` semantics make 0 'no resource id'" rests on a thin textual anchor: the snapshot declares the accessor at :792 with no semantics comment (the nearby `-1`/`-2` comment at :786 belongs to `getAttributeNamespaceID`). The observation itself is carried by the seven `0x00000000` bytes; the semantics tag is interpretive. A fresh-seat Q01 reviewer may want this noted, not deleted.

## 7. Stop rule

Next deletion candidates (L1's facts re-derivable from items 4/6; L3 from item 9) would hollow the §Limitations paragraph that Q10's decision explicitly cites as its basis — that deletion harms an axis, so the set stops at the single sentence in §4.
