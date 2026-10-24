# R63LedgerFirmware — build report (scribe)

Seat: `revenger-r63.R63LedgerFirmware` (scribe, coverage axis).
Scope: draft the evidence ledger for the round-63 firmware record. Lane repo
`/home/vgpnk/Projects/shokunin/revenger-shokunin` (absolute paths only).

## Behavior

Drafted `corpus/live/runs/round-63/LEDGER.md` **after** `inspection.json` existed there
(first observed 2026-10-24T02:24:02Z by a polling watcher; the skeleton fallback was not
needed). The ledger contains, in the order required by the assignment:

1. **Fixture and route section** — generator (`corpus/fixtures/firmware-r63/generator.py`,
   SHA-256 `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4`, recipe
   `python3 -B generator.py`, Python 3.14.8 / zlib 1.3.2 / level 9 / 2048 B image /
   `00` padding / members at 512 and 1024), the fixture image digest, the truth oracle
   digest, the **verbatim** REA command line from `receipt.json`, the producer exit code
   and duration, the **provider id/version from the record envelope**
   (`provider.id` = `binwalk`, `provider.version` = `3.1.0`, plus `normalized_result.engine`
   name/version/executable path/executable SHA-256/`source_revision`/`worker_count`), and
   **binwalk/unblob versions with probe dates** (binwalk 3.1.0, unblob 26.6.4; probed
   2026-10-24T02:22:40Z and 2026-10-24T02:24:44Z host UTC; both executable digests
   recorded).
2. **`## Ledger` table** with a class column, 23 rows:
   - **11 OBSERVATION rows** — O1–O2 record envelope and subject binding; O3 the two
     reported regions verbatim (`provider_id`, offset, `reported_size`, signature,
     description, `reported_confidence`, `size_basis`); O4–O5 the per-region
     `truth.json` comparison result (offset OK · size OK · decompressed sha256 OK ·
     decompressed size OK for both, with the truth digests named); O6 the three padding
     regions the record does not report; O7 no extraction performed; O8 the provider's
     own declared limitations; O9 receipt↔record↔bytes consistency; O10 the two
     independent oracle checks; O11 the independent unblob cross-check.
   - **6 INFERENCE rows** — I1 the oracle-agreement statement **scoped to this fixture**
     (precision 2/2, recall 2/2, zero mismatches); I2 the digest agreement is a
     checker-side decompression, not a record field; I3 `size_basis` is
     `provider_reported_validation_unknown` yet the sizes coincided exactly here; I4 static
     and non-executing; I5 the region set is engine-dependent; I6 what the F counter sees.
   - **6 UNKNOWN rows** — U1 other signature families; U2 extraction completeness; U3 scan
     depth inside member bytes; U4 producer provenance / reproducibility; U5 oracle
     independence (truth.json is same-lane-authored); U6 nothing about a real device.
3. **Score/limitations section** naming exactly what the F counter can and cannot see.

Every conclusion in the ledger is classed; observation, inference and unknown are kept
separate throughout and the section headings are `## Ledger` and
`## Score and limitations`.

## Gates

| Check | Result | Evidence |
|---|---|---|
| `inspection.json` present before drafting | YES — first seen 2026-10-24T02:24:02Z; drafted after | polled watcher job; file present on disk |
| Record shape (claims.md C2a) | PASS — `evidence_id` = `ev_aae7529f…`, `normalized_result` present, `operation` = `inspect_firmware_regions` | `inspection.json` |
| Real REA run with committed receipt (C2b) | PASS — receipt records command, exit_code 0, `fixture_sha256`, `stdout_sha256`, `evidence_id`; `stdout.raw` and `inspection.json` are byte-identical (same SHA-256 `f6997835…`, 3904 B); `stderr.txt` 0 B | `receipt.json` (SHA `e930a549…`) |
| Byte-oracle agreement (C2c) | PASS — 2/2 reported regions agree with `truth.json` on offset, size and decompressed content SHA-256 | ledger author recomputation from the fixture bytes (2/2) **and** `oracle_check.py` → final line `ORACLE OK`, exit 0 |
| No target execution | PASS — the ledger author executed no payload; unblob was run only on the fixture image and on an isolated member copy, in scratch, for read-only chunking | see O11; scratch `/tmp/revenger-r63-ledgercheck/` removed |
| Truth oracle left unmodified | PASS — `truth.json` SHA `9663f90b…` re-read only | file on disk |
| No byte changes outside new round-63 paths | PASS — the only file this seat wrote is the new `corpus/live/runs/round-63/LEDGER.md` and this report | `git status --porcelain` |

## Touched surfaces

| Path | Action | SHA-256 |
|---|---|---|
| `corpus/live/runs/round-63/LEDGER.md` | **created** | `cedc8f701350dfd0c2bcd09fcb36bca9f70f1a5bd61188e3f33c4429bac5f985` (final, 22481 bytes) |
| `.ufo/waves/round-63/build/R63LedgerFirmware.md` | **created** (this report) | self-referential — digest is reported in the seat's final message, not pinned here |

