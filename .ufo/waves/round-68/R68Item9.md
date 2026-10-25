MATCH — item 9's `dex_declared_header` embedded line (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:111`, repeated verbatim at `:213`) is byte-identical to my independent re-derivation: all 14 fields equal, exit 0; the prose sentence at `:107` states nothing the output does not support (two low-severity derivation-wording gaps noted below, no false claim).

# R68 item 9 — independent re-derivation of the dex declared header

Seat: `L1Revenger68.R68Item9` (leaf, read-only). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Nothing edited. No tool installed or upgraded during this seat (no install was needed).

## 1. Commands and actual output

Lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact dex_declared_header
{"checksum_matches": true, "checksum_recomputed": "0x3d120c30", "declared_checksum": "0x3d120c30", "endian_tag": "0x12345678", "fact": "dex_declared_header", "file_size": 112, "format_version": "035", "header_bytes": 112, "header_size": 112, "magic_ascii": "dex\n", "magic_hex": "6465780a30333500", "signature_matches": true, "signature_recomputed": "a5fc7bea8fa9ffaa52243540c8026066511b9fce", "signature_sha1": "a5fc7bea8fa9ffaa52243540c8026066511b9fce"}
EXIT=0
```

The three requested member facts (run once each, same invocation form):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[AndroidManifest.xml]'
{"cd_index": 0, "compressed_size": 416, "crc32": "962d075f", "crc32_matches": true, "crc32_recomputed": "962d075f", "fact": "member[AndroidManifest.xml]", "local_header_offset": 0, "payload_first16_hex": "03000800a001000001001c00c4000000", "payload_offset": 49, "sha256": "73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4", "uncompressed_size": 416}
EXIT=0

$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[classes.dex]'
{"cd_index": 1, "compressed_size": 112, "crc32": "2635c82a", "crc32_matches": true, "crc32_recomputed": "2635c82a", "fact": "member[classes.dex]", "local_header_offset": 465, "payload_first16_hex": "6465780a30333500300c123da5fc7bea", "payload_offset": 506, "sha256": "57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2", "uncompressed_size": 112}
EXIT=0

$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e69666573742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
EXIT=0
```

The `classes.dex` member line matters to this item as a cross-check: its `payload_first16_hex` is exactly magic `6465780a30333500` + declared checksum little-endian `300c123d` (= `0x3d120c30`) + signature start `a5fc7bea` — the same three values the header fact reports.

