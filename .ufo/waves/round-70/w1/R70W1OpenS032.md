OPENED-QUOTE-PRESENT — live S032/S034 source is byte-identical to the committed snapshot (sha256 `0b993022…`), every phrase item 11-12 relies on locates in the live bytes, but three located defects remain: the cited APPNOTE line ranges under-cover 5 of the 12 ZIP offsets item 12 asserts (F1), the S032 header claims the §4.3.7 local-file-header scope its own registry row excludes (F3), and the S045 registry row anchors its four quotes at the wrong live sections (F4).

Seat: R70W1OpenS032 (wave-1 advisory, round-70 / hyaku run 7). Lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Target bytes: commit `aa1842fac199aa524930e5565ed3715de5f84c6d`, entry `corpus/knowledge/round-70-apk-axml-byte-evidence.md`.
Base for comparison: `3f5edbc206351232a3d2d801334dd930499ccaf5`.
No file in the lane was edited. Scratch only: `/tmp/revenger-r70-R70W1OpenS032*` (deleted before returning).
No packages installed (all pacman transactions are host-paused; nothing was needed — `curl`, `python3` stdlib, `base64`, `tar` are pre-existing).

---

## 1. Registry rows read first (as instructed)

`corpus/SOURCES.md:46` (S032) and `corpus/SOURCES.md:48` (S034), read whole.

| row | URL | tier | scope | sections | opened |
|---|---|---|---|---|---|
| S032 | `https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT` | spec / A | central-directory file header + EOCD field layout | §4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; v6.3.10 (rev. Nov 01, 2022) | 2026-10-23, mined |
| S034 | same URL | spec / A | local file header field layout | §4.3.7; v6.3.10; **snapshot lines 387-399**, sha256 `0b993022…` | 2026-10-23, mined |

S032's own scope note (`corpus/knowledge/round-63-zip-central-directory-evidence.md:675`) excludes the local file header ("that is S034"); S034's row cites lines **387-399** for §4.3.7.

## 2. Live fetch today (2026-10-25) — receipt

Command and actual output:

```
$ cd /tmp/revenger-r70-R70W1OpenS032 && date -u '+fetch_start_utc=%Y-%m-%dT%H:%M:%SZ' && curl -sSL --max-time 60 -o APPNOTE.live.txt -w 'http_code=%{http_code} size=%{size_download} url_effective=%{url_effective}\n' 'https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT'
fetch_start_utc=2026-10-25T21:07:14Z
http_code=200 size=174585 url_effective=https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
curl_exit=0
fetch_end_utc=2026-10-25T21:07:14Z
$ sha256sum APPNOTE.live.txt
0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6  APPNOTE.live.txt
```

Second, independent receipt for all four snapshots (21:12:50Z):

```
RECEIPT 2026-10-25T21:12:50Z
APPNOTE.TXT    http=200 bytes=174585 0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6
ResourceTypes.h http=200 bytes=115008 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f
dex-format.html http=200 bytes=281161 f0132964f79cd35ab6e4c2d0f3afe93735ff18cfd6e093523230d6bdf0106ccd
rea(tarball)   http=200 bytes=5634033 412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c
RECEIPT_END 2026-10-25T21:12:54Z
```

`ResourceTypes.h` was fetched as base64 (`?format=TEXT`) from `android.googlesource.com` at the pinned tag `android-15.0.0_r1` and decoded; the REA file was extracted from the `rea-agents-6.5.0` npm tarball member `package/skills/reverse-engineer-anything/references/android-applications.md` (the raw GitHub path `raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/...` returned `404: Not Found`, http=404 — the npm tarball is the same artifact the registry row names, so this is a channel note, not an unreachability of the source).

### Comparison with the lane's committed snapshot

```
$ sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/snapshots/*
0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6  corpus/snapshots/APPNOTE.TXT
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4  corpus/snapshots/dex-format.html
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  corpus/snapshots/rea-android-applications.md
```

