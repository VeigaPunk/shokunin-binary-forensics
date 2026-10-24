# R63ReviewFirmware — C2 saved-record evidence review (round 63, attempt 1)

Reviewed 2026-10-23 after `corpus/live/runs/round-63/inspection.json` landed (23:24) with
`receipt.json` (23:25) and `oracle_check.py` (23:24). All paths relative to the lane repo root.

## Verdict: **HOLDS** — all five checks pass with independently recomputed evidence.

## 1. Envelope — PASS
`corpus/live/runs/round-63/inspection.json` (3904 bytes, single JSON object):
- `evidence_id` = `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259` (non-null).
- `operation` = `inspect_firmware_regions` (exact string).
- `normalized_result` non-null: keys `engine`, `input_size=2048`, `regions[2]`, `coverage=signature_scan`.
- `provider` = `{id: "binwalk", name: "Binwalk", version: "3.1.0"}` — id and version present and non-null.
- Provider-integrity cross-check: `normalized_result.engine.executable_sha256` = `5fc19aac1f357a66a47e8b20a8038a84cb93971cb5d331bd4503b02fcc0a40d6` equals my own `sha256sum /usr/bin/binwalk`.

## 2. Receipt — PASS
`corpus/live/runs/round-63/receipt.json`: all contracted fields present —
- `command` = `npx -y rea-agents@6.5.0 inspect-firmware-regions /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/firmware-r63.bin --format json`
- `exit_code` = 0; `duration_seconds` = 1.296587134
- `fixture_sha256` and `stdout_sha256` (checked below); `evidence_id` identical to the envelope's.
- stdout SHA-256 agreement (recomputed by me): receipt `stdout_sha256` = `f69978355e2897fbaa54daadb3e749d7e31d608913a6c1ee849a07ea33aa71f9` = `sha256sum corpus/live/runs/round-63/stdout.raw`. `cmp` shows `stdout.raw` is byte-identical to `inspection.json` — the envelope is the saved stdout copy, so one hash covers both.
- Version corroboration: npx cache contains `rea-agents` `6.5.0` (alongside other cached versions).

## 3. Fixture SHA-256 — PASS
Receipt `fixture_sha256` and envelope `subject.digest.sha256` both = `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be` = my `sha256sum corpus/fixtures/firmware-r63/firmware-r63.bin` (2048 bytes). Also equals `truth.json` `image.sha256`.

## 4. Oracle — PASS (verdict traced to my own re-derivation)
`python3 -B corpus/live/runs/round-63/oracle_check.py` → `ORACLE OK`, exit 0, one line per truth region:
- padding 0+512 OK, **diagnostic-note zlib offset=512 size=79 decompressed_sha256=OK** `a5718481696cea25cba1346f0898d2e8b2c3cc1ad5324832c9a2fbe500df7b86`, padding 591+433 OK, **component-note zlib offset=1024 size=90 decompressed_sha256=OK** `2d0d86aa6fbbbb0e41824900acff3882c60e3f678b51eff227ffeabbd9eeaba9`, padding 1114+934 OK.
- Independent re-derivation from the fixture bytes (my own Python: `zlib.decompress` at the truth offsets, sha256 over decompressed payloads, byte-for-byte padding fill checks, region walk to EOF): zlib header `78da` @512 → 78 bytes → sha256 `a571…` **MATCH**; `78da` @1024 → 97 bytes → sha256 `2d0d…` **MATCH**; padding all `00`, contiguous coverage 512+79+433+90+934 = 2048 = image size. Every oracle line agrees with my derivation; the record's two reported regions (offset 512/size 79, offset 1024/size 90) match the truth zlib members exactly on offset and size.

## 5. Fixture inertness — PASS
- Full-image magic sweep (recomputed by me): no `MZ`, `\x7fELF`, uImage `27 05 19 56`, `#!`, or Mach-O magics anywhere in the 2048 bytes; first 16 bytes are `00`.
- Both members decompress to plain ASCII text notes ("R63 inert synthetic diagnostic record\nsensor=pressure…", "R63 inert synthetic component inventory\ncomponent=radio…"); no executable magic inside either decompressed payload.
- Padding regions are pure `0x00` (verified byte-for-byte against truth `fill_hex`); zlib headers `78 da` are in binwalk v3.1.0's recognized set (L1 pre-probe). No member is an executable image; everything outside the two members is padding. Fixture never executed by this review (memory-only decompress; no unblob/extraction runs).

## Residual risk / verification gaps
- I did not re-invoke `npx` myself; the live run transcript (command, exit 0, timing) is R63FirmwareRun's receipted record. Corroboration here: receipt fields, stdout-hash agreement, envelope/provider hashes, and the 6.5.0 npx cache entry.
- `oracle_check.py` is sibling-authored (R63FirmwareOracle); I verified its green output against my independent byte derivation, not its code path or its red-mutation tests.
- Record `coverage` is `signature_scan` and reports only the two zlib regions; padding regions exist in truth only — consistent with claims.md ("every region the record reports"), not a mismatch.
- envelope `raw_result` shows the provider staged a temp copy (`/tmp/rea-firmware-7rPoLl/firmware.bin`); that is provider behavior on the same bytes, not a provenance break (stdout copy ≡ envelope).
- Preservation of pre-existing `corpus/live` / `corpus/fixtures` bytes is R63Preservation's guard; out of my scope.

Tools installed by this review: none (base-system `sha256sum`/`python3.zlib` only). No pacman transactions.
