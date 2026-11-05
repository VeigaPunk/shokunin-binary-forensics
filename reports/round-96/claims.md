# Round 96 — frozen claims (revenger, hyaku run 15, attempt 1)

Frozen before any wave seat ran. Base = lane branch tip at freeze
(`2875b9c9fa4cc15fd5a8ff991f04cdd0417bec97`, the round-95 verifier spot-check tip). Nothing
in this file changes after the freeze; a miss is an honest stop, never a narrowed target.
The frozen r93/r94/r95 instruments (`reports/round-93/*`, `reports/round-94/*`,
`reports/round-95/*`) are not modified this round (kumitate r42 rule).

Carry-in. The round-95 non-author verifier spot-check
(`corpus/lessons/round-95-verifier-spotcheck.md`) admitted both r95 claims and routed
defects; THIS round's declared work consumes them: the C1 v5 successor counter freezes the
routed closes as legs (spotcheck §5 item 2 / SCORECARD r95 "Routed to r96" items 1–5), the
spotcheck's §5 item 1 erratum is appended to `corpus/lessons/round-95.md` (lane-internal
votes relabel) in this freeze, item 6 (the non-author re-fetch of S500/S501) was performed
BY the spot-check itself (§3, HTTP 200, sha256 equal to the committed bodies) and is cited
from this round's report, item 3 (calibration vectors authored outside the counter's author)
is honored by authorship: the three NEW vector designs are CriticR95's A4/A3-both findings
and MutationR95's M8, committed in `.ufo/waves/round-95/w1/` before this freeze, and only
their operationalization into deltas happened in this freeze. Every predicate below was
checked to fail on the do-nothing base before the freeze
(`controls/c1v5-do-nothing.log`, rc 1), the red-before was executed and committed at freeze
(`controls/battery5-red-v4.log`), and the full battery was green at freeze
(`controls/battery5-full.log`, `BATTERY5_VERDICT=pass`, `HOLD_R95_BATTERY=pass`).

Deviation disclosed (r95 planned wording): r95's planned line said "the next admissible
C-row through the v4 gate". The frozen v4 counter bytes are row-bound to C10
(`C1_C10_CITES` pins the C10 backing cell to the round-95 entry; `C1_ONLY_C10` pins every
other row to the base archive), so no other C-row can pass those frozen bytes and the
kumitate r42 rule forbids editing them. "The v4 gate" therefore lands as the v5 successor
carrying every v4 leg unchanged plus the routed closes — the same successor pattern the
lane used in r93→r94→r95.

## C1 — coverage K (the lowest non-retired axis, 12/15 = 8.0): C02 partial → held through the v5 gate

**Claim type:** axis move. **Target axis:** coverage. **Axis rule:** this is the round's lowest-axis claim: `SCORECARD.md` r95 section carries
`K_HELD_BACKED` 12/15 = 8.0 as the lowest owned criterion score (the calibration criteria
sit at 10.0), and r95's `planned` row names exactly this move; the stagnation nudge does
not apply (a capability entered in r80/r91 and criteria sit at or above the saturation
line).  **Exploratory:** no.

**What moves.** Coverage-map row C02 (native analysis sessions — decompile/disassemble
providers) moves `partial` → `held`, backed by the NEW admitted entry
`corpus/knowledge/round-96-native-analysis-sessions.md` (REA's documented native routes at
pinned revision `12f6e09` per S502/S503, plus one demonstrated session on this host per the
own-work row S504: `rea decompile` exit 0 with Evidence `ev_cc0b9d88…` and the
ghidra-headless reproduction, both on the committed pe-r75 fixture, both receipted). The
C02 row's knowledge cell names exactly this entry; no other coverage row changes. Two
GitHub-fetched source rows (S502 native-and-artifacts reference 38167 B sha256
`c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24`; S503 skill SKILL.md
35095 B sha256 `b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc`) are
opened 2026-11-05 with receipts committed at FREEZE under `reports/round-96/quote-receipts/`;
the own-work row S504 names the saved record `corpus/live/runs/round-96/`. Three
lane-internal gate votes (reviewer ×2, critic ×1) bind the final normalized candidate
digest `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` under the v5
rules; the admission flip follows the votes and does not change the normalized digest.
The votes are disclosed as lane-internal (LEARNING.md: a subagent the lane dispatched is
still the lane); the verdicts are "met on the frozen counter, pending the non-author
closure".

