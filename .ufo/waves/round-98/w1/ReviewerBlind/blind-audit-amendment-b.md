# Blind audit — ReviewerBlind, revenger round 98 — Amendment B re-audit (C14 candidate)

Seat: ReviewerBlind (reviewer). Independent re-audit after Amendment B; still
blind to every other seat's vote and audit file (ReviewerGate.json and
CriticR98.json were never opened).

New vote-binding digest (normalized per the v6 `digest()` rule):
`73f1d7e044df04373a36c1f94f7e7216a7a513043ef769d5567a98cb53dd80e7`
Supersedes `1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8`
(my prior vote, kept by the L1 in
`.ufo/waves/round-98/w1/superseded-votes-digest-1ea9260c/`).

Amendment commit: `0146c0a`; base of the diff: `cf8a9d4`; original claims
freeze: `9d49002a3804de48d365b7d32849ada06745d64f`. All frozen record bytes
still read at `9d49002` — the amendment touched only the entry text
(`corpus/knowledge/round-98-rea-host-readiness.md`) and `reports/round-98/claims.md`.

## What Amendment B changed (verified from `git diff cf8a9d4 0146c0a`)

1. A `## §Q-map` section appended with exactly 17 rows, Q01–Q17 (counted).
2. Derivation table gained rows: "ghidra scope checks healthy" and
   "installation paths" (two new), plus "S506 body length" (split out of the
   digest row, which no longer carries a byte count in the same clause).
