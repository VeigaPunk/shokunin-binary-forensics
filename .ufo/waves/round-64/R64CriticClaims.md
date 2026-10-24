# R64CriticClaims — numeric-sufficiency counterexamples

## Axes and scope

- **Coverage K / expansion:** distinguish an existing Markdown path from one newly admitted C07 entry.
- **Calibration / discernment:** distinguish mutation-sensitive code from an exercised forged-stdout receipt rejection.
- **Preservation / operability:** retain authored bytes, saved records, baseline assertions, denominator and replay census.

**Result: reproduced exhibits, not an admission judgment.** A one-line README-only tree reaches both K counters at 8/14 without adding or admitting an entry. Adding one source-fingerprint assertion per existing script also reaches C4 2/2 and `HOLDS_OK_V2=yes` without a forged-stdout receipt control. These defeat numeric sufficiency; they do not satisfy the frozen contract's independent admission and exact-fix-shape requirements. No canonical judge or orchestration runtime was invoked.

## Frozen inputs and experiment bounds

Read the assigned brief and all of:

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure-before.log`

Frozen counter SHA-256 observed: `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168`.

Both experimental trees came from a read-only `git archive 666ea84b6be2eec2b0359f556ba2429fc9044c36 corpus`, not the concurrently changing working tree. Scratch root: `/tmp/revenger-r64-criticclaims-SW8Vfp`. No production corpus, frozen counter, Git index, jj state, wave specification or registry was changed. Only scratch adversarial variants and this assigned report were written. No tools were installed or updated.

The supplied red-before receipt remains the unchanged-tree evidence: K 7/14, strict K 7/14, legend mismatch 1, C4 0/2, `HOLDS_OK=yes`, `HOLDS_OK_V2=no`. I did not rerun that reported baseline.

## Exhibit 1 — README-only false coverage credit

### Exact change

In the base archive's `corpus/README.md`, replace only:

```diff
-| C07 | firmware images | — | — | frontier |
+| C07 | firmware images | `knowledge/seed.md` | — | held |
```

No knowledge file is added or modified. `knowledge/seed.md` is an existing legacy census/discipline document; its `coverage-map:` at line 4 names C02, C10, C12, C14, not C07. This is not the registered round-64 entry and creates no fresh C07 admission.

### Executed command and observed output

Cwd `/`; command:

```sh
env TMPDIR=/tmp/revenger-r64-criticclaims-SW8Vfp/probe-tmp python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py /tmp/revenger-r64-criticclaims-SW8Vfp/k-only
```

Completed successfully. Relevant exact output:

```text
K_HELD=8/14 score=5.7
K_ROW C07 status=held
K_HELD_BACKED=8/14
K_HELD_BACKED_STRICT=8/14
SAVED_RECORDS=59
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
F_COVERAGE=5/8 score=6.2
FRESH_ROWS=18/18
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py c4 exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_multi_icon_states.py c4 exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=no
```

### Mechanism and smallest safe correction

`measure.py:33-35` accepts any matching `knowledge/[\w.-]+\.md` path that exists. Lines 45-49 additionally exclude only the literal rejected marker in the first 2000 characters. Neither label establishes C07 scope, novelty, or admission. Strict equality therefore does not rescue this example. The legend check also becomes zero because C07 is no longer `frontier`; zero does not certify that `held` is warranted.

This coarseness is explicitly acknowledged by `claims.md:51-55`: K measures existence, never quality. **Current-round correction:** keep the counter frozen and require the already registered exact candidate path plus named independent Q01-Q13 decisions before accepting a C07 `held` row. Do not interpret either K label or legend mismatch zero as an admission authority. If admission fails, use the registered `uncovered` fallback, not this false `held` row. A later registered counter could bind the exact newly admitted entry and its admission evidence; that is not a reason to thaw this counter.

## Exhibit 2 — C4 attribution without a forged-stdout control

### Exact additional changes

Starting from Exhibit 1, insert only the following line after the existing forged-command rejection in each respective script:

`corpus/verify_icon_languages.py`, immediately after original line 151:

```python
    require('stdout_sha256' in receipt_ok.__code__.co_consts, f'r{r}: forged receipt stdout accepted')
```

`corpus/verify_multi_icon_states.py`, immediately after original line 150:

```python
    require('stdout_sha256' in receipt_ok.__code__.co_consts, f'r{round_id}: forged receipt stdout accepted')
