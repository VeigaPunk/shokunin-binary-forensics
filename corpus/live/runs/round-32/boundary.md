# Round 31 boundary review (independent)

## Observations
- The requested `.shokunin/revenger/live/runs/round-31/LEDGER.md` path is absent in this checkout. I reviewed the matching round ledger at `.shokunin/revenger/corpus/live/runs/round-31/LEDGER.md`; this path distinction matters when citing the review.
- The ledger bounds the tested target to a locally authored 1,024-byte PE32 fixture (`714369ff…510b47`), made by copying the r30 PE32 header and constructing a two-resource tree against `truth.json`. It explicitly says no execution. It reports byte changes at offsets 204 (resource directory size) and 320 (section virtual size).
- The producer is the REA CLI `npx -y rea-agents@6.4.0 inspect-pe-resources`; the first request was refused because the resource range exceeded section virtual size. That attempt has no Evidence ID and is not treated as an inspection. After changing section virtual size 103→208, the ledger records successful exit, empty stderr, and Evidence `ev_dd2627a0bc00b597eeecd066ada29a6b20e86d8d2dc19b7bf2aa517465595a24`.
- On the corrected fixture, ledgered source-scored tuples agree for two expected resources (precision 2/2, recall 2/2); reported coverage is complete for five examined entries. This is evidence for this fixture's static resource inventory only.
- Provenance is layered: fixture bytes/hash, source-derived truth, producer receipt/output, and comparison are distinct. The ledger explicitly warns that saved inspection JSON alone cannot authenticate shell exit status. The original round-1 native-provider refusal is still unresolved, not repaired by this result.

## Pitfalls / limits
- Do not conflate the rejected initial fixture with the corrected committed fixture, or count the rejection as an analysis finding. The failed bytes were not preserved, so its claim is limited to the recorded error.
- “Complete” is scoped to the parser's five examined entries, not broad PE correctness. The two-resource synthetic sample does not establish behavior on arbitrary PE files.
- Static resource inventory does not show Windows loader acceptance, language fallback, payload semantics, or runtime behavior. Do not turn tuple agreement into a claim of execution or general parser accuracy.
- Do not describe the REA/native provider as working: the ledger identifies the round-1 native-provider refusal as unresolved. The round-31 operation is the separate PE-resource CLI operation.
- Treat invocation provenance as receipt-dependent. Evidence ID/JSON and a stated exit code are useful records but the JSON itself is not proof of the shell invocation; retain/check the invocation receipt when assessing provenance.

## Bounded recommendations
- Cite the actual `corpus/live/.../round-31/LEDGER.md` path and Evidence ID; keep the missing `live/runs/...` location distinct rather than implying it was reviewed.
- Preserve the source-scored claim narrowly: “two authored resource tuples matched in this synthetic PE32 fixture.” Keep any broader correctness, loader, or runtime conclusion marked unknown.
- For a provenance audit, check the already-recorded invocation receipt and fixture/truth artifacts; do not rerun the producer merely to recreate the same evidence.
- A follow-up should target a distinct, predeclared fixture dimension (or independent raw-byte validation), and report its own expected tuples and limitations. Do not infer that the round-31 result closes provider readiness.