| source | live sha256 (2026-10-25) | snapshot sha256 | verdict |
|---|---|---|---|
| **APPNOTE.TXT (S032/S034)** | `0b993022…c88c76` | `0b993022…c88c76` | **BYTE-IDENTICAL** (`cmp` exit 0) |
| **ResourceTypes.h (S038)** | `56b88bc4…57c56f` | `56b88bc4…57c56f` | **BYTE-IDENTICAL** (after base64 decode) |
| **rea-android-applications.md (S043)** | `412d9cb4…afa74c` | `412d9cb4…afa74c` | **BYTE-IDENTICAL** |
| **dex-format.html (S045)** | `f0132964…0106ccd` / `b45b3eba…c39306` (two fetches, 5 min apart) | `c0428612…91d9f4` | **DIFFERS** — see §3 |

The APPNOTE live bytes also confirm the version metadata the registry rows state: `APPNOTE.live.txt:2` = `Version: 6.3.10 `, `:4` = `Revised: Nov 01, 2022`.

## 3. S045 `dex-format.html`: differs, and the difference is non-semantic

```
$ cmp dex.live.html corpus/snapshots/dex-format.html
dex.live.html corpus/snapshots/dex-format.html differ: char 273494, line 8946
```

`difflib` opcodes over both files (8957 lines each) give exactly two `replace` hunks and no others:

```
replace 8945 8946 8945 8946   <script nonce="R1GN4pA7+nDrYJ/dulpbEJ8pQlLBzr">   vs   <script nonce="m4V13NT+mpbeamUQBq7smny7XBGnE8">
replace 8950 8951 8950 8951   (one inline JS config blob line; a feature-flag/session array differs)
```

Two live fetches 5 minutes apart (`b45b3eba…` then `f0132964…`) differ from each other in the same two places — the CSP nonce and a session/feature-flag blob rotate per response. So the live document is **not byte-stable across responses**; the drift is server-side session noise, not a content change. Verified consequence: all three dex phrases keep the **same line numbers** in live and snapshot (5956, 5981, 5035), and `wc -l` is 8956 for all three files. No load-bearing dex content changed.

## 4. Quote location at the LIVE source (the ≤25-word located quotes)

