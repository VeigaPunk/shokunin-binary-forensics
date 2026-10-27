# R71W1ScorecardDraft — SCORECARD rows drafted (C1 K 8/14→9/14; C2 calibration leg measured 1/1 under amendment A1)

**Verdict: draft complete, advisory only.** Both rows are drafted in the round-70 table form
(`SCORECARD.md:629`, columns `axis / criterion | before → after | counting command | measured commits | verdict`),
with the exact command and a measured-revision *slot*; no scalar is recorded and **SCORECARD.md was not edited**.
The C2 leg now has a measured after-state: under declared pre-wave-2 counter amendment A1 (`measure.py` sha
`fbd81050…`), the build tree `18200a4` prints `C2_MISSING_ENTRY_EXIT2=1/1`, `C2_TIMEOUT_EXIT2=1/1`,
`C2_GATE_SELFTEST=0 named_legs=1`, `HOLDS_C2_V1=yes` — the row may be written as declared, measured at the final
tip. I found (and the Sentinel independently found) the pre-A1 fixture defect that made that leg unreachable; A1
repairs it by one command-path line and it is recorded (§3a, §4). C1's after-state stays a slot: at `18200a4` the
gate/lint conjuncts are already green but `C1_W2_Q_VOTES=0/16` and the v6 header is still `candidate`, so
`HOLDS_C1_V6=no`. Also recorded, not judged: the frozen counter and claims were edited and reverted mid-wave (§4).

## 1. Axes (named)

| axis | criterion | what the row must show |
|---|---|---|
| coverage | `HOLDS_C1_V6` (C05 sixth pass, K) | 8/14 → 9/14 plus every conjunct of the frozen predicate at the adjudication tip |
| calibration | `HOLDS_C2_V1` (gate exit-2 classification) | both named legs 0/1 → 1/1, self-test exit 0, hold labels unchanged |

## 2. Row drafts (paste-ready; slots in `<…>`, nothing here is a measurement of the after-state)

Command text is identical for both rows; it is the only form I ran (see §3), and it differs from the counter's
docstring (`reports/round-71/measure.py:2` says "git archive corpus snapshot") because `measure.py:169` refuses a
TREE without `TREE/corpus`. A corpus-only archive exits 2 at that guard:

```
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive <commit> | tar -x -C <tree> \
  && cd / && HYAKU_SCRATCH=/fast/scratch/hyaku/revenger-r71/<seat> \
     python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-71/measure.py <tree>
```

**Row C1** — drafted:

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| coverage — knowledge-map ground K (C05 sixth pass) | `K_HELD_BACKED` 8/14 → 9/14; `K_HELD_BACKED_STRICT` 8/14 → 9/14; `C05_STATUS` `uncovered` → `held`; `C05_KNOWLEDGE_COLUMN` `—` → `knowledge/round-71-apk-axml-byte-evidence.md` (`C05_SINGLE_V6` no → yes); `V6_ADMITTED_MARKED` no → yes; `C1_GATE` n/a → `checked_blocks=24 problems=0 exit=0`; `C1_LINT` n/a → `LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0`; `C1_W2_Q_VOTES` 0/16 → 16/16; `HOLDS_C1_V6` no → yes — predicate keys and counts only, **no scalar** | exact command above (`report-71/measure.py`) | `b7abcd8` (red-before) → `18200a4` (wave-1 build, **pre-gate observation** in §3) → `<adjudication tip: the single commit that flips the v6 header to `admitted`, flips only C05 to `held` with the v6 path, and appends this row>` — after-state **unmeasured** (slot only) | draft; C1 not claimable until the wave-2 decision conjunct is 16/16 at that tip |

