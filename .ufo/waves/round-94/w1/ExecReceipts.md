# ExecReceipts — round 94 wave 1: independent C1 receipt fetch + self-verification

Seat: ExecReceipts (executor, coverage axis). Cross-checks ScoutReopen. Date: 2026-11-05.
Bounds respected: writes confined to `.ufo/waves/round-94/w1/ExecReceipts/` and scratch
`/fast/scratch/hyaku/revenger-r94/ExecReceipts` (deleted before this report's yield). No
lane files touched; no git/jj commands; network limited to the two named raw URLs.

## 1. Independent fetch (target 1)

Fetched, as an independent second fetch of the same two raw URLs ScoutReopen uses:

- `https://raw.githubusercontent.com/morluto/rea/main/README.md` → HTTP 200, 30064 bytes,
  sha256 `cb5b40c5752a403fbe20be9af2c08b5ca915c033af142f6f57af227cbaa2b6ba` (S498)
- `https://raw.githubusercontent.com/morluto/rea/main/docs/installation.md` → HTTP 200,
  115812 bytes, sha256 `f05249e642a40562e8f2f1eee8ec23d56401f4b5884ba665c02f9730d8de2267` (S499)

Both served directly (no redirect; `url_effective` equals the requested raw URL; status
captured via `curl -w '%{http_code} %{url_effective} %{size_download}'`, saved in scratch,
now deleted).

Artifacts written (revenger-quote-audit-v1 schema, mirroring the schema shape exercised by
`corpus/audit_source_quotes.py`'s self-test):

- `receipts/S498.receipt.json`, `receipts/S499.receipt.json`
  (`verdict: verified`; required fields sid / fetch_sha256 / length / quote / span /
  http_status / fetched_at / fetch_url all present; `fetched_at: 2026-11-05`;
  `seat: ExecReceipts`)
- `receipts/raw/S498.body` (30064 B), `receipts/raw/S499.body` (115812 B)

Located quotes (≤25 words, verbatim in the raw bytes, character spans into the UTF-8
decoded body as the tool indexes it):

- S498, README "How REA works" section (span 8469–8548): "Your agent calls REA through MCP
  to inspect the target and trace relevant code." — anchors the same heading surface the
  S054 row cites.
- S499, installation.md lead (span 107–187): "Setup previews configuration changes and
  asks for approval before applying them." — byte-identical to the S075 anchor quote, i.e.
  no drift in the approval-boundary sentence between the r93-pinned snapshot and the
  2026-11-05 main revision.

Process note: an initial fetch (pid 2395565) downloaded both bodies before status capture
was in place; its stdout was lost, so the canonical fetch was re-run with status captured
(pid 2396779) and only the re-fetched bytes are shipped/verified. Both runs read the same
URLs seconds apart.

## 2. Self-verification with the lane tool on a scratch copy (target 2)

Scratch copy of `corpus/SOURCES.md` (`cp` to scratch, lane file untouched) with two
synthetic rows appended — 11 cells each, `status mined`, `opened 2026-11-05`,
`used-by corpus/knowledge/round-72-tool-landscape.md`, anchors carrying the same quotes as
my receipts (quote = last double-quoted anchor segment).

Command run:

```
PYTHONUTF8=1 python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/audit_source_quotes.py \
  verify --sources /fast/scratch/hyaku/revenger-r94/ExecReceipts/SOURCES.md \
  --receipts /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-94/w1/ExecReceipts/receipts \
  --sid S498 --sid S499
```

Requirement: exit 0 and `SUMMARY rows=2 verified=2 unreachable=0 unresolved=0`.
**Result: PASS.** Full stdout saved to `receipts-verify.log` (wave dir):

```
S498 terminal=S498 state=verified (ok)
S499 terminal=S499 state=verified (ok)
SUMMARY rows=2 verified=2 unreachable=0 unresolved=0
```

(exit code 0; the tool's own body checks — sha256 == fetch_sha256, length, utf-8,
normalized quote in body, span bounds and `body[span] == quote` — all passed.)

## 3. Cross-seat fetch_sha256 comparison (target 3)

ScoutReopen's receipts landed during my run and were compared. Full record:
`fetch-sha-compare.md`. Summary:

- S498: `fetch_sha256` EQUAL (`cb5b40c5…2b6ba`), lengths equal (30064), raw bodies
  byte-identical (`cmp` exit 0).
- S499: `fetch_sha256` EQUAL (`f05249e6…2267`), lengths equal (115812), raw bodies
  byte-identical (`cmp` exit 0).
- **No drift finding.** ScoutReopen additionally pins main at commit
  `fe677f6cf9853fb12490dfb8ef23ccae3a551049` (its receipt notes, GitHub commits API); my
  unpinned fetch of the same URLs minutes apart reproduced the identical bytes, so that
  pin is consistent with what both seats saw. Quote choices differ per seat (S498) but sit
  in the same body bytes; S499 uses the same sentence at the same span in both receipts.

## Receipt inventory (wave dir)

- `receipts/S498.receipt.json` (994 B), `receipts/S499.receipt.json` (1072 B)
- `receipts/raw/S498.body`, `receipts/raw/S499.body`
- `receipts-verify.log` — full stdout of the verify run above
- `fetch-sha-compare.md` — seat-vs-seat hash comparison

## Risks / notes for the L1

- My receipts are seat-authored evidence only; the L1's `reports/round-94/quote-receipts/`
  and SOURCES.md rows S498/S499 remain the L1's to land. The two independent fetches
  agreeing byte-for-byte strengthens C1_QUOTES/C1_SOURCES but does not substitute for them.
- main may advance again before landing; if the L1 wants the exact commit both seats saw,
  `fe677f6cf9853fb12490dfb8ef23ccae3a551049` is the one recorded by ScoutReopen at fetch
  time (my receipts record the raw URL + body hash, which is what the schema verifies).
- Nothing installed; no provider errors encountered; scratch tree deleted (receipts copied
  into the wave dir first).
