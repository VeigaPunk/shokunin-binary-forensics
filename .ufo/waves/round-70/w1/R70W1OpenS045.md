OPENED-QUOTE-PRESENT — all four S045 phrases the C05 v5 candidate relies on locate in the live AOSP DEX-format page fetched today; the live bytes differ from the lane's committed snapshot only in two page-chrome lines (a per-request CSP nonce and one devsite infrastructure line), the spec body is byte-identical.

# R70W1OpenS045 — non-author re-open of source S045 (wave 1, advisory)

Seat: `R70W1OpenS045` · date: 2026-10-25 · lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`
Targets read at `aa1842fac199aa524930e5565ed3715de5f84c6d`; base for comparison `3f5edbc206351232a3d2d801334dd930499ccaf5`.
No file was edited. All scratch under `/tmp/revenger-r70-opens045*` was deleted before returning.

## Verdict

**OPENED-QUOTE-PRESENT** (the four S045 quotes), with **DIFFERS** (chrome-only) for the committed snapshot vs. live, and two additional located defects (D1 cited-range, D2 located-quote locator) that are advisory wave-1 repair items.

## 1. Registry row read first (CORPUS rule 1 subject)

`corpus/SOURCES.md:59` — S045 (parse of the 13-column row):

```
S045 | DEX format specification (Android Open Source Project) — https://source.android.com/docs/core/runtime/dex-format
     | docs | A
     scope: the declared `header_item` field semantics (magic, checksum, signature, file_size,
             header_size, endian_tag) of one authored `classes.dex` member; not dex program validity
             and not general dex parsing
     anchor: "File layout" → `header_item` field table: checksum row "adler32 checksum of the rest
             of the file (everything but magic and this field)"; header_size "must be 0x70 (112)
             bytes (v40 or earlier)"; `ENDIAN_CONSTANT = 0x12345678`;
             snapshot .ufo/waves/round-67/source-snapshots/dex-format.html
             sha256 c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4, 281157 bytes
     teaches: Declares the dex declared-header field semantics the round-67 C05 v2 candidate re-derives
             for one authored member (adler-32 checksum, SHA-1 signature, 0x70 header, endian tag)
     status: mined | opened: 2026-10-24 | recheck: 180d
     used-by: corpus/knowledge/round-67-apk-axml-byte-evidence.md
```

The ≤25-word located quote recorded for the row is in `corpus/lessons/round-67.md:73-75` (URL, access date
2026-10-24, 18-word quote, location `"File layout" → `header_item` field table, checksum row`). Round-67
recorded the same page as STABLE ("only a per-request CSP nonce + one infrastructure line differ",
`corpus/lessons/round-67.md:76-78`).

## 2. Live fetch today (2026-10-25) — what I got

```
$ date -u '+%Y-%m-%dT%H:%M:%SZ'                      # 2026-10-25T21:07:14Z
$ curl -sL --max-redirs 15 -o /tmp/.../dex.html \
    -w 'http=%{http_code} size=%{size_download} url=%{url_effective}\n' \
    'https://source.android.com/docs/core/runtime/dex-format'
