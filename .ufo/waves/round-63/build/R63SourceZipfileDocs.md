# R63SourceZipfileDocs — is Python's `zipfile` documentation a second source for the C06 entry?

Seat: `R63SourceZipfileDocs` (scribe, coverage axis). Scope: the single decision named in
the item — open `https://docs.python.org/3/library/zipfile.html`, pin it, and decide whether
the C06 candidate entry needs it as a source row. **No `corpus/` byte was changed; no row
was written; nothing was committed.** The snapshot was written to the path the item names
(`.ufo/waves/round-63/source-snapshots/zipfile.html`); this report is the second file.

## 1. Decision

**Screened and excluded — NO S033 row.**

Rationale, in the item's own terms: the C06 entry's build recipe (frozen in
`reports/round-63/claims.md` C1 and repeated in the build-spec item
`R63EntryC06`) declares its sources as *"S032 + APPNOTE URL + section anchors; and the
own-work inputs `corpus/fixtures/archive-r2` fixture.zip + truth.json,
`corpus/live/runs/20261012T164246Z/artifact-inspection.json`"* — a ZIP **spec** row plus
own-work bytes. That recipe sentence cites **no zipfile semantics**, and the entry's
derivation is raw `struct` reads over the fixture bytes, so no entry sentence credits
Python `zipfile` behavior. Per the item, absence from the registry with a search-log note
is the cleaner outcome; a rejected row would additionally need a grounded reject reason
(Q12) and a flip that the source could actually satisfy — which this page cannot.

**Contingency (does not change the decision):** `corpus/fixtures/archive-r2/truth.json`
carries a `build` field that *does* name zipfile semantics
(`"Python zipfile.ZipFile(mode=w, compression=ZIP_DEFLATED, compresslevel=9); write
checksum as bin/checksum; writestr README.txt as stated"`). If the integrated entry asserts
any claim about **zipfile module behavior** (e.g. what `ZIP_DEFLATED` or `compresslevel=9`
mean) rather than quoting that string as a *recorded* oracle label, the exclusion would be
wrong and the drafted row in §7 must be landed instead. L1 owns that call at
integration; §7 is copy-paste ready.

**Contingency closed (verified after the candidate landed):** the integrated entry does
**not** quote the `build` field and asserts no zipfile behavior — it cites S032 (spec) and
the own-work row only, and its own §Sources records this seat's screened-and-excluded
decision. The exclusion therefore stands on the entry's own text, and §7's row is **not
needed and not to be landed** this round. See §9a.

**S033 id availability (asked by `R63EntryC06`):** `S032` = PKWARE APPNOTE
(`R63SourceAppnote`). Because I write no S033, **`S033` stays free**; recommend L1 assign
it to the own-work bundle row (archive-r2 `fixture.zip` + `truth.json` + the saved
`20261012T164246Z/artifact-inspection.json`) that the entry needs under Q01, and have the
entry cite that id as L1-assigned (or cite the own-work inputs by path anchor with the id
marked L1-assigned). I do not own that row's text.

**RESOLVED (L1, 2026-10-23):** L1 took that recommendation — the own-work row lands as
**S033** (next-unused per contract v1) and the entry's S034 mentions are renumbered to
S033 (correction N1 to `R63EntryC06`). The round's ids are the contiguous pair S032 + S033
and no id is skipped or reserved for a zipfile-docs row. The screened-and-excluded
zipfile documentation stays in the search log with no row.

## 2. The open, pinned

| item | value |
|---|---|
| URL requested | `https://docs.python.org/3/library/zipfile.html` |
| final URL (after `-L`) | `https://docs.python.org/3/library/zipfile.html` (no redirect) |
| HTTP status | `200` |
| HTTP `last-modified` | `Sat, 24 Oct 2026 00:16:18 GMT` |
| HTTP `etag` | `"6adbf8d2-22206"` |
| access date (host local, UTC-03) | `2026-10-23` (fetch at `2026-10-24T02:21:51Z`) |
| snapshot path | `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/source-snapshots/zipfile.html` |
| snapshot bytes | `139782` |
| snapshot sha256 | `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739` |
| docs version string (title) | `zipfile — Work with ZIP archives — Python 3.15.1 documentation` |
| page footer date | `Last updated on Oct 24, 2026 (00:13 UTC).` |
| recheck cadence | `on-release` (the `/3/` path is a moving "current stable" alias; today it serves 3.15.1) |