Item 11's `--spec-quotes` was re-run against **live** bytes (the four snapshot files in a scratch copy were replaced by the fetched ones; the lane tree was not touched):

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes
MATCH rea-android-applications.md: first line 7, folded phrase present=True: Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.
MATCH dex-format.html: first line 5949, folded phrase present=True: adler32 checksum of the rest of the file (everything but magic and this field)
MATCH dex-format.html: first line 5956, folded phrase present=True: SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)
MATCH dex-format.html: first line 5981, folded phrase present=True: must be 0x70 (112) bytes (v40 or earlier)
MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;
MATCH ResourceTypes.h: first line 686, folded phrase present=True: Byte offset from the start of this structure where the attributes start
spec_quotes_exit=0
```

Every phrase item 11 relies on locates in the live bytes, at the same line numbers the entry prints. **Item 11 quote: OPENED-QUOTE-PRESENT.**

The quotes items 11-12 rely on for **S032/S034** (the APPNOTE layouts) were located in the live APPNOTE by folding whitespace and searching the raw bytes. Each is quoted verbatim with its live line and the heading it sits under:

| row | § | live line(s) | ≤25-word quote (verbatim from live APPNOTE) |
|---|---|---|---|
| S034 | 4.3.7 | 388 | "local file header signature 4 bytes (0x04034b50)" |
| S034 | 4.3.7 | 395-399 | "file name length 2 bytes extra field length 2 bytes" |
| S032 | 4.3.12 | 521 | "central file header signature 4 bytes (0x02014b50)" |
| S032 | 4.3.12 | 529-533 | "crc-32 4 bytes compressed size 4 bytes uncompressed size 4 bytes file name length 2 bytes extra field length 2 bytes" |
| S032 | 4.3.12 | 538 | "relative offset of local header 4 bytes" |
| S032 | 4.3.16 | 633 | "end of central dir signature 4 bytes (0x06054b50)" |
| S032 | 4.3.16 | 638-641 | "total number of entries in the central directory on this disk 2 bytes total number of entries in the central directory 2 bytes" |
| S032 | 4.4.7 | 911 | "If bit 3 of the general purpose flag is set, this field is set to zero in the local header and the correct" |
| S032 | 4.4.7 | 913 | "value is put in the data descriptor and in the central directory." |
| S032 | 4.4.16 | 983 | "This is the offset from the start of the first disk on which this file appears, to where the local header SHOULD be found." |
| S032 | 4.3.3 | 350 | "All values MUST be stored in little-endian byte order unless otherwise specified in this document for a specific data element." |

All 11 located quotes are ≤25 words, present verbatim in the live bytes, and under the section heading they are attributed to (headings confirmed at live lines 387 = `4.3.7  Local file header:`, 511 = `4.3.12  Central directory structure:`, 632 = `4.3.16  End of central directory record:`). **Item 12 quote: OPENED-QUOTE-PRESENT.**

**Independent corroboration of F1 (below) by a parallel seat.** Seat `R70W1OpenS045` independently located the same APPNOTE line-range defect in its own wave-1 report (`.ufo/waves/round-70/w1/R70W1OpenS045.md` §4, "D1") and reported the same sums I derived (28 over 387-398 and 28 over 511-531, versus the entry's printed 30 and 46). Two seats, two independent re-derivations from the live bytes, same defect and same arithmetic. Its report additionally cites the lane's own round-63 build record `.ufo/waves/round-63/build/R63SourceAppnote.md:69`, which independently places "relative offset of local header" at line **538** — I verified that pointer myself:

```
$ grep -n "538" .ufo/waves/round-63/build/R63SourceAppnote.md
69:| Q10 | §4.3.12 (offset field, last fixed field) | 538 | `relative offset of local header 4 bytes` |
```

---

## 5. F1 — LOCATED DEFECT: the cited APPNOTE line ranges under-cover 5 of the 12 offsets item 12 asserts

The entry states its APPNOTE anchors three times, identically:

- `corpus/knowledge/round-70-apk-axml-byte-evidence.md:4` (S032 `source:` header) — "§4.3.7 local file header (snapshot lines **387-398**), §4.3.12 central directory file header (lines **511-531**) and §4.3.16 end of central directory record (lines **632-646**)"
- `corpus/knowledge/round-70-apk-axml-byte-evidence.md:152` (item 12) — "the layouts are APPNOTE snapshot lines **387-398, 511-531 and 632-646**"
- `corpus/fixtures/apk-r65/entry_checks.py:47` (same comment, in the target commit `aa1842f`)

Re-deriving the offsets from the **live** APPNOTE bytes (raw-byte sha256 `0b993022…`, byte-identical to the snapshot, so live lines = snapshot lines) and comparing each field's line against the cited range:

```
$ python3 final.py   # parses live APPNOTE.TXT, offsets each field, tests the cited ranges
live APPNOTE sha256: 0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6 174585
MATCH local.crc32: live_offset=14 entry_says=14 offset-OK | live_line=395 cited local 387-398 -> inside
MATCH local.compressed_size: live_offset=18 entry_says=18 offset-OK | live_line=396 cited local 387-398 -> inside
MATCH local.uncompressed_size: live_offset=22 entry_says=22 offset-OK | live_line=397 cited local 387-398 -> inside
MATCH local.name_length: live_offset=26 entry_says=26 offset-OK | live_line=398 cited local 387-398 -> inside
MATCH local.extra_length: live_offset=28 entry_says=28 offset-OK | live_line=399 cited local 387-398 -> *** OUTSIDE CITED RANGE ***
MATCH central.name_length: live_offset=28 entry_says=28 offset-OK | live_line=532 cited central 511-531 -> *** OUTSIDE CITED RANGE ***
MATCH central.extra_length: live_offset=30 entry_says=30 offset-OK | live_line=533 cited central 511-531 -> *** OUTSIDE CITED RANGE ***
MATCH central.comment_length: live_offset=32 entry_says=32 offset-OK | live_line=534 cited central 511-531 -> *** OUTSIDE CITED RANGE ***
MATCH central.local_header_offset: live_offset=42 entry_says=42 offset-OK | live_line=538 cited central 511-531 -> *** OUTSIDE CITED RANGE ***
MATCH eocd.total_entries: live_offset=10 entry_says=10 offset-OK | live_line=641 cited eocd 632-646 -> inside
MATCH eocd.cd_size: live_offset=12 entry_says=12 offset-OK | live_line=642 cited eocd 632-646 -> inside
MATCH eocd.cd_offset: live_offset=16 entry_says=16 offset-OK | live_line=645 cited eocd 632-646 -> inside

