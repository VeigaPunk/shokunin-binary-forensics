# VoterGateR99 — findings (round 99, wave w1)

Seat: VoterGateR99 (reviewer). Two votes cast this wave on the C14 candidate
`corpus/knowledge/round-98-rea-host-readiness.md`; the second, on Amendment B digest
`246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da`, is the counting vote.

## Round 1 — digest 36cc6ac2… (claims freeze 7e6edd4): Q16 FAIL, upheld

- Recomputed digest with v7's `digest()`: `36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5` (matched).
- Finding: the derivation row `scope-check classes` (entry line 80) recorded
  `` `10 config_drift` / `11 healthy` / `3 missing_analysis_engine` `` for a command whose actual
  stdout (cat -A) is `     10 classification: config_drift` / `…classification: healthy` /
  `…classification: missing_analysis_engine` — the `classification:` token absent three times, so
  the preamble's "the outputs are those commands' actual stdout" (line 65) and the §Q-map Q16
  row-by-row claim (line 137) were false. My sweep of all 23 rows: 22 reproduced exactly; this row
  was the sole exception. Voted Q16 FAIL; everything else PASS/n/a.
- The L1 upheld the FAIL and spent the amendment budget (Amendment B, commit `9ddd38ac…`).
  Pre-amendment bytes and my first vote live in `.ufo/waves/round-99/w1/superseded-votes-digest-36cc6ac2/`;
  first audit: `gate-audit-36cc6ac2.md`.

## Round 2 — Amendment B, digest 246d09a8… (commit 9ddd38ac): all 17 PASS/n/a, zero FAIL

- Digest recomputed with v7's rule: `246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da` — matches.
- **My Q16 finding is fixed at the source**: the scope-check-classes command now strips the prefix
  and padding (`sed 's/^classification: //'`, `sed 's/^ *//'`), and the preamble states a cell rule
  (one code span per stdout line, ` / `-joined; em-dash text is annotation; record-digest names are
  the rest of the stdout line).
- **deriv_check run by this seat, both directions**: amended entry → `DERIV_ROWS=29
  DERIV_MISMATCH=0`, rc 0, all rows MATCH; pre-amendment bytes (git show to scratch) →
  `DERIV_ROWS=21 DERIV_MISMATCH=7`, rc 1, including exactly my flagged row. The instrument is shown
  able to fail and its 0-mismatch claim is true.
- Amendment B's other fixes verified: analyzeHeadless cause clause removed (exit now credited to
  the transcript, which prints rc=1; launcher path now derived, genuinely under
  `/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC`); "(of 8" denominator now derived as its own row
  (ghidra-named 8, healthy 8); substep status tied to `operation: inventory_artifact` (`grep -A1`);
  members+sizes, root digest, truth.json digest, host identity, skill identity and binwalk/unblob
  zero all newly derived rows, all MATCH; S507's cell no longer cites "exit 1" as a record fact
  (doctor record has 0 exit/rc lines — recounted). Em-dash annotations accurate ("grep exits 1 on
  zero matches" observed; three comma-separated paths on one line observed).
- Side change noted, outside this entry's object: S505's `used-by` cell retargeted to
  `corpus/lessons/round-97.md` (S505 is not cited by this entry; S-id census: S506 18, S507 5).
- Decisions: Q01–Q06, Q09–Q11 PASS; Q07, Q08, Q12–Q15, Q17 n/a; **Q16 PASS** (was FAIL). Q13
  examined under its stricter reading because the §Q-map now credits deriv_check.py: the credit is
  bounded to what the run detects (demonstrated 7-vs-0 by my runs), so no reject condition is met;
  kept n/a. 17/17 agreement with the entry's §Q-map.
- Carry-over re-verification on the amended bytes: headers 6 lines intact; quotes 1 each; S506
  receipt verified; truth.json/fixture equality; transcript 13/13 paired blocks with all claimed
  values and exits; doctor 0 exit lines; S507 anchor byte-exact (41 bytes); fixture last touched at
  `5c9fb20` (round 2); lint own run `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0` rc 0; host
  identity matches `uname`.

## Vote and self-check

- Vote: `reports/round-99/votes/VoterGateR99.json` — 17 decisions (10 PASS / 0 FAIL / 7 n/a),
  bound to `246d09a8…`, artifact `.ufo/waves/round-99/w1/VoterGateR99/gate-audit-246d09a8.md`
  (sha256 `7aee4ce879ceff5201a14b164c59d4934c14625bb952593146d9aa703d1c1ca0`).
- Self-check (v7 `check_vote_notes` rule + distinctness vs my superseded notes and CriticR99's
  notes): `SELFCHECK OK`, rc 0.

## Residual risk / gaps

- Q14/Q15 recorded n/a (rule has no object) where CriticR99 recorded PASS-with-evidence; both
  record no violation and neither fails the counter. Q13 kept n/a with the bounded-credit reasoning
  documented in the audit; a stricter seat could score it PASS — still no FAIL either way.
- The em-dash annotation convention leaves annotation text outside machine comparison; both
  annotations were manually verified true this pass.
- No counter run by this seat on any tree; C1's verdict belongs to the post-freeze counter runs.
- No tools installed or upgraded (none needed). Nothing outside my write scope modified; scratch
  cleaned after receipts were copied.

## Files written

- `reports/round-99/votes/VoterGateR99.json` (current, Amendment B digest)
- `.ufo/waves/round-99/w1/VoterGateR99/gate-audit-246d09a8.md`
- `.ufo/waves/round-99/w1/VoterGateR99/gate-audit-36cc6ac2.md` (superseded first audit, kept as evidence)
- `.ufo/waves/round-99/w1/VoterGateR99/derive_check.sh`, `derive_check.out`, `check_my_vote.py`,
  `check_my_vote_b.py` (receipts)
- `.ufo/waves/round-99/w1/VoterGateR99.md` (this file)