Commands and outputs:

```text
$ curl -sS -L -o .ufo/waves/round-63/source-snapshots/zipfile.html \
    -w 'http=%{http_code} url=%{url_effective} size=%{size_download}\n' \
    https://docs.python.org/3/library/zipfile.html
http=200 url=https://docs.python.org/3/library/zipfile.html size=139782

$ sha256sum .ufo/waves/round-63/source-snapshots/zipfile.html
9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739  .ufo/waves/round-63/source-snapshots/zipfile.html

$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-24T02:21:51Z

$ curl -sS -L -D headers.txt -o /dev/null https://docs.python.org/3/library/zipfile.html
HTTP/2 200
server: nginx
content-type: text/html
last-modified: Sat, 24 Oct 2026 00:16:18 GMT
etag: "6adbf8d2-22206"
content-length: 139782
```

Cross-check (independent read of the same snapshot on disk, twice, agreeing):

```text
$ sha256sum .ufo/waves/round-63/source-snapshots/zipfile.html
9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739  ...
$ stat -c 'bytes=%s' .ufo/waves/round-63/source-snapshots/zipfile.html
bytes=139782
$ head -c 120 .ufo/waves/round-63/source-snapshots/zipfile.html
<!DOCTYPE html>
```

## 3. Why the page is not load-bearing

Three independent grounds, each observable in the snapshot:

**(a) The page refuses to be a format authority — it points at APPNOTE.** Located quote
(module introduction, 19 words):

> Any advanced use of this module will require an understanding of the format, as defined in PKZIP Application Note.

The page links "PKZIP Application Note" to
`https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT` (three occurrences of that
href in the snapshot) — i.e. to the very source that is already S032. A second source that
defers to the first is not an independent authority for the field layout; it is a pointer.
Drafting a docs row here would also create a near-duplicate scope with S032 (the same
W04 shape the census already discloses for S024/S028/S029).

**(b) The entry's derivation never touches the module.** The two readouts in this round
use raw `struct` reads plus `zlib` inflate and never import the module:

```text
$ python3 - <<'PY'   # over both readout scripts
.ufo/waves/round-63/build/zip-readout.py | import zipfile: False | mentions zipfile: 0
/tmp/revenger-r63-entry/readout.py        | import zipfile: False | mentions zipfile: 0
PY
$ grep -rln 'import zipfile' .ufo/waves/round-63/ /tmp/revenger-r63-entry/   # -> no hits
```

The peer readout report agrees: *"stdlib only; no `zipfile` API"*
(`.ufo/waves/round-63/build/R63ZipReadout.md`). The saved-record correspondence and the
truth.json comparison use only the fixture bytes and the saved JSON.

