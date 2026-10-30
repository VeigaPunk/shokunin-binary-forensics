# Round 73 — C10 admission attempt and quote-attribution repair

Freeze: `reports/round-73/claims.md`, counter and candidate-pin.json at commit `606548a086844bef0b724bc5a34e308a085bb0e1`. Candidate and inherited interactive evidence landed at commit `74e1c3e82cde45e1f3f03985891973357acab925`. This is one coverage claim; supporting quote repairs are not a second axis claim.

## Gate

C10 candidate: `knowledge/2026-10-29-rea-evidence-ledger-discipline.md`, normalized SHA-256 `7880b17608f60c3f7462fb3f6602cb4a20d8bcac0a86331b8454697cef76c7c4`. Four fresh-seat Q groups bind 16 criteria; all must PASS/n/a for admission under the unchanged frozen rule. Wave evidence lives in `.ufo/waves/round-73/w1/` and votes in `votes/`; outside discernment review belongs to the integrator, not these lane seats.

### Opened sources and corrections (2026-10-30)

| row | URL and location | located quote (≤25 words) | decision |
|---|---|---|---|
| S427 | https://raw.githubusercontent.com/zhuyansen/awesome-ai-reverse-engineering/63900b2c9e2ae2dac61fc0db7553d4ce88ebb932/README.md, introduction | “each one read and security-graded” | REJECT as primary tool-function evidence; supersedes S071's paraphrased registry quote. Catalog-methodology evaluation is a possible flip. |
| S428 | https://arxiv.org/abs/2403.05286v3, abstract opening | “traditional tools like Ghidra often produce results that are difficult to read and execute.” | ADMIT source row only for stated motivation; supersedes S082's misattribution. No knowledge admission follows. |
| S096 re-open | https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/application/investigation/EvidenceLedger.ts, class comment and record method | “Session-owned set of immutable evidence records.” | Supports the sourced C10 claim narrowly; record rejects conflicting content. The source does not establish host readiness. |

No existing source row's status, recheck or used-by changed during this repair. S427 and S428 are append-only corrections; original wrong quotes remain historical evidence, not current support. The 331 inherited S096–S426 additions were authored/opened in the separate interactive 2026-10-29 pass, not by this round's wave. Their original lessons and reports are retained with their limitations; candidate status is not admission. Census at round entry sees 426 rows, while branch base has 95. Distinguish both denominators.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| quote paraphrase / source misattribution | outside `round-72-verifier-spotcheck.md`: S071 and S082; S427/S428 primary re-opens above | existing Q01/Q02; round-72 word-count audit did not test attribution | New superseding rows; source-audit wave and actual fetch/substring audit rather than quote-word counting. Red-before is the two old quotes absent from their cited source; green is the corrected quotations above. |
| historical completion overstatement | round-72 report/lesson say no worker outcomes, but `.ufo/waves/round-72/w1/` contains 16 source reviews plus registry | landed-means-committed rule; outside spot-check routed it | Preserved these partial outputs at commit 74e1c3e82cde45e1f3f03985891973357acab925; they establish only partial execution, never settled wave or C15 admission. |
| inherited tool-policy discrepancy | `reports/round-73/tool-probes.md` names pacman installations; campaign prompt says all pacman transactions paused | campaign pacman guard | No install repeated this round. Retain the installer record and disclose conflict; absence of -Sy/-Syu does not establish compliance with a full transaction pause. |
| misleading trend proxies | inherited interactive LOG/lesson call registry row growth expansion and lane re-fetch discernment | LEARNING.md: expansion requires admitted uncovered ground, discernment outside review | These labels are superseded as round-73 assessments: source breadth is not admission; lane source review is not outside discernment. |

## Inherited-work resolution and errata

The 2026-10-29 outputs explicitly say interactive, non-round. They are not evidence of an earlier failed round-73 attempt. Preserved: four candidate knowledge files, two interactive lessons, S096–S426, source packs, probe/install report, quote receipts, SKILL pointer, README index. No candidate atlas/bridge is admitted and C16 is not added. The C10 candidate's grouped Q-map cells were split before freeze; no scored candidate prose is repaired after freeze.

Inherited S002 `used-by` touch, old→new: `corpus/knowledge/seed.md` →
`corpus/knowledge/seed.md, corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md`.
No other S002 field changed. The interactive C10 lesson describes this append;
this exact old→new record resolves its abbreviated wording.

Correction to round-72 lesson/report: its statement of no worker outcomes is superseded by the committed partial 16-seat source reviews. There is still no complete 64-seat results handoff for that old wave and no retrospective credit. Existing report bytes remain unchanged.

## Assimilation and frontier

Assimilation: none from shokuknow; the prior full quarantine is not silently reopened. considerthese/2026-10-28.md proposal 1 (read-only quote-substring sampling) is mined as the bounded source-audit procedure, not as proof of source truth. Other proposals remain unchanged. C15 remains uncovered; C16 remains proposed only.

## Honest stop (run-12 wrap-up, attempt 2)

- Wave `v2` (`.ufo/waves/round-73/v2-spec.json`, `v2-plan.json`, `v2-dispatch.json`; ready `v2.ready`, written 12:14, L1 `RevengerR73a2`). Validated under policy v2 (band 64–128): 64 spawn, 0 resume, 42 round-72 source audits, 14 C10 source audits, 4 Q reviewers, 3 executors, 1 connector; roles reviewer 34, critic 20, scout 5, executor 3, scribe 1, connector 1.
- Dispatcher evidence (`.ufo/state/inline-dispatcher.log`, mutable, digest only): `partial revenger 73 v2 34 64` at 12:50:34. Host job cap (100) and dispatcher ceiling kept the wave filling in tranches. Released un-settled at the operator wrap-up; no `WAVE-DONE`, no `v2-results.json`, no vote files.
- Eleven partial seat reports sit in `.ufo/waves/round-73/v2/`. They are committed as partial evidence only; none was integrated, none settles a Q decision, and none is credited toward C10.
- Attempt-1 orphan: `w1.ready` (L1 `RevengerR73`, never spawned, 0/64) was renamed to `w1.ready.attempt1-orphan`, with its `.partial` renamed alongside. The dispatcher `live()` test matches `<name>(a\d+)?`, so `RevengerR73` matched `RevengerR73a2` and the orphan would have been revived with this attempt's seats. Reported to the operator in `.ufo/l0-questions.md`.
- C1 status: unresolved. Counter at `74e1c3e`: `C10_HELD_BACKED=0/1`, `C10_Q_VOTES=0/16`. Frozen predicate and kill rule unchanged; the next round runs them unchanged.
- Mistake (new this attempt): the attempt-1 ready file was left live under a name the dispatcher treats as the current L1. Class `landing`; captured-by `none`; fix: rename the orphan (done) and operator-side fix in `live()` (L0 filed).
