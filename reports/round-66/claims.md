---
round: 66
date: 2026-10-24
author: revenger-r66
claims: [C1, C2]
lane: revenger-shokunin
claim_base: 8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0
contract: reports/round-66/claims.md
counter: reports/round-66/measure.py
status: pre-registered by L1 revenger-r66 before any after-measurement
---

# Round 66 — the falsified C05 adjudication and the last two receipt conjuncts

Two claims on distinct frozen criteria. C1 discharges the round-65 frozen
admission order (D4 of the round-65 closure): the orchestrator-dispatched
64-seat wave ruled on the C05 candidate; the L1 adjudicates, flips the README
C05 row the mandated direction, marks the retained candidate, and re-measures
on the committed tip. C2 lands the last two unguarded `receipt_ok` conjuncts
(routed by R64ReviewSeparability; named in the round-65 planned line).

## Round-65 wave adjudication (input, re-verified this round)

The orchestrator-dispatched v2 wave of exactly 64 seats (spec
`.ufo/waves/round-65/wave-spec.json`, `plan` exit 0, 64/64 reports landed,
zero dead) produced these gate authorities, re-verified by this L1 against
committed bytes at claim base `8214e4dd`:

- Q01 PASS, Q03 PASS, Q04 PASS, Q05 PASS, Q07 PASS, Q09 PASS, Q10 PASS,
  Q12 n/a-correct, Q13 PASS — named seats `.ufo/waves/round-65/R65ReviewEntryQ*.md`.
- **Q02 FAIL** (`.ufo/waves/round-65/R65ReviewEntryQ02.md`): S039 anchor "line 5"
  resolves to `older server.`; the quote sits at snapshot line 7; enum range
  :239-250 misses `RES_XML_RESOURCE_MAP_TYPE` at :253; entry:41's
  `payload_first16_hex` is not the recheck output.
- **Q06 FAIL** (`.ufo/waves/round-65/R65ReviewEntryQ06.md`): one quoted fixture
  premise does not reproduce — entry:41 `4d616e696673742d56657273696f6e`
  (15 bytes, "Manifst-Version") vs readout output
  `4d616e69666573742d56657273696f6e` (16 bytes, "Manifest-Version").
- **Q11 FAIL** (`.ufo/waves/round-65/R65ReviewEntryQ11.md`): entry:41's recorded
  output line is not what its stated deriving command prints (same defect).
- **Q08 superseded by Q11** (QUALITY.md:23); the Q-map's missing Q08 row is a
  separate documented nit (R65ReviewEntryQ04/Q12), not a missing criterion.
- Outside-discernment spot-check `R65SpotcheckDiscern.md`: **REJECT** the
  candidate at its current bytes (Q11, entry:41); AGREE the two retained
  rejected candidates stay rejected.
- Off-criterion corroboration: R65MutEntry FAIL (pristine entry misquotes the
  same readout field), R65CriticEntryDeps FAIL (item-8 false-provenance
  cross-reference + two silent value dependencies), R65EntryQmapDraft FAIL
  (dangling `### Code` / stdout pointers), R65ReviewSourcesTier FAIL
  (S038 cited outside declared scope at entry:71/:126; item-9 dex semantics
  on no registry row), R65SimplifierDrift PASS-with-one-sentence.

L1 re-verification at claim base `8214e4dd` (commands in the report):
`python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'`
prints `payload_first16_hex: 4d616e69666573742d56657273696f6e`; entry:41
records `4d616e696673742d56657273696f6e` — the FAIL is real on committed
bytes. Snapshot line checks re-verified: S039 quote at line 7 (not 5);
`RES_XML_RESOURCE_MAP_TYPE` at ResourceTypes.h:253; zipfile-docs.html title is
"Python 3.15.1 documentation" (S040 row says 3.15.0). **C1 of round 65 is
FALSIFIED; the frozen order's falsification branch applies.**

## Claims