**(c) Every format fact the entry asserts is already covered at tier A by S032.** The
claims the entry makes — central-directory record layout, EOCD record fields and counts,
general-purpose bit flag, compression method, CRC-32 — are the exact sections of APPNOTE
6.3.10 that the S032 seat is pinning. Verified present in the pinned APPNOTE snapshot
(`source-snapshots/appnote.txt`, sha256
`0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, 174585 bytes,
"Version: 6.3.10 … Revised: Nov 01, 2022"):

| entry claim | APPNOTE 6.3.10 section (in the pinned snapshot) |
|---|---|
| central-directory structure & record fields | `4.3.12  Central directory structure:` (line 511) |
| EOCD record: signature `0x06054b50`, disk numbers, entries on this disk, total entries, CD size, CD offset, comment length | `4.3.16  End of central directory record:` (line 632) |
| general-purpose bit flag (incl. bit 11 UTF-8/EFS, bits 1–2 for methods 8/9) | `4.4.4 general purpose bit flag: (2 bytes)` (line 767) |
| compression method, `8 - The file is Deflated` | `4.4.5 compression method: (2 bytes)` (line 854) |
| CRC-32 field | `4.4.7 CRC-32: (4 bytes)` (line 900) |

The zipfile page covers the *same* territory only through the module's Python API
(`ZipInfo.CRC` — "CRC-32 of the uncompressed file"; `ZipInfo.header_offset` — "Byte offset
to the file header"; `zipfile.ZIP_DEFLATED` — "The numeric constant for the usual ZIP
compression method."), i.e. it restates the spec in Python terms rather than adding a
format fact. Restating the spec in Python terms is exactly what would make a docs row a
second, weaker copy of S032.

**(d) The claims.md scope bar.** C1's scope sentence already excludes the territory a
module-semantics row would open: *"no general ZIP parser claim, no trailing-bytes claim,
no provider-completeness claim, no authenticity claim"*, and the entry's scope is
"authored-bytes ↔ spec-field ↔ saved-record correspondence for this one fixture".

## 4. What the page *does* state (for the record, not a claim)

Located ≤25-word quotes with their location in the snapshot (offered so a reviewer can
check the exclusion, and so §7's row is grounded if L1 takes the contingency branch):

| # | quote (words) | location |
|---|---|---|
| Q1 | "Any advanced use of this module will require an understanding of the format, as defined in PKZIP Application Note." (19) | module introduction |
| Q2 | "The numeric constant for the usual ZIP compression method." (9) | `zipfile.ZIP_DEFLATED` |
| Q3 | "The compresslevel parameter controls the compression level to use when writing files to the archive." (15) | `ZipFile.__init__` `compresslevel` parameter |
| Q4 | "CRC-32 of the uncompressed file" (5) | `zipfile.ZipInfo.CRC` |
| Q5 | "Byte offset to the file header" (6) | `zipfile.ZipInfo.header_offset` |
| Q6 | "This module provides tools to create, read, write, append, and list a ZIP file." (14) | module introduction |

Q1 is the decisive one for this decision; Q2/Q3 are the two that would be needed only by
the contingency branch.

## 5. The truth.json build-recipe sentence (the one place zipfile semantics appear)

`corpus/fixtures/archive-r2/truth.json` line 19:

```json
"build": "Python zipfile.ZipFile(mode=w, compression=ZIP_DEFLATED, compresslevel=9); write checksum as bin/checksum; writestr README.txt as stated"
```

Facts about it, each observed:

* It is a **recorded label inside the oracle file** the entry already cites as an own-work
  input — not a value the entry re-derives from bytes. Under Q11 such a string is
  *recorded, not re-derived*, and its support is the own-work truth.json row, not an
  external module manual.
* Nothing in the entry's *measurement* chain depends on it. The EOCD location `2942`, the
  counts `2/2`, the CD offset `2828`, per-member name/offset/sizes/CRC-32 and the
  recomputed inflated SHA-256s all come from the fixture bytes by `struct`/zlib; the
  peer pack (`.ufo/waves/round-63/build/zip-readout.out`) shows every comparable field
  `True` against truth.json with `N/A` where truth.json records no value.
* The two places a *semantic* zipfile claim could sneak in are (i) "ZIP_DEFLATED
  produced method 8" and (ii) "compresslevel=9 explains the compressed sizes". Neither is
  a claim the frozen entry scope makes, and (i) is already answerable from APPNOTE
  `4.4.5` (`8 - The file is Deflated`) without the docs page. The zipfile page does not
  even state the numeric value of `ZIP_DEFLATED`, so it could not settle (i) on its own.

**Consequence for L1:** if the integrated entry repeats that `build` string as a quoted
oracle label, no row is needed. If it turns it into a claim about the module, land §7.

## 6. Exact search-log text (for L1 to append to `corpus/SOURCES.md` `## Search log`)

**STATUS (L1, 2026-10-23): DROPPED in favour of `R63LessonDraft`'s archive-spec note.**
L1's decision is to use the lesson's search-log note — it is the more recent version and
it reconciles the APPNOTE fallback-revision exclusion that my block omits — and to carry
only the **snapshot digest** from this block into the round's `## Gate` record. The block
is retained below verbatim for that purpose (and as the record of what this seat proposed);
it is **not** to be appended to `corpus/SOURCES.md` as a second note.

Append-only prose, matching the existing 2026-10-19/21 note style (query / where / date /
counts / exclusion reason / stop / openers). Counts use the round-62 document-set
convention (own-work bundle counted once, inside identified):

```text
- 2026-10-23, round-63 ZIP central-directory readout (row C06). Query: the primary specification of the ZIP central-directory and end-of-central-directory record layout, and whether Python's zipfile module documentation is a second authority for it. Where: pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, opened 2026-10-23, snapshot sha256 0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6), docs.python.org/3/library/zipfile.html (docs, opened 2026-10-23, snapshot sha256 9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739), and the lane's own archive-r2 fixture bytes, truth.json and the saved 20261012T164246Z inspection record. Identified 3, screened 3, included 2 rows (S032 APPNOTE plus the own-work fixture/saved-record row), excluded 1 without a row: docs.python.org/3/library/zipfile.html - the C06 readout is raw struct reads over the fixture bytes, every format claim it makes rests on APPNOTE 6.3.10 sections 4.3.12, 4.3.16, 4.4.4, 4.4.5 and 4.4.7, and the page itself defers format questions to that same specification ("Any advanced use of this module will require an understanding of the format, as defined in PKZIP Application Note."), so it is a pointer rather than a second authority and no entry sentence credits zipfile behavior. Stop: one tier-A specification covers every field the readout derives, and the entry's own-work inputs cover the byte and saved-record layers. Openers: R63SourceAppnote (APPNOTE), R63SourceZipfileDocs (zipfile documentation, screened and excluded).
```

One-line exclusion reason for the round lesson `## Gate` (asked by `R63LessonDraft`):

```text
Excluded without a row: docs.python.org/3/library/zipfile.html (opened 2026-10-23, snapshot sha256 9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739) - the C06 readout is raw struct reads and every format claim rests on PKWARE APPNOTE 6.3.10 (S032), which the zipfile page itself names as the format authority; no entry sentence credits zipfile behavior.
```

Lesson `## Gate` facts to record if the exclusion is landed: URL
`https://docs.python.org/3/library/zipfile.html`, access date `2026-10-23`, snapshot
sha256 `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`, and quote Q1
(19 words, module introduction) as the ground for the exclusion.

**L1's placement decision (2026-10-23):** the search-log note is the lesson's version
(§6 block dropped); the **snapshot digest** above lands in the round's `## Gate` record,
i.e. in the lesson's zipfile-docs paragraph. The Gate record for the excluded source
therefore carries: URL `https://docs.python.org/3/library/zipfile.html`, access date
`2026-10-23`, snapshot sha256
`9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739` (139782 bytes), and
the 19-word located quote "Any advanced use of this module will require an understanding
of the format, as defined in PKZIP Application Note." (module introduction) as the ground
for the exclusion. `R63LessonDraft`'s draft already carries my exclusion line and that
quote; the digest is the one item to add.

## 7. Contingency row (NOT needed this round; id note below)

**STATUS: not needed and not to be landed.** The candidate entry was re-checked after
landing (§9a): it does not quote `truth.json`'s `build` field and asserts no zipfile
behavior, so the trigger condition for this row is not met. L1's decision (2026-10-23) is
option (a): the own-work row lands as **S033** and the round's ids are the contiguous
pair S032 + S033, so **no id is skipped** and none is reserved for this contingency.

**Id note for any future round:** with S032 (spec) and S033 (own-work) both landing, a
docs row for the zipfile documentation could no longer use S033; if a later round ever
needs it, the next unused id would be **S034**. The row text below is retained for that
future use only, with the id corrected accordingly. Contract v1 shape: 11 columns, no `|`
inside any cell, `used-by` = `—` until an entry cites it.

```text
| S034 | zipfile — Work with ZIP archives, Python documentation — https://docs.python.org/3/library/zipfile.html | docs | A | Python zipfile module behavior only: what the ZIP_DEFLATED constant and the compresslevel argument mean, and that the module defers format semantics to the PKZIP Application Note; not the ZIP record layout, which S032 covers | zipfile.ZIP_DEFLATED; ZipFile.__init__ compresslevel parameter; module introduction; Python 3.15.1 documentation, page last updated Oct 24, 2026 (00:13 UTC) | Which Python-level constants and arguments a recorded build recipe names, so such a recipe can be read without inferring module behavior. | queued | 2026-10-23 | on-release | — |
```

Gate quotes for that row: Q2 (9 words, `zipfile.ZIP_DEFLATED`) and Q3 (15 words,
`ZipFile.__init__ compresslevel`), plus URL, access date `2026-10-23` and snapshot sha256
`9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`. If L1 takes this
branch, the §6 search-log text must be changed to "excluded 0" and this row counted as
included.

## 8. Registry hygiene checks run (read-only)

```text
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
31
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
0
$ grep -n 'docs.python.org' corpus/SOURCES.md | cut -c1-120
25:| S011 | codecs — Codec registry and base classes, Python documentation — https://docs.python.org/3/library/codecs.html | docs | A | ...
```

* Existing rows: 31, no malformed row; last id `S031`, so `S032`/`S033` are both unused.
* The only `docs.python.org` row today is **S011** (`/3/library/codecs.html`) — a
  different URL and a different subject, so a hypothetical S033 would not be a W04
  duplicate-URL hit, but it would overlap S032's scope (see §3a).
* `corpus/SOURCES.md` was **not** modified by this seat.

## 9. Handoff to `R63SourceAppnote` (source-snapshots manifest)

Round-62 precedent has `.ufo/waves/round-62/source-snapshots/manifest.json`; round-63 has
none. **I do not own it** (my item names only the `zipfile.html` snapshot path and this
report, and seats may write only the exact paths their item names), so `R63SourceAppnote`
should create it. Entry for my file, in the round-62 field shape:

```json
{
  "file": "zipfile.html",
  "url": "https://docs.python.org/3/library/zipfile.html",
  "access_date": "2026-10-23",
  "bytes": 139782,
  "sha256": "9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739",
  "origin": "source-opening build seat; copied byte-exact, never executed"
}
```

(For `appnote.txt` the values R63SourceAppnote supplied — 174585 bytes, sha256
`0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` — were independently
recomputed on disk by this seat and agree.)

**Note on the convention that appeared while I worked:** `R63SourceAppnote` wrote
`source-snapshots/appnote.provenance.json` as a per-file provenance sidecar. I wrote the
matching sidecar for my own file —
`source-snapshots/zipfile.provenance.json` (URL, final URL, HTTP 200, content type/length,
access date, `last-modified`, `etag`, bytes, sha256, docs version, page title and
"Last updated on" line, the moving-`/3/`-alias note, and the exclusion decision with its
grounds). It carries the same field shape as the appnote sidecar so the two can be read
together. If L1 prefers a single `manifest.json` in the style of round-62, my sidecar is
redundant and may be folded into it; the values are identical.

## 9a. Post-landing verification of the decision (candidate entry now exists)

The C06 candidate draft appeared at `/tmp/revenger-r63-entry/candidate.md` after my
first pass, and was **revised twice** while I worked. I re-checked every revision against
the decision above. Verdict: the **contingency branch in §5/§7 is NOT triggered** — the
exclusion stands on the actual entry text in every revision.

**Revision 1** (sha256 `630b974a51e0f6ab815a5806a0f415b3f07089df91923dde3a78b6fd49904c7e`):
two `source:` rows (S032 spec + S034 own-work), no `build`-field quote at all
(`grep -n 'ZipFile\|ZIP_DEFLATED\|"build"'` → no hit), no `compresslevel` mention
(`grep -c 'compresslevel'` → 0), and §Sources stating "No third source is cited. The
Python `zipfile` documentation was screened and excluded in this round: the readout reads
the archive's bytes with `struct` and inflates with `zlib`, and credits no `zipfile`
behavior." The compression talk was byte-level only ("compression method 8" reported as a
value read at the spec-derived offset; the payload step "inflating it with `zlib` (raw
DEFLATE)"). No claim of the form "ZIP_DEFLATED produced method 8".

