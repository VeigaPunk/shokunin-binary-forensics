# round 71 — revenger (hyaku run 10)

author: RevengerR71 · base `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f` · frozen claims `reports/round-71/claims.md` · v6 build start `18200a4b18e8dfce291a74028a9012ce4401ca10` · final frozen candidate `4c1eeaee88fd07e442f1bd546faf77be3957d390` (entry SHA-256 `671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092`) · post-freeze corrections are separately identified below · no package installation.

## Gate — source curation and wave-1 pre-gate

### New SOURCES rows opened this round (CORPUS.md rule 1)

- **S052 — ADMIT for the C05 output-description claim (new own-work tier A row).** Command opened 2026-10-27 from the lane root: `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes` (exit 0; six `MATCH` lines). Located stdout quote from the `dex-format.html` match: `MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;`. It reports a snapshot file, first-line number, phrase-presence flag and phrase; it does not print the raw source line. Registry row S052 scope and entry item 11 are limited to that output shape. Final `used-by`: `corpus/knowledge/round-71-apk-axml-byte-evidence.md, corpus/lessons/round-71.md`.
- **S053 — REJECT as support for this C05 entry (new row, supersedes S044).** Source opened 2026-10-27: https://docs.python.org/3/library/zipfile.html, page title `zipfile — Work with ZIP archives — Python 3.15.2 documentation`, section introduction under `# zipfile — Work with ZIP archives`. Located quote: `This module provides tools to create, read, write, append, and list a ZIP file.` The official page is authoritative for the Python module's own API scope, but the C05 entry makes no `zipfile` API claim; its format/layout evidence rests on APPNOTE S032/S034 and direct fixture bytes. Flip: a future entry that relies on a located Python `zipfile` behavior claim may re-open and screen this source. Final `used-by=corpus/lessons/round-71.md`; the existing S044 row was not edited.

### Re-opened existing source rows

- S038: primary AOSP URL was re-opened by `R71W1OpenS038` on 2026-10-27. The reader returned a base64 body without a line-addressable live quote or a new digest; the quoted `attributeStart` phrase and enum anchors are located in the committed `corpus/snapshots/ResourceTypes.h` and derived by item 11. Live byte currency is not claimed.
- S048: `R71W1OpenS048`, 2026-10-27T15:21:21Z; live `header_item` checksum quote (14 words): `adler32 checksum of the rest of the file (everything but magic and this field)`; `header_size` quote (8 words): `must be 0x70 (112) bytes (v40 or earlier)`. The current reader returned rendered text, so no new byte-level digest is claimed.
- S032/S034: `R71W1OpenS032`, 2026-10-27T15:21:46Z; live APPNOTE bytes and committed `corpus/snapshots/APPNOTE.TXT` both SHA-256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`; `wc -c corpus/snapshots/APPNOTE.TXT` → 174585 bytes. Located quote at §4.3.16 line 634 (8 words): `end of central dir signature 4 bytes (0x06054b50)`.
- S049: `R71W1OpenS049`, 2026-10-27T15:21:38Z; `wc -c corpus/snapshots/rea-android-applications.md` → 1992 bytes; SHA-256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`, byte-identical to the committed snapshot. Located route quote at line 7 (17 words): `Start with inspect_android_package on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.`

Quote-word sweep, run 2026-10-27: `python3 -B -c 's=["""adler32 checksum of the rest of the file (everything but magic and this field)""","""must be 0x70 (112) bytes (v40 or earlier)""","""end of central dir signature 4 bytes (0x06054b50)""","""Start with inspect_android_package on the caller\x27s APK path for package identity, manifest declarations, coverage, and inline Evidence."""]; print([len(x.split()) for x in s])'` → `[14, 8, 8, 17]` (S048 checksum, S048 header_size, S032 quote, S049 route).
SOURCES changes this round: no existing row's status/recheck/used-by changed in place. New S052 is mined/90d; its `used-by` is `— → corpus/knowledge/round-71-apk-axml-byte-evidence.md, corpus/lessons/round-71.md`. New S053 is rejected/on-release; its `used-by` is `— → corpus/lessons/round-71.md`. The source registry validation receipts under `.ufo/waves/round-71/sources-s052/validate.log` and `sources-s053/validate.log` exit 0 with the disclosed W04/W01 warnings. Source census before: `census-before.txt`, exit 0 (51 rows); after: `census-after.txt`, exit 0 (53 rows). The after registry also gained one C05 Paths line (S049 → S052) and one 2026-10-27 Search log line (6 identified, 6 screened, 5 included, 1 rejected). Before rows: **51** — `git show b7abcd8:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` (2026-10-27); after rows: **53** — `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` (2026-10-27). Manual histograms/validator output are in `.ufo/waves/round-71/census-after.txt`.

