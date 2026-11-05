# Round 97 — gate, mistakes, frontier (revenger, hyaku run 15, attempt 1) — **DRAFT**

> **Draft status.** This is a drafting seat's draft for the L1 to paste after measurement. Nothing
> here is a verdict: every measured number is a placeholder token the L1 fills from the landing-tree
> run. Lane commit that froze the claims: `3b4b4e5c1d123d5fc5337ad59015b4752366854a`
> (`reports/round-97/claims.md`); base at round start `7d380ce2c75d3dfd24dfb7759d04f207eeeb1a68`.
> The claims file's predicates, targets, counting commands and kill rules are frozen and are not
> re-declared here.

## Gate

### Q01–Q17 decisions on the C02 candidate (entry `corpus/knowledge/round-96-native-analysis-sessions.md`, digest `2f7d4c1b…`)

The lane-internal r96 votes that bind this candidate are committed at
`reports/round-96/votes/{ReviewerGate,ReviewerBlind,CriticR96}.json`; all three files carry the
**same** decision set (11 `PASS`, 6 `n/a`, measured by reading the three committed JSONs), and each
`n/a` carries a Q cross-reference reason. Those decisions are the ones the counter's `C1_VOTES` leg
reads. The **round-97 re-open at the pinned revisions is a parallel seat's file**, written this wave
and not copied here:

> **r97 gate verdicts:** see `.ufo/waves/round-97/w1/ReviewerGate.md` (parallel ReviewerGate seat).
> The L1 pastes its Q01–Q17 verdicts into the cells marked `[[RG-Q01]]` … `[[RG-Q17]]`.

| Q | criterion (short, from `corpus/QUALITY.md`) | r96 committed vote | r97 re-open (L1 fills) |
|---|---|---|---|
| Q01 | tier-A row opened in the writing round; no tier-C sole support | PASS | `[[RG-Q01]]` |
| Q02 | headers `source:` / `verified-at:` / `recheck:` + coverage-map row named | PASS | `[[RG-Q02]]` |
| Q03 | expected value derived independently of the record under test | PASS | `[[RG-Q03]]` |
| Q04 | tool, version and function named; tool's own output scored | PASS | `[[RG-Q04]]` |
| Q05 | readiness claim carries probe, command, date, observed exit | PASS | `[[RG-Q05]]` |
| Q06 | fixture premises byte-verified before any producer call | PASS | `[[RG-Q06]]` |
| Q07 | predicted parser behaviour pre-registered (or n/a) | n/a | `[[RG-Q07]]` |
| Q08 | superseded by Q11 | n/a | `[[RG-Q08]]` |
| Q09 | digest claims bind exact bytes only, not origin/authenticity | PASS | `[[RG-Q09]]` |
| Q10 | finding scoped to the observed family, operation, version, input | PASS | `[[RG-Q10]]` |
| Q11 | every count, identifier, offset, digest carries its deriving command and output | PASS | `[[RG-Q11]]` |
| Q12 | rejected rows state a grounded reject reason and a flip (or n/a) | n/a | `[[RG-Q12]]` |
| Q13 | verifier credited only for clauses its own run detects (or n/a) | n/a | `[[RG-Q13]]` |
| Q14 | quoted hex run carries `2 × N` characters; ellipsis run carries none | PASS | `[[RG-Q14]]` |
| Q15 | stated git identity re-derived by command (or n/a) | n/a | `[[RG-Q15]]` |
| Q16 | a coverage credit is true only for members the script's own output compares | PASS | `[[RG-Q16]]` |
| Q17 | relocation sweep; a superseded row is closed by a new row opening `supersedes S### —` | n/a | `[[RG-Q17]]` |

**Sourced-claim duty (§2b.4) — the sources this round re-opens.** C1 rests on S502 and S503, re-opened
read-only at the pinned revision `12f6e0974cc0db0b3a9b86246accc76556837222` on **2026-11-05**; the
r97 ScoutReopen seat's measured table (HTTP status, byte length, body sha256, quote presence) is its
own file, `.ufo/waves/round-97/w1/ScoutReopen.md`. The located quotes below are the L1's to paste from
that measurement:

- **S502** — REA native-and-artifacts reference, `…/references/native-and-artifacts.md` at `12f6e09` —
  accessed 2026-11-05 — located quote: `[[S502-QUOTE]]` (12 words; receipt span 26309–26411 in the
  committed body `reports/round-96/quote-receipts/raw/S502.body`, sha256 `c818ee34…3cc24`).
- **S503** — REA `SKILL.md` at the same revision — accessed 2026-11-05 — located quote:
  `[[S503-QUOTE]]` (17 words; receipt span 257–389, body sha256 `b5f17fdf…96ccc`).