**Revision 2** (sha256 `dcfe131cbf833c90ba956a54eeadbd46314f829e88f5528b52d7baad6c8ff193`,
current): two changes, neither of which triggers the contingency.

1. **The `build` string is now printed — as a recorded field, and it is not load-bearing.**
   A new derived fact appears (`readout.py --fact 'truth_build_field'`), carrying
   `"recorded_build_string":"Python zipfile.ZipFile(mode=w, compression=ZIP_DEFLATED,
   compresslevel=9); write checksum as bin/checksum; writestr README.txt as stated"` with
   its own note: *"recorded provenance string read from the oracle file; this entry makes
   no claim about the behaviour of any library it names and does not rely on it for any
   value"*. That is exactly the framing `R63SourcesRows` named as the condition for the
   exclusion to hold, and the entry meets it: the string is printed, **not interpreted** —
   no claim is made about what `ZIP_DEFLATED` or `compresslevel=9` mean, and no value in
   the entry derives from it. The entry's own §Sources says so explicitly: *"The one place
   a library name appears is the oracle's recorded `build` string, printed above as a
   recorded field and relied on for no value — this entry makes no claim about what any
   library named there does, so the exclusion stands and no docs row is needed."* The Q12
   cell repeats it. So `grep -c 'compresslevel'` is now 2, but both hits are the quoted
   recorded string plus its "no claim" note, not a semantics claim.
