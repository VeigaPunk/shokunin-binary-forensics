# R63SourceAppnote — S032 PKWARE APPNOTE (ZIP file format specification)

Seat: `revenger-r63.R63SourceAppnote` (scribe, build wave, round 63).
Date opened: **2026-10-23**. Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## Behavior

Opened the PKWARE `.ZIP` File Format Specification, saved a byte-exact plain-text
snapshot at the requested path, extracted the located quotes the C06 candidate
entry needs to rest on, and drafted the `S032` registry row plus its Gate record
for L1 integration.

Nothing outside the two paths named in this item was written: no `corpus/SOURCES.md`
edit (L1 is sole integrator — confirmed by `revenger-r63.R63SourcesRows`), no
`corpus/knowledge/` write, no `corpus/live` or `corpus/fixtures` byte touched, no
target execution, no `README`/`QUALITY.md` edit.

## Snapshot

| field | value |
|---|---|
| path | `.ufo/waves/round-63/source-snapshots/appnote.txt` |
| final URL | `https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT` (no redirect; `url_effective` identical to request) |
| HTTP status | **200** |
| content-type / length | `text/plain` / 174585 |
| server `Date` | `Sat, 24 Oct 2026 02:21:34 GMT` |
| server `Last-Modified` | `Tue, 01 Nov 2022 17:34:41 GMT` |
| `ETag` | `"636158b1-2a9f9"` |
| access date | **2026-10-23** (local lane date; the `Date` header is 2026-10-24 02:21 GMT) |
| spec version | **6.3.10**, Status `FINAL - replaces version 6.3.9`, Revised `Nov 01, 2022` |
| bytes | 174585 |
| **sha256** | **`0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`** |

The snapshot is **byte-exact as served** (ASCII, CRLF line terminators); the sha256
above is of the served bytes, so it re-verifies by re-fetching the URL. A
sidecar `.ufo/waves/round-63/source-snapshots/appnote.provenance.json` records the
same facts in machine-readable form. (LF-normalized variant, for diff-friendly
reading only, sha256 `7dc242eb53db6d95176bd335b03470a143e1ac4a6cb39396f76e8cc56b1ffc0e`
— not the pinned file.)

### Fallback URL — recorded divergence

`https://pkware.com/documents/casestudies/APPNOTE.TXT` returns **HTTP 200** but
redirects to
`https://pkwaredownloads.blob.core.windows.net/pkware-general/Documentation/APPNOTE-6.3.9.TXT`,
which is a **different revision**: version **6.3.9**, revised Jul 15 2020,
173575 bytes, sha256 `c7cf1fecfbde36ebbfbac643e6183d5c76fac983c2066fb8e32c6e4058a87e80`.

All six sections quoted below were diffed between the two revisions and are
**byte-identical**, so the located quotes are stable across the redirect. The
S032 row anchors to the primary URL and the 6.3.10 revision, which is the
revision actually opened and snapshotted.

## Located quotes (load-bearing, each ≤25 words, verbatim)

Line numbers are 1-based lines of the snapshot `appnote.txt`.

| id | section | line(s) | quote (verbatim, ≤25 words) |
|---|---|---|---|
| Q1 | §4.3.12 Central directory structure | 522 | `central file header signature   4 bytes  (0x02014b50)` |
| Q2 | §4.3.12 (field order, crc-32 → lengths) | 529–533 | `crc-32 4 bytes compressed size 4 bytes uncompressed size 4 bytes file name length 2 bytes extra field length 2 bytes` |
| Q3 | §4.4.10–4.4.12 | 941 | `The length of the file name, extra field, and comment fields respectively.` |
| Q4 | §4.4.16 relative offset of local header | 983–985 | `This is the offset from the start of the first disk on which this file appears, to where the local header SHOULD be found.` |
| Q5 | §4.3.16 End of central directory record | 634 | `end of central dir signature    4 bytes  (0x06054b50)` |
| Q6 | §4.3.16 (both total-entries fields) | 638–641 | `total number of entries in the central directory on this disk 2 bytes total number of entries in the central directory 2 bytes` |
| Q7 | §4.4.22 total number of entries in the central dir | 1043 | `The total number of files in the .ZIP file.` |
| Q8 | §4.4.7 CRC-32 (bit-3 exception) | 911–912 | `If bit 3 of the general purpose flag is set, this field is set to zero in the local header and the correct` |
| Q9 | §4.4.7 CRC-32 (where the value lives) | 912–913 | `value is put in the data descriptor and in the central` |
| Q10 | §4.3.12 (offset field, last fixed field) | 538 | `relative offset of local header 4 bytes` |
| Q11 | §4.3.3 byte order | 350–351 | `All values MUST be stored in little-endian byte order unless otherwise specified in this document for a specific data element.` |
| Q12 | §4.4.7 CRC-32 (algorithm constant) | 906 | `the CRC is 0xdebb20e3.` |

