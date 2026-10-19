# round-1 — non-author verification and spot-check (orchestrator, kaika)

Written by the integrator, not the lane (CORPUS.md: corrections and outside reviews are new
files; the lane owns `round-1.md`). Verifiers were fresh agents dispatched by the orchestrator
after the round landed at `8df2fcefc`; full reports are committed in the fleet repo at
`.ufo/waves/kaika-w3/revenger-review.md` and `revenger-critic.md`.

## Spot-check (LEARNING.md — at least one admit and one reject)

| decision | sample | verifier | result |
|---|---|---|---|
| admit | C11 `utf16-unpaired-surrogates-in-resource-names.md` — its full-file diff and code-unit commands reproduce (`1536 1536 [(741, '0xd8', '0x0')]`); reviewer and critic re-opened S009 (Microsoft PE format, `.rsrc`) and S010 — agree | W3ReviewRevenger | agree |
| reject | `long-term-fixity` candidate rejected under Q01 — agree; RFC 3227 rejection: agree with the reject, disagree with its record (§2.1 Order of Volatility is the very primitive its flip names) — a lesson for the next round | W3ReviewRevenger | agree |

## Adjudication

ADMITTED after post-review fixes `8df2fce` (S008/S012 recheck cadences, Q11 provenance blocks on four entries, M14 pointer correction, expansion command in the report). Per-axis: calibration improved (CALIBRATION 2/4→4/4, REPLAY 8/10→10/10), coverage improved (map rows held 0→4 of 14; capability `sources-registry`, 15 rows, census ok), freshness improved (18 stored assertions re-verified: 8 hold, 10 flagged STALE with current values — a flagging measure, per AXES 'stale items flagged or fixed'), depth/operability/adjacency unchanged. Trends: expansion improved (4 entries: 2 uncovered, 2 partial), quality improved, discernment improved. Debts: SKILL.md absent; receipt-command mutation survivor; F03 verdict vs scout STALE; kaidoku/revenger overlap (ADJ-06) is L0.
