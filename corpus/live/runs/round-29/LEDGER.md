# Round 29 evidence ledger — resource language perturbation

- Producer: `npx -y rea-agents@6.4.0 inspect-pe-resources /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r29/fixture.exe --format json`; exit 0, stderr not separately captured (combined tool output is valid single JSON). Static only. Saved producer result `inspection.json`: Evidence `ev_503af514d0af04c0d221c70948be240424911b1c27ef42e82a3c4a07c2c1bfcb`. Baseline `../round-28/inspection.json`: Evidence `ev_bb5fb8cc540834401a018a1bc021a1cab989a7226d27e122ff51bc4387f86537`.
- Fixture: `../../../fixtures/pe-r29/fixture.exe` and `truth.json`; SHA-256 `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5`; copied r28 then changed only offset 576, `09→0c` (little-endian ID 0x0409→0x040c). Source-truth payload at offset 600, 15 bytes, SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.
- OBSERVATION [both Evidence IDs]: parser reported language ID 1033→1036, same type 10/name 1, same payload location/length/hash; reported entire file SHA changed. These are static parser outputs on authored fixtures, not independent proof of loader behavior.
- INFERENCE: this controlled pair supports fixture-scoped language-field sensitivity and unchanged payload attribution, contingent on the independent reviewer reproducing the bytes and comparisons.
- UNKNOWN: Windows loader language fallback, executable behavior, correctness on other PE structures. Original round-1 native `open_binary` provider remains unavailable; not retried.

| check | pass |
|---|---|
| byte_delta_exactly_offset_576 | True |
| baseline_file_sha | True |
| new_file_sha | True |
| distinct_evidence_ids | True |
| same_provider_and_operation | True |
| one_resource_each | True |
| language_from_1033_to_1036 | True |
| type_name_unchanged | True |
| resource_locations_unchanged | True |
| payload_location_digest_unchanged | True |
| directory_and_coverage_unchanged | True |

No semantic code execution; no native provider readiness claim.
