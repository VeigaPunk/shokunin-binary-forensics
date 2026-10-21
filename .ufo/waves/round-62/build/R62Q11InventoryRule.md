# R62Q11InventoryRule — proposed additive QUALITY Q14 (scratch proposal; no corpus edit)

RESULT: COMPLETE

One additive criterion row (Q14) proposed in scratch, grounded in round-61 M26, with two red exemplars (C04, C09) and a precise manual test command. **No corpus file edited; no README row flipped; C04/C09 stay `uncovered`; no admission claimed.** Frozen base `a3498e25ad87bf756288812d0ea7c474b09433c7` (read-only extract in scratch).

## 1. Proposed row — exact text in the scratch proposal, L1 decides

`/fast/scratch/hyaku/revenger-r62/R62Q11InventoryRule/Q14-proposal.md` §3 (id Q14, lesson M26; the reject-when clause names the C04 "edge spans" and C09 r24 raw-0x5B/embedded-target/span cases). Substance: every sentence asserting an exact value (count, offset, size, span, digest, name set, byte string) must appear in an in-entry **factual inventory** naming, per value, the code that derives it and the printed output line that shows it, or marking it recorded with the record and field that literally hold it; a value with no derivation, a value whose named code/output prints something else, a printed number differing from the asserted one, and a prose value absent from the inventory each reject; code text, a code comment or a token present elsewhere in the output never counts as a derivation; **output equality is not completeness**; **Q14 never implies a Q11 pass; Q14 rejects whenever Q11 rejects**. Q01–Q13 are not edited.

Grounding: round-61 M26 ("C04 block reproduced but printed no asserted spans; C09 reproduced but omitted r24 raw-count/span/target derivations"; captured by Q11, "admission failed to enforce it"); `round-61-verifier-spotcheck.md` C1 ("counting `location|start|span|column` gives 0 matches"; "never searches its nine-byte embedded pattern and does not derive the raw 0x5B count or the embedded target"); closure routed debt #1 ("do not treat this closure's byte checks as missing in-entry derivations"); `reports/round-62/claims.md` ("A narrow new quality criterion may make the existing Q11 audit explicit, never weaken it").

## 2. Manual test command (advisory, read-only, stdlib, always exit 0)

```
python3 -B /fast/scratch/hyaku/revenger-r62/R62Q11InventoryRule/q14_inventory.py corpus/knowledge/<entry>.md --root <lane root>
```

Helper sha256 `55d9439c3dbba9568a380ec9904b37eb6d85e2e50dab12a0915dab8ce43e20b8` — not a gate, not a corpus verifier, no new capability; it prints candidate gaps for a non-author auditor. Proposal §2 lists the two companion edits L1 would make (add the row; amend the `corpus/README.md` index line to Q01–Q14); coverage-map rows and their statuses stay untouched.

## 3. Red exemplars (frozen bytes, cwd=/)

