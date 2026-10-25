ALL-MATCH — every dex declared-header value recomputed with my own stdlib parser equals item 9's embedded values, and all four `header_item` field texts item 9 quotes occur in the S045 snapshot under tag-stripped, punctuation-normalized fixed-string matching.

Seat: R67HexDex (leaf, independent dex-header verification). Read-only w.r.t. the lane; my only write is this file. Scratch: `/tmp/R67HexDex/fixture.apk` (copy), no lane file, no git/jj mutation, no tool installs.

## Scope as assigned

1. Recompute over the `classes.dex` member of a `/tmp` copy of `corpus/fixtures/apk-r65/fixture.apk`, with my own Python-stdlib code (no `readout.py`, no `generator.py`, neither read nor executed): magic, `adler32(bytes from offset 12)`, `sha1(bytes from offset 32)`, `file_size` u32@32, `header_size` u32@36, `endian_tag` u32@40.
2. Compare with the values embedded in `corpus/knowledge/round-67-apk-axml-byte-evidence.md` item 9.
3. Confirm the quoted `header_item` field texts (checksum / signature / header_size / endian_tag) actually occur in `.ufo/waves/round-67/source-snapshots/dex-format.html` (fixed-string, tag-stripped rendering).

## 1–2. Independent recompute vs entry item 9

Input identity: `/tmp` copy sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, 947 bytes — equal to the entry's item 1 `archive` sha256, so the bytes I measured are the committed fixture bytes.

Member extraction was done **twice by two independent structures**, and both agree:

