# SCORECARD round-97 section — **DRAFT** (append below the r96 section; do not replace r96 text)

> Draft for the L1 to paste into `SCORECARD.md` **after** the r96 section, as a new
> `## Round 97 (hyaku run 15, attempt 1) — …` heading. Every measurement is a placeholder token the
> L1 fills from the landing-tree run; nothing here is a verdict. The r96 section is **left as it is** —
> the correction line below is **appended**, not substituted (see the correction line's own wording).

## Round 97 (hyaku run 15, attempt 1) — [[R97-HEADLINE]]

Base `7d380ce2c75d3dfd24dfb7759d04f207eeeb1a68`; freeze `3b4b4e5c1d123d5fc5337ad59015b4752366854a`
(claims, do-nothing controls). The v6 admission counter
(`reports/round-97/c1_k_admit_counter6.py`) and the forgery harness
(`reports/round-97/forge_reach6.py`) are committed by the L1 **after** this wave returns; the wave
seats build and check them but do not score the candidate. Wave: one v1 wave, 10 seats
(executor 3, scout 1, scribe 1, connector 1, reviewer 2, critic 1, mutation-tester 1). Claims and
predicates: `reports/round-97/claims.md`, unchanged since the freeze.

| axis / criterion | before → after | counting command | measured commit | verdict |
|---|---|---|---|---|
| coverage — knowledge-map ground K (C1; the lowest owned criterion) | `K_HELD_BACKED` **12/15 (8.0) → [[C1-K-AFTER]]**; coverage row C02 `partial` → `[[C1-C02-STATUS]]` (the candidate entry `corpus/knowledge/round-96-native-analysis-sessions.md` flips `admission-status: candidate → admitted`; the vote-binding digest `2f7d4c1b…` is stable across the flip because the counter's normalization rewrites the status line) | `PYTHONUTF8=1 python3 -B reports/round-97/c1_k_admit_counter6.py --tree <landing-archive-root>` → `C1_VERDICT=[[C1-VERDICT-LINE]]`, `C1_K_HELD_BACKED=[[C1-K-AFTER]]`, exit [[C1-EXIT]]; do-nothing control over the base archive `reports/round-97/controls/base-v6.log` → `C1_VERDICT=fail`, `C1_K_HELD_BACKED=12/15`, rc 1 | `7d380ce` → `3b4b4e5` (freeze) → [[C1-MEASURED-COMMIT]] | [[C1-VERDICT]] |
| calibration — the counter's reach over the routed forgery vectors (C2) | frozen v5 accepts **14/19** of the 19 frozen vectors (counted from the committed receipts, `reports/round-97/controls/c2-v5-reach-from-r96-receipts.txt`) → v6 accepts **[[C2-ACCEPTED-AFTER]]** (target `0/19`); the 19 vectors are rebuilt byte-for-byte from the r96 receipts into `reports/round-97/forgeries/` | `PYTHONUTF8=1 python3 -B reports/round-97/forge_reach6.py --counter reports/round-97/c1_k_admit_counter6.py --deltas reports/round-97/forgeries --work <scratch>` → `C2_ACCEPTED=[[C2-ACCEPTED-AFTER]]`, exit [[C2-EXIT]]; v5 reproduction `reports/round-97/controls/c2-v5-reproduced.log` → `C2_ACCEPTED=14/19`, rc 0; harness stub self-test `reports/round-97/controls/c2-stub-selftest.log` → always-pass stub 19/19 accepted, always-fail stub 0/19 accepted, `SELFTEST verdict=OK`, rc 0 | `7d380ce` → `3b4b4e5` (freeze) → [[C2-MEASURED-COMMIT]] | [[C2-VERDICT]] |

**Correction — the r96 C2 count (appended, the r96 text is not changed).** The r96 SCORECARD calibration
row states **13** counter passes over the 19 CriticR96 forgeries (the same "13" appears in
`corpus/lessons/round-96-verifier-spotcheck.md` and in `.ufo/waves/round-96/w1/CriticR96/findings.md`;
the r96 round lesson `corpus/lessons/round-96.md` carries no accepted-vector count, so the frozen
claim's "SCORECARD and lesson" wording is itself imprecise); the committed receipts
`.ufo/waves/round-96/w1/CriticR96/receipts/summary.json` hold **14** rows with
`observed_verdict=pass` (FG01–FG12, FG15, FG19). The count of record is the one taken from the
committed bytes — `reports/round-97/controls/c2-v5-reach-from-r96-receipts.txt`
(`C2_V5_ACCEPTED 14 / 19`) and `reports/round-97/controls/c2-count-audit.log`
(`accepted 14/19`, rc 0) — and the r97 battery reproduces 14/19 against the frozen v5
(`reports/round-97/controls/c2-v5-reproduced.log`, `C2_ACCEPTED=14/19`, rc 0). The r96 figure of 13
was not re-derived from its own receipts; it is recorded here as a calibration finding of round 97
(lesson `corpus/lessons/round-97.md` `## Mistakes` M8), not silently corrected in place.

**Frontier.** Coverage row C02 (`corpus/README.md`) `partial` → `[[C1-C02-STATUS]]`; K
12/15 → [[C1-K-AFTER]]. Registry: 504 rows at base (S001–S504) → [[SOURCES-ROWS-AFTER]] with one
row appended, **S505**, whose `teaches` opens `supersedes S504 —` and carries the byte-verbatim
located quote for the own-work round-96 record (the r96 S504 quote is a whitespace-reflowed
rendering that is absent from the saved bytes — lesson `## Mistakes` M9); S502/S503/S504 keep
`status=mined`, `opened=2026-11-05`, `recheck=on-release` and used-by
`corpus/knowledge/round-96-native-analysis-sessions.md` unchanged, and **S504 must keep
`status=mined`** — the v6 counter's `C1_SOURCES` leg requires every row of
`NEW_ROW_IDS = ("S502","S503","S504")` to be `mined`
(`reports/round-97/c1_k_admit_counter6.py:405-411`), so a `rejected`/`queued` flip of S504 would
turn that leg red. Census: round start exit 0 (21 × W01, 13 × W04, 0 E-codes);
round end exit [[CENSUS-AFTER-RC]].

**Considerthese.** Proposal 1 of `considerthese/2026-11-05.md` (counter-reachability review: write
the cheapest skip-work control for every frozen predicate before the round lands) is mined and
implemented as `reports/round-97/controls/skip-work-table.md` (six controls S-A…S-F: base tree,
always-pass stub, always-fail stub, admission-only flip, name-keyed lookup table, count audit). It
implements no claim by itself.

**Assimilation.** None — `merge/revenger/` stages 155 ids and all 155 collide with the lane registry
(`.ufo/waves/round-97/assimilation/collisions`, 155 lines; every staged id is present in
`reg-ids`): mass id drift, L0 question appended, nothing adopted.

**planned:** r98 — coverage: the next admissible C-row through the v7 gate, with the D1 quote-check
leg extended to own-work rows; calibration: the v6 counter's remaining reach limits and the
surviving mutants.

---

### Notes for the L1 (not part of the pasted section)

1. **The frozen C2 counting command in `claims.md` cannot be run verbatim.** `claims.md` gives
   `PYTHONUTF8=1 python3 -B reports/round-97/forge_reach6.py --counter reports/round-97/c1_k_admit_counter6.py --deltas reports/round-97/forgeries`
   — **without `--work`**. The harness's argument parser requires `--counter`, `--deltas` **and**
   `--work` (`reports/round-97/forge_reach6.py:144-145`), so the command as written exits **2** with
   `error: --counter, --deltas and --work are required (or use --self-test)` and prints no
   `C2_ACCEPTED=` line. Observed here:
   `PYTHONUTF8=1 python3 -B reports/round-97/forge_reach6.py --counter reports/round-97/c1_k_admit_counter6.py --deltas reports/round-97/forgeries` → rc 2 (argparse usage error, no measurement).
   The C2 row above therefore prints the command **with `--work <scratch>` added**; `claims.md` is
   frozen and was not edited by this seat. If the L1 prefers the claims' command to run verbatim, the
   harness needs a default `--work` (e.g. from `TMPDIR`) — that is an executor change, not a lesson
   change.
2. The C1 counting command in `claims.md` needs no such repair: `c1_k_admit_counter6.py` accepts
   `--tree` (`reports/round-97/c1_k_admit_counter6.py:1048-1049`).
3. The v6 counter's default scratch root still carries the round-96 token
   (`… / "revenger-r96" / "c1v5"`, `reports/round-97/c1_k_admit_counter6.py:45`); pass `--work`
   or `HYAKU_SCRATCH` so the L1's run does not write under the shared `/tmp` default.
