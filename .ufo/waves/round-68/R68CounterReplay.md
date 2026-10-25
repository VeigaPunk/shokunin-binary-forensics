MATCH — the frozen counter replays on base f165908 with output byte-identical to reports/round-68/measure-before.log (98/98 lines, diff exit 0, both sha256 7dfe06d4dd9f2089f166eceb6e9546801281b86cb8377973f38df9e17f804034), counter exit 0, and all eight named labels agree.

# R68CounterReplay — frozen-counter replay on the red-before base tree

## 1. Instrument identity (pre-flight)

| Item | Observed | Expected (frozen) | Verdict |
|---|---|---|---|
| counter file | /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py | same | — |
| sha256 | `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766` | `0de4eb6f...93f7766` | MATCH |
| lines | 528 | — | — |

Command: `sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py`
Output: `0de4eb6f34bdb906fb69fdd173aaac9bcef629e6ff1d4c67f5ba8c91093f7766  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py`

The counter was NOT edited, NOT copied, NOT wrapped. It was executed in place from `/`, exactly as pre-registered.

## 2. Base-commit resolution

The brief's `refs/heads/main~2` was verified, not assumed:

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse refs/heads/main~2
f165908aaffcf14798de53405fe788986bd33ff9
$ git -C ... rev-parse f505526f7ecf4ac1ad51d99aa2d1dd5c57c0bae0^
f165908aaffcf14798de53405fe788986bd33ff9
```

`f505526f7ecf4ac1ad51d99aa2d1dd5c57c0bae0` = "round-68: pre-registration — claims.md (C1 C7 attribution repair, C2 C05 third pass with machine-derived anchors), frozen counter 0de4eb6f, red-before receipt on base f165908". Its sole parent is `f165908aaffcf14798de53405fe788986bd33ff9` = "round-67 verifier spot-check (integrator, hyaku): non-author admit/reject" — i.e. `main~2` IS the pre-registration's parent, so no fallback selection was needed. The build commit `4232235723cf8d4731a1e7e78ca098b8af953a57` sits on top and is correctly excluded from this red-before tree.

`refs/heads/main~2:corpus` tree id = `810ae2c1bd9c27b1318494555290a8deb9762145`.

## 3. Replay command (verbatim, as pre-registered)

```
rm -rf /tmp/r68-seat-replay && mkdir -p /tmp/r68-seat-replay
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive refs/heads/main~2 corpus \
  | tar -x -C /tmp/r68-seat-replay
mkdir -p /tmp/r68-seat-replay-tmp
cd / && TMPDIR=/tmp/r68-seat-replay-tmp \
  python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure.py /tmp/r68-seat-replay
