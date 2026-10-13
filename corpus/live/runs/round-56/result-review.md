# Round 56 independent result review

**Verdict: PASS for the narrow static PE resource-tree claim.** The three reported resource leaves, their payload ranges and hashes, and both RT_GROUP_ICON image links match independently decoded fixture bytes. No target execution or producer rerun was performed. Evidence ID: `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a` (`inspection.raw.json`).

## Independent checks and outputs

Read-only CPython `pathlib`/`hashlib`/`struct` checks on the two supplied `.exe` files; `json.loads` of supplied truth, raw result, and receipt. No binary was loaded or executed. The checks included:

```python
[(len(b), hashlib.sha256(b).hexdigest()) for b in (old, new)]
# [(1536, '41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b'),
#  (1536, '911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b')]
[(i, x, y) for i, (x, y) in enumerate(zip(old, new)) if x != y]
# [(928, 2, 3)]
hashlib.sha256(inspection_raw_json_bytes).hexdigest()
# 59a95f9db16633b337fd058a6d1509c95687445af02d63bb3156309f1811bbe6
new[736:748].hex(' ')
# 05 00 41 00 3d d8 00 de 42 00 21 00
new[896:930].hex(' ')
# 00 00 01 00 02 00 01 01 00 00 01 00 20 00 30 00 00 00 01 00 02 02 00 00 01 00 20 00 30 00 00 00 03 00
```

The old group bytes at 896:930 have the identical first 32 bytes and end `02 00` instead of `03 00`. Truth's old/new SHA-256, 1536-byte size, offset-928 mutation, and expected image links agree with these independent bytes. Receipt's fixture SHA-256 matches the new file; receipt's stdout SHA-256 matches the exact `inspection.raw.json` bytes; its Evidence ID equals the raw result's ID. **The receipt's exit code and reported command/duration are recorded claims, not independently witnessed execution.**

A separate little-endian PE walk checked DOS `e_lfanew=64`, signature `PE\0\0`, machine `0x8664` (34404), PE32+ magic `0x20b`, resource data-directory location 216 and `(RVA 0x2000, bytes 240)`, and `.rsrc` mapping `(RVA 0x2000 -> file offset 512)`. Following entry pointers from 512 gives six directory locations 512, 544, 576, 600, 624, 648; their respective counts are `(named,id)=(0,2),(0,2),(1,0),(0,1),(0,1),(0,1)`. All six raw-result directory records match **by file offset** (the result's directory array is traversal order, not ascending offset); 8 entries and 3 terminal resources are present.

| leaf index | independent path (type / name / language) | entry offsets | data entry | payload offset / bytes / RVA | independently computed SHA-256 |
| --- | --- | --- | --- | --- | --- |
| 0 | ID 3 / ID 1 / ID 1033 | 528, 560, 616 | 672 | 768 / 48 / 8448 | `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003` |
| 1 | ID 3 / ID 2 / ID 1033 | 528, 568, 640 | 688 | 832 / 48 / 8512 | `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae` |
| 2 | ID 14 / named `A😀B!` / ID 1033 | 536, 592, 664 | 704 | 896 / 34 / 8576 | `672ad226768046a16b55dbcae6b0ee050e68e08e72b5089bf658593f549a4c4d` |

Every leaf path, entry location, data-entry location, payload SHA-256, code page 0 and reserved 0 matches `normalized_result`. The name has length 5 UTF-16 code units and exact bytes `41003dd800de42002100` at 738:748, correctly decoding to `A😀B!` (12 bytes including its 2-byte length at 736).

The group payload header decodes as `(reserved=0,type=1,count=2)`. Independent `struct.unpack_from('<BBBBHHIH', ..., 6 + 14*i)` yields images `(width,height,color,reserved,planes,bits,size,id)` of `(1,1,0,0,1,32,48,1)` at 902:916 and `(2,2,0,0,1,32,48,3)` at 916:930. Against the complete walked tree, ID 1 has candidate `[0]`, same-language index `0`, matching 48 bytes; ID 3 has no candidate `[]`, same-language `null`, and no applicable size match `null`. All group/image locations and fields equal the normalized result. Crucially leaf ID 2 is still present, but **the group's second link now names ID 3**; treating that second image as still linked to leaf 1 would be unsupported.

## Claim classification and limits

- **OBSERVATION** (Evidence ID above, independently cross-checked against fixture bytes): the static three-leaf resource inventory, named Unicode group, two declared image links, and missing ID-3 candidate are correct. `coverage.status=complete` is supported **for this bounded reachable resource tree** of eight entries and three leaves, not for the entire program.
- **INFERENCE**: a consumer that resolves icons strictly by the declared image ID and the walked resource tree would not find the second group's ID-3 icon. No fallback policy or actual loader outcome was observed.
- **UNKNOWN**: image decoding, shell/window behavior, execution effects, language fallback, and any runtime path. Other non-group payloads remain opaque, as the REA limitations state. Receipt matching a saved stdout digest establishes file consistency, not independent proof of producer identity/version, execution, or a cryptographic attestation of the Evidence ID.

No unsupported static leaf/link claim found. Do not elevate static parser observations to runtime behavior.
