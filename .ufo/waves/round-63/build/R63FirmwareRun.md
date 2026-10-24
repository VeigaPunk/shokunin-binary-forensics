# R63 firmware inspection run

## Run receipt

The fixture directory was absent at initial inspection. `R63FirmwareFixture` created `generator.py`, `truth.json`, and the inert `firmware-r63.bin`; I used those artifacts and did not edit the fixture paths. The image is 2048 bytes with SHA-256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`.

Ran exactly one producer invocation:

```text
npx -y rea-agents@6.5.0 inspect-firmware-regions /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin --format json
```

- `npx` exit code: 0; output-capture `tee` exit code: 0.
- Duration: 1.296587134 seconds.
- Fixture SHA-256: `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`.
- Exact stdout SHA-256: `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9`.
- Evidence ID: `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`.
- `inspection.json` is the complete producer envelope; it has `operation=inspect_firmware_regions` and a non-null `normalized_result`. `stdout.raw` is the byte-identical raw stdout copy. `stderr.txt` is empty (SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`). Receipt: `corpus/live/runs/round-63/receipt.json`.

## Byte-oracle comparison

Compared each emitted region's `offset` and `reported_size` with the corresponding `truth.json` region. For each reported zlib member, decompressed the fixture bytes at the reported offset and size, then compared decompressed byte count and SHA-256 with the truth oracle.

| Emitted region | Signature | Offset: record / truth | Size: record / truth | Decompressed size: observed / truth | Decompressed SHA-256: observed / truth | Verdict |
|---|---|---:|---:|---:|---|---|
| 1 (`diagnostic-note`) | zlib | 512 / 512 | 79 / 79 | 78 / 78 | `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86` / same | MATCH |
| 2 (`component-note`) | zlib | 1024 / 1024 | 90 / 90 | 97 / 97 | `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9` / same | MATCH |

**Oracle verdict:** both regions reported by REA match the truth offsets, sizes, decompressed sizes, and decompressed content hashes. `truth.json` also describes three padding spans; REA did not report them, and they are not mismatches under the criterion for every region the record reports. `raw_result.Analysis.extractions` is empty, so the content hashes above come from independently decompressing the corresponding fixture byte ranges, not from extraction output in the REA record.

## Tooling and limits

Invoked `rea-agents@6.5.0` through `npx -y` (npm package channel) as required for the inspection; no persistent/global install or update was separately performed. The envelope reports binwalk 3.1.0 and `coverage=signature_scan`; each normalized region uses `size_basis=provider_reported_validation_unknown`. This evidence is limited to the two observed zlib signatures and their byte-oracle agreement; it does not establish scanner completeness or provider validation.
