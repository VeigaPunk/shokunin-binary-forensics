# CriticR91Claims — round 91, attempt 1 (attack seat)

Scope: falsify both frozen claims (`.ufo`-external base `b13aac7`) against the
four attack criteria in the assignment — control reachability, axis naming,
freeze order, fitting. Read-only over the lane; no mutating git/jj; frozen files
untouched. Full evidence, commands and outputs:
`receipts/findings.md` (15 findings), with every control script and log beside
it in `receipts/`.

No local document carries a numbered "§9" (`templates/round-prompt.md` has
sections 1–5; `MISSION.md` 7 sections; `AXES.md` and the role cards are
unnumbered), so the four named criteria were attacked directly. That is a
provenance gap in the assignment, not a lane defect.

## Verdict

Both claims fail as written, on different grounds:

- **C1** — the counter passes the real v3
  (`SM6_MISCLASS=0/22`, `MUTANTS_KILLED=11/11`, `REAL_SELF_MISMATCH=0`,
  `C1_VERDICT=pass`, `receipts/c1-v3-recheck.log`) but **also passes a 21-entry
  lookup table that never reads the stated cell** (`receipts/c1-fit-hardcoded.log`,
  same four lines). The battery admits fitting; the round does not disclose it.
  The claim's own rule — "a control that meets the target means the battery or
  target is wrong; then no data is collected" — is triggered.
