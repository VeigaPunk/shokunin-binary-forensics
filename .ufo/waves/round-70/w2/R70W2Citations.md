ALL-RESOLVE — every explicit locator in the landed entry resolves TRUE (24 locator claims = 25 distinct (target, line) pairs: 9 `file:line`, 7 `lines N-M`, 6 `first line N`, 3 heading lines; `ResourceTypes.h:686` is cited twice), and every `source:` digest/line claim matches item 14 / item 12 / item 11 output; ONE separate prose positional locator is FALSE (`corpus/knowledge/round-70-apk-axml-byte-evidence.md:152`, "the last three lines"), reported below as a located defect that is not one of the enumerated citation forms.

# R70W2Citations — citation resolver on landed bytes

Bytes judged: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd:corpus/knowledge/round-70-apk-axml-byte-evidence.md`
= sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`, 322 lines, 38186 bytes, `admission-status: candidate` (entry:11). Tree `944e37b49d6cf4ba4b29414b74d2b6f98e81dcd4`, commit date 2026-10-25 18:30:34 -0300.
Targets read from `git archive 17ee… corpus` extracted to `/tmp/revenger-r70-R70W2Citations/tree` (scratch, deleted). No lane file was written or edited; every command below is read-only and was run inside the scratch extraction, never in the lane tree.

## 1. Citation table (entry line | citation | what the cited file says there | verdict)

`cat -n`/`awk` line-numbered reads of `corpus/fixtures/apk-r65/readout.py`, `corpus/fixtures/apk-r65/generator.py`, `corpus/snapshots/{ResourceTypes.h,APPNOTE.TXT,dex-format.html,rea-android-applications.md}`, `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`, `/home/vgpnk/Projects/shokunin/kaidoku-shokunin/corpus/README.md`.