Before-cell provenance: `reports/round-71/measure-before.log` as committed at `63b560b` (`K_HELD_BACKED=8/14`, `C05_STATUS=uncovered`,
`C05_KNOWLEDGE_COLUMN=-`, `C1_GATE=n/a`, `C1_LINT=n/a`, `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`; the same file holds
`C2_MISSING_ENTRY_EXIT2=0/1 rc=1 stderr_traceback=yes`, `C2_TIMEOUT_EXIT2=0/1`, `HOLDS_C2_V1=no`). The working-tree
copy was 0 bytes while A1's re-run was being produced.
After-key provenance is the frozen predicate in `reports/round-71/claims.md` §C1 — not a run.

**Row C2** — drafted against the amended counter (A1, `measure.py` sha `fbd81050…`); the after-state below was
measured at the build tree, and must be re-measured at the final tip:

| axis / criterion | before → after | counting command | measured commits | verdict |
|---|---|---|---|---|
| calibration — declared could-not-evaluate outcomes for the registered embedded-output gate | `C2_MISSING_ENTRY_EXIT2` 0/1 (`rc=1 stderr_traceback=yes`) → 1/1 (`rc=2 stderr_traceback=no`); `C2_TIMEOUT_EXIT2` 0/1 (`rc=1`) → 1/1 (`rc=2 stderr_traceback=no`; pre-A1 counter read 0/1 `rc=1` because its probe command did not resolve — §3a, repaired by A1); `C2_GATE_SELFTEST` `exit 0 named_legs=0` → `exit 0 named_legs=1`; `HOLDS_C2_V1` no → **yes** | exact command above, counter sha `fbd81050…` | `b7abcd8` (red-before) → `18200a4` (wave-1 build, measured under A1: legs 1/1 and 1/1, self-test exit 0 with both legs named) → `<final measured tip>` (slot; re-measure under A1) | draft — after-state measured at the build tip, final row must cite the adjudication tip |

Registry row check (not a claim, a locator): `SKILL.md:296` names both mappings — "the live CLI returns exit 2 with
`could-not-evaluate: entry not found:` or `could-not-evaluate: command timed out after 120s:` and no traceback.
Counter labels: `C2_MISSING_ENTRY_EXIT2`, `C2_TIMEOUT_EXIT2`".

**Why no scalar.** The seat spec forbids a scalar in these rows. The counter prints its own derived field
(`measure.py:77`, `K_HELD_BACKED=<n>/<n> score=…`); I transcribe only the counts and predicate keys and leave any
criterion number to L1 at adjudication. Do not lift `score=` from my logs into the row without saying it is the
counter's field, not a measurement I took of the after-state.

## 3. Observed build-state evidence (pre-gate; advisory, not the after-state)

Tree: whole-lane `git archive 18200a4b18e8dfce291a74028a9012ce4401ca10` (build commit
"round-71: build v6 candidate and gate exit-2 cases"). Log: `counter-build.log`, exit 0, wall 4.9 s.

```
K_HELD_BACKED=8/14 score=5.7
K_HELD_BACKED_STRICT=8/14
C05_STATUS=uncovered
C05_KNOWLEDGE_COLUMN=-
C05_SINGLE_V6=no
V6_ENTRY_PRESENT=yes
V6_ADMITTED_MARKED=no
C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
C1_W2_Q_VOTES=0/16
HOLDS_C1_V6=no
C2_MISSING_ENTRY_EXIT2=1/1 rc=2 stderr_traceback=no
C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=no
C2_GATE_SELFTEST=0 named_legs=1
HOLDS_C2_V1=no
```

`HOLDS_OK_V8=yes` on the same run (holds not disturbed). So at the build revision only the vote conjunct and the
`admitted` header are missing on C1 — exactly the two wave-2-dependent keys — and K stays 8/14 because the C05
knowledge column is still `—` (`corpus/README.md:45` status `uncovered`).

### 3a. Located C2 timeout defect (fixture, not gate) — **repaired by amendment A1 before wave-2 scoring**

- Counter writes the sleeper to `<scratch>/timeout-fixture/corpus/sleeper_r71.py` (`measure.py:101`), the entry to
  `…/corpus/knowledge/round-71-timeout-probe.md` (`:100-103`, block text `$ python3 -B sleeper_r71.py` in the frozen
  `d0d59b7…` bytes), and runs `gate_cli(<fixture>, …)` which executes the gate with `cwd=<fixture>`
  (`measure.py:39-40`; leg at `:104-109`).
