# Round 99 — declared claims (FROZEN before any wave seat scores anything)

Lane: revenger. Base (round start, lane head): `3d054a98e3fa768e63b631665a2372fadb51a77a` (the r98
closure spot-check tip). This file, `controls/` and the candidate edit below are frozen by the
claims-freeze commit recorded in the report. Predicates, targets, counting commands and kill rules
below are not edited after the freeze. A change made after any scoring is a new claim, not this one.

Axes: C1 → **coverage**, the lowest owned criterion (K 13/15; C05 `uncovered`, C14 `partial`).
C2 → **calibration**, the admission counter's reach over the round-98 fresh holdout. Two claims on
two distinct axes, causally separable: C1 is scored by the v8 counter's `c14r99` profile on the
landing tree; C2 is scored by the v8 counter's `c02` and `c14` profiles on the round-98 holdout
fixture trees, which the builder makes from pinned inputs (the frozen v6 `_fixture` for c02, the
r98 Amendment-C archive `1b76b4d` for c14) and which never read the round-99 votes, the round-99
README or the edited entry.

Ordering contract, enforced by the L1:
(a) this file, `controls/`, the candidate edit (`admission-status: candidate`) and the round-99
    S506/S507 re-open receipts are committed (the claims freeze);
(b) wave seats build `reports/round-99/c1_k_admit_counter8.py`, its self-test and the harness
    `reports/round-99/forge_reach8.py`; voters cast votes on the candidate; no seat runs any counter
    on a landing tree (C14 held);
(c) the L1 commits the frozen v8 bytes (the v8 freeze);
(d) only after (c): the C1 do-nothing and junk-row controls, the C2 run, then the landing tree, then
    the fresh round-99 holdout (reported, not a target).

## C1 — coverage: C14 `partial → held` through the v8 counter (`c14r99` profile)

