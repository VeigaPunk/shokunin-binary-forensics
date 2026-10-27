# R71W1ReceiptDraft — after-receipt checklist draft (W1 advisory pre-gate, no scoring)

**Verdict: DRAFTED — the checklist is runnable and pins every frozen label; the two provenance gaps I located (counter hash vs pre-registration, and the missing timeout red-before receipt) were repaired by L1 and committed at `da4f1ee` (amendment A1 + rebuilt before-logs, counter `fbd81050`) before wave-2 scoring, so the after-receipt has a consistent harness to measure.** The candidate's C1 gate/lint legs are already green (`24/24`, `LINT_*=0`); the C1 vote label is `0/16` with an empty vote store; C2 reads `1/1`, `1/1`, `HOLDS_C2_V1=yes` under the amended counter. Remaining receipt duties: pin the final candidate revision, quote the counter/amendment hashes, and show all ten HOLD rows.

I am a leaf: no edits to counter, logs, claims, README, entry, controls, SCORECARD, git/jj; no scoring; no source rows opened (so no new-source quotes are owed by this seat).

## 0. Snapshot I measured (moving target — read this before using any label below)

Labels below were produced between 12:20 and 12:25 on lane HEAD `18200a4`; L1 then committed the harness repair at `da4f1ee` (see the repair paragraph below). Read the revision tag on every line.

| item | value | command |
|---|---|---|
| lane HEAD | `18200a4b18e8dfce291a74028a9012ce4401ca10` | `git -C LANE rev-parse HEAD` |
| HEAD tree | `8a7eb11f10d58e5e980701050006441d19948cf6` | `git -C LANE rev-parse 'HEAD^{tree}'` |
| HEAD counter | `d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c` | `git show HEAD:reports/round-71/measure.py \| sha256sum` |
| pre-registered counter | `d0d59b79…f38d06c` — **matches HEAD** (`reports/round-71/pre-registration.txt`) | |
| HEAD claims | `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5` — **matches pre-registration** | |
| worktree counter at my last read (12:25:43) | `fbd81050930657375f7314123ef468e66337b69adee12ce8416bb5dc98cff8f5` (**+1 line vs HEAD**, §6 F1) | `sha256sum reports/round-71/measure.py` |
| worktree claims at my last read | `1febae12…` (clean) | `sha256sum reports/round-71/claims.md` |
| Python | 3.14.8 (`/usr/lib/python3.14`) | `python3 -V` |

Interim state observed and captured at 12:23:18 (no longer on disk; patch preserved): counter `39e92bab…`, claims `5b95d343…`, replacing the `w2-votes/` reader with a `w2-results.json` reader and rewriting three claims sentences. Reverted by 12:25:30–43. Evidence: `dirty-diff.patch` (sha256 `a1413e599bbfb1598c5c8ad08d421ec64fdb8cc2e17fa0ed47997246bde7c580`), §6 F2.

L1 repairs committed during this seat at `da4f1eeae2ff5bb407894e13f7bdccf1b8faf5bd` ("round-71: correct timeout probe fixture path", parent `18200a4`, tree `35466853393f2d261211f8d35c50e6623d393e89`): `reports/round-71/measure.py` now `fbd81050…` (the one-line sleeper repair plus amendment A1), `pre-registration.txt` `d3c9263a…` with two appended lines, `measure-before.log` = `controls/A-do-nothing-base.log` = `7a942804…` (corrected red-before), `measure-amendment-A1.md` `251d6379…`, `controls/C2-missing-before.log` `538127d9…`. `claims.md` stays `1febae12…` (the pre-registered claims bytes). So the final after-receipt measures a later candidate revision on top of a **consistent, committed** amended harness; only the intermediate states below are obsolete.