2. **The id renumbering is applied:** `grep -o 'S03[0-9]' | sort | uniq -c` gives
   **S032 ×10, S033 ×5, S034 ×0**. The own-work row is now cited as S033 in the
   `source:` header and in §Sources, matching L1's option-(a) decision.

**Revision 3** (sha256 `a0158e99d3fa4b3cec132e03f5738015c39ca3abb56437ae1bab81e88f2d1b53`,
80126 B, current; reported by `R63EntryC06` after its nine corrections H1–H7 and N1–N3):
the same framing holds and is now explicit in the sentence-to-output inventory, which
carries a dedicated row for it —

```text
| RP | the oracle's recorded `build` string (recorded-provenance note, not an observation) | `--fact 'truth_build_field'` | `truth_build_field` → `recorded_build_string`, `note` |
```

Both occurrences of the printed string carry the identical note ("recorded provenance
string read from the oracle file; this entry makes no claim about the behaviour of any
library it names and does not rely on it for any value"), the ids are still **S032 ×10,
S033 ×5, S034 ×0**, and the §Sources exclusion statement (now at line 657) and the Q12
cell (line 708) both say the exclusion stands and no docs row is needed. A targeted grep
for a *behaviour* claim ("zipfile produces", "zipfile writes", "ZIP_DEFLATED means",
"compresslevel=9 means", "per the zipfile") returns **no hit**. The embedded stdout
digest moved to `02b0f495…` (17 lines) because the H1/H7 corrections changed the stdout
bytes — the entry seat flagged that deviation explicitly.

**Cross-check:** the entry now also carries my snapshot digest inline in §Sources —
"`.ufo/waves/round-63/source-snapshots/zipfile.html` (sha256
`9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`, accessed 2026-10-23);
it is not cited as support for any claim" — so the digest lands in the entry as well as in
the lesson's Gate record.

