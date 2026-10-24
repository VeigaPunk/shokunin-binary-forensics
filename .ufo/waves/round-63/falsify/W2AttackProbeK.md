# W2AttackProbeK — frozen K counter adversarial review

## Scope, axes, and result

Reviewer: `revenger-r63.W2AttackProbeK` (independent leaf critic). Primary axis: **calibration** (does the frozen counter distinguish real C1 backing from index-only changes?). Impacted claimed axis: **coverage K / C1**. Preserved observation axes: coverage F / C2, C3 calibration, and the printed freshness/replay/calibration holds. This is counterexample evidence, not an admission, quality-gate decision, or canonical round verdict.

**Result: counterexamples found.** A status-only README flip with the new entry absent prints `K_HELD_BACKED=7/14`, not the requested `6/14`. A genuinely nonexistent knowledge link with an existing `.md` prefix also prints `7/14`. The ordinary missing-file control is excluded correctly, and the unchanged candidate-present/partial tree stays `6/14`. The 15th row is visible in both printed denominators (`6/15`), but `HOLDS_OK=yes` and exit 0 remain: the frozen hold predicate does not enforce the denominator void condition.

## Committed inputs and execution

- Measured tip: `db55bd6488e24e956df5818ae34c2a043d7ddc12` (`round-63: C1 candidate entry ... README still partial pending falsify wave`), identified with read-only `git rev-parse HEAD` and `git show --no-patch --format=fuller`.
- Archive command: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar --output=/tmp/revenger-r63-W2AttackProbeK-gCWhYE/tip.tar db55bd6488e24e956df5818ae34c2a043d7ddc12 corpus reports/round-63/measure.py reports/round-63/claims.md reports/round-63/measure-before.log`.
- Archive extracted under `/tmp/revenger-r63-W2AttackProbeK-gCWhYE/baseline`. Cases are private copies of that archive. No counter edits; only the README mutations described below and omission of the candidate in the two (a) cases.
- Frozen `measure.py` SHA-256: `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908`.
- Frozen `claims.md` SHA-256: `aed53241c3e4445fab94e854e3185b235ab2ff45c921d6c95e6e60938c7d1e31`.
- Interpreter: `Python 3.14.8`. Capture metadata: `2026-10-24T03:01:42.901190+00:00`.
- All six full counter runs used `python3 -B`, cwd `/`, and a per-case TMPDIR under this scratch root. The first five independent runs ran concurrently. The final stronger missing-link case ran once afterward. Every stdout, stderr state, and exit code is preserved below.
- No target/fixture execution, REA producer invocation, model argument, additional runtime invocation, git/jj mutation, config edit, tool installation/update, or pacman transaction. The frozen counter's requested saved-input `--self-test` subprocesses were exercised.

## Probe outputs and findings

| Probe | Attacks | K_HELD | C06 | K_HELD_BACKED | HOLDS_OK | Exit |
|---|---|---|---|---|---|---|
| `a-status-only-no-entry` | C1 K / calibration | 7/14 | held | 7/14 | yes | 0 |
| `a2-candidate-linked-no-entry` | C1 K / calibration | 7/14 | held | 6/14 | yes | 0 |
| `b-entry-present-partial` | C1 K / calibration | 6/14 | partial | 6/14 | yes | 0 |
| `c-fifteenth-row` | C1 K / calibration | 6/15 | partial | 6/15 | yes | 0 |
| `d-nonexistent-knowledge` | C1 K / calibration | 7/14 | held | 6/14 | yes | 0 |
| `d2-nonexistent-link-existing-prefix` | C1 K / calibration | 7/14 | held | 7/14 | yes | 0 |

### F1 — C1 K: status-only flip is not bound to the new entry

The committed C06 row (`corpus/README.md:35`) points to the already-existing `knowledge/2026-10-12-rea-readiness-checklist.md` and labels it “archive-tool row only.” In case (a), the new `round-63-zip-central-directory-evidence.md` is absent and changing only `partial → held` produces `K_HELD=7/14 score=5.0`, `K_HELD_BACKED=7/14`, `HOLDS_OK=yes`, exit 0. Thus the requested status-flip-without-entry rejection is falsified on the actual inherited row. Contrasting case (a2) correctly yields `K_HELD_BACKED=6/14` when the README points at the absent candidate itself.

**Cause/evidence:** frozen `reports/round-63/measure.py:32-34` checks only existence of whichever knowledge paths its regex finds in the third cell. It does not bind C06 to the specified new entry. This is a claim-identity/calibration gap, not proof that the candidate's content fails Q01–Q13. The contract explicitly says this probe measures existence, never quality (`claims.md:38-41`).

**Smallest safe correction:** preserve the frozen probe and report this limitation. At the existing C1 admission decision, require the committed C06 cell to name the exact new candidate and require that exact file to exist, in addition to the already-required named fresh-seat Q01–Q13 decisions. A `7/14` result backed only by the old checklist must not be presented as the specified new admission. No second quality authority or weakening of Q01–Q13 is needed.

### F2 — C1 K / frozen denominator hold: counted but not enforced

Case (c) adds one ordinary frontier row C15. The counter prints `K_HELD=6/15 score=4.0` and `K_HELD_BACKED=6/15`: **yes, the printed counter notices the 15th row.** It still prints `HOLDS_OK=yes` and exits 0.

**Cause/evidence:** `measure.py:26-34` derives the denominator from matching rows, whereas `measure.py:179-183` includes no row-count or row-identity assertion. `claims.md:113-117` declares a changed denominator void. The script's docstring also says exit 0 means the probe ran and holds pass and instructs the caller to read printed values; it does not promise automated claim adjudication. Therefore this is an unautomated external-void check, not evidence that the script hides denominator drift.

**Smallest safe correction:** the existing final C1/void adjudication must check exactly the frozen C01–C14 row identities and denominator 14 rather than infer those conditions from `HOLDS_OK=yes`/exit 0. Reject an actual 15-row final tree under the existing contract; do not rewrite the frozen predicate or re-target the denominator.

### F3 — C1 K: nonexistent-link prefix is falsely backed

The ordinary missing path in case (d) is handled correctly: held count becomes `7/14`, backed count stays `6/14`. The stronger case (d2) uses the sole knowledge token `knowledge/2026-10-12-rea-readiness-checklist.md.not-a-real-entry`; that exact path does not exist. The frozen regex instead extracts `knowledge/2026-10-12-rea-readiness-checklist.md`, which exists. The full frozen counter consequently prints `K_HELD_BACKED=7/14`, `HOLDS_OK=yes`, exit 0.

**Cause/evidence:** the `knowledge/[\w.-]+\.md` expression at `measure.py:32-33` has no end-of-token boundary and accepts a prefix of a different nonexistent path. This is an actual backing-parser false positive, distinct from the deliberate absence of quality checking.

**Smallest safe correction:** for this round, the existing admission decision must resolve the exact complete C06 path and candidate identity; do not accept substring backing as existence proof. For a later, newly registered counter, extract complete delimited path tokens and test those exact paths, with both the ordinary missing-file and this existing-prefix control retained. Do not silently change this round's frozen command.

### C0 — C1 K: entry presence alone does not pre-admit

The unchanged committed corpus in case (b) has the candidate present but README C06 still partial. It prints `K_HELD=6/14 score=4.3`, `K_ROW C06 status=partial`, `K_HELD_BACKED=6/14`. This matches the frozen admission order (`claims.md:105-108`); it is not a premature final falsification of C1 while the required fresh review wave is pending.

### Other printed observations (not independent quality decisions)

All six full runs print `F_COVERAGE=5/8 score=6.2`, `C3_CONTROLS_PASS=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `FRESH_ROWS=18/18`, `HOLD_CALIBRATION=4/4`, and `HOLD_REPLAY=10/10`. C2 receipt-command and data-forgery controls/attributed kills are all `2/2`. The K-only perturbations do not change these outputs. This scoped seat did not adjudicate C2's real-run envelope/byte oracle, C3's patch preservation, or any C1 Q-pass; those are not established merely by these counts.

