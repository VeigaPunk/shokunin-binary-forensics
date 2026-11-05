# Round 95 — frozen claims (revenger, hyaku run 15, attempt 1)

Frozen before any wave seat ran. Base = lane branch tip at freeze
(`cb5c26f73c99af268bc71e9f7417bfd7e7738d83`, the round-94 adjudication tip). Nothing in
this file changes after the freeze; a miss is an honest stop, never a narrowed target.
The frozen r93/r94 instruments (`reports/round-93/*`, `reports/round-94/*`) are not
modified this round (kumitate r42 rule).

Carry-in. The round-94 non-author spot-check
(`corpus/lessons/round-94-verifier-spotcheck.md`) admitted both r94 claims and routed six
defects; THIS round's declared work consumes them: the C1 v4 successor counter freezes the
routed closes as legs (spotcheck §6 items 1–5 / SCORECARD r94 "Routed to r95"), the claim
sentences say "named vectors" not "classes" (defect 5), the Gate carries at least one
reject or its sweep (defect C-a), the S499 word count gets an appended correction (C-b),
the report's Stale-lane line carries a progressing/silent grade (C-c), and the r94
freshness row is re-graded (C-d). Defect 6 (votes are lane-dispatched) is honored as a
disclosed residual: votes stay lane-internal this round, the claim verdicts land
"met on the frozen counter, pending the non-author closure", and the per-seat artifact
binding (M4c below) narrows the single-writer gap; the non-author closure remains the
outside check. Every predicate below was checked to fail on the do-nothing base before
the freeze (`controls/c1v4-do-nothing.log`, rc 1), the red-before was executed and
committed at freeze (`controls/battery4-red-v3.log`), and the full battery was green at
freeze (`controls/battery4-full-at-freeze.log`).

## C1 — coverage K (the lowest non-retired axis, 11/15 = 7.3): C10 partial → held through the v4 gate

**Claim type:** axis move. **Target axis:** coverage. **Axis rule:** this is the round's
lowest-axis claim (`SCORECARD.md` r94 section: `K_HELD_BACKED` 11/15 = 7.3, the lowest
non-retired owned axis score; the stagnation nudge does not apply below the 7.0
saturation line — K is the only owned criterion below it). **Exploratory:** no.

**What moves.** Coverage-map row C10 (evidence-ledger discipline — Evidence IDs;
observation/inference/unknown) moves `partial` → `held`, backed by the NEW superseding
candidate `corpus/knowledge/round-95-evidence-ledger-discipline.md` (derived byte-wise
from the r74-rejected `2026-10-29-rea-evidence-ledger-discipline.md`, whose bytes stay
untouched; the superseding entry carries a §Supersession section, the two 2026-11-05
drift-check re-opens S500/S501 folded into the rows they re-verify, and a §Q-map with a
decision for every QUALITY.md criterion). Two source rows are opened THIS round and
appended at landing: S500 (REA evidence.ts at pinned REA revision, drift check of S098)
and S501 (REA EvidenceLedger.ts at the same revision, drift check of S096), both `mined`,
tier A, `opened 2026-11-05`, `used-by` the entry, with receipts committed at FREEZE —
S500 body 17010 bytes sha256 `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f`,
S501 body 18784 bytes sha256 `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac`
(`reports/round-95/quote-receipts/`, fetch log `fetch-log.md`). Three lane-internal gate
votes (reviewer ×2, critic ×1) bind the final normalized entry digest under the v4 rules.
The entry stays documentation-only: no REA run is claimed (Q04/Q10 rows).

**Before → after.** before: `K_HELD_BACKED=11/15` (C10 `partial`); after:
`K_HELD_BACKED=12/15`. Score: 7.3 → 8.0.

