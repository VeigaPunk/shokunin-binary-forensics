# Round 97 — gate, mistakes, frontier (revenger, hyaku run 15, attempt 1)

Claims frozen at `3b4b4e5c1d123d5fc5337ad59015b4752366854a` (`reports/round-97/claims.md`, with
Amendment A recorded before the v6 freeze `85a2c7eb0a980413a62cd9330ffd5b7e9005c332`). Base at round
start `7d380ce2c75d3dfd24dfb7759d04f207eeeb1a68`. Landing and measurement commits are cited in the
SCORECARD round-97 section and the report.

## Gate

### C02 candidate under the v6 counter

Entry `corpus/knowledge/round-96-native-analysis-sessions.md`; vote-binding digest
`2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` (admission-status line normalized).
The landing flip changes only the status line (`candidate` → `admitted`) and the README C02 row
(`partial` → `held`, knowledge cell = this entry only). The digest is unchanged, so the three r96
votes stay bound.

Advisory Q01–Q17 audit (ReviewerGate, `.ufo/waves/round-97/w1/ReviewerGate.md`, not a vote; FAIL: 0):

| Q | decision | Q | decision | Q | decision |
|---|---|---|---|---|---|
| Q01 | PASS | Q07 | n/a | Q13 | n/a |
| Q02 | PASS | Q08 | n/a | Q14 | PASS |
| Q03 | PASS | Q09 | PASS | Q15 | n/a |
| Q04 | PASS | Q10 | PASS | Q16 | PASS |
| Q05 | PASS | Q11 | PASS | Q17 | n/a |
| Q06 | PASS | Q12 | n/a | | |

Each `n/a` carries a Q cross-reference reason in the reviewer file. Non-author admission is still
required; the lane-internal r96 votes are not a non-author judgment (LEARNING.md).

### Sourced-claim duty (§2b.4): sources re-opened this round

Re-opened 2026-11-05 by ScoutReopen (`.ufo/waves/round-97/w1/ScoutReopen.md`):

- **S502** — REA `references/native-and-artifacts.md` at `12f6e0974cc0db0b3a9b86246accc76556837222`.
  HTTP 200, 38167 bytes, sha256 `c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24`
  (equal to the row and to the committed r96 body; `cmp` exit 0). Located quote, verbatim (grep count 1,
  12 words): "`rea decompile <path> --file-offset=0x... --provider ghidra` resolves the source byte offset internally".
- **S503** — REA `SKILL.md` at the same revision. HTTP 200, 35095 bytes, sha256
  `b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc` (equal; `cmp` exit 0). Located quote,
  verbatim (grep count 1, 17 words): "Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction."
- **S504** — own-work record, `corpus/live/runs/round-96/`. The r96 located quote
  "`undefined8 entry(void) { return 0x2a; }`" is absent from the saved bytes (grep count 0). See M9.

### Candidates considered

- **C02 native analysis sessions** — admitted in the flip under the v6 counter on the landing tree
  (`C1_VERDICT=pass`, K 13/15). Non-author closure still pending.
- **C05 Android K-move** — not a round-97 candidate. No new primary APK/AXML byte source was opened.
- **C16 atlas row** — not a round-97 candidate. The frozen K denominator (15 rows) is unchanged.
- **Assimilation** — none. `merge/revenger/` stages 155 rows; all 155 staged ids collide with the lane
  registry (`.ufo/waves/round-97/assimilation/collisions`, 155 lines; registry 504 ids). Mass id drift
  adopts nothing (CORPUS.md §10). An L0 question is appended (`.ufo/l0-questions.md`, round-97 line).

### Rejected or reworked

- **S504 quote** — kept as a source (its digests and Evidence ID hold, `rea-decompile.raw.txt` line 1);
  only the quote form was defective. The correction is a superseding row, **S505**, whose `teaches`
  opens `supersedes S504 —` and whose anchor is the byte-verbatim body (`codeable-decompiled.c`
  lines 6–10, bytes 101–142). S504 is not edited in place; its status stays `mined`.

## Mistakes

| # | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M5 | **used-by path-form miss (carried from r96):** the frozen v5 exclusivity leg compares a used-by cell to the fixture form `knowledge/<entry>`; the census and every row carry `corpus/knowledge/<entry>`. The fixture wrote the short form, so the self-test never saw it. | `reports/round-96/c1-tree-flip-diagnostic.log` (`C1_SOURCES_WHY=S502:usedby-exclusivity:['corpus/knowledge/…']`); `reports/round-97/controls/c1-do-nothing-v5.log` (`C1_SOURCES=fail` on the base tree) | none (the r96 self-test and battery both used the fixture form) | v6 accepts both forms, comparing repo-relative paths after stripping a leading `corpus/`. Shown able to fail: `reports/round-97/controls/red-v5-corpus-prefix.log` (rc 1, `C1_SOURCES=fail`) against `green-v6-corpus-prefix.log` (rc 0, `C1_SOURCES=pass`). |
| M8 | **calibration count mismatch between prose and committed receipts:** the r96 SCORECARD says **13** forged vectors were accepted by the counter; the committed `.ufo/waves/round-96/w1/CriticR96/receipts/summary.json` holds **14** rows with `observed_verdict=pass` (FG01–FG12, FG15, FG19). The r96 lesson states no count. | `reports/round-97/controls/c2-v5-reach-from-r96-receipts.txt` (`C2_V5_ACCEPTED 14 / 19`); `.ufo/waves/round-97/w1/ReviewerClaims.md` finding 2 (confirmed by recount) | none (no count is re-derived from the receipts when a SCORECARD row states a count) | the r97 SCORECARD and this lesson state 14 from the receipts, and the r96 row is corrected by an appended line (not rewritten). The C2 harness recount reproduces 14/19 with a per-delta match (`reports/round-97/controls/c2-v5-reproduced.log`). |
| M9 | **own-work located quote is not byte-verbatim:** the r96 quote `undefined8 entry(void) { return 0x2a; }` ("3 lines") is a whitespace-reflowed rendering. The saved block is five lines (line 7 blank). | `.ufo/waves/round-97/w1/ScoutReopen.md` §2.4 (`grep -c -F` → 0, exit 1); `corpus/live/runs/round-96/codeable-decompiled.c` | `C1_QUOTES` (passes it: the leg does not compare own-work quotes byte-exactly) | S505 superseding row with the byte-verbatim span; the quote-check leg (v6 `C1_QUOTES`) and the holdout run do not yet cover own-work rows byte-exactly, routed to r98 (see Frontier). |
| M10 | **fresh holdout exposed skip-work acceptance outside the frozen vectors:** the v5 counter accepts 8 of 12 named-class fresh forgeries (CriticR97), including row-set K inflation (FR06, FR07: a held row replaced by a copy of another row) and receipt/owner swaps. The frozen 19-vector set did not contain them. | `.ufo/waves/round-97/w1/CriticR97.md` (table, 8 accepted); `.ufo/waves/round-97/w1/CriticR97/holdout-v6.log` (v6: 5 of 12 accepted) | the frozen 19-vector set and its counting command (no row-set or owner-swap vector) | v6 refuses 7 of the 12 holdout forgeries. FR06 and FR07 are refused only incidentally, by the decorated-admitted leg, not by a row-set leg. FR02, FR08, FR09, FR10 and FR12 remain accepted. Routed to r98 as a frozen-counter amendment with its own fresh holdout (no change made in response in this round). |

Shown able to fail: M5 (red-v5 rc 1 / green-v6 rc 0 on the corpus-prefix fixture); M8 (count
recomputed from committed bytes, `c2-v5-reach-from-r96-receipts.txt`, not from prose); M9 (`grep -c -F` = 0
on the saved bytes, reproduced in ScoutReopen §2.4); M10 (holdout rows listed above).

## Frontier

- **Census before** — `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
  at `7d380ce` → exit 0, warnings only (21 × W01, 13 × W04), 0 E-codes.
- **Census after** — see the SCORECARD round-97 section and the report (round-end exit 0 required).
- **Rows added (by tier):** S505 (own-work, tier A, `mined`, `opened` 2026-11-05, `recheck` `on-release`,
  `used-by` = this entry once). Registry 504 → 505 rows.
- **Rows touched old → new:** none in place. S502, S503 and S504 keep `status=mined`, `recheck=on-release`,
  `opened=2026-11-05` and their used-by cells (the counter's `NEW_ROW_IDS` requires `mined`).
- **Frontier rows advanced:** C02 `partial` → `held` (coverage-map frontier → core), backed by this entry.
  The row's knowledge cell now names only this entry; the two pre-contract references it carried
  (`knowledge/seed.md`, `knowledge/2026-10-12-rea-readiness-checklist.md`) remain in the knowledge base
  and are no longer cited from that row.
- **Next frontier (routed):** M10 (fresh holdout forgeries: owner swap, row-set, header/fence, n/a
  boilerplate, dangling own-work pointer); M9 (byte-exact own-work quote leg); the M4 index gap
  (`corpus/knowledge/claude-red-re-bridge.md` still unindexed).

## considerthese

- **Proposal 1 of `considerthese/2026-11-05.md`** (counter-reachability review: write the cheapest
  skip-work control for every frozen predicate before the round lands) — mined and implemented as
  `reports/round-97/controls/skip-work-table.md` (six rows: do-nothing, always-pass stub, always-fail
  stub, id-edited copy, hand-fit name table, count audit). It implements no claim by itself.
