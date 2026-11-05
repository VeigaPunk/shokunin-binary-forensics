# ReviewerGate — round-95 gate evidence for the frozen C1 admission vote

Seat: ReviewerGate (reviewer). Vote target: `corpus/knowledge/round-95-evidence-ledger-discipline.md`.
Candidate normalized digest (the wave-context recipe, run by me over the lane root):

```
476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9
```

Identity and bounds I checked before deciding anything:

- Working-tree entry bytes == freeze commit `6e0bf15` bytes: `sha256sum` of the file and of
  `git show 6e0bf15…:corpus/knowledge/round-95-evidence-ledger-discipline.md` both print
  `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`. Exactly one
  `admission-status:` line exists in the entry (`admission-status: candidate`, line 21).
- Independently re-computed normalized digest with the required recipe: the same value, so my
  vote binds the frozen bytes, not a working copy.
- Non-author receipt verification (`PYTHONUTF8=1 python3 -B` over the committed bytes): for
  S500 the committed body `reports/round-95/quote-receipts/raw/S500.body` is 17010 bytes and
  re-hashes to `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f`
  (`S500.receipt.json fetch_sha256`); for S501 the body is 18784 bytes and re-hashes to
  `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac`. Slicing each committed
  body at the receipt `span` decodes byte-exactly to the receipt `quote` (11 and 7 words,
  both ≤25). `reports/round-95/quote-receipts/fetch-log.md` names both sids with both shas,
  HTTP 200, host `raw.githubusercontent.com`, fetched `2026-11-05`.
- Non-author re-fetch (my own network check, the receipts' honesty claims re-derived): GET of
  both pinned URLs
  `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidence.ts`
  and `.../src/application/investigation/EvidenceLedger.ts` returned HTTP 200 with the exact
  committed lengths and the same sha256 values — 17010/`69fe22…` and 18784/`f7add6…`.
- Gate instruments: `reports/round-95/c1_k_admit_counter4.py --self-test` run by me prints
  `SELFTEST_C1V4=pass legs=24`, rc 0; the frozen control receipts match claims.md
  (`controls/c1v4-do-nothing.log` rc 1, `controls/battery4-red-v3.log` 10/10 reach + mutant
  survives v3, `controls/battery4-full-at-freeze.log` 10/10 kills + mutant dies on v4 +
  `BATTERY4_VERDICT=pass`). I read the counter's vote rules (pinned seated map, strict JSON
  with duplicate-key rejection, digest equality, Q01–Q17 with ≥1 PASS, n/a note ≥6 tokens
  with a `Q\d{2}` cross-reference, distinct per-seat artifact inside the seat's own wave dir
  naming seat + digest) and satisfied them for this vote.
- Entry mechanics for the gate: `corpus/lint_entry.py` rc 0 (`LINT_QMAP=0 LINT_Q14=0
  LINT_Q15=0 LINT_HEADER=0`); `corpus/check_embedded_outputs.py` rc 2 `could-not-evaluate:
  no $ cmd blocks` — the counter's frozen leg treats exactly this shape as clean (no `` $ ``
  prompt line exists in any fence of the entry); `corpus/audit_source_quotes.py verify
  --sid S500 --sid S501` prints `SUMMARY rows=2 verified=2`, rc 0. The README C10 row's
  knowledge cell parses to exactly the one-file set
  `knowledge/round-95-evidence-ledger-discipline.md` and says `held`; every other coverage
  row is byte-identical to the frozen base per the counter's `C1_ONLY_C10` read; the
  wave-registry members map equals the pinned 13-seat map including `ReviewerGate:
  reviewer`.

## Q decisions (one paragraph each)

