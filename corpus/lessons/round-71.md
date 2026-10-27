# round 71 — revenger (hyaku run 10)

author: RevengerR71 · base `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f` · frozen claims `reports/round-71/claims.md` · current pre-gate build `18200a4b18e8dfce291a74028a9012ce4401ca10` · no package installation.

## Gate — source curation and wave-1 pre-gate

### New SOURCES rows opened this round (CORPUS.md rule 1)

- **S052 — ADMIT for the C05 output-description claim (new own-work tier A row).** Command opened 2026-10-27 from the lane root: `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes` (exit 0; six `MATCH` lines). Located stdout quote (12 words) from the `dex-format.html` match: `MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;`. It reports a snapshot file, first-line number, phrase-presence flag and phrase; it does not print the raw source line. Registry row S052 scope and entry item 11 are limited to that output shape. `used-by`: `corpus/knowledge/round-71-apk-axml-byte-evidence.md`.
- **S053 — REJECT as support for this C05 entry (new row, supersedes S044).** Source opened 2026-10-27: https://docs.python.org/3/library/zipfile.html, page title `zipfile — Work with ZIP archives — Python 3.15.2 documentation`, section introduction under `# zipfile — Work with ZIP archives`. Located quote (14 words): `This module provides tools to create, read, write, append, and list a ZIP file.` The official page is authoritative for the Python module's own API scope, but the C05 entry makes no `zipfile` API claim; its format/layout evidence rests on APPNOTE S032/S034 and direct fixture bytes. Flip: a future entry that relies on a located Python `zipfile` behavior claim may re-open and screen this source. S053 remains a rejected row with `used-by=—`; the existing S044 row was not edited.

### Re-opened existing source rows

