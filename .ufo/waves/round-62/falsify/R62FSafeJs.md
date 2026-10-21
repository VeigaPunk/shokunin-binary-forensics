GRADE: BROKEN — C04 CommonJS require-name candidate (Q11)

Frozen revision: `d97761952be256d145d298022de03091de91d358`
Claim base: `5bd4a90fc1a34caa94496601b60537b3aab12301`
Pre-registration: `a3498e25ad87bf756288812d0ea7c474b09433c7`
Candidate SHA-256 (frozen archive): `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`
Axis: C04 admission quality; severity: admission-blocking.

**Observation — reproduction:** I extracted the frozen revision with `git archive` into the assigned scratch tree, reconstructed the candidate's embedded `readout.py` there, and ran it once against that tree (Python 3 standard library; `TMPDIR` under owned scratch). `sha256sum readout.py` printed `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac  readout.py`; the readout exited 0 and emitted 25 JSONL lines; `sha256sum stdout.jsonl` printed `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416  stdout.jsonl`; line count was `25`. These match candidate §Reproduce:74-80.

Exact readout lines included:
`{"fixture":"js-r3","counts":{"imports_edges":3,"named_imports_edges":2,"unnamed_imports_edges":1,"named_import_name_values":["checksum","rot13"]}}`
`{"fixture":"js-r7-v2","counts":{"imports_edges":2,"named_imports_edges":1,"unnamed_imports_edges":1,"named_import_name_values":["rot13"]}}`

**Observation — Q11 defect:** The candidate asserts `readout.py` and stdout digests at lines 4 and 80, and a S029 single-page digest at line 1 (repeated in §Sources:248). Its in-entry reproduction command at lines 74-77 only archives the input and runs `python3 -B readout.py tree`; the script at lines 113, 126, 212-213 hashes fixture/record data and emits JSON, but does not hash itself or its stdout. The sentence-to-output inventory at lines 253-272 has no derivation/output entries for these digests. The S029 page digest likewise has no derivation/output in the readout and is not labeled recorded/not re-derived. The values are stated as facts, not recorded values.

**Inference:** Q11 requires each digest to have its in-entry derivation and output, or be explicitly labeled recorded. The successful output equality and independently matching hashes above establish that the claimed values are correct; they do not supply the missing in-entry derivations. This is a material Q11 failure, so this entry cannot earn C04 admission as frozen. Other Q criteria are not exhaustively adjudicated here.

**Exploit path / impact:** A reviewer relying on the 25-line stdout match or the printed field inventory alone can miss the unsupported hash facts and pass an entry that fails the unchanged Q11 bar. Do not count this C04 candidate toward coverage; this report does not decide C09 or the final K score.

**Smallest remediation:** Add the exact hash commands and their outputs to the candidate reproduction/inventory for the script and stdout digests; either derive-and-print the S029 page digest in-entry or label it explicitly recorded (not re-derived). Then obtain focused non-author-seat review of the corrected hash.

**Scope / side effects:** No fixture JavaScript, producer, network, service, or verifier was invoked; the readout only read archived fixture bytes and saved JSON. No source/worktree files were changed. Writes were limited to the owned scratch archive/helper/stdout and this assigned report. No escape or target-side mutation observed.

VERDICT: BROKEN — Q11 blocks this frozen C04 entry from admission.
Installs: none.
