# Round 98 — declared claims (FROZEN before any wave seat scores anything)

Lane: revenger. Base (round start, lane head): `34c56f9f324723cafd56fd57d718065b2ad2da66`.
This file and `controls/` are frozen by the claims-freeze commit recorded in the report. That commit
also carries the candidate entry, its record and its two registry rows. Predicates, targets, counting
commands and kill rules below are not edited after the freeze. A change made after any scoring is a
new claim, not this one.

Axes: C1 → **coverage**, the lowest owned criterion (K 13/15 = 8.67; rows C05 `uncovered` and C14
`partial`). C2 → **calibration**, the admission counter's reach over the forgeries that round 97 routed.
Two claims on two distinct axes, causally separable. C1 is verified by the v7 counter's `c14` profile,
which does not read the C2 vectors. C2 is verified by the v7 counter's `c02` profile on the round-97
holdout fixture trees, which do not read the C14 row or entry.

Ordering contract, enforced by the L1:
(a) this file, `controls/`, the candidate entry (`admission-status: candidate`), its record and the
S506/S507 rows are committed (the claims freeze);
(b) wave seats build `reports/round-98/c1_k_admit_counter7.py`, its fixtures and the harness. They cast
votes on the candidate, and they do **not** run any counter on a landing tree;
(c) the L1 commits the frozen v7 bytes (the v7 freeze);
(d) only after (c): the do-nothing and junk-row controls, then the landing tree and the holdout.

## C1 — coverage: C14 `partial → held` through the v7 counter (`c14` profile)

- **Surface moved:** coverage-map row C14 (`corpus/README.md`). Its knowledge cell becomes exactly
  `knowledge/round-98-rea-host-readiness.md` and its status `held`. The entry
  `corpus/knowledge/round-98-rea-host-readiness.md` moves `admission-status: candidate → admitted`.
  The flip is recorded as pending the non-author closure (routed defect r97 §6.5). This is a new
  coverage surface: a host-readiness decision table backed by a real route run this round (ZIP
  inventory) and a doctor receipt, which replaces the pre-contract 2026-10-12 checklist as the row's
  backing.
- **Vote-binding digest (normalized, v6 `digest()` rule):**
  `1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8`. The votes bind this digest.
  Any entry edit other than the admission-status line invalidates them.
- **Frozen predicate (one sentence, the same in the counter):** C14 counts as held only when the v7
  counter, run with `--profile c14`, passes every leg it prints. That set is every v6 leg retargeted to
  C14, the S506/S507 rows, the round-98 receipts, votes and wave registry, plus the new legs
  `C1_ROWSET`, `C1_ENTRY_BYTES`, `C1_HEADER_POSITION`, `C1_VERIFIED_AT`, `C1_VOTE_NOTES`,
  `C1_OWNWORK_PATHS`, `C1_QUOTE_BYTES` and `C1_USEDBY_GROUNDED`.
- **Before:** `K = 13/15` held. C14 is `partial` at `34c56f9`
  (`reports/round-98/controls/c1-base-rowstatus.log`: 13 held, 1 partial, 1 uncovered).
- **After (target):** `C1_K_HELD_BACKED=14/15` and `C1_VERDICT=pass` from
  `PYTHONUTF8=1 python3 -B reports/round-98/c1_k_admit_counter7.py --profile c14 --tree <landing-archive-root>`, with exit 0.
- **Do-nothing control (run after the v7 freeze, before landing scoring):** the v7 `c14` profile on
  `git archive` of the claims-freeze commit must print `C1_VERDICT=fail`. In that tree C14 is still
  `partial` and the entry is a candidate.
- **Junk-row control (run after the v7 freeze, before landing scoring):** the claims-freeze tree with
  only the C14 status cell edited to `held` and no other change must print `C1_VERDICT=fail`.
- **Kill rule:** any failing leg on the landing tree, K ≠ 14/15, or a control that passes means C1 is
  **not verified**. An honest miss is recorded, never narrowed. A vote that records any FAIL decision
  fails `C1_VOTES`, and therefore C1.
