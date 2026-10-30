# R73Source078 — S078 (pwn.college reversing module) source re-audit

Seat: R73Source078 (critic, source-accuracy lane). Round 73, wave v2.
Assigned scope: re-open SOURCES.md row S078 only; compare located quote VERBATIM (markup-normalized), scope, tier, used-by, and rejection flip. No other admission; no edits to corpus/SOURCES.md (append-only superseding rows are reserved for routed defects; none found here).

## Located quote (verbatim, <=25 words)

- Quote: "The program is the judge, not your notes." (8 words)
- URL: https://pwn.college/intro-re-pwn~5933fc84/reversing/
- Access date: 2026-10-30 (this re-open; registry/lesson first accessed 2026-10-27)
- Location on page: "The workflow" section, step 4 (CONFIRM): "Feed your answer to the real program. The program is the judge, not your notes. If it says no, one of your guesses was wrong; go back and find which one."

## Verbatim comparison (markup normalized only)

- OBSERVATION (fetch, HTTP 200, ~142 KB HTML): sentence present verbatim, character-for-character after tag stripping; page title "pwn.college", H1 "Reverse Engineering".
- OBSERVATION: both section headings cited in the registry row exist verbatim: "The workflow" (loop: LOOK / STATIC ANALYSIS / DYNAMIC ANALYSIS / CONFIRM) and "Tools in this dojo" (file/strings/readelf, objdump, ltrace, gdb table).
- OBSERVATION: registry quote cell and lesson Gate row quote are identical; no S071-style registry/lesson divergence.
- OBSERVATION: registry cell's parenthetical "CSE 598 Rev&PA course page" is registrar provenance, not quoted page text ("CSE 598" does not appear on the fetched page); harmless, not a quote defect.
- INFERENCE: quote attribution to "The workflow" is correct — the sentence sits inside that section's CONFIRM-step explanation.

## Scope / tier / used-by / rejection-flip comparison

- Scope: row bounds S078 to "the course's own toy-program learning loop" / "learning lead for authorized toy artifacts only; this lane did not execute any dojo challenge". Fetched page context is the dojo's own challenge artifacts (`/challenge/NAME`, "challenge" x228, "dojo" x48); no real-target authorization language present (0 hits for "real target"/"authorized"/"authorization"). Scope bound is faithful — OBSERVATION.
- Tier A: first-party course page used for what the course itself teaches. Appropriate — INFERENCE (tiering is lane convention; the source is first-party for its own curriculum).
- Used-by: corpus/knowledge/round-72-tool-landscape.md line 40 ("pwn.college and OST2 S078-S079 ... Learning leads only; no challenge, training exercise or instruction set was executed.") matches the registry scope exactly — OBSERVATION.
- Rejection flip: lesson Gate row carries no flip condition for S078 (unlike S071/S072/S074); disposition ADMIT tier A stands. Nothing in the re-opened page expands or undermines the toy-program boundary — OBSERVATION.

## Disposition

AGREE with source disposition: ADMIT, tier A, mined, scoped to the course's toy-program learning loop; quote verbatim and correctly attributed; used-by consistent; no rejection flip warranted. Unlike S071/S082 (routed defects per corpus/lessons/round-72-verifier-spotcheck.md), S078 needs no superseding row.

## Network / source failures

None. Single HTTPS fetch succeeded (curl 8.x, system package, no install needed). No pacman/uv/binary installs this seat (pacman pause honored; nothing required).

## Classification notes

- UNKNOWN (not needed for verdict): whether pwn.college page content changed between 2026-10-27 and 2026-10-30 — no 2026-10-27 snapshot retained locally; current content satisfies the quote predicate.
- UNREACHABLE-is-not-false: n/a; all cited strings were reachable and present.
