FAIL — Q11 fails on the header / items 1-8 / Observation text: four located defects (both APPNOTE line ranges end before the fields item 12 credits; six decimal→hex chunk-type conversions are typed, not printed; `rea-agents-6.5.0` is printed by nothing and is absent from the committed snapshot; the Observation bullet claims every value in items 1-15 is printed). All 15 embedded output blocks nevertheless reproduce byte-identically from the lane root — the defect is derivation coverage, not transcription drift.

seat: R70W1PreQ11Items1to8 · target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `aa1842fac199aa524930e5565ed3715de5f84c6d` (sha256 `0913f6515e93889a7a4204a613f52a3ff8d505742038dfa0d46443a79b088368`, 273 lines; the working tree is at that commit and `git status --porcelain` shows no modification under `corpus/`). Scope: Q11 over lines 1-11 (header), 17-98 (items 1-8 + prose) and 231-235 (Observation/inference/unknown). Every command below was re-run by me from `/home/vgpnk/Projects/shokunin/revenger-shokunin`; no file was edited.

## 1. Transcription check — 15/15 blocks reproduce, 0 missing, 0 extra

Extracted every `$` command + its expected lines from the entry bytes and diffed against live stdout (each command run as `python3 -B …` with cwd = lane root):

```
L25 readout.py --fact archive                 rc=0 OK missing=0 extra=0
L32 readout.py --fact eocd                    rc=0 OK missing=0 extra=0
L32 entry_checks.py --eocd                    rc=0 OK missing=0 extra=0
L41 readout.py --fact member[AndroidManifest.xml]  rc=0 OK missing=0 extra=0
L41 readout.py --fact member[classes.dex]     rc=0 OK missing=0 extra=0
L41 readout.py --fact member[META-INF/MANIFEST.MF] rc=0 OK missing=0 extra=0
L56 readout.py --fact axml_chunk_table        rc=0 OK missing=0 extra=0
L65 readout.py --fact spec_derived_struct_widths  rc=0 OK missing=0 extra=0
L74 readout.py --fact axml_string_pool        rc=0 OK missing=0 extra=0
L81 readout.py --fact axml_resource_map       rc=0 OK missing=0 extra=0
L88 readout.py --fact axml_start_element      rc=0 OK missing=0 extra=0
L88 readout.py --fact axml_start_namespace    rc=0 OK missing=0 extra=0
L88 readout.py --fact axml_end_element        rc=0 OK missing=0 extra=0
L88 readout.py --fact axml_end_namespace      rc=0 OK missing=0 extra=0
L103 readout.py --fact dex_declared_header    rc=0 OK missing=0 extra=0
L112 readout.py --fact jar_manifest           rc=0 OK missing=0 extra=0
L121 derive_axml_anchors.py                   rc=0 OK missing=0 extra=0
L121 entry_checks.py --spec-quotes            rc=0 OK missing=0 extra=0
L154 entry_checks.py --zip-layout             rc=0 OK missing=0 extra=0
L177 entry_checks.py --oracle                 rc=0 OK missing=0 extra=0
L211 entry_checks.py --pins                   rc=0 OK missing=0 extra=0
L226 entry_checks.py --stdout-digest          rc=0 OK missing=0 extra=0
blocks with diffs: 0
```

Independent re-derivation of the whole readout: `python3 -B corpus/fixtures/apk-r65/readout.py | wc -l` → `15`, and `entry_checks.py --stdout-digest` → `readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` = entry line 228. `--pins` reproduces all nine pins at entry lines 213-221, including `sha256 05d2280f… 947 bytes corpus/fixtures/apk-r65/fixture.apk` (item 1) and `56b88bc4… 86255 bytes corpus/snapshots/ResourceTypes.h` (item 11 first line, item 14 line 218).

Source-line locators cited in items 2-9 all resolve (`grep -n`): `readout.py:76` → `76:    sig_eocd = b"PK\x05\x06"`; `:105` → `105:        payload_off = lh_off + 30 + lh_name_len + lh_extra_len`; `:51-58` → `51:    w8, w16, w32 = 1, 2, 4` … `58:        "Res_value": [w16, w8, w8, w32],`; `:164-168` → the `emit("axml_string_pool", …)` call; `:166` → `utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),`; `:203` → `aoff = base + 16 + attribute_start + i * attribute_size`; `:211` → `"ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],`; `:22` → `NO_INDEX = 0xFFFFFFFF`; `:233-248` → the dex block; `:49-50` → the two "computed here … not assumed" comment lines. None of these line numbers is printed by any command *inside* the entry — see §4 Tier-B.