**Finding for L1 (material, from my exclusion, not a defect of mine):** because the
zipfile docs take no row, **S033 is left unused**, and the round's own-work row was
drafted as **S034** (the candidate's `source:` header named S034 in 4 places, and the
round-63 lesson draft reserved S034 for it). Contract v1's `id` rule is "S + 3 or more
digits, the next unused; never reused" — with S033 unwritten, **S033, not S034, is the
next unused id**, so the append as drafted would have landed a row whose id skips an id
that the contract's own rule says is next.

**RESOLVED by L1 (decision recorded 2026-10-23, after my finding):** option (a) is
taken. The own-work row lands as **S033** (next-unused per contract v1) and the entry's
S034 mentions are renumbered to S033 (correction N1, tasked to `R63EntryC06`). The
zipfile-docs screened-and-exclusion stays in the search log with **no row**, so **no id is
skipped** and the round's ids are the contiguous pair S032 (spec) + S033 (own-work).
This closes the id-gap question: my §7 contingency row is not needed and no id is reserved
for it. I changed no id myself — the renumbering is the entry seat's correction and L1's
append.

## 9c. Revision-trail reconciliation — the disputed rev1 sub-claim, settled against preserved bytes

`R63LessonDraft`'s draft lesson (23:48:06) states: *"the first candidate revision read
(`630b974a…`) already carried the same `truth_build_field` fact (two occurrences), while
`R63SourceZipfileDocs` first reported a grep for `ZipFile|ZIP_DEFLATED|"build"` returning
no hit; … the earlier premise was not."* `R63SourcesRows` concurred with that reading and
has recorded it in its review.

**That sub-claim is contradicted by evidence that survives, and I record the conflict
verbatim rather than accept it.** The conclusion (exclusion holds) is unaffected; the
premise attribution is not.

