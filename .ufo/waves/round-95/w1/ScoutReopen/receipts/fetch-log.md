# Reopen fetch log — ScoutReopen, round 95 w1 (independent non-author re-fetch)

Host: Linux 7.2.11-arch1-1 x86_64. Fetched at 2026-11-05T17:35:37Z UTC (2026-11-05).
Method: curl -sf, HTTP status recorded from %{http_code}. No retry; both fetches succeeded on first attempt.

- S500 GET https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidence.ts -> HTTP 200, 17010 bytes, sha256 69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f (body receipts/raw/S500.body)
- S501 GET https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/application/investigation/EvidenceLedger.ts -> HTTP 200, 18784 bytes, sha256 f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac (body receipts/raw/S501.body)

## Comparison

| sid | observed sha256 | pinned sha256 (claims.md) | committed receipt body sha256 | verdict |
|---|---|---|---|---|
| S500 | 69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f | 69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f | 69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f | match |
| S501 | f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac | f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac | f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac | match |

cmp: S500 committed-vs-refetched byte-identical; S501 committed-vs-refetched byte-identical.
Receipt quote spans re-checked against the refetched bytes: S500 span [3149,3223) == quote, S501 span [2136,2198) == quote (exact byte match).
