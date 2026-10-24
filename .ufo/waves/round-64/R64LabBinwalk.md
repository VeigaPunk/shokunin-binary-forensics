# R64LabBinwalk report

## Result

Completed the read-only Binwalk cross-oracle on `corpus/fixtures/firmware-r63/firmware-r63.bin` with the existing `/usr/bin/binwalk` 3.1.0. The default scan printed no signature rows. `binwalk --search-all` printed exactly two zlib signatures: offset 512 / size 79 and offset 1024 / size 90. Both offsets and sizes match the two zlib regions in `corpus/fixtures/firmware-r63/truth.json`; the oracle identifies them as `diagnostic-note` and `component-note` respectively, with zero padding elsewhere. No other signature was reported.

The entry wording is confirmed only with the M33 qualification: **Binwalk 3.1.0 with `--search-all` reports the two zlib regions at offsets 512 (79 bytes) and 1024 (90 bytes), and no other signatures; the default scan reports neither, as expected for M33.** Binwalk identifies the zlib signatures and offsets/sizes; names and decompressed content come from `truth.json`, not Binwalk.

## Exact retained evidence

- Full command outputs, including version, default scan, all-offset scan, and the unsupported `-R` attempt: `.ufo/waves/round-64/lab-binwalk.md`.
- Cross-oracle values read from `truth.json`: zlib offset 512 size 79 and zlib offset 1024 size 90; all other recorded regions are zero padding.
- Existing M33 explanation in `corpus/lessons/round-63.md`: zlib's Binwalk signature is `short: true`; the default scan misses nonzero-offset streams, while `--search-all` detects them. This probe reproduces that distinction.

## Risks and blockers

- Do not state that a default Binwalk scan found the members: it printed no signature rows. The two-hit statement requires `--search-all`.
- The installed Binwalk 3.1.0 CLI rejects `-R` (exit 2); its usage exposes `--search-all`, which supplied the useful all-offset scan.
- No tools were installed or updated. No extraction or fixture modification was performed.

Report: `.ufo/waves/round-64/R64LabBinwalk.md`
