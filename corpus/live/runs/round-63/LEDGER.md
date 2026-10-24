# Round 63 — firmware region inspection ledger (authored inert fixture)

Scope: the saved REA record `corpus/live/runs/round-63/inspection.json` (Evidence
`ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`) against the
authored byte oracle `corpus/fixtures/firmware-r63/truth.json`. Every row below is
classed OBSERVATION (read from saved bytes or a saved field), INFERENCE (bounded
interpretation of those bytes) or UNKNOWN (not answerable from this record). No
firmware payload was executed; the fixture is inert authored bytes with two
zlib-wrapped text records and explicit zero padding.

## Fixture and route

| Item | Value | Where observed |
|---|---|---|
| Fixture image | `corpus/fixtures/firmware-r63/firmware-r63.bin`, 2048 bytes, SHA-256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` | `truth.json` `image`; re-hashed by the ledger author from the file on disk |
| Generator | `corpus/fixtures/firmware-r63/generator.py`, SHA-256 `4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4`; recipe `python3 -B generator.py` | file on disk; `truth.json` `build_recipe` |
| Generator parameters | image 2048 B, padding byte `00`, RFC 1950 zlib level 9, Python `3.14.8`, zlib compile/runtime `1.3.2`, members at offsets 512 and 1024 | `truth.json` `build_recipe` |
| Truth oracle | `corpus/fixtures/firmware-r63/truth.json`, SHA-256 `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` | file on disk |
| REA command line (verbatim) | `npx -y rea-agents@6.5.0 inspect-firmware-regions /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin --format json` | `receipt.json` `command` |
| Producer exit | exit code `0`, duration `1.296587134` s | `receipt.json` `exit_code`, `duration_seconds` |
| Provider id/version (record envelope) | `provider.id` = `binwalk`, `provider.name` = `Binwalk`, `provider.version` = `3.1.0`; `normalized_result.engine.name` = `binwalk`, `engine.version` = `3.1.0`, `engine.executable_path` = `/usr/bin/binwalk`, `engine.executable_sha256` = `5fc19aac1f357a66a47e8b20a8038a84cb93971cb5d331bd4503b02fcc0a40d6`, `engine.source_revision` = `null`, `engine.worker_count` = `1` | `inspection.json` `provider`, `normalized_result.engine` |
| REA CLI version | `rea-agents` `6.5.0` — from the receipt command line, **not** from the record envelope (the envelope names the binwalk provider, not the REA CLI) | `receipt.json` `command`; package `package.json` of the cached `rea-agents@6.5.0` |
| binwalk version probe | `binwalk 3.1.0` at `/usr/bin/binwalk`, executable SHA-256 `5fc19aac1f357a66a47e8b20a8038a84cb93971cb5d331bd4503b02fcc0a40d6` — equals the envelope's `engine.executable_sha256`; probe timestamps `2026-10-24T02:22:40Z` and `2026-10-24T02:24:44Z` (host clock, UTC) | ledger author's shell probe; `binwalk --version`; `sha256sum /usr/bin/binwalk` |
| unblob version probe | `26.6.4` at `/home/vgpnk/.local/bin/unblob`, executable SHA-256 `0ce7b624f540c2191ff144892584997fe3fb6ab28ab6ef6b88639f8a7cba1d09`; probe timestamp `2026-10-24T02:24:44Z` (host clock, UTC). **Unblob was not invoked by the REA producer run** — it appears nowhere in the record (`grep -c unblob inspection.json` = 0) and the provider is binwalk only. The version line is therefore host-tooling context (the REA firmware route names Binwalk 3.1.x and Unblob 26.6.x), not part of the record's route; the ledger author invoked unblob separately as an independent cross-check (row O11). | ledger author's shell probe; `unblob --version`; `sha256sum ~/.local/bin/unblob` |
| Engine invocation inside the record | `raw_result.execution.command` = `/usr/bin/binwalk`, args `--quiet --search-all --threads 1 --log /tmp/rea-firmware-7rPoLl/report.json /tmp/rea-firmware-7rPoLl/firmware.bin`, exit `0`, signal `null`, resource limiter `/usr/bin/prlimit`; `version_execution` exit `0`, stdout `binwalk 3.1.0\n` | `inspection.json` `raw_result.execution`, `raw_result.version_execution` |
| Receipt | `corpus/live/runs/round-63/receipt.json`, SHA-256 `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` (pin corrected 2026-10-24: the pre-correction pin ended `5c6b94b`, one hex char off the bytes at every commit since landing — defect found by `W2AttackRecordForgery`); `fixture_sha256` = `bdfe9f46…`, `stdout_sha256` = `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9`, `evidence_id` = `ev_aae7529f…` | file on disk |
| Saved stdout | `stdout.raw` SHA-256 `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` — byte-identical to `inspection.json` (same SHA-256, 3904 bytes); `stderr.txt` is 0 bytes (SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`) | file on disk |
| Checker | `corpus/live/runs/round-63/oracle_check.py` (SHA-256 at the time of the check below: `d0dfd7a1cd105485e47bf52446056a2636fb803c05a404ce56da597f36ce0512`; the file was still being edited by its author and its digest changed during this round, so it is cited by path and behaviour, not by a pinned digest) | file on disk |

