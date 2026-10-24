PASS — the landed C5 patch is no-harm to C2/C3/C4: attributed counts stay 2/2, 2/2, 2/2 and every control passes at HEAD 8214e4d, with mutant traces byte-identical to the pre-patch base except the two new C5 lines.

# R65MutIcon — regression sweep of C2/C3/C4 frozen mutants under the C5 patch

Seat: mutation-tester, round-65 hyaku wave. Scoped no-harm check for C2 (calibration).
Target: committed lane tip `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` (HEAD, clean at start and end
of run; only peer untracked seat reports appeared later, see §Repo state).
Contract read first: `reports/round-65/claims.md` (frozen kill rule, predicate, admission order).
Detector: frozen counter `reports/round-65/measure.py` (332 lines), run from `/` as prescribed.

Scratch (lane-owned, all writes here): `/tmp/r65muticon.AnME32/`
- `tree/` = `git archive 8214e4d | tar -x` (HEAD bytes)
- `base/` = `git archive 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f | tar -x` (pre-patch bytes)
- `manual/`, `hashes/` = mutate-and-restore copies

## Commands and actual output

### 1. After-state, committed HEAD tree (the sweep)

```
S=/tmp/r65muticon.AnME32
git -C .../revenger-shokunin archive 8214e4dd... | tar -x -C "$S/tree"
cd / && TMPDIR="$S/tmp" python3 -B .../reports/round-65/measure.py "$S/tree"
EXIT=0
```

Relevant lines (verbatim):

```
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
C5_CONTROL_PRESENT=2/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=2/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=yes
HOLDS_OK_V3=yes
```

No regression: every C2/C3/C4 count and control equals the pre-patch red-before values in
`reports/round-65/measure-before.log`.

### 2. Baseline re-derivation (pre-patch tree, same detector)

```
git archive 3eebcdd... | tar -x -C "$S/base"; TMPDIR=$S/tmpbase python3 -B measure.py "$S/base"
BASE_EXIT=0
```

Programmatic comparison of the frozen receipt vs my rerun over keys
`K_HELD=, K_ROW C05, C2_, C3_, C4_, C5_, HOLDS_OK`: **IDENTICAL** (including
`C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2`, `HOLDS_OK_V3=no`). The detector is the same one
the red-before receipt used; the only after-delta is the C5 rows.

### 3. Base vs HEAD mutant traces (the actual no-harm diff)

```
diff <(grep '^MUTANT' measure-base.log | sed 's/^MUTANT //') \
     <(grep '^MUTANT' measure-after.log  | sed 's/^MUTANT //')
16c16,18c18   ← only the two c5 lines:
< verify_icon_languages.py c5 exit=0 pass :: PASS: ... forged selection REJECTED
> verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted
< verify_multi_icon_states.py c5 exit=0 pass :: PASS: ... forged second match REJECTED
> verify_multi_icon_states.py c5 exit=1 killed :: AssertionError: r42: forged receipt evidence accepted
```

Every C2 `b`/`d2`, C3 `c3`, C4 `c4` line — script, exit code, state and message — is
byte-identical between base and HEAD, e.g. `verify_icon_languages.py b exit=1 killed ::
AssertionError: r47: forged receipt command accepted` and
`verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted`.

| Label | base 3eebcdd | HEAD 8214e4d |
|---|---|---|
| C2_CONTROLS_PASS | 2/2 | 2/2 |
| C2_RECEIPT_B_KILLED_ATTRIBUTED | 2/2 | 2/2 |
| C3_CONTROLS_PASS | 2/2 | 2/2 |
| C3_RECEIPT_KILLED_ATTRIBUTED | 2/2 | 2/2 |
| C4_CONTROLS_PASS | 2/2 | 2/2 |
| C4_RECEIPT_KILLED_ATTRIBUTED | 2/2 | 2/2 |
| HOLD_CALIBRATION | 4/4 | 4/4 |
| HOLD_REPLAY | 10/10 | 10/10 |

### 4. Hand-run mutant matrix at HEAD (independent of the counter's own loops)

Applied each frozen clause with the counter's own two deletion patterns
(`\s*and\s+<clause>` / `<clause>\s+and\s+`), one hit each, ran `python3 -B corpus/<script>
--self-test` cwd=tree, then restored exact bytes and re-hashed.

| probe | script | regex hits | exit | last line | frozen predicate (`measure.py` line) |
|---|---|---|---|---|---|
| C2-command | verify_icon_languages.py | 1 | 1 | `AssertionError: r47: forged receipt command accepted` | endswith (174) ✓ |
| C2-command | verify_multi_icon_states.py | 1 | 1 | `AssertionError: r42: forged receipt command accepted` | endswith (174) ✓ |
| C3-command | verify_named_multi_icon_states.py | 1 | 1 | `AssertionError: r55: forged receipt accepted` | substring (214) ✓ |
| C3-fixture_sha256 | verify_icon_states.py | 1 | 1 | `AssertionError: r36: forged receipt accepted` | substring (214) ✓ |
| C4-stdout_sha256 | verify_icon_languages.py | 1 | 1 | `AssertionError: r47: forged receipt stdout accepted` | endswith (257) ✓ |
| C4-stdout_sha256 | verify_multi_icon_states.py | 1 | 1 | `AssertionError: r42: forged receipt stdout accepted` | endswith (257) ✓ |
| C5-evidence_id | verify_icon_languages.py | 1 | 1 | `AssertionError: r47: forged receipt evidence accepted` | endswith (306) ✓ |
| C5-evidence_id | verify_multi_icon_states.py | 1 | 1 | `AssertionError: r42: forged receipt evidence accepted` | endswith (306) ✓ |