fixed parts: local=30(entry 30) central=46(entry 46) eocd=22(entry 22)
offsets asserted OUTSIDE the cited ranges: 5 of 12
```

The **offsets are all correct** when re-derived from live bytes, and the three fixed-part totals (30 / 46 / 22) are correct. The defect is the **citation**: the ranges as printed do not contain the lines the cited values come from.

- `local.extra_length` (offset 28) is transcribed from live line **399**; the cited local range ends at **398**.
- `central.name_length` (28), `central.extra_length` (30), `central.comment_length` (32) and `central.local_header_offset` (42) are transcribed from live lines **532 / 533 / 534 / 538**; the cited central range ends at **531**.

**The sharpest statement of F1: the cited ranges cannot produce the printed sums.** Summing only the width rows that fall *inside* each cited range (live APPNOTE bytes):

```
$ python3 - <<'EOF'   # sum field widths inside each cited range
sum over 387-398 = 28      # entry prints "local fixed part: 30 bytes"
sum over 389-399 = 30
sum over 511-531 = 28      # entry prints "central fixed part: 46 bytes"
sum over 520-538 = 46
sum over 632-646 = 22      # entry prints "eocd fixed part: 22 bytes"  <- OK
sum over 634-646 = 22
```

So 30 and 46 are **not** derivable from the ranges the entry prints (28 and 28 are), while 22 is. The local range is short by the one row `extra field length` at 399; the central range is short by the seven rows 532-538 (file name length … relative offset of local header). This is the same arithmetic seat `R70W1OpenS045` independently reported.

The correct ranges for the three layouts, from the live bytes, are **387-399** (§4.3.7), **520-538** (§4.3.12 file header field list, heading at 511) and **634-646** (§4.3.16 field list, heading at 632). Note the registry's own S034 row already cites "snapshot lines **387-399**" (`corpus/SOURCES.md:48`) — the entry narrowed the registry's range by one line and dropped the very line its own `local.extra_length` offset depends on.

**Why this is a defect and not a nit.** The entry's own `Q11` row (`corpus/knowledge/round-70-apk-axml-byte-evidence.md:213`) claims "every count, offset, identifier and digest carries its deriving command and output in items 1-15; the recorded values (APPNOTE widths) are labeled recorded where used". The widths are labeled recorded — but item 12 states *where* they are recorded, and that location is wrong for 5 of the 12 offsets the item prints. A reader who opens APPNOTE lines 511-531 to check `central.local_header_offset: spec offset 42` finds nothing there: the "relative offset of local header" line is at 538. QUALITY.md Q02 requires the header's anchor to be exact, and Q11 requires the deriving command to be re-runnable; the anchor as printed cannot locate 5 of the 12 values it is offered as the source for. This is the same defect class the round-65 spot-check already routed for a wrong line number (D2, `corpus/lessons/round-65-verifier-spotcheck.md:50`).

**The registry's located quotes are unaffected.** All 11 S032/S034 quotes in §4 above locate in the live bytes, so this is a range-arithmetic defect in the entry and its comment, not a missing or absent source quote.

**Suggested repair (advisory; I did not apply it):** change the three cited ranges to `387-399`, `520-538`, `634-646` at `corpus/knowledge/round-70-apk-axml-byte-evidence.md:4`, `:152` and `corpus/fixtures/apk-r65/entry_checks.py:47`. The registry rows need no change (S034 already says 387-399). A wave-2 seat re-running `entry_checks.py --zip-layout` after the edit will still print the same 30/46/22 totals and the same 12 offsets, since the transcription itself is correct.

## 5b. F3 — LOCATED DEFECT (distinct from F1): the S032 header claims a scope its registry row does not carry

F1 is about line arithmetic. This one is about **row scope**, and it is separate.

`corpus/knowledge/round-70-apk-axml-byte-evidence.md:4` is the **S032** `source:` header, and its `scope:` clause claims three layouts:

```
$ sed -n '4p' corpus/knowledge/round-70-apk-axml-byte-evidence.md | grep -o "scope:.*"
scope: the record layouts of §4.3.7 local file header (snapshot lines 387-398), §4.3.12 central directory file header (lines 511-531) and §4.3.16 end of central directory record (lines 632-646) for one authored ZIP archive; ...
```

But the **S032 registry row's scope column** (`corpus/SOURCES.md:46`, column 6) is:

```
central directory file header and end-of-central-directory record field layout for one authored ZIP archive: signature values, field order, length fields, CRC-32 and local-header offset
```

It does **not** include the local file header layout — and the round-63 lesson that opened the row says so explicitly (`corpus/knowledge/round-63-zip-central-directory-evidence.md:675`):

> The row's scope is the central directory file header and end-of-central-directory record field layout and the field meanings above. It is not cited for archive semantics beyond those fields, **for the local file header layout (that is S034)**, for ZIP64, or for any provider's behavior.

The word "local-header offset" in S032's scope column is the *central* header's `relative offset of local header` field (§4.4.16 / live line 538) — a central-directory field, **not** the §4.3.7 local file header layout. Verified:

```
$ awk 'NR==46' corpus/SOURCES.md | tr '|' '\n' | sed -n '6p' | grep -o "local-header offset"
local-header offset
$ awk 'NR==46' corpus/SOURCES.md | tr '|' '\n' | sed -n '6p' | grep -c "local file header"
0
```

So the entry's S032 header claims §4.3.7 under a row that explicitly excludes §4.3.7. The entry's own **S034** header at `:5` gets this right ("scope: §4.3.7 local file header only: the fixed part and the file-name and extra-field length offsets…"), and the registry's S034 row (`corpus/SOURCES.md:48`) carries exactly that scope — so the §4.3.7 claim is *sourced*, but it is sourced to the **wrong row** in the S032 header line. QUALITY.md Q01 requires each load-bearing claim to rest on a tier-A row "for that claim's scope"; the S032 row is not the row for the local file header scope.

This also makes the Q01 row at `:249` imprecise — it says "S032/S034 (ZIP records)", which does not surface which row carries which layout:

```
| Q01 | pass | each load-bearing layout claim rests on a tier-A row for its own scope: ... S032/S034 (ZIP records), ... |
```

**Severity: lower than F1** — no claim is unsourced, both rows are tier A, and the entry cites S034 for §4.3.7 at `:5`. The defect is a scope-misattribution inside one header line, which is exactly the class round-65 routed as D2 (wrong citation) and what QUALITY Q01's "for that claim's scope" clause targets. It is a one-line repair.

**Suggested repair (advisory; I did not apply it):** in the S032 `source:` line at `corpus/knowledge/round-70-apk-axml-byte-evidence.md:4`, drop "§4.3.7 local file header (snapshot lines 387-398), " from the S032 scope clause and leave §4.3.7 to the S034 line at `:5` (which already scopes it correctly); keep §4.3.12 and §4.3.16 under S032, and apply the F1 range widening (`520-538`, `634-646`) there. Alternatively, split the S032 header into two `source:` lines. The registry rows need no change.

## 5c. F4 — the S045 registry row's anchor names the wrong live section (cross-seat, verified here)

Seat `R70W1OpenS045` reported this one; I verified it independently against the live page, and it is a **registry-row** defect (not an entry defect — the C05 entry itself names only `header_item`, not a section).

The S045 row's anchor column (`corpus/SOURCES.md:59`) says:

```
"File layout" → `header_item` field table: checksum row "adler32 checksum of the rest of the file (everything but magic and this field)"; header_size "must be 0x70 (112) bytes (v40 or earlier)"; `ENDIAN_CONSTANT = 0x12345678`; ...
```

In the live page those four phrases are **not** under "File layout" → `header_item`. The live heading structure (fetched 2026-10-25, `sha256 a0457c98c4158d91e85d696e477087ee41e06fe7062d5d12b2c67715cdd606d6`; the live page is not byte-stable across responses, see §3, but its headings and these line numbers are stable):

```
4825 | File layout
4837 | header
4838 | header_item        <- "File layout" only NAMES the header_item type here
...
4964 | Bitfield, string, and constant definitions
5023 | ENDIAN_CONSTANT and REVERSE_ENDIAN_CONSTANT
...
5921 | Items and related structures
5926 | header_item        <- the real header_item field table
```

- checksum row → live line **5949**, under "Items and related structures" → `header_item` (5921/5926), **not** under "File layout"
- signature row → live line **5956**, same section
- header_size "must be 0x70 (112) bytes" → live line **5981**, same section
- `ENDIAN_CONSTANT = 0x12345678` → live line **5035**, under "Bitfield, string, and constant definitions" → "ENDIAN_CONSTANT and REVERSE_ENDIAN_CONSTANT" (4964/5023) — a **different section entirely**, not even a `header_item` section.

So the S045 anchor points a reader at a section that contains only a one-line mention of `header_item` (4838) while the field table it names is 1083 lines later, and the `ENDIAN_CONSTANT` quote is in a third section. The four phrases themselves all locate and are correct — this is a **wrong-section anchor**, the same class as F1 (citation points somewhere other than where the value is), one level up: the defect is in `corpus/SOURCES.md:59`, not in the candidate entry.

**Suggested repair (advisory; I did not apply it):** in the S045 row's anchor column, replace `"File layout" → \`header_item\` field table` with the two real locations — `"Items and related structures" → \`header_item\` (checksum / signature / header_size rows)` and `"Bitfield, string, and constant definitions" → \`ENDIAN_CONSTANT and REVERSE_ENDIAN_CONSTANT\`` (ENDIAN_CONSTANT). Registry-row edits are `status`/`recheck`/`used-by`-only under the append-only rule (CORPUS.md rule 2), so this needs the lane's correction path (a superseding row whose `teaches` opens "supersedes S045 —", or the round lesson's erratum), not an in-place rewrite — flagged, not fixed.

