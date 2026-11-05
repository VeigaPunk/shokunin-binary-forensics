# ScoutReopen — round 94, attempt 1 (scout seat)

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` (commit `060a8e87d6de6b31f91b58524ab0fcad88ae5431`).
Scope: produce the two drift-check source openings (S498, S499) that the frozen C1
claim rests on, and deliver the drift verdict against the rows they supersede-check
(S054, S075).

**Outcome: both openings produced, both `verified` under the lane's real auditor,
both drift verdicts `no-drift`.**

## 1. Fetches (today, 2026-11-05)

| sid | URL | status | bytes | body sha256 |
|---|---|---|---|---|
| S498 | `https://raw.githubusercontent.com/morluto/rea/main/README.md` | 200 | 30064 | `cb5b40c5752a403fbe20be9af2c08b5ca915c033af142f6f57af227cbaa2b6ba` |
| S499 | `https://raw.githubusercontent.com/morluto/rea/main/docs/installation.md` | 200 | 115812 | `f05249e642a40562e8f2f1eee8ec23d56401f4b5884ba665c02f9730d8de2267` |

Both `main`-branch raw URLs returned **200 on the first attempt** — the documented
fallback (GitHub API default-branch path / github.com README page) was **not**
needed and was not used. Each body was re-fetched and re-hashed identically
(second fetch sha256 equals the first for both files), so the fetch is reproducible.

`main` at fetch time = commit `fe677f6cf9853fb12490dfb8ef23ccae3a551049`
(2026-11-05T10:38:12Z, GitHub commits API).

Bodies are byte-exact in the wave dir:
- `.ufo/waves/round-94/w1/ScoutReopen/receipts/raw/S498.body` (30064 B,
  sha256 `cb5b40c5…b6ba`)
- `.ufo/waves/round-94/w1/ScoutReopen/receipts/raw/S499.body` (115812 B,
  sha256 `f05249e6…2267`)

## 2. Receipts

`.ufo/waves/round-94/w1/ScoutReopen/receipts/S498.receipt.json`
(sha256 `681265c1df4e4bf699b3a3e892eaf0e81f250fcc5e415d94cb114e6625b724ef`)
and `.../S499.receipt.json`
(sha256 `38788534e40e3bfa18a40138906488451f52b7d223e351d819112e70846750e7`).

Schema `revenger-quote-audit-v1`; fields: `sid`, `verdict` = `verified`,
`fetch_url`, `http_status` = 200, `fetched_at` = `2026-11-05`, `fetch_sha256`
(sha256 of the body bytes), `length` (body byte length), `quote`, `span`
`{start,end}` (character offsets into the UTF-8 decoded body — the auditor indexes
decoded text), plus the lane's usual `row_url`/`final_url`/`anchor`/
`body_derivation`/`normalization`/`attempts`/`seat`/`notes` fields, matching the
round-74/round-93 receipt shape.

Located quotes (both ≤ 25 words):

- **S498** (18 words) — *"REA connects your agent to tools for inspecting native
  binaries, JavaScript and Electron apps, .NET assemblies, and websites."*
  span `3954..4079` (README.md:65).
- **S499** (11 words) — *"Setup previews configuration changes and asks for approval
  before applying them."*
  span `107..187` (docs/installation.md:4).

**Verification against the lane's real checker** (`corpus/audit_source_quotes.py`,
unmodified, `verify` mode over the committed bytes):

```
S498 terminal=S498 state=verified (ok)
S499 terminal=S499 state=verified (ok)
SUMMARY rows=2 verified=2 unreachable=0 unresolved=0
EXIT=0
```

(The verification ran against a scratch copy of `corpus/SOURCES.md` with the two new
rows appended, because the live registry does not carry S498/S499 yet — that append
is the L1's row, per the claims file's frontier step. The receipts, the body bytes
and the auditor were untouched.)

## 3. Drift verdicts

Full file with every located evidence line:
`.ufo/waves/round-94/w1/ScoutReopen/drift-verdicts.md`.