3. Route row 1 reworded: "Hopper was absent during this run." →
   "Doctor reported Hopper missing the same day (record 1)."; the Observation
   sentence reworded the same way ("on the same day that doctor reported
   Hopper missing").
4. claims.md gains the Amendment B section describing exactly this change and
   naming the new digest.

Nothing else in the entry changed (diff hunks exhausted; entry bytes
10483 → 13824).

## New digest verification

`git show 0146c0a:corpus/knowledge/round-98-rea-host-readiness.md`, normalized
(`admission-status:` lines → `admission-status: candidate`; the entry carries
exactly one such line, still `candidate`), sha256 =
`73f1d7e044df04373a36c1f94f7e7216a7a513043ef769d5567a98cb53dd80e7` — matches
the Amendment B binding digest. The working-tree entry carries the same bytes.

## Named lint probe (Amendment B's command, re-run by this seat)

`PYTHONUTF8=1 python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-98-rea-host-readiness.md --lane .` from the lane root:

```
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
rc=0
```

Matches the Amendment B claim verbatim, exit 0 observed by this seat.

## New derivation rows — re-derived against the frozen record (9d49002)

1. `sed -n '/^scope_checks/,/^informational_checks/p' corpus/live/runs/round-98/rea-doctor-r98.txt | grep -A1 '^  - name: ghidra' | grep -c '    ok: true'` → **8**; and the same range contains exactly **8** `^  - name: ghidra`-prefixed check names. Recorded "8 (of 8 ghidra-named scope checks)" is exact.
2. `grep -c '^    paths\[3\]: ' …rea-doctor-r98.txt` → **1**; `grep -c '^    state: multiple' …rea-doctor-r98.txt` → **1**. Recorded "`1` and `1`" is exact (the `paths[3]` line is the three fnm_multishells paths; `state: multiple` is the installation-paths state).
3. `wc -c < reports/round-98/quote-receipts/raw/S506.body` → **16650**. Exact.

## Reworded clauses — accuracy against the record

- "Doctor reported Hopper missing the same day (record 1)": the frozen doctor
  record reports `hopper` with `classification: missing_analysis_engine` and
  `ok: false` (verified again this pass); "record 1" is the doctor receipt,
  item 1 of the entry's S507 record list; all three S507 records are dated
  2026-11-05. The new wording is more precise than the old one — a doctor run
  and the inventory run are separate runs — and removes the old implication
  that Hopper's absence was probed during the inventory run. Q05 hygiene
  improvement, no claim weakened.
- Observation "on the same day that doctor reported Hopper missing": same-day
  claim is carried by the saved-record dates (2026-11-05); accurate.

## §Q-map — independent cross-check

All 17 rows present with non-empty decisions. The entry's own Q-map marks
Q06, Q14, Q17 as n/a where my audit marks PASS; my notes below record the
labeling difference. No Q-map row claims anything my re-derivation
contradicts. Specifically:

- Q-map Q16's supporting sentence "'Doctor has no binwalk or unblob check'
  refers to the record bytes" — verified: `grep -ci 'binwalk|unblob'` over the
  frozen doctor record → 0.
- Q-map Q14's n/a reason ("No hex string is quoted with a byte count in the
  same clause") is now literally true post-amendment (the only pairing, the
  S506 digest row, was split). Verified by scan: zero hex+byte-count pairings
  remain. Note: the pre-amendment pairing was itself correct (16650 bytes was
  the body's true length), so this was hygiene, not an error fix.

## Per-Q decisions on the amended entry (independent of the entry's Q-map)

- Q01 **PASS** — unchanged from the superseded audit: S506 (tier-A docs row,
  pinned `12f6e09`, opened 2026-11-05, body+receipt committed) and S507
  (own-work record saved 2026-11-05) carry every load-bearing claim; "ready on
  this host for this fixture" stays inside S507's "not other hosts, dates or
  routes" boundary.
- Q02 **PASS** — headers unchanged and complete (two `source:` lines with
  pinned commit/paths, `verified-at: 2026-11-05` with body+fetch-log paths,
  `recheck:` naming re-open/re-run/re-derive targets, `coverage-map: C14`).
- Q03 **PASS** — expectations still come from outside the record under test:
  `truth.json` (fixed round 2) for the inventory, receipt span 7126–7202 and
  body digest for S506; re-derived by command this pass.
- Q04 **PASS** — tool/version/function named (REA CLI 6.7.0, provider
  `rea-artifact-graph` v1); only tool-printed output scored; version rows
  labeled probe outputs.
- Q05 **PASS** — probe classes carried per row; the only capability row
  (ZIP inventory) has command/date/exit/Evidence ID; the reworded Hopper
  clause now states the configuration observation precisely (doctor's report,
  separate run, same day) instead of an ambiguous during-run absence.
- Q06 **PASS** (entry's Q-map says n/a) — my independent call: the criterion's
  reject condition ("a size or count stated from intent rather than from the
  built bytes") is not met — every fixture-derived value is stated from
  `truth.json`/record and re-derived by command; the entry does state
  fixture premises, so the criterion applies and is met. Labeling difference,
  not a failure.
- Q07 **n/a** — no parser accept/refuse/cause prediction offered.
- Q08 **n/a** — superseded by Q11, applied in full.
- Q09 **PASS** — digests bind exact committed bytes; none offered as origin/
  completeness/authenticity; "treats no digest as authenticity or origin"
  retained.
- Q10 **PASS** — one host, one date, REA 6.7.0, per-shell PATH, one fixture;
  unprobed routes labeled unprobed.
- Q11 **PASS** — strengthened by the amendment: the two route-table counts
  that previously leaned on the record prose (8 ghidra checks; installation
  paths) now each carry a derivation row, re-derived by this seat with
  matching outputs. Every count, identifier and digest now has command +
  recorded output in-entry.
- Q12 **n/a** — no rejected row load-bearing.
- Q13 **n/a** — no verifier credited as guarding a clause.
- Q14 **n/a** (changed from PASS in the superseded vote) — post-amendment no
  hex run carries a byte count in the same clause, so the criterion's length-
  consistency duty has no object; the amendment's digest/length split is the
  reason (hygiene; the pre-amendment pairing was correct). The lint's
  `LINT_Q14=0` concurs.
- Q15 **n/a** — no lane-tree git identity sentence; the pinned REA revision
  is part of a fetched URL, not a lane-tree identity claim.
- Q16 **PASS** — every command-credit sentence matches that command's stdout
  (including the two new rows and the "Doctor has no binwalk or unblob check"
  sentence, verified against the record bytes).
- Q17 **PASS** (entry's Q-map says n/a) — my independent call: all cited paths
  resolve at the amendment commit; no relocated pointer, so the criterion's
  reject condition has no instance. No failure either way.

No FAIL. The amendment introduced no defect: every changed byte was
re-verified against the frozen record, the new digest binds, and the named
lint exits 0 on this seat's own run.

## Artifact binding

`artifact_sha256` of this file's bytes is recorded in
`reports/round-98/votes/ReviewerBlind.json`, which binds digest
`73f1d7e044df04373a36c1f94f7e7216a7a513043ef769d5567a98cb53dd80e7`.
