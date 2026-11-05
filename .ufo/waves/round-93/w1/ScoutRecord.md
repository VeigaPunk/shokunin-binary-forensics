# Round 93 — ScoutRecord report (source-opening for the C08 admission)

Seat: ScoutRecord (scout, axis coverage). Lane: `revenger-shokunin`. Date: 2026-11-05.
Scope: open the lane's saved round-77 CDP record this round, produce the two new
SOURCES rows (S495 own-work, S496 external doc) plus the S496 audit receipt, and the
`opens.json` pins for the frozen C1 counter. I did not modify `corpus/SOURCES.md`,
any frozen file, or anything outside my wave dir.

## Outputs (all under `.ufo/waves/round-93/w1/ScoutRecord/`)

| file | sha256 |
|---|---|
| `oracle.log` | `64874d9a3caa5d54d0267aca7de1bc2e452155ff85c18f999428dcd37dcb2ce2` |
| `digests.txt` | `ddd132bb15ffe70a7b584134f2d01b6f0912b6cd339d0c06582566a4267151f0` |
| `opens.json` | `6181e1e0404a65cb22de33b001c052074e2c1e7194a585a26d11f2897f15e61c` |
| `sources-draft.md` | `0c575ecd0efc4df330fcd054b87250a49b48d697f4fe8af1e1ee2205a3c7e2b0` |
| `quote-receipts/S496.receipt.json` | `4bf315934afa61274572abd2e226e2a5ffb6c7423163a8dce50375d609f4a977` |
| `quote-receipts/raw/S496.body` | `ba8018bb02f360686cbff23304da8b6e21923a2e012ade273e3f9a2ce1e2fd64` (35462 B) |
| `quote-verify.log` | `389477b280106ee2f6dd407714a67d0e0f7e54669cb616066eab0b8e1f42c695` |

## Numbers (observed, this round)

- Oracle re-run from the lane root:
  `python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json`
  → exit 0, last line `ORACLE OK (17/17 checks)` (`oracle.log`).
- Re-hash (all three match the pins in `reports/round-93/claims.md`):
  - `corpus/live/runs/round-77/inspection.json` → `b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868`
  - `corpus/fixtures/browser-r77/index.html` → `46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45`
  - `corpus/fixtures/browser-r77/app.js` → `fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593`
- `opens.json` matches the three pins exactly (record sha, oracle tail, both fixture shas).
- S496 fetch: `curl -sS -L https://chromedevtools.github.io/devtools-protocol/` → HTTP/2 200,
  `content-length: 35462`, `Last-Modified: Wed, 04 Nov 2026 04:38:14 GMT`, ETag `6aeab6b6-8a86`.
  Two independent fetches in this session returned byte-identical bodies
  (`ba8018bb…2fd64`). The page carries **no `ms.date` marker** — recorded as absent, not invented.
- Located quote (17 words, tag-free, byte-exact span 3408–3526 of the raw body):
  `"It allows tools to instrument, inspect, debug, and profile Chromium, Chrome, and other Blink-based browsers."`
  — landing-hero intro paragraph, second sentence; access date 2026-11-05.
- Self-check on a scratch copy of `corpus/SOURCES.md` with S495+S496 appended (the lane file
  was never touched): `audit_source_quotes.py verify --sid S496` →
  `S496 terminal=S496 state=verified (ok)`, `SUMMARY rows=1 verified=1 unreachable=0 unresolved=0`, exit 0.
  I also ran the tool's own `self-test` → `self-test: ok (7/7 legs)`.
- Census on the scratch copy: 496 rows, 0 malformed (11 cells each), 0 duplicate ids, 0 enum/tier violations.
- Landing-tree simulation (corpus + reports/round-93 copied to scratch, my `opens.json` and
  `quote-receipts/` dropped in at the paths the frozen counter reads): the frozen counter's own
  `check_opens(root)` → `(True, 'ok')` and `check_quotes(root, ['S495','S496'])` → `(True, 'ok')`.
  Both frozen counter legs that depend on my material therefore pass on a landing-shaped tree.

## The two rows (for the L1 to append to `corpus/SOURCES.md`)

Full text, with the located quote and access dates, is in `sources-draft.md`. Summary:

