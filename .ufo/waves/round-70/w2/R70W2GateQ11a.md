PASS — Q11a on the landed candidate bytes: every count, identifier, offset and digest in the header (lines 1-11), the Scope paragraph and items 1-9 is printed by an embedded command (24/24 blocks reproduce byte-exactly from a fresh extraction), and every one of those values was re-derived by me from the raw fixture bytes and the pinned snapshots with an independent parser; the only non-command citations are two script-local constants and two heading names, each named to a recorded file whose bytes I verified, none presented as re-derived.

seat: R70W2GateQ11a · criterion: Q11a = Q11 over entry lines 1-11 (header), 15 (Scope) and items 1-9 (entry lines 23-105)
target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`, `admission-status: candidate` (line 11), 322 lines, sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`
criterion text: `corpus/QUALITY.md:23` (Q11, supersedes Q08; reject when "a value is correct when re-derived but the entry carries no derivation, or a recorded value is presented as re-derived")
base for comparison: `3f5edbc206351232a3d2d801334dd930499ccaf5` (not needed for the decision; every value below is judged on the landed bytes)

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin cat-file -t 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd
commit
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd:corpus/knowledge/round-70-apk-axml-byte-evidence.md | sha256sum
819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31  -
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd:corpus/knowledge/round-70-apk-axml-byte-evidence.md | wc -l
322
```

All work below ran on a `git archive 17ee7f87… corpus SHONEN.md SCORECARD.md SKILL.md | tar -x` extraction in
`/tmp/revenger-r70-R70W2GateQ11a` (deleted before return). No lane file was edited; no git write was issued.

## 1. Reproduction check — the entry's own commands, re-run by me

I extracted every `$` line and the output lines that follow it from the landed bytes and diffed each against live
stdout (cwd = the extraction, `python3 -B`, exit code required 0). My harness is not the entry's gate.

```
$ python3 -B /tmp/revenger-r70-R70W2GateQ11a/diffblocks.py
commands_checked=24 mismatched=0
```

All 24 commands in the entry (the 15 in items 1-9 plus items 10-17) reproduce their embedded lines exactly,
0 missing and 0 extra, exit 0. So no embedded line in my region is drift.

## 2. Independent re-derivation of every value in the region

I wrote my own byte walker (stdlib `struct`/`zlib`/`hashlib`) over `corpus/fixtures/apk-r65/fixture.apk`; it
shares no code with `readout.py`/`entry_checks.py`. Snapshot, registry and digest values were checked separately
with `sha256sum`/`wc -c`/`sed -n`/`awk`/`grep` (item 14 digests in §3, anchor lines in §4).

```
$ python3 -B /tmp/revenger-r70-R70W2GateQ11a/indep.py
size 947 sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
eocd 925 sig 504b0506 entries 3 cd_size 188 cd_off 737 sum 925
AndroidManifest.xml lho 0 po 49 csz 416 usz 416 crc 962d075f recomp 962d075f sha 73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4
classes.dex lho 465 po 506 csz 112 usz 112 crc 2635c82a recomp 2635c82a sha 57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2
META-INF/MANIFEST.MF lho 618 po 668 csz 69 usz 69 crc e948d738 recomp e948d738 sha 2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49
chunk at 8 type 1 0x1 headerSize 28 size 196
chunk at 204 type 384 0x180 headerSize 8 size 44
resource map entries 9 ['0x0', '0x0', '0x0', '0x0', '0x0', '0x101021b', '0x101021c', '0x0', '0x0']
chunk at 248 type 256 0x100 headerSize 16 size 24
chunk at 272 type 258 0x102 headerSize 16 size 96
attrStart/Size/Count (20, 20, 3)
chunk at 368 type 259 0x103 headerSize 16 size 24
chunk at 392 type 257 0x101 headerSize 16 size 24
xml_total 416
dex magic 6465780a30333500 checksum 3d120c30 recomp 3d120c30
sha1 a5fc7bea8fa9ffaa52243540c8026066511b9fce stored a5fc7bea8fa9ffaa52243540c8026066511b9fce
file_size 112 header_size 112 endian 0x12345678
```

## 3. Value table — every number/hex/identifier in the region and the line that prints it

Entry line numbers are the landed file's. "out" = the entry line that carries the command's actual stdout.

| # | value (entry line) | printed by (entry out line) | my independent check |
|---|---|---|---|
| 1 | S038 row id, URL tag `android-15.0.0_r1`, `2026-10-24`, `round 65` (1) | provenance record, not a byte value: `corpus/SOURCES.md:52` names the same row, URL and date (`grep` below) | matches |
| 2 | `ResourceTypes.h` digest (1) | item 14 `--pins` (228) `sha256 56b88bc4…c56f 86255 bytes` | `sha256sum` = `56b88bc4…c56f`, 86255 bytes |
| 3 | S049/S043 ids (2) | provenance: `SOURCES.md:63` S049 "supersedes S043"; `SOURCES.md:57` S043 | matches |
| 4 | `first line 7` (2) | item 11 `--spec-quotes` (144) `MATCH rea-android-applications.md: first line 7 … Start with `inspect_android_package` on the caller's APK path for package` | `sed -n '7p'` prints that line |
| 5 | rea snapshot digest (2) | item 14 (231) `sha256 412d9cb4…a74c 1992 bytes` | `sha256sum` = `412d9cb4…a74c`, 1992 bytes |
| 6 | S048/S045 ids (3) | provenance: `SOURCES.md:62` S048 "supersedes S045"; `:59` S045 | matches |
| 7 | `four quoted phrases` (3) | item 11 (145-148): exactly four `MATCH dex-format.html` lines, first lines 5949/5956/5981/5035 | snapshot lines 5949/5956/5981/5035 read back as checksum/signature/header_size/ENDIAN_CONSTANT |
| 8 | dex snapshot digest (3) | item 14 (230) `sha256 c0428612…d9f4 281157 bytes` | `sha256sum` = `c0428612…d9f4`, 281157 bytes |
| 9 | S032/S034 ids, `6.3.10`, `2026-10-23`, `round 63` (4,5) | provenance: `SOURCES.md:46,:48` (row ids, 6.3.10, dates) | matches |
| 10 | `§4.3.12`, `§4.3.16`, `§4.3.7` (4,5) | item 12 `--zip-layout` (171-173): `MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399` / `4.3.12: … 511, … 522-538` / `4.3.16: … 632, … 634-646` | snapshot: 387/511/632 are those headings; 389-399 = 11 local fields, 522-538 = 17 central fields, 634-646 = 8 EOCD fields (with 4 wrapped field lines) |
| 11 | APPNOTE digest (4) | item 14 (229) `sha256 0b993022…50cd6 174585 bytes` | `sha256sum` = `0b993022…50cd6`, 174585 bytes |
| 12 | S047/S046 ids, `2026-10-25`, `round 69` (6) | provenance: `SOURCES.md:61` S047 "supersedes S046"; `:60` S046 | matches |
| 13 | derive script + snapshot digests (6) | item 14 (227,228) `74d4c0d9…3aa 4979 bytes`, `56b88bc4…c56f 86255 bytes` | `sha256sum` matches both |
| 14 | S041 id, `2026-10-24`, `round 65`, "the four digests" (7) | provenance `SOURCES.md:55`; item 14 (222-226) prints the four bundle digests plus `entry_checks.py` (226) | all five `sha256sum`s match |
| 15 | `verified-at: 2026-10-25`, `round-70` (8) | run-metadata record; the universal in the same line is tested in §1 (24/24 exact) | matches |
| 16 | item refs `2, 11-14, 16-17` (9) | each named command exists and is embedded (entry 35, 143, 155, 181, 221, 244, 253) | all run, exit 0 |
| 17 | `C05`, `candidate` (10,11) | coverage-map row + mechanical admission label (claim C1's counter reads it) | n/a to Q11 |
| 18 | Scope: `One authored APK`; "Python standard-library"; "No archive member is extracted or executed, nothing is fetched" (15) | item 1 (27) prints the single path; `readout.py:13-18` imports only `hashlib/json/struct/sys/zlib/pathlib`; `entry_checks.py:29-35` and `derive_axml_anchors.py:34-37` likewise (no network module) | verified by reading the sources |
| 19 | item 1: `947`, sha256 `05d2280f…d03e` (23,27) | item 1 (27) | §2 line 1 |
| 20 | item 2: `925`, `737`, `3`, `188`, `3`, `cd_end_equals_eocd_offset: true`; `504b0506 (4 bytes)` (30,34,36) | item 2 (34,36); `737+188=925` arithmetic on two printed fields | §2 line 2 |
| 21 | item 3: `30` in the payload formula (39) | item 12 (156) `local fixed part: 30 bytes (sum of the transcribed field widths)` and (175) `MATCH local.fixed_part: spec width 30, readout.py literal `lh_off + 30` present=True` | snapshot 4.3.7 widths sum to 30 |
| 22 | item 3: per member `cd_index`, `compressed_size`, `crc32`, `crc32_matches`, `local_header_offset`, `payload_first16_hex`, `payload_offset`, `sha256`, `uncompressed_size` (42-47) | item 3 (43,45,47) | §2 lines 3-5; `payload_offset = lho+30+name_len+extra_len` reproduces 49/506/668 |
| 23 | item 4: 6 chunk `type`/`offset`/`size`/`headerSize` rows, `xml_header_type: 3`, `xml_total_size: 416` (54,58) | item 4 (58); walk sums 8+196=204, +44=248, +24=272, +96=368, +24=392, +24=416 = member size | §2 chunk lines |
| 24 | item 4: `1 is 0x0001, 384 is 0x0180, 256 is 0x0100, 258 is 0x0102, 259 is 0x0103 and 257 is 0x0101` (54) | item 11 (132-139) prints all six hex values: `RES_STRING_POOL_TYPE : 239 = 0x0001`, `RES_XML_TYPE : 241 = 0x0003`, `RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100`, `RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100`, `RES_XML_END_NAMESPACE_TYPE : 246 = 0x0101`, `RES_XML_START_ELEMENT_TYPE : 247 = 0x0102`, `RES_XML_END_ELEMENT_TYPE : 248 = 0x0103`, `RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180` | snapshot lines 239/241/244-248/253 read back identically |
| 25 | item 4: `0x0100` shared by FIRST_CHUNK and START_NAMESPACE (54) | item 11 (134,135) | snapshot 244/245 both `0x0100` |
| 26 | item 5: six field-width lists, `total_bytes` 8/28/16/20/20/8, `attr_ext_attribute_start: 20`, `attribute_size: 20`, `node_header_size: 16`, `string_pool_header_size: 28` (63,67) | item 5 (67); item 17 (254-258) compares a second transcription to the printed widths; item 17 (260-277) compares each readout literal to the summed offset | snapshot 218/287/461/621/677/707 struct fields give the same widths |
| 27 | item 6: `flags 0x00000100`, `stringCount 9`, `stringsStart 64`, `styleCount 0`, `stylesStart 0`, 9 offsets, 9 strings (72,76) | item 6 (76); the tested mask `flags & 0x100` is `readout.py:166` (verified line content) and the mask's value appears in the same stdout as `"flags": "0x00000100"` | §2 string pool: 9 offsets, first string at 8+64+0=72 |
| 28 | item 7: `44 less 8` = `36`, `9 times 4`, `entry_count 9`, 9 ids incl. `0x0101021b`/`0x0101021c`, `offset 204` (79,83) | item 4 (58) prints 44 and 8; item 7 (83) prints entry_count 9, the nine ids and offset 204; 36/9=4 arithmetic | §2 resource map: 9 entries, same ids |
| 29 | item 8: `attributeStart 20`, `attributeSize 20`, `attributeCount 3`, three attributes' `name_index`/`ns_index`/`raw_value_index`/`data_type`/`res_id`, `16` (86,90) | item 8 (90); `16` also item 4 (58 `headerSize: 16`) and item 5 (67 `node_header_size: 16`); `readout.py:203`/`:211` verified to contain the cited expressions | §2 `attrStart/Size/Count (20, 20, 3)`; attrExt at 288 + 20 = 308, +3×20 = 368 = end-element chunk |
| 30 | item 8: `NO_INDEX 0xFFFFFFFF at readout.py:22` (86) | value in the same item's stdout as `"ns_index": 4294967295` (90); `readout.py:22` is exactly `NO_INDEX = 0xFFFFFFFF` (source locator, labeled at entry 280) | verified both |
| 31 | item 9: `checksum 0x3d120c30`, signature `a5fc7bea…9fce`, `header_size 112`, `file_size 112`, `header_bytes 112`, `endian_tag 0x12345678`, `magic_hex 6465780a30333500`, `format_version 035` (101,105) | item 9 (105); the four S048 phrases at item 11 (145-148) | §2 dex lines: adler32 and sha1 recompute equal, sizes and endian equal |
| 32 | item 9: `magic`, `format_version`, `file_size`, `header_bytes` "printed without a quoted S045 phrase" (101) | item 9 (105) prints all four; no spec credit claimed for them | matches |

No value in the region is stated in prose without an entry command printing it, with the three exceptions below —
each of which is a locator to a recorded file whose bytes I verified, not a value presented as re-derived.

## 4. Counterexample tests (the strongest ones available)

(a) **Wrong-value test.** I did not trust the readout: my independent walker (§2) reproduced all 27 container/AXML/
dex values, all ten item-14 digests and sizes (`sha256sum`/`wc -c`), and the anchor line numbers
(`ResourceTypes.h` 218/239/241/244-248/253/686/687; `rea-android-applications.md:7`; `dex-format.html` 5949/5956/
5981/5035; `APPNOTE.TXT` 387/511/632 with field lines 389-399/522-538/634-646). Zero mismatches. The r65-class
defect (an embedded value that its own command contradicts) is absent from this region.

(b) **Underived-value test.** Two script-local constants are cited to a source line instead of to a command that
prints that line: `NO_INDEX 0xFFFFFFFF` (entry 86 → `readout.py:22`) and the UTF-8 mask `0x100` (entry 72 →
`readout.py:166`). Both source lines are correct, both values appear in the same item's stdout
(`4294967295` at 90; `0x00000100` at 76), and the entry labels `readout.py:N` citations "source locators checked by
reading the file" (entry 282) — the same convention an admitted entry records for Q11
(`corpus/knowledge/round-63-zip-central-directory-evidence.md:732`: "maps every factual sentence … to a command and
a printed field **or to the recorded file named beside it**"). Smallest safe correction if the gate counts a locator
as no derivation: add one command that prints those two source lines (e.g. `sed -n '22p;166p'
corpus/fixtures/apk-r65/readout.py` with its stdout, or a `--readout-constants` flag on `entry_checks.py`). This is a
coverage gap on two constants, not a wrong value; I do not score it a FAIL because Q11's four categories are values
of the record and both values are in the printed output.

(c) **Recorded-presented-as-derived test.** The two dex-format heading names in the header (entry 3: "Items and
related structures", "Bitfield, string, and constant definitions") are printed by no embedded command. They are true
(snapshot `dex-format.html:5921` and `:4964`; the four phrase lines 5949/5956/5981 sit after 5921 and 5035 after
4964) and they are anchor text under Q02, not a count/identifier/offset/digest of a record value; the recorded file
and its digest are named (entry 3, entry 228). Smallest safe correction if anchor text is in scope: have
`--spec-quotes` print the enclosing heading line for each phrase (one extra output line per file).

(d) **Header-universal test.** Entry 1 claims "every S038 line number and enum value this entry states is printed by
the item-11 command". Every S038 number/enum the entry states is in item 11's 20-line output (`grep -noE "(line|lines)
[0-9]+"` finds only entry 2 `line 7`, the item-11 output lines 144-149 and the item-12 APPNOTE lines 171-173); the
six hex enum values in item 4 are printed at 132-139. Claim holds.

(e) **Provenance test.** Header dates/rounds/supersession resolve to the registry: `SOURCES.md` S038 `2026-10-24`
+ round 65, S032/S034 `2026-10-23` + round 63, S041 `2026-10-24` + round 65, S047 `2026-10-25` + round 69, S048/S049
`2026-10-25` + round 70; S047 "supersedes S046", S048 "supersedes S045", S049 "supersedes S043" (`SOURCES.md:57-63`).

```
$ for s in S032 S034 S038 S041 S047 S048 S049; do printf "%s: " "$s"; grep "^| $s " corpus/SOURCES.md | grep -oE "2026-10-2[0-9]" | sort -u | tr '\n' ' '; grep "^| $s " corpus/SOURCES.md | grep -oE "round[- ][0-9]+" | sort -u | tr '\n' ' '; echo; done
S032: 2026-10-23 round-63 round-70 
S034: 2026-10-23 round-63 round-70 
S038: 2026-10-24 round-65 round-70 
S041: 2026-10-24 round-65 round-70 
S047: 2026-10-25 round-65 round-69 round-70 
S048: 2026-10-25 round-70 
S049: 2026-10-25 round-70
$ grep "^| S049 " corpus/SOURCES.md | grep -o "supersedes S0[0-9]*"
supersedes S043
$ grep "^| S048 " corpus/SOURCES.md | grep -o "supersedes S0[0-9]*"
supersedes S045
$ grep "^| S047 " corpus/SOURCES.md | grep -o "supersedes S0[0-9]*"
supersedes S046
$ grep -c "6\.5\.0" corpus/snapshots/rea-android-applications.md
0   (exit 1: no match)
```

The URL tag `rea-agents-6.5.0` is a citation locator and is absent from the committed snapshot — it cannot be
byte-derived and is not presented as such.

## 5. Cross-check against wave 1 (read only after my verdict was fixed)

Wave 1's two Q11 seats judged commit `aa1842fac199aa524930e5565ed3715de5f84c6d` (273 lines, sha256 `0913f651…`), a
superseded draft — not the landed bytes (`17ee7f87…`, 322 lines, sha256 `819efcb8…`). The defects they located do
not survive on the landed bytes: the APPNOTE ranges now print heading line + first/last transcribed field line and
are complete (verified above); item 11 prints all six hex enum values (entry 132-139); the Reproduce section
(entry 322) says "eight derivation flags" and lists eight, and `entry_checks.py:297` has exactly those eight; item 14
pins `entry_checks.py` itself (entry 226); item 16 prints each member's `method` with the oracle comparison (entry 245-247); and the Observation bullet labels `readout.py:N` as source locators (entry 282). Their `rea-agents-6.5.0`
point is unchanged and remains a URL citation (item (e) above). I did not copy their findings; they are advisory and
this decision rests on my own runs in §1-§4.

## 6. Decision and impact

- **Q11a = PASS** on the landed candidate bytes. No FAIL line exists for this criterion.
- Impacted axes if a reviewer overrules §4(b)/(c): C1 only (a Q11 FAIL would be a kill-rule input, honest stop,
  README stays `uncovered`, header flips to `rejected`). The correction in both cases is text-level (one extra
  command/output block), not a value change — so the honest-stop cost would be disproportionate to the defect.
- What I did not judge: Q01-Q10, Q12-Q15, C2, C3, separability, holds. I read no wave-1 record before §1-§4 were
  complete, and I read no lane file as evidence for a value except the primary records named above.
- **Working-tree note (not my write).** At the end of my run the working tree's entry differed from the judged
  commit in exactly one line — `admission-status:` (diff stat `1 file changed, 1 insertion(+), 1 deletion(-)`,
  working-tree sha256 `53f61ffb…a152` vs committed `819efcb8…4c31`) — a flip to `rejected` citing other wave-2 seats'
  FAILs at `:119`/`:152` (items 11-12). That flip is outside my region and outside my write scope; my PASS is on the
  pinned landed bytes `17ee7f87…` and is unaffected by it.
- Tooling: nothing installed (pacman paused; no `uv`/`npx` needed). Used `python3 3.14.8` (system), `git`
  (read-only), `sha256sum`, `awk`, `grep`. No mutating git/jj command; scratch under
  `/tmp/revenger-r70-R70W2GateQ11a` removed before return.