| path | sha256 at `da4f1ee` | what it adds |
|---|---|---|
| `reports/round-71/measure.py` | `fbd81050930657375f7314123ef468e66337b69adee12ce8416bb5dc98cff8f5` | one-line sleeper-path repair only |
| `reports/round-71/measure-amendment-A1.md` | `251d6379edef214da9e06a0cdf651a345363f04e9eba8ca20e5e69078ade3293` | records the delta, the new counter sha, unchanged claims bytes, "before wave-2 scoring", corrected red-before |
| `reports/round-71/pre-registration.txt` | `d3c9263af55819d316eee4c94e009ad21433ed5eda849a66716278c83060f4bf` | two appended lines: amendment A1 (counter `fbd81050…`, claim hash unchanged) and the corrected red-before summary |
| `reports/round-71/measure-before.log` (= `controls/A-do-nothing-base.log`) | `7a9428048825e542139670a462e3d6067466c5a8157b2e3c0bdcb22c9f761407` | corrected red-before: `C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=yes`, `HOLD_REPLAY=10/10` |
| `reports/round-71/controls/C2-missing-before.log` | `538127d9513a71ec9b06ff3f552a2f7b2915549357e8b19b8bc3054271cd4879` | the missing-entry red-before cited by `claims.md:23` |

The 12:26–12:28 uncommitted intermediates (`amend` `0ab82099…`, `pre-reg` `a873280b…`) are superseded by `da4f1ee` and quoted only in §6 chronology.

## 1. Exact command and revision for the after-receipt

Run the counter against a `git archive` of the final measured revision, never against the lane worktree; record the four provenance lines before the labels.

```sh
LANE=/home/vgpnk/Projects/shokunin/revenger-shokunin
REV=$(git -C "$LANE" rev-parse HEAD)                     # write the 40-hex into the receipt
git  -C "$LANE" rev-parse "$REV^{tree}"
git  -C "$LANE" status --porcelain                        # record; must show no edits under corpus/, SKILL.md, or the round-71 vote store
sha256sum "$LANE/reports/round-71/measure.py" "$LANE/reports/round-71/claims.md"

T=/fast/scratch/hyaku/revenger-r71/receipt
rm -rf "$T" && mkdir -p "$T"
git -C "$LANE" archive "$REV" corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C "$T"

cd / && HYAKU_SCRATCH=/fast/scratch/hyaku/revenger-r71/receipt-scratch \
  python3 -B "$LANE/reports/round-71/measure.py" "$T" \
  > "$LANE/reports/round-71/measure-after.log" 2>&1
rc=$?; printf 'MEASURE_EXIT=%s\n' "$rc" >> "$LANE/reports/round-71/measure-after.log"
```

Receipt must then show, verbatim: `REV` (40 hex), `REV^{tree}`, counter sha256, claims sha256, `MEASURE_EXIT=<n>`, and the whole 47-line stdout (no filtering). While amendment A1 is in force, also record `reports/round-71/measure-amendment-A1.md` sha256 (`251d6379…` at `da4f1ee`) and the pre-registration's appended lines (`d3c9263a…`), and confirm `git ls-files` tracks the amendment, `measure-before.log`, `controls/C2-missing-before.log` and the counter at `REV`. If the receipt is committed after `REV`, also show `git diff --stat "$REV"..HEAD` and that the only change is the receipt log (the r70 spotcheck's measured-tip test).

Counter reads the lane **worktree**, not `$T`, for two inputs — the vote store (`measure.py:49-65`) and the round-70 self-check import (`measure.py:137-140` area). So `git status --porcelain` must show no modifications under those paths at the measured revision (untracked `__pycache__` is expected noise), and the receipt must say so; a dirty `w2-votes/` or a dirty `reports/round-70/measure.py` silently changes the labels.

## 2. All ten HOLD lines (checklist item: every line present, exit 0, plus the roll-up)

The counter prints one row per `corpus/verify_*.py` in sorted order, each `last_line(out+err)` truncated to 140 chars (`measure.py:147`; the 140-cut is expected, not a defect). Required content of `measure-after.log`:

```
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
```

Row 6 is truncated by the counter at `…not general PE validatio`; the script's full last line is `PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.` (verified on the tip archive: `python3 -B corpus/verify_named_multi_icon_states.py --self-test | tail -1`, exit 0). Both spellings must not be treated as a mismatch: the receipt records the counter line as printed and may add the full text as a note.

Checklist: count = 10 rows, all `exit=0`, `HOLD_REPLAY=10/10`, then `GATE_SELFTEST=exit 0`, `F_COVERAGE=5/8 score=6.2`, `FRESH_ROWS=18/18`, `HOLDS_OK_V8=yes`.

