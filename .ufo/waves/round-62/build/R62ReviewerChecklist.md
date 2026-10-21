RESULT: COMPLETE

# R62 reviewer checklist — per-entry Q01–Q13 audit worksheet (C04 candidate A, C09 candidate B)

Scope: audit worksheet only — no gate implementation, no new probe, no second research method.
Applicants: **A** = `corpus/knowledge/round-62-commonjs-require-name-evidence.md` (C04); **B** = `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` (C09).
Ground: `corpus/QUALITY.md:13-25` (Q01–Q13, unchanged), `corpus/lessons/round-61.md` (Gate + fresh-wave erratum + M21–M26), `corpus/lessons/round-61-verifier-spotcheck.md` (routed defects 1–4), `reports/round-62/claims.md` (frozen `a3498e25`).
Read-only ground: `git -C …/revenger-shokunin archive a3498e25ad87bf756288812d0ea7c474b09433c7` → `/fast/scratch/hyaku/revenger-r62/ReviewerChecklist`. No live edit, no jj/Git mutation, no fixture JS/bytecode executed, no REA/chain call, no sibling-lane file touched.

## 0 Binding use rules
- One row per Q id per applicant. Every cell carries `verdict: pass|fail|n/a(reason)|recorded` **and** an evidence pointer (entry line + command + output line, or `file:line` for a read).
- **No pass defaults**: a blank cell is an incomplete worksheet, never a pass; a cell with no pointer is `fail (no derivation)` under Q11 and `fail (no basis)` elsewhere.
- Reviewers re-derive only what the applicant entry asserts; they run no new analyses, parsers or producers and do not repair the entry (L1 integrates).
- `corpus/README.md:33` (C04) and `:38` (C09) stay `uncovered` throughout this wave. A `held` cell before the fresh falsify wave plus explicit all-criteria admission voids C1 (`claims.md` §Counting and admission order).

## 1 Per-Q worksheet (same columns for A and B)
| Q | what the reviewer checks (QUALITY reject clause) | evidence to capture | A verdict | A ptr | B verdict | B ptr |
|---|---|---|---|---|---|---|
| Q01 | load-bearing claim → S-row that is tier A **for that claim's scope**, opened this round (`:13`) | S-id + URL/path + verbatim quote ≤25 words + access date + opener; a rejected row is never support | | | | |
| Q02 | headers `source:`/`verified-at:`/`recheck:`/`coverage-map:` present; anchor is not a bare homepage (`:14`) | the four header lines as written | | | | |
| Q03 | expected value from bytes / specification / pin fixed outside the record under test; a saved path is not both identity and locator (`:15`) | the outside-of-record origin of each expected value | | | | |
| Q04 | tool + version + function named; the tool's **own explicit output** scored; manual analysis labeled manual (`:16`) | quoted provider/tool output field the claim scores | | | | |
| Q05 | readiness/capability claim carries command + date + exit; recorded runs stay past tense (saved records 2026-10-12, provider 6.4.0; host skill names 6.7.0 per S002) (`:17`) | probe line or the past-tense marking | | | | |
| Q06 | every fixture premise byte-verified against the built fixture before use (`:18`) | per-file SHA-256 printed by the entry's own block | | | | |
| Q07 | predicted parser behavior pre-registered with spec ground truth, recorded whichever way it falls; cause stated once, independently reproduced (`:19`) | hypothesis + ground truth + outcome, or `n/a (no prediction)` with reason | | | | |
| Q08 | superseded by Q11 — mark `superseded`; do not re-check separately (`:20`) | — | | | | |
| Q09 | digest claimed only for the exact bytes hashed; no origin / completeness / authenticity inference; saved records byte-preserved (`:21`) | the byte string each digest covers + the preservation diff | | | | |
| Q10 | scope bound to observed family / operation / version / input; contested cross-lane scope reported, not absorbed (`:22`) | the scope sentence + every sibling cite | | | | |
| Q11 | every count / identifier / offset / digest carries, **inside the entry**, its command and that command's output; constants derived; prose-only values labeled `recorded, not re-derived` (`:23`) | the value→command→output ledger (see §3) | | | | |
| Q12 | a rejected source row states a reject reason grounded in a located quote and a flip naming a source change or a scope the reason does not exclude (`:24`) | quote + flip text, or `n/a (no rejected row cited)` | | | | |
| Q13 | verifier/recheck credited only for clauses whose deletion its own run detects; **every other clause named unguarded** (`:25`) | per-verifier detected/unguarded clause list | | | | |

