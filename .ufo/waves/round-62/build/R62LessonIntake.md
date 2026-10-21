RESULT: COMPLETE

# R62LessonIntake — round-62 routed-defect intake table (leaf, no subagents)

Seat `RevengerR61-2.R62LessonIntake` · 2026-10-21 · read-only against frozen
`a3498e25ad87bf756288812d0ea7c474b09433c7` (HEAD of `…/revenger-shokunin`).
Scope: the round-62 lesson intake table for **every** routed item at
`corpus/lessons/round-61-verifier-spotcheck.md:206-218`, each classified as
required correction in NEW candidate scope / avoided by narrow scope / explicit
unresolved debt, preserving old mistakes and lessons.
**No admission claimed. No README row touched (C04/C09 stay `uncovered`).** No
`corpus/` byte, source row, lesson file or git/jj state written by this seat.
Full draft with per-row citations, mined M27 row and preservation check:
`/fast/scratch/hyaku/revenger-r62/R62LessonIntake/R62-lesson-intake-table.md`.

## 1. Frozen evidence base (own commands, scratch copies only)

```
$ git -C …/revenger-shokunin archive a3498e2 | tar -x -C …/R62LessonIntake/tree
$ cd / && TMPDIR=$D python3 -B $D/reports/round-61/measure.py $D
K_HELD=4/14 score=2.9 ; K_ROW C04 status=uncovered ; K_ROW C09 status=uncovered ; K_HELD_BACKED=4/14
C2_CONTROLS_PASS=2/2 ; C2_RECEIPT_B_KILLED=2/2 ; C2_D2_KILLED=2/2 ; C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4 ; HOLD_REPLAY=10/10 ; HOLDS_OK=yes
```

Frozen C1 baseline **K 4/14 (2.9)**; probe is the unchanged one `claims.md:35-38` names.
`git diff --stat 5bd4a90 a3498e2 -- corpus/lessons/round-61.md corpus/lessons/round-61-verifier-spotcheck.md corpus/knowledge/evm-saved-interface-candidates.md corpus/knowledge/commonjs-destructured-require-edges.md` → **empty** (prior lessons, counterexamples, rejected entries byte-preserved). Own byte re-derivation on the frozen fixture (35 B, sha256 `b69834e0…5d93`): pattern `63deadbeef14601057` occurs once at 1 (inclusive span 1–9), raw `0x63` `[1]`, raw `0x5B` `[]`. `corpus/knowledge/round-62-*.md` and `corpus/lessons/round-62.md` **do not exist** at the frozen revision → every "required correction" row is OPEN by observation, not assumption.

## 2. Routed-item coverage map (206-218 → all 18 clauses)

| routed clause (line) | disposition | status |
|---|---|---|
| 1a C04/C09 stay uncovered until a candidate meets unchanged Q11 (208-209) | required correction in NEW candidate scope | OPEN |
| 1b derive or accurately label missing spans/counts/targets (209) | required correction in NEW candidate scope | OPEN |
| 1c closure byte checks ≠ in-entry derivations (210) | required correction in NEW candidate scope | OPEN (constraint) |
| 2a false kasegi citation (211-212) | avoided by narrow scope (new C09) + unresolved debt (retained file `:104-105`, Q10 row `:192`) | avoided/debt |
| 2b Electron-role semantics (211-212) | avoided by narrow scope (new C04) + unresolved debt (retained file `:56-57`) | avoided/debt |
| 2c Q13 overcredit (211-212) | required correction in NEW candidate scope + unresolved debt (retained Q13 row `:208`) | OPEN |
| 2d source search-log counts/dispositions (212) | required correction (round-62 log line) + unresolved debt (round-61 `SOURCES.md:57-59`) | OPEN |
| 2e S019 anchor (212-213) | avoided by narrow scope (new entries) + unresolved debt (`SOURCES.md:33`) | avoided/debt |
| 2f Q12 successor-flip weakness (213) | explicit unresolved debt (criterion text frozen) | carried |
| 2g M25 attribution/capture defects (213) | required correction in NEW candidate scope (new lesson row; `round-61.md` untouched) | OPEN |
| 2h retained rejection warnings block current admission, not future reuse (213-214) | avoided by narrow scope | satisfied by construction |
| 3a K probe existence-only blind spot (215-216) | avoided by narrow scope (`claims.md:41-44`) | already separated |
| 3b K probe non-target-status blind spot (215-216) | explicit unresolved debt (instrument frozen) + required out-of-probe check | carried / check run |
| 3c two-script C2 guard separate from other clauses (216) | avoided by narrow scope | satisfied (2/2,2/2,2/2) |
| 4a SKILL/registry absence (217-218) | explicit unresolved debt | carried |
| 4b prior F03 verdict-vs-STALE discrepancy (217-218) | explicit unresolved debt | carried |
| 4c operator-owned ADJ-06 arbitration (218) | explicit unresolved debt | carried |
| 4d no promotion implied (218) | avoided by narrow scope | satisfied |

