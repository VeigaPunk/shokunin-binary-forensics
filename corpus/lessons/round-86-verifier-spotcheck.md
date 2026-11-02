author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

# revenger round 86 — non-author verifier spotcheck (closure)

Closed at 2026-11-02T14:35Z against lane tip `a29381623cbcdffea9fd9cc4331868bf5e3406f3`
(branch `main`, pushed). Round shape: completing session after attempt 1 died post-landing
(freeze `2311400` + landing `25041d9` landed; receipts/scorecard/log/lesson were worktree-only
residue). Attempt 2 re-derived every after-run receipt from the committed blobs before landing
anything (adjudication `7254587`, receipt completion `4d8716b`, lesson completion `a293816`).
This file verifies that shape; it is a non-author artifact and is NOT committed by the lane.

## 1. Method

All checks are index-free git over committed bytes (`rev-parse`, `cat-file`, `ls-tree`,
`diff-tree`, `merge-base --is-ancestor`, `show`, `log`, `ls-remote`) plus read-only script runs.
No mutating git command touched the lane repo or the fleet root. The C1 sweep re-runs needed a
git repo at the measured tree (`ls-tree HEAD`), so each measured tree was reproduced as
`git clone --shared --no-checkout` of the lane repo into a fresh scratch dir, overlaid with
`git archive <sha> | tar -x` (so worktree bytes = committed bytes exactly), then
`git update-ref HEAD <sha>` — the same landing-state-git-repo construction the lane's own
receipt-completion commit discloses. Scratch-side only; the scratch was deleted after closure.
The sweep scripts were extracted from the committed blobs (`git show <sha>:reports/round-86/orphan_sweep7.py`)
and their sha256 verified against the frozen pins before any run.

## 2. Step-1 conformance — all pass

| check | command (abridged) | observed |
|---|---|---|
| report committed by lane identity | `git log --format='%an <%ae> %H %cI' -1 -- .ufo/reports/round-86/revenger.md` (fleet repo) | `revenger-shokunin <revenger@shokunin.local> a49b10650da4904283c3fe375909313dd1872f3e 2026-11-02T05:48:33-08:00` |
| `SHONEN` heading | read report | `## SHONEN` present, four `[~]` lines, each with a resolvable pointer; no `[x]` written by the author |
| cited hashes exist + ancestry | `git merge-base --is-ancestor <h> refs/heads/main` for 2311400 / 25041d9 / 7254587 / 4d8716b / a293816 / d7fd9d93c522 | all ANCESTOR-OK |
| push parity | `ls-remote origin refs/heads/main` vs `rev-parse refs/heads/main` | both `a29381623cbcdffea9fd9cc4331868bf5e3406f3` |
| cited work in range | `git log d7fd9d93c522..a293816` | exactly the five round-86 commits, all authored `revenger-shokunin` |
| dispatch/complete digest | grep watchdog log | `2026-11-02T03:05:42-08:00 launch revenger round=86 base=d7fd9d93c522 (zcode run14)` / `2026-11-02T05:48:33-08:00 complete revenger round=86 head=a29381623cbc pushed=True` — matches the closure digest verbatim |
| real report, not a marker | read report | substantive: work performed, evidence pointers, landed changes tied to LOG entries, measurements, frontier, trends, SHONEN |

## 3. Attempt-1 landed bytes respected — pass (dispatch note item 1)

- Freeze `2311400` files: `reports/round-86/{claims.md, freshstart-probes.log, orphan_sweep7.py,
  skill-red-greps.log, sweep7-red-prelanding.log, sweep7-selftest-red.log,
  sweep7-v6-blind-prelanding.log}`, `.ufo/waves/round-86/census-round-start-{sanctioned,literal}.log`,
  `reports/round-85/corrections.md` (append-only: 0 removed lines in range).
- Landing `25041d9` files: `corpus/SOURCES.md`, `SKILL.md`, `reports/round-86/usedby-fix-log.txt`.
- `git diff-tree -r --name-only 2311400 a293816 -- <all freeze paths>` → empty;
  `git diff-tree -r --name-only 25041d9 a293816 -- <all landing paths>` → empty. Nothing re-written;
  blob ids identical at landing commits and at the final tip.
