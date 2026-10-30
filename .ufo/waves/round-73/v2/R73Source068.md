# R73Source068 — S068 reopen audit (dnSpyEx continuation fork)

**Seat:** R73Source068 (leaf reviewer, lane-internal). **Date:** 2026-10-30.
**Axes:** coverage; source accuracy. **Assigned row only:** S068. No other source admission.
**Claim context read:** `reports/round-73/claims.md`, `reports/round-73/candidate-pin.json`, `reports/round-73/measure.py` (frozen predicate; C10 candidate `corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md`).

## Verdict (top line)

**DISAGREE with quote verbatimness; AGREE with the source disposition (ADMIT, tier A).** The row's located quote is a cross-location conflation — README opening clause + the GitHub repo-description tagline — not text from the cited README pin. Routed quote defect, same failure class as S071 (paraphrase). Proposed superseding row **S429** below (append-only; old rows untouched).

## Independent reopen evidence

- Pinned README `https://raw.githubusercontent.com/dnSpyEx/dnSpy/de5a83051161e0becc70f32834c2596db6239fbd/README.md` — HTTP 200, 4824 bytes, sha256 `c9f5030bc9ddd3a76fdc4890219066dfea4c1a391aa86644930cd84a9061ecff`, fetched 2026-10-30. Line 3 (markup-normalized): "dnSpyEx is an unofficial continuation of the dnSpy project which is a debugger and .NET assembly editor. You can use it to edit and debug assemblies even if you don't have any source code available. Main features:". **[OBSERVATION]**
- Current `master` README — HTTP 200, byte-identical to the pin (same sha256 `c9f5030b…`). **[OBSERVATION]**
- Commit metadata for pin `de5a83051161e0becc70f32834c2596db6239fbd` (GitHub API, HTTP 200): author date 2023-11-05, message "Typo fix in README.md (#257)". Confirms the row's/entry's "README revision is from 2023" statement. **[OBSERVATION]**
- README history scan (`commits?path=README.md`, HTTP 200): prior revisions `e9a57f052456` (2023-08-20), `81e9c2ee1392` (2023-06-22), `3d8a34d298fe` (2022-03-26) all read "dnSpyEx is a unofficial continuation of the [dnSpy](https://github.com/dnSpy/dnSpy) project which is a debugger and .NET assembly editor." — no revision checked contains "well known". **[OBSERVATION]**
- Original dnSpy README `https://raw.githubusercontent.com/dnSpy/dnSpy/master/README.md` (HTTP 200): "dnSpy is a debugger and .NET assembly editor." — no "well known" phrase. **[OBSERVATION]**
- GitHub repo metadata API (HTTP 200): repository **description** field reads "Unofficial revival of the well known .NET debugger and assembly editor, dnSpy". This is the origin of the quoted tail. `pushed_at` 2026-10-17 (recent repo activity exists, but the row scopes out maintenance cadence, so no row claim is violated). **[OBSERVATION]**

## Comparison against row, lesson, entry

- `corpus/SOURCES.md:82` (S068) quote: "dnSpyEx is an unofficial continuation of the well known .NET debugger and assembly editor, dnSpy" — **NOT verbatim** at the cited pin, even after markup-only normalization (`[dnSpy](https://github.com/dnSpy/dnSpy)` → `dnSpy`): substring test fails. "well known" appears nowhere in the README (grep, exit 1). The string joins the README's opening clause with the repo-description tagline. 15 words — passes the mechanical ≤25 count while failing attribution (the exact failure mode `corpus/lessons/round-72-verifier-spotcheck.md` documents: "The word-count check did not establish quotation attribution"). **[OBSERVATION]**
- `corpus/lessons/round-72.md:27` (S068 Gate row): carries the same conflated quote; ADMIT decision otherwise consistent with evidence. **[OBSERVATION]**
- `corpus/knowledge/round-72-tool-landscape.md:27` ("Need managed assembly inspection"): paraphrases accurately ("calls itself an unofficial continuation and describes similar .NET/Unity functions"); boundary "README was last revised in 2023 in the opened history; active maintenance is not asserted" is confirmed by the 2023-11-05 pin commit. Used-by link is accurate. **[OBSERVATION]**
- Scope (`The fork's own README feature scope and self-description; not evidence of current maintenance cadence or target compatibility`): README lists Debug/Edit .NET and Unity assemblies, themes — scope accurate. Tier A for the project's own self-description is appropriate. No rejection flip applies (admitted row). **[OBSERVATION]**
- Predicate note: S068 is outside the frozen counter's `S096–S109` range, so this defect does not bear on `C10_HELD_BACKED`; it is a source-accuracy finding under this wave's fetch/substring audit duty over S054–S095. **[OBSERVATION]**

## Correct located quote (verbatim, markup-normalized)

> "dnSpyEx is an unofficial continuation of the dnSpy project which is a debugger and .NET assembly editor"

- Words: 17 (≤25). **URL:** https://github.com/dnSpyEx/dnSpy (README at pinned commit `de5a83051161e0becc70f32834c2596db6239fbd`). **Access date: 2026-10-30.**

## Proposed superseding row (append-only; never edit old row)

Next free registry id is **S429** (S427/S428 taken by round-73's S071/S082 supersessions; registry count 428):

`| S429 | dnSpyEx — https://github.com/dnSpyEx/dnSpy | tool | A | Correction of S068 located quote: verbatim README opening, same bounded scope | README.md at de5a83051161e0becc70f32834c2596db6239fbd, accessed 2026-10-30; "dnSpyEx is an unofficial continuation of the dnSpy project which is a debugger and .NET assembly editor" | The repository self-describes as a continuation and lists .NET/Unity debugger/editor features; no claim of active maintenance is made because the README revision is from 2023 | mined | 2026-10-30 | on-release | corpus/knowledge/round-72-tool-landscape.md |`

## Disposition agreement

**AGREE** with ADMIT, tier A, bounded to the fork's own README self-description and feature list; correctly barred from any maintenance/cadence or compatibility claim; used-by and flip fields accurate as recorded. Only the located quote is defective.

## Failures / uncertainty

- GitHub code-search API for "well known" in-repo returned **401 (requires authentication)** — cannot exhaustively exclude the phrase in unvisited historical paths; not load-bearing (README history directly checked, current tree hash-verified). **[UNKNOWN]**
- All other fetches succeeded (README pin, master README, dnSpy original README, commits API, repo API). No target execution performed, none implied by the row.

## Tooling

- No installs/updates this seat; `curl` and `python3` (system, existing) used. Pacman pause honored; no host changes. Receipts (README.pinned.md, README.current.md, README.dnspy-original.md, commit-meta.json, readme-history.json, repo-meta.json) in scratch `/fast/scratch/hyaku/revenger-r73/R73Source068/`; scratch removed after report write.