```

Result: `ARCHIVE_OK`; tree = 502 files under `/tmp/r68-seat-replay/corpus` (+ knowledge, lessons, fixtures, live subdirs).
`EXIT=0`, wall 2.32 s. stderr: **empty (0 lines)**.

Note on scope of the archive: `git archive ... corpus` contains only `corpus/`, so the counter itself is deliberately read from the working tree at the absolute path (sha-pinned above). The measured surface is 100% the archived base tree; only the instrument comes from the checkout.

## 4. FULL counter output (98 lines, verbatim)

```
K_HELD=8/14 score=5.7
K_ROW C05 status=uncovered
K_ROW C07 status=held
K_HELD_BACKED=8/14
C05_REJECTED_MARKED=yes
K_HELD_BACKED_STRICT=8/14
C05_KNOWLEDGE_COLUMN=-
C05_SINGLE_V2=no
C05_SINGLE_V3=no
STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True
SAVED_RECORDS=59
ROW_OPS={'C03': ['inspect_managed_artifact'], 'C05': ['inspect_android_package'], 'C07': ['inspect_firmware_regions'], 'C08': ['capture_browser_scenario', 'inspect_web_page', 'observe_web_session']}
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
C05_STATUS=uncovered
HOLDS_C2_V3=no
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_firmware_regions': 1, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
C5_CONTROL_PRESENT_verify_icon_languages.py=yes
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted
C5_CONTROL_PRESENT_verify_multi_icon_states.py=yes
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c5 exit=1 killed :: AssertionError: r42: forged receipt evidence accepted
C5_CONTROL_PRESENT=2/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
C6_CONTROL_PRESENT_verify_icon_languages.py_exit=yes
MUTANT verify_icon_languages.py c6-control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c6-exit exit=1 killed :: AssertionError: r47: forged receipt exit accepted
C6_CONTROL_PRESENT_verify_icon_languages.py_fixture=yes
MUTANT verify_icon_languages.py c6-control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c6-fixture exit=1 killed :: AssertionError: r47: forged receipt fixture accepted
C6_CONTROL_PRESENT_verify_multi_icon_states.py_exit=yes
MUTANT verify_multi_icon_states.py c6-control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c6-exit exit=1 killed :: AssertionError: r42: forged receipt exit accepted
C6_CONTROL_PRESENT_verify_multi_icon_states.py_fixture=yes
MUTANT verify_multi_icon_states.py c6-control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c6-fixture exit=1 killed :: AssertionError: r42: forged receipt fixture accepted
C6_CONTROL_PRESENT=4/4
C6_CONTROLS_PASS=4/4
C6_RECEIPT_KILLED=4/4
C6_RECEIPT_KILLED_ATTRIBUTED=4/4
C7_GATE_PRESENT=yes
C7_SELFTEST=pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
MUTANT check_embedded_outputs.py control exit=0 pass :: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
MUTANT check_embedded_outputs.py c7 exit=1 killed :: self-test: drifted entry not caught
C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
C7_V2_CLEAN=yes exit=0 :: checked_blocks=16 problems=0
C7_V3_CLEAN=n/a (no v3 file)
C7_CONTROL_PASS=1/1
C7_MUTANT_KILLED=1/1
C7_MUTANT_KILLED_ATTRIBUTED=0/1
MUTANT check_embedded_outputs.py c7neg exit=1 killed :: self-test: drifted entry not caught
C7_NEG_SPOOF_KILLED=1/1
C7_NEG_SPOOF_KILLED_ATTRIBUTED=0/1
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=yes
HOLDS_OK_V4=yes
HOLDS_OK_V5=no
HOLDS_OK_V6=no
```

Exit code: **0**

## 5. Label-by-label check against measure-before.log

| Label | Replay value (line in replay output) | measure-before.log (line) | Verdict |
|---|---|---|---|
| C7_MUTANT_KILLED_ATTRIBUTED | `0/1` (l.77) | `0/1` (l.77) | MATCH |
| C7_NEG_SPOOF_KILLED | `1/1` (l.79) | `1/1` (l.79) | MATCH |
| C7_NEG_SPOOF_KILLED_ATTRIBUTED | `0/1` (l.80) | `0/1` (l.80) | MATCH |
| C7_V3_CLEAN | `n/a (no v3 file)` (l.74) | `n/a (no v3 file)` (l.74) | MATCH |
| K_HELD_BACKED | `8/14` (l.4) | `8/14` (l.4) | MATCH |
| C05_STATUS | `uncovered` (l.14) | `uncovered` (l.14) | MATCH |
| HOLDS_OK_V5 | `no` (l.97) | `no` (l.97) | MATCH |
| HOLDS_OK_V6 | `no` (l.98) | `no` (l.98) | MATCH |

No differing label. The red signal is reproduced exactly: the do-nothing control holds on this tree — C7 attribution is still `0/1` (marker shadowed dead code in the base gate, pre-repair), C05 is still `uncovered`, K_HELD_BACKED is still `8/14`, `C7_V3_CLEAN` is still `n/a`, and both V5/V6 holds are still `no` while exit stays 0 (V1 holds hold).

## 6. Whole-file equality, not just labels

```
$ sed -n '1,98p' /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-68/measure-before.log > /tmp/r68-before.98
   # line 99 of the log is the blank separator before its human header block ("# --- round-68 red-before receipt ...")
