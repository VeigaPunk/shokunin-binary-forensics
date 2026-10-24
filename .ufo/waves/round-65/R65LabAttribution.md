NOT-FALSIFIED for C2's after-state (predicate reproduces 2/2 on committed HEAD bytes), but the frozen attribution rule is a one-sided exact-string tail test: rewording the same genuine control's message to `evidence forged` makes the counter score the still-firing mutant kill unattributed (`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=1/2`, `HOLDS_OK_V3=no`) while the probe still exits 0, and a composed-marker tree with no evidence-id check at all scores `2/2` + `HOLDS_OK_V3=yes` at `C5_CONTROL_PRESENT=1/2`, falsifying the counter's stated anti-spoof sentence (`reports/round-65/claims.md:87-90`).

# R65LabAttribution — C5 attribution-predicate sensitivity probe

Seat: calibration lab (`/skill:godspeed`, leaf, no subagent dispatch). Lane production files were **never** written — two disposable scratch trees under `/tmp/r65-attribution`, one deliberate rewrite each; lane hashes identical before/after (below). No tool installs or upgrades were needed; the pacman guard is untouched.

## Surface and provenance

- Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`, HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0`.
- Trees built read-only from the committed archive (working tree == commit for the probed files):
  `git archive 8214e4d corpus | tar -x -C /tmp/r65-attribution/pristine`, then `cp -a` to `variant` and `spoof`.
- Probed file hash in all three trees at start:
  `64dc17ded0e32805c7a546e29e9f1e84dff30a68cb56df2c7d422c625bfbd93b  corpus/verify_icon_languages.py` (== lane HEAD, == lane working tree at end).
  Companion left untouched in every tree:
  `320bf24ce25c01abce4732f02e97954c9596c690807fbc48e03194c957055818  corpus/verify_multi_icon_states.py`.
- Detector (frozen, unmodified): `cd / && TMPDIR=/tmp/r65-attribution python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure.py <tree>`.
- Rule under test, verbatim: `reports/round-65/claims.md:47-49` ("attributed iff the mutant run exits non-zero and its last output line ends with `forged receipt evidence accepted`"), implemented at `reports/round-65/measure.py:263` (`C5_MARKER`), `:302` (`last.endswith(C5_MARKER)`), mutant at `:261`, `:266-275`, runner at `:117-121`.
- Landed control under test: `corpus/verify_icon_languages.py:155-157` (`forged_evidence['evidence_id']='ev_6e0553…2dc3d'`; `require(not receipt_ok(...), f'r{r}: forged receipt evidence accepted')`).

## Probe A — the briefed variant (message reworded, behavior identical)

`variant` differs from `pristine` in exactly one token string, `corpus/verify_icon_languages.py:157`:

```python
require(not receipt_ok(forged_evidence,command,expected_hash,eid,raw_bytes),f'r{r}: evidence forged')
```

Variant hash `20ad3eabd9a73ff53dc2b52b83ad13d8df8b4854227fd4616f668902195081e4`.

Counter lines, pristine (control) run, exit 0 — `/tmp/r65-attribution/pristine.log:36-45,58-60`:

```
C5_CONTROL_PRESENT_verify_icon_languages.py=yes
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted
C5_CONTROL_PRESENT=2/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
HOLDS_OK_V3=yes
```

Counter lines, variant run, exit **0** — `/tmp/r65-attribution/variant.log:36-45,58-60`:

```
C5_CONTROL_PRESENT_verify_icon_languages.py=no
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: evidence forged
C5_CONTROL_PRESENT=1/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=1/2
HOLDS_OK_V3=no
```

`diff pristine.log variant.log` shows exactly five differing lines — `36`, `38`, `42`, `45`, `60` — i.e. the raw kill (`MUTANT … c5 exit=1 killed`) is byte-identical in kind and the only delta is the message tail; `C5_RECEIPT_KILLED` stays `2/2` while attributed drops to `1/2`.

Independent raw-kill check (fresh copy of the variant bytes, frozen `mutate_c5` applied outside the counter, `--self-test`, cwd = tree):

