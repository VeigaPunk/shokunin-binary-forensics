ENTANGLED — C1's own frozen landing step (flip README C05 → `held`) moves C2's frozen label `HOLDS_C2_V5` from `yes` to `no` (SM6 0→1) at the only tip where C1 holds, so C1 and C2 cannot both be admitted in this round as the contract is written; the §Separability argument checks only single-claim trees and only the "raise" direction, while every frozen predicate is evaluated at the merged final tip.

Seat: `R70W2SepCritic` (fresh wave-2 seat). Target bytes: lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`; base `3f5edbc206351232a3d2d801334dd930499ccaf5`. Counter hashes verified before use:

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && sha256sum reports/round-70/measure.py reports/round-70/measure-a1.py
488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76  reports/round-70/measure.py
96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191  reports/round-70/measure-a1.py
```

Method: three single-claim trees plus a "flip" tree, built in `/tmp/revenger-r70-R70W2SepCritic` from
`git archive 17ee7f8 corpus SHONEN.md SCORECARD.md SKILL.md` (full tree) by reverting the other claims' files to
`git show 3f5edbc:<path>`; the lane working tree was never written. No tool installed or upgraded (nothing needed;
python3 stdlib only).

## Baseline labels, landed candidate bytes (no flip)

```
$ python3 -B reports/round-70/measure.py /tmp/revenger-r70-R70W2SepCritic/full
K_HELD_BACKED=8/14 score=5.7        C05_STATUS=uncovered        V5_ADMITTED_MARKED=no
C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes   C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
HOLDS_C1_V5=no
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0  SELF_MISMATCH=0 exit=0  SELF_CLEAN_FIXTURE=0  SELF_MUTANTS_KILLED=6/6
SHONEN_BOX_COUNT=4  README_ROWS=14   HOLDS_C2_V5=yes
EMB_R65=15/1 EMB_R67=16/0 EMB_R68=17/0 EMB_R69=17/0  EMB_PINNED_SCRIPT_IS_S046=yes
EMB_R68_BYTES_UNCHANGED=yes EMB_R65_BYTES_UNCHANGED=yes EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1  HOLDS_C3_V1=yes
HOLD_REPLAY=10/10  GATE_SELFTEST=exit 0  F_COVERAGE=5/8  FRESH_ROWS=18/18  HOLDS_OK_V7=yes   exit=0
```

## F1 — HARM (fatal): C1's flip moves C2's SM6, so C2's frozen predicate is false at the final tip

