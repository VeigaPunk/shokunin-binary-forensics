# CriticR97 — fresh forgery holdout against the frozen v5 counter (round 97, w1)

Seat: CriticR97 (critic, leaf). Axes: calibration (C2), coverage (C1 falsification input).
Scope: build ≥10 forgery vectors not in FG01–FG20 and run them through the frozen v5 counter
(`reports/round-96/c1_k_admit_counter5.py`, imported read-only). Nothing run against the
candidate landing tree; nothing written into `reports/round-97/`; no v6 scored.

## Build (re-runnable by the L1)

- Script: `.ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py`
- Command (from the lane root, scratch under the seat's own scratch dir):
  `HYAKU_SCRATCH=<scratch>/hyaku TMPDIR=<scratch>/tmp PYTHONUTF8=1 python3 -B .ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py --work <scratch>/work`
- Honest base: `_fixture()` from the v5 counter (freeze archive + lane entry bytes; admitted shape).
- Each vector = one delta applied to a fresh copy of that base. Overlays (changed files, removed list)
  are stored at `fresh/<NAME>/changed/`, `fresh/<NAME>/removed.txt`, `fresh/<NAME>/vector.json`;
  the v5 stdout+rc is at `fresh/<NAME>/v5.log`; all results at `fresh/results.json`; hashes at
  `fresh/MANIFEST.sha256`.
- Build rc: **0** (`BUILD_OK=True vectors=15 accepted=8`). Control rc: **0**, `C1_VERDICT=pass`.
- Bytecode: `sys.dont_write_bytecode` plus `-B` on every run. Check after the build:
  `find reports/round-96 reports/round-93 reports/round-94 reports/round-95 corpus .ufo/waves/round-96 -name __pycache__`
  → 0. `git status --porcelain -- reports/round-96 corpus` → empty.
- Scratch: the counter's default SCRATCH is `/fast/scratch/hyaku/revenger-r96/c1v5`; the seat overrode
  it with `HYAKU_SCRATCH` so nothing touched the r96 scratch path. The seat's scratch was deleted after
  the runs.

## Results (frozen v5 counter, rc and verdict as observed)

The counter was run on each materialised tree with `python3 -B <v5> --tree <tree>`. “K” is the
`C1_K_HELD_BACKED` count on that fixture, not a landing-tree score. Failing legs exclude the WHY/DIFFS lines.

| vector | class | v5 rc | C1_VERDICT | K (fixture) | failing legs | expected correct | outcome |
|---|---|---|---|---|---|---|---|
| FR00-honest-control | control (honest `_fixture`) | 0 | pass | 13/15 | — | pass | control-ok |
| FR01-usedby-case-path | used-by path-form, case only | 1 | fail | 13/15 | C1_SOURCES | FAIL | refused |
| FR02-entry-leading-bom | entry bytes (BOM), votes re-signed | 0 | pass | 13/15 | — | FAIL | **ACCEPTED** |
| FR02b-entry-bom-unsigned | entry bytes (BOM), stale votes | 1 | fail | 13/15 | C1_VOTES | FAIL | refused |
| FR03-c02-held-entry-absent | README vs tree (candidate absent) | 1 | fail | 12/15 | C1_C02_CITES, C1_ADMITTED, C1_TRIO, C1_VOTES, C1_LINT, C1_EMBEDDED, C1_EMBED_NONVACUOUS, C1_QUOTES, C1_K_HELD_BACKED | FAIL | refused |
| FR04-c02-held-plus-other-row | README: C02 held + C14 cell changed | 1 | fail | 13/15 | C1_ONLY_C02 | FAIL | refused |
| FR05-vote-foreign-artifact-sha | vote artifact binding (CriticR96) | 1 | fail | 13/15 | C1_VOTES | FAIL | refused |
| FR06-row-dup-held-over-held | coverage row set: held C06 → copy of held C01 | 0 | pass | 13/15 | — | FAIL | **ACCEPTED** |
| FR07-row-dup-target-over-held | coverage row set: held C06 → copy of C02 | 0 | pass | 13/15 | — | FAIL | **ACCEPTED** |
| FR08-headers-in-fence | provenance headers in ```text fence, votes re-signed | 0 | pass | 13/15 | — | FAIL | **ACCEPTED** |
| FR08b-headers-in-fence-unsigned | same, stale votes | 1 | fail | 13/15 | C1_VOTES | FAIL | refused |
| FR09-verified-at-stale | verified-at 2026-11-05 → 2026-10-01, votes re-signed | 0 | pass | 13/15 | — | FAIL | **ACCEPTED** |
| FR09b-verified-at-stale-unsigned | same, stale votes | 1 | fail | 13/15 | C1_VOTES | FAIL | refused |
| FR10-na-boilerplate-on-pass | ReviewerGate Q09 PASS → n/a with shared NA_NOTE | 0 | pass | 13/15 | — | FAIL | **ACCEPTED** |
| FR11-receipt-owner-swap | S502 receipt fetch_url owner swapped, allowlisted host | 0 | pass | 13/15 | — | FAIL | **ACCEPTED** |
| FR12-own-work-dangling | S504 SOURCES pointer → nonexistent saved-session path | 0 | pass | 13/15 | — | FAIL | **ACCEPTED** |

Counts: 15 vectors + control. v5 accepts **8 of 12** named-class forgeries (FR02, FR06, FR07, FR08, FR09,
FR10, FR11, FR12) and refuses 4 (FR01, FR03, FR04, FR05). The three unsigned variants (FR02b, FR08b,
FR09b) are all refused by `C1_VOTES`. Counting command:
`python3 -c 'import json;r=json.load(open(".ufo/waves/round-97/w1/CriticR97/fresh/results.json"));print(sum(x["outcome"]=="ACCEPTED-by-v5" for x in r),"accepted of",len(r)-1,"forgeries")'`
→ `8 accepted of 15 forgeries`. (The control is counted in `len(r)`, so the denominator is 15 forgeries plus one control, 16 rows.)

## The mutation that makes each accepted vector a forgery

- **FR02 BOM (re-signed):** a UTF-8 BOM is prepended to the admitted entry; votes are re-signed to the new
  digest. Why v5 accepts: `C1_TRIO` uses `startswith`, and the BOM sits on line 1 (`\ufeffsource:`), so
  that line is not counted. Lines 2–4 still start with `source:`, so the leg passes. The unsigned variant
  (FR02b) is refused by `C1_VOTES`.
- **FR06 row-dup, held over held:** the held C06 row is replaced by a byte copy of the held C01 row. The C02
  flip stays. `C1_ROWS_TOTAL` still sees 15 rows, `C1_ONLY_C02` iterates only the rows present, and K becomes
  12 − 1 (C06) + 1 (C01 copy) + 1 (C02) = 13/15. C06 disappears from the coverage map with no new evidence.
- **FR07 row-dup, target over held:** the same, with the C02 flipped row copied over the held C06. C02 is counted
  twice, so K = 13/15.
- **FR08 headers in fence (re-signed):** the `source/verified-at/recheck/coverage-map` headers are wrapped in a
  ```text fence. `C1_TRIO` passes because it matches only the line prefix. The unsigned variant (FR08b) is
  refused by `C1_VOTES`.
- **FR09 verified-at stale (re-signed):** `verified-at: 2026-11-05` → `2026-10-01` while the S502/S503 receipts
  state `fetched_at 2026-11-05`. Nothing compares the header date with the receipts. The unsigned variant
  (FR09b) is refused by `C1_VOTES`.
- **FR10 n/a boilerplate on a PASS:** ReviewerGate flips Q09 from PASS to n/a and pastes the shared `NA_NOTE`
  reason. The vocabulary check only needs ≥6 tokens and a Q-reference, and at least one PASS remains.
  ReviewerBlind and CriticR96 still PASS Q09, so the inter-seat inconsistency is not checked.
- **FR11 receipt owner swap:** the S502 receipt `fetch_url` owner is changed from `morluto` to `attacker-fork`.
  The host stays allowlisted, the body hash is untouched, and the fetch-log check matches only the sid and sha.
  This is the receipt-side neighbour of FG10 (SOURCES-side URL drift, already accepted).
- **FR12 dangling own-work pointer:** the S504 SOURCES row points to `corpus/live/runs/round-96-r97-missing/`.
  v5 never checks that the path exists; S504 has no receipt by design.

## Findings

1. **C1 K-move is gameable by row substitution (FR06, FR07).** K = 13/15 is reachable by deleting a held row
   and duplicating another row. `C1_ROWS_TOTAL` counts rows; it does not check that the id set is exactly
   C01..C15 with one row each. A v6 that claims 13/15 must refuse both. The L1 should score FR06/FR07 against v6
   as the first holdout check.
2. **Vote binding is self-attested.** Every accepted vector that touches the entry (FR02, FR08, FR09) passes only
   because the votes were re-signed. The unsigned variants are all refused by `C1_VOTES`. The counter cannot
   tell a re-signed post-vote edit from an honest vote. This matches the admission caveat in `claims.md`
   (lane-internal votes); it is a limit, not a fixable leg.
3. **Semantic checks absent (FR10, FR11, FR12).** The n/a vocabulary, the receipt fetch identity, and the own-work
   pointer existence are not verified. FR12 is the most direct: an own-work row needs no receipt, so nothing
   verifies its pointer.
4. **BOM and headers are invisible to line-prefix legs (FR02, FR08).** `C1_TRIO` and `C1_ADMITTED` tolerate a
   BOM on any single header line and any non-line-start header. A v6 should compare canonical header lines
   exactly, not by prefix.

## Caveats

- The expected correct verdicts are the seat's judgement from the frozen claim semantics (sourced-claim duty,
  row-set identity, vote independence). They are not stated as legs in `claims.md`; the L1 should accept or
  reject each expectation on its own reading. FR10 is the most judgement-dependent.
