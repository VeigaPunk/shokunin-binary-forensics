REPLAYS-AS-COMMITTED — the frozen counter (sha256 `488f95aa…c88c76`) reproduces `measure-before.log` line for line on the claim base tree, is deterministic (3/3 identical runs per tree), cwd- and lane-worktree-independent, leaves its tree byte-identical, and honours the 0/1/2 exit contract on both probes (README deleted → exit 2 + `COUNTER_ERROR`; gate replaced by `SystemExit(3)` → exit 1, never 2).

# R70W1CounterReplay — replay of `reports/round-70/measure.py`

Seat: leaf, replay only. No lane file was written, edited, committed or pushed. Scratch under `/tmp/revenger-r70-CounterReplay-*`, deleted before return. No package install or update was performed (no tool change to record).

## 0. Instrument identity

```
$ sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-70/measure.py
488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76  …/reports/round-70/measure.py
```
Matches the digest frozen in `reports/round-70/claims.md` (counter line) — so every label below is produced by the pre-registered instrument, not a drifting copy.

Python used by the counter's `run()` (`sys.executable`): `Python 3.14.8`.

## 1. Trees (exactly the recipe in the assignment)

```
git -C …/revenger-shokunin archive 3f5edbc206351232a3d2d801334dd930499ccaf5 corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C /tmp/revenger-r70-CounterReplay-base
git -C …/revenger-shokunin archive aa1842fac199aa524930e5565ed3715de5f84c6d corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C /tmp/revenger-r70-CounterReplay-target
```
Base tree: 514 files, top level `SCORECARD.md SHONEN.md SKILL.md corpus`. Target tree: 523 files, same top level.
Commits between base and candidate: `9c7863f` (considerthese), `dbacce2` (pre-registration + counter + controls), `aa1842f` (C05 v5 candidate).

## 2. Determinism — two (plus a third) runs per tree, byte-identical

```
python3 -B <measure.py abs path> /tmp/revenger-r70-CounterReplay-base   > base-run1.log   # BASE_RUN1_EXIT=0
…                                                                      > base-run2.log   # BASE_RUN2_EXIT=0
diff base-run1.log base-run2.log  → (no output)  BASE_DETERMINISTIC=yes
…                                                                      > base-run3.log   # BASE_RUN3_EXIT=0
diff base-run1.log base-run3.log  → (no output)  BASE_RUN3_IDENTICAL=yes
python3 -B <measure.py> /tmp/revenger-r70-CounterReplay-target         > target-run1.log # TARGET_RUN1_EXIT=0
…                                                                      > target-run2.log # TARGET_RUN2_EXIT=0
diff → (no output)  TARGET_DETERMINISTIC=yes ; run3 identical too
```
The run logs live only in scratch and are deleted with it (§10); the reproducible evidence is the `diff`-identity above and the label text quoted in §3, not a digest of a deleted file.

Also independent of invocation cwd and of TREE being relative:

```
( cd / && python3 -B <measure.py> /tmp/…-target )  → CWD_ROOT_EXIT=0 ; diff vs run1 → CWD_INDEPENDENT=yes
( cd /tmp && python3 -B <measure.py> revenger-r70-CounterReplay-base ) → RELATIVE_TREE_EXIT=0 ; diff vs run1 → RELATIVE_TREE_IDENTICAL=yes
```

## 3. Every label and exit code

### Base tree `3f5edbc2…` — EXIT=0

```
K_HELD_BACKED=8/14 score=5.7
K_HELD_BACKED_STRICT=8/14
C05_STATUS=uncovered
C05_KNOWLEDGE_COLUMN=-
C05_SINGLE_V5=no
V5_ENTRY_PRESENT=no
V5_ADMITTED_MARKED=no
C1_GATE=n/a (no v5 entry or no gate)
C1_LINT=n/a (no v5 entry or no lint)
HOLDS_C1_V5=no
SELF_MISMATCH=n/a (no checker)
SELF_CLEAN_FIXTURE=n/a (no checker)
SELF_MUTANTS_KILLED=n/a (no checker)
SHONEN_BOX_COUNT=4
README_ROWS=14
HOLDS_C2_V5=no
EMB_R65=checked_blocks=15 problems=1 exit=1
EMB_R67=checked_blocks=16 problems=0 exit=0
EMB_R68=checked_blocks=17 problems=7 exit=1
EMB_R69=checked_blocks=17 problems=0 exit=0
EMB_PINNED_SCRIPT_IS_S046=no
EMB_R68_BYTES_UNCHANGED=yes
EMB_R65_BYTES_UNCHANGED=yes
EMB_PIN_MUTANT_KILLED_ATTRIBUTED=n/a (no pin file)
HOLDS_C3_V1=no
HOLD verify_{evm_evidence,icon_languages,icon_states,js_graph_delta,multi_icon_states,named_multi_icon_states,pe_resources,saved_evidence,semantic_trace,shape_evidence}.py exit=0   (10 lines, full text in measure-before.log)
HOLD_REPLAY=10/10
GATE_SELFTEST=exit 0
F_COVERAGE=5/8 score=6.2
FRESH_ROWS=18/18
HOLDS_OK_V7=yes
```

