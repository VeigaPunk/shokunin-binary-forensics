# R70W1ConnSeparability — cross-claim file-overlap / separability scan (wave 1, advisory)

VERDICT: **SEPARABLE — with a split** (one required addition to the frozen §Separability list, below).

The three claims split cleanly into disjoint per-claim change sets **except for one counter-level coupling the frozen
§Separability text does not list**: C1's C05 flip moves C2's `SM6` label (SCORECARD K-statement vs README held rows),
so C1's change set must also carry one SCORECARD `K_HELD_BACKED` line append (9/14). With that append, every
single-claim tree keeps every other claim's labels at or better than base. No claim's change moves another claim's
label otherwise; C3's gate change is verified byte-transparent to C1's `C1_GATE` label.

---

## 1. Files each claim changes or names (from `git ls-tree` base `3f5edbc` vs candidate `aa1842fac`, + claims.md §Separability)

| Claim | Tree files changed | README lines | Counter labels it owns |
|---|---|---|---|
| C1 | `corpus/knowledge/round-70-apk-axml-byte-evidence.md` (new; v5), `corpus/lint_entry.py` (new), `corpus/fixtures/apk-r65/entry_checks.py` (new; the v5 entry's embedded commands run it) — **not** corpus top-level, so SM2-invisible | C05 row (line 34): knowledge col `—` -> `knowledge/round-70-apk-axml-byte-evidence.md`, status `uncovered` -> `held`; index bullet naming `lint_entry.py`; **+ SCORECARD K-line append (required, see §3)** | `K_HELD_BACKED`, `K_HELD_BACKED_STRICT`, `C05_*`, `V5_*`, `C1_GATE`, `C1_LINT`, `HOLDS_C1_V5` |
| C2 | `corpus/self_assessment_check.py` (new tool), fixes in SHONEN.md (SM3/SM4), SCORECARD.md (SM5 erratum), README index lines (SM1 Q-range, SM2 names) | line 9 `Q01–Q13` -> `Q01–Q15`; one index bullet naming `q15_tree_id_check.py`, `derive_axml_anchors.py`, `check_embedded_outputs.py`, `snapshots/`, `self_assessment_check.py` | `SM1..SM6`, `SELF_MISMATCH`, `SELF_CLEAN_FIXTURE`, `SELF_MUTANTS_KILLED`, `SHONEN_BOX_COUNT`, `README_ROWS`, `HOLDS_C2_V5` |
| C3 | `corpus/check_embedded_outputs.py` (gate learns pin rule), `corpus/embedded_output_pins.json` (new), `corpus/derive_axml_anchors_r68.py` (new, pinned copy) | one index bullet naming `derive_axml_anchors_r68.py` | `EMB_R65/R67/R68/R69`, `EMB_R68/R65_BYTES_UNCHANGED`, `EMB_PINNED_SCRIPT_IS_S046`, `EMB_PIN_MUTANT_KILLED_ATTRIBUTED`, `HOLDS_C3_V1` |

Base vs tip corpus deltas (`git ls-tree`): new at tip = `lint_entry.py`, `self_assessment_check.py`,
`derive_axml_anchors_r68.py`, `embedded_output_pins.json`, `knowledge/round-70-apk-axml-byte-evidence.md`.
`entry_checks.py` is NOT a corpus top-level file; it is `corpus/fixtures/apk-r65/entry_checks.py`.

## 2. Counter-label exposure matrix (which claim's change can move which label)

| Label | Computed from (measure.py / tool lines) | Moved by |
|---|---|---|
| `K_HELD_BACKED` (+_STRICT) | README rows 60-68 + existence of cited entry files | C1 only (flip + entry file). C2/C3 README edits must not touch C-rows or row count |
| `C05_*`, `V5_*`, `C1_LINT` | README C05 row / v5 bytes / `lint_entry.py` run (entry + tree-local QUALITY.md + `git cat-file` in LANE) | C1 only (C2's SHONEN/SCORECARD/README edits are not read by lint_entry.py; QUALITY.md read from the tree) |
| `C1_GATE` | `check_embedded_outputs.py` run on v5 (160-163) | C1 (entry bytes) **and C3 (gate bytes)** — see §3.1 for the verified transparency |
| `SM1` | README line 9 vs QUALITY.md max Q id (checker 55-61) | C2 only |
| `SM2` | README naming coverage of top-level `corpus/*.py` + `corpus/*/` dirs (checker 64-73) | C1 (new `lint_entry.py`), C2 (names), C3 (new `derive_axml_anchors_r68.py`) — each must name its own new top-level artifacts |
| `SM3`, `SM4` | SHONEN.md only (90-111) | C2 only |
| `SM5` | SCORECARD.md cites from `## Round 61` + erratum (114-134) | C2 only (C1's K-line append must cite resolving hashes or none) |
| `SM6` | last `K_HELD_BACKED` SCORECARD line's `N/14` vs README held rows (137-145) | **C1 (flip) — the coupling the frozen split omits** |
| `SHONEN_BOX_COUNT`, `README_ROWS` | SHONEN.md / README row count (196-198) | C2-owned; C1 flip and C2/C3 line edits preserve count (verified) |
| `EMB_R65/R67/R68/R69` | `check_embedded_outputs.py` runs on the four retained entries | C3 only (gate + r68 pin). C1 does not touch these entries or the gate. Verified base-gate == modified-gate on r65/r67/r69 (below) |
| `EMB_*_BYTESESCHANGED`, `EMB_PINNED_SCRIPT_IS_S046`, `EMB_PIN_MUTANT_...` | entry sha256 / r68-script sha256 / pin-tamper run | C3 only |
| `HOLDS_OK_V7` (HOLD_REPLAY, GATE_SELFTEST, F_COVERAGE, FRESH_ROWS) | verify_*.py runs, gate self-test, live/runs json, 2 fixed knowledge files | no claim |

## 3. Overlaps found (file-level) and the resolution

### 3.1 Overlap 1 — `corpus/check_embedded_outputs.py` is C3's tool AND C1's `C1_GATE` engine (and C2 names it in README)
Three claims touch this one file's *surface*, but on disjoint dimensions: C3 changes its bytes; C1 consumes it; C2 only
names it in README (SM2). The danger is C3's change moving `C1_GATE`. Evidence that it cannot:

- Pins are keyed by entry basename (`load_pins`, gate 86-95): `embedded_output_pins.json` keys = `['round-68-apk-axml-byte-evidence.md']`; v5 is absent.
- `apply_pin` returns the command unchanged when the entry has no pins (103-104). For v5, pins={} → every command byte-identical to base behavior.
- Direct run, full candidate tree (candidate commit `aa1842fac` corpus + SHONEN/SCORECARD/SKILL):
  - base gate `3f5edbc`: `checked_blocks=22 problems=0`
  - modified (C3) gate: `checked_blocks=22 problems=0`
  → `C1_GATE` is identical under both gate versions.
- Same full tree, base gate vs modified gate on the retained entries (modified gate = C3 tree):
  - r65: `checked_blocks=15 problems=1` (both), r67: `16/0` (both), r69: `17/0` (both); r68: base `17/7`, modified `17/0` (the claimed pin effect, applied only to the pinned r68 entry).
  → C3's change moves only `EMB_R68`, exactly as claimed; r65/r67/r69 labels unchanged.

### 3.2 Overlap 2 — README.md touched by all three claims (disjoint lines; row-count invariant)
- C05 data row (line 34) belongs to C1 alone. Verified base and tip row 34 are byte-identical (`uncovered`), i.e. the
  flip is still pending — C1 owns the only edit to that row.
- Q-range line (line 9, `Q01–Q13`) belongs to C2 alone (SM1).
- Index/naming bullets: C1 adds `lint_entry.py` naming; C2 adds the five-name bullet; C3 adds the `derive_axml_anchors_r68.py`
  naming. All are new additive bullets — no contention.
- `README_ROWS=14` invariant: rows match `^\| C[0-9]+ `; C05 flip edits columns in place, the C2 fix edits a prose
  bullet, naming bullets are prose (`- ...`). Row count unchanged in every single-claim tree.

### 3.3 Overlap 3 (the one real coupling) — `SM6` moves with C1's flip (SCORECARD.md)
Checker `sm6` (self_assessment_check.py 137-145) compares the last SCORECARD line naming `K_HELD_BACKED` against the
README held-row count. Simulated on the base tree + tip checker:

- base (C05 `uncovered`, held=8, SCORECARD last K line 8/14): `SM6=0`.
- apply only C1's flip (C05 → held, held=9, SCORECARD unchanged): **`SM6=1`** → `SELF_MISMATCH` 9 → 10 — C1's
  tree raises C2's label above base.
- apply C1's flip + one appended SCORECARD K row ending `9/14`: `SM6=0` again.

The flip is the only C1 change that moves a C2 label. Note C2 cannot carry the fix: in C2's own tree held=8, so a
9/14 line would make `SM6=1` there. The minimal split therefore assigns the SCORECARD K-line append **to C1** (a new
final ledger row, e.g. `| coverage — knowledge-map ground K | 8/14 -> 9/14 ... |`), disjoint from C2's SM5 erratum
region (SCORECARD.md line 557 area). The appended row must not introduce unresolving hex cites after
`pre-registration|base|tip|commit` (would add an SM5 count); citing resolving commits only, or no hash.

### 3.4 Overlap 4 — `snapshots/` naming (SM2) is C2-owned
Base SM2 missing set (probe on base tree, exp the checker copy): `py:check_embedded_outputs.py`,
`py:derive_axml_anchors.py`, `py:q15_tree_id_check.py`, `dir:snapshots/` — exactly the four of the Before state
(SM2=4). C1 does not need to name `snapshots/` for its own labels; leaving that bullet to C2 keeps C1's tree at base
SM2 (adding it would only improve, never harm). C1 must name its own new top-level py (`lint_entry.py`) or SM2 → 5
in C1's tree; same for C3 (`derive_axml_anchors_r68.py`). Verified: adding the five-name bullet + Q-range fix drops
SM1→0, SM2→0 (SM3/SM4/SM5 remain, belonging to C2's SHONEN/SCORECARD edits, not simulated here).

### 3.5 Overlap 5 — `entry_checks.py` is a fixture script, not corpus top-level
The v5 entry's embedded commands run `python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest/--pins`;
that file is part of C1's change set (absent at base). It is under `fixtures/`, so SM2 does not require naming it.
C1's tree must carry the full `corpus/fixtures/apk-r65/` tree or `C1_GATE` will report `command exited 1/2` problems
(observed in sandbox before the fixture extraction; clean after).

## 4. Minimal per-claim split (keeps every single-claim tree's labels ≥ base)

1. **C1**: C05 row 34 (knowledge col + status); index bullet naming `lint_entry.py`; files `lint_entry.py`,
   v5 entry, `fixtures/apk-r65/entry_checks.py`; **and one SCORECARD `K_HELD_BACKED` row append ending `9/14`**
   (required — §3.3). No other README line, no SHONEN change, no other SCORECARD change.
2. **C2**: README line 9 `Q01–Q15`; five-name index bullet; SHONEN box fixes (SM3/SM4); SCORECARD SM5 erratum.
   No C-row edit, no row add/drop.
3. **C3**: index bullet naming `derive_axml_anchors_r68.py`; gate bytes; `embedded_output_pins.json`;
   `derive_axml_anchors_r68.py`. No README row edit, no SHONEN/SCORECARD change.

All three keep `README_ROWS=14` and `SHONEN_BOX_COUNT=4`; `HOLDS_OK_V7` is untouched by all three.

## 5. Risks / residuals
- The frozen §Separability list omits the SM6/SCORECARD coupling; if the C1-only W2 tree is built exactly per the
  frozen list (no SCORECARD append), its `SELF_MISMATCH` computes 10 vs base 9 → that tree fails an
  at-or-better-than-base audit. The append closes it. (Advisory; wave-1 findings are not kill-rule inputs.)
- C1's appended SCORECARD row must satisfy SM5 (resolving cites only) — trivially met by citing `3f5edbc` (resolves)
  or no hash.
- Full-final-tree merge: C1's SCORECARD append and C2's erratum touch disjoint lines; C1's README bullet and C2's
  bullets are separate lines; no textual conflict.
- `C1_GATE` equivalence was verified on the full candidate tree with both gate versions (22/0 both); the sandbox run
  that required the apk-r65 fixture extraction shows C1 must carry that fixture in its tree.
