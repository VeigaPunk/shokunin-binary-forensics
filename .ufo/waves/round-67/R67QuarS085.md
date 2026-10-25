UNREACHABLE — cited URL returns HTTP 404 ("Page not found – SWGDE" WordPress error page) on all 3 attempts, byte-identical 148,687-byte body; real document bytes never obtained. Both quoted strings are absent from the fetched 404 body itself.

## Row under check
- Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:158` — row S085, campaign `revenger`, round `round2`, class `payload-absent`.
- Claim: two quoted strings are ABSENT from the cited source (and companion URLs / local artifacts).
- Cited source: `https://www.swgde.org/wp-content/uploads/2026/05/2025-01-13-Best-Practices-for-Digital-Evidence-Acquisition-Preservation-and-Analysis-from-C` (URL appears truncated mid-slug; brief restricts fetching to this assigned URL only, so no sibling-URL probing was done).

## Fetch evidence (3 tries)
```
curl -sL --max-redirs 15 -o fetchN.bin -w '%{http_code} %{size_download}'
try1: http=404  size=148687  sha256=971b8d04c90861cece28c25eedbbd3c16f76717cc9b209f60e23dbabf9fddfaf
try2: http=404  size=148687  sha256=971b8d04c90861cece28c25eedbbd3c16f76717cc9b209f60e23dbabf9fddfaf
try3: http=404  size=148687  sha256=971b8d04c90861cece28c25eedbbd3c16f76717cc9b209f60e23dbabf9fddfaf
```
- `file fetch1.bin`: `HTML document, Unicode text, UTF-8 text`
- `<title>`: `Page not found &#8211; SWGDE` — a WordPress 404 template, not the document.
- Bytes retained (≤2MB): `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S085/source.bin` = the 404 body, sha256 `971b8d04c90861cece28c25eedbbd3c16f76717cc9b209f60e23dbabf9fddfaf`, 148,687 bytes.

## Per-string results (grep -F equivalent on raw bytes, decoded text, html.unescape rendering, and tag-stripped text)

| Quoted string | raw bytes | decoded | unescaped | tag-stripped |
|---|---|---|---|---|
| `Best Practices for Mobile Device Evidence Collection & Preservation, Handling and Acquisition` | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |
| `Best Practices for Mobile Device Evidence Collection &amp; Preservation, Handling and Acquisition` (HTML-escaped variant) | NOT FOUND | — | — | — |
| `Best Practices for Mobile Device Evidence Collection &#038; Preservation, Handling and Acquisition` (escaped variant) | NOT FOUND | — | — | — |
| `Hash values from multiple extractions` | NOT FOUND | NOT FOUND | NOT FOUND | NOT FOUND |

Near-miss scan on the tag-stripped body: `Best Practices for Mobile Device` (0), `Hash values` (0), `multiple extractions` (0), `Mobile Device Evidence` (0), `Acquisition, Preservation` (0). Only `Page not found` occurs (title + Elementor JS state). No near-miss names the document.

## Verdict rationale
- Fetch did not "fail" at the transport level (HTTP exchange completes deterministically), but the server delivers only a 404 error page — the real document bytes are never obtained, so the register's absence claim is **neither confirmed nor refuted at the cited source**. Per the item's own rule (ABSENT requires "real document bytes"), the correct verdict is **UNREACHABLE**: 404, three identical attempts.
- As a secondary observation: even within the 404 body, both quoted strings (raw and HTML-escaped) are absent — consistent with, but not proof of, the register's claim.
- The truncated slug (`...-from-C`) suggests a longer filename exists server-side; locating it is outside this seat's assigned-URL scope. Recorded as a finding for any follow-up seat.

## Artifacts
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S085/source.bin` (148,687 B, sha256 above)
- This report: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/R67QuarS085.md`

## Bounds
- No writes outside `.ufo/waves/round-67/`; shokuknow tree read-only (register read only at line 158). No tool installs needed (curl, python3, sha256sum already present). No git/jj mutations.
