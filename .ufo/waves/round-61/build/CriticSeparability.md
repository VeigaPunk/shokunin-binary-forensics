# CriticSeparability — round 61 claims attack (read-only)

Seat `CloseChousa26.CriticSeparability-10`; nothing run, nothing written except this file. Axes judged: coverage, calibration.
Subject `reports/round-61/claims.md` (pre-registration commit e0a4b0c; claim base cf02419). Read: RULES.md, AXES.md, measure.py, measure-before.log, SCORECARD.md, corpus/README.md, QUALITY.md, mutation-post.md, connector.md, three verifiers.

## 1. Separability and distinct axes — HOLDS, with two couplings
- OBS: The write sets don't overlap. C1 touches knowledge/README/SOURCES/lesson; C2 touches the two scripts only (claims.md:66-67). The probe measures K from README text alone (measure.py:23-29) and C2 from the scripts alone (:33-86), so each claim can be measured without the other.
- OBS: The axes are distinct: coverage versus calibration (claims.md:19,42).
- COUPLING A: HOLD_REPLAY counts every `corpus/verify_*.py` (measure.py:89,99). If C1 adds any verifier (for example a Q11 derivation script), the denominator becomes 11 and the C2 hold of 10/10 (claims.md:61) fails because of C1. Fix: C1 adds no `corpus/verify_*.py`.
- TRADEOFF for the judge: C2 is a mutation kill on a test oracle. Under AXES.md:13-15 that reads as operability ("scripts that run produce the stated outcome"), and SCORECARD.md:84 says operability is not a scoring axis here. A calibration reading ("overreach caught", AXES.md:14) is defensible, but the canonical judge has to rule on which axis C2 lands on.

## 2. Is C1 on the lowest non-retired criterion — YES, but the wording drifts
- OBS: AXES.md:33-34 requires the lowest-scoring non-retired *axis*; claims.md:15-17 says *criterion*. Coverage is lowest under any aggregation: F 5.0 and K 2.9, against calibration 10.0 and freshness 10.0 (SCORECARD.md:131-134). Depth is retired (:135). C1 complies.
- COUNTEREXAMPLE: C2 adopts a new calibration criterion with a before score of 0.0 (claims.md:57-59). Once adopted, the lowest criterion at the base is that new one (0.0 < 2.9), so the sentence at claims.md:16-17 is only true before adoption. The rule is still satisfied, because some claim works the lowest either way. The text should say "lowest axis: coverage (min 2.9); C2's new criterion is adopted at a measured 0.0".

## 3. Score-shopping risk of the new calibration criterion — REAL
- OBS: The existing calibration criterion already sits at 10.0, above the saturation line of 7.0 (SCORECARD.md:131,173). AXES.md:36-38 allows a split only when it is "recorded in SCORECARD.md with reason". claims.md doesn't declare a split, give a reason, or say how the axis score aggregates when one criterion is at 10.0 and the other at 0.0.
- STRONGEST COUNTEREXAMPLE: the denominator of 2 is exactly the two known survivors from kaika (mutation-post.md:15,21). The gain is 0 to 10 by construction.
- `verify_named_multi_icon_states.py:72` carries the same `receipt['command']==command` conjunct, and the probe's regex matches it (measure.py:33). Its in-script forgeries cover `normalized_result` only (:89-97). Its receipt control lives in an external battery (mutation-post.md:34-35).
  - [INFERENCE, not run] Mutant b on that file therefore also survives its own `--self-test`.
- Honest scope: every `verify_*.py` with a receipt-command conjunct, which is 3 files. That gives a prediction of 0/3 → 2/3 (6.7), unless the named verifier is also in scope (→ 3/3).
- Precedent: freshness was adopted at a measured base of 4.4 (SCORECARD.md:134). A measured base is acceptable; a scope chosen from the failures is not.

## 4. Falsifiability
- C1: falsifiable, since 4/14 falsifies it (claims.md:38-39). But K is a README string the author writes; the real falsifier is the Q01–Q11 gate.
  - GAP: there is no per-row condition. The prediction is stated on the total, so a swap (C04 becomes held while another row is lost) reads as "one admit". Require C04 and C09 to be `held` (measure.py:27-29 already prints them) and the other 12 rows to be byte-identical.
  - The admission gate should be recorded by a non-author, not by "survives wave-2 attacks" alone (claims.md:33).