## 2 Named fail items (each is a fail, not a warning)
- **F1 missing span/count/target (Q11).** Precedent: C04 claimed its block carried "edge spans" it never printed (0 matches for `location|start|span|column` — `W3JsOverclaimCritic.md` B1); C09's r24 PUSH32 count, raw `0x5B` count, 9-byte pattern span `[1,9]` and embedded JUMPI target `0x10` were correct but underived (`W3EvmR24Immediate.md` BROKEN a–d). Clears only when the applicant's own `## Reproduce` prints each value and `## Provenance` shows the same lines; a correct value with no in-entry derivation is `fail`.
- **F2 record-vs-decoded digest (Q09+Q11).** Precedent: r19's subject digest covers the 39-byte hex carrier `294e6f…`, not the 18 decoded bytes `d1086bce…`; the disjunction `in (sha(raw), sha(d))` hid the referent (`W3EvmFlagsDigest.md` F2). Clears when each digest names the exact bytes it covers and the entry states which one it is.
- **F3 neutral Electron label (Q01/Q04/Q10/Q11).** Precedent: "the provider's kind name" was contradicted by the record's own `electron-role` / `discover-electron-entrypoint` fields and by REA 6.4.0 docs (`W3JsElectronMainLabel.md` F3/F4). Clears by deletion: neither applicant may make an Electron-role claim; any surviving label sentence must quote the record fields and derive them in-entry.
- **F4 unsupported sibling citation (Q01/Q10).** Precedent: `kasegi-shokunin/PROVINCE.md:25` is the **"Refuses"** line cited to support ownership (`W3ProvinceBounds.md` Finding 1); `kaidoku-shokunin/PROVINCE.md:54` is a surface row only (`W3EvmCrossLaneCites.md` Finding 2); a sibling's scoped reading was universalized (Finding 4). Clears when each sibling cite quotes the cited line verbatim **and** that line states the attributed claim; otherwise record "not in the cited line" and drop the attribution.
- **F5 verifier deletion blindspots (Q13).** Precedent: `verify_js_graph_delta.py:47`/`:58` and `verify_saved_evidence.py:117` were credited although deleting that conjunct left the forgery accepted with the verifier still exiting 0; the C04 block had six deletion-blind conjuncts; `verify_evm_evidence.py` detects 0/37 single-conjunct deletions (`W3QualityQ13Apply.md` F1/F2/F5). Clears when each entry names, per verifier, exactly the clauses its own run detects and names the rest unguarded; `recheck:` block credit is limited to stdout-visible changes.

## 3 Mandatory derivation ledger (Q11) — values the applicant must derive, per entry
- **A (C04):** destructured names, specifier, require-call count, per-`imports`-edge `imported_name` (or absent), `specifier`, `resolved_path`, `evidence.location.value` **if any span/location is asserted**, `maps_to` count / `resolution_context` / `resolution_status` / `state` / `resolved_path`, delta removed+added+kept, node kinds, Electron-token count, and the SHA-256 of every fixture file and of each saved record.
- **B (C09):** raw byte length + SHA-256, PUSH-N-skipping walk (opcodes, offsets, immediate spans), raw `0x63` offsets/count, raw `0x5B` offsets/count, 9-byte pattern occurrence count + inclusive span, embedded JUMPI target offset/value, record flags (`evidence_kind`, `discovery_completeness`, `runtime_execution`, functions count), and for every digest the exact bytes it covers (carrier file vs decoded bytes).

## 4 Instrument limits — do not credit the probe as admission
- `K_HELD_BACKED` counts file existence only: a 7-byte stub still scores 6/14 (`W3HoldProbeRerun.md` F3). Necessary, not sufficient.
- The probe is blind to non-C04/C09 status drift: mutant d (C02 `partial`→`frontier`) gave byte-identical stdout and exit (`W3KProbeMutant.md`).
- Baseline re-run on the frozen extract (`cd / && TMPDIR=/fast/scratch/hyaku/revenger-r62/ReviewerChecklist python3 -B reports/round-61/measure.py /fast/scratch/hyaku/revenger-r62/ReviewerChecklist`, exit 0): `K_HELD=4/14 score=2.9`, `K_ROW C04 status=uncovered`, `K_ROW C09 status=uncovered`, `K_HELD_BACKED=4/14`, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`. Baseline only — no flip performed, none authorized.

## 5 Unknowns and boundaries of this worksheet
- It audits claims made in the applicant entries; it cannot supply the missing derivations themselves. A reviewer who cannot locate a derivation records `fail` plus its location — never a repair, never a pass.
- `corpus/SOURCES.md` holds 27 rows (S001–S027) at `a3498e25`; S028–S031 are reserved, not rows. A cite to S028+ is `fail (no row)` until L1 writes the row from an actually opened source (claims.md §Sources).
- Prior rejected candidates, round-61 reports and counterexamples are left byte-unchanged by this seat; no corpus/live, corpus/fixtures, README or SOURCES byte was written.
- Conflicts for the canonical judge: none observed between `reports/round-62/claims.md` and the round-61 closure; the closure's routed defects 1–4 are carried here as F1–F5 and §4.

Proposed artifact: this worksheet (no production file changed). Scratch: `/fast/scratch/hyaku/revenger-r62/ReviewerChecklist` (frozen extract, read-only).
Installs: none (python3 stdlib only; no pacman/uv/npm transaction).
