# round-90 verifier spot-check — revenger (non-author closure)

author: hyaku closure (non-author integrator, @m_zfl)

Closed 2026-11-04 against lane head
`b280719903dee7c3d957da8b1cd7315655511e3d` (= `git ls-remote origin
refs/heads/main`; base `77574c99845ab6662812bd6a88def1e72bf8d71b`). I did not
author this round and did not improve it: every number below is a re-derivation
over committed bytes or a plain probe I ran myself. Lane repo
`/home/vgpnk/Projects/shokunin/revenger-shokunin`; fleet root
`/home/vgpnk/Projects/shokunin`. No `jj` command was run in the lane except
through `scripts/hyaku/jj-lane.sh state` (read-only).

## Step-1 conformance — PASS (two status-neutral defects, below)

- **Report landed by the lane identity, last.** `git -C <fleet> log
  --format='%an <%ae> %H %ad' -- .ufo/reports/round-90/revenger.md` →
  `revenger-shokunin <revenger@shokunin.local> 8e251d43a41d1d0a6f86d4919ca2e863f63f6e4e
  2026-11-04 19:26:08 -0300`. Lane tip `b280719` is dated 19:26:01, so the
  report was written after the last lane commit. `git merge-base --is-ancestor
  8e251d4 refs/remotes/origin/main` → in origin (`f1a5d3e`, fleet HEAD =
  `refs/heads/main` at origin).
- **Substantive report, not a marker.** 12,507 bytes; sections present in
  order: work performed (claims named first), landed changes (each row tied to
  a `LOG.md` entry and a commit), before → after measurements, sources &
  frontier, trend verdicts, `## SHONEN`, round notes. `LOG.md:1261` carries the
  round-90 entry.
- **`SHONEN` heading.** `grep -c '^## SHONEN'` = 1; `grep -cE '^- \[[ x~]\]'`
  = 4, one line per box, all `[~]` with pointers; no `[x]`. `SHONEN.md`
  itself is untouched by the round (not in `git diff --name-status 77574c9
  b280719`).
- **Cited lane commits exist and are ancestors of the branch ref** (never
  `@{u}`; the repo is jj-colocated, HEAD detached). `git merge-base
  --is-ancestor <hash> refs/heads/main` → ancestor for `c7767789` (freeze),
  `abd1394` (landing), `5bdcd5a` (adjudication), `b280719` (wave evidence),
  and the cited base `77574c9`. `git log -1 --format='%an|%s'` on each returns
  the lane's own subject lines.
- **Lane pushed, no uncommitted round work.** `jj-lane.sh state` →
  `branch=main local=b280719… remote=b280719… ahead=0 behind=0 head=detached
  tracked=0 untracked=0`; `git -C <lane> status --porcelain` prints nothing.
- **Prompt carries the template contract.** `.ufo/prompts/revenger-round-90.md`
  (830 lines) carries §1 MISSION/AXES binding, §2 claims 1–3 with distinct
  axes and the lowest-axis clause, §2b frontier step, §3 the L2 floor (≥8
  lanes, one batched call — matches `MISSION.md` §L2 concurrency), §4 the
  report contract with the `SHONEN` heading, and §5 commit-then-push, push
  scope and the L0 channel; §6 is the hyaku addendum. All five child-lane
  items are present (report path, commit-before-report, `SHONEN` heading,
  commit-hash citation rule, write scope).

Status-neutral defects:

1. **Wave-evidence pointers are lane-relative without the repo prefix.** The
   report cites `.ufo/waves/round-90/w1/ExecR90Producer/report.md` and
   `.ufo/waves/round-90/w1-results.json`; those resolve only under
   `revenger-shokunin/`, not under the fleet root where the report lives. A
   reader following the pointer from the report's own directory lands on
   nothing. Resolvable by convention, so a defect, not a marker.
2. **Fleet-root working tree carries other lanes' churn.** `git -C <fleet>
   status --porcelain` shows ` M .scratch/run15-state.json`, ` M
   .ufo/reports/round-84/kama.md` and untracked `.scratch/closure-*-entry.*`
   files plus `after` (24 bytes, 2026-11-03). None names this lane or round;
   the lane's own misroot sweep (`Round notes`) reports the same and leaves
   them alone. Not this lane's debt.

## Per-claim re-check (re-measured, not evidence-verified)

Trees: `git archive <rev> corpus SHONEN.md SCORECARD.md SKILL.md` for C1 and
`git archive <rev> corpus reports` for C2, extracted to a private temp dir;
battery and counter bytes are byte-identical at freeze and tip
(`git rev-parse c7767789:reports/round-90/sm6_battery.py` =
`b280719:…` = `57efe817…`; same for `c2_counter.py` = `ddf6a6bf…`).

### C1 — calibration (SM6 v2): `SM6_MISCLASS` 7/14 → 0/14 — RE-MEASURED, VERIFIES

```
python3 -B reports/round-90/sm6_battery.py --impl /tmp/r90base/corpus/self_assessment_check.py --real /tmp/r90base
  → CASE B10/B11 MISCLASS; R1-real-tree label=0 got=1 MISCLASS; R2-forged-8-of-14 label=1 got=0 MISCLASS
    SM6_MISCLASS=7/14