**Counter (frozen):** `PYTHONUTF8=1 python3 -B reports/round-95/c1_k_admit_counter4.py
--rev <landing>` (the ONLY-C10 base rows are pinned at FREEZE_REV inside the counter).
Legs: `C1_ROWS_TOTAL` (15×5 cells), `C1_C10_HELD`, `C1_C10_CITES` — the C10 backing-cell
knowledge-file set must EQUAL exactly `[knowledge/round-95-evidence-ledger-discipline.md]`
and resolve under `corpus/` (the CriticR94 H3 close; V07 legacy-path and V08
entry-pending both fail here), `C1_ONLY_C10` (every other coverage row byte-identical to
the frozen base archive; a second row moved fails), `C1_ADMITTED` — exactly one
`\s*admission-status\s*:` match CASE-INSENSITIVELY over the whole file, inside the 30-line
header window, value `admitted` (the CriticR94 H1 close; the indented-dup-status vector
now fails, and the digest normalizer uses the same wide anchor), `C1_TRIO`,
`C1_REGISTRY` — its OWN leg, strict-JSON registry equals the pinned seat→role map (the
r94 lesson M6 close; the drop-the-gate mutant now dies, and duplicate JSON keys fail),
`C1_VOTES` (≥2 votes; seats against the PINNED wave registry map frozen in the counter —
membership; canonical seat uniqueness; vote role == pinned role and reviewer|critic;
strict JSON with duplicate keys rejected (CriticR94 M2); digest equality; Q01–Q17
decisions with ≥1 PASS; every `n/a` reason carries ≥6 tokens AND a `Q\d{2}`
cross-reference (CriticR94 M5); one distinct non-empty artifact per vote INSIDE the
seat's own wave dir whose bytes name BOTH the seat and the candidate digest (CriticR94
M4); ANY malformed vote fails the leg outright), `C1_RECEIPTS` — for every new-row sid:
`fetched_at == 2026-11-05`, `http_status == 200`, `fetch_url` host in
{raw.githubusercontent.com, github.com}, committed raw body re-hashes to `fetch_sha256`,
and a committed fetch-log line names the sid and the sha (the CriticR94 H2 close),
`C1_PYCACHE` — no `__pycache__` under corpus/, reports/round-95/ or
.ufo/waves/round-95/ (the r94 lesson M5 close; the wave spec template mandates `-B` for
every seat Python call), `C1_LINT` and `C1_EMBEDDED` (the REAL `corpus/lint_entry.py`
and `corpus/check_embedded_outputs.py`), `C1_EMBED_NONVACUOUS` (every `$ `-prompted line
in any fence needs a non-blank output line; `~~~` fences with `$ ` lines are rejected),
`C1_SIDS` — every `\bS\s?\d{2,}[a-z]?\b` token in the entry normalizes to a registry id
(the CriticR94 M6 close; V19 suffix/spaced forms fail), `C1_SOURCES` (strict registry
read — duplicate rows fail in-counter; every entry sid reaches a `mined` supersession
terminal or sits in the empty REJECTED_OK set; S500/S501 are `mined`, tier A, opened
2026-11-05, with used-by cite-back), `C1_QUOTES` (`audit_source_quotes.py verify` over
the new rows), `C1_K_HELD_BACKED` = 12. There is NO `C1_OPENS` leg: C10 is
documentation-only and has no saved-record oracle; the opening evidence is C1_QUOTES +
C1_RECEIPTS over the rows opened this round. Disclosed limit (carried from r94): the
receipt legs check the committed bytes' honesty fields; a non-author re-fetch and the
non-author closure remain the only real proof of opening.

**Predicate (frozen):** `C1_VERDICT=pass`, exit 0 — every leg above passes.

**Kill rule.** Any leg fails ⇒ C1 **not verified**, reported as such. No counter, claims,
control-receipt or kill-rule byte changes after the freeze; a defect found post-vote is
either a full vote re-bind to the corrected final digest (the r93 lesson M1 procedure) or
an honest miss — never a rule edit.

