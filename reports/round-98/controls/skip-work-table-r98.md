# Skip-work table — round 98 (C1 coverage · C2 calibration)

Paper table only (considerthese/2026-11-05.md proposal 1, standing practice).
Each row: the cheapest way to pass the frozen predicate without doing the work,
and the leg or control that must refuse it. No scoring run here: this lists the
refusing legs by name; the v7 legs named below are the frozen new legs of
`reports/round-98/c1_k_admit_counter7.py` (claims §C1/C2).

Controls assumed present: `make_c1_controls.sh` → `do-nothing/` (claims-freeze
tree unchanged) and `junk-row/` (only C14 `partial → held`) from rev
`9d49002a3804de48d365b7d32849ada06745d64f`; `c2-do-nothing-v6-holdout.log`
(frozen v6 accepts 5/5 routed vectors); the r97 builder
(`.ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py`); the S505 correction
mirror `s505-usedby-fix.diff` + `s505-census.log` + `s505-v6-counter6.log`.

## C1 — coverage: C14 `partial → held` via v7 `--profile c14`

| # | Cheapest skip-work path | Leg / control that must refuse it | Mechanism (one line) |
|---|---|---|---|
| C1-S1 | Flip the README only: C14 cell `partial → held`, no entry, no votes, no receipts | `C1_K_HELD_BACKED` + `C1_ROWS_TOTAL`/`C1_ONLY_C02`-renamed (`C1_ONLY_TARGET`) + the junk-row control | Junk-row control must print `C1_VERDICT=fail`; held count must stay 13/15 without the entry's row-set (`C1_ROWSET`) naming `knowledge/round-98-rea-host-readiness.md` with status `held` |
| C1-S2 | Flip the entry only: `admission-status: candidate → admitted`, README C14 stays `partial` | `C1_K_HELD_BACKED` (`14/15` unreachable) + do-nothing control | Do-nothing control (entry candidate, row `partial`) must print `C1_VERDICT=fail`; held count must stay 13/15 |
| C1-S3 | Copy r96 votes: reuse `reports/round-96/votes/*.json` unchanged | `C1_VOTES` | Vote seat names/roles must equal the pinned r98 seat map (`ExecCounterV7`…`SentinelScope`) and `candidate_sha256` must equal the r98 normalized digest `1ea9260c…` |
| C1-S4 | Re-bind a stale digest: keep old votes, edit entry body lines while preserving the old digest line | `C1_VOTES` + `C1_ENTRY_BYTES` | Any entry edit beyond the `admission-status` line changes the normalized digest; `C1_ENTRY_BYTES` must pin the entry to the vote-bound bytes (`digest()`: sha256 with admission-status lines normalized to `candidate`) |
| C1-S5 | Stub counter: always prints `C1_VERDICT=pass` | `C2_STUB_SELFTEST` (harness, C2 side) + do-nothing/junk-row controls (C1 side) | An always-pass stub scores 5/5 on fully built vectors; the L1's post-freeze controls must both print `C1_VERDICT=fail` |
| C1-S6 | Refuse-everything counter: always prints `C1_VERDICT=fail` | `C1_K_HELD_BACKED` positive requirement + `C2_POSITIVE` (harness) | On the landing tree the counter must print `C1_VERDICT=pass`, `C1_K_HELD_BACKED=14/15`, and v7 `c02` on the landing archive must print `C1_VERDICT=pass` (C02 stays held) |
| C1-S7 | Hand-written entry copy with correct digest but copied (non-independent) votes | `C1_VOTES` + `C1_VOTE_NOTES` | `C1_VOTE_NOTES` requires each PASS note to carry the voter's own specific evidence (n/a notes ≥6 tokens naming a Q id); any FAIL decision fails `C1_VOTES` |
| C1-S8 | Dangling pointers: S506/S507 used-by or own-work paths naming files that do not exist or never cite the row | `C1_OWNWORK_PATHS` + `C1_USEDBY_GROUNDED` | S507's `corpus/live/runs/round-98/` record must exist; every mined used-by pair must resolve to a file that contains the sid token (S505 is the base-registry exhibit: see `s505-ungrounded-count.txt`) |
| C1-S9 | Fake quotes: receipt quote text paraphrased or reflowed instead of byte-exact | `C1_QUOTE_BYTES` + `C1_RECEIPTS` | Quote bytes must re-hash against the committed body (`reports/round-98/quote-receipts/raw/S506.body`, sha256 `ce2d122b…` botched-quotes fail) |
| C1-S10 | Redefined rows: duplicate C14 row, or extra held rows smuggled in | `C1_ROWSET` | Row set must be exactly the frozen 15 rows; any dup/over-held row fails |