python3 -B reports/round-90/sm6_battery.py --impl /tmp/r90land/corpus/self_assessment_check2.py --real /tmp/r90land
  → all 14 cases ok; SM6_MISCLASS=0/14
# do-nothing control (kill c): v1 over the landing tree
  → SM6_MISCLASS=7/14
# kill b: v1 vs v2 over the landing tree
  v1: SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=1 SELF_MISMATCH=1
  v2: SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0 SELF_MISMATCH=0
# kill a: python3 -B corpus/self_assessment_check2.py --self-test → SELFTEST OK …, exit 0
```

The 14 hand labels follow the declared truth rule on their face (current side
of the last `N/D` statement on the last `K_HELD_BACKED` line must state
N = held rows AND D = map rows): I re-derived all twelve synthetic labels and
both real-tree labels by hand from the case definitions and they are correct,
so the battery is not fitted to v2's parser. `diff corpus/self_assessment_check.py
corpus/self_assessment_check2.py` touches only the docstring, `sm6()` and the
SM6 self-test legs (44 changed lines) — SM1–SM5 are byte-identical, and the v1
file is byte-unchanged base→tip (`git diff --stat` shows no entry).

**Limits confirmed in the lane's own record and not hidden:** `SM6` reads the
last `K_HELD_BACKED` line and the last `N/D` statement on it, so in the lane's
real SCORECARD row format it reads the evidence-pointer cell rather than the
stated before→after cell (`CriticR90Claims` `c1-realformat-counterexample.log`);
4/11 mutants survive the battery (`MutR90SM6`); 8/21 out-of-battery probe shapes
are false greens (`ReviewerR90C1`). These are recorded as limits in
`SKILL.md`'s registry row and in `corpus/lessons/round-90.md` M-c.

### C2 — coverage (android record): `C2_CONJUNCTS` 1/6 → 6/6, F4 10/11 → 11/11 — RE-MEASURED, DOES NOT VERIFY

```
python3 -B reports/round-90/c2_counter.py --tree <base 77574c9>
  → K1=FAIL F4_COVERAGE=10/11 … C2_CONJUNCTS=0/6   (counter absent at base)
python3 -B reports/round-90/c2_counter.py --tree <freeze c7767789>
  → K1=FAIL 10/11; K2 missing record; K3=pass; K4/K5/K6 FAIL → C2_CONJUNCTS=1/6
python3 -B reports/round-90/c2_counter.py --tree <landing abd1394>
  → K1=pass 11/11; K2=pass ORACLE OK (22/22); K3=pass 0/9; K4=pass NORM_EQ=identical;
    K5=pass 9d665ffb…/214094fb…; K6=pass ev_affae0e…/ev_d4a3433… → C2_CONJUNCTS=6/6
