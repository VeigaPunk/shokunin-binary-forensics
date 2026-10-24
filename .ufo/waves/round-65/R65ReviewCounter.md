PASS — `reports/round-65/measure.py` matches the frozen contract (all 21 round-64 labels byte-identical, exactly the 6 declared additive labels, `HOLDS_OK_V3` = V2 ∧ C5 2/2 ∧ selftest, one `mutate_c5` match per script, whole-file rejected scan, red-before reproducible byte-for-byte); C1's after-state is NOT yet reachable at HEAD — the current committed tree prints `K_HELD=8/14`, `K_ROW C05 status=frontier`, and only the L1 README flip moves it to the frozen 9/14/held (verified by scratch simulation).

# Seat

`R65ReviewCounter` — independent review of the frozen counter for revenger round 65 (hyaku).
Read-only. No installs/upgrades were needed or performed (no tool, version, channel, or reason to record).

# Frozen inputs reviewed (working tree == HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0`, `git status --porcelain` empty)

| file | sha256 |
|---|---|
| `reports/round-65/measure.py` | `8a2c69c4b0e9a799592c90f0e974ffee05556db5667d7b90ada58f92cf590304` |
| `reports/round-65/claims.md` | `b0b28105af0d284c262e7270b422cc2d408840f642b02322cbb59e5929b9cb47` |
| `reports/round-65/measure-before.log` | `a91fc56385e8e0b26915d9da532b344237b0f83bcda2feba092c79f67887121f` |
| `reports/round-65/measure-after.log` | `b3736823bbdf124174a1eb7cc02576035f8c94fa8a45fc84a89b1df2ddcc6718` |

Freeze integrity: `git log -- reports/round-65/measure.py` returns exactly one commit —
`5a2e7a0 2026-10-24 01:56:40 -0300 round-65: pre-registration — claims.md, frozen counter, red-before receipt`.
The probe was never edited after pre-registration (all later round-65 commits `c7b7cf9`, `6f1761a`, `5b4d29e`, `8214e4d` leave it untouched), so no rule was changed after any seat scored. The round-64 probe is likewise untouched (single commit `3bb430f`; `git show HEAD:reports/round-64/measure.py | sha256sum` = `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168` = on-disk).

# 1. Round-64 labels/formulas unchanged; new labels additive

Scripted comparison of every `print(f"<LABEL>` line, round-64 probe vs round-65 probe:

```
r64 labels: 21 r65 labels: 27
MISSING in r65: []
CHANGED text: []
ADDED: ['C5_CONTROLS_PASS', 'C5_CONTROL_PRESENT', 'C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED',
        'C5_RECEIPT_KILLED', 'HOLDS_OK_V3', 'STRICT_REJECT_WINDOW_SELFTEST']
```

Added set is exactly the frozen new-label list in `claims.md:70-72` plus the per-script
`C5_CONTROL_PRESENT_<script>` lines (same label family) and the `K_ROW C05` row
(`measure.py:33` extends the tuple to `("C05","C07")`; the `K_ROW` print itself is unchanged and
`K_ROW C07` still prints `held`). `diff -u round-64/measure.py round-65/measure.py` shows only:
docstring/comment text, tempdir prefixes `rev-r64-*`→`rev-r65-*`, the `K_ROW` tuple, the
`rejected_marked` window, the `STRICT_REJECT_WINDOW_SELFTEST` insert, the C5 block insert, and the
two `HOLDS_OK_V3` lines. All round-64 formulas (`holds_ok`, `holds_ok_v2`, C2/C3/C4 mutants and
attributions, `F_COVERAGE`, `FRESH_ROWS`, `README_TOKEN_LEGEND_MISMATCH`) are textually unchanged.

# 2. HOLDS_OK_V3 formula

`measure.py:330-331`:

```python
holds_ok_v3 = holds_ok_v2 and c5_attributed == 2 and selftest
print(f"HOLDS_OK_V3={'yes' if holds_ok_v3 else 'no'}")
```