**Before → after.** before: `K_HELD_BACKED=12/15` (C02 `partial`); after:
`K_HELD_BACKED=13/15`. Score: 8.0 → 8.7.

**Counter (frozen):** `PYTHONUTF8=1 python3 -B reports/round-96/c1_k_admit_counter5.py
--rev <landing>`. Every v4 leg carried unchanged: `C1_ROWS_TOTAL` (15×5 cells),
`C1_C02_HELD`, `C1_C02_CITES` (the C02 backing-cell knowledge-file set EQUALS exactly
`[knowledge/round-96-native-analysis-sessions.md]`), `C1_ONLY_C02` (every other coverage
row byte-identical to the frozen base archive), `C1_ADMITTED` (exactly one wide-anchored
status line in the header window, value admitted), `C1_TRIO`, `C1_REGISTRY` (strict JSON
equals the pinned 12-seat map), `C1_VOTES` (≥2; seats against the pinned registry; digest
equality; Q01–Q17 decisions with ≥1 PASS; n/a vocabulary; per-seat artifact in its own
wave dir naming seat + digest), `C1_RECEIPTS` (fetched_at/http 200/host allowlist/body
re-hash/fetch-log line, over S502+S503), `C1_PYCACHE` (WIDENED: no `__pycache__` under
corpus, reports/round-93..96, .ufo/waves/round-95..96), `C1_LINT`, `C1_EMBEDDED`,
`C1_EMBED_NONVACUOUS`, `C1_SIDS`, `C1_SOURCES` (strict registry read; every cited sid
mined-terminal; new rows mined/tier A/opened 2026-11-05/cite-back AND used-by EXCLUSIVE
to this entry — the A3-both close), `C1_QUOTES`, and the NEW `C1_ADMITTED_UNION` (every
knowledge file whose bytes carry an admitted status line must be named in the
coverage-row knowledge union — the A4 shadow-entry close). No saved-record oracle leg:
the record IS the own-work row S504 (cited, digest-pinned in the derivation table).

**Predicate (frozen):** `C1_VERDICT=pass`, exit 0 — every leg passes.

**Kill rule.** Any leg fails ⇒ C1 **not verified**, reported as such. No counter, claims,
control-receipt or kill-rule byte changes after the freeze; a defect found post-vote is
either a full vote re-bind to the corrected final digest (the r93 lesson M1 procedure) or
an honest miss — never a rule edit.

**Do-nothing control (must fail; `controls/c1v5-do-nothing.log`):** the base revision
scores `C1_C02_HELD=fail` ⇒ `C1_VERDICT=fail`, exit 1. **Self-test (positive + kills;
`controls/selftest-c1v5.log`):** `SELFTEST_C1V5=pass legs=33` — the honest
admission-shaped fixture (REAL entry bytes, REAL lint, REAL embedded checker, synthetic
registry/votes/receipts) passes every leg, and thirty-one forged deltas each fail on
their frozen expected leg: the twenty-two v4-carried deltas (H1-indent-dup-status→
C1_ADMITTED, F10-dup-status-fenced→C1_ADMITTED, V10-stale-fetched-at→C1_RECEIPTS,
V27-fabricated-body-foreign-host→C1_RECEIPTS, V07-legacy-path→C1_C02_CITES,
V08-entry-pending→C1_C02_CITES, V03-dup-json-keys-registry→C1_REGISTRY,
V04-dup-json-keys-vote→C1_VOTES, V19-sid-suffix-spaced→C1_SIDS,
F16-unresolved-body-sid→C1_SIDS, V18-na-letter-flood→C1_VOTES, F17-vacuous-na→C1_VOTES,
M6-forged-registry-seat→C1_REGISTRY, M5-pycache-planted→C1_PYCACHE,
F20-foreign-artifact-dir→C1_VOTES, F12-case-dup-seat→C1_VOTES,
F13-role-mismatch→C1_VOTES, F15-traversal→C1_VOTES, F18-ws-output→C1_EMBED_NONVACUOUS,
F18b-tilde-fence→C1_EMBED_NONVACUOUS, F19-stale-new-row→C1_SOURCES,
ONLY-C10-second-row→C1_ONLY_C02) PLUS the nine r95-routed deltas
(A4-shadow-admitted→C1_ADMITTED_UNION, A3-usedby-extra→C1_SOURCES,
M8-pycache-frozen-dir→C1_PYCACHE, ROWS-total-extra-row→C1_ROWS_TOTAL,
TRIO-missing-recheck→C1_TRIO, LINT-qmap-missing-row→C1_LINT,
EMBEDDED-fake-fence→C1_EMBEDDED, QUOTES-mutated-body→C1_QUOTES,
KHELDBACK-broken-cell→C1_K_HELD_BACKED), each with a per-delta receipt
(`controls/per-delta/<delta>.json`, one per delta — the connector's aggregate-only
receipt close).

