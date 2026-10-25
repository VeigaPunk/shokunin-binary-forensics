# R69ReadmeFlipCheck — README C05 row + C1 flip preconditions on current bytes

**NOT-MET — the flip is barred twice over. (a) Three wave Q decisions on the v4 bytes
have landed as FAIL (Q07 `R69ReviewEntryQ07.md:1`, Q14 `R69ReviewEntryQ14.md:1`, Q15
`R69ReviewEntryQ15.md:1`), so §C1's all-pass conjunct is already false and the kill
rule fires: the C05 row stays `uncovered`, the v4 entry becomes `admission-status:
rejected`, and C1 is reported FALSIFIED. (b) Independently, the frozen counter
`reports/round-69/measure.py` (sha256 `bca74e6d…`, the pinned hash) dies with
`NameError: name 'run' is not defined` on **every** tree carrying the round-69 Q15
checker, so it never prints `C7_V4_CLEAN`, `HOLD_CALIBRATION`, `HOLD_REPLAY` or
`HOLDS_OK_V4/V5/V6` and exits 1 — the "counter exit code is 0" conjunct cannot be
satisfied at all.** C2 is additionally blocked because `corpus/lessons/round-69.md`
(required for `Q15_RESTATE_OK=yes`, and already cited by `corpus/QUALITY.md:27`) does
not exist.

