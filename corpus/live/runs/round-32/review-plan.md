# Round 32 independent review plan — PE UTF-16 named resource

## Scope and result

This is an independent, read-only review of the round-32 fixture bytes, saved `inspection.json`, and round-32 ledger. I did not invoke REA or execute the PE. The target is the local 1,024-byte PE32 fixture with SHA-256 `5169ac55c0b145b41c58b72848f694111c325d2c084266ef9d6c8763ce99adbd`. The direct byte checks below corroborate the claimed named-resource case and its reported file locations. The evidence supports a narrow static-format finding for this fixture, not general parser accuracy or runtime behavior.

## Concrete observations

- The PE signature is at file offset `0x40`; COFF machine is `0x014c` (i386), optional-header magic is `0x010b` (PE32), and there is one section. Resource directory entry 2 is `(RVA 0x2000, size 0xF0)` at file offset 200. The `.rsrc` section maps RVA `0x2000` to file offset `0x200`, with virtual size `0xF0`; the resource directory's declared range maps to `[512,752)`.
- At file offset 552, the name field is `0x800000E0`: high bit set and low 31 bits `0xE0` (224). This is a string-name pointer relative to the resource-directory base. Base file offset 512 plus 224 gives file offset 736. At 736, the little-endian 16-bit length is 5; bytes `[738,748)` are `41 00 4c 00 50 00 48 00 41 00`, the five UTF-16LE code units `ALPHA`. Prefix plus code units occupy 12 bytes `[736,748)`, within both the declared directory and file.
- The type-directory counts at file offset 548 are named=1 and ID=1. The root remains numeric type ID 10. The named branch resolves to language ID 1036 and data entry at 616; the numeric-name branch remains ID 3, language ID 1033, data entry at 632. Their payloads are 15 bytes at file offsets 672 and 704. Direct hashing yields `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229` and `cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e` respectively.
- Saved REA Evidence `ev_dcc2411a94ff88169c18f1db3d70ad0792bbccb059dec89bec0df3a578ef653d` represents the first name as `{"kind":"name","name":"ALPHA","utf16le_hex":"41004c00500048004100","location":{"offset":736,"bytes":12}}`, and preserves the second as numeric ID 3. Its two resource identities, language IDs, payload offsets/sizes/hashes, and four directory extents agree with the independent byte layout. Reported coverage is `complete`, five entries, two resources. This is a comparison of saved output to bytes, not independent proof of producer invocation or shell exit status.
- Round-31's fixture had numeric resource names only. Round 32 changes the resource directory/section virtual size from 208 to 240 and converts one name entry to a string pointer while preserving the two payloads. It tests one concrete missing dimension; it is not broad malformed-input or Unicode coverage.

## Assessment and pitfalls

**Observation:** The fixture has one high-bit string pointer, one length-prefixed UTF-16LE name, and one remaining numeric name; the saved static inventory agrees with their identities and locations. **Inference:** This example demonstrates that the parser can report a named resource alongside an ID-named resource in this particular PE32 tree. **Unknown:** Behavior for non-ASCII or supplementary-plane names, invalid UTF-16, zero-length names, out-of-range pointers/lengths, malformed count tables, PE32+, other resource layouts, Windows loader acceptance, language fallback, payload semantics, and execution.

- Do not mistake the `name.location` reported in this response (`offset 736, bytes 12`) for the resource entry location (`offset 552, bytes 8`) or payload location. They refer to distinct structures.
- The resource name's offset is directory-relative, not an absolute file offset or direct RVA. The name record is length-prefixed and not NUL-terminated; the length counts UTF-16 code units. Do not use the nearby ASCII payload strings as a name oracle.
- Preserve raw UTF-16LE bytes and the length. `ALPHA` happens to be ASCII-compatible; this single case does not establish decoding correctness for non-ASCII, surrogate pairs, malformed sequences, normalization, or case handling.
- `complete` is the parser's reported traversal coverage for this bounded input (five entries), not a general correctness guarantee. Agreement with the fixture is not proof of Windows loader acceptance or runtime resource selection.
- `truth.json` and the ledger record authored expectations; they are not independent evidence by themselves. This review derived the checked offsets and bytes from the executable and compared them with the saved result. Receipt/JSON fields likewise do not independently authenticate the actual process invocation.
- The producer record identifies `inspect_pe_resources` from the separate `rea-pe-resources` provider. It does not repair or demonstrate availability of the original native disassembler/provider.

## Bounded recommendations

1. Retain this as a narrowly scoped named-vs-numeric PE32 fixture result; use the Evidence ID and fixture digest when citing the saved inspection. Keep producer receipt provenance separate from byte-level corroboration.
2. If extending this axis, add only targeted cases with a clear oracle: a non-ASCII BMP name, a valid surrogate pair, and a malformed/out-of-range name pointer or truncated length record. Score exact raw bytes, declared length, decoded representation, and locations separately; distinguish a deliberate rejection from an omitted resource.
3. Keep runtime claims out of the result. Any future loader or application behavior check requires a separately declared target and lifecycle, and must not be inferred from this static inventory.
