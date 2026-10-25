MATCH — the entry's end-of-central-directory fact line reproduces byte-for-byte (all 7 fields) and the prose sentence states nothing the output does not support.

Seat: L1Revenger68.R68Item2 (leaf, independent re-derivation of item 2 / C05 evidence, read-only on corpus).

## 1. Command and actual output

Lane root: `/home/vgpnk/Projects/shokunin/revenger-shokunin`

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
EXIT=0
```

Per-member runs (quoted so the shell cannot expand `[...]`; one stdout line each, all exit 0):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py '--fact' 'member[AndroidManifest.xml]'
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
EXIT=0
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[classes.dex]'
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
EXIT=0
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
EXIT=0
```

Process note (my own command error, not an entry defect): my first batch ran the member form as a bare positional — `readout.py "member[$m]"` without `--fact`. `readout.py:43` only sets `ONLY` when `--fact` is present, so that run printed all 15 facts. It is a superset, not a contradiction, and the corrected quoted `--fact` invocations above are the ones compared below.

Full-run corroboration of the entry's Reproduce block (`round-68-apk-axml-byte-evidence.md:194`):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r68i2_full.out
EXIT=0; 15 lines; sha256 = 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247; stderr 0 bytes
```

This equals the entry's claimed `15 stdout lines` / `507d79f8…dad247` exactly. Script identity also re-verified: `sha256sum corpus/fixtures/apk-r65/readout.py` = `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`, matching the entry's `:194` claim; `fixture.apk` sha256 = `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (947 bytes), matching the entry's `:21` claim.

## 2. The entry's embedded line(s)

Same fact line appears twice, both with the claimed command:

- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:31-32` — item 2 block, command at `:31`, line at `:32`.
- `corpus/knowledge/round-68-apk-axml-byte-evidence.md:202` — Reproduce full-stdout block (`:195`–`:211`).

```
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
```

Exact-string comparison (python `==`, not visual): `entry:32 == actual stdout line 3` → **True**; `entry:202 == actual stdout line 3` → **True**. Member lines `:39/:41/:43` and their duplicates `:203/:204/:205` likewise `True` against actual lines 4/5/6.

## 3. Field-by-field verdict (eocd fact, 7 fields)

| field | entry value | actual value | verdict |
|---|---|---|---|
| `cd_end_equals_eocd_offset` | `true` | `true` | MATCH |
| `eocd_offset` | `925` | `925` | MATCH |
| `fact` | `"eocd"` | `"eocd"` | MATCH |
| `offset_of_start_of_cd` | `737` | `737` | MATCH |
| `parsed_entries` | `3` | `3` | MATCH |
| `size_of_central_directory` | `188` | `188` | MATCH |
| `total_entries_cd` | `3` | `3` | MATCH |

Zero differing fields. Key sets identical (7 keys, none extra/missing).

## 4. Independent re-derivation (not using readout.py)

Manual `struct.unpack_from('<IHHHHIIH', b, 925)` over `corpus/fixtures/apk-r65/fixture.apk`:

```
filesize 947  sha256 05d2280f…afe7d03e
rfind EOCD sig PK\x05\x06 at 925  raw 504b0506
{"sig":"0x6054b50","this_disk":0,"cd_disk":0,"entries_this_disk":3,"entries_total":3,
 "cd_size":188,"cd_offset":737,"comment_len":0,"eocd_record_bytes":22,
 "eocd_end":947,"cdoff_plus_cdsize":925,"equals_eocd":true}
CD sig at cdoff: 504b0102
```

Raw bytes (`xxd -s 925 -l 22`): `504b 0506 0000 0000 0300 0300 bc00 0000 e102 0000 0000` → sig `50 4b 05 06`, this-disk 0, cd-disk 0, entries-on-disk 3, total 3, CD size `0xbc`=188, CD offset `0x2e1`=737, comment len 0.
`xxd -s 737 -l 16` → `504b 0102 …` (central-directory header signature at the stated offset).
Signature uniqueness: `PK\x05\x06` occurs exactly once in the file (offset 925), so `rfind` and `find` agree and the prose's "is located at file offset 925" is unambiguous. `925 + 22 = 947 = filesize`, trailing bytes 0 — the EOCD record ends at EOF.

Every readout field is reproduced by an independent parse of the bytes. The fact is grounded, not merely self-consistent.

## 5. Prose judgement — entry line 28

Sentence: *"The end-of-central-directory signature `504b0506` is located at file offset **925**; its record states **3** central-directory entries, a central directory of **188** bytes starting at offset **737**, and `737 + 188 == 925`, so the central directory ends exactly where the end-of-central-directory record begins."*

| prose claim | supported by output? | basis |
|---|---|---|
| signature `504b0506` at offset 925 | YES (indirect) | `eocd_offset: 925`; offset is produced by `readout.py:79-80` (`apk.rfind(b"PK\x05\x06")`), so the field is by construction the signature offset. The literal `504b0506` is **not** a printed field — I confirmed it by hexdump instead. Not a falsity; a printed-field gap. |
| record states 3 central-directory entries | YES | `total_entries_cd: 3` (u16 at eocd+10, APPNOTE 4.3.16 total-entries field) |
| central directory 188 bytes | YES | `size_of_central_directory: 188` |
| starts at offset 737 | YES | `offset_of_start_of_cd: 737` |
| `737 + 188 == 925` | YES | boolean `cd_end_equals_eocd_offset: true` encodes exactly this predicate |
| CD ends exactly where EOCD begins | YES | same boolean, true |

**No prose clause is unsupported or contradicted.** The sentence adds no numeric value absent from the output and makes no causal claim beyond the arithmetic the boolean already encodes.

## 6. Observations (evidence-strength notes, none a MISMATCH)

1. `parsed_entries` is not an independently counted number — `readout.py:85` emits `parsed_entries=total_entries`, i.e. a copy of the declared value. It is *validated* later by `readout.py:118` `assert cursor == eocd`, which forces the loop to consume the CD span exactly, but the emitted field itself overstates what was measured. The prose does not lean on it, so this is a Q08/Q06-class naming note, not a defect in item 2's text.
2. Three EOCD fields are never read or printed: entries-on-this-disk (eocd+8, actual 3), disk numbers (eocd+4/+6, both 0), and comment length (eocd+20, actual 0). The readout also never asserts `eocd + 22 + comment_len == filesize`. All three are benign here (single-disk, no comment, verified independently by me), but the entry asserts nothing about them — an omission, not a false claim.
3. The prose's "signature `504b0506`" is byte-order-correct for the stored little-endian `50 4b 05 06`; the readout's constant is `b"PK\x05\x06"`, consistent.

## 7. Bounds compliance

No file outside this report was written. No edits to `corpus/`, `reports/`, `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `.git`, the jj state or the Git index; no git/jj mutation; `/home/vgpnk/Projects/shokuknow` untouched; `corpus/live/` and `corpus/fixtures/` read-only (fixture bytes only read, never modified — `fixture.apk` sha256 re-confirmed unchanged at `05d2280f…afe7d03e`). No subagents spawned, no background jobs, no peer messages.

Tooling: nothing installed or upgraded; no pacman/uv/npx transactions were needed or attempted.

Verdict restated: **MATCH** — 7/7 fields identical at entry lines `:32` and `:202`, prose at `:28` fully supported, independently re-derived from raw bytes.
