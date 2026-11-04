# ScribeR89Sources — round-89 own-work source rows S480–S482

Seat: `ScribeR89Sources` (scribe, axis: freshness). Lane
`/home/vgpnk/Projects/shokunin/revenger-shokunin`. Round 89 attempt 1,
freeze `c84339c051443e13f6a546cf186cc8965649a932`.

## What was written

Three rows appended to `corpus/SOURCES.md` **inside the `## Registry`
section, directly after S479** (S479 was line 496; the three new rows are
lines 497–499, immediately before the blank line and the `## Paths`
heading at :501). No existing row was edited.

| id | source | kind | tier | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|
| S480 | `reports/round-89/census-red.log` | own-work | A | mined | 2026-11-04 | 2027-02-02 | corpus/lessons/round-89.md, reports/round-89/claims.md |
| S481 | `corpus/live/runs/round-89/receipt.json` | own-work | A | mined | 2026-11-04 | 2027-02-02 | corpus/lessons/round-89.md, reports/round-89/claims.md |
| S482 | `reports/round-89/oracle-design.log` | own-work | A | mined | 2026-11-04 | 2027-02-02 | corpus/lessons/round-89.md, reports/round-89/claims.md |

`recheck` is a valid ISO date (2027-02-02 — not a cadence token), per the
seat instruction; `opened` is the date each source was opened this round
(2026-11-04).

## Located quotes (verbatim, ≤25 words each)

Each quote was re-read from the named file in this seat and checked
byte-for-byte by substring match against the file content.

- **S480** — `reports/round-89/census-red.log:12`:
  `"CENSUS_STALE_UNFLAGGED=10"`.
  The ten `CENSUS_MISMATCH` lines sit at `:2`–`:11` and name exactly
  F01, F03, F04, F07, F08, F12, K01, K03, K04, K05 (verified by parsing
  those lines' second field, in that order).
- **S481** — `corpus/live/runs/round-89/receipt.json:20`:
  `"stdout_sha256": "01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76"`
  (run1 stdout, the landed bytes per `:41`), plus `:6` `rea_version` 6.7.0,
  `:8`–`:10` provider `jadx` / `JADX headless` / `0.7.1`, and `:31`
  `"DIFFER: the two stdouts are byte-non-identical"`.
  The receipt was read **after** `ExecR89Record` landed it (18:00); the
  first read attempt found `corpus/live/runs/round-89/` absent, and the
  wait was filled with the SOURCES-shape work, not a blocking poll.
- **S482** — `reports/round-89/oracle-design.log:20`:
  `"ORACLE OK (19/19 checks)"`; the nineteen `check ok:` lines are `:1`–`:19`
  (counted: 19).

No quote carries a literal or escaped `|`. Every cell in all three rows was
checked for `|` (0 occurrences) and the rows parse at **NF=13** (11 cells).

## Census (sanctioned form)

Command, run from the lane root after the append:

```
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate \
  --root /home/vgpnk/Projects/shokunin \
  /home/vgpnk/Projects/shokunin/revenger-shokunin
```

```
EXIT=0
```

**E lines: none.** (The grep for `	E[0-9]+	` over the validate output
returned zero rows.) The lane line is
`revenger-shokunin	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md`.
31 W lines are reported (the pre-existing disclosed classes: 21 × W01
tier-C-mined, 10 × W04 duplicate-URL-across-scopes) — the same 31 the
lane already carried before this append, so the append added no new
finding. Baseline before the append was the same `EXIT=0`, same 31 W.
Receipt: `.ufo/waves/round-89/w1/ScribeR89Sources/census-validate-after.log`.

Note on E11: the `used-by` cells name `corpus/lessons/round-89.md` (present
on disk in the lane, written by the L1 in parallel with this wave) and
`reports/round-89/claims.md` (the frozen claims file, present). Both
resolve, hence no E11.

## Append-only proof

`git diff --numstat -- corpus/SOURCES.md` → `3 0` (3 insertions, 0
deletions); `git diff -U0 | grep -c '^-[^-]'` → 0 removed lines. No byte of
any pre-existing row changed, and no other lane file was touched by this
seat.

## Scope discipline

- Written in the lane: `corpus/SOURCES.md` (3 appended rows only) and this
  wave report plus its receipt directory
  `.ufo/waves/round-89/w1/ScribeR89Sources/`.
- No commit, no push, no mutating git/jj command, no `MANIFEST.json`,
  `.ufo/state/`, `.scratch/` or sibling-repo write.
- Scratch `/fast/scratch/hyaku/revenger-r89/ScribeR89Sources` held only the
  validate output; deleted before this report was finished (receipts copied
  into the wave report dir first).

## Findings for the L1 (report only, no adjudication)

1. **S481 records a producer fact that is adverse to a frozen kill rule.**
   The receipt states `byte_identical: false` — the two independent
   `rea inspect-android-package` runs differ in bytes (per-run
   `evidence_id`, an mkdtemp runtime path, JVM map key order,
   `load_duration_ms`). The frozen C2 kill rule (c) requires the two runs
   to be byte-identical. The row states the measured fact as the receipt
   prints it and does not upgrade it; the C2 verdict on that leg is the
   L1's to rule, not this seat's.
2. **`corpus/lessons/round-89.md` already assigns S480–S482** to "C1
   source evidence: S480, the committed red receipt" and "C2 source
   evidence: S481 and S482". The row-to-file mapping written here matches
   that assignment: S480 = `census-red.log`, S481 = the producer
   `receipt.json`, S482 = the oracle `oracle-design.log`.
3. **S482's anchor is the freeze-time scratch green run.** The oracle green
   over the *landed* record is carried by
   `corpus/live/runs/round-89/receipt.json` (`oracle.result =
   "ORACLE OK (19/19 checks)"`, exit 0) and the tamper control is
   `reports/round-89/oracle-tamper-control.log` (`ORACLE FAIL (18/19
   checks)`). S482's row text says "freeze-time run over a scratch producer
   record" so the scope is not over-stated; the L1 may want the landed-run
   oracle result cited alongside it.

## Tooling

No tool was installed or upgraded by this seat (none needed; the census
driver is the fleet's own `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`,
read-only against the lane).

## Receipts

- `.ufo/waves/round-89/w1/ScribeR89Sources/census-validate-after.log` —
  sanctioned validate output, `SANCTIONED_EXIT=0`, E-line count 0.
- `.ufo/waves/round-89/w1/ScribeR89Sources/row-shape-receipt.log` — NF=13 per
  new row, 12 separators per row, 0 escaped pipes, `git diff --numstat`
  `3 0`, 0 removed lines.

## Lane census counts after the append

`sources-census.sh census --root /home/vgpnk/Projects/shokunin revenger` →
`rows 482` (was 479), `tier.A 434` (was 431), `tier.B 21`, `tier.C 27`,
`status.mined 447` (was 444), `status.queued 16`, `status.rejected 19`.
Three rows added, all tier A, all `mined`; nothing else moved.
