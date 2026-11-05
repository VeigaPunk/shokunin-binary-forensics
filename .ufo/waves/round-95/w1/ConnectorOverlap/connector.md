# Proposal-1 adoption receipt — round 95 freeze (seat ConnectorOverlap, round 95, attempt 1)

Scope: the control classes named in `considerthese/2026-11-05.md` proposal 1 (counter-reachability review of each new `claims.md`), checked against the r95 freeze at `6e0bf15` (`reports/round-95/controls/`, the self-test delta list in `reports/round-95/claims.md` lines 96-111, and the counter/battery sources). Read-only: committed bytes only; no counter, battery or self-test was executed by this seat.

## A. Receipt inventory — `reports/round-95/controls/` (5 files, all committed at 6e0bf15)

| file | lines | what it records | verdict line(s) |
|---|---|---|---|
| `c1v4-do-nothing.log` | 29 | counter run on the FREEZE base (C1 do-nothing) | `C1_VERDICT=fail`, rc 1; `C1_C10_HELD=fail`; 14 of 17 printed legs fail on base (`C1_ROWS_TOTAL`, `C1_PYCACHE`, `C1_SIDS` pass) |
| `selftest-c1v4.log` | 2 | counter `--self-test` output | `SELFTEST_C1V4=pass legs=24`, rc 0 (aggregate only; no per-delta line) |
| `battery4-red-v3.log` | 14 | red-before: frozen v3 counter on the 10 TREE vectors and the M6 code mutant | `V3_REACH_NEW=10/10`; `MUTANT_V3_REGISTRY_SURVIVES=pass`; `RED_V3_VERDICT=pass`; rc 0 |
| `battery4-full-at-freeze.log` | 18 | full battery at freeze | `SELFTEST_C1V4=pass (POS + 22 deltas + do-nothing)`; 10 per-vector `KILLED` lines; `V4_KILLS=10/10`; `MUTANT_V4_REGISTRY_KILLED=pass`; `POS_C1V4=pass`; `DO_NOTHING_C1V4=fail-as-required`; `HOLD_R94_BATTERY=pass`; `BATTERY4_VERDICT=pass`; rc 0 |
| `census-round-start.log` | 36 | fleet census at round start | `ok` line for the lane; rc 0. No "rows 499" figure appears in the committed log (claims.md line 171 cites it) — not verified here |

Pre-landing caveat: none of the five files carries a timestamp, and all five were committed in the same commit as the predicates they test (see connector report, C-freeze).

## B. Claims self-test delta list — 22 deltas (claims.md lines 99-111) against the counter

Leg mapping check: all 22 claims.md pairs match `EXPECT_FAIL` in `reports/round-95/c1_k_admit_counter4.py` (lines 782-803). The self-test prints one aggregate line; per-delta output is not committed.

| # | delta (claims.md) | expected leg | matches EXPECT_FAIL | individual committed receipt |
|---|---|---|---|---|
| 1 | H1-indent-dup-status | C1_ADMITTED | yes | yes — `battery4-full-at-freeze.log` KILLED line (TREE vector) |
| 2 | F10-dup-status-fenced | C1_ADMITTED | yes | no — aggregate only |
| 3 | V10-stale-fetched-at | C1_RECEIPTS | yes | yes — battery KILLED line |
| 4 | V27-fabricated-body-foreign-host | C1_RECEIPTS | yes | yes — battery KILLED line |
| 5 | V07-legacy-path | C1_C10_CITES | yes | yes — battery KILLED line |
| 6 | V08-entry-pending | C1_C10_CITES | yes | yes — battery KILLED line |
| 7 | V03-dup-json-keys-registry | C1_REGISTRY | yes | yes — battery KILLED line |
| 8 | V04-dup-json-keys-vote | C1_VOTES | yes | yes — battery KILLED line |
| 9 | V19-sid-suffix-spaced | C1_SIDS | yes | yes — battery KILLED line |
| 10 | F16-unresolved-body-sid | C1_SIDS | yes | no — aggregate only |
| 11 | V18-na-letter-flood | C1_VOTES | yes | yes — battery KILLED line |
| 12 | F17-vacuous-na | C1_VOTES | yes | no — aggregate only |
| 13 | M6-forged-registry-seat | C1_REGISTRY | yes | no — aggregate only (the M6 *code* mutant is receipted separately: `MUTANT_V4_REGISTRY_KILLED=pass`) |
| 14 | M5-pycache-planted | C1_PYCACHE | yes | yes — battery KILLED line |
| 15 | F20-foreign-artifact-dir | C1_VOTES | yes | no — aggregate only |
| 16 | F12-case-dup-seat | C1_VOTES | yes | no — aggregate only |
| 17 | F13-role-mismatch | C1_VOTES | yes | no — aggregate only |
| 18 | F15-traversal | C1_VOTES | yes | no — aggregate only |
| 19 | F18-ws-output | C1_EMBED_NONVACUOUS | yes | no — aggregate only |
| 20 | F18b-tilde-fence | C1_EMBED_NONVACUOUS | yes | no — aggregate only |
| 21 | F19-stale-new-row | C1_SOURCES | yes | no — aggregate only |
| 22 | ONLY-C10-second-row | C1_ONLY_C10 | yes | no — aggregate only |

