# pe-resource-review — round 27

## Identity checks
- Evidence id matches required: `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef`
- Operation matches: `inspect_pe_resources`
- Fixture path: `.shokunin/revenger/corpus/fixtures/pe-r27/fixture.exe`
- File size 1024; SHA-256 `523e6dc1b8cc2b48a636ce3cb93736ce46d4c8d58c594d8d8dd2ed72ca2640bb` matches truth.json and inspection `subject.digest` / `normalized_result.artifact`
- Format pe32, machine 332; resource directory RVA 8192, file offset 512, directory bytes 103; data directory file offset 200
- One resource: type id 10 (RT_RCDATA), name id 1, language id 1033
- Payload file offset 600, 15 bytes ASCII `REV-R27-PAYLOAD`, payload SHA-256 `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa` — confirmed by reading fixture bytes and matching inspection payload.location/sha256

## Relation check
- Truth relation: “one reported RT_RCDATA name 1 language 1033 maps to the authored payload bytes”
- Inspection reports exactly one resource with that type/name/language and payload digest/location
- Verifier `--self-test` (exit 0):
  - `POSITIVE ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef 1/1 RT_RCDATA name 1 language 1033 maps to authored payload`
- Exactly one positive relation holds; inventory is 1/1 as stated

## Mutation rejection quote
Verifier self-test line:
`NEGATIVE REJECTED payload relation mismatch`

## What is NOT proved
- No execution of the PE or loader behavior
- No claim of general PE resource-parser completeness beyond this fixture path
- No icon-group / RT_GROUP_ICON behavior (icon_groups empty; limitations state icon candidates and shell loading are unobserved)
- Opaque non-icon payloads beyond digest and byte location; no semantic decode of RCDATA content beyond ASCII match to truth

PASS
