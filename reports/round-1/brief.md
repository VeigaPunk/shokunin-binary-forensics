# Fleet round-1 — bounded calibration move

Authority: ../MISSION.md, ../AXES.md; canonical shokunin protocol; host task role routing only. Baseline lane commit: 286033c5f2b1683fb538e86e15667709bb49b054. Do not relabel historical imported rounds r1-r60 as this fleet round.

## One claim

The existing named two-image PE saved-record verifier must replay after the corpus moves to a standalone checkout, while still checking the original recorded producer paths, Evidence IDs, fixture digests, complete byte-derived normalized results, receipt command/hash and two forged-claim rejections. Read local fixture bytes from the present corpus; compare historical identities to an independently pinned historical path. Never accept a path by copying it out of the field under test, and never rewrite saved JSON, receipts or binary fixtures. No producer rerun, PE execution, engine install, provider readiness claim or extra feature.

Existing failure: `python3 -B corpus/verify_named_multi_icon_states.py` exits 1, `AssertionError: r55 artifact`. Historical corpus path in r55-r57: `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus`. Local corpus: this checkout's corpus directory. Complete baseline census: reports/round-1/baseline.txt.

## Axis selection and rubric

The imported SCORECARD has three unmeasured rows and no rubric. Restrict active axes to mission coverage + calibration (historical depth retained, retired as wrong-fit for this lane assignment). Initialize bounded, explicitly non-global scoring proxies:
- Coverage: 10 times saved successful producer-record families / seven declared artifact families (native-static, managed, JavaScript, Android, archives, firmware, browser-runtime). Baseline 3/7 = 4.29; presence only, not authentication or current runtime capability.
- Calibration: 10 times runnable existing cross-record PE state ledgers / four existing scripts: verify_icon_states.py, verify_multi_icon_states.py, verify_icon_languages.py, verify_named_multi_icon_states.py. Baseline 1/4 = 2.5. Expected after 2/4 = 5.0. The broader ten-verifier census was 7/10; only this one verifier may change, expected 8/10.
Calibration is therefore lowest. This rubric measures portable saved-ledger repeatability, not overall RE competence, producer authentication, valid-Unicode policy or promotion. Historical r59 malformed-name validity criterion stays halted; this is a newly declared repeatability criterion, not a regrade.

## Roles and ownership

Parent owns integration, scorecard, append-only LOG, corpus admission lesson/index, README, PROVINCE current write path, SHONEN canonicalization, commits, pushes and fleet report. One native OMP task call carries all nine roles; taxonomy selects operator-configured routes, no per-lane model params or config mutation. The heterogeneous single-writer review batch is normal shokunin host delegation, not a UFO uniform-item validator wave (which excludes the required planner role).

All agents are leaves. Do not delegate, launch background jobs, run builds/lint/tests/formatters, perform producer calls, execute fixtures, or commit/push. Parent runs acceptance once after integration. Work only in your named write scope; other lane/domain sources are read-only. Report source locations and limits, not assumed results. Subagents are author-side evidence, not promotion/outside discernment verifiers.

Requested acceptance: ordinary lane-root CLI, unrelated CWD, copied corpus under a path with spaces and non-ASCII, unchanged historical inputs, and rejection of forged historic artifact path/receipt command, second-candidate claim, size match, name location and ancestor location. Direct real CLI execution in isolated copies, no mocks.

## Live round clarification

The inherited seven-family coverage proxy above omits the already-recorded EVM surface (`baseline.txt:33`). Use the corrected fixed eight-family presence proxy: the same seven families plus EVM (`inspect_evm_interface`). Before is 4/8 = 5.0/10; expected after is unchanged. This is a taxonomy-limited saved-record presence measure, not exhaustive domain coverage or capability. Calibration at 1/4 = 2.5/10 remains the lowest proxy. The inherited 3/7 measurement is preserved as originally measured, not presented as the current score.

`dispatch.json` records inherited dispatch intent; `batch-receipt.json` records the actual single native nine-role dispatch in this activation. All L2 assessments are author-side. No independent promotion or outside-discernment verdict follows.