1. **The rev1 embedded stdout is preserved on disk and has no build field.**
   `/tmp/revenger-r63-entry/recheck-stdout.txt` (mtime 23:36) has digest
   `e112d4092dfa8e3ed5398f07d1222457455ca06a94e01e988a0f58eab4c445ec` — **exactly** the
   stdout digest the entry seat's own report (`R63EntryC06.md`, written 23:37:48, pinning
   `candidate.md` = `630b974a…`) records for rev1. That preserved file contains
   `grep -c 'compresslevel'` = **0** and `grep -c 'truth_build_field'` = **0**.
2. **Any printed build-field line necessarily contains `compresslevel`.** Read from
   `corpus/fixtures/archive-r2/truth.json` line 19, the recorded string is
   `'Python zipfile.ZipFile(mode=w, compression=ZIP_DEFLATED, compresslevel=9); write
   checksum as bin/checksum; writestr README.txt as stated'` — `contains "compresslevel":
   True`. So a revision carrying that string has `compresslevel` > 0; rev1's preserved
   stdout has 0.
3. **The entry seat's own rev1 report does not list a build-field fact.**
   `grep -c 'truth_build_field' .ufo/waves/round-63/build/R63EntryC06.md` = **0** while
   that report enumerates the derived facts it exercised.
4. **`R63SourcesRows`' own measurement contradicts the reading they endorsed.**
   Their message states `grep -c 'compresslevel'` = **0** on the revision they first
   checked and 2 on `dcfe131c…` — the same 0-vs-2 split I measured, i.e. their number
   agrees with mine and disagrees with the lesson's sentence.
5. **My grep was not blind to the string, and the file was not stable mid-read.** Control
   test: a synthetic line containing the recorded string **does** match my pattern
   (`grep -n -i 'ZipFile\|ZIP_DEFLATED\|"build"'` → 1 hit). On the file whose
   `sha256sum` in the same command printed `630b974a…`, that pattern matched only the
   two prose sentences (the §Sources and Q12 exclusion statements) — no build-field line.
6. **The likely mechanism of the confusion, checkable against mtimes.** The candidate was
   rewritten three times; the lesson draft was written at **23:48:06**, between rev2
   (`dcfe131c…`) and rev3 (`a0158e99…`, mtime 23:49:58). Rev2 carried the build field
   twice (lines 149 and 249), matching the lesson's "two occurrences". So the lesson seat
   read the on-disk file at draft time — which was rev2 — and attributed its content to
   the earlier digest `630b974a…` it had been told about. The digests it names
   (`dcfe131c…` for its own re-check) are consistent with that sequence.

**Net:** my rev1 observation stands as recorded; the lesson's sentence asserting the
opposite about rev1 did not, and it has now been **withdrawn in the lesson** (corrected
draft sha256 `ce04ac74aea6435aaf532d8099cb57448b246b8928b8636d1765d9f27780f378`, 28934 B:
"the build string entered the candidate at revision `dcfe131c…` … the earlier revision
`630b974a…` carried **no** build-field line … An earlier reading in this seat attributed
the two occurrences to `630b974a…`; that attribution is withdrawn here"). The lesson's
*conclusion* — "the candidate prints `truth.json`'s `build` string as a recorded field,
claims no library behavior, so no docs row is needed" — is correct and I confirm it on the
current revision (§9a). The correction was to the attribution of *which* revision first
carried the string, not to the outcome.

**7. Third independent corroboration (reviewer seat, after adopting the correction).**
`R63SourcesRows` re-verified the chain itself and reported a datum of its own that settles
it: on the candidate then on disk (74270 B, mtime 23:35) its test `"compresslevel" in
candidate` printed **False**, and it measured **2** only at `dcfe131c…` (23:44). It has
withdrawn the second-hand sentence from both of its reports
(`.ufo/waves/round-63/build/sources-rows-review.md` §4 and `R63SourcesRows.md`) and
confirmed the current revision's counts match mine (`compresslevel` = 2,
`truth_build_field` = 6, S032 ×10 / S033 ×5 / S034 ×0). So three seats now report the
same 0-before-`dcfe131c` / 2-after split: the entry seat's pinned stdout digest, this
seat's grep plus control test, and the reviewer's independent membership test.

## 9b. Cross-seat consistency checked (§9c reads as a companion to this section; numbering kept as first written)

