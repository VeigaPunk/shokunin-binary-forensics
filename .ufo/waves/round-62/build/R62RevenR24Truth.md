RESULT: COMPLETE
Seat RevengerR61-2.R62RevenR24Truth · leaf · scope: independently decode r24 + its authoring ledger; explain `[1, 9]` as inclusive span; no misquote of the old entry; deliver explicit calculation + evidence wording.
Frozen tree a3498e25ad87bf756288812d0ea7c474b09433c7 (2026-10-21 14:56:58 -0300, "round-62: freeze C1 coverage replacement admission and K4/14 baseline before build") extracted via `git archive` to /fast/scratch/hyaku/revenger-r62/R62RevenR24Truth/; all checks are read-only stdlib on that copy. No REA producer, no bytecode/JS execution, no live-tree edits.

1. Explicit calculation (command + full output)
$ cd / && python3 -B /fast/scratch/hyaku/revenger-r62/R62RevenR24Truth/out/r24_span_calc.py
A. bytes file_sha256=b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93 len=35
B. truth sha256=b69834e0… size=35 sha_eq=True size_eq=True
C. truth embedded_pattern_hex=63deadbeef14601057 pattern_len=9 hex_chars=18
D. byte-search starts=[1] count=1 inclusive_spans=[[1, 9]]
E. arithmetic end=start+len-1: 1+9-1=9 truth_pair=[1, 9] pair_eq_span=True
F. d[1]=0x63 d[9]=0x57 d[10]=0x00 d[9:18]=570000000000000000 d[9:18]==pattern: False possible_starts=27
G. raw 0x63=[1] raw 0x57=[9] raw 0x5b=[] raw_0x5b_count=0
H. instruction_walk=[(0, '0x7f'), (33, '0x50'), (34, '0x00')] push4_instructions=[] executable_push4_count=0 truth_executable_push4_count=0
I. embedded_shape={push4_at:1, selector:deadbeef, eq_at:6, push1_at:7, target_operand 0x10=16, jumpi_at:9} d[16]=0x00 target_is_jumpdest=False
J. immediate=(1, 32) span=[1, 9] span_inside_immediate=True
K. two_occurrence_reading(count=2,start9)=False observed_count=1