Contract lines: `reports/round-70/claims.md:51` (landing step 4: "one revision flips README C05 → `held`"),
`claims.md:82` (C2 predicate: "At the final lane tip: `SELF_MISMATCH=0` …"), `claims.md:89` (kill rule: "Any
conjunct false at the final tip falsifies C2"). The final tip of the round is by construction the flip revision;
the pre-flip tree is not a tip at which C1's predicate can be read (`C05_STATUS=uncovered`).

I applied exactly that flip to a copy (README C05 row → `knowledge/round-70-apk-axml-byte-evidence.md` + `held`,
entry header `admission-status: admitted`; every other byte kept):

```
$ python3 -B reports/round-70/measure.py /tmp/revenger-r70-R70W2SepCritic/flip
K_HELD_BACKED=9/14 score=6.4  K_HELD_BACKED_STRICT=9/14  C05_STATUS=held
C05_KNOWLEDGE_COLUMN=knowledge/round-70-apk-axml-byte-evidence.md  C05_SINGLE_V5=yes  V5_ADMITTED_MARKED=yes
C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes   C1_LINT=... exit=0      HOLDS_C1_V5=yes
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=1    SELF_MISMATCH=1 exit=1
SELF_CLEAN_FIXTURE=0  SELF_MUTANTS_KILLED=6/6  SHONEN_BOX_COUNT=4  README_ROWS=14
HOLDS_C2_V5=no                          <-- was yes on the same bytes before the flip
EMB_R65=15/1 EMB_R67=16/0 EMB_R68=17/0 EMB_R69=17/0  HOLDS_C3_V1=yes
HOLD_REPLAY=10/10 GATE_SELFTEST=exit 0 F_COVERAGE=5/8 FRESH_ROWS=18/18 HOLDS_OK_V7=yes  exit=0
```

Mechanism, located:

- `corpus/self_assessment_check.py:175-187` (`sm6`): `held` = README rows whose status cell is `held`;
  `last` = the **last line of SCORECARD.md containing `K_HELD_BACKED`**; `cur = stmts[-1][1] or stmts[-1][0]`.
- In the landed bytes that last line is `SCORECARD.md:612` — round-69 narrative prose, not a current-state
  statement: `` `K_HELD_BACKED=8/14` (and `K_HELD_BACKED_STRICT=8/14`) before the `NameError`, and only the hold block was``.
  So `cur=8`; the flip makes `held=9`; SM6=1.
- Nothing in `claims.md` or `claims-amendment-A1.md` declares that the flip revision edits `SCORECARD.md`
  (grep over both files shows SM6 only as the before-vector value `SM6=0`, `claims.md:79`).

This is not fixable by a static C2-landed line, which I tested both ways:

```
$ printf '\nK_HELD_BACKED 9/14 (round-70 C05 admission; current state)\n' >> SCORECARD.md
  flip tree  -> SM6=0  SELF_MISMATCH=0        (HOLDS_C2_V5 becomes yes again)
  full tree  -> SM6=1  SELF_MISMATCH=1        (candidate tip now false)
$ printf '\nK_HELD_BACKED 8/14 → 9/14 (round-70)\n' >> SCORECARD.md      # sm6 reads the AFTER value
  full tree  -> SM6=1  SELF_MISMATCH=1
```

No single line written at the candidate revision satisfies SM6 at both the candidate tip (held=8) and the final
tip (held=9); the line must be written **by the flip revision**, i.e. by C1's step 4 editing a C2-owned file.
The two claims are therefore entangled at the contract's own evaluation point: as written, executing the frozen
landing order turns C2's kill rule on (`SELF_MISMATCH=1` at the final tip).

Second-order defect worth naming: C2's instrument is green at the candidate tip only because a **round-69
narrative sentence** (`SCORECARD.md:612`) happens to quote the current count. The checker has no notion of a
current-state K statement, so any future admission silently breaks it — this is the same class the claim exists
to remove (a self-assessment statement that does not track repo state), moved from prose into the instrument.

## F2 — COUPLING (undocumented): README index lines 22 and 24 are needed by C2's SM2 but are owned by C3 and C1

`claims.md:131-133` partitions README index lines per claim (C1 names `lint_entry.py`; C3 names
`derive_axml_anchors_r68.py`). But `corpus/self_assessment_check.py:65` (`sm2`) requires **every top-level
`corpus/*.py` present in the tree** to be named in README. `corpus/lint_entry.py` is C1's file
(`A corpus/lint_entry.py` in the diff) and `corpus/derive_axml_anchors_r68.py` is C3's (`A corpus/derive_axml_anchors_r68.py`).
In the landed tree, C2's `SELF_MISMATCH=0` therefore depends on C1's and C3's index lines:

```
$ cp -r full sm2test && sed -i '/^- `derive_axml_anchors_r68.py`/d; /^- `lint_entry.py`/d' sm2test/corpus/README.md
$ python3 -B sm2test/corpus/self_assessment_check.py --root /tmp/revenger-r70-R70W2SepCritic/sm2test --lane /home/vgpnk/Projects/shokunin/revenger-shokunin
SM1=0 SM2=2 SM3=0 SM4=0 SM5=0 SM6=0
SELF_MISMATCH=2  exit=1
```

Not a label harm in a single-claim tree (C2-only below reads 0, because those files are absent), and it is
benign at the tip (both lines stay). It is still a line that belongs to two claims' labels, and §Separability
does not say so.

## F3 — COUPLING (undocumented, no label harm): `SKILL.md` is changed by all three claims in one block

`git diff 3f5edbc 17ee7f8 -- SKILL.md` adds one hunk (`@@ -283,6 +283,29 @@`) containing C3's `pin rule (round 70)` row,
C2's `self_assessment_check` field table, **and** C1's `lint_entry` field table (`kind | pre-flight lint (NOT a gate …; round 70 C1)`).
§Separability names only README lines as shared. No counter label reads `SKILL.md`, so this is documentation-only.

Negative result (a coupling I looked for and did not find): the repaired SHONEN box 1 no longer quotes SKILL.md
bytes — "size and digest are derived by piping that command to `wc -c` and `sha256sum`; none is quoted here, so
none can drift" (`SHONEN.md`, box 1, landed bytes) — so SM3 does not pin the combined SKILL.md digest and the
C2/C3 SKILL.md overlap creates no SM3 dependence. SM3=0 in the C2-only tree confirms it.

## Single-claim trees (the §Separability test as written)

```
C1-only (base gate + v5 entry + lint_entry + entry_checks + snapshots + SOURCES + README flip):
  C1_GATE=checked_blocks=24 problems=0 exit=0   C1_LINT=... exit=0   HOLDS_C1_V5=yes
  A1_C1=yes (A1_C1_DETAIL=distinct_commands=24 scripts_allowlisted=True readout_lines=15/15 source_rows_tier_a=7/7)
C2-only (base tree + self_assessment_check + SHONEN/SCORECARD + README repairs; C1/C3 files absent):
  SM1..SM6 = 0  SELF_MISMATCH=0  SELF_MUTANTS_KILLED=6/6  SHONEN_BOX_COUNT=4  README_ROWS=14  HOLDS_C2_V5=yes
  A1_C2=yes (base_vector=yes clean_variant=yes defect_variants=6/6)
  EMB_R68=checked_blocks=17 problems=7  HOLDS_C3_V1=no   (base gate; equals base value)
C3-only (gate + pin + derive_axml_anchors_r68.py + README line; C1/C2 files absent):
  EMB_R65=15/1 EMB_R67=16/0 EMB_R68=17/0 EMB_R69=17/0  EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1  HOLDS_C3_V1=yes
  A1_C3=yes   HOLDS_C2_V5=no (no checker; equals base value)   GATE_SELFTEST=exit 0  HOLDS_OK_V7=yes
```

So the letter of `claims.md:133` ("no claim's tree raises another claim's label above its base value") holds:
no single-claim tree raises a foreign label. It is insufficient — the predicates are read at the merged tip, and
that is where F1 bites.

## Dependences checked and cleared (reporting the negatives)

- **"C1's v5 entry running the hardened gate"** — not a dependence. With C3's hardened
  `check_embedded_outputs.py` reverted to base, the C1-only tree still prints
  `checked_blocks=24 problems=0`, `HOLDS_C1_V5=yes`, `A1_C1=yes`. The hardened gate and the base gate agree on
  this entry; C1 does not need C3 to land.
- **"A1 reading the base commit"** — not a cross-claim dependence. `measure-a1.py:94` archives the frozen base
  `3f5edbc` from `LANE`; the C2-only tree prints `A1_C2=yes` (`base_vector=yes`), and the base commit is
  pre-registration data, not another claim's landing.
- C2's landing does not move C1's labels (full candidate tree: `K_HELD_BACKED=8/14`, `C05_STATUS=uncovered`,
  `HOLDS_C1_V5=no` — base values). C3's landing does not move C1's or C2's labels (C3-only above; flip tree
  keeps `HOLDS_C3_V1=yes`). No hold is harmed in any tree (`HOLDS_OK_V7=yes`, `HOLD_REPLAY=10/10`,
  `GATE_SELFTEST=exit 0` in all four trees).

