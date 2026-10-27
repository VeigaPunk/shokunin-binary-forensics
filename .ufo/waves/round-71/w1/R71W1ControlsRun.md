# R71W1ControlsRun — frozen controls A–D audit

VERDICT: **D confirmed, controls reproducible, but two receipt/probe defects make the frozen gate un-greenable as written** — D reaches K 9/14 + gate/lint clean and dies only on `C1_W2_Q_VOTES=0/16` exactly as claimed (labels byte-identical on re-execution), yet the counter's C2 timeout fixture never sleeps (so `HOLDS_C2_V1` can never be `yes`) and three named receipts are missing or stale. Repair the fixture before the final candidate lands; no lane edits made by this seat.

Seat: leaf audit, no spawn. Base `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f`; lane HEAD observed `18200a4 round-71: build v6 candidate and gate exit-2 cases`. Access date for all opened lane files: 2026-10-27. New external source rows: 0.

## 1. Frozen artefacts hash to the receipt

```
d0d59b79…f38d06c  reports/round-71/measure.py      (== pre-registration "Counter SHA-256")
1febae12…8321c3f5  reports/round-71/claims.md       (== pre-registration "Claims SHA-256")
```

So the audited counter and claims are the ones frozen at 12:14.

## 2. Control D reproduced from the frozen base (independent driver, my scratch)

Re-executed D exactly as `reports/round-71/build-controls.py:35-44` defines it (archive base, C05 flip to `knowledge/round-71-apk-axml-byte-evidence.md` + `held`, v5.1 bytes copied to the v6 path, first `admission-status: rejected` → `admitted`, Q16 row inserted). Exact labels:

```
K_HELD_BACKED=9/14 score=6.4
K_HELD_BACKED_STRICT=9/14
C05_STATUS=held
C05_KNOWLEDGE_COLUMN=knowledge/round-71-apk-axml-byte-evidence.md
C05_SINGLE_V6=yes
V6_ENTRY_PRESENT=yes
V6_ADMITTED_MARKED=yes
C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
C1_W2_Q_VOTES=0/16
HOLDS_C1_V6=no
```

`diff` of my run against `reports/round-71/controls/D-C1-v5-copy-with-q16.log` (trailer line excluded) prints nothing → `LABELS_IDENTICAL`. D therefore isolates exactly one conjunct: every other C1 term is green and `HOLDS_C1_V6=no` follows solely from the vote-file predicate at `measure.py:68-85` (`q_votes()`), matching the frozen control statement ("D reaches K 9/14 and clean gate/lint but fails… at `C1_W2_Q_VOTES=0/16`"). `ls .ufo/waves/round-71/w2-votes` → `No such file or directory`, so 0/16 is the honest pre-wave-2 baseline.

A/B/C are consistent with the same counter: A `K_HELD_BACKED=8/14`, `C05_STATUS=uncovered`; B flips status only (`C05_SINGLE_V6=no`, still 8/14); C names the v6 path with `V6_ENTRY_PRESENT=no` and `C1_GATE=n/a`. All three read `HOLDS_C1_V6=no`.

## 3. BLOCKING: the counter's C2 timeout leg cannot reach the timeout

`measure.py:129-132` copies `corpus/` into the fixture tree, writes the sleeper at `corpus/sleeper_r71.py`, and writes the entry command as `python3 -B sleeper_r71.py`, but invokes the gate with `cwd=` the **tree root**. The child therefore looks for `<tree>/sleeper_r71.py`. Reproduced against both the frozen base and HEAD:

```
base: drift entry:2 command exited 2: python3 -B sleeper_r71.py / checked_blocks=0 problems=1  rc=1 (0.05s)
HEAD: drift entry:2 command exited 2: python3 -B sleeper_r71.py / checked_blocks=0 problems=1  rc=1
```

No 120-second wait occurs, so `C2_TIMEOUT_EXIT2=0/1` is structural, not behavioural — and that same value is printed by every control (A–D). Confirmed the HEAD implementation is *not* the cause: with the command spelled `python3 -B corpus/sleeper_r71.py` and an injected 1 s timeout, `evaluate()` raises `could-not-evaluate: command timed out after 1s: python3 -B corpus/sleeper_r71.py` (`HEAD:corpus/check_embedded_outputs.py:102-114`), and HEAD's missing-entry leg already gives `rc=2` with `could-not-evaluate: entry not found: …` and no traceback. Consequence: at the final candidate `HOLDS_C2_V1` stays `no` even with C2 correctly implemented — the frozen predicate would read as a falsification of a true claim. Required wave-1 repair: move the sleeper to the fixture tree root (or spell the entry command `corpus/sleeper_r71.py`) and re-record the counter digest in `pre-registration.txt`, which currently binds `d0d59b79…`.

## 4. Receipt gaps and provenance flaws (no source impact, evidence chain only)

