FAIL — Gate located-quote pointers are false for 2 of 3 sourced rows (S038 span, S039 line) and S040's stated word count is false; snapshot hashes, registry append, mistake-row shape and both fix demonstrations otherwise verify.

Seat: R65LessonDraft (scribe/checker), read-only. Target under test:
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-65.md`
(8488 bytes, sha256 `f55e34110a8b384d98db9b43faba04be94ec516e2f7dc7a8ccdb952fa6531626`, 42 lines).
Rule sources used: seat brief (`## Gate` URL/access date/≤25-word located quote per new row; `## Mistakes` class/evidence/captured-by/fix; fixes shown able to fail), `corpus/lessons/round-1.md:68` (“Quotes ≤25 words, verbatim”), `corpus/lessons/round-64.md:70` (“Every located quote must be at most 25 words and verbatim against the pinned snapshot”), normalization precedent `corpus/lessons/round-63.md:33-34` / `round-62.md:59-60`.

## Rule-by-rule result

| Rule element | Result | Evidence |
|---|---|---|
| Snapshot hash per quoted source | PASS | `sha256sum` of `.ufo/waves/round-65/source-snapshots/*` equals the three hashes in the lesson: `56b88bc4…c56f` (ResourceTypes.h, 86255 B), `412d9cb4…874c` (rea-android-applications.md, 1992 B, 34 lines), `e7fe6715…49c6a` (zipfile-docs.html, 139782 B). Sizes and the “34 lines” claim also match (`wc -c`, `wc -l`). |
| Access date per new row | PASS | All three sourced bullets say “opened 2026-10-24”; date matches snapshot mtimes (`ls -la`, Oct 24 02:33/02:34) and today. S041 is own-work (see V8). |
| URL per new row | PARTIAL (V5) | S038 ✓, S040 ✓, S039 has repo+tag+path but **no URL**; S041 own-work, no URL (precedent `round-64.md:103-108` S037). |
| ≤25-word quote per new row | PASS on length, FAIL on location/count (V1–V3) | Actual counts 23 / 17 / 14 — all ≤25. Stated counts 23 / 17 / **16** (S040 wrong). |
| Quote verbatim against snapshot bytes | FAIL for S038, S039; PASS for S040 | Byte test below. |
| `## Mistakes` rows carry class/evidence/captured-by/fix | PASS | M38 and M37 each have 5 populated cells (id + 4); measured by cell split, `corpus/lessons/round-65.md:29-30`. |
| Fixes shown able to fail | PARTIAL | M38 instance 1 ✓ by execution; M38 instance 2 has no failing assertion (V6); M37 ✓ by selftest implementation + base log line. |

## Violations, verbatim

**V1 — S038 located-quote span is wrong and the quote is not a byte run.**
Lesson `:12` says: `Located quote, lines 608-611 (comment above `struct ResXMLTree_header`): "It is followed by a flat array of ResXMLTree_node structures; the hierarchy of the XML document is described by the occurrance of RES_XML_START_ELEMENT_TYPE" (23 words).`
Snapshot bytes (`grep -n` on `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots/ResourceTypes.h`):
```
607: * describing its content.  It is followed by a flat array of
608: * ResXMLTree_node structures; the hierarchy of the XML document
609: * is described by the occurrance of RES_XML_START_ELEMENT_TYPE
610: * and corresponding RES_XML_END_ELEMENT_TYPE nodes in the array.
611: */
```
The quote begins mid-line **607** and ends mid-line **609**; 610–611 contain no quoted words. Byte test: literal substring `False`; after stripping the ` * ` comment gutter and collapsing newlines `True` (23 words confirmed). The lesson declares no normalization convention, so the quote cannot be read as conformant to `round-1.md:68` “verbatim”.

**V2 — S039 line pointer is wrong (“line 5” vs 7), and the quote needs an undeclared cross-line join.**
Lesson `:13`: `Located quote, line 5: "Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence." (17 words).`
Snapshot: `7: Start with \`inspect_android_package\` on the caller's APK path for package` / `8: identity, manifest declarations, coverage, and inline Evidence. Use`. Line 5 of the snapshot is `older server.` Literal substring `False`; whitespace-normalized join of 7–8 `True` (17 words confirmed). The identical wrong pointer is repeated in the registry: `corpus/SOURCES.md:53` (“line 5 and the "The provider requires" paragraph”; that paragraph is at snapshot line 16). S039 also has no URL (V5).

**V3 — S040 word count is false and no line pointer is given.**
Lesson `:14`: `...(16 words)`. The sentence is **14** words (`len(q.split())`); still ≤25, so only the stated number is false. Snapshot `zipfile-docs.html` has 1494 lines; the sentence occurs in the visible module description at body lines **234–235** and in three meta-description attributes at lines 11/15/16. The lesson locates it only as “module description”, unlike the line-numbered form used for S038/S039 and the `S036_QUOTES=snapshot lines 3-4 …` form in `round-64.md:90`.

