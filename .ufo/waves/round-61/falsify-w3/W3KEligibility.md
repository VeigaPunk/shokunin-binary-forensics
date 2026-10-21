GRADE: PARTIAL — C1 eligibility (C04/C09 base status, work-evidence cells, Q01–Q11 and round-61 tier-A source conjuncts) on ab58069

Scope: eligibility only. Base archive cf02419 and landed ab58069 extracted to
/tmp/revenger-r61w3-W3KEligibility{,-landed}; read-only `git show`/`archive`, no lane writes.

1. HOLDS — both rows uncovered at base. `git show cf02419:corpus/README.md`:
   `:30 | C04 | JavaScript/Electron packages | — | ... | uncovered |`,
   `:35 | C09 | EVM bytecode interfaces | — | ... | uncovered |`. Knowledge cell `—` in both;
   claims.md:21-24 restates exactly this.
2. HOLDS — work-evidence cells existed and resolve at cf02419. Every path named at
   claims.md:22-24 exists in the base tree: `fixtures/js-r3`, `js-r7-v2`, `shapes-r12`,
   `verify_js_graph_delta.py` (base cell also `verify_semantic_trace.py`,
   `verify_shape_evidence.py`), `fixtures/evm-r19`, `evm-r21`…`evm-r26`,
   `verify_evm_evidence.py`; `ls corpus/fixtures | grep '^evm-r'` → r19, r21–r26 (no r20),
   matching README:35.
3. HOLDS — Q01–Q11 boundary. Base `corpus/QUALITY.md:23` already defines Q11 ("Supersedes Q08").
   The base README index stale text at `:9` ("Q01–Q10") is pre-existing and does not make
   claims.md:31 wrong.
4. HOLDS — tier-A rows opened this round. Base SOURCES registry ends at S015; S016–S027 are new
   at 0b6ddf0, `opened 2026-10-21`, tier A for S016–S023/S026/S027 (S024/S025 are rejected rows,
   cited only as rejects). C04 header `:1` cites S020–S023+S027; C09 header `:1` cites
   S016–S019+S026. Round-61 opening is recorded in round-61.md:48-70.
5. HOLDS — no harm. `diff -rq` base→landed over the 10 fixture dirs and 9 saved records
   (20261012T164357Z, round-7 v2, round-19,21–26): all SAME. A1 conditions hold: held rows base 4
   (C01,C11,C12,C13) → landed 6 (+C04,C09); 14 rows both; no other status moved. K re-count with
   the SCORECARD:133 regex → 4 (base) / 6 (landed).
6. GAP — claims.md:33 "and survives the wave-2 attacks" was not met at landing. Wave 2 landed
   0/65 reports (`.ufo/waves/round-61/falsify/dead-seats.json:2,6-8`: `"wave": "r61-falsify"`,
   `"reports_landed": 0`, `"dead": 65`); the lane itself records the unmet conjunct
   (SCORECARD.md:220-222; LOG.md:804). Admission is therefore provisional on this fresh wave, not
   evidenced at ab58069. LOG.md:804 cites `claims.md:32` but the phrase sits on :33 (off-by-one).
7. GAP — Q11 derivation form in the C09 entry (eligibility conjunct claims.md:32 "carries in-entry
   derivations (Q11)"). `evm-saved-interface-candidates.md:60` asserts "the file has no 0x5B byte";
   `:35` asserts "target 16 is a STOP". Both true by my byte read (`r24` raw 0x5b count=0; `r25`
   bytes `0060003560e01c63deadbeef14601057005b00`, byte 16=0x00), but the Reproduce output
   (`:102-138`, Provenance `:140-166`) prints only push4/raw_0x63/jumpi/jumpdest/entry_op — no raw
   0x5B count and no byte 16. Q11's reject condition ("a value is correct when re-derived but the
   entry carries no derivation") applies to :60, and the entry's Q11 row `:187` ("every count ...
   carries the command above and its output") overstates that one count. If Q11 is read literally,
   C09 fails the Q01–Q11 conjunct and K is 5/14, not 6/14.
8. Note — C04 has a smaller parallel at `:39-40` ("not the `module.exports` keys"): the block
   prints `exposes_exported_names=['default']` but never prints the `module.exports` keys. Sibling
   W3JsLabelsDefault owns that line; not counted in this grade.
9. Note — the Gate admit rows (`round-61.md:77-78`) list criteria but omit Q09 for both admits
   (entry tables `:176-188` do record Q09 pass), so the "criteria checked" record is abbreviated,
   not false.

VERDICT: Eligibility premises verify exactly (uncovered at base, work evidence present, round-61
tier-A rows cited, fixtures/records byte-identical, no lost hold); PARTIAL only because
claims.md:33's wave-2 conjunct was unmet and self-disclosed, and the C09 entry leaves one counted
value (:60) underived, which under Q11's letter would leave K at 5/14.

Installs: none. Scratch only under /tmp/revenger-r61w3-W3KEligibility*; lane tree untouched except
this report.