Controls (unmutated, same tree): all four scripts `exit=0` with their PASS lines; both C5
carriers print `C5_CONTROL_PRESENT=yes`.

### 5. Byte-level before/mutated/restored evidence

```
verify_icon_languages.py     pristine 64dc17ded0e32805c7a546e29e9f1e84dff30a68cb56df2c7d422c625bfbd93b
                             restored 64dc17... (same)  restored_ok=True
  C2 mutant a3deb5e5777b285e8f3c3a46113a4e245a33dccce8e0a318802c01dfe3acff0d exit=1
  C4 mutant be4e92d4b9e43175d842e134b9977faf2633d9e34dab3a7f600685f92f27bc15 exit=1
  C5 mutant 90ad7fc6ea955626cc6c26883af71e6d76d1a98b3b898c234a857c8e7196c275 exit=1
verify_multi_icon_states.py  pristine 320bf24ce25c01abce4732f02e97954c9596c690807fbc48e03194c957055818
                             restored 320bf24... (same)  restored_ok=True
  C2 mutant 943a43d1dddea6648898585c3ad19cf9cb8f869416c1ed8bf2357b4b96760efc exit=1
  C4 mutant 12669c314e53714f9ba16f279671b341f9e9dead5adfd0c4062d37bbb2e3c39a exit=1
  C5 mutant 876aef179d7d7a86642ea8296fc185c0ddf2cbf8d145a5482265c9dfaed168f0 exit=1
verify_named_multi_icon_states.py pristine a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe
                                  restored a226bf73... (same)  restored_ok=True
  C3 mutant 21b15fac7b2a5c2f50dff874f9d5be76f75a70742eda3d1a45527806b75cb12a exit=1
verify_icon_states.py             pristine 7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a
                                  restored 7cbd931a... (same)  restored_ok=True
  C3 mutant 6cf557650b13d753ef555cc0b3c1883fdecf903c9cb3cbc90e0ce707e7f1acd6 exit=1
```

`restore_ok=True` for all 8 probes; scratch tree script hashes equal lane bytes
(`sha256sum` scratch vs working tree: SAME ×4).

### 6. Patch shape (why no harm is expected)

```
git diff --numstat 3eebcdd 8214e4d -- corpus/verify_icon_languages.py \
    corpus/verify_multi_icon_states.py corpus/verify_named_multi_icon_states.py corpus/verify_icon_states.py
3  0  corpus/verify_icon_languages.py
3  0  corpus/verify_multi_icon_states.py
```

Insertions only; no deletions; C3's two scripts are untouched (absent from numstat).
`receipt_ok` is unchanged — `corpus/verify_icon_languages.py:118-120` and
`corpus/verify_multi_icon_states.py:121-123` do not appear in the diff. The three added lines
per script are the deep-copied foreign-ID control
(`corpus/verify_icon_languages.py:155-157`,
`corpus/verify_multi_icon_states.py:154-156`), matching the frozen fix shape.

## Findings

1. **No-harm confirmed (primary).** C2 2/2, C3 2/2, C4 2/2 attributed and all controls 2/2
   both before the C5 patch (rerun reproduces `measure-before.log` exactly) and after it
   (HEAD 8214e4d, `HOLDS_OK_V3=yes`, exit 0). The only trace delta is the intended C5 flip.
2. **Latent attribution looseness, pre-existing, not a regression (observation for a future
   counter registration).** The frozen C3 predicate is a substring test
   `"forged receipt" in last.lower()` (`reports/round-65/measure.py:214`). The C5 control
   message `forged receipt evidence accepted` also satisfies it. Today this cannot contaminate
   C3 because the C5 patch touches only `verify_icon_languages.py` /
   `verify_multi_icon_states.py` (numstat 0 for the C3 pair). If a C5-style evidence control is
   later added to `verify_named_multi_icon_states.py` or `verify_icon_states.py`, C3 kills
   could be satisfied by the evidence control alone — recommend a suffix/anchored predicate
   when that counter is next registered. Recorded, not scored: the frozen rule overrides.
3. **Pre-admission K state, context only.** At HEAD the sweep also showed `K_HELD=8/14`,
   `K_ROW C05 status=frontier` — consistent with the declared build state (README C05 not
   flipped; the 9/14 target requires L1's Q01–Q13 admission flip). Not scored by this seat.
4. **Repo state.** Lane HEAD stayed `8214e4d` during the sweep; `corpus/` received no writes
   from me. Late `git status --porcelain` listed only untracked peer seat reports under
   `.ufo/waves/round-65/` (R65BlindDerive, R65CriticHarms, R65DexReprobe, R65EntryCommands,
   R65ExecCensusProbe, R65FixtureRegen, R65ScoutC05Ground, R65ScoutCensus, R65ScribeGate,
   R65SnapshotManifest) — concurrent wave traffic, not mine. I wrote only this report.
5. **Tooling.** No installs or upgrades; python3 stdlib only (existing interpreter). Nothing
   to record under the tooling directive.

## Verdict

**PASS.** The C5 patch does not regress C2/C3/C4: `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`,
`C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, controls 2/2 per
family, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, exit 0 — identical to the pre-patch
baseline, whose rerun matched the frozen red-before receipt exactly.
