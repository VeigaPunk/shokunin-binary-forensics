# R64MutProbe report

## Result

Frozen counter `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py`
run against `/tmp` copies of the PATCHED corpus. Snapshot bytes probed = lane working tree
at 01:19 local: `verify_icon_languages.py` sha256 `a2fd347e…f9239aa3`,
`verify_multi_icon_states.py` sha256 `9345cb8c…9b6a0f7e` (both still current at report time).

| probe | mutant | detector | observed | verdict |
|---|---|---|---|---|
| baseline | none (pristine patch) | frozen counter | `C4_CONTROLS_PASS=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`, exit 0 | target state present on patched bytes |
| **a** | new C4 control lines deleted in both scripts, `stdout_sha256` conjunct intact | each script `--self-test` | both exit 0, PASS lines | **survived** — expected; the control is a guard, not load-bearing |
| **b** | control message changed to end `forged receipt stdout accepted (loose)`; conjunct intact so the frozen `mutate_c4` applies | frozen counter | c4 mutants `exit=1 killed` with last line `AssertionError: r47/r42: forged receipt stdout accepted (loose)`; `C4_CONTROLS_PASS=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=0/2` | **not attributed** — kill real, attribution rejects substring/loose matches |
| b-literal | conjunct deleted *and* message loosened in the tree itself | frozen counter | `C4_CONTROLS_PASS=0/2`, both c4 `could-not-evaluate (clause match count != 1)`, exit 2 | **not counted, not evaluable** — attribution cannot be tested in this shape (frozen mutator refuses) |

Restoration: all three probe trees restored byte-identical to snapshot; restored counter run
exit 0, `C4_CONTROLS_PASS=2/2`, `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`.

## Probe trees and hashes

Scratch (lane-owned): `/tmp/revenger-r64-mutprobe/`.
Snapshot `snapshot/corpus` copied from
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus` via `cp -a`.

| tree | state | `verify_icon_languages.py` | `verify_multi_icon_states.py` |
|---|---|---|---|
| snapshot / baseline | pristine patch | `a2fd347e6379bee4d794d008aa0d1ea8b7823a1c0557775318a22a80f9239aa3` | `9345cb8c91741e36d1d88805cbe1b2fef4a8c890f96a26dd7ea626909b6a0f7e` |
| p-a (mutated) | C4 control deleted | `0f781c6a216bfdaa9cc1ab9b9fe8ae3ab9cb8a79d00ed56c4f94282c80a8efbd` | `0179e93f8bec17d5f4b60047f167ad26aa803a84440e98329fd8a8f2ea7a176d` |
| p-b-attr (mutated) | message loosened | `abc82e4e9888a098758f961e53710caf83c088fb143efacc45617f13634111b9` | `764351b708e55b98e5e55474ba20a9f24e09cca66a71cd6c139a00b8ebf937be` |
| p-b-hand (mutated) | conjunct deleted + message loosened | `ec7c5b6ff8022636fb7b31342bc0209838b55acbac1070cd6d3e1671cc0ee490` | `1fba9e360435a2899ef224a40accdb527353ec16299fdc93df592345d749825f` |
| p-a / p-b-attr / p-b-hand (restored) | all six files re-hashed equal to snapshot | `a2fd347e…` | `9345cb8c…` |

Patch shape verified before probing: both files append three lines after the retained
forged-command control —
`forged_stdout=copy.deepcopy(receipt)`, `forged_stdout['stdout_sha256']=H(b'')`,
`require(not receipt_ok(forged_stdout,…), '… forged receipt stdout accepted')`;
`receipt_ok` keeps `receipt['stdout_sha256']==H(raw_bytes)` (`grep -c` = 1 per file).

## Baseline (pristine patched bytes)

Command (per frozen contract, cwd `/`, TMPDIR lane-owned):

```
cd / && TMPDIR=/tmp/revenger-r64-mutprobe/tmp python3 -B \
  /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py \
  /tmp/revenger-r64-mutprobe/baseline