http=200 size=281161 url=https://source.android.com/docs/core/runtime/dex-format
sha256 c02780f50ec96c3b6bad185f6d54cf9fd0590e806f5f03b87d833bf9314bc63a  /tmp/.../dex.html
```

Two further fetches minutes later (to separate per-request noise from content):

```
2026-10-25T21:15:38Z  sha256 f9e89e63aedcc7c7a9f0f3119feea2ccd193420f04e4dcff12d5fb099952f254  281161 bytes
sha256 1a59e2a3d21ced67e9cfcacff6a039950f8ee386b1d26315a665566de1503acd  281161 bytes   (fetch #2)
```

The three full-file digests differ from each other and from the committed snapshot; the spec body does not:

```
sha256 spec-body (lines 1-8945) snapshot: 677b8a2b48ca4b0edf0fa5d62d6bd1f65b6217aa744d5c1f0525df45b4a6b8b3
sha256 spec-body (lines 1-8945) live    : 677b8a2b48ca4b0edf0fa5d62d6bd1f65b6217aa744d5c1f0525df45b4a6b8b3
bodies identical: True
differing line indexes (1-based): [8946, 8951]
  8946: '<script nonce="R1GN4pA7+nDrYJ/dulpbEJ8pQlLBzr">'  vs  '<script nonce="22P2wm6dUEfG7VMX3StdBQfKA4ktAz">'
         (fetch #3 nonce 'C3Nn8FHbHwVAqx6B+ZMeN/f7nbU8AI' — changes every request)
  8951: devsite app-loader line (rotating API-key/feature-flag list)
```

**Comparison verdict for the S045 snapshot: DIFFERS — whitespace/infrastructure only, no content change.**
The committed `corpus/snapshots/dex-format.html` is 281157 bytes sha256 `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`,
identical to `git show aa1842f…:corpus/snapshots/dex-format.html` and to `.ufo/waves/round-67/source-snapshots/dex-format.html`
(`cmp` → identical), and identical to the digest printed in the candidate's item 14. The live page's own
"Last updated 2026-10-09 UTC." marker is present twice in both files. This reproduces round-67's STABLE
finding; nothing upstream changed.

The other three committed snapshots were re-fetched live today as the seat brief requires — all byte-identical:

| snapshot | committed sha256 / bytes | live sha256 / bytes | verdict |
|---|---|---|---|
| `corpus/snapshots/ResourceTypes.h` | `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` 86255 | same (decoded from `…ResourceTypes.h?format=TEXT`, 86255) | byte-identical |
| `corpus/snapshots/APPNOTE.TXT` | `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` 174585 | same, 174585 (pkware.cachefly.net, http 200) | byte-identical |
| `corpus/snapshots/rea-android-applications.md` | `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` 1992 | same, 1992 (raw.githubusercontent, tag rea-agents-6.5.0, http 200) | byte-identical |
| `corpus/snapshots/dex-format.html` | `c0428612…` 281157 | `c02780f5…` 281161 | DIFFERS (2 chrome lines) |

Minor note (not a defect in the candidate): the S043 row (`corpus/SOURCES.md:57`) names the path
`skills/reverse-engineer-anything/references/android-applications.md`; at tag `rea-agents-6.5.0` that literal
path 404s (`http=404`, body `404: Not Found`, sha256 `d5558cd419c8d46bdc958064cb97f963d1ea793866414c025906ec15033512ed`),
while the file actually lives at `.agents/skills/reverse-engineer-anything/references/android-applications.md`
(http 200, sha256 `412d9cb4…` = the committed snapshot). The cited *bytes* are right; only the path prefix is stale.

## 3. The sentences the C05 entry relies on, located in the live source

The candidate's S045 header line (`corpus/knowledge/round-70-apk-axml-byte-evidence.md:3` at aa1842f) claims
"the four quoted phrases are located by the item-11 `--spec-quotes` command". Those four phrases are the
dex-format.html MATCH lines in item 11's embedded output (`…entry.md:145-148`).

Located at the live source (line numbers are the live file's own lines; headings are the live file's headings):

| # | quote (≤25 words) | live line | heading path it sits under |
|---|---|---|---|
| Q1 | "adler32 checksum of the rest of the file (everything but magic and this field)" | 5949 | `Items and related structures` (h2, line 5921) → `header_item` (h3, 5926) → "Alignment: 4 bytes" (h4, 5928) field table → **checksum** row (5947-5949) |
| Q2 | "SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)" | 5956 | same `header_item` field table → **signature** row (5953-5956) |
| Q3 | "must be 0x70 (112) bytes (v40 or earlier)" | 5981 | same `header_item` field table → **header_size** row (5974-5981) |
| Q4 | "uint ENDIAN_CONSTANT = 0x12345678;" | 5035 | `Bitfield, string, and constant definitions` (h2, 4964) → `ENDIAN_CONSTANT and REVERSE_ENDIAN_CONSTANT` (h3, 5023) → "Embedded in header_item" (h4, 5024) code block (5034-5037) |

Raw live context for Q1-Q3 (table rows) and Q4 (code block):

```
5926 <h3 id="header-item" ...>header_item</h3>
5946 <tr>
5947   <td>checksum</td>
5948   <td>uint</td>
5949   <td>adler32 checksum of the rest of the file (everything but
5950     <code translate="no" dir="ltr">magic</code> and this field); used to detect file corruption
5953 <tr>
5954   <td>signature</td>
5955   <td>ubyte[20]</td>
5956   <td>SHA-1 signature (hash) of the rest of the file (everything but
5974 <tr>
5975   <td>header_size</td>
5981     <p>must be 0x70 (112) bytes
5982       <span style="float:right">(v40 or earlier)</span>
5034 <div></div><devsite-code><pre ...>
5035 uint ENDIAN_CONSTANT = 0x12345678;
```

Uniqueness at the live source (each phrase occurs exactly once in the whole page):

```
1 <- occurrences of: adler32 checksum of the rest of the file (everything but magic and this field)
1 <- occurrences of: SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)
1 <- occurrences of: must be 0x70 (112) bytes (v40 or earlier)
1 <- occurrences of: uint ENDIAN_CONSTANT = 0x12345678;
count of "<td>checksum</td>": 1   "<td>header_size</td>": 1   "<td>endian_tag</td>": 1
```

**End-to-end re-derivation against live bytes.** I copied the candidate's own checker into scratch, swapped
only `corpus/snapshots/dex-format.html` for today's live fetch, and re-ran it:

```
$ cp …/entry_checks.py /tmp/revenger-r70-opens045/corpus/fixtures/apk-r65/
$ cp /tmp/revenger-r70-opens045-dex.html /tmp/revenger-r70-opens045/corpus/snapshots/dex-format.html
$ cd /tmp/revenger-r70-opens045 && python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes ; echo exit=$?
MATCH rea-android-applications.md: first line 7, folded phrase present=True: Start with `inspect_android_package` …
MATCH dex-format.html: first line 5949, folded phrase present=True: adler32 checksum of the rest of the file (everything but magic and this field)
MATCH dex-format.html: first line 5956, folded phrase present=True: SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)
MATCH dex-format.html: first line 5981, folded phrase present=True: must be 0x70 (112) bytes (v40 or earlier)
MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;
MATCH ResourceTypes.h: first line 686, folded phrase present=True: Byte offset from the start of this structure where the attributes start
exit=0
```

`diff` of that live-run output against the entry's embedded block (`…entry.md:144-149` at aa1842f) is empty:
**IDENTICAL: entry's embedded spec-quotes output == live-source run**. The four quoted line numbers the entry
prints (5949, 5956, 5981, 5035) are the live file's own line numbers today.

## 4. Findings

### D1 (located, coverage/Q11-class) — item 12's cited APPNOTE line ranges cannot produce the sums it prints

* Entry: `corpus/knowledge/round-70-apk-axml-byte-evidence.md:152` (and the S032 header line `:4`) at aa1842f:
  "the layouts are APPNOTE snapshot lines **387-398, 511-531** and 632-646". Same ranges in
  `corpus/fixtures/apk-r65/entry_checks.py:47` (comment above the hardcoded `LOCAL_HEADER`/`CENTRAL_HEADER`/`EOCD`
  width lists — the checker never reads APPNOTE.TXT, so no command can catch this).
* Command (lane snapshot `corpus/snapshots/APPNOTE.TXT`, byte-identical to the live file):

```
$ python3 - <<'EOF'   # sum the "N bytes" width rows inside each cited range
4.3.7 as cited range 387-398: rows=10 sum=28      <- entry prints "local fixed part: 30 bytes"
   cited-range rows end at line 398 -> file name length
   full local header ends: 399 extra field length 2 bytes
4.3.12 as cited range 511-531: rows=10 sum=28     <- entry prints "central fixed part: 46 bytes"
   cited-range rows end at line 531 -> uncompressed size
    532 file name length                2 bytes
    533 extra field length              2 bytes
    534 file comment length             2 bytes
    535 disk number start               2 bytes
    536 internal file attributes        2 bytes
    537 external file attributes        4 bytes
    538 relative offset of local header 4 bytes
4.3.16 as cited range 632-646: rows=8 sum=22      <- entry prints "eocd fixed part: 22 bytes"  (OK)
```

* Why it bites the printed output: the entry's item-12 output claims
  `MATCH central.local_header_offset: spec offset 42` and `MATCH central.fixed_part: spec width 46`.
  Offset 42 is reached only after lines 532-537 (`file name length` → `external file attributes`) are added
  (4+2+2+2+2+2+2+4+4+4+2+2+2+2+2+4 = 42), and width 46 only after line 538
  (`relative offset of local header`, 4 bytes). Both lie **outside** the cited 511-531. Likewise
  `MATCH local.extra_length: spec offset 28` requires line 399, outside the cited 387-398.
* The lane's own registry row S034 (`corpus/SOURCES.md:48`) cites the local-file-header layout as
  "snapshot lines **387-399**", and the round-63 source receipt `.ufo/waves/round-63/build/R63SourceAppnote.md`
  records §4.3.12's "relative offset of local header" at line **538** and §4.3.7's §4.3.12 crc/length rows at
  529-533. So the entry's ranges are narrower than both the registry's own anchor and the round-63 receipt.
* Repair (advisory, wave 1): widen the cited ranges to the lines the widths actually come from —
  §4.3.7 → **387-399**, §4.3.12 → **520-538**, §4.3.16 → **632-646** (already complete) —
  in the entry header line 4, in item 12, and in `entry_checks.py:47`; the printed sums (30/46/22) then match
  their cited ranges. 387-399 (heading-anchored, §4.3.7 heading at 387) is preferred over 389-399 because it
  is the convention the lane's own S034 registry row already uses (`corpus/SOURCES.md:48`, "snapshot lines
  387-399") and it matches the entry's existing heading-anchored EOCD range 632-646; first-field-row anchors
  (389-399 / 522-538 / 634-646) are equally arithmetically correct (same sums 30/46/22) — pick one convention
  and apply it to all three records. Cross-seat note sent to and confirmed by `R70W1OpenS032` (S032 row, whose
  report carries the same defect as its F1); no edit made by either seat.

### D2 (located, coverage) — the S045 row's located-quote locator points at the wrong section of the live page

* Registry row `corpus/SOURCES.md:59` (anchor) and the round-67 lesson `corpus/lessons/round-67.md:73-75`
  both locate the quote under `"File layout" → `header_item` field table`.
* Live page structure (fetched today, identical in the committed snapshot):

```
 4825 <h2 id="file-layout" ...>File layout</h2>            <- the section the locator names
 4836 <tr><td>header</td><td>header_item</td><td>the header</td></tr>   <- only mention of header_item here
 4921 ...
 4964 <h2 ...>Bitfield, string, and constant definitions</h2>
 5023 <h3 ...>ENDIAN_CONSTANT and REVERSE_ENDIAN_CONSTANT</h3>
 5035 uint ENDIAN_CONSTANT = 0x12345678;                 <- Q4 lives here, not in the field table
 5921 <h2 ...>Items and related structures</h2>
 5926 <h3 ...>header_item</h3>                            <- the actual `header_item` field table
 5949 adler32 checksum …                                   <- Q1/Q2/Q3 live here
count of "<td>checksum</td>": 1   (whole page — only one checksum row, at 5947)
```

* The `header_item` field table that carries the checksum / signature / header_size rows is under
  **"Items and related structures" → `header_item`**, not under "File layout" (whose table only names
  `header_item` as the *type* of the `header` field at line 4838). And Q4 (`ENDIAN_CONSTANT = 0x12345678`)
  is in the constants section, not in the field table at all — the field table only references it
  (`endian_tag` row, live lines 5990-5993: "uint = ENDIAN_CONSTANT").
* CORPUS rule 1 (`/home/vgpnk/Projects/shokunin/CORPUS.md:112-115`) requires the recorded location to ground
  the quote; as written, a verifier who follows "File layout → `header_item` field table" lands on a table with
  no checksum row and would record the quote ABSENT. The quotes themselves are present (section 3).
* **Scoping caveat (so wave 2 does not mis-score):** the wrong anchor is in the **registry row**
  (`corpus/SOURCES.md:59`) and the round-67 lesson (`corpus/lessons/round-67.md:73-75`); the candidate entry
  itself never names a section for S045 — entry `:3` scopes it to "the declared `header_item` field semantics"
  and `:101`/`:119` say only "the four quoted phrases are located by item 11". The entry inherits the row's
  mis-anchor rather than making it, so this is a registry/lesson-locator defect, not an entry Q02 FAIL. Confirmed
  by `R70W1OpenS032` (their F4, cross-seat, credited to this seat).
* Repair (advisory): correct the locator to `Items and related structures` → `header_item` field table (checksum /
  signature / header_size rows) and `Bitfield, string, and constant definitions` → `ENDIAN_CONSTANT and
  REVERSE_ENDIAN_CONSTANT` (the constant). Note the row is append-only (CORPUS rule 2, `CORPUS.md:116-118`:
  only `status`, `recheck`, `used-by` change in place), so this is a *new superseding row* (teaches opens
  `supersedes S045 —`) or an amendment recorded in the round lesson, not an in-place edit of `SOURCES.md:59`.

### D3 (advisory, prose/credit class — lower severity) — item 9 over-states the per-field comparison

* Entry `…entry.md:101`: "Each declared field is compared with the field semantics S045 states (the four
  quoted phrases are located by item 11); a match between a declared value and its recomputation shows the
  member's header is internally consistent".
* The item-9 output (`…entry.md:104-105`) prints the dex header values
  (`magic_hex, magic_ascii, format_version, declared_checksum, checksum_recomputed, signature_sha1,
  signature_recomputed, file_size, header_size, endian_tag, header_bytes`) but only **two** comparison flags
  exist in the whole readout — `checksum_matches` and `signature_matches`
  (`corpus/fixtures/apk-r65/readout.py:242,245`) — and both are *recomputation* matches, not comparisons
  against the quoted S045 phrases. `magic`, `format_version`, `file_size` and `header_bytes` have no quoted
  S045 phrase among the four, and the entry's own S045 scope line (`:3`) names only
  "(checksum, signature, header_size, endian_tag)".
* The narrower statement is already carried by the Inference section `(d)` at `…entry.md:234`
  ("the dex header's declared checksum, signature, size and endian fields agree with S045's field semantics
  as quoted"). Repair: align item 9's wording with that scope (four fields; two recomputation matches printed),
  or print the per-field comparisons.

### D4 (advisory, note only — landing-order item, not a wave-1 defect)

`corpus/SOURCES.md:59` still carries `used-by: corpus/knowledge/round-67-apk-axml-byte-evidence.md` and
`recheck: 180d`, while the candidate at aa1842f cites S045 in its header (`:3`) and item 11. Per the frozen
claims (`reports/round-70/claims.md`, "Frontier step and assimilation": "with the S045 row's `used-by`
re-pointed old→new at admission"), the re-point is an admission-time (landing-order step 4) action, so it is
correctly still pending at candidate stage. Flagged only so wave 2 checks it at the final tip.

### D5 (cross-seat, independently confirmed here; owner `R70W1OpenS032` F3) — S032 scope clause claims §4.3.7, which S032's row excludes

* The candidate's S032 header line (`…entry.md:4` at aa1842f) puts "§4.3.7 local file header (snapshot lines
  387-398)" in the **S032** scope clause, but S032's registry scope excludes that layout: the S032 scope cell
  (`corpus/SOURCES.md:46`) reads "central directory file header and end-of-central-directory record field
  layout … CRC-32 and local-header offset" and contains no "local file header" phrase
  (`grep -c "local file header"` on that cell → 0), while `corpus/knowledge/round-63-zip-central-directory-evidence.md:675`
  states S032 "is not cited for … the local file header layout (that is S034)". The candidate's own S034 line
  (`:5`) scopes §4.3.7 correctly, so nothing is unsourced — the defect is the attribution on line 4.
* Verified by me independently of the reporting seat (same commands above). Repair is a separate one-line edit
  on the same entry line 4 as D1's range widening — the two must not collide in one edit; D1 changes the range
  strings, D5 drops the §4.3.7 clause from the S032 scope clause.

## 5. What I could not check

* `corpus/lessons/round-70.md` does not exist at aa1842f (`git cat-file -e` → "path does not exist"), so the
  round-70 Gate block that must carry this re-open record (URL, access date 2026-10-25, ≤25-word located quote)
  is not yet present; my §3 table is the material for it. This is a frontier-step item, not a claim conjunct.
* Wave-2 seat decisions on the landed bytes are out of scope for this seat.
* The `<25-word` count of the round-67 lesson quote is recorded there as 18 words; whitespace counting gives 19
  ("field);" counted as one token). Either way it is ≤25, so CORPUS rule 1 is satisfied — noted only to avoid
  a later seat re-litigating it.

## 6. Commands run (all read-only; no mutation in the lane or fleet)

```
curl -sL --max-redirs 15 https://source.android.com/docs/core/runtime/dex-format        (x3, 2026-10-25 21:07-21:15Z)
curl -sL --max-redirs 15 https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
curl -sL --max-redirs 15 https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h?format=TEXT
curl -sL --max-redirs 10 https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md
sha256sum / cmp / diff / python3 (stdlib only) — no packages installed, no host services touched
git -C <lane> show aa1842f…:<path> | git -C <lane> cat-file -e …  (read-only)
```

Tooling: no tool was installed or updated for this seat (curl, git and Python 3 stdlib were already present);
nothing was recorded for the operator install log.
