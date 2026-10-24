FAIL — internal consistency of the candidate entry breaks in three material places (a cited `### Code` block and a "15-line stdout reproduced there" that do not exist in §Reproduce; "attributeCount 3 — all equal to the derived sizes"; a self-contradictory regeneration sentence), while every one of the printed numeric values in items 1-10 agrees with its JSON and with `truth.json` on the enumerated shared fields.

Seat: R65EntryQmapDraft, internal-consistency audit only (no Q01–Q13 decision, no fresh-seat pass claimed).
Target: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md` (162 lines, 20754 bytes) vs `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/truth.json` (103 lines, 2466 bytes).
Mode: read-only. `readout.py` was NOT executed (no re-derivation, no execution evidence manufactured); the entry's stdout hash `507d79f8…` is reported below only as the entry's own claim, not as observed output.

## Method and read-only proofs

```
$ wc -l -c corpus/knowledge/round-65-apk-axml-byte-evidence.md corpus/fixtures/apk-r65/truth.json
  162 20754 corpus/knowledge/round-65-apk-axml-byte-evidence.md
  103  2466 corpus/fixtures/apk-r65/truth.json
$ grep -n '^#' …/round-65-apk-axml-byte-evidence.md
9,13,119,123,129,133,137,154   # no `### Code` heading exists anywhere in the file
$ grep -n '^```' …/round-65-apk-axml-byte-evidence.md
21,24,…,117 (json fences), 158,160 (the only fence in §Reproduce: ```sh)
$ grep -c '"fact":' …/round-65-apk-axml-byte-evidence.md
15
$ sha256sum corpus/fixtures/apk-r65/{fixture.apk,truth.json,generator.py,readout.py}
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  truth.json
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  readout.py
```
All four digests equal the values the entry records (entry:3 for the bundle, entry:5/entry:162 for `readout.py`). `fixture.apk` is 947 bytes on disk. So the entry's file-level provenance resolves even where its in-document pointer does not (finding F1).

## Findings (verbatim, with file:line)

### F1 (material) — entry:15 cites a `### Code` block and a "full 15-line stdout reproduced there"; §Reproduce (entry:154-162) contains neither

Verbatim, entry:15:

> Every numbered item below is produced by the readout in §Reproduce. The command is given with the output it printed; the script is the `### Code` block of that section, saved verbatim as `corpus/fixtures/apk-r65/readout.py`, and the same lines appear in the full 15-line stdout reproduced there.

Evidence:
- The file's only headings are at lines 9, 13, 119, 123, 129, 133, 137, 154 (`grep -n '^#'`). There is no `### Code` heading, and no Python code fence anywhere in the file.
- §Reproduce is lines 154-162: `## Reproduce` (154), prose (156), one ```sh fence (158-160) holding only `python3 -B corpus/fixtures/apk-r65/readout.py`, then the summary paragraph (162). No code body, no 15-line stdout block.
- The 15 fact lines do exist, but are scattered through §Observation at lines 23, 30, 37, 39, 41, 50, 59, 68, 75, 82, 89, 96, 98, 107, 116 (`grep -n '"fact":'` = exactly these 15) — never contiguously "reproduced" in §Reproduce, and never as one stdout block anywhere.

Consequence: the sentence a reader would use to locate the deriving script body and the stdout whose SHA-256 the header pins (entry:5) is false about the document's own contents. The values stand on the file `corpus/fixtures/apk-r65/readout.py` (digest matches, entry:162), so this is a broken internal reference, not a fabricated value. It is still a contradiction inside the entry, and it is the one a Q11/Q02 reviewer reads first.

### F2 (material) — entry:78: "attributeCount **3** — all equal to the derived sizes of item 5"

Verbatim, entry:78:

> The start-element chunk at offset 272 names the element `manifest` with no namespace, `attributeStart` **20**, `attributeSize` **20**, `attributeCount` **3** — all equal to the derived sizes of item 5.

Evidence: item 5's printed `total_bytes` (entry:59) are `ResChunk_header 8`, `ResStringPool_header 28`, `ResXMLTree_attrExt 20`, `ResXMLTree_attribute 20`, `ResXMLTree_node 16`, `Res_value 8`. No derived width is 3; `attributeCount` is a count, not a size. Only the first two values (20, 20) equal item-5 derived sizes, as entry:62 says correctly ("the derived 20-byte `ResXMLTree_attrExt` size is the `attributeStart` value … and the derived 20-byte `ResXMLTree_attribute` size is the observed `attributeSize`"). The universal "all" is false for the third value. The JSON at entry:82 does carry `"attributeCount": 3`, `"attributeSize": 20`, `"attributeStart": 20`, so the values themselves are printed and true; the prose quantifier is the defect.

### F3 (material) — entry:121: the regeneration sentence contradicts itself

Verbatim, entry:121 (final sentence):

> Regenerating the fixture from `generator.py` in a scratch directory on this host (Python 3.14.8) reproduced `fixture.apk` byte-for-byte and `truth.json` up to its embedded `python_version` field, which the same interpreter leaves identical.

Evidence: "up to its embedded `python_version` field" asserts a residual difference in exactly that field; the relative clause "which the same interpreter leaves identical" asserts there is none. `truth.json:67` records `"python_version": "3.14.8"`, equal to the interpreter named in the same sentence — so the hedge is both unnecessary and, read literally, contradicted by the oracle itself. Either the regeneration reproduced `truth.json` exactly (drop "up to…"), or it did not (then "leaves identical" is wrong). This is a wording contradiction, not a numeric one; no `truth.json` value conflicts with the readout.

### F4 (minor) — entry:75: two renderings of the same hex id inside one output line

Verbatim, entry:75:

> `… "ids": ["0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x00000000", "0x0101021b", "0x0101021c", "0x00000000", "0x00000000"], "nonzero": {"versionCode": "0x101021b", "versionName": "0x101021c"}, "offset": 204}`

`ids[5]` renders `0x0101021b`; `nonzero.versionCode` renders `0x101021b` (leading zero dropped). Same integer, two spellings. Prose entry:71 uses `0x0101021b`/`0x0101021c` and therefore matches `ids` but not `nonzero`. Cosmetic only; no value error.

### F5 (minor) — entry:131: "no data descriptors" is carried by no Observation item

Verbatim, entry:131:

> The container is ZIP_STORED with no data descriptors, so the byte walk does not exercise split archives, spanned records or compression.

`ZIP_STORED` is corroborated (items 3's `compressed_size == uncompressed_size` for all three members, entry:37/39/41; `truth.json:51` container `zipfile.ZipFile(ZIP_STORED)`, `truth.json:79,88,97` `"method": 0`). "no data descriptors" is not: no item prints the ZIP general-purpose-bit flag or any field asserting descriptor absence; it is only inferable from `payload_offset == local_header_offset + 30 + len(name)` arithmetic that the entry never states. The Limitations claim therefore reaches past the Observation items on this one property.

### F6 (traceability note, no value conflict) — entry:33: "the walk's end cursor equals the end-of-central-directory offset"

Verbatim, entry:33 clause: "…and the walk's end cursor equals the end-of-central-directory offset". The three member JSON lines under item 3 (entry:37, 39, 41) contain no cursor field. The supporting printed field is item 2's `"cd_end_equals_eocd_offset": true` (entry:30) with `offset_of_start_of_cd 737 + size_of_central_directory 188 == 925`. The claim is true and derivable, but it is evidenced by item 2's output, not by the item-3 walk whose output line it is attached to. No rerun needed; noted for pointer hygiene only.

## Verified consistent (prose value vs the JSON printed beneath it)

Each line: claim (entry line) → printed value (entry line) → arithmetic/ambiguity check. All pass; no numeric contradiction found.

1. archive 947 bytes / `05d2280f…` (19) → `bytes 947`, same sha256 (23) → matches `truth.json:71-72` (`size 947`, same digest) and on-disk `stat` 947 / `sha256sum`.
2. EOCD at 925, 3 entries, CD 188 bytes at 737, `737+188==925` (26) → `eocd_offset 925`, `parsed_entries 3`, `total_entries_cd 3`, `size_of_central_directory 188`, `offset_of_start_of_cd 737`, `cd_end_equals_eocd_offset true` (30). Cross-check: 925+22-byte EOCD = 947 file size; 3×46-byte CD records + 19+11+20 name bytes = 188 CD size.
3. Member walk: local header 30 + name; payload offsets 49/506/668; next header = payload+size (0+49+416=465; 465+41+112=618; 618+50+69=737=CD start). Printed: `payload_offset` 49/506/668, `local_header_offset` 0/465/618, `uncompressed_size`=416/112/69, `crc32_matches true` ×3 (37/39/41). Prose "every member's stated CRC-32 equals the CRC-32 recomputed" (33) holds.
4. AXML header `0300 0800 a001 0000` → type 3, headerSize 8, total 0x1a0=416 (entry:46 vs 37 hex and 50 table). Chunk chain 8+196=204, +44=248, +24=272, +96=368, +24=392, +24=416 = `xml_total_size 416` with `xml_total_size_equals_member true` (50). Hex names 0x0001/0x0180/0x0100/0x0102/0x0103/0x0101 match printed types 1/384/256/258/259/257; headerSize column 28,8,16,16,16,16 matches printed.
5. Field-width sums equal printed `total_bytes`: [2,2,4]=8; [2,2,4,4,4,4,4,4]=28; [4,4,2,2,2,2,2,2]=20; [4,4,4,2,1,1,4]=20; [2,2,4,4,4]=16; [2,1,1,4]=8 (59). `attr_ext_attribute_start 20` = item-8 `attributeStart`; `attribute_size 20` = item-8 `attributeSize`.
6. String pool: `stringCount 9`, `styleCount 0`, `flags 0x00000100`, `stringsStart 64`, 9 strings in the stated order, offsets [0,10,55,66,76,94,108,122,126] and each offset+len(prefix+payload)+pad equals the next; last string 126+5=131 ≤ 196-64=132 (68). Prose "9 strings, 0 styles, 0x00000100, data 64 bytes in" (64) matches.
7. Resource map: 44 = 8 header + 9×4; seven `0x00000000`; `0x0101021b` at idx 5 and `0x0101021c` at idx 6 = strings 5 (`versionCode`) and 6 (`versionName`); `entry_count 9` (75). Prose "seven entries … versionCode/versionName" (71) matches. Item-8 `res_id` 16843291/16843292 = those hex ids.
8. Start element: `element_name "manifest"` (string idx 2), `element_ns null`, `element_ns_index 4294967295`, 3 attributes with name_index 3/5/6, raw_value_index 4/7/8, ns_index 4294967295/0/0, res_id 0/16843291/16843292, data_type 0x03/0x10/0x03, value_size 8 (82). Prose (78) matches every one; string inds resolve against item 6 (`package`, `com.example.r65`, `versionCode`, `versionName`, `1`, `1.0`).
9. Start namespace at 248: prefix_index 0 = `android`, uri_index 1 = `http://schemas.android.com/apk/res/android` (entry:89); end element at 368 name_index 2 = `manifest` (entry:96); end namespace at 392 same pair (entry:98); lineNumber 1 on all four node chunks as printed (82, 89, 96, 98).
10. dex: first16 `6465780a30333500300c123da5fc7bea` → magic hex matches prose `6465780a30333500`; LE checksum bytes 30 0c 12 3d = `0x3d120c30` = declared and recomputed; signature starts `a5fc7bea` in the same hex and in `signature_sha1`/`signature_recomputed`; `file_size 112 = header_size 112` supports "header only" (item 9 / 107).
11. MANIFEST.MF: `bytes 69`, `section_count 1`, first line `Manifest-Version: 1.0` (116) matches member size 69 and first16 hex `4d616e69…` = "Manifest-Version".