| entry line | citation | what the file says there | TRUE/FALSE |
|---|---|---|---|
| 30 | `readout.py:76`, constant `b"PK\x05\x06"` | `76:     sig_eocd = b"PK\x05\x06"` | TRUE |
| 39 | `readout.py:105`, `payload_offset = local_header_offset + 30 + name_length + extra_length` | `105:        payload_off = lh_off + 30 + lh_name_len + lh_extra_len` (formula identical; entry renames the variables it prints) | TRUE |
| 63 | `readout.py:51-58`, manual transcription of S038 struct field lists | `51: w8, w16, w32 = 1, 2, 4` … `58: "Res_value": [w16, w8, w8, w32],` — the six struct width lists; `60: sizes = {name: sum(w) …}` | TRUE |
| 72 | `readout.py:155-168`, strings decoded from pool-stated offsets | `155: offsets = [u32(axml, so + sp["headerSize"] + 4 * i) …]` … `161: s = axml[base + 2:base + 2 + u8len].decode("utf-8")` … `168: offsets=offsets, strings=strings)` | TRUE |
| 72 | `readout.py:166`, UTF-8 flag `flags & 0x100` | `166:         utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),` | TRUE |
| 86 | `readout.py:203`, `aoff = base + 16 + attribute_start + i * attribute_size` | `203:         aoff = base + 16 + attribute_start + i * attribute_size` — character-identical | TRUE |
| 86 | `readout.py:211`, `strings[ans]` (namespace resolved by direct pool indexing) | `211: "ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],` | TRUE |
| 86 | "S038's comment on `attributeStart` (quoted and located by item 11)" | `ResourceTypes.h:686:     // Byte offset from the start of this structure where the attributes start.` (item 11 prints `comment attributeStart : 686`; `687: uint16_t attributeStart;`) | TRUE |
| 101 | `readout.py:233-248`, dex declared header | `233: magic = dex[:8]` … `241: checksum_recomputed=…zlib.adler32(dex[12:])…` `244: signature_recomputed=hashlib.sha1(body_after_sig)…` `247: endian_tag=f"0x{u32(dex, 40):08x}"` `248: header_bytes=len(dex))` | TRUE |
| 288 | `generator.py:8` docstring, "not a valid dex program" | `8:                          contains no classes and is not a valid dex program);` | TRUE |
| 288 | `readout.py:49-50` comments widths "computed here … not assumed" | `49:     # Every fixed offset the readout uses is computed here from the field` / `50:     # widths in ResourceTypes.h's own struct definitions, not assumed.` | TRUE |
| 292 | fleet `.ufo/l0-questions.md:42` = the kaidoku/revenger ADJ-06 overlap | `42: tsukuroi | round-1 | Ratify … and arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed? …` | TRUE |
| 292 | `kaidoku-shokunin/corpus/README.md:27` = APK content-graph inventory | `27: | Archives & packages | … 2026-10-13-r3-apk-inventory … APK content graph (120 deduplicated content nodes; all 130 occurrences hash-verified) …` | TRUE |
| 292 | `kaidoku-shokunin/corpus/README.md:29` = Android decode axis | `29: | knowledge/2026-10-13-r4u-02-jadx-decode | Android decode axis first-held on Godot APKs: inspect-android-package … |` | TRUE |
| 144 | `first line 7` (S049, `rea-android-applications.md`) | `7: Start with \`inspect_android_package\` on the caller's APK path for package` (sentence continues at :8) | TRUE |
| 145 | `first line 5949` (checksum row) | `5949:   <td>adler32 checksum of the rest of the file (everything but` | TRUE |
| 146 | `first line 5956` (signature row) | `5956:   <td>SHA-1 signature (hash) of the rest of the file (everything but` | TRUE |
| 147 | `first line 5981` (header_size row) | `5981:     <p>must be 0x70 (112) bytes` | TRUE |
| 148 | `first line 5035` (`ENDIAN_CONSTANT`) | `5035: uint ENDIAN_CONSTANT = 0x12345678;` | TRUE |
| 149 | `first line 686` (`attributeStart` comment) | `686:     // Byte offset from the start of this structure where the attributes start.` | TRUE |
| 3 (header) | S048 locators: `header_item` table under "Items and related structures", `ENDIAN_CONSTANT` under "Bitfield, string, and constant definitions" | `dex-format.html:5921: <h2 …>Items and related structures</h2>` (5921 < 5949/5956/5981) and `:4964: <h2 …>Bitfield, string, and constant definitions</h2>` (4964 < 5035 < 5921) | TRUE |
| 171 | `heading line 387, transcribed field lines 389-399` (§4.3.7) | `387:    4.3.7  Local file header:`; 389 signature … 399 `extra field length 2 bytes` (400 blank) | TRUE |
| 172 | `heading line 511, transcribed field lines 522-538` (§4.3.12) | `511:    4.3.12  Central directory structure:`; 522 `central file header signature` … 538 `relative offset of local header 4 bytes` (539 blank) | TRUE |
| 173 | `heading line 632, transcribed field lines 634-646` (§4.3.16) | `632:    4.3.16  End of central directory record:`; 634 signature … 646 `.ZIP file comment length` (647 variable comment) | TRUE |
| 152 | "the last three lines print where each record layout sits in the snapshot" | The last three content lines of the item-12 block are `173 MATCH APPNOTE 4.3.16`, `174 MATCH central.fixed_part`, `175 MATCH local.fixed_part`; only ONE of the three is a layout line, and the three layout lines are `171-173` | **FALSE** (see §3) |

Counts: 24 enumerated locator claims (25 distinct target/line pairs; `ResourceTypes.h:686` cited at entry:86 and entry:149) → all TRUE, none FALSE; the table's 25th row is the positional descriptor, FALSE (see §3).

## 2. `source:` line digest/line verification (entry lines 1-7) against item 14 / item 12 / item 11

Independent `sha256sum` + `wc -c` of the ten pinned files in the extracted tree, compared with the embedded item-14 block (entry:222-231):

