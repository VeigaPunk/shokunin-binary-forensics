# ExecR91BatteryX — battery/mutant cross-check (round 91, C1)

**Seat:** ExecR91BatteryX (leaf, read-only over frozen artefacts).
**Lane:** /home/vgpnk/Projects/shokunin/revenger-shokunin
**Frozen base:** b13aac756ac33aa5245c13966c624de4370206d0; lane HEAD at read time d509e982844d31bd26f3cb96e1a663e7d36f2ca8.
**Table:** `.ufo/waves/round-91/w1/ExecR91BatteryX/crosscheck.log` (266 lines; 21 label derivations, 11 mutant rows).

Frozen hashes at read time: battery `22ce984f…98daf4`, mutants `bde07efc…f652ba`, claims `fca9b5d3…0f36cf`.

## Method

- Wrote an independent six-step implementation of claims.md §C1 (`hand_derive`) from the prose, not from `mutants.py`, and re-derived all 21 labels from the fixture text.
- Imported `sm6_battery_v3.CASES`, `mutants.MUTANTS`, `mutants.reference` in-process; built each case with `sm6_battery_v3.build()` in a private scratch temp dir; scored `reference` and all 11 mutants.
- Scored 11 additional single-element probe implementations (each breaking one rule element) to find elements no case can see.

No mutating git, no writes outside the two named wave paths. No tool installed.

## Results

| item | measured |
|---|---|
| labels re-derived as forced | **21/21** (0 unforced) |
| `mutants.reference` vs battery | **0/21** mismatches |
| mutants killed | **11/11** |
| declared kill case wrong in docstring | **none** (11/11 declared cases do kill their mutant) |
| sole killers | B09→M08, R06→M09 |
| identical kill signatures | {B01,B11,R01} (none killed); {B08,R07} (M02,M03,M11) |

Every case's forcing substring is quoted in the log (e.g. B04 `8/14 → 8/15` right side; R04 cell[2] `8/15 (5.3) → 8/15 (5.3)` with the pointer cell's `9/15` outside the region; R06 cell[2] `2.9 → **4.3**` carries no N/D → step 5).

## Disagreements (reported, not edited — frozen files)

1. **Battery docstring provenance is false for R01/R02** (`sm6_battery_v3.py` docstring says "verbatim SCORECARD lines 693 and 667"). Both are truncated: R02 drops `; \`C15_TOOL_ROWS\` 0/18 → 18/18; C15 \`uncovered\` → \`uncovered\`` from cell[2], shortens the pointer cell/hashes/verdict; R01 drops `; the round-73 C10 claim is now falsified-closed, not carried`. Scoring the full rows in-process keeps both labels 0 and the same mutant kill sets — provenance defect, not a mislabel.
2. **`reports/round-91/mutants.reference` is not a file.** The rule in code is `mutants.reference()` inside `reports/round-91/mutants.py`; that function scored 0/21.
3. **M02 and M03 are indistinguishable on this battery** — both kill exactly {B04,B05,B07,B08,R02,R03,R05,R07,R09}. Both die, so the frozen predicate holds; the battery just does not separate "left side of arrow" from "first raw N/D in region".
4. **Eight rule elements have no discriminating case** (probe evidence in log §2): step-1 last-line selection (`P_first_kline` 0/21); step-2 `>=5` threshold (`P_cells_thresh_3` 0/21) and trailing-`|` condition (`P_startswith_only` 0/21); step-3 STRICT truncation — inert, `P_no_strict_split` 0/21; score-before-pair reading of step 4a (`P_score_before_pair` 0/21); step-4b `last` (`P_non_token_first_group` 0/21) and its right-side preference (`P_non_token_left_side` 0/21); step-6 coverage-map/held anchoring (`P_rows_any_table_line` 0/21). A v3 implementation could break any of these and still score 0/21; no frozen mutant depends on them, so C1's predicate is unaffected.
5. **R02 is load-bearing**: it is the sole killer of both "last group after token" (`P_last_group_after_token`) and "whitespace-only skip" (`P_ws_only_skip`).

## Redundancy

- B01: no unique discrimination and no unique rule path — redundant as a discriminator (canonical positive baseline only).
- B11: its only distinctive text (`K_HELD_BACKED_STRICT`) is inert under every mutant and probe — redundant for discrimination, retained as syntactic witness of step 3.
- B08 vs R07: identical kill signatures; one of the two is redundant as a discriminator.
- Not redundant: R01 (only case reaching step 4b), B09/R06 (sole killers), R02 (see above).

## Blockers

None. Nothing in the frozen predicate is contradicted by the measured data; the defects above are provenance/coverage, not label errors.
