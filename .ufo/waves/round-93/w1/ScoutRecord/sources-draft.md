# Round 93 — source-opening draft for the C08 admission (seat ScoutRecord)

Two new SOURCES rows for the L1 to append to `corpus/SOURCES.md` (append-only;
both opened this round, 2026-11-05). I do not edit `corpus/SOURCES.md` myself.

Ids reserved for this lane: **S495** (own-work, the saved r77 CDP record) and
**S496** (external doc, Chrome DevTools Protocol). The S136 supersedes row is
**S497** (peer scout ScoutS136); no id collision.

Both rows carry exactly 11 columns, no `|` inside any cell, `status` `mined`,
`opened` `2026-11-05`, `used-by` `corpus/knowledge/round-93-browser-cdp-runtime-evidence.md`.

## S495 — the lane's own saved round-77 CDP record (own-work, tier A)

| S495 | Saved r77 CDP browser-runtime record and its authored fixture — `corpus/live/runs/round-77/` and `corpus/fixtures/browser-r77/` (opened 2026-11-05) | own-work | A | what the lane's own saved round-77 CDP inspection record states for the authored browser-r77 fixture only — the producer stdout bytes, its receipt and its fixture digests — and no general claim about Chrome, CDP, Electron or any other browser | `corpus/live/runs/round-77/inspection.json` stdout sha256 b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868; `corpus/live/runs/round-77/receipt.json` exit_code 0; `corpus/live/runs/round-77/LEDGER.md` record entry; fixture `corpus/fixtures/browser-r77/index.html` sha256 46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45 and `corpus/fixtures/browser-r77/app.js` sha256 fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593; oracle re-run on 2026-11-05 ends ORACLE OK (17/17 checks) | How to open a saved browser-runtime record as evidence: re-run the fixture oracle over the committed record bytes and let its 17 byte-derived checks confirm that the record's identity fields still bind to the committed fixture | mined | 2026-11-05 | 180d | corpus/knowledge/round-93-browser-cdp-runtime-evidence.md |

Opening evidence (re-run this round, 2026-11-05, from the lane root):

- `python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json`
  → exit 0, last line `ORACLE OK (17/17 checks)` (stdout saved as `oracle.log`).
- sha256 re-hash (`digests.txt`):
  - `corpus/live/runs/round-77/inspection.json` → `b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868`
  - `corpus/fixtures/browser-r77/index.html` → `46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45`
  - `corpus/fixtures/browser-r77/app.js` → `fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593`
- No quote receipt is required for S495 (own-work; the row's `source` cell has no
  `http`, so the counter's external-row quote leg does not apply to it).

## S496 — Chrome DevTools Protocol (docs, tier A)

| S496 | Chrome DevTools Protocol — https://chromedevtools.github.io/devtools-protocol/ (opened 2026-11-05) | docs | A | the protocol's own self-description only — that CDP is the JSON-based protocol Chrome exposes so that clients can instrument, inspect, debug and profile pages; not a compatibility guarantee, not a third-party support commitment, and not a statement about the lane's own fixture | landing-hero intro paragraph, second sentence; the page carries no ms.date marker, HTTP Last-Modified 2026-11-04, ETag 6aeab6b6-8a86 — "It allows tools to instrument, inspect, debug, and profile Chromium, Chrome, and other Blink-based browsers." | That CDP is the protocol Chrome exposes for inspecting and debugging pages, so a saved CDP inspection record can be described as browser-runtime evidence with the protocol named instead of left as an unnamed page observation | mined | 2026-11-05 | 180d | corpus/knowledge/round-93-browser-cdp-runtime-evidence.md |

Located quote (the ONE external sentence the C08 entry may state: that CDP is the
protocol Chrome exposes for inspecting/debugging pages):

> "It allows tools to instrument, inspect, debug, and profile Chromium, Chrome, and other Blink-based browsers."

- URL: `https://chromedevtools.github.io/devtools-protocol/`
- Access date: **2026-11-05** (fetched 2026-11-05T14:49:55Z and re-fetched
  2026-11-05T14:51:21Z; both fetches returned byte-identical bodies)
- Location: landing-hero intro paragraph, second sentence (the sentence directly
  following "The Chrome DevTools Protocol (CDP) is a JSON-based protocol …").
- Revision markers present: HTTP `Last-Modified: Wed, 04 Nov 2026 04:38:14 GMT`,
  ETag `"6aeab6b6-8a86"`, `content-length: 35462`, HTTP status 200.
  The page carries **no `ms.date` marker** and no other revision id — recorded as
  such in the anchor cell rather than invented.
- Body sha256: `ba8018bb02f360686cbff23304da8b6e21923a2e012ade273e3f9a2ce1e2fd64`
  (length 35462 bytes). Raw body saved at `quote-receipts/raw/S496.body`.
- Receipt: `quote-receipts/S496.receipt.json` (schema `revenger-quote-audit-v1`,
  verdict `verified`, byte-exact span 3408–3526 into the raw body).
- Self-check on a scratch copy of `corpus/SOURCES.md` with S495+S496 appended
  (the lane file was not modified):
  `python3 -B corpus/audit_source_quotes.py verify --sources <scratch copy> --receipts <wave dir>/quote-receipts --sid S496`
  → `S496 terminal=S496 state=verified (ok)`,
  `SUMMARY rows=1 verified=1 unreachable=0 unresolved=0`, exit 0.

## Scope discipline for the C08 entry (Q10)

S495 and S496 support only: *the saved r77 record is a CDP inspection record of
the authored fixture, and CDP is the protocol Chrome exposes for inspecting and
debugging pages.* Neither row supports any general claim about Chrome, CDP
stability, Electron, or about browsers other than the authored fixture.
