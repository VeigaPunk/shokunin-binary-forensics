HOLDS-GREEN — every frozen hold conjunct is green on the landed bytes 17ee7f87 (`HOLD_REPLAY=10/10`, `GATE_SELFTEST=exit 0`, `F_COVERAGE=5/8`, `FRESH_ROWS=18/18`, `HOLDS_OK_V7=yes`, counter exit 0), all ten verifier self-tests exit 0 with last lines byte-identical to the base tree, and every `entry_checks.py` flag exits 0 with zero `MISMATCH` lines; two hold-strength limits and one scope note are recorded below, none of which makes a frozen label false.

seat: R70W2HoldSweep (fresh wave-2 leaf) · lane: /home/vgpnk/Projects/shokunin/revenger-shokunin · judged on: operability, calibration
target: lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` (`admission-status: candidate`); base `3f5edbc206351232a3d2d801334dd930499ccaf5`
counters re-verified before use: `measure.py` sha256 `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`, `measure-a1.py` sha256 `96feeaa048f0f2b8ab0f3bb183c714a57ff41e951d4221c09806b6acf2e87191` (both match `claims.md` / amendment A1).

## Trees (stable extraction, no lane writes)

```
D=/tmp/revenger-r70-HoldSweep
git -C <lane> archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C "$D/landed"
git -C <lane> archive 3f5edbc206351232a3d2d801334dd930499ccaf5 corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C "$D/base"
```

## H1 — replay: `verify_*.py --self-test`, 10 of 10, landed vs base

```
$ cd $D/landed && for f in corpus/verify_*.py; do python3 -B "$f" --self-test; echo rc=$?; done
verify_evm_evidence.py            rc=0  NEGATIVE REJECTED candidate destination mismatch
verify_icon_languages.py          rc=0  PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
verify_icon_states.py             rc=0  PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
verify_js_graph_delta.py          rc=0  NEGATIVE REJECTED saved graph disagrees with source truth
verify_multi_icon_states.py       rc=0  PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
verify_named_multi_icon_states.py rc=0  PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
verify_pe_resources.py            rc=0  NEGATIVE REJECTED payload relation mismatch
verify_saved_evidence.py          rc=0  NEGATIVE JS REJECTED: JS: wrong package-main mapping
verify_semantic_trace.py          rc=0  NEGATIVE REJECTED relation differs from source parent
verify_shape_evidence.py          rc=0  NEGATIVE REJECTED changed-property evidence mismatch
REPLAY=10/10   (same ten exit 0 on $D/base → BASE_REPLAY=10/10)
```

Last-line comparison, exact:

```
$ diff <(cd $D/landed/corpus && for f in verify_*.py; do python3 -B "$f" --self-test 2>&1 | tail -1; done) \
       <(cd $D/base/corpus  && for f in verify_*.py; do python3 -B "$f" --self-test 2>&1 | tail -1; done)
(no output) → LAST_LINES_IDENTICAL=yes
```

"The verifiers are untouched" is true by digest, not only by output — all ten files byte-identical base→landed:

```
SAME verify_evm_evidence.py            8265a22f7be8df011cee319a332123a0bfcb011413839a31f602a037c15d0b49
SAME verify_icon_languages.py          2bf9b5feac9e407410b95d15ce898976bfd8d5f4b137f83f6417d2a6e623c0cd
SAME verify_icon_states.py             7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a
SAME verify_js_graph_delta.py          77700f8eb63389f93d1414c965420fdcfab5f196a6fe872dc988490bd7e43aeb
SAME verify_multi_icon_states.py       09c507744c1fd2eb9d4479721314f4e3ce2299dd621992d4fecfb26a11c44cd1
SAME verify_named_multi_icon_states.py a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe
SAME verify_pe_resources.py            57cdb4d325086882100567241f5464caef2a5fdbc5c421fe2b934d9586a6d279
SAME verify_saved_evidence.py          7fbd193232d6be8f5b9997554d7769e90f0fb7b97a502fbd65fb557bafd8c930
SAME verify_semantic_trace.py          088d20623393ef9aa4101d59baf6c5beb1f4179939bf808b90114cda864b8527
SAME verify_shape_evidence.py          eed7725a407bb7c463c39c611463c364118457d777c41cdd9599efbe931dda44
```

## H2 — the four tool self-tests (landed tree, cwd = tree root)

```
$ python3 -B corpus/check_embedded_outputs.py --self-test   → rc=0
  SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pinned script
  verified by digest and named by the entry, commands confined to relative scripts inside the tree