## 3. C1 vote label (single line + its evidence)

Label: `C1_W2_Q_VOTES=16/16` (`measure.py:91`, reader at `measure.py:49-65`).

Reader contract, as frozen at HEAD: four files under `.ufo/waves/round-71/w2-votes/`, filenames exactly `R71W2Q01Q04.json`, `R71W2Q05Q08.json`, `R71W2Q09Q12.json`, `R71W2Q13Q16.json`; each JSON has `seat` equal to the filename stem and `decisions` a dict whose keys are exactly that seat's four Q ids (`measure.py:42-46`); every value is `PASS` or `n/a` (case-sensitive in the frozen reader), no Q counted twice, all 16 present, else the label is `0/16`. Any parse error, unknown seat, extra/missing Q, `FAIL`, or duplicate → `0`.

Checklist for the receipt:
1. `C1_W2_Q_VOTES=16/16` printed.
2. The four paths exist **and** are tracked at `REV`: `git -C LANE ls-files .ufo/waves/round-71/w2-votes` → four names; `sha256sum` each; per-seat `Q01…Q16` verdict table (PASS / n/a) transcribed from the files, not from the seat reports.
3. State that the reader does **not** verify commit status — it globs the worktree — so the status line in §1 is the only guard.
4. Do not print 16/16 from seat prose: the seat names exist nowhere in the lane outside the counter (`grep -rn 'R71W2Q' .` → only `reports/round-71/measure.py:42-46`), so wave-2 dispatch must use exactly those four `name`/`seat` strings or the label stays 0.

At the current candidate the label is `0/16` because `.ufo/waves/round-71/w2-votes/` does not exist — expected before wave 2.

## 4. C2 outputs (three labels; exact strings)

Frozen predicate strings (`claims.md` §C2; registered row `SKILL.md:296`):

- `could-not-evaluate: entry not found:` on stdout, exit 2, no `Traceback` on stderr.
- `could-not-evaluate: command timed out after 120s:` on stdout, exit 2, no `Traceback`.
- `--self-test` exit 0 with both hermetic legs named.

Counter labels to copy verbatim: `C2_MISSING_ENTRY_EXIT2=…`, `C2_TIMEOUT_EXIT2=…`, `C2_GATE_SELFTEST=<rc> named_legs=…`, then `HOLDS_C2_V1=…`.

Observed at HEAD revision `18200a4` (candidate tree, frozen counter `d0d59b79`):

| label | observed | why |
|---|---|---|
| `C2_MISSING_ENTRY_EXIT2` | `1/1 rc=2 stderr_traceback=no` | direct run prints `could-not-evaluate: entry not found: <abs path>`, exit 2 |
| `C2_TIMEOUT_EXIT2` | `0/1 rc=1 stderr_traceback=no` | **counter-side defect**, §6 F3: fixture wrote `corpus/sleeper_r71.py` while the entry declared `python3 -B sleeper_r71.py` and the gate ran with cwd = tree root; command exits 2 → recorded as drift `checked_blocks=0 problems=1` |
| `C2_GATE_SELFTEST` | `0 named_legs=1` | 1.08 s; `SELFTEST OK: … missing-entry and timeout legs passed` |
| `HOLDS_C2_V1` | `no` | timeout leg only |

Independently verified gate behavior (the leg the claim is about, wired correctly): tree root + `sleeper.py` reachable, entry declaring `$ python3 -B sleeper.py`, gate cwd = tree root → stdout `could-not-evaluate: command timed out after 120s: python3 -B sleeper.py`, exit 2, no traceback, wall `2m0.126s`. So the gate satisfies the predicate; only the frozen counter's fixture path did not.

Same run against the uncommitted worktree counter snapshot `fbd81050…` (one-line repair, §6 F1), same tip tree, exit 0, wall `124.64s`: `C2_TIMEOUT_EXIT2=1/1 rc=2 stderr_traceback=no`, `HOLDS_C2_V1=yes`; the whole 47-line log differs from the `d0d59b79` log on exactly two lines (`C2_TIMEOUT_EXIT2`, `HOLDS_C2_V1`), so the repair moves only the C2 leg. C1 still reads `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no` at the candidate.

