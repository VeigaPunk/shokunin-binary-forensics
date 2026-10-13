# Round 57 independent delta review

## Commands and direct output

Independent byte comparison (before reading saved inspection): Python read the two fixture byte strings, computed SHA-256, then enumerated unequal byte positions.

```text
r55: 1536 bytes, SHA-256 41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b
r57: 1536 bytes, SHA-256 71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d
diffs [(924, 48, 47)]; lengths same True
```

Computed SHA-256 directly over both icon payload ranges, [768,816) and [832,880): respectively `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003` and `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae`; each byte range is identical between fixtures. The RT_GROUP_ICON payload [896,930) differs as expected, with r57 digest `78dc9a7dd2d08db459b2bf22958f72fd2d105b56f8c0a28e232a1864a299169c`.

Then read `truth.json`, `inspection.raw.json` and `receipt.json`. The r57 truth manifest SHA-256 and size match direct bytes and records changed offset 924; it specifies group Unicode name `A😀B!`, IDs 1/2, candidates [0]/[1], same-language indices 0/1 and size-match true/false. r55 manifest specifies the same IDs/candidates and both sizes matching before mutation. Saved REA record subject digest matches r57 bytes; it reports those two images and exactly the expected second-image mismatch. Receipt records successful exit (0), command `npx -y rea-agents@6.4.0 inspect-pe-resources ... --format json`, and Evidence ID `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07`.

## Evidence classification

- **OBSERVATION:** Direct byte comparison establishes one changed byte at file offset 924, value 0x30 (48) → 0x2f (47), equal file lengths and the listed file hashes. Direct payload hashing establishes both icon payload byte ranges unchanged. (Local byte evidence; no REA Evidence ID.)
- **OBSERVATION:** Saved static parser output under Evidence ID `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07` identifies the named RT_GROUP_ICON `A😀B!`, two entries (IDs 1 and 2), candidates [0] and [1], same-language resources 0 and 1, with only the second `size_matches:false`. Receipt ties this record to the r57 SHA-256 and successful CLI invocation.
- **OBSERVATION:** r57 truth manifest SHA-256 equals independently computed file SHA-256; declared mutation offset and expected images agree with byte comparison and saved parser result. r55 truth manifest agrees with r55 hash, mutation history and prior expected sizes.
- **INFERENCE:** The r55→r57 artifact delta is precisely the claimed single-byte declared-size mutation, and the saved static inspection is consistent with the manifest while preserving both icon references/candidates. This supports this fixture-specific parser calibration claim.
- **UNKNOWN:** No execution, image decoding, language fallback, or actual OS icon loading was observed. This review does not establish general parser correctness beyond this fixture/case.

## Bounded verdict

**Supported for the specified fixtures and saved evidence.** The independent byte delta, unchanged icon payloads, manifests and recorded parser output align with the claim. Static resource relationships and size comparison only; no runtime behavior asserted.
