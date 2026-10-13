# Round 31 — byte identity and proposed changed ranges

## Observed baseline

- Artifact: `.shokunin/revenger/corpus/fixtures/pe-r30/fixture.exe`; read-only inspection only, no target execution or REA call.
- `wc -c` equivalent: 1024 bytes. SHA-256: `b94d840aa7eb952474b30260bc70e092fb1db832b0aa1bc393936d8dc4ce661a` (Python `len(data)`, `hashlib.sha256(data).hexdigest()`). This matches `corpus/fixtures/pe-r30/truth.json`.
- Bytewise comparison with `pe-r29/fixture.exe` gives exactly one differing byte: file offset 552, `01 -> 02`; the r30 truth file records the same construction and baseline SHA. This is the established r30-vs-r29 relation, not a prediction about the new fixture.
- Header receipts: `e_lfanew` at `0x3c` is `0x40` (64); PE signature at 64; optional-header magic at 88 is `0x010b` (PE32). Resource data-directory entry at optional-header offset 96+16 (file offset 200) reads RVA `0x2000`, size `0x67` (103). The size field is file offsets `[204,208)`.
- Relevant existing resource bytes: root directory at file 512; its type-10 entry points to directory RVA `0x2018` (file 536). At 536 the sole name-ID entry is ID 2, child directory RVA `0x2030` (file 560); at 560 language ID 1036 points to data entry RVA `0x2048` (file 584). Data entry maps payload RVA `0x2058` to file offset 600, size 15. `data[600:615]` SHA-256 is `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`, matching truth. These are static byte/layout observations, not parser results.

## Proposed change ranges from r30 (declaration, not observed output)

The round-31 declaration proposes preserving the header except resource-directory size at `[204,208)`, and a two-resource tree using root 512, type directory 536, name directories 568/592, data entries 616/632, payloads 672/704. The existing tree/data/payload currently occupy overlapping portions of `[512,615)`; an implementation may rewrite that interval to encode the declared tree. The declared payload regions are distinct `[672,687)` and `[704,719)`. Thus the bounded expected changed union versus r30 is `[204,208)`, `[512,615)`, `[672,687)`, and `[704,719)`; ranges are proposals inferred from declared layout, not verified bytes. No specific payload values were supplied in the declaration inspected here; consult fixture truth when authored. Any other changed offsets should be explained against the eventual truth.

Scope boundary: this establishes baseline identity and a proposed byte-change envelope only. It does not establish that a new fixture exists, validate the proposed PE tree, predict or claim an `inspect-pe-resources` result, or imply execution/provider readiness.