- C2, kill classification: falsifiable, with a measured 0/2 (measure-before.log:8,10,12). But "killed" means `rc != 0` (measure.py:77,81), so a SyntaxError, NameError or ImportError after the mutation also counts as a kill.
  - Fix: a kill counts only if the last line is the control's named rejection (for example `forged receipt command accepted`). The probe already prints the tail (:78).
- C2, regex versus claim wording: claims.md:53-54 allows `receipt['command']==<expr>`, but CLAUSE accepts only `command` or an f-string (measure.py:33). A legitimate `==expected_cmd` gives exit 2.
  - claims.md:54 should say that exit 2 means C2 is *unverified/not admitted*, not falsified, and that the right-hand side must be `command` or `f'...'`.
- C2, source self-inspection: a control that asserts the clause text is present in `__file__` would kill b with no behavioral test. Require the forged receipt to differ from the real one only in `command`, and to pass through the same `check` predicate.

## 5. Missing harm conditions (claims.md:68-70 lists four)
1. Other README rows: the 12 rows other than C04/C09 must stay byte-identical, and the count must stay at 14 (README.md:42).
2. README index drift that already exists at the base:
   - README.md:9 says "Q01–Q10", but Q11 exists (QUALITY.md:23).
   - README.md:12 doesn't list `lessons/round-1-verifier-spotcheck.md`.
   - Round 61 adds new knowledge files and `lessons/round-61.md` that have to be indexed.
   - README.md:42-43 names the freeze commit as `a7acc20`; it goes stale once round 61 flips rows and should be re-anchored to cf02419.
3. SOURCES:
   - Append-only: existing rows must stay byte-identical.
   - The census (`revenger ok`, exit 0; measure-before.log:28-30) appears only as a frontier step (claims.md:72-76), not as a condition that voids admission.
4. Freshness hold: the freshness grep (SCORECARD.md:134) must stay at 18/18. Existing knowledge files (`seed.md`, the readiness checklist, the four admitted entries) must stay byte-identical. claims.md:66 allows any write under `corpus/knowledge/`.
5. Other kaika mutants: a, c, d1 and d3 must stay killed after the C2 refactor (mutation-post.md:13-24 shows 10/12 killed). The holds at claims.md:60-62 keep only d2 and the controls.
6. Adjacency:
   - Kaidoku's ground includes "EVM/ASAR tool paging" (connector.md:78), and ADJ-06 is still unresolved (connector.md:18,131).
   - C04/C09 entries risk absorbing that ground, and claims.md has no adjacency harm condition. Adjacency is "unchanged" in SCORECARD.md:136.
   - Fix: each entry names the contested scope and reports it rather than absorbing it.
7. Over-broad `held` (Q10):
   - `held` means an entry "covers the ground" (README.md:19).
   - The C04 surface is "JavaScript/Electron packages" (README.md:30), but the entry covers CommonJS destructured require plus package `main` only. ESM, ASAR and Electron are not covered.
   - Fix: annotate the scope in the row's knowledge cell, following the C06 precedent "(archive-tool row only)" at README.md:32. This is a tradeoff for the judge.

## Smallest safe correction (amend before implementation, as dated errata)
- C2: declare it as a sub-criterion split under saturation, with a reason and an aggregation rule. Either widen the scope to 3 files or justify excluding the named verifier. Count a kill only when the last line matches the control's message. Treat exit 2 as unverified.
- C1: require per-row flips with the other 12 rows unchanged, a non-author record of the Q gate, a scope note in the README cell, no new `verify_*.py`, and an adjacency statement.
- Holds: add README index sync and freeze re-anchor, SOURCES append-only plus census exit 0, freshness 18/18, and mutants a/c/d1/d3 still killed.

Installs: none.
VERDICT: The claims are separable and on distinct axes, and C1 does work the lowest axis. Both predictions are falsifiable but loosely: a crash counts as a kill, and K is a self-written README string. C2's new criterion is score-shopped by its denominator (2/2 equals the known survivors, and the third receipt verifier is excluded). Seven harm holds are missing.
