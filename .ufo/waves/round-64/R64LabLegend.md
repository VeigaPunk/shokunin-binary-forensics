# R64LabLegend — legend-mismatch label, end-to-end probe

Seat: R64LabLegend (mutation-tester / lab). Round 64, v2 wave, lane
`/home/vgpnk/Projects/shokunin/revenger-shokunin`, base `666ea84b`.
Claim under test: `README_TOKEN_LEGEND_MISMATCH` is a live label — exactly 1 at
base with `rows=['C07']`, driven by evidence present in the tree, not a constant.

Verdict: **SURVIVED (label is live on all three prescribed points)** and two
definitional coverage findings recorded below. No contract change proposed.

## Probe environment

- Frozen counter: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py`
  `sha256=b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168`
  (unchanged before and after every run; read-only on the lane).
- Trees: `git archive 666ea84b6be2eec2b0359f556ba2429fc9044c36` extracted to
  `/tmp/revenger-r64-lablegend-{a,b,c,d,e,f,g}`; each run `cd /`,
  `TMPDIR=/tmp/revenger-r64-lablegend-tmp`, `python3 -B measure.py <tree>`.
  Each tree = 966 files. No run wrote inside the lane repo.
- All runs exit 0 (base `HOLDS_OK=yes`) and are deterministic: run A repeated
  byte-identical (see below).

## Required runs — relevant lines verbatim

### (a) pristine base archive `/tmp/revenger-r64-lablegend-a`

```
K_ROW C07 status=frontier
SAVED_RECORDS=59
README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']
F_COVERAGE=5/8 score=6.2
C4_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLDS_OK=yes
HOLDS_OK_V2=no
```

Exit 0. The entire log is **byte-identical** to the committed red-before
receipt: `sha256=8116b216d543984bfb60c6331defae43f384f5c94904658afb8997b8692a1003`
for both `/tmp/revenger-r64-lablegend-run-a.log` and
`reports/round-64/measure-before.log` (`diff` empty).

### (b) C07 `frontier` -> `uncovered` (`/tmp/revenger-r64-lablegend-b`)

Mutation: single line 36 of `corpus/README.md`,
`| C07 | firmware images | — | — | frontier |` -> `... | uncovered |`.
README sha256 `f583bd25...b7c01c` -> `d8d51238...af13d567`.

```
K_ROW C07 status=uncovered
SAVED_RECORDS=59
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
F_COVERAGE=5/8 score=6.2
HOLDS_OK=yes
```

Expected 0, observed **0**. The label is not a constant; the planned fallback
flip (`frontier -> uncovered` on C1 falsification) drives it to 0. `K_HELD`
stays 7/14 and `F_COVERAGE` stays 5/8 — the flip moves only the label, exactly
as the contract states ("K moves only on admission").

### (c) forged record with `operation: inspect_android_package`
(`/tmp/revenger-r64-lablegend-c`)

Mutation: new file
`corpus/live/runs/fake/forged-android-record.json` =
`{"operation": "inspect_android_package", "evidence_id": "EV-MUT-FAKE-0001",
"status": "ok", "tool": "mutant-probe", "normalized_result": {...}}`.
README untouched.

```
K_ROW C07 status=frontier
SAVED_RECORDS=60
README_TOKEN_LEGEND_MISMATCH=2 rows=['C05', 'C07']
F_COVERAGE=6/8 score=7.5
HOLDS_OK=yes
```

Expected: C05 enters the set. Observed **`rows=['C05','C07']`, count 2**. C05
is at `frontier` at base and `ROW_OPS['C05']={'inspect_android_package'}`, so
one saved record for its own surface op makes the row contradict the legend.
The entry ordering follows README row order (C05 at line 34 before C07 at 36).

## Restoration evidence

Both mutated trees restored in place, then compared to the pristine tree by full
manifest (sorted `sha256sum` of every file):

```
restored README (a, b, c): f583bd25ed7a367914cad82443b3c09126c3fb5102284898483cd28024b7c01c  (all three)
diff manifest-a manifest-b -> identical   (# 966 files each)
diff manifest-a manifest-c -> identical   (# 966 files each)
```

Detector re-run on restored bytes: b-restored and c-restored both print
`README_TOKEN_LEGEND_MISMATCH=1 rows=['C07']`, `SAVED_RECORDS=59`,
`K_ROW C07 status=frontier`, `HOLDS_OK=yes` — base state recovered exactly, and
the label's response is attributable to the mutation, not to ordering or
cache state. Heavy trees removed after hashing; logs kept at
`/tmp/revenger-r64-lablegend-run-*.log` (`-a`, `-a2`, `-b`, `-c`, `-d`..`-g`,
`-b-restored`, `-c-restored`).

## Boundary probes (label definition, same counter, same recipe)

| Tree | Mutation | SAVED_RECORDS | MISMATCH |
|---|---|---|---|
| a | none (base) | 59 | 1 `['C07']` |
| b | C07 -> `uncovered` | 59 | **0** `[]` |
| c | forged `inspect_android_package` record | 60 | 2 `['C05','C07']` |
| d | forged `inspect_managed_artifact` record | 60 | 2 `['C03','C07']` |
| e | malformed JSON `{not json at all` under `live/runs/fake/` | 59 | 1 `['C07']` (exit 0) |
| f | record with **only** `{"operation": "inspect_android_package"}` | 60 | 2 `['C05','C07']`, but `F_COVERAGE=5/8` |
| g | C07 -> `Frontier` (capital F) | 59 | **0** `[]` while `K_ROW C07 status=Frontier` |

- **d** — the ROW_OPS map is not C07-hardcoded: C03 (also `frontier`) enters on
  its own surface op. Surface scoping is per-row and general.
- **e** — a malformed record in `live/runs` is skipped, not a crash; the counter
  stays evaluable (exit 0). The `except (ValueError, UnicodeError)` guard is
  load-bearing in practice.
- **f (finding 1, definitional)** — the mismatch loop keys on
  `isinstance(x, dict) and x.get("operation")`, while `F_COVERAGE` additionally
  requires `evidence_id` and `normalized_result`. A bare
  `{"operation": ...}` therefore manufactures a legend "saved record" that is
  not a shaped saved record. Harmless for this round (the round's own record is
  fully shaped and `F` is presence-only by definition), but it means the label
  can be tripped by an unshaped dump. Recorded as a coverage finding only.
- **g (finding 2, robustness)** — the token compare is exact and case-sensitive
  (`cols[-1] == "frontier"`). `Frontier` at C07 yields
  `README_TOKEN_LEGEND_MISMATCH=0` while `K_ROW` prints `status=Frontier`: a
  one-character token change silently disarms the label. Base token is exact
  lowercase `frontier`, so base = 1 is sound; this is a future-drift exposure,
  not a defect at base. Not a contract change — flagged for the lesson M36 text.

## Role-signature note (honesty)

My first batch ran the pristine read and its mutation in parallel against the
same tree; the mutation landed first, so that pass actually measured the
combined b+c state (`rows=['C05']`, SAVED_RECORDS 60). It is discarded, not
reported as a run. All figures above come from isolated trees built afterwards
(`-a`/`-b`/`-c`), with the base run verified against the committed receipt.

## Findings for L1

1. `README_TOKEN_LEGEND_MISMATCH` is live at all three prescribed points; the
   claimed base value 1 `['C07']` and the "0 at round end" exit condition are
   both reachable by the frozen counter (b proves 0 is reachable by the declared
   fallback flip as well as by a `held` flip removing the row from the scan).
2. Finding 1 (unshaped record counts) and finding 2 (case-sensitive token) are
   label-definition observations; neither falsifies C1/C2 and neither changes
   the base reading. If the round wants M36 to name the exact scan predicate,
   its wording should say "a dict carrying a non-empty `operation`" rather than
   "a saved record", and note the token compare is exact.
3. No installs, no git/jj mutations, no writes outside the two scratch trees and
   this report; lane `measure.py` hash unchanged.
