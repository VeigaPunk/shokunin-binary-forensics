# Round 58 non-author LEAF review

## OBSERVATION

I read `/tmp/mission-revenger-standing.md`, the REA `SKILL.md`, the round-58 declaration and repair telemetry in `.shokunin/revenger/LOG.md`, the verifier source, the three fixture byte arrays, saved `inspection.raw.json` and `receipt.json` files. No producer or PE executable was run. The initial implementation's r55 `resource fields` failure is recorded in LOG; this review evaluates the current repaired source, not that failing version.

Command (repository root):
```sh
python3 .shokunin/revenger/corpus/verify_named_multi_icon_states.py
```
Exact stdout/exit:
```text
PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
exit_code=0
```
The verifier independently decodes PE32+ resource directories from bytes, builds a normalized tree, compares `actual == expected` for every field of the **full normalized result** (including named keys, all ancestor entry locations, leaf payload hashes and group-image metadata), verifies artifact identity and saved receipt consistency, and asserts three distinct ordered icon-image states. Thus all three full normalized results agree: r55 3 leaves/2 group records and second ID2 candidate [1], same-language 1, size true; r56 second ID3 candidate [], same-language null, size null; r57 second ID2 candidate [1], same-language 1, size false. First record is ID1 candidate [0], same-language 0, size true in each.

Independent challenges (Python REPL, only `struct.unpack_from`, fixture bytes and JSON; not calling the verifier's decoder for the byte/location derivation):
```python
pe=unpack_from('<I',d,0x3c)[0]           # 64
sec=pe+24+unpack_from('<H',d,pe+20)[0]   # 328
va=unpack_from('<I',d,sec+12)[0]         # 8192
ro=unpack_from('<I',d,sec+20)[0]         # 512
root=ro+unpack_from('<I',d,pe+24+128)[0]-va  # 512
# Root's RT_GROUP_ICON entry, then named-group entry, then language entry:
type_entry=root+16+8                    # 536
type_dir=root+(unpack_from('<I',d,type_entry+4)[0]&0x7fffffff)
group_entry=type_dir+16                 # 592
name_off=root+(unpack_from('<I',d,group_entry)[0]&0x7fffffff)
lang_dir=root+(unpack_from('<I',d,group_entry+4)[0]&0x7fffffff)
lang_entry=lang_dir+16                  # 664
n=unpack_from('<H',d,name_off)[0]
raw=d[name_off+2:name_off+2*n]
```
For **each** r55, r56, r57, independently observed `root=512`, ancestor entry offsets `[536,592,664]` (each 8 bytes); UTF-16 length `n=5` code units at offset **736**, raw hex `41003dd800de42002100`, decoded `A😀B!`, name location `(736,12)` including the length. Saved JSON matches all these values. This specifically challenges the prior implementation's omission of name metadata and its substitution of reported ancestor locations. The current decoder constructs both from bytes; it does not copy them from saved JSON.

Independent byte comparison (Python REPL `[(i,a,b) for i,(a,b) in enumerate(zip(r55,rXX)) if a!=b]`): exact output r56 `[(928, 2, 3)]`, and r57 `[(924, 48, 47)]`; each fixture is 1536 bytes. The former is the second group record's ID2→ID3; the latter its declared size48→47. SHA-256 fixture digests r55 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`, r56 `911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b`, r57 `71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d` agree with both verifier constants and receipts.

Mutation challenge: I separately deep-copied each saved normalized result and passed it to `compare_normalized` against its unchanged byte-derived tree. Exact `(round,mutation,outcome)` output:
```text
(56, candidate_resource_indices=[1], REJECTED: r56 normalized result)
(57, size_matches=True, REJECTED: r57 normalized result)
(55, name.location={offset:738,bytes:12}, REJECTED: r55 normalized result)
(55, entry_locations[0]={offset:538,bytes:8}, REJECTED: r55 normalized result)
```
The first two are the required forged image claims; the latter two exercise the name and ancestor comparisons independently. These tests make no file edits.

Saved stdout SHA-256 recomputation versus receipts: r55 `54ffdeab7108895404efa01edb400c9bc32c36c4f85540babed2f5241137f860`, r56 `59a95f9db16633b337fd058a6d1509c95687445af02d63bb3156309f1811bbe6`, r57 `5c915ebdc4c79a6d98e3b9f374e6e2e67168a1c5b391487ac80bd8e199d34fc8`; all equal. The three saved Evidence IDs are `ev_db785aec4caaa20630a96a8a3b250ff3aae9c0fa454ff36abe4415725fa22e79`, `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a`, `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07` (r55–r57 respectively). The verifier compares these to constants, the saved operation and subject digest, and the receipt's saved command, exit status, duration type/range, Evidence ID and hashes.

## INFERENCE / bounded verdict

**PASS for round 58's fixture-scoped calibration claim:** 3/3 complete normalized results equal byte-derived trees, 2/2 exact one-byte deltas verified, 2/2 requested forged claims rejected. Two more location mutations reject. No calibration harm observed in this bounded set. This validates the static saved-record comparison against these three authored fixtures, not general PE parsing.

## UNKNOWN / boundaries

The receipt hashes and saved command establish internal consistency, **not authentication of the historical REA producer**; neither this review nor the verifier reran it. PE execution, OS icon loading, rendering/image decoding, language fallback, arbitrary PE correctness, unrelated providers and historical producer origin remain unknown. Exact source paths and Evidence IDs are fixed to these authored fixtures. Resource overlap and malformed arbitrary PE behavior are not generalized from this test.
