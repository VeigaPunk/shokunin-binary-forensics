# Round 36 independent icon-group scoring checklist

## Raw-byte oracle

- [ ] Bind the saved result to the exact fixture bytes: independently record PE file SHA-256/size; locate the resource data directory, map RVAs through section raw ranges, and traverse the reachable resource tree from the bytes (not fixture `truth.json` or REA output).
- [ ] Treat numeric resource type **14** (`RT_GROUP_ICON`) and type **3** (`RT_ICON`) as the relevant leaves. Decode every group payload as a bounded `GRPICONDIR`: `WORD reserved`, `WORD type` (must be 1), `WORD count`, followed by exactly `count` 14-byte `GRPICONDIRENTRY` records. Record raw fields: `bWidth`, `bHeight`, `bColorCount`, `bReserved`, `wPlanes`, `wBitCount`, `dwBytesInRes`, `nID` (WORD). Check payload length/count, not just parsed summaries.
- [ ] Independently enumerate each RT_ICON leaf and its payload bytes. Link each group entry by `nID` to RT_ICON **numeric name ID**, within the same language ID. Compare `dwBytesInRes` to referenced icon payload byte size; retain payload SHA-256 for audit, but do not infer equality of group-entry metadata and image contents.

## Required relation fields / scoring

For every RT_GROUP_ICON and RT_ICON leaf, retain identity `{type kind/id, name kind/id or UTF-16 name, language kind/id}`, resource-tree entry locations, data-entry location, payload RVA/file offset/size/SHA-256. For every group also retain group payload header fields and ordered entries with all fields above. For each entry retain its `nID`, the exact matching RT_ICON identity (or explicit missing result), and size-match status. This makes group→icon resolution auditable without flattening away duplicate IDs or language variants.

Score group leaves and ordered entry relations against the raw-byte oracle: no omitted or extra group/icon leaf; exact group fields and entry order/values; each reference resolves to the unique same-language RT_ICON with matching numeric name ID; declared size agrees. Report precision/recall separately for leaves and references. Preserve unresolved/ambiguous relations as explicit outcomes rather than silently dropping them.

## False-positive and missing-reference boundary

A resource merely resembling an icon, having type 3, or appearing near a group is **not** a group reference. Do not link by payload hash, dimensions, position, or ID across languages; the group entry's `nID` plus same-language RT_ICON identity defines the relation. A group with no matching same-language ID is a real group leaf with a **missing reference**, not grounds to omit the group or synthesize an icon. Do not silently fall back to another language; Windows selection/fallback and image decoding/runtime loading are outside this static oracle. A dangling reference or size mismatch is surfaced and scored as such, not counted as a successful link. Round 35's raw fixture had no type-14 leaves, so it is a useful no-group false-positive control only; it does not validate group parsing or link resolution.
