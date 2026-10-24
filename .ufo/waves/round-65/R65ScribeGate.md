# R65ScribeGate — report

REJECT — C1 is falsified by named fresh-seat Q decisions on the present entry
bytes (Q02 FAIL, Q06 FAIL, Q11 FAIL, all citing `payload_first16_hex` at entry
line 41 or unresolvable anchors) and by five further seat failures/rejections
(SpotcheckDiscern REJECT, MutEntry, CriticEntryDeps, ReviewSources,
ReviewSourcesTier), while C2's frozen attribution reproduces 2/2 with both patch
reviewers passing, no-harm 2/2/2/2, and separability PASS in both directions;
4 of 63 peer verdict files were absent at the final scan and are listed as
dependencies, not inferred.

Seat: scribe `revenger-r65.R65ScribeGate`, round 65 attempt 1 (hyaku).
Date: 2026-10-24. Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Scan directory: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/`.
No lesson edit (the addendum below is a draft for L1 to append after
`corpus/lessons/round-65.md:19-22`).

## 1. Addendum draft (deliverable)

```markdown
## Gate admission-decision addendum (wave revenger-r65-v2, scribe R65ScribeGate)

Evidence base: the wave verdict files under `.ufo/waves/round-65/`, scanned
at this scribe's final pass; 59 of 63 peer seats had published, 4 had not and
are named in §Pending seats. A pending row is not evidence of either outcome.

### C1 — `corpus/knowledge/round-65-apk-axml-byte-evidence.md`, README C05

| criterion | seat | verdict | verdict file |
|---|---|---|---|
| Q01 | R65ReviewEntryQ01 | **pending** (no file at final scan) | `.ufo/waves/round-65/R65ReviewEntryQ01.md` (absent) |
| Q02 | R65ReviewEntryQ02 | **FAIL** — S039 line anchor and S038 enum range do not resolve to the named text, and the MANIFEST.MF transcribed line does not reproduce | `.ufo/waves/round-65/R65ReviewEntryQ02.md` |
| Q03 | R65ReviewEntryQ03 | PASS — every expected value byte-derived at check time or pinned outside the record | `.ufo/waves/round-65/R65ReviewEntryQ03.md` |
| Q04 | R65ReviewEntryQ04 | PASS | `.ufo/waves/round-65/R65ReviewEntryQ04.md` |
| Q05 | R65ReviewEntryQ05 | PASS (`ADMIT (Q05 PASS)`) — no readiness/capability claim; one flip-time README defect (F1) required in the same commit | `.ufo/waves/round-65/R65ReviewEntryQ05.md:3` |
| Q06 | R65ReviewEntryQ06 | **FAIL** — one quoted fixture premise does not reproduce (`:41`, MANIFEST.MF `payload_first16_hex`) | `.ufo/waves/round-65/R65ReviewEntryQ06.md:3` |
| Q07 | R65ReviewEntryQ07 | PASS — no parser/provider prediction; four fenced sites | `.ufo/waves/round-65/R65ReviewEntryQ07.md` |
| Q08 | (no seat dispatched) | **GAP — no Q-map row in the entry**; lane precedent `superseded by Q11` (`corpus/knowledge/commonjs-destructured-require-edges.md:203`, `corpus/knowledge/evm-saved-interface-candidates.md:190`); corroborated by `R65ReviewEntryQ12`'s finding | entry `corpus/knowledge/round-65-apk-axml-byte-evidence.md:138-152` |
| Q09 | R65ReviewEntryQ09 | PASS — 16/16 digest-bearing sentences resolve to the bytes claimed | `.ufo/waves/round-65/R65ReviewEntryQ09.md` |
| Q10 | R65ReviewEntryQ10 | PASS (three LOW pointer defects; edit invalidates the decision) | `.ufo/waves/round-65/R65ReviewEntryQ10.md` |
| Q11 | R65ReviewEntryQ11 | **FAIL** — item 3's `member[META-INF/MANIFEST.MF]` line is not what its stated deriving command prints (15-byte `Manifst-Version` vs 16-byte `Manifest-Version`) | `.ufo/waves/round-65/R65ReviewEntryQ11.md` |
| Q12 | R65ReviewEntryQ12 | PASS (correctly n/a; no rejected row cited) | `.ufo/waves/round-65/R65ReviewEntryQ12.md:3` |
| Q13 | R65ReviewEntryQ13 | PASS (no verifier credited) | `.ufo/waves/round-65/R65ReviewEntryQ13.md:3` |