Count: 22 of 22 mapped; 10 individually receipted in the battery log; 12 aggregate-only (rows 2, 10, 12, 13, 15-22). The claims text says each delta "fails on its frozen expected leg"; for the 12 aggregate-only rows that statement rests on the counter's code plus one `pass` line, not on committed per-delta output.

## C. Proposal-1 named control classes — receipt status

Proposal 1 (considerthese/2026-11-05.md line 34) names four cheapest skip-work controls (lookup table, stub that prints the pass line, id-edited copy, no-work base) and, in its "today" paragraph, a hand-written entry copy with correct digest but non-independent votes. Status key: PRESENT = committed receipt on the frozen predicate; PARTIAL = receipt exists but covers only some legs or only an aggregate; ABSENT = no committed receipt in r95 controls.

| proposal-1 class | r95 receipt | status | what the receipt does / does not show |
|---|---|---|---|
| no-work base (do-nothing) | `controls/c1v4-do-nothing.log` (C1: `C1_VERDICT=fail` rc 1); `controls/battery4-full-at-freeze.log` `DO_NOTHING_C1V4=fail-as-required` (C2; battery source requires `C1_C10_HELD=fail` on the base, `forge_battery4.py` ~lines 281-288) | PRESENT | Shows the base is not green. Limit: the base also fails 13 other legs for trivial reasons (no entry, no votes dir, no registry, no receipts), so the C10 leg alone is never shown to discriminate a partially-worked base. No partial-work base receipt exists. |
| stub that prints the pass line | none in `controls/` | ABSENT | The battery's SELFTEST check is a substring test (`"SELFTEST_C1V4=pass" in stdout`, `forge_battery4.py` ~line 249) and the battery does not hash the counter file, so a stub counter would have to survive DO_NOTHING (which needs the literal `C1_C10_HELD=fail`) and POS. No committed stub run shows that it does not. Sibling precedent (cross-domain): kotodama round-94 ran one (see report). |
| id-edited copy | no copy-under-new-id delta; nearest deltas: F16-unresolved-body-sid, V19-sid-suffix-spaced, F19-stale-new-row, ONLY-C10-second-row, V07-legacy-path (rows 5, 9, 10, 21, 22 of §B) | PARTIAL | Id-shape and row-count mutants are receipted in the counter's self-test; only 2 of the 5 nearest deltas (V19, V07) have individual battery receipts; none has committed per-delta output. |
| lookup table fitted to the fixtures | none | ABSENT | Self-test fixtures are generated per run from counter-source code (`_fixture`), so a table keyed to those generated bytes is reachable in principle [INFERENCE]; no fitted-table control was run. The lane's own r91 precedent (a 21-entry table scoring the same as the real counter) is recorded in `measurement-r94.tsv` (row r91 C1) and `considerthese/2026-11-05.md` line 21. |
| hand-written entry copy, correct digest, non-independent votes | none | ABSENT (disclosed residual) | `check_votes` (counter lines 207-277) accepts any pinned seat whose artifact sits in `.ufo/waves/round-95/w1/<seat>/`, names the seat and the digest, and carries a PASS decision. The grep for "author" in the counter returns only the disclosure line 34. No author, lane-identity or independence check exists. claims.md defect 6 discloses that votes stay lane-internal. The r93 critic named "author self-votes" as reachable (`.ufo/waves/round-93/w1/CriticR93.md` line 19); that finding is outside the frozen eleven and is routed to r96 by claims.md line 157-158. |

## D. Result

- Four named classes: 1 PRESENT, 1 PARTIAL (id-edited copy, aggregate-only), 2 ABSENT (stub; lookup table) — plus the explicit non-independent-vote copy, ABSENT and disclosed.
- Proposal 1 is adopted in the claims text (claims.md lines 183-186, "the controls/ directory above is its receipt set"). On the table above, the receipt set does not yet cover every class the proposal names. The adoption itself is recorded by the L1 round lesson, not by this seat.
- Suggested routes (for the L1 and r96; no edit made here): (1) a stub-counter control with committed output; (2) a fitted-table control; (3) per-delta output lines from the self-test; (4) an author/lane-identity check in `check_votes` with a red-before, following tabi-shokunin's M4 precedent (cross-domain, §Cross-domain in the report).

## E. Lane state observed (read-only)

- `git -C revenger-shokunin status --porcelain`: ` M corpus/SOURCES.md`, ` M corpus/lessons/round-94.md`, `?? .ufo/waves/round-95/`. The lane working tree is not clean; this seat reads committed bytes (`6e0bf15`) and did not touch these paths.
- Entry digest check (for the vote binding; not a seat duty): `sha256sum corpus/knowledge/round-95-evidence-ledger-discipline.md` = `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`; `git show 6e0bf15:corpus/knowledge/round-95-evidence-ledger-discipline.md | sha256sum` = the same. The normalized-digest recipe was not run by this seat.
