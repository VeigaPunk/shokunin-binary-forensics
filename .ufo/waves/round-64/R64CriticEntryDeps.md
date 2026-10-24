# R64CriticEntryDeps — derivation-DAG attack

## Axes and review boundary

Impacted axes: **coverage K (C1)**, **depth** (byte-derived technical claims), and **calibration** (independence/provenance wording). This review does not assess C2's verifier controls or issue admission/judgment.

**Dependency finding:** the proposed entry was unavailable at review time. Direct `read` of `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-64-firmware-region-byte-evidence.md:1-180` returned `Path ... not found`. A `glob` over `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/*round-64*;/tmp/revenger-r64-*` also exposed no candidate draft. Following the independent-leaf instruction, I did not wait for another seat. Consequently, neither a clean candidate DAG nor a circular candidate DAG is established.

## Strongest local counterexample: the old checker is not independent measurement

The available checker at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py` obtains `truth_regions` from truth.json (lines 59–62); takes each region's `offset` and `size` from that oracle (101–109); and decompresses `image_bytes[offset:offset + size]` (145–151). Its exact-end condition (149, 156–157) validates an oracle-supplied boundary; it does not discover the compressed length independently. Even its fixture path comes through `truth.image.path` (68–81).

**Counterexample to any proposed independence claim based solely on that checker:** its compressed-size dependency is `truth.json → size → byte slice → exact-end check`, not `fixture bytes → measured stream end → size → comparison with truth`. This is a static data-flow observation, not a mutant run and not an allegation that the absent entry actually reuses that path. The existing checker remains useful for its stated oracle-comparison purpose.

A contrasting local pattern is `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/generator.py:39-49`: `decode_member` feeds the whole suffix to a zlib decoder, requires EOF, and computes `len(image) - offset - len(decoder.unused_data)`. Its offsets still come from the author's `MEMBERS` declarations (52–57), so invoking that generator alone would not demonstrate independent offset discovery either.

## Available-value source map (not a candidate derivation receipt)

| Value | Available source and direction | What remains unavailable |
|---|---|---|
| Image size 2048 and SHA-256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json:28-31`; also asserted in the saved record; SHA repeated in receipt | Candidate's byte-only length/hash derivation |
| Member starts 512 and 1024; compressed lengths 79 and 90 | truth.json:40–64 and `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json:1` agree textually | Candidate's start discovery and measured stream consumption, without truth/record inputs |
| Member ends 591 and 1114; zero-padding spans `(0,512)`, `(591,433)`, `(1114,934)` as `(offset,size)` | truth.json:33–70; saved record reports only two zlib regions, not padding | Candidate's byte-derived complements and all-zero checks |
| Decompressed lengths 78 and 97; SHA-256 `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` and `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` | truth.json:41–44,57–60; plaintext expectations also occur in its build recipe | Candidate's decompression-derived lengths/digests; saved record supplies neither digest |
| Region signature, reported confidence 250, `size_basis=provider_reported_validation_unknown`, `coverage=signature_scan`, Binwalk 3.1.0 | inspection.json:1, raw provider output → normalized record | These are observation metadata, not independent byte-layout authorities |
| Command, exit 0, fixture SHA, stdout SHA `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9`, Evidence ID | `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/receipt.json:2-7`; Evidence ID is also asserted by inspection.json | Candidate's byte/hash/record comparisons; a receipt assertion is not independent layout measurement or authenticity proof |

All numeric/hash values above are transcribed from opened evidence, not independently recomputed by this seat. The saved record's own limitations explicitly separate signature matches/reported sizes from partition validity and runtime mappings.

## Smallest safe correction / required handoff

Provide the missing candidate artifact to a fresh review seat. Its readout should first produce the layout, lengths, decompressed digests, and padding checks from the explicitly selected fixture bytes, then load truth.json and the saved record only for comparison. Stream lengths must come from consumed suffix bytes/EOF, not oracle-sized slices. Preserve a visible direction of **record compared TO byte-derived results**, never byte boundaries sourced FROM record fields. Keep padding and decompressed digests identified as byte/oracle facts that the record itself does not report.

This is a fixable artifact/review dependency, not an established candidate defect or an acceptable quality-for-coverage tradeoff. `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md:23-30,51-55,108-111` still requires the actual entry and independent review; this report cannot substitute for those decisions. No production files were changed, no tests/counters/runtime were invoked, and no tools were installed or upgraded.

Report: .ufo/waves/round-64/R64CriticEntryDeps.md