python3 -B reports/round-81/f_probe4.py <base>/corpus   → F4_COVERAGE=10/11 score=9.09
python3 -B reports/round-81/f_probe4.py <landing>/corpus → F4_COVERAGE=11/11 score=10.00
python3 -B reports/round-90/oracle_battery.py --oracle <landing>/corpus/fixtures/apk-r65/oracle_check.py  → 5/9
python3 -B reports/round-90/oracle_battery.py --oracle <landing>/corpus/fixtures/apk-r65/oracle_check2.py → 0/9
```

**The predicate is reachable without the claimed work — I reproduced it.**
From the freeze tree (counter and instruments present, no record) I copied the
r89 rejected record (`reports/round-89/rejected-android-record/inspection.json`)
to `corpus/live/runs/round-90/inspection.json` and to
`reports/round-90/android-run2.json`, replaced each `evidence_id` with a fresh
random `ev_<64 hex>`, wrote a receipt carrying both sha256 values, and ran the
frozen counter:

```
K1=pass ['F4_COVERAGE=11/11 score=10.00']
K2=pass ['ORACLE OK (22/22 checks)']
K3=pass ['ORACLE_MISCLASS=0/9']
K4=pass ['NORM_EQ=identical']
K5=pass ['78baad3d591aa8a3', 'e9ece5710b89207e']
K6=pass ['ev_fe780896d7cb9cc99', 'ev_4d97189809f782ab3']
C2_CONJUNCTS=6/6
```

No producer was run. This is the §9 defect the lane self-ruled (M-b) and the
critic's `ctl-idedit` finding, independently confirmed. The critic's
`ctl-stub` (in-tree instruments replaced by `print` stubs) fails the same way
because `c2_counter.py:140-146` executes the instruments found inside the tree
under test and never compares them with `instrument-pins.log`.

The landed artifact itself is not nothing: `K5` shows the receipt's digests
equal the two run files, the landed `inspection.json` is run1's exact stdout,
and the unclaimed `verify_evidence_id.mjs` (rea's own `parseEvidence`) marks
both landed runs `ID_CONSISTENT` while an id-edited control is rejected. That
is corroboration, not the frozen rule, and it cannot prove provenance
(`computeEvidenceId` is a digest over content; a content-accurate forgery with
a recomputed id passes by design — battery P2). **The claim as frozen does not
verify.** Re-measured here; the lane's own gate evidence (pins, after-run logs)
was read and its numbers agree.

### Unclaimed items I re-ran (context, not claims)

```
python3 -B reports/round-90/source_path_check.py --root <base>/corpus-tree → SOURCE_PATH_DEAD=1
python3 -B reports/round-90/source_path_check.py --root <landing>          → EXCUSED S481 by S486; SOURCE_PATH_DEAD=0
python3 -B reports/round-90/source_path_check.py --selftest               → SOURCE_PATH_SELFTEST=pass
```

r89 D1 is fixed and the machine check is shown able to fail (red at base,
`EXCUSED` at landing). `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md` → **487** at tip vs **482** at base (the report's command
and numbers); S481's row is byte-identical base→tip.

## Per-axis verdicts

| axis | claim | verdict | reason |
|---|---|---|---|
| calibration | C1 | **improved** | The lane's own self-assessment instrument no longer reports a mismatch where the repo state is true: over the real tree `SM6` 1→0 and `SELF_MISMATCH` 1→0, with the frozen battery 7/14 → 0/14 re-derived and the v1 do-nothing control still 7/14. The counted quantity is a mismatch between the lane's self-assessment statement and observed repo state (README map rows), which is calibration's own signal. Recorded caveat: the critic's label dispute stands unresolved — the surface moved is the gate's verdict fidelity, not a corrected SCORECARD/SHONEN entry — and `SM6` reads the pointer cell in the lane's real row format (M-c). Those are limits routed below, not a re-score. |
| coverage | C2 | **unprovable** | `F4_COVERAGE` really moved 10/11 → 11/11 and the record is a real artifact with matching digests, but the round's frozen predicate is met with no producer run (I reproduced a 6/6 control), so the claim "the android family's first admitted current-producer record" cannot be established by its own counter. The lane self-ruled `NOT VERIFIED`; that ruling stands. Corroboration (id consistency) is unclaimed and proves consistency, not provenance. |
| depth, operability, freshness, adjacency | — | **unchanged** | No claim; `SKILL.md` gained four registry rows (additive), `corpus/QUALITY.md` gained Q17, no entry or script was deleted or weakened, and v1 instruments are byte-unchanged. No harm found. |

**No axis is harmed.** `git diff 77574c9 b280719 -- SCORECARD.md` is +25
lines, no deletions; `PROVINCE.md`, `corpus/knowledge/**` filed bytes (one
append-only dated correction at the end of
`corpus/knowledge/2026-10-12-rea-readiness-checklist.md`),
`corpus/self_assessment_check.py`, `corpus/fixtures/apk-r65/oracle_check.py`
and `reports/round-81/f_probe4.py` are byte-unchanged base→tip.

## Discernment spot-check (LEARNING.md — checked from outside)

| item | decision | re-opened source | agree / disagree | reason |
|---|---|---|---|---|
| S483 — Android Developers `<manifest>` element reference | admit, docs tier A | `https://developer.android.com/guide/topics/manifest/manifest-element`, opened 2026-11-04 by me | **agree** | The lesson's quote is verbatim in the page's `description` ("The root element of the AndroidManifest.xml file. It must contain an `<application>` element and specify `xmlns:android` and `package` attributes."), and the page's `attributes` section carries `package`, `android:versionCode`, `android:versionName` exactly as the row's `scope` states. Tier A for root-element/attribute semantics is correct; the row honestly excludes binary AXML and Gradle merge rules. |
| S484 — Python `xml.etree.ElementTree` docs | admit, docs tier A | same docs page as cited (`docs.python.org/3/library/xml.etree.elementtree.html`, quoted in `ScribeR90Sources/receipts/excerpt-etree.md`) | **agree** | The `Parsing XML` note and the `Comment()` note the lesson quotes are the documented skip-comments/PIs/DOCTYPE behaviour, and the row's scope is limited to the default parser. Its own caveat — that an internal DTD subset can still apply ATTLIST defaults — is exactly the trap `ForgeryR90Probe` N03/N04 found, so the row does not overclaim. |
| S487 — Stack Overflow q/2097813 | **reject**, community tier C | `https://api.stackexchange.com/2.3/questions/2097813?site=stackoverflow&filter=withbody`, opened 2026-11-04 by me (HTML answers 403) | **agree** | The body says verbatim "This file appears to be in a binary XML format." — a question about decoding binary AXML. It says nothing about root-element or attribute semantics, and the oracle parses already-decoded manifest text, so the reject and its flip condition (an AXML-decoding oracle leg) are sound. |
| S486 — round-89 rejected record receipt (own-work, `supersedes S481`) | admit, own-work tier A | `reports/round-89/rejected-android-record/receipt.json` in the lane | **agree** | The path resolves, `sha256sum` = `0afe9eea35bfc1b3cb7b82c8bd3a22de0f7cf26c1ec0f449ff7b7b49b6fada1f` (as the row states), and the old S481 path `corpus/live/runs/round-89/receipt.json` is absent — so the supersession is real and the row's own `teaches` discloses the record is a rejected baseline, not an admitted one. |

`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin
revenger` → **exit 0**, 21 W01 + 10 W04 warnings, 0 E, final line
`revenger ok …/corpus/SOURCES.md` — matching the report's round-end receipt
(and the round-start literal receipt, also exit 0).

## Trend verdicts

- **expansion: unchanged.** No `corpus/knowledge/` entry was admitted this
  round: `git diff --name-status 77574c9 b280719` shows one knowledge file
  modified with an append-only correction (0 deletions), not a new entry on
  uncovered ground. Five `SOURCES.md` rows entered (three external docs tier A,
  one own-work, one rejected community) — curation, not expansion (`CORPUS.md`
  rule 4). The F4 record is a live-run artifact whose claim is unverified, and
  no coverage-map row changed. The report's own "narrowly improved" is
  therefore graded unchanged, as it invited.
- **quality: improved.** A weaker row was superseded by a stronger one with a
  machine check shown able to fail: S481's dead anchor → S486 (`supersedes
  S481`), with `source_path_check` red 1 at base and `SOURCE_PATH_DEAD=0` at
  landing, `--selftest` pass; the knowledge entry that carried the same dead
  path got an appended dated correction; r89 D3's un-receipted count now has
  `reports/round-90/d3-sm2-receipt.log`; Q17 is a new criterion grounded in
  the r89 spot-check lesson. No admitted entry failed a re-check.
- **discernment: improved.** This outside spot-check agrees with the gate on
  every sampled decision (three admits, one reject — table above), and the
  round's own gate refused C2 on its own §9 rule instead of admitting a claim
  its counter cannot support (M-b recorded as a mistake, not hidden). Q17 is
  the grounded `QUALITY.md` criterion the r89 disagreement produced. The
  disagreement that remains — C1's axis label — is routed, not suppressed.

## Routed defects for the lane's next round

1. **C2 predicate (from M-b).** Freeze a counter that (i) verifies the landing
   tree's instrument digests against `instrument-pins.log` (or reads the
   instruments from the freeze commit, never from the tree under test) and
   (ii) requires rea's own `parseEvidence` id consistency on both runs, so an
   id-edited copy and a stubbed-instrument tree fail. Attack `oracle_check3.py`
   with a fresh held-out forgery set before freezing it — its 0/40 is fitted.
2. **SM6 v3 (from M-c).** Read the stated before→after cell of the lane's real
   K row (or require the row to state its after-side next to the token), add
   real-format rows to the battery, kill the 4 surviving mutants
   (`MutR90SM6`), and cover the malformed-row / population-drop class
   (`ConnectorR90`).
3. **C1 axis label.** Name the axis by the surface the round changes (§9): the
   move is gate-verdict fidelity. Either declare a calibration sub-axis for
   self-assessment-instrument fidelity, or pair the next move with a corrected
   SCORECARD/SHONEN entry so the counted mismatch is the lane's assessment, not
   the meter.
4. **D4 (census env pin), routed since r89, still open.** Not worked this round
   and re-flagged here.
5. **Report pointer hygiene.** Prefix lane-repo wave-evidence paths with
   `revenger-shokunin/` (or state the root once) so a fleet-root reader can
   resolve them.

## Admission

C1 verifies on its frozen counter and kill rules; C2 does not verify (its
predicate is reachable with no producer run). Under `AXES.md` a round is
admitted only if every claim verifies and no axis is harmed: **not admitted**,
honest stop — the lane self-ruled the same and filed the record as
`NOT VERIFIED` rather than prettifying it. Status `ok`; verdict
`rejected-honest-stop`.
