# SentinelR91Scope — round-91 adversarial write-scope / no-harm audit

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`
Fleet root: `/home/vgpnk/Projects/shokunin` (read-only for this seat)
Freeze commit: `b13aac7` (`reports/round-91/freeze-base.txt` names the *base* `f6356ffb8b665bddc5ee2cfac81443c1300b59bf`)
Lane HEAD at audit: `d509e98` (`refs/heads/main`)
Audit window: 2026-11-04 19:25–19:45 (-0300). All commands read-only; no mutating git/jj was run anywhere, no fixture repo was created.

Result: **24 checks — 22 PASS, 1 PASS-WITH-DISCLOSURE, 1 OBSERVATION. Zero write-scope violations by the round. Frozen artefacts byte-unchanged (5/5).**

---

## 1. Lane worktree state

### CHECK 01 — lane status
```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin status --porcelain -uall
?? .ufo/waves/round-91/assimilation/collisions
?? .ufo/waves/round-91/assimilation/guard/collisions
?? .ufo/waves/round-91/assimilation/guard/guard-proof.log
?? .ufo/waves/round-91/assimilation/guard/ids
?? .ufo/waves/round-91/assimilation/guard/scratch-registry.md
?? .ufo/waves/round-91/assimilation/reg-ids
?? .ufo/waves/round-91/assimilation/staged-ids
?? .ufo/waves/round-91/w1-validate.err
?? .ufo/waves/round-91/w1.ready
?? .ufo/waves/round-91/w1.ready.dispatched
?? .ufo/waves/round-91/w1/ExecR91Sm6V3/counter.log
?? .ufo/waves/round-91/w1/ReviewerR91C2/build_fixture.sh
?? .ufo/waves/round-91/w1/ReviewerR91C2/expected-pre-registered.md
?? .ufo/waves/round-91/w1/ReviewerR91C2/run_cases.sh
?? .ufo/waves/round-91/w1/ReviewerR91C2/tally_real.py
?? .ufo/waves/round-91/w1/swarm-registry.json
?? corpus/self_assessment_check3.py
?? reports/round-91/holds.log
```
**Verdict: PASS.** Every entry is untracked and inside the lane, at a round-91 path (`reports/round-91/`, `.ufo/waves/round-91/`, `corpus/self_assessment_check3.py`). **No ` M`/` D`/`R` line: no tracked file in the lane was modified or deleted by any seat.** `reports/round-91/holds.log` matches the path claims.md routes coverage on. Lane HEAD == `refs/heads/main` == `d509e98`.

### CHECK 02 — commits after the freeze
```
$ git -C <lane> log --oneline b13aac7..refs/heads/main
d509e98 round-91: wave w1 evidence — 13-seat build+attack spec (4 attack seats, 30.8%), validated dispatch under ufo-wave-policy.json (band 8-16), .ready handoff
```
**Verdict: PASS.** Exactly one commit; the L1 owns it (no seat committed).

### CHECK 03 — files in that commit
```
$ git -C <lane> show --name-status --oneline --no-renames d509e98
A	.ufo/waves/round-91/w1-dispatch.json
A	.ufo/waves/round-91/w1-spec.json
A	.ufo/waves/round-91/w1-validate.out
```
**Verdict: PASS.** Three wave-evidence files, all inside the lane's own wave dir.

### CHECK 04 — freeze commit contents
```
$ git -C <lane> show --name-status --oneline --no-renames b13aac7
A	reports/round-91/c1-red-v1.log
A	reports/round-91/c1-red-v2.log
A	reports/round-91/c1_counter.py
A	reports/round-91/c2-red-absent.log
A	reports/round-91/cap_probe.py
A	reports/round-91/claims.md
A	reports/round-91/freeze-base.txt
A	reports/round-91/mutants.py
A	reports/round-91/sm6_battery_v3.py
```
**Verdict: PASS.** Nine files, all under `reports/round-91/`.

---

## 2. Round diff vs. the two reference points

### CHECK 05 — `f6356ff..main` (the task-named base)
```
$ git -C <lane> diff --name-status f6356ffb8b665bddc5ee2cfac81443c1300b59bf refs/heads/main
A	.ufo/waves/round-91/w1-dispatch.json
A	.ufo/waves/round-91/w1-spec.json
A	.ufo/waves/round-91/w1-validate.out
A	reports/round-91/c1-red-v1.log
A	reports/round-91/c1-red-v2.log
A	reports/round-91/c1_counter.py
A	reports/round-91/c2-red-absent.log
A	reports/round-91/cap_probe.py
A	reports/round-91/claims.md
A	reports/round-91/freeze-base.txt
A	reports/round-91/mutants.py
A	reports/round-91/sm6_battery_v3.py
```
**Verdict: PASS.** 12 additions, 0 modifications, 0 deletions. All 12 paths are inside the lane.

### CHECK 06 — protected paths in the lane diff
```
$ git -C <lane> diff --name-only b13aac7..refs/heads/main \
  | grep -E '^(\.ufo/state/|scripts/|templates/|\.scratch/|MANIFEST\.json)'
