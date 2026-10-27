# R71W2GateReplay — C2 gate exit-2 replay and retained-hold recheck

VERDICT: **PASS — no located defect on the assigned surface.** The real CLI classifies a nonexistent entry and a production-timeout entry as exit 2 with the registered `could-not-evaluate:` text and no traceback, `--self-test` exits 0, the v6 entry gate/lint are green, and every retained pin/drift/HOLD label is byte-identical to the frozen red-before. This seat is not a vote owner: nothing here adjudicates C1 Q01–Q16, and `C1_W2_Q_VOTES=0/16` is mid-wave expected state, not a finding.

Seat: `R71W2GateReplay` (fresh wave-2 leaf, read-only; no source edits, no vote file, no commit). Date: 2026-10-27.

## 1. Identity of what was measured

- Assigned candidate/build commit: `4c1eeaee88fd07e442f1bd546faf77be3957d390`, tree `b6f07f5af8cab9f91019a718024b1254d85ae6c1`.
- Live lane tip during this seat: `a16e6cbe24c51e6952e973d6b47560b49311420d` ("round-71: curate sources and record frontier mistakes"), tree `db7c4ceb720080e800c2992141fc2fbbffd88092` — the tip moved after the candidate while W2 was in flight.
- Both commits were measured. Instruments are byte-identical across them (so the result transfers):

```
$ for c in 4c1eeae a16e6cb; do git show $c:corpus/check_embedded_outputs.py|sha256sum; git show $c:corpus/lint_entry.py|sha256sum; git show $c:corpus/knowledge/round-71-apk-axml-byte-evidence.md|sha256sum; done
4c1eeae gate=05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8 lint=3ef6c7b119b2a5003afdf38ed7981d445565d7575e9aa437e60147393183d76b v6=671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092 tree=b6f07f5af8cab9f91019a718024b1254d85ae6c1
a16e6cb gate=05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8 lint=3ef6c7b119b2a5003afdf38ed7981d445565d7575e9aa437e60147393183d76b v6=671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092 tree=db7c4ceb720080e800c2992141fc2fbbffd88092
$ git diff --stat 4c1eeae HEAD -- corpus
 corpus/SOURCES.md          | 4 ++--
 corpus/lessons/round-71.md | 2 +-
 2 files changed, 3 insertions(+), 3 deletions(-)
$ git diff 4c1eeae c6e284c -- corpus | wc -c
0
```

Both trees were exported read-only with `git archive <commit> | tar -x -C <scratch>` and all legs were run inside the export, matching the counter's TREE model. `lint_entry.py` was called with `--lane /home/vgpnk/Projects/shokunin/revenger-shokunin` exactly as the counter does. Lane worktree status for `corpus/` was `?? corpus/__pycache__/` only (untracked interpreter cache, not an edit by this seat).

## 2. Frozen C2 predicate, conjunct by conjunct

| Frozen conjunct (C2, `HOLDS_C2_V1=yes`) | Observed at tip | Evidence |
|---|---|---|
| nonexistent entry → real CLI exit 2, prints `could-not-evaluate: entry not found:`, no traceback | exit 2, exact text, 0 tracebacks | §3.1 |
| valid entry, declared in-tree command exceeds the 120 s limit → exit 2, prints `could-not-evaluate: command timed out after 120s:`, no traceback | exit 2, exact text, elapsed 120 s, 0 tracebacks | §3.2 |
| `--self-test` exits 0 with fast hermetic cases for both behaviors | exit 0, ~1.09 s, `SELFTEST OK` names missing-entry and timeout | §3.3 |
| registered SKILL.md row names these exact mappings | row 296 names `could-not-evaluate: entry not found:` / `could-not-evaluate: command timed out after 120s:` and "no traceback", and states the self-test injects 1 s | §3.4 |
| existing gate behavior is a hold (v6 gate/lint, retained `EMB_*`/pin labels, confinement, verbatim comparison) | all retained labels byte-identical to `measure-before.log` | §4 |
| counter prints every verifier `HOLD <name> exit=…` row | 10/10 individual rows present | §5 |