## 2. Number / hex / identifier table (scoped regions)

`printed-by` = the entry's own embedded command whose stdout contains that value (verified above).

| entry line | value | printed by (observed output) | verdict |
|---|---|---|---|
| L1 | `S038` | item 5 `"source_anchor": "S038 ResourceTypes.h struct field lists"`; item 11 line 1 `sha256 56b88bc4… ResourceTypes.h` | PASS |
| L1 | `android-15.0.0_r1` (tag in URL) | — (URL is the Q02 anchor, not a derived value) | locator |
| L1 | `2026-10-24`, `65`, `2026-10-25` | — (SOURCES.md:52 row metadata) | Tier-B (unlabeled recorded) |
| L1 | "every S038 line number and enum value … printed by the item-11 command" | item 11 prints 12 line numbers (`218,287,461,612,621,677,707,237,239,241,244,245,246,247,248,253,263,686,687`) and 8 enum values; no S038 line number is stated anywhere else in the entry | PASS (claim true) |
| L2 | `S043`, `S039` | item 11 `MATCH rea-android-applications.md: first line 7`; item 14 `412d9cb4… 1992 bytes corpus/snapshots/rea-android-applications.md` | PASS |
| L2 | `rea-agents-6.5.0` | **nothing**; `grep -c '6\.5\.0' corpus/snapshots/rea-android-applications.md` → `0` | **FAIL D3** |
| L2 | "first line 7" | item 11 `MATCH rea-android-applications.md: first line 7, folded phrase present=True` | PASS |
| L3 | "four quoted phrases" | item 11 prints exactly four `MATCH dex-format.html` lines (`5949, 5956, 5981, 5035`) | PASS |
| L4 | `6.3.10` | — (present at `corpus/snapshots/APPNOTE.TXT:2` `Version: 6.3.10`, printed by no entry command) | Tier-B |
| L4 | `§4.3.7`, `387-398` | **nothing**; snapshot has the heading at 387 and the last fixed field at **399** | **FAIL D1a** |
| L4 | `§4.3.12`, `511-531` | **nothing**; the fields item 12 credits sit at 532/533/534/538 | **FAIL D1b** |
| L4 | `§4.3.16`, `632-646` | — (range is correct: heading 632, `.ZIP file comment length 2 bytes` 646) | Tier-B (correct, unprinted) |
| L5 | `§4.3.7`, offsets 26/28 | item 12 `MATCH local.name_length: spec offset 26 …` / `MATCH local.extra_length: spec offset 28 …` | PASS |
| L6 | `S047`, `S046` | item 14 `74d4c0d9… 4979 bytes corpus/derive_axml_anchors.py` (S047's anchor) | PASS |
| L7 | "four digests" | item 14 prints exactly the four `apk-r65` pins | PASS |
| L8 | `2026-10-25`, `.ufo/waves/round-70/build-entry.py` | builder verified: `build-entry.py:27` `subprocess.run([sys.executable, "-B", *argv[2:]] …)` and `:37` `parts.append(run(c))` | PASS |
| L9 | "five `entry_checks.py` flags named in items 11-15" | items 11-15 name `--spec-quotes, --zip-layout, --oracle, --pins, --stdout-digest` = 5 | PASS |
| L10 | `C05` | — (README row id) | locator |
| L23 | `947`, `05d2280f…d03e` | item 1 `{"bytes": 947, … "sha256": "05d2280f…"}` | PASS |
| L30 | `readout.py:76`, `b"PK\x05\x06"` | locator verified by `grep -n` (§1); no in-entry print | Tier-B |
| L30 | "four signature bytes" | item 2 `eocd signature bytes at offset 925: 504b0506 (4 bytes)` | PASS |
| L36 | `925`, `504b0506`, `4 bytes` | item 2, same line | PASS |
| L39 | `readout.py:105`, `30`, `payload_offset` 49/506/668 | locator verified; `local fixed part: 30 bytes` (item 12); `"payload_offset": 49 / 506 / 668` (item 3) | PASS |
| L50 | `32`-hex, `16` bytes | **nothing** prints either count | **FAIL D5** |
| L54 | `1, 384, 256, 258, 259, 257` | item 4 `"type": 1 / 384 / 256 / 258 / 259 / 257` | PASS |
| L54 | `0x0001, 0x0180, 0x0100, 0x0102, 0x0103, 0x0101` | item 11 `enum RES_STRING_POOL_TYPE : 239 = 0x0001` … `RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180` | PASS as enum values |
| L54 | the six equalities "384 is `0x0180`" … | **nothing** prints the decimal→hex mapping | **FAIL D2** |
| L61 | `S038` | item 5 `source_anchor` | PASS |
| L63 | `readout.py:51-58` | locator verified | Tier-B |
| L63 | `8/28/20/20/16/8`, `20/20` | item 5 `"total_bytes": {"ResChunk_header": 8, "ResStringPool_header": 28, "ResXMLTree_attrExt": 20, "ResXMLTree_attribute": 20, "ResXMLTree_node": 16, "Res_value": 8}` | PASS |
| L70 | `20`, `20` | item 5 `attr_ext_attribute_start: 20`, `attribute_size: 20`; item 8 `"attributeStart": 20, "attributeSize": 20` | PASS |
| L72 | `readout.py:164-168`, `:166`, `0x100` | locators verified; item 6 `"flags": "0x00000100"` | PASS |
| L79 | `9`, `204`, "two non-zero ids" | item 7 `"entry_count": 9 … "offset": 204 … "nonzero": {"versionCode": …, "versionName": …}` (2 keys) | PASS |
| L79 | "one `uint32` per string" (element width 4) | **nothing** prints the width (`bytes_per_field` in item 5 has no resource-map entry; item 7 prints only count 9 and offset 204) | **FAIL D6** |
| L86 | `20/20/3`, `readout.py:203`, `16`, `readout.py:211` | item 8 `"attributeCount": 3, "attributeSize": 20, "attributeStart": 20`; locators verified; `16` = item 4 `"headerSize": 16` and item 5 `"node_header_size": 16` | PASS |
| L86 | `NO_INDEX 0xFFFFFFFF` | item 8 prints `"ns_index": 4294967295` (decimal only); the hex form exists only at `readout.py:22` | Tier-B |
| L233 | "every value in items 1-15 is printed by the command above it" | falsified by D1, D2, D3, D5, D6 | **FAIL D4** |
| L234 | inference (a)-(d): `16`, `readout.py:203`, item 13, item 11 | item 13 `MATCH axml.resource_ids …`; item 11 quotes; `16` printed twice | PASS |

## 3. Defects (located) and the exact corrected text

### D1a/D1b — both APPNOTE line ranges stop before the fields the entry credits (L4, and restated at L152 in item 12)

Entry L4: "§4.3.7 local file header (snapshot lines 387-398), §4.3.12 central directory file header (lines 511-531) and §4.3.16 end of central directory record (lines 632-646)". Entry L152: "the layouts are APPNOTE snapshot lines 387-398, 511-531 and 632-646".

Evidence (snapshot is pinned, `0b993022…`, item 14):

```
$ grep -n '4\.3\.7  Local file header\|4\.3\.12  Central directory structure\|4\.3\.16  End of central\|extra field length              2 bytes\|relative offset of local header 4 bytes\|\.ZIP file comment length' corpus/snapshots/APPNOTE.TXT
387:   4.3.7  Local file header:
399:      extra field length              2 bytes
511:   4.3.12  Central directory structure:
533:        extra field length              2 bytes
538:        relative offset of local header 4 bytes
632:   4.3.16  End of central directory record:
646:      .ZIP file comment length        2 bytes
```

- `387-398` ends at `file name length` (398) and therefore **excludes line 399 `extra field length 2 bytes`** — the field item 3's `payload_offset` formula uses and item 12 credits as `MATCH local.extra_length: spec offset 28`. The lane's own S034 row already says the right thing: `corpus/SOURCES.md:48` — "§4.3.7; version 6.3.10 (revised Nov 01, 2022); snapshot lines 387-399". The entry contradicts its source row by one line.
- `511-531` ends at `uncompressed size` (531). Every central field item 12 credits is **after** it: `MATCH central.name_length: spec offset 28` → line 532, `central.extra_length` (30) → 533, `central.comment_length` (32) → 534, `central.local_header_offset` (42) → 538. The 46-byte fixed part the same command sums (`central fixed part: 46 bytes`) only exists if the range runs to 538.
- No entry command prints any of these three ranges, so this is also a Q11 "value cited only to prose" case, and the value is wrong.

Smallest safe correction — L4, replace the `scope:` clause with:

> scope: the record layouts of §4.3.12 central directory file header (snapshot lines 511-538) and §4.3.16 end of central directory record (lines 632-646) for one authored ZIP archive; the §4.3.7 local file header (lines 387-399) is S034's scope and is cited on the next line; every line number above is printed by the item-12 `--appnote-lines` command; the field widths are MANUALLY transcribed in `corpus/fixtures/apk-r65/entry_checks.py` and the item-12 command sums them; no ZIP-parser or provider behavior is claimed

L152, replace "the layouts are APPNOTE snapshot lines 387-398, 511-531 and 632-646" with "the layouts are APPNOTE snapshot lines 387-399 (§4.3.7, S034), 511-538 (§4.3.12) and 632-646 (§4.3.16), printed by the `--appnote-lines` command above".

Derivation to embed (either add `--appnote-lines` to `entry_checks.py`, printing heading line + last credited field line per record with the snapshot's text, or embed the `grep -n` block above verbatim under item 12). Note for the author: the prose is generated — `.ufo/waves/round-70/build-entry.py:184` carries the same Reproduce sentence — so the repair must edit the builder's template as well as the entry, or the next rebuild re-injects the defect.

### D2 — six decimal→hex chunk-type conversions are typed, not printed (L54)

Entry L54: "The numeric `type` values are decimal here: 1 is `0x0001`, 384 is `0x0180`, 256 is `0x0100`, 258 is `0x0102`, 259 is `0x0103` and 257 is `0x0101`". Item 4 prints the decimals; item 11 prints the hex values as *enum* values; nothing prints the equality `384 = 0x0180` (the pairing is the labeled inference (a), not a printed value).

Smallest safe correction (no new command, no new number): replace with

> The numeric `type` values are decimal here (item 4); the hexadecimal renderings of those values are the enum values item 11 prints (`0x0001`, `0x0180`, `0x0100`, `0x0102`, `0x0103`, `0x0101`), and pairing a chunk's printed `type` with an enum name is the labeled inference (a) below, not a printed value.

### D3 — `rea-agents-6.5.0` (L2) is printed by nothing and is not in the committed record

Entry L2: "…per rea-agents-6.5.0". `grep -c '6\.5\.0' corpus/snapshots/rea-android-applications.md` → `0` (exit 1): the committed snapshot carries no version string, and no entry command prints one. The value is real but it is row metadata (`corpus/SOURCES.md:57`, "tag rea-agents-6.5.0 (npm package rea-agents@6.5.0)"), i.e. cited to prose — Q11 requires it be labeled recorded.

Correction — L2: "…— scope: the route-scope sentence only, what `inspect_android_package` is documented to take and return per the tag `rea-agents-6.5.0` **recorded in the S043 row** (the committed snapshot carries no version string: `grep -n '6\.5\.0' corpus/snapshots/rea-android-applications.md` prints nothing); not provider execution and not the fixture bytes …"

### D4 — the Observation bullet over-claims (L233)

Entry L233: "**Observation** — every value in items 1-15 is printed by the command above it from the committed bytes." Falsified by D1 (three line ranges, item 12), D2 (six conversions, item 4), D5 (two counts, item 3), D6 (one width, item 7).

Correction — L233: "**Observation** — every value in items 1-15 that is derived from the fixture or snapshot bytes is printed by the command above it; the values that are not printed are labeled where they are used (the recorded APPNOTE widths and snapshot line ranges in items 3/5/12, the S043 tag in the header), and the decimal→hex pairing in item 4 is the labeled inference (a)."

### D5 — the 32-hex / 16-byte counts under item 3 (L50) have no command

Entry L50: "The `payload_first16_hex` value printed for `META-INF/MANIFEST.MF` is a 32-hex-character run, which is 16 bytes". Neither `32` nor `16` is printed by any command (item 3 prints the run itself: `"payload_first16_hex": "4d616e69666573742d56657273696f6e"`). The arithmetic is right (`len(run)=32`, `len(bytes.fromhex(run))=16`); the derivation is missing. (Also Q14's clause — same sentence — so the Q14 seat's verdict should agree; the repair is one command or one deletion.)

Correction, pick one:
(a) add under item 3 `$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --payload-prefix-len` printing `META-INF/MANIFEST.MF payload_first16_hex: 32 hex chars = 16 bytes`; or
(b) delete the counts: "The `payload_first16_hex` value printed for `META-INF/MANIFEST.MF` is the first 16 payload bytes in hex, as the readout's field name states; the item-10 command prints that member's first line."

### D6 — "one `uint32` per string" (L79) width is not printed

Entry L79: "The resource-map chunk holds one `uint32` per string". The width 4 appears in no embedded output: item 5's `bytes_per_field` has no resource-map entry, item 7 prints only `"entry_count": 9` and `"offset": 204`. The width is derivable from printed values ((44 − 8) / 9 = 4, item 4's chunk row + item 7's count) but the entry does not print that step.

Correction — L79: "The resource-map chunk holds one 4-byte id per string, as its printed size implies (item 4: `"size": 44, "headerSize": 8`; item 7: `"entry_count": 9`; (44 − 8) / 9 = 4); the readout prints the ids and the non-zero entries keyed by string."

## 4. Tier-B (correct value, no in-entry derivation) — advisory, not blocking

1. L1/L2/L3/L4/L5/L6/L7 row dates, rounds and `mined`/`queued` states (`2026-10-24`, `round 65`, …): SOURCES.md metadata; none is labeled recorded. The header already labels other things "recorded"; one clause ("row metadata below is recorded from `corpus/SOURCES.md`") would cover the class.
2. L4 `6.3.10`: present at `corpus/snapshots/APPNOTE.TXT:2` (`Version: 6.3.10`) but printed by no command.
3. L4 `§4.3.16 632-646`: range correct, printed by no command (same fix as D1).
4. L86 `NO_INDEX 0xFFFFFFFF`: item 8 prints the decimal `4294967295`; the hex form is the script constant at `readout.py:22`. One clause ("`NO_INDEX` 0xFFFFFFFF at `readout.py:22`, whose decimal form item 8 prints as 4294967295") closes it.
5. All `readout.py:NNN` locators (L30, L39, L63, L72, L86, L234): every one resolves (verified, §1) but no in-entry command prints the line numbers. Either add a `--source-lines` check or state that locators are checked by the Q13 clause rather than derived.

## 5. Adjacent defects outside my slice (for the coordinating seat)

- **Header L4 over-credits §4.3.7 to S032.** `corpus/SOURCES.md:46` (S032) credits "§4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22" and its scope column says "central directory file header and end-of-central-directory record field layout" — no §4.3.7, no snapshot line range. §4.3.7 belongs to S034 (`SOURCES.md:48`). Q01-flavored; my D1a correction removes §4.3.7 from the S032 clause anyway.
- **Reproduce (L273) counts six flags as five.** "The five derivation flags are `--pins`, `--eocd`, `--oracle`, `--zip-layout`, `--spec-quotes` and `--stdout-digest`" — six names. Header L9's "five … named in items 11-15" is correct because `--eocd` lives in item 2. The same sentence is in the builder (`build-entry.py:184`), so fix both.
- Reproduce L273 is outside my assigned regions; I report it only because it is a count in generated prose next to my slice.

## 6. Verdict on my scope

Q11 over the header, items 1-8 and the Observation/inference text: **FAIL** (D1-D6). Everything printed is exact — 22/22 commands, 0 missing/extra lines, all digests and pins re-derived — so the repairs are text-level (plus one `entry_checks.py` flag and the builder template), not re-measurement.

No tool installed or upgraded (pacman paused; Python stdlib only). Scratch used: `/tmp/revenger-r70-R70W1PreQ11Items1to8/` (deleted before returning). No file in the lane was written except this report.