```
PRISTINE  unmutated: exit=0 endswith_marker=False
  last='PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED'
MUTANT    (frozen conjunct deleted): exit=1 endswith_marker=False
  last='AssertionError: r47: evidence forged'
```

Result: the kill fires (exit 1, `AssertionError` raised by the evidence-id control) but the `endswith` predicate returns False. **The counter is doing exactly what the frozen rule says**; the rule itself is exact-suffix and one-sided.

Two consequences worth routing:

1. **Probe exit status cannot gate C2.** `reports/round-65/measure.py:332` exits on `holds_ok` (V1) only, so the variant run above exits **0** while printing `HOLDS_OK_V3=no`. `claims.md:122-123` requires `HOLDS_OK_V3=yes` *and* exit 0; the exit half is insensitive to C5 wording, so a grader must read the `HOLDS_OK_V3` line, never the exit code alone.
2. **`C5_CONTROL_PRESENT` is diagnostic, not gating.** It is computed at `measure.py:280-282` and printed at `:303`, but appears in no `holds_ok*` formula (`:322-330`) and not in the exit path (`:332`). `claims.md:87-90` states it "cannot satisfy the after-state" if a tree prints kills without landing the control — see Probe B.

## Probe B — the same rule from the other side (falsifies claims.md:87-90)

`spoof` tree: the entire evidence-id control (`corpus/verify_icon_languages.py:155-157`) replaced by a **source-text self-inspection with no receipt check at all**, and the marker assembled at runtime so the byte-grep cannot see it:

```python
require(("receipt['evidence_"+"id']==evidence_id") in open(__file__).read(),'forged receipt '+'evidence accepted')
```

Spoof hash `308125040b7cef052ebedc56e8c4d2b9b7976201ffab906745fbd02f7df48042`. In pristine the clause literal is present → the line passes and the pristine run stays green (`MUTANT … control exit=0 pass`); the frozen mutation deletes the clause → the line raises with a last output line that ends with the marker. Counter lines, exit **0** — `/tmp/r65-attribution/spoof.log:36-45,58-60`:

```
C5_CONTROL_PRESENT_verify_icon_languages.py=no
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: forged receipt evidence accepted
C5_CONTROL_PRESENT=1/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=yes
```

`diff pristine.log spoof.log` = 3 lines (`36`, `38`, `42`): attribution `2/2` and `HOLDS_OK_V3=yes` are preserved even though the tree performs zero receipt-evidence verification and reports `C5_CONTROL_PRESENT=1/2`. So the round-end gate (`claims.md:122-123`: `HOLDS_OK_V3=yes` + exit 0) *can* be met without the landed control, and the claim sentence at `claims.md:87-90` is false as written. The guard is only defensible if `c5_present==2` is added to the `holds_ok_v3` formula — that is a next-round counter change, not this round's rule (rule changes after scoring are forbidden by `claims.md:76-78`), and it is routed here as a finding only.

## Verdict and scope statement

- C2 **not falsified** on committed HEAD bytes: the landed controls are real (pristine log above; `corpus/verify_multi_icon_states.py` untouched and attributed 2/2 in all three runs), and the counter reproduces `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`, `HOLDS_OK_V3=yes`, exit 0.
- The **attribution predicate's precision** is as demonstrated: exact-suffix, conservative on wording drift (false negative), and satisfiable by a non-evidence detector that emits the marker (false positive) whenever the marker is composed at runtime. Neither observation requires a lane edit; both are recorded for the round lesson (`STRICT`/string-tail surface family alongside M37).
- Independent of wording, all non-C5 counter lines are identical across the three runs (60-line logs, diffs above), so the observed deltas are causally attributable to the single-string rewrites.

## Restoration evidence

- Lane bytes never mutated: `sha256sum corpus/verify_icon_languages.py` = `64dc17de…d93b` both before and after the probe; companion = `320bf24c…5818`; `git rev-parse HEAD` = `8214e4dd…dbe0`. No `git`/`jj` mutation, no lane file written, no sibling report touched.
- Scratch trees are disposable and left in place for inspection: `/tmp/r65-attribution/{pristine,variant,spoof,direct}` with logs `pristine.log`, `variant.log`, `spoof.log` (60 lines each).