## New source rows reopened

Reopened committed `corpus/SOURCES.md:46-47` (S032, S033). S032's primary [APPNOTE.TXT](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT) opened successfully: version 6.3.10, revised Nov 01, 2022; reopened §4.3.12 and §4.3.16 field tables. S033's archive container, complete `truth.json`, and complete saved `artifact-inspection.json` were reopened from the committed archive; all three file digests were independently calculated:

```text
857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e  corpus/fixtures/archive-r2/fixture.zip
7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68  corpus/fixtures/archive-r2/truth.json
2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380  corpus/live/runs/20261012T164246Z/artifact-inspection.json
```

These equal the S033 row's recorded hashes. Reopening and hash agreement are not a Q01–Q13 pass decision.

## Durable per-case receipts

Scratch paths below identify the observed runs, not promised permanent artifacts. The exact mutations, input commit, counter hash, README hash, commands, and full outputs are retained here so the cases can be reconstructed from the commit after scratch cleanup. Tool installs/updates: **none**. Heavy scratch is removed after this report is written; no temporary artifact is needed as the sole evidence pointer.

### `a-status-only-no-entry`

(a) Omit the round-63 candidate file; change only the inherited C06 status from partial to held (retain its readiness-checklist path).

- Candidate file present: `false`.
- README SHA-256: `b4dcba0d6638048881530906068dcd93f46bf9e18422baada3f4af845ebe4603`.
- Command: `TMPDIR=/tmp/revenger-r63-W2AttackProbeK-gCWhYE/tmp-a-status-only-no-entry python3 -B /tmp/revenger-r63-W2AttackProbeK-gCWhYE/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeK-gCWhYE/a-status-only-no-entry`; cwd `/`.

