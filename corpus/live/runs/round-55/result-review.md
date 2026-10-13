# Round 55 — independent result review (byte oracle)

**Verdict: accept only the bounded static PE resource-tree result.** I independently read `fixtures/pe-r55/fixture.exe` as bytes, without using fixture `truth.json`, another review, target execution, or a producer rerun. The saved `inspection.raw.json` matches all three reachable leaf identities, their byte ranges/digests, and the two *ordered static* group-icon references. This does not establish rendering or generic PE coverage.

## Identity and receipt

- Fixture: 1536 bytes, SHA-256 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`. This equals both `receipt.json.fixture_sha256` and the saved result's `subject.digest.sha256` / `normalized_result.artifact.sha256`; recorded artifact length also agrees.
- `inspection.raw.json` SHA-256 **as saved bytes**: `54ffdeab7108895404efa01edb400c9bc32c36c4f85540babed2f5241137f860` = `receipt.json.stdout_sha256`. Evidence ID in receipt and saved result equals `ev_db785aec4caaa20630a96a8a3b250ff3aae9c0fa454ff36abe4415725fa22e79`. Receipt records CLI exit 0. Equality validates these local files' mutual consistency, **not** independent producer origin, execution history, or the CLI's claimed provenance.
- PE headers from bytes: `MZ`, PE header at `0x40`, AMD64 `0x8664`, PE32+ optional magic `0x20b`, one `.rsrc` section mapping RVA `0x2000` to file offset 512. Resource data directory at file offset 216 gives RVA 8192, size 240. These agree with saved format, machine and directory locations.

## Entire reachable resource tree

Reading each IMAGE_RESOURCE_DIRECTORY header and its counted entries from the root at 512 yields **six directory nodes, eight directory entries, three data leaves**; counts and offsets match `normalized_result.directories` and `coverage` (`complete`, `examined_entries: 8`, `resources: 3`). Every directory structure and entry-location claim in the saved JSON matches the byte walk, not merely the labels:

| Leaf index; type / name / language | Path entry offsets; data entry | Payload RVA → file range; SHA-256 |
| --- | --- | --- |
| 0; ID 3 / ID 1 / ID 1033 | 528, 560, 616; 672–687 | 8448 → 768–815 (48); `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003` |
| 1; ID 3 / ID 2 / ID 1033 | 528, 568, 640; 688–703 | 8512 → 832–879 (48); `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae` |
| 2; ID 14 / name `A😀B!` / ID 1033 | 536, 592, 664; 704–719 | 8576 → 896–929 (34); `45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a` |

The group name entry at 592 is a high-bit name pointer to offset 736. At 736 the length is five UTF-16 code units; offsets 738–747 are `41003dd800de42002100`, which decodes to `A😀B!` (the emoji is a surrogate pair). Its directory at 576 has one named entry and zero numeric-name entries. All three data entries have zero code page and reserved fields. No additional reachable resource leaf occurs in this fixture.

The group payload at 896 begins `(reserved=0, type=1, count=2)`. Its 14-byte records, parsed in **stored order**, agree exactly with both saved `icon_groups[0].images` objects:

1. Offset 902–915: 1×1, 0 colors/reserved, planes 1, 32 bits, 48 declared bytes, referenced icon resource ID 1; candidate index `[0]`, same-language index 0, matching 48-byte payload.
2. Offset 916–929: 2×2, 0 colors/reserved, planes 1, 32 bits, 48 declared bytes, referenced icon resource ID 2; candidate index `[1]`, same-language index 1, matching 48-byte payload.

Comparison to **r42 fixture bytes and saved r42 result** (r42 fixture SHA-256 `3ab5008b436eb4facd3966767a507fa4b1625160532585a09a6af2f752b38941`, Evidence `ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d`): r42 has numeric group name ID 1 and size-208 resource directory. Here the directory size is 240, and the group entry instead points to the UTF-16 name. Exactly 12 byte positions differ: 220, 588, 590, 592, 595, 736, 738, 740, 741, 743, 744, 746; the three leaf payload slices are byte-identical, including both ordered link records. The saved r42 group records likewise link IDs 1 then 2 to indices 0 then 1. This isolates the new supported observation to name encoding / tree lookup, not new icon-payload decoding.

## Scoring and limits

At the level of **reachable resource leaves** in this fixture: precision 3/3 and recall 3/3; named group identity 1/1; ordered static references 2/2, no extra group/link or leaf. These denominators derive solely from this complete, tiny byte tree, not from a broad PE sample. `complete` is accepted only for this resource inventory, not a general claim about executable behavior or every possible PE layout. The two links are references/candidates; no Windows icon choice, language fallback, image decode, loading, UI rendering, native provider status, or producer provenance is established. The ID 3 payloads are opaque apart from their ranges and hashes. Reject any inference that this static fixture was executed or that the resource-group candidates were displayed.
