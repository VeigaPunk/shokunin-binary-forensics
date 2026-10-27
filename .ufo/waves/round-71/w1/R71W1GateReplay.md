**Verdict: OPERABLE / calibration green under amendment A1** — all six assigned replays reproduce the registry on committed bytes and the C2 exit-2 contract is demonstrated live at the production 120-second limit (`HOLDS_C2_V1=yes`, counter exit 0); one advisory C1 repair (F2: v6 line 8 cites a nonexistent `corpus/lessons/round-71.md` `## Gate`) and one instrument defect already amended by A1 (F1, §6b).

# R71W1GateReplay — gate replay: self-test, v6 entry, lint, missing-entry, old drift, pinned-r68

- Mode: read-only over the lane. No lane source, receipt or counter byte was written by this seat. Replay trees are `git archive HEAD` snapshots under `/fast/scratch/hyaku/revenger-r71/R71W1GateReplay/` (deleted before return); `HYAKU_SCRATCH` pointed inside that root.
- Lane tip at start: `18200a4b18e8dfce291a74028a9012ce4401ca10` ("round-71: build v6 candidate and gate exit-2 cases"); `git status --porcelain -uno` empty (no tracked working-tree change) at 12:16.
- Frozen identity verified before measuring: `sha256sum reports/round-71/measure.py` = `d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c`, `reports/round-71/claims.md` = `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5` — both equal to `reports/round-71/pre-registration.txt`.
- Registry read: `SKILL.md:288` (verdict map incl. the two new exit-2 reasons), `SKILL.md:289` (self-test row), `SKILL.md:296` (round-71 exit-2 legs row); coverage claim row `corpus/README.md:45`.

## 1. Gate self-test — PASS (exit 0)

```
$ cd <head-tree>   # git archive HEAD corpus, tree 18200a4
$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed
SELFTEST_EXIT=0
```
Both registered leg names (`missing-entry`, `timeout`) are present, which is exactly what `reports/round-71/measure.py:112` tests (`named_legs=1`). Self-test legs live at `corpus/check_embedded_outputs.py:271-285`; the timeout case injects 1 s while the CLI keeps 120 s, as `SKILL.md:296` states.

## 2. v6 entry gate — PASS (≥17 blocks, 0 problems)

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md
checked_blocks=24 problems=0
V6_GATE_EXIT=0
```
Matches `corpus/README.md:45` ("gate 24/24") and the counter's C1 conjunct `blocks>=17 and problems==0` (`reports/round-71/measure.py:86-88`), which printed `C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes`.

## 3. v6 lint — PASS (four zeros)

```
$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md --lane <lane>
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
LINT_EXIT=0
```
Exactly the four labels the frozen predicate names; counter row `C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0`.

## 4. Missing-entry probe — PASS (exit 2, no traceback)

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-missing-entry.md
could-not-evaluate: entry not found: corpus/knowledge/round-71-missing-entry.md
MISSING_EXIT=2
```
Message prefix equals the frozen text `could-not-evaluate: entry not found:` (`corpus/check_embedded_outputs.py:162`); stderr 0 bytes. Base behaviour is the registered red: `reports/round-71/measure-before.log` → `C2_MISSING_ENTRY_EXIT2=0/1 rc=1 stderr_traceback=yes`.

## 5. Exit-2 / usage classification map (operability review, all stdout-only)

Each probe was an entry under a throwaway `corpus/` copy; stderr bytes measured for every case:

| probe | stdout | exit | stderr |
|---|---|---|---|
| entry is a directory (`--entry corpus/knowledge`) | `could-not-evaluate: entry not found: corpus/knowledge` | 2 | 0 |
| unreadable entry (`chmod 000`) | `could-not-evaluate: entry not readable: …/e-unreadable.md` (`:166`) | 2 | 0 |
| entry with no `$ cmd` block | `could-not-evaluate: no `$ cmd` blocks or unsupported command` (`:302`) | 2 | 0 |
| block declaring `$ ls -la` (unsupported) | same message | 2 | 0 |
| block declaring `python3 -c …` (confinement) | same message | 2 | 0 |
| no arguments | docstring usage | **64** (`:309`) | 0 |
| `--entry` with no value / `--self-test extra` | usage | 64 | 0 |
| missing entry | `could-not-evaluate: entry not found:` | 2 | 0 |

No traceback on any path; every declared reason is on stdout, so a caller reading `stdout` alone classifies correctly. Exit-1 semantics are intact: a declared command exiting non-zero still yields `drift entry:N command exited RC` + exit 1 (observed below in §6b), and the registered comparison line `problems += drift(lines, stdout_set, lineno)` is unchanged at `corpus/check_embedded_outputs.py:190` (the round-71 diff touches only `run_cmd` timeout, `evaluate` pre-conditions, `main` dispatch and `_self_test`; `git diff --stat b7abcd8..HEAD -- corpus/check_embedded_outputs.py` = 51 insertions, 19 deletions, none in `drift`).