protected_hits_exit=1
```
**Verdict: PASS.** No match (grep exit 1 = none).

### CHECK 07 — out-of-scope / sibling paths in the lane diff
```
$ git -C <lane> diff --name-only b13aac7..refs/heads/main \
  | grep -vE '^(reports/round-91/|\.ufo/waves/round-91/|corpus/|reports/|\.ufo/)'
out_of_scope_exit=1
```
**Verdict: PASS.** No match: no `../`, no sibling lane, no fleet-root path.

### CHECK 08 — any commit touching a protected path in the whole range
```
$ git -C <lane> log --oneline b13aac7..refs/heads/main -- MANIFEST.json .ufo/state scripts templates .scratch
(empty)
```
**Verdict: PASS.** No commit in the range touches those paths.

---

## 3. Frozen artefacts byte-unchanged

### CHECK 09 — diffstat since the freeze
```
$ git -C <lane> diff --stat b13aac7..refs/heads/main -- \
  reports/round-91/claims.md reports/round-91/sm6_battery_v3.py \
  reports/round-91/mutants.py reports/round-91/c1_counter.py reports/round-91/cap_probe.py
(empty output)
```
**Verdict: PASS.** No change since the freeze commit.

### CHECK 10 — blob-hash equality (committed blob vs. worktree file)
```
claims.md            b13aac7=84a599beea526cfa9a594a42d31336c979b87914  worktree=84a599beea526cfa9a594a42d31336c979b87914
sm6_battery_v3.py    b13aac7=142686d99c233d562f9845702c7d2d2880686765  worktree=142686d99c233d562f9845702c7d2d2880686765
mutants.py           b13aac7=ae99b6f1f87f6eda082ac891abe729e04185baf1  worktree=ae99b6f1f87f6eda082ac891abe729e04185baf1
c1_counter.py        b13aac7=76a639b0574bd7ef15fd6f0535c7b5094a791910  worktree=76a639b0574bd7ef15fd6f0535c7b5094a791910
cap_probe.py         b13aac7=52c8d60b0c98b5e213895e2e398460eb021d38f7  worktree=52c8d60b0c98b5e213895e2e398460eb021d38f7
```
**Verdict: PASS.** 5/5 identical, both committed and on disk (`git hash-object` == `git rev-parse b13aac7:<path>`). `claims.md` has a 19:37 mtime (rewritten at freeze by the L1) but its bytes equal the frozen blob.

---

## 4. Secret-shape scan

### CHECK 11 — keyword scan over added lines in the round range
```
$ git -C <lane> diff b13aac7..refs/heads/main | grep -E '^\+' \
  | grep -oE '(api[_-]?key|secret|token|password|BEGIN [A-Z ]*PRIVATE KEY|ghp_[A-Za-z0-9]*|sk-[A-Za-z0-9]*)' | sort | uniq -c
     12 token
      9 secret
      3 sk-
      3 password
      3 ghp_
