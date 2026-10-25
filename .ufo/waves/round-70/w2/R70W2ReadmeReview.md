# R70W2ReadmeReview — non-author README review at 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd

README-TRUE — all five assigned README statements verify TRUE against the landed tree; no located defect.

Seat: R70W2ReadmeReview (wave 2, fresh; no w1 material read). Lanes: every target read at commit
`17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` (= `C` below) via `git show`/`git ls-tree`; base = `3f5edbc206351232a3d2d801334dd930499ccaf5`.
Preliminaries verified: all three pinned revs resolve (`git cat-file -t` → `commit` ×3); counters byte-match the frozen
hashes (`sha256sum reports/round-70/measure.py` → `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`,
`measure-a1.py` → `96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191`).

## Statement 1 — Index names every top-level corpus/ entry with a true one-line description — TRUE

- Tree: `git ls-tree --name-only C:corpus` → 24 entries (QUALITY.md, README.md, SOURCES.md, check_embedded_outputs.py,
  derive_axml_anchors.py, derive_axml_anchors_r68.py, embedded_output_pins.json, fixtures, knowledge, lessons,
  lint_entry.py, live, q15_tree_id_check.py, self_assessment_check.py, snapshots, 10× verify_*.py).
- Working tree unchanged during wave: `diff <(git ls-tree --name-only C:corpus) <(ls corpus)` → SAME.
- All 14 Index bullets (README:9-24) resolve to real entries. Description truth, per bullet:
  - `QUALITY.md` Q01–Q15, Q11 supersedes Q08 → see Statement 5. TRUE.
  - `SOURCES.md` "tiered, opened sources … search log": `git show C:corpus/SOURCES.md | grep -nE '^#+ '` →
    `## Registry` (table has `tier` and `opened` columns, :13), `## Paths` :65, `## Search log` :76. TRUE.
  - `knowledge/` "retains clearly marked rejected candidates (each carries `admission-status: rejected`)": scanned the
    header of every file — all four rejected candidates (commonjs-destructured-require-edges, evm-saved-interface-candidates,
    round-65/67/68/69-apk-axml) print `admission-status: rejected …`; admitted ones print `admitted`;
    `round-70-apk-axml-byte-evidence.md -> admission-status: candidate` (landing-order step 1 honored). TRUE.
  - `lessons/` → Statement 3. TRUE.
  - `fixtures/` "byte-oracle fixtures; `fixtures/REPLAY.md`": `git ls-tree C:corpus/fixtures` lists `REPLAY.md`. TRUE.
  - `live/runs/` "saved REA outputs, receipts and non-author reviews": run dirs `20261012T163909Z`… plus
    `promotion-review-r5.md`, `review-r1-r3.md`. TRUE.
  - `verify_*.py` "`--self-test`": exactly 10 matching files; `--self-test` literal present in spot-checked
    verify_pe_resources.py and verify_evm_evidence.py (1 hit each). TRUE.
  - `snapshots/`: contains exactly the four named files (APPNOTE.TXT, ResourceTypes.h, dex-format.html,
    rea-android-applications.md). TRUE.
  - `q15_tree_id_check.py` "`--self-test`, `--scan`": 2 hits each. TRUE.
  - `derive_axml_anchors.py` "prints the `ResourceTypes.h` line numbers and enum values an APK entry cites, from the
    pinned snapshot": docstring :1-20 — searches "the pinned AOSP `ResourceTypes.h` bytes for the symbol"; :18 "The
    snapshot it reads is committed at `corpus/snapshots/ResourceTypes.h`". TRUE.
  - `check_embedded_outputs.py` "`--entry`, `--self-test`; reads `embedded_output_pins.json`": flags 2 hits each;
    `PINS_REL = "embedded_output_pins.json"` at :39. TRUE.
  - `derive_axml_anchors_r68.py` "sha256 `bce497d6…`, pinned in `embedded_output_pins.json`":
    `git show C:corpus/derive_axml_anchors_r68.py | sha256sum` →
    `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`; pins JSON maps round-68 entry → this script with
    exactly that digest. TRUE.
  - `self_assessment_check.py` "classes SM1–SM6; `--root`, `--self-test`": docstring defines SM1-SM6 (:8-23);
    `--root` 4 hits, `--self-test` 2 hits. TRUE.
  - `lint_entry.py` "pre-flight lint … §Q-map completeness, Q14 byte-count heuristic, unresolved commit ids, header
    trio; not an admission gate": docstring :1-12 states exactly these four classes and "It is a pre-flight, not an
    admission gate". TRUE.
