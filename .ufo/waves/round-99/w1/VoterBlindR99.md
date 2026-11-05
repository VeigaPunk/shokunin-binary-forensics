# VoterBlindR99 — blind vote findings, revenger round 99 w1

Seat: VoterBlindR99 (reviewer, pinned). Blind protocol held: no round-99 vote file, no other
seat's audit, and no round-98 critic/reviewer audit was read before the vote was cast. Inputs:
the candidate entry, corpus/QUALITY.md, corpus/SOURCES.md, corpus/README.md, S506 committed body
+ fetch log, the three S507 records, corpus/fixtures/archive-r2/truth.json, the 2026-10-12
checklist, and frozen v7's digest/check_vote_notes source. The round-99 claims file was read as
the goal file directs; its predicates were treated as frozen and never edited.

## Files written (all under the lane repo)

- `reports/round-99/votes/VoterBlindR99.json` — the vote (strict JSON, 17 decisions, 17 notes)
- `.ufo/waves/round-99/w1/VoterBlindR99/blind-audit-36cc6ac2.md` — audit artifact
  (sha256 `c14e2f3b03f52077b98012a8629aa295dce527dbe1fe16430031f9a51ee2ed27`)
- `.ufo/waves/round-99/w1/VoterBlindR99/derivations-rerun.txt` — receipt of every re-run command
  (sha256 `67bdb246d57007b1fe1078d9c78ce275599b21a6ee3b2ad9b7b68fbecbce154f`)
- `.ufo/waves/round-99/w1/VoterBlindR99/run-derivations.sh` — the exact runner
  (sha256 `13213116adc4ac3c272c308ff210db3d87af459902d4f50e066234c5e714a009`)

## Verdict

Vote cast against digest `36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5`
(recomputed with frozen v7 `digest()` on the worktree entry: match, `MATCHES_FROZEN=True`).