**The same mis-anchor is in the round-67 lesson** (the round that opened S045), so both artifacts carry it and both need the erratum path:

```
$ sed -n '73,75p' corpus/lessons/round-67.md
  `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`). Located quote (≤25 words),
  "File layout" → `header_item` field table, checksum row: "adler32 checksum of the rest of the
  file (everything but magic and this field); used to detect file corruption" (18 words). Seat
```

The quote itself is verbatim and ≤25 words — only the section it is attributed to is wrong.

**Neither artifact is the candidate entry.** Verified at the target commit: the entry's S045 header (`corpus/knowledge/round-70-apk-axml-byte-evidence.md:3`) scopes S045 to "the declared `header_item` field semantics of one authored `classes.dex` member" — naming `header_item`, never a section — and items `:101` / `:119` say only "the four quoted phrases are located by item 11". The entry therefore **inherits** the row's mis-anchor rather than making it; a wave-2 seat must not score F4 as an entry Q02 FAIL.

## 6. F2 — the recorded widths are never re-derived from the APPNOTE bytes by any command (survivor observation)

The transcription in `entry_checks.py` is a hand-written constant table; `--zip-layout` only sums the constants and greps `readout.py` for the resulting literals. Nothing reads `corpus/snapshots/APPNOTE.TXT` to check the widths. Demonstrated by mutation on a scratch copy (lane untouched):