$ python3 -B corpus/q15_tree_id_check.py --self-test        → rc=0  Q15_SELFTEST=pass (true sentence verified; false sentence killed)
$ python3 -B corpus/lint_entry.py --self-test               → rc=0
  SELFTEST OK: clean 0; four planted defects each scored exactly their class; truncated-run-with-count,
  two-count clause, uppercase run, outside-ellipsis, reordered decision column and duplicate Q-map section handled
$ python3 -B corpus/self_assessment_check.py --self-test    → rc=0
  SELFTEST OK: clean 0; six planted defects each scored exactly their class; fourteen tightened-class probes
  scored as declared; erratum excuses only a resolving, prefix-sharing correction
```

Base comparison of the same gate self-test (the gate legitimately learned clauses under A1's treatment change; verifiers did not):

```
base: SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired   (rc=0)
```

Tool digests on landed bytes (all resolve from the extraction):

```
5f42415bd4124cf916ecfd9b745d030254a29d299afbe8061a89b784e0d9e879  corpus/check_embedded_outputs.py
82e59fce5647f27727644d121dd73641bc14a7bb3293d7e54f2070b0db0335cc  corpus/self_assessment_check.py
3ef6c7b119b2a5003afdf38ed7981d445565d7575e9aa437e60147393183d76b  corpus/lint_entry.py
7d074f98cb7f9ff2be4c17e6b97e60ac8d660c827a32009d85a35df50639d276  corpus/q15_tree_id_check.py
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors_r68.py
2d4f25f6894ac86ced3c9986abd7cdbcf4c6d2aab477cda6dc515585c129b1f9  corpus/fixtures/apk-r65/entry_checks.py
```

`derive_axml_anchors_r68.py` = `bce497d6…` = `S046_SCRIPT_SHA` in `reports/round-70/measure.py:35` and the C3 predicate's stated digest — the S046 binding re-derived independently of the counter (`EMB_PINNED_SCRIPT_IS_S046=yes` in H5 is not the only witness).

## H3 — `entry_checks.py`, every flag, exit 0 and no MISMATCH

```
$ cd $D/landed && for f in --pins --eocd --oracle --zip-layout --container --axml-layout --stdout-digest --spec-quotes; do
    python3 -B corpus/fixtures/apk-r65/entry_checks.py $f; echo rc=$?; done
