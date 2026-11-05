# Round 92 — frozen claims (revenger, hyaku run 15, attempt 1)

Frozen before any build or scoring seat ran. Base = lane branch tip at freeze
(`reports/round-92/freeze-base.txt`). Nothing in this file changes after the freeze; a
miss is an honest stop, never a narrowed target.

Fresh-start reading (quality-pause lift, operator "Authorize all", 2026-11-05): the last three
rejected closures are r89 (honest stop, C1 MISS 2 vs 0, C2 KILLED), r90 (C1 met on a frozen
counter, contested; C2 unprovable) and r91 (`rejected-honest-stop`: C1 reached by a 21-entry
lookup table, C2 passed by two stubs). Every failure in those three was a counter a skip-work
control could reach. The controls below were therefore built and scored **before** freeze
(`controls/`), and every predicate below was checked to fail on the do-nothing base and on
junk variants, and to pass on a positive control that performs only the intended move.

## C1 — coverage K (the lowest non-retired axis, 8/15 = 5.3): one admitted C03 entry

**Claim type:** axis move. **Target axis:** coverage. **Axis rule:** this is the round's
lowest-axis claim (`SCORECARD.md` round-91 K row: K 8/15 = 5.3, lowest non-retired; the
stagnation nudge does not apply below 7.0). **Exploratory:** no.

**What moves.** Coverage-map row C03 (managed (.NET/CLI) assemblies) moves `frontier` →
`held`, backed by one new knowledge entry `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md`
over the lane's authored managed records (`corpus/live/runs/round-76/`, `corpus/live/runs/round-85/`,
fixtures `corpus/fixtures/managed-r76`, `managed-r85`). The entry is scoped to the observed
fixtures and producer surface only (no general .NET claim; Q10). Its load-bearing format facts
cite SOURCES rows **opened this round** (Q01; sourced-claim duty of §2b.4).

**Before → after.** before: `K_HELD_BACKED=8/15` (`corpus/README.md` C03 `frontier`, work cell `—`);
after: `K_HELD_BACKED=9/15` (C03 `held`, knowledge cell cites the entry). Score: 5.3 → 6.0.

**Counter (frozen):** `reports/round-92/c1_k_admit_counter.py --rev <landing>` (committed tree:
git archive of `corpus/` and `reports/round-92/`). Legs: `C1_ROWS_TOTAL`, `C1_C03_HELD`,
`C1_C03_CITES`, `C1_ADMITTED`, `C1_TRIO`, `C1_VOTES` (≥2 vote files from distinct seats with
role reviewer|critic whose `candidate_sha256` equals the entry's digest with its admission-status
line normalised, and PASS/n-a on every Q01–Q17), `C1_LINT` (`corpus/lint_entry.py` exit 0),
`C1_EMBEDDED` (`corpus/check_embedded_outputs.py` exit 0), `C1_SOURCES` (every header S-id is a
mined SOURCES row, cites the entry, opened 2026-11-05), `C1_K_HELD_BACKED` (=9).

**Predicate (frozen):** `C1_VERDICT=pass`, exit 0 — every leg above passes.

**Kill rule.** Any leg fails ⇒ C1 **not verified**, reported as such. A landed entry whose votes
are not from non-author seats, whose sha does not match the committed bytes, or whose embedded
outputs do not re-derive, is not verified regardless of the other legs.

**Do-nothing control (must fail; recorded `controls/c1-do-nothing.log`):** the base tree scores
`C1_K_HELD_BACKED=8/15`, `C1_C03_HELD=fail` ⇒ `C1_VERDICT=fail`.
**Junk control (must fail; `controls/c1-junk-stub.log`):** a stub entry with an `admission-status:
admitted` line, C03 flipped to held, no votes, and an unregistered source id ⇒ fails `C1_VOTES`,
`C1_LINT`, `C1_EMBEDDED`, `C1_SOURCES`.
**Positive reachability:** the intended move cannot be reached by a stub; it is reached only by a
real entry with votes, lint and embedded-output pass. Reachability of the full predicate is
measured by the wave's own run and reported, not assumed.

**Separability.** C1's counter does not read the C08 row; C2 passes with C03 at `frontier`.

## C2 — calibration: the coverage token agrees with the saved records (C08 frontier → uncovered)

