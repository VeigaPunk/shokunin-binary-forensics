# R64SourceReaGuide — pinned REA firmware-analysis guide (S036) read + byte-exact snapshot

Seat: source-readiness / scribe. Round 64 (revenger), attempt hyaku. No git/jj
mutation, no commit, no corpus edit. All work in `/tmp/revenger-r64-src` and the
two lane paths this brief names.

## 1. What was fetched (exact commands and outcomes)

Command (cwd `/tmp/revenger-r64-src`):

```
curl -sS -o rea-firmware-guide.md \
  -w 'HTTP=%{http_code} SIZE_DOWNLOAD=%{size_download} CONTENT_TYPE=%{content_type}\n' -L \
  'https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md'
```

| Observation | Value |
|---|---|
| HTTP status | **200** (no redirect; tag path exists — no tag enumeration needed) |
| content-length | **10695** bytes |
| content-type | `text/plain; charset=utf-8` |
| sha256 (fetched bytes) | `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609` |
| lines | 213 |
| etag | `"323070c5e18148df7792662d81a23b57e47e668f1c1ecaa7f240d644797bab98"` |
| tag ref (`api.github.com/repos/morluto/rea/git/ref/tags/rea-agents-6.5.0`) | `refs/tags/rea-agents-6.5.0` → type `commit`, sha **`3b79af28e80785afce9f5998d8f03289402a1847`** |
| contents API at tag (`docs/firmware-analysis.md?ref=rea-agents-6.5.0`) | size 10695, blob sha **`152819177f8dce2124dea2a6a541e701cee227ed`** |

Tag choice is justified by the round-63 **receipt**, not by the record envelope:
`corpus/live/runs/round-63/receipt.json:2` carries
`npx -y rea-agents@6.5.0 inspect-firmware-regions …` (and `LEDGER.md:19` repeats it
verbatim; `LEDGER.md:22` states the CLI version is read from the command line, not
the envelope, because the envelope names the binwalk provider).

## 2. Snapshot (byte-exact)

Saved to `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md`.
`sha256sum` of the fetched file and the saved snapshot are the identical
`e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`;
`cmp` printed `BYTE_IDENTICAL`; `wc -l -c` → `213 10695`.

Provenance sidecar: `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.provenance.json`
(URL, access date 2026-10-24, status 200, sha256, content-length, etag, tag commit
sha, blob sha, capture command, integrity check, pinned-vs-main note, tier, installs).

