ABSENT — fetch succeeded (HTTP 200, 494 real document bytes) and all three quoted strings are missing in every checked variant; near-miss: the file's `source` field points at RFC 6238 appendix B, the document the quotes paraphrase.

# Quarantine hand-check — row S081

- Register row: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md:156` — `revenger` | round2 | S081 | `payload-absent` | cited URL + three quoted strings | "cited source, companion URLs and local artifacts were all checked; the quote is in none of them". (Distinct `kagi` S081 row exists at register:76 and a gate row at :314 — neither is this seat's row; matched on campaign=`revenger`, round=round2, class=`payload-absent`, URL, and quotes.)
- Cited source: `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/website/public/showcase/aegis/test-vectors.json`
- Class claim: `payload-absent` — the quoted strings are absent from the cited source.

## Fetch record

```
$ curl -sL --max-redirs 15 -w '%{http_code} %{size_download} %{url_effective} redirects=%{num_redirects}' -o quarantine/S081/source.bin 'https://raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/website/public/showcase/aegis/test-vectors.json'
FETCH: 200 494 https://raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/website/public/showcase/aegis/test-vectors.json redirects=0
```

- HTTP: 200 (1 try, no retry needed), redirects: 0
- Bytes: 494 (<= 2 MB → saved at `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/quarantine/S081/source.bin`)
- sha256: `f193953c7ef0d92a5006702412eb35ab85ad9f997a1cbdf28189dab7db73beb0`

## Per-string results (fixed-string, case-sensitive; also checked HTML-escaped needle, html.unescape render, tag-stripped render, and case-insensitive)

| # | Quoted string | raw | unescaped | tag-stripped | case-insens | escaped-needle | verdict |
|---|---------------|-----|-----------|--------------|-------------|----------------|---------|
| 1 | `TOTP: Time-Based One-Time Password Algorithm` | -1 | -1 | -1 | -1 | -1 | ABSENT |
| 2 | `Test Vectors` | -1 | -1 | -1 | -1 | -1 | ABSENT |
| 3 | `X represents the time step in seconds (default value X = 30 seconds)` | -1 | -1 | -1 | -1 | -1 | ABSENT |

(-1 = `bytes.find`/`str.find` miss. The needles contain no `&<>"'` characters, so the HTML-escaped needles are byte-identical to the raw needles; unescape/tag-strip were applied to the full 494-byte document anyway.)

## Fetched document (complete, 494 bytes) — `quarantine/S081/source.bin`

```json
{
  "source": "https://www.rfc-editor.org/rfc/rfc6238.html#appendix-B",
  "public_test_key_ascii": "12345678901234567890",
  "algorithm": "HMAC-SHA1",
  "period_seconds": 30,
  "vectors": [
    { "seconds": 59, "sha1": "94287082" },
    { "seconds": 1111111109, "sha1": "07081804" },
    { "seconds": 1111111111, "sha1": "14050471" },
    { "seconds": 1234567890, "sha1": "89005924" },
    { "seconds": 2000000000, "sha1": "69279037" },
    { "seconds": 20000000000, "sha1": "65353130" }
  ]
}
```

## Near-miss / probable distortion source

The file's `source` field is `https://www.rfc-editor.org/rfc/rfc6238.html#appendix-B` (source.bin byte offset 46). RFC 6238's title is "TOTP: Time-Based One-Time Password Algorithm", its Appendix B is titled "Test Vectors", and §5.2 contains the sentence "X represents the time step in seconds (default value X = 30 seconds)". All three quoted strings are RFC 6238 text (title / appendix heading / §5.2 sentence), not text of this JSON file — the JSON only carries the vector data (`seconds`/`sha1` pairs: RFC 6238 App.B values including `20000000000`/`65353130`) and `period_seconds: 30`, which encodes the same "30 seconds" semantics as the X=30 quote without the literal wording. Case-insensitive probes `totp`, `time-based`, `one-time`, `test vector`, `time step`, `30 second`, `default value`, `aegis` all miss; only `rfc6238` hits (the provenance URL). Fabrication vector: quotes lifted from the cited document's own upstream source, not from the cited document.

## Row verdict

ABSENT — all three strings confirmed absent from the fetched bytes in raw, HTML-unescaped, tag-stripped, case-insensitive, and escaped-needle variants. The register's `payload-absent` claim is correct; the quotes are RFC 6238 content, distorted onto its citing JSON file.

## Tooling

No installs or upgrades performed; `curl` (system), `python3` (system), `html`/`re` stdlib only. No pacman transactions.

Report: `.ufo/waves/round-67/R67QuarS081.md`
