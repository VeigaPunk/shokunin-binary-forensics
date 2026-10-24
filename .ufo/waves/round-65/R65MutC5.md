PASS — frozen C5 kill rule reproduced 2/2 attributed on the landed scripts (exit 1, last line ends `forged receipt evidence accepted`), and the identical mutants survive (exit 0) at base `3eebcdd`, in isolated scratch trees only.

# R65MutC5 — C5 evidence-id mutant: kill attribution + red-before

Seat: mutation-tester, round 65 wave (hyaku). Read-only on lane production files; all mutation done in disposable `/tmp/r65-mutc5` scratch trees. No tool installs were needed (pacman guard untouched).

## Surface measured

- Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`, HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0`, working tree clean (`git status --porcelain` empty).
- Trees: `git archive HEAD corpus | tar -x -C /tmp/r65-mutc5/head` and `git archive 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f corpus | tar -x -C /tmp/r65-mutc5/base`.
- Committed script hashes (HEAD tree == working tree):
  - `corpus/verify_icon_languages.py` `64dc17ded0e32805c7a546e29e9f1e84dff30a68cb56df2c7d422c625bfbd93b`
  - `corpus/verify_multi_icon_states.py` `320bf24ce25c01abce4732f02e97954c9596c690807fbc48e03194c957055818`
- Base-tree script hashes: languages `a2fd347e6379bee4d794d008aa0d1ea8b7823a1c0557775318a22a80f9239aa3`, multi `9345cb8c91741e36d1d88805cbe1b2fef4a8c890f96a26dd7ea626909b6a0f7e`.
- `C5_MARKER` presence: HEAD 1 match per script; base 0 matches per script (`grep -c "forged receipt evidence accepted"` → head `1`,`1`; base `0`,`0`), matching claims.md "exists nowhere at base".

## Mutant (frozen, not re-invented)

Extracted verbatim at run time from `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure.py:261-275` (`C5_CLAUSE` / `mutate_c5`) and `exec`'d, so the applied mutation is the frozen one:

```
C5_CLAUSE = re.compile(r"receipt\['evidence_id'\]\s*==\s*evidence_id")
def mutate_c5(text):
    hits = C5_CLAUSE.findall(text)
    if len(hits) != 1:
        return None
    for pattern in (r"\s*and\s+" + C5_CLAUSE.pattern, C5_CLAUSE.pattern + r"\s+and\s+"):
        out, n = re.subn(pattern, "", text, count=1)
        if n == 1:
            return out
    return None
```

Exactly one clause match per script (`corpus/verify_icon_languages.py:120`, `corpus/verify_multi_icon_states.py:123`), so `mutate_c5` returned a mutant rather than `None` in all four applications.

Effect on both scripts (verbatim mutated `receipt_ok` return line):

```
return (receipt['command']==command and receipt['exit_code']==0 and receipt['fixture_sha256']==expected_hash and receipt['stdout_sha256']==H(raw_bytes))
```

i.e. only `receipt['evidence_id']==evidence_id` and its connector were deleted; `receipt_ok` otherwise untouched. Attacked behaviour: a receipt carrying a *real foreign* evidence id (languages `ev_6e0553…2dc3d`, multi `ev_8ed889…d4421`, `corpus/verify_icon_languages.py:156`, `corpus/verify_multi_icon_states.py:155`) is now accepted.

Mutated file hashes (scratch copies):
- languages mutant `90ad7fc6ea955626cc6c26883af71e6d76d1a98b3b898c234a857c8e7196c275`
- multi mutant `876aef179d7d7a86642ea8296fc185c0ddf2cbf8d145a5482265c9dfaed168f0`
- base languages mutant `a552c4cd5fda7acfc2bf6f7c60ca1cd49874a7b4ee8b1c3c220a85d1fe77fa4d`
- base multi mutant `3f4290c419d7965bdcac29706b3fa8b4882575e83d5905c210b150867ec0952c`

## Detector (bounded, identical in every variant)

`python3 -B <tree>/corpus/<script> --self-test` with `cwd=<tree>` and `TMPDIR=/tmp/r65-mutc5/tmp` — the same invocation as `measure.py:117-121`. Kill attributed iff exit != 0 **and** last stdout/stderr line ends with `forged receipt evidence accepted` (`measure.py:302`).

## Actual outputs (verbatim)

### HEAD `8214e4d` — landed controls

| script | unmutated control | frozen mutant |
|---|---|---|
| `verify_icon_languages.py` | `exit=0` :: `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` | `exit=1` :: `AssertionError: r47: forged receipt evidence accepted` |
| `verify_multi_icon_states.py` | `exit=0` :: `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` | `exit=1` :: `AssertionError: r42: forged receipt evidence accepted` |