$ diff -u /tmp/r68-before.98 /tmp/r68-seat-replay.out
   DIFF_EXIT=0, 0 lines of diff
$ sha256sum /tmp/r68-before.98 /tmp/r68-seat-replay.out
7dfe06d4dd9f2089f166eceb6e9546801281b86cb8377973f38df9e17f804034  /tmp/r68-before.98
7dfe06d4dd9f2089f166eceb6e9546801281b86cb8377973f38df9e17f804034  /tmp/r68-seat-replay.out
```

All 98 captured counter lines are identical — including every MUTANT/HOLD sub-line, which means the individual verifier outputs the red-before receipt recorded are reproducible on the archived base tree, not just the summary labels.

## 7. Determinism run (second execution, same tree)

```
$ cd / && TMPDIR=/tmp/r68-seat-replay-tmp2 python3 -B .../measure.py /tmp/r68-seat-replay > run2
EXIT2=0
7dfe06d4dd9f2089f166eceb6e9546801281b86cb8377973f38df9e17f804034  /tmp/r68-seat-replay.run2
diff -q run / run2 -> RUN2_IDENTICAL
```

Same sha256 on a second run → the counter is deterministic on this tree (no clock, PID, hash-seed or dict-order leakage into the output).

## 8. Side-effect / hermeticity checks

- **Counter does not mutate the tree it measures.** After two runs, a fresh `git archive refs/heads/main~2 corpus` extracted to a pristine dir and compared recursively:
  `diff -r /tmp/r68-seat-pristine /tmp/r68-seat-replay` → exit 0, 0 diff lines.
- **Counter takes its tree from argv only and has no baked-in lane paths.**
  `grep -n -E "/home/|getcwd|os\.environ|sys\.argv|realpath|Path\(" measure.py` →
  `30:TREE = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else None` plus 8 `pathlib.Path(tmp)` scratch uses (ll.173, 224, 263, 307, 359, 411, 473). No `/home/`, no `getcwd`, no `os.environ` read: the run is driven by `argv[1]` and `TMPDIR`. (Verified, not inferred.)
- **Scratch isolation.** Both runs used fresh `TMPDIR` dirs under `/tmp`; nothing was written to the lane repo, `corpus/`, `reports/`, or the lane Git index.

## 9. Bounds compliance

- No file under `corpus/`, `reports/`, `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `.git`, or any sibling lane repo was modified; no `git`/`jj` mutation was run (only `git log`/`rev-parse`/`archive`, all read-only).
- No write to `/home/vgpnk/Projects/shokuknow`.
- This report is the only file I wrote (plus `/tmp` scratch and two `/tmp` capture files).
- No tool installs, no upgrades, no pacman/uv/npm activity → nothing to record under the tooling directive.

## 10. Risks / limits of this result

1. **It confirms reproducibility, not adequacy.** MATCH says the pre-registered instrument reproduces the red-before receipt on base `f165908`; it says nothing about whether V5/V6 will turn green after the C1/C2 build state lands. That gates on the other seats.
2. **The instrument is read from the working tree, not the archive.** If `reports/round-68/measure.py` were edited between pre-registration and now, the replay would silently measure with a different counter. I closed this by sha256-pinning before the run (`0de4eb6f…7766`, equal to the value written in the receipt header) — but the archive-only recipe alone does not protect against that.
3. **Two runs is determinism evidence, not proof.** It excludes common nondeterminism (dict ordering, PIDs, time), not every possible source.
4. **`measure-before.log` lines 1–98 are treated as the counter capture and 99+ as the human header.** Line 99 is blank and line 100 begins `# --- round-68 red-before receipt`, so the split is unambiguous; if a future receipt appends extra prose without a blank separator, a naive `diff` of the whole file would show false differences.

Environment: `linux 7.2.11-arch1-1` x64; python3 (system, `-B` no-bytecode); wall time 2.32 s / 2.39 s.
