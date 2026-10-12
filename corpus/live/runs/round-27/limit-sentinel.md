# pe-limit-sentinel — round 27

- **lane:** pe-limit-sentinel
- **evidence_id:** `ev_a524338e43a8a20a3fb0f018d46ef2fe06732e323bfb3ce98fd813bd223f50ef`
- **operation:** `inspect_pe_resources`
- **verdict:** **PASS**

## Checks

| Check | Result |
| --- | --- |
| Evidence id + operation match task | PASS |
| `inspection.stderr` empty (0 bytes) | PASS |
| No chain/network (or url/http/socket/dns) fields in JSON | PASS |
| Confidence is observational, not over-claim | PASS (`confidence`: `observed`; `authority`: `shipped-artifact`) |
| No PE execution claim | PASS |
| No icon decoding claim | PASS |
| No complete Windows resource loader claim | PASS |
| Limitations not over-read as general PE parser proof | PASS |

## Limitations (as stated; not expanded)

Top-level and `normalized_result.limitations` are identical (3 items):

1. Static PE32/PE32+ type/name/language resource inventory; payloads other than RT_GROUP_ICON remain opaque.
2. Icon candidates are resource-table relationships. Language fallback, image decoding and actual shell/window loading are not observed.
3. Exact shared byte ranges are retained; non-identical overlapping resource structures or payloads are rejected.

## Non-claims confirmed

- Result describes static table inventory + one RT_RCDATA-style payload location/hash; `icon_groups` is empty.
- Explicitly disclaims image decoding and shell/window loading.
- Does not assert runtime PE execution, loader fidelity, language fallback, or a full Windows resource manager.
- `coverage.status` = `complete` is scoped to examined resource-table entries on this fixture (`examined_entries`: 3, `resources`: 1), not a proof of a general PE parser.

## Fail criteria (not triggered)

Would fail if limitations were treated as general PE parser completeness, or if execution/icon-decode/full-loader claims appeared, or if stderr/chain-network noise were present.
