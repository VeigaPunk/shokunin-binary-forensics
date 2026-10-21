GRADE: HOLDS — unchanged round-61 probe re-run on the frozen round-62 candidate archive: K_HELD=4/14, C04/C09 uncovered, C2 attributed 2/2, d2 2/2, controls 2/2, HOLD_CALIBRATION=4/4, HOLD_REPLAY=10/10, HOLDS_OK=yes, probe SHA matches base, no new verifier files.

# R62FHoldCalibration — hold/calibration re-run on the frozen candidate tree

Seat `RevengerR61-2.R62FHoldCalibration` (falsify, leaf). Lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`. No subagent, no watcher, no repair, no admission, no live/corpus/Git mutation.

**Target.** Frozen candidate revision `d97761952be256d145d298022de03091de91d358` (tree `45c4c5da82aae8ca2e44f6e3ed874a33533f54b9`); claim base `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`. Archive `/fast/scratch/hyaku/revenger-r62/R62FHoldCalibration/archive`, 783 files, file list == `git ls-tree -r d977619…`, tree digest `912442749bbe7dea40b989f25a2342ed58ba6234c2e3a9133395d9a5b82badde`; extraction `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive d97761952be256d145d298022de03091de91d358 | tar -x -C <archive>` (exit 0), `git rev-parse d977619…^{commit}` → same hash.

**Candidates.** C04 `corpus/knowledge/round-62-commonjs-require-name-evidence.md` sha256 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`; C09 `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` sha256 `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`; both `admission-status: candidate`.

**Probe identity (OBSERVATION).** `git rev-parse 5bd4a90…:reports/round-61/measure.py d977619…:reports/round-61/measure.py` → both `bc61ac5b6a558661ec52d47176b5131d57e0432f`; the archive copy's sha256 is `ada7a9c97bba394f6539ce6f158ee81a8c342a42fa861d634933226bdd0b50d2`, identical to the base blob — probe byte-unchanged base→frozen. No new verifier files: `git diff --name-status 5bd4a90… d977619… -- 'corpus/*.py' 'corpus/**/*.py'` → empty; the `verify_*.py` path set (11 paths, incl. `corpus/live/runs/round-34/verify_review.py`) and every `corpus/verify_*.py` blob are identical base→frozen.

**Probe run (OBSERVATION)** — cwd=`/`, `TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FHoldCalibration/tmp`, `probe_exit=0`; command `python3 -B /fast/scratch/hyaku/revenger-r62/R62FHoldCalibration/archive/reports/round-61/measure.py /fast/scratch/hyaku/revenger-r62/R62FHoldCalibration/archive`:

```
K_HELD=4/14 score=2.9
K_ROW C04 status=uncovered
K_ROW C09 status=uncovered
K_HELD_BACKED=4/14
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
HOLD verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
HOLD verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
HOLD verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
HOLD verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
HOLD verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
HOLD verify_named_multi_icon_states.py exit=0 PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
HOLD verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
HOLD verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
HOLD verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
HOLD verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
```

All assigned values exact: K=4/14 (denominator 14 unchanged), C04/C09 `uncovered`, C2 attributed 2/2, d2 2/2, controls 2/2, calibration 4/4, replay 10/10, HOLDS_OK=yes.

**Determinism / isolation (OBSERVATION).** Three runs → byte-identical stdout (`sha256(run2)=sha256(run3)=ad003a463878d7b1aac139ded61d27b6d05465c3dffa37c6309bc2deeb9771f6`, `diff` empty). Probe on the claim-base archive `5bd4a90…` gives output byte-identical to the frozen run (`diff base-run.txt run3.txt` empty) ⇒ neither candidate entry changed any counted hold, control, or calibration value. `TMPDIR` honoured (`tempfile.gettempdir()` → owned scratch) and `/tmp/rev-r61-mut-*` count = 0 after the runs ⇒ no mutant spill outside owned scratch. The 783-file archive sha256 manifest is identical before/after ⇒ the probe wrote nothing into the tree. Live `git status --porcelain` shows only the pre-existing untracked `.ufo/waves/round-62/falsify*` wave files ⇒ no corpus, index, or history mutation.

