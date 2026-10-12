# pe-evidence-bind — round 27

**Lane:** pe-evidence-bind  
**Verdict:** PASS  
**Source:** `inspection.json` only (no REA rerun, no PE exec)

## Required binds

| Check | Expected | Observed | OK |
|-------|----------|----------|----|
| evidence_id | `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef` | `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef` | yes |
| operation | `inspect_pe_resources` | `inspect_pe_resources` | yes |
| subject sha256 | `523e6dc1b8cc2b48a636ce3cb93736ce46d4c8d58c594d8d8dd2ed72ca2640bb` | subject.digest.sha256 and normalized_result.artifact.sha256 match | yes |
| resource count | exactly 1 | `len(resources)==1`, coverage.resources==1 | yes |
| type id | 10 | resources[0].type.id == 10 | yes |
| name id | 1 | resources[0].name.id == 1 | yes |
| language id | 1033 | resources[0].language.id == 1033 | yes |
| payload offset | 600 | payload.location.offset == 600 | yes |
| payload bytes | 15 | payload.location.bytes == 15 | yes |
| payload sha256 | `0346b578bdfe68866acea157268520567a5d6e96a28ab8a95835569921f088aa` | match | yes |
| coverage.resources | 1 | 1 | yes |
| icon_groups | empty | `[]` | yes |
| confidence | observed | `observed` | yes |

## Notes

- Fixture path in subject/local_path and parameters.path aligns with pe-r27 fixture.exe.
- Single resource entry index 0; RT type id 10 (RT_RCDATA family id space as recorded).
- No extra resources or icon_groups present.

**Final:** PASS — all pe-evidence-bind criteria satisfied.