### Target tree `aa1842f` (C05 v5 candidate) — EXIT=0

```
K_HELD_BACKED=8/14 score=5.7
K_HELD_BACKED_STRICT=8/14
C05_STATUS=uncovered
C05_KNOWLEDGE_COLUMN=-
C05_SINGLE_V5=no
V5_ENTRY_PRESENT=yes
V5_ADMITTED_MARKED=no
C1_GATE=checked_blocks=22 problems=0 exit=0 ok=yes
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
HOLDS_C1_V5=no
SM1=1
SM2=7
SM3=2
SM4=1
SM5=1
SM6=0
SELF_MISMATCH=12 exit=1
SELF_CLEAN_FIXTURE=0
SELF_MUTANTS_KILLED=6/6
SHONEN_BOX_COUNT=4
README_ROWS=14
HOLDS_C2_V5=no
EMB_R65=checked_blocks=15 problems=1 exit=1
EMB_R67=checked_blocks=16 problems=0 exit=0
EMB_R68=checked_blocks=17 problems=0 exit=0
EMB_R69=checked_blocks=17 problems=0 exit=0
EMB_PINNED_SCRIPT_IS_S046=yes
EMB_R68_BYTES_UNCHANGED=yes
EMB_R65_BYTES_UNCHANGED=yes
EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1
HOLDS_C3_V1=yes
HOLD_REPLAY=10/10
GATE_SELFTEST=exit 0
F_COVERAGE=5/8 score=6.2
FRESH_ROWS=18/18
HOLDS_OK_V7=yes
```
Label inventory identical between trees except the six `SM*` lines, which only appear when the checker exists (`measure.py:181-185`).

## 4. Line-for-line comparison with `reports/round-70/measure-before.log`

```
grep -v '^\$ python3' measure-before.log | grep -v '^# red-before' | grep -v '^EXIT=' > before-stripped
diff before-stripped base-run1.log   → (no output)   BASE_MATCHES_BEFORE=yes
```
All 40 label lines match; the only differences are the three non-label receipt lines (`# red-before` header, `$ python3 …` command echo, `EXIT=0`) that the committed log carries and the counter does not print. This is the required "minus the HOLD verify lines" comparison in the stronger form: even the ten `HOLD …` lines match verbatim, so no line was dropped.

`reports/round-70/controls/A-do-nothing-base.log` is an abbreviated receipt (its ten `HOLD verify_*` lines are elided); its label set and `EXIT=0` match my base run — the only diff against my full output is those ten `HOLD` lines (`diff A-stripped base-run1.log → 25a26,35`).

## 5. Exit-contract probes (scratch copies only)

### Probe 1 — `corpus/README.md` deleted (base copy)

```
PROBE1_EXIT=2
Traceback (most recent call last):
  File "…/reports/round-70/measure.py", line 287, in <module>   sys.exit(main(Path(args[0]).resolve()))
  File "…/measure.py", line 128, in main                        return body(tree, tmp)
  File "…/measure.py", line 135, in body                        rows = readme_rows(tree)
  File "…/measure.py", line 61, in readme_rows                  … read(tree / "corpus/README.md") …
FileNotFoundError: [Errno 2] No such file or directory: '/tmp/revenger-r70-CounterReplay-noreadme/corpus/README.md'
COUNTER_ERROR=uncaught exception (exit 2)
```
**Exit 2, never 1** — as frozen (`measure.py:290-293`). No label is printed before the crash, so a 2 cannot be mistaken for a scored run.

### Probe 2 — `corpus/check_embedded_outputs.py` := `raise SystemExit(3)` (target copy)

```
PROBE2_EXIT=1
C1_GATE=checked_blocks=None problems=None exit=3 ok=no
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
HOLDS_C1_V5=no
SELF_MISMATCH=12 exit=1  (SM1=1 SM2=7 SM3=2 SM4=1 SM5=1 SM6=0)
SELF_CLEAN_FIXTURE=0 ; SELF_MUTANTS_KILLED=6/6
EMB_R65=checked_blocks=None problems=None exit=3
EMB_R67=checked_blocks=None problems=None exit=3
EMB_R68=checked_blocks=None problems=None exit=3
EMB_R69=checked_blocks=None problems=None exit=3
EMB_PINNED_SCRIPT_IS_S046=yes ; EMB_R68_BYTES_UNCHANGED=yes ; EMB_R65_BYTES_UNCHANGED=yes
EMB_PIN_MUTANT_KILLED_ATTRIBUTED=0/1
HOLDS_C3_V1=no
HOLD_REPLAY=10/10 ; GATE_SELFTEST=exit 3 ; F_COVERAGE=5/8 ; FRESH_ROWS=18/18
HOLDS_OK_V7=no
```
Correct partition: a helper exiting non-zero is a **red hold** (exit 1, `GATE_SELFTEST=exit 3`), not a counter exception (which would be 2). `checked_blocks=None` is emitted rather than a crash because `emb()` returns `(None, None)` when the `checked_blocks=…` regex misses (`measure.py:119-123`) — the unparsed gate is visible as `None`, and `HOLDS_C1_V5`/`HOLDS_C3_V1` are both `no`.