- **Surface moved:** coverage-map row C14 (`corpus/README.md`): knowledge cell becomes exactly
  `knowledge/round-98-rea-host-readiness.md`, status `held`; the entry moves
  `admission-status: candidate → admitted` (pending the non-author closure, stated in the body,
  never in the header line). This is the round-98 candidate with the four routed defects fixed:
  - Q11: the "three installation paths" derivation row now counts paths, not lines, and prints `3`;
  - Q16: the two doctor-printed versions (`12.1.4`, `21.0.13`) are credited to the doctor record and
    derived; the preamble credits only the remaining version strings to the probe transcript, which
    prints each of them (`controls/q16-version-attribution.log`);
  - three further derivation rows (ghidra scope-check names, doctor-printed versions, engine and jadx
    classifications), each with the command's exact stdout;
  - PASS notes: every voter writes PASS notes of ≥ 6 tokens, specific and distinct (the `C1_VOTE_NOTES`
    rule), on a fresh digest.
  Lint: `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-98-rea-host-readiness.md --lane .`
  → `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, rc 0 (`controls/lint-candidate-freeze.log`).
- **Vote-binding digest (v6/v7 `digest()` rule):**
  `36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5`. Any entry edit other than the
  admission-status line invalidates the votes.
- **Frozen predicate (one sentence, the same in the counter):** C14 counts as held only when the v8
  counter, run with `--profile c14r99`, passes every leg it prints; that set is every v7 `c14` leg
  with the round-99 votes dir `reports/round-99/votes`, wave dir `.ufo/waves/round-99`, registry
  `.ufo/waves/round-99/w1/swarm-registry.json`, the round-99 pinned seats and `FREEZE_REV` = the
  claims-freeze commit, plus every new v8 leg.
- **Before:** `K = 13/15` held; C14 `partial` at `3d054a98` (`controls/c1-base-rowstatus.log`).
- **After (target):** `C1_K_HELD_BACKED=14/15` and `C1_VERDICT=pass`, exit 0, from
  `PYTHONUTF8=1 python3 -B reports/round-99/c1_k_admit_counter8.py --profile c14r99 --tree <landing-archive-root>`.
- **Do-nothing control (after the v8 freeze, before landing scoring):** the same command on
  `git archive` of the claims-freeze commit must print `C1_VERDICT=fail`.
- **Junk-row control (after the v8 freeze, before landing scoring):** the claims-freeze tree with only
  the C14 status cell edited to `held` must print `C1_VERDICT=fail`.
- **Kill rule:** any failing leg on the landing tree, K ≠ 14/15, or a control that passes means C1 is
  **not verified**; an honest miss is recorded, never narrowed. Any vote recording a FAIL decision fails
  `C1_VOTES` and therefore C1. **Amendment budget:** at most one candidate amendment, only before the
  v8 freeze and before any landing scoring, with a new digest and a full re-vote by the same pinned
  voters; a FAIL after that amendment kills C1.
- **Sourced-claim duty (§2b.4):** C1 rests on S506 (re-opened this round at the pinned revision,
  2026-11-05T18:43:20-03:00, http 200, 16650 bytes, sha256 `ce2d122b…`, byte-identical to the
  committed body, located quote count 1: `quote-receipts/S506-reopen-r99.txt`) and S507 (the saved
  record re-hashed this round: `controls/s507-reopen-r99.txt`).

## C2 — calibration: counter reach over the round-98 fresh holdout

- **Surface moved:** the admission counter's legs against the round-98 holdout classes that frozen v7
  accepts: c02 `V01` hidden-dissent uppercase vote file, `V02` criterion-id-list n/a reason, `E01`
  recheck with no command, `E02` two-run clause count, `E03` coverage-map header naming another row;
  c14 `R01` suffix row outside the count, `V02` FAIL under an out-of-range key, `O01` own-work pointer
  of another round, `L01` fetch-log date vs receipt `fetched_at`.
- **Frozen predicate (one sentence, the same in the harness):** a vector counts as *accepted* when the
  counter prints `C1_VERDICT=pass` on the tree carrying that vector; the harness counts accepted
  vectors over all twelve round-98 holdout vectors (six c02, six c14) built by
  `.ufo/waves/round-98/w1/CriticR98/fresh/build_fresh98.py` with the r98 parity patch
  `.ufo/waves/round-98/w1/L1-holdout-v7/parity-patch.diff` applied to a scratch copy, the counter run as
  `--profile c02` and `--profile c14` (the v7 round-98 constants, unchanged in v8).
- **Before (do-nothing control, frozen v7, run this round before the freeze):** `accepted = 9/12`
  (c02 5/6, c14 4/6), both `HOLDOUT98_CONTROL=control-ok`
  (`controls/c2-do-nothing-v7-holdout98-c02.log`, `controls/c2-do-nothing-v7-holdout98-c14.log`).
- **After (target):** one recorded run prints `C2_ACCEPTED=0/12`, `C2_CONTROL_C02=control-ok`,
  `C2_CONTROL_C14=control-ok` and `C2_STUB_SELFTEST=ok` (an always-pass stub counter scores 12/12 and an
  always-fail stub 0/12 on the fully built vector trees), and `C2_VERDICT=met`.
- **Counting command:**
  `PYTHONUTF8=1 python3 -B reports/round-99/forge_reach8.py --counter reports/round-99/c1_k_admit_counter8.py --work <scratch>`
- **Kill rule:** `C2_ACCEPTED` ≠ 0/12, either control not `control-ok`, or `C2_STUB_SELFTEST` ≠ ok means
  C2 is **not met**.
- **No-regression (reported, a harm check):** the r98 development set under v8:
  `reports/round-98/forge_reach7.py --counter reports/round-99/c1_k_admit_counter8.py --profile c02`
  must still print `C2_ACCEPTED=0/5` with both positives; and v8 `--self-test` must print OK. A failure
  is reported as harm to calibration.
- **Development-set disclosure:** v8 is developed against these twelve vectors, so 0/12 is a
  development-set result. A fresh round-99 holdout is written by the critic seat and run once by the L1
  against the frozen v8, reported separately; no counter change responds to it this round.
- **Real-tree positive (reported):** v8 `--profile c02` on the landing archive is a diagnostic under
  the r98 Amendment A1 rule: no harm to C02 when the C02 README row is byte-identical to the base and
  every failing c02 leg is `C1_ONLY_TARGET` naming only C14.

## Frontier and duties (§2b, not claims)

- **Census before:** exit 0 at base `3d054a98` (`controls/census-round-start.log`). Census at round
  end, exit 0, required.
- **Mistake mined:** the r98 Q11 count-by-lines defect (a derivation command that prints `1` credited
  with "three"), with the fix shown able to fail (the old command prints 1, the new prints 3:
  `controls/q11-paths-old-vs-new.log`).
- **considerthese:** one still-unimplemented proposal from the latest file, mined by the scribe into
  the lesson.
- **Assimilation:** none this round; the 155/155 id collision stays on L0. Re-checked and reported.

## Shape

One v1 wave, 12 seats (policy band 8–16): executor 3, scout 1, scribe 1, connector 1, reviewer 3,
critic 1, mutation-tester 1, sentinel 1. Attack share 5/12. Connector seats 1. The L1 holds the
planner seat (the validator rejects `planner`). Godspeed leads every L2 prompt.
