# Round 27 — PE resource identity to payload bytes

Hand-built PE32, no compiler and no execution. One `.rsrc` section. One resource: type 10 (RT_RCDATA), name 1, language 0x0409. Payload at file offset 600 is the 15 bytes `REV-R27-PAYLOAD`. Whole-file SHA-256 `523e6dc1b8cc2b48a636ce3cb93736ce46d4c8d58c594d8d8dd2ed72ca2640bb`. Truth: `corpus/fixtures/pe-r27/truth.json`.

Command (once, exit 0, stderr empty): `npx -y rea-agents@6.4.0 inspect-pe-resources <absolute fixture.exe> --format json`. Evidence `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef`, operation `inspect_pe_resources`, provider `rea-pe-resources`. Saved in `inspection.json`. Subject and artifact SHA match the fixture. Exactly one resource: type 10, name 1, language 1033, payload offset 600, 15 bytes, SHA-256 `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa`. `coverage.resources` is 1. `icon_groups` is empty. Confidence is `observed`.

OBSERVATION: the reported resource location and digest equal the authored payload bytes. INFERENCE: that single type/name/language identity owns those bytes in this static table. UNKNOWN: loader behavior, language fallback, icon decoding, and whether the parser is complete on any other PE. Limitations in the Evidence say non-icon payloads stay opaque and shell loading was not observed.

Verifier: `python3 .shokunin/revenger/corpus/verify_pe_resources.py --self-test` prints one positive line and `NEGATIVE REJECTED payload relation mismatch`, exit 0. This route is not EVM, ZIP, ELF, or JS-graph. No PE execution.
