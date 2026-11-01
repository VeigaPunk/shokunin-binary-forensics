# Round 77 — the browser-runtime family moves through a real CDP producer run on the host's own browser; the r76 gate-payload refutation leg becomes committed, machine-checked receipts (criterion G)

Base `3e980481002fb344dd6454feae84c9c588c3e873` (r76 tip + integrator
spot-check). Freeze `5acef36fe6cd473308bd57ec103372a2cc17ac4a` (claims +
instruments + red-befores, committed before any after-run). Two claims:
**C1 coverage** (criterion F — browser-runtime family record through a real
`rea inspect-web-page` 6.8.0 run on an authored inert local page, loopback
CDP) and **C2 calibration** (new bounded criterion G — provider-gate payload
receipt fidelity, carrying the r76 spotcheck routed item 2). Neither is
exploratory.

## Carry-in dispositions (r76 non-author closure; addressed first)

1. **Census literal-command layout defect.** Re-run this round before writing
   anything: the closure contract's literal `sources-census.sh validate
   --root <fleet root> revenger` exits **2** on this host (a lane id resolves
   to `<root>/<id>-shokunin/`, the old-host layout; output
   `revenger missing … revenger-shokunin/corpus/SOURCES.md`). The sanctioned
   form — explicit lane dir — exits **0** (31 disclosed W01/W04 warnings,
   final `ok …/corpus/SOURCES.md`). Recorded next to the old-host literal in
   `SKILL.md` §4a with the exact commands (the operator-side item itself
   stays routed, r74/r75/r76 lineage).
2. **Scratch-probe leg durability (routed item 2).** Both provider-gate
   payloads reproduced live on this host and committed as exact producer
   stdout bytes: `corpus/live/runs/round-77/provider-gates/android-gate.json`
   (`code: capability_unavailable`, `details: provider_id: jadx, operation:
   inspect_android_package`) and `firmware-gate.json` (`provider_id:
   binwalk`, `operation: inspect_firmware_regions`), machine-checked by
   `reports/round-77/gate_probe.sh` — this is claim C2's substance.
3. **Two cosmetic wording notes (routed item 3), applied.** (a) `f_probe.py`
   prints the score at two decimals (`7.50`, `8.75`) where the r71 frozen
   counter prints one (`7.5`, `8.8`): representation-only — the families
   mapping was AST-verified equal by the r76 non-author spotcheck; noted
   wherever this round quotes F scores. (b) "kebab-case equivalents for every
   F family" is family-level-true: all 8 families have manifest coverage
   **including `inspect-pe-resources`** (the native-static family's name,
   unlisted in S445); only `inventory_artifact` has no alias (archives is
   covered via `inspect-artifact`). Recorded here; S445 stays
   byte-untouched (append-only registry).

## Gate

Fresh-start §7: the three rejected closures named by the round contract
(r71, r72, r73 fleet reports) were re-read (MANIFEST verdict rows + the lane
SCORECARD sections) and spot-checked. Ruled out, and why: **K-map admissions
(C05/C15)** — every path requires the wave Q-review surface, absent on this
host; the r74 L0 stands unanswered (re-checked this round); r71's C05 kill
defects are scope-sentence repairs needing that same surface. **C10** —
disposed `rejected` by the frozen kill rule in r74; no repair-and-revote.
**r73's C1** — unresolved by wave release; its candidate pin is the
r74-disposed candidate. Declared claims are reachable by neither a
do-nothing control nor those routes.

Sources opened this round (rows appended):

| row | path/command | located quote (≤25 words) | decision |
|---|---|---|---|
| S447 | `corpus/live/runs/round-77/` + `corpus/fixtures/browser-r77/` + loopback CDP commands, opened 2026-11-01 | "`operation`: inspect_web_page … provider: id: rea-cdp-browser" | ADMIT (tier A, own-work) |
| S448 | `corpus/live/runs/round-77/provider-gates/` + `reports/round-77/gate_probe.sh`, opened 2026-11-01 | "details: provider_id: jadx, operation: inspect_android_package" | ADMIT (tier A, own-work) |

Census: round start — literal form exit 2 (`revenger missing`), sanctioned
explicit-lane-dir form exit 0 (31 W, disclosed W01/W04 classes, final `ok
…/corpus/SOURCES.md`); round end re-run after the S447/S448 append — see the
report's Sources & frontier section and `reports/round-77/census-after.log`.

The routed-premise re-derivation that opened C1 (same discipline as r76's
carry-in refusal, applied in favor of action this time): the r76 lesson
routed the browser family on "browser needs a caller-supplied CDP endpoint",
reading "caller-supplied" as operator-supplied. Re-derived: in REA's usage
the caller is whoever invokes the CLI. The host already carries a CDP-capable
browser (Chrome/156.0.8078.74; Edge also present), probed 2026-11-01. No
install, no update, no external surface: the browser runs headless with a
scratch profile bound to loopback (CDP 9333), serving only the committed
fixture bytes over `http://127.0.0.1:8477`. Android, by contrast, was probed
and is genuinely unreachable: the gate demands a caller-supplied
`REA_JADX_MCP_JAR` (jadx-headless-mcp 0.7.1), absent on this host — recorded
as the committed receipt, not scratch (S448). F therefore moves 6/8 → 7/8,
not 8/8.