### Derived field offsets (arithmetic on the §4.3.12 / §4.3.16 fixed-header field lists)

Summing the byte widths listed in §4.3.12 gives a **46-byte** fixed central
directory file header; summing §4.3.16 gives a **22-byte** fixed end-of-central-directory
record.

Central directory file header (§4.3.12), offsets from the header start:

| off | len | field | off | len | field |
|---|---|---|---|---|---|
| 0 | 4 | central file header signature `0x02014b50` | 28 | 2 | file name length |
| 4 | 2 | version made by | 30 | 2 | extra field length |
| 6 | 2 | version needed to extract | 32 | 2 | file comment length |
| 8 | 2 | general purpose bit flag | 34 | 2 | disk number start |
| 10 | 2 | compression method | 36 | 2 | internal file attributes |
| 12 | 2 | last mod file time | 38 | 4 | external file attributes |
| 14 | 2 | last mod file date | 42 | 4 | relative offset of local header |
| 16 | 4 | **crc-32** | | | |
| 20 | 4 | compressed size | | | |
| 24 | 4 | uncompressed size | | | |

End of central directory record (§4.3.16), offsets from the EOCD start:

| off | len | field | off | len | field |
|---|---|---|---|---|---|
| 0 | 4 | end of central dir signature `0x06054b50` | 10 | 2 | total number of entries in the central directory |
| 4 | 2 | number of this disk | 12 | 4 | size of the central directory |
| 6 | 2 | number of the disk with the start of the central directory | 16 | 4 | offset of start of central directory |
| 8 | 2 | total number of entries in the central directory on this disk | 20 | 2 | .ZIP file comment length |

The `crc-32` at offset 16 and `relative offset of local header` at offset 42 are
**derivable from the spec's own field list**, not from any implementation — that
is the property the C06 entry needs, since it is a manual byte-derived readout.

## Gate record (for `corpus/lessons/round-63.md` `## Gate`)

