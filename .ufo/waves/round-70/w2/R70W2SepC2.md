ENTANGLED — C2's own single-claim tree is clean (SELF_MISMATCH 9→0, `HOLDS_C2_V5` no→yes, `A1_C2` no→yes, every other claim's label byte-identical to base), but C1's required C05 flip alone moves **C2's** `SM6` 0→1 (SELF_MISMATCH 9→10) because `corpus/README.md` gains a 9th `held` row while `SCORECARD.md`'s last `K_HELD_BACKED` statement still reads 8/14; C2's predicate is evaluated at the final tip, which includes that flip, so C2 is not admissible separately unless C1's flip revision also appends one plain `K_HELD_BACKED … 9/14` SCORECARD line.

Seat R70W2SepC2 · wave 2 (falsify) · landed target `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` · claim base `3f5edbc206351232a3d2d801334dd930499ccaf5`
Frozen counter under test: `reports/round-70/measure.py` sha256 `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`, `reports/round-70/measure-a1.py` sha256 `96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191` (both re-hashed, match claims.md / A1).
Checker under test: `corpus/self_assessment_check.py` sha256 `82e59fce5647f27727644d121dd73641bc14a7bb3293d7e54f2070b0db0335cc`.
I did not read `.ufo/waves/round-70/w1/` before forming the verdict above; the wave-1 connector note was opened only afterwards to cross-check (see §6).

## 1. Trees built (all scratch, `git archive` of the named commits, no lane file touched)

```
D=/tmp/revenger-r70-R70W2SepC2
git -C .../revenger-shokunin archive 3f5edbc… corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C $D/base
git -C .../revenger-shokunin archive 17ee7f8… corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C $D/landed
```

| tree | content |
|---|---|
| `base` | claim base archive, untouched |
| `c2` | base **+ only claim C2's change set**: `corpus/self_assessment_check.py` (landed bytes), `SHONEN.md` (landed bytes), `SCORECARD.md` (landed bytes = base + erratum block), and exactly five `corpus/README.md` index lines — the `Q01–Q13`→`Q01–Q15` line (SM1) and bullets naming `snapshots/`, `q15_tree_id_check.py`, `derive_axml_anchors.py`, `check_embedded_outputs.py`, `self_assessment_check.py` (SM2). Deliberately **excluded** (C1/C3-owned per claims.md §Separability, line 131): the `derive_axml_anchors_r68.py` and `lint_entry.py` bullets, the `lessons/` line, the Known-gaps paragraph, the C05 row. |
| `c1only` | base + the C05 flip only (knowledge column → `knowledge/round-70-apk-axml-byte-evidence.md`, status → `held`) |
| `flip` | landed + the C05 flip only (the realistic final-tip revision) |
| `cure` | `flip` + one appended `K_HELD_BACKED 8/14 -> 9/14` SCORECARD line |
| `strictonly` | `flip` + only a `K_HELD_BACKED_STRICT=9/14` line |
| `c1sm` / `c3sm` / `c1nobullet` | base + C1's `lint_entry.py` with/without its own naming bullet; base + C3's `derive_axml_anchors_r68.py` + its bullet |

Surfaces of the `c2` tree: `corpus/README.md` sha256 `88f7e892…534b`, `SHONEN.md` `2cb4aa37…7c35` (= landed), `SCORECARD.md` `3f86dfdf…aa90` (= landed), checker `82e59fce…35cc` (= landed). `c2/corpus/README.md` vs landed README differs **only** in the C1/C3/unowned lines listed above (diff lines 14, 21a22, 22a24, 57-58).

## 2. Base labels (control A) — reproduce the documented before-vector exactly