```
$ python3 -B .../q14_inventory.py frozen/corpus/knowledge/commonjs-destructured-require-edges.md --root frozen
NO-FACTUAL-INVENTORY  commonjs-destructured-require-edges.md:1 entry has no `## Factual inventory` table
GAP-COVERAGE-CLAIM    commonjs-destructured-require-edges.md:80 claims 'span' but no print in the entry code shows it :: ...not the v2 digests, edge spans or the unnamed edge (...); this entry's block carries those values.
$ python3 -B .../q14_inventory.py frozen/corpus/knowledge/evm-saved-interface-candidates.md --root frozen
NO-FACTUAL-INVENTORY  evm-saved-interface-candidates.md:1 entry has no `## Factual inventory` table
PROSE-VALUE-NOT-IN-INVENTORY evm-saved-interface-candidates.md:63 '0x10' :: ...its embedded JUMPI target (0x10)...   ('0x5B' same sentence)
PROSE-VALUE-NOT-IN-INVENTORY evm-saved-interface-candidates.md:91 '37' :: ...none of 37 single-conjunct deletions...   ('9' same sentence; the [1, 9] inclusive span)
GAP-COVERAGE-CLAIM    evm-saved-interface-candidates.md:91 claims 'span' but no print in the entry code shows it
$ python3 -B red_exemplar_check.py frozen   # C04 extent_vocab_hits=0 pattern_hits=0; C09 pattern_hits=0
```

C04: the block has 0 hits for `span|location|column|start|offset` while its Limitations sentence says "this entry's block carries those values" — the closure's count, reproduced. C09: the block never searches the nine-byte pattern and its printed output carries neither `0x5b` nor `0x10`. The asserted values are **correct** (frozen bytes, read-only: `len 35 / raw 0x5b count 0 / raw 0x63 count 1 / pattern len 9 / pattern starts [1]`) — M26's shape: right value, no in-entry derivation.

## 4. Controls (synthetic, scratch only)

```
control-green.md -> no findings;  control-red.md -> ROW-VALUE-NOT-PRINTED (bytes=36 not in the output)
control-record-wrong.md -> ROW-VALUE-WRONG-RECORD (value 16 only on lines without r24)
control-recorded.md -> clean when records/rec.json holds ev_test_1; else RECORD-DOES-NOT-HOLD-VALUE
```

## 5. Conflict recorded (peer `R62CriticQ14`)

The critic argues **no** Q14 row should be added ("Its reject conditions … are Q11's own text") and showed a value-presence inventory is silent on its mutants. Its conditional is adopted verbatim in the row text and its rules 1–4 are the row's audit procedure. Three mutant rounds were run against the command; every named class is now surfaced — round-1 m1 `:63 '16'`, m2 `:71 '0x10'`, m3 `:63 '0x10'`, m4 `GAP-COVERAGE-CLAIM`; round-2 a1 `ROW-UNTAGGED-ROW`, a3 `:63 '16'` (per-record coverage), a5 `:63 '0x10'` (a source citation no longer exempts), a6/a6b/a6c `:63 '16'` (`fixture.raw:16` is a value, not a locator), a7/a7b `RECORDED-WITHOUT-FIELD`/`RECORD-FIELD-NOT-FOUND`, a8/a9 `GAP-COVERAGE-CLAIM`; round-3 b1 `:63 '16'` (a negated record mention no longer widens the scope), b3 `ROW-VALUE-NOT-PRINTED … bytes is bound to ['18','18','34'], not to '30'` (value must be bound to its key), b4 `RECORD-FIELD-NOT-FOUND` (exact field key, all tokens on that field's line), b6 `GAP-COVERAGE-CLAIM` (the class term must be a printed field key, not a string literal). The honest control `v0` no longer trips a false `ROW-NOT-IN-CODE-PRINT`. The critic stopped after round 3 with the position that a lexical helper can only be triage; its final verdict is unchanged — prefer no Q14 row, and if one is added, only with the conditional plus §6. The mutant coverage above is a statement about the command, not a validation of the row; the proposal adopts the triage-only limit (proposal §6 item 10) and L1 keeps both readings.

## 6. Limits / unknowns — known-silent classes

Proposal §6 lists them in full (ten items). The command is **triage, never certification**: it cannot check that a printed field was derived from the same record by the same method (raw bytes vs decoded instructions), that an inventory and an output that agree are not both wrong, that words without numerals ("several") are counts, that a record-less sentence is bound to the right row, that tokens inside identifiers are values, or that the stored output still matches its code; the round-3 fixes rely on negation markers ("unlike", "not") and on the class term being a printed field key, so paraphrases and renamed keys remain silent. It does not touch Q01 tier scope, Q03/Q06 premises, Q07, Q09 or Q13. Not the round's admission mechanism; the non-author Q11 audit remains the necessary admission condition. Scratch copy is removed on landing; the row text and rules survive in this report and the proposal file.

## 7. Touched surfaces / installs

Written: this report (lane `.ufo/waves/round-62/build/`) and scratch under `/fast/scratch/hyaku/revenger-r62/R62Q11InventoryRule/` (proposal, helper, two checkers, four controls, frozen extract). Not touched: `corpus/` (verified `git diff --stat -- corpus/` empty), no jj/Git index or history mutation, no fixtures, no live runs. Installs / updates: **none** (stdlib Python only).
