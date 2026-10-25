MATCH — the frozen counter replayed on the base tree `222a7a7` emits stdout byte-identical to the committed `measure-before.log` (sha256 `e1cf90f3…`, `diff -u` empty) and exits 0; every requested label matches, including the six labels the claims declare as the do-nothing control. **Qualifier that changes what the round may claim: the pinned counter cannot evaluate the after-run at all (F4–F10) — C1 and C2 are NOT EVALUABLE, not falsified.**

# R69CounterReplay — red-before replay of the frozen round-69 counter

seat: `L1Revenger69.R69CounterReplay` (leaf) · lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` · date: 2026-10-25

## Axes walked

- **reproducibility of the red-before receipt** — does an independent seat, from `/`, get the committed receipt back?
- **base-commit identity** — is the tree the receipt was run on actually `222a7a7`, and is the assignment's `refs/heads/main~1` shortcut correct?
- **non-destructiveness** — does the replay mutate the lane, `corpus/`, or the extracted tree?

## 1. Base commit resolution (the assignment's shortcut does NOT hold)

`refs/heads/main~1` is **not** the base commit — it is the round-69 build commit.

```
$ git -C …/revenger-shokunin log --format='%H %s' refs/heads/main -5
35e12584d37434632fa06a6c2975ab55f29a8d3f round-69: wave preparation — 64-seat v2 spec + builder, validated plan (exit 0), dispatch taskCall (64 tasks), swarm registry, slot acquire receipt (D2)
da022615b052977f3b0c1b4c501564d977bf7b0d round-69: build — C05 v4 candidate with the complete routed repair bundle …, S047 row supersedes S046, QUALITY Q15 criterion
e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968 round-69: pre-registration — claims …, frozen counter measure.py, Q15 checker, red-before receipt
222a7a702529fb60598633ebdf5e1442007bc15d round-68 verifier spot-check (integrator, hyaku): non-author admit/reject
d00f77942d78cb9a3b41547370d7a8a4ebea6c72 round-68: measurement receipt re-pinned to the final measured commit 1c34603 …

$ git rev-parse refs/heads/main~1 refs/heads/main HEAD
da022615b052977f3b0c1b4c501564d977bf7b0d
35e12584d37434632fa06a6c2975ab55f29a8d3f
35e12584d37434632fa06a6c2975ab55f29a8d3f
```

Per the assignment's fallback I resolved by the pre-registration's parent: pre-registration = `e1d22ca`, its parent = **`222a7a7` = `main~3`**, which is the hash the frozen contract names. `git merge-base --is-ancestor 222a7a7 refs/heads/main` → `yes`.

Corpus tree ids per commit (read-only):

```
222a7a7:corpus  = 2c45edaf870fa0b35936114f34a51767dba67ed3   ← measured base
e1d22ca:corpus  = 5bf8cd43e17670d6d0c0b7e24d859171f017fdec   ← pre-registration (adds corpus/q15_tree_id_check.py)
da0226 :corpus  = 7aeabf218889dee89036de808573aacf11bd6e69   ← build
35e12584:corpus = 7aeabf218889dee89036de808573aacf11bd6e69   ← tip (build state, unchanged by wave prep)
```

Counter pin verified: `sha256sum reports/round-69/measure.py` = `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` — matches `claims.md` and `measure-before.log`.

## 2. Replay command (exactly as instructed)

```sh
rm -rf /tmp/revenger-r69-replay; mkdir -p /tmp/revenger-r69-replay/tree /tmp/r69-seat-replay
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive \
  222a7a702529fb60598633ebdf5e1442007bc15d corpus | tar -x -C /tmp/revenger-r69-replay/tree
# 507 files under /tmp/revenger-r69-replay/tree/corpus
cd /
TMPDIR=/tmp/r69-seat-replay python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-69/measure.py \
  /tmp/revenger-r69-replay/tree