## C2 — calibration: v7 `--profile c02` over the r97 routed holdout

Target: `C2_ACCEPTED=0/5` on FR02/FR08/FR09/FR10/FR12, `C2_POSITIVE=pass`,
`C2_STUB_SELFTEST=ok`, FR06/FR07 refused by `C1_ROWSET`. One run of
`forge_reach7.py` prints all of these.

| # | Cheapest skip-work path | Leg / control that must refuse it | Mechanism (one line) |
|---|---|---|---|
| C2-S1 | Flip nothing: ship v6 unchanged and declare 5/5 "reach" | `C2_ACCEPTED` do-nothing baseline (`c2-do-nothing-v6-holdout.log`: v6 accepts 5/5) | Target is 0/5; v6's 5/5 is the control the target must beat, not a pass |
| C2-S2 | Stub counter that rejects everything (constant fail) | `C2_POSITIVE` | v7 `c02` must accept FR00 honest control (`C2_POSITIVE=pass`); a refuse-everything stub scores 0/5 by failing the positive too |
| C2-S3 | Stub counter that accepts everything (constant pass) | `C2_STUB_SELFTEST` | An always-pass stub must score 5/5 on fully built vectors so every vector delta is proven applied (`C2_STUB_SELFTEST=ok`); a stub that "0/5s" by ignoring vectors is exposed |
| C2-S4 | Copy v6 legs and rename them (refuse FR06/FR07 only incidentally via `C1_ADMITTED_UNION`) | `C2_ROWSET_FR06=C1_ROWSET`, `C2_ROWSET_FR07=C1_ROWSET` | The named refusing leg for both row-set forgeries must be the new `C1_ROWSET` leg, not `C1_ADMITTED_UNION` |
| C2-S5 | Entry leading BOM (FR02) accepted | `C1_ENTRY_BYTES` | Entry bytes must be BOM-free and hash-equal to the vote-bound bytes |
| C2-S6 | Headers inside a fenced block (FR08) accepted | `C1_HEADER_POSITION` | `source/verified-at/recheck/coverage-map/admission-status` headers must sit outside fences at the entry head |
| C2-S7 | Stale `verified-at` (FR09) accepted | `C1_VERIFIED_AT` | `verified-at` must equal the fetch/own-work date 2026-11-05, not a carried-forward old date |
| C2-S8 | Boilerplate n/a note on a PASS (FR10) accepted | `C1_VOTE_NOTES` | n/a notes must be ≥6 tokens and name the Q id; PASS notes must not be copied boilerplate |
| C2-S9 | Dangling own-work pointer (FR12) accepted | `C1_OWNWORK_PATHS` | Own-work S-row paths must resolve to saved records on disk |
| C2-S10 | Vectors not rebuilt: measure against stale/partial trees | `C2_STUB_SELFTEST` + r97 builder (`build_fresh.py`) | Stub self-test requires the fully built vector trees; trees must be rebuilt by the frozen builder |

## Standing notes

- Ordering (claims §Ordering contract): this table is paper only. The L1
  commits v7 bytes first, then runs the do-nothing/junk-row controls and the
  `forge_reach7.py` harness; no seat runs a counter on a landing tree.
- S505 mirror: `s505-v6-counter6.log` records that the used-by fix
  (`s505-usedby-fix.diff`: `mined → queued`, used-by → `—`) makes frozen v6
  **fail** on the corrected copy (`C1_SOURCES_WHY=S504:terminal-mined-expected:S505:queued`,
  exit 1) while the freeze baseline passes (exit 0) — S505 is out of v6's
  `NEW_ROW_IDS`, but its `supersedes S504` chain makes S504's terminal row
  S505, so v6 reads the correction as a defect. Census stays exit 0
  (`s505-census.log`). The correction is logged, not landed (frozen corpus).
