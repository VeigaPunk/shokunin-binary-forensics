# Round 50 — non-author LEAF review

**PASS (bounded):** Saved r47–r49 PE32+ fixtures and records agree on the three resource paths, payload hashes, and group-language selection; the verifier passes. No REA or PE execution was performed in this review.

Command (repository root `/home/vgpnk/Projects/prymeagnt/revenger`):

```console
$ python .shokunin/revenger/corpus/verify_icon_languages.py
PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
```

Exit code: `0`. Independently inspected the fixture bytes and saved `inspection.raw.json` / `producer-receipt.json` for rounds 47, 48, 49. All three are 1,536-byte PE32+ files (`machine=0x8664`); resource directory RVA `0x2000` maps to file offset `512`, declared length `208`. Traversal records 7 entries and 3 leaves. Every leaf has numeric type/name/language IDs and a file-backed data entry; paths and payloads are:

| Index | Type/name/language (r47, r48, r49) | Entry offsets (type/name/language), data entry | Payload RVA, file offset, bytes | SHA-256 |
|---|---|---|---|---|
| 0 | 3/1/1033 in all | 528/560/616; 672 | 0x2100, 768, 48 | `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003` |
| 1 | 3/1/1036 in all | 528/560/624; 688 | 0x2140, 832, 48 | `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae` |
| 2 | 14/1/**1036, 1041, 1033** | 536/592/664; 704 | 0x2180, 896, 20 | `cc3745185dc1ae877dff5b3561df1162b7487fe78af6761a85649989979a3d01` |

The RT_GROUP_ICON payload at 896 is identical in all three: header `(reserved=0,type=1,count=1)`, followed by one 14-byte image entry at 902 with resource ID 1, declared size 48. It names both RT_ICON candidates `[0,1]`; matching the group's language against those resource languages yields **r47: 1036 → index 1**, **r48: 1041 → none**, **r49: 1033 → index 0**. `size_matches` is respectively `true/null/true`. No language fallback is inferred. Both 48-byte icon payloads and their hashes remain unchanged and distinct, as do all their decoded resource metadata. Compared with r47, the only change in r48 is file byte offset **664: 0x0c → 0x11** (group language low byte); in r49 it is **664: 0x0c → 0x09**. The respective fixture SHA-256 values are `cc02c78b44883f2217b7a8f82fa6fafc990ae6d0ca71f0eab8a3fbc4f2ba44ba`, `dc6483a985f12dbc0da4122db64565ed76c14a5e76ea8758658b4a54c35bc129`, and `d26b165ee497da494e1b5605a72877597030de53f94eba674c905bffbb079114`.

The verifier re-derives resource records from fixture bytes, compares every decoded field to each saved normalized result, checks file/subject/artifact identity, evidence ID, and receipt exit code / stdout SHA-256 / fixture SHA-256. It deep-copies r48's saved result, forges its selection from `null` to `0`, and correctly rejects the mismatched icon group. This is a saved-record mutation test, **not** a fresh REA execution or a test that REA rejects a changed on-disk fixture. Saved receipt commands report `npx -y rea-agents@6.4.0 inspect-pe-resources ... --format json` with exit code 0, and their stdout hashes match saved raw JSON bytes; that establishes internal receipt consistency, **not independent producer provenance**.

**Gaps / scope:** No failed check for these three authored fixtures. The verifier compares selected envelope fields but not all metadata (`provider`, confidence, authority, environment, limitations, evidence links, etc.); it cannot authenticate who generated saved records or receipts. The parser only establishes static resource-table relationships for these numeric-ID, three-level, PE32+ fixtures: it does not prove general PE parser correctness, full PE validity/loader behavior, language fallback, decoded icon appearance, or actual shell/window icon loading. Group-resource coverage is bounded to the declared resource directory and these fixture bytes; no new REA or PE execution was attempted.
