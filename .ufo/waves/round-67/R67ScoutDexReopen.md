STABLE — fresh 2026-10-24 fetch of https://source.android.com/docs/core/runtime/dex-format differs from the committed snapshot only in 2 infrastructure lines (per-request CSP `<script nonce>` and a devsite feature-flag list in the app_loader JS config); the `header_item` section is byte-identical after tag-stripping, every quoted field text still occurs verbatim, and the footer is unchanged at `Last updated 2026-10-09 UTC`. First data point for the S045 row's 180d recheck: recorded below.

# R67ScoutDexReopen — independent re-open of S045 (dex-format spec)

## Fetch and hashes

Command (exactly the assigned URL, nothing else fetched):

```
curl -sL --max-redirs 15 -o /tmp/r67dex/fresh.html 'https://source.android.com/docs/core/runtime/dex-format'
```

| file | sha256 | bytes |
|---|---|---|
| fresh fetch `/tmp/r67dex/fresh.html` (2026-10-24) | `9680dc4d5a9b9a2cebd74b2a49d42a2ea5dd2a48d8c1fddf9dd1f614e06d07e1` | 281157 |
| committed snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` | `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` | 281157 |

Snapshot sha256 reproduced exactly and matches the S045 row's pinned digest (`corpus/SOURCES.md:59`).

## Byte drift — fully characterized (2 changed lines of ~9k; equal file lengths)

`diff snapshot fresh` output is 4 lines total: changes at old lines 8946 and 8951 only.

- **Line 8946** — CSP nonce, per-request value:
  - snapshot: `<script nonce="R1GN4pA7+nDrYJ/dulpbEJ8pQlLBzr">`
  - fresh:    `<script nonce="Q4aPdM+NvxtWfmFzPwSrU4NJlTue9U">`
- **Line 8951** — devsite `app_loader` JS config; first differing char at offset 1633 of the 7346-char line. The quoted-string token diff shows the embedded feature-flag list changed server-side:
  - snapshot begins `…["Profiles__enable_developer_profile_benefits_ui_redesign","EngEduTelemetry__enable_engedu_telemetry","DevPro__enable_goog…`
  - fresh begins    `…["MiscFeatureFlags__enable_explicit_template_dependencies","MiscFeatureFlags__enable_dark_theme","DevPro__enable_free_bene…`

Both are hosting-infrastructure bytes, not document content. Everything else in the file is byte-identical.

## Last-updated footer (the assigned date field)

Both copies contain, verbatim: `Last updated 2026-10-09 UTC.` — the footer has NOT advanced since the snapshot was taken.

## header_item section — tag-stripped fixed-string comparison

Extraction: from `<h3 id="header-item"` (both files, line 5926) to the next `<h3` opener; strip `<script>`/`<style>` blocks, then all tags, `html.unescape`, whitespace-fold.

- raw section: 7665 chars (both) — byte-identical
- stripped section: 4043 chars (both) — **identical**, stripped-text sha256 (first 16) `beb2ff7111c48137` both sides

## Anchors the S045 row and v2 entry rely on — all still verbatim in the fresh fetch

`corpus/SOURCES.md:59` (S045 anchor) and `corpus/knowledge/round-67-apk-axml-byte-evidence.md:3,106`:

| quoted text | present in fresh |
|---|---|
| `adler32 checksum of the rest of the file (everything but magic and this field)` (checksum row) | yes |
| `SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)` (signature row) | yes |
| `must be 0x70 (112) bytes (v40 or earlier)` (header_size row) | yes |
| `uint = ENDIAN_CONSTANT` (endian_tag row, fresh line 5991) | yes |
| `uint ENDIAN_CONSTANT = 0x12345678;` (ENDIAN_CONSTANT discussion block, fresh line 5035) | yes |
| `magic` / `file_size` / `header_size` / `endian_tag` field names | yes |

Both `header_item` grep anchors (`<td>header_item</td>` lines 4838/6242; `h3#header-item` line 5926) occur at identical line numbers in both files.

## Recheck data point (first entry for the row's 180d recheck)

- re-opened: 2026-10-24 by R67ScoutDexReopen (independent fetch, not the row opener)
- fetch sha256: `9680dc4d5a9b9a2cebd74b2a49d42a2ea5dd2a48d8c1fddf9dd1f614e06d07e1`
- result: content STABLE; drift confined to nonce + feature-flag infra lines; all quoted anchors verified verbatim; footer date 2026-10-09 UTC unchanged

## Unknowns / gaps

- None for this question. The two drifted lines were inspected to their last differing character; no other byte differs (equal file length + 2-line diff).

## Tooling record (operator directive 2026-10-19)

No tools installed or updated for this task — `curl`, `sha256sum`, `diff`, `grep`, python3 stdlib (`re`, `html`, `hashlib`) sufficed. Nothing written into the lane besides this report; fetched bytes kept only in `/tmp/r67dex/` (outside the lane).
