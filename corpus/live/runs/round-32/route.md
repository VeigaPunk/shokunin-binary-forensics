# Round 32 route note — saved PE resource inspection shape

## Scope and source

Read-only review of `.shokunin/revenger/corpus/live/runs/round-31/inspection.json` only. No REA producer was invoked and no target was executed. The record identifies Evidence `ev_dd2627a0bc00b597eeecd066ada29a6b20e86d8d2dc19b7bf2aa517465595a24`, operation `inspect_pe_resources`, provider `rea-pe-resources` v1, and subject `fixture.exe` (SHA-256 `714369ff1bfcd2e04a5f6c32f938778b38c6c455ae6a019b51e6c2d702510b47`).

## Observations

- The saved record has top-level `evidence_id`, `subject`, `provider`, `analysis_profile`, `predicate_type`, `operation`, `parameters`, `raw_result`, `normalized_result`, `confidence`, `authority`, `environment`, `limitations`, `locations`, and `evidence_links` fields. Here `analysis_profile`, `raw_result`, `environment` are null; `evidence_links` is empty.
- `normalized_result` contains artifact identity (`path`, `sha256`, `bytes`), `format`, `machine`, resource-directory metadata, `directories`, `resources`, `icon_groups`, `coverage`, and `limitations`.
- Resource items in this record have `index`, `type`, `name`, `language`, `entry_locations`, `data_entry_location`, `code_page`, `reserved`, and `payload`. `payload` has an RVA, file `location` (`offset`, `bytes`), and SHA-256.
- The two observed resource type/name/language values all use tagged integer forms, e.g. `{"kind":"id","id":10}`. `directories` exposes `named_entries` and `id_entries`; all four directory rows here report zero named entries. Coverage is `complete`, with `examined_entries: 5` and `resources: 2`.
- The record itself says non-`RT_GROUP_ICON` payloads remain opaque; the listed payloads are byte ranges and digests, not decoded content. Its limitations also exclude language fallback and actual loading behavior.

## Inference and unknowns

- The `{kind, id}` discriminator is an observed encoding for numeric identifiers, not evidence of the encoding for a named PE resource. This sample contains no named entries, so the named-value key/type, Unicode decoding, and any name normalization are **unknown** from this record.
- `named_entries` is a count on directory rows and should not be mistaken for the concrete resource name representation. A named resource might be represented in the same `type`/`name`/`language` slots, but that is only a schema-shaped hypothesis pending a named-resource sample or authoritative schema.
- `icon_groups: []` is observed for this fixture; do not treat it as evidence that the parser omits icon groups generally.

## Bounded recommendations / pitfalls

1. For downstream display of this saved record, render the observed numeric form explicitly (for example, `ID 10`) and preserve the original tagged object. Do not silently coerce IDs into strings or assume every value is numeric.
2. Keep named-resource handling conditional until a fixture with named entries is available. Then capture the full saved JSON and verify exact shape, encoding, and ordering; do not fabricate a `{kind:"name", ...}` contract from this ID-only record.
3. Keep `entry_locations` and payload `location` distinct: one points to resource-table entries, the other to payload bytes. Preserve file offsets/lengths and payload digest when presenting opaque resources.
4. Keep claims bounded to static inventory. “Complete” is the parser's reported inventory coverage for this input, not proof of runtime selection, successful decoding, or shell/window presentation.
