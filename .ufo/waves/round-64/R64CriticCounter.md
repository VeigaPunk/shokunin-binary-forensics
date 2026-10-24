# R64CriticCounter — counter attack evidence

## Scope and axes

Axes: **coverage K / admission identity**, **calibration / causal attribution**, and **evidence provenance / legend consistency**. Operability and frozen replay/calibration holds were checked only as part of the expressly assigned scratch attacks.

This is an independent critic's reproduction, not a round verdict, admission, or assessment of the executors' final patches. Corpus inputs came from the immutable claim-base archive `666ea84b6be2eec2b0359f556ba2429fc9044c36`, not the concurrently changing working tree. Frozen counter: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py`, SHA-256 `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168`.

## Results

Four scratch counter invocations were executed concurrently, each with `python3 -B`, cwd `/`, and TMPDIR `/tmp/revenger-r64-counter-YU8AXi`. Inputs were the base archive plus only the modifications specified below.

| Scratch suffix | K backed / strict | Legend mismatch | C4 controls / attributed | Calibration / replay holds | HOLDS_OK / V2 | Exit |
|---|---|---|---|---|---|---|
| `-decoy` | 8/14 / 8/14 | 0 | 2/2 / 0/2 | 4/4 / 10/10 | yes / no | 0 |
| `-always` | 7/14 / 7/14 | 1 | 0/2 / 2/2 | 2/4 / 8/10 | no / no | 1 |
| `-forged` | 7/14 / 7/14 | 2 | 2/2 / 0/2 | 4/4 / 10/10 | yes / no | 0 |
| `-combined` | 8/14 / 8/14 | 0 | 2/2 / 2/2 | 4/4 / 10/10 | yes / yes | 0 |

All four retained F coverage 5/8 and freshness rows 18/18. The combined tree retained C2 command-attributed kills 2/2, C2 d2 kills 2/2, and C3 attributed kills 2/2. The named round-64 firmware knowledge entry was absent from the combined tree.

## 1. Decoy knowledge citation survives both K counters

**Counterexample.** In the base corpus README, replace only C07 with:

```text
| C07 | firmware images | `knowledge/decoy.md` | — | held |
```

Create `/tmp/revenger-r64-counter-YU8AXi-decoy/corpus/knowledge/decoy.md` containing exactly:

```text
Decoy only. No firmware facts, byte readout, source, or independent admission.
```

**Observed evidence:** `K_HELD=8/14 score=5.7`, `K_ROW C07 status=held`, `K_HELD_BACKED=8/14`, `K_HELD_BACKED_STRICT=8/14`, and `README_TOKEN_LEGEND_MISMATCH=0 rows=[]`. The probe exited 0 although C4 remained 0/2 and `HOLDS_OK_V2=no`.

**Mechanism:** counter lines 33–35 check filename existence; lines 37–49 additionally exclude one literal rejected marker in the first 2,000 characters. Neither checks entry identity, actual firmware content, or independent admission. The decoy has no rejected marker, so “strict” adds no protection against an unreviewed decoy.

**Impacted axes:** coverage and calibration if numeric backing is presented as admitted knowledge. This is a deliberately limited existence counter, not by itself a defect in the frozen C1 process: claims lines 51–55 explicitly require separate Q01–Q13 reviewers and say the probe never measures quality.

**Smallest safe correction:** keep the frozen probe unchanged; require the independent gate decisions to bind the exact named entry and delivered revision before C07 changes to held. Do not interpret either K label, or exit 0, as admission. A future registered counter could constrain the expected C07 entry identity, but another self-authored status field would not establish independent admission.

## 2. Suffix spoofing: naive attack is caught by holds; relocated clause defeats all printed targets

### 2a. Always-failing unrelated assertion

In each archived verifier, append after its existing main invocation:

```python
assert False, 'unrelated: forged receipt stdout accepted'
```

**Observed evidence:** both C4 mutant lines ended with `AssertionError: unrelated: forged receipt stdout accepted`; the label printed `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`. However, `C4_CONTROLS_PASS=0/2`, `HOLD_CALIBRATION=2/4`, `HOLD_REPLAY=8/10`, `HOLDS_OK=no`, `HOLDS_OK_V2=no`, exit 1.

**Conclusion for this cheat:** the exact `endswith` test does not distinguish an unrelated assertion using the same suffix. The always-failing cheat survives the isolated attribution label but **does not survive the full controls/hold conditions**. This is not evidence of whole-round acceptance.

### 2b. Stronger combined counterexample: move the matched clause outside receipt_ok

Starting from the base archive in both scripts, delete the original ` and receipt['stdout_sha256']==H(raw_bytes)` conjunct from `receipt_ok`. Preserve all other original code and assertions. Append:

```python
def unrelated_assertion():
    receipt={'stdout_sha256': 'not-a-digest'}
    raw_bytes=b'unrelated'
    assert not (True and receipt['stdout_sha256']==H(raw_bytes)), 'unrelated: forged receipt stdout accepted'

