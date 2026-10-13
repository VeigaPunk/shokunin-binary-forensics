# Round 32 scoring observations and bounded recommendations

## Concrete observations from round 31

- The round-31 ledger and scoring contract concern a **single synthetic PE32 resource-table fixture**, not a general parser benchmark. The corrected fixture has SHA-256 `714369ff1bfcd2e04a5f6c32f938778b38c6c455ae6a019b51e6c2d702510b47`; saved successful result is Evidence `ev_dd2627a0bc00b597eeecd066ada29a6b20e86d8d2dc19b7bf2aa517465595a24`.
- Its independent truth consists of exactly two resource occurrences, identified by full `(type ID, name ID, language ID)` tuples: `(10,2,1036)` and `(10,3,1033)`. Each is a 15-byte payload with a distinct file range and digest. The record reports two entries and `coverage.status=complete` after examining five directory entries. The scored result was precision 2/2 and recall 2/2 because each result matched exactly one independently source-decoded truth occurrence and its payload offset, length, and digest also matched.
- The full tuple is the identity key; payload location, length, digest, entry locations, and data-entry location are audited attributes. Matching only names or hashes risks conflating entries. Duplicate result rows cannot count twice against one truth occurrence. Compare order-independently while retaining locations.
- Round 31 also records a first rejected producer attempt: `invalid_request` / `invalid_format`, “Resource range leaves its section's virtual size.” That attempt has no Evidence ID, was not counted as an inspection, and the rejected bytes were not preserved. The documented correction enlarged section virtual size to 208; the successful result is on the corrected fixture. Do not attach the refusal to the corrected bytes or treat it as a parser finding about those bytes.
- The saved successful JSON alone does not authenticate shell exit status. Likewise, empty stderr is not proof of process success. Ledger separately reports the invocation exit code; preserve this distinction when writing a new result record.
- The independent review strengthened the coverage claim by decoding fixture bytes independently, rather than using `truth.json` as its oracle. Its conclusion is expressly fixture-scoped. It does not establish Windows loader acceptance, execution behavior, general PE correctness, or native-provider readiness.

## Refusal and scoring criteria to preserve

For any round-32 fixture, define the oracle from source bytes or an independently decoded manifest before comparing producer output. Count precision as `TP / all reported resources` and recall as `TP / all oracle resources`. A TP requires a one-to-one exact full-identity match plus the required payload attributes. State numerator and denominator, not just “pass.” Require complete coverage and the expected resource count before claiming full recall.

Do not score a refusal, missing Evidence ID, wrong artifact digest/format, incomplete or unknown coverage, missing/extra/duplicate rows, identity mismatch, wrong payload offset/length/hash, conflated payloads, or an oracle that is not independent. A refusal is useful telemetry, but has no resource rows to score. Keep an invalid first attempt and a corrected successful attempt as separate states, with separate hashes if both are preserved. Do not silently normalize named entries into numeric IDs, reorder tuple fields, or overlook language IDs.

## Bounded recommendations for round 32

1. Before scoring, record fixture path, exact SHA-256, size, format, source/truth provenance, and whether the target was ever executed. Keep the fixture and oracle immutable for the scored run.
2. Derive the truth independently from bytes (or another source-independent decoder), including every occurrence's `(type,name,language)` identity, payload range/length/digest, and structural locations useful for audit. Check that oracle occurrences are unique where the fixture design expects uniqueness.
3. Save the complete producer response and Evidence ID, plus invocation exit status and stderr as distinct receipts. If refused, record the exact refusal and stop scoring that attempt; repair only within authorized fixture scope and score any rerun against its newly identified bytes.
4. Report exact TP, FP, FN, precision, recall, coverage state, artifact-hash agreement, and attribute agreement. Keep limitations specific to the exercised fixture and operation; do not infer runtime semantics or broad parser reliability from one synthetic case.
5. If a reviewer is part of the round contract, wait for and record an independent review before upgrading the verdict. A review that shares the producer output as its oracle is not independent.

No round-32 producer result was examined or scored in this note. These are rubric observations and bounded recommendations derived from the round-31 ledger, not claims about a round-32 outcome.
