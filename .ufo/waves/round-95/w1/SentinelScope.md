# SentinelScope — round 95 w1 scope audit (findings)

Full numbered checks with evidence: `.ufo/waves/round-95/w1/SentinelScope/audit.md`.
Snapshot 14:43:31 (-03), 2026-11-05. Seats still writing; 4 of 13 seats had no w1 output yet.

## Findings

1. **FAIL — unexpected lane paths dirty or untracked** (not in the freeze set):
   `M SKILL.md`, `M corpus/README.md`, `M corpus/SOURCES.md`, `M corpus/lessons/round-94.md`,
   `?? corpus/lessons/round-95.md`. Metadata shows in-place writes at 14:36:01, 14:36:41, 14:37:05,
   14:37:35, 14:38:19. The bytes match the ScribeLesson scratch tree (except lesson round-95.md,
   which differs at line 60). Writer not identified. Most likely the L1 integrator; a seat writing
   lane files would violate its bounds. Confirmation needed.
2. **PASS — pycache in corpus/, reports/round-95/, and the wave dir** (five checks, 14:37:05 to 14:43:31).
   **FAIL — reports/round-94/__pycache__/c1_k_admit_counter3.cpython-314.pyc** (ignored by .gitignore;
   written 14:23:14, pre-wave, matching the L1 debug scratch timestamp; the frozen r94 dir should be cleaned by the L1).
3. **PASS — /tmp write roots, sysctl, sudo, pacman in w1** (one negative mention in ScoutReopen.md:61).
   **PASS — no changes in ~/.local/bin since the wave spec.**
4. **FAIL — fleet-root misroot**: untracked `evb.ts` at /home/vgpnk/Projects/shokunin, written 14:39:35
   (22885 B, REA evidenceBundle TypeScript source). Not referenced by any lane or wave path. Writer unresolved;
   candidates by timestamp: ConnectorOverlap, ExecReceipts, ReviewerBlind. Fleet owner should remove it.
   Other fleet-root changes are orchestrator logs or pre-wave state, not seat writes.
5. **PASS — per-seat bounds** for the eight seat dirs written so far (ConnectorOverlap, ExecBattery, ExecCensus,
   ExecFrozen, ExecReceipts, ReviewerBlind, ScoutCiteback, ScoutReopen). No seat output outside its own dir.
6. **PASS — no jj writes after the wave started** (last .jj write 14:30:00, the freeze).
7. **INFO** — ExecCensus ran `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate` (fleet-root
   script); its write behaviour was not inspected here.

## Not done by this seat

- Nothing was fixed, deleted, or edited. The evb.ts, pyc, and lane-path items are reported for their owners.
- Four seats (ScribeLesson, ReviewerGate, CriticR95, MutationR95) had no w1 output at snapshot time; their
  bounds are unverified. Re-run checks 1, 2, 4 after they finish.

## Self-disclosure

`git status` in the lane and fleet repos may refresh `.git/index`; the fleet `.git` mtime 14:43:31 reflects
this audit's status call. Scratch `/fast/scratch/hyaku/revenger-r95/SentinelScope/` is removed on exit.
