GRADE: PARTIAL — SCORECARD.md round-61 section (K row :199, replacement-L1 note :217-223)
Target `SCORECARD.md:186-235` at landed ab58069. Archives only: `git archive --format=tar cf02419
corpus` → /tmp/revenger-r61w3-W3ScorecardRow/b ; `ab58069 corpus` → …/a (corpus tree 998437d =
0597e53's, identical).
## HOLDS (measured)
1. K row before→after (:199) reproduced end-to-end.
   - base cf02419: `python3 -B reports/round-61/measure.py …/b` → `K_HELD=4/14 score=2.9`,
     `K_ROW C04 status=uncovered`, `K_ROW C09 status=uncovered`, `K_HELD_BACKED=4/14`, exit 0.
   - landed ab58069: same probe → `K_HELD=6/14 score=4.3`, `K_ROW C04 status=held`,
     `K_ROW C09 status=held`, `K_HELD_BACKED=6/14`, exit 0. 10·4/14=2.857→2.9, 10·6/14=4.286→4.3;
     matches claims.md:38 predictions.
2. Counting cell (:199) "regex as `:133`": SCORECARD.md:133 does hold
   `grep -cE '^\| C[0-9]+ .*\| held \|$' corpus/README.md` — the regex claims.md:36-37 names and the
   probe implements (measure.py:24-25). ✓
3. Measured-commit cell (:199) `cf02419` → `0b6ddf0` matches measure-after.log's archive command. ✓
4. All seven knowledge files named by held rows C01/C04/C09/C11/C12/C13 exist; README row count 14.
5. Note (:217-223): `git show 0597e53` changes exactly the C09 entry + lesson M25 ✓; the two probe
   blocks in measure-after.log are line-for-line identical (27 lines each, identical=True) ✓;
   dead-seats.json: seats=65, dead=65, reports_landed=0, host_end SIGHUP 13:10:51, no report .md ✓;
   corpus byte-identical 0597e53↔ab58069 so the re-measure carries — my probe on …/a gives
   K_HELD_BACKED=6/14, C2 attributed 2/2, HOLDS_OK=yes.
## Mismatches (severity ordered)
A. BROKEN-by-overstatement, :199 "each backed by an **admitted** entry" — contradicted 21 lines
   later by this same section (:220-223: the pre-registered "survives the wave-2 attacks" conjunct
   is unmet, 0 attack results) and by claims.md:30-34, where admission = Q01-Q11 + tier-A source +
   Q11 derivations + surviving the wave-2 attacks. The probe's K_HELD_BACKED (measure.py:32-33)
   checks only that a named `knowledge/<slug>.md` exists — existence, not admission. Should read
   "backed by an existing entry file (admission pending)".
B. Counting attribution, :199 — score 4.3 is NOT from K_HELD_BACKED. The probe prints `score=`
   from `len(held)` (measure.py:26) and K_HELD_BACKED separately (measure.py:34). Mutant (README
   untouched, C09 entry file deleted from the landed tree): `K_HELD=6/14 score=4.3` but
   `K_HELD_BACKED=5/14` — score unmoved, admission metric moved. No number is wrong at this
   landing (both 6/14), but a README flip without a backing file still moves the SCORECARD score
   that A1 was written to exclude. The cell must name K_HELD (score) and K_HELD_BACKED separately.
C. Note :220-223 — "the K row's verdict rests on the non-author closure" names a closure that did
   not exist at ab58069: wave 2 gave 0 reports (dead-seats.json) and wave 3 was dispatched later
   (falsify-w3-dispatch-attempts.json 13:41:59 vs commit 13:32:21) — a forward dependency stated as
   a resting ground, and now stale the other way: 43 wave-3 reports already sit in
   .ufo/waves/round-61/falsify-w3/ and the K row has not been re-adjudicated against them.
D. Evidence placement, :201-203 — F and freshness cite "measured commits: same", but
   measure-before.log has NO `COVERAGE` and NO freshness lines; only the after side was measured
   this round (measure-after.log:40-42). The before values are real (re-ran both commands on the
   cf02419 archive: `COVERAGE 4 / 8 score= 5.0 families= ['native-static','javascript','archives',
   'evm']`; freshness 12+6=18) and corpus/live is byte-identical 35b2e8b↔cf02419, so no number is
   wrong — but "before → after" for those rows is under-evidenced in this round's logs, and the
   0597e53 appended section re-ran neither F nor freshness.
## Residual risk / gaps
- The appended 0597e53 section re-ran the probe, fixture diff, both Reproduce blocks, R24_SPAN and
  the census only. C09/lesson edits touch neither corpus/live nor knowledge/seed.md
  (`git diff 0b6ddf0..0597e53 -- corpus/` = SOURCES.md + C09 entry + lessons/round-61.md), so F and
  freshness carry by inference, not by measurement.
- I verified the K metric only; whether C04/C09 pass Q01-Q11, Q11 derivations and tier-A SOURCES
  scope is other seats' scope (W3KEligibility, W3SrcContractCells) — not adjudicated here. :203's
  "18/18 rows still present" counts `| (holds|STALE)` cells (seed.md 12 + checklist 6); the stronger
  kaika wording at :134 ("hold or flagged with current value") was not re-run this round.
VERDICT: The K row's numbers, counting regex and measured commits are exactly reproducible
(2.9→4.3, K_HELD_BACKED 4/14→6/14, cf02419→0b6ddf0, identical at the landed tree) and the
replacement-L1 note is factually accurate on the commit, the identical re-measure and the 65 dead
seats — but :199's "admitted entry" contradicts :220-223 in the same section, its score is the
K_HELD score rather than the K_HELD_BACKED it names (mutant: score 4.3 with backed 5/14), and the
note's "rests on the non-author closure" names a closure that did not exist when the row landed.
Installs: none (git archive + python3 -B only).