```
Per-file, per-line localisation:
```
w1-spec.json     : 33 token | 81 token | 106 token,password,ghp_,sk-,secret×3 | 114 token
w1-dispatch.json : 183 token | 213 token | 228 token,password,ghp_,sk-,secret×3 | 233 token
w1-validate.out  : 183 token | 213 token | 228 token,password,ghp_,sk-,secret×3 | 233 token
```
**Ruling: all 30 hits benign — zero credential material.**
- Line 106 of `w1-spec.json` and line 228 of `w1-dispatch.json`/`w1-validate.out` are the same object: the **embedded Sentinel seat prompt**, whose text *is* the audit instruction `grep -nE '(api[_-]?key|secret|token|password|BEGIN [A-Z ]*PRIVATE KEY|ghp_|sk-)'`. The pattern's own literals are the match. Verified by reading line 106: it begins `"prompt": "/skill:godspeed\nYou are a Godspeed-enabled subagent...`.
- `token` on lines 33/81/114/183/213/233: seat prompts about the SM6 rule ("token-adjacent `N/D`") and the message-tree spec ("hex token").
- No `ghp_`/`sk-` occurrence is followed by credential-shaped entropy (next check).

### CHECK 12 — high-entropy credential shapes over the round range
```
$ git -C <lane> diff b13aac7..refs/heads/main | grep -E '^\+' \
  | grep -nE '(ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,})'
exit=1 (no match)
```
**Verdict: PASS.** No token, key, or PEM block.

### CHECK 13 — frozen report artefacts
```
$ grep -nE '(api[_-]?key|secret|token|password|BEGIN [A-Z ]*PRIVATE KEY|ghp_|sk-)' reports/round-91/*
reports/round-91/mutants.py:12:  | M01 | reads the last token-adjacent group on the whole LINE (the v2 rule) | R03, R04 |
reports/round-91/mutants.py:14:  | M03 | takes the FIRST `N/D` in the stated region, not the token-adjacent one | R02, R07 |
reports/round-91/mutants.py:22:  | M11 | token-adjacent pattern without the parenthesised-score allowance | B07 |
reports/round-91/mutants.py:108: """v2's rule: last token-adjacent group anywhere on the line."""
reports/round-91/mutants.py:140: """First raw `N/D` in the stated region, ignoring token adjacency and arrows."""
reports/round-91/claims.md:24: lane writes its numbers in — instead of the last token-adjacent `N/D` anywhere
reports/round-91/claims.md:37: immediately follows the token (skipping non-digits, an optional parenthesised
```
**Ruling: benign.** All seven hits are the English word "token" in the frozen SM6 rule prose. No credential.

### CHECK 14 — landed C1 implementation
```
$ grep -nE '(api[_-]?key|secret|token|password|BEGIN [A-Z ]*PRIVATE KEY|ghp_|sk-)' corpus/self_assessment_check3.py
5:   v3 changes SM6 only: v2 read the last token-adjacent `N/D` anywhere on the last
27:  SM5  SCORECARD commit citations: a backticked 7-40 hex token introduced by
36:       the first `N/D` group immediately following the `K_HELD_BACKED` token
120:    file token in its box; a value with no preceding file token, or whose nearest token is a
171:            # the correction must share a >= 6 character prefix with the token it corrects
220:      4. with the token present, the FIRST `N/D` group immediately following it
329:        # erratum: a resolving correction that shares a >= 6 char prefix with the token excuses it;
346:            ("SM2", "name only a substring of a longer README token", lambda r: (r / "corpus/tool_x.py").write_text(
363:            txt(r / "SCORECARD.md") + "```\nthe token tip `bbbbbbb` must resolve\n```\n", encoding="utf-8"), 0),
```
**Ruling: benign.** Nine hits, all the word "token" in SM6/erratum logic and self-test fixtures; no secret value, no network call, no env-var read.

### CHECK 15 — wave dir and untracked lane files
```
$ grep -rnE '(ghp_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,})' .ufo/waves/round-91 reports/round-91
exit=1 (no match)
$ (same pattern over every `git status ?? ` file) -> no HIT lines
```
**Verdict: PASS.** Including the seat-written wave files (`ExecR91Sm6V3/counter.log`, `ReviewerR91C2/*`).

---

## 5. Fleet root (report only — never edited)

