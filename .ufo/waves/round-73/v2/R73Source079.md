# R73Source079 — S079 (OST2 Architecture 1001 x86-64 Assembly) source re-audit

Seat: R73Source079 (critic, source-accuracy lane). Round 73, wave v2.
Assigned scope: re-open SOURCES.md row S079 only; compare located quote VERBATIM (markup normalized only), scope, tier, used-by, and rejection flip. No other admission; no edits to corpus/SOURCES.md (append-only superseding rows reserved for routed defects; one anchor imprecision found here — proposal at bottom, old row untouched).

## Located quote (verbatim, <=25 words)

- Quote: "This class teaches Intel x86 assembly language. It requires you know C programming." (13 words)
- URL: https://p.ost2.fyi/courses/course-v1%3AOpenSecurityTraining2%2BArch1001_x86-64_Asm%2B2021_v1/about
- Access date: 2026-10-30 (this re-open; registry/lesson first accessed 2026-10-27)
- Location on page: `<meta property="og:description" content="...">` in the page `<head>` (raw-HTML line 114, byte offset 3533 of 20496) — NOT in the visible "About This Course" body text.

## Verbatim comparison (markup normalized only)

- OBSERVATION (fetch, HTTP 200, 20496 bytes, sha256 12c526126cd168acf6283b0ff36dbe8b1d2e28d0a4545d483d9fe186c7e2dd2e; two independent fetches byte-identical): the quoted sentence is present character-for-character in the og:description meta tag: `<meta property="og:description" content="This class teaches Intel x86 assembly language. It requires you know C programming." />`.
- OBSERVATION: under visible-text extraction (script/style stripped, tags stripped, entities decoded), the quote is ABSENT: "This class teaches", "teaches Intel x86", "It requires you know" all 0 hits. The visible "About This Course" body instead reads "It teaches the basic concepts and describes the hardware that assembly code deals with. It also goes over many of the most common assembly instructions..." (truncated in display at "students will be show…" but full sentence present in raw HTML).
- OBSERVATION: the visible "Requirements" section says "You must be comfortable with C programming." — same substance, different wording from the quoted clause "It requires you know C programming."
- OBSERVATION: page `<title>` "Architecture 1001: x86-64 Assembly | OpenSecurityTraining2" matches the registry row's named course; URL carries the 2021_v1 course run id as cited.
- OBSERVATION: registry quote cell (SOURCES.md line 93) and lesson Gate row (corpus/lessons/round-72.md line 38) carry the IDENTICAL quote string — no S071-style registry/lesson divergence.
- INFERENCE: the quote is verbatim-located at the cited URL, but the registry anchor field ("About This Course" and "Requirements") names visible sections that do not contain it; the true locus is the page's OpenGraph description metadata, which is course-authored summary text on the same cited page.

## Scope / tier / used-by / rejection-flip comparison

- Scope: registry bounds S079 to "the named 2021 course page's prerequisites and stated relation to RE; not a claim that its lessons were completed". Fetched page supports both halves: About body names "reverse engineering" among specialties the course underpins; Requirements states C-programming comfort; nothing on the page asserts this lane completed any lesson. Scope faithful — OBSERVATION (page) + INFERENCE (scoping judgment).
- Tier A: first-party course page (OpenSecurityTraining2's own platform) used for what the course itself states about scope/prerequisites. Appropriate; not tier inflation — INFERENCE (tier is lane convention).
- Used-by: corpus/knowledge/round-72-tool-landscape.md line 40 ("pwn.college and OST2 S078–S079 | Their course pages describe toy reverse-engineering exercises and x86-64 assembly prerequisites/workflows. | Learning leads only; no challenge, training exercise or instruction set was executed.") — matches registry scope exactly; path exists — OBSERVATION.
- Rejection flip: lesson Gate row for S079 is an ADMIT with no flip condition (unlike S071/S072/S074); nothing in the re-opened page expands or undermines the admitted scope — OBSERVATION.
- Predicate impact: S079 is outside the C10 mined range S096–S109; this audit has no effect on the C10_HELD_BACKED counter — OBSERVATION.

## Disposition

AGREE with source disposition: ADMIT, tier A, mined, scoped to the stated 2021 course scope/prerequisite; not a completed course. Unlike S071 (registry paraphrase) and S082 (quote belonging to a different source) per corpus/lessons/round-72-verifier-spotcheck.md, the S079 quote is verbatim AT the cited URL, so the admission's evidential basis holds.

One imprecision, fixable, same family as the routed defects but lower severity: the anchor names visible sections; the quote lives in og:description metadata. Smallest safe correction, per contract rule 2 (corrections are new rows; old row never edited) and the S427/S428 precedent:

PROPOSED superseding row (integrator assigns next unused id, S429 observed free; NOT written by this seat — read-only):

| S429 | OpenSecurityTraining2 Architecture 1001 x86-64 Assembly — https://p.ost2.fyi/courses/course-v1%3AOpenSecurityTraining2%2BArch1001_x86-64_Asm%2B2021_v1/about | docs | A | Correction of S079 quote anchor: og:description metadata, not the visible About body | og:description meta tag + visible "Requirements" section, course Arch1001_x86-64_Asm+2021_v1, accessed 2026-10-30; "This class teaches Intel x86 assembly language. It requires you know C programming." | supersedes S079 — quote verbatim in the about page's og:description; visible Requirements body corroborates with "You must be comfortable with C programming."; admission scope/tier unchanged. | mined | 2026-10-30 | 180d | corpus/knowledge/round-72-tool-landscape.md, corpus/lessons/round-73.md |

If the integrator judges metadata-located quotes acceptable under "normalizing markup only" with the anchor caveat recorded in the lesson, agreeing-with-disposition stands without the new row; either way the old S079 row stays untouched.

## Network / source failures

None. Single HTTPS fetch of the cited URL succeeded (curl, system package — no install). No pacman/uv/npm/binary installs this seat; host pacman pause honored.

## Classification notes

- OBSERVATION: all page-content claims above are from the 2026-10-30 fetch (sha256 recorded); byte offsets and line numbers cited.
- INFERENCE: og:description is course-authored summary text maintained by OST2 for the same cited page; treat as first-party page content, not third-party commentary.
- UNKNOWN: whether the 2026-10-27 fetch saw identical bytes — no local snapshot retained; current content satisfies verbatim quote location either way (meta tag present now).
- UNREACHABLE-is-not-false: n/a; all cited strings reachable and verified.