## 3. Counterexamples cited (original wave, unmodified)

1b/1c `W3EvmR24Immediate.md:17-20,33`; `W3EvmR24SpanFix.md:10-13`; `W3JsOverclaimCritic.md:6,42`. 2a `W3ProvinceBounds.md:11-16` (kasegi line is the "Refuses" line; `grep -c deployed kasegi-shokunin/PROVINCE.md` → 0), `W3EvmCrossLaneCites.md:10,18`. 2b `W3JsElectronMainLabel.md:18-26,28-36`, `W3JsOverclaimCritic.md:10`. 2c `W3QualityQ13Apply.md:7-22,23-36,37-48,49` (F5 = C09 withheld verifier credit — precedent). 2d `W3SrcSearchLog.md:4,5-8,9,16`. 2e `W3SrcContractCells.md:8` + independent re-open: page 38 117 B, sha256 `3407a364…a64`, "runtime" once, in the §Contract Metadata intro, never in the anchored section. 2f `W3QualityQ12Fail.md:21,24,34`. 2g `W3LessonMistakes.md:21,25`, `W3EvmR24SpanFix.md:15`; own check `git show 0b6ddf0:…evm-saved-interface-candidates.md`: "inconsistent"/"two occurrences"/"defect"/"inclusive" each **0** occurrences — the file says only "lists embedded-pattern offsets `[1, 9]`; the bytes contain the pattern only at 1". 3a/3b `W3HoldProbeRerun.md:36-45`, `W3KProbeMutant.md:20,22` (mutant d `C02 partial→frontier` SURVIVED, stdout+exit identical to pristine).

## 4. Compensation for 3b (the check the probe cannot do)

Base `5bd4a90` vs frozen `a3498e2` README statuses compared row by row — identical for all 14 rows (C04 and C09 `uncovered`, denominator 14). Probe left untouched.

## 5. Proposed change (scratch only — L1 owns the corpus)

`…/R62LessonIntake/R62-lesson-intake-table.md`: 18-row intake table with dispositions/statuses/citations; mined mistake row **M27** ("correct-value-without-in-entry-derivation", captured by existing Q11) with a red-before exemplar, mapping onto existing M26 (`round-61.md:128`); preservation and non-claims sections. Nothing applied; `git status --porcelain corpus reports` → empty.

## 6. Unknowns (honest)

Candidate files and the round-62 lesson do not exist yet, so "avoided by narrow scope" rows rest on frozen `claims.md:16-28` scope text, not landed bytes, and must be re-checked against the landed entries. Whether L1 amends round-61 `SOURCES.md:57-59` or only appends a round-62 line is an integration decision; both options are recorded, nothing edited. Frozen census: 27 rows (mined 22 / queued 1 / rejected 4); S028–S031 reserved, not rows.

Installs: none. Tools: git (read-only), python3 stdlib, curl (one public spec page only).
