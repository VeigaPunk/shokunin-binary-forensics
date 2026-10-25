SURVIVORS — all six SM-class neutralization mutants and all three named literal-matching cheats are killed (A1_C2 kills every cheat; the frozen counter's mutation leg alone does not kill fixture-shaped ones), but one hybrid checker (pristine honest fallback + `$SELF_ASSESSMENT_ANSWER` override) survives BOTH counters with every label green — an env-canary control would close that class.

# R70W2CheckerMut — mutation probe of `corpus/self_assessment_check.py` (landed 17ee7f87)

Seat: R70W2CheckerMut (wave-2 falsify, leaf). Scope: kill-test the landed C2 checker against the frozen
counters. No lane file was written; all work happened in scratch `/tmp/revenger-r70-R70W2CheckerMut/`
(deleted before return). No packages installed (python3 stdlib only; no pacman, no uv/npx installs).

## Setup and baseline (detector sanity)

- Scratch tree: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C /tmp/revenger-r70-R70W2CheckerMut/tree` — 25 corpus entries.
- Frozen counters verified before use: `sha256sum` → measure.py `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`, measure-a1.py `96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191` — both match claims.md/claims-amendment-A1.md.
- Pristine checker: `corpus/self_assessment_check.py` sha256 `82e59fce5647f27727644d121dd73641bc14a7bb3293d7e54f2070b0db0335cc` (= sha256 of `git show 17ee7f87…:corpus/self_assessment_check.py`, blob oid `9ce01f881649a4138197bbd537fa79131601d3d2`). Class functions at lines 55 (`sm1`), 65 (`sm2`), 97 (`sm3`), 127 (`sm4`), 140 (`sm5`), 175 (`sm6`); `evaluate` at 190.
- Counter legs under test: measure.py:72-117 (`build_self_fixture` + `self_check`: clean fixture must score rc0/`SELF_MISMATCH=0`; each planted class must score rc1/`SELF_MISMATCH=1`/class=1) printed at measure.py:183-191; measure-a1.py:88-114 (`variant`, randomized literals) and 116-138 (`a1_c2`: documented before-vector on `git archive 3f5edbc…` + clean variant 0 + six randomized defect variants exactly 1).
- Neither counter manipulates the environment: the only `env` occurrences in both files are the `#!/usr/bin/env python3` shebangs (`grep -n env measure.py measure-a1.py` → line 1 each). Counter subprocesses inherit my shell env, in which `SELF_ASSESSMENT_ANSWER` is unset.

Baseline on the landed tree with the pristine checker (both counters run concurrently on the same tree state; full logs saved per state):

```
== baseline 3s measure_rc=0 a1_rc=0
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0
SELF_MISMATCH=0 exit=0
SELF_CLEAN_FIXTURE=0
SELF_MUTANTS_KILLED=6/6
HOLDS_C2_V5=yes
A1_C2_DETAIL=base_vector=yes clean_variant=yes defect_variants=6/6
A1_C2=yes
```

The landed tree scores `SELF_MISMATCH=0` (C2 treatment is in the landed bytes) and the detector is green — a baseline failure would have made every later result inconclusive; it did not fail.

## Battery A — six class-neutralization mutants (each `def smN(...)` gets `return 0` as its first statement)

Overlay: mutated checker written into the SCRATCH tree's `corpus/self_assessment_check.py`; the lane file was never touched.

| mutant (landed blob line) | measure.py | measure-a1.py | verdict |
|---|---|---|---|
| sm1 → 0 (:55) | `SELF_MUTANTS_KILLED=5/6`, `HOLDS_C2_V5=no` | `A1_C2=no` (`base_vector=no defect_variants=5/6`) | KILLED |
| sm2 → 0 (:65) | `SELF_MUTANTS_KILLED=5/6`, `HOLDS_C2_V5=no` | `A1_C2=no` (`base_vector=no defect_variants=5/6`) | KILLED |
| sm3 → 0 (:97) | `SELF_MUTANTS_KILLED=5/6`, `HOLDS_C2_V5=no` | `A1_C2=no` (`base_vector=no defect_variants=5/6`) | KILLED |
| sm4 → 0 (:127) | `SELF_MUTANTS_KILLED=5/6`, `HOLDS_C2_V5=no` | `A1_C2=no` (`base_vector=no defect_variants=5/6`) | KILLED |
| sm5 → 0 (:140) | `SELF_MUTANTS_KILLED=5/6`, `HOLDS_C2_V5=no` | `A1_C2=no` (`base_vector=no defect_variants=5/6`) | KILLED |
| sm6 → 0 (:175) | `SELF_MUTANTS_KILLED=5/6`, `HOLDS_C2_V5=no` | `A1_C2=no` (`base_vector=yes defect_variants=5/6`) | KILLED |

Every mutant drops the frozen counter to `5/6` (the counter's planted defect of the neutralized class now scores 0, so `per.get(cls) != "1"`), and A1_C2 to `defect_variants=5/6`. Note the nuance on sm6: its base-tree before-value is 0, so `base_vector=yes` survives neutralization — the randomized-defect-variant leg is what kills it. The base-vector leg alone is not a complete detector.

## Battery B — three named literal-matching cheats

**Cheat 1 — base-marker echo** (prints the documented before-vector `SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0 / SELF_MISMATCH=9` when base-tree markers are seen — SKILL.md sha256 prefix `a12fb8e2` (verified: base SKILL.md = `a12fb8e2507dd5de…`, 51809 bytes) AND README `Q01–Q13` line (verified: base corpus/README.md line 9) — and all-zeros otherwise):
measure.py: `SELF_MUTANTS_KILLED=0/6`, `HOLDS_C2_V5=no`; measure-a1.py: `A1_C2_DETAIL=base_vector=yes clean_variant=yes defect_variants=0/6`, `A1_C2=no`. **KILLED by both counters** (the randomized defect variants expose it).

**Cheat 2 — fixture-literal hardcoder** (dumb grep keyed to the frozen counter's `build_self_fixture` literals: `Q01–Q01`, `corpus/unnamed.py`, `101 bytes`, `revenger-r64.R64ReviewSkill`, `deadbee0123`, `8/14 → 9/14`):
measure.py: `SELF_CLEAN_FIXTURE=0`, **`SELF_MUTANTS_KILLED=6/6`** — it survives the frozen counter's mutation leg — but the tree-run leg trips it on the landed tree: `SM4=1 … SELF_MISMATCH=1 exit=1` because landed `SHONEN.md` line 6 contains the literal in an explanatory clause ("Lane attestation, not a non-author check: the named verifier `revenger-r64.R64ReviewSkill` …"), so `HOLDS_C2_V5=no` on this tree. measure-a1.py: `A1_C2_DETAIL=base_vector=no clean_variant=yes defect_variants=0/6`, `A1_C2=no`. **KILLED by A1_C2** (both the base-vector leg and the randomized-variant leg).

**Cheat 3 — env-var oracle** (entire answer from `$SELF_ASSESSMENT_ANSWER`; unset → all-clean):
measure.py: `SELF_MUTANTS_KILLED=0/6`, `HOLDS_C2_V5=no`; measure-a1.py: `A1_C2_DETAIL=base_vector=no clean_variant=yes defect_variants=0/6`, `A1_C2=no`. **KILLED by both counters.** The oracle path is live, shown on a broken tree (planted `corpus/unnamed.py`):

```
$ python3 -B tree-broken/corpus/self_assessment_check.py --root tree-broken --lane <LANE>   # pristine honest
SM2=1 / SELF_MISMATCH=1, rc=1
$ SELF_ASSESSMENT_ANSWER=$(printf 'SM1=0\nSM2=0\nSM3=0\nSM4=0\nSM5=0\nSM6=0\nSELF_MISMATCH=0') \
  python3 cheat3_env_oracle.py --root tree-broken --lane <LANE>
SM1=0 … SM6=0 / SELF_MISMATCH=0, rc=0    # forged all-clean on a broken tree
```

## Extended probes (same probe family; recorded as coverage findings)

**Cheat 2b — shape-gated, control-J faithful** (fires the keyed literals only when the tree has the counter-fixture shape `corpus/tool.py` + `corpus/fixtures/f.txt` + `corpus/verify_a.py`; all-clean on any other tree — the landed corpus has none of the three, verified by `ls`):
measure.py: `SELF_CLEAN_FIXTURE=0`, `SELF_MUTANTS_KILLED=6/6`, tree-run `SELF_MISMATCH=0 exit=0` → **`HOLDS_C2_V5=yes`** — it survives the ENTIRE frozen counter on the landed tree. measure-a1.py: `A1_C2_DETAIL=base_vector=no clean_variant=yes defect_variants=0/6`, `A1_C2=no`. **KILLED by A1_C2 only.** Independently reproduces amendment A1's control-J rationale: the frozen counter's mutation leg cannot kill a fixture-shaped cheat; A1_C2's base-vector + randomized-variant legs are the legs that do.

**Cheat 3b — hybrid env-override (THE SURVIVOR)**: the pristine honest checker with one hook inserted at the top of `main()` — if `$SELF_ASSESSMENT_ANSWER` is set, print it and exit; otherwise behave exactly honestly:

```
== cheat3b-env-hybrid 3s measure_rc=0 a1_rc=0
SELF_MISMATCH=0 exit=0
SELF_CLEAN_FIXTURE=0
SELF_MUTANTS_KILLED=6/6
HOLDS_C2_V5=yes
A1_C2_DETAIL=base_vector=yes clean_variant=yes defect_variants=6/6
A1_C2=yes
```

Both counters exit 0 with every C2 label green. No counter input distinguishes it from the honest checker: the counters never set the variable, and the honest fallback passes every fixture, the tree run, the base-vector leg and all randomized variants. The backdoor fires only on invocations made with the variable set (demo above shows the identical oracle path). This is a coverage finding, not a contract change: a canary-env control (counter sets a poison value and requires the checker's output to be unaffected) would close the class; that is the lane's call, not mine.

## Restoration evidence

- After every driver run the scratch tree's checker was restored from the pristine copy; each driver printed `restored sha256: 82e59fce5647f27727644d121dd73641bc14a7bb3293d7e54f2070b0db0335cc` — byte-identical to the landed blob (verified against `git show 17ee7f87…:corpus/self_assessment_check.py` at setup).
- `tree-broken` was a scratch copy; the lane repo, its corpus/, reports/, SHONEN.md, SCORECARD.md, SKILL.md were only ever read. Writes: this report + `/tmp/revenger-r70-R70W2CheckerMut/*` (deleted before return).

## Findings for the gate

1. The landed checker's six class functions are genuinely load-bearing: every single-class neutralization is killed by both counters (`5/6` + `A1_C2=no`). C2's mutation defense holds for the assigned battery on the landed bytes.
2. A1_C2 is the leg that kills literal-matching cheats: the base-marker echo, the dumb fixture-literal hardcoder and the env-oracle all die to it, and it alone kills the J-faithful shape-gated variant that the frozen counter passes outright (`HOLDS_C2_V5=yes` with cheat2b overlaid). The frozen counter's mutation leg alone is insufficient against fixture-shaped cheats.
3. One survivor class exists: an env-gated override over an honest fallback passes both counters with all labels green (cheat3b). Neither counter probes the environment. Recorded as a coverage finding; no contract change proposed or made by this seat.