unrelated_assertion()
```

Also apply the decoy README/file change from attack 1. Do **not** add the round-64 forged-stdout receipt controls.

The unrelated assertion succeeds in the control because a non-digest string differs from the hash. The global C4 regex finds its sole occurrence here, outside `receipt_ok`. Deleting the conjunct leaves `assert not (True)`, which always fails with the accepted suffix. No actual receipt participates in that failure.

**Observed counter evidence:**

```text
K_HELD=8/14 score=5.7
K_ROW C07 status=held
K_HELD_BACKED=8/14
K_HELD_BACKED_STRICT=8/14
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C2_D2_KILLED=2/2
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: unrelated: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: unrelated: forged receipt stdout accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=yes
```

Counter exit: **0**. Separate direct calls using the actual archived r47 and r42 receipts, with only `stdout_sha256` replaced by `H(b'')`, produced:

```text
verify_icon_languages.py FORGED_STDOUT_ACCEPTED=True; ACTUAL_DIGEST_DIFFERS=True
verify_multi_icon_states.py FORGED_STDOUT_ACCEPTED=True; ACTUAL_DIGEST_DIFFERS=True
BASE_ARCHIVE_ENTRY_ABSENT=True
```

**Mechanism:** `C4_CLAUSE` / `mutate_c4` at lines 212–223 use an unrestricted whole-file regex. Claims lines 65–68 require deleting the conjunct **inside receipt_ok**. The counter does not enforce that location. Lines 241–247 then attribute solely from return code and suffix. This is a concrete structural counter defect, beyond the naive suffix-only attack.

**Impacted axes:** calibration and coverage. All printed round targets and both hold summaries can be obtained without either claimed deliverable, while actual receipt validation is weakened.

**Smallest safe correction:** for this frozen round, independently review the delivered diff against the frozen shape: the original conjunct remains inside `receipt_ok`, every original assertion remains, and the new control actually deep-copies the receipt, changes only its stdout digest, and calls `receipt_ok`. The independent C1 gate must reject the decoy identity/content substitution. For a future registered counter, restrict mutation to the AST range of `receipt_ok` and fail not-evaluable if its exact conjunct is absent there. That minimal structural check defeats this reproduction. Do not patch or reinterpret the frozen round-64 counter after measurement.

These intentionally off-contract scratch edits demonstrate the counter's limits; they do not establish that the executors' real patches contain this defect or authorize trading away receipt validation for a better metric.

## 3. Forged operation-only JSON is counted as a saved record

**Counterexample.** Add only:

`/tmp/revenger-r64-counter-YU8AXi-forged/corpus/live/runs/round-64/forged-record.json`

```json
{"operation":"inspect_managed_artifact"}
```

No Evidence ID, result, subject, receipt, or actual managed inspection exists in this added file.

**Observed evidence:** `SAVED_RECORDS=60` (base receipt: 59), `README_TOKEN_LEGEND_MISMATCH=2 rows=['C03', 'C07']` (base: C07 only), F remained 5/8, exit 0, `HOLDS_OK_V2=no`.

**Mechanism:** lines 63–70 accept any JSON object with a truthy operation. That is weaker than even the presence-only F classifier at lines 82–88, which requires an Evidence ID and non-null normalized result. The legend diagnostic can therefore attribute “saved record” presence to authored junk.

**Impacted axes:** provenance and calibration if this diagnostic is described as proof of an actual operation. It is not a route/execution/provenance check.

**Closed boundary:** adding forged records alone cannot turn a genuine legend mismatch into zero. `record_ops` is an add-only union; extra operations can only retain or add mismatched frontier rows. The executed add-only cheat increased the mismatch and failed the zero target. Removing the genuine historical C07 record would cross the frozen-byte void condition and was not performed.

**Smallest safe correction:** retain the frozen presence semantics, disclose that this label scans operation-tagged JSON, and require independent provenance/byte-preservation evidence before calling the result a genuine saved inspection. Future registered tightening must not confuse adding a few forgeable JSON fields with authenticating provenance.

## Reproduction and boundaries

The archived baseline was created with this non-mutating Git operation:

```sh
mkdir -p /tmp/revenger-r64-counter-repro
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 666ea84b6be2eec2b0359f556ba2429fc9044c36 corpus | tar -xf - -C /tmp/revenger-r64-counter-repro
```

Make four separate copies of that baseline; apply only each case's exact edits above. For each case, run the frozen counter with cwd `/`, using an absolute tree path, for example:

```sh
TMPDIR=/tmp/revenger-r64-counter-repro python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py /tmp/revenger-r64-counter-repro-combined
```

The direct-call evidence was obtained by loading each combined script using `runpy.run_path` (not as `__main__`), reading its actual producer receipt and raw JSON for the first EXPECTED round (47 / 42), assigning `receipt['stdout_sha256']=H(b'')`, then calling its exported `receipt_ok(receipt, receipt['command'], EXPECTED[r][0], EXPECTED[r][1], raw_bytes)`.

No production corpus, frozen contract/counter, wave registry/spec, index, commit, push, sibling lane, or fleet file was changed. Only this report was written in the lane. No tools installed or updated. All attack scratch directories were removed after their evidence was captured; the snippets, base revision, counter fingerprint, commands, and observed outputs above are the durable reproduction record.

Report: .ufo/waves/round-64/R64CriticCounter.md