### Probe 3 (extra) — `corpus/README.md` emptied

```
EMPTY_README_EXIT=2
ZeroDivisionError: division by zero      (measure.py:144, K_HELD_BACKED score)
COUNTER_ERROR=uncaught exception (exit 2)
```
Also 2, not 1. Consistent with "the counter could not evaluate".

### Probe 4 (extra) — argument errors

```
python3 -B <measure.py> /tmp/…-doesnotexist → usage: measure.py TREE (TREE/corpus must exist) ; NO_TREE_EXIT=2
python3 -B <measure.py>                     → usage: measure.py TREE (TREE/corpus must exist) ; NO_ARG_EXIT=2
```

## 6. Hermeticity / no side effects

```
cp -r target → hermetic ; sha256sum all files before ; run ; sha256sum after
diff h-before.txt h-after.txt → (no output)   TREE_UNCHANGED_BY_COUNTER=yes   (HERMETIC_RUN_EXIT=0)
ls -d /tmp/rev-r70-measure-* | wc -l → 0       (the counter's own tempdirs are removed in `finally`, measure.py:127-131)
```
Lane-worktree independence — the lane was dirty during the replay (`git status --porcelain | wc -l` = 14; `M SHONEN.md`, `M SKILL.md`, `M corpus/README.md`, `M corpus/self_assessment_check.py`), yet:

```
BASE_DIRTYLANE_EXIT=0 ; diff base-run1 base-dirtylane → BASE_UNAFFECTED_BY_DIRTY_LANE=yes
TARGET_DIRTYLANE_EXIT=0 ; diff target-run1 target-dirtylane → TARGET_UNAFFECTED_BY_DIRTY_LANE=yes
```
This is structural, not luck: `LANE` is used only as the `--lane` string (`measure.py:107,167,180`), and both consumers use it solely for `git -C <lane> cat-file -e <h>^{commit}` (`corpus/lint_entry.py:82`, `corpus/self_assessment_check.py:116`) — object-store resolution, never worktree reads. The docstring's "reads only TREE (and git object lookups in LANE for hash resolution)" (`measure.py:6-7`) is therefore accurate; `QUALITY.md` is read beside the lint script inside TREE (`corpus/lint_entry.py:159`).

## 7. Findings (all advisory, wave-1 pre-gate; none is a kill-rule input)

**F1 — MEDIUM (operability): the process exit code does not encode claim state; the do-nothing base tree exits 0 with all three claim labels `no`.**
Evidence: `return 0 if holds_ok else 1` at `reports/round-70/measure.py:278`, where `holds_ok` is computed at `measure.py:276` from `HOLD_REPLAY`, `GATE_SELFTEST`, `F_COVERAGE`, `FRESH_ROWS` only — `HOLDS_C1_V5`, `HOLDS_C2_V5`, `HOLDS_C3_V1` are never consulted. Command output: base run `BASE_RUN1_EXIT=0` together with `HOLDS_C1_V5=no`, `HOLDS_C2_V5=no`, `HOLDS_C3_V1=no` (§3), while `measure.py:9` advertises "0 every hold green; 1 a named hold is red" and three of the printed labels are literally named `HOLDS_*`.
Why it is not a predicate deviation: `claims.md` makes "Counter exit 0" a conjunct of `HOLDS_OK_V7` (the Holds section) and every claim predicate is label-based, so a red claim with a green holds-bundle is exactly what the frozen text describes — the base tree's exit 0 is the control-A behaviour the claims predict.
Residual risk: any wrapper keyed on `$?` (`measure.py TREE && echo green`) reports the untouched base tree as green, and `claims.md`'s C1 sentence "the command that would show it unmoved is the counter" is true only if the reader reads `HOLDS_C1_V5`, not the status. Suggested repair for a future round (NOT performed here — read-only seat): say in the docstring that the exit code reflects `HOLDS_OK_V7` only, or add a `--claims` mode that exits 1 when any `HOLDS_C{1,2,3}_*` is `no`. Frozen-predicate-wise the cheapest honest fix is documentation, since editing `measure.py` now would violate the freeze.

