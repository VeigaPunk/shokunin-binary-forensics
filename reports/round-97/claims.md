# Round 97 — declared claims (FROZEN before any wave seat scores anything)

Lane: revenger. Base (round start, lane head): `7d380ce2c75d3dfd24dfb7759d04f207eeeb1a68`.
Frozen by the freeze commit recorded in the report (this file + `controls/`). Predicates, targets,
counting commands and kill rules below are not edited after the freeze. A change after any scoring
is a new claim, never this one.

Axes: C1 → **coverage** (lowest owned criterion, K 12/15 = 8.0). C2 → **calibration** (the admission
counter's reach over routed forgery vectors). Two claims, two distinct axes, causally separable:
C1 is verified by a counter that does not read the C2 vectors, and C2 by a battery that does not read
the C02 row.

Ordering contract (enforced by the L1): (a) this file and `controls/` committed; (b) the wave seats build
`c1_k_admit_counter6.py` and its red-before fixtures, and do **not** score the candidate on the landing
tree; (c) the L1 commits the frozen v6 counter; (d) only then the landing tree and the forgery battery are
scored with the committed v6 bytes.

## C1 — coverage: K held-row ground, C02 `partial → held` through a v6 admission counter

- **Surface moved:** coverage-map row C02 (`corpus/README.md`) and the candidate entry
  `corpus/knowledge/round-96-native-analysis-sessions.md` (flip `admission-status: candidate → admitted`
  on the landing tree; the vote-binding digest normalizes that line, so the three r96 votes stay bound).
- **Frozen predicate (one sentence, same in the counter):** C02 counts as held only when the v6 counter
  passes every leg of the r96 v5 set AND the used-by exclusivity leg accepts the census form
  `corpus/knowledge/<entry>` as well as the fixture form `knowledge/<entry>`, for a used-by cell naming the
  admitted entry exactly once across the S502/S503/S504 rows.
- **Before:** `C1_K_HELD_BACKED = 12/15` (K 8.0). Measured at `7d380ce` over `git archive 7d380ce corpus reports .ufo`
  with the frozen v5 counter: `reports/round-97/controls/c1-do-nothing-v5.log` → `C1_VERDICT=fail`,
  `C1_SOURCES=fail` (the only failing leg with the flip absent is the used-by path-form leg), `C1_K_HELD_BACKED=12/15`.
- **After (target):** `C1_K_HELD_BACKED = 13/15` (K 8.67) and `C1_VERDICT=pass` on the landing tree.
- **Counting command:**
  `PYTHONUTF8=1 python3 -B reports/round-97/c1_k_admit_counter6.py --tree <landing-archive-root>`
  Verdict lines: `C1_VERDICT=pass`, `C1_K_HELD_BACKED=13/15`. Exit 0.
- **Do-nothing control:** the base archive (`7d380ce`) under v6 must print `C1_VERDICT=fail` and
  `C1_K_HELD_BACKED=12/15`. A v6 that passes the base tree is wrong; fix before scoring.
- **Red-before (required):** a corpus-prefixed landed-tree fixture on which v5 fails `C1_SOURCES` and v6
  passes it; and a decorated-admitted-line fixture (`admission-status: admitted (…)`) that v5 accepts
  (`C1_ADMITTED_UNION=pass`) and v6 must refuse.
- **Kill rule:** any failing leg of v6 on the landing tree, or K ≠ 13/15 → C1 is **not verified**.
  Honest miss is recorded, never narrowed.
- **Admission caveat:** the counter verifies the measured K move. The r96 votes are lane-internal
  (ReviewerGate, ReviewerBlind, CriticR96); admission of the entry still needs the non-author closure
  (LEARNING.md). This round does not claim non-author admission.
- **Sourced-claim duty (§2b.4):** C1 rests on S502 and S503, which this round re-opens at the pinned revisions
  (access date and located quotes in the lesson `## Gate`).

## C2 — calibration: counter reach over the routed forgery vectors

- **Surface moved:** the admission counter's legs against the CriticR96 vectors (FG01–FG20, FG17 absent, so
  19 vectors) and the MutationR96 `d-host` survivor, which r96 routed to r97.
- **Frozen predicate (one sentence, same in the battery):** a delta counts as *accepted* when the counter
  prints `C1_VERDICT=pass` on the tree carrying that delta; the battery counts accepted deltas over the 19
  frozen vectors.
- **Before (do-nothing control, frozen v5):** `C2_V5_ACCEPTED = 14/19`, from the committed CriticR96 receipts,
  `reports/round-97/controls/c2-v5-reach-from-r96-receipts.txt`. Note: the r96 SCORECARD and lesson state
  **13** accepted; the committed `summary.json` holds **14** `observed_verdict=pass` rows (FG01–FG12, FG15,
  FG19). That mismatch is a calibration finding of this round, recorded here, not silently corrected.
- **After (target):** `C2_ACCEPTED = 0/19` under v6 on the 19 frozen vectors (the same 19 deltas, rebuilt
  byte-for-byte from the r96 receipts into `reports/round-97/forgeries/`), with every vector rejected by at least
  one named failing leg.
- **Counting command:**
  `PYTHONUTF8=1 python3 -B reports/round-97/forge_reach6.py --counter reports/round-97/c1_k_admit_counter6.py --deltas reports/round-97/forgeries`
  Output line: `C2_ACCEPTED=<n>/19`; target `C2_ACCEPTED=0/19`.
- **Positive control:** the landing tree (honest candidate) is accepted by v6 (`C1_VERDICT=pass`); a
  blanket-refusing stub is rejected by the battery's stub check. Without the positive control, a
  refuse-everything counter would score 19/19 rejected and is not a gain.
- **Do-nothing control:** the frozen v5 counter (14/19 accepted) does not reach the target, so the
  target is not reachable by no work.
- **Kill rule:** any vector accepted by v6 → C2 is **not met**. A vector that v6 cannot refuse in
  scope is reported as an honest miss, not excluded.
- **MutationR96 `d-host`:** included as a mutation of v6 (the mutation-tester must show the mutant dies).

## Frontier and duties (§2b, not claims)

- **Census before:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` at
  round start → exit 0 (warnings W01/W04 pre-existing, recorded in the report). Census after: round end, exit 0 required.
- **Mistakes mined** (`corpus/lessons/round-97.md ## Mistakes`): (i) the r96 used-by path-form miss (M5, captured-by
  none, fix = v6 red-before); (ii) the r96 forgery count mismatch 13 vs 14 in SCORECARD/lesson (captured-by none,
  fix = count from committed receipts in the report, shown by the control receipt above).
- **considerthese:** proposal 1 of `considerthese/2026-11-05.md` (counter-reachability review: skip-work controls
  built before the freeze, paper table). Lands as a lesson section; it implements no claim by itself.
- **Assimilation:** none this round. `merge/revenger/` stages 155 rows and all 155 staged ids collide with the lane
  registry (`.ufo/waves/round-97/assimilation/collisions`, 155 lines). Mass id drift → L0 question appended,
  nothing adopted (CORPUS.md / prompt §10).

## Shape

One v1 wave, 10 seats (policy band 8–16): executor 3, scout 1, scribe 1, connector 1, reviewer 2, critic 1,
mutation-tester 1. Attack share 4/10 (reviewer ×2, critic, mutation-tester) ≥ 25 %. Connector seats 1 (≤2).
The planner seat is held by the L1 (the validator rejects `planner`). Godspeed leads every L2 prompt.
