MATCH — `--fact eocd` re-derives byte-for-byte: exit 0, all 7 fields equal the embedded line, prose sentence contains no false statement (one clause, the signature hex, is not printed by the command but is verified true from the fixture bytes).

# R69Item2 — per-item re-derivation of the end-of-central-directory fact

Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin (HEAD `35e1258`). No file in the lane was written or edited by this seat; scratch under /tmp/revenger-r69-* was deleted after use. No tool was installed or upgraded (nothing needed: `python3` stdlib was sufficient).

## 1. Command and actual output

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
EXIT_CODE=0
```

- exit code **0**; stderr **0 bytes** (`/tmp/revenger-r69-item2-stderr.txt` was empty).
- stdout is one line, 180 bytes including the trailing newline.
- sha256 of that line: `9049be16f508804a8f33895996c18d31e59e7e277420c06812e0144a547d1c32` (two independent runs produced the same digest — deterministic).
- No stray JSON keys: exactly the 7 keys `fact` + 6 values.

Whole-script cross-check (the entry's `recheck:` claim, entry line 194):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py
exit=0 ; 15 lines
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/revenger-r69-item2-full.txt
```

The digest equals the `507d79f8…dad247` the entry quotes at line 194 and repeats at line 196-197, and the line count is the claimed 15. So the single-fact line is not an isolated survivor: the whole stdout reproduces.

## 2. The entry's embedded line and its location

- Item-2 prose: `corpus/knowledge/round-69-apk-axml-byte-evidence.md:30`
- Item-2 fenced block: command at **line 33**, embedded JSON at **line 34**
- Same line repeated inside the full-stdout transcript at **line 202**

Embedded text (line 34, verbatim):

```
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
```

Byte-exact comparison (not eyeballed): `cmp` of the actual stdout against line 34 reported only `EOF on ...-actual.txt after byte 180` — i.e. the actual 180-byte line is a byte-prefix of the 180-byte line-34 + newline stream, and `sha256sum` of `sed -n '34p'` gives the *same* `9049be16…d1c32`. Line 34 and line 202 are themselves byte-identical (the 360-byte combined extract was exactly two 180-byte copies). Verdict: **no character differs**, including key order, spacing and value spelling (lowercase `true`, no trailing spaces).

## 3. Field-by-field verdict

| # | Field in actual output | Embedded line (34 / 202) | Entry prose (line 30) | Verdict |
|---|---|---|---|---|
| 1 | `fact: "eocd"` | `"fact": "eocd"` | — (block only) | MATCH |
| 2 | `eocd_offset: 925` | `"eocd_offset": 925` | "located at file offset **925**" | MATCH |
| 3 | `total_entries_cd: 3` | `"total_entries_cd": 3` | "its record states **3** central-directory entries" | MATCH |
| 4 | `parsed_entries: 3` | `"parsed_entries": 3` | (same clause — see §5 note on aliasing) | MATCH |
| 5 | `size_of_central_directory: 188` | `"size_of_central_directory": 188` | "a central directory of **188** bytes" | MATCH |
| 6 | `offset_of_start_of_cd: 737` | `"offset_of_start_of_cd": 737` | "starting at offset **737**" | MATCH |
| 7 | `cd_end_equals_eocd_offset: true` | `"cd_end_equals_eocd_offset": true` | "`737 + 188 == 925`, so the central directory ends exactly where the end-of-central-directory record begins" | MATCH |

**Fields that differ: none (0 of 7).** Field 7's prose arithmetic is independently correct: `737 + 188 = 925`.

## 4. Does the prose state anything the output does not support?

Clause-by-clause, against the actual output:

| Prose clause (line 30) | Supported by the printed output? | Independent check |
|---|---|---|
| "end-of-central-directory signature `504b0506`" | **No** — no emitted field carries the signature bytes | fixture bytes at 925 are `50 4b 05 06` (hex `504b0506`) — **true** |
| "is located at file offset **925**" | Yes — `eocd_offset: 925` | `apk.rfind(b"PK\x05\x06")` = 925; no earlier occurrence (`rfind` over `[0,925)` = −1) |
| "its record states **3** central-directory entries" | Yes — `total_entries_cd: 3` and `parsed_entries: 3` | EOCD record decodes both `entries-this-disk` and `entries-total` as 3 |
| "a central directory of **188** bytes starting at offset **737**" | Yes — `size_of_central_directory: 188`, `offset_of_start_of_cd: 737` | struct decode at +12/+16 gives 188 / 737 |
| "`737 + 188 == 925`" | Yes — arithmetic, and `cd_end_equals_eocd_offset: true` | 925 |
| "so the central directory ends exactly where the end-of-central-directory record begins" | Yes — `cd_end_equals_eocd_offset: true` | `cd_off + cd_size = 925 = eocd_offset` |

Answer: the prose asserts **one** thing the quoted command output does not print — the signature byte string `504b0506`. It is not a false statement: I decoded the record directly from `corpus/fixtures/apk-r65/fixture.apk`, and every byte-level value the prose names is present on disk. Recorded as finding F1 (provenance wording, not a fact error).

## 5. Independent byte decode of the EOCD record (depth)

