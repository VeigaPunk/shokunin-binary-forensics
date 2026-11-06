author: hyaku closure (non-author integrator, @m_zfl)

# revenger round 100 — non-author verifier spot-check (closure)

Lane round: revenger r100 (hyaku run 15, attempt 1). Base `0350014d30e91da411ee624025d8d1bb7afc6ccf`,
lane tip `cdb0774b0bbde2797f2e3a1ad660487a7bbccfbf`. Report `.ufo/reports/round-100/revenger.md`
(fleet commit `d389aa7f1532bc1f2f4c92ce9d83e8229275050d`). Dispatched prompt `.ufo/prompts/revenger-round-100.md`
(fleet commit `4bdc8531f6b207ea256864f9392a821e035e5314`).
Driver digest (copied from `.ufo/watchdog.log`):
`2026-11-05T19:38:35-03:00 launch revenger round=100 pgid=1164174 driver=hyaku-inline attempt=1`;
`2026-11-05T22:05:56-03:00 complete revenger round=100; hyaku-inline attempt=1`.

Outcome: **status ok, admitted**. C1 (calibration, r99 fresh holdout v8 12/12 → v9 0/12 accepted,
development set) and C2 (coverage, capability `apk-manifest-cross-decode`, table 4 → 5 rows) both verify
on their frozen predicates and kill rules. No axis harmed. Routed defects in §5 do not bar admission.

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report attribution | `git log --format='%an %H %ci' -- .ufo/reports/round-100/revenger.md` | `revenger-shokunin d389aa7f… 2026-11-05 22:05:32 -0300` | ok — lane identity; after lane tip `cdb0774b` (committed 22:05:08) and before the 22:05:56 completion line |
| prompt committed | same on `.ufo/prompts/revenger-round-100.md` | `revenger-shokunin 4bdc8531… 19:38:33` | ok |
| SHONEN heading | `awk '/^## SHONEN/…' report \| grep -c '^- \['`; `grep -cE '^\s*- \[[ x~]\]' SHONEN.md` | 4 lines, 4 boxes, all `[~]` with pointers | ok |
| cited commits exist + ancestry | `git cat-file -t <h>`; `git merge-base --is-ancestor <h> main` for `0350014d`, `05e854ce`, `173abe91`, `a5e91dd8`, `cdb0774b` | all `commit`, all `anc-ok` | ok |
| pushed, clean | `scripts/hyaku/jj-lane.sh state <lane>` | `branch=main local=cdb0774b… remote=cdb0774b… ahead=0 behind=0 head=detached tracked=0 untracked=0` | ok |
| leftovers | `git -C <lane> status --porcelain` | empty | ok |
| remote | `git ls-remote origin refs/heads/main` | `cdb0774b0bbde2797f2e3a1ad660487a7bbccfbf` | ok |
| prompt contract | read §1–§5 + addendum of the prompt | MISSION/AXES binding (§1), 1–3 claims + lowest-axis/nudge (§2), frontier step (§2b), L2 ≥8 one batch (§3), report path + required sections + SHONEN (§4), commit-then-push, push scope, L0 (§5); write scope, lands-last and landed-hash citation in the addendum (lines 448, 472, 516) | ok |
| deletions in round range | `git diff --numstat 0350014d cdb0774b \| awk '$2!=0'` | none (578 files, additions only) | ok |

Round commits (`git log --format='%h %an %s' 0350014d..main`): `05e854c` claims freeze, `173abe9`
instrument freeze, `a5e91dd` landing, `cdb0774` wave evidence — all `revenger-shokunin`.

## 2. Per-claim re-check

Which claims were re-measured vs evidence-verified: the C2 row count, the SOURCES row count, the
instrument/claims freeze integrity and the APK decode itself were **re-measured** by me; the C1
counter/harness verdicts and the C2 probe/controls are lane-owned instruments, so per PROTOCOL §Gate
standard (Closure consequence) their **committed evidence** was verified and not re-executed.

### C1 — calibration (v9 counter over the r99 fresh holdout): verified

