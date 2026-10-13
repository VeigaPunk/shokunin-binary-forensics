# Round 56 icon-group independent static review

**Verdict:** Pass for the narrow static relationship claim. An independent read of the supplied PE bytes reproduces both ordered `GRPICONDIRENTRY` records and the REA result for candidates, same-language match, and size. No execution, producer rerun, or icon decoding was performed.

## Evidence and identity

- Producer Evidence ID: `ev_44be7fd71ca9e8028e71b2714bea44597bd8b25ee83922003747e03fd231342a` (`inspection.raw.json`, operation `inspect_pe_resources`). `receipt.json` records the producer command `npx -y rea-agents@6.4.0 inspect-pe-resources .../pe-r56/fixture.exe --format json`, exit 0; this reviewer did **not** execute it.
- Independent local byte evidence, **not a REA Evidence ID**: read-only Python `Path.read_bytes`, `struct.unpack_from`, and `hashlib.sha256` over the supplied files. The `inspection.raw.json` SHA-256 `59a95f9db16633b337fd058a6d1509c95687445af02d63bb3156309f1811bbe6` equals `receipt.json.stdout_sha256`. This is consistency of saved files, not authentication of producer provenance.
- SHA-256 / bytes: r55 `41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b` / 1536; r56 `911f96b3c7cdf4b83ce49a75eadef9f6e77387578feab07605cc8dbcfaabe83b` / 1536; `truth.json` `ac83d9bf6ca24128e269a25d43216befd1b385132f525f13db9f43ae05121c6a` / 684; receipt SHA-256 `1b2bcfe2323219b069b33c64259c9e052a26ef9264cb46b9c4d707ae164066ee`.

## Reproducible checks and observed output

Read-only Python operations performed in the REPL (no fixture execution):

```python
b = Path('.../pe-r56/fixture.exe').read_bytes()
old = Path('.../pe-r55/fixture.exe').read_bytes()
[(i, old[i], b[i]) for i in range(len(b)) if old[i] != b[i]]
# [(928, 2, 3)]
pe = struct.unpack_from('<I', b, 0x3c)[0]  # 0x40
b[pe:pe+4], struct.unpack_from('<H', b, pe+24)[0]
# (b'PE\x00\x00', 0x20b) -- PE32+
# Resource directory RVA 0x2000, size 240; .rsrc VA 0x2000, raw offset 512.
# Followed IMAGE_RESOURCE_DIRECTORY entries, then IMAGE_RESOURCE_DATA_ENTRY
# RVA->file-offset mapping against .rsrc; three leaves in traversal order:
# index 0: (type 3, name/id 1, language 1033), payload @768, 48 bytes
# index 1: (type 3, name/id 2, language 1033), payload @832, 48 bytes
# index 2: (type 14, name A😀B!, language 1033), payload @896, 34 bytes
struct.unpack_from('<HHH', b, 896)
# (0, 1, 2) -- group reserved, icon type, record count
struct.unpack_from('<BBBBHHIH', b, 902), struct.unpack_from('<BBBBHHIH', b, 916)
# (1, 1, 0, 0, 1, 32, 48, 1), (2, 2, 0, 0, 1, 32, 48, 3)
```

**Observation:** Group payload header `00 00 01 00 02 00`; first entry at file `[902,916)` is `0101000001002000300000000100`; second at `[916,930)` is `0202000001002000300000000300`. Thus the two entries are ordered IDs **1 then 3**, both declaring 48 bytes. The only r55→r56 changed byte is at offset 928 (`02`→`03`), inside the second record's 16-bit ID field; `truth.json` names the same mutation. The group name's length-prefixed UTF-16LE bytes at 736 decode as `A😀B!` (`41003dd800de42002100`). The resource-leaf payload hashes independently computed were `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`, `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae`, and `672ad226768046a16b55dbcae6b0ee050e68e08e72b5089bf658593f549a4c4d`, matching producer Evidence ID above.

**Static relationship inference from independently parsed leaves:** Entry 0, ID 1, has candidate resource index `[0]`, same-language (1033) index `0`, and declared size 48 equals leaf size 48 (`true`). Entry 1, ID 3, has no RT_ICON name/id 3 in this parsed resource table: candidate indices `[]`, same-language index `null`, size match `null` (not `false`, since there is no candidate payload to compare). These values and entry offsets match `inspection.raw.json` / Evidence ID above and `truth.json` expected images. ID 2 remains an extant RT_ICON leaf but is **not** a candidate for the mutated second record.

**Unknown / limits:** Static candidate references do not prove the shell or a window will load either icon. No language fallback behavior, image decoding, visual validity, runtime selection, or execution was observed. This review covers the supplied 1536-byte fixture and saved JSON only; it does not authenticate the receipt or claim broader parser correctness. The absence of ID 3 is bounded to the resource tree independently traversed in this fixture.