**Do-nothing control (must fail; `controls/c1v4-do-nothing.log`):** the base revision
scores `C1_C10_HELD=fail` ⇒ `C1_VERDICT=fail`, exit 1. **Self-test (positive + kills;
`controls/selftest-c1v4.log`):** `SELFTEST_C1V4=pass legs=24` — the honest
admission-shaped fixture (REAL entry bytes, REAL lint, REAL embedded checker, synthetic
registry/votes/receipts/fetch-log) passes every leg, and twenty-two forged deltas each
fail on their frozen expected leg: H1-indent-dup-status→C1_ADMITTED,
F10-dup-status-fenced→C1_ADMITTED, V10-stale-fetched-at→C1_RECEIPTS,
V27-fabricated-body-foreign-host→C1_RECEIPTS, V07-legacy-path→C1_C10_CITES,
V08-entry-pending→C1_C10_CITES, V03-dup-json-keys-registry→C1_REGISTRY,
V04-dup-json-keys-vote→C1_VOTES, V19-sid-suffix-spaced→C1_SIDS,
F16-unresolved-body-sid→C1_SIDS, V18-na-letter-flood→C1_VOTES, F17-vacuous-na→C1_VOTES,
M6-forged-registry-seat→C1_REGISTRY, M5-pycache-planted→C1_PYCACHE,
F20-foreign-artifact-dir→C1_VOTES, F12-case-dup-seat→C1_VOTES,
F13-role-mismatch→C1_VOTES, F15-traversal→C1_VOTES, F18-ws-output→C1_EMBED_NONVACUOUS,
F18b-tilde-fence→C1_EMBED_NONVACUOUS, F19-stale-new-row→C1_SOURCES,
ONLY-C10-second-row→C1_ONLY_C10.

**Separability.** C1's counter reads the C10 row, the entry, the votes, the receipts, the
registry and the base archive; it never runs the battery's forged trees or mutant code.
C2's battery builds its own synthetic fixtures from the frozen v3/v4 fixture generators
plus scratch copies for mutants; its verification does not need C1 landed.

## C2 — calibration: the v4 counter kills the r94-routed NAMED VECTORS the frozen v3 counter still passes

**Claim type:** axis move. **Target axis:** calibration (evidence-ledger discipline: the
frozen v3 counter still passes eleven r94-routed named vectors — CriticR94 findings
H1/H2/H3, M2/M4/M5/M6 and r94 lessons M4/M5/M6 — mined and routed in
`corpus/lessons/round-94.md` and `.ufo/waves/round-94/w1/CriticR94/findings.md`).

**What moves.** `reports/round-95/c1_k_admit_counter4.py` and
`reports/round-95/forge_battery4.py` land as the successor instrument and its battery.
The ELEVEN named vectors, each with its r94 receipt class: H1-indent-dup-status (V14),
V10-stale-fetched-at, V27-fabricated-body-foreign-host, V07-legacy-path, V08-entry-pending,
V03-dup-json-keys-registry, V04-dup-json-keys-vote, V19-sid-suffix-spaced,
V18-na-letter-flood, M6-registry-mutant (a CODE mutant: the registry gate dropped), and
M5-pycache-planted (SentinelScope F1). Red: every TREE vector passes the FROZEN v3
counter on an honest v3-shaped fixture (with the r93-M1 vote re-bind where a body edit
moves the v3 digest), and the M6 code mutant SURVIVES the frozen v3 self-test — the
committed MutationR94 C1_REGISTRY SURVIVED finding, reproduced. After: the v4 counter
kills every TREE vector on its frozen leg and the same code mutant DIES on v4.

**Before → after (red-before, committed at freeze).** before:
`controls/battery4-red-v3.log` — `V3_REACH_NEW=10/10`,
`MUTANT_V3_REGISTRY_SURVIVES=pass`, `RED_V3_VERDICT=pass`. after:
`controls/battery4-full-at-freeze.log` — `SELFTEST_C1V4=pass`, `V4_KILLS=10/10`
(the TREE vectors), `MUTANT_V4_REGISTRY_KILLED=pass`, `POS_C1V4=pass`,
`DO_NOTHING_C1V4=fail-as-required`, `HOLD_R94_BATTERY=pass`, `BATTERY4_VERDICT=pass`.

**Counter (frozen):** `PYTHONUTF8=1 python3 -B reports/round-95/forge_battery4.py
--stage full` (predicate), plus `... --stage red-v3` as the committed red-before. The v2
and v3 counter/battery bytes (`reports/round-93/*`, `reports/round-94/*`) are not
modified; mutants run on scratch copies only. Disclosed provisioning: the frozen
battery3's `--stage full` mkdtemps under its own SCRATCH constant without creating it, so
the battery4 HOLD leg pre-creates `/fast/scratch/hyaku/revenger-r94/battery3` before the
re-run (the r94 lesson M1 pattern: provision the environment, never edit frozen bytes).