**V4 — normalization is undeclared.** The Gate preamble (lesson `:10`) and the bullet list contain no “normaliz/whitespace/verbatim” clause (`grep -n "normaliz\|whitespace\|verbatim" corpus/lessons/round-65.md` → no match). Rounds 62 and 63 declare it explicitly (`round-63.md:33-34`: “verbatim against the pinned snapshot; whitespace in the snapshot is normalized, no word is invented”). Without that clause V1/V2 read as verbatim failures; with it, the remaining defect is the false line span.

**V5 — S039 carries no URL.** `:13` gives `morluto/rea`, tag `rea-agents-6.5.0`, and the in-repo path; `corpus/SOURCES.md:53` is the same. S036 (a docs row of the same provenance family) carries a full URL (`round-64.md:84`). Locator is resolvable (repo+tag+path), so severity is low.

**V6 — M38's second caught instance has no failing check.** M38's fix cell (lesson `:29`) says “…derive the pool-header width from the struct's own five trailing u32s … Shown able to fail: the same readout against the buggy bytes exits non-zero …”. The red/green demonstration exercises only the node chunk-size instance. The pool width is *emitted* (`corpus/fixtures/apk-r65/readout.py:61-68`, `string_pool_header_size`) but never asserted against the observed `headerSize` collected at `readout.py:137`; a regression 28→24 would print a wrong number and still exit 0. Additionally, the committed red-before log already shows the corrected value (`"string_pool_header_size": 28`, `.ufo/waves/round-65/m38-red-before.log:2`), so instance 2's red state exists only as prose. Instance 1's demonstration is sound: the log's chunk table carries `"size": 4294967295` at offset 280 and ends in `StopIteration` at `readout.py:179`.

