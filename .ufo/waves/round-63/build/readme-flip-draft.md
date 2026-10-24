# R63 README flip draft — C06 row (proposal only, not applied)

Proposal for the post-admission flip of the C06 coverage-map row in
`corpus/README.md` (file NOT edited by this seat). Apply only after the fresh
falsify wave's named Q01–Q13 pass decisions land and the entry file
`corpus/knowledge/round-63-zip-central-directory-evidence.md` is committed in
the same revision (claims.md admission order; `K_HELD_BACKED` reads the
knowledge cell, so the file must exist or the row does not back).

## Before (current, `corpus/README.md:35`, byte-exact)

```
| C06 | archives (ZIP inventory) | `knowledge/2026-10-12-rea-readiness-checklist.md` (archive-tool row only) | `fixtures/archive-r2`, `nested-r11`, `duplicate-r15` | partial |
```

## After (proposed replacement line)

```
| C06 | archives (ZIP inventory) | `knowledge/round-63-zip-central-directory-evidence.md` (manual byte-derived central-directory readout of `fixtures/archive-r2/fixture.zip` only; no general ZIP-parser, trailing-bytes, provider-completeness or authenticity claim) | `fixtures/archive-r2`, `nested-r11`, `duplicate-r15` | held |
```

### What changed in the line
- knowledge cell: pre-contract checklist citation replaced by the new admitted
  entry `knowledge/round-63-zip-central-directory-evidence.md` with a scope
  parenthetical in the row's existing style (C04/C09 round-62 precedent).
- work-evidence cell: **unchanged** (`fixtures/archive-r2`, `nested-r11`,
  `duplicate-r15`).
- status cell: `partial` -> `held`; line still ends `| held |`.
- No other map row is touched; denominator stays 14.

## Regex / counter check (frozen `reports/round-63/measure.py`)

Counter regexes used by the frozen probe and `corpus/SCORECARD.md`:
- row regex `^\| C[0-9]+ ` — matches the proposed line: **True**
- held regex `\| held \|$` — matches the proposed line: **True**
- status cell `line.rsplit('|', 2)[-2].strip()` -> `held`
- `knowledge/[\w.-]+\.md` in `split('|')[3]` ->
  `knowledge/round-63-zip-central-directory-evidence.md` (the only path in the
  knowledge cell)

Local simulation on the base README text (in-memory, repo untouched):
```
ROWCOUNT before/after: 14 14
K_HELD before/after: 6 7
after row matches row-regex: True
after row matches held-regex: True
after status cell: held
knowledge paths in cell: ['knowledge/round-63-zip-central-directory-evidence.md']
other rows identical: True
```

Frozen counter run on a scratch copy of the base `corpus/` tree with the
proposed line applied and a labeled scratch entry file present
(`/tmp/revenger-r63-readmeflip`, `TMPDIR` lane-owned, repo untouched):
```
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=7/14
FRESH_ROWS=18/18
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
PROBE_EXIT=0
```
`K_HELD_BACKED=7/14` counts the row only because the entry file exists in the
scratch tree; the same tree without the file yields `K_HELD=7/14` but
`K_HELD_BACKED=6/14` — a README flip without the committed entry is not backed.

## Ordering and scope notes for L1
1. Land the entry file (and its Q01–Q13 self-check) first, then the row flip,
   in the same revision.
2. Do not flip before the fresh falsify wave's named independent Q01–Q13 pass
   decisions land; claims.md makes the flip conditional on admission, and the
   probe measures existence, never quality.
3. The parenthetical scope is reconciled against the candidate's own
   `coverage-map:` header and `## Limitations` (round-62 finding F3). If the
   admitted entry's wording differs, the entry's wording wins verbatim.
4. C3 (calibration) and C2 (firmware F) do not require any other map row
   change: `corpus/README.md` carries no per-round firmware row text, and
   claims.md makes any status change other than C06 a void condition.
