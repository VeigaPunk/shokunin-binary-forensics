# R63SourcesRows — contract-v1 conformance review of the round-63 SOURCES.md rows

Seat: `revenger-r63.R63SourcesRows` (reviewer, build wave, round 63). Date **2026-10-23** (lane local; host `-03`, UTC 2026-10-24 02:4x).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Full review (verdict tables, corrected row text, Gate bullets, search-log wording): **`.ufo/waves/round-63/build/sources-rows-review.md`**.

## Scope actually exercised

- Read `corpus/SOURCES.md` (31 rows, ids `S001`–`S031`, `## Registry` at lines 11–46), contract v1 (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`), `CORPUS.md` §sources-v1, `corpus/QUALITY.md` Q01–Q13.
- Reviewed `R63SourceAppnote`'s draft **S032** row (`.ufo/waves/round-63/build/R63SourceAppnote.md:126`, handed over in-band; that seat did **not** edit `corpus/SOURCES.md`).
- Reviewed `R63SourceZipfileDocs`' **S033** decision: the seat's report **landed after my first pass** (`.ufo/waves/round-63/build/R63SourceZipfileDocs.md`, 17844 bytes, 23:43) and I re-reviewed it against its evidence — **decision confirmed: screened and excluded, no row**. It was also corroborated during the review by two sibling reports (`R63EntryC06.md:164,181-182`, `R63LessonDraft.md:34-37`).
- Also checked the C06 entry's proposed own-work row, now **S033** after L1's renumbering (`/tmp/revenger-r63-entry/candidate.md` `## Sources`; it was drafted as S034).
- Verified the round-63 `source-snapshots/manifest.json` (created by `R63SourceAppnote`) against the bytes on disk — all three digests match.
- No `corpus/SOURCES.md` edit — L1 (`revenger-r63`) is the sole integrator.

## Verdicts (per requested check)

**S032 — PASS on all ten checks; appendable.**

| check | verdict |
|---|---|
| 11 pipe-columns (`awk NF==13`) | **PASS** — 12 pipes → 11 cells → NF=13; scratch copy with the row inserted validates `file ok`, **EXIT=0**, rows 32, malformed 0 |
| no `\|` inside cells | **PASS** |
| `kind` enum | **PASS** — `spec` |
| `tier` scoped to `scope` | **PASS** — `A` for the two records' field layout; not `community`, so E10 does not arm |
| `anchor` names an exact section, not a homepage | **PASS** — §4.3.12 (l.511), §4.3.16 (l.632), §4.4.7 (l.900), §4.4.10 (l.937), §4.4.16 (l.981), §4.4.21 (l.1032), §4.4.22 (l.1041) all exist; revision pinned (6.3.10, revised Nov 01 2022) |
| `teaches` one grounded benefit | **PASS** — one sentence; offsets re-derived by me from the spec's own field widths: 46-byte CD header (crc-32 @16, relative offset @42), 22-byte EOCD (entries @8/@10); agrees with the fixture readout's observed offsets |
| `status` enum | **PASS** — `queued` (correct for `used-by = —`) |
| `id` next unused | **PASS** — `S032` after `S001`–`S031`, no gaps, no reuse |
| `used-by` paths exist or `—` | **PASS** — `—` |
| **no NEW duplicate URL** | **PASS** — `pkware.cachefly.net/…/APPNOTE.TXT` in no existing row; with S032 inserted the census still prints exactly the three disclosed W04s (S024/S028/S029) + `ok`, **EXIT=0** — no new W04, no E04 |

**S033 (Python zipfile docs) — NO ROW, screen-and-exclude. Decision confirmed against the landed report.** Measured grounds: the readout imports `struct`/`zlib` only (`grep -c 'import zipfile'` = 0 in both `build/zip-readout.py` and the candidate readout); the snapshot `zipfile.html` (139782 B, sha256 `9520a8cb…`, Python 3.15.1) contains **0** occurrences of `0x02014b50`/`0x06054b50` and no "end of central directory", so it states no field layout; and the page's own deferral quote ("Any advanced use of this module will require an understanding of the format, as defined in PKZIP Application Note.", 19 words) is **verbatim** in the snapshot with its hyperlink target pointing at **the same APPNOTE URL as S032** — a pointer, not a second authority. Absence + search-log note, not a rejected row.

**Search-log counts — L1 has since decided; recorded here so the divergence is visible.** (Earlier note in this file, superseded: I had judged the seat's §6 counts preferable to my own first-pass draft. L1 has since chosen the **lesson's** `## Search log` note — 3/3/1/2, with the APPNOTE fallback revision as the second exclusion — and dropped the seat's §6 block; my §5c wording is marked superseded in the review file. The exclusion reason is identical in substance across all three and was verified independently by me.)

**S033 (own-work row for the C06 entry) — PASS on all checks.** The entry seat's proposed own-work row (drafted as `S034`, **renumbered to `S033`** by L1's id decision, which I verified on the current candidate revision `a0158e99…`: `grep -o 'S03[0-9]' candidate.md | sort | uniq -c` → **S032 ×10, S033 ×5, S034 ×0**) passes every check: 11 cells / NF=13, no `|` inside any cell, `kind` `own-work`, `tier` `A` for the lane's own re-runnable bytes, anchor naming exact files + digests + Evidence IDs + base commit, one grounded `teaches`, `status` `queued`, `recheck` `on-release`, `used-by` `—`, id = next unused. Its `source` cell is path-only (no URL), so it never enters the duplicate-URL rule. **The round's ids are the contiguous pair S032 + S033 with no id skipped.**

**My condition on the exclusion — MET and verified.** The exclusion rested on the entry not crediting zipfile behaviour. The candidate now prints the oracle's `build` string, so I checked it: on the current revision `a0158e99d3fa4b3cec132e03f5738015c39ca3abb56437ae1bab81e88f2d1b53` (80126 B) `compresslevel` = 2 and `truth_build_field` = 6, and every occurrence carries the note "recorded provenance string read from the oracle file; this entry makes no claim about the behaviour of any library it names and does not rely on it for any value"; the entry text presents the string as a recorded field relied on for no value, and I re-ran `readout.py --fact 'truth_build_field'` myself (exit 0). That is the S031 / r24 `embedded_pattern_hex` discipline, so **the exclusion holds and the contingency docs row stays unlanded**.

**Revision-trail correction (my error, withdrawn).** An earlier version of this file said the earlier revision "already carried the same `truth_build_field` fact". That was a draft-lesson claim I repeated instead of trusting my own measurement, and it is **wrong**. Verified myself: the preserved rev1 stdout `/tmp/revenger-r63-entry/recheck-stdout.txt` (17 lines, sha256 `e112d409…`) has `compresslevel` = 0 and `truth_build_field` = 0; any printed build-field line necessarily contains "compresslevel" (`truth.json:19` contains it — I checked); my own first-pass check on the then-current candidate printed `"compresslevel" in candidate` → **False**, and I measured **2** only at revision `dcfe131c…` (23:44). The string entered at `dcfe131c…`, not rev1. The conclusion is unchanged — the string is a recorded field, no docs row is needed — but the attribution was wrong. The lesson seat has since corrected its own sentence identically (its `## Gate`: "the build string entered the candidate at revision `dcfe131c…` … that attribution is withdrawn here").

**Search-log counts — divergence resolved by L1, recorded not smoothed.** Three counts were in play for the same query: mine (2/2/1/1), the zipfile seat's §6 (3/3/2/1, own-work bundle counted as an included row), and the lesson's `## Search log` note (3/3/1/2, with the APPNOTE fallback revision as the second exclusion). **L1's decision: land the lesson's note, drop the seat's §6 block.** My §5c wording in the review file is marked superseded; the exclusion reason is identical in substance across all three and was verified independently by me. One note lands; the divergence is recorded in both seats' reports rather than quietly dropped.

## Baseline census (unchanged registry, measured)

`validate --root … revenger` → three pre-existing W04s (S024/S028/S029) + `ok`, **EXIT=0**; `census` → rows 31, tier A 29 / C 2, mined 26 / queued 1 / rejected 4, missing 0, **EXIT=0**. Frozen manual census: malformed 0, duplicate ids none, enum violations none, tier inflation none, mined rows with missing `used-by` none.

## Findings (6)

1. **Must-fix (text):** the opener's `## Gate` block re-joins the §4.4.7 quote into **35 words** (contract rule 1 caps it at 25). The quotes *table* splits it correctly (23 + 11); the lesson draft already uses the split form — only the hand-over block needs the same split. Corrected Gate bullets are in the review's §5b.
2. **Should-fix (text):** the row's anchor omits **§4.3.3**, the section that states the byte order ("All values MUST be stored in little-endian byte order…", l.350-351) that the readout's `struct.unpack_from("<I"/"<H")` depends on; the entry's own `source:` header *does* cite §4.3.3. Adding `§4.3.3` to the anchor closes the Q01 tie at zero cost. The row remains conformant without it.
3. **Non-blocking observation:** the two APPNOTE URLs now serve **different revisions** — primary 6.3.10 (sha256 `0b993022…`, 174585 B) vs `pkware.com/…/APPNOTE.TXT` → 6.3.9 (sha256 `c7cf1fec…`, 173575 B). I diffed them: 43 diff lines, all in the change log and APPENDIX B third-party mappings; the §4.3.12 and §4.3.16 blocks are **byte-identical across revisions** (extracted-block digests `2ffc98cc…` and `a1bb6d42…` match in both), so the quotes are stable. The row pins the actually-opened URL + revision, which is the honest choice.
4. **Ordering constraint for L1:** E11 fires when a **`mined`** row's `used-by` path is absent on disk, and `corpus/knowledge/round-63-zip-central-directory-evidence.md` does not exist yet. Append S032 as `queued` / `—`, then flip `queued→mined` + `used-by` in the same append as the entry lands, logging the old→new pair in the round lesson.
5. **Minor, lesson Gate:** the anchor's `§4.4.10-4.4.12` and `§4.4.21-4.4.22` have no located quote in the lesson draft's nine S032 quotes (all measured ≤25 words) nor in the entry's six. Rule 1 needs one quote grounding `teaches` (satisfied), but both quotes are verbatim and ≤25 words and are supplied in the review's §5b so every anchored section is covered.
6. **Manifest — closed.** `R63SourceAppnote` created `.ufo/waves/round-63/source-snapshots/manifest.json` with three entries (`appnote.txt`, `zipfile.html` with `registry_row: "none (screened and excluded … pointer to S032, not a second authority)"`, `rea-firmware-guide.md` with `registry_row: "none (lead only)"`). I verified all three digests against the bytes on disk: `0b993022…`, `9520a8cb…`, `d4a25c85…` — all match. The zipfile seat's `zipfile.provenance.json` sidecar coexists and is redundant against the manifest entry (values agree); L1 owns whether to keep both.

**Finding 5 (id space) is closed:** L1 assigned `S033` to the own-work row and withdrew the `S034` reservation, so the round lands the contiguous pair **S032 + S033 with no id skipped**.

**Residual observation (not a blocker).** The search-log note L1 chose counts *identified 3, screened 3, included 1 row (S032), excluded 2*, but the round lands **two** registry rows (S032 + S033) and the note's "Where:" clause lists only the APPNOTE URL, its fallback revision and the zipfile docs — the own-work bundle has no search-log unit of its own (the lesson's other note is the firmware-premise query, 3/3/0/3). Under round-61/62's convention that bundle counted once inside "identified", so this is a coverage gap rather than a wrong count, and the lesson's `## Gate` already records S033 with its digests so no reader is misled. Optional one-clause remedy is in the review file.