## Ledger

| # | Class | Statement | Basis | Result |
|---|---|---|---|---|
| O1 | OBSERVATION | The saved record carries Evidence ID `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`, `operation` = `inspect_firmware_regions`, `predicate_type` = `rea.analysis`, `confidence` = `observed`, `authority` = `shipped-artifact`, `environment` = `null`, `relationship_coverage` = `null`, `evidence_links` = `[]`, `analysis_profile` = `null`. | `inspection.json` top-level fields | Fields as saved |
| O2 | OBSERVATION | The record's subject digest is the fixture: `subject.digest.sha256` = `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`, `subject.name` = `firmware-r63.bin`, `subject.local_path` = the fixture path, `subject.format` = `file`, `subject.architecture` = `null`; `normalized_result.input_size` = `2048`; `locations` = one `file-offset-range` 0–2048. | `inspection.json` `subject`, `normalized_result.input_size`, `locations` | Digest equals the fixture SHA-256 re-hashed from disk; input size equals the fixture size |
| O3 | OBSERVATION | The record reports **exactly two** regions, both `signature` = `zlib`. Region 1: `provider_id` `2b2ce3b4-3c1d-4ee4-86de-e97fb12ec0fd`, `offset` `512`, `reported_size` `79`, `reported_confidence` `250`, `description` "Zlib compressed file, total size: 79 bytes", `size_basis` `provider_reported_validation_unknown`. Region 2: `provider_id` `d9281d07-8c6b-49a3-968c-b971e2dfa9fc`, `offset` `1024`, `reported_size` `90`, `reported_confidence` `250`, `description` "Zlib compressed file, total size: 90 bytes", `size_basis` `provider_reported_validation_unknown`. | `inspection.json` `normalized_result.regions` | Two regions, no third |
| O4 | OBSERVATION | Region 1 compared against the authored truth: truth region `offset` `512`, `size` `79`, `kind` `zlib`, `decompressed_member.sha256` `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86`, `decompressed_member.size` `78`. Offset agrees, size agrees, decompressed digest agrees, decompressed length agrees. | `truth.json` `regions[1]` vs record region 1 | offset OK · size OK · decompressed sha256 OK · decompressed size OK |
| O5 | OBSERVATION | Region 2 compared against the authored truth: truth region `offset` `1024`, `size` `90`, `kind` `zlib`, `decompressed_member.sha256` `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9`, `decompressed_member.size` `97`. Offset agrees, size agrees, decompressed digest agrees, decompressed length agrees. | `truth.json` `regions[3]` vs record region 2 | offset OK · size OK · decompressed sha256 OK · decompressed size OK |
| O6 | OBSERVATION | The truth oracle declares five regions in total; the three that the record does **not** report are `kind` `padding` fillers (`offset` 0 size 512, `offset` 591 size 433, `offset` 1114 size 934, fill `00`). The record's `coverage` is `signature_scan` and it carries no padding region. Padding bytes were independently checked to be all-zero at those spans. | `truth.json` `regions`; `inspection.json` `normalized_result.coverage`; `oracle_check.py` output `record=not-expected padding=OK` for all three | Padding is not a reportable signature region; 0 false positives from the record |
| O7 | OBSERVATION | The record performed **no extraction**: `raw_result.report[0].Analysis.extractions` = `{}`; `normalized_result` has no `extraction_gaps` key (keys are exactly `engine`, `input_size`, `regions`, `coverage`). | `inspection.json` | No extraction, no gap list |
| O8 | OBSERVATION | The record's own limitations include: signature matches and reported sizes do not establish partition validity, encryption or runtime mappings; "Binwalk may infer unknown lengths before emitting its report"; only Linux supported; one worker; unblob's default sandbox and skip rules remain enabled; missing external extractors / unknown chunks / encrypted chunks / depth limits yield partial coverage; extracted code is never executed; a listed gap does not mean the target is corrupt; the launcher executable is hashed but interpreter, shared libraries and installed Python package dependencies are not independently attested, and source revision remains unknown for caller-supplied builds. | `inspection.json` `limitations` | Provider-declared limits, quoted in substance |
| O9 | OBSERVATION | The producer run is internally consistent: receipt `stdout_sha256` = `f6997835…` equals the SHA-256 of both saved `stdout.raw` and `inspection.json`; receipt `fixture_sha256` = `bdfe9f46…` equals the fixture and the record's subject digest; receipt `evidence_id` equals the record's `evidence_id`; producer exit `0`; stderr empty. | `receipt.json` vs `inspection.json` vs files on disk | All five cross-checks agree |
| O10 | OBSERVATION | Two independent checks of record-vs-truth agreement were run and both pass: (a) the ledger author's own recomputation from the fixture bytes — for each record region, `zlib.decompressobj` over `image[offset:offset+reported_size]` yields the truth digest and length (2/2), and the image SHA-256 and size match `truth.json`; (b) `oracle_check.py` — final line `ORACLE OK`, exit `0`, five region lines all `OK`. | author recomputation; `oracle_check.py` run | 2/2 regions agree by both routes |
| O11 | OBSERVATION | **Independent cross-check with the second scanner named in the REA firmware route (unblob 26.6.4), run by the ledger author outside the REA record.** On the whole 2048-byte padded image, unblob 26.6.4 reports **no chunk at all** — its JSON report contains only `StatReport`, `FileMagicReport` (`application/octet-stream`), `HashReport` (image SHA-256 `bdfe9f46…`) and `RandomnessReport`, with zero `ChunkReport` entries and zero subtasks; extraction produced 0 files. On the isolated 79-byte member `image[512:591]` (SHA-256 `bf3dd2e42d36324ae17e81c66cb5d699ac74b1a017628fcfb4302846b1c7c352`) it reports one `ChunkReport`, handler `zlib`, `start_offset` 0, `end_offset` 79, size 79, `is_encrypted` false, and extracts `zlib.uncompressed` of 78 bytes with SHA-256 `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` — equal to the truth digest for `diagnostic-note`. | ledger author's unblob runs, 2026-10-24 (host clock, UTC), scratch under `/tmp/revenger-r63-ledgercheck/` | unblob: 0 chunks on the whole image; 1 zlib chunk + 78-byte plaintext matching truth on the isolated member |
| I1 | INFERENCE | **Oracle agreement, scoped to this fixture only.** On this authored image, with this binwalk version and this route, the record's two reported regions correspond to the two authored truth members on all three checked axes (offset, size, decompressed content SHA-256): precision 2/2 (no reported region falls outside the truth member set), recall 2/2 (no authored zlib member is missing from the record), zero mismatched fields across 6 checked region fields. This says nothing about binwalk or REA firmware inspection on any other image. | O3–O6, O10 | 2/2 · 2/2 · 0 mismatches — fixture-scoped |
| I2 | INFERENCE | The digest agreement is a property of the **bytes at the record's reported offset/size window**, not a field the record carries: the record reports only `offset`, `reported_size`, `signature`, `description`, `reported_confidence` and `size_basis` — it carries no per-member name and no decompressed digest. The truth member names `diagnostic-note` and `component-note` are oracle-side labels that the record does not echo. | O3, O4, O5 (record region key set) | Digest check is a checker-side decompression, not a record field |
| I3 | INFERENCE | The record's `size_basis` is `provider_reported_validation_unknown` on both regions, i.e. the provider does not claim the sizes were validated. On this fixture the two reported sizes coincided **exactly** with the true member lengths (79 and 90 bytes) as measured from the authored bytes — so the provider's inference happened to be correct here, but this fixture does not establish that provider-reported lengths are generally correct or validated. | O3, O4, O5 | Exact agreement on this fixture; general validation not established |
| I4 | INFERENCE | This is a static, non-executing inventory: the fixture's members are ASCII text records, the record declares `authority` `shipped-artifact`, and the record's own limitations state extracted code is never executed. Nothing in the record observes a booted target, a flash layout, or any runtime behaviour. | O1, O7, O8 | Static only |
| I5 | INFERENCE | **Scanner coverage differs between the two engines on this image, so "the firmware region" is engine-dependent.** Binwalk's signature scan found both zlib members at their authored offsets (O3), while unblob 26.6.4 found **nothing** in the same whole image (O11) and only identified the member once it was presented as a standalone zlib stream. The record's own `coverage` field says `signature_scan`, which is binwalk's coverage class, not a claim of container-aware discovery. Any downstream statement about "the regions of this image" must name the engine; the REA record's region set is the binwalk set. This inference is about these two engines on this one synthetic image, not about the engines' general detection ability. | O3, O7, O11 | Engine-dependent region set — engine must always be named |
| I6 | INFERENCE | **What the F counter sees (working tree, re-implementation of the frozen block in `reports/round-63/measure.py`).** Over `corpus/live/runs/**/*.json`, counting dicts with a truthy `evidence_id` and a non-null `normalized_result` keyed by `operation`, the firmware family is present because exactly one such file — `corpus/live/runs/round-63/inspection.json` — carries `operation` = `inspect_firmware_regions`. Observed result on the current working tree: `F_COVERAGE=5/8`, families `['native-static', 'javascript', 'archives', 'firmware', 'evm']`, score `10 × 5/8 = 6.25` (was 4/8, 5.0). `receipt.json` is **not** counted (it has an `evidence_id` but no `normalized_result`). The frozen counter run on a committed `git archive` tree, and the `measure-after.log` on the final tip, remain L1's to execute. | frozen `measure.py` F block, re-implemented against the working tree; O1, O9 | F 5/8 on the working tree — the L1-committed measurement is not yet observed |
| U1 | UNKNOWN | **Other signatures.** This image contains only two zlib members and three all-zero padding spans (O6), so it cannot show whether the route detects any other firmware signature family (uImage, squashfs, LZMA, tar, …). The L1 pre-probe recorded in `reports/round-63/claims.md` (2026-10-23, a 1056-byte header+payload image, 85-signature scan, zero findings) is a different observation from a detection on this 2048-byte synthetic image; this ledger does not transfer it into a claim about other signatures. | `truth.json` `regions` (only `zlib` and `padding` kinds); claims.md pre-probe | No evidence about any other signature family |
| U2 | UNKNOWN | **Extraction completeness.** The record extracted nothing (`extractions` = `{}`), so it cannot show what extraction would yield, whether either member would be carved, whether decompressed payloads would be published, whether any extractor dependency is missing, or whether the `extraction_gaps` list would have been populated. `coverage` `signature_scan` bounds the record to a signature scan. The independent unblob run (O11) shows one member *can* be decompressed to a truth-matching digest once isolated, but that was an author-side probe outside the REA record — the record itself says nothing about extraction, and the second member (offset 1024) was not extracted by any route observed here. | O7, O8, O11 | Record's extraction behaviour unknown; only member 0 independently extracted |
| U3 | UNKNOWN | **Scan depth inside member bytes.** Whether the engine considered signature candidates *within* the compressed member payloads, and whether `--search-all` would have surfaced anything there, is not shown by the record; the record's region list is the only output. The isolated-member unblob probe (O11) decompressed member 0 and found no nested chunk inside its 78-byte plaintext, but that is an author-side observation outside the record and was not repeated for member 1. | O3, O6, O11 | Unknown for the record; member 0 plaintext showed no nested chunk in one author-side probe |
| U4 | UNKNOWN | **Provenance and reproducibility.** One invocation at one moment. The receipt establishes internal consistency between saved bytes, digests and the Evidence ID (O9); it does not authenticate that a producer ran at that time, does not bind the Evidence ID to an external service, and provides no independent third-party witness. The saved JSON alone does not prove the shell exit status. | O9, receipt field list | Producer origin not independently proven |
| U5 | UNKNOWN | **Oracle independence.** `truth.json` and the image were authored by the same lane seat that generated the fixture. Oracle agreement is therefore internally consistent (and reproducible by two routes, O10), but it is not third-party validation; a non-author seat would have to re-derive the regions to make it so. | `generator.py` authorship; O10 | Internally consistent, not third-party |
| U6 | UNKNOWN | **Nothing about a real device.** The payload is inert authored text; no vendor image, no boot, no flash layout, no driver, no hardware behaviour is observed or claimed. The record's `subject.format` is `file`, not `firmware`. | O2, I4 | No device-level claim possible |

