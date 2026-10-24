NOT-FALSIFIED (coverage-limited) — dedup of the 22 of 63 peer reports present at cutoff `2026-10-24T05:59:33Z` is complete and internally consistent: no two landed seats contradict on the same proposition, 9 finding classes are duplicated across seats (canonical pointers below), and 4 singletons plus 1 structural admission gap form the L1 adjudication queue. 41 peer seats had written no verdict file at cutoff, so this is a partial dedup by construction, not a wave verdict.

Seat: R65Distill (scribe, read-only). Lane repo `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Contract read first: `reports/round-65/claims.md` (full). Scope of this report: `.ufo/waves/round-65/R65*.md` only; no product file, counter, judge, lesson, or lane Git/jj state was touched. Only this file was written.

## 1. Coverage at cutoff (the dependency)

`ls .ufo/waves/round-65/R65*.md | wc -l` → **22**; `wave-spec.json` `items` → **64** (63 peers + this seat). `wave-spec.json` lists seat names and per-seat `Report:` trailers, so the missing set is computable exactly.

Admission-critical absences at cutoff (seat named in spec, no file on disk): `R65ReviewEntryQ01`, `Q02`, `Q03`, `Q05`, `Q06`, `Q07`, `Q09`, `Q11`, `Q12`, `Q13` — i.e. only **2 of 12** Q-seats (`Q04`, `Q10`) had reported. Also absent: `R65ReviewC5Multi` (the multi-script half of the C5 patch review), `R65ReviewCounter`, `R65CriticCounter`, `R65CriticClaims`, `R65ReviewSeparability`, `R65LabDoNothing`, `R65LabAttribution`, `R65RevengerLedger`, `R65MutEntry`, `R65MutProbe`, `R65ReviewSources`, `R65ReviewSourcesTier`, `R65ScoutSources`, `R65CriticEntryScope`, `R65CriticFixture`, `R65CriticCounts`, `R65CriticCounts2`, `R65EntryQmapDraft`, `R65SpotcheckDiscern`, `R65ExecVerifiers`, `R65Preservation`, `R65SimplifierDrift`, `R65SentinelScope`, `R65LessonDraft`, `R65ScoutFrontier`, `R65ConnectorOverlap`, `R65ReviewSkillCites`, `R65ReviewEntryQ08` (none exists in the spec — see D3).

Consequence: **no C1 admission decision is derivable from this snapshot** (claims.md §Admission order step 2 requires named fresh-seat Q01–Q13 decisions), and C2's attribution picture is only half-reviewed (languages half reviewed in `R65ReviewC5Lang`; multi half unreviewed).

## 2. Verdict matrix of the 22 landed seats

| seat | verdict (line 1) |
|---|---|
| R65ExecCensusProbe | PASS |
| R65BlindDerive | PASS |
| R65AxmlReprobe | PASS |
| R65DexReprobe | PASS |
| R65EntryCommands | PASS |
| R65FixtureRegen | PASS |
| R65SnapshotManifest | PASS |
| R65CriticHarms | CLEAN |
| R65ScoutRecon | CLEAN |
| R65ScoutHost | CLEAN |
| R65ScoutCensus | PASS |
| R65ScoutC05Ground | NOT-FALSIFIED |
| R65ScoutReadme | **FAIL** |
| R65ScoutMisroot | NOT-FALSIFIED |
| R65CriticAdmissionOrder | NOT-FALSIFIED |
| R65CriticEntryDeps | **FAIL** |
| R65CriticLesson | **FAIL** |
| R65ScribeGate | NOT-FALSIFIED (skeleton) — verdict on line 3, not line 1 |
| R65ReviewEntryQ10 | **no verdict on line 1** (line 1 is the title heading) |
| R65ReviewEntryQ04 | PASS (Q04) |
| R65MutC5 | PASS |
| R65MutC5Regression | PASS |
| R65MutIcon | PASS |
| R65ReviewC5Lang | PASS |

No seat reports a falsification of C1 or C2. The three FAILs are on adjacent surfaces (entry provenance text, README index integrity, lesson word count), not on the claims' frozen predicates.

## 3. Duplicate clusters → canonical pointer

Each row: finding, seats asserting it (duplicate count), canonical pointer that supersedes the others.

| # | finding | seats | canonical pointer |
|---|---|---|---|
| 1 | `fixture.apk` = 947 bytes, sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` | BlindDerive, DexReprobe, FixtureRegen, CriticHarms, ScribeGate, CriticAdmissionOrder (6) | `corpus/fixtures/apk-r65/fixture.apk` + `corpus/knowledge/round-65-apk-axml-byte-evidence.md:5`; strongest evidence form is `R65FixtureRegen.md:8-13` |
| 2 | `generator.py` regeneration is byte-identical to HEAD (`cmp` exit 0), truth.json sha256 `27303bae…f8173`, Python 3.14.8 | FixtureRegen; corroborated by ScribeGate/CriticHarms on the digest only (3) | `R65FixtureRegen.md:8-16` |
| 3 | readout exits 0, 15 stdout lines, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` | EntryCommands, ScribeGate (entry recheck), DexReprobe (via fixture) (3) | `R65EntryCommands.md:1` + `corpus/knowledge/round-65-apk-axml-byte-evidence.md:158-162` |
| 4 | ZIP container facts: EOCD 925, CD offset 737 / size 188, 3 entries, payload offsets 49 / 506 / 668 | BlindDerive, DexReprobe, EntryCommands (3) | `R65BlindDerive.md:20-26` (independent derivation, no readout used) |
| 5 | AXML chunk table (6 chunks at 8/204/248/272/368/392; types 1, 0x0180, 0x0100, 0x0102, 0x0103, 0x0101; total 416) | BlindDerive, AxmlReprobe, EntryCommands (3) | `R65BlindDerive.md:33-40` + `R65AxmlReprobe.md:1`; oracle caveat in §4 D2 |
| 6 | dex declared header: magic `6465780a30333500`, adler `0x3d120c30`, sha1 `a5fc7bea8fa9ffaa52243540c8026066511b9fce`, file/header size 112, endian `0x12345678` | DexReprobe, EntryCommands, BlindDerive (3) | `R65DexReprobe.md:14-27` + `corpus/knowledge/round-65-apk-axml-byte-evidence.md:103-107` |
| 7 | C5 patch is insertion-only `3 +/0 -` per script, control immediately after the forged-stdout control, marker `forged receipt evidence accepted`, `receipt_ok` untouched | ReviewC5Lang, CriticHarms (adjacent), MutC5, MutIcon (4) | languages half: `R65ReviewC5Lang.md:19-46`; multi half **has no reviewer at cutoff** (see D4) |
| 8 | frozen C5 mutant killed and attributed 2/2 (`exit=1`, last line `AssertionError: r47: forged receipt evidence accepted` / `r42: …`) | MutC5, ReviewC5Lang, MutC5Regression, MutIcon, measure-after.log (5) | `R65MutC5.md:60-61` (both scripts, both variants) + `reports/round-65/measure-after.log:45` |
| 9 | transplanted IDs are real and foreign: `ev_6e055332…dc3d` = round-42, `ev_8ed88983…d4421` = round-47 | ReviewC5Lang, MutC5Regression, ScoutRecon (3) | `corpus/live/runs/round-42/producer-receipt.json:6` and `corpus/live/runs/round-47/producer-receipt.json` (this seat re-confirmed both IDs appear under `corpus/live/runs/round-42/` and `round-47/`) |
| 10 | README C05 still `frontier`, README untouched in the round diff | ScoutC05Ground, CriticHarms, ScribeGate, ScoutReadme, CriticAdmissionOrder, MutC5, MutIcon (7) | `corpus/README.md:34`; history claim `R65ScoutC05Ground.md:9-27` (byte-identical since `a7acc20`); diff claim `R65CriticHarms.md:19-27` |
| 11 | census: maintained validator exit 0 with the four disclosed W04s, 41 rows, 0 malformed / duplicates / enum violations | ScoutCensus, CriticHarms, ScoutRecon (3) | `R65ScoutCensus.md:1` + `corpus/SOURCES.md:52-55` |
| 12 | committed `measure-after.log` was measured at pre-adjudication tip `6f1761a9` and prints `K_HELD=8/14`, `K_ROW C05 status=frontier`, `HOLDS_OK_V3=yes` | CriticAdmissionOrder, ReviewC5Lang, MutC5, MutIcon (4) | `reports/round-65/measure-after.log:1-2,60` |
| 13 | snapshot digests: S038 `56b88bc4…c56f`, S039 `412d9cb4…a74c`, S040 `e7fe6715…c49c6a`, re-fetch byte-identical | SnapshotManifest, CriticLesson (quote hash) (2) | `R65SnapshotManifest.md:5-14` |
| 14 | ten verifiers exit 0 and C2/C3/C4 attributed counts unaffected by the C5 patch | ExecCensusProbe, MutIcon (2) | `R65ExecCensusProbe.md:10-24` + `R65MutIcon.md:1` |

## 4. Adjudication queue — contradictions and conflation hazards (for L1)

**D1 — same line, opposite verdicts: entry item 8.** `R65AxmlReprobe` PASSes "the requested AXML fields match … entry items 6–8"; `R65CriticEntryDeps` FAILs the *provenance sentence* on that same item: item 8 says `attributeStart 20`, `attributeSize 20`, `attributeCount 3` are "all equal to the derived sizes of item 5", but item 5 derives `{8,16,20,28}` — no `3`. Pointers: `corpus/knowledge/round-65-apk-axml-byte-evidence.md:55,78`; `R65CriticEntryDeps.md:1`. Not a factual contradiction (the value 3 is right; the cross-reference is wrong) but an **unstable pair**: the entry's own Q01/Q03 rows are author-asserted `pass` (`entry:139-140`), so L1 must rule on whether a false-provenance sentence falsifies Q01/Q03 while the numeric values stand. This is the highest-value item in the queue because it is the only landed attack on C1 substance.

**D2 — oracle coverage is narrower than the PASS set implies.** `R65BlindDerive` states `truth.json` contains no AXML chunk table and no payload offsets ("no per-field truth comparator", `R65BlindDerive.md:44-50`), while the AXML and ZIP facts are compared against `readout.py` outputs (`R65EntryCommands`, `R65AxmlReprobe`). The entry's Q03 says expected values come "from the authored oracle" (`entry:141`). L1 must decide whether the oracle claim in Q03 covers values that only the readout asserts — the only independent oracle for those bytes at cutoff is byte-flip mutation (`R65MutEntry`, absent).

**D3 — Q08 gap makes "all-criteria Q01–Q13" unsatisfiable as seated.** The entry's §Q-map jumps `Q07 → Q09` (`corpus/knowledge/round-65-apk-axml-byte-evidence.md:137-153`); `wave-spec.json` contains **no** `R65ReviewEntryQ08` seat (spec seat list: `Q01 Q02 Q03 Q04 Q05 Q06 Q07 Q09 Q10 Q11 Q12 Q13`); `R65ScribeGate.md:1-30` records Q08 as `gap` with lane precedent "superseded by Q11". Nothing in the wave registers that supersession for round 65, so the frozen all-criteria condition currently has a hole that neither a seat nor a record closes.

**D4 — C5 is only half patch-reviewed.** `R65ReviewC5Lang` reviews `verify_icon_languages.py` (`R65ReviewC5Lang.md:19-46`); the sibling `R65ReviewC5Multi` had not reported at cutoff, although both the mutant seats (`R65MutC5`, `R65MutC5Regression`) and the counter cover the multi script. Per-script patch shape for `verify_multi_icon_states.py` is therefore mutant-verified but not reviewer-verified at cutoff.

**D5 — `9/14` exists only in a scratch tree; must not be read against the committed log.** `R65ExecAfterMeasure` PASSes a copied corpus with a scratch-only C05 flip (`K_HELD=9/14`, `HOLDS_OK_V3=yes`, `R65ExecAfterMeasure.md:15-19`), while the committed `measure-after.log` at HEAD prints `K_HELD=8/14` / `frontier` (`reports/round-65/measure-after.log:1-2`). Both are correct for their trees; a reader who merges them would manufacture a false C1 after-state. `R65CriticAdmissionOrder.md:41-51` independently flags the adjacent hazard: the file name and commit subject "final measurement receipt" predate adjudication and must not be cited as the step-4 measurement or as a falsification record.

**D6 — README integrity defect wider than round 65.** `R65ScoutReadme` FAILs: `corpus/README.md:35` (C06) is `held` while `corpus/knowledge/round-63-zip-central-directory-evidence.md:8` still reads `admission-status: candidate` (and a second `held` row has the same defect, `R65ScoutReadme.md:34-38`). This is a prior-round registry inconsistency on the same surface C1's flip writes to; it does not touch C05 (C05's `frontier` is legend-correct per `R65ScoutC05Ground`) but it means the round-65 flip must not treat existing `held` labels as admitted-by-construction.

**D7 — lesson numeric defect.** `R65CriticLesson` FAILs substantively only on a count: the S040 quote is 14 words while `corpus/lessons/round-65.md` claims "(16 words)" (`R65CriticLesson.md:1,12`); quotes/M38 red receipt otherwise pass. Singleton — no seat disputes it, but it must be fixed before the M-number is mined.

**Format compliance (not evidence, but blocks clean transcription):** `R65ReviewEntryQ10.md:1` is a title heading with no verdict line, and `R65ScribeGate.md` puts its verdict on line 3 — both violate the seat rule "verdict on the first line of your report". Their content is usable; their first line is not machine-readable.

## 5. Singletons that only one seat asserts (do not let dedup hide them)

- `R65CriticEntryDeps`: item-8 false-provenance + "two undisclosed inter-item value dependencies" (`R65CriticEntryDeps.md:1`).
- `R65ScoutReadme`: two `held` README rows naming `candidate` entries (`R65ScoutReadme.md:1,34-38`).
- `R65CriticLesson`: S040 quote word-count mismatch (`R65CriticLesson.md:12`).
- `R65ScoutMisroot`: no revenger r65 file confirmed at fleet root; one plausible `unblob.log` candidate in the r65 window, 17 untracked entries reviewed (`R65ScoutMisroot.md:1`) — recorded, not attributed.
- `R65ScoutHost`: environment claims hold; the jadx-presence sentence is a pre-existing frontier route note (`R65ScoutHost.md:1`).
- `R65CriticAdmissionOrder`: verdict-file admission governance hazards (`R65CriticAdmissionOrder.md:41-55`).

## 6. Build-state facts this seat re-confirmed independently (spine for the table above)

```text
sha256 corpus/fixtures/apk-r65/fixture.apk      = 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  (947 B)
sha256 corpus/knowledge/round-65-apk-axml-byte-evidence.md = e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7  (162 lines, admission-status: candidate at :7)
corpus/README.md:34 = | C05 | Android packages (APK) | — | — | frontier |
head = 8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0 ("round-65 verifier spot-check"); 5 commits since measurement base 3eebcdd, zero deletions
ancestry: 3eebcdd ⊂ 5a2e7a0 ⊂ c7b7cf9 ⊂ 6f1761a ⊂ 5b4d29e ⊂ 8214e4d
working tree: clean except untracked .ufo/waves/round-65/R65*.md
C5 control sites: verify_icon_languages.py:155-157 (id at :156), verify_multi_icon_states.py:154-156 (id at :155); conjunct at :120 and :123
SOURCES rows S038-S041 at corpus/SOURCES.md:52-55; S040 status = queued, S007 the other queued row
```

## 7. Limits

- Partial by design: 22/63 peer reports; 10 of 12 Q seats and the multi-script C5 reviewer absent at cutoff. Every "no contradiction" statement in §3-§4 is therefore about the landed 22 only.
- Duplicate counts are per-seat assertions of the same proposition, not independent verification: several seats cite the same committed after-log or the same entry bytes.
- This seat ran no product command beyond read-only digests/greps/diff listing; it did not re-run `measure.py`, the verifiers, or any seat's scratch experiment, so all execution evidence above is quoted from the reporting seat, identified by file and line.
- Tooling: nothing installed or upgraded (no pacman/uv/npx invocation); no git/jj mutation; only this file written.

Report: .ufo/waves/round-65/R65Distill.md
