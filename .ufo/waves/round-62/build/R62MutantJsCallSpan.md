RESULT: COMPLETE
# R62MutantJsCallSpan — bounded source-slice premise

Axes: coverage (frozen C1); safeguards: Q11 traceability and exact byte preservation.
Scope: one unnamed require-edge end-column defect in my isolated archived js-r3 saved record; no production integration or admission decision.
Frozen revision: `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Read claim contract at `reports/round-62/claims.md:7-60`, unchanged Q11/Q13 at `corpus/QUALITY.md:23-25`, and prior missing-span diagnosis at `corpus/lessons/round-61-verifier-spotcheck.md:70-74,206-218`; all were also opened in the extracted frozen tree.

## Archive and proposed evidence artifacts
Scratch root: `/fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/`.
Actually executed, cwd `/`:
```text
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar --output=/fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/frozen.tar a3498e25ad87bf756288812d0ea7c474b09433c7
tar -xf /fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/frozen.tar -C /fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/tree
git get-tar-commit-id < /fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/frozen.tar
output: a3498e25ad87bf756288812d0ea7c474b09433c7
```
Proposed readout code: `/fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/detect_call_span.py`.
Complete actual output: `/fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/probe-output.txt`.
Inputs fixed independently: `tree/corpus/fixtures/js-r3/index.js` and `tree/corpus/live/runs/20261012T164357Z/analysis.json`; no locator comes from saved subject paths.

## Mutant, detector and observed output
Selected `normalized_result.graph.edges[9]` by relation `imports`, properties `kind=require`, and absence of `imported_name`; detector prints `source_call_matches=1 unnamed_require_edges=1`.
Mutant: `evidence.location.value.end.column: 50 -> 49`; all other parsed and raw record content retained.
Applied with `xd://ast_edit` + `xd://resolve`: `Applied 1 replacement in 1 file.`
Stdlib byte comparison printed `exact_expected_field_replacement=True`, `record_lengths=(193573, 193573)`, `changed_byte_offsets=[31794, 31795]`, `changed_byte_text=('50', '49')` (raw file offsets, zero-based).
Expected detector: independent regex extraction of the authored ASCII `require` call compared with the source slice selected by the saved edge; end-exclusive slicing is a bounded interpretation, not provider-wide semantics.
The identical command ran on pristine, mutated and restored bytes, cwd `/`:
```text
python3 -B /fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/detect_call_span.py /fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/tree
```
| Phase | Source-derived call span (line:column) | Saved span | source_call | saved_slice | slice_equal | Exit |
|---|---|---|---|---|---|---|
| pristine | 1:28–1:50 | 1:28–1:50 | `"require('./transform')"` | `"require('./transform')"` | True | 0 |
| mutated | 1:28–1:50 | 1:28–1:49 | `"require('./transform')"` | `"require('./transform'"` | False | 1 |
| restored | 1:28–1:50 | 1:28–1:50 | `"require('./transform')"` | `"require('./transform')"` | True | 0 |
Probe verdict: **KILLED**. Baseline and restoration pass; mutant fails for the missing closing parenthesis, not a crash or hash rejection. No existing verifier was exercised or credited.

## Restoration and exact hashes
Restoration ran in the detector orchestration's `finally` block, even on failure:
```text
tar -xf /fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/frozen.tar -C /fast/scratch/hyaku/revenger-r62/R62MutantJsCallSpan/tree corpus/live/runs/20261012T164357Z/analysis.json
restore_exit=0
record_exact_bytes_restored=True
source_exact_bytes_unchanged=True
```
Hash derivation actually executed: `sha256 = lambda data: hashlib.sha256(data).hexdigest()` on the corresponding `Path.read_bytes()` snapshots; full-byte restoration was separately compared with `restored_record == pristine_record`.
| Exact byte scope | SHA-256 |
|---|---|
| Saved JSON before and restored | `7c3ba8c15673a7e48600bba3f42a6ca3935dbd75e30832569a631979e31ed452` |
| Saved JSON mutated | `43fc61fce71e39e3b6fad56be7e13fa71ab727223050a8553f4ffdbfdd71cbb7` |
| Authored index.js before and after | `f7d8bf470bb37d5eacedd7d571705bc80cc365195069ce1b7c6d4a24ae869fd7` |

## What the NEW C04 entry should print
Embed the supplied detector code itself and its actual output inside the entry, not merely this report or an equality summary. Print both fixed input paths, match/edge counts, selected edge index, source-derived and saved coordinates, exact `source_call` and `saved_slice`, equality, and exit for each phase. Derive any copied hashes in-entry with hashing code plus output, or explicitly label them recorded.
This probe covers only this js-r3 edge's off-by-one end-column premise. It does not derive destructured-name correspondence, test js-r7-v2, establish every span, prove identifier authenticity, or demonstrate another verifier's deletion sensitivity. A successful equality check is not Q11 completeness or all-criteria admission.
No fixture JavaScript, bytecode, REA producer, service, network target or other runtime was invoked. No writes targeted live corpus/README, prior rejected entries, counterexamples, fixtures or saved records; only my assigned report and scratch artifacts were written. README remains outside my write scope and is not marked held. No source rows, new gate, promotion or current-producer claim.
Installs or updates: none.
