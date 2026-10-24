# R64ScoutRecon — C1 fixture/saved-record recon

## Axes and scope

Axes: evidence fidelity; usefulness for the entry's correspondence section; preservation of observation/inference/unknown boundaries. Assigned recon is complete. Confidence is **high** for the current file inventory, hashes, saved JSON fields and literal checker behavior; historical execution claims below are attributed to the ledger, not newly reproduced.

Read the frozen round contract, relevant frozen-counter sections and red-before receipt. Inspected only the named fixture/run evidence and bounded checker references. No production edits, git/jj operations, payload execution, REA invocation, oracle/test run or tool installation. No scratch created.

## Inventory — observed current files

Both directory listings were flat and complete: three fixture files and six saved-run files. Exact byte sizes came from `stat --printf`; digests came from `sha256sum` over the absolute directory globs.

| Absolute path | Bytes | SHA-256 |
|---|---:|---|
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin` | 2048 | `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/generator.py` | 5532 | `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4` |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json` | 1933 | `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md` | 22671 | `25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6` |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json` | 3904 | `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py` | 11034 | `d0dfd7a1cd105485e47bf52446056a2636fb803c05a404ce56da597f36ce0512` |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/receipt.json` | 492 | `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stderr.txt` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw` | 3904 | `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` |

`cmp --silent /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/stdout.raw` succeeded with no output: the retained JSON and stdout are byte-identical. The observed receipt digest ends **`5c6b94d`**, matching the corrected pin in LEDGER line 26, not the historical erroneous `5c6b94b`.

## Directly usable correspondence evidence

Sources: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/truth.json:28-72`; `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json` JSON fields; `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/receipt.json:2-7`.

- Current image SHA-256 and size equal `truth.image.sha256` / `truth.image.size`, the record's `subject.digest.sha256` / `normalized_result.input_size`, and the receipt's `fixture_sha256` (digest only there).
- The record's Evidence ID is `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`; the receipt repeats it. Its `stdout_sha256` equals the measured hash of both retained stdout and inspection JSON. These are **internal consistency observations**, not authenticated producer origin.
- Record `operation=inspect_firmware_regions`, `provider.id=binwalk`, `provider.version=3.1.0`, `coverage=signature_scan`; engine worker count is 1 and source revision is null. Saved engine executable digest: `5fc19aac1f357a66a47e8b20a8038a84cb93971cb5d331bd4503b02fcc0a40d6` (not a fresh measurement of the host executable).
- Receipt command names **REA CLI 6.5.0**: `npx -y rea-agents@6.5.0 inspect-firmware-regions /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin --format json`. CLI version is from the receipt command, not the provider version. Producer exit 0 and duration 1.296587134 seconds are saved receipt fields, not an invocation by this scout.

All ranges below are half-open. Padding and decompressed fields are **oracle declarations**, not fields emitted by the saved scanner record. This scout did not independently decompress the image or recheck the padding bytes.

| Truth region | Byte range | Compressed/padding bytes | Saved record comparison | Truth plaintext bytes / SHA-256 |
|---|---|---:|---|---|
| padding, fill `00` | `[0,512)` | 512 | Not reported by the signature scan | n/a |
| `diagnostic-note`, zlib | `[512,591)` | 79 | offset 512, reported_size 79, signature zlib: equal to truth | 78 / `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` |
| padding, fill `00` | `[591,1024)` | 433 | Not reported by the signature scan | n/a |
| `component-note`, zlib | `[1024,1114)` | 90 | offset 1024, reported_size 90, signature zlib: equal to truth | 97 / `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` |
| padding, fill `00` | `[1114,2048)` | 934 | Not reported by the signature scan | n/a |

The normalized record contains exactly two regions, each with `provider_id`, `offset`, `reported_size`, `signature`, `description`, `reported_confidence=250`, and `size_basis=provider_reported_validation_unknown`. It contains **no member name or decompressed digest/length**. The entry must derive decompressed digests from fixture byte windows before comparing to truth; it must not say REA emitted them. Exact size agreement on this image does not upgrade the provider's size-validation claim. No probability interpretation of confidence 250 is established here.

`raw_result.report[0].Analysis.extractions={}`; normalized result has only `engine`, `input_size`, `regions`, `coverage`, with no `extraction_gaps`. This is saved inspection evidence, not an extraction or execution receipt.

## LEDGER headings and required epistemic layers

