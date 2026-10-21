GRADE: PARTIAL — C1 K-probe existence-as-taste on frozen d97761952be256d145d298022de03091de91d358 (current 4/14 correct; nonfatal admission-path gaps)

Seat `RevengerR61-2.R62FCriticKCounter` (critic, leaf). Frozen `d97761952be256d145d298022de03091de91d358`, claimbase `5bd4a90fc1a34caa94496601b60537b3aab12301`, prereg `a3498e25ad87bf756288812d0ea7c474b09433c7` (all `git rev-parse ^{commit}` verified). Archive: `git -C <lane> archive d977619… | tar -x -C /fast/scratch/hyaku/revenger-r62/R62FCriticKCounter/tree` (+ `… corpus` into `probe-tree`). Candidate sha256: C04 `round-62-commonjs-require-name-evidence.md` `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`; C09 `round-62-evm-dispatch-byte-evidence.md` `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`. Probe `reports/round-61/measure.py` `ada7a9c97bba394f6539ce6f158ee81a8c342a42fa861d634933226bdd0b50d2` (= pinned).

## Observation
O1 Frozen probe, archived copy, cwd=/, `TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FCriticKCounter/tmp`, exit 0 (`probe-frozen.out` sha256 `ad003a46…71f6`):
`K_HELD=4/14 score=2.9` · `K_ROW C04 status=uncovered` · `K_ROW C09 status=uncovered` · `K_HELD_BACKED=4/14` · `C2_CONTROLS_PASS=2/2` · `C2_RECEIPT_B_KILLED=2/2` · `C2_D2_KILLED=2/2` · `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2` · `HOLD_CALIBRATION=4/4` · `HOLD_REPLAY=10/10` · `HOLDS_OK=yes`. Identical K/holds to `reports/round-62/measure-before.log` (base 5bd4a90).
O2 Held rows at frozen `corpus/README.md:30,40-42`: C01, C11, C12, C13; C04 `:33` and C09 `:38` `uncovered`, cell 3 has no `knowledge/*.md` path (only `lessons/round-61.md`); new candidates are NOT named in any row.
O3 Tree identity 5bd4a90→d977619: `corpus/live` a35d3071…, `corpus/fixtures` c6287377…, `corpus/QUALITY.md` 19f66afe…, `corpus/README.md` ffcd00bd… unchanged. `git diff --name-status 5bd4a90 d977619 -- corpus`: only `M SOURCES.md`, `A` the two candidates, `A lessons/round-62.md`. No `verify_*.py` added (10 present), no SKILL/registry/gate file in tree or lane root. Preserved sha256 match the build reference: rejected C04 `690db9f1…a6f3`, rejected C09 `3e17b88f…1361`, spotcheck `c83f2d29…65d2`, `lessons/round-61.md` `da59f8d9…3c08`, r61 claims/measure-before/after `428e903c…`/`60cc3b63…`/`017f7fc7…`.
O4 Counterexample battery `kmut.py` (sha256 `7a3cbb8c…94a4`) runs the unchanged probe on scratch copies of the archived corpus with one README edit each; output `kmut.out` (sha256 `2d27e97e…175f`):
```
A_new_candidate   C04 held, cell3=round-62 C04 (still `admission-status: candidate`)  K_HELD=5/14 K_HELD_BACKED=5/14
B_old_rejected    C04 held, cell3=round-61 rejected file                           K_HELD=5/14 K_HELD_BACKED=5/14
C_empty_stub      C04 held, cell3=1-line stub file                                  K_HELD=5/14 K_HELD_BACKED=5/14
D_nontarget_C03   C04+C03 held (K_ROW shows only C04/C09)                           K_HELD=6/14 K_HELD_BACKED=6/14
E_missing_file    C04 held, cell3 file absent                                       K_HELD=5/14 K_HELD_BACKED=4/14
F_trailing_space  C04 held + trailing space after final `|`                         K_HELD=4/14 K_HELD_BACKED=4/14, yet K_ROW C04 status=held
```
O5 Guards present in frozen text: `claims.md:41-44` (K_HELD_BACKED is existence, not admission; per-candidate Q01–Q13 decisions are the independent necessary condition); `:82-85` (K_HELD_BACKED = K_HELD, denominator 14, only C04/C09 change, flipped row names only its NEW admitted entry); `:57` lost held row voids (covers demotion masking); `:87` no verify_*.py add/delete; `:89-91` TMPDIR; `:93-95` recommendations from fresh non-author/corrector seats, L1 adjudicates, focused re-review names corrected hash; `:100-101` no Q14/lexical helper. Lesson `round-62.md:93-101,104-112` repeats: no Q14, Q01–Q13 unchanged, both candidates "candidate, not admitted", fresh independent decision required. LOG:825-832 "candidates, not admissions", "no new gate software/registry claim".
O6 Author self-assessments live inside the candidates: C04 `:278-296` "QUALITY check — decisions, not admission… this seat's reading"; C09 `:186-202` "proposed by the author; not self-admission". Neither names its author seat; LOG:828 records that L1 also edited candidate text ("L1 removed stale reserved-row wording…").
O7 No frozen text (claims, lesson, either entry) specifies what happens to `admission-status: candidate` on admission. C09 `:15-17`: "nothing here flips a coverage row, and no README target row is held by this file." C04 `:5-6,280`: map row "stays `uncovered` until…", `admission-status: candidate (not admitted)`. README index `corpus/README.md:11-13` describes `knowledge/` as admitted entries plus rejected candidates "each carries an `admission-status: rejected` header"; at d977619 it also holds two `candidate`-status files.

