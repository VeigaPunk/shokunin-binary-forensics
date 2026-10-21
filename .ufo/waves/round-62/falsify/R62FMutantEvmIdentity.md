GRADE: HOLDS — r19 subject-digest substitution changes the printed scope to decoded-only

Frozen revision: `d97761952be256d145d298022de03091de91d358` (resolved with `/usr/bin/git rev-parse --verify`, then extracted with `/usr/bin/git archive` into this seat's scratch).
Candidate: `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`.
Candidate SHA-256, unchanged in all three runs: `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`.
Scratch S: `/fast/scratch/hyaku/revenger-r62/R62FMutantEvmIdentity`; archived tree T: `S/tree`.
Axes: correct digest referent; observable semantic change rather than record-hash-only detection; exact restoration.

## Observation — one mutation, one bounded detector

Mutant: change ONLY `T/corpus/live/runs/round-19/inspection.json:1`, JSON pointer `/subject/digest/sha256`, from the carrier hash to the locally decoded bytecode hash. Artifact/bytecode fields, fixture bytes, saved evidence id and readout source remain unchanged. This is an isolated scratch mutation, not a correction to any saved production record.
Carrier derivation printed by the detector: `r19_carrier_bytes=39 sha256=294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827`.
Decoded derivation printed by the detector: `r19_decoded_bytes=18 sha256=d1086bce32141782858674721977939681534320ece338f455dad57b40c0e723`.
Expected detector: manual comparison against the entry's complete `## Provenance` stdout, with a structured field diff to distinguish scope behavior from the incidental record-file digest change. The readout itself is not expected to reject inputs.
Executed `/usr/bin/env TMPDIR=/fast/scratch/hyaku/revenger-r62/R62FMutantEvmIdentity/tmp /usr/bin/python3 -B /fast/scratch/hyaku/revenger-r62/R62FMutantEvmIdentity/probe.py PHASE` separately with PHASE `pristine`, `mutant`, `restored`, always cwd `/`.
Each invokes `/usr/bin/python3 -B /fast/scratch/hyaku/revenger-r62/R62FMutantEvmIdentity/readout.py /fast/scratch/hyaku/revenger-r62/R62FMutantEvmIdentity/tree`, with a 30-second bound and the same TMPDIR.
`probe.py` verifies that readout bytes equal the frozen in-entry Python block before invoking it. Readout source SHA-256: `740f321e97e28d7f11b4a58e106f054447a284519c59487398752bc87cd37eeb`.

Exact relevant outputs (complete stdout, stderr and detector logs are retained as `S/{pristine,mutant,restored}.{stdout,stderr,log}`):
```text
phase=pristine
readout_exit=0
readout_stderr=b''
stdout_equals_provenance=true
r19_digest_scopes={"artifact":"carrier_file_bytes_only","bytecode":"decoded_bytecode_bytes_only","subject":"carrier_file_bytes_only"}
semantic_diff=[]
detector_exit=0
phase=mutant
readout_exit=0
readout_stderr=b''
stdout_equals_provenance=false
r19_digest_scopes={"artifact":"carrier_file_bytes_only","bytecode":"decoded_bytecode_bytes_only","subject":"decoded_bytecode_bytes_only"}
semantic_diff=[{"actual":"decoded_bytecode_bytes_only","path":"r19.digest_scopes.subject","provenance":"carrier_file_bytes_only"},{"actual":"47f1fc39304bc0bf4c89aceb14abe53a068838d11826afd81bf4683a5f2c0248","path":"r19.record.sha256","provenance":"e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948"}]
detector_exit=1
phase=restored
readout_exit=0
readout_stderr=b''
stdout_equals_provenance=true
r19_digest_scopes={"artifact":"carrier_file_bytes_only","bytecode":"decoded_bytecode_bytes_only","subject":"carrier_file_bytes_only"}
semantic_diff=[]
detector_exit=0
```

| phase | r19 record SHA-256 (4175 bytes in every phase) | full readout stdout SHA-256 |
|---|---|---|
| pristine | `e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948` | `aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf` |
| mutant | `47f1fc39304bc0bf4c89aceb14abe53a068838d11826afd81bf4683a5f2c0248` | `91dee48c7b0a57e07bdf9cc1b79cda3a3430b9a5587ae63f5c0af836f054738c` |
| restored | `e892dd18ff219f71ce2644a3f5a3e3ad3479d2ca46df9e2a7c260e7b33f15948` | `aff3efda2691cb95ed7146292f602ba5dc5c40794e5c64efda3aaa7275f235bf` |

## Inference — scoped semantic/Q11 audit, not output equality alone

Primary candidate paths: `:324-332` computes referents from hashes of the actual carrier and decoded bytes; `:365-371` reads and decodes the fixture and extracts the subject digest; `:403-405` independently applies the referent function to subject/artifact/bytecode. `:442` records the pristine r19 output; `:227-229` names these inventory fields.
The two locally derived hashes differ. After substitution, the subject digest does not satisfy either carrier branch (`:326-329`) but satisfies the decoded branch (`:330-331`), explaining the observed scope transition. Artifact remains carrier-only and bytecode remains decoded-only. Thus this result is not merely a token-presence check or the inevitable change of `record.sha256`.
No scoped Q11 failure was found: this digest-role claim carries both its actual in-entry derivation and its printed output. No failed Q is asserted by this assigned probe; no conclusion is made about other entry values or all-criteria admission.
Mutant verdict: KILLED by the bounded external Provenance-diff detector, with pristine/restored passing. The readout exits 0 throughout, as expected for a manual readout; this demonstrates input-drift visibility, NOT a deletion-sensitive guard or Q13 coverage. Candidate `:163-170` expressly disclaims such guard credit.

## Restoration and unknowns

Restored the original subject digest immediately after the mutant run. The restored 4175-byte record has the exact pristine SHA-256 above; restored stdout also has the exact pristine/recorded stdout hash. Candidate and readout hashes remained unchanged.
Only own scratch and this report were written. No fixture JS/EVM execution, producer/provider calls, blockchain/RPC, build, lint, formatter, or live-production edits occurred.
Unknown/unclaimed: evidence-id authentication, producer origin, custody, runtime behavior, present provider capability, and admission. None follows from these digest comparisons. No correction is indicated by this scoped result.

VERDICT: HOLDS for the assigned frozen r19 identity-scope attack; mutant KILLED by manual Provenance comparison, bytes restored. Installs/updates: none.
