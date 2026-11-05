# CriticR98 findings: round 98, wave w1

Seat: CriticR98 (critic). Axes: calibration (C2), coverage (C1). No commit, stage or push. No v7 run. No counter run on any tree with C14 held. No install.

## Status after Amendment C (lane commit 1b76b4d)

Vote and audit are bound to candidate digest `6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f`.

Decisions: FAIL on Q11 and Q16; PASS or n/a elsewhere. Both FAILs fail `C1_VOTES` and therefore C1, per the claims.

- **Q11 (FAIL, narrow).** The registration counts (14; 4 aligned, 1 manual, 8 missing, 1 stale; 9 missing or stale), the eight ghidra checks, the scope counts and the classes are now derived. "Doctor lists three such installation paths" is not: its rows print `1` and `1`. Deriving command that does give 3: `grep '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt | cut -d: -f2 | tr ',' '\n' | grep -c .`.
- **Q16 (FAIL).** The preamble says each version string comes from the probe transcript. `ghidra-version 12.1.4` is printed by the doctor record only (0 occurrences in `host-probes-r98.txt`).
- Verified and accepted: the preamble's transcript structure (13 `$` lines, 13 `rc=` lines, none unpaired); the disclosure that doctor exit 1 and inspect exit 0 are not record lines; Q06 PASS (archive-r2 sha256 857989f5… equals truth.json `archive_sha256`); the lint on the 1b76b4d corpus extract (`LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, rc 0).

## Deliverables

| Path (repo-relative) | What it is |
|---|---|
| `reports/round-98/votes/CriticR98.json` | vote bound to `6d27c129…`; artifact `critic-audit-6d27c129.md`, sha256 `1209dc7dcd47b175f4b8c9f8e5f00a875ddc73df21ed9b1fb23015b3a25dd33e` |
| `.ufo/waves/round-98/w1/CriticR98/critic-audit-6d27c129.md` | re-audit of the Amendment C candidate (the vote artifact) |
| `.ufo/waves/round-98/w1/CriticR98/critic-audit-73f1d7e0.md`, `critic-audit.md` | superseded audits (digests 73f1d7e0… and 1ea9260c…), kept unchanged |
| `.ufo/waves/round-98/w1/CriticR98/fresh/build_fresh98.py` | holdout builder, pinned to base 1b76b4d and digest 6d27c129; `--c14-variant candidate` only |
| `.ufo/waves/round-98/w1/CriticR98/fresh/MANIFEST.sha256` | sha256 of the builder, vector specs, overlays, results and the v6 log (70 files) |
| `.ufo/waves/round-98/w1/CriticR98/fresh/vectors/c02/fixture/`, `vectors/c14/candidate/` | vector specs (`vector.json`, `changed/`, `removed.txt`); c02 also `counter.log` |
| `.ufo/waves/round-98/w1/CriticR98/fresh/results-c02-fixture.json`, `results-c14-candidate.json` | per-vector records |
| `.ufo/waves/round-98/w1/CriticR98/fresh/v6-holdout-run.log` | stdout of the frozen-v6 c02 run, rc 0 |

## Holdout: 12 new named forgeries (6 per profile)

Each class is new against r97 FR01 to FR12 and r96 FG01 to FG20 (and the r96 self-test deltas where they touch the same leg):

| # | Name | Class | Why new |
|---|---|---|---|
| C02-V01 | hidden-dissent-uppercase-vote | a FAIL vote saved as `ReviewerBlind.JSON`, outside the `*.json` glob | FR05 binds an artifact sha; FG05 and FG06 are artifact and symlink; self-test F12 is a case-duplicate seat. None reads a vote filename outside the glob. |
| C02-V02 | qid-list-as-na-reason | n/a reason made only of criterion ids | FR10 is boilerplate on a flipped PASS; F17 is `-`; V18 a letter flood. This passes the six-token and names-a-Q-id test with no content. |
| C02-E01 | recheck-names-no-command | `recheck: none` | FR09 is a stale verified-at value; FG14 a shifted trio line; the self-test deletes the line. This keeps the line and empties its value. |
| C02-E02 | two-run-clause-count | a clause with two hex runs, one count wrong | The Q14 lint skips clauses with more than one run. No FG or self-test covers it. |
| C02-E03 | coverage-map-other-row | entry `coverage-map: C05` while README C02 cites the entry | FR03/FR04 change README rows; FG15 is a Q-map row. The entry's own coverage header is unchecked. |
| C02-R01 | held-row-backed-by-candidate | held C06 cites the round-98 candidate (unadmitted, other round) | FR03 deletes the entry; FR04 changes an unrelated cell; FR06/FR07 duplicate rows. K counts file existence only. |
| C14-R01 | suffix-row-outside-count | held row `C14a` inserted after C14 | FR06/FR07 duplicate existing ids; self-test ROWS-total-extra-row adds C16. A suffixed id is invisible to the `C[0-9]+ ` regex. |
| C14-V01 | placeholder-pass-note | PASS decision on ReviewerGate Q09 with note `ok` | FR10 flips a PASS to n/a with boilerplate; this keeps PASS and writes a placeholder. |
| C14-V02 | fail-under-extra-key | FAIL under key Q18 | F13, V04 and F17 are other vote defects; none reads keys outside Q01 to Q17. |
| C14-Q01 | receipt-span-shift | S506 receipt span moved +1 byte | FG09 is an irrelevant quote; V27 a foreign body; QUOTES-mutated-body changes the body. This names other bytes. |
| C14-O01 | ownwork-pointer-foreign-round | S507 source re-pointed to the existing `corpus/live/runs/round-96/` | FR12 is a dangling pointer. This pointer exists and names another round's record. |
| C14-L01 | fetchlog-date-vs-receipt | fetch-log header 2026-11-04; receipt fetched_at 2026-11-05 | FG19 is a merged log line; V10 a stale receipt date. This pairs two valid-looking dates that disagree. |