```

**Exit code: 0.** stderr: empty (0 bytes). stdout: 105 lines, 57 label lines, no duplicate labels.

### 2.1 Receipt comparison

```
$ wc -l < reports/round-69/measure-before.log
105
$ diff -u reports/round-69/measure-before.log /tmp/revenger-r69-replay/replay-base.out
DIFF_EMPTY: byte-identical
$ sha256sum reports/round-69/measure-before.log /tmp/revenger-r69-replay/replay-base.out
e1cf90f357a94da84ab65ee4ef6d17bc0dc034f95b5458c735d3cce21edd6f29  …/measure-before.log
e1cf90f357a94da84ab65ee4ef6d17bc0dc034f95b5458c735d3cce21edd6f29  …/replay-base.out
```

Committed-blob check (the receipt is really committed, not a working-tree artifact):

```
git rev-parse 35e12584…:reports/round-69/measure-before.log   → 456f3181c496396452e998c2562e5d387a1956b7
git cat-file blob 35e12584…:reports/round-69/measure-before.log | sha256sum → e1cf90f3…  (== disk)
git rev-parse e1d22ca…:reports/round-69/measure-before.log    → 456f3181c496396452e998c2562e5d387a1956b7  (unmodified since registration)
```

## 3. Label-by-label comparison (Verdict: MATCH on all)

| label | committed receipt | this replay | match |
|---|---|---|---|
| `K_HELD` | `8/14 score=5.7` | `8/14 score=5.7` | ✓ |
| `K_ROW C05 status` | `uncovered` | `uncovered` | ✓ |
| `K_ROW C07 status` | `held` | `held` | ✓ |
| `K_HELD_BACKED` | `8/14` | `8/14` | ✓ |
| `K_HELD_BACKED_STRICT` | `8/14` | `8/14` | ✓ |
| `C05_STATUS` | `uncovered` | `uncovered` | ✓ |
| `C05_SINGLE_V2` | `no` | `no` | ✓ |
| `C05_SINGLE_V3` | `no` | `no` | ✓ |
| `C05_SINGLE_V4` | `no` | `no` | ✓ |
| `C05_KNOWLEDGE_COLUMN` | `-` | `-` | ✓ |
| `C05_REJECTED_MARKED` | `yes` | `yes` | ✓ |
| `HOLDS_C2_V3` | `no` | `no` | ✓ |
| `HOLDS_C2_V4` | `no` | `no` | ✓ |
| `README_TOKEN_LEGEND_MISMATCH` | `0 rows=[]` | `0 rows=[]` | ✓ |
| `Q15_PRESENT` | `no` | `no` | ✓ |
| `Q15_SELFTEST` | `n/a (no checker)` | `n/a (no checker)` | ✓ |
| `Q15_FALSE_KILLED` | `n/a (no checker)` | `n/a (no checker)` | ✓ |
| `Q15_RESTATE_OK` | `n/a (no checker)` | `n/a (no checker)` | ✓ |
| `C7_GATE_PRESENT` | `yes` | `yes` | ✓ |
| `C7_SELFTEST` | `pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired` | identical | ✓ |
| `C7_RED_ON_R65_CANDIDATE` | `yes exit=1 :: checked_blocks=15 problems=1` | identical | ✓ |
| `C7_V2_CLEAN` | `yes exit=0 :: checked_blocks=16 problems=0` | identical | ✓ |
| `C7_V3_CLEAN` | `yes exit=0 :: checked_blocks=17 problems=0` | identical | ✓ |
| `C7_V4_CLEAN` | `n/a (no v4 file)` | `n/a (no v4 file)` | ✓ |
| `C7_CONTROL_PASS` | `1/1` | `1/1` | ✓ |
| `C7_MUTANT_KILLED` | `1/1` | `1/1` | ✓ |
| `C7_MUTANT_KILLED_ATTRIBUTED` | `1/1` | `1/1` | ✓ |
| `C7_NEG_SPOOF_KILLED` | `1/1` | `1/1` | ✓ |
| `C7_NEG_SPOOF_KILLED_ATTRIBUTED` | `0/1` | `0/1` | ✓ |
| `HOLD_CALIBRATION` | `4/4` | `4/4` | ✓ |
| `HOLD_REPLAY` | `10/10` | `10/10` | ✓ |
| `HOLDS_OK` | `yes` | `yes` | ✓ |
| `HOLDS_OK_V2` | `yes` | `yes` | ✓ |
| `HOLDS_OK_V3` | `yes` | `yes` | ✓ |
| `HOLDS_OK_V4` | `yes` | `yes` | ✓ |
| `HOLDS_OK_V5` | `yes` | `yes` | ✓ |
| `HOLDS_OK_V6` | `yes` | `yes` | ✓ |
| `FRESH_ROWS` | `18/18` | `18/18` | ✓ |
| `STRICT_REJECT_WINDOW_SELFTEST` | `pass old_window_miss=True` | identical | ✓ |

Every other line (the 20 `MUTANT …` / `C2_*`…`C6_*` calibration-attribution lines, the `SAVED_RECORDS`/`ROW_OPS`/op-frequency lines, the 10 `HOLD <script> exit=0 …` replay lines, `F_COVERAGE=5/8 score=6.2`, `F_FAMILIES=[…]`) is byte-identical because the whole 105-line stdout is byte-identical — `diff -u` returned empty, so there is no differing label to name.

### 3.1 Cross-check against the claims' declared do-nothing control

`claims.md` §C1 "Do-nothing control" declares, on `222a7a7`: `K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`, `K_ROW C05 status=uncovered`, `C05_SINGLE_V4=no`, `HOLDS_C2_V4=no`, `C7_V4_CLEAN=n/a (no v4 file)`. All six are reproduced exactly by this independent replay. `claims.md` §C2 red-before declares `Q15_PRESENT=no` and `Q15_RESTATE_OK=n/a` — both reproduced.

The counter's exit contract is `2 = not evaluable, 0 = the V1 holds hold, 1 = a hold failed`; exit **0** here means the base tree's held rows and the ten-verifier replay still hold, which is consistent with the receipt's `HOLDS_OK=yes`/`HOLDS_OK_V6=yes`. Note the receipt itself records no exit status (105 stdout lines, no `EXIT=` line), so **exit 0 is established by this replay, not merely re-confirmed**.

Cross-check of the counter's Q15 path, so that the four `n/a` labels are a genuine absence and not a swallowed git failure (`reports/round-69/measure.py:151-182`): the q15 block is gated on `TREE/corpus/q15_tree_id_check.py` existing (line 156-157) and on `TREE/corpus/QUALITY.md` carrying `^\| Q15 \|` (line 153). On the base tree neither exists:

```
git ls-tree -r 222a7a7… --name-only | grep -i q15   → ABSENT at 222a7a7
git ls-tree -r e1d22ca… --name-only | grep -i q15   → corpus/q15_tree_id_check.py
git ls-tree -r refs/heads/main --name-only | grep -i q15 → corpus/q15_tree_id_check.py
git show refs/heads/main:corpus/QUALITY.md | grep -c '^| Q15 |'  → 1
```

## 4. Non-destructiveness

- The counter mutates only `tempfile.TemporaryDirectory` copies of `TREE/corpus` (`measure.py:213,264,303,347,399,451,521`; `shutil.copytree(TREE/"corpus", work/"corpus")`), and each context exits before the next — `/tmp/r69-seat-replay` was empty again after the run (`find … -mindepth 1` → no output).
- The extracted tree is unchanged by the replay: a second fresh extraction of `222a7a7:corpus` diffs clean against the post-run tree — `diff -rq tree tree2` → `TREE_UNMODIFIED_BY_COUNTER: identical after replay`.
- Lane worktree untouched by me: `git status --porcelain` (read-only) shows only the pre-existing untracked `.ufo/waves/round-69/assimilation/` created by another seat; no `corpus/`, `reports/` or live/fixture bytes modified. No mutating git/jj command was run; no file written outside this report and `/tmp/revenger-r69-replay`.

## 5. Findings (none of them change the MATCH verdict)

**F1 — base-commit shortcut is wrong (would have measured the build tree).** The assignment's default `refs/heads/main~1` resolves to `da0226` (the build commit, whose `corpus` tree is `7aeabf21…`), i.e. the *already-repaired* tree, not the claim base. Following it would have replayed the counter on the wrong bytes. Resolved by the pre-registration parent rule to `222a7a7` (`main~3`), matching `claims.md`. Recommend the parent record base commits by hash only; an N-ago shortcut drifts as the round lands commits.

**F2 — `claims.md` §C2 red-before sentence is contradicted by the frozen receipt it cites.** The contract states: "On the base tree: … `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes` (the checker ships with the claims revision …)". The committed `measure-before.log` — and this independent replay of it — reads `Q15_SELFTEST=n/a (no checker)` and `Q15_FALSE_KILLED=n/a (no checker)`, because `corpus/q15_tree_id_check.py` is absent at `222a7a7` and first appears at `e1d22ca` (the claims revision). The receipt is right and the prose is wrong; the parenthetical reasoning ("ships with the claims revision") is exactly what makes `pass`/`yes` unattainable on the base tree. This is the same defect class as round-68 D1 (an identity/state asserted against contradicting bytes, pointer `claims.md` §C2 vs `measure-before.log:22-25`). It does **not** void C2 — the frozen pass predicate requires `Q15_SELFTEST=pass`/`Q15_FALSE_KILLED=yes` on the *final measured tree*, and the control's discriminating power is carried by `Q15_PRESENT=no → yes` and `Q15_RESTATE_OK=n/a → yes`, both of which the receipt does show. But the sentence should be restated (Q15-style) so the red-before claim is exactly what the receipt prints.

**F3 — `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1` is present in the base receipt and faithfully reproduced.** It is not a replay divergence; it is the known open D5 separability/attribution coupling (C7 spoof killed 1/1, attribution 0/1) carried forward un-pre-empted by the pending C7 L0. Recorded so that the after-run is compared against `0/1`, not an assumed `1/1`.

## 6. Tooling

No tool installed or upgraded (host-wide pacman transactions are paused; nothing needed). Used only existing `git`, `tar`, `diff`, `sha256sum`, `python3` (3.x stdlib), `awk`, `od`.

## 7. Full replay stdout (verbatim, 105 lines, exit 0)

<!-- replay-begin -->
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
ROW_OPS={'C03': ['inspect_managed_artifact'], 'C05': ['inspect_android_package'], 'C07': ['inspect_firmware_regions'], 'C08': ['capture_browser_scenario', 'inspect_web_page', 'observe_web_session']}
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
C05_STATUS=uncovered
HOLDS_C2_V3=no
HOLDS_C2_V4=no
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_firmware_regions': 1, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
Q15_PRESENT=no
Q15_SELFTEST=n/a (no checker)
Q15_FALSE_KILLED=n/a (no checker)
Q15_RESTATE_OK=n/a (no checker)
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
C5_CONTROL_PRESENT_verify_icon_languages.py=yes
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted
C5_CONTROL_PRESENT_verify_multi_icon_states.py=yes
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c5 exit=1 killed :: AssertionError: r42: forged receipt evidence accepted
C5_CONTROL_PRESENT=2/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
C6_CONTROL_PRESENT_verify_icon_languages.py_exit=yes
MUTANT verify_icon_languages.py c6-control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c6-exit exit=1 killed :: AssertionError: r47: forged receipt exit accepted
C6_CONTROL_PRESENT_verify_icon_languages.py_fixture=yes
MUTANT verify_icon_languages.py c6-control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c6-fixture exit=1 killed :: AssertionError: r47: forged receipt fixture accepted
C6_CONTROL_PRESENT_verify_multi_icon_states.py_exit=yes
MUTANT verify_multi_icon_states.py c6-control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c6-exit exit=1 killed :: AssertionError: r42: forged receipt exit accepted
C6_CONTROL_PRESENT_verify_multi_icon_states.py_fixture=yes
MUTANT verify_multi_icon_states.py c6-control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c6-fixture exit=1 killed :: AssertionError: r42: forged receipt fixture accepted
C6_CONTROL_PRESENT=4/4
C6_CONTROLS_PASS=4/4
C6_RECEIPT_KILLED=4/4
C6_RECEIPT_KILLED_ATTRIBUTED=4/4
C7_GATE_PRESENT=yes
C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
MUTANT check_embedded_outputs.py control exit=0 pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
MUTANT check_embedded_outputs.py c7 exit=1 killed :: drifted entry output accepted
C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
C7_V2_CLEAN=yes exit=0 :: checked_blocks=16 problems=0
C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
C7_V4_CLEAN=n/a (no v4 file)
C7_CONTROL_PASS=1/1
C7_MUTANT_KILLED=1/1
C7_MUTANT_KILLED_ATTRIBUTED=1/1
MUTANT check_embedded_outputs.py c7neg exit=1 killed :: drifted entry output accepted (spoofed)
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=yes
HOLDS_OK_V4=yes
HOLDS_OK_V5=yes
HOLDS_OK_V6=yes
```
<!-- replay-end -->