Source: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md`.

Headings: line 1 `Round 63 — firmware region inspection ledger (authored inert fixture)`; line 11 `Fixture and route`; line 30 `Ledger`; line 58 `Score and limitations — what the F counter can and cannot see`; line 102 `Verification commands run by the ledger author (read-only)`.

- **OBSERVATION, O1–O9 (lines 34–42):** saved metadata, digest/size, two zlib regions, truth comparisons, three declared padding spans, empty extraction, provider limitations, and receipt consistency. O4–O6's byte/decompression confirmations are the ledger author's recorded checks; only the field values and current whole-file hashes were independently read/measured by this scout.
- **Historical checks, O10–O11 (lines 43–44):** ledger reports a separate byte recomputation plus `oracle_check.py` yielding `ORACLE OK`, exit 0. It also reports a separate unblob 26.6.4 probe: zero chunks on the complete image; one zlib chunk and a truth-matching 78-byte plaintext when the first 79-byte member was isolated. Those unblob outputs were scratch artifacts, not files in this inventory; line 118–119 says that scratch was removed. Treat these as attributed ledger observations, not freshly inspected scanner outputs or part of the REA record.
- **INFERENCE, I1–I6 (lines 45–50):** 2/2 fixture-specific reported-vs-authored member agreement, digest correspondence being checker-side rather than a record field, exact size coincidence without general validation, static/non-runtime scope, engine-dependent discovery, and F being saved-record presence. Do not generalize beyond this fixture/route/version.
- **UNKNOWN, U1–U6 (lines 51–56):** other signature families, extraction completeness, scan depth/nested candidates, authenticated producer provenance/reproducibility, independent oracle derivation, and anything about a real device/vendor image/boot/hardware remain unresolved.

Narrow wording trap: LEDGER line 24 says unblob appears nowhere in the record, citing a lowercase text search. The actual record **does mention `Unblob` in generic limitations**, but its provider and execution are binwalk only. Reuse the bounded conclusion “unblob was not the saved producer,” not the stronger literal absence wording. Likewise, O11's standalone unblob extraction must not be attributed to REA.

The entry should preserve the contract's authored-bytes ↔ saved-record scope. `authority=shipped-artifact` is merely an observed envelope value; it does not turn the authored fixture into a vendor artifact or authenticate the record.

## `oracle_check.py` — literal source behavior, not a fresh run

Source: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py`.

- `load_json` (15–21) accumulates file/decode errors; `integer` (24–25) excludes booleans; `mismatch` (28–29) appends diagnostics.
- `main` (32–39) accepts `--record` and `--truth`. Defaults (10–12) are anchored to the checker location; a relative image path resolves against the truth file's parent (73–81), not cwd.
- Identity/shape checks (46–96): operation exactly `inspect_firmware_regions`; subject SHA string; normalized result object; truth/record region arrays; readable image; declared image size/hash equal actual bytes; record subject hash and normalized input size equal actual image.
- Truth-region byte checks (100–168): objects, integer offsets, positive integer sizes, in-bounds spans; padding bytes equal repeated declared fill; zlib/gzip regions decompress; stream ends exactly at declared compressed size (`eof` and no unused data or unconsumed tail); decompressed SHA-256 and length equal truth. Unsupported kinds fail. The decompression window is the **truth** offset/size; record agreement is checked separately below.
- Partition coverage (170–177): sorted truth spans must be contiguous from zero and end at the image length, rejecting gaps/overlap through the expected-start comparison.
- Record matching (179–208): sort reportable truth regions and record regions by offset; equal count; compare each paired offset, `reported_size`, and `signature` exactly. Padding is deliberately not reportable.
- Diagnostics/exit (210–229): prints a `REGION` line per truth region, each `MISMATCH`, then `ORACLE OK` or `ORACLE MISMATCH`; returns 0 or 1, with the module's direct-execution guard calling `main()`.

This checker **does not check** receipt command/exit/stdout binding, Evidence-ID authenticity or binding, provider/version/engine hash, `coverage`, confidence/size-basis semantics, or consistency of `raw_result.file_map` with normalized regions. Use the separately inspected receipt/record fields for internal correspondence, never call those oracle-checked properties.

Semantic-tool availability: `read xd://lsp` returned “No such tool: xd://lsp”; mounted devices were only `ast_edit` and `debug`. No LSP server interface was available to query or warm up. The source summary above is literal text/source evidence, **not semantic reference proof**. Bounded text-reference search over the fixture/run directories and round-63/64 reports found the checker's documented invocation in LEDGER line 110; direct entry is visible at source lines 228–229. No exported-library call graph is claimed.

## Counting and remaining gaps

`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py:25-49` counts held/backed knowledge paths, not entry quality; lines 55–78 compare frontier tokens with saved operation presence; lines 80–97 count F family presence. `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure-before.log:1-10` records K 7/14, C07 frontier, one C07 legend mismatch, F 5/8 and one firmware record. Those are frozen historical receipt values, not a new probe run by this seat.

All required artifacts were present. No prerequisite blocks the entry's local correspondence section. The entry still needs its own byte-derived commands and independent Q01–Q13 admission evidence. **This recon read truth and saved results before any derivation, so it is not Q03 blind independence and makes no admission verdict.** The historical provenance, broader-provider/extraction/runtime and device-level unknowns remain as documented above.

Tool installs/updates: none.