**Q01 — PASS.** Every load-bearing claim rests on a tier-A row at its stated scope, and the
rows carrying the executable REA contract were re-opened by THIS round. The Evidence-record
row cites S098/S103 (tier A, `corpus/SOURCES.md:111–118` family) plus S500 — the 2026-11-05
re-open of `evidence.ts` whose committed body I re-fetched and re-hashed: line 148 carries
the confidence enum `z.enum(["observed","derived","inferred"])` and lines 121–128 the five
value authority vocabulary, matching the receipt quote "Source authority vocabulary owned by
Evidence and reused by its consumers." The session-ledger row cites S096/S101 plus S501, whose
committed evidence.ts-sibling `EvidenceLedger.ts` body matches the receipt quote "Record
evidence idempotently; conflicting content is rejected." at line 58 and the
`EvidenceIntegrityError("Conflicting evidence record")` path at line 74. The qualification
rule (S099 lines 444–464 `validateVerifiedResolution`, 543–569 `evidenceQualifies` with rank
`{inferred:1, derived:2, observed:3}`, contradicting-ids-empty at 458) and the residual-unknown
verified branch (`residualUnknown.ts:65–70` `disposition: z.literal("verified")`,
`evidence_ids` min 1) and the ECL statuses (`evidenceCompletionLedger.ts:15–27`) match the
entry's §Qualification and layer tables line-for-line; the issue contracts I re-read on
fetched GitHub pages #50 (acceptance criteria: dedup, retention until session close,
limit-bound truncation errors rather than evicting silently; Non-goals: DB persistence,
cloud sync, filesystem import/export), #73 (Correctness: "Inference cannot satisfy observed
authority.", contradictions visible) and #21 ("Secrets and arbitrary environment values never
enter evidence.") all exist as quoted. S104/S106 are tier A and S105/S107/S109 tier B/case
adjacent-methodology rows are never sole support — the entry labels each in the
adjacency table with explicit non-REA boundaries, and line 78 says S105 is never sole
support. The claim-of-record that rows S096–S109 were opened 2026-10-29 by the superseded
candidate's round is disclosed in `verified-at`, and this round's drift re-opens of the two
schema-side sources confirm the pinned bytes are unchanged.

**Q02 — PASS.** Header trio is present in the frozen head window: fifteen `source:` lines
(each an S-ID with URL/commit pin and a file/line-level anchor, none a bare homepage — e.g.
S096 names the class header and `record`/`clear` methods commit `12f6e09…`), `verified-at:`
2026-11-05 naming the supersession and the two re-open receipts, `recheck:` naming the
`git -C ~/.local/share/rea rev-parse HEAD` plus URL re-open-and-compare-`fetch_sha256`
commands, and `coverage-map: C10` naming the row it fills. The two new S500/S501 source
lines carry their receipt paths and open dates (entry lines 16–17). Corpus lint confirms
(`LINT_HEADER=0`).

**Q03 — n/a.** Note: no byte oracle or expected fixture value exists in this
documentation-only entry; nothing is compared against a record under test, so the
independent-derivation criterion has no object here (see Q03/Q11 rows and cross-ref Q11).

**Q04 — PASS.** The entry credits no tool with any output: "No REA MCP analysis run" is
stated in `verified-at`, the Limitations say no `record`/`record_unknown`/`export_evidence_bundle`
call was made, and every schema statement is attributed to a named source file at the pinned
commit. The only code that ran for the gate (lint/embed/quote-audit) is gate-side, and I ran
those checks myself with outputs recorded above.

**Q05 — n/a.** Note: the entry makes no readiness, capability or installation claim against
any real host surface (see Q05 scope in corpus/QUALITY.md, cross-ref Q-map row Q05 and the
Scope section); pins are source-scope, not host state.

**Q06 — n/a.** Note: no authored fixture is built, edited or claimed anywhere in the entry
(see Q06 in corpus/QUALITY.md, cross-ref the Q-map Q06 row and the Scope section); there is
no producer call to premise-check.

**Q07 — n/a.** Note: no predicted parser behavior, accept/refuse hypothesis or
pre-registered sampling claim appears in the entry (see Q07 in corpus/QUALITY.md, cross-ref
Q-map Q07 row); nothing rests on an unreproduced cause.

**Q08 — n/a.** Note: Q08 is a historical criterion superseded by Q11 per corpus/QUALITY.md
(cross-ref Q11 and the entry Q-map Q08 row); nothing remains to apply beyond the Q11 check.

**Q09 — PASS.** The only digests in play are the receipts' `fetch_sha256` values binding the
exact committed quote-audit bodies (verified by re-hash and non-author refetch above), and
the Scope explicitly denies authenticity use: "does not treat a hash, receipt, or decompiler
string as authenticity or source identity (Q09 / PROVINCE)". No similar recomputation
confirms producer origin; the receipt verdicts are labeled internal-consistency evidence
only. The superseded 2026-10-29 candidate's hash claim (installed-vs-checkout byte
difference) was removed with the old header; nothing in the new entry infers origin from a
hash.

