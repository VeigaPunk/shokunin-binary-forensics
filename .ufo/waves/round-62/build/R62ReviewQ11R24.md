RESULT: COMPLETE

# R62ReviewQ11R24 — underived premise inventory for the C09 EVM candidate (read-only review)

Seat: RevengerR61-2.R62ReviewQ11R24 · reviewer · scope: old C09 rejected candidate `corpus/knowledge/evm-saved-interface-candidates.md` and `.ufo/waves/round-61/falsify-w3/W3EvmR24Immediate.md`. Frozen revision `a3498e25ad87bf756288812d0ea7c474b09433c7` (`git archive` → `/fast/scratch/hyaku/revenger-r62/R62ReviewQ11R24/landed`); all execution on that extracted copy only, cwd=extracted tree. No bytecode, fixture JS, chain, REA producer or live-target probe executed; no production edit, no git/jj index or history mutation, README untouched (C04/C09 stay `uncovered`).

**Harm checks.** `git diff --stat a3498e25 -- corpus/fixtures corpus/live` → empty; same for `corpus/knowledge corpus/lessons corpus/QUALITY.md corpus/README.md` → empty; `git show a3498e25:corpus/README.md | grep '^| C(04|09) '` → both rows end `| uncovered |`. Rejected candidate file, round-61 reports/counterexamples and the verifier lesson are byte-preserved.

## A. raw-0x5B-count vs `jumpdest=[]` (the load-bearing distinction)