--pins           rc=0  mismatch=0  lines=10
--eocd           rc=0  mismatch=0  lines=1   (eocd signature bytes at offset 925: 504b0506 (4 bytes))
--oracle         rc=0  mismatch=0  lines=34
--zip-layout     rc=0  mismatch=0  lines=20  (central.fixed_part spec width 46 ↔ readout.py `cursor + 46`; local 30 ↔ `lh_off + 30`)
--container      rc=0  mismatch=0  lines=3   (3/3 records: flags=0x0000 method=0, bit 3 clear, oracle method 0)
--axml-layout    rc=0  mismatch=0  lines=24  (valueSize 12 / valueDataType 15 / valueData 16 all MATCH the readout literals)
--stdout-digest  rc=0  mismatch=0  lines=1   (readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247)
--spec-quotes    rc=0  mismatch=0  lines=6   (all quoted phrases located in the committed snapshots)
```

## H4 — frozen counter on the landed tree (the hold block, verbatim)

```
$ python3 -B reports/round-70/measure.py $D/landed ; echo MEASURE_RC=$?
C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
HOLDS_C1_V5=no            (V5_ADMITTED_MARKED=no — correct at the candidate landing point, landing order step 1)
SELF_MISMATCH=0 exit=0 · SELF_CLEAN_FIXTURE=0 · SELF_MUTANTS_KILLED=6/6 · SHONEN_BOX_COUNT=4 · README_ROWS=14 · HOLDS_C2_V5=yes
EMB_R65=checked_blocks=15 problems=1 · EMB_R67=16/0 · EMB_R68=17/0 · EMB_R69=17/0
EMB_PINNED_SCRIPT_IS_S046=yes · EMB_R68_BYTES_UNCHANGED=yes · EMB_R65_BYTES_UNCHANGED=yes · EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1 · HOLDS_C3_V1=yes
HOLD_REPLAY=10/10
GATE_SELFTEST=exit 0
F_COVERAGE=5/8 score=6.2
FRESH_ROWS=18/18
HOLDS_OK_V7=yes
MEASURE_RC=0
```

Base (do-nothing control) reproduces `claims.md` §Controls A: `K_HELD_BACKED=8/14`, `C05_STATUS=uncovered`, `HOLDS_C1_V5=no`, `SELF_MISMATCH=n/a (no checker)`, `HOLDS_C2_V5=no`, `HOLDS_C3_V1=no`, `HOLD_REPLAY=10/10`, `GATE_SELFTEST=exit 0`, `HOLDS_OK_V7=yes`, exit 0.

A1 counter on the landed tree (predicate conjunct, re-derived):

```
A1_C1_DETAIL=distinct_commands=24 scripts_allowlisted=True readout_lines=15/15 source_rows_tier_a=7/7
A1_C2_DETAIL=base_vector=yes clean_variant=yes defect_variants=6/6
A1_C3_DETAIL=binds_s046=yes script_digest=yes script_prints_17_lines=yes
A1_C1=yes A1_C2=yes A1_C3=yes A1_RC=0
```

Direct (non-counter) reproductions on the landed tree:

```
$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md --lane <lane>
LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0   rc=0
$ python3 -B corpus/self_assessment_check.py --root . --lane <lane>
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0  SELF_MISMATCH=0   rc=0
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md → checked_blocks=17 problems=0
$ … round-65… → checked_blocks=15 problems=1 · round-67… → 16/0 · round-69… → 17/0
$ python3 -B corpus/q15_tree_id_check.py --scan corpus/lessons/round-69.md --lane <lane> → rc=0  Q15_RESTATE_OK=yes
```

## H5 — hold-strength limits (recorded; no frozen label is false)

**L1 — `--self-test` is inert in 4 of the 10 verifiers, so `HOLD_REPLAY` measures full-run exit for those four.**
`corpus/README.md:17` documents `verify_*.py` as taking `--self-test`; six verifiers branch on it
(`corpus/verify_evm_evidence.py:66`, `verify_js_graph_delta.py:69`, `verify_pe_resources.py:60`,
`verify_saved_evidence.py:130`, `verify_semantic_trace.py:89`, `verify_shape_evidence.py:112` — each
`if "--self-test" in sys.argv:`), while four have zero `sys.argv`/`argparse` references and call `main()`
unconditionally (`verify_icon_languages.py:183`, `verify_icon_states.py:180`, `verify_multi_icon_states.py:183`,
`verify_named_multi_icon_states.py:106`). Probe — stdout is byte-identical with and without the flag:

```
$ for f in verify_icon_languages.py verify_icon_states.py verify_multi_icon_states.py verify_named_multi_icon_states.py; do
    md5sum <(python3 -B corpus/$f) vs <(python3 -B corpus/$f --self-test)