- S038: primary AOSP URL was re-opened by `R71W1OpenS038` on 2026-10-27. The reader returned a base64 body without a line-addressable live quote or a new digest; the quoted `attributeStart` phrase and enum anchors are located in the committed `corpus/snapshots/ResourceTypes.h` and derived by item 11. Live byte currency is not claimed.
- S048: `R71W1OpenS048`, 2026-10-27T15:21:21Z; live `header_item` checksum quote: `adler32 checksum of the rest of the file (everything but magic and this field)` (18 words); `header_size`: `must be 0x70 (112) bytes (v40 or earlier)` (12 words). The current reader returned rendered text, so no new byte-level digest is claimed.
- S032/S034: `R71W1OpenS032`, 2026-10-27T15:21:46Z; live APPNOTE bytes and committed `corpus/snapshots/APPNOTE.TXT` both SHA-256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, 174585 bytes. Located quote at §4.3.16 line 634 (13 words): `end of central dir signature 4 bytes (0x06054b50)`.
- S049: `R71W1OpenS049`, 2026-10-27T15:21:38Z; raw reference 1992 bytes, SHA-256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`, byte-identical to the committed snapshot. Located route quote at line 7 (20 words): `Start with inspect_android_package on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.`

SOURCES changes this round: no existing row's status/recheck/used-by changed in place. New S052 is mined/90d; its `used-by` is `— → corpus/knowledge/round-71-apk-axml-byte-evidence.md, corpus/lessons/round-71.md`. New S053 is rejected/on-release; its `used-by` is `— → corpus/lessons/round-71.md`. The source registry validation receipts under `.ufo/waves/round-71/sources-s052/validate.log` and `sources-s053/validate.log` exit 0 with the disclosed W04/W01 warnings. Before census: 51 rows at base; after rows: 53 (S052+S053). The final round-end census and full manual histograms are in `census-after.txt`.

### C05 pre-gate decision record (wave 1 is advisory, not admission)

`R71W1EntryBlocks` and `R71W1Reproduce` independently found 24/24 embedded blocks byte-identical to round-70 v5.1 and the gate reports `checked_blocks=24 problems=0`, exit 0; `lint_entry.py` reports QMAP/Q14/Q15/HEADER all 0 after the pre-gate repairs. `R71W1GateQ04` and `R71W1GateQ11b` agree the `--spec-quotes` stdout description and the ZIP/AXML compared-literal list match command output. `R71W1GateQ13Q16` confirms the three gate survivor classes are named in Q13, and the different-in-tree-echo case is honestly unguarded. These are pre-gate observations only; wave-2 Q01–Q16 votes decide the C1 claim.

Wave-1 reviewers found the following pre-gate changes before final candidate freeze: (1) item 5 must say `--axml-layout` compares only its printed AXML literals, not every `readout.py` offset (`:189` lineNumber and `:197` styleIndex remain locators-only); (2) qualify the Observation sentence so it does not imply manually transcribed/derived values are printed by their command; (3) Q16 must list the exact checked ZIP/AXML literal subsets and locator-only lines; (4) Q14 must not claim every hex literal appears in a command block; (5) Q08 is labeled `superseded by Q11`, Q12 explains no rejected-source row is asserted; (6) the recheck header names items 2 and 11–17; (7) the coverage-map header says only selected fields are compared with the oracle. The measured stdout confirms `--zip-layout` has 20 stdout lines (the `$ command` line is not counted): APPNOTE locators are lines 16–18 and fixed-part comparisons are lines 19–20.

The Q-map is an author assertion, not admission evidence: `R71W1QmapCritic` correctly notes that a clean lint is only structural. Wave-2 seats must re-derive the cited outputs and decisions on the final landed candidate; they must not accept this lesson's or the entry's own Q-map as proof.

### Discernment sample

The round-71 source-screen sample offered for non-author spot-check is S052 (ADMIT for the command-output-shape claim) and S053 (REJECT for this C05 entry's source support). The non-author closure's agreement/disagreement and reasons are pending its independent review; no self-attestation is counted as outside discernment.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M58 | measurement-receipt omission: an aggregate replay label hides per-verifier outcomes | r70 verifier spot-check `corpus/lessons/round-70-verifier-spotcheck.md:24-26,91-94` records ten `HOLD` rows missing from `reports/round-70/measure-after.log`; `reports/round-71/measure-before.log:33-43` now contains all ten `HOLD <name> exit=0` rows | prior non-author spot-check's routed defect #1 | capture complete counter stdout, retaining every verifier row, not only `HOLD_REPLAY=10/10`; shown able to fail by r70 after receipt (0 `HOLD ` rows) vs r71 receipt (10 rows) |
| M59 | recon path omission: the seat searched an unprovided, incorrect lane subdirectory and could not locate the exact quarantine register | `R71W1Quarantine.md:5-7` searched `/home/vgpnk/Projects/shokuknow/lanes/revenger` and did not run the register query; L1 ran the specified `awk -F'|' -v l='revenger' '$2 ~ ("`" l "`") && $3 ~ /round[0-9]+/ && $4 ~ /S[0-9]+/ {print $4, $5}' /home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md` and obtained 26 rows at `.ufo/waves/round-71/assimilation/quarantine-slice` | none — the L2 item omitted the absolute register path despite the host contract naming it | include the exact absolute register path and command in each future quarantine task; this round's lane-author rerun found the full 26-row slice; no campaign source was edited |

## Assimilation and frontier

Assimilation: none. No `merge/revenger/` entries or package source rows were appended; the adoption gate remains closed. The lane quarantine slice was re-derived with the spacing-tolerant command at `.ufo/waves/round-71/assimilation/quarantine-slice` (26 data rows; all are historical r1-r4 entries). The independent W1 scout did not locate the register because its task omitted the exact path; L1's rerun used the exact contract path. The prior round-70 quarantine lesson reports 26 verdicts (4 PRESENT, 19 ABSENT, 1 UNREACHABLE, 2 UNVERIFIED-REACHABLE); no new source verdicts or adoptions are claimed here.

From `considerthese/2026-10-26.md`, proposal 1 only: this lesson carries a compact proposal → acted evidence → next-gate status ledger. The prior proposals are marked only from recorded sources; proposal 1 itself is first used this round and its next-gate check remains pending until wave-2 adjudication.
| Proposal (origin) | Adopted? | Evidence | Held at next gate |
|---|---|---|---|
| 2026-10-24 #1 hex/ASCII sanity pass | No observed adoption | No entry-wide hex→ASCII checker; `corpus/lint_entry.py` output scan | — |
| 2026-10-24 #2 provider-refusal line | No observed adoption | `corpus/lessons/round-70.md` gate and latest LOG show no new per-round refusal-line field | — |
| 2026-10-24 #3 claim hit-rate ledger | Yes, round 70 | `corpus/lessons/round-70.md` claim-hit-rate section; two derivations disagree on 2/18 and explicitly lead with the stricter per-predicate 11/18 reading | Pending: not rechecked as a proposal effect in round 71 |
| 2026-10-25 #1 routed-repair carry-through | Yes, round-70 connector seat | `.ufo/waves/round-70/w2/R70W2ConnRoutedCarry.md`; round-71 routed items are the next carry-through set | Pending: round-71 wave-2/closure |
| 2026-10-25 #2 stdout-built entry | Yes, round 70 | `.ufo/waves/round-70/build-entry.py`; 24/24 blocks re-derived, but C05 still failed prose decisions | Pending: round-71 final C05 gate |
| 2026-10-25 #4 Q-map completeness lint | Yes, round 70 | `corpus/lint_entry.py`; r70 missing-Q16 lint `LINT_QMAP=1`, v6 after row `LINT_QMAP=0` | Pending: final Q review remains separate from lint |
| 2026-10-25 #5 cross-pass disagreement ledger | No observed adoption | No corresponding ledger found in `corpus/lessons/` | — |
| 2026-10-26 #1 adoption ledger (this proposal) | Yes, first use in this lesson | This table | Pending: update after round-71 final gate |
| 2026-10-26 #2 Q16 prose pre-read | Yes, applied in wave 1 | `.ufo/waves/round-71/w1/R71W1Prose.md`; it located prose claims not visible to the 24-block gate | Pending: wave-2 final candidate review |
| 2026-10-26 #3 one stated reading for hit-rate claims | Yes, round-70 lesson | `corpus/lessons/round-70.md` leads with stricter per-predicate reading and records the alternative | Pending: no hit-rate claim in this round |
| 2026-10-26 #4 per-role seat yield | No observed adoption | No per-role yield ledger in round-71 pre-gate artifacts | — |

The ledger separates adoption evidence from whether the adopted form held at a later gate. A single report table does not establish a recurring process; this proposal's next-gate check remains pending.

## Wave-1 record

Validated v1 wave 1: 40 seats, 0 dead. Roles: reviewer 9, critic 4, mutation-tester 3, sentinel 1, revenger 1, executor 7, scout 7, scribe 5, connector 2, simplifier 1. Attacks (reviewer/critic/mutation-tester/sentinel/revenger): 18/40. §3 planner held by L1; connectors carry the bounded overlap/ledger walk. W1 results: `.ufo/waves/round-71/w1-results.json`. No tools installed or updated.