## Landed-state verification (post-append, read-only)

Both rows are now in the live registry; I re-ran the checks against it rather than leaving this as a pre-append opinion.

- `corpus/SOURCES.md` → **33 rows**; `| S032 |` and `| S033 |` present, each 12 pipes → 11 cells → **NF=13**, no `|` inside any cell, **no duplicate ids**.
- **S032 landed with `§4.3.3` in the anchor** — `§4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022)` — so **Finding 2 is closed**; status `mined`, `used-by` both paths.
- **S033 landed** as `own-work`, tier `A`, anchor carrying the three file digests + Evidence IDs + base commit, status `mined`.
- **`used-by` paths resolve** (E11 clean): `corpus/knowledge/round-63-zip-central-directory-evidence.md` and `corpus/lessons/round-63.md` both exist.
- **Census after append:** `validate` → exactly the three pre-existing W04s (S024/S028/S029) + `ok`, **EXIT=0** (no new W04/E04/E03); `census` → rows 33, tier A 31 / C 2, mined 28 / queued 1 / rejected 4, missing 0, EXIT=0.
- **Finding 4 closed as recommended:** the lesson logs the flip old→new in place (`queued`/`—` → `mined`/both paths, same commit as the entry), satisfying contract rule 2 with the E11 path resolvable at validation.
- **Finding 1 closed in the landed lesson:** the §4.4.7 quote appears in the 23+11 split form; I re-measured all nine landed Gate quotes at 7/21/7/8/23/24/23/12/20 words — none over 25.
- **Finding 5 remains open, non-blocking:** the landed Gate has no quote for the anchor's `§4.4.10-4.4.12` or `§4.4.21-4.4.22`; rule 1 is satisfied by the existing quotes, and the two verbatim ≤25-word quotes are in the review's §5b if wanted.
- **Residual search-log observation accepted as-is by L1:** the landed `## Search log` states the unit convention explicitly, which covers the own-work row's absence from the included count; no remedy clause added.

