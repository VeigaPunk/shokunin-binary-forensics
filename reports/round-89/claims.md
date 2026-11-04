# round-89 claims (frozen before any landing or after-run)

Lane `revenger`, round 89 attempt 1. Lane repo
`/home/vgpnk/Projects/shokunin/revenger-shokunin`. Base
`2b017fa3c616a84b7b491e3312029fa8a8c076e6` (r88 adjudication + the r88
non-author spot-check). This file, the two sha-pinned instruments, the red
receipts, the blind-token control and the round-start census receipts are
committed as the freeze BEFORE the record/row landing and BEFORE any
after-run.

Two claims, distinct axes (freshness, coverage), causally separable, neither
exploratory. The lowest non-retired axis is coverage (K 8/15 = 5.3, F4
10/11 = 9.09); K stays operator-blocked (L0 r74 unanswered, re-read this
round), so the round's coverage claim takes the lowest **reachable** coverage
criterion, F4 — the r83–r88 routing shape, re-probed fresh this round rather
than asserted (the routing evidence is below, not a claim).

## Routing evidence for the lowest-axis obligation (not a claim)

`REA_JADX_MCP_JAR` is now SET on this host
(`/home/vgpnk/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar`)
and `jadx` is on PATH (`/usr/bin/jadx`, 1.5.6) — the r83–r88 "android hard
gate" no longer holds. The K blocker is unchanged: the r74 L0 question is
still unanswered in `.ufo/l0-questions.md`.

## C1 — freshness: the host-readiness census is re-derived against the live host (stale-unflagged rows 10 → 0)

Axis: **freshness** (stored assertions re-verified; the criterion whose
18-row marker count read 18/18 while ten rows stated host facts this host
contradicts). Not coverage: no map row changes.

Frozen counter: `corpus/census_reprobe.py` v1 (sha256 pinned below). It
re-derives each of the 18 census rows from the live host — PATH presence,
version commands, `import pwn`, the `rea` MCP entry's own `rea-agents@<v>`
spec, the skill directory's `*.md` listing, SKILL.md frontmatter, the skill's
own `rea-agents@` pin — and requires the row's last two cells (observed,
verdict) to state the observed value and not its opposite. The mint cell is
never scored (it legitimately records the old state).

- Rows: seed.md F01–F12 (5-cell shape) and
  2026-10-12-rea-readiness-checklist.md K01–K06 (4-cell shape).
- Predicate, one sentence: a census row MISMATCHES iff its observed+verdict
  cells fail to state the live value the frozen probe derives (or state its
  opposite); `CENSUS_STALE_UNFLAGGED` is the count of such rows.
- Target: `CENSUS_STALE_UNFLAGGED=0` over the landing tree. Red = 10
  (falsifies any claim of a smaller base).
- Counting command:
  `PYTHONUTF8=1 python3 -B corpus/census_reprobe.py --root <tree>` (exit 0
  iff 0; 1 if > 0; 2 missing input; 64 usage). `--selftest` is hermetic.
- Kill rules: (a) the eight `--selftest` legs must each hold, each planting
  one defect of one rule kind (`CENSUS_SELFTEST=pass`, exit 0); (b) the
  blind-token control (`reports/round-89/junk-control.log`) — every row's
  scored cells padded with every live token — must NOT reach 0 (it scores 7:
  the forbidden-opposite and version legs bite), so the target is not
  reachable by inserting tokens; (c) the base tree unchanged must score 10
  (`reports/round-89/census-red.log`), so a do-nothing control fails.
- Red receipt: `reports/round-89/census-red.log` (over
  `git archive 2b017fa3 corpus/knowledge`, live host probes) —
  `CENSUS_ROWS=18`, ten `CENSUS_MISMATCH` lines (F01, F03, F04, F07, F08,
  F12, K01, K03, K04, K05), `CENSUS_STALE_UNFLAGGED=10`, exit 1.
- Selftest receipt: `reports/round-89/census-selftest.log` (9 legs, pass,
  exit 0).
- Instrument pin: `corpus/census_reprobe.py` — the authoritative pin is the
  `sha256sum` line committed in `reports/round-89/instrument-pins.log` (this
  file does not pre-state a hash it cannot derive). The closure re-derives it
  with
  `sha256sum corpus/census_reprobe.py corpus/fixtures/apk-r65/oracle_check.py`
  over the freeze commit.

## C2 — coverage: the android family's first current-producer record (criterion F4, 10/11 → 11/11)