- Walk of `PK\x03\x04` local headers: `classes.dex` local-header offset 465, payload offset 506, method 0 (stored), usz=csz=112, CRC-32 `2635c82a` recomputed over payload ✓, payload sha256 `57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2` (equals the entry's item 3 `member[classes.dex]` sha256).
- Walk of the EOCD (`@925`, `total_entries_cd=3`, `cd_off=737`, `cd_size=188`, `cd_off+cd_size==eocd` → true) and each central-directory record. `CD1 classes.dex method=0 flags=0x0000 crc=2635c82a csz=112 usz=112 lho=465` — agrees with the local header; **0 bytes** between the dex payload end (506+112=618) and the next local header (`META-INF/MANIFEST.MF` @618). So the 112-byte dex is exactly the member payload, no padding, no data descriptor.

| # | field | byte offsets taken | item 9 embedded value | my recompute | match |
|---|---|---|---|---|---|
| 1 | magic | `D[0:8]` | `6465780a30333500` (`dex\n035\0`) | `6465780a30333500` = `b'dex\n035\x00'` | ✅ |
| 2 | declared checksum | `u32@8` | `0x3d120c30` | `0x3d120c30` | ✅ |
| 3 | checksum recompute | `adler32(D[12:])` (100 bytes) | equals declared (`checksum_matches: true`) | `0x3d120c30` == declared | ✅ |
| 4 | declared signature | `D[12:32]` | `a5fc7bea8fa9ffaa52243540c8026066511b9fce` | `a5fc7bea8fa9ffaa52243540c8026066511b9fce` | ✅ |
| 5 | signature recompute | `sha1(D[32:])` (80 bytes) | equals declared (`signature_matches: true`) | `a5fc7bea8fa9ffaa52243540c8026066511b9fce` == declared | ✅ |
| 6 | file_size | `u32@32` | `112` | `112` (== `len(D)` == 112) | ✅ |
| 7 | header_size | `u32@36` | `112` | `112` | ✅ |
| 8 | endian_tag | `u32@40` | `0x12345678` | `0x12345678` | ✅ |

Supporting offsets also read clean (`link_size=0`, `map_off=0`), consistent with a header-only inert member — the entry's own `Limitations` line already disclaims dex validity, and item 9's closing clause ("declared-header self-consistency facts about one inert member; dex validity is not claimed") is borne out: the "file" is exactly the 112-byte header.

Entry text compared (verbatim, `corpus/knowledge/round-67-apk-axml-byte-evidence.md:106:raw`):

> 9. The `classes.dex` payload's first eight bytes are `6465780a30333500` — the magic `dex\n035\0`. Its declared checksum **`0x3d120c30`** equals the Adler-32 recomputed over the bytes from offset 12 on … and its declared 20-byte signature equals the SHA-1 recomputed over the bytes from offset 32 on … The header's declared `file_size` and `header_size` are both 112 … and the endian tag is `0x12345678`, S045's `ENDIAN_CONSTANT`.

Every numeric/hex claim in that paragraph is confirmed against the bytes. The fenced `dex_declared_header` block at line 109-111 reproduces values that my parser reproduces exactly, so that block is not a drifted readout for this member.

## 3. Snapshot occurrence check (S045 `header_item` texts)

Snapshot: `.ufo/waves/round-67/source-snapshots/dex-format.html`, 281157 bytes, sha256 `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` — matches the hash S045 declares in `corpus/SOURCES.md:59`. Title: `Dalvik executable format | Android OS core topics | Android Open Source Project`; canonical URL `https://source.android.com/docs/core/runtime/dex-format` present in the snapshot (the URL S045 declares). So the snapshot is the AOSP DEX format spec and is the same artifact the registry row pins.

Method: strip `<script>/<style>`, strip all tags, HTML-unescape, NFKC, collapse whitespace, then normalize space-before-`)`/`,`/`;`/`.`/`:`; search fixed strings. Offsets below are character offsets in that normalized rendering (the HTML is one line, so raw line numbers are not meaningful); counts are substring occurrences.

| quoted field text (as item 9 / S045 use it) | occurrences | normalized offset | verdict |
|---|---|---|---|
| `adler32 checksum of the rest of the file (everything but magic and this field)` | 1 | 26141 | ✅ present |
| `SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)` | 1 | 26272 | ✅ present (see nuance A) |
| `must be 0x70 (112) bytes (v40 or earlier)` | 1 | 26801 | ✅ present |
| `endian_tag uint = ENDIAN_CONSTANT` | 1 | 26883 | ✅ present |
| `uint ENDIAN_CONSTANT = 0x12345678;` | 1 | 13963 | ✅ present |
| `ubyte[8] = DEX_FILE_MAGIC` | 1 | 26024 | ✅ present |

Context at the `header_item` table (normalized 25873-27000) reads, in order: `magic ubyte[8] = DEX_FILE_MAGIC … checksum uint adler32 checksum of the rest of the file (everything but magic and this field); used to detect file corruption signature ubyte[20] SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field); used to uniquely identify files file_size uint size of the entire file (including the header), in bytes … header_size uint … must be 0x70 (112) bytes (v40 or earlier) must be 0x78 (120) bytes (v41 or later) endian_tag uint = ENDIAN_CONSTANT`. All four fields item 9 attributes to S045 are there, in the field order item 9 assumes (magic 0-7, checksum 8-11, signature 12-31, file_size 32-35, header_size 36-39, endian_tag 40-43), which is also why taking u32@32/36/40 is the spec-correct read.

## Nuances and residual risk

- **A — signature quote needs punctuation normalization.** Raw fixed-string grep of the full sentence finds 0 hits because the live page wraps `magic`, `checksum` and `this field` in inline elements, so tag-stripping leaves `…(everything but magic , checksum , and this field)`. After collapsing spaces before commas the sentence matches item 9 character for character. This is a rendering artifact, not a paraphrase: the word sequence and punctuation of the quoted sentence are the page's. The other three quotes match before punctuation normalization (each is also found as a raw-HTML fixed string for its leading clause: `adler32 checksum of the rest of the file`, `SHA-1 signature (hash) of the rest of the file`, `must be 0x70 (112) bytes`, `ENDIAN_CONSTANT`).
- **B — the page's own magic example is `039`, not `035`.** Normalized offset 11386ff shows `ubyte[8] DEX_FILE_MAGIC = { 0x64 0x65 0x78 0x0a 0x30 0x33 0x39 0x00 } = "dex\n039\0"`, and `035` occurs only twice, both in the version-history prose (`Prior to version 037 most versions of Android have used version 035 of the format`, offsets 12933/12989). Item 9 does **not** claim S045 prints a `035` example: it claims the fixture's magic is `035` and cites S045's `header_size` rule with the qualifier "(v40 or earlier)", which by the page's own version list covers 035. Consistent; no misattribution.
- **C — independence limits.** I did not run `readout.py` or `generator.py` (running the former would make the check circular; running the latter is a round-65 evidence question, not mine). I therefore verify the *values*, not the script's provenance or the entry's `Reproduce` stdout hash. The entry's member/archive sha256 pins are corroborated by my recompute.
- **D — normalization dependence.** The pass in §3 is against the normalized rendering; a stricter raw-bytes grep of the full sentences fails for the signature sentence only (nuance A). Recorded rather than papered over.

## Evidence commands (actual, run 2026-10-24)

```
$ sha256sum corpus/fixtures/apk-r65/fixture.apk
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk

$ cp → /tmp/R67HexDex/fixture.apk; my own struct/hashlib walk (local headers + EOCD/CD cross-check)
EOCD@ 925 entries 3 cd_off 737 cd_size 188 comment_len 0 cd_end==eocd: True
CD1 classes.dex  method=0 flags=0x0000 crc=2635c82a csz=112 usz=112 lho=465
  local: method 0 crc 2635c82a csz 112 usz 112 pstart 506 crc_ok True stored==payload True
  payload sha256 57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2
  bytes between payload end and next member: 0
  adler(dex[12:]) 3d120c30 decl 3d120c30
  sha1(dex[32:]) a5fc7bea8fa9ffaa52243540c8026066511b9fce
  file_size u32@32 112 header_size u32@36 112 endian u32@40 0x12345678

dex len 112
magic first8 hex 6465780a30333500
magic raw b'dex\n035\x00'
declared checksum  u32@8  0x3d120c30
declared signature 20B@12 a5fc7bea8fa9ffaa52243540c8026066511b9fce
declared file_size  u32@32 112
declared header_size u32@36 112
declared endian_tag u32@40 0x12345678
recomputed adler32(D[12:]) = 0x3d120c30
recomputed sha1(D[32:])    = a5fc7bea8fa9ffaa52243540c8026066511b9fce
checksum match: True   signature match: True   file_size==len(D): True   endian==0x12345678: True

$ sha256sum .ufo/waves/round-67/source-snapshots/dex-format.html
c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4  dex-format.html

$ grep -o -F 'adler32 checksum of the rest of the file' dex-format.html | head -n3     → 1 hit
$ grep -o -F 'SHA-1 signature (hash) of the rest of the file' dex-format.html | head -n3 → 1 hit
$ grep -o -F 'must be 0x70 (112) bytes' dex-format.html | head -n3                      → 1 hit
$ grep -o -F 'ENDIAN_CONSTANT' dex-format.html | head -n3                               → 3 hits (raw HTML cap)
$ tag-strip + NFKC + punctuation-normalize (my code) → all six quoted strings found (table §3)
```

Cross-reference: `corpus/SOURCES.md:59` (S045 row) declares the same snapshot sha256 and the same three `header_item` quotes, so the snapshot↔registry↔entry citation chain is internally consistent for this item.

## Tooling

No installs or upgrades were performed (no package needed; Python 3 stdlib only). Scratch: `/tmp/R67HexDex/` (copy of the fixture) — lane untouched.

## Blockers

None.

Report: .ufo/waves/round-67/R67HexDex.md
