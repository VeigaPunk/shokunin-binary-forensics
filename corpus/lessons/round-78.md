# Round 78 — the province probe learns the browser surface it was blind to (criterion P3); the criterion-G/R gate instruments are registered per the §Gate standard

Base `9676f52f627cacbcf1eeab8093c212743ec4a2bd` (r77 tip + non-author spot-check).
Freeze `f042b2959a257644782405f295272486389fc908` (claims + sha-pinned instruments +
red-befores, committed before any after-run). Two claims, distinct axes, causally
separable, neither exploratory: **C1 coverage** (criterion P revision, instrument P3 —
the r77-routed P2 blind spot closed with its own red-before) and **C2 calibration**
(gate-registry registration of criterion G's `gate_probe.sh` and criterion R's
`receipt_probe.sh` — the r77 carry-in, resting on S449).

## Carry-in dispositions (r77 non-author closure; addressed first)

1. **Criterion G's instrument has no Gate-registry row (criterion R unregistered
   since r76 — inherited).** Both registered this round in the SKILL.md
   `## Gate registry` (claim C2's substance): full §Gate-standard row fields (name,
   kind `gate` — both scripts can fail, red exit 1 / green exit 0 — entry command,
   verdict map, self-test, pinned-value path, write scope, owner), with the
   self-test disposition recorded honestly: neither probe exposes a self-invocation
   mode, so the standard's self-test clause is NOT satisfied and is NOT claimed —
   routed debt; the two-evidences clause is carried by the committed red/green log
   pairs over pinned revisions. The registration also records the producer-coupling
   note (receipt_probe legs 1/2/4 read the installed rea's operation names; a
   producer update turns it red until its pinned rows are superseded — that redness
   is the criterion working). The criterion-instrument class question (do P/F/counters
   also take rows?) is recorded as **routed, not settled** — SKILL.md registry note,
   no exemption claimed.