**Separability.** C1's counter reads the C02 row, the entry, the votes, the receipts, the
registry and the base archive; it never runs the battery's forged trees or mutant code.
C2's battery builds its own synthetic fixtures from the frozen v4/v5 fixture generators
plus scratch copies for mutants; its verification does not need C1 landed.

## C2 — calibration: the v5 counter closes the r95-routed NEW vectors the frozen v4 counter still passes, and the self-test coverage gap

**Claim type:** axis move. **Target axis:** calibration (evidence-ledger discipline: the
frozen v4 counter passes three routed NEW vectors — CriticR95 A4 shadow entry, A3-both
used-by drift, MutationR95 M8 frozen-dir pycache — and its self-test has NO discriminating
delta on six legs and no per-delta receipts; spotcheck §5 item 2, routed in
`corpus/lessons/round-95.md` and `.ufo/waves/round-95/w1/`).

**What moves.** `reports/round-96/c1_k_admit_counter5.py` and
`reports/round-96/forge_battery5.py` land as the successor instrument and its battery.
Red (committed at freeze): the FROZEN v4 counter PASSES all three NEW vectors built on an
honest v4-shaped fixture (`controls/battery5-red-v4.log` — `V4_REACH_NEW=3/3`) and the six
legs are absent from v4's frozen self-test delta map
(`V4_SELFTEST_UNCOVERED=6/6`); `RED_V4_VERDICT=pass`. After: the v5 counter kills every
NEW vector on its frozen leg (`V5_KILLS=3/3`), its self-test carries a discriminating
delta for all six legs with a per-delta receipt each (`DELTA_RECEIPTS=31/31`), the same
registry-gate code mutant DIES on v5 (`MUTANT_V5_REGISTRY_KILLED=pass`), the
stub-prints-the-pass-line control is rejected (the connector's finding;
`STUB_REJECTED=pass`), and the frozen r95 battery holds (`HOLD_R95_BATTERY=pass`).
Vector-authorship disclosure: the three NEW vector designs are CriticR95's and
MutationR95's committed findings (outside the counter author); fresh v5 attacks authored
by this round's CriticR96 seat are routed to r97 and are not this round's predicate.

**Before → after.** before: `V4_REACH_NEW=3/3` + `V4_SELFTEST_UNCOVERED=6/6` (frozen v4);
after: `V5_KILLS=3/3` + `DELTA_RECEIPTS=31/31` + `V5_SELFTEST` full coverage.

**Counter (frozen):** `PYTHONUTF8=1 python3 -B reports/round-96/forge_battery5.py
--stage full` (predicate), plus `... --stage red-v4` as the committed red-before. The v4
counter/battery bytes (`reports/round-95/*`) are not modified; mutants run on scratch
copies only.

**Predicate (frozen):** `BATTERY5_VERDICT=pass` (exit 0) from `--stage full`.