Checklist: record the three labels, the full stdout of the timeout leg (the exact reason line), wall time ≥120 s (a fast leg means the fixture is unreachable again — treat as `no`, never as pass), and `stderr_traceback=no`.

## 5. Compare with the r70 verifier spotcheck

The r70 spotcheck (`.ufo/waves/round-71/sources-s052/validate/corpus/lessons/round-70-verifier-spotcheck.md`) sampled 2 admits + 1 scope admit + 4 rejects → **0 disagreements**, and routed five status-neutral items. Mapping to this round's checklist:

| r70 routed item | r71 receipt requirement | state I observed |
|---|---|---|
| 1. `measure-after.log` omitted the ten `HOLD` rows (`HOLD_REPLAY` printed; re-run printed all ten) | §2 requires all ten rows verbatim, in order, plus `HOLD_REPLAY=10/10` | candidate/counter prints all ten (§2 block) |
| 2. `C1_LINT` read `LINT_QMAP=1 ['Q16']` at the rejected entry | §1/§3 require the exact `C1_LINT` line; expected `LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0`, exit 0 | candidate: exactly that, exit 0; `C1_GATE=checked_blocks=24 problems=0 exit=0` (≥17 required) |
| 3. gate residuals: missing entry exits 1, timeout exits 1 with traceback | §4 requires exit 2 + reason line + no traceback for both | missing: fixed (`1/1 rc=2`, no traceback). Timeout: gate verified directly (`could-not-evaluate: command timed out after 120s: …`, exit 2, wall 2m0s); with the amended counter (`fbd81050`) the leg reads `1/1 rc=2` and `HOLDS_C2_V1=yes`; with the pre-registered bytes (`d0d59b79`) it reads `0/1 rc=1` (§6 F1/F3) |
| 4. SHONEN boxes remain `[~]`, promotion operator-owned | not a receipt item; do not claim promotion | untouched |
| 5. retained residuals (env-override hybrid checker, `PROVINCE.md` pin, one-directional comparison) | not measured by this counter; the receipt must not claim them closed | outside this seat's evidence |

Also: the `0 disagreements` figure is r70's audit; the r71 receipt must state its own spotcheck result and must not inherit it.

## 6. Findings and conflicts (verbatim, for the canonical judge)

**F1 — counter hash no longer matches the pre-registered value (provenance conflict).**
`reports/round-71/pre-registration.txt`: `Counter SHA-256: d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c`. That is `HEAD:reports/round-71/measure.py`. The worktree file at 12:25:43 is `fbd81050…f8f5`, differing by exactly one line:

```
-    slow.write_text('```\n$ python3 -B sleeper_r71.py\nfinished\n```\n',encoding='utf-8')
+    slow.write_text('```\n$ python3 -B corpus/sleeper_r71.py\nfinished\n```\n',encoding='utf-8')
```
(`reports/round-71/measure.py:103` in the worktree; `git diff reports/round-71/measure.py`). At 12:26 L1 added `reports/round-71/measure-amendment-A1.md` (sha256 `0ab82099…2b7`) recording exactly this delta, the new counter sha, unchanged claims bytes, and "before wave-2 scoring"; it also appended a 10th line to `pre-registration.txt` (worktree sha256 `a873280b…230`): `Pre-wave2 counter amendment A1: … claim hash unchanged (1febae12…), counter SHA now fbd81050…. Only the timeout fixture command path changed…`. `R71W1Sentinel` independently located the same defect (`.ufo/waves/round-71/w1/R71W1Sentinel.md` §F1, HIGH). The repair is effective and narrowly scoped: at `fbd81050` the C2 legs read `1/1`, `1/1`, `0 named_legs=1`, `HOLDS_C2_V1=yes`, and the 47-line log differs from the `d0d59b79` run on exactly those two lines. Status at hand-off: L1 committed all five items at `da4f1ee` (counter `fbd81050…`, amendment `251d6379…`, pre-registration `d3c9263a…`, `measure-before.log`/A-log `7a942804…`, `controls/C2-missing-before.log` `538127d9…`), so the residual is only a receipt duty: quote the counter sha, cite amendment A1 by path+sha, and show `git ls-files` tracking them at `REV`; otherwise the labels are measured by bytes the receipt cannot name.