**Claim type:** axis move. **Target axis:** calibration (self-assessment vs repo state; the
mismatch class is M36 — a coverage token says `frontier` while a saved record exists for that
row's own surface operations).

**What moves.** Coverage-map row C08 (browser/Electron runtime evidence) moves `frontier` →
`uncovered`: its saved record exists (`corpus/live/runs/round-77/`, fixture `corpus/fixtures/browser-r77`,
the CDP run, S447) and no knowledge entry is claimed for it. `uncovered` is the legend's own token
for "work evidence exists, no admitted entry" (`corpus/README.md` legend).

**Before → after.** before: `README_TOKEN_LEGEND_MISMATCH=2 rows=['C03','C08']` (the frozen
round-66 probe over the committed corpus); after: `rows=['C03']` (C03 is the round's other
claim C1's row and clears only if C1 lands). The probe checks `frontier` only, so the counter
also rejects a `held` token without a backing file (`C2_NO_UNBACKED`).

**Counter (frozen):** `reports/round-92/c2_legend_counter.py --rev <landing>` — runs the frozen
`reports/round-66/measure.py` unmodified over the committed corpus (cwd=/, TMPDIR under scratch)
and adds `C2_ROWS_TOTAL` (15 rows), `C2_C08_CLEAR`, `C2_NO_NEW` (flagged rows ⊆ {C03}),
`C2_NO_UNBACKED` (K_HELD == K_HELD_BACKED).

**Predicate (frozen):** `C2_VERDICT=pass`, exit 0.

**Kill rule.** Any leg fails ⇒ C2 not verified.

**Do-nothing control (must fail; `controls/c2-do-nothing.log`):** `rows=['C03','C08']` ⇒
`C2_C08_CLEAR=fail`, `C2_NO_NEW=fail`, verdict fail.
**Junk controls (must fail):** `controls/c2-junk-held.log` (C08 → `held` with no backing file;
`C2_NO_UNBACKED=fail`); `controls/c2-junk-deleted.log` (C08 row deleted; `C2_ROWS_TOTAL=fail`).
**Positive control (must pass; `controls/c2-positive.log`):** only the intended C08 token change ⇒
`C2_VERDICT=pass`. This proves the predicate is reachable by the real move alone.

**Separability.** C2 passes with C1 absent (C03 flagged-or-not is allowed only as `C03`), and C1
passes with C2 absent (C1 counts held rows only, C08 is `frontier` and uncounted).

## Frontier step (§2b; not a claim)

- `corpus/SOURCES.md`: new rows for the managed-format facts the C1 entry cites, each opened this
  round (2026-11-05), each with an located ≤25-word quote in the round lesson's `## Gate`; census
  before → after with the commands in the report.
- One mistake mined into `corpus/lessons/round-92.md` `## Mistakes`: the M36 recurrence (C03 and
  C08 flagged for two rounds with the probe not in any standing battery) — fix = register
  `c2_legend_counter` in the SKILL gate registry; red-before `controls/c2-do-nothing.log`. A second
  mistake: the r91 wave-4 quarantine duty was not performed (`grep -c -i quarantin
  corpus/lessons/round-91.md` → 0) — fix = this round's register verdicts (26 rows).
- Sourced claim: C1 rests on the new S-rows (§2b.4).

## Round shape (fixed here, before dispatch)

ONE v1 wave, 10 seats, band 8–16 (`scripts/hyaku/ufo-wave-policy.json`):
scout ×2 (quarantine register slice; managed-format source opening), scribe ×1 (entry draft +
SOURCES rows in the wave dir; writes a READY marker when lint and embedded checks pass),
executor ×2 (real producer re-run and record oracle; independent cross-check of the C2 legend
numbers and the candidate-entry commands), reviewer ×2 (blind derivation from fixture bytes;
Q-gate votes), critic ×1 (attacks both counters and both claims), mutation-tester ×1 (mutants of
the two counters), connector ×1 (sibling overlap; considerthese proposal 1 measurement).
Attack seats: reviewer ×2 + critic + mutation-tester = 4/10 = 40 % (≥25 %). The L1 holds the
canonical planner seat; no planner seat is dispatched (validator rejects it).
The L1 alone writes SOURCES.md, README.md, SKILL.md, SCORECARD.md, LOG.md and the round lesson.

## Predicates are the frozen sentences

- C1: `C1_VERDICT=pass` from `c1_k_admit_counter.py --rev <landing>`.
- C2: `C2_VERDICT=pass` from `c2_legend_counter.py --rev <landing>`.
Neither predicate, counter, control receipt, kill rule or target may change after the freeze.
A miss is recorded as a miss.