FLAG_NOOP verify_icon_languages.py           out=3373e4a5b00ae4f08d55043b6ae6128e
FLAG_NOOP verify_icon_states.py              out=545d9a261f97d9f0b33195c59a8ad52d
FLAG_NOOP verify_multi_icon_states.py        out=a8489af3a145b9031741e916e513a397
FLAG_NOOP verify_named_multi_icon_states.py  out=33d4a47378f78e06ad2fb5e10c6bc645
```

These four still do real fixture verification and exit 0, so `HOLD_REPLAY=10/10` and the §Holds gloss "every
`verify_*.py --self-test` exit 0" both remain literally true; what the label does not give for those four is a
self-test *mode* distinct from the full run. Not a red hold, not a located defect in the candidate entry.

**L2 — `HOLD_REPLAY` pins no verifier digest; a one-line stub keeps the hold green.**
`reports/round-70/measure.py:246-252` globs `(tree/"corpus").glob("verify_*.py")`, runs each `--self-test` and
counts `rc == 0`; nothing compares a digest. Mutants on copies in `/tmp` (`cp -r` of the landed tree, lane
untouched):

```
M1  break a real assertion (`verify_icon_states.py`: `len(current) == len(baseline) == 1024` → `999`)
    → HOLD verify_icon_states.py exit=1 AssertionError · HOLD_REPLAY=9/10 · HOLDS_OK_V7=no · MEASURE_RC=1
M2  replace verify_shape_evidence.py with `print("PASS: stub")`
    → HOLD verify_shape_evidence.py exit=0 PASS: stub · HOLD_REPLAY=10/10 · HOLDS_OK_V7=yes · MEASURE_RC=0
M3  delete corpus/verify_pe_resources.py
    → HOLD_REPLAY=9/9 · HOLDS_OK_V7=no · MEASURE_RC=1
```

M1/M3 are the positive controls (the hold can go red for a failing or absent verifier, and the deleted case is
caught by the `len(ps) == 10` conjunct); M2 is the limit: the hold cannot tell a stub from the real verifier, so
its protection comes only from the bytes actually present at the tip. I re-derived that the tip's bytes are the
real ones (H1 digests, all SAME as base), which is the conjunct the counter does not itself check.

**L3 — scope note on the word "every".** The extraction holds 11 `verify_*.py`, not 10:

```
$ find $D/landed -name 'verify_*.py' | wc -l   → 11
$ python3 -B corpus/live/runs/round-34/verify_review.py --self-test
FileNotFoundError: [Errno 2] No such file or directory: '.shokunin/revenger/corpus/fixtures/pe-r34/fixture.exe'   rc=1
```

It is a round-34 saved non-author reviewer script with a hardcoded out-of-tree path
(`corpus/live/runs/round-34/LEDGER.md:8`), excluded by the counter's non-recursive glob
(`reports/round-70/measure.py:246`) and by the documented census of ten (`corpus/README.md:61`, `SKILL.md:32`).
`HOLD_REPLAY=10/10` is therefore correct under that scoping; the §Holds parenthetical in `claims.md` should be
read as "every `corpus/verify_*.py`".

## Verdict inputs (for the kill-rule ledger, not a Q decision)

This seat made no Q01-Q15 decision and no C1 PASS/FAIL call; it attacks the hold block only. Hold inputs handed
to the L1: `HOLD_REPLAY=10/10` (green, independently replayed), `GATE_SELFTEST=exit 0`, `F_COVERAGE=5/8`,
`FRESH_ROWS=18/18`, `HOLDS_OK_V7=yes`, counter exit 0 — with L1/L2/L3 above as the hold's calibration record.
`HOLDS_C1_V5=no` at the landed target is the frozen landing-order state (step 1: `admission-status: candidate`,
README C05 row unflipped), not a red hold.

## Files changed

None. This report is the only write. Scratch `/tmp/revenger-r70-HoldSweep` (two extractions + three mutant
copies) deleted before return. No lane or fleet git command was mutating; all reads used `git archive` / `git show`.
No package installed or upgraded (no `uv tool`, no `npx`, no pacman); the sweep used the system `python3`
(3.14) and coreutils only, so there is no tool/version/channel entry to record.

## Risks / blockers

- L2 means a future stub verifier at the tip would not be caught mechanically; the digest identity in H1 is a
  manual check this seat performed, not a counter conjunct. A tightening would add a verifier-digest table to the
  hold (not proposed here — predicate changes are frozen).
- L1's four inert flags are a documentation-vs-behavior gap that a later operability claim could trip over.
- No blocker: every artifact needed (both extractions, both counters, all ten verifiers, `entry_checks.py`,
  the four tool self-tests) was present at the pinned commit.