**F2 — transient counter/claims rewrite observed (no committed trace).** At 12:23:18 the worktree held counter `39e92bab…` and claims `5b95d343…`; the diff replaced the vote reader with a `w2-results.json` reader and rewrote three claims sentences, e.g. HEAD `The counter parses committed per-seat JSON vote files under \`.ufo/waves/round-71/w2-votes/\`; each carries a unique seat and its assigned Q decisions.` vs interim `The counter reads \`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-71/w2-results.json\`, binds four named reviewer seats to their assigned Q subsets, and parses their final \`output\` text as either JSON-wrapped votes or plain \`Qnn: PASS|n/a|FAIL\` lines.` Also interim `D … has no orchestrator \`w2-results.json\`` vs HEAD `D … fails the frozen vote-file predicate at \`C1_W2_Q_VOTES=0/16\``. Reverted; HEAD claims hash equals the pre-registered claims hash. Preserved patch: `dirty-diff.patch` sha256 `a1413e59…7c580`. Report as an observed state change, not as a standing defect.

**F3 — frozen counter's C2 timeout leg cannot reach its own predicate.** `reports/round-71/measure.py:100-103` writes the sleeper to `<scratch>/timeout-fixture/corpus/sleeper_r71.py` but, at HEAD, declares `$ python3 -B sleeper_r71.py`; `gate_cli(d, …)` (`:105`) runs the gate with cwd = the tree root, and `corpus/check_embedded_outputs.py:102-115` executes the declared command with `cwd=Path.cwd()`. Result on the tip archive:

```
drift entry:2 command exited 2: python3 -B sleeper_r71.py
checked_blocks=0 problems=1
RC=1
```
i.e. `C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=no`. The same wiring makes the leg insensitive to the behavior under test: a gate that still raised `TimeoutExpired` (control F) would print the same `0/1 rc=1 no traceback`, so the leg cannot discriminate a correct fix from an unchanged one at the frozen hash.

**F4 — the cited missing-entry red-before receipt was absent, then added (uncommitted) at 12:26:44.** `claims.md:23`: `Red-before receipts are \`controls/C2-missing-before.log\` and \`controls/C2-timeout-before.log\`.` At 12:20 `git ls-files reports/round-71/controls/` returned only `A-do-nothing-base.log`, `B-C1-readme-flip-only.log`, `C-C1-admitted-stub.log`, `C2-timeout-before.log`, `D-C1-v5-copy-with-q16.log` — the missing-entry receipt did not exist. L1 then wrote `reports/round-71/controls/C2-missing-before.log` (sha256 `538127d9…879`): a base-gate traceback ending `FileNotFoundError: [Errno 2] No such file or directory: 'corpus/knowledge/does-not-exist.md'` and `RC=1`, matching the claim's before. It is committed at `da4f1ee`. I reproduced the same base behavior independently on `b7abcd8` (`--entry …/round-71-missing-entry.md` → `FileNotFoundError` traceback, `RC=1`).

**F5 — the committed red-before timeout label is non-diagnostic; the worktree log is not.** At HEAD, `reports/round-71/measure-before.log` prints `C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=no`; the claims' `Before` sentence says the base produces `TimeoutExpired` traceback and exit 1. That label was produced by the unreachable-script path (F3), so the committed red-before is right by coincidence, not by exercise. L1 re-ran the red-before at 12:28:29; the worktree log now reads `C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=yes` and is otherwise byte-identical (diff: one line), consistent with the repaired fixture reaching the base gate's 120 s timeout. The re-run log is committed at `da4f1ee` (`7a942804…407`). The receipt must record that hash, keep the old and new labels separate, and note the replacement happened after amendment A1 and before wave-2 scoring.

**F6 — exit code does not encode the claims.** `measure.py:3-5` docstring: `Exit 0 = prior holds green, 1 = named hold red, 2 = could not evaluate`; `body` returns `0 if holds else 1` (`:165`), where `holds` is only `HOLDS_OK_V8` (`:163`). Red-before has `HOLDS_C1_V6=no`, `HOLDS_C2_V1=no` and `MEASURE_EXIT=0`. The receipt must print both claim labels and the exit separately and must not infer claim status from `MEASURE_EXIT`.