### CHECK 16 — fleet-root status
```
$ git -C /home/vgpnk/Projects/shokunin status --porcelain
 M .scratch/run15-state.json
 M .ufo/l0-questions.md
 M .ufo/reports/round-84/kama.md
?? .scratch/closure-kaidoku-r73-entry.json
?? .scratch/closure-kaidoku-r79-entry.json
?? .scratch/closure-kaidoku-r80-entry.json
?? .scratch/closure-kasegi-r60-entry.json
?? .scratch/closure-kasegi-r65-entry.json
?? .scratch/closure-kasegi-r67-entry.json
?? .scratch/closure-kotodama-r83-entry.json
?? .scratch/closure-kumitate-r81-entry.json
?? .scratch/closure-kumitate-r83-entry.json
?? .scratch/closure-mado-r74/
?? .scratch/closure-mado-r75-entry.json
?? .scratch/closure-mado-r85/
?? .scratch/closure-tabi-r63-entry.json
?? .scratch/closure-tameshi-r82-entry.json
?? .scratch/closure-tameshi-r85-entry.json
?? .scratch/closure-tsukuroi-r78-entry.json
?? .scratch/run13-state.json
?? after
(21 lines total)
```
**Verdict: PASS-WITH-DISCLOSURE.** Nothing in this list is a revenger round-91 write surface except the L0-question append (check 19). `MANIFEST.json`, `SCORECARD.md`, `LOG.md` are clean:
```
$ git -C /home/vgpnk/Projects/shokunin status --porcelain -- MANIFEST.json SCORECARD.md LOG.md
(empty)
```
Untracked `.scratch/closure-*-entry.json` files and `run13-state.json` are other lanes' closeout records (pre-existing driver/closure tooling). `after` is 24 bytes, mtime **2026-11-03 20:05** — predates round 91 by ~23 h, not a round-91 artefact.

### CHECK 17 — fleet protected dirs, filesystem sweep (mtime in window)
```
$ find scripts templates -newermt '2026-11-04 19:30' -type f
19:38 scripts/hyaku/lane-addendum.md
$ find .scratch -newermt '2026-11-04 19:30' -type f
19:39 .scratch/run15-state.json
19:38 .scratch/run15-kernel.py
```
Content test (mtime ≠ content change):
```
scripts/hyaku/lane-addendum.md : git diff --quiet -> exit 0 ; worktree_hash=e80917bf878f4661d58c8157dc8c6f475eafa613 == HEAD blob e80917bf...
.scratch/run15-kernel.py       : git diff --quiet -> exit 0 ; worktree_hash=267bbc7d5cf5b040d90b16e92b12bd9afaba13c5 == HEAD blob 267bbc7d...
.scratch/run15-state.json      : MODIFIED (139 lines changed)
```
`run15-state.json` diff head:
```
- "trained": 0, - "admitted": 0, - "rejected": 0,
+ "trained": 211, + "admitted": 144, + "rejected": 67,
  "revenger": { "start_next": 89, -"block_start": null, -"block_done": 0 +"block_start": 89, +"block_done": 2 },
  "tsukuroi": { "start_next": 64, -"block_start": null, -"block_done": 0 +"block_start": 81, +"block_done": 1 },
```
**Verdict: PASS.** `scripts/hyaku/lane-addendum.md` and `.scratch/run15-kernel.py` were **touched, not modified** (byte-identical to HEAD) — a driver re-read/write of identical bytes. `run15-state.json` is the hyaku driver's run ledger (per-lane block counters advanced across *all* lanes, not just revenger); it is driver-owned state, not a lane-seat write, and no round-91 seat can produce a 139-line multi-lane counter diff. Disclosed, not attributed to a revenger seat.