exit: 0 · stderr: empty · lines: 105 · sha256(stdout): `e1cf90f357a94da84ab65ee4ef6d17bc0dc034f95b5458c735d3cce21edd6f29`

---

# Addendum — the pinned counter cannot score the after-run (F4–F11)

Triggered by peer `L1Revenger69.R69ReviewC7Gate` (report `.ufo/waves/round-69/R69ReviewC7Gate.md`). Their claim reproduced exactly and widened into the defects below — F4 (crash), F5 (unreachable leg), F6 (exit status reads V1 only), F10 (all inherited and mis-certified by the round-68 receipt) — with the repair set in F7 and the convergence record in F9. **F11 is a separate, independent blocker on the build state itself** (the landed derivation extension broke `C7_V3_CLEAN`, so the tree is void by its own contract) and it survives any counter re-pin. **The MATCH verdict above stands** — my base-tree replay is still byte-identical to the committed receipt — but that receipt completed only because the base tree happens to lack the Q15 checker, so the crash path was never exercised. **C1 and C2 are not evaluable as pinned.**

## F4 (blocker) — `NameError: name 'run' is not defined` on every tree from `e1d22ca` onward

`reports/round-69/measure.py:158` calls `run(...)` at module top level; `def run` is at `:187`. Python executes top-level statements in order, so the call precedes the definition.