## 3. Exact commands and outputs (tip archive)

All commands `cd` into the scratch export; nothing was written under the lane.

### 3.1 Missing-entry CLI

```
$ python3 -B corpus/check_embedded_outputs.py --entry "$PWD/corpus/knowledge/round-71-missing-entry.md"
could-not-evaluate: entry not found: /fast/scratch/hyaku/revenger-r71/R71W2GateReplay/tip/corpus/knowledge/round-71-missing-entry.md
MISSING_RC=2
TB=0            # grep -c Traceback <stderr>
```
stderr was empty. The live-lane copy of the same call (absolute path, cwd = lane) returned identically: `LIVE_MISSING_RC=2`, same text, `TB=0`.

### 3.2 Production 120 s timeout via the real CLI (scratch in-tree fixture)

```
$ cp -a corpus to/corpus
$ printf 'import time\ntime.sleep(300)\n' > to/corpus/sleeper_r71.py
$ printf '```\n$ python3 -B corpus/sleeper_r71.py\nfinished\n```\n' > to/corpus/knowledge/round-71-timeout-probe.md
$ cd to && python3 -B corpus/check_embedded_outputs.py --entry "$PWD/corpus/knowledge/round-71-timeout-probe.md"
TIMEOUT_RC=2 elapsed_s=120
---STDOUT---
could-not-evaluate: command timed out after 120s: python3 -B corpus/sleeper_r71.py
---STDERR---
---TRACEBACK_COUNT---
to/timeout.err:0
to/timeout.out:0
```

The 120 s elapsed bounds the gate's production limit (the sleeper sleeps 300 s; the fixture is in scratch, not the lane, and the gate's runtime constant `TIMEOUT=120` was not touched). The counter's own independent CLI leg at the tip also read `C2_TIMEOUT_EXIT2=1/1 rc=2 stderr_traceback=no` (§5).

Falsification of the pre-amendment spelling, to show A1 is load-bearing and the green above is not a fast drift:

```
$ printf '```\n$ python3 -B sleeper_r71.py\nfinished\n```\n' > preA1/corpus/knowledge/round-71-timeout-probe.md
$ cd preA1 && timeout 30 python3 -B corpus/check_embedded_outputs.py --entry "$PWD/corpus/knowledge/round-71-timeout-probe.md"
drift entry:2 command exited 2: python3 -B sleeper_r71.py
checked_blocks=0 problems=1
PREA1_RC=1
```
i.e. the old relative spelling never reaches the timeout and would have scored the leg red for the wrong reason (stderr already located by `R71W1Sentinel` §F1); the amended `corpus/sleeper_r71.py` does reach it.

### 3.3 Gate self-test

```
$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed
SELFTEST_RC=0   elapsed_ms=1088
```

### 3.4 v6 entry gate and lint

```
$ python3 -B corpus/check_embedded_outputs.py --entry "$PWD/corpus/knowledge/round-71-apk-axml-byte-evidence.md"
checked_blocks=24 problems=0
GATE_RC=0

$ python3 -B corpus/lint_entry.py --entry "$PWD/corpus/knowledge/round-71-apk-axml-byte-evidence.md" --lane /home/vgpnk/Projects/shokunin/revenger-shokunin
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
LINT_RC=0
```
24 checked blocks ≥ the frozen 17-block floor, zero problems. The registry row checked:

```
$ grep -n "could-not-evaluate\|timed out\|entry not found" SKILL.md
288:| verdict map | `0` clean … · `1` failed … · `2` could-not-evaluate (no `$ cmd` blocks, unsupported command, unreadable/missing entry, or declared command times out after 120s; each prints the applicable `could-not-evaluate:` reason) · `64` usage … |
296:| round-71 exit-2 legs | Self-test covers missing entry and timeout with hermetic fixtures (timeout injected as 1s in self-test); the live CLI returns exit 2 with `could-not-evaluate: entry not found:` or `could-not-evaluate: command timed out after 120s:` and no traceback. Counter labels: `C2_MISSING_ENTRY_EXIT2`, `C2_TIMEOUT_EXIT2`; round-71 claims/counter in `reports/round-71/`. |
```

