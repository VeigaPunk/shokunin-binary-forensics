# R64CriticFixture — fixture/oracle framing attack

Seat: `revenger-r64.R64CriticFixture`. Review only: no admission, round judgment, integration, or production edits.

## Axes and evidence boundary

- **Coverage K:** whether C07 denotes the narrow authored-fixture correspondence actually demonstrated.
- **Depth:** byte-derived layout versus oracle labels/recipe metadata.
- **Calibration:** scanner/manual attribution, oracle independence, and provenance limits.
- **Operability:** what the cited checker actually verifies.

Frozen authority: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md:18-55,108-123`. The counter and baseline receipt were read; no counter or runtime was invoked by this critic.

**Candidate dependency:** discovery found no target entry under `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/`; direct read of the author-designated `/tmp/revenger-r64-entry/candidate.md` returned `Path ... not found`. Therefore this report cannot quote or clear the entry's actual sentences. The author subsequently described intended qualifiers by message; intentions are not an inspected artifact. Required sentence wording is supplied below rather than invented quotations.

## 1. Two truth.json states can satisfy the checker

**Counterexample [INFERENCE, static control-flow proof; not an executed mutant]:** retain the saved image, image identity, regions, and record, but replace `build_recipe.members[0].payload_utf8` with a contradictory string. The checker never reads `build_recipe`, so every tested condition and the error list are unchanged. Renaming `regions[1].name` likewise changes only the printed display label (`oracle_check.py:214,220`), not acceptance. Thus `ORACLE OK` cannot establish the recipe or member-label truth.

A stronger structural variant replaces the first padding region `(offset=0,size=512,fill_hex=00)` with two padding regions `(0,256,00)` and `(256,256,00)`. Both filler comparisons succeed; the sorted spans remain contiguous; both zlib regions and their cardinality remain unchanged. The accepted JSON need not contain exactly five regions or three maximal padding spans. This is a different oracle description of the same physical bytes, not evidence for a second physical image.

**Evidence:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py:59-96,101-168,170-208,210-225` checks image identity, declared filler bytes, exact compressed EOF/content, contiguous coverage, and the reported non-padding tuples. It neither canonicalizes padding nor validates recipe metadata. `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/oracle-rerun.log:6-13` records the other seat's unmodified baseline `ORACLE OK`, exit 0; this is not my execution.

**Strongest physical-identity alternative is already addressed:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63CriticFixture.md:16-31` records an exercised alternate image with the first 512 bytes changed to `ff`; the same saved record was rejected on `subject.digest.sha256`. Current checker lines 88-96 contain the digest/length binding. Do not reopen this as an unfixed identity defect or infer cryptographic uniqueness beyond that binding.

**Impacted axes:** depth, calibration, operability; coverage K only if these checks are overstated as broader knowledge.

**Smallest safe correction:** state that the checker compares the specified byte/record fields, not that it authenticates a unique/canonical oracle or validates `build_recipe`. Call member names **recorded oracle labels**, never byte-derived names: zlib streams do not carry those labels. Derive maximal padding spans independently in the entry if claiming maximality. Preserve the existing fixture/checker bytes; no new checker capability is needed for the frozen claim.

**Defect versus tradeoff:** non-unique equivalent descriptions are not a defect in a field-correspondence checker. Crediting it with recipe authenticity, canonical segmentation, or independent authorship would be a fixable claim-attribution defect. A broad firmware claim bought with that calibration loss would be a coverage-for-calibration trade for the canonical judge, not a no-harm improvement.

## 2. Only two regions belong to the saved signature-scan observation

**Evidence:** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json` reports only `(offset=512,reported_size=79,signature=zlib)` and `(1024,90,zlib)`, with Binwalk `3.1.0`, `coverage=signature_scan`, and `size_basis=provider_reported_validation_unknown`. Its execution arguments include `--search-all`; `Analysis.extractions` is `{}`. The saved region objects contain neither padding spans, decompressed hashes/sizes, nor member names.

`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-63.md:218` records M33: default nonzero-offset zlib detection differs from `--search-all`; a format name or a magic-looking header is not a detectability proof. `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/LEDGER.md:39,46-56` already separates padding/manual decompression from scanner findings, records unblob finding zero chunks on this whole image, and excludes device-level conclusions.

The pinned guide snapshot `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md:91-95` says reported sizes preserve Binwalk output and can be inferred; signatures/confidence do not prove partitions or runtime behavior. I read the local snapshot, not a fresh upstream fetch.

**Smallest safe correction:** identify the engine, version, function, scan mode, and exact fixture whenever attributing discovery. Attribute padding and decompression to manual byte analysis. Say the measured compressed lengths agree with reported sizes here, not that Binwalk generally validates them.

## 3. Exact sentence roles requiring qualifiers

These are suggested entry sentences, **not quotations from an available candidate**:

