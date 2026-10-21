GRADE: HOLDS — admission order / no pre-credit on frozen d97761952be256d145d298022de03091de91d358 (C04/C09 uncovered; candidates pending; rejected warnings preserved; K target unchanged)

Seat `RevengerR61-2.R62FAdmissionOrder` (critic). Frozen `d97761952be256d145d298022de03091de91d358`; claimbase `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Archive: `git -C …/revenger-shokunin archive d977619… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62FAdmissionOrder/tree` (cwd=/).
Target hashes (sha256, frozen tree): claims.md `41cc8b73…6c571c02`; lessons/round-62.md `cf0339eb…0449d6ae`; corpus/README.md `2c8606d3…96e8e23f`; README.md `c2938d89…b499fffd3`; C04 candidate `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`; C09 candidate `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`.

## Observations (primary)
1. Map rows. `corpus/README.md:33` C04 and `:38` C09 read `— (round-61 candidate rejected; see lessons/round-61.md) | … | uncovered`. Root `README.md` has no coverage rows; the map is `corpus/README.md`. `rg -c '^\| C[0-9]+ '` → `14`; status tally: held 4, partial 4, frontier 4, uncovered 2. `corpus/README.md` sha256 at 5bd4a90 = frozen = `2c8606d3de51014c83f5be1e2b1309a8f42c343a5c2b006cc73ed0ee96e8e23f`.
2. Unchanged probe on the frozen archive. `TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FAdmissionOrder/tmp python3 -B <tree>/reports/round-61/measure.py <tree>` (cwd=/, Python 3.14.8). Output:
   `K_HELD=4/14 score=2.9` / `K_ROW C04 status=uncovered` / `K_ROW C09 status=uncovered` / `K_HELD_BACKED=4/14` / `C2_CONTROLS_PASS=2/2` / `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` / `C2_D2_KILLED=2/2` / `HOLD_CALIBRATION=4/4` / `HOLD_REPLAY=10/10` / `HOLDS_OK=yes` / `probe_exit=0`. These lines are identical to `reports/round-62/measure-before.log`. Log `measure-frozen.log` sha256 `f2215b4161dad9577860b9c99d6e2f2599bc237b2a82fdedb340b6f6f8609934`. The probe sha256 is `ada7a9c97bba394f6539ce6f158ee81a8c342a42fa861d634933226bdd0b50d2`, identical to 5bd4a90. The non-.ufo tree digest was the same before and after the run (`9783db6c…ac44f6`), so the run did not write into the tree.
3. Candidates are pending, not pre-credited.
   - C04 `:5-6`: "coverage-map: C04 … the map row stays `uncovered` until a fresh falsify wave and an explicit all-criteria admission" / "admission-status: candidate (not admitted)". Its Q table `:278-280` is headed "decisions, not admission".
   - C09 `:15-17`: "admission-status: candidate — round-62 build wave, not admitted … nothing here flips a coverage row, and no README target row is held by this file". `:186`: "proposed by the author; not self-admission". `:204-206`: "this file asserts no admission".
   - Lesson `round-62.md:103-106` sets the build-stage status of both to "candidate, not admitted". `:15`: "no provisional held flips". `:4`: "No prior candidate is pre-credited".
   - LOG `:825` heading "candidates, not admissions"; `:828` "README remains uncovered pending fresh attacks".
   - SCORECARD.md has an empty diff from 5bd4a90 to the frozen revision, so no new K score is claimed.
4. Prior rejected warnings are unchanged. `git diff --stat 5bd4a90 d977619 --` over both old candidate files, `lessons/round-61*.md`, `reports/round-61`, `.ufo/waves/round-61`, `corpus/README.md`, `corpus/QUALITY.md`, `corpus/live`, `corpus/fixtures`, `corpus/verify_*.py`, SCORECARD.md and PROVINCE.md → empty.
   - Both old files `:5`: "admission-status: rejected — round-61 fresh falsify wave on ab58069".
   - `lessons/round-61.md:105-110`: reject rows plus "C04/C09 return to `uncovered`; final admitted 0 of these 2". No new entry cites S001–S027 (`rg -o 'S0(0[0-9]|1[0-9]|2[0-7])\b'` → no matches).
5. The clarifications are append-only. `git diff a3498e2 d977619 -- reports/round-62/claims.md` is one hunk at `@@ -75,3 +75,28 @@`, with zero `-` lines. The target text at `claims.md:9-14` is byte-identical to the declaration: "lifting K to at least 5/14 (3.6); 6/14 (4.3) if both independently pass. **4/14 falsifies C1**".
   - Every appended rule adds a necessary condition or narrows one: `:83-85` K_HELD_BACKED = K_HELD, denominator 14, only C04/C09 may change, and the knowledge cell names the NEW entry; `:93-96` non-author fresh seats, re-review by message to an existing seat, exact corrected hash, original attack result preserved; `:98-101` Q11 applies to every value, with no Q14 or lexical helper.
   - None relaxes `:47-51` "admit only entries that pass all criteria … If unresolved, retain the candidate as rejected".
6. Quality gates are unchanged. `corpus/QUALITY.md` sha256 is `811ebf73…fb51c45d1` at both 5bd4a90 and the frozen revision. Rows are exactly Q01–Q13, with no Q14.
7. Source status is not admission. S028–S031 are `mined` with `used-by` = the lesson plus the candidate. The fleet contract `SOURCES-CONTRACT-v1.md:36` defines "`mined` (cited by ≥1 path in `used-by`)", and `:56-57` counts expansion only for "admitted `knowledge/` entries". This matches the round-61 precedent: S016 and S026 are still mined, used by the rejected file.

## Inference
- On this frozen state, nothing credits either candidate toward K. The only route to 5/14 is a later explicit map edit after the fresh-wave Q01–Q13 decision. Before that, the 4/14 falsifier remains live.
- [INFERENCE] Residual risk, already named in `claims.md:42-44` and `R62CriticFrozenClaim.md`: `K_HELD_BACKED` checks only that a row exists. A future flip therefore needs the separate per-row, all-criteria decision. The probe alone cannot certify it.

## Nonfatal wording notes (no Q failed; not a defect on this axis)
- `lessons/round-62.md:3-4` cites the declaration as `a3498e25…` for `reports/round-62/claims.md`. The governing file at the frozen revision also contains the append at `:79-102`. LOG `:832` records the append, but the lesson does not.
- C09 Q table `:191-201` marks Q02–Q13 as bare "pass", while Q01 says "proposed pass, pending independent audit". It is still covered by the `:186`/`:204-206` disclaimers.
- C09 Q11 basis `:200`, "Every claimed value is a field of the printed output", is phrased as output-coverage. Under `lessons/round-62.md:97-101`, that alone cannot pass. This belongs to the Q11 inventory seats, not to admission order.
- `measure-before.log:2` ran the live-checkout probe path on the archived corpus, not an archived probe. The bytes are pinned (observation 2), so this does not affect the result.

## Unknown
- The fresh-wave Q01–Q13 outcomes for either candidate are outside this seat's scope and were not judged here.
- Whether L1's final flip will satisfy `claims.md:83-85` has not been observed yet.

## Smallest correction
None required. Optional wording fix: the lesson's declaration line could also name `d977619` for the appended clarifications.

VERDICT: HOLDS. Both rows are still uncovered on the frozen state (map plus probe K 4/14), both candidates are pending and not pre-credited, the rejected warnings are byte-preserved, and the clarifications leave the K ≥ 5/14 target and the 4/14 falsifier unchanged.
Installs: none. Scratch: /fast/scratch/hyaku/revenger-r62/R62FAdmissionOrder/{tree,tmp,measure-frozen.log}.
