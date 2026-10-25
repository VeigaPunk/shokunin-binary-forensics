# R67HexContainer — independent container hex verification (C1 item 3)

PASS — all three `payload_first16_hex` values and all three member `sha256` values in
`corpus/knowledge/round-67-apk-axml-byte-evidence.md` item 3 reproduce byte-identically by three
independent code paths off a `/tmp` copy of the committed fixture; `META-INF/MANIFEST.MF` first-16
decodes to ASCII `Manifest-Version` (first 9 = `Manifest-`); the entry's repair note about the
round-65 draft's 15-byte transcription at r65 entry:41 is accurate, including the exact dropped byte.

Read-only seat: no lane byte was written except this report. Scratch dir:
`/tmp/revenger-r67-hex-R67HexContainer/` (fixture copy + one verifier script).

## Verified object identity

- Worktree copy taken from `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/fixture.apk`
  into `/tmp/revenger-r67-hex-R67HexContainer/fixture.apk`:
  `sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, `947 bytes` — equal to
  the entry's item 1 and to the S041 pin.
- Verified bytes **are** the committed bytes: `git status --porcelain -- corpus/fixtures/apk-r65
  corpus/knowledge/round-65-…md corpus/knowledge/round-67-…md` is empty at HEAD
  `7668510ffc49733daf023e40ff3300ef387ebde5`; `git rev-parse HEAD:corpus/fixtures/apk-r65/fixture.apk`
  and `git hash-object corpus/fixtures/apk-r65/fixture.apk` are both
  `b62216a955a4b130b67b7f8d35806abf07be92fa`; last commit touching the fixture is
  `c7b7cf9 round-65: candidates …` (consistent with "unchanged since `c7b7cf98`").
- Pinned neighbour files re-hashed, all equal to the entry header: `truth.json`
  `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`, `readout.py`
  `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`. Whole readout stdout
  SHA-256 = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` (entry `recheck:` pin).

## Path A — stdlib `struct` walk of the central directory + local headers (my own, not the lane readout)

`python3 -B /tmp/revenger-r67-hex-R67HexContainer/verify_container.py fixture.apk` (script retained at
that path; reads only the `/tmp` copy). Derivation: reverse scan for `PK\x05\x06`, unpack the 46-byte
central-directory record with name/extra/comment lengths from the record itself, then unpack the
30-byte local header at the recorded offset and compute
`payload_offset = lho + 30 + lname_len + lextra_len`, `first16 = payload[:16].hex()`,
`sha256(payload)`.

```
cd_offset=737 cd_size=188 eocd=925  cd_end_equals_eocd_offset=true  total_entries_cd=3
cd_walk_end_cursor=925 cd_walk_ends_at_eocd=true
[0] AndroidManifest.xml   lho=0   payload_offset=49  method=0 flags=0x0000 csize=416 usize=416
    crc32 962d075f == recomputed 962d075f   sha256 73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4
    payload_first16_hex 03000800a001000001001c00c4000000
[1] classes.dex           lho=465 payload_offset=506 method=0 flags=0x0000 csize=112 usize=112
    crc32 2635c82a == recomputed 2635c82a   sha256 57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2
    payload_first16_hex 6465780a30333500300c123da5fc7bea
[2] META-INF/MANIFEST.MF  lho=618 payload_offset=668 method=0 flags=0x0000 csize=69  usize=69
    crc32 e948d738 == recomputed e948d738   sha256 2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49
    payload_first16_hex 4d616e69666573742d56657273696f6e      first16_ascii "Manifest-Version"
```

## Path B — `zipfile` (different parser, CRC-verifying on read)

Same script, second derivation: `zipfile.ZipFile(...).open(name).read()` per member (which validates
the member CRC), plus `testzip()`.

```
zipfile_names = ["AndroidManifest.xml","classes.dex","META-INF/MANIFEST.MF"]   testzip = None
sha256_payload_manual == sha256_payload_zipfile : true  for all three members
zipfile_len: 416 / 112 / 69     (== uncompressed_size for all three)
```

The two payload digests agree only if the computed `payload_offset` windows are exactly right, so
Path A's offset arithmetic and Path B's independent parser mutually validate.

## Path C — Info-ZIP `unzip` + raw `dd` at the stated offsets

```
unzip -p fixture.apk <member> | od -An -tx1 -N16
  AndroidManifest.xml          03000800a001000001001c00c4000000
  classes.dex                  6465780a30333500300c123da5fc7bea
  META-INF/MANIFEST.MF         4d616e69666573742d56657273696f6e
dd if=fixture.apk bs=1 skip=49|506|668 count=16 | od -An -tx1   → identical three strings
```

## Deriving-command cross-check (allowed form) and verbatim embedding