- Freeze integrity (re-measured): `git diff --stat 173abe91 cdb0774b -- reports/round-100/{c1_k_admit_counter9.py,forge_reach9.py,cap_apk_probe.py,controls_c2.sh,census_line_check.py}` → empty;
  `git show cdb0774b:reports/round-100/<f> | sha256sum | cut -c1-8` → `8e2eafc8`, `3acdd3a9`, `b2c9d189`,
  `479f690e`, `c3b754aa` — equal to the freeze commit subject and the report. `git diff --stat 05e854ce cdb0774b -- reports/round-100/claims.md` → empty (claims unedited after freeze).
- Before (evidence): `reports/round-100/controls/c1-do-nothing-v8.log` — 12 vector rows each ending `ACCEPTED`
  (6 `C02-N*`, 6 `C14-N*`), `HOLDOUT99_CONTROL=control-ok` ×2 → **12/12**.
- After (evidence): `reports/round-100/controls/post-freeze/c1-v9-frozen.log` — twelve `R100_VECTOR … refused legs=<one leg>`,
  `R100_ACCEPTED=0/12`, `R100_CONTROL_C02=control-ok`, `R100_CONTROL_C14=control-ok`, `R100_STUB_SELFTEST=ok`,
  `R100_VERDICT=met`, `# rc=0` → **0/12**. Matches the report.
- No-regression conjuncts (evidence): `noreg1-selftest-v9.log` `SELFTEST_C1V9=OK legs=128`, rc 0;
  `noreg2-forge8-v9.log` `C2_ACCEPTED=0/12`, `C2_STUB_SELFTEST=ok`, `C2_VERDICT=met`, rc 0;
  `noreg3-c14r99-freeze-archive.log` `C1_K_HELD_BACKED=14/15`, `C1_VERDICT=pass`, rc 0.
- rc/verdict agreement (answers CriticR100 A1, evidence): `c1-v9-vector-rc.log` — 12 × `rc=1 C1_VERDICT=fail`,
  2 × `rc=0 C1_VERDICT=pass` (controls). The harness gap stands as a routed item; the measured 0/12 is not
  affected.
- Generalization (evidence, reported not scored): `CriticR100/receipts/logs/holdout100-v{8,9}-c{02,14}.log` →
  v8 `accepted=4/4` + `3/4`, v9 `accepted=4/4` + `3/4`, all `control-ok` → 7/8 both. Pre-registered as a
  development-set claim (`claims.md` §C1 disclosure), so it does not falsify C1; it bounds it.
- Pre-freeze ruling on `C1_DERIV_RERUN` (re-measured): `git show 1b76b4d:corpus/knowledge/round-98-rea-host-readiness.md | grep -ci verbatim` → 0;
  `git show 0350014d:… | sed -n 66p` → "command's stdout verbatim, one code span per stdout line…". The
  conditional leg is grounded in the entries as stated; the declaration-strip evasion remains open (routed).

### C2 — coverage, capability `apk-manifest-cross-decode`: verified

- Row count (re-measured): the claim's `awk … SCORECARD.md | wc -l` over `git show <rev>:SCORECARD.md` →
  **4** at `0350014d`, **5** at `a5e91dd8`, 5 at `cdb0774b`. The new row cites S508 and S509 (kill-rule
  citation leg satisfied).
- Probe (evidence): `post-freeze/c2-probe-landing.log` and `c2-probe-freeze.log` — `CAP_FIXTURE_SHA=pass`,
  androguard 4.1.4 / apktool 3.0.3 version lines, `CAP_ANDROGUARD=pass`, `CAP_APKTOOL=pass`,
  `CAP_TAMPER_DETECTED=pass`, `CAP_APK_VERDICT=pass`, rc 0.
- Controls (evidence): `post-freeze/c2-controls.log` `C2_CTRL_STUB=refused`, `C2_CTRL_FLIP=refused`,
  `C2_CONTROLS=control-ok`, rc 0; `c2-controls-detail/` flip run prints `CAP_FIXTURE_SHA=fail` (so control
  (iii) holds by observation; the script does not enforce it — routed). Do-nothing:
  `controls/c2-base-capability-rows.log` `C2_DO_NOTHING rows=4 probe=absent verdict=fail`.
