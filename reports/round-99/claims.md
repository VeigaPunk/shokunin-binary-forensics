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

---

## Amendment A — recorded before the v8 freeze and before any landing-tree scoring (2026-11-05)

Appended; no frozen sentence above is replaced. Source: ReviewerClaimsR99 F1–F4
(`.ufo/waves/round-99/w1/ReviewerClaimsR99.md`), received before any v8 bytes were frozen.

**A1 — S505 grounding (F1, blocker).** v7 `c14` (and therefore v8 `c14r99`) checks
`C1_USEDBY_GROUNDED` over S505, S506, S507. S505's `used-by` names
`corpus/knowledge/round-96-native-analysis-sessions.md`, which never cites S505, so C1 was unreachable
through the declared surface. The r98 correction (`mined → queued`, used-by `—`) harms C02 (v7 `c02`
`C1_SOURCES`: `S504:terminal-mined-expected:S505:queued`, r98 lesson). This amendment grounds S505 by
citation instead: its `used-by` cell becomes `corpus/lessons/round-97.md`, the document that
introduced S505 and cites it (`grep -cw S505 corpus/lessons/round-97.md` ≥ 1); status stays `mined`,
so the S504 → S505 chain stays terminal-mined. Landed in this amendment's commit, logged old → new in
the round-99 lesson. Scratch evidence before landing (claims-freeze archive + this one cell): v7
`--profile c02` → `C1_VERDICT=pass`, K 13/15, rc 0 (no harm to C02); v7 `--profile c14` →
`C1_USEDBY_GROUNDED=pass`; `sources-census.sh validate --file` → ok
(`controls/amendA-s505-scratch.log`). The C1 surface therefore also moves this one registry cell. The
entry bytes are untouched, so the vote digest `36cc6ac2…` is unchanged and no re-vote is needed.
**`FREEZE_REV` for `c14r99` becomes this amendment's commit** (README is byte-identical to `7e6edd4`),
and the C1 do-nothing and junk-row controls are built from this amendment's commit.

**A2 — new legs keep r98 controls honest (F2).** v8 legs visible in `c02`/`c14` must key on surfaces
the r98 honest fixture trees carry; round-99-surface checks go in `c14r99`-only legs. A leg that breaks
either r98 control yields `control-BROKEN`, which the C2 kill rule already counts as not met.

**A3 — invocation evidence (F3, tightening).** The recorded C2 run must also print one
`C2_VECTOR <profile>-<id> accepted|refused legs=<…>` line for each of the twelve vectors; fewer than
twelve such lines means C2 is not met.

**A4 — receipts (F4, info).** Under `c14r99`, `RECEIPTS_DIR` stays `reports/round-98/quote-receipts`;
the round-99 S506 re-open receipt is claims-side evidence for the sourced-claim duty only.

## Amendment B — the single candidate amendment (recorded before the v8 freeze and before any landing-tree scoring, 2026-11-05)

This is the one candidate amendment the C1 kill rule allows. After it, any FAIL vote kills C1.

Trigger: VoterGateR99 voted Q16 FAIL on digest `36cc6ac2…` (`reports/round-99/votes/VoterGateR99.json`): the
"scope-check classes" row's recorded output was not the command's stdout. CriticR99 (before casting
any vote) reported the same row, the S507 `teaches` cell's "exit 1" (the doctor record has no exit
line), the "of 8" denominator not printed, the substep status not tied to the operation, member
labels and the root digest not derived, and "because … not on PATH" stated as an observation.

The author's edits, made before any scoring:
- the derivation table is regenerated so that every output cell is the command's stdout verbatim,
  under a cell rule stated in the preamble (one code span per stdout line, joined by ` / `;
  annotation only after an em dash). Padding and prefixes are removed in the commands (`sed`, `cut`),
  not in the cells. Rows were added for the host identity, the ghidra-named scope-check count, the
  ghidra-headless launcher path, the installed skill identity, the absent binwalk/unblob checks,
  members with sizes, the inventory root digest and the truth.json archive digest. The scope-check
  count row is split into two rows;
- the route table's analyzeHeadless clause no longer states a cause;
- §Q-map Q11 and Q16 rows are restated for the new table;
- the S507 registry row's `teaches` cell drops "exit 1" as a record fact: "its exit code 1 was
  observed in the L1 session and is not a line of the record" (logged old → new in the lesson).

A new instrument, `reports/round-99/controls/deriv_check.py`, re-runs every derivation row and
compares stdout with its cell. Shown able to fail: on the claims-freeze entry it reports
`DERIV_MISMATCH=7`, rc 1; on this amendment's entry `DERIV_ROWS=29 DERIV_MISMATCH=0`, rc 0
(`controls/amendB-deriv-check.log`). Lint rc 0, all counts 0. v7 `--profile c14` on a copy of this
tree: `C1_DERIV_TABLE`, `C1_SOURCES`, `C1_QUOTE_BYTES`, `C1_OWNWORK_PATHS`, `C1_LINT` pass. Census
exit 0.

**New vote-binding digest:** `246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da`. It
supersedes `36cc6ac2…`. The votes cast on `36cc6ac2…` are moved to
`.ufo/waves/round-99/w1/superseded-votes-digest-36cc6ac2/` as evidence and no longer count; the three
pinned voters (VoterGateR99, VoterBlindR99, CriticR99) vote on the new digest. `FREEZE_REV` for
`c14r99` stays `61e27feb…` (README unchanged). Predicate, counter, target and kill rule are unchanged.