- seat: `L1Revenger69.R69ReadmeFlipCheck` (independent leaf; no subagent dispatch)
- date: 2026-10-25 · lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`
- contract read first: `reports/round-69/claims.md`, `reports/round-69/measure.py`,
  `reports/round-69/measure-before.log`
- **no edits**: this seat wrote only this report and `/tmp/revenger-r69-flip/*`
  (scratch, deleted at return). No git write of any kind. Nothing flipped.
- tools installed/updated: **none** (standing `python3` 3.14, `git`, `tar`,
  `sha256sum`; pacman paused host-wide, no transaction attempted)

## 1. README C05 row — exact text and status cell

`corpus/README.md:34` (no trailing whitespace; em dash U+2014 in the knowledge column):

```
| C05 | Android packages (APK) | — | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (round-65 orchestrator-dispatched wave, falsified Q02/Q06/Q11, adjudicated round-66) | uncovered |
```

Columns per the header at `corpus/README.md:28` (`| row | surface | knowledge entries | work evidence | status |`):

| column | value |
|---|---|
| row | `C05` |
| surface | `Android packages (APK)` |
| **knowledge entries** | `—` (em dash — **not** the round-69 entry) |
| work evidence | `` `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (…) `` |
| **status cell** | **`uncovered`** |

The round-69 v4 entry exists and is marked `admission-status: candidate`
(`corpus/knowledge/round-69-apk-axml-byte-evidence.md:11`), exactly as §C1 requires
at build time ("the README C05 row is **not** flipped at build time"). So `uncovered`
is *correct and intended* right now; it is not a defect — but it is also not a flip.

## 2. Counter run — labels, verbatim, per commit

Invocation exactly as frozen (`claims.md` §Frozen counter): `git archive <commit>
corpus | tar -x -C <tree>`, then `cd / && TMPDIR=… python3 -B
reports/round-69/measure.py <tree>`.

| commit | role | exit | last labels printed | crash |
|---|---|---|---|---|
| `222a7a7` | base / red-before | **0** | `Q15_PRESENT=no`, `Q15_SELFTEST=n/a (no checker)`, `C7_V4_CLEAN=n/a (no v4 file)`, `HOLDS_OK_V6=yes` | none |
| `e1d22ca` | pre-registration | **1** | `Q15_PRESENT=no` | `NameError` @ `measure.py:158` |
| `da02261` | build | **1** | `Q15_PRESENT=yes` | `NameError` @ `measure.py:158` |
| `35e1258` | main tip (wave prep) | **1** | `Q15_PRESENT=yes` | `NameError` @ `measure.py:158` |

Tip run (`refs/heads/main` = `35e1258`), labels before the crash, verbatim:

```
K_HELD=8/14 score=5.7
K_ROW C05 status=uncovered
K_ROW C07 status=held
K_HELD_BACKED=8/14
C05_REJECTED_MARKED=yes
K_HELD_BACKED_STRICT=8/14
C05_KNOWLEDGE_COLUMN=-
C05_SINGLE_V2=no
C05_SINGLE_V3=no
C05_SINGLE_V4=no
STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True
SAVED_RECORDS=59
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
C05_STATUS=uncovered
HOLDS_C2_V3=no
HOLDS_C2_V4=no
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
Q15_PRESENT=yes
Traceback (most recent call last):
  File "/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
               ^^^
NameError: name 'run' is not defined
EXIT=1
```

### 2.1 Defect F — `run` is used before it is defined (fatal, blocks the whole gate)

- call site: `reports/round-69/measure.py:158` — `rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")`
- definition: `reports/round-69/measure.py:187` — `def run(tree, script, *args):`

Python executes top-down, so at line 158 `run` does not exist. The Q15 branch is
entered whenever `TREE/corpus/q15_tree_id_check.py` exists — i.e. on **every** commit
from `e1d22ca` onward. Consequence on the measured after-tree:

- `C7_V4_CLEAN` (required `yes`), `C7_RED_ON_R65_CANDIDATE`, `C7_V2_CLEAN`,
  `C7_V3_CLEAN`, `C7_CONTROL_PASS`, `C7_MUTANT_KILLED*`,
  `C7_NEG_SPOOF_KILLED*`, `HOLD_CALIBRATION`, `HOLD_REPLAY`, `HOLDS_OK`,
  `HOLDS_OK_V2..V6` are **never printed**;
- exit is **1**, not 0. Both §C1 and §C2 require "the counter's exit code is 0".
  §C1's `C7_V4_CLEAN=yes` is likewise unprintable.

Hash check: `reports/round-69/measure.py` is byte-identical at all three post-base
revisions — `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377`
(matches the pinned value in `claims.md` and `measure-before.log`). So this is the
frozen instrument, not a working-copy artefact, and `claims.md` forbids editing it
after the pre-registration revision. The base tree only escapes because it has no Q15
checker, so the branch prints `n/a` — which is why the committed red-before receipt
looks complete and the defect was undiscoverable from it.

### 2.2 Defect G — `Q15_FALSE_KILLED` would pass on a missing-file crash (masked)

With `run` hypothetically defined, the D1 scan target is
`TREE/reports/round-69/d1-false-sentence.md` (`measure.py:161-165`), but the frozen
invocation archives **only `corpus`**. In a corpus-only tree the file is absent:

```
$ cd /tmp/…/t-35e1258 && python3 -B corpus/q15_tree_id_check.py --scan \
    reports/round-69/d1-false-sentence.md --lane …/revenger-shokunin
FileNotFoundError: [Errno 2] No such file or directory: 'reports/round-69/d1-false-sentence.md'
D1_SCAN_EXIT=1
```

`measure.py:165` reads `q15_false_killed = rc != 0` → the label would print
`Q15_FALSE_KILLED=yes` for a `FileNotFoundError`, not for a flagged false sentence.
The same pattern applies to the lesson scan (2.3). Soundness hole, currently hidden by
defect F.

### 2.3 Defect H — the C2 lesson does not exist, and `QUALITY.md` already cites it

- `corpus/QUALITY.md:27` carries the Q15 row (so `Q15_PRESENT=yes` holds) and cites
  `M48 (`lessons/round-69.md`)`.
- `git ls-tree --name-only 35e1258 corpus/lessons/` ends at
  `corpus/lessons/round-68-verifier-spotcheck.md`; `corpus/lessons/round-69.md`
  **does not exist** at the tip, at `da02261`, or in the working tree.

So the Q15 row's mistake pointer is dangling, and `Q15_RESTATE_OK` — the C2 pass
predicate "the lesson's restated tree-identity sentence re-derives" — cannot be
`yes` (counter would print `Q15_RESTATE_OK=n/a (no round-69 lesson)`).
`claims.md` §C2 also requires the restated sentence in "this round's lesson", which is
the same absent file.

### 2.4 Defect I — `claims.md` §C2's red-before narrative contradicts its own receipt

`claims.md:137-139`:

> **Red-before (committed history).** On the base tree: `Q15_PRESENT=no` (no
> criterion row), `Q15_RESTATE_OK=n/a` (no round-69 lesson), `Q15_SELFTEST=pass`
> and `Q15_FALSE_KILLED=yes` (the checker ships with the claims revision and the D1
> fixture is committed as evidence of the defect class).

The named receipt `measure-before.log` (measured on `222a7a7`, which
`git merge-base --is-ancestor` confirms **precedes** `e1d22ca`) actually prints:

```
Q15_PRESENT=no
Q15_SELFTEST=n/a (no checker)
Q15_FALSE_KILLED=n/a (no checker)
Q15_RESTATE_OK=n/a (no checker)
```

`Q15_SELFTEST=pass` / `Q15_FALSE_KILLED=yes` are asserted for a tree that cannot
contain the checker. This is exactly the Q15/M46–M47 class the criterion exists to
catch, inside the criterion's own enabling document.

## 3. Substantive status of each predicate, measured without the counter

Because the counter cannot print the C7 labels, the same commands were run by hand in
the `35e1258` scratch tree (`cwd` = tree, which is what `run()` uses):

| predicate | how measured | result |
|---|---|---|
| `Q15_SELFTEST` | `python3 -B corpus/q15_tree_id_check.py --self-test` | exit 0, `Q15_SELFTEST=pass (true sentence verified; false sentence killed)` |
| `Q15_FALSE_KILLED` (real) | same checker, `--scan reports/round-69/d1-false-sentence.md --lane <lane>`, cwd = lane root | exit 1, `Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)` — the fixture *is* killed; only the counter's wiring (2.2) is unsound |
| `C7_V4_CLEAN` | `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md` | exit 0, `checked_blocks=17 problems=0` → **clean** |
| `C7_RED_ON_R65_CANDIDATE` | `--entry corpus/knowledge/round-65-…md` | exit 1, `checked_blocks=15 problems=1` → red, as frozen |
| `C7_V2_CLEAN` | `--entry corpus/knowledge/round-67-…md` | exit 0, `checked_blocks=16 problems=0` |
| `C7_V3_CLEAN` | `--entry corpus/knowledge/round-68-…md` | **exit 1, `checked_blocks=17 problems=7`** — regression, see 3.1 |

### 3.1 Defect J — the build breaks the round-68 candidate's C7 cleanliness

`measure-before.log` records `C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0`.
On the post-build tree the same command yields 7 drift problems:

```
drift entry:137 embedded output line not in recheck stdout: enum RES_STRING_POOL_TYPE : 239
drift entry:138 … enum RES_XML_TYPE : 241
drift entry:139 … enum RES_XML_START_NAMESPACE_TYPE : 245
drift entry:140 … enum RES_XML_END_NAMESPACE_TYPE : 246
drift entry:141 … enum RES_XML_START_ELEMENT_TYPE : 247
drift entry:142 … enum RES_XML_END_ELEMENT_TYPE : 248
drift entry:143 … enum RES_XML_RESOURCE_MAP_TYPE : 253
checked_blocks=17 problems=7
```

Cause: C1 repair item 1 extends `corpus/derive_axml_anchors.py` (diff
`222a7a7..35e1258`: `corpus/derive_axml_anchors.py | 51 ++++-`), which now emits
`enum RES_STRING_POOL_TYPE : 239 = 0x0001` where the frozen v3 block quotes
`enum RES_STRING_POOL_TYPE : 239`; the gate compares whole lines
(`derive_axml_anchors.py` enum-line count 7 at base → 8 at tip). The v3 entry's
**bytes are unchanged** (so the "prior candidates keep every byte" void clause is not
triggered), but its gate verdict flips `yes → no`. `HOLDS_OK_V6` requires
`c7_v3_clean` (`measure.py:574-575`), so if the counter ran, V6 would read `no`.
No claim, void clause or precondition in `claims.md` covers this coupling.

## 4. C1 precondition table — met / unmet on the current bytes

| # | precondition (`claims.md` §C1 frozen predicate) | label on `35e1258` | met? |
|---|---|---|---|
| 1 | `K_HELD_BACKED=9/14` | `8/14` | **NO** (flip pending; by design pre-flip) |
| 2 | `K_HELD_BACKED_STRICT=9/14` | `8/14` | **NO** (same) |
| 3 | `K_ROW C05 status=held` | `uncovered` (`C05_STATUS=uncovered`) | **NO** (flip pending) |
| 4 | `C05_SINGLE_V4=yes` | `no` (`C05_KNOWLEDGE_COLUMN=-`) | **NO** (row names no entry) |
| 5 | `HOLDS_C2_V4=yes` | `no` | **NO** (needs 1–4) |
| 6 | `README_TOKEN_LEGEND_MISMATCH=0` | `0 rows=[]` | **YES** |
| 7 | `C7_V4_CLEAN=yes` | **unprintable** (defect F); hand-run = exit 0, 0 problems | **NOT MEASURABLE by the counter**; substance clean |
| 8 | every applicable Q01–Q15 decision PASS | **three FAILs among seven landed decisions**: Q07 FAIL, Q14 FAIL, Q15 FAIL (Q01/Q04/Q06 PASS, Q12 n/a); Q02/Q03/Q05/Q08/Q09/Q10/Q11/Q13 not yet landed | **NO — already false, kill rule fires** |
| 9 | spot-check not REJECT | `R69SpotcheckDiscern.md`: "**AGREE (both checks)**" | **YES** |
| 10 | counter exit code 0 | **1** (`NameError`, all post-`e1d22ca` trees) | **NO — structurally impossible with the pinned counter** |

C2 (for completeness, since C1's flip and C2 land in the same revision):

| precondition | status |
|---|---|
| `Q15_PRESENT=yes` | **YES** — `corpus/QUALITY.md:27` |
| `Q15_SELFTEST=pass` | **YES** — checker exit 0 (not print-able by the counter) |
| `Q15_FALSE_KILLED=yes` | substantively **YES** (fixture killed at lane root), but the counter's wiring would report it from a `FileNotFoundError` (2.2) |
| `Q15_RESTATE_OK=yes` | **NO** — `corpus/lessons/round-69.md` does not exist (2.3) |
| counter exit 0 | **NO** — same `NameError` |

### 4.1 Wave Q decisions landed at this seat's return (snapshot 2026-10-25T10:17Z)

Read from `.ufo/waves/round-69/R69ReviewEntryQ*.md`, first line of each (these are
untracked working-tree reports, so `K_*` labels over the committed tree cannot see
them, but they are the decisions the admission order requires):

| Q | report | verdict |
|---|---|---|
| Q01 | `R69ReviewEntryQ01.md:1` | PASS |
| Q04 | `R69ReviewEntryQ04.md:1` | PASS |
| Q06 | `R69ReviewEntryQ06.md:1` | PASS |
| Q07 | `R69ReviewEntryQ07.md:1` | **FAIL** — entry:91 states a namespace-resolution mechanism `readout.py:211` does not implement |
| Q12 | `R69ReviewEntryQ12.md:1` | n/a (no rejected-sources row) |
| Q14 | `R69ReviewEntryQ14.md:1` | **FAIL** — entry:48 attaches "15-byte" to an ellipsis-truncated run and relabels the 16-byte `payload_first16_hex` as "the correct 9-byte pair" |
| Q15 | `R69ReviewEntryQ15.md:1` | **FAIL** — entry:8's `c7b7cf98` carries an unguarded tree-identity sentence with no deriving command |
| Q02/Q03/Q05/Q08/Q09/Q10/Q11/Q13 | not landed | — |

Consequence under §C1's kill rule ("Any Q FAIL on the v4 bytes … → the C05 row stays
`uncovered`, the v4 entry is marked `admission-status: rejected` … and C1 is reported
**FALSIFIED**"): the all-pass conjunct is already false on three independent
criteria, so no flip is admissible even if the counter defect were repaired. Repair
items 6 and 7 of §C1 were supposed to close the Q07 and Q14 classes and, per these
two reviews, did not.

## 5. Verdict

**NOT-MET.** Unmet preconditions, in blocking order:

1. **Q07, Q14 and Q15 FAIL on the v4 bytes** (§4.1). This is the decisive bar: §C1's
   kill rule converts any Q FAIL into `C05` staying `uncovered`, the v4 entry becoming
   `admission-status: rejected`, and C1 **FALSIFIED**. A flip is now inadmissible on
   the merits, independent of every instrument problem below.
2. **counter exit code 0** — impossible: `NameError` at `measure.py:158` on every tree
   carrying the Q15 checker; it also suppresses `C7_V4_CLEAN` and all `HOLDS_OK_V*`.
   Independently reproduced by `R69Q15CheckerRun.md:3` ("the end-to-end gate is BROKEN
   by the frozen counter (`measure.py:158` `NameError` …)"). The instrument is pinned
   and marked never-editable after `e1d22ca`, so this cannot be repaired inside the
   frozen contract — it needs an L1 adjudication (void/redrive) and must not be
   hand-patched at flip time.
3. **`Q15_RESTATE_OK=yes`** — the round-69 lesson that must carry the restated
   tree-identity sentence does not exist, though `corpus/QUALITY.md:27` already points
   at it (`M48 (lessons/round-69.md)`); C2's pass branch is therefore unreachable too.
4. **C05 row flip set** (`K_HELD_BACKED*` 9/14, `status=held`, `C05_SINGLE_V4`,
   `HOLDS_C2_V4`) — correctly still `uncovered`/8-14 per admission order step 1; these
   are pending, and item 1 above means they should stay pending.
5. **`Q15_FALSE_KILLED` soundness** and **`C7_V3_CLEAN` regression** — neither is a
   C1 pass-branch conjunct today, but both corrupt the flip's evidence base: the first
   would accept a missing-file crash as an ability-to-fail receipt (independently
   flagged by `R69ReviewEntryQ15.md:1`), the second means the committed
   `measure-before.log` claim `C7_V3_CLEAN=yes` is not reproducible on the tree the
   flip would be recorded against (and `HOLDS_OK_V6` would read `no`).

Met now: `README_TOKEN_LEGEND_MISMATCH=0`, the spot-check is AGREE, the v4 candidate
is present as `candidate` (not rejected — that re-mark is the L1's action, not this
seat's), and the v4 entry is substantively clean under the C7 gate (`exit 0,
checked_blocks=17 problems=0`). None of those is sufficient for a flip.

## 6. Risks / notes for the adjudicating L1

- Do **not** fix `measure.py` to flip: the hash is pinned and `claims.md` says it is
  never edited after the pre-registration revision. Fixing it silently would make
  `measure-before.log` and the after-run incomparable.
- The `C7_V3_CLEAN` regression (3.1) is a *shared-script* coupling: extending
  `derive_axml_anchors.py` changes the embedded-output contract of a frozen prior
  candidate. Any future repair that extends a script cited verbatim by an older entry
  needs a gate run over all candidates, not just the new one.
- `HOLDS_OK_V6` is still coupled to `c7_v3_clean` (`measure.py:574-575`), so D5's open
  L0 now has a second, independent instance of the same coupling class.
- Sibling convergence, checked before returning: `R69Q15CheckerRun.md:3` independently
  reports the same `measure.py:158` `NameError` and calls the end-to-end gate BROKEN.
  `R69CounterIntegrity.md:1` reports `INTACT`, but by its own scope note
  (`R69CounterIntegrity.md:66`) it "did not run the counter on the after/landed tree" —
  so `INTACT` there means *bytes match the pin*, and does not contradict the crash.
  Neither reading should be reconciled by editing the counter.
- Scratch: `/tmp/revenger-r69-flip/` (four extracted trees, counter logs, C7 logs) —
  deleted before return.