**Drift finding:** `main` is *not* the same document — HTTP 200, 15474 bytes,
sha256 `d4a25c8569b37c3d030431333db08fc459af54a163af7815b4505cce2f16a898`. `diff`
shows main adds a `rea doctor` firmware-readiness paragraph (`main` docs: "`rea
doctor` does not currently inspect firmware readiness") and a Windows submodule
checkout section, among other text. Any C07 entry must cite the **tag** snapshot
above; quoting `main` would cite bytes the 6.5.0 record producer never shipped.

## 3. Located quotes (each ≤25 words; line numbers are the snapshot's)

Line numbers verified against the saved snapshot whose sha256 is above.

| # | Lines | Words | Quote |
|---|---|---|---|
| Q1 | 3–4 | 13 | "REA accepts **Binwalk 3.1.x** for region inspection and **Unblob 26.6.x** for explicit extraction." |
| Q2 | 4–5 | 11 | "The report parsers are verified with Binwalk 3.1.0 and Unblob 26.6.4." |
| Q3 | 26–27 | 12 | "Binwalk must print `binwalk <version>` and Unblob must print the version alone." |
| Q4 | 83–84 | 18 | "Both return Evidence with the original path and SHA-256, raw producer reports, actual executable path/digest, version and limitations." |
| Q5 | 84–86 | 18 | "Binwalk signature UUIDs and Unblob blob IDs are producer-local identities; compare content hashes and source ranges across runs." |
| Q6 | 86–87 | 16 | "A matching version does not attest an installed build's source revision, so that field remains unknown." |
| Q7 | 91 | 9 | "Region offsets refer to bytes in the original firmware." |
| Q8 | 93–94 | 13 | "Binwalk can replace unknown lengths with the next signature or EOF before serialization." |
| Q9 | 94–95 | 15 | "Neither a signature nor its confidence byte proves a valid partition, encryption or runtime behavior." |
| Q10 | 123–124 | 18 | "Inspection requires separately configured Binwalk (`REA_BINWALK_COMMAND`); without it, the inspection step is unavailable and the region remains unexamined." |
| Q11 | 149–151 | 21 | "This milestone does not add PPC decompilation, raw flash load profiles, bootloader/device tree semantics, vulnerability scanning, emulation or hardware runtime capture." |

Also present and usable as route-scope text: line 56 (CLI form
`rea inspect-firmware-regions /path/to/firmware.bin`) and lines 65–68 (MCP tool
name `inspect_firmware_regions`). Word counts were computed mechanically
(`len(q.split())`) for every row; max 21.

## 4. What `inspect-firmware-regions` does, per this tag

Q4 + Q5 + Q10 + Q7/Q8/Q9: the route returns Evidence carrying the original path and
SHA-256, raw producer reports, the actual executable path/digest, version and
limitations; region offsets are byte offsets in the original firmware; reported
sizes are producer output that may be inferred; signature UUIDs are producer-local;
inspection needs a separately configured Binwalk (`REA_BINWALK_COMMAND`) and, per
lines 26–30, a `--version` banner check plus util-linux `prlimit`.

Record correspondence (observation layer only, `corpus/live/runs/round-63/inspection.json`):

| Guide | Record field | Match |
|---|---|---|
| Q4 original path + SHA-256, executable path/digest | `subject.digest.sha256` `bdfe…10be`, `subject.local_path`, `normalized_result.engine.executable_path` `/usr/bin/binwalk`, `executable_sha256` `5fc1…40d6` | present |
| Q3 version banner `binwalk <version>` | `raw_result.version_execution.stdout.text` = `"binwalk 3.1.0\n"`, `args` `["--version"]` | exact |
| Q2 verified with Binwalk 3.1.0 | `provider.version` = `3.1.0` | exact |
| Q6 source revision stays unknown | `normalized_result.engine.source_revision` = `null` | exact |
| Q7 offsets in original firmware | `regions[0].offset` 512, `regions[1].offset` 1024; record `limitations[0]` = "Signature matches and reported sizes do not establish partition validity…" | consistent |
| Q8/Q9 sizes/confidence caveats | `reported_size` 79/90, `reported_confidence` 250, `size_basis` = `provider_reported_validation_unknown` | token matches guide wording |

## 5. Entropy / signature-scan statement — the decisive finding

* `grep -c -i entropy` over the snapshot → **0**. The pinned guide contains **no
  entropy statement at all**.
* The record's `normalized_result.coverage` is **`signature_scan`**. That token is
  *not* defined verbatim in this guide either; the nearest supporting sentences are
  Q5 (signature UUIDs are producer-local; compare content hashes and ranges) and
  Q9 (a signature/confidence byte proves no partition, encryption or runtime
  behavior), plus Q11's exclusion of vulnerability scanning.
* Consequence for C1: a C07 entry citing S036 **may** state signed-region offsets,
  producer-reported sizes/confidence, and that confidence proves no validity — it
  **may not** claim entropy scanning, extraction, or validity from this source.
  Extraction prerequisites (Unblob 26.6.x, Q1/Q2) are unexercised by the round-63
  record, which is inspection-only (`raw_result.execution.command` `/usr/bin/binwalk`;
  no unblob provider present).

## 6. Gates

| Gate | Result |
|---|---|
| Pinned URL serves a document (not 404) | PASS — HTTP 200, 10695 bytes |
| Snapshot byte-exact vs fetched bytes | PASS — same sha256, `cmp` byte-identical |
| Tag provenance pinned beyond a branch | PASS — tag ref → commit `3b79af28e80785afce9f5998d8f03289402a1847`; contents blob `152819177f8dce2124dea2a6a541e701cee227ed` |
| Every quote ≤25 words with line numbers | PASS — max 21 words; line numbers against pinned sha256 |
| Pinned vs main distinguished | PASS — different sha256 and size; drift recorded |
| Entropy claim availability | FAIL-AS-EXPECTED (no entropy text) — recorded as a scope limit, not hidden |

## 7. Touched surfaces

* `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md` (new, 10695 bytes)
* `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.provenance.json` (new, 1919 bytes)
* `.ufo/waves/round-64/R64SourceReaGuide.md` (this report)
* Scratch `/tmp/revenger-r64-src/` (fetch + headers + main-copy compare); removable on landing.

No `corpus/**`, `README`, `SOURCES.md`, `MANIFEST.json`, wave spec/registry, jj state
or Git index touched. No installs or upgrades were performed (`installs: none`).

## 8. Out of scope / dependencies

* Appending S036 to `corpus/SOURCES.md` and citing it in a lesson/entry is L1/planner
  integration; this seat only supplies the snapshot, sidecar and quotes. `corpus/SOURCES.md:82`
  already carries the un-rowed lead this seat discharges ("open it when the firmware
  family is claimed").
* Bytes, `truth.json` digests and admission-status work belong to C1's author/critic
  seats; nothing here adjudicates C07.
* The record itself cannot be re-executed by this seat (no re-run per scribe rules);
  correspondence above is read from the saved JSON only.