- The gate evaluates from the invocation cwd, not the entry's directory — `evaluate(args[1], Path.cwd())`
  (`corpus/check_embedded_outputs.py:297`) — and `run_cmd` passes that cwd to the child (`:111-112`), matching every
  existing entry, whose blocks are root-relative (`corpus/knowledge/round-70-apk-axml-byte-evidence.md:26`,
  `$ python3 -B corpus/fixtures/apk-r65/readout.py …`).
- Consequence under the frozen counter, reproduced directly from the same fixture shape:
  `drift entry:2 command exited 2: python3 -B sleeper_r71.py` / `checked_blocks=0 problems=1` / `RC=1` — the child
  exits 2 because the script is one directory away, so the gate never reaches its 120 s timeout and
  `C2_TIMEOUT_EXIT2` read `0/1` at every tree, product code notwithstanding.
- Proof the gate is right, with the fixture at the tree root (`probe2/sleeper_r71.py`, everything else identical):
  `could-not-evaluate: command timed out after 120s: python3 -B sleeper_r71.py`, `real 2m0.123s`, `RC=2`, no
  traceback.
- Minimal repair (fixture-only; confinement and the 120 s limit untouched): declare `$ python3 -B
  corpus/sleeper_r71.py` and keep the sleeper under `corpus/`, or write it beside the tree root. L1 did exactly the
  first as **pre-wave-2 amendment A1** (`reports/round-71/measure-amendment-A1.md`; counter `d0d59b7…` →
  `fbd81050…`, one-line delta, C1 vote source and all predicates/targets/kill rules unchanged;
  `pre-registration.txt` now carries the A1 line). I did not edit it.
- Post-A1 measurement (mine, this seat): counter `fbd81050…` on `18200a4` prints `C2_TIMEOUT_EXIT2=1/1 rc=2
  stderr_traceback=no`, `C2_MISSING_ENTRY_EXIT2=1/1`, `C2_GATE_SELFTEST=0 named_legs=1`, `HOLDS_C2_V1=yes`, exit 0,
  wall 124.8 s. Convergence: `R71W1Sentinel.md:46-58` (§F1) located the same defect independently; its §5 records
  L1's in-session intent to make the same narrow correction.

## 4. Recorded, not judged: the frozen counter and claims were edited, then reverted, mid-wave

Sequence I observed on the same two paths (no edit by me; `git status` for both paths is clean now):

1. First read, start of seat — bytes matched the pre-registration:
   `d0d59b7…d06c` `reports/round-71/measure.py`, `1febae1…3f5` `reports/round-71/claims.md`.
2. Mid-seat — `git status` showed ` M reports/round-71/claims.md` and ` M reports/round-71/measure.py`, and
   `sha256sum` read `39e92babebc5b3550f01583e360ea77211e0f0f2b9af45725d70acd1c1affcec` /
   `5b95d343b7f2e5c228d22f7de4dd4d43cb9b1844e4709969d07129c6acc1d19b`. The diff replaced the per-seat
   `w2-votes/*.json` source with a single `LANE/.ufo/waves/round-71/w2-results.json`, added a `vote_pairs()`
   text/JSON scraper (`Qnn: PASS|n/a|FAIL` regex, recursive dict/list walk), relaxed the match to
   `value.upper() in ('PASS','N/A')`, and reworded `claims.md` §C1 and its do-nothing-control paragraph to match
   (measure.py:202 lines at that moment).
3. End of seat — reverted to the frozen bytes: `sha256sum` again `d0d59b7…d06c` / `1febae1…3f5`, both paths `git
   status` clean, mtime `2026-10-27 12:25:30 -0300`, measure.py back to 173 lines — which is why every locator in
   this report uses the frozen numbering. Only an untracked `reports/round-71/__pycache__/` remains in the lane
   (not mine: every command I ran used `python3 -B`).
