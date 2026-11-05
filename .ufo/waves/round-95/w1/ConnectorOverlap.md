# ConnectorOverlap — round 95, attempt 1 (revenger)

Seat: ConnectorOverlap (connector, leaf, no dispatch). Read-only over siblings and over the lane's committed bytes (freeze `6e0bf15`). Judged on coverage. Milestone: C1 K 11/15 → 12/15 (C10 via the v4 gate); C2 v4 counter kills the r94-routed named vectors; 13 seats.

Written: `.ufo/waves/round-95/w1/ConnectorOverlap/measurement-r95.tsv`, `.ufo/waves/round-95/w1/ConnectorOverlap/connector.md`, this file. Nothing else written. No lane file, git state, sibling lane, fleet file or `~/.local/bin` touched. No installs or updates performed. Scratch `/fast/scratch/hyaku/revenger-r95/ConnectorOverlap/` created and removed before yield (it held no files).

## 1. Sibling scan — CROSS-DOMAIN (belongs to each lane; not absorbed here)

Scope: the newest three files of each sibling's `corpus/lessons/`, selected by mtime (chousa-shokunin, kotodama-shokunin, tabi-shokunin, souji-shokunin), keyword-scanned for counter-reachability, receipt honesty and vote binding, then targeted reads of the cited lines. Not every line of every file was read. No sibling file was edited.

| lane | newest three files scanned | overlapping evidence (file:line) | theme | disposition |
|---|---|---|---|---|
| chousa-shokunin | `round-80-verifier-spotcheck.md`, `round-80.md`, `round-79-erratum.md` | `round-80.md:150` — a preserved attempt's controls and claims committed in one commit, so controls-before-freeze is shown by commit order only | receipt honesty (freeze ordering) | CROSS-DOMAIN. Same limit applies to r95's single freeze commit `6e0bf15` (see connector.md §E and measurement caveat C-freeze). |
| chousa-shokunin | (same) | `round-80.md:169-171` — "A hollow record passes the counter": base bytes reach `GATE_GROUNDING=PASS` on a do-nothing control | counter reachability | CROSS-DOMAIN. Relevant to how much the r95 do-nothing receipts discriminate (connector.md §C row 1). |
| chousa-shokunin | (same) | `round-80.md:176-180` — the drawn battery prints PASS on one run and FAIL on the next over the same bytes | battery stability | CROSS-DOMAIN. The r95 battery uses fresh `mkdtemp` fixtures; no flake was observed in r95 committed logs. |
| kotodama-shokunin | `round-94.md`, `round-93-verifier-spotcheck.md`, `round-93.md` | `round-94.md:117` — a stub control "prints `SELFTEST PASS 89/89` with only 34 ok lines" and fails SELFTEST, BATTERY and MUTATION | stub-that-prints-pass class, receipted in a sibling | CROSS-DOMAIN. Precedent for the r95 class that has no receipt (connector.md §C row 2). |
| kotodama-shokunin | (same) | `round-94.md:58`, `round-94.md:123` — verifier defect classes accepted by the grader; an independent critic's 13 new counterfeit classes | named-vector routing | CROSS-DOMAIN. Same pattern as r95's eleven named vectors, in another lane's counter. |
| kotodama-shokunin | (same) | `round-93-verifier-spotcheck.md:31` — do-nothing controls with committed refusal receipts | do-nothing receipts | CROSS-DOMAIN. Comparable receipt form. |
| tabi-shokunin | `round-68.md`, `round-68-verifier-spotcheck.md`, `round-67-verifier-spotcheck.md` | `round-68.md:42`, `:55`, `:72` — pre-fix gate passed self-adjudication: a literal `tabi` match let the seat alias `TabiR68a2` through (M4); fixed by identity matching and QUALITY 126; `round-68-verifier-spotcheck.md:38-40` committed red receipts | vote binding / self-vote | CROSS-DOMAIN. Direct precedent for r95's ABSENT class "non-independent votes" (connector.md §C row 5). |
| souji-shokunin | `round-67.md`, `round-67-verifier-spotcheck.md`, `round-66-verifier-spotcheck.md` | `round-67.md:59` (M2) — a kill-power selftest case fired whether or not the rule was reverted, so it was vacuous; `round-67.md:66` (M9) — a frozen target did not measure two clauses of the claim, and a candidate with no scrub met it | vacuous kill receipts; claim wording wider than the frozen predicate | CROSS-DOMAIN. M2 bears on r95's twelve aggregate-only self-test deltas (connector.md §B); M9 is the same overreach class as r94 C2's "classes" wording. |

