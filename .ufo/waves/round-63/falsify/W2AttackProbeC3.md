# W2AttackProbeC3 — frozen C3 counter attack

## Scope and axes

Assigned claim: **C3 calibration**, specifically the attribution predicate and the meaning of `C3_CONTROLS_PASS`. Axes: calibration correctness (designated-control attribution), control reachability/completeness, and reproducible committed-byte provenance. C1 quality/admission and C2 run authenticity are outside this leaf assignment; their incidental printed counts are not admission decisions.

**Review result:** the committed candidate reproduces the literal C3 target, **2/2 attributed kills**. Requested attacks (a) and an unlabeled version of (b) correctly give **0/2 attribution**. Two counter limitations are demonstrated: (c) deleting both forged-receipt controls still prints **`C3_CONTROLS_PASS=2/2`**, and a stronger (b) crashes before the designated controls with a keyword-bearing `RuntimeError` yet receives **2/2 attribution**. These are probe-semantics findings, not evidence that the unmodified candidate currently lacks its controls. No adjudication or integration performed.

## Provenance and execution

Lane tip attacked: `db55bd6488e24e956df5818ae34c2a043d7ddc12` (tip message: round-63 C1 candidate entry/SOURCES/lesson; README still partial). Extracted committed bytes with:

```sh
mkdir -p /tmp/revenger-r63-W2AttackProbeC3/baseline /tmp/revenger-r63-W2AttackProbeC3/tmp
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive db55bd6488e24e956df5818ae34c2a043d7ddc12 corpus reports/round-63/measure.py reports/round-63/claims.md | tar -x -C /tmp/revenger-r63-W2AttackProbeC3/baseline
```

Baseline and all four attack variants were independently run through the **unchanged, archived frozen counter**, cwd `/`:

```sh
env TMPDIR=/tmp/revenger-r63-W2AttackProbeC3/tmp python3 -B /tmp/revenger-r63-W2AttackProbeC3/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeC3/baseline
env TMPDIR=/tmp/revenger-r63-W2AttackProbeC3/tmp python3 -B /tmp/revenger-r63-W2AttackProbeC3/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeC3/a-no-attribution-label
env TMPDIR=/tmp/revenger-r63-W2AttackProbeC3/tmp python3 -B /tmp/revenger-r63-W2AttackProbeC3/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeC3/b-pre-control-crash
env TMPDIR=/tmp/revenger-r63-W2AttackProbeC3/tmp python3 -B /tmp/revenger-r63-W2AttackProbeC3/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeC3/c-deleted-controls
env TMPDIR=/tmp/revenger-r63-W2AttackProbeC3/tmp python3 -B /tmp/revenger-r63-W2AttackProbeC3/baseline/reports/round-63/measure.py /tmp/revenger-r63-W2AttackProbeC3/b2-keyword-pre-control-crash
```

The last invocation used `subprocess.run` with the same argv, environment and cwd so its process exit could also be captured. First three attacks ran concurrently. Only verifier self-tests and the frozen counting probe were executed; no fixture payload, firmware target, or producer CLI was executed. No tools installed/updated; existing Python **3.14.8** used. Read `/home/vgpnk/.omp/agent/RULES.md`; no pacman transaction.

Archived SHA-256:

| Artifact | SHA-256 |
| --- | --- |
| `reports/round-63/measure.py` | `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908` |
| `reports/round-63/claims.md` | `aed53241c3e4445fab94e854e3185b235ab2ff45c921d6c95e6e60938c7d1e31` |
| `corpus/verify_named_multi_icon_states.py` | `a226bf73eaba8f9162c763272b5eed4864fc202de23b8d99839c5e19d34cfffe` |
| `corpus/verify_icon_states.py` | `7cbd931a3a8ef6394b4a69c49f5aec5615b5c9717cb18e2a394075b6cee3214a` |

Each variant was a tree copy of that archive; only the two verifier scripts were edited in `/tmp`. The counter itself performed its frozen, exactly-one-site identity-conjunct deletions. No lane corpus bytes, index, jj state, registry/spec files, or source rows were changed.

## Baseline — attacks C3's claimed 2/2 result

Relevant observed output:

```text
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLDS_OK=yes
```

The baseline supports the frozen numeric C3 claim on the pinned bytes.

## (a) Remove the required phrase — attacks C3 attribution's negative boundary

Changed only both designated failure messages from `forged receipt accepted` to `mismatched identity accepted`; receipt forgery and rejection logic stayed intact.

```text
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: mismatched identity accepted
MUTANT verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: mismatched identity accepted
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLDS_OK=yes
```

Both unmutated controls exited 0. **Requested exclusion holds:** a kill without `forged receipt` is not attributed. `HOLDS_OK=yes` does not imply the C3 target was met.

## (b) Crash before the designated control — attacks C3 crash exclusion

Added a synthetic pre-control guard after constructing the forged receipt, before the existing designated negative-control assertion. It raises only if the forged receipt is accepted, so the unmutated scripts remain green:

Named insertion after original line 77:

```python
 if receipt_ok(forged, command, digest, eid, raw):
  raise RuntimeError('unrelated pre-control crash')
```

Icon insertion after original line 152:

```python
    try:
        receipt_ok(forged, expected_hash, evidence_id, raw_bytes, round_id)
    except AssertionError:
        pass
    else:
        raise RuntimeError('unrelated pre-control crash')
```

Observed:

```text
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: RuntimeError: unrelated pre-control crash
MUTANT verify_icon_states.py c3 exit=1 killed :: RuntimeError: unrelated pre-control crash
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLDS_OK=yes
```

Both unmutated controls exited 0. **Unlabeled-crash exclusion holds.** The original designated assertions are still present but are not reached by these mutants.

### (b2) Stronger counterexample: keyword-bearing pre-control crash

Cloned (b), changing only the injected exception text to:

```python
raise RuntimeError('forged receipt cache unavailable before control')
```

This is a deliberately synthetic crash message, not evidence of any real cache or cache operation. The exception still occurs before the designated negative-control assertion.

```text
MUTANT verify_named_multi_icon_states.py c3 exit=1 killed :: RuntimeError: forged receipt cache unavailable before control
MUTANT verify_icon_states.py c3 exit=1 killed :: RuntimeError: forged receipt cache unavailable before control
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLDS_OK=yes
PROBE_EXIT=0
```

**Finding W2C3-1:** crash exclusion is not semantic. `measure.py:162` accepts any nonzero exit whose selected last line contains the substring. The code therefore follows the contract's literal `iff` rule (`claims.md:84–85`), but does not guarantee the accompanying promise that a crash is not attributed (`claims.md:85–86`). This counterexample must not be presented as a failure of the literal frozen numeric predicate; it demonstrates that the predicate is weaker than that prose assurance.

Impacted axes: calibration correctness and attribution provenance.

Smallest safe correction: do not redefine or edit the frozen predicate mid-round. Bound any current result to **text-attributed** kills. For a separately preregistered semantic crash-exclusion requirement, the demonstrated `RuntimeError` should be excluded by requiring the designated `AssertionError` terminal message and control location, not an arbitrary substring. That is a probe-design correction, not a patch made by this seat.

## (c) Delete both forged-receipt controls — attacks C3 control completeness

Deleted original named lines **76–78** (deep-copy, command forgery, rejection assertion), and original icon lines **151–158** (deep-copy, hash forgery, try/except/else rejection). Preserved the real-receipt checks and their identity conjuncts, so the frozen clause mutation remains evaluable.

```text
MUTANT verify_named_multi_icon_states.py control exit=0 pass :: PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_named_multi_icon_states.py c3 exit=0 pass :: PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
MUTANT verify_icon_states.py control exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
MUTANT verify_icon_states.py c3 exit=0 pass :: PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLDS_OK=yes
```

**Finding W2C3-2:** the assignment's requested property, “both controls deleted → `c3_controls` must fail,” does **not** hold. At `measure.py:159–160`, `c3_controls` means only “unmutated self-test exits zero”; it does not demonstrate that forged-receipt controls exist or ran. `holds_ok` (`179–181`) requires that count but omits `c3_attributed`, so the deleted-control tree still prints `HOLDS_OK=yes`.

This does **not** bypass a caller that independently enforces the frozen C3 target **2/2**: deletion correctly drops `C3_RECEIPT_KILLED_ATTRIBUTED` to **0/2**. It does refute using `C3_CONTROLS_PASS` or `HOLDS_OK` alone as evidence that the new controls are present. This is a fixable measurement/labeling limitation, not evidence of a current candidate control deletion.

Impacted axes: calibration completeness and truthful control provenance.

Smallest safe correction: for this frozen round, require and report the explicit C3 attributed-count target separately from `HOLDS_OK`, and describe `C3_CONTROLS_PASS` as clean-self-test success only. If control-presence failure is a required metric in a future preregistration, qualify each control by both its unmutated pass and its designated mutation response, rather than just exit 0. No frozen-file change is proposed for credit in this review.

## Cross-run observations and reproduction identities

All five runs printed the same non-C3 aggregates: `K_HELD=6/14`, `K_ROW C06 status=partial`, `K_HELD_BACKED=6/14`, `F_COVERAGE=5/8`, `FRESH_ROWS=18/18`, `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`, `C2_D2_KILLED=2/2`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`. These are counter observations only; this leaf did not review C1 Q01–Q13 or validate C2 provenance/oracle agreement.

Variant script SHA-256 (named first, icon second):

| Variant | Named | Icon |
| --- | --- | --- |
| (a) | `20d0421705af6c2fd4e62688a9105fa4a063b216f4dd8d9f2521eede3af6e491` | `a3a9b6195f8896e4cf69193cb0b7d8d3d7f122bcffa2b2f6f78ef133f200bbfe` |
| (b) | `cfe32e3d7fbebf5ea2eaecc9a9225ae88bf5dfd1d6ba978c3bf966ec1cf99fb1` | `f21ebce968ce259ee4a94cd9be7f1c9af5fcb043fbbe4234648fc53c9df1ba57` |
| (b2) | `4fad0b0faf6df88d99181a3e22b74aba0556caada5e3790c4b0514d7b450b9c7` | `2536e371220661e61373e3bcef473ff245dcc6e5d07cc1d6282f01776010613f` |
| (c) | `ef2f35a5f5f65b15db311dea36d905223674fcf649404ced85b8a13aab419acd` | `ad0c040ee5d8403087b5d2911132d8468c2e346c37170e4b0c0644650a07a933` |

Evidence is embedded above so the owned `/tmp/revenger-r63-W2AttackProbeC3` scratch can be removed after this report lands. Only this named report is written into the lane. No source rows introduced; no installs, model arguments, other runtime invocation, or configuration changes.