## Smallest safe correction

1. **Declare and execute the joint edit at the flip revision.** `claims.md` §Separability must state that the
   C1 flip revision also writes one current-state line into `SCORECARD.md` (C2's file), because SM6 reads the last
   `K_HELD_BACKED` line in that file. Verified correction on the flip tree:
   `printf '\nK_HELD_BACKED 9/14 (round-70 C05 admission; current state)\n' >> SCORECARD.md` →
   `SM6=0 SELF_MISMATCH=0` → `HOLDS_C2_V5=yes`, with `HOLDS_C1_V5=yes`, `HOLDS_C3_V1=yes`, `HOLDS_OK_V7=yes`
   unchanged. This is the minimum: no other frozen conjunct moves, and it is the only variant that is green at
   both tips (the `8/14 → 9/14` form and the candidate-tip `9/14` form both read SM6=1, shown above).
2. Optional, non-entangling, if the L1 prefers not to edit a C2 file inside C1's revision: re-anchor `sm6` on a
   current-state statement (e.g. a dedicated `K_HELD_BACKED_CURRENT` line, or the last `K_HELD_BACKED` line of
   the last `## Round N` section) **and** land a round-70 SCORECARD section with that line at the flip revision —
   anchoring alone does not fix it, because the last section at the flip tip is still round 69
   (`SCORECARD.md:612`), so the round-70 row must exist anyway. Any such change must be re-run through
   `measure-a1.py`'s base-vector leg (`SM6=0` on `git archive 3f5edbc`, currently green) before it is relied on.
3. If the round will not accept (1) or (2): the honest outcome is that C2's frozen predicate is false at the
   final tip and its kill rule fires (`claims.md:89`) — C2 falsified, not "separable". A `HOLDS_C2_V5=yes`
   printed on the pre-flip candidate revision does not satisfy the contract, which reads the final tip.

Scope note: I judge separability only. I did not form Q01-Q15 decisions and did not read
`.ufo/waves/round-70/w1/` before reaching this verdict.

Scratch: `/tmp/revenger-r70-R70W2SepCritic` (full, flip, c1only, c2only, c3only, sm2test, fix-*, fix2) — deleted
after writing this report. Tooling: nothing installed or upgraded; `python3` stdlib + the lane's own scripts only.