```
$ python3 - <<'EOF'   # in a scratch copy of corpus/
p='corpus/snapshots/APPNOTE.TXT'; b=open(p,'rb').read()
old=b"      file name length                2 bytes\r\n      extra field length              2 bytes\r\n"
new=b"      file name length                9 bytes\r\n      extra field length              9 bytes\r\n"
assert old in b; open(p,'wb').write(b.replace(old,new,1))
EOF
MUTATED APPNOTE.TXT: local name/extra field widths 2 -> 9 bytes (offset of every later field shifts)
b011fb727387745bda00e1c66b7ceaa2aac7e16799de215fdc0a3a21b74143ae  corpus/snapshots/APPNOTE.TXT

$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout
local fixed part: 30 bytes (sum of the transcribed field widths)
...
MATCH local.extra_length: spec offset 28, readout.py literal `u16(apk, lh_off + 28)` present=True
zip_layout_exit=0            <-- SURVIVES a spec that now says 9 bytes

$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes
... all MATCH ... spec_quotes_exit=0

$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
drift entry:219 embedded output line not in recheck stdout: sha256 0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6 174585 bytes corpus/snapshots/APPNOTE.TXT
checked_blocks=22 problems=1
gate_exit=1
```

Reading: `--zip-layout` and `--spec-quotes` both exit 0 on a spec whose field widths were corrupted; only the **digest pin** (`--pins`, item 14) notices, and the embedded-output gate catches it via that pin. The entry is honest that the widths are "manually transcribed" (`:152`) and labels them recorded (`:213`), so this is *not* a false claim — it is a **coverage limit**: no command in the lane re-derives the recorded widths from the snapshot bytes. Q11's "recorded, not re-derived" label is honored; the recorded values happen to be right (verified in §5 against live bytes). I record this as a survivor observation, not a defect: adding a width-vs-snapshot check to `entry_checks.py --zip-layout` would make the recorded values self-policing.