The old block prints `jumpdest={valid}` = the **instruction-level** JUMPDEST set from the PUSH-skipping walk (`[i for i,op,_ in ins if op==0x5b]`). Entry:66 asserts a **raw byte-level** fact ("the file has no 0x5B byte"). Different quantities: a 0x5B byte inside a PUSH-N immediate is a raw occurrence but never an instruction start, so it is absent from the walk set. Frozen-copy run (`raw_vs_walk.py`, exit 0): r19 `[16]`/1, r21 `[16]`/1, r22 `[30,32]`/2, r23 `[]`/0, r24 `[]`/0, r25 `[17]`/1, r26 `[17]`/1 (raw offsets / count; walk set identical, `raw_equals_walk=True` in all seven) — but `synthetic_605b bytes=605b raw_0x5b_offsets=[1] count=1 walk_jumpdest=[] count=0 raw_equals_walk=False`. The seven fixtures agree only because no 0x5B byte lies inside an immediate in any of them, so `jumpdest=[]` cannot license "no 0x5B byte": the new entry needs a **separate raw byte scan**, scoped to the **decoded code bytes** (r19's carrier is ASCII hex text whose own raw 0x5B count is 0, while its decoded bytes hold one at 16).

## B. Inventory: 15 underderived premises (full table with reasons and exact per-premise readouts in scratch `premise_inventory.md`)

| # | Premise (old entry line) | Underderived | Exact necessary readout |
|---|---|---|---|
| P1 | "one PUSH32" (:39) | yes | `executable_push32=[(0,32)]` + `instruction_count=3` |
| P2 | "immediate contains the r19 pattern" (:39) | yes | `pattern9_occurrences=[1] pattern9_len=9` |
| P3 | `[1,9]` inclusive span (:94-96) | yes | `inclusive_spans=[(1,9)] occurrences_inside_immediate=[1]` |
| P4 | "one 9-byte occurrence" (:94) | yes | occurrence count in the same line |
| P5 | "no 0x5B byte" (:66) | yes | `raw_0x5b_offsets=[] raw_0x5b_count=0` (separate raw scan) |
| P6 | "embedded JUMPI target (0x10)" (:65) | yes | `embedded_at=1 selector_imm=deadbeef cmp_op=0x14 push1_operand=0x10 jump_op=0x57 embedded_target=16 target_byte=0x0 target_is_walk_jumpdest=False target_is_raw_0x5b=False target_is_instruction_start=False target_inside_immediate=True` |
| P7 | "0x63 at offset 1, inside that immediate" (:40) | partly | `raw_0x63_offsets=[1]` + `push_n_immediate_spans=(0,1,32,32)` |
| P8 | "no executable PUSH4" (:40) | **no** | already printed; keep `executable_push4=[]` |
| P9 | "three reported pairs" (:87) | yes | `TOTAL_normalized_function_tuples=4 records_reporting_pairs=3 per_record_counts=[(19,1),(21,1),(22,2),(23,0),(24,0),(25,0),(26,0)]` — the block prints 4 tuples, not 3 |
| P10 | "0/37 single-conjunct deletions" (:92) | yes | label **recorded (not re-derived)** with its path, or omit |
| P11 | "run 2026-10-12" (:88) | yes | label **recorded**, or omit |
| P12 | "contains the r19 pattern" wording (:39) | yes | r24 holds r19 offsets **6–14** only (9 of r19's 18 bytes) → print both sides' spans |
| P13 | "several simpler rules also yield an empty output" (:66) | yes | in-entry rule table `walk_skip_jd/walk_skip_nojd/raw_nojd/raw_rawjd/raw_stopentry` + `raw_0x35_count`/`raw_0x1c_count` (r19 1/1 vs r24 0/0 → missing CALLDATALOAD/SHR prologue confound) |
| P14 | "subject digest equals the fixture bytes' SHA-256" (:46) | partly | old block used `sha in (sha(raw),sha(d))`, conflating scopes; r19 matches only the **carrier** digest → print `subject_digest_eq_decoded` and `subject_digest_eq_carrier` separately (+ `decoded_sha256`, `carrier_sha256`) |
| P15 | "every value rests on this block" (:195, Q13) | yes | 2 of 7 clauses survive deletion undetected (W3EvmQTable F2) → name unguarded clauses; credit only what the run detects |

P1-P6 are exactly the four W3EvmR24Immediate Q11 breaks plus the two counts it attributed to the span correction (W3EvmR24SpanFix F2). Truth values unchanged and re-confirmed here; only the derivation was missing.

## C. Necessary readouts executed on the frozen copy (exit 0; full output `readout_out.txt`)

Scratch blocks (not landed): `readout.py`→`readout_out.txt`, `rules.py`, `raw_vs_walk.py`. r24: `instruction_count=3 instructions=[(0,'0x7f','63deadbeef…'),(33,'0x50',''),(34,'0x0','')] executable_push32=[(0,32)] push_n_immediate_spans=(0,1,32,32) raw_0x5b_offsets=[] raw_0x5b_count=0 walk_jumpdest=[] raw5b_eq_walkjd=True raw_0x63_offsets=[1] pattern9_occurrences=[1] inclusive_spans=[(1,9)] occurrences_inside_immediate=[1] pattern9_len=9 embedded_at=1 selector_imm=deadbeef push1_operand=0x10 jump_op=0x57 embedded_target=16 target_byte=0x0 target_is_walk_jumpdest=False target_is_raw_0x5b=False target_is_instruction_start=False target_inside_immediate=True normalized_functions=[] normalized_function_count=0`. Rule run: `r24 raw_0x35_count=0 raw_0x1c_count=0 raw_0x5b_count=0 entry_byte=0x7f walk_skip_jd=[] walk_skip_nojd=[] raw_nojd=[(1,16)] raw_rawjd=[] raw_stopentry=[]` — only the naive raw scanner fires on r24 (the "does not show the provider excludes PUSH data" inference); the missing 0x35/0x1c prologue is a second, independent confound. Totals: `TOTAL_normalized_function_tuples=4 records_reporting_pairs=3` (resolves P9). Opcode ground truth re-opened this round at the pinned public tag (v2.20.0 `instructions/__init__.py`: `EQ=0x14` L55, `JUMPI=0x57` L106, `JUMPDEST=0x5B` L109, `PUSH1=0x60` L122, `PUSH4=0x63` L125, `PUSH32=0x7F` L153; `runtime.py` L29 "The jump destination shouldn't be part of the data corresponding to `PUSH-N` opcodes."): P1/P6/P12 constants are derivable but must be **printed**, not assumed.

## D. Boundaries honoured

Did not re-run the known-failed check: the old entry's `## Reproduce` block was **not** executed by me; output equality is not treated as completeness; no `reports/round-61/measure.py` run. No repair/edit/re-freeze of the rejected candidate — the retained file and its rejection warning stay byte-identical, and old rejected text is not cited as factual support for any new claim. No current-producer, general-method, runtime, Electron-role or authenticity claim; no new gate or promotion; no README row flipped.

## E. Residual risk / verification gaps

P13's rule set is my reconstruction of the round-61 counterexample rules (`counterexamples/r24-scanner-rules.py`); the author may pick a narrower set, but it must be computed in-entry. The synthetic `605b` string is my own byte string, not a fixture — a scope argument only, never a fixture claim. `r24 LEDGER.md:3` / `LOG.md:289` remain the only external wording of the [1,9] span; the new entry must derive it or label it recorded. I did not verify `verify_evm_evidence.py`'s clause-detection matrix, so P15's unguarded-clause list must come from the new entry's own run.

## F. Proposed changes (scratch only; L1 decides landing)

`premise_inventory.md`, `readout.py`, `readout_out.txt`, `rules.py`, `raw_vs_walk.py` under `/fast/scratch/hyaku/revenger-r62/R62ReviewQ11R24/` — candidate in-entry blocks for `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md` carrying the P1-P15 readout lines; its `## Provenance` must paste the actual frozen-copy output and P10/P11 must be labelled recorded. No change proposed to `corpus/README.md` (C09 stays `uncovered` until the fresh falsify wave and an explicit all-criteria admission).

Installs: none. Tools: `git` (read-only archive/diff/show), `python3 -B` (stdlib only), `curl` (two public execution-specs source files, read-only, for the opcode-constant derivation). No pacman/uv/cargo/npm transaction, no service restart, no package installed or updated.