```
$ python3 -B reports/round-70/measure.py /tmp/revenger-r70-R70W2SepC2/base      # exit=0
K_HELD_BACKED=8/14 score=5.7 ; K_HELD_BACKED_STRICT=8/14 ; C05_STATUS=uncovered
C05_KNOWLEDGE_COLUMN=- ; C05_SINGLE_V5=no ; V5_ENTRY_PRESENT=no ; V5_ADMITTED_MARKED=no
C1_GATE=n/a ; C1_LINT=n/a ; HOLDS_C1_V5=no
SELF_MISMATCH=n/a (no checker) ; SELF_CLEAN_FIXTURE=n/a ; SELF_MUTANTS_KILLED=n/a
SHONEN_BOX_COUNT=4 ; README_ROWS=14 ; HOLDS_C2_V5=no
EMB_R65=checked_blocks=15 problems=1 exit=1 ; EMB_R67=checked_blocks=16 problems=0 exit=0
EMB_R68=checked_blocks=17 problems=7 exit=1 ; EMB_R69=checked_blocks=17 problems=0 exit=0
EMB_PINNED_SCRIPT_IS_S046=no ; EMB_R68_BYTES_UNCHANGED=yes ; EMB_R65_BYTES_UNCHANGED=yes
EMB_PIN_MUTANT_KILLED_ATTRIBUTED=n/a ; HOLDS_C3_V1=no
HOLD_REPLAY=10/10 ; GATE_SELFTEST=exit 0 ; F_COVERAGE=5/8 ; FRESH_ROWS=18/18 ; HOLDS_OK_V7=yes
$ python3 -B corpus/self_assessment_check.py --root base --lane .../revenger-shokunin     # exit=1
SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0  SELF_MISMATCH=9
$ python3 -B reports/round-70/measure-a1.py base                                          # exit=1
A1_C1=no A1_C2=no A1_C3=no
```
This is byte-for-byte the documented before-vector (`claims.md` §C2 "Before": SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0, SELF_MISMATCH=9; §C3 "Before": `EMB_R68 problems=7`), and control A's `HOLDS_C1/C2/C3_V*=no` with `HOLDS_OK_V7=yes`.

## 3. C2-only tree: the claim's own labels move to target, and nothing else moves

```
$ python3 -B reports/round-70/measure.py c2      # exit=0
K_HELD_BACKED=8/14 ; K_HELD_BACKED_STRICT=8/14 ; C05_STATUS=uncovered ; C05_KNOWLEDGE_COLUMN=-
C05_SINGLE_V5=no ; V5_ENTRY_PRESENT=no ; V5_ADMITTED_MARKED=no ; C1_GATE=n/a ; C1_LINT=n/a ; HOLDS_C1_V5=no
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 ; SELF_MISMATCH=0 exit=0
SELF_CLEAN_FIXTURE=0 ; SELF_MUTANTS_KILLED=6/6 ; SHONEN_BOX_COUNT=4 ; README_ROWS=14 ; HOLDS_C2_V5=yes
EMB_R65=15/1 ; EMB_R67=16/0 ; EMB_R68=17/7 ; EMB_R69=17/0 ; EMB_PINNED_SCRIPT_IS_S046=no
EMB_R68_BYTES_UNCHANGED=yes ; EMB_R65_BYTES_UNCHANGED=yes ; EMB_PIN_MUTANT_KILLED_ATTRIBUTED=n/a ; HOLDS_C3_V1=no
HOLD_REPLAY=10/10 ; GATE_SELFTEST=exit 0 ; F_COVERAGE=5/8 ; FRESH_ROWS=18/18 ; HOLDS_OK_V7=yes
$ python3 -B reports/round-70/measure-a1.py c2   # exit=1
A1_C1_DETAIL=no v5 entry            -> A1_C1=no   (= base)
A1_C2_DETAIL=base_vector=yes clean_variant=yes defect_variants=6/6 -> A1_C2=yes   (base: no)
A1_C3_DETAIL=no pin file            -> A1_C3=no   (= base)
$ diff <(measure.py base) <(measure.py c2)
11,13c11,19  SELF_MISMATCH/CLEAN/MUTANTS n/a -> SM1..SM6=0, SELF_MISMATCH=0, SELF_CLEAN_FIXTURE=0, SELF_MUTANTS_KILLED=6/6
16c22        HOLDS_C2_V5=no -> yes
```
Only the C2 block moves; every other line of the counter is identical to base, so **C2's tree raises no other claim's label**. `A1_C2` reproduces the pinned before-vector on `git archive 3f5edbc…` (SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0, `SELF_MISMATCH=9`) and scores the clean variant 0 and six freshly randomised single-defect variants exactly (`defect_variants=6/6`) — i.e. the checker is not fixture-shaped.

