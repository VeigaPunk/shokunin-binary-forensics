# R71W2CounterReplay — final-tip counter replay, C2 both legs green, C1 red only for the absent committed votes

**Verdict (instrument replay, not a Q verdict):** the frozen counter is faithful and deterministic on the final candidate tip — `git archive` replay at `a16e6cb` (A3 counter `82c817e1…`) and at `c6e284c` (A2 counter `718daa96…`) produce **byte-identical** receipts (stdout `075de59f…`, exit 0, stderr 0 bytes, ten `HOLD` rows), both C2 legs are green from a real archive tree (`C2_MISSING_ENTRY_EXIT2=1/1`, `C2_TIMEOUT_EXIT2=1/1`, `rc=2`, no traceback, `HOLDS_C2_V1=yes`), and C1 is red **only** on `C1_W2_Q_VOTES=0/16` because no committed `.ufo/waves/round-71/w2-votes/` exists yet at any lane commit (C05 still `uncovered`, entry still `candidate`; the adjudication revision has not landed). In a scratch replica of the registered adjudication the counter turns `HOLDS_C1_V6=yes` with `K 9/14` and the ten HOLD rows intact — but that same green receipt is produced **without** the landing rule's `K_HELD_BACKED 8/14 → 9/14` SCORECARD row, which only the separate self-assessment instrument catches (`SM6=1`). Three operability constraints for L1 are located below (§7 F1–F3). **Wave state changed while this seat ran:** the first real vote file landed at 13:18 with `Q09=FAIL` (§9), which makes the `16/16` conjunct unreachable while that file stands — the kill-rule consequence belongs to L1 and to the reviewer's located defect, not to this replay.