- **S495** (own-work, tier A, opened 2026-11-05, recheck 180d) — the saved r77 record:
  source cell names `corpus/live/runs/round-77/` + `corpus/fixtures/browser-r77/`; anchor pins the
  stdout sha256, the receipt `exit_code 0`, the LEDGER record entry and both fixture shas; teaches =
  how to open a saved browser-runtime record as evidence (re-run the fixture oracle so 17
  byte-derived checks re-bind the record to the committed fixture); status `mined`;
  used-by `corpus/knowledge/round-93-browser-cdp-runtime-evidence.md`.
- **S496** (docs, tier A, opened 2026-11-05, recheck 180d) — Chrome DevTools Protocol:
  scope limited to the protocol's own self-description (that CDP is the JSON-based protocol Chrome
  exposes for inspecting/debugging pages — no compatibility, support or lane-fixture claim);
  anchor = landing-hero intro paragraph 2nd sentence, no `ms.date` marker, HTTP Last-Modified
  2026-11-04, ETag, plus the ≤25-word quote as the last quoted segment (audit-tool anchor rule);
  teaches = that CDP is the protocol Chrome exposes for inspecting/debugging pages, so a saved CDP
  inspection record can be called browser-runtime evidence; status `mined`;
  used-by `corpus/knowledge/round-93-browser-cdp-runtime-evidence.md`.

Both rows: exactly 11 cells, no `|` inside any cell, ids verified unused (current max S494).
Id allocation agreed with peer scout ScoutS136, who takes **S497** for the S136 supersedes row.

## Landing requirements the L1 must satisfy (defect-risk if skipped)

1. `reports/round-93/opens.json` — the frozen counter reads `root/reports/round-93/opens.json`,
   **not** the wave dir. Copy my `opens.json` there byte-for-byte.
2. `reports/round-93/quote-receipts/` — `check_quotes` runs
   `audit_source_quotes.py verify --receipts reports/round-93/quote-receipts`. Copy my whole
   `quote-receipts/` directory there, keeping `raw/S496.body` beside `S496.receipt.json`
   (the tool resolves the body as `<receipts>/raw/<sid>.body`).
3. `corpus/SOURCES.md` must carry S495 and S496 appended (registry tail) before `C1_SOURCES`/`C1_QUOTES` pass.
4. The entry head must cite **only** S495 and S496 among S-ids: `C1_SOURCES` collects ids from the
   entry's first 15 lines and requires each one to be `mined`, opened `2026-11-05`, and to name
   `corpus/knowledge/round-93-browser-cdp-runtime-evidence.md` in used-by.

## Deviations / notes (no frozen file touched)

- `used-by` written **repo-relative** (`corpus/knowledge/round-93-browser-cdp-runtime-evidence.md`),
  not the absolute path named in my seat brief: the frozen SOURCES contract requires repo-relative
  used-by paths, every existing row uses that form, and the counter's check (`ENTRY in r[10]`)
  passes either way because the absolute path contains the relative one.
- S495 needs no quote receipt: the counter only runs the quote leg for rows whose *source* cell
  contains `http`, and S495's source cell names repo paths only.
- The round-start opening output referenced in `claims.md`
  (`controls/oracle-opening.log`) sits in the frozen `reports/round-93/controls/` tree, which I may
  not write; my equivalent evidence is `oracle.log` in this wave dir for the L1 to place.
- Tooling: no install was needed (curl + python3 + sha256sum already present); no pacman action taken.
- Scratch used: `$HYAKU_SCRATCH/revenger-r93/ScoutRecord/`, removed as the last step of this seat.

## Vote schema — not produced by this seat (deliberate, and it does not block C1)

The frozen counter's `C1_VOTES` leg accepts a vote only when `role` is `reviewer` or `critic`
and the seat is a registry member. `swarm-registry.json` records **ScoutRecord with role
`scout`**, so any vote JSON I wrote would either fail the leg (role `scout`) or misstate my
seat's role (claiming `reviewer`/`critic`). I therefore wrote no vote and recorded the reason
here rather than fabricate one. `C1_VOTES` needs ≥2 distinct registry seats with roles
reviewer|critic — those are the round's reviewer (×3) and critic (×1) seats, whose votes the L1
lands at `reports/round-93/votes/`. My wave-dir artifacts are the inputs their votes bind to
(`artifact_path` under `.ufo/waves/round-93/w1/<seat>/` with `artifact_sha256` over the committed
bytes).
