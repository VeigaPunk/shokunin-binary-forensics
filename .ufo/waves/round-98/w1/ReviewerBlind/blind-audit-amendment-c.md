# Blind audit — ReviewerBlind, revenger round 98 — Amendment C re-audit (C14 candidate)

Seat: ReviewerBlind (reviewer). Third independent pass; still blind to every
other seat's vote and audit file (ReviewerGate.json and CriticR98.json were
never opened; the CriticR98 findings were taken only from the Amendment C text
in claims.md).

Vote-binding digest (normalized per the v6 `digest()` rule):
`6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f`
Supersedes `73f1d7e044df04373a36c1f94f7e7216a7a513043ef769d5567a98cb53dd80e7`
(Amendment B) and `1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8`
(original freeze).

Amendment commit: `1b76b4d`; diff base: `0146c0a`; frozen record bytes still
read at `9d49002a3804de48d365b7d32849ada06745d64f`. The amendment touched only
the entry (`corpus/knowledge/round-98-rea-host-readiness.md`: derivation
preamble, three new rows, Q-map Q06 row) and `reports/round-98/claims.md`
(Amendment C section).

## What Amendment C changed (verified from `git diff 0146c0a 1b76b4d`)

1. Derivation preamble rescoped: the table claims only counts, identifiers and
   digests; version strings and exit codes are credited to the probe transcript
   `corpus/live/runs/round-98/host-probes-r98.txt`; the doctor exit code (1)
   and the `rea inspect-artifact` exit code (0) are disclosed as L1-session
   observations, "not lines of any record".
2. Three derivation rows added: client registration count (`14`), registration
   state split (`4 aligned / 1 manual / 8 missing / 1 stale`),
   missing-or-stale registrations ("nine") (`9`).
3. Q-map Q06 changed n/a → PASS (digest-verified premise evidence).

## Digest verification

`git show 1b76b4d:corpus/knowledge/round-98-rea-host-readiness.md`, normalized
(exactly one `admission-status: candidate` line retained), sha256 =
`6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f` — matches
the Amendment C binding digest.

## New derivation rows — re-derived against the frozen record (9d49002)

1. `grep -c '^    - client:' corpus/live/runs/round-98/rea-doctor-r98.txt` → **14**. Exact.
2. `awk '/^    - client:/{c=$3} /^      state:/{print $2}' … | sort | uniq -c` → `4 aligned` / `1 manual` / `8 missing` / `1 stale`. Exact.
3. same awk piped to `grep -cE '^(missing|stale)$'` → **9**. Exact — the
   Observation's "nine stale or missing client registrations" now derives.

## Rescoped preamble — accuracy against the records

- Probe transcript structure: all **13** `$ …` command lines are followed by
  printed output and an `rc=` line (0 blocks missing); `rea --version → 6.7.0`,
  `jadx --version → 1.5.6`, `binwalk --version → binwalk 3.1.0`,
  `unblob --version → 26.6.4` each verified present with their `rc=0` lines.
  The transcript credit for version strings is exact.
- Exit-code disclosure: `grep -i exit` over the frozen doctor record and the
  inspect record → **0 lines** in each. "Not lines of any record" is exact;
  the two exit codes (doctor 1, inspect 0) are now honestly labeled L1-session
  observations instead of implied record lines.
- The preamble's `\|` escape note matches the table's rendering.

## Named lint probe (re-run by this seat on the amended bytes)

`PYTHONUTF8=1 python3 -B corpus/lint_entry.py --entry <amended entry> --lane <lane>`:

```
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
rc=0
```

Matches the Amendment C claim; exit 0 observed by this seat.

## Per-Q decisions on the amended entry

- Q01 **PASS** — sources unchanged (S506 pinned docs row, S507 own-work record), boundaries intact.
- Q02 **PASS** — headers unchanged and complete.
- Q03 **PASS** — expectations still external (round-2 truth.json; S506 receipt span/digest); re-derived by command.
- Q04 **PASS** — strengthened: version values are now explicitly credited to the probe transcript (a record whose every block carries output + rc), so no tool output is restated without its record.
- Q05 **PASS** — probe classes unchanged; only the ZIP-inventory row is capability (command, date, exit disclosed, Evidence ID).
- Q06 **PASS** — my standing call from the Amendment B pass, now also the entry's Q-map decision: the ZIP route is a producer call whose premise (archive digest, member sizes in round-2 `truth.json`) matches the fixture bytes (`sha256sum` = `857989f5…e27e` = truth.json `archive_sha256`, verified by this seat in both prior passes and re-verified in the Amendment B pass); no size or count is stated from intent.
- Q07 **n/a** — no parser accept/refuse/cause prediction offered.
- Q08 **n/a** — superseded by Q11, applied in full.
- Q09 **PASS** — digests bind exact committed bytes; none offered as origin/completeness/authenticity.
- Q10 **PASS** — one host, one date, REA 6.7.0, one fixture; unprobed routes labeled.
- Q11 **PASS** — strengthened: every count, identifier and digest now carries command + recorded output (the three registration counts the critic flagged now derive exactly: 14; 4/1/8/1; 9), and the values not derived in-table are explicitly credited to the probe transcript or disclosed as session observations. No value rests on uncredited prose.
- Q12 **n/a** — no rejected row load-bearing.
- Q13 **n/a** — no verifier credited as guarding a clause.
- Q14 **n/a** — no hex run carries a byte count in the same clause (0 pairings scanned); lint `LINT_Q14=0` concurs.
- Q15 **n/a** — no lane-tree git identity sentence; the REA revision pin is a fetched-URL component.
- Q16 **PASS** — the preamble no longer credits the table with values it does not print; every credit matches stdout (all 13 transcript blocks, all derivation rows re-derived by this seat, "Doctor has no binwalk or unblob check" = 0 hits in the frozen record).
- Q17 **PASS** — all cited paths resolve at `1b76b4d`; no relocated pointer.

**No FAIL.** Final: 11 PASS (Q01–Q06, Q09–Q11, Q16, Q17), 6 n/a (Q07, Q08,
Q12, Q13, Q14, Q15).

Labeling note: my decisions now agree with the entry's §Q-map on Q06 (both
PASS); I keep Q17 PASS where the Q-map says n/a — a labeling difference, not a
failure (all cited paths resolve; no dead pointer exists).

## Artifact binding

`artifact_sha256` of this file's bytes is recorded in
`reports/round-98/votes/ReviewerBlind.json`, which binds digest
`6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f`.
