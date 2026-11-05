# Round 95 — C10 admitted through the v4 gate (coverage K 11/15 → 12/15); the r94 routed closes frozen as v4 legs and named vectors (calibration)

Freeze `6e0bf15fed58f357b7fa0c881371ac7616a116f7` (claims, v4 counter, battery, controls, red-before,
superseding candidate, S500/S501 receipts — committed before any seat ran). Base
`cb5c26f73c99af268bc71e9f7417bfd7e7738d83` (round-94 adjudication tip). Predicates and kill rules:
`reports/round-95/claims.md`, unchanged since the freeze.

## Gate

Decisions this round, for the coverage-K move and the calibration counters.

### Admission candidate — C10 (`knowledge/round-95-evidence-ledger-discipline.md`)

- Decision: **admit** (pending the frozen counter's C1 verdict and the non-author closure).
- Opened THIS round, located quotes (≤25 words), access date 2026-11-05:
  - **S500** — REA Evidence schema at revision `12f6e09`,
    `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidence.ts`,
    HTTP 200, 17010 bytes, sha256 `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f`.
    Quote (11 words), body span 3149–3223: "Source authority vocabulary owned by Evidence and reused by its consumers."
    Teaches the confidence/authority vocabulary the entry's Evidence-record row cites.
  - **S501** — REA EvidenceLedger at revision `12f6e09`,
    `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/application/investigation/EvidenceLedger.ts`,
    HTTP 200, 18784 bytes, sha256 `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac`.
    Quote (7 words), body span 2136–2198: "Record evidence idempotently; conflicting content is rejected."
    Teaches the session-ledger dedup/conflict rule the entry's session-ledger row cites.
- Receipts and fetch log: `reports/round-95/quote-receipts/` (`S500.receipt.json`, `S501.receipt.json`,
  `raw/*.body`, `fetch-log.md`); `corpus/audit_source_quotes.py verify` → `SUMMARY rows=2 verified=2`.
- Q-map: the entry's own §Q-map records a decision for Q01–Q17 (lint clean: `LINT_QMAP=0 LINT_Q14=0
  LINT_Q15=0 LINT_HEADER=0`). The non-author votes (ReviewerGate, ReviewerBlind, CriticR95) decide
  the admission under the frozen counter.
- Supersession: the 2026-10-29 candidate stays byte-preserved at `status: rejected` (round-74 kill
  rule). The new entry supersedes it by a new file, never by an in-place rewrite (CORPUS corrections rule).

### Rejects (for the discernment spot-check)

- **REJECTED — a seventh C05 Android candidate this round.** Reason: six rejected candidates already
  on record (`knowledge/round-65-…` through `round-71-apk-axml-byte-evidence.md`, each
  `admission-status: rejected` with located Q failures); no new primary APK/AXML byte source was
  opened this round, so re-gating would repeat a known failure. Flip: a newly opened primary source
  carrying located AXML byte-level rules that the Q-map can cite without prose credit to a script.
- **REJECTED — re-admitting the 2026-10-29 C10 candidate in place.** Reason: the CORPUS corrections
  rule (new entries, never rewrites) and the r74 kill rule set its `rejected` status; the bytes stay.
  Flip: none needed; the supersession entry is the admitted successor. Recorded here so the reject
  is visible in the gate, not only in the superseded file's header.

### Calibration counters — gate decisions

- The v4 counter admits a C10 move only under its frozen legs; a candidate that fails any leg is
  reported as a miss, not re-scoped. The eleven named v3-passing vectors are the battery's
  discriminating set (see `reports/round-95/forge_battery4.py`).

## Mistakes (mined; class · evidence · captured-by · fix)

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| **M1** | **reaped-scratch dependency in a committed frozen instrument (recurrence of r94 M1).** The frozen `reports/round-94/forge_battery3.py --stage full` mkdtemps under `/fast/scratch/hyaku/revenger-r94/battery3` without creating that root; with the root reaped, `FileNotFoundError` before any verdict prints (`FileNotFoundError: … revenger-r94/battery3/full-…`, observed on the round-95 HOLD leg before the fix). | the HOLD leg of `reports/round-95/forge_battery4.py` (`b3.SCRATCH.mkdir` provisioning) and `reports/round-95/controls/battery4-full-at-freeze.log` (`HOLD_R94_BATTERY=pass` after provisioning) | none: r94 M1 fixed only the red-v2 stage's dirs, not the full stage's root | the successor runner pre-creates the frozen battery's own scratch root before invoking it; frozen bytes are not edited. **Able to fail:** before the provisioning line, `HOLD_R94_BATTERY=fail` (the `FileNotFoundError` run); after it, `pass`. Routed to any later freeze: every committed instrument must create its own scratch root. |
| **M2** | **helper-only registry gate (r94 M6 recurrence in my own successor).** The first v4 draft carried `C1_REGISTRY` as a leg but the first V03 duplicate-key delta built the JSON in Python, so `json.loads` collapsed the duplicate and the delta never reached the strict reader. | `reports/round-95/forge_battery4.py` V03 path — the first run returned `v4 … rc=0 failing=[]` (self-test `SELFTEST_C1V4=fail`: `V03-dup-json-keys-registry: expected fail on C1_REGISTRY, got rc=0`) | the self-test itself caught it (`SELFTEST_C1V4=fail` on the first run) | delta rewritten to inject a literal duplicate member into the raw registry text; self-test then `pass legs=24`. **Able to fail:** the pre-fix self-test run printed `fail`. |
| **M3** | **red-stage fixture shape mismatch (the v3 counter reaches vectors only when its own digest is re-bound).** The first red-v3 run blocked H1 and V19 with `rc=1` because the body edit moved the v3 digest and the votes were not re-bound. | `reports/round-95/controls/battery4-red-v3.log` (final run) vs the first run (`V3_REACH_NEW=8/10`, `RED_V3_VERDICT=fail`) | the red stage itself (`RED_V3_VERDICT=fail` on the first run) | `rebind_v3` applies the r93 M1 procedure (candidate digest, artifact bytes and sha move together) for body-editing deltas only. Final `V3_REACH_NEW=10/10`. |
| **M4** | **the v3 counter's mutant survives its own self-test (r94 M6, now shown as a survivor on the frozen bytes).** A code mutant that drops the v3 registry gate keeps `SELFTEST_C1V3=pass`. | `reports/round-95/controls/battery4-red-v3.log` line `MUTANT_V3_REGISTRY_SURVIVES=pass` | `none` on the frozen v3 (its registry check lives in `C1_VOTES`) | v4 splits the check into `C1_REGISTRY`; the same mutant dies on v4 (`MUTANT_V4_REGISTRY_KILLED=pass`). |
| **M5** | **a revision mislabel in my own SKILL.md registry note.** The first registry row said the counter was "frozen at `cb5c26f`"; `cb5c26f` is the BASE (`FREEZE_REV`, the round-94 tip), and the freeze commit that carries the frozen bytes is `6e0bf15`. `claims.md` itself was right. | `SKILL.md` registry row for `c1_k_admit_counter4`, corrected before landing (`base revision cb5c26f`); `claims.md` header names base `cb5c26f` and the freeze in its Carry-in paragraph | none (a prose label, not a predicate) | label corrected; no counter or claim byte changed. |
| **M6** | **a SOURCES row written without its closing pipe, caught by the census (E01 `fields=10`).** The S500/S501 rows were appended with a `used-by` cell and no trailing `|`. | `scripts/sources-census.sh validate --root … revenger` before the fix: `E01 S500 fields=10`, `E01 S501 fields=10`, rc 1; after `| ` fix: rc 0 | the census (E01) | append the closing pipe; census rc 0 (`reports/round-95/controls/census-round-start.log` is the pre-append run; the end-of-round census is the record of the fix). |
| **M7** | **the C10 coverage cell named extra `knowledge/*.md` paths.** My first README C10 cell cited `knowledge/seed.md` and the superseded candidate; the frozen `C1_C10_CITES` leg requires the exact one-file set. | the v4 counter on the working tree before the edit (`C1_C10_CITES` would fail: the cell names three files) | the frozen leg itself (caught before landing, by reading the counter, not by a run) | cell trimmed to the admitted entry alone; the counter's `C1_C10_CITES=pass` after the edit. |
| **M8** | **residue from my own debug import, found by the sentinel.** An inline `python3 -` debug session loaded `reports/round-94/c1_k_admit_counter3.py` through importlib without `-B`, writing `reports/round-94/__pycache__/c1_k_admit_counter3.cpython-314.pyc` (gitignored, so no tracked byte changed). | `.ufo/waves/round-95/w1/SentinelScope.md` finding 2 (written 14:23:14); `find . -name __pycache__` before removal lists the one path | the sentinel's pycache check (`C1_PYCACHE`-class audit), not the counter (the counter reads only its own round's surfaces) | the directory removed from the lane (`rm -rf reports/round-94/__pycache__`); the lane-wide `find` returns 0 afterwards. Routed to r96: `C1_PYCACHE` should cover every frozen round directory the counter reads, and debug sessions use `python3 -B` only. |
| **M9** | **a sentinel bounds false positive on L1 integration writes, and an unattributed fleet-root file.** Sentinel FAIL (1) lists `SKILL.md`, `corpus/README.md`, `corpus/SOURCES.md`, `corpus/lessons/round-94.md` and `round-95.md` as "unexpected" dirty paths; these are the L1's own landing writes (the round shape assigns them to the L1), so the finding is a false positive against the seat-bounds rule. Its FAIL (4) names an untracked fleet-root `evb.ts` (22885 B, REA evidenceBundle TypeScript) written 14:39:35 with no attributable writer; it was absent from the fleet root at this round's sweep (`git -C /home/vgpnk/Projects/shokunin status --porcelain` lists only the orchestrator's `.scratch/run15-state.json`). | `.ufo/waves/round-95/w1/SentinelScope.md` findings 1 and 4; fleet-root status at sweep time | the sentinel's bounds check (no attribution rule for the L1's own writes) | no fleet-root file was copied or deleted by this L1 (the sweep found none attributable to revenger); the L1's writes are named in this round's report; routed to the protocol owner: the bounds check must exclude the L1's round-shape writes, and fleet-root writers must name themselves. |

Found-none sweep: not needed — nine mined (M1–M9).

## Corrections (append-only; the filed bytes stay)

- **C-r95-1 — S499 word count (round-94 spot-check defect C-b).** Recorded in `corpus/lessons/round-94.md`
  (appended): "(13 words)" is 11 words. The quote is verbatim.
- **C-r95-2 — r94 freshness row (round-94 spot-check defect C-d).** The r94 SCORECARD `freshness … improved`
  row carried no declared claim; re-graded `unchanged` by the appended r95 erratum in `SCORECARD.md`.
- **C-r95-3 — r94 `## Gate` reject (round-94 spot-check defect C-a).** The r94 Gate records no rejected
  candidate. Appended to `corpus/lessons/round-94.md` (see the C-r95-1 correction note) and carried
  forward: the r95 Gate above records two rejects with reasons and flip conditions.

## Frontier and census

- Census round start: `reports/round-95/controls/census-round-start.log` → `… rc=0`, `ok`
  (`scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`); rows 499.
- Census round end: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → rc 0, no E-codes (see report).
- Rows added: S500, S501 (tier A, `mined`, opened 2026-11-05, used-by the entry).
- Rows touched old→new (used-by only; status and recheck unchanged): S002, S096–S109 each gain
  `corpus/knowledge/round-95-evidence-ledger-discipline.md` (15 rows; previous used-by listed the
  2026-10-29 candidate or `seed.md`, both kept).

## Assimilation

- none this round. Frozen collision check (`ExecCensus`, seat artifact under the wave dir): the
  staged 155 `S…` ids of `merge/revenger/SOURCES.append.md` still collide with the lane registry
  (L0 `revenger | round-91` open); nothing adopted.

## considerthese

- Adopted as practice, receipt set PARTIAL: proposal 1 of `considerthese/2026-11-05.md` ("Counter-reachability review of each new `claims.md`, written before the round lands"). Evidence: `reports/round-95/controls/` (do-nothing base rc 1, selftest pass, red-v3 10/10 reach + the mutant survives on v3, full battery kills) and this round's M2 (a self-test caught a helper-only delta before the freeze). ConnectorOverlap's receipt check (`.ufo/waves/round-95/w1/ConnectorOverlap/connector.md`) finds the receipt set does NOT yet cover every named class: no stub-that-prints-the-pass-line control exists, and twelve of the twenty-two self-test deltas are receipted only by the aggregate `SELFTEST_C1V4=pass` line. Recorded as a gap, not a verdict; routed to r96 (receipt each delta individually).
- Not adopted: proposal 2 (frozen-counter validity rate) — re-measured by the connector seat over the r94 window in its wave dir (`measurement-r95.tsv`); reported, not a criterion.