| item 14 line | pinned value | recomputed | verdict |
|---|---|---|---|
| 222 | `05d2280f…d03e` 947 B `fixture.apk` | `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` 947 B | TRUE |
| 223 | `27303bae…8173` 2466 B `truth.json` | `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173` 2466 B | TRUE |
| 224 | `eaa9444c…7c1a` 9599 B `generator.py` | `eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a` 9599 B | TRUE |
| 225 | `92e347c3…3976` 11236 B `readout.py` | `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` 11236 B | TRUE |
| 226 | `2d4f25f6…b1f9` 15062 B `entry_checks.py` | `2d4f25f6894ac86ced3c9986abd7cdbcf4c6d2aab477cda6dc515585c129b1f9` 15062 B | TRUE |
| 227 | `74d4c0d9…83aa` 4979 B `derive_axml_anchors.py` | `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa` 4979 B | TRUE |
| 228 | `56b88bc4…c56f` 86255 B `snapshots/ResourceTypes.h` | `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` 86255 B | TRUE |
| 229 | `0b993022…0cd6` 174585 B `snapshots/APPNOTE.TXT` | `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` 174585 B | TRUE |
| 230 | `c0428612…d9f4` 281157 B `snapshots/dex-format.html` | `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` 281157 B | TRUE |
| 231 | `412d9cb4…a74c` 1992 B `snapshots/rea-android-applications.md` | `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` 1992 B | TRUE |

Ten-of-ten digests and sizes TRUE, so every `source:` line's "digest printed in item 14" resolves to the file it names.

Per-source line claims:
- **L1 S038** — "digest printed in item 14": TRUE (row 228). "every S038 line number and enum value this entry states is printed by the item-11 command, none is typed by hand": TRUE — the derivation prints 20 lines, and each line number the entry relies on was re-checked against the snapshot bytes: `218 struct ResChunk_header`, `287 struct Res_value`, `461 struct ResStringPool_header`, `612 struct ResXMLTree_header`, `621 struct ResXMLTree_node`, `677 struct ResXMLTree_attrExt`, `707 struct ResXMLTree_attribute`, `237 enum {`, `239 RES_STRING_POOL_TYPE = 0x0001`, `241 RES_XML_TYPE = 0x0003`, `244 RES_XML_FIRST_CHUNK_TYPE = 0x0100`, `245 RES_XML_START_NAMESPACE_TYPE = 0x0100`, `246 …END_NAMESPACE… = 0x0101`, `247 …START_ELEMENT… = 0x0102`, `248 …END_ELEMENT… = 0x0103`, `253 …RESOURCE_MAP… = 0x0180`, `263 };`, `686 // Byte offset from the start of this structure where the attributes start.`, `687 uint16_t attributeStart;` — all 19 symbol lines land on the named symbol.
- **L2 S049** — "first line 7": TRUE (§1). "re-fetched … byte for byte with the committed snapshot": the committed snapshot's digest/size equal the S049 registry row's (`412d9cb4…`, 1992 B) — consistent, not independently re-fetched by me.
- **L3 S048** — four quoted phrases: TRUE (six `MATCH` lines incl. the four dex phrases, item-11 output reproduced exactly). "heading 'Items and related structures'" / "`ENDIAN_CONSTANT` under 'Bitfield, string, and constant definitions'": TRUE (5921 / 4964). "the live page differs from the snapshot only in page-chrome lines": CONCORDANT with the S048 registry row ("per-request CSP nonce and one devsite loader line") — paraphrase, not independently verifiable without a fetch, which this seat did not perform.
- **L4 S032 / L5 S034** — "heading and field line numbers printed by item 12": TRUE for §4.3.12 (511 / 522-538) and §4.3.16 (632 / 634-646) and §4.3.7 (387 / 389-399). The 15 spec-offset `MATCH … present=True` lines were each re-resolved against the readout source: `eocd+10`(80), `eocd+12`(78), `eocd+16`(79), `cursor+28`(91), `cursor+30`(92), `cursor+32`(93), `cursor+42`(94), `lh_off+14`(102), `lh_off+18`(101), `lh_off+22`(113), `lh_off+26`(99), `lh_off+28`(100), `cursor+46`(95), `lh_off+30`(103/105) — TRUE, and the offsets match the APPNOTE field order above (EOCD 4+2+2+2+2=12 → size at 12, offset at 16; central 4+2·6+4+4+4+2=28 → name 28, extra 30, comment 32, external 38+4 → local-header offset 42; local 4+2·5+4=14 → crc 14, comp 18, uncomp 22, name 26, extra 28).
- **L6 S047** — "digests printed in item 14" for `derive_axml_anchors.py` (227) and `snapshots/ResourceTypes.h` (228): TRUE. Registry row S047 (`corpus/SOURCES.md:61`) states script sha256 `74d4c0d9…`, 20 output lines — the run prints exactly 20 lines.
- **L7 S041** — "the four digests printed in item 14, which also prints the digest of `entry_checks.py`": TRUE (222-226; four fixture-bundle files + checker).