## 6. Live 120-second timeout — the assigned calibration leg

**a) Contract gate, correctly rooted** (copy of the HEAD `corpus/`; `corpus/sleeper_r71.py` sleeps 130 s; probe entry declares `$ python3 -B corpus/sleeper_r71.py`):

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-timeout-probe.md
could-not-evaluate: command timed out after 120s: python3 -B corpus/sleeper_r71.py
TIMEOUT_EXIT=2 WALL=120s     # stderr bytes = 0
```
Text equals the frozen prefix `could-not-evaluate: command timed out after 120s:` (`corpus/check_embedded_outputs.py:113-114`), measured at the production limit, no traceback.

**b) Frozen counter `d0d59b79…` — F1: the timeout leg could never reach the timeout.** Whole counter on the HEAD tree finished in 4.63 s:

```
COUNTER_EXIT=0
C2_MISSING_ENTRY_EXIT2=1/1 rc=2 stderr_traceback=no
C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=no
C2_GATE_SELFTEST=0 named_legs=1
HOLDS_C2_V1=no
```
Root cause reproduced by rebuilding the pre-A1 fixture exactly (`measure.py:100-103`): the sleeper was written to `TREE/corpus/sleeper_r71.py` while the probe entry declared the bare `$ python3 -B sleeper_r71.py` and `gate_cli(d, …)` runs with `cwd=TREE` (`measure.py:36-37,105`), so Python never opened the file:

```
$ cd <pre-A1 timeout-fixture replica>; python3 -B corpus/check_embedded_outputs.py --entry $PWD/corpus/knowledge/round-71-timeout-probe.md
drift entry:2 command exited 2: python3 -B sleeper_r71.py
checked_blocks=0 problems=1
REPLICA_EXIT=1 WALL=0s      # stderr bytes = 0
```
So the red was a fixture path, not a gate defect: `HOLDS_C2_V1=no` would have survived any repair to the gate. (Independently found as §F1 by `R71W1Sentinel`.)

**c) Amended counter A1 (`fbd81050…`, one-line probe-command change, `reports/round-71/measure-amendment-A1.md`) on the same HEAD tree — green, at real wall time:**

```
COUNTER_REPAIRED_EXIT=0
C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
C1_W2_Q_VOTES=0/16
C2_MISSING_ENTRY_EXIT2=1/1 rc=2 stderr_traceback=no
C2_TIMEOUT_EXIT2=1/1 rc=2 stderr_traceback=no
C2_GATE_SELFTEST=0 named_legs=1
HOLDS_C2_V1=yes
WALL=124.69s
```
`124.69 s` wall is the proof the leg now waits out the production 120 s; the four-second pre-A1 run was the proof it did not. `git diff -- reports/round-71/measure.py` = 1 hunk, 1 insertion / 1 deletion; `measure-before.log` re-ran on base with both C2 legs `rc=1 … traceback=yes` (correct red for the old gate), 48 lines, `HOLD_REPLAY=10/10`, `HOLDS_OK_V8=yes`.

**d) Child reaping.** Immediately after the timed-out gate exited, its sleeper PID was gone; the `-B -B corpus/sleeper_r71.py` PIDs visible at that instant were concurrent siblings' *live* gate runs (each showed a non-1 PPID and sub-120 s elapsed, then disappeared). No orphan is left by the timeout path — `subprocess.run(..., timeout=)` kills the child before the exception propagates.

## 7. Old drift and pinned-r68 — unchanged, matching red-before exactly

```
$ for e in 65 67 68 69; do python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-$e-apk-axml-byte-evidence.md; done
round-65 rc=1 drift entry:41 embedded output line not in recheck stdout: {... "payload_first16_hex": "4d616e696673742d56657273696f6e" ...}  checked_blocks=15 problems=1
round-67 rc=0 checked_blocks=16 problems=0
round-68 rc=0 checked_blocks=17 problems=0
round-69 rc=0 checked_blocks=17 problems=0
```
Identical to `reports/round-71/measure-before.log` (`EMB_R65=15/1 exit=1` — the registered M39 drift at `entry:41`, `SKILL.md:288` pinned-value row; `EMB_R67=16/0`, `EMB_R68=17/0`, `EMB_R69=17/0`).

Pinned-r68 case, digests against the frozen counter constants (`measure.py:17-19`):

```
ef7f0232edb74baecc2754e6671f00914ec02e077606fcb7f21880de0830798e  corpus/knowledge/round-68-apk-axml-byte-evidence.md
cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a  corpus/knowledge/round-65-apk-axml-byte-evidence.md
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors_r68.py
```
→ `EMB_R68_BYTES_UNCHANGED=yes`, `EMB_R65_BYTES_UNCHANGED=yes`, `EMB_PINNED_SCRIPT_IS_S046=yes`. Pin mutant (append `# tampered` to the pinned copy `corpus/derive_axml_anchors_r68.py`, then re-run the r68 entry):

