NO-REGRESSION — all ten `verify_*.py` self-tests exit 0 and every round-67 counter label holds at its round-67 value; the only label movement is the round-68 claim's own pass-branch (C7_MUTANT_KILLED_ATTRIBUTED 0/1 → 1/1, HOLDS_OK_V5 no → yes) plus new round-68 labels, none of them worse.

seat: L1Revenger68.R68HoldSweep (leaf, read-only sweep) · date: 2026-10-25
lane: /home/vgpnk/Projects/shokunin/revenger-shokunin · measured ref: `refs/heads/main` = `4232235723cf8d4731a1e7e78ca098b8af953a57` (round-68 build commit; parent `f165908aaffcf14798de53405fe788986bd33ff9` = claim base)
counter: `reports/round-68/measure.py` sha256 `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` (re-hashed this seat, matches the pin in `claims.md` and `measure-before.log`)
scratch tree: `TREE=/tmp/revenger-r68-holdsweep-WKk9` — produced exactly per the frozen contract, `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive refs/heads/main corpus | tar -x -C "$TREE"`
edits: none (this file is the only write; no other repo path touched)

## 1. The ten `verify_*.py` self-tests (replay family) — per-script exit codes

Command actually run, from the scratch tree root (same `cwd` and same `--self-test` argv the counter uses at `reports/round-68/measure.py:496-497`):

```
cd /tmp/revenger-r68-holdsweep-WKk9 && for f in corpus/verify_*.py; do
  out=$(python3 -B "$f" --self-test 2>&1); rc=$?
  echo "EXIT=$rc  $f  :: $(printf '%s' "$out" | tail -1)"
done
```

| # | script | exit | last output line (trimmed) |
|---|--------|------|----------------------------|
| 1 | `corpus/verify_evm_evidence.py` | **0** | `NEGATIVE REJECTED candidate destination mismatch` |
| 2 | `corpus/verify_icon_languages.py` | **0** | `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` |
| 3 | `corpus/verify_icon_states.py` | **0** | `PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED` |
| 4 | `corpus/verify_js_graph_delta.py` | **0** | `NEGATIVE REJECTED saved graph disagrees with source truth` |
| 5 | `corpus/verify_multi_icon_states.py` | **0** | `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` |
| 6 | `corpus/verify_named_multi_icon_states.py` | **0** | `PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size).` |
| 7 | `corpus/verify_pe_resources.py` | **0** | `NEGATIVE REJECTED payload relation mismatch` |
| 8 | `corpus/verify_saved_evidence.py` | **0** | `NEGATIVE JS REJECTED: JS: wrong package-main mapping` |
| 9 | `corpus/verify_semantic_trace.py` | **0** | `NEGATIVE REJECTED relation differs from source parent` |
| 10 | `corpus/verify_shape_evidence.py` | **0** | `NEGATIVE REJECTED changed-property evidence mismatch` |

