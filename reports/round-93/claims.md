# Round 93 — frozen claims (revenger, hyaku run 15, attempt 1)

Frozen before any build or scoring seat ran. Base = lane branch tip at freeze
(`reports/round-93/freeze-base.txt`: `281a5bad66e844190a570cb35d257c6974749993`).
Nothing in this file changes after the freeze; a miss is an honest stop, never a
narrowed target.

Fresh-start carry-in (run-15 Amendment 27 authorized this lane's fresh start;
r89–r91 were the rejected trio and are read; r92 landed and was admitted by the
non-author spot-check `corpus/lessons/round-92-verifier-spotcheck.md`). The r92
spot-check routed six defects to this round; routed items 1–5 are worked here
(relabel, entry erratum, note-level tightening, S136 supersedes row, successor
counters), item 6 (L0 r91) stays routed around. Every predicate below was
checked to fail on the do-nothing base before the freeze
(`controls/*-do-nothing.log`), and the battery's v1-only stage
(`controls/battery-v1-only.log`) proves the red-before: five routed forgery
classes reach the frozen v1 counter.

## C1 — coverage K (the lowest non-retired axis, 9/15 = 6.0): one admitted C08 entry

**Claim type:** axis move. **Target axis:** coverage. **Axis rule:** this is the
round's lowest-axis claim (`SCORECARD.md` r92 section: K 9/15 = 6.0, lowest
non-retired axis score; the stagnation nudge does not apply below the 7.0
saturation line). **Exploratory:** no.

**What moves.** Coverage-map row C08 (browser/Electron runtime evidence) moves
`uncovered` → `held`, backed by one new knowledge entry
`corpus/knowledge/round-93-browser-cdp-runtime-evidence.md` derived from the
lane's saved round-77 CDP record (`corpus/live/runs/round-77/` — inspection
stdout sha256 `b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868`,
receipt exit 0, fixture `corpus/fixtures/browser-r77/`, oracle 17/17). The entry
is scoped to the authored fixture and the saved record only (no general browser,
Chrome, CDP or Electron claim; Q10). Its load-bearing facts cite SOURCES rows
opened this round (Q01; sourced-claim duty of §2b.4): S495 (the round-77 record,
own-work tier A, opened 2026-11-05 by re-running the oracle — round-start opening
output committed as `controls/oracle-opening.log`) and any external row the entry
cites, fetched this round with `audit_source_quotes.py`-format receipts.

**Before → after.** before: `K_HELD_BACKED=9/15` (C08 `uncovered`, knowledge cell
`—`); after: `K_HELD_BACKED=10/15` (C08 `held`, knowledge cell cites the entry).
Score: 6.0 → 6.7.