## Inference
I1 Current 4/14 is the correct pre-admission value, not a failed implementation: no row was flipped (O2), no fresh-wave Q decision exists yet (`falsify/` contained only peer reports at write time), and claims `:45-46` require uncovered status while drafting and attacking. The K value C1 must reach is still pending, not falsified.
I2 The existence-only blind spots B, C, D, E and the demotion/denominator variants are covered by separate, pre-registered necessary checks (O5). The fresh all-criteria recommendations stay separate from the probe and from the in-entry author tables (O6 labels them non-admission; claims `:93`). No new gate, registry conformity or promotion is claimed (O3, O5).
I3 Residual gap (A + O7): the probe counts a file still marked `candidate` as backing, and no procedure defines the header transition. Admitting without editing leaves a held row contradicting the entry's own C09 `:16-17` sentence and the README index (a factual value that would then fail Q11). Admitting with an edit changes the hash the fresh wave attacked, and claims `:93-95` / lesson `:110-112` do not say whether a header-only edit counts as a "correction" that needs focused re-review. The build critic's correction 2(c) (`R62CriticFrozenClaim.md:23`) and README plan F4 (`R62ReadmeAdmissionPlan.md:62-64`) flagged this, and it was not carried into claims `:79-101`.
I4 F is fail-safe (it undercounts) but brittle: an admitted flip whose row ends `| held | ` reads 4/14 while K_ROW prints `held`. The final row must end exactly `| held |`.
I5 L1 is a corrector (O6), so L1's adjudication cannot itself serve as any candidate's independent Q decision. Claims `:93` already separates the two; the author/corrector exclusion list should name L1 alongside R62JsEntry/R62EvmEntry (build report names).

## Path and statuses required for final ≥5/14 (per candidate)
1. Fresh non-author/corrector seats give a recorded Q01–Q13 pass on the exact candidate sha256, with a Q11 per-value audit, not output equality.
2. L1 records the adjudication in lesson `## Gate`; any correction gets a focused re-review on the corrected hash.
3. The entry's `admission-status:` and self-status sentences are updated, bound to the reviewed hash via a recorded diff/re-review.
4. README row: cell 3 names only the new file; the old rejected file stays in cell 4; the row ends `| held |`.
5. Unchanged probe on the committed archive: K_HELD = K_HELD_BACKED ≥ 5, denominator 14, base→final 14-row status diff where only C04/C09 change, attributed 2/2 checked separately, HOLDS_OK=yes, preservation hashes as in O3, TMPDIR recorded.

## Unknown
Fresh-wave Q outcomes for either candidate; whether L1 will treat a header-only edit as a correction. I did not audit candidate Q11 contents (other seats' scope).

## Smallest safe correction (non-blocking, before any held flip)
Append to claims/lesson: "On admission, `admission-status:` becomes `admitted — round 62, <Gate ref>` and the self-status sentences (C04:5,280; C09:15-17) are updated. This header/status-only diff is recorded with the pre- and post-edit sha256 and is focused-re-reviewed by an existing fresh seat. A held row naming a file whose header is not `admitted` does not count." Also amend README index `:11-13` to mention pending `admission-status: candidate` files. No repair performed.

VERDICT: PARTIAL. K4/14 at d977619 is correct and holds/preservation are intact. Recommendations stay separate and no gate/registry is claimed. The admission-status transition and its hash binding are unspecified (probe variant A counts an unadmitted candidate), and the README index wording is stale. Neither is a fatal contradiction of a current requirement, and no Q fails at the frozen state.
Installs: none. Scratch: `/fast/scratch/hyaku/revenger-r62/R62FCriticKCounter/` (`tree/`, `probe-tree/`, `kmut.py`, `kmut.out`, `probe-frozen.out`, `tmp/`).