```text
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=7/14
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
STDERR=(empty)
PROBE_EXIT=0
```

### `a2-candidate-linked-no-entry`

(a, contrasting control) Omit the round-63 candidate file; point C06 at that absent candidate and set held.

- Candidate file present: `false`.
- README SHA-256: `8fab4db845d25550c6c46e65259ce8d92f984f82d7a1e8da9e62fa9a2ec85686`.
- Command: `TMPDIR=/tmp/revenger-r63-W2AttackProbeK-gCWhYE/tmp-a2-candidate-linked-no-entry python3 -B /tmp/revenger-r63-W2AttackProbeK-gCWhYE/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeK-gCWhYE/a2-candidate-linked-no-entry`; cwd `/`.

```text
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=6/14
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
STDERR=(empty)
PROBE_EXIT=0
```

### `b-entry-present-partial`

(b) Unmodified committed corpus: candidate exists, C06 remains partial and still names the readiness checklist.

- Candidate file present: `true`.
- README SHA-256: `7ccd8d4484db710800a34a0b3718c8f73523e5c5666359e81e2f44ddbaca7ab6`.
- Command: `TMPDIR=/tmp/revenger-r63-W2AttackProbeK-gCWhYE/tmp-b-entry-present-partial python3 -B /tmp/revenger-r63-W2AttackProbeK-gCWhYE/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeK-gCWhYE/b-entry-present-partial`; cwd `/`.

```text
K_HELD=6/14 score=4.3
K_ROW C06 status=partial
K_HELD_BACKED=6/14
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
STDERR=(empty)
PROBE_EXIT=0
```

### `c-fifteenth-row`

(c) Append exactly `| C15 | counter-only denominator control | — | — | frontier |` after C14; no other README edit.

- Candidate file present: `true`.
- README SHA-256: `99a3711ac4743d006b324aea3586624d17ef25b70aad3cbe41ba2910dc1aeca6`.
- Command: `TMPDIR=/tmp/revenger-r63-W2AttackProbeK-gCWhYE/tmp-c-fifteenth-row python3 -B /tmp/revenger-r63-W2AttackProbeK-gCWhYE/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeK-gCWhYE/c-fifteenth-row`; cwd `/`.

```text
K_HELD=6/15 score=4.0
K_ROW C06 status=partial
K_HELD_BACKED=6/15
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
STDERR=(empty)
PROBE_EXIT=0
```

### `d-nonexistent-knowledge`

(d) Set C06 held and its sole knowledge path to `knowledge/round-63-counter-probe-nonexistent.md`, which does not exist.

- Candidate file present: `true`.
- README SHA-256: `c16e6cdc6ac75028fd0a9a7f85b985b7bbc0fe7b850ea77501565bed23dcad81`.
- Command: `TMPDIR=/tmp/revenger-r63-W2AttackProbeK-gCWhYE/tmp-d-nonexistent-knowledge python3 -B /tmp/revenger-r63-W2AttackProbeK-gCWhYE/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeK-gCWhYE/d-nonexistent-knowledge`; cwd `/`.

```text
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=6/14
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
STDERR=(empty)
PROBE_EXIT=0
```

### `d2-nonexistent-link-existing-prefix`

(d, stronger counterexample) Set C06 held and its sole knowledge path to `knowledge/2026-10-12-rea-readiness-checklist.md.not-a-real-entry`, which does not exist; its .md prefix does exist.

- Candidate file present: `true`.
- README SHA-256: `c9cec8757f098c43adf7f1454d58d76eef6d6cbe64297d9b1af7ba91491d40f7`.
- Command: `TMPDIR=/tmp/revenger-r63-W2AttackProbeK-gCWhYE/tmp-d2-nonexistent-link-existing-prefix python3 -B /tmp/revenger-r63-W2AttackProbeK-gCWhYE/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeK-gCWhYE/d2-nonexistent-link-existing-prefix`; cwd `/`.
- Exact full-link existence: `false`; frozen regex extraction: `['knowledge/2026-10-12-rea-readiness-checklist.md']`; extracted prefix exists.

```text
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=7/14
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
STDERR=(empty)
PROBE_EXIT=0
```
