SHARED-ARTIFACT-ACCEPTABLE — C2 is *not* verifiable in a world where C1's v2 file never landed (measured: `C7_V2_CLEAN=n/a` ⇒ `HOLDS_OK_V5=no`), but it *is* verifiable in every reachable round-end state, because the v2 file exists independently of C1's verdict (rejected candidates are retained, claims.md:65-66); the coupling is unidirectional (C2→C1's bytes), and `C7_V2_CLEAN` is a genuine calibration arm (the no-false-positive half of the gate) using C1's artifact as a shared input — disclosed: it also makes C2's verdict hostage to a defect inside C1's file.

# R67CriticSeparability — separability attack, counter side

Seat: R67CriticSeparability (critic) · scope: counter-side separability of C1 vs C2 under
AXES.md "causally separable — each verifiable without the others having landed"
(/home/vgpnk/Projects/shokunin/AXES.md:31-32). Counter: sha256
`7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e` (matches pinned value).
Method: `git archive HEAD corpus` into three /tmp scratch trees (`full`, `c2only`, `v2drift`),
frozen counter run per tree. Counterfactual trees are counterexamples, not measurements.

## Label dependency map (measure.py)

C1's predicate reads (all C1-side surfaces): `K_HELD_BACKED` (:37), `K_ROW C05` (:32-34),
`K_HELD_BACKED_STRICT` (:58), `README_TOKEN_LEGEND_MISMATCH` (:98), `C05_SINGLE_V2` (:64-67)
— plus wave-level Q/spot-check decisions outside the counter. **C1 reads no C7 label and no
gate byte** — counter-verified: C1's labels are functions of README rows + knowledge files
only.

C2's predicate reads: `C7_GATE_PRESENT` (:378 — C2's own file), `C7_SELFTEST` (:385-387 —
own file), `C7_CONTROL_PASS` (:388 — own bytes), `C7_MUTANT_KILLED_ATTRIBUTED` (:389-408 —
own file, mutated), `C7_RED_ON_R65_CANDIDATE` (:409-411 — r65 entry, pre-existing artifact,
not C1's), `C7_V2_CLEAN` (:412-418 — **C1's artifact, hardcoded path**),
`HOLDS_OK_V5` (:452-454 — `holds_ok_v4 ∧ c7_targets`, and `c7_targets` includes
`c7_v2_clean`).

## Counterexample 1 (demonstrated): C2 alone cannot print HOLDS_OK_V5=yes

Tree `c2only` = committed tip `7668510` with `corpus/knowledge/round-67-apk-axml-byte-evidence.md`
deleted (gate present, gate-side world identical to tip). Counter output:

```
C7_GATE_PRESENT=yes
C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
C7_V2_CLEAN=n/a (no v2 file)
C7_CONTROL_PASS=1/1
C7_MUTANT_KILLED=1/1   C7_MUTANT_KILLED_ATTRIBUTED=0/1
HOLDS_OK=yes  V2=yes  V3=yes  V4=yes  HOLDS_OK_V5=no
```

Every gate-property label is green (modulo the attributed defect below); the conjunction still
fails because measure.py:413-418 short-circuits `c7_v2_clean=False` on `not v2.is_file()`.
**Answer to the assigned question: no — C2 alone cannot print `HOLDS_OK_V5=yes`.**

## Counterexample 2 (demonstrated): a defect inside C1's artifact falsifies C2

Tree `v2drift` = tip with the v2 entry's correct 16-byte hex at its line 42 reverted to the r65
drift `4d616e696673742d56657273696f6e`. Gate itself byte-perfect; measured:

```
C7_V2_CLEAN=no exit=1 :: checked_blocks=16 problems=2
HOLDS_OK_V5=no
```

One byte-level defect *inside C1's deliverable* sinks C2's frozen predicate while every
gate-own label is green. C1's counter labels are unchanged (still 8/14, C05 uncovered — the
counter never runs the gate for K labels). This is doubly-attributed single-defect coupling:
the same corrupt bytes would fail C1's Q-attacks *and* C2's predicate — but under C2's verdict
the calibration column eats a coverage-side defect. Unidirectional: C1's verdict is never
affected by the gate (`C7_V2_CLEAN` is not in C1's predicate; the Q attacks are).

## Why acceptable anyway (verdict-level separability)

1. AXES.md's phrase is "verifiable without the others *having landed*" — the operative noun is
   the claim/verdict, not the artifact. Under the either-way order the v2 file exists in every
   reachable round-end state: kill branch retains it byte-preserved as `admission-status:
   rejected` (claims.md:65-66). So C2's verdict is determinable whether C1 passes or fails —
   in the failure state the gate just has to be measured over committed bytes that stay clean
   (they are: at tip `C7_V2_CLEAN=yes exit=0 checked_blocks=16 problems=0`).
2. Direction asymmetry: C1's frozen predicate contains zero C2-owned labels; C1 verifies with
   no gate at all. Entanglement that admits independent verification of one claim and
   conditional verification of the other is a shared input, not a mask — there is no state
   where a false C1 verdict props up a false C2 verdict or vice versa.
3. `C7_V2_CLEAN` is not gratuitous: a verbatim gate has two calibration arms — must fire on
   drift (`C7_RED_ON_R65_CANDIDATE`, verified: exit 1 naming entry:41, `problems=1`) and must
   *not* fire on a clean entry. The v2 entry is simply the chosen clean case. The residual
   defect is *choice of fixture*, not the arm itself: a gate-owned hermetic clean fixture (the
   self-test already builds one — `_self_test` clean/full entries, gate :118-137) would have
   made the no-FP arm C2-local. As designed, C2's pass imports an integrity assumption about
   C1's bytes. Under a strict artifact-level reading of "without the others having landed"
   this is ENTANGLED; I rule the verdict-level reading because the frozen predicate's
   either-way structure already guarantees the file exists whenever the counter runs.
4. Honest asymmetry disclosure for the report: claims.md:71-72's "causally separable … C2 adds
   one new file and touches no existing byte" is true only at the counter-visible `corpus/`
   boundary — the build commit `7668510` also edited `SKILL.md` (+21 lines, gate-registry row;
   `git show HEAD -- SKILL.md`), an existing file outside the `corpus` archive the counter
   reads. And at measurement level C2's conjuncts include a property of C1's bytes. Separable:
   yes at verdict level; no at strict artifact level. Report should say which.

## Smallest safe correction

None to the frozen predicate (it stands either way). If the wave wants the separability
sentence to survive a strict reading without a counterchange, the honest phrasing is:
*artifact-surfaces byte-disjoint inside `corpus/`; C2's verdict additionally depends on the
v2 file being present and drift-clean — a dependency satisfiable in every round-end state
because rejected candidates are retained.* Optional hardening (not required): point
`C7_V2_CLEAN` at a gate-owned fixture, or accept `n/a` as meeting the arm — both would
weaken the frozen counter, so leave it and disclose.

## Side evidence (observed, another seat's remit — not re-litigated here)

Committed tip measures `C7_MUTANT_KILLED=1/1` but `C7_MUTANT_KILLED_ATTRIBUTED=0/1`: the
mutant self-test's last line is `self-test: drifted entry not caught` (gate :132-134 require
fires before the MARKER require at :141, which is unreachable under the mutant). C2's
predicate needs 1/1 — C2 currently fails on its own artifact independent of C1. Pointer for
the C7 critic seats; I did not diagnose beyond the require-order read.

Tooling: none installed (stock python3/git/sed sufficient).