- Q01-Q06 PASS, Q09-Q11 PASS, Q16 PASS (10 PASS)
- Q07, Q08, Q12, Q13, Q14, Q15, Q17 n/a — each with a located reason (the only grep hit for the
  trigger language is the entry's own map row; Q08 superseded by Q11 at corpus/QUALITY.md:23)
- Q09 recorded PASS, never n/a (the entry carries 64-hex digests; v7's applicability rule honored)
- 0 FAIL

Self-check with the real v7 `check_vote_notes` (extracted by AST, PROFILE="c14", votes dir
holding only my vote): `ok=True`, `ok; Q09 applicability checked against 64-hex digest claims`.
Exit codes observed: all derivation/probe re-runs rc=0; the two `grep -c` absence checks (rc=1,
count 0) are the expected no-match exits.

## Evidence highlights

- All 21 derivation-table rows reproduced byte-for-byte from the lane root, including the fixed
  "three installation paths" row: `paths[3]` line (doctor record line 316) holds three
  comma-separated fnm_multishells paths and the new command prints `3` (old count-by-lines
  behavior would print 1).
- All four S506 quotations verified as byte-exact substrings of the committed body (lines 22,
  34, 26); the marked paraphrase matches body lines 35-37 exactly as attributed. Unquoted
  locator prose was never used as a quote match.
- Every version string credited to the probe transcript (rea 6.7.0, jadx 1.5.6, java 21.0.13,
  binwalk 3.1.0, unblob 26.6.4) is printed there with its own command and rc= line; the
  doctor-printed versions (ghidra 12.1.4, java 21.0.13) are derived inside the entry from the
  doctor record.
- truth.json (round-2 expectation source) matches the evidence on archive digest, root size and
  member sizes; member sha256s in the evidence equal truth.json's (extra corroboration, not
  cited by the entry).
- The K05 correction sentence is accurate: the 2026-10-19 re-probe row (checklist line 40,
  inside `## Re-verification 2026-10-19`) records "pwntools import fails"; the round-98 probe
  rc=0 corrects it. The line-61 row belongs to the 2026-11-04 section.
- All twelve corpus/reports paths cited by the entry resolve at the lane root.

## Residual risks / observations (no Q failure)

1. Doctor exit code 1 and inspect exit code 0 are session observations, derivable from nothing
   in the lane (both records carry no rc= line); the entry discloses this honestly. If either
   record were regenerated, the two exit codes would have nothing to re-check against.
2. PASS-note distinctness across voters cannot be coordinated under the blind protocol; my
   notes embed seat-specific commands and full outputs to minimize verbatim collision risk.
3. I did not run corpus/lint_entry.py or any counter — not in this seat's assigned probes; the
   lint/log lines in claims.md remain L1/executor verification surface.

## Tooling

No tools installed or upgraded; stock coreutils/python3 sufficed. Scratch
`/fast/scratch/hyaku/revenger-r99/VoterBlindR99/` deleted before yield; receipts copied to the
wave dir first. No git/jj mutation anywhere; read-only commands only.

---

# Amendment B re-vote (supersedes the vote above)

RevengerR99 instructed a full blind re-vote after Amendment B (lane commit `9ddd38a`); my vote on
`36cc6ac2…` was moved to the superseded dir and was never re-read. Blindness held for the second
round too: no vote file, no other seat's audit, no round-98 critic/reviewer audit, and no
claims.md amendment FAIL text. I read only the entry's own diff since `7e6edd4` to scope the work.

## Verdict (Amendment B)

Digest recomputed with frozen v7 `digest()`: `246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da`,
`MATCHES_246d09a8 = True`; entry still `admission-status: candidate`.

- **11 PASS** (Q01-Q06, Q09-Q11, Q13, Q16), **6 n/a** (Q07, Q08, Q12, Q14, Q15, Q17), **0 FAIL**.
- Vote: `reports/round-99/votes/VoterBlindR99.json`; audit:
  `.ufo/waves/round-99/w1/VoterBlindR99/blind-audit-246d09a8.md`
  (sha256 `8bacb5f977e44f28f328eae7ad161ed904db9bc825d7affebb297919b4d65107`); receipt:
  `derivations-rerun-amended.txt` (sha256 `e99af3f3b10b749423bd4eecf08aa7307ee8dff7fd5c6530df7f3c4448bb91f1`).
- Self-check with the real v7 `check_vote_notes` (PROFILE=c14, my vote alone in a scratch votes
  dir): `ok=True`, `ok; Q09 applicability checked against 64-hex digest claims`.

## Amendment-B evidence (all re-run this round, exit codes observed)

- All 29 amended derivation rows re-ran byte-identically with my own runner (independent of the
  entry-cited control): host identity, healthy 11 / failing 13, classes 10/11/3, 14 registration
  pairs (4 aligned / 1 manual / 8 missing / 1 stale), missing-or-stale 9, ghidra-named 8 and
  healthy 8, headless launcher path, doctor versions 12.1.4 / 21.0.13, engine/jadx pairs, skill
  identity stale, binwalk/unblob count 0 (grep rc=1, matching the cell's em-dash annotation),
  paths 3, `state: multiple`, cli 6.7.0, evidence ID, substep status anchored to
  `operation: inventory_artifact`, members `. 2964 / README.txt 84 / bin/checksum 16160`, root /
  truth.json / fixture digests all `857989f5…`, record digests with the awk-rendered names,
  S506 body `ce2d122b…` / 16650 bytes.
- The entry's Q11/Q16 credit to `reports/round-99/controls/deriv_check.py` is true: my run
  printed `DERIV_ROWS=29 DERIV_MISMATCH=0`, exit 0. I also demonstrated its guard scope on two
  scratch mutants (lane untouched): deleted output cell → `MISMATCH … DERIV_MISMATCH=1` rc=1;
  corrupted command path → `MISMATCH … DERIV_MISMATCH=1` rc=1.
- S506 quotes byte-exact (body lines 22, 34, 26; paraphrase lines 35-37); K05 correction
  accurate; rc= absent from both records so the session-observation disclosure for exit codes 1/0
  stands; 14/14 cited paths resolve.

## Decision notes

- Q13 moved n/a → PASS: Amendment B credits a verifier (deriv_check.py) inside the entry, and the
  credit exactly equals its own run's detection (shown by the mutants); the transcript-sourced
  values and session exit codes are named as outside the table. The entry's own Q13 map row still
  reads "No verifier is credited as guarding a clause" — stale rationale wording; the criterion's
  reject condition (a guard whose check survives deletion) is nowhere met, so this is an
  observation, not a failure.
- Q14: the record-digest cell's `…` is now the awk command's own output, so even the truncation is
  command-printed bytes, not entry-side elision — n/a stands.
- Observation: the amendment commit also reworded the S507 SOURCES row prose (registry is L1
  surface); tier A / own-work / opened 2026-11-05 unchanged, so Q01/Q02 unaffected.

Scratch deleted after copying receipts; no tool installs; no git/jj mutations; frozen bytes
untouched by me (mutants lived only in `/fast/scratch/hyaku/revenger-r99/VoterBlindR99/`).