- **S032** — PKWARE APPNOTE.TXT, `.ZIP` File Format Specification — <https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT> — spec, tier A — accessed **2026-10-23**, HTTP **200**, version **6.3.10** (revised Nov 01, 2022), snapshot `.ufo/waves/round-63/source-snapshots/appnote.txt` sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`.
  - §4.3.12: "central file header signature   4 bytes  (0x02014b50)"
  - §4.3.12: "crc-32 4 bytes compressed size 4 bytes uncompressed size 4 bytes file name length 2 bytes extra field length 2 bytes"
  - §4.4.16: "This is the offset from the start of the first disk on which this file appears, to where the local header SHOULD be found."
  - §4.3.16: "end of central dir signature    4 bytes  (0x06054b50)"
  - §4.3.16: "total number of entries in the central directory on this disk 2 bytes total number of entries in the central directory 2 bytes"
  - §4.4.7: "If bit 3 of the general purpose flag is set, this field is set to zero in the local header and the correct value is put in the data descriptor and in the central directory."
  - §4.3.3: "All values MUST be stored in little-endian byte order unless otherwise specified in this document for a specific data element."

## Draft SOURCES.md row (S032) — L1 appends verbatim

Contract v1 shape: 11 columns. Single physical line, `NF=13` under the census
awk, no `|` inside any cell. Validated against the census commands copied from
`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`: rows 32, malformed 0, duplicate ids
none, enum violations none, tier inflation none.

```markdown
| S032 | PKWARE APPNOTE.TXT — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT | spec | A | central directory file header and end-of-central-directory record field layout for one authored ZIP archive: signature values, field order, length fields, CRC-32 and local-header offset | §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022) | The central directory header is a fixed 46-byte record whose crc-32 sits at offset 16 and whose relative offset of local header sits at offset 42, and the end of central directory record is a fixed 22-byte record whose two total-entries counts sit at offsets 8 and 10, so a byte readout of an archive can be checked field by field against the specification. | queued | 2026-10-23 | on-release | — |
```

Column-by-column:

| column | value |
|---|---|
| id | `S032` |
| source | `PKWARE APPNOTE.TXT — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT` |
| kind | `spec` |
| tier | `A` (primary/authoritative for this scope: the format's own specification) |
| scope | central directory file header and end-of-central-directory record field layout for one authored ZIP archive: signature values, field order, length fields, CRC-32 and local-header offset |
| anchor | `§4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022)` |
| teaches | The central directory header is a fixed 46-byte record whose crc-32 sits at offset 16 and whose relative offset of local header sits at offset 42, and the end of central directory record is a fixed 22-byte record whose two total-entries counts sit at offsets 8 and 10, so a byte readout of an archive can be checked field by field against the specification. |
| status | `queued` |
| opened | `2026-10-23` |
| recheck | `on-release` |
| used-by | `—` |

Status `queued` (not `mined`) is the correct value on arrival per contract v1
(`queued` = opened, worth mining; `mined` = cited by ≥1 path in `used-by`). When
L1 lands the C06 entry, `status` → `mined` and `used-by` →
`corpus/knowledge/round-63-zip-central-directory-evidence.md`; contract v1 rule 2
requires that in-place change be logged old→new in the round lesson.

## Scope bound — what this source does *not* license

The S032 row is scoped to the two fixed records' field layout. It does not
license, and this seat makes no claim about: a general ZIP parser claim; trailing
bytes after the EOCD; provider completeness (`rea-agents` `inspect-*` output
coverage); authenticity or provenance of an archive; compression-method
semantics beyond the recorded field; or ZIP64 (the spec's ZIP64 records,
§4.3.14/§4.3.15, are explicitly out of this row's anchor and out of the fixture's
scope — the fixture is a plain, non-ZIP64 archive).

## Independent corroboration (read-only, no claim extended)

Read-only decode of the authored fixture `corpus/fixtures/archive-r2/fixture.zip`
(sha256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`, 2964
bytes) at the spec offsets above yields, in both central directory headers:

- `bin/checksum` — crc-32 `0xb3df9ea7`, compressed 2668, uncompressed 16160, name len 12, extra len 0, comment len 0, local-header offset 0
- `README.txt` — crc-32 `0x72a557b1`, compressed 78, uncompressed 84, name len 10, extra len 0, comment len 0, local-header offset 2710

and in the EOCD at file offset 2942: signature `0x06054b50`, total-entries-on-disk
= 2 (offset 8), total-entries = 2 (offset 10), central-directory size 114,
central-directory offset 2828, comment length 0. The sizes agree with
`corpus/fixtures/archive-r2/truth.json` (`compressed_size` 2668 / 78,
`size` 16160 / 84) and the archive sha256 agrees with `truth.json`
`archive_sha256`.

This corroboration is **recorded as evidence that the spec offsets apply to this
fixture**; the field *values* are the C06 entry's claim (`R63EntryC06` /
`R63ZipReadout`), not this seat's. Nothing here was written to `corpus/`.

## Gates checked (exercised)

