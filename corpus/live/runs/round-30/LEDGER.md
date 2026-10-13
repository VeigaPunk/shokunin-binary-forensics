# Round 30 — name-ID sensitivity ledger

Static PE fixture: `corpus/fixtures/pe-r29/fixture.exe` → `corpus/fixtures/pe-r30/fixture.exe`; known byte truth in `corpus/fixtures/pe-r30/truth.json`. REA CLI `npx -y rea-agents@6.4.0 inspect-pe-resources <absolute r30 fixture> --format json` exited 0. Captured combined output at `inspection.json` (separate empty stderr not authenticated). No PE execution.

- OBSERVATION (fixture bytes): exactly one changed byte, file offset 552, `0x01→0x02`; file SHA `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5` → `b94d840aa7eb952474b30260bc70e092fb1db832b0aa1bc393936d8dc4ce661a`. Payload 600..614 remains SHA `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. Byte comparison performed locally; not a REA observation.
- OBSERVATION (saved REA output): baseline Evidence `ev_503af514d0af04c0d221c70948be240424911b1c27ef42e82a3c4a07c2c1bfcb` (r29 `inspection.json`), new Evidence `ev_178f0cb2ef7b5e4f61e73e19f71cba354c44a337b998da07ee559cb93ede53df` (`inspection.json`). Both normalized records report one type-ID 10, language-ID 1036 resource with payload location offset 600/length 15 and same payload SHA; only reported name-ID changes 1→2. Artifact path and file SHA change. Complete normalized-record comparison leaves no other difference.
- INFERENCE: this controlled pair supports static name-field sensitivity and stable payload attribution for this PE fixture only; it does not validate the parser generally.
- UNKNOWN: actual Windows loader behavior, payload semantics, independent authentication of saved producer invocation from the JSON alone, native decompilation. The original Ghidra/IDA/Hopper provider refusal is unresolved.

Checks (`True` required):
- exit_zero: `True`
- new_evidence_id: `True`
- source_sha: `True`
- new_sha: `True`
- sole_byte_552: `True`
- baseline_resource_name: `True`
- new_resource_name: `True`
- type_and_language: `True`
- payload_identity: `True`
- all_other_normalized_equal: `True`
- record_structure: `True`

Result: 11/11 local checks passed. Non-author `reviewer.md` independently verified 10/11 from saved bytes and JSON; `exit_zero` is a local producer receipt, not independently authenticated by saved JSON. `boundary.md` pointer label corrected after reviewer finding.