### 3.5 Adjacent exit-2 / exit-1 classification probes (verdict map not collapsed)

```
$ python3 -B corpus/check_embedded_outputs.py --entry "$PWD/corpus/knowledge"      # a directory
could-not-evaluate: entry not found: …/corpus/knowledge
DIRENTRY_RC=2

$ python3 -B corpus/check_embedded_outputs.py --entry "$PWD/probe-unsupported.md"  # `$ python3 -B -c print(1)`
could-not-evaluate: no `$ cmd` blocks or unsupported command
UNSUPPORTED_RC=2

$ python3 -B corpus/check_embedded_outputs.py --entry "$PWD/corpus/knowledge/round-65-apk-axml-byte-evidence.md"
drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, "compressed_size": 69, …}
checked_blocks=15 problems=1
EMB_round-65 rc=1
```
Exit 2 is reserved for could-not-evaluate and real drift still exits 1 — the two classes are not merged, and no could-not-evaluate path prints a traceback.

## 4. Retained pin/drift hold

One retained drift hold and the pin holds, both unchanged from the frozen baseline:

```
$ for r in round-68 round-65 round-67 round-69; do python3 -B corpus/check_embedded_outputs.py --entry "$PWD/corpus/knowledge/$r-apk-axml-byte-evidence.md"; done
EMB_round-68 rc=0 :: checked_blocks=17 problems=0
EMB_round-65 rc=1 :: checked_blocks=15 problems=1
EMB_round-67 rc=0 :: checked_blocks=16 problems=0
EMB_round-69 rc=0 :: checked_blocks=17 problems=0

$ sha256sum corpus/knowledge/round-68-apk-axml-byte-evidence.md corpus/knowledge/round-65-apk-axml-byte-evidence.md corpus/derive_axml_anchors_r68.py
ef7f0232…0830798e  round-68-apk-axml-byte-evidence.md   (= R68_SHA)
cf42cc20…01c4d05a  round-65-apk-axml-byte-evidence.md   (= R65_SHA)
bce497d6…50d1f1e249  derive_axml_anchors_r68.py         (= S046_SHA)

$ # pin mutant: append "# tampered" to every pinned `use` path of the round-68 entry, then re-run the entry
$ cd pin && python3 -B corpus/check_embedded_outputs.py --entry "$PWD/corpus/knowledge/round-68-apk-axml-byte-evidence.md"
drift entry:128 pinned historical script digest mismatch: corpus/derive_axml_anchors_r68.py
checked_blocks=16 problems=1
PINMUT_RC=1
```
The pin mutant is killed with the attributed marker (`EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1` in §5). These pin legs ran on the candidate export; `corpus/derive_axml_anchors*.py` and `corpus/embedded_output_pins.json` are byte-identical at both measured commits (sha256 prefixes `74d4c0d9`, `bce497d6`, `34c400c4` at `4c1eeae` and at `a16e6cb`), so the result carries to the tip. The label histogram versus the frozen red-before moves **only** the intended cells:

