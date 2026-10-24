# R63SourcesRows — contract-v1 conformance review of the round-63 SOURCES.md rows

Seat: `revenger-r63.R63SourcesRows` (reviewer, build wave, round 63). Date **2026-10-23** (lane local; host `-03`, UTC 2026-10-24 02:4x).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Full review (verdict tables, corrected row text, Gate bullets, search-log wording): **`.ufo/waves/round-63/build/sources-rows-review.md`**.

## Scope actually exercised

- Read `corpus/SOURCES.md` (31 rows, ids `S001`–`S031`, `## Registry` at lines 11–46), contract v1 (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`), `CORPUS.md` §sources-v1, `corpus/QUALITY.md` Q01–Q13.
- Reviewed `R63SourceAppnote`'s draft **S032** row (`.ufo/waves/round-63/build/R63SourceAppnote.md:126`, handed over in-band; that seat did **not** edit `corpus/SOURCES.md`).
- Reviewed `R63SourceZipfileDocs`' **S033** decision: its own report had **not landed** at hand-over (seat still `running`, report absent) — the decision was reviewed against the artifacts it must rest on and is corroborated by two sibling reports that landed during the review (`R63EntryC06.md:164,181-182`, `R63LessonDraft.md:34-37`): **screened and excluded, no row**.
- Also checked the C06 entry's proposed own-work row **S034** (`/tmp/revenger-r63-entry/candidate.md` `## Sources`).
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

**S033 (Python zipfile docs) — NO ROW, screen-and-exclude.** Measured grounds: the readout imports `struct`/`zlib` only (`grep -c 'import zipfile'` = 0 in both `build/zip-readout.py` and the candidate readout); the snapshot `zipfile.html` (139782 B, sha256 `9520a8cb…`, Python 3.15.1) contains **0** occurrences of `0x02014b50`/`0x06054b50` and no "end of central directory", so it states no field layout. Absence + search-log note, not a rejected row.

**S034 (own-work row for the C06 entry) — PASS on all checks**, with one L1 caveat: `S034` is lawful but leaves `S033` unused (with S033 screened out, the next unused id after S032 is S033); either choice is conformant, and only `S034` needs the "reserved id went unused" note in the lesson. Its `source` cell is path-only (no URL), so it never enters the duplicate-URL rule.

## Baseline census (unchanged registry, measured)

`validate --root … revenger` → three pre-existing W04s (S024/S028/S029) + `ok`, **EXIT=0**; `census` → rows 31, tier A 29 / C 2, mined 26 / queued 1 / rejected 4, missing 0, **EXIT=0**. Frozen manual census: malformed 0, duplicate ids none, enum violations none, tier inflation none, mined rows with missing `used-by` none.

## Findings (5)

1. **Must-fix (text):** the opener's `## Gate` block re-joins the §4.4.7 quote into **35 words** (contract rule 1 caps it at 25). The quotes *table* splits it correctly (23 + 11); the lesson draft already uses the split form — only the hand-over block needs the same split. Corrected Gate bullets are in the review's §5b.
2. **Should-fix (text):** the row's anchor omits **§4.3.3**, the section that states the byte order ("All values MUST be stored in little-endian byte order…", l.350-351) that the readout's `struct.unpack_from("<I"/"<H")` depends on; the entry's own `source:` header *does* cite §4.3.3. Adding `§4.3.3` to the anchor closes the Q01 tie at zero cost. The row remains conformant without it.
3. **Non-blocking observation:** the two APPNOTE URLs now serve **different revisions** — primary 6.3.10 (sha256 `0b993022…`, 174585 B) vs `pkware.com/…/APPNOTE.TXT` → 6.3.9 (sha256 `c7cf1fec…`, 173575 B). I diffed them: 43 diff lines, all in the change log and APPENDIX B third-party mappings; the §4.3.12 and §4.3.16 blocks are **byte-identical across revisions** (extracted-block digests `2ffc98cc…` and `a1bb6d42…` match in both), so the quotes are stable. The row pins the actually-opened URL + revision, which is the honest choice.
4. **Ordering constraint for L1:** E11 fires when a **`mined`** row's `used-by` path is absent on disk, and `corpus/knowledge/round-63-zip-central-directory-evidence.md` does not exist yet. Append S032 as `queued` / `—`, then flip `queued→mined` + `used-by` in the same append as the entry lands, logging the old→new pair in the round lesson.
5. **Minor, lesson Gate:** the anchor's `§4.4.10-4.4.12` and `§4.4.21-4.4.22` have no located quote in the lesson draft's nine S032 quotes (all measured ≤25 words) nor in the entry's six. Rule 1 needs one quote grounding `teaches` (satisfied), but both quotes are verbatim and ≤25 words and are supplied in the review's §5b so every anchored section is covered.

## Corrected / recommended text

The **registry row for S032 is unchanged except for the anchor cell** (add `§4.3.3`); corrected full row text, the ≤25-word Gate bullets, and the search-log note for the screened-out second source are in `.ufo/waves/round-63/build/sources-rows-review.md` §5a–§5c. The row text L1 should append, as handed over by the opener and confirmed conformant:

```
| S032 | PKWARE APPNOTE.TXT — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT | spec | A | central directory file header and end-of-central-directory record field layout for one authored ZIP archive: signature values, field order, length fields, CRC-32 and local-header offset | §4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022) | The central directory header is a fixed 46-byte record whose crc-32 sits at offset 16 and whose relative offset of local header sits at offset 42, and the end of central directory record is a fixed 22-byte record whose two total-entries counts sit at offsets 8 and 10, so a byte readout of an archive can be checked field by field against the specification. | queued | 2026-10-23 | on-release | — |
```

## Out of scope / not done

No `corpus/` edit of any kind (no SOURCES.md, lesson, knowledge entry, README flip, QUALITY.md change); no `corpus/live` or `corpus/fixtures` byte touched; no target executed (the ZIP fixture was read as bytes only); no commit, push, publish or deploy; no `~/.omp/agent/config.yml` or routing-table edit; no model arguments.

**Tooling:** none installed or upgraded; no pacman/`uv`/`npm`/binary install, no system upgrade. Network use: read-only `curl` GETs/HEADs to public documentation URLs (pkware cachefly, pkware.com, docs.python.org) for verification.

**Scratch:** `/tmp/revenger-r63-sourcesrows/` — row checker `check_row.py`, a scratch `corpus/` copy for census validation, one re-fetched APPNOTE copy. Removed after this report landed.
