# Round 28 — one-byte PE resource calibration

Baseline: `corpus/fixtures/pe-r27/fixture.exe`, saved `../round-27/inspection.json`, Evidence `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef`. Altered: `corpus/fixtures/pe-r28/fixture.exe`, `inspection.json`, Evidence `ev_bb5fb8cc540834401a018a1bc021a1cab989a7226d27e122ff51bc4387f86537`. `npx -y rea-agents@6.4.0 inspect-pe-resources <absolute pe-r28 fixture.exe> --format json` exited 0 with empty stderr; one producer invocation, no PE execution.

Source truth: byte-identical except at file offset 600, `0x52` (`R`) → `0x53` (`S`); whole-file digests `523e6dc1b8cc2b48a636ce3cb93736ce46d4c8d58c594d8d8dd2ed72ca2640bb` → `9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`; 15-byte resource payload `REV-R27-PAYLOAD` → `SEV-R27-PAYLOAD`; payload digest `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa` → `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`. Fixture `truth.json` records constants and provenance; no compiler used.

Checks (local comparison of saved Evidence to authored files, **not** a second REA producer):
- one_byte_delta: True
- baseline_identity: True
- changed_identity: True
- distinct_evidence_id: True
- resource_count: True
- resource_identity: True
- payload_offset_and_length: True
- new_payload_digest: True
- old_payload_digest: True
- different_payload_digest: True

OBSERVATION: two REA records report distinct Evidence IDs and matching artifact digests; each has exactly one type 10/name 1/language 1033 resource with payload at offset 600, length 15. Their payload hashes match the respective authored bytes. INFERENCE: for these two PE files, this static parser relates the same resource identity to a changed payload and reflects a single altered input byte. UNKNOWN: actual PE loader behavior, parsing completeness on other files, runtime selection of language, parser implementation/cause of reported difference, and authenticity of saved records beyond this local replay. No native disassembly/provider claim.

Independent non-author LEAF `pe-delta-review` confirmed all ten checks by independently hashing both fixtures and comparing both saved REA records (`reviewer.md`). The review cannot independently authenticate the author’s REA invocation/exit status, and neither analysis observes runtime behavior.