Both mutants: exit non-zero ∧ last line ends with the marker → **killed and attributed 2/2**. Unmutated controls exit 0, so the kill is caused by the mutation, not by tree breakage.

### Base `3eebcdd` — red-before (same mutants, same detector)

| script | unmutated control | frozen mutant |
|---|---|---|
| `verify_icon_languages.py` | `exit=0` :: `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` | `exit=0` :: `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` |
| `verify_multi_icon_states.py` | `exit=0` :: `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` | `exit=0` :: `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` |

Both base mutants **survive** (exit 0, no marker) → red-before established exactly as claims.md requires: the C5 mutant is uncaught at base.

## Frozen-counter cross-check (independent of my driver)

`TMPDIR=/tmp/r65-mutc5/tmp python3 -B .../reports/round-65/measure.py /tmp/r65-mutc5/head` → **`MEASURE_HEAD_EXIT=0`**, with:

```
K_HELD=8/14 score=5.7
K_ROW C05 status=frontier
K_HELD_BACKED=8/14
K_HELD_BACKED_STRICT=8/14
STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True
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

Counter's own mutant lines at HEAD (verbatim, log `/tmp/r65-mutc5/measure-head.log`):

```
MUTANT verify_icon_languages.py c5 exit=1 killed :: AssertionError: r47: forged receipt evidence accepted
MUTANT verify_multi_icon_states.py c5 exit=1 killed :: AssertionError: r42: forged receipt evidence accepted
```

Same counter on base tree (`/tmp/r65-mutc5/measure-base.log`, `MEASURE_BASE_EXIT=0`) reproduces the pre-registered red-before labels bit for bit against `reports/round-65/measure-before.log`:

```
K_HELD=8/14 score=5.7
K_ROW C05 status=frontier
C5_CONTROL_PRESENT=0/2
C5_CONTROLS_PASS=2/2
C5_RECEIPT_KILLED=0/2
C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2
HOLDS_OK_V3=no
MUTANT verify_icon_languages.py c5 exit=0 pass :: PASS: 3/3 group-language states, ...
MUTANT verify_multi_icon_states.py c5 exit=0 pass :: PASS: 4/4 two-image states, ...
```

## Findings

1. **Kill rule reproduced, attributed, at HEAD 2/2** — exit 1 and marker-suffixed last line for both scripts; unmutated controls green.
2. **Red-before reproduced 2/2** — identical mutants exit 0 at `3eebcdd`, so the C5 control is the sole catcher of this defect (base `C5_CONTROL_PRESENT=0/2`).
3. **No baseline failure / no inconclusive run** — every control run exits 0 in both trees; no `could-not-evaluate` emitted.
4. **Build-state observation (not my claim):** at HEAD `8214e4d` the counter still prints `K_HELD=8/14`, `K_ROW C05 status=frontier`; `corpus/README.md:34` row reads `| C05 | Android packages (APK) | — | — | frontier |`. The claimed after-state `K_HELD=9/14` / `status=held` is therefore **not** present at this revision — consistent with "README C05 NOT flipped" build state, so C1 adjudication/flip remains outstanding. The candidate entry is present (`corpus/knowledge/round-65-apk-axml-byte-evidence.md` exists at HEAD).
5. **Disclosed spoof surface (unchanged, out of scope):** `C5_CONTROL_PRESENT` is a text grep (`measure.py:280`), so a script that merely contains the marker string and exits non-zero could spoof attribution. This is the pre-registered routed debt (claims.md "Routed inputs" item 2); I did not probe it, per seat scope.

## Restoration evidence

- Pristine extracted trees were never written. Re-hash after all runs: head languages `64dc17de…bfbd93b`, head multi `320bf24c…7055818`, base languages `a2fd347e…f9239aa3`, base multi `9345cb8c…09b6a0f7e` — all equal to the values captured before mutation.
- Mutated scratch copies were restored from pristine bytes and re-hash to the pristine values:
  `work-head-verify_icon_languages.py` `64dc17de…`, `work-head-verify_multi_icon_states.py` `320bf24c…`, `work-base-verify_icon_languages.py` `a2fd347e…`, `work-base-verify_multi_icon_states.py` `9345cb8c…`.
- All scratch under `/tmp/r65-mutc5/` (trees, work copies, logs `measure-head.log`, `measure-base.log`) is disposable and outside the lane; no lane file, index, or jj state was modified — this report is the only file written under the lane.

## Verdict

**PASS / calibration holds.** C5 mutant is killed with the frozen attribution predicate 2/2 on the landed scripts and survives 2/2 at base; the frozen counter independently prints `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2` and `HOLDS_OK_V3=yes` with exit 0 at HEAD.