**Q10 — PASS.** Every table row carries an explicit boundary cell ("The vocabulary is REA's
schema, not a claim that a given tool output was observed here"; "not a run receipt"; "not a
REA API"; "out-of-province PSYCH tier and live probing are not adopted"), and the Unknown
section keeps the cross-lane unverified items (installed-skill byte drift, target-investigation
unknowns, adjacent sources not executed as oracles) visible rather than absorbed. No sentence
states a cross-lane or cross-scope universal.

**Q11 — PASS.** This entry re-derives nothing numerically; counts and spans live in the
receipts, and the fields the entry asserts (`evidence_id`, confidence ranks, issue numbers,
contract clause names) are quoted from the cited source files (verified line-for-line above)
rather than computed. Derived-vs-recorded is labeled: the two re-open rows are labeled
"confirms … unchanged in the current bytes" (a recording of a drift check, not a new
derivation), and no value cited to prose is presented as re-derived.

**Q12 — n/a.** Note: no rejected source registry row is load-bearing for this entry's
claims; the superseded 2026-10-29 file is a knowledge entry rejected by the round-74 kill
rule, not a SOURCES row (cross-ref Q12 in corpus/QUALITY.md and the Supersession section).

**Q13 — n/a.** Note: the entry credits no verifier or recheck command with guarding any
clause value (cross-ref Q13 in corpus/QUALITY.md and the Q-map Q13 row); its `recheck:`
names re-open commands, never a clause-level guard claim.

**Q14 — n/a.** Note: no hex string, byte-length assertion or ASCII byte rendering appears
anywhere in the committed entry text (cross-ref Q14 in corpus/QUALITY.md and Q-map Q14 row);
only the receipts carry binary-derived lengths, and those are not hex runs.

**Q15 — PASS.** The pinned external revision identity resolves under the entry's own.
`recheck:` command family, not asserted blindly: I fetched the raw.githubusercontent URLs
carrying the full commit id `12f6e0974cc0db0b3a9b86246accc76556837222` and their bodies
re-hash to the frozen receipt values, which is the byte-level derivation the entry's
verified-at/recheck headers claim (the fetch sha comparison is the deriving command; no
lane-tree object identity is asserted anywhere in the entry, so no `git rev-parse
X:corpus` obligation exists — matching the entry's Q15 row "no lane-tree git identity is
asserted").

**Q16 — PASS.** Each claim stays inside the cited sentence: I located every contract phrase
in its fetched source as of this round ("Only qualifying observed evidence can verify a
resolution." in `evidence-workflows.md` line 42; the #50 acceptance criterion "Memory and
record-count bounds return typed truncation/limit errors rather than evicting evidence
silently" and Non-goals "Database persistence, cloud synchronization, or filesystem
import/export."; #73 Correctness "Inference cannot satisfy observed authority."; the S103
quote on #21; the enum/rank/backing clauses in the three fetched `.ts` files), and nothing
in the Statistics/adjacent-methodology tables claims more stake in a source than the source
states ("survey prose is not a run receipt"; "does not admit a finding by itself"). No run
output is invented anywhere in the entry.

**Q17 — n/a.** Note: no adjudication relocates any cited artifact for this entry; the
superseded candidate stays byte-preserved at its original path `knowledge/2026-10-29-…`
status `rejected` (cross-ref Q17 in corpus/QUALITY.md and the Q-map Q17 row), requiring no
citation sweep.

## Decision summary

PASS: Q01, Q02, Q04, Q09, Q10, Q11, Q15, Q16 (8). n/a: Q03, Q05, Q06, Q07, Q08, Q12, Q13,
Q14, Q17 (9, each with a ≥6-token note carrying a Q cross-reference, filed in vote.json).
Q01's re-open receipts (`reports/round-95/quote-receipts/S500.receipt.json`,
`S501.receipt.json`, `raw/*.body`, `fetch-log.md`) support the sourced claim; my own
re-fetch is the non-author spot-check the admission continues to keep open as the outside
closure condition.
