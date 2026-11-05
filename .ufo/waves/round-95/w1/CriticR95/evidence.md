# CriticR95 — vote evidence, round-95 C10 candidate admission

Seat: **CriticR95** (critic, pinned in `.ufo/waves/round-95/w1/swarm-registry.json`)
Candidate: `corpus/knowledge/round-95-evidence-ledger-discipline.md`
Candidate digest (sha256 over entry bytes with every `admission-status` line normalized
to `admission-status: candidate`, per the frozen recipe):
**476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9**

## Byte grounding performed before deciding

- Working-tree entry sha256 equals `git show 6e0bf15fed58f357b7fa0c881371ac7616a116f7:corpus/...` sha256 (`476edc36…79fb9`): the voted bytes are the frozen bytes.
- `reports/round-95/quote-receipts/S500.receipt.json`: host `raw.githubusercontent.com`, HTTP 200, `fetched_at` 2026-11-05, body 17010 bytes, sha256 `69fe2245…b8f`, located quote + span, named in `fetch-log.md` with the same sha.
- `reports/round-95/quote-receipts/S501.receipt.json`: host `raw.githubusercontent.com`, HTTP 200, `fetched_at` 2026-11-05, body 18784 bytes, sha256 `f7add697…dac`, located quote + span, named in `fetch-log.md` with the same sha.
- `corpus/QUALITY.md` Q01–Q17 read in full; the entry's `source:`/`verified-at:`/`recheck:`/`coverage-map:` header block, `## Supersession`, `## Scope`, ledger-layer table, qualification rule, observation/inference/unknown split, `## Limitations` and `## §Q-map` read in full.
- My attack battery (findings.md): the v4 gate kills 5 of 7 new forged trees; the two survivors are routed findings about counter coverage, not defects in the candidate entry's content.

## Decisions Q01–Q17 (this seat's own pass; entry §Q-map compared afterwards — no disagreements)

| Q | decision | grounding |
|---|---|---|
| Q01 | PASS | Load-bearing schema claims (confidence enum, authority vocabulary, idempotent `record` with conflicting-content rejection) rest on tier-A rows S500/S501 opened this round (2026-11-05) at REA pin `12f6e09` with committed bodies and receipts; adjacent methodology rows are labeled non-REA and never sole support (S105 boundary stated in Limitations). |
| Q02 | PASS | `source:` rows with URL + file anchor + commit, `verified-at:` date + re-open statement, `recheck:` concrete commands (git rev-parse, re-open URLs, compare fetch_sha256), `coverage-map: C10` named. Anchors are file+symbol, not bare homepages. |
| Q03 | n/a | See vote notes. |
| Q04 | PASS | No tool run is credited; entry states "No REA MCP analysis run"; schema statements cite named source files at a pinned commit. |
| Q05 | n/a | See vote notes. |
| Q06 | n/a | See vote notes. |
| Q07 | n/a | See vote notes. |
| Q08 | n/a | See vote notes. |
| Q09 | PASS | Receipts bind exact committed bytes only; the entry explicitly does not treat a hash/receipt as authenticity or source identity (Q09 / PROVINCE boundary in Scope). |
| Q10 | PASS | Claims scoped to REA contracts at `12f6e09`; adjacent papers labeled vocabulary/method leads, not REA behavior; no cross-lane scope absorbed; unknowns listed (installed-skill bytes differ from pinned copy). |
| Q11 | PASS | Identifiers (enum names, `evidence_id`, issue numbers, commit pin) are source-anchored; no byte counts or digests are asserted as re-derived; recorded-vs-rederived labeling respected (verified-at names the re-open commands in `recheck:`). |
| Q12 | n/a | See vote notes. |
| Q13 | n/a | See vote notes. |
| Q14 | n/a | See vote notes. |
| Q15 | n/a | See vote notes. |
| Q16 | PASS | Each ledger-layer row states only what its cited source names (S500/S501 re-opens quote located spans; S099's six qualification clauses are enumerated, not paraphrased past); no run output is invented. |
| Q17 | n/a | See vote notes. |

## Independence note

Decisions were taken from QUALITY.md + entry bytes + frozen receipts directly; the
entry's §Q-map was consulted only afterwards as a cross-check. Critic attack work
(findings.md) did not change any candidate byte: the survivors A4/A3-both are counter-
coverage findings routed to r96, and neither touches the entry's content or the C10
backing claim.

CriticR95 · candidate 476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9 · 2026-11-05