**F7 — vote-seat strings are unregistered.** `R71W2Q01Q04/Q05Q08/Q09Q12/Q13Q16` appear only at `measure.py:42-46` (HEAD and worktree); neither `claims.md` nor `pre-registration.txt` names them. Wave-2 dispatch (L1) must use exactly these strings in the `seat` field and filenames, or `C1_W2_Q_VOTES` stays `0/16` for a naming reason.

**F8 — snapshot coupling.** `q_votes()` reads `LANE/.ufo/waves/round-71/w2-votes` (`:50`) and the retained round-70 fixture loads `LANE/reports/round-70/measure.py`; both are the worktree, not `$T`. Receipt must record that these matched `REV`.

## 7. Out of scope / limits

- No counter, log, claims, README, entry, controls or SCORECARD edit; no git/jj mutation; no installs; no source rows opened.
- I did not run the E/F C2 controls; F3's insensitivity argument is from the two observed invocations (`0/1 rc=1 no traceback`), not from running E/F.
- Preview values are the **candidate** state (README C05 `uncovered`, header `candidate`, votes `0/16`): `K_HELD_BACKED=8/14`, `C1_GATE checked_blocks=24 problems=0`, `C1_LINT` all zero, `HOLDS_C1_V6=no`. They are not the after-receipt; the after-receipt must show `9/14`, `held`, `admitted`, `16/16`.
- `EMB_R65=checked_blocks=15 problems=1 exit=1` is the retained round-70 drift hold; the receipt must reproduce it and must not explain it away.
- Preview ran on Linux, Python 3.14.8; the frozen counter (`d0d59b79`) took 4.8 s because its timeout leg never ran, and the repaired counter (`fbd81050`) took 124.64 s with the leg live. The after-receipt will likewise take ≈2.5 min.
- Provenance changed while this seat was drafting (12:21 → 12:28): three worktree states of `reports/round-71/measure.py` (`d0d59b79` = HEAD/pre-registered, `39e92bab` = interim `w2-results` rewrite, `fbd81050` = one-line sleeper repair) and two of `claims.md` (HEAD `1febae12`, interim `5b95d343`, reverted to HEAD); settled at `da4f1ee` with counter `fbd81050` and claims `1febae12`. Every label above is tagged with the counter hash that produced it; do not mix them.
- The lane worktree also contains untracked `reports/round-70/__pycache__/` and `reports/round-71/__pycache__/` (mtime 12:22:59 / 12:23:26, i.e. after my first preview; not created by my `python3 -B` runs). They are bytecode litter, not source; the receipt's `git status` line must list them as untracked rather than present a clean tree.
- Scratch receipts were hashed, then deleted; values above are transcribed from them.

## 8. Artifacts (scratch, deleted after transcription)

| path (under `/fast/scratch/hyaku/revenger-r71/R71W1ReceiptDraft/`) | sha256 |
|---|---|
| `measure-head.py` (HEAD counter, `d0d59b79…`) | `d0d59b79…f38d06c` |
| `preview-head-counter.log` (47 lines, exit 0) | `90f45cea9f93ad09882733b9effa565fdc7b6077d3b7f07a78b9755d9f799cd9` |
| `preview-after.log` (identical to above) | `90f45cea…99cd9` |
| `measure-fbd81050.py` (worktree counter snapshot) | `fbd81050930657375f7314123ef468e66337b69adee12ce8416bb5dc98cff8f5` |
| `preview-repaired.log` (47 lines, exit 0, 124.64 s) | `075de59f09c127beb9021d50132bf56b9b27af349b92dca3c1a4223150d44ceb` |
| `dirty-diff.patch` (12:23:18 state, reverted) | `a1413e599bbfb1598c5c8ad08d421ec64fdb8cc2e17fa0ed47997246bde7c580` |
| `timeout-wired.log` (gate timeout, exit 2) | `8d4c89cfaf099eb62aaf8c016f5d069211025cb09df6a8bab5f0a846e5006d62` |

Full 47-line preview (frozen counter `d0d59b79`, tree = `git archive 18200a4` `corpus SHONEN.md SCORECARD.md SKILL.md`, cwd `/`, `HYAKU_SCRATCH` under scratch):

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

Report: `.ufo/waves/round-71/w1/R71W1ReceiptDraft.md`
