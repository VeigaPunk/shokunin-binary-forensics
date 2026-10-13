# Round 29 — static CLI route (independent derivation)

## Route

The recorded supported static-inspection route is:

```sh
npx -y rea-agents@6.4.0 inspect-pe-resources <absolute-path-to-fixture.exe> --format json
```

Evidence for this route: `.shokunin/revenger/LOG.md`, Round 28 result, records that exact command shape on the absolute `pe-r28/fixture.exe` path, exit 0 and empty stderr. Round 27 LOG records the same `inspect-pe-resources` operation; saved inspections `.shokunin/revenger/corpus/live/runs/round-27/inspection.json` and `round-28/inspection.json` identify operation `inspect_pe_resources`, provider `rea-pe-resources` version `1`, and static resource inventory. This is a route supported by the checked-in run record, not an independently tested invocation. No producer command was run for this report.

For a future round-29 producer call, the documented invocation shape would substitute the absolute path to `corpus/fixtures/pe-r29/fixture.exe` for the placeholder. Do not interpret this report as confirmation that the round-29 fixture exists, that a new invocation succeeded, or that new Evidence was created.

## Raw-byte checks (performed read-only)

Fixture checked: `.shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe` (1024 bytes). `truth.json` is adjacent at `.shokunin/revenger/corpus/fixtures/pe-r28/truth.json`.

Reproducible checks from repository root:

```sh
python -c 'from pathlib import Path; import hashlib; p=Path(".shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe"); b=p.read_bytes(); print(len(b),hashlib.sha256(b).hexdigest()); print("lang-entry",b[576:584].hex(" "),int.from_bytes(b[576:578],"little"))'
python -c 'from pathlib import Path; import hashlib; b=Path(".shokunin/revenger/corpus/fixtures/pe-r28/fixture.exe").read_bytes(); print("language-id",int.from_bytes(b[576:578],"little"),"payload",b[600:615],"payload-sha256",hashlib.sha256(b[600:615]).hexdigest())'
```

Observed output: `1024 9e1815a37778fc4aaf828f6d22d8c5154e9126614dda2f445768bf35d6ad1034`; bytes at file offset 576 are `09 04 00 00 48 00 00 00`, hence little-endian language ID `0x0409` / 1033. The 15 payload bytes at offset 600 hash to `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.

Independent in-memory mutation oracle check (no fixture written): changing only byte 576 from `0x09` to `0x0c` leaves payload bytes untouched and gives whole-file SHA-256 `6cb7c33709d67f4f7e8c138d28451581c12d94af7e01afb345e97e5adb3853f5`; the observed changed-offset list is exactly `[(576, 9, 12)]`. This confirms the declared byte-level input relation, not parser output for the altered image. The round-28 saved inspection at `.shokunin/revenger/corpus/live/runs/round-28/inspection.json` reports one resource, type ID 10/name ID 1/language ID 1033, entry locations including `{offset:576,bytes:8}`, and payload offset 600/length 15 with the digest above.

## Boundaries

**OBSERVATION:** The repository documents a successful `inspect-pe-resources` static CLI invocation on r28. The r28 file contains language entry bytes `09 04` at offset 576; saved r28 normalized inspection associates that resource entry with language 1033 and the unchanged opaque payload at offset 600, length 15.

**INFERENCE:** The round-29 declaration's one-byte edit `09→0c` at offset 576 is a controlled language-ID input perturbation (1033→1036) while preserving payload bytes. Reusing the documented command shape is the supported static route for testing the declared relation.

**UNKNOWN:** No r29 producer invocation/result was made or checked here, so whether CLI output emits language ID 1036, whether it assigns a new Evidence ID, and whether any other output changes remain unverified. This does not establish loader language fallback/selection, runtime behavior, general PE parser completeness, or authenticity of prior saved records beyond their checked-in contents.