Item 14's own count sentence ("the ten files under `corpus/` that the commands above read, including the script that prints items 2 and 11-17"): TRUE — exactly ten distinct files are read by the 25 embedded commands, all under `corpus/`, and `entry_checks.py` prints item 2's second command and items 11-17.

## 3. The one FALSE locator (located defect, not an enumerated citation form)

`corpus/knowledge/round-70-apk-axml-byte-evidence.md:152` (landed commit 17ee7f87):

> "…each is compared with the literal in the readout source; **the last three lines print where each record layout sits in the snapshot** (heading line and the first and last transcribed field lines)."

Deriving command and its actual output (run from the extracted tree):

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout
… (20 stdout lines) …
16 MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399
17 MATCH APPNOTE 4.3.12: heading line 511, transcribed field lines 522-538
18 MATCH APPNOTE 4.3.16: heading line 632, transcribed field lines 634-646
19 MATCH central.fixed_part: spec width 46, readout.py literal `cursor + 46` present=True
20 MATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True
```

The block's last three lines (entry:173-175) are `MATCH APPNOTE 4.3.16`, `MATCH central.fixed_part`, `MATCH local.fixed_part`; two of them do not print a snapshot location at all, and the three lines that print the three record layouts are stdout lines 16-18 (entry:171-173). So the descriptor is false as written. **What it does not do:** it falsifies no printed value — all 20 lines reproduce byte-exactly (§4) and the three layout lines do appear, just not last. A seat deciding Q11/Q13 ("every claim carries its deriving command") can carry this as a located FAIL (`entry:152` + the output above); a seat reading it as a pure prose-position slip can record it as a minor defect. I do not issue a Q decision — I report that this is the only locator in the entry that does not resolve.

## 4. Block replay: every `$` command re-run on the landed bytes

A scratch harness extracted each fenced block, ran every `$ ` command from the extracted tree root, and diffed the concatenated stdout against the embedded lines:

```
--- block at entry line 25: 1 cmd --- EXACT MATCH (1 lines)
--- block at entry line 32: 2 cmds -- EXACT MATCH (2 lines)
--- block at entry line 41: 3 cmds -- EXACT MATCH (3 lines)
--- block at entry line 56: 1 cmd --- EXACT MATCH (1 lines)
--- block at entry line 65: 1 cmd --- EXACT MATCH (1 lines)
--- block at entry line 74: 1 cmd --- EXACT MATCH (1 lines)
--- block at entry line 81: 1 cmd --- EXACT MATCH (1 lines)
--- block at entry line 88: 4 cmds -- EXACT MATCH (4 lines)
--- block at entry line 103: 1 cmd -- EXACT MATCH (1 lines)
--- block at entry line 112: 1 cmd -- EXACT MATCH (1 lines)
--- block at entry line 121: 2 cmds -- EXACT MATCH (26 lines)
--- block at entry line 154: 1 cmd -- EXACT MATCH (20 lines)
--- block at entry line 180: 1 cmd -- EXACT MATCH (34 lines)
--- block at entry line 220: 1 cmd -- EXACT MATCH (10 lines)
--- block at entry line 236: 1 cmd -- EXACT MATCH (1 lines)
--- block at entry line 243: 1 cmd -- EXACT MATCH (3 lines)
--- block at entry line 252: 1 cmd -- EXACT MATCH (24 lines)
TOTAL BLOCK MISMATCHES: 0
```

17 blocks / 25 commands, every one exit 0, every embedded line reproduced verbatim (strict equality, both directions — so no stale or extra line). This is the byte-level basis for "every locator resolves": the outputs the citations point into are the outputs the landed scripts print today.

Derivation cross-checks that back the table: `derive_axml_anchors.py` exit 0 printing `sha256 56b88bc4… ResourceTypes.h` + 19 symbol lines (item 11's first block); `entry_checks.py --spec-quotes` exit 0 with the six `MATCH … first line N` lines; `--pins` exit 0 with the ten digests; `--stdout-digest` exit 0 printing `readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`; `--eocd` exit 0 printing `eocd signature bytes at offset 925: 504b0506 (4 bytes)` (independent of the readout's own offset 925, and 737+188=925 agrees with `cd_end_equals_eocd_offset: true`).

## 5. Other observations (not FALSE, recorded for the gate)

1. **Stale row name at entry:101** — "`magic`, `format_version`, `file_size` and `header_bytes` are printed without a quoted **S045** phrase", while the same sentence's first half names **S048** and the header (entry:3) says "S048 — supersedes S045". `corpus/SOURCES.md:62` confirms S048 supersedes S045 with "the four quoted phrases … unchanged", and `:59` shows S045's own anchor column carries the same three phrases plus `ENDIAN_CONSTANT` — so the substantive claim (no quoted phrase covers those four fields) is TRUE either way; only the row identifier is stale. No line number is involved, so it is outside the enumerated citation forms; it is a naming defect a Q01/Q09 seat may want to carry.
2. **Cross-lane citations are exact** (entry:292): the fleet question line and both kaidoku README lines say what the entry says they say, and the entry's non-absorption fence is consistent with them.
3. **`readout.py:N` label honesty** — the entry labels these as "source locators checked by reading the file, and the literals they concern are compared in items 12 and 17" (entry:282). Verified: each of the five `readout.py:N` literals is a literal of the cited line, and items 12/17 do compare the corresponding literals. The `+ 16` in `readout.py:203` is labeled an inference (entry:283(b)) and item 4 does print `headerSize: 16` for that chunk and item 5 prints `node_header_size: 16`.
4. **Limitations claim** "the readout reads no compression method or flag byte itself" (entry:288): TRUE — the only `flags` reads in `readout.py` are the AXML string-pool word (`152`, `166`); no ZIP general-purpose-flag or method read exists in the file.
5. **Item 11's "the output below is the complete set"** (entry:119): TRUE for every S038 line number / enum value the entry states (§2, L1). Item 7's self-limitation ("the array layout is S038's; its source line is not among the lines item 11 prints") is also accurate — no resource-map struct line is printed.
6. **Item 15 / Reproduce consistency**: `--stdout-digest` runs the readout with `check=True` (`entry_checks.py:126/223/275`) and `ONLY` gating (`readout.py:23,27,43`) means an absent/unknown `--fact` degrades to a full dump — consistent with Q13's named unguarded clause (entry:310). The eight flags named at entry:322 all exist as `--pins --eocd --oracle --zip-layout --axml-layout --container --spec-quotes --stdout-digest`, and the seven named in items 2/11-14/16-17 are exactly those minus `--stdout-digest` (used by item 15), so entry:9's flag list is complete.

## 6. Scope, limits, tooling

- I judged citations only; I issue no Q01-Q15 decision. My evidence bears directly on Q11 (locators), Q09 (digest scoping — ten digests verified), Q14 (no prose byte count beside a hex run; the only counts are command output), Q15 (the entry states no git object id — TRUE: no 40-hex id appears in the entry; the ids in this report are mine).
- Not checked (outside the mandate): the S048 live-page re-fetch (no network fetch performed), whether `truth.json`'s declared resource ids are the framework's values (the entry does not claim they are), and the C05 README flip (the landed commit keeps `uncovered`, consistent with landing order step 1).
- Read-only git only (`show`, `archive`, `rev-parse`, `log -1`); no mutating git/jj anywhere; nothing installed or upgraded (no package, `uv`, or `npx` transaction — no tool was needed).
- Scratch `/tmp/revenger-r70-R70W2Citations/` (extracted tree, `entry.md`, `verify.py`) deleted before return; the only file I wrote is this report.
