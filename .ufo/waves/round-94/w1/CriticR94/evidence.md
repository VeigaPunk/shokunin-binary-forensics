# CriticR94 — Q01–Q17 adjudication of the round-94 candidate

Candidate: `corpus/knowledge/round-72-tool-landscape.md` at lane tip `060a8e8`, admission-status
normalised.

candidate digest (counter, `--rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431`):
`01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`

Checked by me at the tip: the counter (`--rev`), the real `corpus/lint_entry.py` (LINT_QMAP/Q14/Q15/HEADER
all 0), the real `corpus/check_embedded_outputs.py` (entry has no `$` block; exit 2 no-blocks, accepted by
the counter's own no-command check), the SOURCES tiers of the cited tool-role rows (S054, S055–S070, S073,
S075, S077, S095 all tier A), and the rejected rows S071, S072, S074, S091, S093, S427 (each carries a quoted
reject reason and a flip). Not checked by me: the S498/S499 rows and `reports/round-94/quote-receipts/` do
not exist at `060a8e8` (grep count 0; the directory is absent). Q01/Q02/Q09 PASS below are therefore
conditional on the L1 landing those rows and receipts; the counter's C1_SOURCES and C1_QUOTES are the
arbiters for their presence and I did not vote on their bytes.

I did not fetch the sources: no network use beyond the named URLs was needed for the vote, and the cited
row texts are the lane's own registry.

| Q | decision | adjudication |
|---|---|---|
| Q01 | PASS | Load-bearing tool-role statements rest on tier-A primary project rows (S054–S070, S073, S075, S077, S095), opened in r72 (the writing round). Tier-C catalog rows S071/S072/S087/S088 are discovery-only and are not cited as support. Conditional on the landing of S498/S499 for the admission re-grounding (see above). |
| Q02 | PASS | Header carries `source:` (S-ids, URLs, anchors), `verified-at:`, `recheck:`, `coverage-map: C15`. The `source:` S498/S499 lines point at rows and receipts that the landing must add; conditional as above. |
| Q03 | n/a | The entry derives no expected byte or semantic value. Its tables state project-declared roles, not measured values. |
| Q04 | PASS | The entry credits no tool with an output it did not produce; every statement is the project's own documented scope, and the entry says no tool was installed or run. |
| Q05 | n/a | The entry makes no readiness or capability claim; the Q-map and the boundary sentences say so explicitly. |
| Q06 | n/a | The entry describes no fixture and no producer call; it has no offset, operand or size. |
| Q07 | n/a | The entry makes no parser prediction; the only predictions are the bounded "not reproduced" statements. |
| Q08 | n/a | The entry carries no count, offset or identifier that needs re-derivation; S-IDs are registry names, not derived values. |
| Q09 | PASS | The entry claims no digest, origin, completeness or authenticity. The receipts it names are for fetched bytes only (the fetch-receipt sentence in the S498/S499 header lines is scoped to the bytes). Conditional on the landed receipts. |
| Q10 | PASS | Scope is named per project and repeated in each row (`not a census`, `not tool execution`, `not host readiness`, `not accuracy`); the cross-lane game and bounty material is explicitly not absorbed. |
| Q11 | n/a | Supersedes Q08 (historical). The entry derives no counts, offsets or digests; S-IDs are names. The Q-map's PASS on Q11 is not disputed, only its applicability. |
| Q12 | PASS | Rejected rows S071, S072, S074, S091, S093 and S427 each carry a quoted reject reason in SOURCES and a flip that names a successor or a scope the reject does not exclude. Verified in the row text. |
| Q13 | n/a | No verifier or recheck command is credited. S077 is cited as a first-party report that the lane did not rerun; the entry says so. |
| Q14 | n/a | The entry contains no hex run and no byte count; the lint Q14 check reports 0. |
| Q15 | PASS | The entry asserts no git object or tree identity; revision locators stay in SOURCES. The lint Q15 check reports 0. |
| Q16 | PASS | Each tool statement stays inside the cited project's documented output or scope; the table's boundary column restates limits rather than extending them. |
| Q17 | n/a | The entry relocates no cited artifact and carries no path rename; the erratum section names S082/S083/S427/S428 without moving them. |

Counts: PASS on Q01, Q02, Q04, Q09, Q10, Q12, Q15, Q16 (8); n/a on Q03, Q05, Q06, Q07, Q08, Q11, Q13, Q14,
Q17 (9). The entry's own Q-map differs from this on Q11 only (it says PASS; I say n/a, because no derived value
exists to check). That divergence is not a defect of the entry.

## Relation to the instrument (not part of the Q vote)

The Q-map cells in the entry are not cross-checked against any vote by the counter (findings M8: an entry
that says `Q02 | FAIL` while every vote says PASS passes C1). This vote reports the candidate's Q-map as
written except Q11. The vote itself is the adjudication above; it does not depend on the counter's
Q-map handling.

## Scope of this adjudication

- Candidate bytes only; the counter result (`--rev`) is the verdict of record, and it reports
  `C1_K_HELD_BACKED=10/15` at the tip (the C15 flip has not landed). My vote is on the candidate digest.
- The C1 predicate is not decided by this vote. Findings H1-H3 are about the counter and the claim
  wording, not the candidate's content; they are in `findings.md`.