## Corrected / recommended text — **now LANDED**

The only substantive change I recommended to the S032 row was the anchor cell (add `§4.3.3`), and **the landed row carries it**: `§4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022)`. The rest of the row is byte-identical to the opener's hand-over. Full row text, the ≤25-word Gate bullets and the search-log material are in `.ufo/waves/round-63/build/sources-rows-review.md` §5a–§5c (with §5c marked superseded in favour of the landed lesson note):

```
| S032 | PKWARE APPNOTE.TXT — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT | spec | A | central directory file header and end-of-central-directory record field layout for one authored ZIP archive: signature values, field order, length fields, CRC-32 and local-header offset | §4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022) | The central directory header is a fixed 46-byte record whose crc-32 sits at offset 16 and whose relative offset of local header sits at offset 42, and the end of central directory record is a fixed 22-byte record whose two total-entries counts sit at offsets 8 and 10, so a byte readout of an archive can be checked field by field against the specification. | mined | 2026-10-23 | on-release | corpus/knowledge/round-63-zip-central-directory-evidence.md, corpus/lessons/round-63.md |
```

(As landed, `status` is `mined` with both `used-by` paths rather than the drafted `queued`/`—`; the flip is logged old→new in the lesson, satisfying contract rule 2.)

## Out of scope / not done

No `corpus/` edit of any kind (no SOURCES.md, lesson, knowledge entry, README flip, QUALITY.md change); no `corpus/live` or `corpus/fixtures` byte touched; no target executed (the ZIP fixture was read as bytes only); no commit, push, publish or deploy; no `~/.omp/agent/config.yml` or routing-table edit; no model arguments.

**Tooling:** none installed or upgraded; no pacman/`uv`/`npm`/binary install, no system upgrade. Network use: read-only `curl` GETs/HEADs to public documentation URLs (pkware cachefly, pkware.com, docs.python.org) for verification.

**Scratch:** `/tmp/revenger-r63-sourcesrows/` — row checker `check_row.py`, a scratch `corpus/` copy for census validation, one re-fetched APPNOTE copy. Removed after this report landed.
