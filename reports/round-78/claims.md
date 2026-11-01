# Round 78 claims (frozen before any after-run)

Base `9676f52f627cacbcf1eeab8093c212743ec4a2bd` (r77 tip + non-author spot-check;
watchdog launch `2026-11-01T00:53:15-07:00 launch revenger round=78 base=9676f52f627c
(zcode run14)` — the driver's constant process label, not a round counter; the lane's
self-consistent hyaku numbering calls this run 17).

Two claims, distinct axes, causally separable, neither exploratory.

## C1 — coverage (criterion P revision, instrument P3)

The r77 non-author spot-check routed item (and the r77 lesson `## Routed forward`):
the P2 province probe's surface list predates the browser surface — its checks are a
fixed token list, so a stale or unrecorded browser-surface record is invisible to it
**by construction** (r77 `p2-rerun.log` passed 11/11 while the new surface existed).
P3 (`reports/round-78/province_probe3.sh`) supersedes P2 as the criterion's measuring
instrument: the eleven P2 checks are carried byte-identically, and a twelfth surface
`cdp-browser` is added with its own dedicated absent-sentinel token
(`[absent on this host: cdp-browser]`, written only if that surface is ever recorded
absent — the r75 per-surface-token rule). Presence is not readiness (Q05): the probe
resolves the recorded browser binaries, the same presence semantics as the engine rows.

Falsifiable before→after (negative-control pattern, criterion-N class):

- **Red (before):** on a fixture tree whose PROVINCE.md carries a planted stale
  browser record (the present-record block replaced by the absent sentinel while the
  browser binaries are genuinely present on this host), frozen P2 prints
  `P2_SURFACES_RESOLVED=11/11 UNRECORDED_ABSENT=0 STALE_RECORDS=0 P2_SCORE=10.0`,
  **exit 0 — a false-pass** (`p3-before.log`, run before this freeze).
- **Green (after):** P3 on the same fixture flags it:
  `cdp-browser  STALE-RECORD …`, `P3_SURFACES_RESOLVED=11/12 … P3_SCORE=9.2`,
  **exit 1** (`p3-negctl-run.log` LEG2, attribution = the printed line names
  `cdp-browser`). Third leg (by-design disclosure, not a kill leg): P3 on a
  fixture with the browser record removed entirely stays green — a PRESENT
  surface with no record is not a defect (`P3_NEGCTL_UNRECORDED_PRESENT_GREEN_BY_DESIGN=ok`);
  the UNRECORDED-ABSENT branch cannot be manufactured for cdp-browser inside a
  fixture because the probe reads fixed host paths (unlike r75's ghidra leg,
  which faked an empty HOME) — disclosed as a harness limit, not claimed.
  Positive control: P3 on the lane tree itself → `12/12 0 0 P3_SCORE=10.0`, exit 0 —
  no PROVINCE.md byte changes are needed for the green run (the dated present-record
  from r77 already satisfies the probe).

Score boundary (disclosed): the P criterion's score is **10.0 → 10.0** — held, not
moved; the claimed improvement is the instrument's newly caught defect class
(false-pass → flagged), measured by `P2_NEGCTL_STALE_BROWSER_FLAGGED=0/1 →
P3_NEGCTL_STALE_BROWSER_FLAGGED=1/1`. No K row, no F family, no PROVINCE byte moves
with this claim.

Counting commands:

- red:   `bash reports/round-75/province_probe2.sh <fixture-with-stale-browser-record>` → exit 0
- after: `bash reports/round-78/province_probe3.sh <same-fixture>` → exit 1, and
  `bash reports/round-78/province_probe3.sh` (lane tree) → exit 0, `P3_SCORE=10.0`

Instruments sha-pinned at freeze: `province_probe3.sh` and `p3_negctl.sh` (see
`git ls-tree` of the freeze commit); the frozen P2 bytes
(`reports/round-75/province_probe2.sh`, sha256
`04b543162f9682bc0a28d033378f8e553247b5b403c254034d9226cb25298b03`) are reused
unchanged as the red leg.

## C2 — calibration (gate-registry registration; the r77 carry-in, item 1)

The r77 non-author spot-check routed item 1: `reports/round-77/gate_probe.sh`
(criterion G) has no row in the SKILL.md Gate registry — the lane's registry home
(PROTOCOL.md §Gate standard: "closure grades no gate conformant until its registry
row exists at the lane's *registry home*") — and criterion R's
`reports/round-76/receipt_probe.sh` has been unregistered since r76 (inherited).
Both scripts can fail (red exit 1 / green exit 0), so under the §Gate standard both
are gates. This claim registers both, with the standard's row fields (name, kind,
entry command, verdict map, self-test, pinned-value path, write scope, owner) and an
honest self-test disposition (neither probe exposes a self-invocation mode; the gap
is recorded as routed debt, the two-evidences clause is satisfied by the committed
red/green log pairs over pinned revisions).