1. **Absent red-before receipt.** `claims.md:23` names `controls/C2-missing-before.log`; the directory contains only `A-…`, `B-…`, `C-…`, `C2-timeout-before.log`, `D-…`. The missing-entry red is observable only in aggregate via `C2_MISSING_ENTRY_EXIT2=0/1 rc=1 stderr_traceback=yes` inside A.
2. **Control A is a byte-identical copy of the red-before log** (`sha256 e2ea4fc3…b608586` for both `measure-before.log` and `A-do-nothing-base.log`). A is therefore not an independent execution and carries no `CONTROL=` trailer, unlike B/C/D. Acceptable as data, but it must not be cited as a second run.
3. **D's trailer does not match its producer.** `D-C1-v5-copy-with-q16.log` ends `CONTROL=D-C1-v5-q16-vote-control EXIT=0`; `build-controls.py:21` would print `CONTROL=D-C1-v5-copy-with-q16`. Additionally `build-controls.py` mtime (12:15:53) is later than every control log (latest 12:15:20) and later than `claims.md` (12:13:02) — the committed builder is not the exact producer of the committed receipts.
4. **E and F are declared but never built or run.** `claims.md:27` registers E (declared text, exit 1 retained) and F (missing-entry only) with "both read `HOLDS_C2_V1=no`", while `pre-registration.txt:7` lists only A–D and `build-controls.py` has no E/F function and no E/F log exists. This also contradicts `claims.md:17` ("No additional exit-text-only control is claimed"). Either build both or strike them from the frozen text before wave-2 scoring.
5. **`C2-timeout-before.log` post-dates the frozen claims** (mtime 12:15:20 vs claims 12:13:02) and its traceback shows the double-flag child `['-B', '-B', 'sleeper.py']` from a scratch tree at `/fast/scratch/…`, i.e. the fixture placement that *does* sleep was a one-off, not the counter's.

6. **Stale vote mechanism in the C1 control sentence.** `claims.md:17` explains D's red as "no orchestrator `w2-results.json`, so `C1_W2_Q_VOTES=0/16`", but the frozen counter never reads `w2-results.json`: `q_votes()` (`measure.py:68-85`) requires four per-seat files under `.ufo/waves/round-71/w2-votes/` keyed by `R71W2Q01Q04`/`Q05Q08`/`Q09Q12`/`Q13Q16`. The observed 0/16 comes from that directory being absent, not from a missing results file — align the sentence with the implemented predicate.

## 5. Control-side observations for the final gate (advisory, not defects of D)

- **D's admitted header still declares rejection.** The rewrite at `build-controls.py:39` changes only the first token; the line then reads `admission-status: admitted — the round-70 fifth-pass candidate (v5.1, …), REJECTED by the dispatched wave-2 decisions on these bytes …`. `C1_LINT` returns `LINT_HEADER=0` because `corpus/lint_entry.py:20` checks only that the first lines carry `source:`/`verified-at:`/`recheck:` — header self-contradiction is a wave-2 Q-map judgement, not a lint catch. Do not read `LINT_HEADER=0` as "no rejection marker".
- **Flip visibility:** A prints `SM1..SM6=0 / SELF_MISMATCH=0`, while B, C and D all print `SM6=1 / SELF_MISMATCH=1 exit=1` (still `HOLDS_OK_V8=yes`). Flipping C05 without a consistent knowledge map is visible to `self_assessment_check.py`; the final candidate must keep `SELF_MISMATCH=0`, which is a stricter requirement than any control exercises.
- **Votes are out-of-band by construction.** `q_votes()` (`measure.py:68`) reads the absolute lane path `LANE/.ufo/waves/round-71/w2-votes`, never the `TREE` argument, so `HOLDS_C1_V6` is not a pure function of the measured snapshot: any later vote directory flips D as well. This is consistent with the frozen claim (committed per-seat JSON files) but should be stated in the Gate draft so D's isolation is not over-read.
- Minor, unexercised: `backed()`/`strict` (`measure.py:26-38`) inspect only the first `knowledge/…` path in a row (`split('|')[3]`, `findall(...)[0]`); a multi-path C row would have its extra entries' admission status ignored. No current row is multi-path.
- The ten per-verifier `HOLD <name> exit=…` rows are present and complete in A–D (`HOLD_REPLAY=10/10`), so round-70's routed receipt omission is indeed corrected by this round's captured output.

## 6. Recommendation to L1 (wave-1 advisory, pre-gate)

1. Fix the C2 timeout fixture placement in `measure.py` (sleeper at tree root, or command `corpus/sleeper_r71.py`), re-run A–D, re-record counter sha in `pre-registration.txt`; without this C2 cannot read green.
2. Add `controls/C2-missing-before.log` (or amend `claims.md:23` to cite the base leg already inside A).
3. Either build/run E and F with receipts or delete them from the frozen control text, and resolve the E/F contradiction at `claims.md:17` vs `:27`.
4. Re-generate B/C/D with the committed `build-controls.py` so the D trailer matches its producer, and mark A as a copy of `measure-before.log` rather than a separate execution.

Scratch `/fast/scratch/hyaku/revenger-r71/R71W1ControlsRun/` used and deleted after the receipts above were transcribed; no `/tmp`, no pacman, no installs, no lane source writes.

Report: `.ufo/waves/round-71/w1/R71W1ControlsRun.md`