2. `[1, 9]` = inclusive span: source-field semantics vs array-of-occurrences convention
- Field semantics (what r24's producer recorded): `corpus/fixtures/evm-r24/truth.json:9-13` `embedded_pattern_hex` `63deadbeef14601057` (9 bytes) + `embedded_pattern_offsets [1, 9]` is the inclusive `[first_offset, last_offset]` pair of ONE occurrence. Proof from bytes, not name: exactly one occurrence exists (D); the second element reproduces `start + length − 1 = 1 + 9 − 1 = 9` (E); the span lies wholly inside the PUSH32 immediate (J). Corroborated by both authoring-time prose records (§3).
- Array-of-occurrences convention (what the plural name suggests): elsewhere plural `*_offsets` enumerates individual offsets — pe-r33/truth.json:14-39 `changed_offsets` = five individual `{offset,before,after}` entries (738,740,742,744,746); pe-r41/truth.json:8-11 `header_changed_offsets` = individual offsets (68,69,84,…). Read that way, `[1, 9]` would claim occurrences at 1 and 9 — byte-falsified: observed count 1 (D, K); offset 9 holds `0x57`, the pattern's LAST byte, and `d[9:18]` ≠ pattern (F). Fixture may not be renamed (claims.md harm clause), so the round-62 entry must state the r24 semantics explicitly; discriminator = arithmetic (E) + byte search (D), never the field name.
- Same decode gives the explicit embedded target the C09 candidate must carry: embedded `PUSH1 0x10; JUMPI` → operand 16; byte 16 is `0x00`; raw `0x5B` count 0, so 16 is not a JUMPDEST (I, G); raw-byte vs instruction counts separated (G vs H).

3. Historical ledger, verbatim (no misquote)
- LOG.md:289 (2026-10-12): "dispatch-looking bytes `63deadbeef14601057` occur only inside immediate offsets 1–9, not as instructions".
- corpus/live/runs/round-24/LEDGER.md:3: "The r19 dispatch-looking nine bytes `63 deadbeef 14 60 10 57` occupy offsets **1–9 within that immediate**".
- Old entry AS FIRST LANDED (git show 0b6ddf0:corpus/knowledge/evm-saved-interface-candidates.md:88-89; blob saved at out/orig-candidate-0b6ddf0.md): "lists embedded-pattern offsets `[1, 9]`; the bytes contain the pattern only at 1 (fixture left unchanged)." — it did NOT say "two occurrences" and did not call the bytes inconsistent. `0b6ddf0` = 0b6ddf07f33184baf901dd807ddc72a95f4010c1; the correction 0597e53 changed only this sentence (out/correction-diff-0b6ddf0-0597e53.patch).
- The two-occurrence misread was the build seats' reading of the plural field name: .ufo/waves/round-61/build/ExecSelectorKeccak.md:26 "Truth defect"; ScribeEntryEvm.md:30-32 "The second entry is inconsistent with the bytes".
- Lesson M25 (corpus/lessons/round-61.md:41) attributes that phrasing to the entry too ("the build seats and the C09 entry (at `0b6ddf0`) stated that … names two occurrences 'inconsistent with the bytes'") — that attribution is imprecise against the 0b6ddf0 text; already flagged in-lane (corpus/lessons/round-61.md:117-119 "M25's imprecise attribution"; W3EvmR24SpanFix.md F3 LOW). Round-62 wording must quote the 0b6ddf0 sentence verbatim and attribute the misread to the seats, not repeat M25's attribution.
- Retained entry's corrected sentence, quoted as history only (corpus/knowledge/evm-saved-interface-candidates.md:94-96): "`embedded_pattern_offsets` `[1, 9]` is the inclusive byte span of the one 9-byte pattern occurrence (offsets 1–9, authoring note `LOG.md:289`), consistent with the bytes." Its known defect remains: no in-entry derivation (W3EvmR24Immediate BROKEN b; W3EvmQTable F1) — the new candidate must derive it, per §4.
- Closure recount is consistent with, not a substitute for, my D line (round-61-verifier-spotcheck.md: "all byte-search starts=[1]; inclusive spans=[[1,9]]; occurrence count=1").

4. Correct evidence wording — proposed (scratch file, ready to lift into round-62-evm-dispatch-byte-evidence.md)
- /fast/scratch/hyaku/revenger-r62/R62RevenR24Truth/out/r24-span-wording-proposal.md: §1 span+target sentence with every value derived in-entry; §2 embeddable snippet + observed output (matches calc lines D/G/I; equals M25's own fix check, round-61.md:41 fix cell); §3 field-semantics-vs-convention paragraph; §4 history paragraph with the verbatim quotes above; §5 derived-vs-recorded labels (saved `ev_50d5ffb1…` record fields cited, not claimed).
- Core span sentence: "`embedded_pattern_offsets` `[1, 9]` is the inclusive `[first_offset, last_offset]` pair of one occurrence: the byte search finds exactly one 9-byte occurrence (start 1), `1 + 9 − 1 = 9` reproduces the second element, and the two-occurrence reading is byte-falsified (offset 9 holds the pattern's last byte `0x57`; `d[9:18]` ≠ pattern)."

5. Bounds and unknowns
- Did not re-open S028/S029/S030/S031 source rows or judge Q01–Q13 for the candidate (entry writers' seat); this is input wording + derivation, not an admission and not a K credit.
- Did not read the saved round-24 inspection.json record fields beyond §5 labels (not needed for the span question); no provider behavior claim made or implied.
- Full script: out/r24_span_calc.py; proposal: out/r24-span-wording-proposal.md; pre-correction blob: out/orig-candidate-0b6ddf0.md; correction diff: out/correction-diff-0b6ddf0-0597e53.patch — all under /fast/scratch/hyaku/revenger-r62/R62RevenR24Truth/out/.
- No README row marked held; prior evidence untouched; counterexamples and rejected files read read-only.

Installs: none.