- **C2** — the probe prints `CAP_MESSAGE_TREE=pass` (landed instrument,
  `receipts/probe-landed.log`) but the frozen extraction rule ("every
  **backticked** repo-relative path and every `.log` filename") cannot reach the
  probe's own floor: implemented literally it yields `cited=8 < 20` and fails
  (`receipts/probe-spec-conformant.log`). The pass comes from an extraction
  rule (prose paths) that was chosen after the freeze and is not in the claim.
  Worse, controls with **no commit-tree check** and **no filesystem check**
  also pass (`receipts/probe-stubD.log`, `receipts/probe-stubE.log`).

## Findings

17 total. Blocking as written: **6**. While this seat ran, the landing seats
drafted an uncommitted `SCORECARD.md` round-91 section and the `claims.md`
erratum; they disclose C1-3 (README index), C1-10 (SCORECARD rewording), C2-1
(backticked rule, via the erratum), C2-5 (8 ambiguous + 1 genuine miss) and the
mutant-survival limits. They do **not** disclose C1-1 (fitted table), C1-9
(editing the frozen claims file), C1-4, C1-5, or the C2-2/C2-3/C2-4 probe holes.

| id | claim | finding | status |
|---|---|---|---|
| C1-1 | C1 | fitted 21-entry table passes the counter | **blocking** |
| C1-3 | C1 | real leg is whole-tree: v3 itself trips SM2 until `corpus/README.md` indexes it; that edit is undeclared in the claim | **blocking → disclosed** in the SCORECARD row (uncommitted at review) |
| C1-9 | C1 | the frozen `claims.md` was edited after data (appended `## Erratum`), against its own "nothing changes after the freeze" invariant | **blocking for the freeze invariant** |
| C2-1 | C2 | frozen backticked-only extraction cannot reach `cited≥20`; the passing instrument uses an unfrozen rule | **blocking** (disclosed only by the post-freeze erratum) |
| C2-2 | C2 | stub with no tree/filesystem check passes: planted path is self-identifying (`missing/`), leg 4 ignores exit code and K | **blocking** |
| C2-3 | C2 | worktree-existence control passes with `misses=1` vs the instrument's `misses=9` | **blocking** |
| C2-4 | C2 | leg 4 passes while the instrument reports `misses=9 exit=1`; the lane's history is non-conformant under the round's own instrument | **blocking** (predicate as written) |
| C1-2 | C1 | hard-coded `8/15` is killed (6/22) — battery discriminates there | non-blocking |
| C1-4 | C1 | real leg unpinned; v2's frozen `REAL=0` became 1 then 0 with tree state; archive run gives 34 | material |
| C1-5 | C1 | battery docstring claims R01/R02 are "verbatim" SCORECARD lines; both differ (R02 truncates the stated cell) | non-blocking |
| C1-6 | C1 | axis label calibration is contested (gate fidelity vs self-assessment); disclosed, and the r90 counterexample is a mutated row, not a committed one | disclosed |
| C1-7 | C1 | counter docstring says `0/21`, behaviour is `0/22` | minor |
| C1-8 | C1 | frozen bytes unchanged since `b13aac7`; labels precede the impl (19:36 < 19:42) | pass |
| C1-10 | C1 | real-tree SM6=0 obtained by rewording the SCORECARD prose that named `K_HELD_BACKED`; gate blind spot routed to r92 | material, disclosed in the erratum |
| C2-5 | C2 | 8 of 9 misses are ambiguity false positives (`claims.md`×30, `truth.json`×53, …); multi-match→miss was chosen post-freeze | material, disclosed in the SCORECARD row |
| C2-6 | C2 | grounding "seven of nine rounds r80–r88" reproduces as 6/9 (and 14/19 of those misses are ambiguity) | material |
| C2-7 | C2 | operability is a real `AXES.md` axis but not a scoring axis in this lane's SCORECARD; capability row only | non-blocking |

## Two strongest

1. **C1-1** — `receipts/impl_fit_hardcoded.py` (21 tuples of
   `(map rows, held, raw K line text) → label`, fake self-test, unconditional
   `SELF_MISMATCH=0`) scores `C1_VERDICT=pass` on the frozen counter. The
   mutant leg never touches `--impl`, so only the 21 fixed cases constrain it,
   and they are enumerable. The target is reachable by the cheapest possible
   skip: a lookup table.
2. **C2-2** — `receipts/stubD.py` performs no tree lookup and no filesystem
   lookup: it flags only cited names containing the literal `missing` (the
   probe's own spelling, also used by the instrument's selftest at
   `message_tree_check.py:231,248`) and reports the real range as
   `misses=99 exit=1`. Observed: `CAP_PLANTED_MISS=pass`, `CAP_REAL=pass`,
   `CAP_MESSAGE_TREE=pass`, exit 0. The probe certifies neither tree
   membership nor real-range conformance.

## Impacted axes

- **calibration (C1):** the counter measures conformance to a fixed case table,
  not that the gate reads the stated cell; the real leg also measures SM1–SM5
  (a README-index edit decides the verdict) and is not pinned to a tree.
- **operability (C2):** the predicate's extraction rule was superseded after the
  freeze; the real leg cannot distinguish tree-scoped from worktree-scoped
  checking and ignores its own instrument's failure signal. The capability
  ("measurable") is supported by the run, but the conformance number K=9 is
  89 % ambiguity false positives and the lane's history is reported
  non-conformant (1 true miss: `ufo-wave-policy.json`, a fleet-root path).

## Smallest safe corrections

- **C1:** generate one battery case at counter-run time (seeded random
  rows/held + random true/false statement) or score `--impl` against
  `mutants.reference` on randomized inputs; declare the `corpus/README.md`
  index line as part of the landing; pin `--real` to `git archive <landing>`.
  If the frozen files cannot change, report C1 as "conforms to a battery that
  admits fitting", not as the rule verified.
- **C1 provenance:** label R01/R02 "truncated" or quote byte-exactly; state that
  the committed K row is read correctly by v2 and the red rests on authored
  variants.
- **C2:** restate the extraction rule to what the instrument implements and
  record that the frozen backticked-only rule scores `cited=8`; plant an
  ordinary-looking absent path; make the planted fixture include a commit whose
  cited path exists in the worktree but not in that commit; require leg 4's
  exit code to match K and cross-check `commits` against `rev-list --count`.
- **Freeze invariant (C1-9):** move the `## Erratum` out of
  `reports/round-91/claims.md` into `SCORECARD.md`/`LOG.md` (r89 precedent) and
  keep the frozen file byte-identical to `b13aac7`; the erratum's C2 re-reading
  is a post-data reinterpretation of the claim it claims not to change.
- **C2 disclosure:** report K=9 with the ambiguity classification (8 ambiguous,
  1 true miss) and the reproduced r80–r88 figure (6/9 rounds), or drop the
  number.

## Reproducibility

Every finding above was reproduced in this seat. The two claims that did not
reproduce are C2-6's "seven of nine rounds" (observed 6/9) and C1-5's "verbatim"
battery rows (both differ). Controls and logs:
`receipts/spec_extract.py`, `spec-extract-real.log`, `probe-spec-conformant.log`,
`impl_fit_hardcoded.py`, `c1-fit-hardcoded.log`, `impl_hard815.py`,
`c1-hard815.log`, `stubA.py`, `stubD.py`, `stubE.py`,
`probe-stub{A,D,E}.log`, `probe-landed.log`, `msg-tree-real.log`,
`msg-tree-r80-88.log`, `classify_misses.py`,
`miss-classification-{real,r80-88}.log`, `c1-v{2,3}-{now,recheck}.log`,
`c1-real-leg-tree-dependence.log`, `c1-red-on-archive.log`,
`battery-r01-r02-provenance.log`.

Tooling: none installed or upgraded this seat (no `pacman`, no `uv tool`).
Scratch `$HYAKU_SCRATCH/revenger-r91/CriticR91Claims` removed before yield;
fixture repos were `git clone`/`git init` under that scratch with `-C` on every
call and toplevel asserted.