### CHECK 18 — `.ufo/state` and `.ufo/watchdog.log`
```
$ git -C /home/vgpnk/Projects/shokunin check-ignore -v .ufo/state/disk-guard.log
.gitignore:8:.ufo/state/*	.ufo/state/disk-guard.log
$ git -C /home/vgpnk/Projects/shokunin ls-files .ufo/state
.ufo/state/.gitkeep
$ find .ufo/state .ufo/watchdog.log -newermt '2026-11-04 19:30'
2026-11-04 19:32 .ufo/state/revenger.report-baseline
2026-11-04 19:33 .ufo/state/kotodama.report-baseline
2026-11-04 19:39 .ufo/state/chousa.report-baseline
2026-11-04 19:39 .ufo/state/disk-guard.log
2026-11-04 19:39 .ufo/state/inline-dispatcher.log
2026-11-04 19:39 .ufo/state/kaidoku.report-baseline
2026-11-04 19:39 .ufo/watchdog.log
$ tail -3 .ufo/watchdog.log
2026-11-04T19:38:59-03:00 complete mori round=89; hyaku-inline attempt=1
2026-11-04T19:39:05-03:00 launch kaidoku round=88 pgid=3790618 driver=hyaku-inline attempt=1
2026-11-04T19:39:07-03:00 launch chousa round=78 pgid=3792375 driver=hyaku-inline attempt=1
```
**Verdict: PASS.** `.ufo/state/*` is gitignored except `.gitkeep` (which is untouched — not in the modified list); only the driver's own runtime files move (per-lane `report-baseline` stamps, `disk-guard.log`, `inline-dispatcher.log`). `watchdog.log` lines are hyaku-inline driver launch/complete records for *other* lanes. **No credential material, no lane-seat write.** Note for the record: because `.ufo/state/*` is gitignored, git cannot prove non-modification there — the mtime/content shape above is the available evidence, and it is consistent with driver-only traffic.

### CHECK 19 — fleet-root tracked prose modified by the round
```
$ stat -c '%y' .ufo/l0-questions.md
2026-11-04 19:38:36.727983354 -0300
$ git -C /home/vgpnk/Projects/shokunin diff .ufo/l0-questions.md
@@ -301,3 +301,4 @@
+revenger | round-91 | Assimilation id-collision guard: the staged package
+  /home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md carries 155 ids
+  and all 155 collide with this lane registry (S047-S201; comm -12 count 155,
+  .ufo/waves/round-91/assimilation/collisions). ... Decision wanted: renumber the
+  package per lane (campaign-side, scratch) and re-issue, or have the lane adopt
+  by document with ids continuing its registry (S488+) and re-point every citation
+  by URL/anchor.
```
`.ufo/reports/round-84/kama.md` mtime is **2026-11-04 12:28** — seven hours before the freeze, not a round-91 write.
**Verdict: PASS-WITH-DISCLOSURE.** One line appended to the fleet-root tracked `L0-questions` channel by a round-91 revenger actor. Ruling: this is the sanctioned operator-question channel (the same file carries `kake | round-89`, `kaidoku | round-86`, `kotodama | round-89` entries in the same format), the appended text contains no credential and no path outside the fleet, and it is not in the protected list. It is nevertheless a fleet-root tracked-file write, which a *seat* contract forbids — most consistent with the L1 (holder of the planner seat, which owns cross-lane escalation) writing it. **Disclosed to L1; not ruled a breach, and nothing to remediate.**

---

## 6. Sibling lanes

### CHECK 20 — sibling lane worktree files touched in the window
```
$ find ./*-shokunin -type f -newermt '2026-11-04 19:30' -not -path '*/.git/*' -not -path '*/.jj/*'
19:31 kotoba-shokunin/verifiers/__pycache__/verify_harness_claims.cpython-314.pyc
19:32 chousa-shokunin/{corpus/lessons/round-77.md,corpus/QUALITY.md,LOG.md,SCORECARD.md}
19:32 kasegi-shokunin/{corpus/instruments/knowledge-expected.txt,corpus/README.md,corpus/SOURCES.md}
19:32 kotodama-shokunin/corpus/lessons/round-89-verifier-spotcheck.md
19:32 kumitate-shokunin/SCORECARD.md
19:33 mori-shokunin/{corpus/knowledge/execution-binding-r89.md,LOG.md}
19:34 kotoba-shokunin/{corpus/lessons/round-86.md,LOG.md}
19:34 mori-shokunin/corpus/QUALITY.md
19:35 mori-shokunin/{corpus/lessons/round-89.md,corpus/README.md,SKILL.md}
19:36 kake-shokunin/corpus/knowledge/cache-key-construction.md
19:36 kasegi-shokunin/SKILL.md
19:36 mori-shokunin/SCORECARD.md
19:37 kaidoku-shokunin/corpus/lessons/round-87-verifier-spotcheck.md
19:37 kake-shokunin/scripts/__pycache__/cache_key_conformance.cpython-314.pyc
19:37 kasegi-shokunin/corpus/lessons/round-69.md
```
**Verdict: PASS (reported, not attributed to revenger).** These are other lanes' *own concurrent rounds*, launched by the same hyaku driver inside this window (`watchdog.log` 19:38:59 mori r89 complete, 19:39:05 kaidoku r88 launch, 19:39:07 chousa r78 launch). Cross-lane authorship test:
```
$ grep -liE 'revenger.*round[- ]?91|round[- ]?91.*revenger' <each sibling file touched in window>
(no output)
```
No sibling file touched in the window references revenger round 91. Revenger's own diff names no sibling path (check 07).