seat: `R71W2CounterReplay` · wave 2 (fresh falsification) · measured 2026-10-27 13:04–13:25 -03
lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` · measured commits `c6e284c` then `a16e6cb`; tree `db7c4ceb…`
scratch: `/fast/scratch/hyaku/revenger-r71/R71W2CounterReplay/` (deleted after receipts copied here)
No seat judges the round; nothing below admits or rejects any Q01–Q16 decision.

## 1. Receipts

| object | sha256 / value |
|---|---|
| counter at HEAD (`git show HEAD:reports/round-71/measure.py`) | `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61` (A2, as registered) |
| counter worktree bytes used by run5/run6 (A3) | `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2` (A3, mtime 13:13:57, **uncommitted**) |
| claims (`reports/round-71/claims.md`) | `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5` (unchanged through A1/A2/A3) |
| red-before (`reports/round-71/measure-before.log`) | `7a9428048825e542139670a462e3d6067466c5a8157b2e3c0bdcb22c9f761407`, 10 `HOLD` lines, `MEASURE_EXIT=0` (A3 rerun at 13:14:59 is byte-identical to the A2 rerun) |
| measured tip when the replay finished | `33fadb2` (`a16e6cb` → `33fadb2` commit only adds A3, its receipts, and deletes a `.pyc`) |
| `corpus` subtree at `a16e6cb` and at `33fadb2` | `c6cc640b03e1631b864c4967709b667bb6bae291` at both — the measured tree is the same object at either SHA, so run5's receipt describes both |
| counter at `33fadb2` (HEAD blob = worktree) | `82c817e1…` = the A3 bytes run5/run6/run7 used |
| archive of `a16e6cb` (`corpus SHONEN.md SCORECARD.md SKILL.md`) | `90b4d49a9088119c9db53fbccefb656f024fc996737e062588d5f8c88f48dc14` (the same archive can be taken at `33fadb2` because its `corpus` subtree is identical) |
| archive of `c6e284c` (same paths) | `dbfc4f8768a1bbadaf7290b153905f6aba58be83d470df392e1f31d006e7e50f` |

## 2. Commands

```
# archive replay tree (cwd lane), then run from / as the seat spec requires
git -C <lane> archive --format=tar <SHA> corpus SHONEN.md SCORECARD.md SKILL.md > tree.tar && tar -xf tree.tar -C tree
cd / && HYAKU_SCRATCH=<scratch> python3 -B <lane>/reports/round-71/measure.py <scratch>/tree
```

| run | counter | tree | wall | stdout | stderr | exit |
|---|---|---|---|---|---|---|
| run1 | A2 `718daa96` | `c6e284c` | 125.46 s | `075de59f…` | 0 B | 0 |
| run5 | A3 `82c817e1` | `a16e6cb` | 124.61 s | `075de59f…` (`RUN1_RUN5_IDENTICAL=yes`) | 0 B | 0 |
| run2 | A2 | replica, flip+admitted+votes, **no** SCORECARD row | 124.66 s | `5986865a…` | 0 B | 0 |
| run3 | A2 | replica + SCORECARD row | 124.50 s | `0eb2c8d3…` | 0 B | 0 |
| run4 | A2 | run3 repeated | 124.44 s | `0eb2c8d3…` (`cmp` identical) | 0 B | 0 |
| run6 | A3 | run3 tree, A3 bytes | 124.60 s | `0eb2c8d3…` (`RUN3_A2_vs_RUN6_A3_IDENTICAL=yes`) | 0 B | 0 |
| run7 | A3 | `a16e6cb` + entry marked `rejected` (kill-rule shape) | 124.73 s | `075de59f…` (= run5) | 0 B | 0 |

Every run costs ~125 s because the C2 timeout leg genuinely waits out the production 120-second limit (`measure.py:101-107`); nothing here short-circuits it.

## 3. Final-tip receipt (`a16e6cb`, A3 counter, run5) — all labels

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
C2_TIMEOUT_EXIT2=1/1 rc=2 stderr_traceback=no
C2_GATE_SELFTEST=0 named_legs=1
HOLDS_C2_V1=yes
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

Ten individual `HOLD` rows are present, `HOLD_REPLAY=10/10`, exactly as the round-70 omission correction requires. `EMB_R65 problems=1 exit=1` is **not** a regression: it is identical in `measure-before.log`, so the retained-round-70 hold is unchanged.

Diff of run5 against `measure-before.log` (base) has exactly the expected cells and no others: `V6_ENTRY_PRESENT no→yes`; `C1_GATE/C1_LINT n/a → checked_blocks=24 problems=0 / LINT 0/0/0/0 exit=0`; both C2 legs `0/1 rc=1 traceback=yes → 1/1 rc=2 traceback=no`; `C2_GATE_SELFTEST named_legs 0→1`; `HOLDS_C2_V1 no→yes`; plus the harness `MEASURE_EXIT=0` trailer that the recording wrapper appends.

## 4. C2 legs — exact text and shape

On the archived tree (`tree-run1`, identical bytes to `tree-final` for `corpus`):

```
$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed
SELFTEST_EXIT=0