```
$ diff <baseline labels> <tip labels>
6c6
< V6_ENTRY_PRESENT=no
---
> V6_ENTRY_PRESENT=yes
8,13c8,13
< C1_GATE=n/a
< C1_LINT=n/a
< C2_MISSING_ENTRY_EXIT2=0/1 rc=1 stderr_traceback=yes
< C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=yes
< C2_GATE_SELFTEST=0 named_legs=0
< HOLDS_C2_V1=no
---
> C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes
> C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
> C2_MISSING_ENTRY_EXIT2=1/1 rc=2 stderr_traceback=no
> C2_TIMEOUT_EXIT2=1/1 rc=2 stderr_traceback=no
> C2_GATE_SELFTEST=0 named_legs=1
> HOLDS_C2_V1=yes
```
`K_HELD_BACKED=8/14`, `C05_STATUS`, `EMB_R65=checked_blocks=15 problems=1 exit=1`, `EMB_R67/R68/R69`, the three byte pins, `SM1–SM6=0`, `SELF_MISMATCH=0 exit=0`, `SELF_CLEAN_FIXTURE=1`, `SELF_MUTANTS_KILLED=6/6`, `HOLD_REPLAY=10/10`, `GATE_SELFTEST=exit 0`, `F_COVERAGE=5/8 score=6.2`, `FRESH_ROWS=18/18`, `HOLDS_OK_V8=yes` are all unchanged — including the deliberately-retained red `EMB_R65` label, which is a held historical observation, not a regression introduced by round 71.

## 5. Frozen counter at the tip (independent corroboration)

`python3 -B reports/round-71/measure.py <tip-export>` with `HYAKU_SCRATCH` inside this seat's scratch:

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
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-shape evidence mismatch
HOLD_REPLAY=10/10
GATE_SELFTEST=exit 0
F_COVERAGE=5/8 score=6.2
FRESH_ROWS=18/18
HOLDS_OK_V8=yes
COUNTER_TIP_RC=0
```
The block above is the captured log verbatim. Running the same counter on the candidate archive `4c1eeae` produced an identical label set with `COUNTER_RC=0`; only the archived tree hash differed.

Counter exit 0 here reflects the prior-holds bundle (`HOLDS_OK_V8`), consistent with its registered contract: `HOLDS_C1_V6=no` is the mid-wave C1 target state with zero committed vote files, and C2 is `yes`.

## 6. What this seat did not do (scope)

- No source, counter, claims, amendments, SKILL, SCORECARD, LOG or vote file was created or modified. No commit, push, spawn, or `agent://all`. No route/config change. No package or tool install (nothing was needed).
- No C1 Q01–Q16 decision is expressed. `C1_W2_Q_VOTES=0/16` reflects that the four reviewer vote files are not yet committed; `K_HELD_BACKED=8/14` and `V6_ADMITTED_MARKED=no` reflect the frozen landing order (entry landed as `admission-status: candidate`, README C05 still uncovered), not a C2 failure.
- Scratch `/fast/scratch/hyaku/revenger-r71/R71W2GateReplay/` (exports, fixtures, counter logs) was deleted after this report was written.

## 7. Residual risks and limits (stated, not scored)

1. The self-test exercises the timeout leg at function level with a 1 s injected limit; the production 120 s path is covered only by the real-CLI leg (counter + §3.2). This is the registered design, so not a defect, but the self-test alone cannot catch a regression in the CLI timeout wiring.
2. A directory passed as `--entry` is reported as "entry not found" rather than a distinct "not readable/is a directory" reason. The registered text only names missing/unreadable entries, so this is within contract, but it means the reason string does not distinguish the two.
3. The timeout fixture lives in scratch and copies `corpus/`; if a future `corpus/` change made `check_embedded_outputs.py` depend on the lane's `.git` or on untracked files, this export-based leg could diverge from a live-lane run. The live-lane missing-entry call matched the export exactly (§3.1).
4. Vote-file and pin checks are structural (filename/stem, exact key sets, digest membership), not cryptographic identity; `HOLDS_C1_V6` remains a mechanical predicate, not an admission verdict. This seat's PASS does not substitute for the four fresh reviewer vote files.
5. Measurements are of the archived candidate/tip trees; the lane tip moved during the wave (`4c1eeae` → `c6e284c` → `a16e6cb`). Byte-identical instruments plus the moved-labels-only diff is the evidence that the result still applies to the tip; if the tip moves again before adjudication, L1 should re-run the counter at the final tip.

Report: `.ufo/waves/round-71/w2/R71W2GateReplay.md`