```
$ python3 -B reports/round-69/measure.py <tree of 35e12584 corpus-only>
EXIT=1
stdout lines: 22
C7_ labels printed: 0
stderr: Traceback (most recent call last):
  File "…/reports/round-69/measure.py", line 158, in <module>
    rc, last = run(TREE, "q15_tree_id_check.py", "--self-test")
NameError: name 'run' is not defined
```

Gate: the Q15 block runs iff `TREE/corpus/q15_tree_id_check.py` exists (`:156-157`). That file is `ABSENT at 222a7a7`, first present at `e1d22ca` — so **the red-before receipt completed by accident of the missing checker**, and any after-run tree (which necessarily contains it) crashes. `LANE` (`:30`), `TREE` (`:32`) and `C7_GATE_REL` (`:424`, used at `:446`) are all defined before use, so `run` is the *only* forward reference.

Severity: the crash exit is **1**, which the counter's own contract (`:19`) defines as "a hold failed" — the instrument reports a **false red against the claims** instead of exit 2 ("not evaluable"). It cannot signal its own unevaluability.

The Q15 checker itself is sound — it is only the call that is broken:

```
$ python3 -B <tree>/corpus/q15_tree_id_check.py --self-test
Q15_SELFTEST=pass (true sentence verified; false sentence killed)   EXIT=0
```