Full run (Q02's stdout-SHA-256 claim re-derived, not trusted):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r68i9_full.txt; echo EXIT=$?
EXIT=0
$ wc -l /tmp/r68i9_full.txt
15 /tmp/r68i9_full.txt
$ sha256sum /tmp/r68i9_full.txt
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/r68i9_full.txt
```

`507d79f8…` is exactly the digest the entry states in `## Reproduce` (`verified-at`/Q02 basis), 15 lines matches "Exit 0; 15 stdout lines".

Independent byte decode (Python `zipfile`+`struct`+`zlib`+`hashlib`, no readout code reused; `corpus/fixtures/apk-r65/fixture.apk`, member `classes.dex`):

```
len 112 sha256 57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2
magic 6465780a30333500 'dex\n' '035' 0            # byte 7 == 0x00, i.e. the trailing NUL
checksum 0x3d120c30 adler 0x3d120c30              # adler32(d[12:]) == declared @8
endian_tag@40 0x12345678
declared sig bytes12-31 a5fc7bea8fa9ffaa52243540c8026066511b9fce
bytes 32..112 sha1 a5fc7bea8fa9ffaa52243540c8026066511b9fce
file_size 112 header_size 112 actual len 112
first16 6465780a30333500300c123da5fc7bea
```

Fixture identity: `sha256sum corpus/fixtures/apk-r65/fixture.apk` → `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (matches S041 anchor at entry `:5`). Readout identity: `sha256sum corpus/fixtures/apk-r65/readout.py` → `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` (matches the entry's stated readout sha256).

## 2. Exact line equality (not eyeballed)

Compared the entry's two `dex_declared_header` object lines against the actual stdout with Python string equality and per-field JSON comparison:

```
LINE 111 EXACT_EQUAL True
LINE 213 EXACT_EQUAL True
actual keys: ['checksum_matches', 'checksum_recomputed', 'declared_checksum', 'endian_tag', 'fact',
              'file_size', 'format_version', 'header_bytes', 'header_size', 'magic_ascii', 'magic_hex',
              'signature_matches', 'signature_recomputed', 'signature_sha1']
nfields 14
```

No key set difference, no field value difference, no length difference — the two lines are identical strings and both are identical to the re-derived line. Also diffed the whole `## Reproduce` fenced block (`:199` command line, 15 stdout lines `:200-214`):

```
block lines 15, actual lines 15
mismatched lines: 0 of 15
```

## 3. Field-by-field verdict (declared header, 14/14)

| field | actual | entry `:111`/`:213` | verdict |
|---|---|---|---|
| `fact` | `dex_declared_header` | same | MATCH |
| `magic_hex` | `6465780a30333500` | same | MATCH (independently bytes 0-7 of the member) |
| `magic_ascii` | `dex\n` | same | MATCH (JSON escape for `dex`+LF) |
| `format_version` | `035` | same | MATCH (bytes 4-6) |
| `declared_checksum` | `0x3d120c30` | same | MATCH (little-endian u32 @8) |
| `checksum_recomputed` | `0x3d120c30` | same | MATCH (adler32(`d[12:]`), reproduced) |
| `checksum_matches` | `true` | same | MATCH (declared == recomputed) |
| `signature_sha1` | `a5fc7bea8fa9ffaa52243540c8026066511b9fce` | same | MATCH (hex of declared bytes 12-31) |
| `signature_recomputed` | `a5fc7bea8fa9ffaa52243540c8026066511b9fce` | same | MATCH (sha1(`d[32:]`), reproduced) |
| `signature_matches` | `true` | same | MATCH |
| `file_size` | `112` | same | MATCH (u32 @32; equals member length 112) |
| `header_size` | `112` | same | MATCH (u32 @36; 0x70 per S045 for `035`) |
| `endian_tag` | `0x12345678` | same | MATCH (u32 @40; S045 `ENDIAN_CONSTANT`, entry `:3`/`:59`) |
| `header_bytes` | `112` | same | MATCH (len of the member) |

Derivation sites in the readout (`corpus/fixtures/apk-r65/readout.py`): `magic = dex[:8]` at `:233`, `checksum = u32(dex, 8)` at `:234`, `signature = dex[12:32]` at `:235`, the `emit("dex_declared_header", …)` block at `:237-248`, offsets 32/36/40 at `:246-247`, adler recomputation at `:241-242`, sha1 recomputation at `:244-245`, `header_bytes=len(dex)` at `:248`.

## 4. Prose judgment — `corpus/knowledge/round-68-apk-axml-byte-evidence.md:107`

Clause by clause, does the output support it?

| prose clause (`:107`) | support in the output | verdict |
|---|---|---|
| "first eight bytes are `6465780a30333500`" | `magic_hex` is exactly 16 hex chars = 8 bytes | supported |
| "the magic `dex\n035\0`" | `magic_ascii` + `format_version`; the trailing `\0` (byte 7 = `0x00`) is readable only from `magic_hex`, not from `magic_ascii` | supported (render-only) |
| "declared checksum `0x3d120c30` equals the Adler-32 recomputed over the bytes from offset 12 on" | `declared_checksum`, `checksum_recomputed`, `checksum_matches: true` | supported |
| "declared 20-byte signature equals the SHA-1 recomputed over the bytes from offset 32 on" | `signature_sha1` (40 hex chars = 20 bytes), `signature_recomputed`, `signature_matches: true` | supported; the word "20-byte" is a count not printed as a field (see F2) |
| "declared `file_size` and `header_size` are both 112" | `file_size: 112`, `header_size: 112` | supported; the meaningful part — that 112 is also the member's actual length — is visible only via `header_bytes: 112` (see F1) |
| "endian tag is `0x12345678`, S045's `ENDIAN_CONSTANT`" | `endian_tag: 0x12345678`; S045 quote `ENDIAN_CONSTANT = 0x12345678` at `corpus/SOURCES.md:59` and entry `:3` | supported |
| "These are declared-header self-consistency facts about one inert member; dex validity is not claimed" | matches Q09 row `:180` and `## Limitations` `:162` ("The dex member is a header only and is intentionally not a valid dex program") | supported; no overreach |

No clause asserts a value the output contradicts, and no clause generalizes beyond this one member. The prose does not claim a dex program is valid, does not claim a signature block or install validity, and does not attribute the readout to a producer tool (Q04/Q07/Q09/Q10 bases at `:175-180` remain consistent with what the output actually is).

## 5. Findings (by severity)

**F1 — LOW (prose, `:107`).** `header_bytes` is the only field in the embedded output that the entry never interprets anywhere (grep: `header_bytes` occurs at `:111` and `:213` only, both inside output blocks). It duplicates `file_size` for this fixture, but it is the field carrying *actual* payload length — the one that makes `file_size: 112` a self-consistency check rather than a lone declared number. The prose therefore states the declared pair but not the check that the declared size equals the member. Not a false claim; a derivation-chain gap under the Q11 basis ("each count … carries … the command that derives it"). Cheap close: one clause reading `header_bytes` as the member length, or rename to `member_bytes`.

**F2 — LOW (prose, `:107`).** "20-byte signature" is a count carried by no output field: the readout prints the 40-hex `signature_sha1`, not a length. The count is derivable from the hex length (or from S045), but Q11 asks for the deriving command/output to be in the entry. Not a mismatch. Cheap close: a `signature_bytes: 20` field, or prose "the 40-hex (20-byte) `signature_sha1`".

**Observation (no defect, residual risk).** `checksum_matches` is computed as `adler32(dex[12:])` (`readout.py:241-242`) over the whole member, not `adler32(dex[12:file_size])`. For this fixture `file_size == len == 112`, so the two spans coincide and the entry's prose ("from offset 12 on") is exactly the code and exactly S045's "the rest of the file". On a member with trailing bytes past the declared `file_size` the check would silently cover the wrong span while the prose would still read as correct — out of scope for C05 (single fixture, `## Limitations` `:162` fences generalization), recorded as residual risk only.

**No field mismatch, no unsupported prose claim, no transcription drift** (the M39 class the entry's `verified-at` `:6` says it repairs) in the `dex_declared_header` block: both embedded occurrences are byte-identical to a fresh run, and the whole 15-line `## Reproduce` block diffs clean.

## 6. Build-state corroboration (read-only)

`grep -n C05 corpus/README.md` → `34:| C05 | Android packages (APK) | … | uncovered |` — the C05 row is still `uncovered`, consistent with the entry's `admission-status: candidate` (`:9`) and the brief's "README not flipped". This item makes no claim about the other C05 criteria; the dex-header fact it was asked to re-derive holds.

## 7. Verification gaps

- I did not re-run `corpus/derive_axml_anchors.py` (item 11; other seats own it); my S045 quote is taken from the registry row `corpus/SOURCES.md:59`, which I read, not from the fetched AOSP snapshot (`.ufo/waves/round-67/source-snapshots/dex-format.html`) — I had no reason to re-fetch and did not.
- The member facts were re-derived but only as a cross-check for the dex payload; their own claim rows (items 1-3) were not audited field-by-field here.
- `endian_tag`'s *semantics* (that `0x12345678` is `ENDIAN_CONSTANT` and means little-endian) rests on S045's registry quote; the output only prints the value, and the entry scopes that attribution to S045 (`:3`), which is where I checked it.