## Score and limitations — what the F counter can and cannot see

The F criterion is **selected-family saved-record presence** (`SCORECARD.md` command F,
mirrored by the frozen `reports/round-63/measure.py`). Its whole definition is: over
`corpus/live/runs/**/*.json`, load each file as JSON, skip unparsable ones, and for every
dict that has a truthy `evidence_id` and a non-null `normalized_result`, increment a counter
keyed by that file's `operation`; a family counts as present if any counted file's
`operation` is in that family's set.

**Can see**
- That at least one saved JSON file somewhere under `corpus/live/runs/` carries a non-empty
  `evidence_id`, a non-null `normalized_result`, and `operation` == `inspect_firmware_regions`.
- The resulting family set and the numeric coverage: observed on the current working tree as
  `F_COVERAGE=5/8` (families `native-static`, `javascript`, `archives`, `firmware`, `evm`),
  score 6.25, up from 4/8 / 5.0. `receipt.json` is correctly not counted (no
  `normalized_result`), so the single new record moves the count by exactly one.
- That the counter scans the whole tree, so the count is "present anywhere", not "present at
  this path" — a record placed elsewhere under `corpus/live/runs/` would count identically.

**Cannot see**
- Whether the record came from a real run: no exit code, no command line, no stderr, no
  duration, no producer identity is read by the counter. `receipt.json` supplies those, but
  the counter never looks at it.
