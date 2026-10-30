# Round 74 — frozen claims (revenger, hyaku run 13)

Freeze commit: this commit (claims.md + `measure.py` + `corpus/audit_source_quotes.py` +
`measure-before.log`, all landed together before any seat fetched or scored). Lane base:
`c70085776ee3c51fc76ac82a7b590d7971df112a` (round-73 closure tip). SHA-256 pins at freeze:
`corpus/audit_source_quotes.py` sha256 `72c6938a7e27631f0e0c3ba280f8debe58377371e3b3e73b043e4f0dcc58743f`,
`reports/round-74/measure.py` sha256 `ff2e52bdd6705bfb3d1a2140451a8ab16416cbb57c9cebeeabb78d75296e4ea6`
(a reader re-derives them with `sha256sum`).

Two claims, causally separable, distinct axes. No third claim. The lane's lowest-scoring
non-retired axis is coverage (K 8/15 = 5.3); claim C1 works it.

## C1 (coverage) — execute the frozen round-73 admission order on the C10 candidate

Carried unchanged from round 73 under the frozen rule (`corpus/lessons/round-73.md`
`## Honest stop`; `reports/round-73/claims.md`, counter, `candidate-pin.json` — all
byte-untouched). Predicate, counter, kill rule and target are round-73's exactly:

- Target: `C10_HELD_BACKED=1/1` and `C10_Q_VOTES=16/16` from the UNCHANGED counter
  `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-73/measure.py TREE`
  over an isolated `git archive` of the measured commit; `K_HELD_BACKED` 8/15 → 9/15
  (5.3 → 6.0).
- Before (base `c7008577`, re-measured this freeze): `C10_HELD_BACKED=0/1`,
  `C10_Q_VOTES=0/16`, `K_HELD_BACKED=8/15`, `HOLDS_C10=no`, counter exit 0.