4. Then, same minute, the recorded remediation: `reports/round-71/measure-amendment-A1.md` appears, `pre-registration.txt`
   gains one line ("Pre-wave2 counter amendment A1 … counter SHA now `fbd81050…`. Only the timeout fixture command
   path changed … This correction is made before wave-2 scoring."), `measure.py` is `fbd81050…` with the single
   hunk `sleeper_r71.py` → `corpus/sleeper_r71.py` (§3a), and `measure-before.log` is momentarily **0 bytes** while
   A1's red-before re-run is produced (A1 states it "replaces the prior receipt before any wave-2 scoring"). The
   claims file is back to `1febae1…` and its A1 note says the C1 vote source remains the per-seat `w2-votes/*.json`
   predicate, i.e. the `w2-results.json` variant of stage 2 was withdrawn.

Claims state "Frozen predicates, counter and kill rules below may not change after any seat scores"
(`reports/round-71/claims.md:8`); wave-1 seats were scoring throughout. I neither made nor reverted those changes and
judge none of them; the sequence is recorded because the row's counting command and before-cell must name the
revision actually used. One factual note: my counter runs bracket stages 2–4 and the C1 keys are **byte-identical**
across the frozen and `39e92ba…` revisions (`diff counter-build.log counter-build-rev39e92ba.log` → empty, both exit
0), because `.ufo/waves/round-71/w2-results.json` and `…/w2-votes/` are both absent at the build tree, so every C1
key quoted in §3 holds on all revisions; only the vote key's *source path* differs (`C1_W2_Q_VOTES=0/16` either
way). The C2 keys are the exception and required A1: `C2_TIMEOUT_EXIT2` goes `0/1` → `1/1` between `d0d59b7…` and
`fbd81050…` on the identical tree.

## 5. Touched surfaces

- Written: this report only. No SCORECARD/README/claims/measure.py/entry/gate edit, no git or jj mutation, no
  commit, no spawn, no `agent://all`.
- Scratch `/fast/scratch/hyaku/revenger-r71/R71W1ScorecardDraft/` — created, used for the archive tree, both counter
  logs, the self-test log, and the two gate probes; receipts are quoted above; **deleted** before returning.
- No source row was opened this round (no SOURCES/SKILL source-tree reading beyond the gate registry locator at
  `SKILL.md:296`), so no access-date/≤25-word quote is owed by this seat.

## 6. Out of scope / limits

- Wave 1 is advisory: the C1 after-state is a slot, not a measurement; K 9/14, `C05_STATUS=held` and `16/16` are
  unverified at any tip. The C2 after-state *is* measured, but only at the build tip `18200a4` under A1 — the final
  row must re-measure at the adjudication tip.
- A1's own red-before re-run was not visible to me as a file: `reports/round-71/measure-before.log` was 0 bytes when
  I last read it. I therefore ran the amended counter on base `b7abcd8` myself (§7, last block): both C2 legs stay
  `0/1` with tracebacks and `HOLDS_C2_V1=no`, so A1 does not move the before-state. That run is mine and is not a
  substitute for the registered receipt.
- The withdrawn `w2-results.json` variant's soundness (a PASS scraped from prose by regex, `n/a` vs `N/A` casing) is
  untested here and is moot under A1's restored per-seat predicate — a wave-2/critic question, not mine.
- No scalar recorded for either axis, per the seat spec; the counter's own `score=` field is left as printed.

## 7. Appendix — receipts (copied here because the scratch dir is deleted)

Full counter output on `git archive 18200a4…` (identical on the frozen `d0d59b7…` and the transient `39e92ba…`
revisions; exit 0):

