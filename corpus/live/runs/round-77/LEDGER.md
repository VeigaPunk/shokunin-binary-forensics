# round-77 run ledger — browser-runtime family record through the current producer

One bounded, passive, non-executing producer observation of an authored inert
local page, saved as producer-emitted bytes:

- fixture: `corpus/fixtures/browser-r77/` — two authored static files
  (`index.html` 316 bytes sha256 `46e51761…b45`, `app.js` 101 bytes sha256
  `fb079fa2…593`; the committed files are the source of truth — no generator),
  `truth.json` (authored anchors + run pin + producer expectations +
  volatile-not-compared list), `oracle_check.py` (premise leg re-hashes the
  fixture bytes on every run; record leg checks 15 identity facts derived from
  those same bytes).
- serving: `python -m http.server 8477 --bind 127.0.0.1` from the fixture
  directory (loopback only). Browser: the host's own Chrome/156.0.8078.74,
  headless, loopback CDP (`--remote-debugging-port=9333`, scratch profile).
  Nothing was installed, updated or fetched; no external network surface.
- discovery: `rea list-browser-targets http://127.0.0.1:9333 --format json`
  (exit 0) → exactly one page target `F6A6B5C8E48625523BCEA0CE47F68B42`,
  saved as `target-listing.json` (auxiliary; its operation
  `list_browser_targets` is in no F family set).
- record: `inspection.json` = the exact stdout of
  `rea inspect-web-page http://127.0.0.1:9333 F6A6B5C8E48625523BCEA0CE47F68B42
  --allowed-origins http://127.0.0.1:8477 --format json` (rea 6.8.0, provider
  `rea-cdp-browser`), exit 0, 3.498 s, stderr empty, stdout sha256
  `b045a4ee…e868`, `operation: inspect_web_page`, Evidence
  `ev_a0134e6f482424baa278ec374f9bf0e984738a113106556b9933d2fd403918fd`;
  receipt in `receipt.json`.
- identity oracle: `python -B ../../fixtures/browser-r77/oracle_check.py
  truth.json ../../live/runs/round-77/inspection.json` →
  `ORACLE OK (17/17 checks)`: fixture bytes re-hashed against truth.json;
  operation/provider/evidence-shape; pinned url/origin; the loaded title
  `r77 probe page [loaded]` re-derived from the authored `<title>` plus the
  inline script's own string literal (proves the inline script executed);
  the app.js src dom-url; both script lengths (101/46) byte-derived from the
  committed files; **both CDP `cdp_hash` values equal the sha256 of the
  corresponding authored script text** — the producer's own content hashes
  bind the record to the committed bytes; the single Script resource
  (content_size 101, `text/javascript`, reconciliation `exact`).
- observation vs inference vs unknown: the record's identity fields are
  observations (producer-derived from authored bytes served over loopback);
  that the frozen F counter counts family browser-runtime from this record is
  a predicate evaluation (counter bytes committed, unchanged); whether the
  closure judge accepts the family move as honest coverage improvement is
  outside this ledger (unknown, adjudicated externally). Inference (labeled):
  "the caller-supplied CDP endpoint" the r76 lesson named is supplied here by
  the caller's own host browser — a loopback-bound, scratch-profile,
  fixture-only process, not a substrate change and not an install.
- volatility (disclosed): a fresh run reproduces the oracle verdict but not
  the stdout bytes — `evidence_id`, `target_id`/`frame_id`,
  `script_key`/`cdp_hash` (per session), `capture_window` timestamps and
  completeness counters are per-run (`truth.json` .volatile_not_compared).
  The late-attach class (`attach_limited`) is why script *source text* is not
  retained in the record; identity rests on the byte-derived hashes/lengths
  above, not on retained sources.
- carry-in: `provider-gates/` holds the committed receipts for the r76
  refutation leg (b) — the producer's own gate payloads carrying snake_case
  `details.operation` (`inspect_android_package` via the jadx gate,
  `inspect_firmware_regions` via the binwalk/Linux gate) — machine-checked by
  `reports/round-77/gate_probe.sh`. The third refutation surface (a real
  record writing snake_case `operation` into the frozen predicate's field) is
  this directory's own `inspection.json` for the browser family, alongside
  the r76 managed record.
