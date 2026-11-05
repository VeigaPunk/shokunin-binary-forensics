# Round 99 C1/C2 skip-work table (ExecControlsR99)

Freeze: Amendment A commit `61e27feb4e8099af7f9bf41fbf69e223354f691e` (entry bytes and
corpus/README.md byte-identical to the original claims freeze `7e6edd4d…`; adds the S505 used-by
grounding and `.ufo/waves/round-99/w1/swarm-registry.json`). Vote-binding digest re-confirmed
independently: v7 `digest()` on the committed candidate prints
`36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5`.

Instruments used for the dry-runs (all on scratch copies under
`/fast/scratch/hyaku/revenger-r99/ExecControlsR99/`; frozen bytes untouched, no lane writes):

- frozen counter `reports/round-98/c1_k_admit_counter7.py` (v7), `--profile c14`;
- frozen harness `reports/round-98/forge_reach7.py` plus byte-copied `forgeries7/` mutators;
- trees extracted with `git archive 61e27feb…` / `9d49002a…` (read-only git);
- WIP v8 `reports/round-99/c1_k_admit_counter8.py`, final sha256
  `620dfca9959572449638cab203485555c5d45f5a8e89c5b68121ffc2d3023581` (self-test
  `SELFTEST_C1V8=OK legs=98`); the C1-1 acceptance run is against these bytes. Earlier
  `c7a9a2c2…` and `a8a64ee1…` were superseded before acceptance.

Every dry run below is the round-98 development set / freeze-archive copies — the disclosed
development use, never a landing tree. `rc` = observed process exit code. Leg names are identical
in v8 (`c14r99` keeps every v7 leg, per the frozen interface contract); v8-only legs are named
`C1_VOTES_GLOB, C1_NA_REASON, C1_RECHECK_CMD, C1_HEX_CLAUSES, C1_COVMAP_ROW, C1_ROW_IDS,
C1_DECISION_KEYS, C1_OWNWORK_ROUND, C1_FETCHLOG_DATE` (v8 author commitment shared with
ExecHarness8/MutationR99). Where a row says *not run*, the refusing rule is quoted from frozen
code/contract instead.

## C1 routes (v8 `c14r99` surface; lazy L1 tries to bank C14 without the work)

| # | Lazy move | Refusing leg / rule | Dry-run instrument | Observed |
|---|---|---|---|---|
| C1-1 | Flip README only: C14 status cell `partial → held`, nothing else (no entry flip, no votes) | `C1_TARGET_CITES` (row cell must name exactly `knowledge/round-98-rea-host-readiness.md`), `C1_ADMITTED` (entry line must read `admission-status: admitted`), `C1_VOTES`/`C1_VOTES_GLOB` (no round-99 votes in tree). Note: `C1_K_HELD_BACKED` alone WOULD be satisfied (14/15) — the junk-row control exists precisely to show the other legs refuse | v7-c14 on the amended freeze tree (do-nothing analog, same legs); v8 c14r99 junk-row acceptance run | v7-c14 on `61e27feb…` tree: rc=1, `C1_VERDICT=fail`, 8 legs fail incl. `C1_TARGET_CITES`, `C1_ADMITTED`, `C1_VOTES`; v8 (sha `c7a9a2c2…`) junk-row run: rc=1, `C1_VERDICT=fail`, 6 legs fail, and `C1_K_HELD_BACKED=14/15` prints `pass` — the K leg alone is satisfied by the bare flip, the other legs refuse (see `.ufo/waves/round-99/w1/ExecControlsR99/accept/junk-row.log`) |
| C1-2 | Flip header only: edit the coverage-map legend or the table header row, C0x rows untouched | No leg reads header prose: `evaluate()` reads only lines matching `^\|[ \t]*C[0-9]+ ` with 5 cells (v7 c1_k_admit_counter7.py:775-777); the route is inert — verdict stays fail on the unmet legs | v7-c14 on mutated copy `r2-header` (legend + header cell edited) | rc=1, `C1_VERDICT=fail`; failing-leg set byte-identical to the untouched-tree baseline (diff empty, 8 legs) |
| C1-3 | Reuse round-98 votes as the round-99 votes | `C1_VOTES` digest binding ("vote digest mismatch"), then FAIL decisions ("decision Q11='FAIL' not PASS/n-a"), then `C1_VOTE_NOTES` (r98 short PASS notes fail the ≥6-token rule); under v8 additionally `C1_VOTES_GLOB` and the pinned-seat check — r98 seat names are absent from the round-99 `PINNED_SEATS`, so "seat not in pinned registry" fires first | v7-c14 on the amended freeze tree (its `reports/round-98/votes/` are the stale r98 votes) | rc=1, `C1_VOTES_WHY=vote digest mismatch for CriticR98 digest=36cc6ac2…` |
| C1-4 | Copy votes and patch only `candidate_sha256` to the round-99 digest | Next `C1_VOTES` check in line: any recorded FAIL decision refuses ("decision Q11='FAIL' not PASS/n-a" — claims kill rule: a vote recording FAIL fails `C1_VOTES`); artifacts must also name the new digest (see C1-5). v8 adds `C1_DECISION_KEYS` | v7-c14 on mutated copy `r4-digest` (all three r98 votes re-pointed at `36cc6ac2…`) | rc=1, `C1_VOTES_WHY=vote CriticR98 decision Q11='FAIL' not PASS/n-a digest=36cc6ac2…`; `C1_VOTE_NOTES` also fails on r98 short notes |
| C1-5 | Votes without artifacts (or artifact bytes not matching the vote/digest) | `C1_VOTES` artifact checks in order: path outside own seat dir → not a file → empty → `artifact sha mismatch` → "artifact does not name the candidate digest" (v7 check_votes, c1_k_admit_counter7.py:225-318; same rule in v8) | v7-c14 on mutated copy `r5-artifact` (digests re-pointed, FAILs forced to PASS, one forged voter with a missing artifact file) | rc=1, `C1_VOTES_WHY=artifact does not name the candidate digest: '.ufo/waves/round-98/w1/CriticR98/critic-audit-6d27c129.md'`; the missing-file check for the forged voter was not reached (earlier voter refused first) — code-named above |
| C1-6 | PASS notes copied verbatim between voters | `C1_VOTE_NOTES`: "PASS note shared verbatim" flags every voter sharing the note (v7 check_vote_notes, c1_k_admit_counter7.py:585-621; `notes_seen` map) | v7-c14 on mutated copy `r6-notes` (ReviewerGate Q06 note copied verbatim into ReviewerBlind, decision forced PASS) | rc=1, `C1_VOTE_NOTES_WHY=ReviewerBlind.json:Q06:PASS note shared verbatim; … ReviewerGate.json:Q06:PASS note shared verbatim` |
| C1-7 | S506 receipt date drift (`fetched_at` moved off `verified-at`/round date) | `C1_RECEIPTS` ("S506:fetched_at:'…'!=2026-11-05") and `C1_VERIFIED_AT` ("S506:fetched_at differs from verified-at/ROUND_DATE"); v8 adds `C1_FETCHLOG_DATE` (fetch-log date vs receipt) | v7-c14 on mutated copy `r7-receipt` (S506 `fetched_at` 2026-11-05 → 2026-11-04) | rc=1, both WHY lines observed verbatim |