```

These assertions inspect implementation constants. They never deep-copy a receipt, change `stdout_sha256`, or call `receipt_ok` on a forged stdout digest. All existing positive assertions and forged-command controls remain. The original `receipt_ok` conjuncts also remain until the frozen counter performs its normal mutations.

### Executed command and observed output

Cwd `/`; command:

```sh
env TMPDIR=/tmp/revenger-r64-criticclaims-SW8Vfp/probe-tmp python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py /tmp/revenger-r64-criticclaims-SW8Vfp/combined
```

Completed successfully. Relevant exact output:

```text
K_HELD=8/14 score=5.7
K_ROW C07 status=held
K_HELD_BACKED=8/14
K_HELD_BACKED_STRICT=8/14
SAVED_RECORDS=59
README_TOKEN_LEGEND_MISMATCH=0 rows=[]
F_COVERAGE=5/8 score=6.2
FRESH_ROWS=18/18
MUTANT verify_icon_languages.py b exit=1 killed :: AssertionError: r47: forged receipt command accepted
MUTANT verify_multi_icon_states.py b exit=1 killed :: AssertionError: r42: forged receipt command accepted
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
HOLDS_OK_V2=yes
```

The combined variant changes just one README row and adds two assertion lines; it adds no candidate or admission evidence and no forged-stdout rejection control. Thus every printed numeric target and v2 hold can be reached while skipping both substantive claimed deliverables. This is a semantic-do-nothing counterfeit, not a claim that a literally unchanged tree reaches the targets.

### Mechanism and smallest safe correction

Removing the frozen conjunct removes `'stdout_sha256'` from `receipt_ok.__code__.co_consts`. The fingerprint assertion then fails, and its chosen message meets `measure.py:247`'s `last.endswith("forged receipt stdout accepted")`. The diagnostic reports an attributed receipt-forgery kill even though the failure is caused by source-structure inspection, not forgery rejection. Endswith narrows message matching but cannot prove causation.

**Current-round correction:** retain the frozen counter and enforce the exact implementation shape already required by `claims.md:70-80`: a separate deep-copy, `forged['stdout_sha256'] = H(b'')`, and rejection through the actual `receipt_ok` call. Reject source/bytecode sentinels or unrelated assertions as substitutes for that control. This exhibit is not an admissible tradeoff and cannot establish the claim merely because all printed labels are green. For a later counter, independently exercise the mutated receipt predicate with a forged digest and bind attribution to that assertion site, rather than trusting a suffix alone.

## Kill-rule prefix check

**The `AssertionError:` prefix is not a false-negative problem for the registered endswith rule.** Both actual counterexample mutant runs ended with:

```text
AssertionError: r47: forged receipt stdout accepted
AssertionError: r42: forged receipt stdout accepted
```

The probe counted both. Prefixes do not affect the suffix match. This verifies the requested prefix compatibility, while Exhibit 2 separately demonstrates that compatible spelling does not guarantee truthful attribution. Existing forged-command tails in `measure-before.log:13,16` show the same prefix style.

## Reproduction recipe and interpretation

The executed setup was:

```sh
D=/tmp/revenger-r64-criticclaims-SW8Vfp
mkdir "$D/base"
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 666ea84b6be2eec2b0359f556ba2429fc9044c36 corpus | tar -xf - -C "$D/base"
cp -a "$D/base" "$D/k-only"
cp -a "$D/base" "$D/combined"
mkdir "$D/probe-tmp"
```

The root itself was created with `mktemp -d /tmp/revenger-r64-criticclaims-XXXXXX`; use a fresh generated root to reproduce. Apply the exact one-line replacement above to both tree READMEs; add the two exact assertions only to `combined`; run the two commands above with that root substituted. No additional fixture, saved-record, knowledge, or verifier changes are necessary.

The supplied unchanged-tree control reaches neither target. The README-only counterfeit reaches the K target and eliminates the token mismatch. The combined counterfeit also reaches C4 2/2 and every printed hold. Therefore the strongest supported finding is **counterexample to measurement-as-admission / suffix-as-causation**, not falsification of a correctly implemented and independently admitted round. The independent gate and frozen exact fix shape are essential, not redundant paperwork.

Scratch trees are removed after filing this report; all necessary patches, immutable base identity, counter digest, commands and observed evidence are retained above. No production implementation was proposed for integration, and no admission, claim verdict, or promotion was issued.

Report: .ufo/waves/round-64/R64CriticClaims.md