$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-missing-entry.md
could-not-evaluate: entry not found: corpus/knowledge/round-71-missing-entry.md
MISSING_EXIT=2
```

The timeout leg was verified through the counter's own substring assertion (`measure.py:105-107`: `'could-not-evaluate: command timed out after 120s:' in stdout`, `rc==2`, no `Traceback`), which recorded `1/1` in runs 1, 3, 4, 5, 6; the ~125 s wall time per run is the corroborating evidence that the production limit was actually consumed rather than short-circuited by drift.

## 5. C1 vote binding — A2/A3, verified independently of any real vote

`q_votes(TREE)` was exercised directly against synthetic trees under scratch (`import` of the frozen module; no lane data used as input). A2 bytes `718daa96`:

| input | `q_votes` |
|---|---|
| four valid per-seat files, 16 `PASS` | 16 |
| 16 × `n/a` | 16 |
| one `FAIL` value | 0 |
| one assigned Q missing | 0 |
| extra Q key beyond the assigned four | 0 |
| stem ≠ `seat` | 0 |
| duplicate seat file (`_dup.json`) | 0 |
| duplicate decision key (`"Q09":"FAIL","Q09":"PASS"`) | 0 |
| valid non-object root (`[1,2]`) | 0 (no exception, receipt not truncated) |
| votes dir absent / `.ufo` absent | 0 |
| malformed `stray.JSON` (upper-case suffix) | **16** (ignored, not refused) |

A3 bytes `82c817e1`, same fixtures plus containment:

| input | `q_votes` |
|---|---|
| four valid per-seat files | 16 |
| vote member is a symlink | 0 |
| vote root is a symlink | 0 |
| non-regular member (FIFO) | 0 |
| unhashable `seat` (`["x"]`) | 0 |
| duplicate decision key / non-object / `FAIL` / missing Q / stray `.JSON` | 0 / 0 / 0 / 0 / **16** |

So amendment A2's two registered refusals (duplicate keys, non-object roots) and A3's containment additions hold, and the counter's vote source is the measured `TREE` — confirmed end-to-end by runs 2/3/6 (§6), where the only difference from run5 is the votes directory inside the archived tree.

## 6. Adjudicated-shape replica (label: simulation, **not** a vote)

Trees built only in scratch from the `c6e284c` archive: (a) registered flip replica of `build-controls.py:27-34` (`flip(d, True)` on the C05 row), (b) `admission-status: candidate… → admitted` on line 12 of the v6 entry, (c) four synthetic `seat`/`decisions` files with all-`PASS` values (instrument input, **not** reviewer decisions), (d) the landing rule's SCORECARD statement appended.

| run | SCORECARD row | C1 | SM6 / SELF_MISMATCH | exit |
|---|---|---|---|---|
| run2 | **absent** | `K 9/14`, `C05_STATUS=held`, `C05_SINGLE_V6=yes`, `V6_ADMITTED_MARKED=yes`, `C1_GATE=24/0`, `C1_LINT 0/0/0/0`, `C1_W2_Q_VOTES=16/16`, `HOLDS_C1_V6=**yes**` | `SM6=1`, `SELF_MISMATCH=1 exit=1` | **0** |
| run3/run4/run6 | `K_HELD_BACKED 8/14 → 9/14` appended at EOF | identical rows (`HOLDS_C1_V6=yes`, `HOLDS_C2_V1=yes`) | `SM6=0`, `SELF_MISMATCH=0 exit=0` | 0 |

Full run3 label set (run4 and run6 are `cmp`-identical): uniform `0eb2c8d3…`, 45 metric lines, ten `HOLD` rows, `HOLD_REPLAY=10/10`, `HOLDS_OK_V8=yes`, `EMB_*` and `SELF_CLEAN_FIXTURE=1`, `SELF_MUTANTS_KILLED=6/6` unchanged.

SM6 position probe (`self_assessment_check.py:175-190` takes the **last** `K_HELD_BACKED` line): inserting `K_HELD_BACKED 8/14 → 9/14` before the existing terminal `K_HELD_BACKED 8/14 → 8/14` gives `SM6=1, SELF_MISMATCH=1, exit=1`; appending it at EOF gives `SM6=0, SELF_MISMATCH=0, exit=0`.

## 7. Findings (instrument/operability, no Q judged)

- **F1 — the counter does not bind the landing rule's SCORECARD row.** Run2 is measured proof: README flipped to `held` + v6 admitted + 16/16 votes with **no** `K_HELD_BACKED 8/14 → 9/14` row yields `HOLDS_C1_V6=yes` and counter exit 0. `SELF_MISMATCH=1` is printed and discarded (`measure.py:138` sets `self_ok`, `measure.py:163` `holds` never reads it; `measure.py:92` `c1` never reads it). The registered adjudication revision must therefore append the row by discipline, not by gate; the counter cannot catch its omission.
- **F2 — SM6 needs the row at EOF**, not merely present: the same statement inserted mid-file leaves `SM6=1` (probe above). Appending after the existing terminal `K_HELD_BACKED 8/14 → 8/14` line is the shape that scores 0.
- **F3 — the mandated archive command fails closed if the vote path is not committed.** At `a16e6cb`:

  ```
  $ git archive --format=tar HEAD corpus SKILL.md SCORECARD.md SHONEN.md .ufo/waves/round-71/w2-votes > t.tar
  fatal: pathspec '.ufo/waves/round-71/w2-votes' did not match any files   # exit 128, t.tar = 0 bytes
  ```
  A `&&` chain stops safely; a `;`/newline chain feeds an empty tar onward and the counter then exits 2 (`usage: measure.py TREE`). Control: `git archive HEAD .ufo/waves/round-71/w1-attack-inventory.md` exits 0 and yields `.ufo/…` members, so dot-paths archive normally once committed — the votes directory must exist in the measured commit before this single-command replay is used.
- **F4 — counter bytes moved mid-wave.** A3 (`82c817e1…`) was written at 13:13:57 and documented at 13:14:38, after the W2 topology freeze `c6e284c` (13:03) and after `.ufo/waves/round-71/w2.ready.dispatched` (13:04) while W2 seats were scoring. `reports/round-71/post-freeze-corrections.md` records this. My runs 1–4 straddle that boundary (run1–run3 = A2, run5/run6 = A3); runs 3 and 6 are byte-identical, and run1/run5 are byte-identical, so no observed label moves — but any W2 receipt citing counter bytes must name which SHA it used, and the red-before (`7a942804…`) is unchanged by the A3 rerun.
- **F5 — vote-file contract vs instrument.** The W2 contract says each vote file has *exactly* the keys `seat` and `decisions`; the counter accepts extra top-level keys (probe: `{"seat":…,"decisions":{…},"note":"x"}` → 16). Low severity, worth a claims line rather than a re-gate.
- **F6 — case-sensitive vote glob (pre-existing, W1 §5 A8).** A malformed `stray.JSON` in the votes directory is silently ignored (`root.glob('*.json')`), still scoring 16/16.
- **F7 — the vote files remain structural receipts.** `q_votes` checks stems, assigned-Q sets and values only (as A2/A3 state); `HOLDS_C1_V6=16/16` in runs 3/4/6 is an instrument result over synthetic `PASS` bytes and is **not** evidence that any reviewer voted PASS.

## 8. Blockers and residuals

- **No committed votes exist at any lane commit** (`git ls-tree -r HEAD -- .ufo/waves/round-71/w2-votes` is empty at `33fadb2`), so the operative C1 measurement from a commit is `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`, `C05_STATUS=uncovered`, `V6_ADMITTED_MARKED=no`. Two vote files exist only in the worktree (13:18/13:24), one of them carrying `Q09=FAIL` (§9); the frozen predicate can only be satisfied by votes that are committed and all `PASS`/`n/a`.
- **The adjudicated commit does not exist yet.** HEAD `33fadb2` is pre-adjudication (votes uncommitted, C05 `uncovered`, entry `candidate`); L1's adjudication or honest-stop revision is what the last replay must measure. Because `corpus` is the same object at `a16e6cb` and `33fadb2` (`c6cc640b…`) and the counter at HEAD is the A3 `82c817e1…` bytes used here, run5's receipt already describes `33fadb2`; the post-adjudication replay is F3's command with the new SHA, and §6 run3/run6 (honest admission shape) or §9 run7 (honest-stop shape) give the expected label sets, both exit 0 with ten HOLD rows.
- **`EMB_R65 problems=1 exit=1`** is a retained round-70 hold, unchanged from red-before; it is not attributable to this round's candidate.

## 9. Wave-2 vote state observed while this seat ran (fact, not a verdict)

Two real vote files appeared while this seat ran (both **uncommitted**; `git ls-tree -r HEAD -- .ufo/waves/round-71/w2-votes` is empty at `33fadb2`), 13:18 and 13:23:

```
$ ls -la .ufo/waves/round-71/w2-votes/          # 13:18 capture; Q01Q04 landed 13:23
-rw-r--r-- 1 vgpnk vgpnk 87 Oct 27 13:18 R71W2Q09Q12.json
$ cat .ufo/waves/round-71/w2-votes/R71W2Q09Q12.json
{"seat":"R71W2Q09Q12","decisions":{"Q09":"FAIL","Q10":"PASS","Q11":"PASS","Q12":"n/a"}}
sha256 140ae8628a74b0df5ab2b8ca43fc80c062caa709b0990115b28fa13c91592bbc