- Observation (not a defect, recorded for honesty): `embedded_output_pins.json` and README.md itself have no dedicated
  Index bullet; the pins file is named inside the `check_embedded_outputs.py` and `derive_axml_anchors_r68.py`
  descriptions. The checker's own SM2 class counts top-level `corpus/*.py` files and dirs, not the pins JSON, so this
  is consistent with the lane's own tooling.

## Statement 2 — Known gaps: AGENTS.md absent; SKILL.md carries a Gate registry — TRUE

- `git cat-file -e C:AGENTS.md` → `fatal: path 'AGENTS.md' does not exist in '17ee7f8…'`; same for
  `C:corpus/AGENTS.md`. ABSENT both. TRUE.
- `git cat-file -e C:SKILL.md` resolves; `git show C:SKILL.md | grep -n '## Gate registry'` → `272:## Gate registry
  (registry home; PROTOCOL.md §Gate standard)`. Registry rows (`| name |`, sed -n '272,$'): exactly
  `check_embedded_outputs` (:5 rel), `self_assessment_check` (:19 rel), `lint_entry` (:30 rel) — the three the bullet
  names. TRUE.
- "the ten `verify_*.py` replay verifiers are not registered gates": 10 verify_*.py files counted; no `verify_` name
  row in the registry; the registry's own family note (:14 rel) says the gate is "deliberately OUTSIDE the
  `verify_*.py` replay family: the ten-verifier census and `HOLD_REPLAY=10/10` denominator are frozen". TRUE.

## Statement 3 — lessons line: round-N.md + round-N-verifier-spotcheck.md for N in 61–69 — TRUE

- `git ls-tree --name-only C:corpus/lessons` → `2026-10-12-r1-provider-gap.md`, `round-1.md`,
  `round-1-verifier-spotcheck.md`, and for every N in 61-69 both `round-N.md` and `round-N-verifier-spotcheck.md`
  (23 files incl. `.gitkeep`), exactly the set the README:14 line describes; "the directory listing is the authority"
  is self-consistent. TRUE.

## Statement 4 — Coverage map untouched; C05 still `uncovered` — TRUE

- `git show C:corpus/README.md | grep -cE '^\| C[0-9]+ '` → `14` (rows C01-C14 at README:37-50); the file's own
  "Rows 14" claim (README:52) holds.
- `git diff 3f5edbc… C -- corpus/README.md | grep -cE '^[+-]\| C'` → `0`: no coverage-table row changed base→landed.
- C05 row (README:41): knowledge column `—`, status `uncovered`; `grep -o 'uncovered|held|partial|frontier'` on the
  row → `uncovered`. Round-70 entry header is `admission-status: candidate` (knowledge/ scan above) — landing order
  step 1 honored, README unflipped. TRUE.

## Statement 5 — QUALITY range Q01–Q15 — TRUE

- `git show C:corpus/QUALITY.md | grep -oE '^\| Q[0-9]+ '` → `Q01 Q02 Q03 Q04 Q05 Q06 Q07 Q08 Q09 Q10 Q11 Q12 Q13 Q14
  Q15` — all 15 rows present.
- Q11 row opens "`Supersedes Q08.`" (QUALITY.md:20 area, `| Q11 | Supersedes Q08. Each count, identifier, offset and
  digest …`). README:9's "`Q01–Q15 (Q11 supersedes Q08)`" is exact. TRUE. (Base README said `Q01–Q13`; that stale
  range is repaired in this landing, matching C2's SM1 fix.)

## Verdict and kill-rule relevance

**README-TRUE.** No FALSE statements; no located defect (no path:line + failing output to cite). This seat contributes
no falsifying input to C1's kill rule from the README axis, and corroborates the C2 mechanical conjuncts that touch
README prose (`README_ROWS=14`, SM1 range repaired, index coverage of top-level entries).

## Residual risk / verification gaps

- I verified SOURCES.md's description structurally (tier/opened columns, Paths/Search-log sections), not by reading
  every row; a stale row inside SOURCES is out of my assigned scope.
- The C05 work-evidence cell names only the round-65 retained candidate, while knowledge/ also retains round-67/68/69
  rejected candidates — the row is frozen-untouched by landing order, so in-scope this is an observation, not a
  defect; it is also covered by the row's per-round lesson pointers.
- Timing: report assembled ~6 min into the seat window; no dependencies on other seats; no scratch files created
  (nothing to clean under /tmp/revenger-r70-*).