Axis: **coverage** — a named surface (the android family's producer route)
moves from unrecorded to recorded; no score is re-labelled and no existing
record is re-counted.

Frozen counters (both must hold):
1. `reports/round-81/f_probe4.py` (byte-unchanged, sha pinned below) over the
   landing `corpus`: `F4_COVERAGE=11/11`. Red over the base archive:
   `F4_COVERAGE=10/11` (`reports/round-89/f4-red.log`), with
   `inspect_android_package` absent from the operation census.
2. `corpus/fixtures/apk-r65/oracle_check.py` over the committed record:
   `ORACLE OK (19/19 checks)`, exit 0. The oracle re-hashes the committed
   fixture bytes against `truth.json` (premise leg) and derives every record
   expectation from those bytes — package name and the two declared version
   attributes from the authored AXML string table, `class_count` from the DEX
   header's own `class_defs_size` at 0x60, `resource_count` from the authored
   member table — never from the record (Q03).

- Target: F4 = 11/11 **and** ORACLE OK 19/19 over the committed record bytes.
  F4 alone is not the claim: F4 counts any record carrying `evidence_id` +
   `normalized_result`, so a fabricated record would move it.
- Kill rules: (a) a record-shaped forgery must not pass — the tampered control
  (package_name rewritten) scores `ORACLE FAIL (18/19)`, exit 1
  (`reports/round-89/oracle-tamper-control.log`); (b) the no-work control is
  the base archive at 10/11 (`reports/round-89/f4-red.log`), so the target is
  not reachable by doing nothing; (c) the producer must be the current
  provider (receipt: `rea --version` 6.7.0, provider `jadx` 0.7.1, command,
  exit, stderr, stdout sha256), and the two independent producer runs must be
  byte-identical, so the record is a reproducible producer output — not a
  provenance or authenticity claim (Q09).
- Red receipts: `reports/round-89/f4-red.log`,
  `reports/round-89/oracle-design.log` (oracle green over a scratch run),
  `reports/round-89/oracle-tamper-control.log`.
- Instrument pin: `corpus/fixtures/apk-r65/oracle_check.py` — sha256 in
  `reports/round-89/instrument-pins.log`; `reports/round-81/f_probe4.py` is
  byte-unchanged and its pin is re-derived there too.

## Separability

C1 touches `corpus/knowledge/seed.md`,
`corpus/knowledge/2026-10-12-rea-readiness-checklist.md`, `corpus/census_reprobe.py`
and the SKILL registry row for it. C2 touches `corpus/fixtures/apk-r65/oracle_check.py`,
`corpus/live/runs/round-89/**` and the SKILL note for the oracle. Each claim's
counters read only its own files: the census gate never opens
`corpus/live/runs`, and F4/the oracle never open the census rows. A C1-only
tree (base + census fix) scores `CENSUS_STALE_UNFLAGGED=0` with F4 still
10/11; a C2-only tree (base + record + oracle) scores F4 11/11 with the
census still 10. Both receipts land with the round.

## No-harm statement (pre-declared)

No criterion instrument is rewritten: `f_probe4.py`, `mg_probe.py`,
`ag_probe2.py`, the `verify_*.py` set, `receipt_probe2.py`,
`gate_probe2.py`, `probe_negctl2.sh`, `receipt_sweep.py`,
`self_assessment_check.py` and `check_embedded_outputs.py` are not edited this
round. `PROVINCE.md`, `corpus/QUALITY.md`, `corpus/README.md`'s coverage map,
`corpus/knowledge` beyond the two census files, and `corpus/live/runs` before
round-89 are byte-unchanged (no-harm diff receipt at landing). The census
files gain an appended `## Re-verification 2026-11-04` table; the earlier
tables stay byte-identical (the gate reads the last occurrence per id, so the
append is the correction — the same shape both files already use).

## Routed, not claimed

- K (8/15, 5.3) stays operator-blocked: L0 r74 unanswered.
- `self_assessment_check.py` reads `SELF_MISMATCH=2` at base: SM2 names
  `audit_source_quotes.py` as unindexed (fixed this round as an unclaimed
  correction in the README index) and SM6 hardcodes a `/14` denominator
  against the now-15-row map — the instrument is denominator-blind; routed to
  a future calibration claim, not repaired here (a post-score counter change
  is never this round's rule).
- The census literal form (`sources-census.sh validate --root <fleet>
  revenger`) now exits 0 on this Linux host; the r74–r88 exit-2 lineage is
  Windows-layout history. No L0 action needed; recorded for the closure.
