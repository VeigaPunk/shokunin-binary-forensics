# Considerthese mining note — proposal 2 of `considerthese/2026-11-05.md` ("Frozen-counter validity rate")

Seat: ConnectorOverlap (revenger round 93, wave 1). Mined exactly one still-unimplemented proposal. This note does not edit QUALITY.md; the landing shape is the L1's call.

## What the proposal is

File and date: `considerthese/2026-11-05.md`, proposal 2, written by the shokunin-binary-forensics reflection bot (window closing 2026-11-05 10:26 BRT). Verbatim intent: *"Frozen-counter validity rate. Track, per round, how many met-on-the-counter claims were later contested or re-measured as NOT VERIFIED. … A running count turns 'the counter was weak' into a number I can report, and it tells me whether round 92's pre-freeze controls actually reduce it."* The bot had observed that rounds 90 and 91 looked like 2-of-2 in that state and that r92 was the first round to freeze skip-work controls before the claims.

## Measured numbers (committed bytes at lane rev `02050cb2a6758e3bd9cec696ff0e42df6f23511a`, the r93 freeze)

Denominator: every frozen claim of the round (2 per round). Full table with per-row evidence pointers: `measurement.tsv` in this directory; commands: `measurement-commands.sh`.

| round | invalid/total | shape | round outcome |
|---|---|---|---|
| r89 | 2/2 | both outright counter-failures (C1 MISS 10 findings -> 2 vs target 0; C2 KILLED — forged records pass the oracle, runs differ at byte 20) | not admitted (honest stop) |
| r90 | 2/2 | C1 met-contested (M-c real-format blind spot); C2 met-but-NOT-VERIFIED (ctl-idedit and ctl-stub also 6/6) | not admitted (`rejected-honest-stop`) |
| r91 | 2/2 | C1 met-contested (a 21-entry lookup table passes; spot-check re-measured NOT VERIFIED); C2 NOT VERIFIED (stubD/stubE pass) | not admitted (`rejected-honest-stop`) |
| r92 | 2/2 | both met-contested (critic full forgery passes the C1 counter 12/12 legs; partial/held+seed/trailing-cell/record-deletion pass the C2 counter) | **admitted** — on the non-author spot-check's independent re-derivation (§2), counter forgery routed to r93 |

Running rate: **8 of 8 = 100%** across r89–r92. Met-on-the-counter subset (r90–r92): **6 of 6 = 100%** contested or not-verified. The flat 100% answers the bot's question negatively for the window: r92's pre-freeze skip-work controls (do-nothing, junk-stub, positive) were necessary but not sufficient — every r92 counter still had a named forgery class reach it. The controls caught *lazy* skips; the surviving reachability was *skilled* forgery (fabricated votes, id-edited copies, lookup tables, stub instruments), which only the routed successor counters (r93's C1 v2/C2 v2 + `forge_battery.py`) target.

Three measurement-integrity caveats, all verified in the bytes:

1. **Compute from corrections, not first-pass headings.** `SCORECARD.md:1674` (r91 section) still reads "(C1 verified)"/"(C2 capability, verified)" while the verdicts of record are C1 contested and C2 NOT VERIFIED; the correction of record is the r92 SCORECARD correction row (r91 D2) plus the round-91 lesson and spot-check. SCORECARD is append-only, so the stale heading stays; any criterion must name lesson-final-measurements tables + spot-checks + correction rows as the source.
2. **"Later" vs in-round.** The proposal says "later contested"; r92's contest is in-round (critic findings recorded at adjudication). The sub-class split in `measurement.tsv` (failed-killed / met-contested / met-not-verified) keeps both readings computable.
3. **r93 is self-referential.** r93's own claims ARE the anti-reachability instruments. The first meaningful post-fix reading of this rate is r93's adjudication, and the honest appender is a later round (or the closure), not this round's own gate.

## Proposed landing shape (L1 decides; nothing edited here)

Preferred: a **QUALITY.md criterion row** citing `considerthese/2026-11-05.md` proposal 2 (file + date named), with (a) the operational definition fixed to the denominator used here (all frozen claims of the round; invalid = failed-killed, met-contested, or not-verified), (b) the authoritative-source rule (corrections over first-pass headings), and (c) the r89–r92 baseline 8/8 from `measurement.tsv` so a later round appends r93's reading without re-measuring. Alternative: a `corpus/lessons/round-93.md` section recording the same baseline and the append-at-adjudication duty. Precedent for mining-without-adoption exists (r92 spot-check §3 row 6: the 2026-11-04 own-work-ratio proposal was re-measured, agreed, and correctly not adopted as a criterion); this proposal differs in that it is a countable per-round duty with a committed baseline, which is why a criterion row is the better fit.

## Risks

- **Target-gaming:** a round could pick safe claim shapes to keep the rate low. Mitigation: the criterion counts claims, not rounds, and the denominator is frozen per claims.md (2 claims/round in this window).
- **Self-reference:** r93 scoring itself would be the lane grading its own fix. Mitigation: the r93 reading is appended at adjudication by the closure and re-confirmed by r94's opening, mirroring the r89 census-correction pattern.
- **Double-counting revisions:** a claim re-frozen in a later round (none in r89–r92) could count twice; the criterion should key on (round, claim id).