C1 evidence chain: authored fixture (two static files; the committed bytes
are the source of truth; `truth.json` pins authored anchors + run pin +
volatile-not-compared list; `oracle_check.py` re-hashes the fixture bytes on
every run — premises from bytes, not intent, Q06) → loopback serve + headless
Chrome + `rea list-browser-targets` (exit 0; one page target) → one real
`rea inspect-web-page … --allowed-origins http://127.0.0.1:8477 --format
json` run (exit 0, 3.498 s, stderr empty; `inspection.json` is the exact
stdout bytes, sha256 `b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868`,
Evidence `ev_a0134e6f482424baa278ec374f9bf0e984738a113106556b9933d2fd403918fd`)
→ identity oracle `ORACLE OK (17/17 checks)`, including the two
**`cdp_hash == sha256(authored script text)` bindings** — the producer's own
content hashes bind the record to the committed bytes — → frozen F probe
`F_COVERAGE=7/8 score=8.75` over the landing tree (`f-red.log` 6/8 at
freeze).

C2 evidence chain: red `gate-red.log` (over the base archive: receipts
absent, `GATE_LEG0_RECEIPTS_PRESENT=no`, exit 1) → receipts + probe land →
green `gate-after.log` exit 0 (`GATE_LEG1_ANDROID_MATCH=1`,
`GATE_LEG2_FIRMWARE_MATCH=1`, `GATE_LEG3_NEGCTL_FLAGGED=1`,
`GATE_VERDICT=green`) — the mutated `details.operation` copy is flagged by
the same comparator that passes the committed bytes.

Boundary: F is presence-only (routed debt, r63) — the claim text (a real
current-producer record of a real browser page with byte-derived identity)
is the gate; K 8/15 untouched; no knowledge entry admitted; no capability
table row (the fixture/oracle/probe are instruments, not a new analysis
capability — the CDP observation route is REA's, exercised once). Q05
honored: the PROVINCE browser record cites the demonstrated run, and the
demonstration receipt is committed; presence alone would not have grounded
it.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| Assumed observation: script source text expected in the record | first scratch `inspect-web-page` run used `--include-script-sources`; the record returned `source.included: true` with empty text for both scripts — the browser session attached after page load (`completeness.conditions: ["attach_limited", …]`), so parse-time source capture never had the scripts | reading the producer record before pinning truth expectations (Q06 held; no expectation was written from intent) | identity anchored instead on the producer's own `cdp_hash` values (== sha256 of the authored script texts) and byte lengths; the late-attach limitation disclosed in the LEDGER and `truth.json`; a fresh-run reproduction checks the oracle verdict, not source-text retention |
| Incomplete red tree: instrument bytes not in the red extraction | first `f-red` run invoked `red-base/reports/round-76/f_probe.py` when only `corpus` had been extracted from the base archive — file not found, exit 2 | the red-before run itself (before the freeze commit) | red tree = archive of every path the command names (`corpus` + the instrument), then re-run; `f-red.log` committed from the working form |
| Surface-reachability premise inherited unexamined (the r76 routing class, this lane's own routing) | r76 routed "browser needs a caller-supplied CDP endpoint" under the implication the operator supplies it; "caller" in REA's usage is whoever invokes the CLI — the lane itself on this host | this round's §9 pre-declaration re-derivation before any fixture was authored | PROVINCE browser surface record (dated present + demonstrated, S447); the family moved this round; the class rule stands: a routed blocker premise is re-derived from the tool's own contract before it is accepted as operator-blocking |

## Routed forward

- The last uncovered F family is **android**: hard-gated on a caller-supplied
  `REA_JADX_MCP_JAR` (jadx-headless-mcp 0.7.1, absent; gate receipt
  committed). It moves only when that JAR exists on this host; a do-nothing
  control cannot reach it and neither can this lane without the surface.
- K stays blocked (r74 L0 unanswered, re-checked this round); C05/C15 routes
  unchanged.
- Criterion R extension to the legacy receipt-quoting registry rows (r76
  routed) remains open; criterion G covers the gate-payload receipt class
  only.
- F presence-only semantics remain routed debt (r63); the C7 behavioural-leg
  L0 and the r68+ counter residuals are unchanged.
- The P2 province probe's surface list predates the browser record (its
  checks are a fixed token list; re-run this round, exit 0, 11/11 — the new
  record is invisible to it by construction). Wiring the browser surface into
  a future P revision is the owner's call (a future registering round).

## Census

Round start (2026-11-01): literal form `bash <fleet-root>/scripts/sources-census.sh
validate --root <fleet-root> revenger` → exit 2, `revenger missing
…/revenger-shokunin/corpus/SOURCES.md`; sanctioned form `bash
<fleet-root>/scripts/sources-census.sh validate --root <fleet-root>
<lane-dir>` → exit 0, 31 W (W01/W04 disclosed classes), final `ok
…/fleet/shokunin-binary-forensics/corpus/SOURCES.md`. Row count
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ 446 at base → 448 after (S447, S448). Round-end receipt:
`reports/round-77/census-after.log`.
