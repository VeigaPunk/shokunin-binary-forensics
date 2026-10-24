NOT-FALSIFIED — the C05 `frontier → held` flip has an exact contract-and-legend-consistent edit (one coverage-map row, `naming only the new entry`, plus mandatory removal of the `## Frontier` C05 bullet); two pre-existing staleness defects of the same class are already at base (C07 `## Frontier` bullet, C07 `—` work-evidence cell) and must not be reproduced for C05.

## 1. Exact edit required on admission (all-criteria Q01–Q13 pass)

File: `corpus/README.md`. Claims contract: `reports/round-65/claims.md:25-27` — C05 flips "`frontier → held` naming only the new entry"; "No other README row changes" (`:28`); admission order `claims.md:118-121` (L1 flips, same revision as the Gate decision).

### 1a. Coverage-map row — `corpus/README.md:34`

Current:

```
| C05 | Android packages (APK) | — | — | frontier |
```

Replacement (shape follows admitted-sibling rows C06 `:35` / C07 `:36` / C09 `:38`: entry path + parenthetical scope fence in the knowledge cell, fixture in the work-evidence cell):

```
| C05 | Android packages (APK) | `knowledge/round-65-apk-axml-byte-evidence.md` (manual byte-derived readout of `fixtures/apk-r65/fixture.apk` — container members, binary-AXML `AndroidManifest.xml`, `classes.dex` declared header — only; no install/signature, dex-validity, provider or authenticity claim) | `fixtures/apk-r65` | held |
```

Notes:
- "naming only the new entry" binds the knowledge cell: exactly `knowledge/round-65-apk-axml-byte-evidence.md`, nothing else (no `seed.md`, no second entry).
- Work-evidence cell `—` → `fixtures/apk-r65` is required by the legend's own definitions (`README.md:25-26`: "fixture and run records stay in `fixtures/` and `live/runs/`" = work evidence) — the fixture exists and is the entry's substrate. Leaving `—` after `held` reproduces C07's live defect (see §3). The contract names only the status flip and the entry; filling this cell is legend-mandated, not contract-forbidden.
- Counter parse: `reports/round-65/measure.py:31` requires the line to end `| held |`; `K_ROW C05` (`:33-35`) reads the last cell — any of `held`/`uncovered`/`frontier` parses.
- `K_HELD_BACKED` (`:36-37`) requires `knowledge/…` paths in the knowledge cell to exist — `corpus/knowledge/round-65-apk-axml-byte-evidence.md` is committed (header read, `admission-status: candidate` at `:7`). `K_HELD_BACKED_STRICT` (`:43-54`) only decrements on `admission-status: rejected` — `candidate` does not decrement. 9/14 follows automatically on the token change.

### 1b. `## Frontier` section — remove the C05 bullet, `corpus/README.md:69-70`

Current:

```
- C05 Android — REA `inspect_android_package`; jadx 1.5.6 is present; needs an
  authored APK fixture.
```

On admission this entire bullet must be deleted. The section header (`README.md:61`) scopes the list to "Ground being explored and not yet held, nearest first" — a `held` C05 contradicts the section's own predicate (exactly the M36 class, §3). "No other README row changes" binds table rows only; the Frontier bullet is not a coverage-map row, so removal violates nothing.

## 2. Falsification branch (`frontier → uncovered`, `claims.md:27`)