- **Admission caveat:** the votes are lane-internal. Admitting the entry needs the non-author closure
  (LEARNING.md). The entry's admission line says so.
- **Sourced-claim duty (§2b.4):** C1 rests on S506 (REA connection-and-recovery reference at pinned
  revision `12f6e09`, fetched 2026-11-05) and S507 (own-work record saved 2026-11-05).

## C2 — calibration: counter reach over the round-97 routed holdout forgeries

- **Surface moved:** the admission counter's legs against the five round-97 holdout forgeries that
  frozen v6 accepts (FR02 entry leading BOM, FR08 headers in a fence, FR09 stale verified-at, FR10
  n/a boilerplate on a PASS note, FR12 dangling own-work pointer). Also the two row-set forgeries
  (FR06, FR07), which v6 refuses only incidentally through `C1_ADMITTED_UNION`.
- **Frozen predicate (one sentence, the same in the harness):** a vector counts as *accepted* when the
  counter prints `C1_VERDICT=pass` on the tree carrying that vector. The harness counts accepted vectors
  over the five routed vectors, rebuilt by the round-97 builder
  (`.ufo/waves/round-97/w1/CriticR97/fresh/build_fresh.py`), with the counter run as `--profile c02`.
- **Before (do-nothing control, frozen v6):** `accepted = 5/5` (FR02, FR08, FR09, FR10, FR12), re-run
  on this host on 2026-11-05: `reports/round-98/controls/c2-do-nothing-v6-holdout.log`
  (`BUILD_OK=True vectors=15 accepted=5`. The five accepted are exactly the routed five. FR00 honest
  control passes.)
- **After (target):** `C2_ACCEPTED=0/5`, printed in one recorded run together with `C2_POSITIVE=pass`
  (v7 `c02` accepts the FR00 honest control tree) and `C2_STUB_SELFTEST=ok` (an always-pass stub
  counter scores 5/5 and an always-fail stub 0/5 on the **fully built** vector trees, so every vector
  delta is applied). The run also prints `C2_ROWSET_FR06=C1_ROWSET` and `C2_ROWSET_FR07=C1_ROWSET`:
  the named leg that refuses each row-set forgery must be `C1_ROWSET`.
- **Counting command:**
  `PYTHONUTF8=1 python3 -B reports/round-98/forge_reach7.py --counter reports/round-98/c1_k_admit_counter7.py --work <scratch>`
  Output lines: `C2_ACCEPTED=<n>/5`, `C2_POSITIVE=<pass|fail>`, `C2_STUB_SELFTEST=<ok|fail>`,
  `C2_ROWSET_FR06=<leg list>`, `C2_ROWSET_FR07=<leg list>`.
- **Kill rule:** `C2_ACCEPTED` ≠ 0/5, `C2_POSITIVE` ≠ pass, `C2_STUB_SELFTEST` ≠ ok, or `C1_ROWSET`
  missing from either row-set line means C2 is **not met**.
- **Development-set disclosure:** v7 is developed against these five vectors, so 0/5 is a
  development-set result. The discrimination evidence is a **fresh round-98 holdout** written by the
  critic seat. The L1 runs it once against the committed v7, after the v7 freeze. It is reported
  separately and is not part of the target. No counter change responds to it in this round.
- **Positive control on the real tree (reported):** v7 `--profile c02` on the landing archive must
  print `C1_VERDICT=pass`, so C02 stays held. A fail is reported as harm to C02.

## Frontier and duties (§2b, not claims)

