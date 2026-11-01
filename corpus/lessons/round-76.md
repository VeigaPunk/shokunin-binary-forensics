# Round 76 — the routed F-counter revision was premised on a false record: the producer still speaks the frozen name space; the managed family moves through a real 6.8.0 run; per-leg receipt correction (criterion R)

Base `6f3a646c691017f92012fc4cf928d9e946838b84`. Freeze
`68feeca6b625dc94d31de3954cac75391cc22146` (claims + frozen probes + red-befores,
committed before any after-run; `c21e5a4` before it is an empty-path commit,
mined below). Two claims: **C1 coverage** (criterion F — managed family record
through a real `rea inspect-managed-artifact` 6.8.0 run on an authored managed
fixture) and **C2 calibration** (new bounded criterion R — SOURCES-row receipt
fidelity, carrying non-author carry-in item 1). Neither is exploratory.

## Carry-in dispositions (addressed first)

1. **S444 per-leg correction (non-author carry-in item 1).** Re-ran both legs
   on this host before writing anything: `rea --llms | grep -cE 'inspect_'` →
   **2** (`inspect_macho`, `inspect_signature` — the two Hopper-wrapper
   manifest rows); `rea doctor | grep -cE 'inspect_'` → **0**. Correction row
   **S445** (`supersedes S444`) records the exact per-leg values and is
   machine-checked by `reports/round-76/receipt_probe.sh`. One number in the
   carry-in needed correcting in turn: the substance was stated as "all 14
   frozen-F family names absent"; the frozen F counter counts **11 operation
   names across 8 families** (SCORECARD F command; `reports/round-71/measure.py:161`)
   — all 11 are absent from the manifest *text*, and the substance stands, but
   the absence turned out to be a representation artifact, not name drift (next item).
2. **F-counter amendment (non-author carry-in item 2, sanctioned).** Not
   executed — the premise is refuted by producer evidence, and the lane's
   frozen-instrument discipline (r69; M50) forbids revising a frozen counter
   without cause:
   - `rea --llms` 6.8.0 declares kebab-case equivalents for every F family
     (`inspect-managed-artifact`, `inspect-android-package`,
     `capture-browser-scenario`, `inspect-web-page`, `observe-web-session`,
     `inspect-firmware-regions`, `inspect-artifact`, `inspect-evm-interface`,
     `analyze-javascript-application`) — S445.
   - The producer's own provider-gate error payloads carry snake_case
     `details.operation: inspect_android_package` /
     `inspect_firmware_regions` (scratch probes, 2026-11-01, not committed as
     evidence).
   - A real 6.8.0 record writes `operation: inspect_managed_artifact` into the
     exact field the frozen predicate reads (`corpus/live/runs/round-76/inspection.json`,
     S446).
   So the frozen counter's name space is the producer's record vocabulary; the
   r75 routing ("names no longer exist in the producer") was derived from the
   one aggregated grep that carry-in item 1 corrects. F was **provider-gated
   per family**, not name-drifted: android needs a caller-supplied
   `REA_JADX_MCP_JAR` (jadx-headless-mcp 0.7.1); the 6.8.0 firmware route needs
   Linux + caller-supplied `REA_BINWALK_COMMAND`; browser needs a
   caller-supplied CDP endpoint; **managed works on this host via the built-in
   `rea-dotnet-static` provider**. Predicate unchanged, families unchanged,
   counter bytes unchanged; the amendment discipline's red-before duty is
   honored by `reports/round-76/f-before.log`.

## Gate

Fresh-start §7: the three rejected closures (r71, r72, r73 fleet reports)
were re-read and spot-checked this round. Ruled out, and why: **K-map
admissions (C05/C15)** — every path requires the wave Q-review surface, absent
on this host (r74 L0 unanswered; checked this round), and r71's C05 defects
are scope-sentence repairs needing the same surface; **C10** — disposed
`rejected` by the frozen kill rule in r74, no repair-and-revote; **r73's C1**
— unresolved-by-wave-release, its candidate pin is now the r74-disposed
candidate. Declared claims (F move, receipt correction) are reachable by
neither a do-nothing control nor those routes.

Sources opened this round (rows appended):

| row | path/command | located quote (≤25 words) | decision |
|---|---|---|---|
| S445 | `rea --llms` + `rea doctor` re-run per leg, 2026-11-01 | "\| \`rea inspect-macho <path>\` \| Run inspect_macho without launching Hopper \|" | ADMIT (tier A, own-host, supersedes S444) |
| S446 | `corpus/live/runs/round-76/` + `corpus/fixtures/managed-r76/`, opened 2026-11-01 | "`operation`: inspect_managed_artifact … `classification`: status: managed … module: r76-managed.dll" | ADMIT (tier A, own-work) |