- Row edit: `| C05 | Android packages (APK) | — | `fixtures/apk-r65` | uncovered |` — the legend (`README.md:24-26`) defines `uncovered` as "work evidence exists but no admitted knowledge entry," and `fixtures/apk-r65` is committed work evidence; the `—` evidence cell would itself contradict the token.
- If the rejected candidate is retained under `knowledge/` (like C04's `commonjs-destructured-require-edges.md`), follow the C04 row's own convention (`README.md:33`): name `retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md`` in the work-evidence cell — "a rejected candidate … is evidence, not coverage" (`README.md:24`).
- `## Frontier` bullet: `uncovered` is still "not yet held," so the C05 bullet may stay — but the clause "needs an authored APK fixture" is then factually stale (the fixture exists). Rewrite required either way, e.g. "authored APK fixture `fixtures/apk-r65` exists; the round-65 entry was rejected at the Q-gate — a fresh fixture or re-entry is the next probe."

## 3. Other README text that goes stale by the legend's own rules (M36 class)

M36 = "the coverage-map token `frontier` contradicted the legend's own definition" (`corpus/lessons/round-64.md:182`); registered counter `README_TOKEN_LEGEND_MISMATCH` compares `frontier` tokens against `live/runs` operations only (`measure.py:63-86`, `ROW_OPS` C05 = `{inspect_android_package}`).

- **Counter blind spot (observed):** no `live/runs/*.json` carries `operation=inspect_android_package` — grep over `corpus/` hits only `README.md:69`, `SOURCES.md:53`, the entry (`:2, :6, :131, :135`) and lessons. So `README_TOKEN_LEGEND_MISMATCH` stays `0` under either flip and **cannot detect** fixture-cell or Frontier-prose staleness; those are legend-text obligations the counter does not see. (Same blind spot let M36-class drift survive C06/C07.)
- **Already stale at base — C07 `## Frontier` bullet** (`README.md:63-66`): C07 row is `held` (`README.md:36`) yet its Frontier bullet remains under "not yet held" — the same defect this wave must not commit for C05. Routed debt: `corpus/lessons/round-64.md:248` (`(d) ## Frontier C07 prose goes stale after the flip … L1 debt`), `corpus/lessons/round-64-verifier-spotcheck.md:78` item 3.
- **Already stale at base — C07 work-evidence cell `—`** (`README.md:36`): `corpus/fixtures/firmware-r63/` exists (directory listing, this read) and the C07 entry itself cites it — fixture records are work evidence per `README.md:25-26`. The `—` contradicts the column's own convention. C05's flip must not copy this.
- **`admission-status: candidate` marker**: on admission, the entry's `candidate` header (`round-65-apk-axml-byte-evidence.md:7`) left in place reproduces the exact M36-shaped drift already live for C06 (`round-63-zip-central-directory-evidence.md:8`) and C07 (`round-64-firmware-region-byte-evidence.md:6`), flagged MEDIUM-4 in `.ufo/waves/round-64/R64ReviewEntryQ01.md:109-119`. Clean precedent: round-62 entries carry `admission-status: admitted — recorded round-62 Gate decision…` (`round-62-commonjs-require-name-evidence.md:6`, `round-62-evm-dispatch-byte-evidence.md:21-23`). The STRICT counter does not penalize `candidate` (scans for `rejected` only, `measure.py:43-53`), so this is a textual-drift finding, not a count blocker — but leaving it reproduces a named defect.
- **`## Index` `lessons/` bullet** (`README.md:14`): names lessons only through `round-61.md` — rounds 62-64 already absent at base; the omission is pre-existing and non-exhaustive by convention, no new staleness this round.
- **`## Known gaps`, C03/C08/evidence-custody Frontier bullets, `## Index` `knowledge/` bullet**: unaffected by the flip — `knowledge/` bullet (`README.md:11`) is satisfied once the map names the new entry.

## 4. Minimal edit summary (admission)

Two contiguous regions of `corpus/README.md`, nothing else: (a) rewrite row `:34` per §1a; (b) delete the two-line C05 bullet at `:69-70`. Everything else stays consistent; no other row's status, the legend sentence, the census footer, `## Known gaps`, or `## Index` needs touching. If the seat also honors the legend's own rules beyond the letter of the contract, the C07 Frontier bullet (`:63-66`) is the one unowned pre-existing staleness item — flag to L1 as round-64 routed debt, not this claim's edit scope ("No other README row changes" arguably shields it anyway).

## Evidence index

- `corpus/README.md:21-26` (legend), `:34` (C05 row), `:35-36` (C06/C07 held shapes), `:61,:63-70` (Frontier section + C07/C05 bullets), `:14` (lessons bullet), `:11-13` (knowledge bullet).
- `reports/round-65/claims.md:19-30` (C1), `:110-123` (frozen admission order).
- `reports/round-65/measure.py:28-54` (K parsing/strict), `:56-60` (selftest), `:63-86` (ROW_OPS + mismatch).
- `corpus/knowledge/round-65-apk-axml-byte-evidence.md:6-7` (coverage-map C05; `admission-status: candidate`).
- `corpus/lessons/round-64.md:182` (M36 row), `:248` (routed C07 Frontier staleness); `corpus/lessons/round-64-verifier-spotcheck.md:78` (debt item 3).
- `.ufo/waves/round-64/R64ReviewEntryQ01.md:109-119` (candidate-marker MEDIUM-4 precedent).
- Grep evidence: `inspect_android_package` absent from `corpus/live/runs/**` (only prose/doc hits); `corpus/fixtures/firmware-r63/` present (glob listing).

Confidence: high on the row edit (contract + counter + sibling-shape triangulate); high on the Frontier-bullet removal (section's own predicate); medium on the `—` work-evidence cell being legend-required rather than merely conventional (contract is silent; C07 shows the alternative shipped anyway). Remaining unknown: whether L1 keeps the rejected candidate on falsification — the C05 uncovered-row cell wording depends on it (§2).
