# MutationR92Counters — round-92 revenger, attempt 1 (report)

Mutated the two frozen counters (`reports/round-92/c1_k_admit_counter.py`,
`reports/round-92/c2_legend_counter.py`, freeze commit `9402183a`) with 28 one-line mutants,
built from copies in seat scratch (`/fast/scratch/hyaku/revenger-r92/MutationR92Counters/`,
deleted before yield). Full per-mutant diffs, deciding controls and demo evidence:
`Report: .ufo/waves/round-92/w1/MutationR92Counters/mutants.md` (same dir as this file,
subpath `MutationR92Counters/mutants.md`).

## Harness validation
Pristine counter copies (hash-identical to frozen: c1 `fe766d9…0f5`, c2 `47fa19d…943`) run
over control trees rebuilt from `git archive 9402183a` reproduce **all six frozen control
logs byte-for-byte** (`diff` empty; exits match). Frozen files, `claims.md`, `controls/*`
untouched (hashes re-verified after all runs).

## Result: 28 mutants — 5 KILLED, 23 SURVIVED (10 undetected on frozen controls)

C1 — 21 mutants (19 one-per-leg + 2 Q-set variants): **1 KILLED** (m18 verdict-gate
`ok=all(legs.values())`→`True`, flipped by base-do-nothing and junk-stub), 20 SURVIVED.
- Structural cause: do-nothing fails 10 legs, junk-stub fails 4 admission legs at once, so
  no single-leg drop flips a verdict; votes dir does not exist at freeze, so every
  vote-subcheck mutant (sha m08, role m09, distinct-seat m10, Q-set m11/m11b, Q-verdict m12)
  and the sources opened-date mutant (m15; stub's unregistered S999 masks the date conjunct)
  and the rows-total drop (m01) are output-identical to pristine on the frozen controls.
- m11/m11b additionally crash (`KeyError 'Q02'`) on any partial-decision votes tree — the
  pristine Q-set guard is what short-circuits before the Q-verdict guard; detection there is
  by crash, a clean pass requires co-dropping both guards (m11c, demo-killed).
- m02 (15→14) and m17 (K 9→8) flip legs in opposite directions on the two trees but never
  the verdict; they are killed automatically by the post-READY positive control.

C2 — 7 mutants: **4 KILLED** — n01 (rows-total→True, by c2-junk-deleted), n02 (15→14, by
c2-positive pass→fail AND c2-junk-deleted fail→pass), n05 (NO_UNBACKED→True, by
c2-junk-held), n06 (verdict gate, by all three must-fail trees). 3 SURVIVED:
- n03 (`C2_C08_CLEAR`→True): provably verdict-equivalent — C08 flagged ⟹ `C2_NO_NEW` also
  fails. The leg is redundant with NO_NEW at verdict level; no control can kill it.
- n04 (`C2_NO_NEW`→True): leg-detected on do-nothing only because C08_CLEAR masks the
  verdict; demo kill control verified: c2-positive + C07 `held→frontier` + planted
  `inspect_firmware_regions` record → probe flags C07 → pristine fail vs mutant pass.
- n07 (labels-missing `return 1`→`return 0`): undetected — no control breaks the probe.
  Violates the documented exit contract on the probe-crash path (demo: README-as-directory
  tree → pristine exit 1, mutant exit 0).

## Routed suggestions (demo-verified in scratch; NOT added to frozen controls)
1. Votes-bearing C1 junk stubs (one defect each: wrong sha / role executor / same seat twice
   / missing decisions / a FAIL decision) — each flips `C1_VOTES` fail→pass on the
   corresponding mutant (m08–m12, m11c). Demo outputs recorded.
2. Registered-source stub (planted S901 row, opened 2026-10-01) — isolates the opened-date
   conjunct: pristine `C1_SOURCES=fail` vs m15 `pass`.
3. Per-leg stubs for lint/embedded/sources (current junk-stub fails all four at once).
4. Post-READY positive + variants (14-row positive; positive minus admitted line / minus
   trio lines / with mangled C03 token) — kill m01–m07, m13–m17 bundles leg-isolating.
5. Probe-crash C2 junk control asserting exit≠0 when the probe emits no labels (kills n07).
6. NO_NEW-isolating C2 junk control: positive move + a non-C03 frontier-with-record row
   (kills n04).
7. n03: no control exists — `C2_C08_CLEAR` is logically implied by `C2_NO_NEW`; informational
   leg or drop.

## Integrity
No tooling installed; stock `python3`, read-only git only (`archive` to scratch). Lane writes
by this seat: this file + `MutationR92Counters/mutants.md` only. Scratch deleted. Observed
(not mine, live wave): `M SKILL.md` pre-existing; `M .gitignore` appeared during the run.
No defects found in the frozen counters themselves; findings are control-suite coverage gaps
plus one C2 leg redundancy — routed above, contracts unchanged.
