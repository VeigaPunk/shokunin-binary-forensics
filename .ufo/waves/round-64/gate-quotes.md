# Round-64 lesson — Gate quote blocks (draft for L1)

Scribe seat `R64ScribeGate`, 2026-10-24. Quotes are verbatim against the pinned
snapshot after whitespace normalization (line wraps inside the snapshot collapsed
to single spaces; no word changed or invented). Every quote is at most 25 words.
Access date **2026-10-24** for both rows. Computed values below were produced by
this seat from the named files; nothing was rerun from the provider.

## S036 — REA firmware-analysis guide (pinned `rea-agents-6.5.0`)

- Snapshot: `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.md`
- Provenance: `.ufo/waves/round-64/source-snapshots/rea-firmware-guide.provenance.json`
- URL (pinned tag): <https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md>
- Requested ref: tag `rea-agents-6.5.0`; tag commit `3b79af28e80785afce9f5998d8f03289402a1847`;
  blob `152819177f8dce2124dea2a6a541e701cee227ed`
- HTTP status: **200**; `content-type: text/plain; charset=utf-8`
- Bytes: **10695**; lines: **213**
- sha256: `e422b4816b1dbc912680afefb8e23acfd8ead4aea08c3d722d4ccb5207933609`
- Access date: **2026-10-24** (host-local 01:17, -03:00; response `date` 04:17:17 GMT)
- Tier: **A for route-scope sentences only** — what `inspect_firmware_regions`
  does per the version that produced the round-63 record. Not fixture-byte
  evidence, not evidence of local provider execution, not provider completeness.
- Divergence recorded, not smoothed: `main` serves a **different revision**
  (`.../rea/main/docs/firmware-analysis.md`, 15474 bytes, sha256
  `d4a25c8569b37c3d030431333db08fc459af54a163af7815b4505cce2f16a898`; 2026-10-23
  commit touching the path `15450643f7502114c4f0755416f97b8f0b358b69`). The
  round-64 quotes pin the tag snapshot, never `main`.

Located quotes (snapshot line numbers; whitespace-normalized):

- lines 3–4: "REA accepts **Binwalk 3.1.x** for region inspection and **Unblob 26.6.x** for explicit extraction."
- lines 4–5: "The report parsers are verified with Binwalk 3.1.0 and Unblob 26.6.4."
- lines 8–9: "No device, root privilege, mount, emulation or execution of extracted programs is needed."
- lines 27–28: "Inspection and extraction have independent prerequisites; one does not require the other."
- lines 83–85: "Both return Evidence with the original path and SHA-256, raw producer reports, actual executable path/digest, version and limitations."
- lines 85–86: "Binwalk signature UUIDs and Unblob blob IDs are producer-local identities; compare content hashes and source ranges across runs."
- lines 86–87: "A matching version does not attest an installed build's source revision, so that field remains unknown."
- line 91: "Region offsets refer to bytes in the original firmware."
- lines 91–94: "`reported_size` preserves Binwalk's output; `size_basis=provider_reported_validation_unknown` reflects that Binwalk can replace unknown lengths with the next signature or EOF before serialization."
- lines 94–95: "Neither a signature nor its confidence byte proves a valid partition, encryption or runtime behavior."
- lines 103–104: "Decompressed children have unknown original byte ranges and runtime addresses. Task lineage does not establish a byte-for-byte mapping through decompression."
- lines 121–122: "Nested unknown chunks use `inspect_firmware_regions` on the actual published child rather than repeating the same extraction with unchanged handlers."
- lines 123–124: "Inspection requires separately configured Binwalk (`REA_BINWALK_COMMAND`); without it, the inspection step is unavailable and the region remains unexamined."

## S037 — own-work bundle digests (computed by this seat)

Every value below was computed with `sha256sum`/`stat` on the lane working tree
at scribe time; byte counts are from `stat -c %s`.

| file | bytes | sha256 |
|---|---|---|
| `corpus/fixtures/firmware-r63/firmware-r63.bin` | 2048 | `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` |
| `corpus/fixtures/firmware-r63/truth.json` | 1933 | `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` |
| `corpus/live/runs/round-63/inspection.json` | 3904 | `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` |
| `corpus/live/runs/round-63/receipt.json` | 492 | `e930a549db16a180d4ab05307e073cd71599a3317b9f3d15a0d97843d5c6b94d` |

Supplementary (same bundle, not named in the S036/S037 quote requirement):
`corpus/fixtures/firmware-r63/generator.py` 5532 bytes
`4e5d5975e3cf6362f6fd430f2147d42f75d011978f7d6b5ec86d224c77793db4`;
`corpus/live/runs/round-63/LEDGER.md` 22671 bytes
`25a4a18b76a2a55f3b7ea397ee23bba948be3f1c1a3e13a3194c0f057bb1e1a6`;
`corpus/live/runs/round-63/stdout.raw` 3904 bytes
`f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9`.

Observed correspondence (checked by this seat; observation layer only, no
provider rerun, no authenticity or completeness claim):

- `receipt.json.fixture_sha256` = image sha256 = `truth.json.image.sha256` =
  `inspection.json.subject.digest.sha256` = `bdfe9f46…8510be` (matches).
- `receipt.json.stdout_sha256` = `inspection.json` sha256 = `stdout.raw` sha256
  = `f6997835…aa71f9` (matches); `cmp inspection.json stdout.raw` is
  byte-identical, so the saved record is the receipt's stdout verbatim.
- `receipt.json.evidence_id` = `inspection.json.evidence_id`
  = `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`.
- `truth.json.image.size` = 2048; `truth.json.regions` has 5 entries, 2 of kind
  `zlib`; `inspection.json.provider` = `{"id":"binwalk","name":"Binwalk","version":"3.1.0"}`
  and `operation` = `inspect_firmware_regions`; `receipt.json.command` names
  `rea-agents@6.5.0` — consistent with the S036 quote at lines 4–5 (parsers
  verified with Binwalk 3.1.0), but a matching version does not attest a source
  revision (S036 lines 86–87).

## Status flips this round (old → new, lesson-ready)

README C07 token — `corpus/README.md` line 36 observed at scribe time:
`| C07 | firmware images | — | — | frontier |`.

- old: `frontier`
- new (C1 admitted on all criteria): `held`, naming only
  `knowledge/round-64-firmware-region-byte-evidence.md` in the knowledge column.
- fallback (C1 falsified): `uncovered` ("work evidence exists, no admitted
  knowledge"). Exactly one of the two flips lands; no other README row changes.
- Not yet landed at scribe time: README C07 still reads `frontier`; L1 performs
  the flip at round end after adjudication.

Registry rows S036 / S037 — `corpus/SOURCES.md` observed at scribe time: 35 rows,
last id `S035`; **neither S036 nor S037 exists yet**.

- old: absent (next unused id `S036`).
- new: appended rows, status `queued` when opened and worth mining, then flipped
  `queued → mined` on landing when `used-by` cites the new C07 entry (contract v1
  rule 2: only `status`, `recheck`, `used-by` change in place; each change is
  logged old→new here). `used-by` for S036: the C07 entry; for S037: the C07
  entry (plus the lesson only if it cites the row).
- Verification command for the flip:
  `grep -nE '^\| S03[67] ' corpus/SOURCES.md` → both rows present, status column
  `mined`, `used-by` naming `corpus/knowledge/round-64-firmware-region-byte-evidence.md`.