**Preservation (OBSERVATION).** `.ufo/waves/round-62/preservation/manifest.tsv` (611 rows: G1 live 345, G2 fixtures 98, G3 rejected candidates 2, G4 round-61 waves 161, G5 verifier lesson 1, G6 round-61 reports 4) re-verified against the extracted frozen archive: 0 missing, 0 sha256/size mismatch. `git diff --stat 5bd4a90… d977619… -- corpus/knowledge/commonjs-destructured-require-edges.md corpus/knowledge/evm-saved-interface-candidates.md corpus/lessons/round-61.md corpus/lessons/round-61-verifier-spotcheck.md reports/round-61/` → empty (prior rejected text and round-61 reports byte-preserved). The corpus delta base→frozen is exactly `M corpus/SOURCES.md` (+9/−0, additive; S001, S002, S008, S016, S019, S020, S022, S024, S025, S026, S027 row text verified IDENTICAL) plus `A` the two candidate entries and `A corpus/lessons/round-62.md`. `corpus/README.md` untouched (sha256 `2c8606d3de51014c83f5be1e2b1309a8f42c343a5c2b006cc73ed0ee96e8e23f`); held rows C01/C11/C12/C13 intact; denominator 14.

**Counterexample battery (OBSERVATION — scratch copies, unmodified archived probe).**

| scenario (scratch copy) | K_HELD | K_HELD_BACKED | K_ROW | HOLDS_OK |
|---|---|---|---|---|
| C04 cell → real candidate file, status `held` | 5/14 | 5/14 | C04 held | yes |
| C09 cell → nonexistent stub name, status `held` | 5/14 | **4/14** | C09 held | yes |
| C04+C09 → real candidate files, both `held` | 6/14 | 6/14 | both held | yes |

One real admission would lift K to 5/14 (C1 target met); both would give 6/14 (score 4.3). The Amendment-A1 `K_HELD_BACKED` gate refuses a row naming a nonexistent knowledge file. Sim copies were removed after the run; the live README and corpus were never modified.

**Source registry (OBSERVATION).** `bash scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → `revenger ok /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md`, `census_rc=0`; three W04 advisories (duplicate URL across scopes) for S024 (pre-existing) and the new S028/S029 re-opens — W-codes do not change status and the validator reports `ok`.

**Inference (not directly observed).** (i) The frozen tree is a true "candidate landed, no held flip" state: both entries exist on disk with `admission-status: candidate` while README C04/C09 remain `uncovered`, so K=4/14 is the intended pre-admission baseline, not a C1 falsification. (ii) `K_HELD_BACKED` is existence-only, so a physically present stub with the right name would pass it without passing Q01–Q13 — the already-routed round-61 blind spot, not a new defect; the binding admission condition remains the named per-candidate Q01–Q13 decision, never the probe count. (iii) `HOLD_REPLAY=10/10` counts `corpus/verify_*.py` by non-recursive glob (10 files); `corpus/live/runs/round-34/verify_review.py` sits outside that glob — unchanged probe behaviour and unchanged file set, a scope fact rather than a round-62 regression.

**Not covered by this seat.** Q01–Q13 admission judgements on either candidate entry; the entries' Q11 derivation audit; S028–S031 quote verification; README flips and final integration (other fresh-wave seats / L1). Not executed: no fixture-JS or EVM execution, no REA producer call, no chain/RPC; the only external command was the read-only census validator.

**Residual risk.** (1) Low — `K_HELD_BACKED` remains existence-only, so K alone can never evidence admission; L1 must rely on the named per-candidate Q decisions. (2) Low — two new W04 duplicate-URL advisories (S028/S029), the declared narrower re-opens beside S016/S022; non-fatal, validator reports `ok`. (3) Low — no new verifier file, no changed corpus byte, no lost baseline held row, no denominator change, no Q01–Q13 weakening in the frozen delta.

**VERDICT — HOLDS.** The frozen candidate revision `d97761952be256d145d298022de03091de91d358` preserves every hold the round-62 pre-registration demands: probe byte-identical to base (`ada7a9c97bba394f6539ce6f158ee81a8c342a42fa861d634933226bdd0b50d2`), no new verifier files, K_HELD=K_HELD_BACKED=4/14 with C04/C09 still `uncovered`, C2 controls 2/2, d2 2/2, receipt-command attributed 2/2, HOLD_CALIBRATION 4/4, HOLD_REPLAY 10/10, HOLDS_OK=yes, probe_exit=0, deterministic across three runs, no `/tmp` spill, archive and prior-rejected bytes unchanged. No material finding; no repair needed; no admission asserted by this seat.

Installs: none. No package, tool, or runtime was installed or updated (pre-existing `python3` and `bash` only).
