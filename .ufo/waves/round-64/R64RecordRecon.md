# R64RecordRecon report

## Result

Created `.ufo/waves/round-64/record-recon.md` with the requested field-by-field correspondence for C1 and exact read-only command/output transcript. It compares the saved round-63 observation record and stdout with the firmware fixture truth and receipt.

## Evidence retained

- `inspection.json` and `stdout.raw` are byte-identical (`cmp` output recorded in `record-recon.md`).
- Operation is `inspect_firmware_regions`; record and receipt evidence IDs are identical.
- Record subject SHA-256, truth image SHA-256, and receipt fixture SHA-256 are the same value: `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`. Record/truth size is `2048`.
- The two observed zlib regions (offset/size `512/79` and `1024/90`) match truth exactly by offset, size, and kind.
- Truth has three padding regions not reported by the saved record; its two decompressed-member SHA-256 values are also absent from the record. The readout explicitly marks these as record-absent/not comparable, not as record/truth agreement.
- Receipt stdout SHA-256 matches the measured hash of `stdout.raw`; receipt exit code is `0`.

## Scope and risks

This is a readout of saved evidence only. No firmware scan was rerun and no corpus source, fixture, or saved record was modified. The observed record reports signatures and sizes; it does not establish the complete truth layout, decompressed member digests, partition validity, authenticity, or execution behavior. No tool was installed.

## Files changed

- `.ufo/waves/round-64/record-recon.md` — correspondence table and exact commands/outputs.
- `.ufo/waves/round-64/R64RecordRecon.md` — this report.

Blockers: none.

Report: .ufo/waves/round-64/R64RecordRecon.md
