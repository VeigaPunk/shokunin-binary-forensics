# R64LabBlind — independent firmware-byte derivation

## Axes and scope

Axes: independence from the candidate; complete byte-layout accounting; agreement with the authored oracle; no fixture/source mutation.

Confidence: **high** for the byte-derived values and oracle correspondence below. Candidate/readout comparison remains unavailable because those artifacts were absent at the inspected paths. This is evidence, not a Q01–Q13 admission decision.

## Independence and method

I derived the values first from `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin` alone, using Python stdlib `pathlib`, `hashlib`, `itertools`, `json`, `sys`, and `zlib` in Eval. I had not read the author's readout script, any entry draft, or `truth.json` when that derivation completed. The required frozen contract itself disclosed the planned image size and member offsets; the derivation did **not** use those numbers as scan inputs.

The scan enumerated every byte equal to `0x78`, attempted `zlib.decompressobj()` at each position, required `decoder.eof`, and measured consumed bytes using `len(input_suffix) - len(decoder.unused_data)`. Independently, `itertools.groupby` enumerated maximal zero-byte runs. Python reported `3.14.8`; zlib runtime reported `1.3.2`. No REA/provider command, target execution, or filesystem extraction was used.

## Observed independent values

Image size: **2048 bytes**.

Image SHA-256: `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`.

The exhaustive `0x78` scan found **only offsets 512 and 1024**. Both produced complete zlib members; there were no rejected header candidates.

All ranges below are half-open, `[start, end)`.

| Region derived from bytes | Start | End | Size |
| --- | ---: | ---: | ---: |
| All-zero span outside members | 0 | 512 | 512 |
| Complete zlib member | 512 | 591 | 79 |
| All-zero span outside members | 591 | 1024 | 433 |
| Complete zlib member | 1024 | 1114 | 90 |
| All-zero span outside members | 1114 | 2048 | 934 |

The five regions account for all 2048 bytes: 1879 all-zero bytes outside members plus 169 compressed bytes.

**Important distinction:** all maximal zero-byte runs in the *whole image* are `[0,512)`, `[591,1024)`, `[1098,1099)`, and `[1114,2048)`. The isolated zero at offset **1098 lies inside the second compressed member**; it is not an additional padding region. Total zero bytes are therefore 1880, not 1879.

| Member offset | Compressed bytes | Decompressed bytes | Compressed SHA-256 | Decompressed SHA-256 |
| ---: | ---: | ---: | --- | --- |
| 512 | 79 | 78 | `bf3dd2e42d36324ae17e81c66cb5d699ac74b1a017628fcfb4302846b1c7c352` | `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` |
| 1024 | 90 | 97 | `8c32fdb048dc29f3f47dd1fb1c8fe53790d239309e340e03bd486d8722d424ff` | `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` |

Decompressed UTF-8 content at 512, including final newline:

```text
R63 inert synthetic diagnostic record
sensor=pressure
units=kPa
state=nominal
```

Decompressed UTF-8 content at 1024, including final newline:

```text
R63 inert synthetic component inventory
component=radio
revision=fixture-only
execution=disabled
```

## Post-derivation comparison and remaining dependency

Only after the independent values had been returned by Eval did I open `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json`.

Observed agreement:

- Image length and SHA-256 exactly match `truth.json:28-32`.
- All five ordered regions, offsets, sizes, zero-fill values, decompressed lengths, and decompressed SHA-256 values exactly match `truth.json:33-72`.
- Both complete payload strings exactly match `truth.json:13-23`.
- Every byte in each outside-member span was independently checked to equal zero.

The post-derivation stdlib comparison returned `true` for `image_size_matches`, `image_sha256_matches`, `ordered_region_fields_match`, `all_padding_regions_zero`, and `recipe_payloads_match`. **No disagreement with the oracle was found.** The compressed SHA-256 values above are additional independent observations; the oracle does not carry those fields.

The requested candidate/readout comparison could not yet be performed:

- Exact entry path `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-64-firmware-region-byte-evidence.md`: glob returned `Path not found`.
- Discovered candidate scratch directory `/tmp/revenger-r64-entry`: `read` returned `(empty directory)`.
- Narrow globs `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/*readout*` and `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/*firmware*`: returned no matching files.

These are bounded observations at inspection time, not claims that no draft exists anywhere. As instructed for an independent leaf, I did not wait for another seat. The remaining dependency is the candidate entry or readout output; no comparison with either is claimed.

## Evidence and limits

The first Eval call produced the image identity, both complete stream measurements and hashes, payload text, and all maximal zero runs before oracle access. A second Eval call compared that retained independent result with the subsequently opened oracle. The author's script was never opened or invoked. No exported code contract was analyzed, so LSP definition/reference tracing was not applicable.

This establishes correspondence for one authored inert fixture only. It does not establish vendor-image authenticity, provider completeness, general firmware layout rules, or execution behavior. No repository code, fixture, oracle, live record, Git/JJ state, or index was modified. Only this assigned report was written. No tools were installed or updated, and no build, verifier suite, formatter, or linter was run.

Report: .ufo/waves/round-64/R64LabBlind.md