## F5 (blocker) — under the frozen invocation, `Q15_FALSE_KILLED=yes` is unreachable (silently)

The frozen invocation archives **only** `corpus`: `git archive <commit> corpus | tar -x -C <tree>`. But the D1 fixture the counter scans lives outside `corpus`:

- `measure.py:161` — `d1 = TREE / "reports/round-69/d1-false-sentence.md"`; `:168` prints `Q15_FALSE_KILLED=n/a (no d1 fixture)` and sets the flag `False` when absent.
- `git archive 35e12584 corpus` → `<tree>/reports` does not exist.

Measured with a diagnostic-only copy carrying just the F4 block move (7 insertions / 7 deletions, no other change; sha256 recorded in §F7):

| tree | `Q15_PRESENT` | `Q15_SELFTEST` | `Q15_FALSE_KILLED` | `Q15_RESTATE_OK` | exit |
|---|---|---|---|---|---|
| A: `corpus` only (frozen invocation) | `yes` | `pass` | **`n/a (no d1 fixture)`** | `n/a (no round-69 lesson)` | **0** |
| B: `corpus` + `reports/round-69/d1-false-sentence.md` | `yes` | `pass` | `yes exit=1 :: Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)` | `n/a (no round-69 lesson)` | 0 |

`diff A B` = exactly one line (A:24). So the fixture is the sole blocker, the label is reachable, and — critically — **the counter still exits 0 while the C2 leg is `n/a`**. C2's frozen predicate requires `Q15_FALSE_KILLED=yes` on the final measured tree; the registered invocation can never produce it.

## F6 (predicate integrity) — the claims' "counter exit code is 0" conjunct is vacuous for both claims

`measure.py:577` is `sys.exit(2 if not evaluable else 0 if holds_ok else 1)`. `holds_ok` (`:557-559`) is built from the C2–C7 fixture controls, `HOLD_REPLAY` and `FRESH_ROWS` only. **No `q15_*`, `c05_single_v4`, `c05_status`, `holds_c2_v4` or `c7_v4_clean` term reaches `evaluable` or `holds_ok`.**

**Wider, and verified: the exit expression reads V1 only.** `:577` names `evaluable` and `holds_ok` (V1, `:557-559`) and nothing else. `holds_ok_v2`…`holds_ok_v6` (`:561-575`) are each referenced exactly twice — their own definition and their `print(...)` — and never by the exit expression, so the whole V2→V6 ladder is printed and discarded:

```
$ sed -n '577p' measure.py | grep -oE "holds_ok(_v[0-9])?|evaluable|mismatch" | sort -u
evaluable
holds_ok
$ for v in 2 3 4 5 6; do grep -c "holds_ok_v$v" measure.py; done
3 3 3 3 2
```