Read-only: `corpus/live/runs/round-63/{inspection.json,receipt.json,stdout.raw,stderr.txt,oracle_check.py}`,
`corpus/fixtures/firmware-r63/{generator.py,truth.json,firmware-r63.bin}`,
`reports/round-63/{claims.md,measure.py}`, `SCORECARD.md`, `PROVINCE.md`, `corpus/README.md`,
and the prior-round LEDGERs used as style references (round-29, 32, 36, 57, 59).

Not touched: no git/jj mutation, no commit, no push, no `.ufo/waves/round-63/` spec or
registry file, no MANIFEST.json, no fleet repo file, no sibling lane, no lane index, no
README status row, no QUALITY.md row.

## Findings

- **Byte-oracle agreement is 2/2 and reproducible by two independent routes** (my own
  recomputation and the sibling `oracle_check.py`), so C2's byte-oracle condition is met
  on the evidence available in the working tree.
- **The record's region set is engine-dependent.** Binwalk 3.1.0 (the record's provider)
  found both zlib members at their authored offsets; unblob 26.6.4 found **zero** chunks
  in the same 2048-byte image and only identified a member once it was presented as a
  standalone zlib stream (extracting 78 B whose SHA-256 matches truth). The record's own
  `coverage` value is `signature_scan`. Recorded as I5 and reflected in the F-counter
  "cannot see" list — any downstream statement about "the regions of this image" must name
  the engine.
- **The record carries no member names and no decompressed digests** — the truth labels
  `diagnostic-note` / `component-note` are oracle-side and are not echoed by the record.
  The digest agreement is therefore a checker-side decompression over the record's reported
  offset/size window (I2), not a field comparison.
- **Both regions carry `size_basis` = `provider_reported_validation_unknown`**, yet the
  reported sizes (79, 90) coincided exactly with the true member lengths. Correct here,
  but the fixture does not establish that provider-reported lengths are validated (I3).
- **The F counter, re-implemented from the frozen `reports/round-63/measure.py` block and
  run against the current working tree, prints `F_COVERAGE=5/8`**, families
  `['native-static','javascript','archives','firmware','evm']`, score 6.25 (was 4/8 /
  5.0). `receipt.json` is correctly not counted (it has `evidence_id` but no
  `normalized_result`), so the new record moves the count by exactly one. **The frozen
  counter on a committed `git archive` tree, and `measure-after.log` on the final tip, were
  not run by this seat — they remain L1's.**
- **The record's own limitations text was transcribed into O8** rather than paraphrased
  away, including that binwalk "may infer unknown lengths before emitting its report" and
  that interpreter/shared-library/package dependencies are not independently attested.

## Out of scope (not done, by design)

- Did not re-run the REA producer (the receipt and saved bytes are the producer's; this
  seat is a scribe, and the role forbids invoking another runtime).
- Did not run the frozen `measure.py` over a committed tree, did not write
  `reports/round-63/measure-after.log`, did not flip README C06 or any README status.
- Did not write `corpus/knowledge/*` — the C1 candidate entry is `R63ZipPremise`'s item.
- Did not modify `oracle_check.py` (still being edited by its author during this round;
  its digest changed mid-round, so the ledger cites it by path and behaviour rather than a
  pinned digest).
- Did not extract member 1 (offset 1024) with unblob; only member 0 was isolated and
  extracted. U2 and U3 record this.
- Did not transfer the claims.md 2026-10-23 uImage pre-probe into a claim about other
  signature families (U1).

## Findings for the canonical judge — conflicts and caveats, verbatim

No conflict was observed between the record, the receipt, the truth oracle and my own
checks; every cross-check agreed. The caveats a judge should weigh:

1. `oracle_check.py` was **still being edited by its author during this round** (digest
   changed from `68bb2a3b…` to `d0dfd7a1…` between two of my listings). The ledger cites it
   by path and behaviour, not by a pinned digest. A judge who pins that digest must take the
   final committed one.
2. The unblob whole-image finding (0 chunks) is an **author-side observation outside the
   REA record**, run in scratch by this seat; it is not part of the saved record and is
   not part of the C2 claim. It is recorded as O11/I5 and does not weaken C2, whose record
   is binwalk-scoped.
3. `truth.json` is **same-lane-authored**, so the oracle agreement is internally consistent
   but not third-party validation (U5). A non-author seat must re-derive the regions before
   the agreement can be called independently confirmed.
4. The `F_COVERAGE=5/8` figure above is from a **re-implementation of the frozen F block
   against the working tree**, not from the frozen counter on a committed archive. It is
   reported as an observation of the working tree, and the committed measurement is
   explicitly left to L1.

## Artifact paths

- Ledger: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md`
  (repo-relative: `corpus/live/runs/round-63/LEDGER.md`)
- This report: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63LedgerFirmware.md`

## Tooling

No tool was installed or upgraded by this seat. Binwalk 3.1.0 (`/usr/bin/binwalk`) and
unblob 26.6.4 (`/home/vgpnk/.local/bin/unblob`) were already present on the host and were
used read-only; `rea-agents@6.5.0` was already cached in the npm npx cache and was **not**
invoked by this seat. No pacman transaction was attempted (pacman is paused host-wide).