```
drift entry:128 pinned historical script digest mismatch: corpus/derive_axml_anchors_r68.py
checked_blocks=16 problems=1
PIN_MUTANT_RC=1  PIN_MARKER_IN_STDOUT=True  STDERR_EMPTY=True
```
i.e. `EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1` with the registered marker (`corpus/check_embedded_outputs.py:34,144-153`), unchanged.

## 8. Pre-gate C1 state (expected, not a defect)

Frozen counter on the HEAD tree (pre-A1 run): `K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`, `C05_STATUS=uncovered`, `C05_KNOWLEDGE_COLUMN=-`, `C05_SINGLE_V6=no`, `V6_ENTRY_PRESENT=yes`, `V6_ADMITTED_MARKED=no`, `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`. That is the landing order the claims freeze (`candidate` landed, README C05 unflipped, votes pending); the v6 gate/lint conjuncts are already green, so the only remaining C1 conjuncts are the README flip, the admitted header line and 16/16 wave-2 votes. `HOLDS_OK_V8=yes`, `HOLD_REPLAY=10/10`, `FRESH_ROWS=18/18`, `F_COVERAGE=5/8 score=6.2` in both runs.

## 9. Source / mistake frontier touched by this replay

- New row this round: **S052** (`corpus/SOURCES.md:66`), access date **2026-10-27**, located quote ≤25 words: `MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;` — reproduced byte-identically by `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes` (line 5 of 6); row scope correctly says "output shape … not the raw source line".
- Frozen prose repair, item 11: the `--spec-quotes` output is exactly six `MATCH <file>: first line N, folded phrase present=True: <phrase>` lines (verified, complete set, no extra), matching `corpus/knowledge/round-71-apk-axml-byte-evidence.md:120` "the output below is the complete set".
- Frozen prose repair, item 12: `--zip-layout` prints exactly 20 lines; lines 16–18 are `MATCH APPNOTE 4.3.7 … 387`, `4.3.12 … 511`, `4.3.16 … 632` (the three layouts), and lines 19–20 are `central.fixed_part: spec width 46` / `local.fixed_part: spec width 30` — precisely the bounded wording now in the entry, exit 0.
- Q13 names the surviving forged-block case and attributes it (`… R70W2EntryMutants`, entry line 311); Q16 row states the output-bounded coverage rule (line 314).

**F2 (advisory repair, C1).** Entry line 8 (S052 anchor) says the `--spec-quotes` line is "recorded in `corpus/lessons/round-71.md` `## Gate`". That file does not exist: `git ls-files | grep -c lessons/round-71` → `0`, and `test -f corpus/lessons/round-71.md` fails while `corpus/lessons/round-70.md` exists; the string `lessons/round-71` occurs in the lane only in that entry line. A candidate that cites a nonexistent record path is exactly the dangling-reference class the Q06/Q13 reviewers killed in earlier rounds. Repair before the final candidate lands: either write the round-71 lesson's `## Gate` section (L1 owns adjudication text) or drop the trailing clause from the anchor.

**F3 (instrument wording, low).** `--self-test` asserts the `CannotEvaluate` *reason strings* (`corpus/check_embedded_outputs.py:271-285`), not the CLI's exit-2 mapping in `main()` (`:296-303`). The exit-2 contract therefore rests on the counter's live CLI legs (§6c) and this replay, not on the self-test. `SKILL.md:296` reads "Self-test covers missing entry and timeout with hermetic fixtures; the live CLI returns exit 2 …", which is accurate as written, but a future reader must not credit `--self-test` with exit-code coverage; keep both legs in the counter.

**Observation, not mine (recorded for the L1).** Between 12:25:43 and 12:28 the lane working tree carried round-71 changes that were not mine — counter A1 at `fbd81050…`, an appended amendment paragraph in `pre-registration.txt`, and a regeneration window in which `reports/round-71/measure-before.log` was 0 bytes at 12:26:27 before returning to its 48 lines. They are since committed as `da4f1ee` "round-71: correct timeout probe fixture path" (tip after my replays: `da4f1ee`, `measure.py` still `fbd81050…`, `measure-before.log` 48 lines). All measurements above name the exact counter hash and tree they used, so the §6b and §6c runs stay attributed to `d0d59b79…` and `fbd81050…` respectively regardless of commit placement. Risk to note: the red-before receipt is a required claim input, so re-running receipts should preserve the prior file (or write a sibling file) rather than truncating it in place.

## Blockers

None. Nothing in this replay contradicts the frozen predicates at the current tip; no lane byte was edited by this seat.

Report: `.ufo/waves/round-71/w1/R71W1GateReplay.md`