## C2 routes (calibration; lazy harness work)

| # | Lazy move | Refusing rule | Dry-run instrument | Observed |
|---|---|---|---|---|
| C2-1 | Stub counter (always-pass or always-fail) | `C2_VERDICT` kill rule: accepted must be `0/12`; an always-pass counter prints `12/12`; an always-fail counter breaks the honest controls (`C2_POSITIVE`/`C2_CONTROL_*`). `C2_STUB_SELFTEST` separately proves the harness can count both ways | `forge_reach7.py --counter stub_pass.py` and `--counter stub_fail.py` | stub-pass: rc=0, `C2_ACCEPTED=5/5`, `C2_VERDICT=not-met`; stub-fail: rc=0, `C2_ACCEPTED=0/5`, `C2_POSITIVE=fail`, `C2_VERDICT=not-met` |
| C2-2 | Editing the builder (weaken a mutator so a vector stops mutating) | Accepted-count rule (a weakened vector gets accepted → `>0`) plus `C2_STUB_SELFTEST`'s `delta_applied` check (a non-control tree with no delta fails the self-test) | byte-copied harness+`forgeries7` with `m_verified_at_stale` (FR09) no-op'd, real v7 as counter, `--profile c02` | rc=0, `VECTOR FR09 verdict=pass failing=none`, `C2_ACCEPTED=1/5`, `C2_STUB_SELFTEST=fail`, `C2_VERDICT=not-met` |
| C2-3 | Dropping a vector from the battery | The frozen kill rule is textual: `C2_ACCEPTED=0/12` exactly — a dropped vector changes the denominator (`0/11 ≠ 0/12`); the harness stub self-test count also mismatches | byte-copied harness with FR10 removed from `ORDER`/`ROUTED_FIVE`, real v7 as counter, `--profile c02` | rc=0, `C2_ACCEPTED=0/4`, `C2_STUB_SELFTEST=fail`, `C2_VERDICT=not-met` |
| C2-4 | A control-BROKEN run (honest control fails) | `C2_POSITIVE`/`C2_POSITIVE2` in forge_reach7; `C2_CONTROL_C02=control-ok` / `C2_CONTROL_C14=control-ok` + kill rule in forge_reach8 (frozen claims §C2; forge_reach8 landed 19:01 but is ExecHarness8's instrument — its own 12-vector runs left to that seat and the L1, *not run* here) | `forge_reach7.py --counter stub_fail.py` (FR00 honest control fails) | rc=0, `C2_POSITIVE=fail`, `C2_POSITIVE2=fail`, `C2_VERDICT=not-met` |

## Reading

No route above reaches a passing verdict by skipping work: every C1 route is refused by a named
counter leg, and every C2 route is refused by the harness's cross-checks (denominator, controls,
stub self-test). The two controls in `make_c1_controls_r99.sh` are the enforcement points for C1-1:
the junk-row tree differs from the real landing tree only in that the entry stays `candidate` and
the votes stay absent, which is exactly what `C1_ADMITTED`/`C1_TARGET_CITES`/`C1_VOTES` refuse.