### C05 pre-gate decision record (wave 1 is advisory, not admission)

`R71W1EntryBlocks` and `R71W1Reproduce` (`.ufo/waves/round-71/w1/R71W1EntryBlocks.md`, `R71W1Reproduce.md`) independently found the 24/24 embedded blocks byte-identical to round-70 v5.1. Reproduce with `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0`, exit 0; `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` reports QMAP/Q14/Q15/HEADER all 0, exit 0. `R71W1GateQ04` and `R71W1GateQ11b` (`.ufo/waves/round-71/w1/R71W1GateQ04.md`, `R71W1GateQ11b.md`) agree the `--spec-quotes` stdout description and the ZIP/AXML compared-literal list match command output. `R71W1GateQ13Q16` (`.ufo/waves/round-71/w1/R71W1GateQ13Q16.md`) confirms the three gate survivor classes are named in Q13, and the different-in-tree-echo case is honestly unguarded. These are pre-gate observations only; wave-2 Q01–Q16 votes decide the C1 claim.

Wave-1 reviewers found the following pre-gate changes before final candidate freeze: (1) item 5 must say `--axml-layout` compares only its printed AXML literals, not every `readout.py` offset (`:189` lineNumber and `:197` styleIndex remain locators-only); (2) qualify the Observation sentence so it does not imply manually transcribed/derived values are printed by their command; (3) Q16 must list the exact checked ZIP/AXML literal subsets and locator-only lines; (4) Q14 must not claim every hex literal appears in a command block; (5) Q08 is labeled `superseded by Q11`, Q12 explains no rejected-source row is asserted; (6) the recheck header names items 2 and 11–17; (7) the coverage-map header says only selected fields are compared with the oracle. Evidence: `.ufo/waves/round-71/w1/R71W1Prose.md`, `R71W1GateQ04.md`, `R71W1GateQ11b.md`, `R71W1GateQ13Q16.md`, and `R71W1QmapCritic.md`. `python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout | wc -l` outputs 20; APPNOTE locators are lines 16–18 and fixed-part comparisons are lines 19–20.

The Q-map is an author assertion, not admission evidence: `R71W1QmapCritic` (`.ufo/waves/round-71/w1/R71W1QmapCritic.md`) correctly notes that a clean lint is only structural. Wave-2 seats must re-derive the cited outputs and decisions on the final landed candidate; they must not accept this lesson's or the entry's own Q-map as proof.
### Post-freeze corrections and measurement boundary

The final candidate bytes were frozen for wave 2 at `c6e284c6583fa3502754361f411b66646880ba02`; the reviewed candidate remains `4c1eeaee88fd07e442f1bd546faf77be3957d390` (SHA-256 `671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092`). Post-freeze changes did not change those bytes, the C1 predicate, or any wave-2 Q decision. `a16e6cbe24c51e6952e973d6b47560b49311420d` corrected only the new S052/S053 `used-by` cells, validation-receipt pointers and this lesson's provenance; the old→new values are logged above. `33fadb25cdb260ee4a6ac2b0a2bb62c4c1bb8057` hardened the frozen vote parser against symlinked roots/members and unhashable `seat` values; `.ufo/waves/round-71/vote-parser-control-a3.txt` records valid=16 and each malformed control=0. It changed no claim threshold or candidate content.

Counter limitation disclosed by `.ufo/waves/round-71/w2/R71W2Sentinel.md` F4 and `.ufo/waves/round-71/w2/R71W2CounterReplay.md`: the final counter executes the round-70 self-check diagnostic from the live absolute lane path (`reports/round-70/measure.py` via `LANE`), rather than from the measured archive. The C1/C2 target checks and vote parsing read the archived `TREE`; this residual is not represented as hermetic.

### Final wave-2 C1 decisions (fresh seats; candidate bytes at `4c1eeaee88fd07e442f1bd546faf77be3957d390`, SHA-256 `671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092`)
Reviewer report locators in the table are relative to `.ufo/waves/round-71/w2/`; the four vote files are under `.ufo/waves/round-71/w2-votes/`.