Exactly `V2 ∧ C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED==2 ∧ STRICT_REJECT_WINDOW_SELFTEST=pass` as
frozen in `claims.md:64-66`. `holds_ok_v2` (unchanged) still requires `len(mismatch)==0` and
`fresh==18`. Exit code is still `sys.exit(2 if not evaluable else 0 if holds_ok else 1)` — i.e.
tied to V1, not V3 (see F3).

# 3. mutate_c5 — exactly one match per script, exact conjunct deletion

Regex `receipt\['evidence_id'\]\s*==\s*evidence_id` (`measure.py:261`):
`grep -o … | wc -l` = **1** in `corpus/verify_icon_languages.py` and **1** in
`corpus/verify_multi_icon_states.py`. The probe itself refuses to score a non-unique clause:
`if len(hits) != 1: return None` and the caller sets `evaluable = False` → exit 2
(`measure.py:266-272`, `293-297`).

Applying the same function offline to each committed script deletes exactly the conjunct and its
connecting `and`, nothing else, and leaves compilable Python:

```
--- verify_icon_languages.py: hits=1 mutated=True len 10531->10479
-    return (receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and
-            receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes))
+    return (receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and receipt['stdout_sha256']==H(raw_bytes))
compiles: yes
--- verify_multi_icon_states.py: hits=1 mutated=True len 10693->10641
(same single-conjunct deletion)
compiles: yes
```

`receipt_ok` bodies are identical in both scripts and each contains the conjunct once
(`verify_icon_languages.py:119-120`, `verify_multi_icon_states.py:122-123`).

Transplant controls are exactly as frozen and use **real foreign** IDs, cross-site:

- `corpus/verify_icon_languages.py:155-157` transplants
  `ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d` (present in
  `corpus/live/runs/round-42/producer-receipt.json`) and asserts
  `not receipt_ok(forged_evidence, …)` with message `f'r{r}: forged receipt evidence accepted'`.
- `corpus/verify_multi_icon_states.py:154-156` transplants
  `ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421` (present in
  `corpus/live/runs/round-47/producer-receipt.json`).
- Deep-copy of the genuine receipt differing only in `evidence_id` ⇒ the removed conjunct is the
  only possible rejection cause; the marker string occurs exactly once per script
  (`grep -c` = 1 / 1), so no cross-attribution from the pre-existing forged-command/stdout controls.

# 4. Rejected-marker scan reads whole files; window self-test

`measure.py:43-49` reads the entire file (`p.read_text(...)`, no slice). The only `[:2000]` in the
probe (`measure.py:57`) is the deliberate old-window demonstration:

```python
seeded = b"A" * 3000 + b"admission-status: rejected"
old_window_miss = b"admission-status: rejected" not in seeded[:2000]
new_window_hit  = b"admission-status: rejected" in seeded
selftest = old_window_miss and new_window_hit
```

Window independence at the committed tree: the two retained rejected candidates mark at byte
**712** (`evm-saved-interface-candidates.md`, 13249 B) and **859**
(`commonjs-destructured-require-edges.md`, 13371 B), both < 2000. Direct computation of old vs new
definition over the same archive tree: `STRICT old[:2000]=9 new[whole]=9` on the post-flip scratch
tree (both `8` on the unflipped tree, printed as `K_HELD_BACKED_STRICT=8/14`). So the repair changes
no current count, as the claims require.

# 5. Red-before reproduced byte-for-byte

```
git archive 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f corpus | tar -x -C $S/tree
cd / && TMPDIR=$S/tmp python3 -B reports/round-65/measure.py $S/tree
EXIT=0
diff -u reports/round-65/measure-before.log $S/out.log  →  IDENTICAL
```