**Counter (frozen):** `reports/round-93/c1_k_admit_counter2.py --rev <landing>`.
Legs: `C1_ROWS_TOTAL` (15×5 cells), `C1_C08_HELD`, `C1_C08_CITES` (exact entry
path), `C1_ADMITTED`, `C1_TRIO`, `C1_VOTES` (≥2 distinct registry seats, roles
reviewer|critic, digest-bound, Q01–Q17 each PASS or reasoned `n/a`, ≥1 PASS,
`artifact_path`+`artifact_sha256` bound to committed wave bytes — the r92
critic's closes: registry membership, no all-`n/a`, artifact sha binding),
`C1_LINT`, `C1_EMBEDDED`, `C1_EMBED_NONVACUOUS` (a `$ command` fence embeds
≥1 output line — critic finding 6 close), `C1_SOURCES` (mined, opened
2026-11-05, used-by the entry), `C1_QUOTES` (`audit_source_quotes.py verify`
over every external header row — critic finding 7 close), `C1_OPENS`
(`reports/round-93/opens.json` re-derives: the counter re-runs the round-77
oracle over the archived record, re-hashes the record and both fixture files),
`C1_K_HELD_BACKED` = 10.

**Predicate (frozen):** `C1_VERDICT=pass`, exit 0 — every leg above passes.

**Kill rule.** Any leg fails ⇒ C1 **not verified**, reported as such. A landed
entry whose votes are not bound to committed wave artifacts, whose seats are not
in the wave registry, whose sha does not match the committed bytes, or whose
embedded outputs do not re-derive, is not verified regardless of the other legs.

**Do-nothing control (must fail; `controls/c1v2-do-nothing.log`):** the base
tree scores `C1_C08_HELD=fail` ⇒ `C1_VERDICT=fail`.
**Self-test (positive + kills; `controls/selftest-c1v2.log`):** an honest-shaped
admission fixture passes every leg, and four vote forgeries (registry-absent
seat, artifact sha mismatch, all-`n/a`, unreasoned `n/a`) each kill `C1_VOTES`.

**Separability.** C1's counter reads the C08 row, the entry, votes, opens and
sources; it does not read the battery's forged trees. C2 (below) passes with C08
still `uncovered`.

## C2 — calibration: the routed successor counters kill the routed forgery classes

**Claim type:** axis move. **Target axis:** calibration (evidence-ledger
discipline: the lane's own counting instruments could be reached by nine named
forgery classes; the routed successor counters must reject all nine while the
honest state still passes — no blanket refusal).

**What moves.** `reports/round-93/c1_k_admit_counter2.py` and
`reports/round-93/c2_legend_counter2.py` land as the successor instruments of
the two frozen r92 counters, with the r92 critic's closes frozen as their legs
(exact-token, record sha pin, archive-isolated probe execution, registry-bound
artifact-sha votes, reasoned-`n/a` rule, `audit_source_quotes.py verify`) and
`reports/round-93/forge_battery.py` freezing the nine classes as machine cases.

**Before → after.** before: the v1 counter is reachable by 5/5 C2-side forgery
classes (`controls/battery-v1-only.log`, `V1_REACH_C2=5/5`), and the committed
r92 critic receipts prove the C1-side classes reachable (`R92_RECEIPTS=4/4`).
after: `V2_KILLS=9/9` (all nine classes rejected by the v2 counters), positives
pass (`POS_C1V2=pass`, `POS_C2V2=pass`), do-nothing still fails
(`DO_NOTHING_C2=fail`), receipts resolve (`R92_RECEIPTS=4/4`).

**Counter (frozen):** `PYTHONUTF8=1 python3 -B reports/round-93/forge_battery.py
--stage full` — plus `... --stage v1-only` as the committed red-before. The nine
classes F1–F9 are the r92 critic findings 1–5 and MutationR92Counters Demo A–D
recipes: F1 full forgery, F2 all-`n/a` votes, F3 registry-absent seats, F4
artifact sha mismatch, F5 `partial` token, F6 `held`+seed token, F7 trailing
cell, F8 record deletion, F9 probe shadow via a planted `tempfile.py` beside the
mutable probe source.

**Predicate (frozen):** `BATTERY_VERDICT=pass` (exit 0) from `--stage full`.

**Kill rule.** Any class surviving a v2 counter, any positive control failing,
or the do-nothing control passing ⇒ C2 not verified. The v2 counters' frozen
bytes may not change after the freeze; a surviving class is a miss, not a
counter edit (kumitate r42 rule).

**Self-tests (gate standard; committed):** `controls/selftest-c1v2.log`,
`controls/selftest-c2v2.log` — isolated fixtures, asserted exits and finding
ids; `controls/battery-full.log` is the frozen-input run over the committed
BASE bytes with its expected verdict committed beside it.

**Separability.** The battery builds every tree from the frozen BASE archive;
C2's verification needs only the instruments and the committed receipts, never
the r93 entry or votes. C1's verification never runs the battery.

## Frontier step (§2b; not a claim)

- `corpus/SOURCES.md`: new rows for the facts the C1 entry cites, each opened
  this round (2026-11-05), each with a located ≤25-word quote in the round
  lesson's `## Gate`; census before → after with the commands in the report.
- The r92-routed S136 correction lands as a NEW row whose `teaches` opens
  `supersedes S136 —` (SOURCES rule 2), grounded in a re-open of the addendum
  this round.
- One mistake mined into `corpus/lessons/round-93.md` `## Mistakes` (the
  "lane-internal seats labelled non-author" overreach class; the S136
  frozen-cell lesson-bullet class; and any this-round class with its own
  red-before).
- Sourced claim: C1 rests on the new S-rows (§2b.4).
- Assimilation: expected `none` (mass id drift + unanswered L0 r91), verified
  fresh at round end with the frozen collision check.

## Round shape (fixed here, before dispatch)

ONE v1 wave, 13 seats, band 8–16 (`scripts/hyaku/ufo-wave-policy.json`):
scout ×2 (round-77 record opening + S495/S496 rows with audit receipts; S136
addendum re-open + supersedes row), scribe ×1 (C08 entry draft + READY digest),
executor ×3 (oracle/embedded re-derivation; frozen-battery integrity re-run;
round-end census + no-harm diff receipts), reviewer ×3 (Q-gate vote with
provenance; blind derivation vote; r92-entry errata drafting), critic ×1
(attacks both counters and both claims), mutation-tester ×1 (one-per-leg mutants
of both v2 counters), connector ×1 (sibling overlap; considerthese mining),
sentinel ×1 (write-scope/safety audit). Attack seats: reviewer ×3 + critic +
mutation-tester = 5/13 = 38.5 % (≥25 %). Connector: 1 (≤2). The L1 holds the
canonical planner seat; no planner seat is dispatched (validator rejects it).
The L1 alone writes SOURCES.md, README.md, SKILL.md, SCORECARD.md, LOG.md, the
round lesson, and reports/round-93/votes/*.

## Predicates are the frozen sentences

- C1: `C1_VERDICT=pass` from `c1_k_admit_counter2.py --rev <landing>`.
- C2: `BATTERY_VERDICT=pass` from `forge_battery.py --stage full`.
Neither predicate, counter, control receipt, kill rule or target may change
after the freeze. A miss is recorded as a miss.