| Q | decision | fresh seat / evidence |
|---|---|---|
| Q01 | PASS | `R71W2Q01Q04.md:6` — tier-A, scope-bounded sources |
| Q02 | PASS | `R71W2Q01Q04.md:7` — header trio and anchors |
| Q03 | PASS | `R71W2Q01Q04.md:8` — independent byte derivation |
| Q04 | PASS | `R71W2Q01Q04.md:9-10` — six MATCH rows and 20 stdout lines |
| Q05 | PASS | `R71W2Q05Q08.md:9` — no readiness or producer claim |
| Q06 | PASS | `R71W2Q05Q08.md:10` — fixture/oracle pins |
| Q07 | PASS | `R71W2Q05Q08.md:11` — no parser prediction |
| Q08 | PASS (superseded by Q11) | `R71W2Q05Q08.md:12` |
| Q09 | **FAIL** | `R71W2Q09Q12.md:3-5` — Q-map says an out-of-corpus builder is named undigested, but the only named generator is inside `corpus/` and is hashed in item 14 |
| Q10 | PASS | `R71W2Q09Q12.md:7-9` — single fixture and ADJ-06 fence |
| Q11 | PASS | `R71W2Q09Q12.md:11-13` — displayed values and manual widths bounded |
| Q12 | n/a | `R71W2Q09Q12.md:15-17` — no rejected-source row or reject/flip claim in the entry; S053 is registry-only |
| Q13 | PASS | `R71W2Q13Q16.md:5-6` — three gate survivor classes named unguarded |
| Q14 | PASS | `R71W2Q13Q16.md:7` — byte-counted outputs are exact |
| Q15 | PASS | `R71W2Q13Q16.md:8` — no git/tree identity claim |
| Q16 | **FAIL** | `R71W2Q13Q16.md:9-14` and `R71W2Q16Scope.md:9-12` — item 17 claims the AXML field offsets the readout uses are compared, but `--axml-layout` omits `readout.py:189` (`lineNumber`) and `:197` (`styleIndex`); the item-17/Observation locator set also omits the `readout.py:203` `aoff` expression |

Frozen kill rule executed without repair or re-gate: C1 **falsified / honest stop**. At vote commit `da70b5bd2da7274f03d37eb4f49372643d5bf2e0`, the four Q vote files contain 16 decisions with FAILs at Q09 and Q16; the C1 pass-count predicate is `0/16`. The subsequent decision commit `dac9590236f0d3e7213c30ccdb343f0891a36644` marks the v6 `admission-status` rejected; C05 README remains `uncovered`. The A3 counter SHA `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2` was measured on that adjudicated tree; `reports/round-71/measure-after.log` confirms `C1_W2_Q_VOTES=0/16` and `HOLDS_C1_V6=no`.

### C2 gate exit-2 adjudication

On A3 counter SHA `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2`, the final measurement at `dac9590236f0d3e7213c30ccdb343f0891a36644` records `C2_MISSING_ENTRY_EXIT2=1/1 rc=2 stderr_traceback=no`, `C2_TIMEOUT_EXIT2=1/1 rc=2 stderr_traceback=no`, `C2_GATE_SELFTEST=0 named_legs=1`, and `HOLDS_C2_V1=yes`; exact counter output and all ten `HOLD <name> exit=0` rows are in `reports/round-71/measure-after.log`. The independent real-CLI replay observed the production timeout at 120 seconds with no traceback (`.ufo/waves/round-71/w2/R71W2GateReplay.md:58-68`). The exit-2 claim is verified; it changes only the registered gate's classification of missing/unreadable entry and timeout.


### Candidate record

- Candidate: `corpus/knowledge/round-71-apk-axml-byte-evidence.md`, frozen at `4c1eeaee88fd07e442f1bd546faf77be3957d390` with SHA-256 `671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092`.
- Admitted: none this round.
- Rejected: the sixth-pass candidate after the located Q09/Q16 FAILs; its `admission-status` is rejected and C05 remains `uncovered`. No repair or re-gate followed wave-2 scoring.

## Wave-2 record

Validated v1 wave 2: 34/34 result records and all seats settled by WAVE-DONE; 0 empty outputs. Roles (from `w2-results.json`): reviewer 10, critic 5, mutation-tester 4, executor 5, scout 3, scribe 2, connector 2, sentinel 1, revenger 1, simplifier 1. Attacks (reviewer/critic/mutation-tester/sentinel/revenger): 21/34. Count command: `python3 -B -c 'import json,collections;w=json.load(open(".ufo/waves/round-71/w2-results.json"));c=collections.Counter(r["agent"] for r in w["results"]);print(w["seats"],len(w["results"]),sum(not r["output"].strip() for r in w["results"]),c)'` → `34 34 0 Counter({'reviewer': 10, 'critic': 5, 'executor': 5, 'mutation-tester': 4, 'scout': 3, 'scribe': 2, 'connector': 2, 'sentinel': 1, 'revenger': 1, 'simplifier': 1})`. Four per-seat vote files cover Q01–Q16 and were committed at `da70b5bd2da7274f03d37eb4f49372643d5bf2e0`. `R71W2ConnCarry` settled but returned no useful report; this is disclosed, not counted as a dead seat. W2 results: `.ufo/waves/round-71/w2-results.json`.