Decoded from the fixture with `struct.unpack_from("<IHHHHIIH", ...)` at offset 925 — no readout helper reused:

```
file_bytes 947
sig_at_925 504b0506
disk_no 0 cd_disk 0 n_disk 3 n_total 3 cd_size 188 cd_off 737 comment_len 0
arithmetic_737_plus_188 925
cd_end 925 eocd 925
first_sig_before_925 -1
```

Three structural corroborations the prose does not state but which hold:

1. **The record ends exactly at EOF**: 925 + 22-byte fixed record = **947** = file size, with `comment_len 0`. So nothing trails the EOCD and `eocd_offset` is not a lucky interior match.
2. **Central-directory size is explained, not just copied**: 3 records × 46-byte fixed part + 50 name bytes (`AndroidManifest.xml` 19 + `classes.dex` 11 + `META-INF/MANIFEST.MF` 20) = **188**, i.e. zero extra fields and zero per-record comments. Matches `size_of_central_directory: 188` exactly.
3. **737 is the end of the local-record chain, not a coincidence**: `payload_offset + compressed_size` per member gives 49+416 = 465, 506+112 = 618, 668+69 = **737** — the same numbers the member facts print, and the point where the central directory starts.

## 6. Why `parsed_entries` is not a tautology (invariant check)

`readout.py:86` sets `parsed_entries=total_entries`, i.e. the field is an alias of the u16 at EOCD+10, not an independent walk counter — worth naming, since a reading could otherwise treat it as a second witness. The walk is nevertheless enforced:

- `readout.py:77` — `eocd = apk.rfind(b"PK\x05\x06")` (last occurrence, as APPNOTE requires).
- `readout.py:90` — `assert apk[cursor:cursor+4] == b"PK\x01\x02"` per central-directory record.
- `readout.py:119` — `assert cursor == eocd` after three records.
- `--fact eocd` only suppresses *printing* (`emit` at readout.py:26-30), so the walk still executes; a wrong entry count would raise `AssertionError` and exit non-zero.

Exit 0 therefore proves three `PK\x01\x02` records were actually walked and ended at 925 — the "3" in the output is corroborated by the walk, not only echoed from a header field. Field widths used (`+10` entries, `+12` size, `+16` offset) are the APPNOTE EOCD layout and match the record I decoded independently.

## 7. Findings

**F1 (low, provenance wording — no fact error).** The item-2 clause "signature `504b0506`" is not printed by `--fact eocd`; the emitted fields (readout.py:81-86) carry offsets and counts only. The entry's preamble at line 19 says "Every numbered item below is produced by the readout", and item 2's signature substring is produced by the readout's *reading* (readout.py:76-77) but not by its *output*. The statement is true of the file (verified above), so this is an attribution/precision nit, not a fiction. A fix would be to add the signature field to the emit list or to word the clause as read from the fixture bytes.

**F2 (low, self-assessment enumeration — adjacent to this fact).** The Q14 row at entry line 184 lists `504b0506` among strings that "carry byte counts from their own clauses". The `504b0506` clause (line 30) states no byte count — it says only "signature … located at file offset 925" (a grep for `504b0506` returns exactly two lines: 30 and 184; neither gives a length). Under Q14's own escape ("hex without a count clause is excluded"), `504b0506` should be in the excluded set. The same loose enumeration covers `0300 0800 a001 0000`: its clause at line 52 gives headerSize 8 and total size 416, but no byte count for the quoted 8-byte run. (`6465780a30333500` is correctly covered — line 109 says "first eight bytes".) This makes Q14 more permissive than its stated rule, not the item-2 fact wrong.

## 8. Residual risk and verification gaps

- **No oracle for this fact.** `truth.json` top-level keys are `axml_declared`, `build_recipe`, `image`, `members` — it declares the image sha256/size and per-member records but **no** EOCD offset, CD size or entry count. Item 2 is therefore byte-derived only, with no authored-oracle cross-check. It is still a fact about this one authored fixture, which is exactly its declared scope; the gap matters only if a reader expects oracle agreement.
- **EOCD spec anchor is absent from the frontmatter.** S032 §4.3.12 (central directory) and S034 §4.3.7 (local header) anchor item 3, but the EOCD record layout that item 2 relies on is not covered by a cited APPNOTE section in `source:`. Layout facts are nonetheless confirmed by the independent struct decode above.
- **Signature uniqueness is empirical**, not structural: `rfind` returns 925 and no earlier `PK\x05\x06` exists in this 947-byte file, so "is located at" is unambiguous *here*; no archive-wide guarantee is claimed and none is needed.
- **Coverage note:** this seat checked only the `eocd` fact and its prose/Q14 touchpoints. The other 14 stdout lines, the AXML chunk walk and the dex header were not re-derived here (sibling seats own them); the full-stdout digest reproducing identically is the only cross-item signal I can offer.

## 9. Reproducibility of this report

All commands were run from `/home/vgpnk/Projects/shokunin/revenger-shokunin` with `python3 -B`; the script sha256 is `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`, matching the entry's S041 frontmatter anchor and line 194. `git status --porcelain` on the entry, `readout.py` and `fixture.apk` was empty at `35e1258` — no working-tree drift between the entry's build and this re-derivation.