**C1 — coverage, README C05 adjudicated disposition (lowest non-retired axis,
8/14 = 5.7).** Per `reports/round-65/claims.md:110-123` step 3, on
falsification the C05 row flips `frontier → uncovered`. Frozen after-state:
`K_ROW C05 status=uncovered` AND `C05_REJECTED_MARKED=yes` AND
`K_HELD=K_HELD_BACKED=K_HELD_BACKED_STRICT=8/14` AND
`README_TOKEN_LEGEND_MISMATCH=0`. `K_HELD` is unchanged by construction (the
claim is the honest adjudicated-negative move on the named coverage-map
surface, not held ground); a tree that flips `held` while the gate failed, or
leaves `frontier`/no marker, misses the after-state. The retained candidate
`corpus/knowledge/round-65-apk-axml-byte-evidence.md` is marked
`admission-status: rejected` naming the failing seats; its other bytes are
preserved verbatim as rejected evidence (retention precedent: the round-61
rejected candidates on C04/C09). README C05 names the fixture under work
evidence and the retained candidate as rejected; `## Frontier` C05 prose is
refreshed in the same revision (round-64 routed item: C05 prose refresh at
disposition time). No other coverage-map row changes status.

**C2 — calibration, new criterion C6 (receipt exit_code + fixture_sha256
guards):** `C6_RECEIPT_KILLED_ATTRIBUTED` **0/4 → 4/4** by exactly two in-script
controls per script in `corpus/verify_icon_languages.py` and
`corpus/verify_multi_icon_states.py`, appended after the existing
forged-evidence control: deep-copy the receipt, set `forged['exit_code']=1`,
`require(not receipt_ok(...))` message ending `forged receipt exit accepted`;
deep-copy, set `forged['fixture_sha256']=H(b'')`, `require(not receipt_ok(...))`
message ending `forged receipt fixture accepted`. Frozen mutation (the round's
own kill rule), one per conjunct: delete exactly the conjunct
`receipt['exit_code']==0` or `receipt['fixture_sha256']==expected_hash` (each
with its connecting `and`) from `receipt_ok` — regexes
`receipt\['exit_code'\]\s*==\s*0` and
`receipt\['fixture_sha256'\]\s*==\s*expected_hash`, exactly one match per
script each — run `--self-test` on a fresh tree copy; a kill is **attributed**
iff the mutant exits non-zero and its last output line ends with that
conjunct's marker. Red-before: all four mutants exit 0 at base (control
receipt below). `C6_CONTROL_PRESENT` is the anti-spoof guard: it greps the
landed script bytes for each control's attribution string, so a tree printing
kills without landing the controls cannot satisfy the after-state.

## Frozen counter and red-before

Counter: `reports/round-66/measure.py` (extends the round-65 probe; all
round-65 labels and formulas unchanged; new labels: `C05_REJECTED_MARKED`,
`C6_CONTROL_PRESENT`, `C6_CONTROLS_PASS`, `C6_RECEIPT_KILLED`,
`C6_RECEIPT_KILLED_ATTRIBUTED`, `HOLDS_OK_V4`; `K_ROW C05` re-used as the
disposition readout). Do-nothing control: `reports/round-66/measure-before.log`,
measured over `git archive 8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0 corpus`
with the round-66 probe — a tree with no adjudication and no C6 work, so it
meets neither after-state.

Expected red-before lines (C1): `K_ROW C05 status=frontier`,
`C05_REJECTED_MARKED=no`, `K_HELD=8/14`, `K_HELD_BACKED=8/14`,
`K_HELD_BACKED_STRICT=8/14`, `README_TOKEN_LEGEND_MISMATCH=0`.
Expected red-before lines (C2): `C6_CONTROL_PRESENT=0/4`,
`C6_CONTROLS_PASS=4/4` (unmutated scripts pass), `C6_RECEIPT_KILLED=0/4`,
`C6_RECEIPT_KILLED_ATTRIBUTED=0/4` — the C6 mutants delete conjuncts that no
existing control exercises, so self-tests exit 0. After: `4/4`, `4/4`, `4/4`,
`4/4`; `HOLDS_OK_V3=yes` → `HOLDS_OK_V4=yes`.

## Claim sizing and controls (fleet lesson conformance)

- After-states re-derive from committed bytes with one command:
  `git archive <commit> corpus | tar -x -C <tree> && python3 -B reports/round-66/measure.py <tree>`.
- Do-nothing control: the before-log above (a tree with no claimed work meets
  neither target).
- C1 names its surface (README C05 disposition) and the command that shows it
  unmoved (`K_ROW C05 status` + `C05_REJECTED_MARKED`); its verdict is the
  mandated adjudicated flip, honestly negative — no admission is claimed.
  C2 is a calibration guard on the last two `receipt_ok` conjuncts
  (C2/C3/C4/C5 chain continuation), not a re-score.