- FR11 is a neighbour of FG10 on the receipt side, not a new class. Treat it as a near-duplicate if the holdout
  is used for scoring.
- K values are fixture values (the admitted honest shape) and are not a landing-tree score. No candidate tree
  was touched.
- The three re-signed vectors are reproducible only with the build script (votes are regenerated), not from the
  overlays alone.

## Open questions for the L1

- Whether the FR06/FR07 row-set substitution should be added to the v6 legs (it changes C1's K definition).
- Whether FR10 counts as a refusal under the claim (n/a semantic) or is out of scope for the counter.

## Tooling

No tools installed or upgraded this seat (`uv`, `python3` and `git` already present; no pacman use).

## Files written

- `.ufo/waves/round-97/w1/CriticR97.md` (this file)
- `.ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py`
- `.ufo/waves/round-97/w1/CriticR97/fresh/<NAME>/{changed/,removed.txt,vector.json,v5.log}` for 16 names
- `.ufo/waves/round-97/w1/CriticR97/fresh/results.json`, `.../fresh/MANIFEST.sha256`
- Scratch `/fast/scratch/hyaku/revenger-r97/CriticR97/` removed before yield.

## Verdict for the seat

Build rc 0; control rc 0 (pass); 12 named-class forgeries plus 3 unsigned variants run through frozen v5:
8 accepted, 4 + 3 refused. Calibration gap confirmed: v5 accepts 8 of 12 named-class forgeries, including the
K inflation of FR06/FR07. The C2 target (0/19) and the C1 kill rule are untouched by this seat, which
scored no v6.
