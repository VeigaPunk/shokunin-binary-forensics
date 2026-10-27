PASS — S048 re-opened fresh on raw bytes; checksum and header_size quotes re-located at the row's stated lines; live-vs-snapshot diff is page-chrome-only.

- Access: 2026-10-27T16:10:03Z (UTC), `https://source.android.com/docs/core/runtime/dex-format`.
- Output form: raw HTTP response bytes via `curl -sSL` (`http_code=200`, `size_download=281157`) saved to scratch — byte- and line-addressable this run, stronger than W1's reader-rendered text (`R71W1OpenS048.md` could not recompute a digest). No reader needed.

Commands and outputs (cwd `/fast/scratch/hyaku/revenger-r71/R71W2OpenS048/`):
- `date -u +%Y-%m-%dT%H:%M:%SZ` → `2026-10-27T16:10:03Z`
- `curl -sSL -o dex-format-live.html -w 'http_code=%{http_code} size=%{size_download}' <url>` → `http_code=200 size=281157`
- `sha256sum` → live `bdbee4ddee3aaee0c276ecdf8a48f36310902c27ad43e1fb2c31ea38cbf5662a` (281157 bytes); committed snapshot `corpus/snapshots/dex-format.html` `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` (281157 bytes) — snapshot digest re-derived here and matches the recorded value.
- `diff <snapshot> <live>` → exactly 2 changed lines: `8946c8946` `<script nonce="…">` (per-request CSP nonce) and `8951c8951` (devsite `app_loader.js` line, per-request payload). All content lines unchanged.
- `grep -n` on live bytes: checksum phrase line 5949; `<td>header_size</td>` line 5975, `must be 0x70 (112) bytes` phrase line 5981; `uint ENDIAN_CONSTANT = 0x12345678;` line 5035. Identical line numbers in the committed snapshot and consistent with `corpus/SOURCES.md:62` anchors (checksum row 5949, header_size row 5981, ENDIAN_CONSTANT 5035).

Located quote (14 words, live `header_item` checksum row): "adler32 checksum of the rest of the file (everything but magic and this field)"
Located quote (8 words, live `header_item` `header_size` row): "must be 0x70 (112) bytes (v40 or earlier)"

- Snapshot limits: the committed snapshot remains the frozen byte anchor; live digests are per-request unstable because the nonce/loader chrome changes each fetch (row's 2026-10-25 fetch: 281161 bytes; today: 281157, same class of 2-line chrome diff). Line-level anchors hold today only because content bytes matched the snapshot. Scope honored: declared `header_item` field semantics only; not dex program validity. Both quotes ≤25 words. No edits made; scratch receipts inlined above and `/fast/scratch/hyaku/revenger-r71/R71W2OpenS048/` removed.
