# Round-63 SOURCES.md rows — contract-v1 conformance review (pre-append)

Seat: `revenger-r63.R63SourcesRows` (reviewer, build wave). Reviewed **2026-10-23** (lane local date; host `-03`, UTC 2026-10-24 02:2x).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

Contract: `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` (v1, frozen 2026-10-19).
Registry reviewed: `corpus/SOURCES.md` (31 rows, ids `S001`–`S031`, `## Registry` at lines 11–46).

**No `corpus/SOURCES.md` edit was made.** This seat reviews; `revenger-r63` (L1) is the sole integrator.

---

## 1. Baseline measured before any review (unchanged registry)

```
$ bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
EXIT=0

$ bash .../sources-census.sh census --root /home/vgpnk/Projects/shokunin revenger
revenger	rows	31   tier.A 29   tier.C 2   status.mined 26   status.queued 1   status.rejected 4
FLEET	missing	0
EXIT=0
```

The three disclosed W04s are the pre-existing S024/S028/S029 same-URL/different-scope warnings (claims.md "Frontier and routed debt"). **Baseline is clean: 0 E-codes.**

Frozen manual census (contract §Census) on the live file: rows 31, malformed (`NF!=13`) **0**, tier `A=29 C=2`, status `mined=26 queued=1 rejected=4`, duplicate ids **none**, enum/tier-inflation violations **none**, mined rows with missing used-by paths **none** (all 26 mined rows' `used-by` paths resolve on disk).

---

## 2. S032 — draft row reviewed

Source of the draft: `.ufo/waves/round-63/build/R63SourceAppnote.md:126` (opener seat `R63SourceAppnote`, handed over in-band; the seat did not edit `corpus/SOURCES.md`).

Draft row, verbatim as handed over:

```
| S032 | PKWARE APPNOTE.TXT — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT | spec | A | central directory file header and end-of-central-directory record field layout for one authored ZIP archive: signature values, field order, length fields, CRC-32 and local-header offset | §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022) | The central directory header is a fixed 46-byte record whose crc-32 sits at offset 16 and whose relative offset of local header sits at offset 42, and the end of central directory record is a fixed 22-byte record whose two total-entries counts sit at offsets 8 and 10, so a byte readout of an archive can be checked field by field against the specification. | queued | 2026-10-23 | on-release | — |
```

### Verdict per requested check

| # | check | verdict | evidence |
|---|---|---|---|
| 1 | 11 pipe-columns (`awk NF==13`) | **PASS** | 12 pipes → 11 cells → NF=13. Inserted on a scratch copy of `corpus/SOURCES.md` and validated: `file rows 32`, malformed 0, `file ok`, **EXIT=0**. |
| 2 | no `\|` inside cells | **PASS** | no cell contains a pipe; the only `\|` characters are the 12 row delimiters. |
| 3 | `kind` enum | **PASS** | `spec` ∈ `spec·docs·paper·code·tool·dataset·talk·book·community·own-work` (contract Shape). `spec` is the right kind: PKWARE's own format specification. |
| 4 | `tier` scoped to `scope` | **PASS** | tier `A` for scope "central directory file header and end-of-central-directory record field layout" — the format's own primary specification is authoritative for that scope (contract: A = "primary or authoritative for that scope (spec …)"). Not `community`, so E10 does not arm. The scope is bounded to *field layout of two records*, which is exactly what the cited sections state. |
| 5 | `anchor` names an exact section, not a homepage | **PASS** | anchor = `§4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022)`. Every cited section exists in the snapshot: §4.3.12 → line 511, §4.3.16 → line 632, §4.4.7 → line 900, §4.4.10 → line 937, §4.4.16 → line 981, §4.4.21 → line 1032, §4.4.22 → line 1041. Revision pin present (6.3.10, revised Nov 01 2022). Not a bare homepage. |
| 6 | `teaches` is one grounded benefit | **PASS** | one sentence, one benefit ("a byte readout … can be checked field by field against the specification"). Grounding re-derived by me from the §4.3.12 field list: 4+2+2+2+2+2+2+4+4+4+2+2+2+2+2+4+4 = **46 bytes**, crc-32 at **16**, relative offset of local header at **42**; §4.3.16: 4+2+2+2+2+4+4+2 = **22 bytes**, entries-on-this-disk at **8**, total entries at **10**. Both sums and offsets are the spec's own field widths, not an implementation's layout, and they agree with the fixture readout's observed offsets (`crc32 = u32(data,pos+16)`, `local_offset = u32(data,pos+42)`, `entries_on_disk = u16(data,eocd+8)`, `total_entries = u16(data,eocd+10)` — `build/zip-readout.py`). |
| 7 | `status` enum | **PASS** | `queued` ∈ `queued·mined·rejected`. `queued` is the correct arrival state for a row whose `used-by` is `—`; `mined` requires ≥1 cited path (contract Shape). |
| 8 | `id` is the next unused | **PASS** | existing ids `S001`–`S031`, no gaps, no reuse (`sort\|uniq -d` empty). `S032` is next unused. |
| 9 | `used-by` paths exist or are `—` | **PASS** | `used-by` = `—` (em dash). Nothing to resolve; E11 does not arm on a non-`mined` row. |
| 10 | **no NEW duplicate URL** | **PASS** | `pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT` appears in no existing row (all 20 distinct registry URLs enumerated; no pkware host). With S032 inserted, `validate` still prints exactly the **same three** pre-existing W04s and `ok`, **EXIT=0** — no new W04, no E04. |

Additional contract checks not in the requested list:

| check | verdict | evidence |
|---|---|---|
| `opened` ISO and not in the future | PASS | `2026-10-23`; census E08 does not arm (`validate --today 2026-10-23` EXIT=0). The HTTP `Date` header was `Sat, 24 Oct 2026 02:21:34 GMT`; lane local date is 2026-10-23, and the round's own records use 2026-10-23. |
| `recheck` ISO / cadence / `on-release` | PASS | `on-release` matches the census' `symbolic()` pattern and the precedent of other pinned-spec rows (S002, S006, S010, S016, S018). |
| row inside `## Registry` (E12) | PASS | must be inserted **before** `## Paths`; inserting after the last registry row (line 45) is correct — a row-shaped line after `## Paths` is E12/exit 1. |
| append-only (rule 2) | PASS | a brand-new row, no existing row modified. |
| rule 1 — opened this round + Gate record | **PASS for the row; see Finding 2 for the Gate text** | snapshot + provenance sidecar exist at `.ufo/waves/round-63/source-snapshots/appnote.txt` (sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, 174585 bytes, CRLF, byte-exact as served) and `appnote.provenance.json`. **I independently re-fetched the URL: sha256 identical to the snapshot** (byte-exactness confirmed, not taken on report). All twelve quoted strings are verbatim substrings of the whitespace-normalized snapshot; all ≤25 words. |
| no credential material / private URLs / `op://` (rule 6) | PASS | public PKWARE CDN URL only. |

### Overall verdict on S032

**CONFORMANT — append as-is (with the two Finding-1/Finding-2 text corrections below, which are Gate/anchor refinements, not structural defects).**

---

## 3. Findings

### Finding 1 (must-fix, text only) — the `§4.4.7` Gate quote in the hand-over is 35 words, over the ≤25-word limit

Contract rule 1 requires the lesson `## Gate` to record "a ≤25-word quote with its location". The opener's quotes **table** splits that quote into Q8 (23 words) + Q9 (11 words), but the **Gate-record block** re-joins them into one 35-word string:

> "If bit 3 of the general purpose flag is set, this field is set to zero in the local header and the correct value is put in the data descriptor and in the central directory." — **35 words**

Measured word counts of the seven Gate bullets in `R63SourceAppnote.md`: 7, 21, 24, 8, 23, **35**, 20. Only that one is over 25. Fix by pasting the split form or trimming. All seven Gate quotes are otherwise verbatim in the snapshot (I re-checked each against the normalized text) and each is located.

### Finding 2 (should-fix, text only) — the anchor omits the byte-order section the readout depends on

The row's `teaches` states field **offsets** (crc-32 at 16, relative offset at 42, entries at 8/10) and the C06 readout reads those multi-byte fields little-endian (`struct.unpack_from("<I"/"<H")`). The row's anchor lists §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22 — but **not** §4.3.3, which is where the specification states the byte order ("All values MUST be stored in little-endian byte order unless otherwise specified…", lines 350–351; §4.4.1.1 states the same as Intel low-byte:high-byte at lines 654–655). The opener already extracted that quote (Q11) and it is in the Gate record, but the row's anchor does not point at it, so a Q01 reader cannot tie the little-endian reading of the offsets to the row. Adding `§4.3.3` to the anchor closes this at zero cost and keeps the claim inside the row's own scope.

### Finding 3 (non-blocking observation, for L1) — the two APPNOTE URLs now serve different revisions

`https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT` (the row's URL) serves **6.3.10**, revised Nov 01 2022, sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, 174585 bytes.
`https://pkware.com/documents/casestudies/APPNOTE.TXT` (the build-spec fallback) returns HTTP 200 but **redirects** to `https://pkwaredownloads.blob.core.windows.net/pkware-general/Documentation/APPNOTE-6.3.9.TXT` — a **different revision**, 6.3.9, revised Jul 15 2020, 173575 bytes, sha256 `c7cf1fecfbde36ebbfbac643e6183d5c76fac983c2066fb8e32c6e4058a87e80`.

I diffed the two revisions myself: **43 diff lines total**, all in the change log and APPENDIX B third-party extra-field mapping (Pixar USD header ID, Tandem, …). The two record-layout sections the row rests on are **byte-identical across revisions** — extracted-block digests match exactly: §4.3.12 block `2ffc98cca559f543a535170768804a4817fb0e874f5330971810ecea9da092e7`, §4.3.16 block `a1bb6d42ce5b5a7af3f471718d7b16632e712528ba35dc09b029859e63baa323` in **both** files. So the row's quotes are stable either way; pinning the actually-opened URL + revision (as the row does) is the honest choice, and the divergence is already recorded in `appnote.provenance.json`. Not a defect. It does mean the `on-release` recheck is the right cadence, and that a future re-open must compare the revision header, not just the bytes.

### Finding 4 (advisory) — ordering constraint for L1's flip

`status`/`used-by`/`recheck` are the only in-place mutable columns (contract rule 2), and the census' E11 fires when a **`mined`** row's `used-by` path does not exist on disk. The C06 entry path `corpus/knowledge/round-63-zip-central-directory-evidence.md` does not exist yet. So: append S032 as `queued` / `used-by —` **now**, and either (a) flip to `mined` + that path in the same append as the entry lands, or (b) append as `queued` and log the `queued → mined` + `— → corpus/knowledge/round-63-zip-central-directory-evidence.md` old→new pair in `corpus/lessons/round-63.md`. Precedent: `R62SourceEvmOwn` ("E11 sequencing for L1: `used-by` must resolve when the row is validated").

### Finding 5 (id space) — the own-work bundle row

`claims.md` reserves `S032` (APPNOTE) and "S033 if used" (Python zipfile docs). The C06 entry also needs an **own-work** row for the authored bytes + saved record (round-62 shape: S028↔S031, S029↔S030). If zipfile docs is screened out (Finding 6), `S033` is free and the own-work row should take `S033`; if a zipfile row is written, the own-work row takes `S034`. Either way the id must be the **next unused**, and the own-work row's `source` cell must be **repo-relative paths only** (no URL) — the census' `url_of()` returns empty for path-only sources, so an own-work bundle never enters the duplicate-URL rule (`R62SimplifyEntrySurface` measured this).

---

## 4. S033 — Python zipfile docs decision (reviewed)

**Dependency status: RESOLVED.** The seat's report `.ufo/waves/round-63/build/R63SourceZipfileDocs.md` (17844 bytes, written 2026-10-23 23:43) landed after my first pass, and the seat's in-band message confirms the same decision. I have re-reviewed the landed report against its own evidence; the decision is **confirmed** and one count discrepancy with my draft search-log wording is reconciled below.

**Decision the evidence supports: NO `S033` row — screen and exclude with a search-log note.** Grounds, all measured by me:

1. **The readout credits no zipfile behaviour.** `.ufo/waves/round-63/build/zip-readout.py` and the entry seat's `/tmp/revenger-r63-entry/readout.py` parse the archive with `struct` and inflate with `zlib` only. Their import blocks are `binascii, hashlib, json, os, struct, sys, zlib` — **no `zipfile`**, and a grep for `zipfile|ZipFile|ZIP_DEFLATED|compresslevel|namelist|getinfo` over the entry seat's artifacts (`readout.py`, `facts.txt`, `facts.json`, `readout.stdout.txt`) returns **zero hits**. So zipfile semantics are not load-bearing for any entry sentence.
2. **The docs would not carry the load-bearing claim anyway.** The snapshot `.ufo/waves/round-63/source-snapshots/zipfile.html` (139782 bytes, sha256 `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`, title `zipfile — Work with ZIP archives — Python 3.15.1 documentation`) contains **0** occurrences of `0x06054b50`, **0** of `0x02014b50`, and **0** of "end of central directory"; "central directory" appears 5 times, all in prose about the module's behaviour. The record field layout the entry needs is in APPNOTE (S032), not in the Python docs.
3. **Contract-wise, absence beats a rejected row here.** The build item states it directly: "absence from the registry with a search-log note is cleaner than a rejected row needing a grounded reject reason" — and a `rejected` row would need a grounded reject reason plus a `flip:` clause (Q12) that a documentation page that simply does not discuss the field layout cannot honestly supply.
4. **The landed report adds a fourth ground I verified independently: the page defers format semantics to APPNOTE itself.** Its Q1 quote — "Any advanced use of this module will require an understanding of the format, as defined in PKZIP Application Note." (19 words, module introduction) — is **verbatim** in the snapshot (I stripped HTML tags and normalised whitespace; `verbatim=True`), and the hyperlink target of that anchor is **`https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT`** — literally the same URL as S032's `source`. So the docs page is a *pointer* to S032, not an independent authority. Its other cited APPNOTE sections (§4.4.4 general purpose bit flag l.767, §4.4.5 compression method l.854, §4.4.7 CRC-32 l.900) all exist in the pinned snapshot, as the seat states.
5. **Landed-report facts reconcile with my measurements:** URL `https://docs.python.org/3/library/zipfile.html`, HTTP 200, no redirect, access date 2026-10-23 (fetch 2026-10-24T02:21:51Z), snapshot `.ufo/waves/round-63/source-snapshots/zipfile.html`, **139782 bytes, sha256 `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`** — identical to the digest I computed independently before the report landed. The page's docs version string is "Python 3.15.1 documentation".

Consequences for L1:
- `S033` is then **unused**; the round lesson should say so (round-62 precedent: "the reserved id went unused"), and the own-work bundle row takes `S033` (Finding 5).
- The round search log (`corpus/SOURCES.md` `## Search log`, and `corpus/lessons/round-63.md` `## Gate`) must carry the exclusion with its reason and counts — e.g. *identified 2 (APPNOTE 6.3.10, Python zipfile 3.15.1 docs); screened 2; included 1 (S032); excluded 1 (Python zipfile docs — not load-bearing: the readout uses raw `struct`/`zlib` reads and credits no zipfile behaviour; the page states no central-directory/EOCD field layout). Stop: APPNOTE §4.3.12/§4.3.16 state both records' field lists.*
- The zipfile snapshot itself is fine to keep on disk as evidence of the screen (record its URL/date/sha256 in the search-log note); it is not a registry row.

**Search-log counts — one discrepancy to reconcile (mine vs the landed report).** My §5c draft wording counts the round as *identified 2, screened 2, included 1 (S032), excluded 1 (zipfile docs)*. The landed report counts the **own-work bundle as a document set**: *identified 3, screened 3, included 2 rows (S032 APPNOTE plus the own-work fixture/saved-record row), excluded 1 without a row (zipfile docs)*. **The landed report's counts are the correct ones for L1 to use**, because round-62 set the convention this round follows (the round-61/62 search-log notes count "own-work bundles … as additional included registry rows" and their totals likewise include the own-work set: "identified 2, screened 2, included 2 rows (S028, S031)"). My §5c wording below is therefore **superseded**: L1 should paste the landed report's §6 text (or the seat's one-line exclusion reason), not my earlier draft. The exclusion reason itself is identical in substance to mine and verified above.

**Contingency row (not for landing under this decision) — checked anyway.** The landed report §7 supplies a contingency `S033` docs row for the case where the integrated entry turns `truth.json`'s recorded build label (`"Python zipfile.ZipFile(mode=w, compression=ZIP_DEFLATED, compresslevel=9)"`, `corpus/fixtures/archive-r2/truth.json:19`) into a claim about zipfile module behaviour. I ran the contract check on that drafted row: **11 cells / NF=13 PASS, `kind` `docs` PASS, `tier` `A` scoped to module behaviour only PASS, `status` `queued` PASS, `recheck` `on-release` PASS, `used-by` `—` PASS, no pipe inside any cell PASS, no duplicate URL (the only `docs.python.org` row today is S011 `/3/library/codecs.html`, a different URL and subject) PASS.** Only the id caveat applies (S033 would be the next unused only after S032 lands). **The contingency does not fire for the drafted entry**: `grep -c 'compresslevel' /tmp/revenger-r63-entry/candidate.md` = **0**, and the candidate never mentions the build label, so quoting `truth.json`'s label as a *recorded* value keeps the exclusion correct, exactly as the seat states.

**One condition on the exclusion that L1 must hold.** The exclusion rests on the entry **not** crediting zipfile behaviour. The C06 entry's own-work row (S034) cites `truth.json` as an *authored oracle file*; if the integrated entry quotes the `build` string, it must present it as **recorded intent**, not as a claim about what the module did. That is the same discipline round-62 used for `r24 truth.json embedded_pattern_hex is recorded intent only` (S031's anchor). If the entry instead asserts module semantics, the exclusion no longer holds and the contingency row becomes the landing path — with the search-log text changed to "excluded 0" and that row counted as included, as the landed report instructs.

---

## 4b. Addendum — S033 decision corroborated; S034 (own-work) row also checked

Written after the parent asked for an immediate return; the following facts were gathered in the same pass and are recorded because they land in the same append.

**S033 (Python zipfile docs) — corroborated, no row.** While this review was running, two sibling reports landed and independently record the same decision:
- `.ufo/waves/round-63/build/R63EntryC06.md:164` — "Q12 | n/a | no rejected source row is cited; the Python `zipfile` documentation was screened and excluded without a row, so no reject reason is owed." and `:181-182` — "The Python `zipfile` documentation is **not** cited: the readout is raw `struct` reads plus `zlib` inflate and credits no `zipfile` behavior."
- `.ufo/waves/round-63/build/R63LessonDraft.md:34-37` — "**S033** (Python `zipfile` docs) — recorded as **screened-and-excluded, no registry row**, with the reason: the C06 readout is raw `struct` reads (`grep -c 'import zipfile'` = 0 in both the build readout script and the candidate readout), so no entry sentence credits `zipfile` behavior."

The opener seat's own report (`R63SourceZipfileDocs.md`) was still absent at hand-over; its decision is now corroborated by two sibling reports that state the same exclusion and the same reason, so the §4 verdict stands. The one thing still owed by that seat is the **search-log text** — §4/§5c above is the wording L1 can use if the seat does not land its own.

**S034 (own-work row for the C06 entry) — checked, conformant with one id caveat.** The entry seat's candidate carries a proposed registry row (extracted from `/tmp/revenger-r63-entry/candidate.md`, `## Sources`):

```
| S034 | Authored archive-r2 bytes and the saved archive inventory record — `corpus/fixtures/archive-r2/fixture.zip`, `corpus/fixtures/archive-r2/truth.json`, `corpus/live/runs/20261012T164246Z/artifact-inspection.json` | own-work | A | byte content of one authored ZIP archive and the literal saved fields of one archive inventory record for it, at base commit 55bcb6e1aeb4d42923a4e98db6580f67142b41ac; added scope is central-directory-to-oracle-to-saved-record correspondence, not provider accuracy or completeness | fixture sha256 857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e; truth.json sha256 7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68; saved record sha256 2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380; … | A byte readout of one archive's central directory can be checked field by field against an independent oracle and against one saved record's literal fields, without claiming the record is complete or authentic. | queued | 2026-10-23 | on-release | — |
```

Checks: 12 pipes → 11 cells → **NF=13 PASS**; no `|` inside any cell **PASS**; `kind` `own-work` ∈ enum **PASS**; `tier` `A` for scope "byte content of one authored ZIP archive and the literal saved fields of one archive inventory record" — the lane's own re-runnable bytes, which is contract tier A ("the lane's own re-runnable gate output") **PASS**; `anchor` names exact files + their SHA-256 digests + the base commit, not a homepage **PASS**; `teaches` one grounded benefit **PASS**; `status` `queued` **PASS**; `opened` `2026-10-23` **PASS**; `recheck` `on-release` **PASS**; `used-by` `—` **PASS**. `source` is **path-only, no URL**, so the census' `url_of()` returns empty and the row never enters the duplicate-URL rule (`R62SimplifyEntrySurface` measured) — **no new W04/E04**. The three `source` paths all exist on disk (`corpus/fixtures/archive-r2/fixture.zip`, `corpus/fixtures/archive-r2/truth.json`, `corpus/live/runs/20261012T164246Z/artifact-inspection.json`).

**One caveat, for L1 (id space).** The candidate's own-work row is `S034`, but the contract says the id is "the next unused". With S033 screened out and unused, the next unused after S032 is **S033**, so `S034` leaves a gap. This is *lawful* (round 62 left `S029` unused and recorded it) but the lesson draft currently flags the gap as L1's call (`.ufo/waves/round-63/build/R63LessonDraft.md:45-47`), and this review endorses that framing: **L1 may either take `S033` for the own-work row (contiguous, next-unused) or keep `S034` and record the unused `S033` in the round lesson.** Either is conformant; only `S034` needs the explicit "reserved id went unused" note.

**Second caveat (minor, applies to the lesson's Gate).** The S032 row's anchor cites `§4.4.7`, `§4.4.10-4.4.12` and `§4.4.21-4.4.22`, but the lesson draft's nine S032 quotes (§4.3.12 ×3, §4.3.16 ×2, §4.4.16, §4.4.7 ×2, §4.3.3 — all measured ≤25 words: 7/21/7/8/23/24/23/12/20) and the entry's six §Sources quotes (§4.3.12 ×2, §4.3.16 ×2, §4.4.16, §4.3.3) between them leave `§4.4.10-4.4.12` and `§4.4.21-4.4.22` without a located quote. Contract rule 1 requires *a* ≤25-word quote grounding `teaches`, which is satisfied; the uncovered anchor sections are the name/extra/comment length fields (§4.4.10–4.4.12) and the two total-entries field definitions (§4.4.21–4.4.22), both of which the entry's readout does read. Should-fix, not a blocker: add the two quotes in §5b below (they are verbatim and ≤25 words) so every anchored section has a located quote.

---

## 5. Corrected / recommended row text for L1 to append

Structural defects: **none** — the drafted S032 row is appendable as-is. The following is the same row with Finding 2 applied (anchor gains `§4.3.3`) and Finding 1 applied (the Gate bullet for §4.4.7 split so no quote exceeds 25 words). **The registry text itself is byte-identical to the opener's draft apart from the anchor cell.**

### 5a. Registry row (one physical line; 11 cells; NF=13)

```
| S032 | PKWARE APPNOTE.TXT — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT | spec | A | central directory file header and end-of-central-directory record field layout for one authored ZIP archive: signature values, field order, length fields, CRC-32 and local-header offset | §4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12, §4.4.16, §4.4.21-4.4.22; version 6.3.10 (revised Nov 01, 2022) | The central directory header is a fixed 46-byte record whose crc-32 sits at offset 16 and whose relative offset of local header sits at offset 42, and the end of central directory record is a fixed 22-byte record whose two total-entries counts sit at offsets 8 and 10, so a byte readout of an archive can be checked field by field against the specification. | queued | 2026-10-23 | on-release | — |
```

*(If L1 prefers the opener's anchor byte-for-byte, the row is still conformant — Finding 2 is a strengthening, not a conformance failure.)*

### 5b. `## Gate` bullets for `corpus/lessons/round-63.md` (each ≤25 words, each located, each verbatim)

- **S032** — PKWARE APPNOTE.TXT, `.ZIP` File Format Specification — <https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT> — spec, tier A — accessed **2026-10-23**, HTTP **200**, version **6.3.10** (revised Nov 01, 2022); snapshot `.ufo/waves/round-63/source-snapshots/appnote.txt`, sha256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6` (re-fetched and identical).
  - §4.3.3: "All values MUST be stored in little-endian byte order unless otherwise specified in this document for a specific data element."
  - §4.3.12: "central file header signature   4 bytes  (0x02014b50)"
  - §4.3.12: "crc-32 4 bytes compressed size 4 bytes uncompressed size 4 bytes file name length 2 bytes extra field length 2 bytes"
  - §4.3.16: "end of central dir signature    4 bytes  (0x06054b50)"
  - §4.3.16: "total number of entries in the central directory on this disk 2 bytes total number of entries in the central directory 2 bytes"
  - §4.4.7: "If bit 3 of the general purpose flag is set, this field is set to zero in the local header and the correct" (23 words)
  - §4.4.7: "value is put in the data descriptor and in the central directory." (11 words)
  - §4.4.10-4.4.12: "The length of the file name, extra field, and comment fields respectively." (12 words)
  - §4.4.16: "This is the offset from the start of the first disk on which this file appears, to where the local header SHOULD be found."
  - §4.4.21-4.4.22: "The total number of files in the .ZIP file." (9 words)

### 5c. Search-log note for the screened-out second source — **superseded; use the landed report's §6 text**

My earlier draft wording (identified 2 / screened 2 / included 1) is **superseded**: it does not count the own-work bundle as a document set, which is the convention round-61/62 used and which the landed `R63SourceZipfileDocs.md` §6 follows (identified 3 / screened 3 / included 2 rows — S032 plus the own-work fixture/saved-record row — / excluded 1 without a row). **L1 should paste the landed report's §6 search-log text verbatim**, whose exclusion reason I verified independently (§4 above: the docs page's own deferral quote is verbatim, and its "PKZIP Application Note" hyperlink target is the same APPNOTE URL as S032). The one-line exclusion reason the seat offers for the round lesson `## Gate` is likewise verified and sufficient:

> Excluded without a row: docs.python.org/3/library/zipfile.html (opened 2026-10-23, snapshot sha256 `9520a8cbce7d3c8b7ea6704f60ac1122856da14d1bdc4161075912303a270739`) - the C06 readout is raw struct reads and every format claim rests on PKWARE APPNOTE 6.3.10 (S032), which the zipfile page itself names as the format authority; no entry sentence credits zipfile behavior.

My §4/§5b/§5a text above stands unchanged.

---

## 6. What this seat did and did not do

**Did:** read `corpus/SOURCES.md`, contract v1, `CORPUS.md` §sources-v1, `corpus/QUALITY.md` Q01–Q13, the opener's report and draft row; ran the maintained census (`validate`, `census`) on the live lane and on a scratch copy carrying the candidate row; re-fetched APPNOTE independently and diffed the two revisions; re-derived the §4.3.12/§4.3.16 offsets and byte totals from the spec's own field lists; verified every quote for verbatim-ness and word count; verified the entry readout imports no `zipfile`; verified no new duplicate URL.

**Did not:** edit `corpus/SOURCES.md`; edit `corpus/lessons/`, `corpus/knowledge/`, `corpus/README.md`, `corpus/QUALITY.md`; touch `corpus/live` or `corpus/fixtures` bytes; commit, push, publish or deploy; edit `~/.omp/agent/config.yml` or any routing table; execute any target payload (the ZIP fixture was read as bytes only).

**Scratch:** `/tmp/revenger-r63-sourcesrows/` (row checker `check_row.py`, a scratch `corpus/` copy for census validation, one re-fetched APPNOTE copy) — removed after this report landed.

**Tooling:** none installed or upgraded. No `pacman`, `uv`, `npm` or binary install; no system upgrade. Network use: three `curl` GETs/HEADs to public documentation URLs (pkware cachefly, pkware.com, docs.python.org) for read-only verification. No model arguments set.
