# Round 94 — frozen claims (revenger, hyaku run 15, attempt 1)

Frozen before any wave seat ran. Base = lane branch tip at freeze
(`freeze-base.txt`: `9876cb38c5415fbc86336a26a68e05680c397fd5`, the round-93 adjudication
tip). Nothing in this file changes after the freeze; a miss is an honest stop, never a
narrowed target. The frozen r93 instruments (`reports/round-93/*`) are not modified this
round (kumitate r42 rule).

Fresh-start carry-in (run-15 Amendment 27 moved this lane's block marker; the lane resumes
at r94). The lane's recent closure history was read before this freeze: r92 landed and was
admitted by the non-author spot-check (`corpus/lessons/round-92-verifier-spotcheck.md`;
its defects 1–5 were worked in r93, defect 6 = L0 r91 stays routed around); r93 landed and
was admitted 6/6 by `corpus/lessons/round-93-verifier-spotcheck.md`, whose routed items —
the C1 v3 successor counters with the critic's closes as frozen predicates, and the
considerthese proposal-2 re-measurement — are worked THIS round. r89's honest stop and the
r90/r91 contested verdicts stay on the record. Every predicate below was checked to fail on
the do-nothing base before the freeze (`controls/c1v3-do-nothing.log`), the red-before was
executed and committed at freeze (`controls/battery3-red-v2.log`), and the full battery was
green at freeze over synthetic fixtures (`controls/battery3-full-at-freeze.log`).

## C1 — coverage K (the lowest non-retired axis, 10/15 = 6.7): C15 uncovered → held through the v3 gate

**Claim type:** axis move. **Target axis:** coverage. **Axis rule:** this is the round's
lowest-axis claim (`SCORECARD.md` r93 section: `K_HELD_BACKED` 10/15 = 6.7, the lowest
non-retired owned axis score; the stagnation nudge does not apply below the 7.0 saturation
line). **Exploratory:** no.

**What moves.** Coverage-map row C15 (selected reverse-engineering tool repositories and
declared boundaries) moves `uncovered` → `held`, backed by the r72 candidate entry
`corpus/knowledge/round-72-tool-landscape.md`, re-grounded this round: two drift-check
source rows (S498 = REA root README re-open, S499 = REA installation docs re-open, both
accessed 2026-11-05 with `audit_source_quotes.py`-schema receipts), one new §Q-map row
(Q17), and three lane-internal gate votes (reviewer ×2, critic ×1) bound to the final
normalised entry digest under the v3 rules. The entry stays scoped to named project
sources — no tool execution, host readiness, accuracy or market-coverage claim (Q10); the
r73 erratum section stays byte-identical.

**Before → after.** before: `K_HELD_BACKED=10/15` (C15 `uncovered`); after:
`K_HELD_BACKED=11/15`. Score: 6.7 → 7.3.

