RESULT: COMPLETE
# R62MutantEvmDigest — bounded r19 identity counterexample
Frozen revision: `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Axes: identity-scope discrimination; independently derived byte identities; exact restoration; no production/data harm.
Scope: one in-memory mutation of r19 `subject.digest.sha256`; standard-library Python only, no provider or target execution.
Prerequisites read: agent RULES, godspeed and REA skill boundaries, frozen claims, verifier-spotcheck lesson, unchanged QUALITY Q09/Q11/Q13.
Primary inputs, relative to the extracted root: `corpus/fixtures/evm-r19/fixture.hex` and `corpus/live/runs/round-19/inspection.json`.
The saved record is primary recorded data, not an authenticated producer receipt. No rejected knowledge entry supplies factual support.

## Commands and proposed artifact
Both commands ran with cwd `/`; archive extraction returned no output.
```sh
mkdir -p /fast/scratch/hyaku/revenger-r62/R62MutantEvmDigest && git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar a3498e25ad87bf756288812d0ea7c474b09433c7 | tar -xf - -C /fast/scratch/hyaku/revenger-r62/R62MutantEvmDigest
python3 -B /fast/scratch/hyaku/revenger-r62/R62MutantEvmDigest/r62_mutant_evm_digest.py /fast/scratch/hyaku/revenger-r62/R62MutantEvmDigest
```
Proposed artifact: the scratch `r62_mutant_evm_digest.py` named above; it hashes carrier bytes unchanged, ASCII-strips/decodes the hex carrier, and compares separately named identities.
Mutant: replace only the subject digest's ASCII bytes with the independently calculated decoded digest. JSON equality against a copy with only that field changed confirms the mutation boundary.
Expected detector: require `subject_eq_carrier AND artifact_eq_carrier AND bytecode_eq_decoded`; the same detector consumes pristine, mutated and restored record bytes.
No existing verifier, future candidate entry or current producer is credited with this detector.

## Actual bounded readout
```text
python=3.14.8
carrier_bytes=39
decoded_bytes=18
carrier_sha256=294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827
decoded_sha256=d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723
record_file_before_sha256=e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948
recorded_evidence_id=ev_0ad0097eb137ff9196b29ac3fb6109d8f72ee0761e2655fa1fca594295cf6f42
recorded_parameters.encoding=hex
recorded_normalized_result.artifact.sha256=294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827
recorded_normalized_result.bytecode.sha256=d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723
pristine.memory_record_sha256=e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948
pristine.subject.digest.sha256=294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827
pristine.equalities={"subject_eq_carrier":true,"subject_eq_decoded":false,"subject_eq_saved_artifact":true,"subject_eq_saved_bytecode":false,"artifact_eq_carrier":true,"bytecode_eq_decoded":true,"subject_in_carrier_or_decoded":true}
pristine.detector=PASS failures=[]
mutation_byte_range_half_open=[137,201]
mutation_only_subject_digest=True
mutated.memory_record_sha256=47f1fc39304bc0bf4c89aceb14abe53a068838d11826afd81bf4683a5f2c0248
mutated.subject.digest.sha256=d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723
mutated.equalities={"subject_eq_carrier":false,"subject_eq_decoded":true,"subject_eq_saved_artifact":false,"subject_eq_saved_bytecode":true,"artifact_eq_carrier":true,"bytecode_eq_decoded":true,"subject_in_carrier_or_decoded":true}
mutated.detector=FAIL failures=["subject_eq_carrier"]
restored.memory_record_sha256=e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948
restored.subject.digest.sha256=294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827
restored.equalities={"subject_eq_carrier":true,"subject_eq_decoded":false,"subject_eq_saved_artifact":true,"subject_eq_saved_bytecode":false,"artifact_eq_carrier":true,"bytecode_eq_decoded":true,"subject_in_carrier_or_decoded":true}
restored.detector=PASS failures=[]
carrier_file_after_sha256=294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827
record_file_after_sha256=e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948
memory_restored_bytes_exact=True
carrier_file_unchanged=True
record_file_unchanged=True
strict_verdict=KILLED
disjunctive_verdict=SURVIVED
```

## Verdict and scope boundary
**KILLED by the proposed role-specific detector; SURVIVED by the disjunctive membership predicate.** Baseline and restored controls pass, so the strict kill is not an unrelated baseline failure.
`subject_eq_carrier` and `subject_eq_saved_artifact` change true→false; `subject_eq_decoded` and `subject_eq_saved_bytecode` change false→true. Independently anchored artifact/carrier and bytecode/decoded equalities remain true.
`subject in (carrier_sha256, decoded_sha256)` stays true: it accepts either identity and therefore cannot detect the subject's reassignment from the hex carrier to its decoded content. This is a scope-coverage finding, not permission to relax the contract.
Restoration ran in `finally`: the exact original in-memory bytes were restored, and reread carrier/record file bytes and full hashes match their pre-probe values. Neither file was ever written.
For the new C09 entry, carry separately named identities plus the equivalent derivation code AND output inside that entry; this report alone cannot repair Q11. Output equality does not establish completeness, authenticity, provider behavior or runtime semantics.
No source rows, prior evidence, README, QUALITY or production implementation were edited. Only this assigned report was written outside own scratch. C1 admission and README held status are not claimed; fresh falsify and all-criteria admission remain prerequisites.
Installs/updates: none.
