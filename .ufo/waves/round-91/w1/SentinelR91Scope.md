# SentinelR91Scope — round-91 write-scope / no-harm audit (report)

Scope: lane `revenger-shokunin` at HEAD `d509e98` (`refs/heads/main`), freeze `b13aac7`, base `f6356ff`. Read-only throughout; no fixture repo, no mutating git/jj, nothing installed.

**Result: 24 checks — 22 PASS, 1 PASS-WITH-DISCLOSURE, 1 OBSERVATION. Zero write-scope violations. Frozen artefacts byte-unchanged (5/5).**

## Checks and verdicts

| # | Check | Verdict |
|---|---|---|
| 01 | `git -C <lane> status --porcelain -uall` | PASS — 18 untracked, all at round-91 lane paths; **no tracked file modified/deleted** |
| 02 | `git -C <lane> log --oneline b13aac7..refs/heads/main` | PASS — 1 commit `d509e98` (L1) |
| 03 | `git show --name-status d509e98` | PASS — 3 wave-evidence files |
| 04 | `git show --name-status b13aac7` | PASS — 9 files, all `reports/round-91/` |
| 05 | `git diff --name-status f6356ff..main` | PASS — 12 adds, 0 mods, 0 dels, all in-lane |
| 06 | protected-path filter on lane diff | PASS — none (grep exit 1) |
| 07 | out-of-scope/sibling filter on lane diff | PASS — none (grep exit 1) |
| 08 | `git log b13aac7..main -- MANIFEST.json .ufo/state scripts templates .scratch` | PASS — empty |
| 09 | `git diff --stat b13aac7..main -- <5 frozen files>` | PASS — empty |
| 10 | blob-hash equality vs `b13aac7:` for the 5 frozen files | PASS — 5/5 identical (committed and on disk) |
| 11 | keyword secret scan over added lines | PASS — 30 hits, all benign (see rulings) |
| 12 | high-entropy credential shapes (`ghp_{20,}`, `sk-{20,}`, PEM, AKIA, xox) | PASS — no match |
| 13 | frozen `reports/round-91/*` scan | PASS — 7 hits, all the word "token" |
| 14 | `corpus/self_assessment_check3.py` scan | PASS — 9 hits, all the word "token" |
| 15 | `.ufo/waves/round-91` + all untracked lane files | PASS — no credential shape |
| 16 | fleet-root `status --porcelain` | PASS-WITH-DISCLOSURE — 3 tracked mods, 18 untracked; none revenger-protected |
| 17 | `scripts/`, `templates/`, `.scratch/` mtime sweep + content test | PASS — `lane-addendum.md`/`run15-kernel.py` byte-identical to HEAD (touch only); `run15-state.json` = driver run ledger |
| 18 | `.ufo/state` + `.ufo/watchdog.log` | PASS — gitignored except `.gitkeep`; only driver runtime files move; watchdog lines are hyaku-inline launches for other lanes |
| 19 | fleet-root tracked prose diff | PASS-WITH-DISCLOSURE — `L0-questions` +1 line (revenger r91 assimilation question), sanctioned channel, no credential, no out-of-fleet path |
| 20 | sibling-lane worktree sweep | PASS — 16 files in window, all other lanes' own concurrent rounds; none references revenger r91 |
| 21 | kaidoku content test | PASS — byte-identical to HEAD (mtime-only) |
| 22 | revenger `.jj` store | PASS — L1 commit path only |
| 23 | dispatch-spec write-target audit | PASS — protected paths appear only in the "Never edit" contract prose; no `../`; `reportDir` `.ufo/waves/round-91/w1` |
| 24 | peer fixture protocol + peer git usage | PASS — `ReviewerR91C2/build_fixture.sh` uses `mktemp -d` under `$HYAKU_SCRATCH`, `git -C "$D"` everywhere, toplevel asserted, fixture-local identity; no peer mutating git on the lane |

## Secret-shape rulings (every hit named)

- `.ufo/waves/round-91/w1-spec.json:106`, `w1-dispatch.json:228`, `w1-validate.out:228` — the **embedded Sentinel seat prompt**, i.e. this audit's own instruction text `grep -nE '(api[_-]?key|secret|token|password|…|ghp_|sk-)'`. The pattern's literals are the match. Benign.
- `w1-spec.json:33,81,114` / `w1-dispatch.json:183,213,233` / `w1-validate.out:183,213,233` — the word "token" in seat prompts (SM6 "token-adjacent `N/D`", message-tree "hex token"). Benign.
- `reports/round-91/mutants.py:12,14,22,108,140` and `reports/round-91/claims.md:24,37` — "token" in the frozen SM6 rule prose. Benign.
- `corpus/self_assessment_check3.py:5,27,36,120,171,220,329,346,363` — "token" in SM6/erratum logic and self-test fixtures; no secret value, no env-var read, no network call. Benign.
- High-entropy scan over the whole round range, the wave dir and the new implementation: **zero matches**.

## Frozen artefacts

`git diff --stat b13aac7..refs/heads/main -- reports/round-91/{claims.md,sm6_battery_v3.py,mutants.py,c1_counter.py,cap_probe.py}` → **empty**. Per-file `git hash-object` == `git rev-parse b13aac7:<path>` for all five. **Byte-unchanged.**

## Disclosures / observations for the L1

1. **OBS-01 (state, not defect).** `reports/round-91/message_tree_check.py` was still absent at the 19:42 snapshot (C2 executor running); `corpus/self_assessment_check3.py` landed 19:42. C2 must not be reported as passed before the instrument exists and `cap_probe.py` runs green.
2. **OBS-02 (freeze divergence).** `claims.md` fixes a **12-seat** wave; `w1-spec.json` and commit `d509e98` carry **13** (extra `ReviewerR91C2`), attack 4/13 = 30.8 %. Inside the 8–16 band and above the 25 % floor, but it diverges from the frozen round shape and should be recorded in the round report rather than silently absorbed.
3. **OBS-03.** `reports/round-91/holds.log` (cited by claims.md as the coverage receipt, `K_HELD_BACKED=8/15`, `F4_COVERAGE=11/11`) is untracked; the L1 commits.
4. **Fleet-root note.** `.ufo/l0-questions.md` gained one revenger round-91 line at 19:38 (assimilation id-collision question). Sanctioned L0 channel with precedent from kake r89 / kaidoku r86 / kotodama r89; no credential, no out-of-fleet path, not a protected path. Reported, not edited, not ruled a breach.

## Files

- Full command/output evidence: `.ufo/waves/round-91/w1/SentinelR91Scope/audit.md`
- This report: `.ufo/waves/round-91/w1/SentinelR91Scope.md`

Report: .ufo/waves/round-91/w1/SentinelR91Scope.md