Census: round start exit 0 (31 W, disclosed W01/W04 classes,
`receipts in scratch`, final line `ok …/corpus/SOURCES.md`); round end re-run
after the S445/S446 append — see the report's Sources & frontier section and
`reports/round-76/census-after.log`.

C1 evidence chain: authored fixture (generator self-check re-derives every
premise from the built bytes; regen byte-identical; 924 bytes, sha256
`25ece37da2e0effbe313662d81469371d59a1de4c610ed081b8a68bcdd75733c`) → one real
producer run (exit 0, 3.22 s, stderr empty; `inspection.json` is the exact
stdout bytes, sha256 `9da6800d…b0c65c`) → identity oracle `ORACLE OK (10/10
checks)` → frozen F probe `F_COVERAGE=6/8 score=7.50` over the landing tree.

C2 evidence chain: red `receipt-before.log` (LEG3 FAIL, LEG4
`S444_MISMATCH_FLAGGED`, exit 1) → S445 lands → green `receipt-after.log`
exit 0 with the negative control still firing (the base row's recorded claim
stays flagged; that is the criterion doing its job).

Boundary: F is presence-only (routed debt since r63) — the claim text (real
producer record, real managed artifact, byte-derived identity) is the gate; K
8/15 untouched; no knowledge entry admitted; no capability table row (the
fixture is a fixture, not a new analysis capability).

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| Aggregated receipt counts (r75 carry-in, the round's central find) | S444 recorded one number ("prints 0") for a two-leg command; the `--llms` leg alone prints 2 | non-author r75 closure carry-in, re-verified per leg here before any write | criterion R: receipts that span multiple legs must record per-leg values, machine-checkable (S445 tokens `llms=2 (inspect_macho, inspect_signature)` / `doctor=0`), with the probe flagging the old row (LEG4). Rule: a receipt citing a counting command must be re-runnable to the same value per leg, or name the leg it does not cover |
| Routing on an un-re-derived premise (r75 routed debt) | the F-counter revision was routed on "names no longer exist in the producer", derived from the aggregated grep; the producer's payloads and a real record show the frozen name space intact | this round's pre-declaration re-derivation (three independent surfaces: manifest, error payloads, record) | disposition recorded in claims.md §carry-in + S445; revision not executed. Rule: a routed instrument revision inherits the burden of re-deriving the routing premise before changing frozen bytes |
| treecommit absolute-path invocation → empty commit | `c21e5a42db4c84419adc6f12118b1ea18dd9aa21` committed 0 files: absolute Windows paths are not repo-relative, so every path resolved to "absent on disk, absent in parent" and the commit carried no change; caught by the mandated `git diff <base>..<new> --stat` printing empty | the mandated post-commit diff check (run immediately; before the report) | helper docstring: paths are repo-relative with forward slashes; content re-committed on top as `68feeca6`. Rule: after every treecommit, require a non-empty `--name-status` for a non-empty path list; an empty output with a non-empty path list is a failed landing even at exit 0 |
| Generator metadata-layout asserts (self-caught, Q06 held) | first build: stream-header Offset fields pointed at the headers' own positions instead of the stream data; root-header size formula dropped a 4-byte field; COR20 cb padded to 48 instead of the declared 72; self-check name window too narrow (4 bytes) for `#Strings` | the generator's round-trip self-check refusing (each assert fired on the built bytes, Q06 working as designed) | data-offset cursor separated from header cursor; formula corrected; asserts now re-parse the final image (PE dir 14 → COR20 → metadata → 5 stream headers → heaps round-trip); regen byte-identical |

## Routed forward

- Provider gates are caller-supplied surfaces (PROVINCE: engines caller-supplied
  per REA; substrate remediation refused): android (`REA_JADX_MCP_JAR`),
  firmware 6.8.0 route (Linux + `REA_BINWALK_COMMAND`), browser (CDP endpoint).
  F's remaining open families (android, browser-runtime) move only when the
  operator supplies a provider; no L0 filed this round (the r74 L0 on the
  dispatch surface already covers the class of operator-supplied surfaces).
- K stays blocked (r74 L0 unanswered, re-checked this round); C05/C15 routes
  unchanged.
- Criterion R extends naturally to every SOURCES row quoting a counting
  command (444 legacy rows) — a full registry sweep is future work; S444 was
  the flagged instance.
- F presence-only semantics remain routed debt (r63); the C7 behavioural-leg
  L0 and the r68+ counter residuals are unchanged.

## Census

Round start: `bash <fleet>/scripts/sources-census.sh validate --root <fleet>
<lane-dir>` → exit 0, 31 W (W01/W04 disclosed classes), final `ok …/corpus/SOURCES.md`.
Row count `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ 444 at base → 446 after (S445, S446). Round-end receipt:
`reports/round-76/census-after.log`.
