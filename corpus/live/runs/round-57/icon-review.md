# Round 57 independent icon-group review

## Boundary and evidence

- **Independent bytes first:** read `fixtures/pe-r55/fixture.exe` and `fixtures/pe-r57/fixture.exe` directly, parsed PE resource directory and group payload with Python `struct`, then read `fixtures/pe-r57/truth.json` and `live/runs/round-57/inspection.raw.json` / `receipt.json`. No target execution or producer rerun.
- **Evidence ID:** `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07` (`inspect_pe_resources`, r57); independent local byte observations below are grounded by the stated file SHA-256s, not a new REA Evidence ID. Receipt reports CLI `npx -y rea-agents@6.4.0 inspect-pe-resources /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r57/fixture.exe --format json`, exit 0, stdout SHA-256 `5c915ebdc4c79a6d98e3b9f374e6e2e67168a1c5b391487ac80bd8e199d34fc8`.

## Actual independent Python commands and output (abbreviated only where stated)

```python
from pathlib import Path
import hashlib, struct
p = Path('.shokunin/revenger/corpus/fixtures')
a, b = (p/x/'fixture.exe').read_bytes() for x in ('pe-r55', 'pe-r57')
print([(len(x),hashlib.sha256(x).hexdigest()) for x in (a,b)])
print([(i,a[i],b[i]) for i in range(len(a)) if a[i]!=b[i]])
```

```text
[(1536, '41c0132a9ecd8274d9afcfc079fefc0c5beb14c1ae81bc7bfa0a2832e140572b'), (1536, '71d11fba01d4daa040e04e649a70c39bcdb475ce2e0a2801f6171a325db0494d')]
[(924, 48, 47)]
```

Parsed PE32+ `.rsrc` RVA `8192` to file offset `512`. Walked type/name/language directories, including UTF-16LE named group (`41003dd800de42002100` -> `A😀B!`), and data-entry RVA-to-file offsets. Both files contain ordered resources: index 0 `RT_ICON` ID 1 language 1033, payload offset 768 length 48; index 1 `RT_ICON` ID 2 language 1033, payload offset 832 length 48; index 2 `RT_GROUP_ICON` name `A😀B!` language 1033, payload offset 896 length 34. The group header `struct.unpack_from('<HHH', payload, 0)` returns `(0, 1, 2)`; two packed `GRPICONDIRENTRY`s are read in order with `struct.unpack_from('<BBBBHHIH', payload, 6 + 14*index)`.

```text
pe-r55 group header (0, 1, 2)
entry 0 offset 902 tuple (1, 1, 0, 0, 1, 32, 48, 1) candidates [0] same_language [0] size_matches [True]
entry 1 offset 916 tuple (2, 2, 0, 0, 1, 32, 48, 2) candidates [1] same_language [1] size_matches [True]
pe-r57 group header (0, 1, 2)
entry 0 offset 902 tuple (1, 1, 0, 0, 1, 32, 48, 1) candidates [0] same_language [0] size_matches [True]
entry 1 offset 916 tuple (2, 2, 0, 0, 1, 32, 47, 2) candidates [1] same_language [1] size_matches [False]
r55 versus r57 resource payload equality [((3, 1, 1033), True), ((3, 2, 1033), True), ((14, 'A😀B!', 1033), False)]
```

Candidate indices above are assigned by exact numeric `RT_ICON` name equal to group `resource_id`; same-language index additionally requires language 1033. The `dwBytesInRes` field of second entry starts at file offset **924**; its low byte changes `0x30` to `0x2f`. Width/height respectively 1×1 and 2×2; planes 1 and bit depth 32 on both entries. Both icon payloads are byte-identical across versions.

## Saved-result comparison and verdict

- **OBSERVATION:** `truth.json` names exactly offset 924 and expects indices `[0]`, `[1]`, same-language indices 0, 1, and only second r57 `size_matches:false`. The independent parse agrees. The saved `inspection.raw.json` normalized result under Evidence ID `ev_068eb9b682385b760251b6d23ba70680ec57b0e55b95ce242921a3f021e1cd07` reports precisely two images at offsets 902 and 916, declared lengths 48 and 47, IDs 1 and 2, candidate indices `[0]` and `[1]`, same-language indices 0 and 1, and matches `true` and `false`. The receipt cites this same ID and successful command exit.
- **INFERENCE:** The one-byte mutation changes only the second group-image declared length; it does not remove a candidate, change the language match, or modify either RT_ICON payload. `size_matches:false` is a static comparison of declared group size 47 with matching RT_ICON data-entry size 48, not evidence of image corruption or load failure.
- **UNKNOWN:** Actual image decoding, OS language fallback, shell/window icon selection, and runtime handling of this mismatch were not tested. Opaque RT_ICON payloads were not independently decoded. The saved result's `coverage.status=complete` is limited to its static resource-table inventory (three resources, eight examined entries), not runtime coverage.

**Bounded verdict:** PASS for the stated static regression claim on these two 1,536-byte fixture files and the saved r57 REA result. No broader PE-resource implementation or runtime behavior is established.