- Independent decode (re-measured; plain run of the two installed decoders in a `/tmp` scratch cwd,
  not the lane's probe): `androguard axml corpus/fixtures/apk-r65/fixture.apk` →
  `package="com.example.r65" ns0:versionCode="1" ns0:versionName="1.0"`; `apktool d -s -f -o <scratch> fixture.apk`
  rc 0 → `AndroidManifest.xml` `package="com.example.r65" n0:versionCode="1" n0:versionName="1.0"`, `apktool.yml`
  `version: 3.0.3`; `jq -c .axml_declared.strings truth.json` → `[…,"com.example.r65",…,"1","1.0"]`. Both
  real decoders agree with truth, so the capability runs independently of the probe — this answers the
  digest-keyed PATH-shim attack (CriticR100 A2 / ReviewerCapR100 attack 3) for the claim, while the probe's
  own blindness to it stays a routed instrument defect. `git diff --stat 0350014d cdb0774b -- corpus/fixtures/apk-r65` → empty.
- M23: `claims.md:65-67` says "the row and the probe cite" S508/S509; the frozen probe cites neither.
  The frozen predicate and kill rule (`claims.md:85-87, 100-101`) bind only the row, which cites both, so
  C2 verifies; the half-unmet surface sentence is a disclosed conformance defect (routed).

### No-harm sweep

`git diff 0350014d cdb0774b -- SCORECARD.md` → additions only (one capability row + the `## Round 100`
section; no criterion row edited). `git diff --stat 0350014d cdb0774b -- corpus/README.md PROVINCE.md corpus/QUALITY.md SHONEN.md corpus/knowledge`
→ empty; only `SCORECARD.md` (+29) and `SKILL.md` (+24, four registry rows) among governed files. K stays
14/15.

## 3. Per-axis verdicts

| axis | verdict | reason |
|---|---|---|
| coverage | improved | capability table 4 → 5, probe pass, independent decoder re-run agrees with truth |
| calibration | improved | v9 refuses 12/12 routed r99 classes (development set), controls ok, three no-regression conjuncts green; fresh r100 holdout shows no generalization (7/8 both) |
| depth | unchanged | no knowledge entry added or changed |
| freshness | unchanged | no entry re-verified; no `verified-at` moved |
| operability | unchanged | four SKILL registry rows describe the round's own instruments only |
| adjacency | unchanged | PROVINCE byte-unchanged |

## 4. Discernment spot-check (LEARNING.md §Discernment is checked from outside)

Sampled from `corpus/lessons/round-100.md` `## Gate`; sources re-opened live on 2026-11-05 (UTC 2026-11-06).

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S508 androguard `axml` docs | admit (tier A, `mined`) | `curl -sSL https://androguard.readthedocs.io/en/latest/tools/androaxml.html` → 200, 8751 B, sha256 `6507e7607f8c…`; pinned RST `…/eef97351/docs/tools/androaxml.rst` → 200, 205 B, `a091672b7cb4…`; `grep -c -F 'Parse the AndroidManifest.xml from an APK and show/save the XML file.'` → 1 in each | agree | bytes identical to the receipts; 11-word quote (≤25) located; scope limited to the CLI's stated function; `latest`-vs-4.1.4 caveat recorded honestly |
| S509 Apktool wiki intro | admit (tier A, `mined`) | `https://apktool.org/wiki/the-basics/intro` → 200, 23480 B, `7e1c418b4572…`; mdx source → 200, 1626 B, `f640bbffc535…`; `grep -c -F 'I: Decoding AndroidManifest.xml with resources'` → 1 in each | agree | bytes identical; 5-word quote located; scope does not over-claim `-s` behaviour |
| `https://apktool.org/documentation` as anchor | reject (331-byte meta-refresh stub; wiki used instead) | → 200, 331 B, `42e19905d983…`, `http-equiv="refresh" content="0; url=/wiki/the-basics/intro"` | agree | a redirect stub carries no quotable content |
| an `apktool d -s` documentation quote | reject (no page located; `-s` kept observation-only) | `https://apktool.org/wiki/the-basics/cli` → 404; `https://apktool.org/docs/cli` → 404 | agree | the probed pages do not exist; declining a quote rather than inventing one is the right call (sweep is narrow — three URLs) |
| unconditional `C1_DERIV_RERUN` (pre-freeze instrument decision) | reject in favour of the conditional leg | `git show 1b76b4d:…/round-98-rea-host-readiness.md \| grep -ci verbatim` → 0; `0350014d` line 66 declares the rule | agree | the leg's ground ("under the entry's cell rule") exists only where declared; evasion routed |

`corpus/SOURCES.md` new rows re-opened: S508 and S509 (above); both quotes ≤25 words and located.
Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
→ rc 0, 21 × W01, 13 × W04, 0 E-codes, no finding names S508/S509 — equal to the report's round-end line.
Row count `grep -cE '^ {0,3}\| S[0-9]{3,} ' corpus/SOURCES.md` → 507 at `0350014d`, 509 at `a5e91dd8`.

## 5. Trend verdicts

- **expansion: improved** — a capability admitted to `SCORECARD.md` (LEARNING.md expansion observable) that
  runs on this host with the real decoders (re-run above), on two tier-A sources opened and mined this round.
- **quality: unchanged** — no knowledge entry added, re-verified or superseded.
- **discernment: improved** — the non-author spot-check agrees with the gate on both admits and all three
  sampled rejects; the counter's new legs refuse the routed classes with rc-consistent verdicts. Bounded:
  the fresh r100 holdout (7/8 accepted by v8 and v9) shows the gain is development-set only.

## 6. Routed defects (lane fixes next round, r101)

1. **Search log missing (CORPUS.md §SOURCES.md rule 5).** ScoutSourcesR100 opened 12 bodies plus 7 404
   probes (`.ufo/waves/round-100/w1/ScoutSourcesR100/fetch-receipts.md`); `git diff 0350014d cdb0774b -- corpus/SOURCES.md`
   adds only S508/S509 and no search-log line (identified/screened/included/excluded, exclusion reasons).
   The lesson `## Gate` also carries no explicit rejected-candidates list; the rejects above had to be read out
   of prose. Add the r100 search-log line and a rejects list.
2. **C2 probe blind to a digest-keyed PATH shim** (CriticR100 A2, ReviewerCapR100 attack 3): randomize the
   tamper value per run and add a second tampered attribute; check decoder identity.
3. **M23:** the frozen probe does not cite S508/S509 although `claims.md:65-67` says it does — next probe
   revision cites them.
4. **`controls_c2.sh` does not enforce `CAP_FIXTURE_SHA=fail`** on the flip (claims §C2(iii)); make it a
   script assertion; add MutationR100's surviving probe mutants (compare-only-package, skip-fixture-sha,
   swallow-decoder-failure) as controls.
5. **forge_reach9 reads verdict lines, not rc** (CriticR100 A1): require rc/verdict agreement in the harness.
6. **C1 generalization:** CriticR100's seven accepted fresh classes as v10 legs, scored on a new holdout; the
   `C1_DERIV_RERUN` declaration-strip evasion.
7. Carried from r99 and still open: C14 Q13 rationale; C02 no-harm rule (M19); `d-host` survivor; M4
   `claude-red-re-bridge.md`; producer-attribution census; L0 assimilation (`revenger | round-91`).

## 7. Operator notes

SHONEN: all four boxes are `[~]`. Boxes 2 (end-to-end task: this closure independently re-ran both decoders
against the fixture truth) and 4 (PROVINCE byte-unchanged across the round) look checkable by a non-author
now; boxes 1 and 3 need a dedicated SKILL/instruction review. Promotion is operator-owned; nothing here
writes `[x]`.
