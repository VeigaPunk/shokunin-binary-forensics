Q11 PASS — all 16 embedded `$ cmd`/output segments in the v2 entry re-verified verbatim against fresh runs of `corpus/fixtures/apk-r65/readout.py`; every count/offset/identifier/digest in prose carries its deriving command + output or is labeled recorded; constants are derived (item 5 `spec_derived_struct_widths`, item 8 attrExt-relative provenance), not assumed.

Seat: R67ReviewEntryQ11 (fresh, non-author). Entry under test: `corpus/knowledge/round-67-apk-axml-byte-evidence.md` @ commit 7668510. Criterion text: `corpus/QUALITY.md` Q11 row (supersedes Q08).

## Evidence

1. M39 check on v2 entry — `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-67-apk-axml-byte-evidence.md` (from lane root):
   `checked_blocks=16 problems=0` exit 0.
2. Independent re-derivation (own fenced-block parser, `$` line restarts the command inside a fence; each output line must appear verbatim in that command's fresh stdout): `cmd_segments: 16 unique: 16 missing: 0`. All 16 commands exited 0.
3. Full re-run: `python3 -B corpus/fixtures/apk-r65/readout.py` → 15 stdout lines, `sha256sum` = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — exactly the `recheck:` pin in the entry header.
4. M39 baseline contrast — `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-65-apk-axml-byte-evidence.md`:
   `drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, ... "payload_first16_hex": "4d616e696673742d56657273696f6e", ...}` — `checked_blocks=15 problems=1` exit 1, naming entry:41. The v2 entry carries the corrected 16-byte pair `4d616e69666573742d56657273696f6e` on entry:42 (its block's command is entry:41), verbatim in the re-run stdout.
5. Digest spot-verification (`sha256sum`, all match entry anchors):
   - `corpus/fixtures/apk-r65/fixture.apk` = `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (entry items 1, S041 anchor)
   - `truth.json` = `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`; `readout.py` = `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`
   - `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` = `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` (S043 anchor)
   - `.ufo/waves/round-67/source-snapshots/dex-format.html` = `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` (S045 anchor)
6. Coverage of Q11 clauses:
   - Counts/offsets: 947, 925, 737+188=925, 3 entries, 416/204/248/272/368/392 chunk offsets, 9 strings/styles, 20/20/3 attribute fields — every one appears in a shown `--fact` output line in the same item's block.
   - Constants derived: headerSize column {28,8,16,16,16,16} tied to item-5 derived `total_bytes`; `attributeStart`/`attributeSize` 20 = derived `ResXMLTree_attrExt`/`ResXMLTree_attribute` widths; attrExt location derived `chunk_base + 16` (derived node header) per S038:677 + snapshot lines 685-687, readout.py:200-203.
   - Recorded labeled: all-zero resource-map entries "recorded as observed"; `ns_index` `0xffffffff` "recorded as observed and treated as null"; the prose `4d616e69666573742d` ASCII prefix restated from the output's 16-byte pair, with the r65 drift explicitly labeled recorded-history.
   - No recorded value presented as re-derived found.
7. Oracle agreement spot (item-7 claim surface): `truth.json` `axml_declared.resource_ids` = readout `ids` array verbatim, including `0x0101021b`/`0x0101021c` at indices 5-6.

## OFF-criterion notes

- OFF- `git status --porcelain` shows untracked `corpus/lessons/round-67.md` in the working tree (outside the committed claim surface this seat reviewed; note only).
- OFF- The v2 block numbering shifted one line vs r65: the corrected hex pair sits at entry:42 (command at :41), while claims.md's repair description indexes the r65 drift site "entry:41". Cosmetic; the gate names the right drift and the v2 bytes carry the right pair.

Tooling: no installs/updates this seat (system `python3`, `sha256sum` sufficed).
Report: `.ufo/waves/round-67/R67ReviewEntryQ11.md`
