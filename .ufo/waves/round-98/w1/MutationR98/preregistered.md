# MutationR98 — pre-registration (round 98, wave w1)

Written before `reports/round-98/mutants/mutate7.py` was run against any counter. Frozen
contract: `reports/round-98/claims.md` at lane commit `9d49002a3804de48d365b7d32849ada06745d64f`.
Source harness (read-only): `reports/round-97/mutants/mutate.py`. Port target:
`reports/round-98/mutants/mutate7.py` — same CLI (`--counter --out --kill-tree --selftest
--label --jobs`) plus `--profile {c02|c14}`.

## Operator set

Carried from v6, unchanged semantics: `cmp` (comparison operator inverted), `not` (boolean
`not` deleted in a decision), `if` (non-compare/non-not `if` test negated), `d-host`
(MutationR96's host-allowlist sub-check removal; anchor broadened to any
`if <name> not in <UPPERCASE-CONST>:` whose next line is a `fails.append` containing
`:host`, uniqueness still required — on the frozen v6 counter this matches exactly the
r97 anchor `if host not in HOST_ALLOWLIST:`).

New classes, instantiated only against the eight new v7 legs (`C1_ROWSET`,
`C1_ENTRY_BYTES`, `C1_HEADER_POSITION`, `C1_VERIFIED_AT`, `C1_VOTE_NOTES`,
`C1_OWNWORK_PATHS`, `C1_QUOTE_BYTES`, `C1_USEDBY_GROUNDED`), per leg L:

1. **del-leg-L** — the `legs["L"] = ...` assignment in `evaluate` is deleted (or, if it is
   the sole statement of an `if` arm, replaced by `pass`): the leg is never decided.
2. **widen-re-L** — every str-literal `re.match` / `re.fullmatch` / `re.search` pattern
   inside a function attributed to L is widened to `r"[\s\S]*"` (accept anything).
   Disclosed limitations: `re.sub`/`re.split` and module-level `re.compile` names are out
   of scope; a pattern already equal to the widening is a no-op and is skipped (reported,
   not counted). A regex that only shapes WHY text is excluded by the same message-slot
   rule v6 uses.
3. **inv-cmp-L** — not a new class: the carried generic `cmp`/`not`/`if` classes already
   produce one mutant per decision inside every function attributed to L (attribution is
   derived from the counter source, so renamed/new check functions are covered without a
   hard-coded map). Registered here so each new leg has an explicit inversion vector.
4. **drop-why-L** — the statement emitting `C1_L_WHY=` is deleted (or replaced by `pass`
   when it is a sole `if`-arm statement).

`--profile` is appended to the counter invocation of the `--tree` detector only when the
counter source contains the literal `--profile` flag (the v7 contract CLI); the frozen v6
counter has no such flag and is run without it. The operator set is profile-independent:
on v6 the new classes find no sites, so the V6R98 reproduction is within the same
operator set.

## Predicted killers, per new-leg mutant (pre-registered before any run)

- **del-leg-L**: killed by the tree detector on *any* tree — the `C1_L` verdict line
  disappears from the verdict set (or the counter crashes), which differs from the
  unmutated run. The self-test detector additionally kills it iff v7's self-test asserts
  a verdict naming `C1_L` (missing line or `KeyError` → rc ≠ 0). Prediction: killed by
  both detectors on any v7 that prints `C1_L`.
- **inv-cmp-L** (each `cmp`/`not`/`if` mutant in an L-attributed function): killed by the
  v7 self-test delta that names `C1_L` (the flipped sub-check must change that delta's
  verdict), or by the honest POS fixture if the flip breaks an honest-tree pass, or by
  the `c14`-profile tree detector on the claims-freeze archive, where every new leg fails
  at baseline (verdict-set change). Survival of any such mutant = a real sub-check gap
  (the r97 m029 / d-host / m059 / m061 / m079 class), recorded as a finding, never
  softened.
- **widen-re-L**: (a) if the regex gates acceptance (`not re.match(...)` → `fails.append`),
  widening makes the negative delta for L pass → killed by the self-test delta naming
  `C1_L`; (b) if the regex detects a reject-shape (`re.match(bad)` → `fails.append`),
  widening fails the honest POS fixture → killed by the self-test POS delta; (c) on the
  `c14` freeze tree C1_L fails at baseline, so a widened check that stops failing is
  killed by the tree detector.
- **drop-why-L**: **pre-registered expected survivor on both detectors.** Both detectors
  compare only verdict lines (`C1_<LEG>=pass|fail|n/m`, `C1_K_HELD_BACKED`, `C1_VERDICT`)
  and the exit code; WHY text is not instrumented. This class documents that gap (the v6
  "message-only" category made structural); it must not be read as a counter defect and
  must not trigger a contract change.

## Carried expectations

- **d-host**: r97 left it surviving the tree detector (`mutate-v6-kill.out`:
  `KILL_TREE d-host killed=False why=survived`) and killed by the self-test. The same
  split is predicted on v7 unless v7's self-test adds a self-consistent foreign-host
  receipt delta (r97 open question 2). Either outcome is recorded as observed.
- **C1_ONLY_C02 → C1_ONLY_TARGET rename**: attribution is derived, so the renamed leg is
  picked up without harness edits; r97's m002/m003/m004 (base_readme cmp/if) are predicted
  to survive the tree detector again if the same weak/WHY-only sub-check structure is
  retained, and to die on the self-test.
- A v7 leg decided without any comparison/`if`/`not` (pure `all`/`any`) is reported
  `NO_SITE`, not mutated (v6 precedent: `C1_TRIO`).

## Port calibration on frozen v6 (before any v7 run)

Frozen v6 counter `reports/round-97/c1_k_admit_counter6.py`
(sha256 `80c1f10b93ac9c3688c4dbd45286da7f08730b17b50930f5cb1d82dc4df3f2f4`), run as
`--label V6R98 --kill-tree <materialized git archive 7d380ce corpus reports .ufo>
--selftest`. Pre-registered reproduction targets, from the recorded r97 run
`reports/round-97/controls/mutate-v6-kill.out` (label `V6`):

- identical 140-site table: same mutant names, classes, functions, lines, legs labels and
  edit descriptions (byte-diff of the `MUTANT ` lines against the recorded run);
- `NO_SITE leg=C1_TRIO`; `EXCLUDED_MSG=7 (…): L345,L369,L429,L441,L460,L475,L501`;
- `BASE_TREE rc=1 verdicts=22`;
- `MUTANT_KILL_V6R98=107/140` with the same survivor set as `SURVIVORS_TREE` in the
  recorded run (d-host among them);
- `MUTANT_SELFTEST_V6R98=137/140`; `SURVIVORS_SELFTEST=m011-cmp-check_registry-L203,
  m029-cmp-check_votes-L253,m034-cmp-check_votes-L270`.

Any difference is reported in the findings file, never absorbed silently. A v7 dry run
(only if the work-in-progress counter exists during this seat's window) is sites-only —
no detectors, disclosed as such.