- One round, two claims, distinct axes (coverage / calibration), causally
  separable: C1 touches README + the candidate's status line + lesson/SOURCES;
  C2 touches two verifier scripts only; the probe lines are independent.

## Registered (not scored) work this round — wave-routed defect dispositions

Declared before data; each names its wave finding:

1. C06/C07 retained header repair (R65ScoutReadme FAIL §C): the admitted
   entries `round-63-zip-central-directory-evidence.md` and
   `round-64-firmware-region-byte-evidence.md` still say
   `admission-status: candidate`; flip each to `admitted` (admissions are on
   record in lessons/round-63.md:188-192 / round-64.md:258-266). Counter-neutral.
2. S043 supersedes S039 (D2 + R65ReviewSources F1): re-open the pinned
   snapshot; anchor `lines 7-8`. S039 stays immutable history.
3. S044 supersedes S040 (R65ReviewSources F2): retitle the bound bytes
   Python 3.15.1 (not 3.15.0); status `queued` carries over.
4. `## Search log` note(s) for the round's bounded searches (R65ReviewSources
   F3 found none written for round 65): one retro note for round 65's opens
   plus one for round 66's re-opens.
5. S042 own-work row: the round-65 wave finding corpus (64 reports under
   `.ufo/waves/round-65/`) — the evidence C1 adjudicates on.
6. `SKILL.md` currency refresh (R65ReviewSkillCites FAIL): bounded E1–E9-style
   corrections for the landed C5/C6 controls, the round-66 instrument, and
   the M37–M40 ids — the sections the finding names, nothing more.
7. Carried-forward erratum (D1): the round-65 report's seat mix "scribe 3"
   is corrected to **scribe 4** (committed spec: reviewer 20, critic 10,
   executor 10, scout 9, mutation-tester 7, scribe 4, sentinel 1,
   simplifier 1, revenger 1, connector 1; 64/64 delivered).

Routed forward (not landed this round): counter label-spoof surface
(R65CriticCounter — AST-bound counter debt continues); generator conditional
symlink escape (R65SentinelScope — fixture bytes are sha-pinned, cannot change
without breaking the pin; documented limitation); evidence-id transplant
prongs (a)/(b)/(d) and the injectivity registry (R65RevengerLedger);
one-sided endswith attribution asymmetry (R65LabAttribution); the
verbatim-output-diff gate proposal for quoted entry outputs (R65ReviewEntryQ02
recommendation — candidate for a future registered counter).

## Admission order (this round)

1. Pre-registration lands first (this file + probe + red-before receipt).
2. Adjudication + build: C05 `frontier → uncovered`, candidate marker,
   `## Frontier` prose refresh, C6 controls, registered dispositions, lesson,
   SOURCES rows S042–S044, SKILL.md refresh — one revision (the flip and the
   Gate record land together, per the round-63/64 marker discipline).
3. Measure on a committed archive at the final tip; `HOLDS_OK_V4=yes` and
   probe exit 0 required at round end.
4. Wave evidence commitment: the 64 round-65 seat reports land under
   `.ufo/waves/round-65/` in the same revision as the adjudication (inherited
   orchestrator-dispatched artifacts; committing them is preservation, not
   authorship). A fresh round-66 wave spec is prepared and validated under
   `.ufo/waves/round-66/` for the orchestrator's between-round dispatch.

## Frontier step conformance

- Census before: exit 0 (41 rows ending S041; four disclosed W04s
  S024/S028/S029/S034). Census after must exit 0 with rows 41 → 44
  (+S042 own-work, +S043 supersedes S039, +S044 supersedes S040).
- At least one sourced claim: C1 rests on S042 (the dispatched wave's gate
  corpus, opened this round).
- Mistakes mined in `corpus/lessons/round-66.md` `## Mistakes`: M39
  (number-drift — quoted output line transcribed, not reproduced: entry:41,
  captured-by Q11), M40 (number-drift/anchor — lesson located-quote pointers
  stated from intent: S038 span, S039 line, S040 word count, captured-by the
  round-lesson located-quote rule), plus the misroot disposition note.
- Rejected evidence preserved: the C05 candidate keeps every byte except the
  `admission-status:` line; fixture, oracle, readout, sources and the wave
  corpus stay committed and cited.