- Vote files land at `.ufo/waves/round-73/votes/R73Q{01,05,09,13}.json` with exactly the
  frozen shape the counter parses: `{"seat":"R73Qnn","candidate_sha256":"7880b17608f60c3f7462fb3f6602cb4a20d8bcac0a86331b8454697cef76c7c4","decisions":{"Qxx":"PASS|FAIL|n/a"}}`
  (groups Q01–Q04, Q05–Q08, Q09–Q12, Q13–Q16; normalized digest as defined by the frozen
  counter's `digest()`; only PASS/n/a count toward 16/16).
- Kill rule (unchanged): any required FAIL, or an unavailable required review, falsifies
  C1 — the candidate keeps every byte except `admission-status:`, which becomes
  `rejected`; README C10 stays `partial`; no repair-and-revote this round.
- Admission order (unchanged, SKILL §6.3): seats vote with no status flip on disk →
  adjudicate → only on all-PASS/n-a flip `admission-status:` to `admitted` and README C10
  to `held` naming only this candidate → measure on the committed tip.
- Do-nothing control: base scores 0/1 (log below). A status-flip-only tree scores 0/1
  (round-73 `measure-before.log`).

## C2 (calibration) — new bounded criterion QA: source-registry quote fidelity over S054–S095 plus the nine MANUAL rows

Surface named by the counting command, not a number: the registry block S054–S095
(round-72 tool-landscape rows, 42 ids; superseded rows resolve through the registry's own
`supersedes` chains — currently S071→S427, S082→S428, `chains` prints `TERMINALS=42/42`)
plus the nine rows `reports/round-73/verify_quotes.log` left MANUAL (S115, S130, S131,
S343, S379, S380, S381, S398, S400).

- Predicate (one sentence, same in this file, in the counter's code, and on every
  receipt): a required row is RESOLVED iff a committed receipt at
  `.ufo/waves/round-74/quote-audit/<terminal>.receipt.json` (schema
  `revenger-quote-audit-v1`) shows verdict `verified` — the row's located quote appears
  verbatim after whitespace collapse at its recorded span inside
  `.ufo/waves/round-74/quote-audit/raw/<terminal>.body`, whose sha256 and length the
  receipt pins — or verdict `unreachable` with ≥2 recorded fetch attempts at distinct
  URLs carrying status/error evidence. Anything else is UNRESOLVED.
- Target: `QA_TARGET=yes`, i.e. `QA_UNRESOLVED=0/42` AND `QA_MANUAL_UNRESOLVED=0/9` AND
  `QA_VERIFIED_TOTAL>=40/51` AND `QA_NEGCTRL=pass`, from
  `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-74/measure.py TREE`.
- Before: base `c7008577` carries no receipts → `QA_RECEIPTS`-equivalent state is
  unresolved 51/51, `QA_NEGCTRL=n/a`, `QA_TARGET=no` (`measure-before.log`, committed at
  freeze).
- Negative control (instrument able to fail): when the S427 receipt verifies, the
  counter checks that the historical S071 quote ("Each repo is read and security-graded")
  is ABSENT from the S427 body — the round-73 spot-check showed that exact drift is real.
  `QA_NEGCTRL=fail` blocks the target. The verifier's `--self-test` additionally kills a
  not-in-body quote, a wrong span, a digest mismatch, and a single-attempt unreachable
  (7/7 legs, exit 0).
- Reachability control (run in scratch before freeze, never committed): a synthetic
  registry + 51 synthetic receipts drives `measure.py` to `QA_TARGET=yes` — the target is
  reachable by legitimate data, not only by fabrication.
- Kill rule: if the target is not `yes` at the final measured commit, C2 is falsified
  (honest stop): receipts and corrections land as evidence, the score records the honest
  fraction, and no acceptance condition is repaired after data.
- Score: calibration criterion QA is 0.0 before; 10.0 only at the final measured commit
  that prints `QA_TARGET=yes` (partial states report the honest fraction `resolved/51 × 10`,
  capped by the ≥40-verified leg). Corrections that the audit forces land ONLY as new
  superseding registry rows (append-only; `teaches` opens `supersedes S0NN —`), each
  opened this round and gated in `corpus/lessons/round-74.md` `## Gate`.

Receipt contract (seats write; the counter reads): fields `schema, sid, row_url,
fetch_url, final_url, http_status, fetched_at, fetch_sha256, length, anchor, quote,
span{start,end}, verdict, body_derivation, normalization, attempts[], seat, notes`. A
`body_derivation` other than `raw response bytes` (e.g. PDF text extraction) names the
exact command; the counter verifies the stored bytes only, and the seat report carries the
derivation evidence. Seats never edit registry rows.

## Holds (both claims)

Do not alter `corpus/live`, `corpus/fixtures`, admitted entries, Q01–Q16, or any coverage
row except C10-on-pass. `reports/round-73/*` stays byte-identical. Registry changes:
append-only rows plus `status`/`recheck`/`used-by` touches logged old→new in the round
lesson. No capability claim; no C15/C16 change; pacman pause binds; scratch only under
`/fast/scratch/hyaku/revenger-r74/`; `/tmp` files under 50 MB only.

## Wave shape (declared)

One v1 wave, 32 seats, policy `scripts/hyaku/ufo-wave-policy.json` (band 32–48): 4
criterion-group vote reviewers, 21 two-row source audits (11 reviewer, 10 critic), 2
manual-row scouts, 1 labrat connectivity probe, 1 connector, 1 critic (claims/instruments),
1 reviewer (instruments), 1 mutation-tester (instruments). Attack seats
reviewer/critic/mutation-tester/labrat = 29/32. L1 holds the §3 planner seat. Dispatch via
the inline spawn handoff (`.ufo/waves/round-74/w1.ready`); WAVE-DONE required before the
report.

## Controls summary

| control | expected at freeze |
|---|---|
| do-nothing base `c7008577`, C1 counter | `C10_HELD_BACKED=0/1`, `C10_Q_VOTES=0/16`, exit 0 |
| status-flip-only tree, C1 | 0/1 (round-73 committed log, unchanged) |
| do-nothing base, C2 counter | `QA_TARGET=no`, unresolved 51/51, `QA_NEGCTRL=n/a` |
| verifier self-test | `self-test: ok (7/7 legs)`, exit 0 |
| scratch reachability fixture | `QA_TARGET=yes` |
