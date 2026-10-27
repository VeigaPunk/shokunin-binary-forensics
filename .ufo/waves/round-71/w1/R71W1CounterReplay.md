# R71W1CounterReplay — base replay, control-D replay, frozen vote-parser refusal probe

**Base replay is faithful on the amended freeze (46/46 lines, 10/10 HOLD rows, exit 0, only the `MEASURE_EXIT` trailer absent) and control D reproduces 45/45 metric lines under the pre-amendment counter and 44/45 under A1 (the timeout row correctly flips to traceback=yes), but the frozen votes-dir parser still has two refusal gaps — a valid-JSON non-object vote file crashes the counter to exit 2 with a traceback instead of a red hold, and duplicated JSON keys let `"Q01":"FAIL","Q01":"PASS"` read as PASS — and A1 leaves the control-D receipt and the gate wall-time expectation stale.**

seat: `R71W1CounterReplay` · wave 1 (advisory pre-gate) · measured 2026-10-27 12:18–12:33 -03
lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`, HEAD `18200a4`, base `b7abcd8`
final frozen bytes measured: `reports/round-71/measure.py` = `fbd81050…` (173 lines, = HEAD blob `d0d59b79…` + amendment A1's one-line fixture path), `claims.md` = `1febae12…`, `measure-before.log` = `7a942804…`
scratch: `/fast/scratch/hyaku/revenger-r71/R71W1CounterReplay/` (deleted after receipts copied here)
No seat judges the round; everything below is measured evidence and repair recommendations for L1.

## 1. Receipts (hashes and exits)

| object | sha256 / value |
|---|---|
| counter, pre-registered (`pre-registration.txt:4`) | `d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c` (= `git show 18200a4:reports/round-71/measure.py`) |
| counter, amended A1 (`pre-registration.txt:9`) | `fbd81050930657375f7314123ef468e66337b69adee12ce8416bb5dc98cff8f5` |
| claims (`pre-registration.txt:5`) | `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5` (identical at HEAD and worktree) |
| red-before, amended | `reports/round-71/measure-before.log` `7a9428048825e542139670a462e3d6067466c5a8157b2e3c0bdcb22c9f761407`, mtime 12:28:29 |
| red-before, superseded | 12:11:25 capture, `C2_TIMEOUT_EXIT2=… stderr_traceback=no` |
| `pre-registration.txt` at close | `d3c9263af55819d316eee4c94e009ad21433ed5eda849a66716278c83060f4bf` (lines 9–10 = A1 + corrected red-before) |
| my base replay stdout (amended counter) | `73326a3c4942043aac6e717eb4017bb0078b4ad86979de9b3c042bf8a2bd4420`, `EXIT=0`, stderr 0 bytes, 10 `HOLD` lines |
| my base replay stdout (pre-amendment counter) | `9c204c5326dcfc56ac9e36d5d557bb64f9db02ddefc55ab5434a942ed8299d0e`, `EXIT=0`, identical to the 12:11 receipt except its trailer |
| control D v6 bytes | `269da7bf691dc69b4bb4a148581c37c3ae401c621b79a78f998f537f668359f0` |

Base tree built exactly as `build-controls.py:19-25` does (`git archive b7abcd8 corpus SHONEN.md SCORECARD.md SKILL.md`). Scratch set via `HYAKU_SCRATCH`; the counter removes its own scratch in `main()`'s `finally` (`measure.py:69`).

## 2. Base-archive replay vs `measure-before.log`

Amended counter (`fbd81050…`) on base:

```
$ diff -u reports/round-71/measure-before.log base-replay.bare
@@ -45,4 +45,3 @@
 F_COVERAGE=5/8 score=6.2
 FRESH_ROWS=18/18
 HOLDS_OK_V8=yes