Key lines: `K_HELD=8/14`, `K_ROW C05 status=frontier`, `K_HELD_BACKED=8/14`,
`K_HELD_BACKED_STRICT=8/14`, `STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True`,
`C5_CONTROL_PRESENT=0/2`, `C5_CONTROLS_PASS=2/2`, `C5_RECEIPT_KILLED=0/2`,
`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2`, `HOLDS_OK=yes`, `HOLDS_OK_V2=yes`, `HOLDS_OK_V3=no`,
exit 0. The do-nothing control is genuine and reproducible.

# 6. Counter on the CURRENT committed tree (HEAD `8214e4d`, scratch archive)

Command: `git archive 8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0 corpus | tar -x -C $B/tree`, then
from `/`: `TMPDIR=$B/tmp python3 -B /…/reports/round-65/measure.py $B/tree` → **EXIT=0**.
Every label line, verbatim:

```
K_HELD=8/14 score=5.7
K_ROW C05 status=frontier
K_ROW C07 status=held
K_HELD_BACKED=8/14
K_HELD_BACKED_STRICT=8/14
STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True
SAVED_RECORDS=59
ROW_OPS={'C03': ['inspect_managed_artifact'], 'C05': ['inspect_android_package'], 'C07': ['inspect_firmware_regions'], 'C08': ['capture_browser_scenario', 'inspect_web_page', 'observe_web_session']}
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
{'analyze_javascript_application': 6, 'compare_application_versions': 1, 'compare_javascript_export_shapes': 3, 'extract_artifact': 2, 'inspect_analysis_view': 1, 'inspect_artifact': 4, 'inspect_evm_interface': 7, 'inspect_firmware_regions': 1, 'inspect_pe_resources': 30, 'trace_application_feature': 2, 'trace_javascript_semantics': 2}
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, … forged selection REJECTED
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_icon_languages.py d2 exit=1 killed :: AssertionError: r47: receipt
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, …
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
MUTANT verify_multi_icon_states.py d2 exit=1 killed :: AssertionError: r42: receipt
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; …
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, …
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py control exit=0 pass :: …
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py control exit=0 pass :: …
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
C5_CONTROL_PRESENT_verify_icon_languages.py=yes
MUTANT verify_icon_languages.py control exit=0 pass :: …
MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted
C5_CONTROL_PRESENT_verify_multi_icon_states.py=yes
MUTANT verify_multi_icon_states.py control exit=0 pass :: …
MUTANT verify_multi_icon_states.py c5 exit=1 killed :: AssertionError: r42: forged receipt evidence accepted
C5_CONTROL_PRESENT=2/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, …
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, …
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, …
HOLD verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; …
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=yes
```

The committed `reports/round-65/measure-after.log` is byte-identical to this run
(`diff -u` → no output); `git diff --stat 6f1761a 8214e4d -- corpus` shows only
`corpus/lessons/round-65-verifier-spotcheck.md | 76 +++++`, so the receipt is an honest measurement
of a corpus-identical tree.

**The C1 after-state is not present:** the frozen target is `K_HELD 8/14 → 9/14` with
`K_ROW C05 status=held` (`claims.md:24-31`); HEAD prints `8/14` / `frontier`. Every other after
label (`C5_*` 2/2, `HOLDS_OK_V3=yes`, exit 0) is already green.

# 7. Sensitivity check — the counter does reach the frozen after-state on the prescribed flip

Read-only simulation in the scratch copy only (never the lane): flip the single README row to
`` | C05 | Android packages (APK) | `knowledge/round-65-apk-axml-byte-evidence.md` (…) | `fixtures/apk-r65`; `fixtures/apk-r65/readout.py` | held | ``, re-run the frozen probe:

```
K_HELD=9/14 score=6.4
K_ROW C05 status=held
K_ROW C07 status=held
K_HELD_BACKED=9/14
K_HELD_BACKED_STRICT=9/14
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
C5_CONTROL_PRESENT=2/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=yes
EXIT=0
```

