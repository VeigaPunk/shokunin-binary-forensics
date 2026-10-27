VERDICT: REPAIR Q-map n/a rationale before wave 2 — lint is clean, but Q08 and Q12 use inapplicable `n/a` labels where the criterion is superseded or actually applicable.

## Evidence

- Candidate Q-map (`corpus/knowledge/round-71-apk-axml-byte-evidence.md:295-314`) has exactly one row per Q01–Q16. `python3 -B reports/round-71/measure.py .` → `C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0`; also `C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes`. This establishes structural lint and embedded output consistency, not correctness of the reasons or admissions.
- Q08 says `n/a | superseded by Q11 ...` (entry:306). But QUALITY.md:23 explicitly says Q11 supersedes Q08, and QUALITY.md:32 requires every `n/a` to name why it cannot apply. The axis applies historically but is superseded; label it `superseded by Q11` (as other entries do), rather than n/a. Candidate itself describes value derivations under Q11 (entry:309), underscoring this is not an inapplicable subject.
- Q12 says `n/a | this entry writes no rejected-source row` (entry:310). Q12 is an admission criterion about rejected-source rows, and this entry has no such row; however, the candidate does have a source list and explicitly records supersession among source citations. More importantly, the candidate is a new-source C05 entry and can legitimately be evaluated against Q12: absence of a rejected-source row makes the criterion non-triggered, not necessarily impossible to apply. The rationale needs to explain no reject/flip row exists and hence no Q12 object is asserted, or use the project's accepted `n/a` convention with that clearer reason.
- Q13 names the gate's one-directional deletion weakness, superset-output weakness and forged alternate in-tree command case (entry:311); this is candid and consistent with the command semantics. Q16 calls credits bounded to printed output and claims repaired prose was checked (entry:314), but the map's Q04 and Q11 explanations are broad self-support: Q04 concludes “no tool claim” while the entry discusses the readout and derivation tools extensively (entry:302; items 11-17), and Q11 asserts every count/offset/identifier/digest carries derivation output without a sentence-to-output inventory. These require independent reviewer coverage; the author map is not itself proof.
- Candidate's explicit limits at entry:289 include single fixture, no compression and non-valid dex program. Entry:283-285 separates observations, inferences and unknowns. These are useful honest bounds, but do not substitute for decisions supported by each Q axis.

## Counterexample / risk

A map can pass `LINT_QMAP=0` while misclassifying the semantics of n/a: QUALITY.md:32 mandates a reason, and Q08's own current criterion has been superseded, not made impossible to evaluate. A lint-clean map therefore is not evidence of criterion satisfaction. Q12's bare “no rejected-source row” also does not articulate why the criterion cannot apply; if a reject row is present elsewhere in the entry/header/source apparatus, that row still needs its own Q12 test.

## Impacted axes

Calibration (n/a vs superseded/applicable classification) and coverage (Q01–Q16 are present, but completeness of justifications and self-support remains unproven). Not an admission judgment.

## Smallest safe correction

Change Q08 decision to `superseded by Q11` and point to QUALITY.md:23; preserve Q11 as the operative row. Clarify Q12 as `n/a` only if an explicit scan establishes there is no rejected-source row in this entry; otherwise evaluate the actual rejected row's located quote and viable flip. Wave-2 reviewers should treat the Q-map as a claim inventory, independently check cited prose/output rather than accepting its own basis, especially Q04/Q11/Q16.

## Checks / scope

Read frozen `reports/round-71/claims.md` and `reports/round-71/pre-registration.txt`; no lane source edits. Ran the registered counter/lint command above and the candidate embedded-output gate. An initial attempt to invoke `measure.py` without its required TREE argument exited 2 with `usage: measure.py TREE (TREE/corpus must exist)`; rerun with `.` produced the captured full output. Scratch `/fast/scratch/hyaku/revenger-r71/R71W1QmapCritic/` was removed. No installs.