- Whether the record's regions are **correct**. The counter does not compare against
  `truth.json`; a record whose regions were offset, resized or fabricated would score
  identically. The 2/2 byte-oracle agreement recorded in O4–O6 and I1 comes from the
  separate check in O10, not from F.
- **Which engine produced the regions, or how complete the region set is.** The counter
  reads `operation` only; it does not read `provider.id`, `normalized_result.engine`, or
  `normalized_result.coverage`. I5 shows the region set is engine-dependent on this image
  (binwalk finds two zlib regions; unblob 26.6.4 finds none in the same bytes), so F's
  firmware tick says "a record with this operation name exists", not "the firmware regions
  of this image were enumerated".
- Whether the fixture was inert, authored, or authentic; whether the record is complete or
  truncated; whether the Evidence ID is genuine; whether the engine's own declared
  limitations were respected.
- Anything about **extraction**, **other signatures**, or **runtime** behaviour: F is a
  presence counter over operation names, not a quality or completeness measure. The UNKNOWN
  rows U1–U6 remain open regardless of the F count.
- The F count alone is not a family claim: it would count a hand-written JSON file with a
  fabricated `evidence_id` and `operation`. The evidence for C2 is the record **plus** the
  receipt **plus** the byte-oracle check, and this ledger records only the last of those
  three as verified by the ledger author (O10).

## Verification commands run by the ledger author (read-only)

```sh
sha256sum corpus/fixtures/firmware-r63/{generator.py,truth.json,firmware-r63.bin} \
          corpus/live/runs/round-63/{inspection.json,receipt.json,stdout.raw,stderr.txt,oracle_check.py}
binwalk --version            # binwalk 3.1.0
unblob --version             # 26.6.4
sha256sum /usr/bin/binwalk ~/.local/bin/unblob
python3 -B corpus/live/runs/round-63/oracle_check.py     # ORACLE OK, exit 0
# unblob cross-check (O11), scratch only:
unblob --report whole_report.json -e outdir3 firmware-r63.bin    # 0 chunks on the whole image
unblob --report member_report.json -e out4 member0.zlib         # 1 zlib chunk, 78 B plaintext
```

The ledger author did not execute any firmware payload, did not re-run the REA producer, and
did not modify the fixture, the record, the receipt, the oracle or any file outside this
ledger and its build report. Scratch under `/tmp/revenger-r63-ledgercheck/` was removed
after the checks above.
