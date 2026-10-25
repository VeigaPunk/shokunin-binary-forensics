MATCH — item 3's three embedded `member[...]` lines reproduce byte-identically (11/11 fields each, 0 diffs, exit 0), and every clause of the item-3 prose sentence is supported by the observed output, the readout's own assert, or an independent byte walk; three wording/precision notes below are hardening, not defects.

# Seat
R68Item3 — independent re-derivation of entry item 3 (the three central-directory members), read-only. No file written except this report. No tool installed or upgraded (no pacman/uv/npx used).

# Anchor bytes (all read-only)
| artifact | sha256 |
|---|---|
| `corpus/fixtures/apk-r65/readout.py` | `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` (matches entry:194) |
| `corpus/fixtures/apk-r65/fixture.apk` | `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` |
| `corpus/knowledge/round-68-apk-axml-byte-evidence.md` | `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b` |
| `.ufo/waves/round-63/source-snapshots/appnote.txt` | `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` (= S034's recorded digest) |

# Command and actual output
Lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`, three separate invocations (as the entry does):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[AndroidManifest.xml]
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
exit 0
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[classes.dex]
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
exit 0
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[META-INF/MANIFEST.MF]
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
exit 0
```

Determinism: stdout sha256 prefix identical across two runs for each of the three facts (`a3cb2dce30ab65de`, `259eb381ffe35bb2`, `61558db742cbb0e5`).
Full run: exit 0, **15** stdout lines, sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — equal to entry:7 and entry:194.

# Field-by-field comparison against the entry
Entry block: `corpus/knowledge/round-68-apk-axml-byte-evidence.md:38` (cmd) / `:39` (JSON), `:40`/`:41`, `:42`/`:43`. Prose sentence: `:35`.

| field | AndroidManifest.xml (entry:39) | classes.dex (entry:41) | META-INF/MANIFEST.MF (entry:43) |
|---|---|---|---|
| `cd_index` | 0 = 0 ✓ | 1 = 1 ✓ | 2 = 2 ✓ |
| `compressed_size` | 416 ✓ | 112 ✓ | 69 ✓ |
| `uncompressed_size` | 416 ✓ | 112 ✓ | 69 ✓ |
| `crc32` | `962d075f` ✓ | `2635c82a` ✓ | `e948d738` ✓ |
| `crc32_recomputed` | `962d075f` ✓ | `2635c82a` ✓ | `e948d738` ✓ |
| `crc32_matches` | true ✓ | true ✓ | true ✓ |
| `fact` | `member[AndroidManifest.xml]` ✓ | `member[classes.dex]` ✓ | `member[META-INF/MANIFEST.MF]` ✓ |
| `local_header_offset` | 0 ✓ | 465 ✓ | 618 ✓ |
| `payload_first16_hex` | `03000800a001000001001c00c4000000` ✓ | `6465780a30333500300c123da5fc7bea` ✓ | `4d616e69666573742d56657273696f6e` ✓ |
| `payload_offset` | 49 ✓ | 506 ✓ | 668 ✓ |
| `sha256` | `73d1e0f2…9fae4` ✓ | `57cfe887…548c2` ✓ | `2e5da249…7c0a49` ✓ |

Programmatic check (parse entry line at 39/41/43, parse fresh stdout, compare key set): **11 keys each, 0 differing keys, full-line string equality True** for all three. Verdict per member: **MATCH**.

Independent corroboration of the same numbers, from raw bytes with a separate walker (no readout.py):
```
eocd 925 cd_off 737 cd_size 188 entries 3 filesize 947
[0] PK\x01\x02 AndroidManifest.xml  cd_namelen=19 cd_extralen=0 cd_commentlen=0 method=0
    lho=0   lh_namelen=19 lh_extralen=0 payload_offset=49  (0+30+19+0) crc 962d075f match=True csz=416 usz=416
[1] PK\x01\x02 classes.dex           cd_namelen=11 cd_extralen=0 cd_commentlen=0 method=0
    lho=465 lh_namelen=11 lh_extralen=0 payload_offset=506 (465+30+11+0) crc 2635c82a match=True csz=112 usz=112
[2] PK\x01\x02 META-INF/MANIFEST.MF  cd_namelen=20 cd_extralen=0 cd_commentlen=0 method=0
    lho=618 lh_namelen=20 lh_extralen=0 payload_offset=668 (618+30+20+0) crc e948d738 match=True csz=69 usz=69
walk_end_cursor 925 eocd 925 equal True
```
Oracle cross-check: all three rows (local_header_offset, compressed/uncompressed size, crc32, sha256) equal `corpus/fixtures/apk-r65/truth.json.members[]` — supports entry:152's claim for these members.

# Prose judgment (`:35`) — clause by clause
Sentence: "Walking the three central-directory records (46-byte fixed part per S032 §4.3.12) and their local headers (30-byte fixed part per S034 §4.3.7) selects three members; every member's stated CRC-32 equals the CRC-32 recomputed over its payload bytes, and the walk's end cursor equals the end-of-central-directory offset. Each member's `payload_offset` is derived by the readout as `local_header_offset + 30 + name_length + extra_length` from the S034 §4.3.7 field list (readout.py:99-105), not assumed:"

| clause | supported? | evidence |
|---|---|---|
| three CD records select three members | yes | 3 emitted lines `cd_index` 0/1/2; independent walk hits exactly 3 `PK\x01\x02` records and lands on EOCD; `eocd` fact `parsed_entries`/`total_entries_cd`=3 |
| 46-byte fixed part, S032 §4.3.12 | yes | snapshot `appnote.txt:511-539` field list sums to 46 (4+2+2+2+2+2+2+4+4+4+2+2+2+2+2+4+4); readout asserts `PK\x01\x02` and advances `46+name+extra+comment` (readout.py:96); S032 row `corpus/SOURCES.md:46` names §4.3.12 and the 46-byte record |
| 30-byte fixed part, S034 §4.3.7 | yes | snapshot `appnote.txt:387-399` is exactly §4.3.7 and sums to 30 (4+2+2+2+2+2+2+4+4+4+2+2), with crc-32 at +14, compressed +18, uncompressed +22, name len +26, extra +28 — the exact offsets readout.py:99-105 reads; S034 row `SOURCES.md:48` records this digest `0b99302…` |
| every member's stated CRC-32 == recomputed over payload | yes | `crc32_matches:true` and `crc32 == crc32_recomputed` in all three lines; my own walker recomputed all three independently |
| walk's end cursor == EOCD offset | yes, but not as an emitted field | readout.py:119 `assert cursor == eocd, (cursor, eocd)`; the commands exited 0, so the assert held; my independent walk gives cursor=925=eocd. Nearest emitted field is `eocd.cd_end_equals_eocd_offset` (a different quantity: `cd_off+cd_size==eocd`, also true) — see note N1 |
| `payload_offset = local_header_offset + 30 + name_length + extra_length` | yes | readout.py:105 is literally `payload_off = lh_off + 30 + lh_name_len + lh_extra_len`; cited range 99-105 covers 99 (`lh_name_len`), 100 (`lh_extra_len`), 103 (`lh_name`), 105 (`payload_off`) — the range is accurate; arithmetic holds per member: 49=0+30+19+0, 506=465+30+11+0, 668=618+30+20+0 |
| "not assumed" | yes | every offset is read from the archive's own fields; no constant payload offset appears in the source |

Nothing in the output contradicts the prose, and nothing in the prose outruns what the bytes show.

# Findings (none blocking)
- **N1 (precision, low).** The walk-cursor clause has no emitted field; it is carried by the assert at `readout.py:119` plus exit 0, and the nearest printed analogue (`cd_end_equals_eocd_offset`) measures `cd_off+cd_size`, not the record walk. Both are true here, so the claim stands, but a reader cannot verify it from the item-3 block alone. Cheapest fix at the next admission pass: print `walk_end_cursor`/`walk_end_equals_eocd` in the `eocd` fact, or name the assert in the prose.
- **N2 (precision, low).** "its stated CRC-32" is the **local header's** crc-32 (`readout.py:102`, `lh_off+14`). The central directory's own crc-32 (offset 16 per §4.3.12, `appnote.txt` field list) is never read: `grep -c "cursor + 16\|cursor + 20\|cursor + 24"` on readout.py = 0. So no CD-vs-LH CRC cross-check is performed (none is claimed). Wording is defensible because the sentence's own citation is S034 (local header), but "its local header's stated CRC-32" would remove the ambiguity.
- **N3 (precision, low).** "`name_length` + `extra_length`" does not say *which* header's lengths; the code uses the local header's (`lh_name_len`/`lh_extra_len`). Here CD and LH lengths coincide (19/11/20 and 0/0/0), so the sentence is unfalsified on this fixture, but a fixture where the CD extra field differs from the LH extra field would make the unqualified phrase wrong. "the local header's name and extra lengths" would be exact.
- **N4 (tool observation, not an entry defect).** `readout.py` treats an unrecognized `--fact` id as a silent no-op with exit 0 (`ONLY` filter at readout.py:23/26/43; unknown fact never emits): `--fact member` → 0 lines, exit 0; `--fact member[nope]` → 0 lines, exit 0. It also honours only the **first** `--fact` when the flag repeats (`--fact member[AndroidManifest.xml] --fact eocd` → 1 line). Consequence for the C1/C7 gate class: a typo'd fact id in a future entry would yield an empty block that still exits 0 — the same "empty/transcribed block" evidence trap this entry repairs for M39, merely relocated from transcription to invocation. The three blocks under review are non-empty and reproduce exactly, so this is hardening: exit 2 on unknown fact (as `derive_axml_anchors.py` already does for missing symbols) would close it.

# Verification gaps (declared)
- I did not re-run `generator.py` (by design — entry:152 reasons that regeneration is round-65 evidence, not this entry's claim); fixture provenance rests on the pinned sha256 only.
- I did not verify the AXML/dex items (4-11); out of this seat's scope.
- Source rows were checked against the pinned snapshot for §4.3.7 / §4.3.12 only; no live fetch of APPNOTE was made, per the entry's own pinned-anchor discipline.

Verdict: **MATCH** — item 3 is reproducible and its prose is supported; N1-N3 are wording tightenings worth taking at the admission pass, N4 is a readout hardening for the gate class rather than a defect in this entry.
