# fetch_sha256 cross-check — ExecReceipts vs ScoutReopen (2026-11-05)

Independent second fetch of the same two raw URLs
(`https://raw.githubusercontent.com/morluto/rea/main/README.md` and
`https://raw.githubusercontent.com/morluto/rea/main/docs/installation.md`),
receipts under `.ufo/waves/round-94/w1/ExecReceipts/receipts/`, compared against
ScoutReopen's receipts at `.ufo/waves/round-94/w1/ScoutReopen/receipts/`.

| sid | fetch_url (both seats) | ExecReceipts `fetch_sha256` | ScoutReopen `fetch_sha256` | verdict | length (mine / scout) | raw bodies |
|---|---|---|---|---|---|---|
| S498 | https://raw.githubusercontent.com/morluto/rea/main/README.md | `cb5b40c5752a403fbe20be9af2c08b5ca915c033af142f6f57af227cbaa2b6ba` | `cb5b40c5752a403fbe20be9af2c08b5ca915c033af142f6f57af227cbaa2b6ba` | EQUAL | 30064 / 30064 | byte-identical (`cmp` exit 0) |
| S499 | https://raw.githubusercontent.com/morluto/rea/main/docs/installation.md | `f05249e642a40562e8f2f1eee8ec23d56401f4b5884ba665c02f9730d8de2267` | `f05249e642a40562e8f2f1eee8ec23d56401f4b5884ba665c02f9730d8de2267` | EQUAL | 115812 / 115812 | byte-identical (`cmp` exit 0) |

Result: **no drift finding**. Both seats fetched the same main-branch raw URLs on
2026-11-05 with HTTP 200 and got byte-identical bodies; `fetch_sha256`, `length`,
`http_status`, `fetch_url` and `fetched_at` agree on every compared field.

Agreement details:

- ScoutReopen additionally pins main at commit
  `fe677f6cf9853fb12490dfb8ef23ccae3a551049` (recorded in its receipt notes,
  from the GitHub commits API); my receipts fetched the same raw URLs minutes
  apart without a commit pin, and the bytes match, so that pin is consistent
  with the bytes both seats saw.
- The located quotes differ per seat by design (S498: I anchored the
  "How REA works" section sentence, ScoutReopen anchored the overview sentence;
  S499: both seats anchored the same S075 approval sentence at the identical
  span 107–187). Both seats' quotes live in the identical body bytes, and each
  receipt independently passes `corpus/audit_source_quotes.py verify`.
- Per the task rule, unequal hashes would have been recorded as a drift
  finding (not an error); no drift was observed for either sid.
