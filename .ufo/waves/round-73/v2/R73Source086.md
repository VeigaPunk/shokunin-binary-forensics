# R73Source086 — S086 source audit (round-73 v2 wave)

seat: R73Source086 · lane: revenger-shokunin · date: 2026-10-30 · scope: SOURCES.md row S086 only

## Assigned row

`corpus/SOURCES.md:100` (11 cells, unique id — verified `grep -c '^| S086 |' corpus/SOURCES.md` → 1):

- source: Does reverse engineering need a bigger model? — https://rea.tools/blog/reverse-engineering-models/
- kind: docs · tier: A · status: mined · opened: 2026-10-27 · recheck: on-release
- used-by: corpus/knowledge/round-72-tool-landscape.md

## Independent re-open (2026-10-30)

- Fetch: `curl -sSL https://rea.tools/blog/reverse-engineering-models/` → HTTP 200, 48025 bytes, exit 0. No network failure.
- Page identity: title "Does reverse engineering need a bigger model?", byline "By N0zoM1z0 · 13 October 2026" — matches the row's anchor cell exactly (observation).
- Anchor: a "Takeaway" section exists on the page; it is a bulleted list of recommendations (observation).

## Located quote (verbatim, ≤25 words)

> "Train the next useful experiment, and test its oracle."

- Located: final bullet of the "Takeaway" list, https://rea.tools/blog/reverse-engineering-models/, accessed 2026-10-30.
- Word count: 9 words. Verbatim match — page HTML contains the string character-for-character after tag stripping (observation). Markup normalization only: none needed beyond tag/entity stripping.
- Same Takeaway list also contains "The value of feedback depends on what the checker actually verifies." — supports the row's `teaches` cell ("the essay itself cautions that the checker must be understood") and the entry's "checking what it actually verifies" wording (observation).

## Entry wording check (round-72-tool-landscape.md:45)

- "The essay recommends testing the oracle and checking what it actually verifies, while reporting first-party reconstruction experiences." — supported: quote verbatim; first-person reconstruction narrative present on page ("That is the result I …"). Agree.
- "Useful first-person perspective, not independent model benchmarking." — agrees with tier-A scope limited to the author's own stated perspective. Agree.

## Disposition

**Agree with ADMIT, tier A for the author's own stated research perspective only.** No scope widening, no capability claim beyond the essay's self-report, correct recheck policy (on-release) for a living blog page. No rejection flip applies (row is admitted).

## Routed-defect check (round-72-verifier-spotcheck.md)

The spotcheck's routed quote defects cover **S071** (registry quote not verbatim) and **S082** (quote misattributed; actually S083's abstract). S086 is not sampled and not flagged there (`grep -n 'S086' corpus/lessons/round-72-verifier-spotcheck.md` → no match). My re-open confirms no quote defect for S086, so **no superseding row is proposed for S086**; append-only supersession applies to S071/S082 seats, not this row. No other source admission from this seat.

## Classification

- Observation: quote verbatim at cited URL/anchor; page byline/date match row; entry wording supported.
- Inference: none required — all row cells are directly evidenced by the re-opened page.
- Unknown: none. Page content could drift after 2026-10-30; recheck=on-release covers this.

## Environment notes

- No tools installed or updated this seat (curl/python3 already present; pacman paused host-wide, respected).
- Network: single HTTPS fetch, success; no source/network failures to report.
- Reads only under the lane root; scratch /fast/scratch/hyaku/revenger-r73/R73Source086/ (fetched page.html) removed after this report was written. No corpus/shared/sibling/fleet writes; no git/jj mutations; no builds/tests run.
