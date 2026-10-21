# R62BaselineHolds — frozen C1 baseline hold re-measure (round 62, attempt 1)

RESULT: COMPLETE

Scope: one authorized verification run of the UNCHANGED round-61 probe on the frozen round-62 base archive + exact stdout comparison vs `reports/round-62/measure-before.log`. No admission, no README flip, no corpus mutation, no old-mutant re-run outside the probe. Full transcript: `/fast/scratch/hyaku/revenger-r62/R62BaselineHolds/evidence-identity.txt`.

## 1. Revision binding

- Base archived `5bd4a90fc1a34caa94496601b60537b3aab12301`; claims frozen at `a3498e25ad87bf756288812d0ea7c474b09433c7` (= `HEAD`). `git diff --stat 5bd4a90 a3498e25` touches ONLY `LOG.md`, `reports/round-62/claims.md`, `reports/round-62/measure-before.log` — zero `corpus/` changes ⇒ corpus tree byte-identical across both revisions.
- Probe unchanged: worktree blob == frozen blob `bc61ac5b6a558661ec52d47176b5131d57e0432f` (`git hash-object reports/round-61/measure.py` == `git rev-parse 5bd4a90:reports/round-61/measure.py` == `git rev-parse a3498e25:reports/round-61/measure.py`).

## 2. Commands (scratch only, cwd=/)

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar 5bd4a90fc1a34caa94496601b60537b3aab12301 corpus | tar -x -C /fast/scratch/hyaku/revenger-r62/R62BaselineHolds/before
extract_rc=0 ; 470 corpus files
$ cd /
$ python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-61/measure.py /fast/scratch/hyaku/revenger-r62/R62BaselineHolds/before
probe_exit=0            # stderr empty
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
census_rc=0
```

Extraction integrity: all 470 archived blobs re-hashed as git blob SHA-1 against `git ls-tree -r 5bd4a90 -- corpus` → 0 mismatches, 0 missing; post-run tree re-hash unchanged (`7a9734aa…`). The probe mutates only fresh `tempfile.TemporaryDirectory()` copies. Env: Python 3.14.8 [GCC 16.2.1 20260810]; probe cwd = `/`.

## 3. Exact stdout comparison vs `reports/round-62/measure-before.log`

The before-log embeds the probe stdout as the 27-line block between the `measure.py` invocation line and `probe_exit=0`; byte comparison against the fresh run's stdout:

```
expected_sha256= ad003a463878d7b1aac139ded61d27b6d05465c3dffa37c6309bc2deeb9771f6
actual_sha256=   ad003a463878d7b1aac139ded61d27b6d05465c3dffa37c6309bc2deeb9771f6
EXACT_MATCH= True        # unified diff empty
```

Line order and the trailing `HOLDS_OK=yes` reproduced exactly.

## 4. Recorded values (fresh run; identical to before-log)

- **K = 4/14, score 2.9**: `K_HELD=4/14 score=2.9`, `K_HELD_BACKED=4/14`.
- **C04 status=uncovered**, **C09 status=uncovered**; denominator unchanged at 14 (`grep -cE '^\| C[0-9]+ ' corpus/README.md` = 14); held rows = C01, C11, C12, C13.
- **C2**: `C2_CONTROLS_PASS=2/2`, `C2_RECEIPT_B_KILLED=2/2`, `C2_D2_KILLED=2/2`, **`C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`**. Both b kills attributed, not crashes: last lines `AssertionError: r47: forged receipt command accepted` (verify_icon_languages.py) and `AssertionError: r42: forged receipt command accepted` (verify_multi_icon_states.py), both exit=1; both controls exit=0; both d2 rows fail at `receipt`.
- **All holds**: `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`; all 10 `HOLD …` rows `exit=0` (rows not matching `exit=0` = none): verify_evm_evidence, icon_languages, icon_states, js_graph_delta, multi_icon_states, named_multi_icon_states, pe_resources, saved_evidence, semantic_trace, shape_evidence.
- **Probe exit = 0** (2 = could-not-evaluate, 1 = failed hold); stderr empty. Census tail identical to before-log (same W04 warning, ok registry, rc=0).

## 5. Byte-preservation / no-credit checks

- `git status --porcelain` → only `?? .ufo/waves/round-62/` (untracked report dir); `git diff --stat -- corpus reports LOG.md` empty ⇒ no corpus/live, corpus/fixtures, reports or LOG change. Prior rejected round-61 entries, `corpus/lessons/round-61*.md` and round-61 reports/counterexamples untouched.
- Extracted verifier digests equal the round-61 lesson's recorded values: `verify_icon_languages.py` `0f781c6a…a8efbd`; `verify_multi_icon_states.py` `0179e93f…7a176d`; extracted `corpus/README.md` `2c8606d3…e96e8e23f`.

## 6. Constraints honored

- **README stays uncovered**: C04/C09 remain `uncovered`; no row status flipped, no admission, no score improvement claimed. Baseline still K 4/14 ⇒ 4/14 still falsifies C1 until a genuinely gated NEW entry lifts it to ≥5/14. No new gate/registry/promotion claim; this is a measurement artifact only.
- No old failed mutant re-run standalone; the only mutant executions were the probe's own internal fresh-temp copies in the single authorized run.
- No fixture JS, EVM bytecode, REA producer, live-target, chain/RPC or service action; no jj/Git index/history mutation (read-only `archive`, `ls-tree`, `hash-object`, `diff`, `status`, `rev-parse`).

## 7. Residual risk / verification gaps

- The probe is the counting instrument only: `K_HELD_BACKED=4/14` proves row/file existence, **not** Q01–Q13 quality admission; per-candidate Q01–Q13 decisions remain the independent admission condition for the round-62 C04/C09 candidates.
- A build-wave landing touching `corpus/README.md` rows changes this number; only the L1 integrator should re-measure after the build wave and the fresh falsify wave.
- The W04 census warning (duplicate URL across scopes, S024) is pre-existing, does not change lane status (`ok`, rc=0), and was not caused by this run.

## 8. Proposed changes

None to corpus or production tree. Scratch-only artifacts under `/fast/scratch/hyaku/revenger-r62/R62BaselineHolds/` (optional L1 reuse; not admission evidence): `probe-stdout.txt` (27 lines, sha256 `ad003a46…77f6`), `probe-stderr.txt` (empty), `evidence-identity.txt` (full transcript + digests), `before/` (frozen 5bd4a90 corpus extract, 470 files, 0 blob mismatches, kept for the post-build re-measure).

## 9. Installs

None. Only pre-existing `python3` 3.14.8, `bash`/`coreutils` and `git` were used.

RESULT: COMPLETE — K 4/14 (2.9), C04/C09 uncovered, C2 attributed 2/2, d2 2/2, controls 2/2, HOLD_CALIBRATION 4/4, HOLD_REPLAY 10/10, HOLDS_OK=yes, probe exit 0, cwd=/, stdout byte-identical to `reports/round-62/measure-before.log`. No admission, no README flip.