| Entry location / role | Suggested wording |
|---|---|
| Opening scope, immediately after C07 identification | “Here ‘firmware’ names coverage row C07 and the `inspect_firmware_regions` route; the input is one authored inert 2048-byte image of zero padding and two zlib-wrapped text members, not an identified vendor firmware format or device image.” |
| Layout table lead-in | “This table is a manual byte-derived layout; its three zero-padding spans are not Binwalk findings. Member names are recorded oracle labels.” |
| Saved-record observation | “The saved Binwalk 3.1.0 `--search-all` signature scan reports two zlib regions, at byte offsets 512 and 1024, with reported sizes 79 and 90; it reports no padding regions or decompressed-member digests.” |
| Size/digest comparison | “Manual EOF-based decompression measures compressed lengths 79 and 90 and derives inflated sizes/digests; those results are compared with truth.json, while only offsets, reported sizes and signatures are compared with the saved region fields.” |
| Oracle/recheck interpretation | “The checker validates the specified image/region correspondence; it does not prove a unique truth.json representation, the build recipe, independent oracle authorship, producer origin, or authenticity.” |
| Conclusion / coverage statement | “This establishes correspondence for these authored bytes and this saved signature-scan record only; it establishes no extraction, execution, partition validity, general firmware-format coverage, or provider completeness.” |

These qualifiers preserve the frozen C1 scope rather than introducing another claim. The unchanged Q03/Q04/Q09/Q10/Q11/Q13 criteria are relevant; this critic supplies no per-criterion admission decisions.

## 4. Available readout draft concern

The source snapshot I read at `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/firmware-readout.py:10,20-32,60-70` used `EXPECTED_MEMBER_OFFSETS=(512,1024)` and checked those positions. That verifies expected locations but does not discover them independently. Its `zero_spans` also labels all zero-byte runs as padding without first excluding compressed-member interiors. I did not execute this draft or establish that this particular fixture has interior zero runs.

**Smallest safe correction:** discover candidate starts from bytes before comparison; define padding as zero-checked complements of measured member extents, or explicitly restrict the prose to expected-position verification rather than exhaustive discovery. This draft concern was sent directly to its owner. It is not a finding against an uninspected final entry, and no later correction is assumed.

## Post-review owner notice

After this report was first delivered, `revenger-r64.R64FirmwareReadout` reported that `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/firmware-readout.py` now scans all byte offsets and excludes measured zlib extents from padding; its output is `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/firmware-readout.out`. Section 4 records the earlier inspected snapshot, not a claim that the owner-reported correction is absent. I did not re-audit or execute the later version; independent final verification remains with the assigned reviewers/integrator.

## Candidate now available — first text review addendum

The author subsequently supplied `/tmp/revenger-r64-entry/candidate.md`; I inspected its scope, correspondence, limitations and criterion-map sentences (read snapshot `D753`, 455 lines). This resolves the earlier **text-availability** dependency only. No commands or printed outputs were executed or independently verified by this critic.

The actual draft now carries the main requested qualifiers:

- Lines 10 and 157 expressly make “firmware” the C07 coverage label, not a real family/format identification.
- Lines 17 and 158 define padding as maximal zero runs **outside** measured member ranges. Line 17 also discloses the internal zero byte at 1098; this is the draft's claim, not my byte measurement.
- Line 89 explicitly calls member names recorded oracle/generator labels, not byte-derived values.
- Lines 125 and 160 attribute the two zlib matches to the saved Binwalk 3.1.0 `--search-all` scan, exclude padding/inflated digests from record fields, and retain the unknown-size-validation qualification.
- Lines 127 and 159 deny canonicity, uniqueness, authenticity, and general firmware conclusions.

**Remaining exact sentence corrections (depth/calibration; sent to the author):**

1. **Line 5:** “The C07 row also names the REA `extract_firmware` route and firmware families…” is not true of the inspected README row 36 (`| C07 | firmware images | — | — | frontier |`). Suggested replacement: “This entry does not cover `extract_firmware`, vendor/device images, container formats, or other firmware fixtures.” Do not inflate the coverage row's actual contents.
2. **Line 179:** “The independent oracle `truth.json`…” should be “The authored oracle `truth.json`…; the manual readout is independent of the saved record.” The same generator authored image and oracle; independent record comparison is not independent oracle authorship.
3. **Line 123:** “the agreement is complete for every field both documents can express” should be “the 25 selected comparisons match.” The checker and readout compare a selected field set, not every expressible recipe/identity/interpretation claim; the ignored-recipe counterexample above remains relevant to that distinction.
4. **Lines 10, 125 and 127:** affirmative historical production language (“produced by”, “were produced independently”, “was produced on a private workspace copy”) is stronger than the saved-byte evidence alone. Suggested wording: “The saved record attributes the scan to Binwalk 3.1.0 with `--search-all` and names a private workspace copy; the manual readout independently derives the compared byte values. Receipt/digest consistency does not independently authenticate that historical invocation.” This keeps the existing no-authenticity disclaimer aligned with the affirmative sentences.

These are small, fixable framing corrections, not a request to alter preserved inputs or add capability. This first text review supplies no Q01–Q13 admission decision, no claim verdict, and no judgment of any later draft.

## Final owner-reported disposition

After the first text review, `revenger-r64.R64EntryC07` reported applying all four wording corrections to `/tmp/revenger-r64-entry/candidate.md` (reported SHA-256 `e86a5b1c9f382c186818fe55c78eed1537aa907151853e81f6aef80d4ff86cc9`), with the embedded script unchanged and the same reported stdout digest. This is the author's disposition, not a second review or independently exercised verification. The earlier availability blocker is resolved; final artifact verification and admission remain with their assigned owners.

## Tooling and scope

Only this assigned report was written. No production/fixture/saved-record changes; no git/jj mutations; no runtime, scanner, test, build, counter, or canonical judge invoked; no tools installed or upgraded; no scratch created. Outstanding evidence dependency is the actual candidate text and its independent admission reviews, not access to the existing fixture/oracle sources.

Report: .ufo/waves/round-64/R64CriticFixture.md