## §Comparison with the oracle — checked against `truth.json`

Enumerated shared fields in entry:121 all agree:
- image sha256/size → `truth.json:71-72` identical.
- members' `local_header_offset` 0/465/618 → `truth.json:78,87,96`; `crc32` 962d075f/2635c82a/e948d738 → `truth.json:77,86,95`; uncompressed sizes 416/112/69 → `truth.json:82,91,100`; member `sha256` values → `truth.json:81,90,99` (also agree, though not enumerated).
- nine strings → `truth.json:37-46` identical order/content.
- three attribute rows → `truth.json:3-25` `name_idx 3/5/6`, `ns_idx 4294967295/0/0`, `data_type 3/16/3`, `raw_value_idx 4/7/8`, `data 4/1/8`, all equal to item 8's printed values.
- two non-zero resource ids → `truth.json:26-36` identical list.

No shared-field value conflicts. The only defect in this section is the wording of F3 (entry:121). Note `truth.json:70` `"path": "fixture.apk"` vs the readout's repo-relative `path` (entry:23) differ as strings but denote the same file from different bases and are not in the enumerated comparison set; not counted as a conflict.

## §Limitations vs what Observation actually claims

- "single element with three attributes", "no nested elements" — backed: exactly one start-element chunk (type 258) and one end-element chunk (type 259) in the six-chunk table (entry:50), `attributeCount 3` (entry:82).
- "UTF-8 string pool only", "no styles" — backed: `flags 0x00000100`, `utf8 true`, `styleCount 0`, `stylesStart 0` (entry:68).
- "no CDATA" — backed: the chunk table enumerates all six child chunks and none is `0x0104`.
- "dex member is a header only" — backed: `file_size 112 == header_size 112` (entry:107).
- "ZIP_STORED" — backed by compressed==uncompressed (entry:37/39/41) and `truth.json:51,79,88,97`.
- "no data descriptors" — NOT backed by any item's output (F5).
- "intentionally not a valid dex program", generalization caveat — intent/scope statements; consistent with §Observation/inference/unknown (entry:125-127) and not contradicted internally.

