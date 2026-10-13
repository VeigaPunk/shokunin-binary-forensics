# Round 56 independent PE resource tree review

## Verdict
PASS: the three RT_ICON/RT_GROUP_ICON leaf identities, file offsets, lengths, and SHA-256 digests independently agree with REA's normalized result. The changed group entry points to resource ID 3, for which this tree contains no matching RT_ICON leaf; ID 1 has a same-language candidate and matching size. This is static structure, not proof of runtime icon loading.

## Evidence and byte checks
REA Evidence ID: `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a` (receipt binds it to fixture SHA-256 `911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b`).

Independent read-only commands/checks (Python `struct`, `hashlib`; no executable run):
- `sha256sum` equivalent via `hashlib.sha256(path.read_bytes())`: r55 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`; r56 `911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b`.
- Parsed PE `e_lfanew=64`, PE32+ optional header, resource RVA `0x2000`, size 240; `.rsrc` maps RVA 0x2000 to file offset 512. Traversed directory entry words recursively from root offset 512, resolving UTF-16 name strings and data-entry RVAs through section mapping.
- Independently obtained tree: type 3 / name ID 1 / lang 1033 -> data entry offset 672, RVA 8448, file offset 768, size 48, SHA-256 `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`.
- type 3 / name ID 2 / lang 1033 -> data entry offset 688, RVA 8512, file offset 832, size 48, SHA-256 `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae`.
- type 14 / UTF-16 name `A😀B!` / lang 1033 -> data entry offset 704, RVA 8576, file offset 896, size 34, SHA-256 `672ad226768046a16b55dbcae6b0ee050e68e08e72b5089bf658593f549a4c4d`.
- Independently hashed exact slices `[768:816]`, `[832:880]`, `[896:930]`; values equal the listed hashes and REA. The group leaf bytes include two 14-byte records at offsets 902 and 916: IDs 1 and 3, each declares 48 bytes. `fixture.exe[928:960].hex()` begins `0300000000000000...`, consistent with ID 3 at record offset 916 + 12.

## Observation / inference / unknown
**Observation:** direct table traversal and hashes yield the three leaves above; REA reports the same identities/ranges/digests, and its receipt's artifact digest matches the independently computed r56 digest. REA's group image candidates are ID 1 -> resource index 0, same language, size matches; ID 3 -> no candidate. Truth file states mutation at offset 928, second group image ID 2→3; truth is corroborative fixture metadata, not my primary parsing basis.

**Inference:** the group metadata's second image reference is unresolved in this resource tree, whereas the first resolves by ID/language/declared size. This is a table relationship only.

**Unknown:** whether Windows/shell/application loading applies language fallback, decodes these payloads, or displays either icon; no execution or image-loading test was performed. Non-group payload contents and broader PE semantics are outside this check.

## Limits
Independent review was scoped to the supplied r55/r56 fixtures, r56 truth metadata and round-56 raw inspection/receipt. This was offline byte parsing only; no REA producer rerun, CLI invocation, or target execution. The comparison validates the reported three leaves, not every parser property or behavior.