```
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
for f in 'member[AndroidManifest.xml]' 'member[classes.dex]' 'member[META-INF/MANIFEST.MF]'; do
  python3 -B corpus/fixtures/apk-r65/readout.py --fact "$f"; echo "exit=$?"; done
```
All three exit 0 and print, in order, exactly the JSON above with `payload_first16_hex` =
`03000800a001000001001c00c4000000` / `6465780a30333500300c123da5fc7bea` /
`4d616e69666573742d56657273696f6e` and `sha256` =
`73d1e0f2…fae4` / `57cfe887…48c2` / `2e5da249…0a49` — i.e. readout stdout, Path A, Path B and
Path C all agree on all six values.

Byte-for-byte embedding check of the entry itself (script compares each embedded line to the
current stdout set): the entry carries six `{"cd_index"…}` lines — `entry:38`, `:40`, `:42` (item 3)
and `:175`, `:176`, `:177` (full-stdout appendix), 3 distinct lines × 2 occurrences —
`verbatim-in-stdout=True` for all six. Both copies of the MANIFEST.MF line already carry the
16-byte pair, so the item-3 repair is not stranded in one block.

## MANIFEST.MF ASCII claim

`bytes.fromhex("4d616e69666573742d56657273696f6e")` → 16 bytes → `b'Manifest-Version'`;
`[:9]` → `b'Manifest-'` (entry:45 claim exact); `b"Manifest-Version: 1.0"[:16]` == those bytes
(entry:45 "the 16-byte prefix of `Manifest-Version: 1.0`" exact). Payload first line is
`'Manifest-Version: 1.0\r'`, one blank-line-separated section — consistent with item 10.

## r65:41 drift — the repair note is accurate

```
grep -n '4d616e696673742d' corpus/knowledge/round-65-apk-axml-byte-evidence.md
41:{"cd_index": 2, … "payload_first16_hex": "4d616e696673742d56657273696f6e", …}
```
- r65:41 hex = 30 chars = **15 bytes**, decodes `Manifst-Version`; v2 hex = 32 chars = **16 bytes**,
  decodes `Manifest-Version`. Programmatic check: removing byte index **5** (`0x65`, `'e'`) from the
  correct 16-byte value yields exactly the r65 bytes — a single dropped byte, so the r65 column could
  not have been a `[:16]` hex of a 69-byte payload. The v2 note at entry:45 states "15-byte
  `4d616e696673742d…`" and "16-byte pair": both numerically correct.
- r65:41 sits exactly on the line number the v2 entry and `admission-status` cite (`entry:41`).
- r65 line 7 (its own rejection note) quotes the **correct** pair while its embedded output at :41
  carries the drifted one — the drift is confined to the evidence line, which is precisely the
  failure shape C2 targets.

## Cross-item corroboration (incidental, within my assigned item 3 only)

The `classes.dex` first-16 is not arbitrary: `first16 == magic8 ‖ declared_checksum(LE) ‖ signature[:4]`
(`6465780a30333500` ‖ `300c123d`→`0x3d120c30` ‖ `a5fc7bea`), and from the `/tmp` copy
`adler32(dex[12:]) = 0x3d120c30`, `sha1(dex[32:]) = a5fc7bea8fa9ffaa52243540c8026066511b9fce`,
`file_size = header_size = 112`, `endian = 0x12345678` — matching entry item 9 and S045's declared
field semantics. Item 3's hex and item 9's declared-header facts are therefore mutually consistent,
not two independent transcriptions.

## Notes for the L1 (not defects in the verified values)

1. `payload_first16_hex` is byte-derived, not literal: `readout.py:105` is
   `payload_off = lh_off + 30 + lh_name_len + lh_extra_len` and `readout.py:118` is
   `payload_first16_hex=payload[:16].hex()`; the entry's citation `readout.py:99-105` lands exactly on
   the two length reads through the `payload_off` assignment. `grep 'truth' readout.py` has no match —
   the item-3 values cannot be oracle-echoed.
2. The v2 entry's prose at `:45` quotes the drifted prefix `4d616e696673742d…` as the repair note. A
   naive whole-text grep/diff check would flag the v2 entry over its own quotation; C2's fenced-blocks-
   whose-first-line-is-`$ cmd` scope is what keeps `--entry` clean here. Relevant to the C7
   separability/discernment seats, not a claim of a defect.
3. Container properties I observed that the entry asserts in §Limitations: all three members
   `method=0` (stored) and local `flags=0x0000` (no data descriptors); `testzip() = None`.

## Scope of this seat / not claimed

Verified: item 3's six values, the MANIFEST.MF ASCII claim, the r65:41 repair note. Not verified here
(assigned to sibling seats): AXML chunk/string/resource-map/attribute walk (items 4-8), the S038/S043/
S045 registry anchors and their line numbers, README/C05 status, counter labels, generator re-run.
No tool was installed or upgraded (nothing was needed). No network used. No lane write other than this
report; no git/jj mutation.

## Risks / blockers

None blocking. Residual risk confined to the two notes above (naive whole-text gates false-positive on
entry:45; item 3's provenance valid only while `fixture.apk` stays at
`05d2280f…d03e`, which `R67FixtureHold` owns).