**Kill rule.** Any NEW vector surviving v5, the M6 mutant surviving v5's self-test, any
positive control failing, the do-nothing control passing, the stub control passing a
stub, or the r95 hold failing ⇒ C2 **not verified**. Survivors are a miss, not a counter
edit (kumitate r42 rule). New forgeries the wave's critic finds beyond the frozen three
are routed to r97 with receipts — they do not change this predicate.

**Separability.** The battery imports the frozen v4 fixture generator and the v5 counter,
builds every tree from the FREEZE_REV archive plus synthetic fixtures in scratch, and
never reads the wave's landed votes or the C02 flip. C1's verification never runs the
battery.

## Frontier step (§2b; not a claim)

- `corpus/SOURCES.md`: S502, S503 and S504 appended at landing (all opened 2026-11-05;
  S502/S503 GitHub-fetched with receipts frozen pre-data under
  `reports/round-96/quote-receipts/`, located ≤25-word quotes in the round lesson's
  `## Gate`; S504 own-work naming the saved record). Census before → after with the
  driver command and its exit codes in the report. Census round start (pre-freeze): exit 0
  (`controls/census-round-start.log`).
- Sourced claim: C1 rests on S502 and S503 (§2b.4) plus the own-work record S504.
- One mistake mined into `corpus/lessons/round-96.md` `## Mistakes` (class · evidence ·
  captured-by · fix); candidates this round: the counter5 build-time delta defects caught
  by its own self-test before the freeze (F19 stale anchor, V10/V27 row-sid mismatches,
  the materialization drop of non-archived planted dirs, the BACKED-exclusion parser
  filter — each caught by `SELFTEST FAIL` lines in a pre-freeze run), the unindexed
  `knowledge/claude-red-re-bridge.md` candidate found by the union survey, and any
  wave-found defect.
- Gate reject record: the round-96 `## Gate` carries at least one reject with reasons
  (candidates this round: a C05 Android K-move — the r95 spot-check already ruled a
  seventh candidate without a new primary APK/AXML source is a repeat failure; adding a
  C16 atlas row this round — would change the frozen K denominator mid-round).
- Assimilation: expected `none` (155/155 staged-id collisions; L0 `revenger | round-91`
  unanswered) — re-verified fresh at round end with the frozen collision check by the
  connector seat.
- considerthese: proposal 1 of `considerthese/2026-11-05.md` (pre-landing
  counter-reachability review) remains ADOPTED as standing practice — this freeze's
  controls directory is its receipt set, now with per-delta receipts and the stub control
  closing r95's recorded PARTIAL gap.

## Round shape (fixed here, before dispatch)

ONE v1 wave, 12 seats, band 8–16 (`scripts/hyaku/ufo-wave-policy.json`: waveMinLanes 8,
waveMaxLanes 16): ScoutReopen ×1 (scout), ScribeLesson ×1 (scribe), ExecSession ×1,
ExecReceipts ×1, ExecBattery ×1, ExecFrozen ×1 (executor), ReviewerGate ×1, ReviewerBlind ×1
(reviewer), CriticR96 ×1 (critic), MutationR96 ×1 (mutation-tester), ConnectorOverlap ×1
(connector), SentinelScope ×1 (sentinel). Attack seats: reviewer ×2 + critic +
mutation-tester = 4/12 = 33.3 % (≥25 %). Connector: 1 (≤2). Residual call: none.
The L1 holds the canonical planner seat; no planner seat is dispatched (the validator
rejects it). Routing is `task.agentModelOverrides` (operator-owned); no model is passed.
The L1 alone writes SOURCES.md, README.md, SKILL.md, SCORECARD.md, LOG.md, the round
lesson, and `reports/round-96/votes/*`; seats write only their own wave dirs and scratch.
Spec-template rule (r94 lesson M5): every seat Python invocation uses `python3 -B`; no
seat writes into any lane file directory.

## Predicates are the frozen sentences

- C1: `C1_VERDICT=pass` from `c1_k_admit_counter5.py --rev <landing>`.
- C2: `BATTERY5_VERDICT=pass` from `forge_battery5.py --stage full`.
Neither predicate, counter, control receipt, kill rule or target may change after the
freeze. A miss is recorded as a miss.
