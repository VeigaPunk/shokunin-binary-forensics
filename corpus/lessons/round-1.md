# Fleet round-1 lesson — preserve identity, relocate reads

Round: current fleet round 1, interactive continuation of interrupted work; not a renumbering of imported r1–r60.
Sources: `LOG.md` sections “Fleet round-1 declaration”, “implementation smoke”, and “interactive continuation”; work commit `7c3ce197341b0babe0046b1d9cbb59f1ba43f54e`; `.ufo/waves/fleet-round-1-interactive/local-acceptance.json`; `reports/round-1/reviewer.md:12-41`.

## Principle and boundary

A saved PE Evidence artifact path is historical identity, not an input locator for a relocated corpus. The existing named two-image ledger now reads bytes via its own `__file__`-relative `ROOT` while checking artifact and receipt-command identity against an independently fixed `HIST`. Copying the expected path out of the saved field, or rewriting history to the current checkout, would launder the field under test.

This is a demonstrated property only of authored r55–r57 saved normalized records and their checked receipts. It does not authenticate the historical REA producer, exercise a PE loader, validate arbitrary PE files, or reverse the falsified r59 malformed-Unicode refusal claim. The envelope's `parameters.path` and `locations` are not comprehensively checked by this verifier; they are not part of the six claimed rejection cases.

## Gate

- Candidate: admit a narrow observation that the named ledger can replay unchanged saved inputs after relocation while retaining its checked historical identities. **Locally accepted as round evidence only**: real verifier passes in three contexts, six isolated semantic/path forgeries reject with expected findings and exit 1, and all nine source inputs match baseline/work/current SHA-256. Command: `python3 -B reports/round-1/replay_scenarios.py`, observed exit 0; full stdout/stderr and input revision hashes in `.ufo/waves/fleet-round-1-interactive/local-acceptance.json`.
- Candidate: count the predecessor's nine-member batch, a validated/rendered plan, or a live interactive process as a verified completed round. **Rejected**: the operator requires a complete authorized routed width-32 native task batch. Canonical plan exit 0 produced 32 distinct scopes, but the executed route assessment exits 2 and dispatch count is zero. Evidence: `.ufo/waves/fleet-round-1-interactive/routing-assessment-run.json`.
- Candidate: equate saved receipt hashes or Evidence IDs with authenticated producer origin/native readiness. **Rejected**: these checks establish internal consistency only; no producer was called. The exact boundary is exercised against saved records, not a running target.
- Candidate: claim the language/multi-image ledgers are repaired, the Evidence envelope is wholly authenticated, or r59 refusal now passes. **Rejected**: these are outside the single change and remain named gaps; no unrelated known failing check or r59 producer was rerun.
- Corpus admission: **no new `knowledge/` entry admitted**. `corpus/QUALITY.md` is absent; do not invent a quality bar or use this author-side lesson as a promotion/independence substitute.
- Outside spot-check: **not performed**. The inherited specialist reports are author-side, and no new specialist was dispatched through unauthorized routes. A non-author must independently sample at least one admit and one reject before discernment can improve.

## Outcomes and next action

Calibration improved locally for the replay criterion; coverage remained the same fixed four of eight selected saved-record families (command and exact outputs in `coverage-remeasurement.json` beside the acceptance evidence). Expansion unchanged; quality improved only for re-verification; discernment unchanged.

The round remains unadmitted. Operator-owned global role bindings must supply reviewer/critic/sentinel `@m_grok`, scribe `@m_composer`, connector `@m_antigravity` with `@m_zfl` fallback. A fresh interactive continuation then revalidates and dispatches the complete canonical 32-scope payload, preserving the same round and owned work. Missing lane craft/quality/index/registry files need a separately declared sourced restoration and outside spot-check; they are explicit debt, not silently filled with generic advice.