**Counter (frozen):** `PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py
--rev <landing>` (base for the ONLY-C15 leg is pinned at FREEZE_REV inside the counter).
Legs: `C1_ROWS_TOTAL` (15×5 cells), `C1_C15_HELD`, `C1_C15_CITES`, `C1_ONLY_C15` (every
other coverage row byte-identical to the frozen base archive — a second row moved fails),
`C1_ADMITTED` (exactly ONE `admission-status:` line in the whole file, inside the 15-line
header window, value `admitted` — the CriticR93 finding-1 close), `C1_TRIO`,
`C1_VOTES` (≥2 votes; seats against the PINNED wave registry map frozen in the counter —
the finding-2 close; canonical seat uniqueness — finding 3; vote role == pinned role and
reviewer|critic — finding 3; digest equality; Q01–Q17 decisions with ≥1 PASS and `n/a`
reasons ≥20 chars — finding 9; one distinct non-empty artifact per vote inside
`.ufo/waves/round-94/` after resolution, containing the candidate digest — findings 4/5;
ANY malformed vote fails the leg outright), `C1_REGISTRY` (the wave registry file equals
the pinned seat→role map), `C1_LINT` and `C1_EMBEDDED` (the REAL `corpus/lint_entry.py`
and `corpus/check_embedded_outputs.py`, no stubs — the finding-11 close; a docs-only entry
with no `$` blocks passes the embedded leg only via the checker's exit 2 no-blocks reason
AND the counter's own no-`$`-block verification), `C1_EMBED_NONVACUOUS` (a ``` block whose
first line is `$ …` needs ≥1 non-blank output line; a `~~~` fence containing a `$ ` line is
rejected — the finding-7 close), `C1_SOURCES` (whole-entry S-id collection — the finding-6
close; every sid resolves; every sid outside the frozen REJECTED_OK set
{S071,S072,S074,S091,S093,S427} reaches a `mined` supersession terminal; the REJECTED_OK
sids stay `rejected`; the NEW rows S498/S499 are `mined`, tier A, opened 2026-11-05, with
used-by cite-back to the entry), `C1_QUOTES` (`audit_source_quotes.py verify` over the NEW
rows), `C1_K_HELD_BACKED` = 11. There is NO `C1_OPENS` leg: C15 is documentation-only and
has no saved-record oracle; the opening evidence is C1_QUOTES over the rows opened this
round (stated here because the r93 wording overreached — CriticR93 W3/W12).

**Predicate (frozen):** `C1_VERDICT=pass`, exit 0 — every leg above passes.

**Kill rule.** Any leg fails ⇒ C1 **not verified**, reported as such. No counter, claims,
control-receipt or kill-rule byte changes after the freeze; a defect found post-vote is
either a full vote re-bind to the corrected final digest (the r93 lesson M1 fix) or an
honest miss — never a rule edit.

**Do-nothing control (must fail; `controls/c1v3-do-nothing.log`):** the base tree scores
`C1_C15_HELD=fail` ⇒ `C1_VERDICT=fail`, exit 1.
**Self-test (positive + kills; `controls/selftest-c1v3.log`):**
`SELFTEST_C1V3=pass legs=14` — the honest admission-shaped fixture (REAL entry bytes,
REAL lint, REAL embedded checker, synthetic registry/votes/receipts) passes every leg, and
twelve forged deltas (dup-status, forged-registry, case-dup seat, role mismatch, empty
artifact, traversal, unresolved body sid, vacuous n/a, whitespace-only output, tilde
fence, stale new-row date, second-row move) each fail on their frozen expected leg.

**Separability.** C1's counter reads the C15 row, the entry, the votes, the receipts, the
registry and the base archive; it never runs the battery's forged trees. C2's battery
builds its own synthetic fixtures from the FREEZE_REV archive and never reads the landed
C15 flip; its verification does not need C1 landed.

## C2 — calibration: the v3 counter kills the routed forgery classes the frozen v2 counter still passes

**Claim type:** axis move. **Target axis:** calibration (evidence-ledger discipline: the
r93 successor counters remained reachable by the r93 critic's named forgeries outside the
frozen nine classes — CriticR93 findings 1–12, mined as r93 lesson M3 and routed here).

**What moves.** `reports/round-94/c1_k_admit_counter3.py` and
`reports/round-94/forge_battery3.py` land as the successor instrument and its battery. The
ten frozen classes (F10 dup-status, F11 forged-registry, F12 case-dup seat, F13 role
mismatch, F14 artifact binding, F15 traversal, F16 unresolved body sid, F17 vacuous n/a,
F18 whitespace/mixed fence, F18b tilde fence) plus F19 (stale new-row date) and the
ONLY-C15 second-row control each fail the v3 counter on its frozen expected leg; the
honest fixture passes with REAL instruments; the untouched base fails; and the FROZEN r93
battery re-run stays `BATTERY_VERDICT=pass`.

