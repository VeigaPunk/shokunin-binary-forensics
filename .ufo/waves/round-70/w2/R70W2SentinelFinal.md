# R70W2SentinelFinal — final scope & safety review of landed round-70 bytes

**Verdict: CONTAINED** — every changed path is inside the lane; PROVINCE.md identical at base and landed; ADJ-06 reported-not-absorbed (entry fence + SCORECARD row); wave-1 F1 command confinement is closed on these bytes; no network at recheck time in any shipped script; no fixture bytes executed; no writes outside temp dirs (verified by extraction find-hash before/after all runs); no credential material. Verdict formed from the landed bytes (17ee7f87ea8ee72a427af0fd8e7586d09bad99cd) and my own runs; wave-1 reports were not consulted as a source (only encountered as diff hunks in the scope scan).

## Scope: changed paths

- `git diff --stat 3f5edbc… 17ee7f8…` → 91 files, +24615 −19. `git diff --name-status` → all 91 paths inside the lane repo; none absolute, none contain `..` (awk on field 2: no match).
- Non-`.ufo` changed paths: SCORECARD.md, SHONEN.md, SKILL.md, considerthese/2026-10-25.md, corpus/README.md, corpus/SOURCES.md, corpus/check_embedded_outputs.py, corpus/derive_axml_anchors_r68.py, corpus/embedded_output_pins.json, corpus/fixtures/apk-r65/entry_checks.py, corpus/knowledge/round-70-apk-axml-byte-evidence.md, corpus/lint_entry.py, corpus/self_assessment_check.py, corpus/snapshots/{APPNOTE.TXT,dex-format.html,rea-android-applications.md}, reports/round-70/{measure.py, measure-a1.py, claims.md, claims-amendment-A1.md, build-controls.py, build-controls-a1.py, before-treated-tools-on-base.log, measure-before.log, controls/*.log (11)}.
- Worktree HEAD = 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd; `git diff 17ee7f8 -- PROVINCE.md` empty ⇒ working tree clean for tracked files (earlier sha256sum-vs-rev-parse difference was algorithm mismatch: blob id vs sha256, not content).

## PROVINCE.md refusals intact

- `git rev-parse 3f5edbc…:PROVINCE.md` = `797f67fe7ae3cc9e94782cf131af70bedc3391ed`; `git rev-parse 17ee7f8…:PROVINCE.md` = same. No change between base and landed.

## ADJ-06 not absorbed

- Landed entry `corpus/knowledge/round-70-apk-axml-byte-evidence.md:292`: "The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S049 only; this lane ran no provider and makes no readiness claim (Q05 fence). The kaidoku/revenger ADJ-06 overlap (fleet `.ufo/l0-questions.md:42`, open) stays reported, not absorbed: the kaidoku lane's APK content-graph inventory and Android decode axis (`kaidoku-shokunin/corpus/README.md:27` and `:29`) are not restated, and this entry claims none of that surface." Only kaidoku mention is the fence. SCORECARD.md round-70 row keeps ADJ-06 **OPEN** ("reported-not-absorbed in r67-r69 scorecard rows").

## Wave-1 F1 (command confinement) closed on these bytes

- `corpus/check_embedded_outputs.py` `confined()`/`inside()`/`run_cmd()` (lines 84–112): argv[0] must be `python3`/`python`/`sys.executable`; script argument must be relative, inside cwd, resolve within root, and not a symlink; `-c`/`-m`/absolute/`..`/symlink all rejected.
- Self-test asserts each refusal: `not confined(["python3","-c","print(1)"], tmp)`, `not confined(["python3","-B","-m","json.tool"], tmp)`, `not confined(["python3","-B","/etc/passwd.py"], tmp)`, `not confined(["python3","-B","../x.py"], tmp)`, `not confined(["python3","-B","link.py"], tmp)` (symlink) — all passed (`GATE_SELFTEST=exit 0`).
- `run_cmd` executes only `[sys.executable, "-B", *argv[1:]]` (no shell), cwd=tree root, timeout=120.

## No network at recheck time in any shipped script

- grep for `socket|urllib|http|requests|urlopen|curl|wget|ftp|smtp|telnet|nc|netcat|/dev/tcp|ssl.|aiohttp|httpx` over: `corpus/check_embedded_outputs.py`, `corpus/lint_entry.py`, `corpus/self_assessment_check.py`, `corpus/fixtures/apk-r65/entry_checks.py`, `corpus/derive_axml_anchors_r68.py`, `reports/round-70/measure.py`, `reports/round-70/measure-a1.py`, `reports/round-70/build-controls.py`, `reports/round-70/build-controls-a1.py` → no matches. Only occurrences are URL strings in data/template text, never executed: entry source-header rows (S038/S049/S048/S032/S034), `build-entry.py` TEMPLATE (lines 46–50), `build-w1-spec.py` spec text, and `corpus/fixtures/apk-r65/generator.py:39` `http://schemas.android.com/apk/res/android` (XML namespace constant; generator.py is never re-run by the entry — entry line: "this entry does not re-run `generator.py`").

## No execution of fixture bytes

- `readout.py` reads `fixture.apk`/`truth.json` via `struct`/`json` only (docstring: "Reads only the fixture's own bytes with struct; no producer is called"). `entry_checks.py` subprocesses only `readout.py` (lines 125/222/274). No `exec(`/`eval(`/`importlib`/`marshal`/`pickle`/`compile(` in any shipped script. Entry scope header: "No archive member is extracted or executed, nothing is fetched and no producer is called at recheck time".

## No writes outside temp dirs (verified operationally)

- Ran in a `git archive 17ee7f8` extraction (`/tmp/revenger-r70-R70W2SentinelFinal-YYY8`): gate `--self-test`, gate `--entry` (24 blocks), lint `--self-test`, lint `--entry`, selfchk `--self-test`, selfchk `--root`, derive_r68, and the full frozen counter `measure.py` on the extraction.
- `find -printf '%p %s %T@\n' | sort | sha256sum` before = `903689507256940964696a248e35a6fb25cf504e23abd601b6a4f69e56017bac`, after = identical. No file created/changed/touched in the tree.
- Code-level: gate writes only inside its `--self-test` `TemporaryDirectory` (lines 188–237); lint/selfchk write nothing (subprocess only for read-only `git cat-file -e`); measure.py/measure-a1.py build fixture/mutant trees inside `tempfile.mkdtemp` and `shutil.rmtree` them; measure-a1's `git -C {LANE} archive … | tar -x -C {dest}` writes into a temp `dest` (read-only git, fixed commit, no user input).

## No credential material

- grep `password|passwd|secret|token|api_key|BEGIN …PRIVATE KEY|aws_|ghp_|sk-[A-Za-z0-9]{10,}|credential|op://|session` over all 91 changed files: matches are vocabulary in public spec text (APPNOTE.TXT §5.2/§5.4 "password"/"Tokenizing", lines 127/280/863/2183/2609), SKILL.md rules text (line 123: "no credential material, session/private URLs or `op://` references"), and SCORECARD "README_TOKEN_LEGEND_MISMATCH" diagnostics (legend tokens, not secrets). Entry itself: 0 `op://`, no private/session URLs.

## Operability (all runs green in extraction)

| run | result |
|---|---|
| `check_embedded_outputs.py --self-test` | exit 0, SELFTEST OK |
| `lint_entry.py --self-test` | exit 0 (clean 0; four planted defects each scored exactly their class) |
| `self_assessment_check.py --self-test` | exit 0 (clean 0; six planted defects scored exactly; fourteen tightened probes) |
| `derive_axml_anchors_r68.py` | exit 0; 17 lines; line 1 = `sha256 56b88bc4… ResourceTypes.h` (snapshot-digest line) |
| gate `--entry` (tree root) | `checked_blocks=24 problems=0` exit 0 |
| lint `--entry` | `LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0` exit 0 |
| `self_assessment_check.py --root --lane` | SM1–SM6 all 0, `SELF_MISMATCH=0` exit 0 |
| `measure.py` on extraction | exit 0: `C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes`; `C1_LINT=… exit=0`; `HOLDS_C2_V5=yes` (SELF_MISMATCH=0, SELF_CLEAN_FIXTURE=0, SELF_MUTANTS_KILLED=6/6, SHONEN_BOX_COUNT=4, README_ROWS=14); `HOLDS_C3_V1=yes` (EMB_R68=17/0, EMB_R65=15/1, EMB_R67=16/0, EMB_R69=17/0, EMB_PINNED_SCRIPT_IS_S046=yes, EMB_R68/R65_BYTES_UNCHANGED=yes, EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1); `HOLD_REPLAY=10/10`, `GATE_SELFTEST=exit 0`, `F_COVERAGE=5/8`, `FRESH_ROWS=18/18`, `HOLDS_OK_V7=yes`. `HOLDS_C1_V5=no` with `C05_STATUS=uncovered`, `V5_ADMITTED_MARKED=no` — correct pre-admission state (candidate, README unflipped; admission awaits wave-2 Q decisions). |

## Pins (C3) verified

- `corpus/embedded_output_pins.json`: round-68 entry's `corpus/derive_axml_anchors.py` → `use: corpus/derive_axml_anchors_r68.py`, sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`.
- `sha256sum corpus/derive_axml_anchors_r68.py` = `bce497d6…` (match). r68 vs current `derive_axml_anchors.py` differ (round-69 extension: RES_XML_FIRST_CHUNK_TYPE, enum-block bounds, `import re`); base 3f5edbc derive vs r68 = 63 diff lines — r68 is a genuine historical revision.
- A1_C3 pin rule enforced in gate `apply_pin()` (lines 126–146): dig mismatch → `pinned historical script digest mismatch` (marker exits non-zero); pin's `use` confined; entry text must name the digest. r68 entry names the digest (grep count = 1).
- Registered C7 line `problems += drift(lines, stdout_set, lineno)` present exactly once, `check_embedded_outputs.py:178`.

## Tooling

No tools installed (no pacman package, no uv/npx). Used existing `python3` and read-only `git` (cat-file/archive/show/diff). Record: none.

## Notes

- My verdict was formed from the landed bytes and my own runs; the wave-1 evidence files appear in the diff because the wave-1 integration commit added them, but they were not consulted as decision inputs (only the A1 amendment and the claims contract, which are frozen and were read first).
- A1_C1 mechanical labels: `A1_C1_DETAIL` logic (distinct commands ≥17, readout lines 15/15 verbatim, ≥5 tier-A source rows) is satisfied on these bytes (24 distinct commands; readout prints 15 lines; entry has 7 `source: S###` rows) — noted for the C1 gate seats, not a sentinel verdict.