Additional C1 failures on the present bytes (not Q rows, but admission-blocking
under the contract's "all-criteria" and tier rules):

- `R65CriticEntryDeps` **FAIL** — item 8 (`:78`) claims `attributeCount=3` is
  "equal to the derived sizes of item 5", but item 5 emits `{8,16,20,28}`; item
  8 also silently consumes item 6's string table and item 7's resource map, and
  item 7 silently consumes item 6's strings (F1–F3).
- `R65EntryQmapDraft` **FAIL** — three internal inconsistencies in the
  candidate: cited `### Code` block and "15-line stdout reproduced there" do
  not exist in §Reproduce; `attributeCount 3 — all equal to the derived sizes`;
  self-contradictory statement.
- `R65ReviewSources` **FAIL** — S038 PASS, **S039 FAIL** (anchor cited `:5`,
  quote at `:7`), **S040 FAIL** (row says CPython 3.15.0; the sha256-bound
  snapshot is 3.15.1), S041 PASS, plus the contract-v1 rule-5 search-log note
  missing.
- `R65ReviewSourcesTier` **FAIL** — tier inflation on two rows: S038 cited
  outside its declared scope/anchors (`:71`, `:126`), and the DEX-header field
  semantics at `:103` rest on no registry row.
- `R65ScoutReadme` **FAIL** (README-index level, pre-existing): `held` rows C06
  and C07 name entries whose headers still say `admission-status: candidate` —
  not introduced by C1, but it means the README flip commit cannot claim a
  clean index without adjudicating those two rows.

Supporting C1 evidence that PASSed (fixture/oracle/readout layer is sound):
`R65FixtureRegen` PASS (byte-exact regeneration at HEAD `8214e4dd`),
`R65BlindDerive` PASS, `R65AxmlReprobe` PASS, `R65DexReprobe` PASS,
`R65CriticCounts` NOT-FALSIFIED (60+ numbers re-derived independently, zero
discrepancies), `R65CriticCounts2` NOT-FALSIFIED (41 rows, A=39 C=2),
`R65CriticHarms` CLEAN, `R65Preservation` PASS, `R65ScoutCensus` PASS,
`R65ExecCensusProbe` PASS, `R65SnapshotManifest` PASS,
`R65ScoutC05Ground` NOT-FALSIFIED (C05 `frontier` since `a7acc20`),
`R65CriticEntryScope` NOT-FALSIFIED, `R65CriticAdmissionOrder` NOT-FALSIFIED,
`R65ScoutSources` PASS (enum names verbatim against S038),
`R65ScoutFrontier` PASS-WITH-REQUIRED-EDITS.

### C2 — C5 evidence-id transplant guard

| check | seat | verdict | file |
|---|---|---|---|
| patch shape, languages | R65ReviewC5Lang | PASS — insertion-only (3+/0-), one control immediately after forged-stdout, `receipt_ok` untouched | `.ufo/waves/round-65/R65ReviewC5Lang.md` |
| patch shape, multi | R65ReviewC5Multi | PASS — all shape checks, HEAD `8214e4d` vs base `3eebcdd` | `.ufo/waves/round-65/R65ReviewC5Multi.md` |
| frozen mutant attribution | R65MutC5 | PASS — 2/2 attributed, exit 1, last line ends `forged receipt evidence accepted` | `.ufo/waves/round-65/R65MutC5.md` |
| mutant specificity | R65MutC5Regression | PASS — foreign-real and fabricated IDs both rejected by pristine `receipt_ok`; conjunct-deletion mutant accepts both | `.ufo/waves/round-65/R65MutC5Regression.md` |
| no harm to C2/C3/C4 | R65MutIcon | PASS — attributed counts stay 2/2, 2/2, 2/2 | `.ufo/waves/round-65/R65MutIcon.md` |
| after-state reachable | R65ExecAfterMeasure | PASS — scratch C05 flip yields every target and exit 0 | `.ufo/waves/round-65/R65ExecAfterMeasure.md` |
| separability both directions | R65LabDoNothing | PASS — C2-only tree flips C5 0/2→2/2 with K fixed 8/14; C1-only tree flips K 8/14→9/14 with C5 fixed 0/2 | `.ufo/waves/round-65/R65LabDoNothing.md` |
| attribution-predicate sensitivity | R65LabAttribution | NOT-FALSIFIED for the after-state, **but** the rule is a one-sided exact-string tail test: a rewording of the same genuine control scores 1/2 unattributed while the probe exits 0, and a composed-marker tree with no evidence-id check scores 2/2 at `C5_CONTROL_PRESENT=1/2`, falsifying the anti-spoof sentence (`reports/round-65/claims.md:87-90`) | `.ufo/waves/round-65/R65LabAttribution.md` |
| verifier replay | R65ExecVerifiers | PASS — ten self-tests, calibration 4/4, replay 10/10 | `.ufo/waves/round-65/R65ExecVerifiers.md` |

### Decision text (L1)

- **C1 — falsified.** The frozen admission condition is named fresh-seat
  Q01–Q13 pass decisions on the entry; the wave record now contains explicit
  **Q02 FAIL, Q06 FAIL and Q11 FAIL**, all citing entry line 41 (MANIFEST.MF
  `payload_first16_hex` is not the readout's output) or unresolvable anchors,
  plus Q-map/seat gap Q08. Independent non-Q seats fail the same bytes
  (`R65SpotcheckDiscern` REJECT, `R65MutEntry`, `R65CriticEntryDeps`,
  `R65EntryQmapDraft`, `R65ReviewSources`, `R65ReviewSourcesTier`), and
  `R65ReviewSeparability` PASSes C1/C2 separability. Under
  `reports/round-65/claims.md` §Admission order step 3 the flip is therefore
  `corpus/README.md:34` `frontier → uncovered`; `K_HELD` stays 8/14 and no entry
  is named. A repair is possible (all defects are single-clause text edits over
  sound fixture/readout/oracle bytes: `R65FixtureRegen`, `R65BlindDerive`,
  `R65CriticCounts` all pass), but any entry edit invalidates the present
  decisions (`R65ReviewEntryQ10` residual risk; `R65ReviewEntryQ05` states the
  flip-time README defect must be corrected in the same commit), so a corrected
  entry needs fresh Q01–Q13 decisions before a `held` flip; no such re-review
  exists in this wave.
- **C2 — hold.** `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2` is reproduced on
  the landed scripts with attribution semantics, both patch reviewers pass, and
  the no-harm/separability receipts hold. Record the after-state on the final
  committed archive (`K_HELD=9/14` **only if** C1 is repaired-and-admitted;
  otherwise `K_HELD=8/14` with C05 `uncovered`), plus the LabAttribution
  one-sidedness as future-round debt on the attribution predicate
  (`HOLDS_OK_V3` may be printed `yes` by a composed-marker tree —
  `R65LabAttribution`).
```

## 2. Observed per-seat verdicts (59 of 63 peers)

Extraction command (cwd `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65`):
`for f in *.md; do grep -m1 -E '^(PASS|FAIL|CLEAN|NOT-FALSIFIED|ADMIT|REJECT)' "$f"; done`.

| seat | verdict | waves-file |
|---|---|---|
| R65AxmlReprobe | PASS | R65AxmlReprobe.md |
| R65BlindDerive | PASS | R65BlindDerive.md |
| R65ConnectorOverlap | NOT-FALSIFIED | R65ConnectorOverlap.md |
| R65CriticAdmissionOrder | NOT-FALSIFIED | R65CriticAdmissionOrder.md |
| R65CriticCounts | NOT-FALSIFIED | R65CriticCounts.md |
| R65CriticCounts2 | NOT-FALSIFIED | R65CriticCounts2.md |
| R65CriticEntryDeps | **FAIL** | R65CriticEntryDeps.md |
| R65CriticEntryScope | NOT-FALSIFIED | R65CriticEntryScope.md |
| R65CriticFixture | NOT-FALSIFIED | R65CriticFixture.md |
| R65CriticHarms | CLEAN | R65CriticHarms.md |
| R65CriticLesson | **FAIL** | R65CriticLesson.md |
| R65DexReprobe | PASS | R65DexReprobe.md |
| R65Distill | NOT-FALSIFIED (coverage-limited) | R65Distill.md |
| R65EntryCommands | PASS | R65EntryCommands.md |
| R65EntryQmapDraft | **FAIL** | R65EntryQmapDraft.md |
| R65ExecAfterMeasure | PASS | R65ExecAfterMeasure.md |
| R65ExecCensusProbe | PASS | R65ExecCensusProbe.md |
| R65ExecVerifiers | PASS | R65ExecVerifiers.md |
| R65FixtureRegen | PASS | R65FixtureRegen.md |
| R65LabAttribution | NOT-FALSIFIED (one-sided rule) | R65LabAttribution.md |
| R65LabDoNothing | PASS | R65LabDoNothing.md |
| R65MutC5 | PASS | R65MutC5.md |
| R65MutC5Regression | PASS | R65MutC5Regression.md |
| R65MutEntry | **FAIL** | R65MutEntry.md |
| R65MutIcon | PASS | R65MutIcon.md |
| R65Preservation | PASS | R65Preservation.md |
| R65ReadmeLegend | NOT-FALSIFIED | R65ReadmeLegend.md |
| R65ReviewC5Lang | PASS | R65ReviewC5Lang.md |
| R65ReviewC5Multi | PASS | R65ReviewC5Multi.md |
| R65ReviewEntryQ04 | PASS | R65ReviewEntryQ04.md |
| R65ReviewEntryQ10 | PASS | R65ReviewEntryQ10.md |
| R65ReviewEntryQ12 | PASS | R65ReviewEntryQ12.md:3 |
| R65ReviewEntryQ13 | PASS | R65ReviewEntryQ13.md:3 |
| R65ReviewSkillCites | **FAIL** (SKILL.md stale in five blocks) | R65ReviewSkillCites.md |
| R65ReviewSources | **FAIL** | R65ReviewSources.md |
| R65ReviewSourcesTier | **FAIL** | R65ReviewSourcesTier.md |
| R65ScoutC05Ground | NOT-FALSIFIED | R65ScoutC05Ground.md |
| R65ScoutCensus | PASS | R65ScoutCensus.md |
| R65ScoutFrontier | PASS-WITH-REQUIRED-EDITS | R65ScoutFrontier.md |
| R65ScoutHost | CLEAN | R65ScoutHost.md |
| R65ScoutMisroot | NOT-FALSIFIED | R65ScoutMisroot.md |
| R65ScoutReadme | **FAIL** | R65ScoutReadme.md |
| R65ScoutRecon | CLEAN | R65ScoutRecon.md |
| R65ScoutSources | PASS | R65ScoutSources.md |
| R65SentinelScope | FINDINGS (token outside the seat vocabulary) — scope inert/credential-free; conditional generator symlink escape | R65SentinelScope.md |
| R65SnapshotManifest | PASS | R65SnapshotManifest.md |
| R65SpotcheckDiscern | **REJECT** (entry at current bytes, Q11 line 41) | R65SpotcheckDiscern.md |
| R65ReviewEntryQ02 | **FAIL** | R65ReviewEntryQ02.md |
| R65ReviewEntryQ03 | PASS | R65ReviewEntryQ03.md |
| R65ReviewEntryQ05 | PASS (`ADMIT (Q05 PASS)`) | R65ReviewEntryQ05.md:3 |
| R65ReviewEntryQ06 | **FAIL** | R65ReviewEntryQ06.md:3 |
| R65ReviewEntryQ07 | PASS | R65ReviewEntryQ07.md |
| R65ReviewEntryQ09 | PASS | R65ReviewEntryQ09.md |
| R65ReviewEntryQ11 | **FAIL** | R65ReviewEntryQ11.md |
| R65ReviewSeparability | PASS (C1/C2 separable on the frozen counter) | R65ReviewSeparability.md |
| R65MutProbe | NOT-FALSIFIED (frozen recheck passes at base; 3 of 4 named self-consistency points are non-gating) | R65MutProbe.md |
| R65LessonDraft | **FAIL** (2 of 3 Gate quote locations false; S040 word count false) | R65LessonDraft.md |

Pending (no verdict file at final scan, 4): `R65ReviewEntryQ01`,
`R65CriticCounter`, `R65SimplifierDrift`, `R65RevengerLedger`.

## 3. Commands and outcomes (exact)

1. `read /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md`
   — frozen contract loaded in full (kill rule, predicate, admission order,
   registered counter repair).
2. `ls -la /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/`
   — first scan: `build-wave-spec.py`, `m38-red-before.log`,
   `plan-validated.json`, `wave-spec.json`, `source-snapshots/`, empty `briefs/`;
   **zero verdict `.md` files**.
3. Wave-spec parse (`python3` on `wave-spec.json`): `wave=revenger-r65-v2`, 64
   items, roles `{executor:10, scribe:4, scout:9, reviewer:20, critic:10,
   mutation-tester:7, sentinel:1, simplifier:1, revenger:1, connector:1}`; each
   brief carries `Report: .ufo/waves/round-65/<Name>.md`, so the seat name is
   the verdict-file basename.
4. Timed rescans of the scan directory: 2 files at first rescan, 10, 31, 36,
   39, 48, 50, **60 at final scan** (`ls -1 *.md | wc -l` → 60, including this
   report). Peer coverage by the same listing + wave-spec set difference:
   `peers 63 observed 59 missing 4`.
5. Verdict extraction per file: `grep -m1 -E '^(PASS|FAIL|CLEAN|NOT-FALSIFIED|ADMIT|REJECT)'`
   (table in §2; heading-first files were read at their verdict line — Q05 at
   `:3`, Q06 at `:3`, Q12 at `:3`, Q13 at `:3`).
6. Build-state digests (this seat, `sha256sum`):
   - `corpus/fixtures/apk-r65/fixture.apk` →
     `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`
     (947 B; matches the contract and every reprobe seat).
   - `corpus/knowledge/round-65-apk-axml-byte-evidence.md` →
     `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7`
     (162 lines; the same digest `R65MutEntry` and `R65ReviewEntryQ10` record).
   - `corpus/lessons/round-65.md` →
     `f55e34110a8b384d98db9b43faba04be94ec516e2f7dc7a8ccdb952fa6531626`.
7. `grep -n 'C05' corpus/README.md` → `34:| C05 | Android packages (APK) | — | — | frontier |`
   (not flipped) and `69:` the stale `## Frontier` C05 bullet;
   `R65ScoutFrontier` requires both rows edited in the admission commit.
8. C5 source pointers (`grep -n`): attribution strings at
   `corpus/verify_icon_languages.py:157` and
   `corpus/verify_multi_icon_states.py:156`; the frozen conjunct at
   `receipt_ok` bodies `:120` and `:123`, one match per script;
   mutant extraction/attribution in `reports/round-65/measure.py:260-306`
   (`C5_CLAUSE`, `mutate_c5` refusing `len(hits)!=1`, `C5_MARKER` tail match).
9. `read reports/round-65/measure-before.log` — red-before reproduced:
   `K_HELD=8/14`, `K_ROW C05 status=frontier`,
   `C5_CONTROL_PRESENT=0/2`, `C5_CONTROLS_PASS=2/2`, `C5_RECEIPT_KILLED=0/2`,
   `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=0/2`,
   `STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True`,
   `HOLDS_OK_V3=no`.

## 4. Gates

- Bounds: one write only, the brief-named report path; no git/jj mutation, no
  lesson/product/README/SCORECARD/LOG edit, no subagent dispatch, no tool
  installed or upgraded. PASS.
- Contract-first: `claims.md` read before any verdict statement. PASS.
- Verdict-file discipline: 59 peer files observed with pointers; 4 pending
  named rather than given a verdict; no seat's verdict is inferred from its
  role or from another seat. PASS.
- Pointer discipline: every scored row cites a verdict file (and line for the
  four heading-first files); every failure quoted carries the seat's own
  file:line. PASS.
- Admission-record completeness: **near reached** — Q01 alone of the thirteen
  criteria had no verdict file at final scan, and four non-Q seats were absent;
  the addendum's table records that explicitly rather than filling the rows.

## 5. Findings

1. **C1 fails on explicit named-seat Q decisions, not on inference.**
   `R65ReviewEntryQ11` FAIL, `R65ReviewEntryQ06` FAIL and `R65ReviewEntryQ02`
   FAIL all turn on entry `:41`: the quoted
   `"payload_first16_hex": "4d616e696673742d56657273696f6e"` is 15 bytes
   ("Manifst-Version") where the readout prints
   `"4d616e69666573742d56657273696f6e"` (16 bytes, "Manifest-Version").
   `R65SpotcheckDiscern` REJECTs the entry at its current bytes and
   `R65MutEntry` shows the admitted `recheck:` stdout hash cannot catch this
   class (it authenticates the readout's bytes, not the entry's quoted values);
   the entry's cited `### Code` block and 15-line stdout block do not exist
   (`grep -c '^### '` → 0).
2. **Conflict to be adjudicated, recorded verbatim.** `R65EntryCommands` says
   "16 commands executed; all 30 output lines matched; no mismatches", while
   `R65ReviewEntryQ02`, `R65ReviewEntryQ06`, `R65ReviewEntryQ11`,
   `R65SpotcheckDiscern` and `R65MutEntry` all find the `:41` line different
   from the readout's output. Five seats against one on the same entry digest
   (`e173e643…`); the canonical judge must resolve which extraction is correct,
   but the admission-blocking count is already on the FAIL side and Q13's
   reviewer independently confirms "entry line 41 is not verbatim readout
   output" after replaying the commands.
3. **Q08 remains a structure gap.** The entry's §Q-map has twelve rows
   (Q01–Q07, Q09–Q13); no Q08 row and no Q08 seat exist. Lane precedent records
   `superseded by Q11` (`commonjs-destructured-require-edges.md:203`,
   `evm-saved-interface-candidates.md:190`); `R65ReviewEntryQ12` independently
   flags the same gap. An "all-criteria Q01–Q13" sentence cannot be written from
   a twelve-row map.
4. **C2's after-state is real but its guard is one-sided.** `R65MutC5` (2/2
   attributed), `R65MutC5Regression` (specificity), `R65MutIcon` (no harm to
   C2/C3/C4), `R65LabDoNothing` (separability both directions), `R65ExecAfterMeasure`
   (exit 0 with all targets) all pass; `R65LabAttribution` nevertheless shows a
   genuine control reworded to `evidence forged` scores 1/2 unattributed with
   probe exit 0, and a composed-marker tree without an evidence-id check scores
   2/2 at `C5_CONTROL_PRESENT=1/2`. The frozen claim's own anti-spoof sentence
   (`claims.md:87-90`) is therefore falsified by a tree the counter can print.
   This belongs in the lesson's routed-forward debt, not in this round's score
   (the frozen predicate reproduced on the landed scripts).
5. **README work is larger than a single-token flip.** `R65ScoutFrontier`
   requires the admission commit to flip `corpus/README.md:34` **and** remove or
   rewrite the stale `## Frontier` C05 bullet at `:69-70` (and notes the
   pre-existing stale C07 bullet at `:63-66`). `R65ScoutReadme` fails the
   README index because C06/C07 are `held` while their entries still read
   `admission-status: candidate`. `R65ReadmeLegend` confirms a contract- and
   legend-consistent C05 edit exists.
6. **Lesson-level failures beyond the entry.** `R65CriticLesson` FAIL: three
   Gate quotes are verbatim and ≤25 words, but S038 cites lines 608-611 for a
   span at 607-609, S039 cites line 5 for a quote at 7-8, and S040 claims 16
   words against 14. `R65ReviewSkillCites` FAIL: `SKILL.md` is stale in five
   load-bearing blocks against the round-65 tree.
7. **Environment/scope checks are clean or bounded.** `R65ScoutHost` CLEAN
   (three environment claims verified), `R65ConnectorOverlap` NOT-FALSIFIED (no
   fleet report touches APK/C05; absence does not close the ADJ-06 question),
   `R65ScoutRecon` CLEAN, `R65ScoutMisroot` NOT-FALSIFIED (no confirmed misrooted
   seat file), `R65SentinelScope` FINDINGS (scope inert/credential-free; one
   conditional symlink escape in the generator's fixed output names).
8. **`R65SentinelScope` uses `FINDINGS`, outside the seat vocabulary.** Its
   file resolves and reports findings but its first-line token is not one of
   PASS/FAIL/NOT-FALSIFIED/ADMIT/REJECT/CLEAN; an adjudication token must be
   supplied or the seat re-run.

## 6. Known limits

- This seat makes no admission decision. The addendum's decision text is the
  L1-shaped conditional form the brief asks for, grounded in the verdict files
  observed at scan time; later files may change the C1 outcome (a corrected
  entry would need fresh Q decisions, not these).
- No counter run, mutant run, verifier run, census run or provider call by this
  seat. The printed numbers are from the frozen red-before log and from sibling
  seats' reports, attributed as such.
- Pending seats at final scan: `R65ReviewEntryQ01`, `R65CriticCounter`,
  `R65SimplifierDrift`, `R65RevengerLedger`. Their absence is recorded, not
  bridged; the C1 outcome does not depend on them (three explicit Q FAILs
  stand on their own records).
- No installs or upgrades (nothing was fetched; the pacman guard was not
  touched). Tools used: `read`, `write`, `bash` (`ls`, `grep`, `sed`, `head`,
  `sha256sum`, `python3 -B`).

## 7. Artifact paths

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/R65ScribeGate.md` (this report)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/` (49 read-only peer verdicts scanned)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md` (frozen contract)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure-before.log` (red-before)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure.py` (C5 block `:260-306`)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md` (sha256 `e173e643…`)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-65.md` (sha256 `f55e3411…`; not edited)