**Before → after (red-before, committed at freeze).** before:
`controls/battery3-red-v2.log` — a fresh re-run of the COMMITTED r93 critic attack scripts
against the FROZEN r93 v2 counter prints `V2_REACH_NEW=8/8 runnable + 1 receipt-backed`,
`RED_V2_VERDICT=pass`: every re-runnable named vector still passes v2 on this host today
(F13's v2 reach is the committed CriticR93 finding-3 receipt — its A28/A29 vectors were
critic-interactive and are not committed as scripts; stated exactly). after:
`V3_KILLS=12/12`, `POS_C1V3=pass`, `DO_NOTHING_C1V3=fail-as-required`,
`HOLD_R93_BATTERY=pass`, `BATTERY3_VERDICT=pass`.

**Counter (frozen):** `PYTHONUTF8=1 python3 -B reports/round-94/forge_battery3.py --stage
full` (predicate), plus `... --stage red-v2` as the committed red-before. The v2 counter
bytes (`reports/round-93/*`) are not modified.

**Predicate (frozen):** `BATTERY3_VERDICT=pass` (exit 0) from `--stage full`.

**Kill rule.** Any class surviving v3, any positive control failing, the do-nothing control
passing, or the r93 hold failing ⇒ C2 **not verified**. Surviving classes are a miss, not a
counter edit (kumitate r42 rule). New forgeries the wave's critic finds beyond the frozen
twelve are routed to r95 with receipts — they do not change this predicate.

**Separability.** The battery imports the v3 counter and builds every tree from the frozen
FREEZE_REV archive plus synthetic fixtures in scratch; it never reads the wave's landed
votes or the C15 flip. C1's verification never runs the battery.

## Frontier step (§2b; not a claim)

- `corpus/SOURCES.md`: S498 and S499 appended this round (both opened 2026-11-05, receipts
  under `reports/round-94/quote-receipts/`, located ≤25-word quotes in the round lesson's
  `## Gate`); census before → after with the driver command and its exit codes in the
  report. Census round start (pre-freeze): exit 0, 21 W01 + 15 W04, 0 E
  (`controls/census-round-start.log`).
- Sourced claim: C1 rests on S498/S499 (§2b.4).
- One mistake mined into `corpus/lessons/round-94.md` `## Mistakes` (candidates this round:
  the reaped r93 attack-script scratch dirs that broke the committed red re-run — fixed by
  pre-creating the bare dirs, disclosed in the battery source; any wave-found defect).
- Assimilation: expected `none` (155/155 staged-id collisions; L0 `revenger | round-91`
  unanswered) — verified fresh at round end with the frozen collision check.
- considerthese: proposal-2 measurement re-run over the r93→r94 window (the r93 connector
  baseline: 8/8 contested/not-verified over r89–r92), reported, not adopted.

## Round shape (fixed here, before dispatch)

ONE v1 wave, 13 seats, band 8–16 (`scripts/hyaku/ufo-wave-policy.json`: waveMinLanes 8,
waveMaxLanes 16): ScoutReopen ×1, ScoutErrata ×1 (scout), ScribeLesson ×1 (scribe),
ExecReceipts ×1, ExecBattery ×1, ExecCensus ×1, ExecFrozen ×1 (executor), ReviewerGate ×1,
ReviewerBlind ×1 (reviewer), CriticR94 ×1 (critic), MutationR94 ×1 (mutation-tester),
ConnectorOverlap ×1 (connector), SentinelScope ×1 (sentinel). Attack seats: reviewer ×2 +
critic + mutation-tester = 4/13 = 30.8 % (≥25 %). Connector: 1 (≤2). Residual call: none.
The L1 holds the canonical planner seat; no planner seat is dispatched (the validator
rejects it). Routing is `task.agentModelOverrides` (operator-owned); no model is passed.
The L1 alone writes SOURCES.md, README.md, SKILL.md, SCORECARD.md, LOG.md, the round
lesson, and `reports/round-94/votes/*`; seats write only their own wave dirs and scratch.

## Predicates are the frozen sentences

- C1: `C1_VERDICT=pass` from `c1_k_admit_counter3.py --rev <landing>`.
- C2: `BATTERY3_VERDICT=pass` from `forge_battery3.py --stage full`.
Neither predicate, counter, control receipt, kill rule or target may change after the
freeze. A miss is recorded as a miss.