```

Output (excerpt; full log `/tmp/revenger-r64-mutprobe/out/baseline2.log`), exit 0:

```
MUTANT verify_icon_languages.py control exit=0 pass :: PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted
MUTANT verify_multi_icon_states.py control exit=0 pass :: PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
C2_RECEIPT_B_KILLED=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLDS_OK=yes
HOLDS_OK_V2=no
```

`K_HELD_BACKED=7/14`, `README_TOKEN_LEGEND_MISMATCH=1` (C07 still `frontier`) — expected
pre-integration state; `HOLDS_OK_V2=no` follows from that mismatch, not from C4.
`C4_RECEIPT_KILLED_ATTRIBUTED=2/2` on the current patched bytes is the C2 target state.

## Probe (a) — control deleted, conjunct intact

Mutation (only the three new lines per file removed; forged-command control and
`stdout_sha256` conjunct untouched):

```
corpus/verify_icon_languages.py:120:            receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes))
corpus/verify_multi_icon_states.py:123:            receipt['evidence_id']==evidence_id and receipt['stdout_sha256']==H(raw_bytes))
forged receipt stdout accepted occurrences after deletion: verify_icon_languages.py:0, verify_multi_icon_states.py:0
```

Detector — `python3 -B corpus/<script> --self-test`, cwd `/tmp/revenger-r64-mutprobe/p-a`:

```
PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
ICON_LANGS_EXIT=0
PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
MULTI_STATES_EXIT=0
```

Verdict: mutant **survived** (self-test stayed green). This is the claimed guard property,
not a conjunct coverage gap: the self-test does not fail when its own guard is absent, and
the conjunct itself is still killed by the frozen c4 mutant (baseline `2/2`). A detector
that killed this mutant would mean the control was load-bearing for other assertions.

## Probe (b) — attribution rejects loose/substring matches

Tree p-b-attr: only the control message changed in both scripts, from
`…: forged receipt stdout accepted` to `…: forged receipt stdout accepted (loose)`;
conjunct and control placement intact, so frozen `mutate_c4` still matches exactly once.
Detector: same frozen counter invocation on `p-b-attr`; exit 0.

```
MUTANT verify_icon_languages.py c4 exit=1 killed :: AssertionError: r47: forged receipt stdout accepted (loose)
MUTANT verify_multi_icon_states.py c4 exit=1 killed :: AssertionError: r42: forged receipt stdout accepted (loose)
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLDS_OK=yes
```

Verdict: both mutants are genuinely killed (`exit=1`, non-zero), yet
`C4_RECEIPT_KILLED_ATTRIBUTED=0/2` — the registered `endswith("forged receipt stdout
accepted")` attribution refuses a line that merely contains the phrase as a prefix of a
longer message. Confirms attribution is exact-suffix, not substring/loose.

Secondary note: the counter process itself exits 0 here because C4 is not a term of
`HOLDS_OK` (v1); `HOLDS_OK_V2` does include the attributed counts and reads `no`. C4
admission must therefore be read from the label, not the exit code.

## Probe (b) literal double mutant — recorded, not evaluable

Tree p-b-hand: `receipt['stdout_sha256']==H(raw_bytes)` and its connecting `and` deleted in
`receipt_ok`, plus the same loose message. Frozen counter exit 2:

```
MUTANT verify_icon_languages.py control exit=1 killed :: AssertionError: r47: forged receipt stdout accepted (loose)
MUTANT verify_multi_icon_states.py control exit=1 killed :: AssertionError: r42: forged receipt stdout accepted (loose)
MUTANT verify_icon_languages.py c4 could-not-evaluate (clause match count != 1)
MUTANT verify_multi_icon_states.py c4 could-not-evaluate (clause match count != 1)
C4_CONTROLS_PASS=0/2
C4_RECEIPT_KILLED_ATTRIBUTED=0/2
HOLDS_OK=no
```

Interpretation: with the conjunct already gone, `mutate_c4` finds zero matches and the
counter refuses to evaluate (`evaluable=False`, exit 2); the in-script guard correctly
fails the un-mutated control runs. This shape is not counted, but it does not exercise
attribution — p-b-attr is the valid attribution probe.

## Restoration

Bytes restored from `snapshot/corpus` with `cp`; hashes re-checked:

```
restored p-a / p-b-attr / p-b-hand: a2fd347e…f9239aa3, 9345cb8c…9b6a0f7e (all six equal snapshot)
lane working tree at same moment:   a2fd347e…f9239aa3, 9345cb8c…9b6a0f7e (unchanged)
```

Restored-byte detector, measure.py on `p-a`, exit 0:

```
C2_RECEIPT_B_KILLED=2/2
C4_CONTROLS_PASS=2/2
C4_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLDS_OK=yes
```

## Findings for the planner (not judged, not integrated)

1. **Transient patch defect observed mid-wave.** The first snapshot of
   `corpus/verify_icon_languages.py` (sha256 `2e9e56e8…26d7d15`, mtime 01:17:08) had the
   new C4 lines *replacing* the pre-existing forged-command `require` instead of being
   appended after it (`git diff --stat`: `4 +++-`). Baseline on that snapshot:
   `C2_RECEIPT_B_KILLED=1/2`, `HOLDS_OK=no` (`/tmp/revenger-r64-mutprobe/out/baseline.log`).
   The file was corrected to `a2fd347e…` before the probes above (diff `3 +++`, 0
   deletions; forged-command `require` at line 151). L1 should confirm the landed commit
   carries the append-only shape and re-run the counter on the committed archive — a
   replaced forged-command control would silently regress C2 while C4 still reads 2/2.
2. Attribution results hold only for the frozen `measure.py`; `C4_RECEIPT_KILLED_ATTRIBUTED`
   is exact-suffix, and the process exit code does not reflect C4 (use the label or
   `HOLDS_OK_V2`).
3. No lane file changed by this seat; `/tmp/revenger-r64-mutprobe/` left in place for
   inspection (safe to remove on landing).

## Bounds and tooling

- Writes only under `/tmp/revenger-r64-mutprobe/` plus this report path. No git/jj
  mutations, no commits/pushes, no edits to lane corpus, `.ufo` spec/registry,
  MANIFEST.json, fleet repo, sibling lanes or lane index.
- No tools installed or upgraded (pacman untouched).

Report: `.ufo/waves/round-64/R64MutProbe.md`