-MEASURE_EXIT=0
```
`DIFF_STATUS=1`, one hunk, one line: the trailer the recording harness appends. All 46 numbered lines reproduce, **including all ten `HOLD` rows** (`HOLD_REPLAY=10/10`): `verify_evm_evidence.py`, `verify_icon_languages.py`, `verify_icon_states.py`, `verify_js_graph_delta.py`, `verify_multi_icon_states.py`, `verify_named_multi_icon_states.py`, `verify_pe_resources.py`, `verify_saved_evidence.py`, `verify_semantic_trace.py`, `verify_shape_evidence.py`, each `exit=0`.

Key reproduced rows: `K_HELD_BACKED=8/14 score=5.7`, `K_HELD_BACKED_STRICT=8/14`, `C05_STATUS=uncovered`, `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`, `C2_MISSING_ENTRY_EXIT2=0/1 rc=1 stderr_traceback=yes`, `C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=yes`, `C2_GATE_SELFTEST=0 named_legs=0`, `HOLDS_C2_V1=no`, `SELF_MISMATCH=0 exit=0`, `SELF_CLEAN_FIXTURE=1`, `SELF_MUTANTS_KILLED=6/6`, `GATE_SELFTEST=exit 0`, `F_COVERAGE=5/8 score=6.2`, `FRESH_ROWS=18/18`, `HOLDS_OK_V8=yes`, `EXIT=0`.

Determinism: two runs with identical counter bytes were line-identical (`RUN2_IDENTICAL=yes` at the pre-amendment generation).

Pre-amendment cross-check (measured before A1 landed, counter then on disk `d0d59b79…` at 12:21 and a transient worktree variant later): that counter reproduced the **12:11** receipt byte-for-byte too (diff again only the `MEASURE_EXIT` trailer, stdout `9c204c53…`), but the whole counter run finished in **2.11 s wall**. A 300-second sleeper behind a real 120-second gate timeout cannot finish in 2 s, so the 12:11 receipt's timeout leg never reached the timeout: it recorded a fast `command exited 2` drift (`stderr_traceback=no`). That is the defect amendment A1 describes; the amended run takes ~2 min and correctly reports `stderr_traceback=yes` on base. A1 is therefore materially correct, and the pre-amendment `C2_TIMEOUT_EXIT2` red row was measuring the wrong thing even though both generations print `0/1`.

## 3. Freeze timeline (measured, for the receipt)

- 12:11:25 `measure-before.log` recorded (pre-amendment).
- 12:21:0x `measure.py` = `d0d59b79…` = pre-registered; `claims.md` = `1febae12…`; `w1.ready.dispatched` 12:21.
- 12:21:41–12:23:18 worktree `claims.md`/`measure.py` carried an uncommitted rewrite (claims `5b95d34…`, counter 201 lines `a86c6a95…`/`39e92bab…`) that replaced the votes-dir parser with a single `.ufo/waves/round-71/w2-results.json` parser. At that moment the receipt's SHAs did not describe the on-disk bytes, and `git diff reports/round-71/` showed 53 changed counter lines plus 6 claims lines.
- 12:26–12:28 the rewrite was reverted: `claims.md` back to `1febae12…`, counter to `fbd81050…` (HEAD `d0d59b79…` + one line), `measure-amendment-A1.md` added, `pre-registration.txt:9` amended, `measure-before.log` re-run to `7a942804…`.

Residual risk is narrower than the churn suggests: by 12:33 the receipt was internally reconciled — `pre-registration.txt:9` records amendment A1 and the `fbd81050…` counter SHA, and line 10 records the corrected red-before (exit 0, C2 both `stderr_traceback=yes`, `HOLD_REPLAY=10/10`, `HOLDS_OK_V8=yes`, all ten HOLD lines), which matches my replay exactly. What remains is that one receipt now carries two counter SHAs: line 4 (`d0d59b79…`, the frozen baseline) and line 9 (`fbd81050…`, operative). Recommend the validator read line 9 as operative and that any checker comparing `sha256sum reports/round-71/measure.py` only against line 4 be amended, otherwise a correct gate run reads as a freeze violation.

## 4. Strongest do-nothing control D — replayed

D rebuilt from base with the registered builder's own mutation (`build-controls.py` imported; `dcontrol()` = README C05 flip + round-70 v5.1 bytes at the v6 path + `admission-status: admitted` + Q16 row), then the counter run.

Pre-amendment counter (`39e92bab…`), full registry diff against `controls/D-C1-v5-copy-with-q16.log`:

```
@@ -45,4 +45,4 @@
-CONTROL=D-C1-v5-q16-vote-control EXIT=0
+CONTROL=D-C1-v5-copy-with-q16 EXIT=0
```
**45/45 metric lines identical** — `K_HELD_BACKED=9/14`, `C05_STATUS=held`, `C05_SINGLE_V6=yes`, `V6_ADMITTED_MARKED=yes`, `C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes`, `C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0`, `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`, `HOLDS_OK_V8=yes`, `EXIT=0`. D stays red only on the vote conjunct, as `claims.md:17` asserts.

Two defects in that receipt surface here:
- The registered trailer label `D-C1-v5-q16-vote-control` is not what the builder emits (`build-controls.py:82` passes `D-C1-v5-copy-with-q16`), so the D log is not byte-reproducible by the registered builder.
- `SELF_MISMATCH=1 exit=1` appears in D while the counter prints `HOLDS_OK_V8=yes` and exits 0: `self_ok` is computed at `measure.py:138` and never used; `holds` at `measure.py:163` is `ok==len(ps)==10 and frc==0 and len(present)==5 and fresh==18`. The instrument that catches D's forged tree cannot influence the exit code; only reading `HOLDS_C1_V6` does.
- By `measure.py:92`, `c1` needs only K/status/path/admitted/gate/lint/votes, so with D's already-green gate, lint and K=9/14 a 16/16 vote file alone flips `HOLDS_C1_V6=yes` [INFERENCE from code + measured D rows; writing `w2-results.json`/`w2-votes` under the lane is outside this seat's write scope]. All discrimination against D therefore rests on the four vote files.

Amended-counter (`fbd81050…`) D replay, diff against the registered log = **two lines**:

```
-C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=no
+C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=yes
-CONTROL=D-C1-v5-q16-vote-control EXIT=0
+CONTROL=D-C1-v5-copy-with-q16 EXIT=0
```
The other 44 metric lines are identical, including `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`, `SELF_MISMATCH=1 exit=1`, `HOLDS_OK_V8=yes`, `EXIT=0`; the run took ~140 s wall instead of ~3 s. So `controls/D-C1-v5-copy-with-q16.log` is superseded by A1: its timeout row records the broken fixture path (`command exited 2`, no traceback), not the production timeout. Re-run D under `fbd81050…` if the controls are to remain byte-reproducible receipts.

## 5. Frozen vote-parser refusal matrix

Frozen parser is the per-seat votes-dir form (`measure.py:49-62`): `root=LANE/'.ufo/waves/round-71/w2-votes'`, `path.stem == seat`, `set(decisions) == set(expected)`, `value in ('PASS','n/a')`, no repeated Q. Probed with a copy whose only change is the `LANE=` constant (diff = 1 hunk, 4 changed lines), all under scratch:

| fixture | `q_votes()` |
|---|---|
| A0 directory absent | 0 |
| A1 four valid per-seat files, 16 PASS | 16 |
| A2 malformed JSON text in one file | 0 |
| A3 one `FAIL` value | 0 |
| A4 seat missing one assigned Q | 0 |
| A5 file stem ≠ `seat` | 0 |
| A6 duplicate seat via extra `_dup.json` stem | 0 |
| A7 unknown seat name | 0 |
| A8 stray `stray.JSON` malformed file | **16** (ignored, not refused) |
| A9 raw duplicate decision key `"Q01":"FAIL","Q01":"PASS"` | **16** |
| A10 raw duplicate `"seat"` key (unknown then valid) | **16** |
| A11 `n/a` values | 16 |
| A12 valid JSON that is a list | **AttributeError** |
| B1 `decisions` is a list (dict check) | 0 |
| B2 `decisions` is a list of dicts | 0 |
| B3 file contains a JSON string | **AttributeError** |
| B4 file contains a JSON number | **AttributeError** |
| B5 `seat` key absent | 0 |

The refusals that matter are correct: malformed text, FAIL, missing Q, wrong stem, duplicate seat, wrong/absent seat all return 0. Two gaps:

1. **Duplicate keys are last-wins, not refused** (A9/A10). `json.loads` collapses `"Q01":"FAIL","Q01":"PASS"` to PASS, so a reviewer JSON object that both fails and passes Q01 scores 16/16. `claims.md:11` requires "no FAIL/duplicate". Repair: parse with `object_pairs_hook` and return 0 on any duplicate key inside the file or inside `decisions`.
2. **Valid JSON that is not an object crashes the parse** (A12/B3/B4). `measure.py:55` calls `data.get('seat')` after the guarded `json.loads`, and the guard only catches `OSError/ValueError/UnicodeError`, so a list/string/number vote file raises `AttributeError`. End-to-end, with such a file present and everything else valid:

```
$ python3 -B counter-amended-patched.py base-tree ; echo RC=$?
K_HELD_BACKED=8/14 score=5.7
…
C1_LINT=n/a
COUNTER_ERROR=uncaught exception (exit 2)          # RC=2
stderr: File "…/measure.py", line 55, in q_votes
        seat=data.get('seat'); expected=EXPECTED_VOTES.get(seat)
        AttributeError: 'list' object has no attribute 'get'