2. **Literal census form's old-host layout defect** — re-run this round before
   writing anything: the closure contract's literal `sources-census.sh validate
   --root <fleet root> revenger` exits **2** (lane id resolves to
   `<root>/<id>-shokunin/`, the old-host layout); the sanctioned explicit-lane-dir
   form exits **0** (31 W, disclosed W01/W04 classes). The sanctioned form stays
   documented next to the old-host literal in `SKILL.md` §4a (recorded r77; nothing
   to change — it is current). Operator-side item stays routed (r74/r75/r76/r77/r78
   lineage).
3. **Cosmetic report-title / driver-label note — applied to future titles.** The
   round report title now names both label spaces and types them: the lane's
   self-consistent hyaku number (run 17: r75=14, r76=15, r77=16, r78=17) alongside
   the watchdog's constant driver label (`zcode run14`), named as the driver's
   process label, not a run counter.

## Gate

Fresh-start §7 (the r71/r72/r73 rejected closures were re-read and spot-checked;
r74–r77 were admitted, so the constraint binds via the rejected lineage only).
Ruled out, and why (full list in `reports/round-78/claims.md` §7): **F android** —
hard-gated on the caller-supplied `REA_JADX_MCP_JAR`, re-probed this round (env
unset, no jadx on PATH, no `~/tools/jadx*`; committed receipt S448 stands); a
do-nothing control reaches the identical state. **K admissions (C05/C15)** — the
wave Q-review surface is absent on this host; the r74 L0 stands unanswered
(re-checked in the fleet `.ufo/l0-questions.md` this round). **r73's C1 (C10)** —
disposed `rejected` by the frozen r74 kill rule. **Criterion C repair** (the 2
failing replay verifiers, `r47: artifact` / `r55 artifact`) — re-run this round,
fails on old-host authored-fixture artifact assertions; repair means re-authoring
the r47/r55–r57 fixture chains, ruled out on §9 sizing, stays routed. **Criterion R
extension / criterion N attribution pair** — the routed calibration alternatives,
superseded this round by the r77 spotcheck's routed item 1 (registration); both stay
routed for future rounds.

Sources opened this round (rows appended):

| row | path/command | located quote (≤25 words) | decision |
|---|---|---|---|
| S449 | fleet `PROTOCOL.md` §Gate standard :375-420 at checkout `57fa881f`, opened 2026-11-01 | "closure grades no gate conformant until its registry row exists at the lane's registry home" | ADMIT (tier A, fleet-protocol) |
| S450 | `corpus/lessons/round-77-verifier-spotcheck.md` :156-166 + `corpus/lessons/round-77.md` :130-135, opened 2026-11-01 | "The P2 province probe's surface list predates the browser record" | ADMIT (tier A, own-work) |

Census: round start — literal form exit 2 (`revenger missing`), sanctioned form
exit 0 (31 W, disclosed W01/W04 classes); round end after the S449/S450 append —
see the report's Sources & frontier section and `reports/round-78/census-after.log`.

C1 evidence chain: the routed blind spot (S450) → fixture construction (the tree's
own PROVINCE.md bytes with the r77 browser present-record block replaced by the
dedicated sentinel `[absent on this host: cdp-browser]`; scaffolding per the r75
negctl pattern: `.git` + `corpus/training/bounty-triage/MODULE.md` so the two
location-dependent probes resolve and the browser record is the only variable) →
red: frozen P2 on the fixture prints `P2_SURFACES_RESOLVED=11/11 UNRECORDED_ABSENT=0
STALE_RECORDS=0 P2_SCORE=10.0` **exit 0** (`p3-before.log`, committed at freeze —
the false-pass, by construction: the browser surface is not in v2's list) → P3
lands (eleven v2 checks byte-identical + the twelfth surface) → green: P3 on the
same fixture prints `cdp-browser STALE-RECORD …`, `P3_SURFACES_RESOLVED=11/12 …
P3_SCORE=9.2` **exit 1**, attributed (the failing line names cdp-browser);
`P3_NEGCTL_VERDICT=green` over all legs (`p3-negctl-run.log`, re-run from a fresh
`git archive` extraction after the disclosed post-freeze LEG4 correction — see
Mistakes row 3); positive control: P3 on the lane
tree → `12/12 0 0 P3_SCORE=10.0` exit 0 — **no PROVINCE.md byte was touched this
round**; the r77 dated present-record already satisfies the probe. Disclosed:
P3_NEGCTL_UNRECORDED_PRESENT_GREEN_BY_DESIGN=ok — a present surface with no record
is not a defect, and the UNRECORDED-ABSENT branch cannot be manufactured for
cdp-browser inside a fixture (fixed host paths; unlike r75's ghidra leg, which faked
an empty HOME) — a harness limit, not claimed as a kill leg.

C2 evidence chain: S449 (the §Gate standard: row fields :401, registry-home rule
:420) → red `registry-before.log` (registered instruments **3**; probe-path rows
**0** — the grep no-match exit 1 is itself the red state) → the two registry rows
land (append-only; every pre-existing byte unchanged) → green `registry-after.log`
(**5** / **2**). The rows register what is true, including the gaps: no self-test
mode (routed debt), the two-evidences pairs, the pinned probe shas
(`gate_probe` `a594b57f…e84a` at its r77 freeze pin; `receipt_probe`
`9315f8d8…d5a11`), write scopes, owner.

Boundary: P score held **10.0 → 10.0** at 12 surfaces — the claimed improvement is
the instrument's newly caught defect class (`P2_NEGCTL_STALE_BROWSER_FLAGGED=0/1 →
P3_NEGCTL_STALE_BROWSER_FLAGGED=1/1`), not a score move; no K row, no F family, no
PROVINCE byte, no knowledge entry, no capability row (P3 is an instrument revision
of an existing criterion, not a new analysis capability). C2 moves no criterion
score (C 5.0, N 10.0, R 10.0, G 10.0 all held) — the closed gap is that two in-use
verdict instruments were invisible to gate-conformance checking; they are now
registered with verdict maps, pinned values, write scope and owner. The frozen
instruments' bytes are untouched (P2, f_probe, receipt_probe, gate_probe, r71
counter — blob-compared at adjudication).

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| Dropped fixture scaffolding (inherited r75 pattern not carried) | the first `p3_negctl.sh` draft built PROVINCE-only fixtures; `bounty-triage-module` and `lane-repo` probe against the fixture dir, so both printed UNRECORDED-ABSENT and the red leg exited 1 for the wrong reason (`9/11, 2 UNRECORDED` — not the blind `11/11, exit 0` the claim needs); the r75 harness had solved this (`probe_negctl.sh` scaffolds `.git` + the MODULE.md into each fixture) and the pattern was not carried | the red-before run itself, before the freeze (Q06: no expectation written from intent survived contact with the run) | r75 scaffolding copied into the harness (disclosed in the script header); re-run → LEG1 shows the true blind false-pass; mined here so the next probe-revision round starts from the scaffolded shape |
| Semantically impossible expectation in the first LEG3 draft | the draft asserted P3 on the record-removed fixture must flag UNRECORDED-ABSENT; the run printed `12/12 … exit 0` with `cdp-browser PRESENT` — correct probe semantics: a PRESENT surface with no record is not a defect, and cdp-browser's binaries sit at fixed host paths, so the absent state is not manufacturable inside a fixture (r75's ghidra leg could fake an empty HOME; this surface cannot) | the red-before run + reading the probe's own branch semantics before rewriting the expectation | LEG3 restructured as a by-design disclosure (`P3_NEGCTL_UNRECORDED_PRESENT_GREEN_BY_DESIGN=ok`) with an explicit not-claimable line; the harness green now rests on LEG1 (v2 blind) + LEG2 (v3 attributed kill) + LEG4 (positive control), which is exactly what the claim asserts |
| Instrument tree-resolution: LEG4 targeted the instrument's own tree, not the target tree | the frozen harness ran LEG4's P3 with no argument; P3 then resolves its root from `dirname $0` — identical when invoked at the lane root (all pre-freeze runs), wrong from a `git archive` extraction (no `.git` there → `lane-repo UNRECORDED-ABSENT` → 11/12 exit 1). Caught the moment the committed-bytes receipt was produced: the extraction run failed LEG4 while the lane-root run passed it — the discrepancy is the defect signature | the adjudication receipt run (commit 7f303c3d bytes, extraction in scratch) — the run r77's closure judge would run | post-freeze correction, disclosed: `bash "$P3" "$L"` (LEG4 tests the TARGET tree, as the LANE_DIR contract says); committed in the round-78 correction commit together with this row; red-befores and the C1 predicate bytes are unaffected (LEG1–LEG3 do not read LEG4's tree resolution), the corrected instrument sha is pinned at adjudication |
| SOURCES row written in prose shape, not the census parser's row grammar | the first round-end census run failed: `E01 S449 fields=12` — the cell-embedded `gate\|probe` escape is still a raw pipe to the fleet parser (`awk` splits on `|`; escaped or not), then `E11` (used-by wants bare comma-separated paths; "…claims.md C2" is not a path) and `E05` (kind enum is closed: spec/docs/paper/code/tool/dataset/talk/book/community/own-work; "fleet-protocol" is not in it) — three fires, one cause: the row was written as prose with annotations, not in the grammar the validator enforces | the round-end census receipt itself (`census-after.log` records the full fire chain in its header; exit 1 twice before the fix) | pipe-free phrasing, bare comma-separated used-by paths, kind `docs`; re-run → sanctioned form exit 0, 31 W (same disclosed classes); the grammar is recorded here so the next appended row starts conformant |

## Routed forward

- **Criterion-instrument registration class**: whether P/F/counters take full
  registry rows (the SKILL.md registry note records the disposition as routed, not
  settled). Also routed: self-test modes for `receipt_probe`/`gate_probe` (both rows
  record the gap honestly; adding one means a superseding instrument revision, not
  an edit of the pinned bytes).
- **Criterion C repair** (the two failing replay verifiers) — routed since r75;
  re-confirmed failing this round (`r47: artifact`, `r55 artifact`).
- **Criterion R extension** to the legacy receipt-quoting rows, and **criterion N's
  mutation-killed attribution pair** — the r76/r75 routed calibration items, both
  still open (this round's C2 consumed the registration item instead).
- **F android** — hard-gated on the caller-supplied `REA_JADX_MCP_JAR` (absent,
  re-probed; S448 receipt stands). Moves only when the surface appears.
- **K** — blocked on the wave Q-review surface (r74 L0 unanswered, re-checked).
- **Census literal form** — operator-side routing continues (r74–r78 lineage); the
  sanctioned form is documented in SKILL.md §4a.
- P2 stays committed as the superseded instrument (frozen bytes; its 11/11 hold on
  the clean lane remains true and is re-shown by the negctl's LEG1 fixture run being
  its only remaining use here).

## Census

Round start (2026-11-01): literal form `bash <fleet-root>/scripts/sources-census.sh
validate --root <fleet-root> revenger` → exit 2, `revenger missing
…/revenger-shokunin/corpus/SOURCES.md`; sanctioned form → exit 0, 31 W (W01/W04
disclosed classes), final `ok …/fleet/shokunin-binary-forensics/corpus/SOURCES.md`.
Row count `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`
→ 448 at base → 450 after (S449, S450). Round-end receipt:
`reports/round-78/census-after.log` (sanctioned form exit 0, 31 W — same disclosed
W01/W04 classes; its header discloses the same-round E01/E11/E05 fire chain on
S449's original prose-shaped cells, fixed and re-run — lesson Mistakes row 4).