This is exactly the frozen after-state named in the seat brief; `K_HELD_BACKED` and
`K_HELD_BACKED_STRICT` stay equal (9/14) as the claims require, and `C05` remains absent from
`README_TOKEN_LEGEND_MISMATCH` because no `inspect_android_package` saved record exists
(`SAVED_RECORDS=59`, operation census above). The counter is responsive and the flip is the only
missing move.

# Findings by severity

**F1 — HIGH (C1 admission gate; sequencing, not a counter defect).** At the current committed tip
`8214e4d` the frozen probe prints `K_HELD=8/14` and `K_ROW C05 status=frontier`; the claim's
after-state (9/14, held) is unmet. `measure-after.log` is likewise a pre-flip measurement (8/14).
C1 can only be admitted after L1 flips `corpus/README.md` C05 on an all-criteria Q01–Q13 pass and
re-runs the probe on the final committed archive; a final receipt left at 8/14 falsifies C1 per
`claims.md:24-25` ("8/14 falsifies"). Evidence: §6, §7.

**F2 — MEDIUM (evidence hygiene).** `reports/round-65/measure-after.log` carries no header naming
the measured revision, command, or probe sha256. It is byte-identical to a run on `8214e4d`
(§6) and `LOG.md:901` attributes it to the candidate commit, but the log alone cannot prove which
tree produced it. Recommend the final receipt record `git rev-parse HEAD`, the cwd/TMPDIR shape and
the probe sha256 `8a2c69c4…` (round-62 precedent, `LOG.md:852`).

**F3 — LOW (gate reading).** The probe's exit code is tied to `HOLDS_OK` (V1) only: the base tree
exits **0** with `HOLDS_OK_V3=no` (§5), and it would also exit 0 if V3 regressed at any tree where
V1 holds. `claims.md:121-123` requires `HOLDS_OK_V3=yes` **and** exit 0, so the contract is not
violated, but "probe exit 0" must never be quoted as C2/C1 evidence on its own.

**F4 — LOW (residual text-scan surface, already routed).** `C5_CONTROL_PRESENT` is a substring test
on script bytes (`measure.py:299`; the marker occurs exactly once per script today), so
`C5_CONTROL_PRESENT=2/2` alone is not proof of an executed control — the attribution conjunct
(`rc != 0 and last.endswith(C5_MARKER)`, `measure.py:302`) is what gives it teeth. This is the
acknowledged AST-bound-counter debt (`claims.md` §Routed 2), unchanged by this round.

**F5 — INFO (invariant not encoded).** The frozen target also asserts
`K_HELD_BACKED == K_HELD_BACKED_STRICT` at both ends (`claims.md:24-26`), but neither `holds_ok_v2`
nor `holds_ok_v3` reads those labels; a future flip naming an entry marked
`admission-status: rejected` could raise `K_HELD` while V3 stays `yes`. At both ends measured here
the pair is equal (8/14, 9/14), and V3's formula is exactly as frozen — so this is a reading
requirement for adjudication, not a formula defect.

No other actionable finding: label set additive-only, V3 formula exact, C5 clause unique and
exactly deleted, whole-file scan confirmed, red-before reproducible, after-state reachable.

# Residual risk and verification gaps

- I verified the counter, not the entry: Q01–Q13 admission of
  `corpus/knowledge/round-65-apk-axml-byte-evidence.md`, the fixture/oracle/readout bytes, and the
  SOURCES S038–S041 rows are other seats' scope. The counter's C1 labels only prove a held row names
  an existing file with no `admission-status: rejected` marker.
- Census, README legend semantics beyond the token scan, and lesson text were not re-verified here.
- Scratch trees used: `/tmp/r65base.8towQE` (base archive), `/tmp/r65counter.r6zvau`
  (HEAD archive + flip simulation), `/tmp/r65head.XXXXXX` (HEAD archive for the after-log diff). No
  lane file, index, or jj state was written; the only lane write is this report.