```
All rows printed after line 10 are lost (`C1_W2_Q_VOTES`, `HOLDS_C1_V6`, both C2 legs, all ten `HOLD` rows, `HOLDS_OK_V8`). The receipt's contract (`pre-registration.txt:8`) is "1 a named hold red, 2 could not evaluate"; a malformed vote file should keep `HOLDS_C1_V6=no` and exit 1, not destroy the rest of the receipt. Repair: require `isinstance(data, dict)` inside the existing `try`, or return 0 on non-dict.

Minor: A8 shows `*.json` case-sensitivity — a malformed `stray.JSON` in the votes directory is silently ignored rather than refused. Harmless for the count, worth a line in the claims if intentional.

## 6. Operability notes for the gate

1. **Gate wall time**: with A1, every counter run pays the full 120-second production timeout (`measure.py:101-103` writes the sleeper, `gate_cli` waits), so a gate run is ~2 min longer than the 12:11 receipt implies. Budget for it; do not let an outer harness timeout (e.g. 120 s) kill the run and be mistaken for exit 2.
2. **C1 vote leg is outside the measured tree**: `measure.py:50` reads a lane-absolute path, so a `git archive` of the final tip alone cannot reproduce `C1_W2_Q_VOTES`; the gate must also pin the sha of the four `.ufo/waves/round-71/w2-votes/*.json` files (or commit them) for the receipt to be replayable. My base replay is green only because that directory is absent.
3. **`SELF_MISMATCH` is advisory**: it is printed and ignored (`measure.py:138,163`); if it is meant to gate, wire it into `holds`; if not, say so in the claims so a control like D is not read as "counter green, therefore fine".
4. **Control-D receipt**: fix the builder/registry label mismatch (`build-controls.py:82` vs the log's `CONTROL=D-C1-v5-q16-vote-control`) and re-run D under `fbd81050…` so its timeout row matches A1.

## 7. Scope, sources, tooling

- Writes: only `.ufo/waves/round-71/w1/R71W1CounterReplay.md` plus scratch. No lane source, no votes directory, no `w2-results.json`, no git/jj mutation, no fleet-root/sibling-lane writes, no `agent://all`, no subagent dispatch beyond the single labrat.
- New source rows opened: none (lane code, receipts, control logs only), so no Gate source quotes are owed from this seat.
- Tooling: nothing installed or updated; Python 3 stdlib only; no pacman transactions.
- Scratch `/fast/scratch/hyaku/revenger-r71/R71W1CounterReplay/` deleted after these receipts were copied; `base-tree`, `D-tree`, `fakelane` and the counter's own `revenger-r71/counter` scratch removed.
