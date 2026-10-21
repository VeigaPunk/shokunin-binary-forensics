RESULT: COMPLETE

# R62ConnectLearning — cross-axis check of round-61 closure; final-report wording constraints

Seat `RevengerR61-2.R62ConnectLearning` (leaf; no dispatch). Frozen base
`a3498e25ad87bf756288812d0ea7c474b09433c7` (claim base `5bd4a90…`). Ground: `reports/round-62/claims.md`,
`corpus/QUALITY.md`, `corpus/lessons/round-61.md`, `corpus/lessons/round-61-verifier-spotcheck.md`,
`SCORECARD.md`, `LOG.md`, `reports/round-61/claims.md`, `.ufo/waves/round-61/falsify-w3/`. All execution on
extracted copies, cwd=`/`. **No corpus byte, README cell, SOURCES row, lesson or production file was
written.** No producer, fixture JS, EVM bytecode or live target ran.

## 1 Cross-axis check — three claims, each independently re-derived

- **coverage K is the lowest non-retired scored criterion — holds.** Base: K 2.9, F 5.0,
  calibration-C 10.0, freshness 10.0, receipt-kill 10.0 (`SCORECARD.md:199-203`, `:247-248`; depth
  retired `:135`). Probe on the frozen extract: `K_HELD=4/14 score=2.9`, `K_HELD_BACKED=4/14`,
  `K_ROW C04/C09 status=uncovered`, exit 0.
- **the prior C2 gain does not rescue C1 — holds.** `corpus/lessons/round-61.md:111-113`
  ("C2's receipt-command kill stays 2/2; it does not rescue"); `round-61-verifier-spotcheck.md:10`,
  `:204` ("No axis gain compensates for C1's failed target: the whole round is rejected"). The probe
  shows C2 `2/2` and K `4/14` **in the same run** — separable, not additive.
- **expansion unchanged / quality improved / discernment improved narrowly — holds, and is narrow.**
  `round-61-verifier-spotcheck.md:200-203`; its non-author table `:142-146` (C04 disagree-with-initial-
  admit / agree-with-final-reject; C09 agree; S024 agree) — **3 items sampled**, so "narrowly" is
  accurate. No contradiction among the three; the one live contradiction is inside `SCORECARD.md`
  (W8), a stale provisional row, not a claim conflict.

## 2 New bounded evidence: the K probe cannot carry an admission

`reports/round-61/measure.py` is unchanged. `K_HELD_BACKED` counts **file existence**
(`measure.py:32-34`); `score=` is computed from `K_HELD`, not `K_HELD_BACKED` (`measure.py:26`).
Four counterexamples on scratch copies of the frozen tree, reproduced end-to-end by
`reproduce_k_probe_counterexamples.py` (`evidence/reproduce-script.out`), each probe exit 0:

| # | mutation (scratch only) | probe output |
|---|---|---|
| M1 | C04+C09 → `held`, cells name **only the two round-61 `admission-status: rejected` files** | `K_HELD=6/14 score=4.3`, `K_HELD_BACKED=6/14` |
| M2 | C04+C09 → `held` + **4-line stub** knowledge files (`admission-status: none`) | `K_HELD=6/14 score=4.3`, `K_HELD_BACKED=6/14` |
| M3 | **only non-target** C07 `frontier→held` | `K_HELD=5/14 score=3.6`, `K_HELD_BACKED=4/14` |
| M4 | **only** non-target C02 `partial→frontier` | stdout **byte-identical** to baseline |

M1/M2: the probe credits **rejected** and **stub** entries — it would report round-62's 6/14 target
with no admissible knowledge. M3: the `score=` line reaches round-62's own 5/14 / 3.6 target from a
non-target row flip, `K_HELD_BACKED` unmoved. M4: non-target status drift is invisible — confirming the
routed defect (`round-61-verifier-spotcheck.md:215-216`, `claims.md:41-43`) by fresh measurement.

## 3 Proposed artifact — final-report wording constraints

Full artifact (scratch, for L1): `/fast/scratch/hyaku/revenger-r62/R62ConnectLearning/
proposed-wording-constraints.md` — all 11 constraints in a table with the measurement forcing each, the
grade/scalar arithmetic and six drop-in report sentences. The five deciding the verdict:

| id | constraint | forced by |
|---|---|---|
| W1 | a count never stands for an admission — name the admitted path, its `admission-status` and the Q01–Q13 decision | M1, M2 |
| W2 | report `K_HELD_BACKED`, denominator 14 — not `K_HELD` | `measure.py:32-34` |
| W3 | never report `score=` alone — print it beside `K_HELD` and `K_HELD_BACKED` on one line | M3 |
| W4 | no mean/total/"N of M"/round score — the unweighted mean of the five base criteria is 7.58 ≥ the 7.0 saturation line (`SCORECARD.md:173`) while the only criterion round 62 works (K, 2.9) is below it | arithmetic |
| W5 | no wave-grade tally, percentage or pass rate (HOLDS 30 / PARTIAL 31 / BROKEN 5 of 66, threshold 34, no majority; a "non-BROKEN" 92.4 % reading would clear a rejected candidate) — adjudicate each finding by name | `adjudication.json` |
W6–W11 (one claim per axis, C2 not netted, no inherited provisional wording, expansion unchanged until
admission, preservation digests, README stays uncovered) are tabulated in the scratch artifact.

## 4 Limits, unknowns, handoff

- The mutations are probe behaviour on scratch copies: not admissions, not corpus defects.
  `git status --porcelain` in the live repo prints only `?? .ufo/waves/round-62/` (the wave's own
  untracked reports); `git diff --stat HEAD -- corpus/ reports/ SCORECARD.md LOG.md` is empty.
- I do not decide admission, README cell text, per-candidate Q tables, S028–S031, or the lesson body —
  those belong to L1 and the sibling seats. Round-61's closure *report file* is absent from this
  repository (`git show 6e60ffb4…` → `bad object`); the committed lesson
  `corpus/lessons/round-61-verifier-spotcheck.md` is the artifact I relied on. Round-61's grades are
  advisory by the lane's own ruling (`:182`); my counts are a recount, not a vote.
- L1 handoff: apply W1–W11 to the round-62 final report; drop-in sentences are in
  `proposed-wording-constraints.md` §2. Conclusion to carry: **K is lowest, C2's retained 2/2 does not
  rescue C1, round-61's discernment gain was narrow (3 sampled items), and round-62 expansion must be
  stated as a function of new admissions only.** README C04/C09 remain `uncovered`; nothing here admits
  any row. Scratch (lane-owned): `proposed-wording-constraints.md`, `reproduce_k_probe_counterexamples.py`,
  `evidence/`, `mutants/`.

Installs: none (Python 3 stdlib + coreutils + `git archive`); no pacman/uv/npm/cargo transaction.
