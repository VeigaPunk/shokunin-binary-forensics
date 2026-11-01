# Round 77 claims — pre-registration (freeze)

Base: `3e980481002fb344dd6454feae84c9c588c3e873` (r76 tip + integrator
spot-check). Two claims, distinct axes (coverage, calibration), causally
separable, neither exploratory. Probes frozen before any after-run:

| instrument | sha256 |
|---|---|
| `reports/round-76/f_probe.py` (frozen r76 instrument, reused unchanged) | `e15a43af56f453479681b49e063741bb008245ed758af7fc2d685aa5e64f39ed` |
| `reports/round-77/gate_probe.sh` (new, this freeze) | `a594b57f58bcc5f401242d71a9ef50b14489b1dab142191bb8b96ec06c3ae84a` |

## C1 — coverage, selected-family record presence (criterion F): browser-runtime

The r76 lesson routed the browser family on "a caller-supplied CDP endpoint";
the caller on this host is this lane, and the host already carries a
CDP-capable browser (Chrome/156.0.8078.74 at
`C:/Program Files/Google/Chrome/Application/chrome.exe` — present surface,
probed 2026-11-01; nothing installed or updated; loopback-only, scratch
profile, deleted after the round). Author `corpus/fixtures/browser-r77/`
(two inert static files, `index.html` 316 B sha256 `46e51761…b45` + `app.js`
101 B sha256 `fb079fa2…593`; the committed files are the source of truth;
`truth.json` pins authored anchors, the run pin and a volatile-not-compared
list; `oracle_check.py` re-hashes fixture premises on every run and checks 15
record facts derived from those bytes). Serve the fixture directory on
`http://127.0.0.1:8477` (loopback only), launch the host Chrome headless with
CDP on `http://127.0.0.1:9333`, discover the page target with
`rea list-browser-targets`, then run ONCE:
`rea inspect-web-page http://127.0.0.1:9333 <targetId> --allowed-origins http://127.0.0.1:8477 --format json`
(rea 6.8.0, built-in provider `rea-cdp-browser`), saving the producer-emitted
stdout bytes at `corpus/live/runs/round-77/inspection.json` with
`target-listing.json`, `receipt.json` and `LEDGER.md`. Admission condition
(all must hold): record `operation == "inspect_web_page"`;
`normalized_result` non-null; oracle verdict `ORACLE OK (17/17 checks)` over
the committed record and committed fixture bytes — including the two CDP
`cdp_hash == sha256(authored script text)` bindings; the frozen F probe
counts family `browser-runtime`.