- **S504** — saved round-96 native-session record, own-work, `corpus/live/runs/round-96/` — opened
  2026-11-05 — located quote: `[[S504-QUOTE]]` (the **byte-verbatim** replacement span; the r96
  one-liner is a whitespace-reflowed rendering that is absent from the saved bytes — see M9. The
  superseding row is S505, draft at `.ufo/waves/round-97/w1/ScribeLesson/S505.row.md`.)

**Assimilation:** none — merge/revenger 155 staged ids collide with the registry (L0 question appended; nothing adopted)

### Candidates considered

- **C02 native analysis sessions — the entry under the v6 gate; not admitted by this seat.** The
  entry's own bytes are unchanged (the three r96 votes bind digest `2f7d4c1b…`, which the counter's
  normalization keeps stable across a status-line flip). Whether C02 flips to `held` is the L1's
  measurement on the landing tree, not this seat's call: `[[C1-VERDICT]]`.
- **C05 Android K-move — not a round-97 candidate.** No new primary APK/AXML byte source was opened;
  the r95/r96 routing stands.
- **C16 atlas row — not a round-97 candidate.** The frozen K denominator is unchanged.

### Rejected sources — none appended as a new row beyond S505 this round

S502 and S503 re-opened clean (measured by the ScoutReopen seat). S504's row is not rejected: its
source, digests and Evidence ID all hold; only the **quote form** was defective, and the correction
route is a superseding row, not a rejection (M9). The S505 draft row is appended by the L1 only after
`sources-census.sh validate` passes on the candidate registry (see the row draft's own note).

## Mistakes

| # | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M5 | **real-tree used-by path-form miss (r96's miss, carried):** the frozen v5 used-by exclusivity leg compares a row's used-by cell against the fixture form `knowledge/<entry>` while the census and every existing row carry the census form `corpus/knowledge/<entry>`; the fixture wrote the short form, so the miss stayed hidden | `reports/round-96/c1-tree-flip-diagnostic.log` (`C1_SOURCES_WHY=S502:usedby-exclusivity:['corpus/knowledge/round-96-native-analysis-sessions.md']`, and the same for S503, S504) and `reports/round-97/controls/c1-do-nothing-v5.log` (`C1_SOURCES=fail` is the only failing leg with the flip absent); `corpus/SOURCES.md` rows 519–521 | none — the self-test and the frozen battery both ran the fixture form | **routed to r97 and fixed in v6:** the successor counter normalises a leading `corpus/` before the exactly-once check (`reports/round-97/c1_k_admit_counter6.py:426-427`); red-before proven on a corpus-prefixed fixture (`reports/round-97/controls/red-v5-corpus-prefix.log` → `C1_SOURCES=fail`, rc 1) and green on the same fixture under v6 (`green-v6-corpus-prefix.log` → `C1_SOURCES=pass`, `C1_VERDICT=pass`, rc 0); the frozen v5 counter is not edited |
| M8 | **calibration count mismatch between prose and committed receipts:** the r96 prose states **13** accepted forged vectors, while the committed CriticR96 receipt aggregate holds **14** rows with `observed_verdict=pass`. Measured attribution of the "13": it is in the `SCORECARD.md` r96 calibration row ("found 13 counter PASSES") and in `corpus/lessons/round-96-verifier-spotcheck.md` ("records 13 counter PASSES out of 19 forgeries") and in `.ufo/waves/round-96/w1/CriticR96/findings.md` ("13 counter PASSES (findings F1–F13), 6 kills"); **the r96 round lesson `corpus/lessons/round-96.md` carries no accepted-vector count at all** (its only "13" is `C1_K_HELD_BACKED` at 13/15) — so the frozen claim's wording "the r96 SCORECARD and lesson state 13" is itself imprecise, and the mismatch is recorded here rather than silently corrected | `.ufo/waves/round-96/w1/CriticR96/receipts/summary.json` (19 rows; 14 `observed_verdict=pass`: FG01–FG12, FG15, FG19) counted by `reports/round-97/controls/skip-work/count_summary.py` → `accepted 14/19`, logged at `reports/round-97/controls/c2-count-audit.log` (rc 0) and `reports/round-97/controls/c2-v5-reach-from-r96-receipts.txt` (`C2_V5_ACCEPTED 14 / 19`); the "13" prose sites are `SCORECARD.md` (r96 calibration row), `corpus/lessons/round-96-verifier-spotcheck.md` and `.ufo/waves/round-96/w1/CriticR96/findings.md` | none — the r96 prose was not re-counted against its own committed receipts | count from the committed receipts, not from the prose: the control receipt above is the count of record, and the r97 battery reproduces it against the frozen v5 (`reports/round-97/controls/c2-v5-reproduced.log` → `C2_ACCEPTED=14/19`, rc 0) |
| M9 | **r96 S504 located quote is not byte-verbatim:** the r96 lesson's `## Gate` quote for the own-work record is a whitespace-reflowed one-liner (`undefined8 entry(void) { return 0x2a; }`, described as "3 lines"); the saved bytes are a five-line block and the one-liner occurs nowhere in them, so the quote cannot be located by a byte comparison | `corpus/lessons/round-96.md` (r96 `## Gate`, the S504 line) is the defect site; `grep -c -F` of the one-liner over `corpus/live/runs/round-96/codeable-decompiled.c` → **0** (exit 1); the r96 verifier spot-check D1 (`corpus/lessons/round-96-verifier-spotcheck.md`, item 3 / D1) and the r97 ScoutReopen seat's re-measurement (`.ufo/waves/round-97/w1/ScoutReopen.md` §3) | the counter's `C1_QUOTES` leg **passes it** — that leg runs the receipt audit over `RECEIPT_ROW_IDS = ("S502","S503")` only, and its own normalisation is whitespace-insensitive, so a reflowed rendering of an own-work body is invisible to it | superseding row **S505** carries the byte-verbatim span, and the round-97 lesson quotes it as `[[S504-QUOTE]]`; draft row at `.ufo/waves/round-97/w1/ScribeLesson/S505.row.md` (11 cells, `teaches` opens `supersedes S504 —`, status `mined`, used-by the candidate entry exactly once). The frozen r96 lesson file is **not** edited this round (frozen bytes), and the frozen v5 counter is **not** edited |

## Frontier

- **Census before** — `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
  → **exit 0**, warnings only: **21 × W01** and **13 × W04**, **0 E-codes** (receipt:
  `.ufo/waves/round-97/w1/ScribeLesson/receipts/census-before.log`). The registry bytes are the base
  bytes: `git show 7d380ce:corpus/SOURCES.md | sha256sum` =
  `db18d1fd48017ee0ede21cb0e1f046387836b7540f85a37193f32b44fe17977e` = `sha256sum corpus/SOURCES.md`
  (same for `corpus/README.md`, `d3dd5ab6…`), so the census run above **is** the census at `7d380ce`.
- **Rows touched (old → new):** **none in place.** S502, S503 and S504 keep `status=mined`,
  `recheck=on-release`, `opened=2026-11-05` and `used-by=corpus/knowledge/round-96-native-analysis-sessions.md`
  unchanged — their used-by cells already carry the census form, which is why M5 needs no registry
  edit and only a counter fix. **S504 must keep `status=mined`**: the frozen v6 counter's
  `C1_SOURCES` leg requires every row in `NEW_ROW_IDS = ("S502","S503","S504")` to be `mined`
  (`reports/round-97/c1_k_admit_counter6.py:410-411`), so flipping S504 to `rejected`/`queued` would
  turn that leg red. **One row appended:** S505 (own-work, tier A, `mined`, opened 2026-11-05,
  recheck `on-release`, used-by the candidate entry exactly once; `teaches` opens
  `supersedes S504 —` and carries the byte-verbatim located quote).
- **Registry size:** 504 rows at base (S001–S504; tier A 455 / B 21 / C 28; status mined 468 /
  queued 16 / rejected 20) → **505 rows** with S505 appended (tier A 456, mined 469).
- **Coverage:** the coverage-map row C02 (`corpus/README.md`) moves `partial` → `held` only if the
  landing-tree measurement says so; K `12/15 (8.0)` → `[[C1-K-AFTER]]`. The entry's status line is
  the flip surface (the vote digest is stable across it).
- **Calibration:** the 19 frozen vectors are the C2 surface; v5 accepted `14/19` (measured from the
  committed receipts), v6 target `0/19`; the L1 measures `[[C2-ACCEPTED]]`.
- **Census after:** the L1's round-end census must exit 0 (`[[CENSUS-AFTER-RC]]`).

## considerthese

- **Proposal 1 of `considerthese/2026-11-05.md` (counter-reachability review: write the cheapest
  skip-work control for every frozen predicate, before the round lands) — mined, and implemented as
  `reports/round-97/controls/skip-work-table.md`** (the paper table: control | claim | expected v6
  verdict or count | reason | predicate it tests | observed value, six rows S-A…S-F, each control
  script under `reports/round-97/controls/skip-work/`). It implements no claim by itself: the table's
  purpose is to show that the C1 and C2 counters cannot be met by skip-work (base tree, always-pass
  stub, always-fail stub, admission-only flip, name-keyed lookup table) and that the C2 count is
  taken from committed receipts rather than prose (M8).
- Proposals 2–5 of the same file are not mined this round (a per-round validity rate, a self-forecast
  and two watch items all need a landed round to measure against).