**Predicate (frozen):** `BATTERY4_VERDICT=pass` (exit 0) from `--stage full`.

**Kill rule.** Any named vector surviving v4, the M6 mutant surviving v4's self-test, any
positive control failing, the do-nothing control passing, or the r94 hold failing ⇒ C2
**not verified**. Survivors are a miss, not a counter edit (kumitate r42 rule). New
forgeries the wave's critic finds beyond the frozen eleven are routed to r96 with
receipts — they do not change this predicate.

**Separability.** The battery imports the frozen v3 fixture generator and the v4 counter,
builds every tree from the FREEZE_REV archive plus synthetic fixtures in scratch, and
never reads the wave's landed votes or the C10 flip. C1's verification never runs the
battery.

## Frontier step (§2b; not a claim)

- `corpus/SOURCES.md`: S500 and S501 appended at landing (both opened 2026-11-05, receipts
  frozen pre-data under `reports/round-95/quote-receipts/`, located ≤25-word quotes in the
  round lesson's `## Gate`); census before → after with the driver command and its exit
  codes in the report. Census round start (pre-freeze): exit 0, rows 499
  (`controls/census-round-start.log`).
- Sourced claim: C1 rests on S500 and S501 (§2b.4).
- One mistake mined into `corpus/lessons/round-95.md` `## Mistakes` (class · evidence ·
  captured-by · fix); candidates this round: the reaped-scratch provisioning defect found
  in the frozen battery3 HOLD (M1 class recurrence, closed by provisioning), any
  wave-found defect.
- Gate reject record (r94 spotcheck C-a): the round-95 `## Gate` carries at least one
  reject with reasons (candidates this round: a C05 Android K-move — six rejected
  candidates on record and no new sourced byte-evidence this round; re-admitting the
  r74-rejected candidate in place — barred by the corrections rule).
- Assimilation: expected `none` (155/155 staged-id collisions; L0 `revenger | round-91`
  unanswered) — verified fresh at round end with the frozen collision check.
- considerthese: proposal 1 of `considerthese/2026-11-05.md` (pre-landing
  counter-reachability review per new claims.md) is ADOPTED as this round's practice: the
  controls/ directory above is its receipt set, and the round lesson records the adoption
  with the file + date citation.

## Round shape (fixed here, before dispatch)

ONE v1 wave, 13 seats, band 8–16 (`scripts/hyaku/ufo-wave-policy.json`: waveMinLanes 8,
waveMaxLanes 16): ScoutReopen ×1, ScoutCiteback ×1 (scout), ScribeLesson ×1 (scribe),
ExecReceipts ×1, ExecBattery ×1, ExecCensus ×1, ExecFrozen ×1 (executor), ReviewerGate ×1,
ReviewerBlind ×1 (reviewer), CriticR95 ×1 (critic), MutationR95 ×1 (mutation-tester),
ConnectorOverlap ×1 (connector), SentinelScope ×1 (sentinel). Attack seats: reviewer ×2 +
critic + mutation-tester = 4/13 = 30.8 % (≥25 %). Connector: 1 (≤2). Residual call: none.
The L1 holds the canonical planner seat; no planner seat is dispatched (the validator
rejects it). Routing is `task.agentModelOverrides` (operator-owned); no model is passed.
The L1 alone writes SOURCES.md, README.md, SKILL.md, SCORECARD.md, LOG.md, the round
lesson, and `reports/round-95/votes/*`; seats write only their own wave dirs and scratch.
Spec-template rule (r94 lesson M5): every seat Python invocation uses `python3 -B`; no
seat writes into any lane file directory.

## Predicates are the frozen sentences

- C1: `C1_VERDICT=pass` from `c1_k_admit_counter4.py --rev <landing>`.
- C2: `BATTERY4_VERDICT=pass` from `forge_battery4.py --stage full`.
Neither predicate, counter, control receipt, kill rule or target may change after the
freeze. A miss is recorded as a miss.