Falsifiable before→after:

- **Red (before):** registered instruments in the Gate registry = **3**
  (`check_embedded_outputs`, `self_assessment_check`, `lint_entry`); probe-path rows
  = **0** (`registry-before.log`, run before this freeze).
- **Green (after):** registered instruments = **5**; probe-path rows = **2**
  (`registry-after.log`).

Score boundary (disclosed): no existing calibration criterion re-scores (C 5.0, N
10.0, R 10.0, G 10.0 all held); the claimed improvement is the closed
registration gap — two in-use verdict instruments that closures could not
gate-conformance-check now have registered verdict maps, pinned values, write scope
and owner. The registration rests on S449 (PROTOCOL.md §Gate standard, opened this
round); C1 rests on S450 (the committed r77 routed items, opened this round).

Counting commands (cwd = lane root):

- `sed -n '/^## Gate registry/,/^## [^G]/p' SKILL.md | grep -cE '^\| name \|'` → 3 before, 5 after
- `grep -cE 'reports/round-7[67]/(gate|receipt)_probe' SKILL.md` → 0 before, 2 after

Separability: C1's tree (P3 + negctl, no SKILL/SOURCES bytes) runs its negctl legs
green without C2's rows; C2's tree (SKILL rows, no P3 bytes) holds the registry
counts without C1's probe. Verified both ways in scratch (`c1-only.log`,
`c2-only.log`, committed at adjudication).

## §7 fresh-start gate + §9 sizing — what was ruled out, and why

The round contract §7 names the r71/r72/r73 rejected closures; the four rounds since
(r74–r77) were admitted, so the fresh-start constraint binds via the rejected
lineage only. Re-read (MANIFEST verdict rows + reports) and spot-checked; ruled out:

1. **F android (coverage 8/8).** Hard-gated on a caller-supplied `REA_JADX_MCP_JAR`
   (jadx-headless-mcp 0.7.1). Re-probed this round: env var unset, no `jadx` on PATH,
   no `~/tools/jadx*`; the committed r77 gate receipt (S448) stands. A do-nothing
   control reaches the identical state; not claimable.
2. **K-map admissions (C05/C15).** Every path requires the wave Q-review surface,
   absent on this host; the r74 L0 stands unanswered (re-checked this round — the
   question is still cited as open by later lanes' entries). r71's C05 kill defects
   were scope-sentence repairs needing that same surface.
3. **r73's C1 (C10 wave candidate).** Disposed `rejected` by the frozen r74 kill
   rule; no repair-and-revote (r74 disposition re-checked).
4. **Criterion C repair (calibration; the 2 failing replay verifiers).** Both fail
   on old-host authored-fixture artifact assertions (`r47: artifact`,
   `r55 artifact`); repair means re-authoring/relocating the r47 and r55–r57 fixture
   chains, a different substantial move routed since r75 — ruled out of this round
   on sizing (§9), left routed.
5. **Criterion R extension to the legacy receipt-quoting rows / criterion N's
   mutation-killed attribution pair.** The r76/r77 routed calibration alternatives;
   superseded this round by the r77 spotcheck's routed item 1 (registration), which
   is mandatory carry-in and is itself this round's calibration claim. Both remain
   routed for future rounds.

Do-nothing control: both declared claims are unreachable by it (P2 stays blind to
the browser-record class; the registry stays at 3 rows / 0 registered probes).

## Carry-in dispositions (r77 non-author closure; addressed first, status-neutral)

1. **Gate-registry rows for criterion G, and criterion R settled the same way** —
   this is claim C2 (above).
2. **Literal census form's old-host layout defect** — operator-side routing
   (r74/r75/r76/r77 lineage). Re-run this round before writing anything: literal
   form exit 2, sanctioned explicit-lane-dir form exit 0 (31 W, disclosed W01/W04
   classes). The sanctioned form stays documented in `SKILL.md` §4a (r77);
   `census-before.log` / `census-after.log` carry the round receipts.
3. **Cosmetic report-title / driver-label note** — applied to this round's report
   title: the lane's self-consistent hyaku number (run 17) is stated alongside the
   watchdog's driver label (`zcode run14`), named as the driver's process label, not
   a run counter.
