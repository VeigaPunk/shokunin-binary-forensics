GATE PASS / COUNTER BLOCK — the patched HEAD CLI classifies both declared could-not-evaluate cases at exit 2 with the frozen texts and zero traceback (real production timeout measured at 120 s wall, child reaped), but the registered counter's timeout fixture starts no process, so `C2_TIMEOUT_EXIT2` is structurally 0/1 regardless of gate behaviour.

# R71W1TimeoutProbe — C2 exit-2 calibration and operability probe

Lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · measured tip `18200a4b18e8dfce291a74028a9012ce4401ca10` ("round-71: build v6 candidate and gate exit-2 cases") · gate `corpus/check_embedded_outputs.py` sha256 `05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8`, identical to the copy each fixture runs · frozen base `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f` · probe date 2026-10-27 · lane source untouched (`git diff --stat HEAD -- corpus/check_embedded_outputs.py` → no output) · scratch `/fast/scratch/hyaku/revenger-r71/R71W1TimeoutProbe/` created, all receipts transcribed below, then deleted · no source row opened this round (host-local execution only, so no ≤25-word source quote is owed by this seat) · no install, no pacman, no routing change.

Scope: frozen C2 predicate legs only (`claims.md` C2: missing entry, production-120 s command timeout, `--self-test`), plus the operability of the counter fixture that implements them. No C1 scoring, no round judgement.

## 1. Frozen legs, exercised on the real CLI (HEAD, cwd = lane root unless stated)

| Leg | Command | rc | stdout (verbatim) | stderr | traceback |
|---|---|---|---|---|---|
| M missing entry, relative | `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-does-not-exist-TP.md` | **2** | `could-not-evaluate: entry not found: corpus/knowledge/round-71-does-not-exist-TP.md` (84 B) | 0 B | none |
| M-abs missing entry, counter spelling | `python3 -B corpus/check_embedded_outputs.py --entry "$PWD/corpus/knowledge/round-71-missing-entry.md"` | **2** | `could-not-evaluate: entry not found: /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-71-missing-entry.md` | 0 B | none |
| M-dir entry path is a directory | `--entry corpus/knowledge` | **2** | `could-not-evaluate: entry not found: corpus/knowledge` | 0 B | none |
| T production timeout, sleeper resolvable in-tree | fixture root = cwd, `sleeper_tp.py` at fixture root, entry declares `$ python3 -B sleeper_tp.py` | **2** | `could-not-evaluate: command timed out after 120s: python3 -B sleeper_tp.py` (75 B, sha256 `a836f359370c3e72be61900fdfb2217d5d59b1f871c8441e0af3f4beee1b0e19`) | 0 B | none, stdout or stderr |
| S self-test | `python3 -B corpus/check_embedded_outputs.py --self-test` | **0** | `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed` (155 B, sha256 `8b27dec249fdf045b187839ea760143ee81da30424ee05e2556f8c14f3ce6082`) | 0 B | none |
| U usage | no arguments | **64** | 1459-byte `__doc__` (docstring) | 0 B | none; no `could-not-evaluate` line |

Leg T details: nothing was injected — the gate's own default path was used (`check_embedded_outputs.py:102` `run_cmd(..., timeout=120)`, `:158` `evaluate(..., timeout=120)`, CLI call `:297`). Wall clock `rc=2 wall_s=120` (harness: 120.18 s). `pgrep -af sleeper_tp.py` after the run → `none`, so `subprocess.run`'s timeout kill is not leaking the declared command. Leg S wall 1062 ms (hermetic `tempfile.TemporaryDirectory`, `:292`), with the timeout leg injected at 1 s (`:281`); that matches the frozen text ("The timeout self-test uses a one-second injected timeout, while the counter's CLI leg exercises the declared production 120-second timeout").

Contract anchors in the gate: `:158-166` (`is_file()` guard → `CannotEvaluate("… entry not found: …")`, unreadable → `entry not readable`), `:102-114` (`TimeoutExpired` → `CannotEvaluate("… command timed out after {timeout}s: {cmd}")`), `:296-308` (`except CannotEvaluate` at `:298` → print + `sys.exit(2)` at `:300`; `checked_blocks=` trailer only at `:306`), `:274-285` (self-test missing-entry and injected-1 s timeout legs). Declared mapping: `SKILL.md:296`; verdict map `SKILL.md:288`.

Live red-before, for the receipt `claims.md:23` names but the controls directory lacks (`R71W1ControlsRun` §4.1): the frozen base gate (`git show b7abcd8:corpus/check_embedded_outputs.py`, run from scratch) on a nonexistent entry gives `rc=1`, empty stdout, 16-line stderr ending `FileNotFoundError: [Errno 2] No such file or directory: 'missing-TP.md'` — an independent reproduction of the C2 "Before" sentence.

## 2. The registered counter's timeout fixture never starts the sleeper (independent reproduction)

Counter fixture (identical text at HEAD `reports/round-71/measure.py:100-103` and in the modified working tree `:129-132`): copy `corpus/` into `<scratch>/timeout-fixture/corpus`, write the sleeper to `d/'corpus/sleeper_r71.py'`, write the entry command `python3 -B sleeper_r71.py`, then invoke the gate through `gate_cli(d, …)` = `subprocess.run([sys.executable, '-B', d/'corpus/check_embedded_outputs.py', …], cwd=d)` (`:39-40`). The child's cwd is the fixture **root**, where no `sleeper_r71.py` exists; `confined()`/`inside()` (`:79`, `:91-100`) validate path shape only, never existence, so the command is allowed and Python exits 2 for the missing file. Reproduced byte-faithfully:

```
COUNTER_SHAPE rc=1 wall_ms=29
drift entry:2 command exited 2: python3 -B sleeper_r71.py
checked_blocks=0 problems=1
```

No `could-not-evaluate: command timed out after 120s:` line, no 120 s wait, stderr empty. The gate turns the child's exit 2 into drift at `:186-187`, so `measure.py:135`'s `timed.returncode==2 and '… timed out after 120s:' in timed.stdout` is false by construction and `HOLDS_C2_V1=no` is printed even against a correct gate. This confirms `R71W1ControlsRun` §3 and `R71W1Sentinel` from the CLI side rather than through `evaluate(timeout=1)`: no sibling report records the *default-120 s CLI* leg, which is the leg the frozen predicate names.

## 3. Repair, proven at the production limit

Two one-line shapes, both verified to resolve (fast sleeper `print("finished")`, entry line `finished`):

- sleeper written to the fixture root, command unchanged `python3 -B sleeper_r71.py` → `repair_resolution_rc=0`, `checked_blocks=1 problems=0`;
- sleeper kept at `corpus/sleeper_r71.py`, entry command respelled `python3 -B corpus/sleeper_r71.py` → `checked_blocks=1 problems=0` (`rc=0`).

The full production timeout classification was measured for the root shape (leg T: exit 2, exact text, no traceback, 120 s wall, no stray child). Once the child starts, both shapes take the same single `TimeoutExpired` branch (`check_embedded_outputs.py:113-114`), so classification is spelling-independent; only resolution differs. Recommended minimal repair for L1: write the sleeper to `d/'sleeper_r71.py'` (or change the entry text), which leaves the rest of the fixture and the 120 s production default untouched.

Two cautions attached: (a) the repaired fixture must be re-run at the real 120 s limit, not only with an injected 1 s timeout, or the committed receipt still lacks the declared production-limit observation; (b) any `measure.py` edit changes the counter bytes recorded at `pre-registration.txt:4` (`Counter SHA-256: d0d59b79…`) — re-record the sha and note the wave-1 fixture repair in the Gate draft instead of leaving a stale digest.

## 4. Counter provenance as observed (receipt integrity, not a C1/C2 judgement)

The lane working tree currently carries **uncommitted** counter changes made after the pre-registration receipt (`pre-registration.txt` mtime `12:14:15`, `claims.md` `12:21:41`, `measure.py` `12:23:18`):

- `reports/round-71/measure.py` working-tree sha256 `39e92babebc5b3550f01583e360ea77211e0f0f2b9af45725d70acd1c1affcec`; `git show HEAD:reports/round-71/measure.py` sha256 `d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c` — equal to the recorded `pre-registration.txt:4` value.
- The uncommitted diff replaces `q_votes()` (per-seat `w2-votes/*.json`) with a single `w2-results.json` reader, and `claims.md` C1 companion sentences were rewritten to match.

Consequence for my scope: the C2 fixture is byte-identical in both representations (HEAD `:100-103`, worktree `:129-132`), so the defect and this probe are representation-independent. But a measurement taken from the working tree would not be against the recorded counter, and the recorded sha would silently describe different bytes. L1 owns the integration decision; this seat records the divergence only.

## 5. Operability notes for the final gate

- Margin: the counter allows `TIMEOUT+30` = 150 s around the gate (`measure.py:39` default 150, `:134`), and the gate's own timeout is 120 s wall (measured 120.18 s). ~30 s headroom, so a correct fixture will not trip `outer_timeout=yes` (`:138`).
- Exit-2 stdout is exactly one line; no `checked_blocks=` trailer is printed on the could-not-evaluate path (`:296-308`), so consumers must not parse that trailer for exit-2 legs.
- The message echoes path/command as written (relative stays relative, absolute stays absolute); the counter's substring checks (`'entry not found:'`, `'command timed out after 120s:'`) are robust to argument form.
- `--entry <directory>` is classified `entry not found` via the `is_file()` guard, not `IsADirectoryError` — no traceback path exists there.
- Self-test is fast and hermetic (1.06 s, private tempdir) and names both declared legs; `GATE_SELFTEST` hold line is `measure.py:179` in the worktree / `:150` at HEAD.

## 6. Risks for wave 2

- The gate as landed at HEAD is correct on both declared legs; the residual C2 risk is entirely in the frozen counter fixture. If wave 2 scores against the unedited fixture, `HOLDS_C2_V1` reads `no` for a fixture bug, i.e. a true claim is falsified.
- If the fixture is repaired only for resolution and not re-run at 120 s, the receipt proves resolution but not the timeout classification. Leg T above is this wave's only captured production-limit observation, and it uses a scratch fixture name (`sleeper_tp.py`), not the committed one.
- The recorded counter sha no longer matches the working-tree bytes (§4); the final measured tip must disclose which counter produced its labels.
- I did not run `measure.py` end-to-end (counter replay is another seat's scope), did not re-run controls A–D, and did not touch C1. No blocker was hit; nothing was deferred for capability reasons.

Report: .ufo/waves/round-71/w1/R71W1TimeoutProbe.md