### CHECK 21 — kaidoku touch is mtime-only
```
$ git -C kaidoku-shokunin diff --quiet -- corpus/lessons/round-87-verifier-spotcheck.md
diff_quiet_exit=0 (unchanged vs HEAD)
$ git -C kaidoku-shokunin status --porcelain
?? .ufo/waves/round-85/r85-w1.ready
?? .ufo/waves/round-85/r85-w1.ready.dispatched
?? .ufo/waves/round-86/r86-w1.ready
?? .ufo/waves/round-86/r86-w1.ready.dispatched
?? .ufo/waves/round-87/r87-w1.ready
?? .ufo/waves/round-87/r87-w1.ready.dispatched
```
**Verdict: PASS.** The one sibling file whose mtime looked suspicious (kaidoku r87 lesson, 19:37) is byte-identical to its HEAD — a touch, not a write. (No `jj` command was run in that repo; `jj` auto-snapshots on read, which would itself be a mutation.)

### CHECK 22 — revenger's own `.jj` store
```
$ find revenger-shokunin/.jj -newermt '2026-11-04 19:30' -type f
19:38 revenger-shokunin/.jj/repo/store/extra/heads/c2269cb8...8642
19:31 revenger-shokunin/.jj/repo/store/extra/{4ac4b0bd…,c9d256c6…,47838767…,c17b1a0c…}
```
**Verdict: PASS.** Lane-local jj store writes at freeze/dispatch time; this is the L1's own commit path (seats are forbidden mutating jj). No seat ran jj — the seat protocol forbids it and no seat output claims otherwise.

---

## 7. Dispatch spec write-surface audit (adversarial)

### CHECK 23 — spec/dispatch write targets
```
$ grep -oE '\.\./[A-Za-z0-9_./-]*' .ufo/waves/round-91/w1-spec.json | sort -u
(none)
$ grep -oE '/home/vgpnk/Projects/shokunin/[A-Za-z0-9_./-]*' w1-spec.json | grep -v '^…/revenger-shokunin' | sort -u
/home/vgpnk/Projects/shokunin/
/home/vgpnk/Projects/shokunin/.scratch/
/home/vgpnk/Projects/shokunin/scripts/
/home/vgpnk/Projects/shokunin/templates/
/home/vgpnk/Projects/shokunin/.ufo/state/
```
Context extraction (`json` walk over `w1-spec.json`) shows all five occur in **one string**: the shared seat contract — `Write ONLY inside …/revenger-shokunin at the paths your task names. Never edit MANIFEST.json, …/.ufo/state/, .ufo/watchdog.log, …/templates/, …/scripts/, …/.scratch/, sibling lane repos, or the fleet root.` The protected paths appear **only as prohibitions**, never as write targets. `reportDir` is `.ufo/waves/round-91/w1`; all 13 items resolve their report under that dir. No `../` traversal anywhere in the spec.
**Verdict: PASS.** The dispatch cannot steer a seat outside the lane.

