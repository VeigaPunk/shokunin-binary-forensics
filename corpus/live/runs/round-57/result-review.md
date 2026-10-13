# Round 57 independent result review (LEAF, read-only artifact inspection)

## Scope and method
Read `/tmp/mission-revenger-standing.md` and the REA skill. No target execution, REA rerun, recursive agent, commit, push, or merge. First examined `pe-r55/fixture.exe` and `pe-r57/fixture.exe` using Python `Path.read_bytes` and `hashlib.sha256` to determine their lengths, digests, and sole differing byte. Then read the truth and saved result/receipt JSON using `json.loads`; independently traversed the PE resource-directory bytes using `struct.unpack_from` before comparing parsed structures with the saved result. The resource parser walked directory entries and computed data-entry RVA→file-offset conversion from the `.rsrc` section. This is independent byte inspection, not a second REA run.

Evidence ID from the saved REA result and receipt: `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07`. This ID names the **saved producer result**; the reviewer did not create a new REA Evidence ID. Byte offsets and digests below refer directly to the two on-disk fixtures.

## Actual inspection commands / outputs
These are the substantive commands run in the persistent Python REPL, abbreviated only where a parser was expanded into helper functions:

```python
a = Path('.shokunin/revenger/corpus/fixtures/pe-r55/fixture.exe').read_bytes()
b = Path('.shokunin/revenger/corpus/fixtures/pe-r57/fixture.exe').read_bytes()
print(len(a), len(b), hashlib.sha256(a).hexdigest(), hashlib.sha256(b).hexdigest())
print([(i, a[i], b[i]) for i in range(min(len(a),len(b))) if a[i] != b[i]])
# 1536 1536 41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b 71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d
# [(924, 48, 47)]

# struct-derived PE32+ header: e_lfanew=64, machine=34404, optional magic=0x20b;
# resource data-directory location=216, RVA=8192, size=240;
# .rsrc section RVA=8192, raw offset=512, raw size=1024.
# Walk resource-directory entries from file offset 512. Actual output:
# directories (offset, bytes, named, IDs):
# [(512,32,0,2),(544,32,0,2),(600,24,0,1),
#  (624,24,0,1),(576,24,1,0),(648,24,0,1)]
# visited entries=8; resource leaves=3.

# Decode named entry UTF-16LE at 736: 05 00 41 00 3d d8 00 de 42 00 21 00
# -> A😀B!, utf16le_hex=41003dd800de42002100.
# Decode group bytes [896:930], header [896:902] = 00 00 01 00 02 00;
# image 0 [902:916] declares 48 bytes and resource ID 1;
# image 1 [916:930] declares 47 bytes and resource ID 2.
# Parse raw result and compare independent structures:
print(inddirs == raw['normalized_result']['directories'],
      indresources == raw['normalized_result']['resources'],
      [{'resource_index':2,'images':groupimgs}] == raw['normalized_result']['icon_groups'])
# True True True
print(hashlib.sha256(rawp.read_bytes()).hexdigest())
# 5c915ebdc4c79a6d98e3b9f374e6e2e67168a1c5b391487ac80bd8e199d34fc8
```

## OBSERVATION — all leaves and links match bytes
- Root directory at 512 has ID types 3 and 14. RT_ICON type 3 has two ID names 1/2, language 1033. RT_GROUP_ICON type 14 has named key `A😀B!` (length 5 UTF-16 code units, 12 bytes including its length field), language 1033. Resource directory size 240 ends at 752 and includes the name bytes 736–747. The traversal produced exactly the saved six directories, including all `location`, entry counts, zero-valued directory metadata and all eight entry slots. Evidence ID above and direct file bytes.
- Leaf index **0**: type ID 3/name ID 1/lang ID 1033; entry offsets 528, 560, 616 (each 8 bytes); data entry 672 (16 bytes), RVA 8448; payload `[768,816)` (48 bytes), SHA-256 `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003`. Its code page and reserved words are zero. Matches every reported leaf field and r55/r57 bytes.
- Leaf index **1**: type ID 3/name ID 2/lang ID 1033; entry offsets 528, 568, 640; data entry 688 (16 bytes), RVA 8512; payload `[832,880)` (48 bytes), SHA-256 `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae`. Code page/reserved are zero. Matches every reported leaf field and r55/r57 bytes.
- Leaf index **2**: type ID 14/named key `A😀B!`/lang ID 1033; entry offsets 536, 592, 664; data entry 704 (16 bytes), RVA 8576; payload `[896,930)` (34 bytes), SHA-256 `78dc9a7dd2d08db459b2bf22958f72fd2d105b56f8c0a28e232a1864a299169c`. Code page/reserved are zero. The r55 payload digest is `45eb70319667352d8bfea3249f7fb30166c6835d2cf564b5ec303bf2d716c17a`; only byte 924 changed.
- Group link **0**, record `[902,916)`: width/height 1/1, color/reserved 0/0, planes 1, bits 32; declared size 48 and resource ID 1. Searching independently parsed icon leaves by type/name gives candidate `[0]`, whose language 1033 matches the group and whose payload size is 48. The saved `same_language_resource_index:0` and `size_matches:true` are byte-supported.
- Group link **1**, record `[916,930)`: width/height 2/2, color/reserved 0/0, planes 1, bits 32; declared size **47** and resource ID **2**. Matching type/name yields candidate `[1]`, whose language 1033 matches the group but whose payload size is **48**. The saved `same_language_resource_index:1` and `size_matches:false` are byte-supported. Offset 924 is the low byte of this second record’s little-endian `declared_bytes` field (`30 00 00 00` → `2f 00 00 00`). Neither icon leaf nor its bytes changed.
- Independently derived `artifact` size 1536, SHA-256, `format:pe32-plus`, machine 34404, directory RVA/location 8192/[512,752), data-directory location [216,224), all six `directories`, all three complete `resources`, both `icon_groups` links and the `coverage` counts (`examined_entries:8`, `resources:3`) agree with saved `normalized_result`. The coverage label `complete` is bounded to this parseable resource tree, not other PE semantics.
- The saved receipt records command `npx -y rea-agents@6.4.0 inspect-pe-resources .../pe-r57/fixture.exe --format json`, exit code 0 and Evidence ID above; its fixture SHA matches the independently computed r57 digest. The SHA-256 of actual saved `inspection.raw.json` bytes is `5c915ebdc4c79a6d98e3b9f374e6e2e67168a1c5b391487ac80bd8e199d34fc8`, equal to the receipt’s `stdout_sha256`. The raw result's `subject.digest` and `normalized_result.artifact.sha256` both match r57. Fixture truth files' SHA/size/diff/expected IDs/candidates/language/size predicates agree with this independent inspection.

## INFERENCE / UNKNOWN / verdict
**INFERENCE:** This controlled one-byte r55→r57 mutation isolates the second group-image declared-size mismatch while retaining both icon candidates and their same-language links. No alternate changed byte was found across the 1536-byte fixture.

**UNKNOWN:** No image decoding, shell selection/loading, PE execution, or dynamic language fallback was observed; the reported `same_language_resource_index` is a static table relationship. The receipt plus saved-stdout hash checks consistency of **saved artifacts**, not independent attestation that the named CLI/version truly ran; no producer rerun was authorized. `coverage.status:complete` cannot establish completeness outside this bounded resource tree or guarantee general parser correctness on other PEs.

**Bounded verdict: PASS** for the stated static fixture claim and all three leaves/two links in saved `normalized_result`. No unsupported runtime claim is accepted. Evidence ID above identifies the producer record, corroborated by the independent fixture-byte checks.