### Results

Frozen v6, c02 (observed on this host; log `v6-holdout-run.log`):

```
CONTROL-honest | rc=0 | pass | K=13/15 | control-ok
C02-V01 | rc=0 | pass | ACCEPTED
C02-V02 | rc=0 | pass | ACCEPTED
C02-E01 | rc=0 | pass | ACCEPTED
C02-E02 | rc=0 | pass | ACCEPTED
C02-E03 | rc=0 | pass | ACCEPTED
C02-R01 | rc=1 | fail | refused (C1_ONLY_C02, C1_ADMITTED_UNION)
HOLDOUT98_CONTROL=control-ok
HOLDOUT98 accepted=5/6   rc=0
```

c14 (not run; the L1 runs v7). `--build-only` on base 1b76b4d: `C14_LANDING_BUILT variant=candidate entry_digest=6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f`, `HOLDOUT98_BUILD=ok vectors=6`, rc 0. The six c14 expectations are predictions from reading v6, not runs. The honest c14 control's lint is expected to pass (`LINT_QMAP=0` on 1b76b4d); it has not been run.

## Calibration hazards for the L1

**H1. The r97 honest control carries boilerplate PASS notes.** `c1_k_admit_counter6._fixture` writes `NA_NOTE` on PASS decisions Q02, Q09, Q10 (and an NA_BY_Q note on Q01). v6 does not read PASS notes. C1_VOTE_NOTES is a new leg for both profiles, and the claims require the v7 c02 profile to accept the FR00 control (C2_POSITIVE). A C1_VOTE_NOTES that rejects boilerplate PASS notes fails C2_POSITIVE; a lenient one passes C14-V01. The leg's definition needs a decision before the v7 freeze.

**H2. (Resolved.)** The candidate is lint-clean on 1b76b4d, so the c14 honest control is not confounded by C1_LINT. The qmap-dev variant was removed.

**H3. Interface hazard for ExecCounterV7.** v6's `check_receipts` has a `ref` map with S502 and S503 only. With `RECEIPT_ROW_IDS = (S506,)` in the c14 profile it raises KeyError unless v7 adds S506. Flagged from reading v6, not a v7 run.

**H4. Landing edits are incomplete in the claims' description.** The claims require a logged old-to-new correction of S505's used-by cell. The builder applies the cell edits only (status `queued`, used-by `—`). The log entry is not built; the L1 adds it on the landing commit.

**H5. Synthetic c14 votes.** The c14 honest votes, wave registry and artifacts are synthetic fixture bytes written by the builder. The base 1b76b4d has no seat votes, so the honest tree's votes are not evidence about the candidate.

## Tools

None installed or updated. Used: `git` (read-only: `archive`, `show`, `diff`, `rev-parse`), `tar`, `sha256sum`, `wc`, `grep`, `awk`, `sort`, `uniq`, Python 3.14 stdlib, and the lane's `corpus/lint_entry.py` on a 1b76b4d extract. Scratch removed after the final build.

## Open questions for L1

1. Q11 and Q16 are FAIL on digest 6d27c129; C1 misses on the frozen bytes unless the entry is amended again (the Q11 fix is the one command above, or a `recorded` label; the Q16 fix is to drop the transcript credit for `ghidra-version 12.1.4` or cite the doctor record).
2. H1: how C1_VOTE_NOTES treats boilerplate PASS notes, given the r97 control.
3. H3 and H4 for ExecCounterV7 and the landing commit.
