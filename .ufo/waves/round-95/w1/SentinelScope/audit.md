# SentinelScope — round 95 wave w1 scope audit (read-only)

Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin (HEAD 6e0bf15, freeze commit)
Audit window: 14:34:30 (w1-spec.json) to 14:43:31 (final recheck), 2026-11-05 (-03).
Wave state at audit time: 8 of 13 seat dirs present in w1/ (ConnectorOverlap, ExecBattery,
ExecCensus, ExecFrozen, ExecReceipts, ReviewerBlind, ScoutCiteback, ScoutReopen). ScribeLesson,
ReviewerGate, CriticR95, MutationR95 had scratch activity and no w1 output yet. Findings are a
snapshot; seats were still writing when the audit closed.

Method: git status --porcelain and git status --ignored --porcelain (lane and fleet), find over
mtime/ctime, grep -rIlE over the wave dir, stat, cmp against scratch copies. No writes to lane
or fleet paths. Two seat-scratch-only actions by this seat: mkdir of its own scratch dir (removed at
exit). Note: `git status` may refresh .git/index in the lane and fleet repos (the fleet .git dir
mtime 14:43:31 is from this audit's status call). That is a benign index refresh, not a content write.

## Summary

| # | check | result |
|---|---|---|
| 1 | lane git status vs expected dirty set | FAIL (5 unexpected lane paths) |
| 2 | corpus/ and reports/round-95 __pycache__ / *.pyc, 5 samples | PASS (corpus, reports/round-95, wave dir all empty) |
| 2b | whole-lane pycache outside the checked scope | FAIL (reports/round-94/__pycache__, pre-wave, ignored) |
| 3a | /tmp write roots in w1 seat outputs | PASS (no hits) |
| 3b | sysctl / sudo / pacman invocations in w1 | PASS (one negative mention, not an invocation) |
| 3c | ~/.local/bin changes since wave spec | PASS (none) |
| 4 | fleet-root status / misroot | FAIL (untracked fleet-root file evb.ts written 14:39:35) |
| 5 | per-seat output bounds (w1/<Seat>/ only) | PASS for the 8 seat dirs present; 4 seats not yet written |
| 6 | jj op-store writes after wave start | PASS (last jj write 14:30:00, pre-wave) |
| 7 | out-of-lane absolute path references in seat outputs | INFO (3 refs; all read-only per the seat text) |

## 1. Lane git status vs expected dirty set — FAIL

Expected at audit time (per task): corpus/knowledge/round-95-evidence-ledger-discipline.md, reports/round-95/,
and .ufo/waves/round-95/. Observed: the first two are committed at 6e0bf15 and are clean. Only
.ufo/waves/round-95/ is untracked as expected. Five additional paths are dirty or untracked:

- M SKILL.md — +18 lines, two new registry rows (c1_k_admit_counter4, forge_battery4). mtime 14:37:35.201, ctime = mtime.
- M corpus/README.md — C10 row moved partial to held; C10 follow-up bullet rewritten. mtime 14:37:05.155, ctime = mtime.
- M corpus/SOURCES.md — S096–S104 used-by column gains round-95 entry; S002 and S108 analogues. mtime 14:36:41.838, ctime = mtime.
- M corpus/lessons/round-94.md — appended "C-r95-1" correction (S499 word count). mtime 14:36:01.013, ctime = mtime.
- ?? corpus/lessons/round-95.md — untracked round-95 lesson. mtime 14:38:19.122, ctime = mtime, 10491 B. Differs from the ScribeLesson scratch draft (ScribeLesson/tree/corpus/lessons/round-95.md, 10416 B, mtime 14:38:05) at line 60.

Evidence:
- git -C /home/vgpnk/Projects/shokunin/revenger-shokunin status --porcelain (T0, T3, T5)
- stat on the paths above (mtime = ctime on every lane file: each was written in place at that time)
- cmp: corpus/lessons/round-94.md, corpus/README.md, corpus/SOURCES.md were byte-identical to /fast/scratch/hyaku/revenger-r95/ScribeLesson/tree/ copies at 14:38:11 (scratch copies were refreshed from the lane at that time, ctime 14:38:11, mtime preserved).

Attribution: no seat spec authorizes writes to corpus/ or SKILL.md. The ScribeLesson spec says "Draft the round-95 lesson into your wave dir; the L1 finalizes the lane file from your draft." The lane-wide text matches the ScribeLesson scratch tree, and the L1 integration role finalizes lane files. The most likely writer is the L1 integrator, but file metadata does not prove who wrote the bytes. Status: UNCONFIRMED violation candidate. The L1 or ScribeLesson must state which actor wrote these paths. If ScribeLesson wrote them, this is a seat-bounds violation (corpus/ and SKILL are lane files). The lesson file also differs from its scratch draft, which points to a later edit after the copy.

## 2. corpus/ and reports/round-95 __pycache__ / *.pyc — PASS

Command: find corpus reports/round-95 \( -name __pycache__ -o -name '*.pyc' \) -print
- T1 14:37:05 empty; T2 14:37:13 empty; T3 14:40:22 empty; T4 14:40:28 empty; T5 14:43:31 empty.
- Also searched the wave dir (.ufo/waves/round-95): empty at T5.

## 2b. Whole-lane pycache — FAIL (outside the checked scope, pre-wave)

- reports/round-94/__pycache__/c1_k_admit_counter3.cpython-314.pyc, 46897 B, mtime 14:23:14.520.
- Ignored by .gitignore (git status --ignored shows "!! reports/round-94/__pycache__/"), so the tracked status hides it.
- Timestamp matches scratch dir /fast/scratch/hyaku/revenger-r95/dbg-s_fq4ckt (14:23:14.521): a debug import of the frozen r94 counter without -B, before any seat spawned (w1-spec.json at 14:34:30). Not a seat write.
- Impact: the frozen r93/r94 instrument directory now contains a compiled artifact. Tracked bytes are unchanged. The L1 should delete the directory. This seat did not touch it.

## 3a. /tmp write roots in w1 — PASS

grep -rIlE '/tmp' .ufo/waves/round-95/w1 → no output (T5). /tmp hits in wave-level files (w1-spec.json, w1-dispatch.json, w1-plan.out, w1-run.out) are the rendered task text quoting the /tmp rule, not seat writes.

## 3b. sysctl / sudo / pacman invocations in w1 — PASS

grep -rIlE '/tmp|sysctl|sudo|pacman' .ufo/waves/round-95/w1 → one file: w1/ScoutReopen.md (line 61: "No tools installed, no sudo, no host sysctl touched"). Negative statement; no invocation found. The w1/ExecCensus outputs mention no pacman or sudo.

## 3c. Host tool installs — PASS

find /home/vgpnk/.local/bin -maxdepth 1 -newer .ufo/waves/round-95/w1-spec.json → none. No tool installs recorded in the wave.

## 4. Fleet root integrity — FAIL (misroot)

git -C /home/vgpnk/Projects/shokunin status --porcelain at T5:
- M .scratch/run15-state.json — mtime 14:30:04, fleet orchestrator state (labels RevengerR95 seat roster). Not a seat write.
- ?? .ufo/closure-kaidoku-r92.json — mtime 10:13:39, predates the wave.
- ?? evb.ts — **MISROOT**. Fleet root, mtime 14:39:35.169, 22885 B, a TypeScript source (imports evidenceErrors.js, result.js, evidence.js, residualUnknown.js, immutableJson.js) — REA evidenceBundle.ts content. Written inside the fleet root during the wave. No lane path, scratch file, or wave file references "evb" (grep -rlE '\bevb\b|evidenceBundle\.ts' over the wave and scratch dirs, minus dbg-s_fq4ckt, returned only mirrors and copies of the SOURCES/ledger files, none naming evb.ts). Attribution: UNRESOLVED. Candidates by timestamp are seats writing at 14:38–14:40 (ConnectorOverlap, ExecReceipts, ReviewerBlind). The shape of the file (a raw REA source fetch with a bare relative name) suggests a fetch run with cwd = fleet root. Fleet owner should remove it. This seat did not remove it.
- Earlier at T0 the fleet status also showed ?? .ufo/reports/round-94/kotodama.md (sibling kotodama, 14:34:43); it was not present at T5.

Other fleet-root writes in the window (not seat-attributable, fleet orchestrator): .ufo/state/disk-guard.log (14:35:04), .ufo/state/inline-dispatcher.log (14:35:11), .ufo/watchdog.log, .ufo/prompts/kagi-round-43.md. None reference a seat path other than the revenger launch line.

Sibling lanes (read only): kotodama-shokunin modified LOG.md (14:31:28), SCORECARD.md (14:32:02), corpus/SOURCES.md (14:30:46), tools/check-advance-evidence.py (14:30:46). kotoba-shokunin untracked round-92 items (pre-wave). No revenger seat path is in those files. Sibling activity, not this wave.

## 5. Per-seat output bounds — PASS for dirs present

Each seat dir under w1/ holds only its own outputs (T5):
- ConnectorOverlap/ (measurement-r95.tsv, connector.md) + ConnectorOverlap.md
- ExecBattery/ (red-v3.log, full.log, battery-repro.md) + ExecBattery.md
- ExecCensus/ (assimilation/{reg-ids,staged-ids,collisions}, census-assimilation.md, census-validate*.tsv, *.stderr) + ExecCensus.md
- ExecFrozen/ (digest.txt, freeze-state.md) + ExecFrozen.md
- ExecReceipts/ (receipts_field_audit.py, receipts-audit.md) + ExecReceipts.md
- ReviewerBlind/ (derivation.md, vote.json) + ReviewerBlind.md
- ScoutCiteback/ (cite-back-sweep.md) + ScoutCiteback.md
- ScoutReopen/ (receipts/{fetch-log.md,fetch-time.txt,raw/S500.body,raw/S501.body}, reopens.md) + ScoutReopen.md
- swarm-registry.json at w1/ (orchestrator file, mode 600)

Not yet written at T5: ScribeLesson, ReviewerGate, CriticR95, MutationR95. Each has scratch activity only.

Scratch deletion at yield is not yet checkable for the running seats.

## 6. jj op-store writes after wave start — PASS

find .jj -newer reports/round-95/claims.md → 36 files, newest 14:30:00.787 (freeze commit time). No .jj writes after the wave's first seat output (14:35).

## 7. Out-of-lane absolute path references in w1 — INFO

grep -rhoE '/home/vgpnk/Projects/shokunin/[A-Za-z0-9._-]+|/home/vgpnk/Projects/shokuknow[^ ]*' .ufo/waves/round-95/w1:
- /home/vgpnk/Projects/shokuknow (1): ExecCensus/census-assimilation.md:4 says read-only, no write.
- /home/vgpnk/Projects/shokunin/scripts (1): ExecCensus/census-assimilation.md:8 runs scripts/sources-census.sh validate. This is a fleet-root script; the seat reports it read-only but the script itself was not inspected by this audit. Note for the L1.
- /home/vgpnk/Projects/shokunin/revenger-shokunin (5): lane paths.

## Blocking items for the L1 / integrator

1. Name the writer of SKILL.md, corpus/README.md, corpus/SOURCES.md, corpus/lessons/round-94.md, corpus/lessons/round-95.md (check 1). Confirm that no seat wrote them.
2. Remove fleet-root evb.ts (check 4) and identify the seat that wrote it. The fleet owner should do this; this seat did not.
3. Delete reports/round-94/__pycache__/ (check 2b). Use `python3 -B` for future counter runs of frozen instruments.
4. Re-run the pycache and dirty-path check after the four missing seats finish.