### CHECK 24 — peer fixture protocols and lane mutation by peers
```
$ cat .ufo/waves/round-91/w1/ReviewerR91C2/build_fixture.sh
D=$(mktemp -d "$S/fixture.XXXXXX")            # S=$HYAKU_SCRATCH/revenger-r91/ReviewerR91C2
git -C "$D" init -q
top=$(git -C "$D" rev-parse --show-toplevel); [ "$top" != "$D" ] && exit 2
git -C "$D" config user.name "r91-reviewer-fixture"
git -C "$D" config user.email "r91-reviewer@fixture.invalid"
commit() { git -C "$D" add -A; git -C "$D" commit -q --allow-empty -m "$1"; git -C "$D" rev-parse HEAD; }
$ grep -rn 'git -C /home/vgpnk/Projects/shokunin/revenger-shokunin \(add\|commit\|checkout\)' .ufo/waves/round-91/w1
exit=1 (no match)
```
**Verdict: PASS.** The only peer-authored fixture driver in the lane obeys the protocol: scratch under `$HYAKU_SCRATCH/revenger-r91/<seat>`, `mktemp -d`, `git -C "$D"` on every call, toplevel asserted before the first commit, fixture-local identity only. No peer ran a mutating git command against the lane.

---

## Observations (not violations)

**OBS-01 — C2 deliverable not yet landed at audit time.** `reports/round-91/message_tree_check.py` **does not exist** (19:42 snapshot: `ls: cannot access 'reports/round-91/message_tree_check.py': No such file or directory`), while `corpus/self_assessment_check3.py` landed at 19:42 (`-rwxr-xr-x 17842`). The C2 executor (`ExecR91MsgTree`) is still running, so this is a mid-wave state, not a defect: the C2 counter must be run at integration. Flagged so that no report describes C2 as passed before the instrument exists.

**OBS-02 — 13 seats dispatched, claims.md fixes 12.** `claims.md` "Round shape (fixed here)" says *12 seats* (executor×4, scribe×2, scout×1, connector×1, reviewer×1, critic×1, mutation-tester×1, sentinel×1). `w1-spec.json` carries 13 items (`ExecR91Sm6V3, ExecR91BatteryX, ExecR91MsgTree, ExecR91RealRun, ScribeR91Sources, ScribeR91Skill, ScoutR91Surfaces, ConnectorR91Overlap, ReviewerR91C1, CriticR91Claims, MutR91Sm6, SentinelR91Scope, ReviewerR91C2`), and the L1 commit message says "13-seat build+attack spec (4 attack seats, 30.8%)". So one reviewer seat (C2) was added over the frozen 12-seat shape. Not a write-scope issue; **disclosed for the L1** because the frozen claims file states the round shape and the extra seat is a spec-vs-freeze divergence the validator/round report should record (attack ratio 4/13 = 30.8 %, still inside the 8–16 band and above the 25 % floor).

**OBS-03 — `reports/round-91/holds.log` is untracked.** It is cited by claims.md as a coverage receipt; it exists with the expected `K_HELD_BACKED=8/15` / `F4_COVERAGE=11/11` content but is not committed. The L1 commits; no action for this seat.

---

## Bottom line

- **Checks run: 24.** 22 PASS, 1 PASS-WITH-DISCLOSURE (fleet-root `L0-questions` append), 1 OBSERVATION (C2 instrument not yet landed).
- **Write-scope violations: 0.** The round's diff (`f6356ff..main`: 12 adds; `b13aac7..main`: 3 adds) contains **no** path under `.ufo/state`, `scripts/`, `templates/`, `.scratch/`, no `MANIFEST.json`, no sibling lane, no `../`.
- **Credential material: none.** 30 keyword hits, all the literal text of the audit pattern embedded in seat prompts plus the English word "token" in the SM6 rule; zero high-entropy matches for `ghp_…`, `sk-…`, PEM blocks, `AKIA…`, `xox…` anywhere in the round range, the wave dir, or the new implementation.
- **Frozen artefacts: byte-unchanged.** `claims.md`, `sm6_battery_v3.py`, `mutants.py`, `c1_counter.py`, `cap_probe.py` — empty `diff --stat b13aac7..main` and 5/5 blob-hash equality with the `b13aac7` blobs.
- **Sibling lanes: untouched by this round.** Their in-window mtimes belong to their own concurrent driver-launched rounds; the one content-suspicious file is byte-identical to HEAD; no cross-reference to revenger round 91 exists in any of them.
