# R64FirmwareReadout — C1 derivation pack

## Files changed

- `.ufo/waves/round-64/firmware-readout.py` — stdlib-only byte derivation script; reads only `corpus/fixtures/firmware-r63/firmware-r63.bin`.
- `.ufo/waves/round-64/firmware-readout.out` — captured output, with the process exit code appended.
- `.ufo/waves/round-64/R64FirmwareReadout.md` — this evidence report.

The script scans all byte offsets for valid `0x78` zlib/DEFLATE headers and retains candidates whose decompressor reaches EOF. It derives compressed size from the suffix length less `unused_data`, hashes the image and decoded streams, and reports maximal all-zero spans outside the measured member extents. Span endpoints are half-open.

## Retained execution evidence

Ran `python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/firmware-readout.py`; exit code **0**. The exact printed output and exit code are retained in `.ufo/waves/round-64/firmware-readout.out`.

Derived values:

- Image: 2048 bytes; SHA-256 `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`.
- Maximal all-zero padding spans: `(0, 512)`, `(591, 1024)`, `(1114, 2048)`.
- Zlib member at offset 512: compressed 79 bytes; decoded 78 bytes; decoded SHA-256 `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86`.
- Zlib member at offset 1024: compressed 90 bytes; decoded 97 bytes; decoded SHA-256 `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9`.

## Separate cross-check

Compared the derived values with `corpus/fixtures/firmware-r63/truth.json`: image size/digest, each padding region, and both member offsets, compressed sizes, decoded sizes and decoded digests match. The saved `corpus/live/runs/round-63/inspection.json` independently records the same subject image digest and provider-reported zlib regions at offsets 512/1024 with sizes 79/90. That saved inspection is an observation record, not proof of extraction or execution.

## Risks and limits

- Disclosure: `truth.json` was opened during the initial artifact-discovery read, before the first script run. The script itself reads only the binary fixture, and the saved `.out` is from its byte scan, but the authoring process was not blind to the oracle. Do not treat this as a blind derivation claim.
- The first draft treated a zero byte inside the second compressed member as padding. The final script excludes measured member extents; its final output has only the three spans above.
- This pack supports byte correspondence for this authored synthetic fixture only. It makes no real-vendor firmware, general format, authenticity, extraction, or execution claim. No independent admission decision is claimed here.
- No tools were installed. No build, lint, or test suite was run; the requested script execution is the verification reported above.

Blockers: none.

Report: `.ufo/waves/round-64/R64FirmwareReadout.md`