## Gates / claims

- No Q01–Q13 pass is claimed here; this seat's finding is only "the entry is not internally consistent as written". Admission under the frozen order (`reports/round-65/claims.md` §Admission order step 2) is a named fresh-seat decision; this audit neither substitutes for nor pre-empts it.
- C1/C2 after-state labels were not measured by this seat (no commit, no counter run); nothing here modifies coverage or calibration status. `README` C05 is untouched (entry:7 still `admission-status: candidate`).
- The three material findings (F1-F3) are prose/pointer-level: none requires a new measurement, a re-run of `readout.py`, or a fixture change. F2/F3 are single-clause edits; F1 needs the referenced `### Code` body and 15-line stdout either inserted into §Reproduce or the sentence rewritten to point at the file path plus the distributed fact lines.

## Out of scope (not audited, reported as dependencies)

- Source anchoring: S038 anchor lines 218/239-250/461/612/621/677/707/287, S032 §4.3.12 and S034 §4.3.7 section numbers — registry/snapshot checks, not internal consistency.
- The regeneration claim itself (entry:121 / verified-at entry:4): an execution claim this seat did not reproduce; only its wording was audited (F3).
- The `recheck:` stdout digest `507d79f8…` (entry:5, entry:162) and "Exit 0; 15 stdout lines": not re-executed. Internal coherence of the count was checked (15 printed `"fact":` lines = 15 claimed stdout lines).
- §§Q-map rows (entry:137-152), §Cross-lane scope note (entry:133-135), `claims.md`, `measure.py`, `measure-before.log`, README/SOURCES/lesson surfaces — outside this seat's audit scope and untouched.
- S039/snapshot digests and `.ufo/waves/round-65/source-snapshots/*` — not read.

## Touched surfaces

- Wrote only this file: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/R65EntryQmapDraft.md`.
- No git/jj command run; no file under `corpus/`, `reports/`, `LOG.md`, `SCORECARD.md`, `SHONEN.md` was modified; no tool installed or upgraded (nothing needed).
- `readout.py` not executed; no production code, judge, or commit touched.

## Artifact / evidence paths

- Entry under audit: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md` (lines 15, 33, 71, 75, 78, 121, 131, 154-162 cited).
- Oracle: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/truth.json` (lines 3-25, 26-36, 37-46, 51, 67, 69-72, 77-100 cited).
- Fixture bundle digests: `fixture.apk` 05d2280f… (947 B), `truth.json` 27303bae…, `generator.py` eaa9444c…, `readout.py` 92e347c3… — all matching entry:3/5/162 as recorded.
- Frozen contract read for context: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md`.