## 7. Gate / lint state on the target bytes (context, unchanged by this seat)

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
checked_blocks=22 problems=0
gate_exit=0
$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
lint_exit=0
```

Working-tree entry sha256 equals the target commit's (`0913f651…`, verified with `git show aa1842f:… | sha256sum`), so the lines cited above are the attack target's bytes.

## 8. Verdict detail

- **Source freshness (S032/S034): OPENED-QUOTE-PRESENT.** Live APPNOTE.TXT is byte-identical to the committed snapshot (sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, 174585 bytes, http 200, fetched 2026-10-25T21:07:14Z and re-fetched 21:12:50Z). Version 6.3.10, revised Nov 01 2022, confirmed at live lines 2 and 4. **No quote is absent.** The registry's 11 located S032/S034 quotes and all 6 item-11 phrases locate in the live bytes.
- **Quote-absence list: empty.**
- **DIFFERS:** only `dex-format.html` (S045) — a rotating CSP nonce at line 8946 and a session/feature-flag blob at line 8951; the live page is not byte-stable across two responses 5 minutes apart. All quoted dex phrases keep identical line numbers (5949 / 5956 / 5981 / 5035) and all 8956 lines match; no load-bearing content changed. The committed snapshot `c0428612…` remains the pinned artifact and the entry's item-14 digest still matches it, so the entry's own pin is intact.
- **Located defect F1 (advisory, wave-1):** `corpus/knowledge/round-70-apk-axml-byte-evidence.md:4` and `:152` and `corpus/fixtures/apk-r65/entry_checks.py:47` cite APPNOTE ranges `387-398 / 511-531 / 632-646`; 5 of the 12 offsets item 12 asserts (local.extra_length @ live 399; central.name_length @532, central.extra_length @533, central.comment_length @534, central.local_header_offset @538) come from lines **outside** those ranges. The cited ranges cannot produce the printed sums (28 and 28 vs the printed 30 and 46; the EOCD range is fine at 22). Correct ranges: `387-399`, `520-538`, `634-646`. Offsets and fixed-part totals are themselves correct. **Independently corroborated by seat `R70W1OpenS045`** (its §4 "D1", same sums; it also cites `.ufo/waves/round-63/build/R63SourceAppnote.md:69` placing "relative offset of local header" at 538, which I verified).
- **Located defect F3 (advisory, wave-1; distinct from F1, scope not arithmetic):** the **S032** `source:` header at `corpus/knowledge/round-70-apk-axml-byte-evidence.md:4` claims "§4.3.7 local file header (snapshot lines 387-398)" in its scope, but the S032 registry row (`corpus/SOURCES.md:46`) scopes S032 to the central-directory header and EOCD only, and the round-63 lesson states S032 "is not cited for … the local file header layout (that is S034)" (`corpus/knowledge/round-63-zip-central-directory-evidence.md:675`). §4.3.7 is correctly scoped on the S034 line at `:5` and sourced by S034's registry row (`:48`), so no claim is unsourced — the defect is that one header line attributes a layout to the row that excludes it (QUALITY Q01 "for that claim's scope"). One-line repair: drop the §4.3.7 clause from the S032 scope clause.
- **Coverage observation F2 (advisory):** no lane command re-derives the recorded APPNOTE widths from the snapshot bytes; `--zip-layout` and `--spec-quotes` both exit 0 on a corrupted spec (only the digest pin catches it).
- **Located defect F4 (advisory, wave-1; cross-seat, verified here):** the **S045 registry row** (`corpus/SOURCES.md:59`) anchors its four quotes at `"File layout" → \`header_item\` field table`, but in the live page the checksum (5949), signature (5956) and header_size (5981) rows are under **"Items and related structures" → `header_item`** (5921/5926) — "File layout" only *names* `header_item` at 4838 — and `ENDIAN_CONSTANT` (5035) is under **"Bitfield, string, and constant definitions" → "ENDIAN_CONSTANT and REVERSE_ENDIAN_CONSTANT"** (4964/5023), a different section entirely. All four phrases locate and are correct; the *anchor* points at the wrong sections. The **same mis-anchor is in the round-67 lesson** that opened S045 (`corpus/lessons/round-67.md:73-75`, verified). Registry/lesson defect, **not an entry defect** — the C05 entry names only `header_item`, never a section (`:3`, `:101`, `:119`), so it inherits the row's anchor and must not be scored as an entry Q02 FAIL. Needs the lane's append-only correction path (CORPUS.md rule 2), not an in-place rewrite.

Wave-1 findings are advisory and are not kill-rule inputs under the frozen contract (`reports/round-70/claims.md`, "Landing order" step 2). F1 and F3 are offered as repairs to apply before the candidate is declared final; F4 needs the registry correction path; F2 is offered as an optional hardening.

## 9. Reproduce

```sh
cd /tmp/revenger-r70-<scratch>
curl -sSL -o APPNOTE.live.txt https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
sha256sum APPNOTE.live.txt /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/snapshots/APPNOTE.TXT
cmp APPNOTE.live.txt /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/snapshots/APPNOTE.TXT && echo IDENTICAL
sed -n '387,400p;511,545p;632,650p' APPNOTE.live.txt   # the three layouts the entry cites
```

Commands recorded: `curl` (pre-existing), `python3` stdlib (pre-existing), `base64`/`tar`/`sha256sum`/`cmp`/`diff` (coreutils, pre-existing). Nothing installed or upgraded.