```
K_HELD_BACKED=8/14 score=5.7
K_HELD_BACKED_STRICT=8/14
C05_STATUS=uncovered
C05_KNOWLEDGE_COLUMN=-
C05_SINGLE_V6=no
V6_ENTRY_PRESENT=yes
V6_ADMITTED_MARKED=no
C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
C1_W2_Q_VOTES=0/16
HOLDS_C1_V6=no
C2_MISSING_ENTRY_EXIT2=1/1 rc=2 stderr_traceback=no
C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=no
C2_GATE_SELFTEST=0 named_legs=1
HOLDS_C2_V1=no
EMB_R65=checked_blocks=15 problems=1 exit=1
EMB_R67=checked_blocks=16 problems=0 exit=0
EMB_R68=checked_blocks=17 problems=0 exit=0
EMB_R69=checked_blocks=17 problems=0 exit=0
EMB_R68_BYTES_UNCHANGED=yes
EMB_R65_BYTES_UNCHANGED=yes
EMB_PINNED_SCRIPT_IS_S046=yes
EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1
SM1=0
SM2=0
SM3=0
SM4=0
SM5=0
SM6=0
SELF_MISMATCH=0 exit=0
SELF_CLEAN_FIXTURE=1
SELF_MUTANTS_KILLED=6/6
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validatio
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_REPLAY=10/10
GATE_SELFTEST=exit 0
F_COVERAGE=5/8 score=6.2
FRESH_ROWS=18/18
HOLDS_OK_V8=yes
```

Gate self-test on the same tree (`python3 -B corpus/check_embedded_outputs.py --self-test`, exit 0):

```
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed
```

Gate timeout probe, counter fixture shape (`sleeper_r71.py` under `corpus/`, gate cwd = tree):

```
drift entry:2 command exited 2: python3 -B sleeper_r71.py
checked_blocks=0 problems=1
RC=1
```

Gate timeout probe, sleeper at the tree root (`sleeper_r71.py` beside `corpus/`, gate cwd = tree):

```
could-not-evaluate: command timed out after 120s: python3 -B sleeper_r71.py
real 2m0.123s
RC=2   (no traceback on stdout or stderr)
```

### Amendment-A1 counter (`fbd81050…`), two trees, this seat's runs

`18200a4` (build), exit 0, wall 124.8 s — the C2 and C1 conjuncts only; every other key matches the block above:

```
K_HELD_BACKED=8/14 score=5.7
C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
C1_W2_Q_VOTES=0/16
HOLDS_C1_V6=no
C2_MISSING_ENTRY_EXIT2=1/1 rc=2 stderr_traceback=no
C2_TIMEOUT_EXIT2=1/1 rc=2 stderr_traceback=no
C2_GATE_SELFTEST=0 named_legs=1
HOLDS_C2_V1=yes
HOLDS_OK_V8=yes
```

`b7abcd8` (base), exit 0, wall 122.3 s — the target is red under the same amended counter, so A1 does not move the
before-state (this is my run, not a substitute for L1's re-run receipt):

```
K_HELD_BACKED=8/14 score=5.7
K_HELD_BACKED_STRICT=8/14
C05_STATUS=uncovered
C05_KNOWLEDGE_COLUMN=-
C05_SINGLE_V6=no
V6_ENTRY_PRESENT=no
V6_ADMITTED_MARKED=no
C1_GATE=n/a
C1_LINT=n/a
C1_W2_Q_VOTES=0/16
HOLDS_C1_V6=no
C2_MISSING_ENTRY_EXIT2=0/1 rc=1 stderr_traceback=yes
C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=yes
C2_GATE_SELFTEST=0 named_legs=0
HOLDS_C2_V1=no
```

The rest of that base run: `EMB_R65=checked_blocks=15 problems=1 exit=1`, `EMB_R67/68/69` problems 0, the three
byte/pin labels `yes`, `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1`, `SELF_MISMATCH=0 exit=0`,
`SELF_MUTANTS_KILLED=6/6`, ten `HOLD … exit=0` lines, `HOLD_REPLAY=10/10`, `GATE_SELFTEST=exit 0`,
`F_COVERAGE=5/8 score=6.2`, `FRESH_ROWS=18/18`, `HOLDS_OK_V8=yes`.