## 2. Frozen-counter validity rate, r94–r95 window (measurement-r95.tsv)

Carried rows r89–r93 are unchanged from the r94 measurement.

- r94 C1 — spot-check re-derived the frozen predicate (held rows 10 → 11 of 15; 14 counter legs pass; do-nothing `C1_C15_HELD=fail`). Verdict class `spotcheck-admitted`; **counted 1** (headline) because the closure's own caveat "votes lane-dispatched" (`round-94-verifier-spotcheck.md:53`, `:122`) is open.
- r94 C2 — 12 named vectors killed (`BATTERY3_VERDICT=pass`). Class `spotcheck-admitted`; **counted 1** (headline) because the "classes" wording overreaches the named vectors (`:64`, `:121`).
- r95 C1, C2 — `pending`; counted 0; no committed verdict until landed and closed by a non-author.

Totals:

| reading | r89–r93 | r94 | running |
|---|---|---|---|
| headline (r94 both counted 1) | 10 of 10 invalid | 2 of 2 | **12 of 12 = 100 %** |
| sibling (r94 both counted 0, the closure's own verdict words) | 8 of 10 | 0 of 2 | **8 of 12 = 67 %** |

The rate has no r95 reading yet. Whether v4 plus the r95 controls reduces it is measurable only after r95 is closed. Proposal 2 remains a baseline, not an adopted criterion.

Re-check of the r94 closure's own recount: `awk` over rows r90–r93 gives 8 rows with 0 `clean`, matching this seat's table.

## 3. Proposal-1 adoption receipt (connector.md)

- `controls/` holds five committed files (census, do-nothing, self-test aggregate, red-before v3, full battery). All were committed in the freeze commit with the predicates they test.
- The 22 self-test deltas in claims.md map one-for-one onto the counter's `EXPECT_FAIL` table. Ten are individually receipted in the battery log; twelve are receipted only by the self-test's aggregate `pass` line.
- Proposal 1 names four cheapest controls and one explicit test. Receipt status:
  - no-work base — PRESENT (both counters), with the limit that the base fails 14 of 17 legs, so the C10 leg alone is never shown to discriminate;
  - stub that prints the pass line — ABSENT;
  - id-edited copy — PARTIAL (nearest deltas are receipted only in part);
  - lookup table — ABSENT;
  - hand-written entry copy with correct digest and non-independent votes — ABSENT, disclosed as defect 6 in claims.md.
- Verdict on the adoption: the claims text says "the controls/ directory above is its receipt set". On the evidence the receipt set does not yet cover every named class. This is a finding, not a verdict on the round.

## 4. Open items and routes (for the L1 and reviewers; no edit made here)

1. Non-independent votes: `check_votes` (counter lines 207-277) has no author or lane-identity check; a vote artifact that names a pinned seat and the digest passes. The r93 critic named "author self-votes" (`.ufo/waves/round-93/w1/CriticR93.md:19`) and claims.md routes new forgeries to r96 (lines 157-158). tabi-shokunin's M4 fix is the precedent to cite.
2. Stub counter and fitted table: no committed control. kotodama round-94 shows the stub control is cheap to run.
3. Per-delta self-test output: 12 of 22 deltas have no committed per-delta receipt. A red-before that breaks each delta's rule (souji M2 pattern) would show whether each delta is vacuous.
4. Census: `controls/census-round-start.log` does not print the "rows 499" figure that claims.md line 171 cites. Not verified here.
5. Proposal-1 adoption must be recorded by the L1 round lesson with the file and date citation (claims.md lines 183-186). Not done by this seat.
6. Lane tree at reading time: `M corpus/SOURCES.md`, `M corpus/lessons/round-94.md`, `?? .ufo/waves/round-95/`. Likely L1 work in progress; this seat did not touch these paths.

## 5. Checks not run

- No counter, battery, self-test or census was executed by this seat (reading committed bytes only). Leg and verdict statements above are from committed logs and source text, not fresh runs.
- The normalized vote digest was not recomputed; `sha256sum` of the working-tree entry equals `git show 6e0bf15:` bytes (`476edc36…479fb9`).
- No `git` write, no network use, no installs.

## Summary for the main agent

Counted r94–r95 window: headline 12 of 12 invalid (100 %), sibling reading 8 of 12 (67 %); r95 pending. Proposal-1 receipts: 1 present, 1 partial, 2 absent, 1 absent-and-disclosed. Cross-domain precedents recorded above for chousa, kotodama, tabi and souji; none absorbed.