- Primary URL HTTP 200; body is `text/plain`; `url_effective` == request URL (no redirect).
- Re-fetch of the primary URL reproduces sha256 `0b993022…` exactly (two independent fetches agree) — the snapshot is the served bytes.
- Fallback URL HTTP 200 but serves revision 6.3.9 (different sha256, different byte count); every quoted section compared byte-for-byte across the two revisions and identical.
- All twelve quote strings verified as verbatim substrings of the whitespace-normalized snapshot text (each `found=True`), each ≤25 words (longest is Q4/Q6 at 24/23).
- Draft S032 row validated against the contract-v1 census: 32 rows, 0 malformed, 0 duplicate ids, 0 enum violations, 0 tier inflation, `NF=13`.
- Snapshot decoded at the spec-derived offsets agrees with `truth.json` (sizes and archive digest).

## Tooling

No tools installed or upgraded. No `pacman`, `uv`, `npm` or binary installs were
needed or performed; the only network access was two `curl` GETs (primary +
fallback) and two verification re-fetches of the primary URL, plus one HEAD for
response headers. No `~/.omp/agent/config.yml` or routing-table edit. No model
arguments were set.

## Out of scope / not done (deliberately)

- `corpus/SOURCES.md` was **not** edited — L1 (`revenger-r63`) is the sole
  integrator; `revenger-r63.R63SourcesRows` (reviewer) confirmed this in-band.
- `corpus/lessons/round-63.md` was **not** created — `R63LessonDraft` owns it;
  the Gate record above is handed over as text.
- `corpus/knowledge/round-63-zip-central-directory-evidence.md` was **not**
  created — `R63EntryC06` owns it.
- No `README` C06 flip (L1 owns it, and only after fresh falsify-wave Q01–Q13
  pass decisions land).
- No `QUALITY.md` edit (Q01–Q13 never weakened).
- The S033 (Python `zipfile` docs) row was **screened and excluded** by
  `revenger-r63.R63SourceZipfileDocs` — that page defers format semantics to
  PKWARE APPNOTE ("Any advanced use of this module will require an
  understanding of the format, as defined in PKZIP Application Note.", module
  introduction, 19 words), so it is a pointer to S032 rather than a second
  authority. S033 therefore remains free for L1 to assign to the own-work bundle
  row. This is recorded, not re-litigated: my row does not depend on S033.

## Manifest — created by this seat

`revenger-r63.R63SourceZipfileDocs` confirmed in-band that it does **not** own
the shared `source-snapshots/manifest.json` (its item names only its own
snapshot path and its report path), so this seat created
`.ufo/waves/round-63/source-snapshots/manifest.json` in the round-62 field
shape, covering all three snapshots in the directory:

| file | bytes | sha256 | url |
|---|---|---|---|
| `appnote.txt` | 174585 | `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` | `https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT` |
| `zipfile.html` | 139782 | `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739` | `https://docs.python.org/3/library/zipfile.html` |
| `rea-firmware-guide.md` | 15474 | `d4a25c8569b37c3d030431333db08fc459af54a163af7815b4505cce2f16a898` | `https://raw.githubusercontent.com/morluto/rea/main/docs/firmware-analysis.md` |

Every manifest entry was re-verified against the bytes on disk (bytes and
sha256 both match, all three `OK`). The manifest also carries the extra fetch
fields for each source (status, final URL, `Last-Modified`, `ETag`) plus the
APPNOTE fallback-revision divergence, and marks `zipfile.html` /
`rea-firmware-guide.md` as **no registry row**.

Per-seat provenance sidecars coexist with the manifest and are not listed in it:
`appnote.provenance.json` (mine) and `zipfile.provenance.json`
(`R63SourceZipfileDocs`).

## Artifacts

| path | what |
|---|---|
| `.ufo/waves/round-63/source-snapshots/appnote.txt` | byte-exact APPNOTE.TXT 6.3.10 snapshot, sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` |
| `.ufo/waves/round-63/source-snapshots/appnote.provenance.json` | URL / status / date / sha256 sidecar for the APPNOTE fetch |
| `.ufo/waves/round-63/source-snapshots/manifest.json` | round-63 source-snapshot manifest, all three entries re-verified against disk bytes |
| `.ufo/waves/round-63/build/R63SourceAppnote.md` | this report |