| sid | re-opened | baseline | verdict | evidence |
|---|---|---|---|---|
| S498 | REA root `README.md` (main) | S054 @ `0cd7ef45` | `no-drift` | `README.md:65` scope sentence byte-identical; 38/38 "What you can analyze" `Target` rows identical; heading list empty-diff |
| S499 | REA `docs/installation.md` (main) | S075 @ `0cd7ef45` | `no-drift` | `docs/installation.md:4` approval statement byte-identical, same span 107..187; `# Installation and setup` + `## Review setup changes` present; heading list empty-diff |

The baseline is the pinned revision both old rows cite
(`0cd7ef456bf960da265e04b341e82a24b1e377d5`); I fetched it read-only and its sha256
values equal the ones recorded in the round-74 receipts
(`.ufo/waves/round-74/quote-audit/S054.receipt.json`, `…/S075.receipt.json`), so the
comparison baseline is the same byte set the old rows were verified against.

### Adjacent changes recorded (scope-neutral, not hidden)

- README `:197` (current) `Hopper, Ghidra, IDA or Kuna` vs pinned `:192`
  `Hopper, Ghidra or IDA`; overview `:67` now "Hopper, Ghidra, IDA or Kuna"; FAQ
  heading "Do I need Hopper, Ghidra or IDA?" (pinned `:344`) → "Do I need a native
  analysis engine?" (current `:349`). A provider addition *inside* the unchanged
  native-binary family — the declared family set is unchanged, and no entry claim
  enumerates REA's native engines.
- installation.md adds approval-adjacent detail the pinned revision lacked: the
  unattended-approval path (`:707`, restating the pre-existing `--yes
  --install-hopper` route — the flag already existed at pinned `:151`/`:754`/`:769`),
  a pre-approval macOS-version check (`:736`), a dry-run approval path (`:401`), and
  a new "Readiness check" table (`:381`) whose `One analysis engine` row also lists
  `jadx` and `kuna`. Every one is still an *approval* statement — the boundary is
  restated/strengthened, never bypassed, and nothing claims installation or
  readiness on this host.

## 4. What the L1 needs from this seat

- Receipts + bodies are at
  `.ufo/waves/round-94/w1/ScoutReopen/receipts/{S498,S499}.receipt.json` and
  `.ufo/waves/round-94/w1/ScoutReopen/receipts/raw/{S498,S499}.body`. The counter's
  `C1_QUOTES` leg reads `reports/round-94/quote-receipts/` and expects exactly this
  layout (`<sid>.receipt.json` beside `raw/<sid>.body`), so copying the `receipts/`
  directory contents to `reports/round-94/quote-receipts/` satisfies it unchanged.
- The `S498`/`S499` rows themselves must still be appended to `corpus/SOURCES.md` by
  the L1 (`mined`, tier `A`, opened `2026-11-05`, `used-by` cite-back to
  `knowledge/round-72-tool-landscape.md`) — `C1_SOURCES` requires them and they do
  not exist in the registry yet.
- The entry already cites S498/S499 in its source header and carries the Q17 row, so
  the receipt paths it names
  (`reports/round-94/quote-receipts/S498.receipt.json`) must resolve after the copy.

## 5. Bounds honoured

- Wrote only inside `.ufo/waves/round-94/w1/ScoutReopen/` (plus scratch).
- No lane file edited (no `corpus/`, `reports/`, SCORECARD, LOG, SKILL, README,
  PROVINCE, QUALITY); no git/jj write command run anywhere; the fleet repo, sibling
  lanes, `.ufo/state`, `.ufo/watchdog.log` and `shokuknow` untouched.
- Network limited to the two named `github.com/morluto/rea` raw URLs (plus the
  pinned-commit raw URLs of the same repository, used read-only as the drift
  baseline, and the GitHub commits API for the `main` sha). No other host contacted.
- Scratch `/fast/scratch/hyaku/revenger-r94/ScoutReopen/` deleted before yielding;
  all durable receipts copied into the wave dir first.
- No tool installed; no package manager invoked; no sudo; no sysctl touched.
- Read-only seat: no subagent dispatch.
