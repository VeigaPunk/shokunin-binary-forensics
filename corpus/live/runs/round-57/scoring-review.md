# Round 57 independent PE-resource scoring review

Evidence: REA `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07` (`inspection.raw.json`); producer receipt reports `npx -y rea-agents@6.4.0 inspect-pe-resources .../pe-r57/fixture.exe --format json`, exit 0. This review did **not** rerun REA or execute the target. It parsed the two fixture byte arrays independently with Python `struct`/`hashlib` before loading the saved REA result and receipt. Truth JSON was checked against those bytes, not treated as substitute evidence.

## Independent byte checks (actual Python REPL commands and output)

- `len(b55),len(b57),hashlib.sha256(b55).hexdigest(),hashlib.sha256(b57).hexdigest(),[(i,a,b) for i,(a,b) in enumerate(zip(b55,b57)) if a!=b]` → `1536, 1536, 41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b, 71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d, [(924, 48, 47)]`.
- `struct.unpack_from('<I',b57,0x3c)[0]` → `64` (`PE\0\0` at offset 64); machine `0x8664`, optional magic `0x20b`. `b57[216:224].hex(' ')` → `00 20 00 00 f0 00 00 00` (resource RVA `0x2000`, directory size 240). The `.rsrc` section maps RVA `0x2000` to file offset 512 (virtual/raw size 1024).
- Walked IMAGE_RESOURCE_DIRECTORY headers/entries and data entries from the mapped root, independently. Directory `(offset, length, named count, ID count)` → `(512,32,0,2), (544,32,0,2), (600,24,0,1), (624,24,0,1), (576,24,1,0), (648,24,0,1)`. Eight directory entries lead to precisely three leaves:

  | type/name/lang | entry offsets | data-entry offset | payload RVA / file offset / bytes | independently computed payload SHA-256 |
  |---|---|---:|---|---|
  | `3/1/1033` | `528,560,616` | 672 | `0x2100 / 768 / 48` | `d7aaca7bc7951c9249a7798838189374fa953d3def03aebb375ee731768e5003` |
  | `3/2/1033` | `528,568,640` | 688 | `0x2140 / 832 / 48` | `2f503cace29956c75acd5356de2f8fa98485b01edd654daf0f81a739b44c82ae` |
  | `14/A😀B!/1033` | `536,592,664` | 704 | `0x2180 / 896 / 34` | `78dc9a7dd2d08db459b2bf22958f72fd2d105b56f8c0a28e232a1864a299169c` |

- `b57[736:748].hex(' ')` → `05 00 41 00 3d d8 00 de 42 00 21 00`: length five UTF-16 code units, decoded `A😀B!`, exact REA `utf16le_hex` `41003dd800de42002100`.
- `b55[896:930].hex(' ')` → `00 00 01 00 02 00 01 01 00 00 01 00 20 00 30 00 00 00 01 00 02 02 00 00 01 00 20 00 30 00 00 00 02 00`; `b57[896:930].hex(' ')` → `00 00 01 00 02 00 01 01 00 00 01 00 20 00 30 00 00 00 01 00 02 02 00 00 01 00 20 00 2f 00 00 00 02 00`. Header is reserved=0, type=1, count=2. `struct.unpack_from('<BBBBHHIH',b57,902)` → `(1,1,0,0,1,32,48,1)`; at 916 → `(2,2,0,0,1,32,47,2)`. Thus group image records occupy offsets 902–915 and 916–929; byte 924 alone changes the second size from 48 to 47. IDs remain 1 and 2. Both RT_ICON payloads and their SHA-256 digests are unchanged.

## Comparison with saved REA finding

**OBSERVATION** — Evidence ID above identifies the correct 1536-byte r57 SHA-256 and records PE32+, machine 34404, six directories, eight entries, three leaf resources, and the three exact path/entry/data/payload locations and hashes in the table. The Unicode name is recovered without losing the surrogate pair. Raw headers independently yield zero directory characteristics/timestamps/versions and zero leaf code page/reserved values as returned; the scripted comparison of all directory fields and all listed leaf paths, offsets, RVAs, sizes and hashes printed `field discrepancies []`.

**OBSERVATION** — REA returns exactly one group containing two image descriptors. It records first image `resource_id:1`, `declared_bytes:48`, `candidate_resource_indices:[0]`, `same_language_resource_index:0`, `size_matches:true`; second image `resource_id:2`, `declared_bytes:47`, `candidate_resource_indices:[1]`, `same_language_resource_index:1`, `size_matches:false`. The independent resource tree has exactly one RT_ICON with each corresponding ID, both at language 1033, with 48-byte payloads. Therefore the two candidate links and both same-language picks are supported; **no false link** was found. The mismatch belongs **only** to image 2's declaration (47 ≠ 48), not an absent/changed icon payload. The r57 group payload hash differs from r55, as expected from the one changed byte.

**INFERENCE / bounded verdict** — Within this synthetic, readable PE resource tree, reported leaf-identity recall is **3/3**, leaf-identity precision **3/3**, group-descriptor recall/precision **2/2**, and unique candidate/same-language link precision and recall **2/2** against independently enumerated byte-grounded links. No missed leaf, invented leaf, extra group image, missing image or false candidate link was identified. The truth file's r55→r57 hypothesis is corroborated by the one-byte diff. These are local counts, not a claim of population-wide PE parser accuracy.

**UNKNOWN** — The RT_ICON payloads were not decoded or displayed, so valid icon rendering, requested dimensions versus actual image contents, Windows language fallback, shell selection/loading, and runtime behavior remain unobserved. Other payload semantics, other files or malformed-PE behavior are outside this comparison. REA explicitly limits candidate edges to static resource-table relationships; do not upgrade them to observed runtime references. The receipt's exit code and SHA fields describe the producer run but this review did not independently re-execute or authenticate that producer process.