- **Before (red, committed `f-red.log`):** `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <git-archive 3e98048 corpus>` → `F_COVERAGE=6/8 score=7.50`, `F_FAMILIES=['archives', 'evm', 'firmware', 'javascript', 'managed', 'native-static']` (exit 0).
- **After (target):** same command over the landing commit's archive → `F_COVERAGE=7/8 score=8.75`, `F_FAMILIES` including `browser-runtime`; probe exit 0. Disclosed histogram delta: `inspect_web_page: 1` (the family record) and `list_browser_targets: 1` (auxiliary discovery record; `list_browser_targets` is in no family set — no other family moves).
- **Falsifier:** F stays 6/8, or any admission condition above fails, or the oracle fails on the committed bytes.
- **Boundary (disclosed):** F is presence-only (routed debt, r63); the claim text — a real current-producer record of a real browser page with byte-derived identity (producer `cdp_hash` values equal to the authored scripts' sha256s) — is the gate, not the counter alone. Android stays uncovered (caller-supplied `REA_JADX_MCP_JAR` absent; gate reproduced this round, `provider-gates/android-gate.json`). No K row moves; no knowledge entry admitted; Q05 honored — the surface is demonstrated by the run receipt, not by presence.

Counting command: `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <tree/corpus>`.

## C2 — calibration, provider-gate payload receipt fidelity (new bounded criterion G)

Carries the r76 verifier-spotcheck routed item 2: refutation leg (b) — the
producer's provider-gate payloads carrying snake_case `details.operation` —
stood verified but only as uncommitted scratch probes; the spotcheck routed
"commit a small payload receipt next round for full durability". Land
`corpus/live/runs/round-77/provider-gates/{android-gate.json,firmware-gate.json,receipt.json}`
(exact producer-emitted stdout bytes of the two gate runs, exit 1 each, plus
an L1 receipt) and probe `reports/round-77/gate_probe.sh`, which re-runs both
legs live and machine-checks the committed receipts per leg (criterion-R
per-leg receipt discipline: `code`, `category`, `details.provider_id`,
`details.operation` each), with a mutated-copy negative control (LEG3).

- **Before (red, committed `gate-red.log`, exit 1, over the base archive):** `GATE_LEG0_RECEIPTS_PRESENT=no`, `GATE_VERDICT=red`.
- **After (target):** exit 0; `GATE_LEG0_RECEIPTS_PRESENT=yes`, `GATE_LEG1_ANDROID_MATCH=1`, `GATE_LEG2_FIRMWARE_MATCH=1`, `GATE_LEG3_NEGCTL_FLAGGED=1` (the mutated `details.operation` is flagged), `GATE_VERDICT=green`.
- **Falsifier:** any leg disagrees at the after-run, or the negative control fails to fire (a mutated receipt would compare equal), or a receipt byte drifts from its pinned sha256 (`android-gate.json` `4d0e6ea5…7330`, `firmware-gate.json` `1dfc910c…cb19`).

Counting command: `bash reports/round-77/gate_probe.sh` (needs `rea` on PATH; host-bound by design — the criterion checks this host's producer against committed receipts).

## Carry-in dispositions (protocol work, not claims)

1. **Census literal-command layout (r76 spotcheck routed item 1).** The
   closure contract's literal `sources-census.sh validate --root <fleet root>
   revenger` exits 2 on this host (lane id `revenger` resolves to
   `<root>/revenger-shokunin/`, the old-host layout; re-run this round, exit
   2). The sanctioned form — explicit lane dir — exits 0 and its output is
   byte-identical to the r76 committed `census-after.log` shape. Recorded
   next to the old-host literal in `SKILL.md` §4a, with the real commands and
   exit codes, in the round-77 lesson `## Census`.
2. **Payload receipt durability (routed item 2)** — this is C2 above.
3. **Two cosmetic wording notes (routed item 3).** (a) `f_probe.py` prints
   the score at two decimals (`7.50`, `8.75`) where the r71 frozen counter
   prints one (`7.5`/`8.8`): representation-only, families mapping verified
   equal by the r76 non-author spotcheck (AST) — noted where this round
   quotes F scores. (b) "kebab-case equivalents for every F family" is
   family-level-true: all 8 families covered including `inspect-pe-resources`
   (native-static's name, unlisted in S445); only `inventory_artifact` has no
   alias (its family is covered via `inspect-artifact`) — recorded in the
   round-77 lesson; S445 stays byte-untouched (append-only registry).

## Fresh-start §7 — routes re-read and ruled out

The three rejected closures named by the round contract (r71, r72, r73 fleet
reports) were re-read (MANIFEST verdicts + lane SCORECARD sections). Ruled
out, and why: **K-map admissions (C05/C15)** — every admission path requires
the wave Q-review surface, absent on this host; the r74 L0 stands unanswered
(re-checked this round); the r71 C05 kill defects are scope-sentence repairs
needing that same surface. **C10** — disposed `rejected` by the frozen kill
rule in r74; no repair-and-revote. **r73 C1** — unresolved by wave release;
its candidate pin is the r74-disposed candidate. Declared claims are
reachable by neither a do-nothing control nor those routes: C1 needs a new
real producer record on a new authored fixture through a locally supplied CDP
surface; C2 needs committed receipts plus a live three-leg instrument.

## Separability

C1 verifies from `corpus/fixtures/browser-r77/` +
`corpus/live/runs/round-77/{inspection.json,target-listing.json,receipt.json}`
alone (F probe + oracle; the provider-gates subtree not required). C2
verifies from `corpus/live/runs/round-77/provider-gates/` + the pre-existing
`apk-r65`/`firmware-r63` fixtures + the live producer alone (gate_probe; the
browser fixture/record not required — `gate_probe.sh` references no
browser-r77 path). Single-claim trees are demonstrated in
`f-separability.log` / `g-separability.log` at the after-measurement.

## §9 sizing

Do-nothing control at base: F stays 6/8 (no browser record exists) and the
gate payloads stay uncommitted scratch history (gate probe red) — neither
claim is reachable without the work. No K/P2/F-instrument bytes change; no
frozen counter is touched.