- Instrument pins re-hashed from the committed blobs: v7 sha256
  `f955cd7d634f8aa4f61c1734195dd32c959e8d5f347f5cd320484360c1948618` at freeze AND tip (identical);
  v6 `b2db45b07bc86ffd501971582730497e2d5ddc83e685665c200fc24b3c7f12b7` at base AND tip (identical);
  `sed -n 165p` of the landing v7 blob → `USED_BY_ACCOUNTING = True` (the mutant recipe's exact target line).

## 4. C1 re-run (calibration) — pass, re-measured by this verifier (dispatch note item 2)

Command per leg: `PYTHONUTF8=1 python -I -B <committed v7 blob> --lane <extracted tree> --fleet <fleet root> --format summary`.

| leg | committed receipt says | this verifier observed | match |
|---|---|---|---|
| red over base `d7fd9d9` tree | `SWEEP_SRC registry=disk rows=451 sites=499 cited=493 mismatch=6 absent=0` + 6 mismatch rows, basis `26/52/1`, exit 0 | `SWEEP_SRC registry=disk rows=451 sites=499 cited=493 mismatch=6 absent=0` + the same six rows (S448→reports/round-77/claims.md, S449→SKILL.md, S450→reports/round-78/province_probe3.sh, S451→reports/round-79/claims.md, S453→reports/round-79/claims.md, S456→reports/round-80/orphan-before.log), exit 0 | exact on the claim line |
| green over adjudication tip `7254587` | `SWEEP_SRC registry=disk rows=452 sites=495 cited=495 mismatch=0 absent=0`, basis `26/53/1`, exit 0 | `SWEEP_SRC registry=disk rows=452 sites=495 cited=495 mismatch=0 absent=0`, lessons=53, exit 0 | exact on the claim line |
| v6 blind at base | `grep -c SWEEP_SRC` → 0, exit 0 | 0, exit 0 | exact |
| v6 blind at adjud tip | `grep -c SWEEP_SRC` → 0 | 0 | exact |
| standing re-run at final tip `a293816` | exit 0, `mismatch=0 absent=0`, `LANDABLE_ORPHANS=0` | `SWEEP_SRC registry=disk rows=452 sites=495 cited=495 mismatch=0 absent=0`, `LANDABLE_ORPHANS=0`, exit 0 | exact on the claim line |

Disclosed basis drift, explained and claim-neutral: my runs print `fleet-reports=27` where the
receipts print 26, because `.ufo/reports/round-86/revenger.md` was committed to the fleet root at
13:48:33Z, AFTER the lane's last receipt-bearing push (13:43:42Z) — the receipts honestly name the
26-report basis they ran on. The same +1 fleet-report also shifts the non-claim gating counts
(e.g. red ABSENT 77 vs receipt 62; green CITED=1067 COMMITTED=1003 ABSENT=64 vs receipt
1064/1001/63): every shifted token traces to citations introduced by the fleet-side round-86
report over trees where those paths are not lane-committed. The claim quantities (SWEEP_SRC
mismatch/absent and LANDABLE_ORPHANS) reproduce exactly.

Independent drift cross-checks re-opened by this verifier: base `SKILL.md` greps `S449` → 0 while
base `reports/round-78/claims.md` greps `S449` → 1 (the drift direction confirmed); landing
S448 used-by cell = `corpus/lessons/round-77.md` (drop applied per `usedby-fix-log.txt`); landing
S449 cell = `reports/round-78/claims.md` (the citing pointer kept, so `mined` stays valid).

## 5. C2 re-run (depth) — pass, re-measured (dispatch note item 3)

`grep` over `git show` blobs, frozen commands from `claims.md`:

| command | base `d7fd9d9` | landing `25041d9` | tip `a293816` |
|---|---|---|---|
| `grep -cE '^\| M[0-9]+ \|' SKILL.md` | 9 | 10 | 10 |
| `grep -c 'cite-back' SKILL.md` | 0 | 2 | 2 |
| `grep -c 'used-by' SKILL.md` | 4 | 8 | 8 |

9/0/4 → 10/2/8 as claimed. Committed receipts (`skill-red-greps.log`, `skill-green-greps.log`)
carry the same values including the base re-derivation.

## 6. Gate/selftest evidence — verified from committed receipts (not executed, per protocol) (dispatch note item 4)

- `sweep7-selftest-after.log`: 21 v6 legs + 4 SRC legs (SRC_PLACEHOLDER / SRC_CITEBACK_VECTORS /
  SRC_ABSENT_VECTOR / SRC_MUTANT_FLAGGED), all `ok`, final `SWEEP_SELFTEST=pass`, `SELFTEST_EXIT=0`,
  run from the committed blob (sha pin matches). The freeze-time `sweep7-selftest-red.log` carries
  the same suite red-side with the mutant tail `selftest: used-by accounting drifted (used-by class)`.
- `sweep7-mutant-kill-after.log`: recipe `sed 's/^USED_BY_ACCOUNTING = True$/USED_BY_ACCOUNTING = False/'`,
  mutated copy sha256 `0bfe69a08d3d0491e55a6af5e2fa08a9438b732ea1a8eb7579f61b73db3028c3` (matches the
  claims.md pin), diff exactly `165c165`, `MUTANT_EXIT=1` attributed `selftest: used-by accounting
  drifted (used-by class)`. This verifier confirmed line 165 of the committed blob is the switch.
- Holds over the `25041d9` landing archive (dispatch note item 5), `holds-over-landing-archive.log`:
  `M_RECORDED=3/3 score=10.00` exit 0; `F4_COVERAGE=10/11 score=9.09` exit 0; `A1V2_RECORDED=5/5
  score=10.00` exit 0; `A1_RECORDED=3/3 score=10.00` exit 0; probe blob pins named (mg
  `1840c30c…`, f4 `4d871971…`, ag2 `f9772ab1…`). K held-rows 8/15 is the carried r72/r74 constant
  (`K_HELD_BACKED=8/15`, 5.3) — operator-blocked route re-checked (L0 probe 3), not attempted. Agree.
- Freshness 18/18: re-measured by this verifier over the landing blobs —
  `git show 25041d9:corpus/knowledge/seed.md | grep -cE '^\| [FK][0-9]+ .*\| (holds|STALE)'` → 12;
  same over `2026-10-12-rea-readiness-checklist.md` → 6; total 18. Also independently printed in
  `noharm-diff.txt` (FRESH_ROWS 12 + 6).

## 7. No-harm and separability — verified

- `noharm-diff.txt`: freeze..landing = 3 files, 29 insertions (4+7+18), 6 deletions; protected
  paths empty; SKILL.md hunks additions-only. Range file list re-derived by this verifier
  (`diff-tree -r --name-status d7fd9d93c522 a293816`): exactly the 25 expected round files — no
  PROVINCE.md, no corpus/knowledge/, no QUALITY.md, no fixtures, no standing verifier.
- `PROVINCE.md`: diff-tree over the range → empty (byte-unchanged), as claimed.
- SCORECARD append-only: 0 removed lines in range; the round-86 section records calibration
  improved (C1), depth improved (C2), coverage unchanged-hold, freshness unchanged-hold.
- Separability receipts read and consistent: `c1-only.log` (SWEEP_SRC mismatch=0 with the disclosed
  S472→lesson absent; SKILL greps at red 9/0) and `c2-only.log` (greps 10/2 with v7 absent; base
  S449 drift intact). The disclosed S472→lesson absent is correct-by-construction at the landing
  (the lesson is adjudication content); at the adjudication tip it is cited, so absent=0.
- LOG.md append-only (0 removed lines); round-86 block carries all eight entries the report names
  (Carry-in first / Claims / Fresh-start §7 / Holds + honesty / Mistakes mined / Trends /
  Adjudication completion (attempt 2) / Lesson completion).
- SOURCES census commands re-run over the landing blob: rows 471 → 472; malformed 0; duplicate
  ids none; S472 appended directly after S471 inside the Registry.

## 8. Mistakes mined — eight real (dispatch note item 6)

`corpus/lessons/round-86.md` `## Mistakes` holds exactly 8 rows (6 attempt-1 + 2 completing-session),
each with class · evidence pointer · captured-by · fix. Spot-verified:

1. receipt-format assertion — corroborated by the committed `sweep7-real-after.log` itself: its
   section 2 header states the corrected form ("the 62→63 ABSENT movement; absent never gates")
   and section 4 records the post-write full-format classification with the exact printed row.
2. invalid sweep construction — corroborated by the same receipt's provenance note
   ("SWEEP_ERROR git ls-tree failed … invalid construction, discarded, disclosed"; rebuilt as a
   landing-state git repo). This verifier independently hit the same requirement (sweep needs
   `ls-tree HEAD`) and confirms the disclosed fix is the right one.
3. count-from-intent (used-by 7 drafted vs 8 grepped) — this verifier's own grep of the landing
   blob prints 8.
4. mutant line-165 pin — verified byte-exact above.
The remaining four (em-dash placeholder parse, probe parse desync, frozen-command vs first
wording, stale-index diff garbage, heredoc truncation — note: five of the six attempt-1 rows are
process recurrences) carry concrete evidence pointers and fixes; nothing contradicts them.

## 9. Discernment spot-check (non-author)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S472 row (tier A, own-work) | ADMIT | `CORPUS.md` used-by definition; `reports/round-86/sweep7-red-prelanding.log`; `sweep7-v6-blind-prelanding.log`; the landing SOURCES.md row | agree | the ≤25-word located quote "repo-relative paths of the knowledge entries or lessons citing the row" (11 words) is verbatim from CORPUS.md's used-by definition; the own-work evidence paths exist, are committed, and this verifier re-ran both receipts value-for-value — the row teaches exactly what the drift demonstrated |
| coverage/K move (fresh-start §7) | REJECT (stay routed) | `.ufo/l0-questions.md` line 233 (revenger r74); `freshstart-probes.log` probe 3 | agree | the deciding wave Q-review surface does not exist on this host (L0 r74 unanswered, re-read with counts 1/1); a do-nothing control reaches the claim identically, so refusing to declare it is the honest routing, not laziness |
| coverage/F android move | REJECT (stay gated) | `freshstart-probes.log` probe 1 (`REA_JADX_MCP_JAR=UNSET`, `jadx: not on PATH`) | agree | the hard gate is environmental and re-probed fresh this round; F4's 10/11 honest exception stands |

Census validator re-run by this verifier: contract-literal form
(`sources-census.sh validate --root <fleet> revenger`) → exit 2, `revenger missing …/shokunin-clone/shokunin/revenger-shokunin/corpus/SOURCES.md`
— reproduces the disclosed r74–r86 operator-side lineage (L0 r79 stands); sanctioned
explicit-lane-dir form → exit 0, 31 W (21 W01 + 10 W04), zero E — matches `census-after.log`
(SANCTIONED_EXIT=0, SANCTIONED_W=31, SANCTIONED_E=0). Both round-start receipts re-read and match.

## 10. Per-axis verdicts (non-author)

| axis | verdict | evidence |
|---|---|---|
| calibration | improved | C1 re-measured: mismatch=6 → 0 over a live six-row class; instrument mutation-checked; after-run receipts re-derived from committed blobs before landing |
| depth | improved | C2 re-measured: 9/0/4 → 10/2/8; SKILL.md now carries the cite-back rule, placeholder semantics, division of labor, and the M42 signature |
| coverage | unchanged | all reachable surfaces saturated/hard-gated/operator-blocked with fresh receipts; holds re-run green; K untouched |
| freshness | unchanged (held) | 18/18 re-measured over landing blobs; knowledge bytes untouched in range |
| operability | unchanged (held) | M/A1/A1v2/F4 probe holds re-run green; no verifier byte changed |
| adjacency | unchanged | PROVINCE byte-unchanged; ADJ-06 remains reported-not-absorbed; no contested scope this round |

## 11. Trend verdicts (non-author)

- expansion: unchanged — no knowledge admission (K untouched, operator-blocked), no new
  capability row (v7 is a supersession of the registered `cited-evidence orphan sweep`
  capability, first-working r80 unchanged), denominators held (3/3, 3/3, 5/5, 10/11).
- quality: improved — the routed per-source accounting vector became machine-caught with a
  mutation-checked switch over a live six-row class, and the skill gained the decision ground
  the drift demonstrated missing; no admitted entry failed its re-check.
- discernment: improved — eight real defects mined (six attempt-1, two completing-session),
  four caught before any committed byte could mislead; the attempt-1 death and worktree-only
  residue are disclosed and receipted rather than papered over; this verifier's spot-check
  agrees with the round's admit and both sampled rejections.

## 12. Notes and routed items (status-neutral; none bar admission)

1. Census contract-literal form exit 2 persists (r74–r86 operator-side lineage; L0 r79 carries
   the operator question; routed around again this round with both receipts). Operator-side.
2. SHONEN box 1: the standing non-author re-confirmation need now names the r86 SKILL.md bytes
   (SKILL.md changed this round); routing re-recorded, no box marked by the author — correct.
   All four boxes are `[~]` with resolvable pointers; this verifier confirms box 3's substance
   (frozen counting commands and v7 recipes were re-executed verbatim by a non-author — this
   session — with observed exits matching promises), which an operator may cite toward the
   promotion-time `[x]` on boxes 1–4.
3. L2 floor remains non-executable on this host (no dispatch surface, r74 L0 re-read); every
   verdict re-derives from committed bytes — disclosed, not violated.
4. Lowest-axis obligation (coverage) routed on documented unreachability: probe 6's enumeration
   is receipted and every cited gate was re-opened by this verifier. Accepted this round; the
   routing must be re-probed fresh each round (it was) until an operator ruling or a provider
   surface move changes a gate.
5. Attempt-1 mid-round death handled per the respawn/inherit rules: attempt-1's landed bytes
   untouched (section 3), the worktree-only residue re-derived from committed blobs BEFORE
   landing, and the honest shape recorded in LOG + lesson erratum. No rewrite anywhere.
6. Routed forward (unchanged, per lesson `## Routed forward`): criterion R full extension;
   criterion N attribution pair; criterion C repair (§9); F android gate; K L0; census literal
   form (operator); SHONEN box 1 non-author re-confirmation (operator, r86 bytes); treecommit
   discipline (held 10/10 + 3/3).

## 13. Closure decision

Both claims verify (C1 and C2 re-measured by this verifier from committed bytes; gates/selftest
verified from committed receipts); no axis is harmed; conformance defects are status-neutral and
named above. **status ok, verdict admitted.**