### Discernment sample

The sample offered for external non-author spot-check is S052 (ADMIT for the command-output-shape claim) and S053 (REJECT for this C05 entry's source support). `R71W2SpotcheckDraft.md` is a lane-dispatched scribe, not an outside reviewer; agreement/disagreement and reasons remain pending independent closure. No self-attestation or lane-seat result is counted as outside discernment.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M58 | scope (measurement-receipt omission: an aggregate replay label hides per-verifier outcomes) | round-70 non-author verifier spotcheck `corpus/lessons/round-70-verifier-spotcheck.md:24-26,91-94` records ten `HOLD` rows missing from `reports/round-70/measure-after.log`; observed sweeps `grep -c '^HOLD ' reports/round-70/measure-after.log` → 0 and `grep -c '^HOLD ' reports/round-71/measure-before.log` → 10 (`measure-before.log:33-42`) | none — no QUALITY/protocol criterion required the individual receipt rows; first routed by the round-70 spotcheck | capture complete counter stdout, retaining every verifier row, not only `HOLD_REPLAY=10/10`; shown able to fail by the r70 zero-row output and pass by the r71 ten-row output |
| M59 | reference-drift (quarantine register path was mislocated) | `.ufo/waves/round-71/w1/R71W1Quarantine.md:5-7` searched `/home/vgpnk/Projects/shokuknow/lanes/revenger` and did not run the register query; L1 ran `awk -F'\x7c' -v l='revenger' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {n++} END {print n+0}' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` → 26 | none — the W1 item prompt omitted the absolute register path | run the same `awk` with `/home/vgpnk/Projects/shokuknow/lanes/revenger/absent-defect-register.md` → exit 2, 0 rows; the contract path query returns 26. Both red-before and repaired-path commands were executed this round. |
| M60 | scope (Q16/Q09 prose-claim overreach: a self-map credited a digest scope and literal set beyond the entry's evidence) | final wave-2 Q09 FAIL `.ufo/waves/round-71/w2/R71W2Q09Q12.md:3-5`; Q16 FAIL `.ufo/waves/round-71/w2/R71W2Q13Q16.md:9-14` / `.ufo/waves/round-71/w2/R71W2Q16Scope.md:9-12`; votes `.ufo/waves/round-71/w2-votes/` | Q09/Q16 in `corpus/QUALITY.md` plus fresh reviewer decisions; the author's Q-map did not catch the located conflicts | apply the frozen kill: mark only v6 `admission-status` rejected, keep C05 uncovered, and do not repair/re-gate after the vote; later C05 work must re-derive the cited source/offset set before any new claim |

## Assimilation and frontier

Assimilation: none. No `merge/revenger/` entries or package source rows were appended; the adoption gate remains closed. The lane quarantine slice was re-derived with the spacing-tolerant query at `.ufo/waves/round-71/assimilation/quarantine-slice`; `wc -l .ufo/waves/round-71/assimilation/quarantine-slice` → 26 data rows, all historical r1-r4 entries. The independent W1 scout did not locate the register because its task omitted the exact path; L1's rerun used the exact contract path. The prior round-70 quarantine lesson reports 26 verdicts (4 PRESENT, 19 ABSENT, 1 UNREACHABLE, 2 UNVERIFIED-REACHABLE); no new source verdicts or adoptions are claimed here.

From `considerthese/2026-10-26.md`, proposal 1 only: this lesson records all 14 proposals in the three in-scope files, their acted evidence or negative sweep, and the round-71 next-gate result where applicable. Proposal 1 was updated after wave-2 adjudication; whether this ledger becomes a recurring process remains untested.
| Proposal (origin) | Adopted? | Evidence / sweep | Held at next gate |
|---|---|---|---|
| 2026-10-24 #1 hex/ASCII sanity pass | No observed adoption | `grep -rni 'ascii' corpus/lint_entry.py` → two self-test fixture strings only; `grep -rni 'hex.*ascii' corpus/lint_entry.py` and `grep -rni 'ascii.*hex' corpus/lint_entry.py` → no matches; no entry-wide hex→ASCII checker |
| 2026-10-24 #2 provider-refusal line | No observed adoption | `grep -rni 'refusal' corpus/lessons/round-70.md LOG.md` and `grep -rni 'provider-refus' corpus/lessons/round-70.md LOG.md` → route/history prose only; no per-round refusal-line field (`.ufo/waves/round-71/w2/R71W2LessonReview.md:106-110`) |
| 2026-10-24 #3 claim hit-rate ledger | Yes, round 70 | `corpus/lessons/round-70.md` records the 11/18 stricter per-predicate reading and 2/18 disagreement | N/A: no hit-rate claim in round 71 |
| 2026-10-24 #4 undispatched-wave backlog | No observed adoption | `grep -ni 'undispatched' corpus/lessons/round-70.md` and `grep -ni 'backlog' corpus/lessons/round-70.md` → no matches (`.ufo/waves/round-71/w2/R71W2LessonReview.md:97-103`) | — |
| 2026-10-24 #5 burst-aware reporting | No observed adoption | `grep -ni 'burst' corpus/lessons/round-70.md` → no match (`.ufo/waves/round-71/w2/R71W2LessonReview.md:97-103`) | — |
| 2026-10-25 #1 routed-repair carry-through | Yes, round-70 connector seat | `.ufo/waves/round-70/w2/R70W2ConnRoutedCarry.md`; round-71 applied the routed pre-gate repairs | Partial only: C1 still falsified by distinct Q09/Q16 defects; no admission |
| 2026-10-25 #2 stdout-built entry | Yes, round 70 | `.ufo/waves/round-70/build-entry.py`; r71 re-derived 24/24 embedded blocks, but W2 still found Q09/Q16 prose defects | Structural output held; semantic admission did not |
| 2026-10-25 #3 "Did the instrument run" line | Yes, first used this round | `reports/round-71/measure-after.log` and the final measurement line in `LOG.md` record command, exit and outputs | Pending a later independent gate |
| 2026-10-25 #4 Q-map completeness lint | Yes, round 70 | `corpus/lint_entry.py`; r70 missing-Q16 lint `LINT_QMAP=1`, r71 `LINT_QMAP=0` | Structural lint held; Q09/Q16 semantics did not |
| 2026-10-25 #5 cross-pass disagreement ledger | No observed adoption | `grep -rli 'cross-pass' corpus/lessons/` and `grep -rli 'disagreement ledger' corpus/lessons/` → only round-69, round-69-verifier-spotcheck and this round-71 ledger mention the terms; no standalone ledger file (`.ufo/waves/round-71/w2/R71W2LessonReview.md:106-110`) | — |
| 2026-10-26 #1 adoption ledger (this proposal) | Yes, first use in this lesson | This 14-row table, updated after the final Q01–Q16 decisions | Yes: updated with Q09/Q16 FAIL and honest-stop outcome; bookkeeping does not prove admission |
| 2026-10-26 #2 Q16 prose pre-read | Yes, applied in wave 1 | `.ufo/waves/round-71/w1/R71W1Prose.md`; it located prose claims beyond the 24-block gate | Not fully held: Q16 still FAIL, so the candidate was rejected |
| 2026-10-26 #3 one stated reading for hit-rate claims | Yes, round-70 lesson | `corpus/lessons/round-70.md` leads with the stricter per-predicate reading and records the alternative | N/A: no hit-rate claim in this round |
| 2026-10-26 #4 per-role seat yield | No observed adoption | `grep -ni 'yield' corpus/lessons/round-70.md` → no match; round 71 reports roles and one malformed output, not a per-role yield metric | — |

The ledger separates adoption evidence from next-gate performance. It records the honest stop, not a recurring process or a reason to admit C05.

## Wave-1 record

Validated v1 wave 1: 40/40 result records, 0 empty outputs. Roles: reviewer 9, critic 4, mutation-tester 3, sentinel 1, revenger 1, executor 7, scout 7, scribe 5, connector 2, simplifier 1. Attacks (reviewer/critic/mutation-tester/sentinel/revenger): 18/40. Count command: `python3 -B -c 'import json,collections;w=json.load(open(".ufo/waves/round-71/w1-results.json"));c=collections.Counter(r["agent"] for r in w["results"]);print(w["seats"],len(w["results"]),sum(not r["output"].strip() for r in w["results"]),c)'` → `40 40 0 Counter({'reviewer': 9, 'executor': 7, 'scout': 7, 'scribe': 5, 'critic': 4, 'mutation-tester': 3, 'connector': 2, 'sentinel': 1, 'revenger': 1, 'simplifier': 1})`. §3 planner held by L1; connectors carry the bounded overlap/ledger walk. W1 results: `.ufo/waves/round-71/w1-results.json`. No tools installed or updated.