$ cat .ufo/waves/round-71/w2-votes/R71W2Q01Q04.json
{"seat":"R71W2Q01Q04","decisions":{"Q01":"PASS","Q02":"PASS","Q03":"PASS","Q04":"PASS"}}
sha256 3b03a703aa2d05e5afb4b6222cd9e14b2cb2e0b70fe98d9cee0c7c66c3a50ca2
```

Instrument reading of those exact bytes (A3 `q_votes` over an archive copy with the file placed under `TREE/.ufo/waves/round-71/w2-votes/`): `q_votes(TREE)=0`, parsed object as above, decision key set exactly `Q09–Q12`. Both files are structurally conformant (unique keys, exact assigned sets, `PASS`/`n/a` values as assigned); the `Q09`-file placement yields `q_votes=0` with both files present, i.e. it is refused **solely** for the `FAIL` value, and `R71W2Q05Q08`/`R71W2Q13Q16` had not yet written when this seat closed.

Reviewer's located defect, as filed in `.ufo/waves/round-71/w2/R71W2Q09Q12.md`: the entry's Q09 basis (`corpus/knowledge/round-71-apk-axml-byte-evidence.md:308`) states "the builder script outside `corpus/` is named as undigested", while the only named builder is `corpus/fixtures/apk-r65/generator.py` and item 14 hashes that exact in-corpus file (`:225`, `sha256 eaa9444c…`). That contradiction is the reviewer's evidence; this seat only confirms the file's bytes and the counter's reading of them.

Consequences that follow mechanically from the frozen predicate and kill rule — for L1 to execute, not for this seat:

- `C1_W2_Q_VOTES` can never reach `16/16` while this file stands, because `decisions` values other than `PASS`/`n/a` make `q_votes` return 0 outright (`measure.py:64-70`).
- Therefore `HOLDS_C1_V6=no` regardless of the other twelve Q decisions, and no `K_HELD_BACKED 8/14 → 9/14` row or README flip is admissible.
- The §4 kill rule applies if this vote is final and committed: keep C05 `uncovered`, mark only the v6 `admission-status` line `rejected`, save every other byte, and report C1 falsified / honest stop — **no repair or re-gate after the vote**.
- The file was uncommitted when measured; a later change to it is its author's act and must be re-measured from the commit, not inferred from this receipt.

The mandated kill-rule edit was also measured on the final-tip archive (run7: entry line 12 `candidate… → rejected`, no votes, nothing else changed, A3 counter, 124.73 s): `K_HELD_BACKED=8/14`, `C05_STATUS=uncovered`, `V6_ADMITTED_MARKED=no`, `C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes`, `C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0`, `C1_W2_Q_VOTES=0/16`, `HOLDS_C1_V6=no`, `HOLDS_C2_V1=yes`, ten `HOLD` rows, `HOLDS_OK_V8=yes`, stderr 0 bytes, exit 0 — and its stdout is **byte-identical** to run5's (`075de59f…`). So the honest-stop mark leaves gate, lint and both C2 legs green, and the counter cannot distinguish `admission-status: candidate` from `admission-status: rejected`: it only tests for the literal `admitted` line (`measure.py:79`). The distinction therefore lives in the entry bytes and the report, not in the counter receipt.

**F8 — `0/16` is ambiguous on the receipt line.** `C1_W2_Q_VOTES=0/16` is printed identically for "no vote files", "incomplete assignment", "malformed" and "a `FAIL` was cast" (§5 matrix, §9). The counter never prints which Q failed, so a reader of the receipt alone cannot tell a falsified wave from a not-yet-voted one; L1 must read the four vote files/reports to locate the failing Q. This is a reporting limitation of the frozen counter, not a change to its predicate.

## 10. Scope, tooling, cleanup

- Writes: this report only (plus scratch). No source, no votes directory, no `w2-votes`, no SCORECARD/README/claims edit, no git/jj mutation, no fleet-root or sibling-lane write, no `agent://all`, no subagent dispatch.
- Tooling: Python 3 stdlib only; nothing installed or updated; no pacman transactions; no route/config change.
- Scratch `/fast/scratch/hyaku/revenger-r71/R71W2CounterReplay/` held the archives, the seven run captures and the probe trees; it is deleted after these receipts were copied here. The counter's own `revenger-r71/counter` scratch is removed by `measure.py:69`'s `finally`.