Per-class attribution on the base tree (each C2 repair kills exactly its class):
- SM1 `1→0`: `corpus/README.md:9` `Q01–Q13`→`Q01–Q15` (`QUALITY.md` holds Q15).
- SM2 `4→0`: bullets for `snapshots/`, `q15_tree_id_check.py`, `derive_axml_anchors.py`, `check_embedded_outputs.py` (`self_assessment_check.py` bullet added for the new file, else it would be a 5th miss).
- SM3 `2→0` + SM4 `1→0`: `SHONEN.md` box 1 rewritten to `[~]` with no quoted `N bytes` / `sha256` and no `Named non-author verifier:` seat clause.
- SM5 `1→0`: `SCORECARD.md:605` `erratum: e1d22caf -> e1d22caa…` (prefix 8 ≥ 6; `git -C lane cat-file -e e1d22caa…^{commit}` resolves).
- SM6 `0→0`: unchanged, because the C2 tree keeps the C05 row `uncovered` (8 held = SCORECARD's last K statement, `SCORECARD.md:612`).

## 4. The entanglement: C1's flip moves C2's SM6 (the falsifying finding)

```
$ python3 -B corpus/self_assessment_check.py --root c1only --lane .../revenger-shokunin   # base + C05 flip ONLY
SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=1   SELF_MISMATCH=10          (base: SM6=0, SELF_MISMATCH=9)
$ python3 -B corpus/self_assessment_check.py --root flip    --lane .../revenger-shokunin   # landed + C05 flip ONLY
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=1   SELF_MISMATCH=1  exit=1
$ python3 -B reports/round-70/measure.py flip | grep -E 'SM6|SELF_MISMATCH|HOLDS_C2|K_HELD_BACKED=|C05_STATUS'
K_HELD_BACKED=9/14 score=6.4 ; C05_STATUS=held
SM6=1 ; SELF_MISMATCH=1 exit=1 ; SELF_CLEAN_FIXTURE=0 ; SELF_MUTANTS_KILLED=6/6 ; HOLDS_C2_V5=no
```
Mechanism, all in bytes: `corpus/self_assessment_check.py:178` counts README rows matching `| held |$`; the flip at `corpus/README.md:41` (landed text: `| C05 | Android packages (APK) | — | … | uncovered |`) turns that count 8→9; `:179-184` then compares it with the **last** SCORECARD line containing `K_HELD_BACKED`, which at the landed tip is `SCORECARD.md:612` `` `K_HELD_BACKED=8/14` `` inside the round-69 erratum prose. 9 ≠ 8 → `SM6=1`.

This is not a C2 defect (C2's bytes are correct at the landed candidate: `landed` tree scores `SM1..SM6=0 SELF_MISMATCH=0 exit=0`), and not a checker defect (it is doing exactly what its docstring says: the SCORECARD's stated K must equal the README held rows). It is a **composition** defect: `claims.md:131` asserts "no claim's tree raises another claim's label above its base value", and C1's tree does — C2's SM6 0→1, hence SELF_MISMATCH 9→10. C2's frozen predicate is read "at the final lane tip", and the final tip is the flip revision (C1 landing order step 4), so C2 as written cannot be admitted without a byte that C1's declared change set ("C1 names `lint_entry.py` and flips the C05 row") does not contain.

Cure, verified (one plain SCORECARD statement, appended after the erratum):
```
$ printf '\nK_HELD_BACKED 8/14 -> 9/14 (round-70 C1 flip after-state)\n' >> cure/SCORECARD.md
$ python3 -B corpus/self_assessment_check.py --root cure --lane .../revenger-shokunin
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0   SELF_MISMATCH=0   exit=0
```
Trap worth recording for whoever writes that line: a `K_HELD_BACKED_STRICT=9/14`-only line does **not** cure it, because `self_assessment_check.py:182` truncates each line at `K_HELD_BACKED_STRICT` before matching, leaving `stmts` empty → SM6 stays 1:
```
$ python3 -B corpus/self_assessment_check.py --root strictonly …
SM6=1   SELF_MISMATCH=1   exit=1
```

## 5. The other direction (other claims' trees vs C2's labels) — no further harm

```
$ python3 -B corpus/self_assessment_check.py --root c1sm      # base + lint_entry.py + its own naming bullet
SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0  SELF_MISMATCH=9        (= base)
$ python3 -B corpus/self_assessment_check.py --root c3sm      # base + derive_axml_anchors_r68.py + its bullet
SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0  SELF_MISMATCH=9        (= base)
$ python3 -B corpus/self_assessment_check.py --root c1nobullet  # base + lint_entry.py WITHOUT its bullet
SM2=5  SELF_MISMATCH=10
```
So the per-claim README-naming convention is load-bearing but sufficient: each claim naming its own new top-level `corpus/` artifact keeps SM2 at base. C3's new `derive_axml_anchors_r68.py` is likewise covered by C3's own bullet. No other cross-claim label movement was observed in any tree.

## 6. Cross-check against the (non-author) wave-1 record — after my verdict

`.ufo/waves/round-70/w1/R70W1ConnSeparability.md` (VERDICT "SEPARABLE — with a split") independently names the same coupling ("C1's C05 flip moves C2's `SM6` … C1's change set must also carry one SCORECARD `K_HELD_BACKED` line append (9/14)"). My numbers agree on the mechanism and the required append; I add the measured base-vs-flip values (SM6 0→1, SELF_MISMATCH 9→10, `HOLDS_C2_V5=no` at the flip), the strict-only-line trap, and the note that this makes `claims.md:131`'s assertion false as literally written rather than merely "an unlisted addition".

## 7. Notes, risks, blockers

- **Scope discipline.** No lane file was written, edited, committed or pushed; every attack ran on `cp -r`/`git archive` copies under `/tmp/revenger-r70-R70W2SepC2`. Scratch deleted after this report. No package installs or upgrades were needed (Python stdlib only; no `uv tool`/`npx` run).
- **Unmeasured C2 surface (coverage note, not a kill).** C2's claim says the tool is "registered as a gate" — the `SKILL.md` `## Gate registry` row and the `corpus/README.md` Known-gaps paragraph carry that, but **no frozen label reads `SKILL.md`** (only SM3 reads it indirectly through SHONEN quotes, which are now absent). So "registered as a gate" is asserted in prose and verified by nothing; I did not count it against C2 because the frozen predicate does not name it.
- **`A1_C2` needs the lane repo.** `measure-a1.py:a1_c2` shells `git -C <LANE> archive 3f5edbc…` and SM5 shells `git cat-file` in the lane; both worked read-only from this seat. If either is run from a sandbox repo the labels would read `no` for reasons unrelated to the claim.
- **What a FAIL here would mean.** Nothing in C2's own bytes failed: at the landed candidate the checker scores 0 and `HOLDS_C2_V5=yes`, and `A1_C2=yes`. The falsifying fact is the final-tip coupling in §4; if the L1 lands the flip without the SCORECARD 9/14 statement, C2's frozen predicate reads `HOLDS_C2_V5=no` at the final tip and C2 falsifies — mechanically, by command, not by judgement.
