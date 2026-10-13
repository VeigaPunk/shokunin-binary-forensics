# Independent delta review — round 56

## Checks performed (no target execution)
Commands/equivalent Python byte checks run independently on the supplied files:
- Read r55/r56 bytes; lengths: 1536 / 1536.
- SHA-256: r55 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b`; r56 `911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b`.
- Bytewise comparison found exactly one changed offset: 928 (`0x3a0`), old `0x02`, new `0x03`; all other 1535 bytes equal. At offset 928 the little-endian resource ID changes `0200` to `0300`.
- SHA-256 of group payload at file range `[896,930)` is r55 `45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a`, r56 `672ad226768046a16b55dbcae6b0ee050e68e08e72b5089bf658593f549a4c4d`. r56 digest agrees with inspection payload digest. The group payload has two image entries; first entry remains ID 1 and second entry ID changes 2→3.
- Truth manifest checks: r55 hash equals `source_sha256`; r56 hash equals `sha256`; stated size 1536 matches. Manifest changed offset `[928]` and mutation description agree with byte comparison. Manifest expects image ID 1 candidate `[0]`, same language 0, size match true; ID 3 no candidate and null language/size. These values match normalized inspection.

## Evidence and assessment
**Evidence ID:** `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a` (inspection.raw.json; receipt records same ID, exit code 0 and matching fixture SHA-256).

**Observation:** The supplied bytes differ only at offset 928, within the RT_GROUP_ICON payload at `[896,930)`. The Unicode group name is `A😀B!` in the inspection, and its payload range/hash are internally consistent. The inspection reports icon resource ID 1 resolving to candidate index 0, same-language and size match true; ID 3 has no candidate.

**Inference:** This round is a clean, single-field mutation of the second group-image resource reference; the reported parser output and truth manifest are consistent with the files. It demonstrates relationship inventory behavior, not image decoding or runtime loading.

**Unknown / limits:** Static artifact evidence only. No execution, image decode, shell/window load, language fallback, or independent validation of parser internals. The inspection labels coverage complete for its bounded resource inventory, while payloads other than RT_GROUP_ICON remain opaque as stated in its limitations.

**Verdict:** PASS — byte delta, payload digest, truth manifest, and recorded inspection agree within the stated static-analysis scope.