10/10 exit 0, in an independent invocation (not the counter's), matching the counter's own `HOLD <script> exit=0` lines one for one. The four named calibration scripts are `verify_icon_states.py`, `verify_multi_icon_states.py`, `verify_icon_languages.py`, `verify_named_multi_icon_states.py` (`measure.py:499-500`).

Non-vacuity note: six of the ten exit 0 on an explicit negative-control rejection line (`NEGATIVE REJECTED …`), and the four named ones exit 0 only after printing a `PASS` summary that counts the forged candidates they rejected — so no script reaches exit 0 on an empty/silent path. The four calibration scripts carry no `--self-test` argv branch (`verify_icon_languages.py:183`, `verify_icon_states.py:180`, `verify_multi_icon_states.py:183`, `verify_named_multi_icon_states.py:106` are bare `__main__`), so the flag is inert for them and exit 0 is their full built-in suite — the same behaviour the counter relies on.

## 2. Counter over the same tree

```
cd / && TMPDIR=/tmp/revenger-r68-counter-XXXX python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py \
  /tmp/revenger-r68-holdsweep-WKk9
```

**counter exit code: 0** (the V1 holds hold; `measure.py:528`).

### Labels requested by this seat, round-67 (`reports/round-67/measure-after.log`) vs round-68 (this run)

| label | round-67 | round-68 | status |
|---|---|---|---|
| `HOLD_CALIBRATION` | 4/4 | **4/4** | held |
| `HOLD_REPLAY` | 10/10 | **10/10** | held |
| `FRESH_ROWS` | 18/18 | **18/18** | held |
| `F_COVERAGE` | 5/8 score=6.2 | **5/8 score=6.2** | held |
| `README_TOKEN_LEGEND_MISMATCH` | 0 rows=[] | **0 rows=[]** | held |
| `STRICT_REJECT_WINDOW_SELFTEST` | pass, old_window_miss=True | **pass, old_window_miss=True** | held |
| `C2_RECEIPT_B_KILLED_ATTRIBUTED` | 2/2 | **2/2** | held |
| `C3_RECEIPT_KILLED_ATTRIBUTED` | 2/2 | **2/2** | held |
| `C4_RECEIPT_KILLED_ATTRIBUTED` | 2/2 | **2/2** | held |
| `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED` | 2/2 | **2/2** | held |
| `C6_RECEIPT_KILLED_ATTRIBUTED` | 4/4 | **4/4** | held |
| `HOLDS_OK` | yes | **yes** | held |
| `HOLDS_OK_V2` | yes | **yes** | held |
| `HOLDS_OK_V3` | yes | **yes** | held |
| `HOLDS_OK_V4` | yes | **yes** | held |
| `HOLDS_OK_V5` | no | **yes** | improved (C1 pass branch) |
| `HOLDS_OK_V6` | (label absent) | **yes** | new label, yes |

Supporting controls read identically to round 67 and are the reason the attributed counts are not empty: `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`, `C2_D2_KILLED=2/2`, `C3_CONTROLS_PASS=2/2`, `C4_CONTROLS_PASS=2/2`, `C5_CONTROL_PRESENT=2/2`, `C5_CONTROLS_PASS=2/2`, `C5_RECEIPT_KILLED=2/2`, `C6_CONTROL_PRESENT=4/4`, `C6_CONTROLS_PASS=4/4`, `C6_RECEIPT_KILLED=4/4`.

### Full-label diff against the round-67 after-receipt

`grep -vE '^MUTANT |^#|^$'` on both logs, sorted, `diff` — the *entire* delta is:

```
4a5,6
> C05_SINGLE_V3=no
> C05_STATUS=uncovered
30c32,34
< C7_MUTANT_KILLED_ATTRIBUTED=0/1
> C7_MUTANT_KILLED_ATTRIBUTED=1/1
> C7_NEG_SPOOF_KILLED=1/1
> C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
33a38
> C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
38a44
> HOLDS_C2_V3=no
43c49,50
< HOLDS_OK_V5=no
> HOLDS_OK_V5=yes
> HOLDS_OK_V6=yes
```

Every line above is either a label newly introduced by the frozen round-68 counter (`claims.md` §Frozen counter: `C7_NEG_SPOOF_KILLED`, `C7_NEG_SPOOF_KILLED_ATTRIBUTED`, `C7_V3_CLEAN`, `C05_SINGLE_V3`, `C05_STATUS`, `HOLDS_C2_V3`, `HOLDS_OK_V6`) or the C1 pass-branch improvement. **No round-66/round-67 label moved down.**

## 3. C7 attribution — direct spot-check of the repaired surface

```
C7_GATE_PRESENT=yes
C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
MUTANT check_embedded_outputs.py c7 exit=1 killed :: drifted entry output accepted
C7_CONTROL_PASS=1/1
C7_MUTANT_KILLED=1/1
C7_MUTANT_KILLED_ATTRIBUTED=1/1
MUTANT check_embedded_outputs.py c7neg exit=1 killed :: drifted entry output accepted (spoofed)
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
C7_V2_CLEAN=yes exit=0 :: checked_blocks=16 problems=0
C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0
```

The attributed marker is now reachable and is the last line of the failing run: `corpus/check_embedded_outputs.py:143-144` prints `self-test: drifted entry not caught` then `MARKER` (= `drifted entry output accepted`, `:36`) last. The negative control proves the attribution rule is not "any non-zero exit": the spoofed marker text is killed (exit 1) yet reads `C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1`. This is the round-67 `0/1` → round-68 `1/1` movement claimed by C1, and it is the only calibration movement.

## 4. Frozen-surface checks run alongside the sweep (no writes)

- **Replay family byte-stability** (`f165908` vs `4232235`, per-file sha256 over `corpus/verify_*.py`): all 10 `IDENTICAL`; `file_count=10`. Examples: `verify_icon_languages.py 2bf9b5feac9e407410b95d15ce898976bfd8d5f4b137f83f6417d2a6e623c0cd`, `verify_multi_icon_states.py 09c507744c1fd2eb9d4479721314f4e3ce2299dd621992d4fecfb26a11c44cd1`. The replay set did not move, so `HOLD_REPLAY=10/10` is measured on the same ten files round-67 measured.
- **`corpus/live` + `corpus/fixtures` byte-stability** (`claims.md` §Void conditions: changed bytes there void the round): extracted both commits and `diff -r` → `LIVE_IDENTICAL`, `FIXTURES_IDENTICAL`; combined content manifest sha256 `69f9bd28e782d552c868c5d76ae2908e49d2d35cceb8af99d9cb00ea3710d940` on both sides. A raw `git archive | sha256sum` over those paths *does* differ between the two commits (tar carries commit-time mtimes) — that is archive metadata, not content; the content manifest above is the correct instrument.
- **README not flipped**: `git diff f165908 4232235 -- corpus/README.md` is empty, and the C05 row at `corpus/README.md:34` reads identically at both commits (`… uncovered |`). Consistent with `admission-status: candidate` in `corpus/knowledge/round-68-apk-axml-byte-evidence.md` and with `C05_STATUS=uncovered` / `C05_SINGLE_V3=no` / `HOLDS_C2_V3=no` in the counter — the expected pre-adjudication build state, not a regression.
- **Counter determinism**: second full run with a different `TMPDIR` produced byte-identical stdout, exit 0 (`diff` empty → `COUNTER_DETERMINISTIC_IDENTICAL`).
- **Lane worktree**: `git status --porcelain` shows only two untracked wave files (`.ufo/waves/round-68/build-wave-spec.py`, `wave-spec.json`); `corpus/` is clean at `4232235`, so the archived tree equals the committed tree.

## Verdict

**NO-REGRESSION.** Every requested label sits at its round-67 value: `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `FRESH_ROWS=18/18`, `F_COVERAGE=5/8 score=6.2`, `README_TOKEN_LEGEND_MISMATCH=0 rows=[]`, `STRICT_REJECT_WINDOW_SELFTEST=pass`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`, `C6_RECEIPT_KILLED_ATTRIBUTED=4/4`, `HOLDS_OK=yes`, `HOLDS_OK_V2=yes`, `HOLDS_OK_V3=yes`, `HOLDS_OK_V4=yes`. The single movers — `C7_MUTANT_KILLED_ATTRIBUTED` 0/1 → 1/1 and `HOLDS_OK_V5` no → yes — are the C1 pass branch, and `HOLDS_OK_V6=yes` is a new label; none of them is a regression, and no calibration control that passed in round 67 now fails. Counter exit code 0.

## Risks / open items (for the adjudicating L1, not defects this seat may touch)

1. `C7_V3_CLEAN=yes exit=0 :: checked_blocks=17 problems=0` is true *at build state*, but `C05_SINGLE_V3=no` / `HOLDS_C2_V3=no` mean the counter does not yet bind the v3 entry to the README row — C2's pass branch is still gated on the wave's Q01–Q13 decisions, as `claims.md` intends. Nothing in this sweep should be read as C2 evidence.
2. `HOLD_REPLAY` counts only exit codes; six of the ten scripts earn exit 0 through their own negative control, so the label is meaningful but does not by itself prove positive-path coverage. The per-script last-lines in §1 are the stronger receipt.
3. The `git archive | sha256sum` mtime artefact in §4 is a trap for any later seat comparing frozen-byte claims by raw archive hash; use per-file content manifests.

## Tooling

No installs, no upgrades, no pacman transactions (host-wide pause respected). Tools used: `git archive`, `tar`, `sha256sum`, `diff`, `python3` (system interpreter, `-B`) — all already present.

## Machine-readable summary

```
REF=4232235723cf8d4731a1e7e78ca098b8af953a57
COUNTER_SHA256=0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766
VERIFY_EXITS=evm:0,icon_languages:0,icon_states:0,js_graph_delta:0,multi_icon_states:0,named_multi_icon_states:0,pe_resources:0,saved_evidence:0,semantic_trace:0,shape_evidence:0
VERIFY_PASS=10/10
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
FRESH_ROWS=18/18
F_COVERAGE=5/8 score=6.2
README_TOKEN_LEGEND_MISMATCH=0
STRICT_REJECT_WINDOW_SELFTEST=pass
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
C6_RECEIPT_KILLED_ATTRIBUTED=4/4
C7_MUTANT_KILLED_ATTRIBUTED=1/1 (r67: 0/1)
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLDS_OK=yes HOLDS_OK_V2=yes HOLDS_OK_V3=yes HOLDS_OK_V4=yes HOLDS_OK_V5=yes HOLDS_OK_V6=yes
COUNTER_EXIT=0
LIVE_FIXTURES_MANIFEST_SHA256=69f9bd28e782d552c868c5d76ae2908e49d2d35cceb8af99d9cb00ea3710d940 (identical at f165908 and 4232235)
VERDICT=NO-REGRESSION
```