Waiving witness (peer's construction, independently reproduced here): base archive `222a7a7` with only `corpus/knowledge/round-68-apk-axml-byte-evidence.md` deleted →

```
RC=0
C7_V3_CLEAN=n/a (no v3 file)
C7_V4_CLEAN=n/a (no v4 file)
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes … HOLDS_OK_V5=yes
HOLDS_OK_V6=no
```

A failed V6 does not move the exit code.

`evaluable` is no escape hatch either: it is set `False` only in the C2–C7 mutation branches (`:221,:272,:311,:355,:407,:459,:529,:534`), so exit **2 is unreachable for any claim leg**.

Consequence: the exit-code conjunct in both claims is not merely weak — it is **no gate at all**. Exit 0 survives `C7_V3_CLEAN=n/a`, `HOLDS_OK_V6=no`, `Q15_FALSE_KILLED=n/a`, and every claim label being `no`. Run A above is one witness (exit 0 with `Q15_FALSE_KILLED=n/a`); the deletion run above is another. D5 kill-rule-closure class, and the reason F4/F5 never surface as a red exit.

## F10 — the defect is inherited, and round-68's receipt states a false entailment about it

The round-69 counter is "the round-68 counter plus the round-69 labels", and the round-68 counter carries the identical unwired exit expression:

```
$ git show d00f779:reports/round-68/measure.py | sha256sum
0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766     # matches the sha claims.md cites
:523 holds_ok_v5 = (holds_ok_v4 and c7_targets)
:525 holds_ok_v6 = (holds_ok_v5 and c7_neg_killed == 1 and c7_neg_attributed == 0
:528 sys.exit(2 if not evaluable else 0 if holds_ok else 1)
```

So no round using this counter has ever had the C7 gate, the C4/C5/C6 arms, or even the README legend match (`mismatch` feeds `holds_ok_v2` at `:561-562`, also unread at `:577`) enforced through exit status. Peer `R69ReviewC7Gate` checked the ancestry: r67 `measure.py` @d00f779 exits on `holds_ok` at `:455` (V1 at `:439`), r68 at `:528` (V1 `:508`), r69 at `:577` — the same V1-only expression in all three.

Round-68's `measure-after.log:108` then certifies by that exit code:

```
counter exit code: 0 (the V1 holds hold; every V-label is yes)
```

Precision (peer's correction, adopted): the observation was **true of that run** — its `:93-98` shows every V-label `yes` — so this is not a false observation. What the code refutes is the **certification**: "exit code 0" does not entail "every V-label is yes", since exit 0 is emitted with `HOLDS_OK_V6=no` (witness above). It is a false *entailment* read off a real reading — still the D1 class (a meaning asserted against contradicting bytes), and outside Q15's current scope, which checks git object ids rather than the semantics of a mechanical signal. Recommended follow-up: a criterion that a stated meaning of a counter signal is re-derived by running that signal's own producer, plus the falsification control F7(3).

## F7 — repair set for a re-pinned counter (parent decision; I did not touch the frozen file)

1. Move the `def run(...)` block above the Q15 section. Minimal move measured here — 7 insertions / 7 deletions, no semantic change, exactly:

```diff
@@ -148,6 +148,13 @@
 print(f"FRESH_ROWS={fresh}/18")
 
+def run(tree, script, *args):
+    proc = subprocess.run([sys.executable, "-B", str(tree / "corpus" / script), *args],
+                          cwd=tree, capture_output=True, text=True, timeout=300)
+    tail = (proc.stdout + proc.stderr).strip().splitlines()
+    return proc.returncode, tail[-1] if tail else ""
+
+
 # Q15 calibration target (round-69): the tree-identity criterion.
@@ -182,13 +189,6 @@
 evaluable = True
-
-
-def run(tree, script, *args):
-    proc = subprocess.run([sys.executable, "-B", str(tree / "corpus" / script), *args],
-                          cwd=tree, capture_output=True, text=True, timeout=300)
-    tail = (proc.stdout + proc.stderr).strip().splitlines()
-    return proc.returncode, tail[-1] if tail else ""
 

The diagnostic copy was scratch and is deleted; no sha256 is claimed for it — re-derive from the diff above on any re-pin.
2. Widen the frozen archive to `git archive <commit> corpus reports/round-69/d1-false-sentence.md` (or archive the full commit) so `Q15_FALSE_KILLED` is reachable.
3. Wire the exit status to the *terminal* hold, not merely define a new one. Today `:577` reads `holds_ok` (V1) while V2–V6 are printed and discarded (F6), so adding `holds_ok_v7` without changing `:577` would reproduce the defect exactly. Write `sys.exit(2 if not evaluable else 0 if holds_ok_v7 else 1)` where `holds_ok_v7 = holds_ok_v6 and q15_present and q15_selftest and q15_false_killed and q15_restate and c05_single_v4 and c7_v4_clean` (`c05_single_v4`/`c7_v4_clean` matter: C1's own v4 gate is currently unwired too, `:492-493`). Add a self-test leg asserting that a deliberately falsified claim label yields a non-zero exit — otherwise nothing detects a re-wiring regression.
4. Add a crash guard: wrap the top-level body so an unexpected exception exits **2** (not 1), preserving the "1 = a hold failed" meaning.
5. Re-run **both** receipts under the new pin, and run the red-before on the *registration* tree as well as the claim base — a checker-present tree is the control that would have caught F4, F5 and F6 at registration time.

Until that re-pin, the honest status of this round's claims is **not evaluable**, not falsified: the pinned instrument cannot produce `Q15_*` (F4), cannot reach `Q15_FALSE_KILLED=yes` (F5), and its exit code does not measure either claim (F6). `claims.md`'s own rule ("The counter's sha256 is pinned … it is never edited after this revision") means the repair must be a new pre-registration revision with a new pinned sha — never an in-place edit of `reports/round-69/measure.py`.

## F8 — diagnostic artifacts (all in /tmp, deleted)

Trees `222a7a7:corpus` (`2c45edaf…`) and `35e12584:corpus`+fixture (`7aeabf21…`), patched copy `patched.py`, runs `A.out`/`B.out` were scratch under `/tmp/revenger-r69-replay2` and have been removed. Nothing in the lane was written except this report.

## F9 — peer cross-check (converged with `L1Revenger69.R69ReviewC7Gate`)

The peer reached the same three defects from the bytes independently, and settled one thing I had left open:

- **`checked_blocks=17` on both `C7_V3_CLEAN` and `C7_V4_CLEAN` is correct, not a defect.** The v3 and v4 embedded `$ cmd` lists are byte-identical (17 blocks each); the derivation block's *output* grew from 17 to 20 lines (v4 prints the live 20-line `derive_axml_anchors.py` output) without adding a block, and the S032/S034 source lines land in the header, not in a fence. `C7_V4_CLEAN=yes` stands; no claim from me.
- **Ordering of the repair.** F4 fires first and masks F5/F6: on any checker-present tree the counter never reaches the archive-dependent or exit-chain-dependent code. The repair must be sequenced block-move → archive widening → exit-chain wiring, each re-verified.
- **Vacuity enumeration (explicit).** The claim-specific labels that cannot influence exit status are: C2 — `Q15_PRESENT`, `Q15_SELFTEST`, `Q15_FALSE_KILLED`, `Q15_RESTATE_OK`; C1 — `C05_SINGLE_V4`, `HOLDS_C2_V4`, `C7_V4_CLEAN`. All seven are label-only — and per F6 the exit expression reads only V1, so the entire V2→V6 ladder is invisible as well, `HOLDS_OK_V6` and `C7_V3_CLEAN` included. The only claim-adjacent signal that is *wired* anywhere is the README legend `mismatch`, and it dies in `holds_ok_v2`, also unread.
- **Shared verdict:** C1 and C2 are **NOT EVALUABLE** with the pinned `bca74e6d…` counter — not falsified. The base-tree replay in §1–§7 is unaffected by all of this and remains byte-identical to `measure-before.log`.

## F11 (added last) — the build commit itself trips a declared void condition: the in-place derivation extension broke `C7_V3_CLEAN`

Independent of the counter defects, and surviving any re-pin. Measured on the **committed HEAD archive** (`35e12584:corpus`, `7aeabf21…`), not on the in-flux worktree, so this is build state and not a sibling's uncommitted edit. Re-verified after the tip moved to `1446da59` (`corpus` now `257643d9…`, `derive_axml_anchors.py` still `74d4c0d9…`): identical results, counter pin still `bca74e6d…`, and the committed `reports/round-69/measure-after.log` reports `counter exit code: 1`, `C7_V3_CLEAN=no … problems=7`, `HOLDS_OK_V6=no`. So the void-triggering state is **committed at the tip**, not a transient:

```
=== corpus/knowledge/round-67-apk-axml-byte-evidence.md  rc=0 :: checked_blocks=16 problems=0
=== corpus/knowledge/round-68-apk-axml-byte-evidence.md  rc=1 :: checked_blocks=17 problems=7
=== corpus/knowledge/round-69-apk-axml-byte-evidence.md  rc=0 :: checked_blocks=17 problems=0
```

The seven drifts, verbatim from the gate:

```
drift entry:137 embedded output line not in recheck stdout: enum RES_STRING_POOL_TYPE : 239
drift entry:138 … RES_XML_TYPE : 241
drift entry:139 … RES_XML_START_NAMESPACE_TYPE : 245
drift entry:140 … RES_XML_END_NAMESPACE_TYPE : 246
drift entry:141 … RES_XML_START_ELEMENT_TYPE : 247
drift entry:142 … RES_XML_END_ELEMENT_TYPE : 248
drift entry:143 … RES_XML_RESOURCE_MAP_TYPE : 253
```

**Mechanism, exactly.** The extension appended a value field to seven lines that already existed; nothing new was added for those symbols:

| v3 embedded (round-68, `:137-143`) | current derivation stdout |
|---|---|
| `enum RES_STRING_POOL_TYPE : 239` | `enum RES_STRING_POOL_TYPE : 239 = 0x0001` |
| `enum RES_XML_TYPE : 241` | `enum RES_XML_TYPE : 241 = 0x0003` |
| … seven lines … | … same seven, each with ` = 0xNNNN` appended |
| — | *and three genuinely new lines:* `enum block open : 237`, `enum block close : 263`, `enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100`, plus `comment/field attributeStart : 686/:687` |

`check_embedded_outputs.py` matches each embedded line against recheck stdout, so a reformat reads as drift even though every fact is unchanged.

Script identity is unambiguous — each entry cites the sha of the file it was derived with, and the file was edited in place between them:

```
git cat-file blob 222a7a7:corpus/derive_axml_anchors.py  | sha256sum → bce497d6…f1e249   # v3 S046 cite, "17 output lines"
git cat-file blob refs/heads/main:corpus/derive_axml_anchors.py | sha256sum → 74d4c0d9…2a83aa   # v4 S047 cite, "20 output lines"
```

**Consequence for the round.** `C7_V3_CLEAN=no` → `HOLDS_OK_V6=no` at the build commit. `claims.md` void list includes "`HOLDS_OK_V4`/`HOLDS_OK_V5`/`HOLDS_OK_V6` not yes", so **the tree as landed is void by its own contract**, before any counter question. This is a second, independent blocker: it would survive a perfect instrument. And it is self-inflicted by claims repair item 1 ("`corpus/derive_axml_anchors.py` is extended") interacting with the void condition "prior rejected candidates … keep every byte" — v3's bytes are untouched, but the shared script it was derived with is not.

**Repair that satisfies both entries.** The gate is **exact-line membership**, not substring: `corpus/check_embedded_outputs.py:84-85` reports `l not in stdout_set` for each quoted line, against `:104 stdout_set = set(stdout.splitlines())`. (Proof that substring matching is not what runs: all seven bare lines are *prefixes* of their valued counterparts, so a substring matcher would have printed `problems=0`, not 7 — the peer verified the same by quoting a strict prefix `enum block open` and getting `drift entry:3`, rc=1.) So the repair is a **superset of complete lines**: emit the original 17 lines byte-verbatim as their own complete lines, and additionally emit the value/extra lines. v3's block and v4's block are then both exact-line subsets of one stdout. Restate S047's "20 output lines" to the superset total. Alternative with the same property: restore `derive_axml_anchors.py` to `bce497d6…` and put the 20-line derivation in a round-scoped script that v4 cites. Both keep "prior candidates … every byte"; only editing v3 does not. Peer measured the one-wayness directly — `.ufo/waves/round-69/R69ReviewC7Gate.md:460-466`, "The one-way direction is **measured, not assumed**": an entry quoting a single line of the 20-line derivation stdout returns `checked_blocks=1 problems=0`, rc=0, `# rc=0 — no reverse check` — confirming no reverse check exists. **Pointer trap worth flagging for any later reader:** that same report's `:197` shows `checked_blocks=1 problems=0` too, but it is the *opposite* result — a deliberately weakened gate (`drift()` → `lines[:1]`) accepting a two-line block, i.e. a gate failing to catch drift (§F4, open D5). Same numbers, opposite meaning; cite `:460-466` for one-wayness and `:197` only for the weakening witness. Caveat on the superset form: it prints the seven symbols in two forms, so a future uniqueness or two-way rule would re-break both entries — the round-scoped script is the durable form, and it is the one I would recommend if only one is taken. (Sibling `measure-after.log` reported the drift first; §F11 confirms the attribution on committed archives at both `35e12584` and the current tip.)
