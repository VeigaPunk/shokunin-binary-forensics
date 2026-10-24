CLEAN — round diff 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f..8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0 is additions-only: zero changed bytes under corpus/live or pre-existing corpus/fixtures, no README/QUALITY.md touched, rejected candidates untouched, SCORECARD/LOG/SOURCES pure tail appends.

Seat: R65CriticHarms — harms sweep over the round diff, read-only.
Measured at HEAD `8214e4d` (2026-10-24 02:54 -0300); `git status --porcelain` empty (no uncommitted edits in sweep).

## Check 1 — changed bytes under corpus/live or pre-existing corpus/fixtures: NONE

```
$ git diff 3eebcdd..HEAD -- corpus/live | wc -c
0
$ git diff --name-status 3eebcdd..HEAD -- corpus/fixtures
A  corpus/fixtures/apk-r65/fixture.apk
A  corpus/fixtures/apk-r65/generator.py
A  corpus/fixtures/apk-r65/readout.py
A  corpus/fixtures/apk-r65/truth.json
```

`apk-r65/` did not exist at base (all four paths status `A`); no pre-existing fixture path was modified. Void condition not met.
Fixture hash matches build-state claim: `sha256sum corpus/fixtures/apk-r65/fixture.apk` = `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, 947 bytes (diff header `Bin 0 -> 947 bytes`), consistent with SOURCES.md S041 row.

## Check 2 — touched README rows other than C05 candidate line: NONE

```
$ git diff --name-only 3eebcdd..HEAD | grep -ic 'readme\|quality'
0
```

`corpus/README.md` absent from diff entirely — the C05 row itself is untouched at HEAD, consistent with frozen admission order (claims.md:112-121: flip only on L1 all-criteria adjudication). No README file of any name changed.

## Check 3 — weakened Q01–Q13 text in QUALITY.md: NONE

`corpus/QUALITY.md` exists but is absent from the diff (grep above = 0). No byte of it changed, so no criterion text was weakened.

## Check 4 — edited retained rejected candidates: NONE

```
$ grep -rln 'admission-status: rejected' corpus/knowledge/
corpus/knowledge/evm-saved-interface-candidates.md
corpus/knowledge/commonjs-destructured-require-edges.md
```

Neither file appears in `git diff --name-status` output (only `A corpus/knowledge/round-65-apk-axml-byte-evidence.md` under knowledge/). Retained rejected candidates byte-identical to base.

## Check 5 — SCORECARD append-only: CONFIRMED

```
$ git diff 3eebcdd..HEAD -- SCORECARD.md
SCORECARD.md | 27 +++++++++++++++++++++++++++   (0 deletions)
  @@ -425,3 +425,30 @@   → pure tail append
base: 427 lines → head: 454 lines (+27, all trailing)
```

Appended block is the Round 65 section ("Round 65 (hyaku) — verified calibration guard, coverage candidate pending dispatch"). Same shape for the other modified files: `LOG.md` 888→903 (+15, `@@ -886,3 +886,18`), `corpus/SOURCES.md` 84→88 (+4, `@@ -49,6` — rows S038–S041 inserted at end of the `## Registry` table, before `## Paths` at line 57; correct placement, unlike round-64 E12). `SOURCES.md` row count consistent with claims census expectation (37 → 41 ≥ "38+").

## Whole-diff structural check

```
$ git diff --summary 3eebcdd..HEAD | grep -v '^ create'   → (empty)
$ git diff --name-status 3eebcdd..HEAD | grep -c '^[MDR]' → 3 (LOG.md, SCORECARD.md, corpus/SOURCES.md,
  corpus/verify_icon_languages.py, corpus/verify_multi_icon_states.py = 5 total M; no D/R/mode changes)
```

All changes are `A` (19 files) or `M` with 0 deletions (5 files). Only binary under corpus/ is the new fixture.apk. `git diff --stat` total: `23 files +7248 -0`.

## Adjacent observation (not a violation)

The two verifier-script edits are exactly the frozen C2 insertion shape: `@@ -152,6 +152,9` and `@@ -151,6 +151,9`, +3 lines each, placed inside `check()` immediately after the pre-existing forged-stdout control, transplanting the contracted real foreign evidence IDs (`ev_6e055…3d` languages; `ev_8ed88…21` multi), message ending `forged receipt evidence accepted`. `import copy` and `receipt_ok` pre-exist at base and are untouched. No finding; recorded for the mutant-attribution seats' context.

Scope note: sweep covers committed diff at `8214e4d` with clean tree. Edits landing after this snapshot (wave reports, L1's prospective C05 flip) are outside this measured state and were not observed.