**F2 — MEDIUM (calibration, feeds the C2 repair seats): the C2 "before" of 9 is a base-tree number; at the candidate tip the same instrument reads 12 (`SM2` 4→7), and my target run reproduces control H exactly.**
Evidence: `before-treated-tools-on-base.log` → `SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0 SELF_MISMATCH=9`; `controls/H-tools-only.log` → `SM2=7 SELF_MISMATCH=12`; my target run (§3) → `SM1=1 SM2=7 SM3=2 SM4=1 SM5=1 SM6=0 SELF_MISMATCH=12`, byte-identical C2 label block to H. So the two independent trees agree, but the repair target at `aa1842f` is 0-from-12: the SM2 leg must additionally name the artifacts the pre-registration and candidate commits introduced (`corpus/lint_entry.py`, `corpus/self_assessment_check.py`, `corpus/derive_axml_anchors_r68.py`, `corpus/snapshots/` — the `SM2` docstring at `corpus/self_assessment_check.py:11-14` counts every top-level `corpus/*.py` and `corpus/*/`). A repair seat that fixes only the four files named in `claims.md` ("`q15_tree_id_check.py`, `derive_axml_anchors.py`, `check_embedded_outputs.py`, `snapshots/`") lands at `SELF_MISMATCH=5`, not 0 — worth a wave-1 warning, not a defect in the counter.

**F3 — INFO (calibration): `HOLDS_C3_V1=yes` already at the candidate commit.**
Evidence: §3 target block — `EMB_R68=checked_blocks=17 problems=0`, `EMB_R65 … problems=1`, `EMB_R67 … 0`, `EMB_R69 … 0`, `EMB_PINNED_SCRIPT_IS_S046=yes`, `EMB_R68_BYTES_UNCHANGED=yes`, `EMB_R65_BYTES_UNCHANGED=yes`, `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1`. C3's mechanical predicate is satisfied before the final tip (the gate fix and the pinned script are in `dbacce2`/`aa1842f`), so at the final tip C3 can only regress, not be delivered — wave 2 should read C3 as a regression guard rather than a pending delivery. Not a defect: the claims never say C3 is red at the candidate.

**F4 — INFO (operability): `HOLD_REPLAY` is hard-pinned to exactly ten verifiers** (`measure.py:276`, `ok == len(ps) == 10`). Adding an eleventh `corpus/verify_*.py` in a later revision turns the label red without any hold actually failing. Round-frozen counter, so no action this round; recorded so a future round's copy does not inherit the tripwire silently.

**Non-findings (checked, clean):** `C05_KNOWLEDGE_COLUMN` extraction reads field 3 only (`measure.py:75-79`), so the C05 row's evidence column mentioning `knowledge/round-65-apk-axml-byte-evidence.md` at `corpus/README.md:34` (candidate bytes) correctly does **not** count as a knowledge-column entry — `C05_KNOWLEDGE_COLUMN=-`, `C05_SINGLE_V5=no`. The candidate entry's header `admission-status: candidate` yields `V5_ADMITTED_MARKED=no`, which is the landing-order step-1 state, not a defect.

## 8. Answers to the assigned questions

1. Two scratch trees built by `git archive` from `3f5edbc2…` and `aa1842f…` — done (§1).
2. Counter run twice on each by absolute path — done; determinism diffed, identical (§2). Third run each plus cwd/relative-path variants also identical.
3. Every label and exit code recorded (§3); base `EXIT=0`, target `EXIT=0`, label inventory enumerated.
4. Probe (1) README deleted → `PROBE1_EXIT=2` + `COUNTER_ERROR=uncaught exception (exit 2)`, never 1 (§5).
5. Probe (2) gate := `raise SystemExit(3)` → `PROBE2_EXIT=1`, labels reported verbatim (§5).
6. Base output vs `measure-before.log` — line for line identical after stripping only the receipt header/command/`EXIT=` lines; the `HOLD verify_*` lines match too (§4).
7. **Verdict: REPLAYS-AS-COMMITTED.**

## 9. Risks / blockers

- No blocker; no missing artifact. Everything the seat needed was present at `aa1842f` and in the frozen receipt set.
- Advisory risk carried to wave 2: F1 (exit code vs claim labels) and F2 (C2 before-count is 12 at the candidate tip, not 9) — both are repair/documentation items for the final bytes, not counter defects.
- The lane worktree is dirty from sibling repair seats (`M SHONEN.md SKILL.md corpus/README.md corpus/self_assessment_check.py`); I verified this does not perturb any counter label, so wave-2 seats may replay at the final tip while other seats hold worktree edits.

## 10. Scratch cleanup

`rm -rf /tmp/revenger-r70-CounterReplay-*` — base/target/noreadme/gate3/hermetic/emptyreadme trees, all run logs and hash snapshots removed. No lane file was created or modified by this seat other than this report.