* `R63LessonDraft`'s draft lesson (`/tmp/revenger-r63-lesson/round-63.md`, sha256
  `7dda3ff86ab9c06eef760b3f72a211a6f913a1095ce47a3861699a4a59bcbf8d`) carries my
  exclusion line, my 19-word located quote, the `truth.json` `build`-field caveat
  "resolved", and the S033-gap flag — consistent with §1 and §9a.
* `R63SourceAppnote` created `.ufo/waves/round-63/source-snapshots/manifest.json` with my
  `zipfile.html` entry (139782 bytes, sha256
  `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739` — matching my pin)
  marked "no registry row (screened and excluded: the page defers format semantics to
  PKWARE APPNOTE, so it is a pointer to S032, not a second authority)". My
  `zipfile.provenance.json` sidecar coexists and is not listed there; either is redundant
  against the other, and the values agree.
* `R63EntryC06` cites S032 + S033 (after L1's renumbering) and confirms it credits no
  zipfile behavior.
* `R63SourcesRows` (reviewer seat) **CONFIRMED** the decision and independently
  reproduced every ground: the Q1 deferral quote verbatim in the snapshot with its
  hyperlink target literally `https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT`
  (the same URL as S032, so pointer not second authority); `import zipfile` count 0 in
  both readouts; all five cited APPNOTE sections present in the pinned snapshot (§4.4.4
  l.767, §4.4.5 l.854, §4.4.7 l.900, §4.3.12 l.511, §4.3.16 l.632); and the snapshot
  facts matching mine exactly (139782 bytes, the same sha256, the 3.15.1 docs build). Its
  review is recorded in `.ufo/waves/round-63/build/sources-rows-review.md`.

### One conflict between two sibling seats, for the record

On the **search-log counts** the two seats differ, and the difference is a counting
convention, not a factual error:

* `R63LessonDraft`'s archive-spec note: identified **3**, screened **3**, included **1**
  row (S032), excluded **2** — counting the APPNOTE fallback URL's different revision
  (6.3.9) as the second exclusion, and counting the own-work bundle as *not* a document
  set for the "included" figure.
* `R63SourcesRows`' first pass said 2/2/1 for the same reason (own-work bundle not counted
  as a document set), then wrote to L1 that **my §6 text (3/3/2/1) is the correct one**
  and that its own §5c wording is superseded, with L1 to paste my §6 text verbatim.

L1 has since decided: **use the lesson's version** (it reconciles the fallback-revision
exclusion) and drop my §6 block, carrying only the snapshot digest into the Gate record.
That is L1's call and it is the one in force; my §6 block is retained above for the
record and for the digest, and is **not** to be appended. Both counts are internally
consistent under their own conventions, and no seat's arithmetic is wrong — but only one
note may be landed, and the lesson's is the one L1 chose.

## 10. Out of scope / not done

* No `corpus/` file was read-modified or written: `corpus/SOURCES.md`, `corpus/README.md`,
  `corpus/lessons/round-63.md`, `corpus/knowledge/*` untouched.
* No git/jj mutation, no commit, no push, no lane index touch.
* No admission decision, no Q01–Q13 judgement of the candidate, no README C06 flip
  proposal — those belong to `R63ReviewC06Q`, `R63CriticCounts` and L1.
* The candidate entry did not exist at report time (`/tmp/revenger-r63-entry/candidate.md`
  absent; the entry seat's readout script and stdout were present), so the §5 contingency
  is stated against the frozen claims.md/build-spec recipe text and the peer readout pack,
  not against landed entry prose. **Superseded by §9a**: the candidate has since landed
  and been revised twice (sha256 `630b974a…` then `dcfe131c…`) and was re-checked in both
  revisions; it prints the oracle's `build` string as a *recorded field* with an explicit
  "no claim about the behaviour of any library it names" note and relies on it for no
  value, so the contingency is not triggered and the exclusion stands on the entry's own
  text.
* I did not renumber any id in the candidate (S034 → S033) — that was L1's decision and
  the entry seat's correction N1; I verified the renumbering landed (S034 ×0) and
  recorded it. I changed no `corpus/` byte, no lesson file and no search-log note.
* No tool installed or updated. No pacman transaction (host-wide pacman pause honored).
  Only `curl` and `python3` (standard library) were used.
* No `npx`/network call other than the two `curl` GETs to `docs.python.org` recorded in §2.

## 11. Report path

`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63SourceZipfileDocs.md`