- **Census before:** `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
  at round start (base `34c56f9`) → exit 0, warnings only. A census after the S506/S507 append also
  exits 0. A census at round end, with exit 0, is required.
- **Mistake mined:** routed r97 defect §6.1, the S505 `used-by` cell naming an entry that never cites
  S505 (captured-by: none, since v6 checks used-by only for S502–S504). The fix is the v7
  `C1_USEDBY_GROUNDED` leg, shown able to fail on the base registry, plus a logged old→new correction of
  the S505 `used-by` cell.
- **considerthese:** one still-unimplemented proposal from the latest file, if any. Mined by the scribe
  and landed as a lesson section.
- **Assimilation:** none this round. The round-97 collision (155/155 staged ids) stays open on L0. The
  package's current presence is re-checked and reported.

## Shape

One v1 wave, 12 seats (policy band 8–16): executor 3, scout 1, scribe 1, connector 1, reviewer 3,
critic 1, mutation-tester 1, sentinel 1. Attack share 5/12 (reviewer ×3, critic, mutation-tester), which
is ≥ 25 %. Connector seats 1 (≤ 2). The L1 holds the planner seat, because the validator rejects
`planner`. Godspeed leads every L2 prompt.

---

## Amendment A — recorded before the v7 freeze and before any landing-tree scoring (2026-11-05)

This amendment is appended. It does not replace any frozen sentence above. It comes from
ReviewerClaims findings F1–F7 (`.ufo/waves/round-98/w1/ReviewerClaims.md`). It clarifies or tightens
the claims and widens no target. It was sent to ExecCounterV7 and ExecHarness7 before any v7 bytes
were frozen.

**A1 — C2 real-tree positive control (F1).** The c02 profile compares the README with its own
`FREEZE_REV` and accepts a difference in C02 only (`C1_ONLY_TARGET`). The round-98 landing changes
C14, so v7 `--profile c02` on the landing archive cannot pass by construction. That run is therefore
reported as a diagnostic only, under this rule: **no harm to C02** when (i) the C02 README row on the
landing tree is byte-identical to the row at `34c56f9`, and (ii) every failing c02 leg on the landing
tree is `C1_ONLY_TARGET`, with its diff list naming only C14. A failing leg other than that one is
reported as harm.

**A2 — `C1_USEDBY_GROUNDED` scope (F2).** The leg checks only the profile's row set: c14 checks
S505, S506 and S507; c02 checks S502, S503 and S504. A row is grounded when every knowledge path in
its used-by cell exists and cites the row id as a whole word. A used-by cell of `—` is grounded. The
S505 correction is fixed at status `mined → queued` and used-by
`corpus/knowledge/round-96-native-analysis-sessions.md → —`, logged old→new in the lesson.

**A3 — FR10 mechanism (F3).** The PASS-note rule of `C1_VOTE_NOTES` applies only in the c14
profile. The c02 honest fixture uses boilerplate notes on its PASS rows. In both profiles the leg also
refuses a vote that marks Q09 `n/a` when the entry contains a 64-hex digest token, because Q09
governs digest claims. That applicability rule is what refuses FR10.

**A4 — second positive (F4).** The harness also builds `FR00b-benign-extra-file`: FR00 plus one new
file, `reports/round-98/benign-r98.txt`, holding one plain sentence. It prints `C2_POSITIVE2`. C2 is
met only if `C2_POSITIVE=pass` and `C2_POSITIVE2=pass` both hold, in addition to the frozen
conditions. This makes C2 stricter.

**A5 — do-nothing receipt recipe (F5).** `controls/c2-do-nothing-v6-holdout.log` was produced with
a scratch copy of the r97 builder whose `COUNTER` line points at
`reports/round-97/c1_k_admit_counter6.py`. The committed builder still drives v5 by default, and
under v5 it yields `accepted=8`. ReviewerClaims reproduced both numbers
(`ReviewerClaims/rb5-table.txt`, `rb6-table.txt`).

**A6 — normative contract (F6, F7).** The v7 interface contract in the wave context of
`.ufo/waves/round-98/w1-spec.json` is normative for leg names and profile constants. In the c14
profile, `C1_DERIV_TABLE` recomputes the entry's recorded digests from the tree: the archive-r2
fixture, the S506 body, and the record-file prefixes.