**V7 — M37's evidence pointer is a bare seat name.** `:30`: `routed by R64ReviewSeparability: the round-64 probe's `rejected_marked` scanned only the first 2000 bytes…`. The report resolves at `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/R64ReviewSeparability.md:137-138` (finding 2, naming `measure.py:38-41`), but the row gives no path/line. Substance holds: `reports/round-65/measure.py:56-60` seeds `b"A"*3000 + marker`, asserts `old_window_miss` and `new_window_hit`; `reports/round-65/measure-before.log:6` records `STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True`. Marker offsets 859 and 712 verified exactly (`python3` byte scan of `corpus/knowledge/*.md`).

**V8 — S041 records no URL/quote/access date and delegates its digests.** `:15`: “authored this round; digests in the registry row and the entry header.” Own-work rows are exempt from URL/quote by precedent (`round-64.md:103-108` lists S037's digests inline; also `corpus/SOURCES.md:9`). Substance is present in `corpus/SOURCES.md:55` (four digests) and the entry header; only the recording style deviates.

**V9 — census command path does not exist in the lane.** `:17`: “seven manual census commands and `scripts/sources-census.sh validate` both exit 0 at round end.” `ls -d scripts` in the lane root → `No such file or directory`. The script lives at `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`. Claim substance verified from the fleet root: `bash scripts/sources-census.sh validate revenger-shokunin` → four disclosed `W04` lines (S024/S028/S029/S034) plus `ok …/corpus/SOURCES.md`, **exit 0**. The “seven manual census commands” have no receipt and are not re-runnable from the written path.

## Corroboration and conflict (reported, not adjudicated)

`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-65-verifier-spotcheck.md:50` states for S038: “quote at lines 608–611 verbatim, 23 words ≤ 25”. My byte check contradicts the span and the “verbatim” status (V1). The same file already routed “D2” for the S039 “line 5” pointer (`:52`), agreeing with V2. Reported verbatim for the canonical judge; I made no edit to either file.

## Lesson claims that verified (so the failure is localized)

- `git log --format='%h %s' -3 -- reports/round-65/claims.md` → `5a2e7a0 round-65: pre-registration …` — matches “pre-registration … at 5a2e7a0”.
- `git show 3eebcdd7…:corpus/SOURCES.md | grep -c '^| S[0-9]'` → `37`; current → `41`; `git diff --numstat 3eebcdd7… -- corpus/SOURCES.md` → `4 0`; deletions count → `0`. Rows 37→41 and “no pre-existing row changed” both hold.
- Fixture: `947` bytes, sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` — matches lesson `:22` and `corpus/SOURCES.md:55`.
- C5 transplant IDs are real and foreign as claimed: `ev_6e055332…` present under `corpus/live/runs/round-42/`, `ev_8ed88983…` under `corpus/live/runs/round-47/` (`grep -rl`).
- C5 patch shape: regex `receipt\['evidence_id'\]\s*==\s*evidence_id` matches exactly **1** per script; `git diff --numstat 3eebcdd7… -- corpus/verify_icon_languages.py corpus/verify_multi_icon_states.py` → `3 0` and `3 0` (insertions only, `receipt_ok` untouched); attribution phrase at `verify_icon_languages.py:157` and `verify_multi_icon_states.py:156`.
- Counter receipts: `reports/round-65/measure-before.log:6,42-45` → `STRICT…=pass old_window_miss=True`, `C5_CONTROL_PRESENT=0/2`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2`; `measure-after.log:42-45,60` → `2/2`, `2/2`, `HOLDS_OK_V3=yes`; `K_HELD=8/14`, `K_ROW C05 status=frontier` at both ends — consistent with the lesson's honest “CANDIDATE LANDED, admission pending” and with the brief's build state (README not flipped).
- Wave shape `:42`: `.ufo/waves/round-65/wave-spec.json` has 64 items; roles `reviewer 20, executor 10, critic 10, scout 9, mutation-tester 7, scribe 4, sentinel 1, simplifier 1, revenger 1, connector 1`; `plan-validated.json` → `counts {spawn:64}`, `dispatch.calls=1`, 64 tasks. “64 seats, ≥25% attack roles” holds under any attack definition that includes mutation-tester+critic (17/64 = 27%). The `plan` exit-0 itself was not re-run by me (artifact-backed only).
- M38 evidence file: sha256 of `.ufo/waves/round-65/m38-red-before.log` = `aaba825263b5ce3613d8972831fa0e92bb7805547846056103e526293d814392` — matches the row.
- M38 fix description matches landed code: `corpus/fixtures/apk-r65/generator.py:67-70` (`struct.pack("<HHI", chunk_type, 16, 8 + len(payload))`, docstring “inside headerSize (16)”).

## Repair list (cheap, in-place; no claim is harmed by any of them)

1. `:12` span `608-611` → `607-609`; add the normalization/verbatim clause to the Gate preamble (copy `round-63.md:33-34` form).
2. `:13` `line 5` → `lines 7-8`; add S039's URL (or record the repo+tag+path locator as the row's URL-form and say so); `corpus/SOURCES.md:53` carries the same wrong pointer — fix at next touch, never by in-place rewrite of a mined row.
3. `:14` `(16 words)` → `(14 words)`; add `body lines 234-235` (or `meta description lines 11/15/16`).
4. `:17` `scripts/sources-census.sh` → `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` (or record it as fleet-root-relative).
5. `:29` either add the derived-vs-observed width assertion to `readout.py` (making instance 2’s fix able to fail) or scope the “Shown able to fail” sentence to the chunk-size instance.
6. `:30` add the resolving path `.ufo/waves/round-64/R64ReviewSeparability.md:137-138`.
7. `:15` inline S041’s four digests, matching `round-64.md:103-108`.

## Axes (as judged on this seat)

- coverage: every element of the three stated rule elements checked against bytes for all four new rows; 9 distinct defects recorded with pointers.
- calibration: the check is falsifiable and demonstrated failing — the same procedure passes S040’s literal quote and fails S038/S039, and it independently reproduces the spotcheck’s D2. No claim in C1/C2 was scored or re-measured by this seat.

## Touched surfaces

- Written: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/R65LessonDraft.md` (this file) only.
- Read-only: lane `corpus/lessons/`, `corpus/SOURCES.md`, `corpus/fixtures/apk-r65/{fixture.apk,readout.py,generator.py,truth.json}`, `corpus/verify_*.py`, `reports/round-65/*`, `.ufo/waves/round-65/*`, `.ufo/waves/round-64/R64ReviewSeparability.md`, `scripts/sources-census.sh` (fleet root). No git/jj mutation; `git show`/`git diff`/`git log` read-only queries only. No subagents. No tool installs (nothing needed; pacman paused, none attempted).

## Out of scope / not done here

Counter re-measurement on a committed tree, README C05 flip, Q01–Q13 admission, C5 mutant execution, fixture regeneration, entry-content review. Measurements cited from `measure-before.log`/`measure-after.log` are L1 artifacts; `measure-after.log`’s tree commit and provenance are for the counter seats.

## Artifact paths

- Under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-65.md`
- Snapshots: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots/{ResourceTypes.h,rea-android-applications.md,zipfile-docs.html}`
- Red-before: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/m38-red-before.log`
- Contract/claims: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md`, `measure.py`, `measure-before.log`, `measure-after.log`
- Registry: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:52-55`
- Prior spotcheck (read, not edited): `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-65-verifier-spotcheck.md:50-52`
- Precedent rules: `corpus/lessons/round-1.md:68`, `round-62.md:59-60`, `round-63.md:33-34`, `round-64.md:70,90,103-108`
