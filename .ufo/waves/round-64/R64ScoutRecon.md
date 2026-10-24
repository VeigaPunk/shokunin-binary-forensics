# R64ScoutRecon

Assigned recon complete; high confidence for measured file facts and literal saved fields/source. Detailed inventory, correspondence table, LEDGER layering and checker checks are saved at `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/scout-recon.md`.

- Inventoried all 3 files in `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/` and all 6 files in `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/`, with exact byte sizes and SHA-256. Image is 2048 bytes, SHA-256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`. Retained stdout and inspection JSON are byte-identical (3904 bytes; `cmp --silent` succeeded).
- Saved Binwalk 3.1.0 `inspect_firmware_regions` record has exactly the truth's two offset/size/signature triples: `(512,79,zlib)` and `(1024,90,zlib)`. Coverage is `signature_scan`; both sizes have `provider_reported_validation_unknown`; no extraction is recorded.
- Member names and decompressed content digests/lengths are oracle-side or byte-derived, **not saved scanner fields**. Three padding spans are truth-side, not reported signature regions.
- Read all LEDGER headings and O/I/U layers; read `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/oracle_check.py` checks. It checks byte/hash/size/padding/stream boundaries, truth partition coverage and sorted normalized region count/offset/size/signature. It does not authenticate receipts, Evidence IDs or provider identity, or check raw-vs-normalized consistency.
- Preserve LEDGER U1–U6: other signatures, extraction/depth completeness, authenticated provenance, independent oracle derivation and real-device behavior remain unknown. O11 unblob results are historical ledger-author probes outside the REA record, with scratch removed. The record mentions `Unblob` in generic limitations despite LEDGER line 24's literal absence wording; saved execution is binwalk only.
- LSP unavailable: `xd://lsp` was not mounted (only ast_edit/debug devices); checker analysis is literal source evidence, not semantic call-graph proof.
- No oracle/test/producer/payload execution; no production edits, git/jj operations, installs or scratch. Only the two requested report artifacts were written. This seat read truth before deriving anything and cannot satisfy Q03 blind derivation or provide an admission verdict.

No required artifact missing. Remaining entry work is outside this recon seat: byte-derived in-entry commands and independently gated admission.

Report: .ufo/waves/round-64/R64ScoutRecon.md
