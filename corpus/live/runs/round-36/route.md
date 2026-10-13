# Round 36 — static icon-group inspection route

## Recommendation

For a bounded, execution-free PE resource inventory, use the established CLI shape with an explicit absolute fixture path:

```sh
npx -y rea-agents@6.4.0 inspect-pe-resources "/absolute/path/to/fixture.exe" --format json
```

This is a CLI route recommendation only; this lane did not invoke the command or inspect a target. The repository’s rounds 27–35 record this command shape, and the REA native/artifacts guide also documents `rea inspect-pe-resources ./selected.exe --json` (or the `inspect_pe_resources` API with an absolute `path`).

## Saved Evidence fields to score

In the saved Evidence envelope, check `operation: "inspect_pe_resources"`, `provider.id: "rea-pe-resources"`, and `normalized_result`. The result exposes top-level `resources` and `icon_groups` arrays. The group/icon relationship fields are:

- Each `icon_groups[]` entry has `resource_index` (an index into `resources`) and `images`.
- Each image has its directory-entry `location`, parsed dimensions/planes/bit depth, `declared_bytes`, and `resource_id`.
- `candidate_resource_indices` lists all reported resources with numeric type ID 3 (`RT_ICON`) and numeric name ID matching the group entry’s `resource_id`.
- `same_language_resource_index` is the candidate whose language identity matches the group resource’s language, or `null` if none.
- `size_matches` is a boolean comparing that same-language candidate’s payload byte count with the group entry’s `declared_bytes`; it is `null` when there is no same-language candidate.

Resolve and score these links against independently authored fixture bytes and the corresponding resource rows (type 14 = `RT_GROUP_ICON`; type 3 = `RT_ICON`). Also check the group's referenced image-entry location and resource identities. Keep `candidate_resource_indices`, exact same-language selection, and size agreement distinct; do not collapse them into a claim that Windows selected or rendered an icon.

## Limits

This operation statically parses resource-table relationships. It does not decode image payloads, perform Windows language fallback, or observe shell/window loading. `coverage.status: "complete"` is scoped to the reported resource tree. A saved JSON Evidence record is not by itself proof that a particular CLI invocation/package version produced it; retain a producer receipt/raw output separately if provenance matters. No target execution, native provider setup, or repeat diagnostics are recommended for this question.
