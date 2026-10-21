GRADE: BROKEN — round-62 C04 `round-62-commonjs-require-name-evidence.md` and C09 `round-62-evm-dispatch-byte-evidence.md` sentence-to-output inventories as Q11 substitute (Q11 failed on both)

Seat R62FCriticInventoryMethod (critic; not author/corrector). Frozen revision `d97761952be256d145d298022de03091de91d358`
(`git archive` → `/fast/scratch/hyaku/revenger-r62/R62FCriticInventoryMethod/tree`, cwd=/, TMPDIR under that seat).
Candidate SHA-256: C04 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3`; C09 `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e`.
`git diff --name-status a3498e25…d9776195 -- corpus/fixtures corpus/live` → empty; `corpus/QUALITY.md` not in the full diff (Q01–Q13 unchanged).

## Observation (commands on archived copy only)
O1 Both §Reproduce blocks, extracted verbatim, run with Python 3.14.8: C04 `exit=0 lines=25 sha=58b63dd9…0c416 stderr=0`, `cmp` equal to the entry's stdout;
   C09 `exit=0 lines=8 sha=aff3efda…235bf stderr=0`, equal. Output equality holds; that alone cannot pass Q11 (claims.md:97-101, lesson :97-101).
O2 Hidden helper / Q14: `grep -i "Q14|helper|lexical|token|verify_"` on both entries → only disclaimers (C04:65,276; C09:164). The full diff adds no `.py`
   and no QUALITY row. No hidden helper authority landed. But both Q11 decision rows rest on the inventory itself (C04:294 "the §Sentence-to-output
   inventory maps every factual sentence"; C09:200 "`## Evidence inventory` names the field and the value"). The inventory is the instrument under attack.
### C04 — values with no in-entry derivation or recorded label
O3 C04:1 and C04:248, ECMA page "single-page SHA-256 `06db92a8…7d27d7f`". This digest has no derivation command or output in the entry and no
   "recorded, not re-derived" label (contrast items 7 and 20, which carry that label). Inventory rows 1–30 never cover header/§Sources. → Q11 failure condition.
O4 C04:248 says the quote is "— 8 words." Over the entry's own quote, `len(q.split())`=6. The page form it gives, "Set value to ? GetV ( value , propertyName ).", splits to 10.
   `[A-Za-z]+` gives 6. The count has no in-entry derivation and none of these obvious conventions reproduces it. → Q11.
O5 C04:4,77,80 give `readout.py` SHA-256 `31dac211…`, stdout SHA-256 `58b63dd9…` and "25 stdout lines". I re-derived all three and they are correct (O1; the block's sha = `31dac2113f1b…02ac`).
   But no `sha256sum`/`wc` command or its output appears in the entry. Correct-but-underived → Q11 ("a value is correct when re-derived but the entry carries no derivation").
O6 Referent mismatch on "line 1" (C04:2 anchor `index.js:1`, item 3 "line 1 is …", item 11 "saved location … is exactly the manual … span").
   Code C04:161-162: `lines=[l for l in text.split("\n") if l.strip()]; enumerate(lines,1)`. So `line_number_1based` is the ordinal among non-empty lines,
   not the physical line. Code C04:148: `span_text_from_fixture` slices the regex-matched line and ignores the saved `start_line`, which is never compared to anything.
   Mutation (scratch copy only; one blank byte prepended to js-r3/index.js): `mutJ exit=0`, `{'line_number_1based': 1}`, the delta is still `kept ['checksum','rot13']`,
   every edge prints `start_line 1` with span text `{ rot13, checksum } = require('./transform')`, and physical line1 of the mutated file is `''`.
   The readout still prints full agreement while the saved line now points at an empty line. Frozen bytes have `blank=0` and `physical_lines=7`, so the value is coincidentally correct.
   The derivation never derives the claimed referent (physical line, saved-line correspondence). → Q11; also undercuts the Q03/Q06 basis for item 11.
O7 Item 11 says "the saved spans are the manual spans", but no printed field computes that equality. The reader compares `[28,50]` to `[28,50]` by eye (output equality, not derivation).
   Column unit (chars vs bytes vs UTF-16) is labelled by the code's own field names (`start_column_0based`, `end_column_0based_end_exclusive`), not derived; ASCII-only is not printed.
### C09 — values the inventory points at but the code does not derive
O8 C09:56 "r19's carrier is a 39-byte `0x`-prefixed ASCII hex file". Code C09:362,366 `bytes.fromhex(carrier[2:-1]…)` assumes a 2-byte prefix and 1-byte trailer.
   No output field prints those bytes; on frozen bytes they are `0 x … \n` (od). Mutation (scratch copy; prefix→`zz`, trailer→`?`): `mutE exit=0`;
   `decoded SAME`, `instructions SAME`, `valid_jumpdest_offsets SAME`, `jumpi_with_preceding_push1 SAME`, `candidate_pairs_normalized SAME`, `pattern SAME`.
   Only the carrier sha and subject/artifact scopes changed. QUALITY Q11: "Constants such as header offsets are derived, not assumed." Here they are assumed. → Q11.
O9 Several "each record" claims (C09 Obs3, Inference 2: "each record's own kind, deployment_authenticity and hardfork … unknown") point only at `r19.*`.
   Inventory row C09:241 maps three fields to one pointer `r19.recorded.bytecode.kind`. The values are in stdout for all 7 (correct), but the inventory under-points.
O10 "11 instruction tuples" (C09:78) is a count with no printed count field; it is countable from the `r19.instructions` list. "pattern … derived from the files' own bytes" (C09:101)
   is derived from r19 only (`derive_pattern(r19)`, C09:362). Inventory row "artifact bytes and encoding" (C09:239) gives only `39`; `encoding` is printed but not inventoried.

## Inference
I1 [INFERENCE] Both inventories enumerate observation sentences. They do not audit headers, §Sources, §Reproduce metadata or the code's referents. They therefore let value-token presence in
   stdout stand in for derivation, which is the easier substitute that claims.md:100-101 and the lesson's Gate forbid. O3–O6 and O8 are values a token/pointer audit passes and Q11 fails.
I2 C04 O3/O4/O5/O6 are actual missing requirements under unchanged Q11 → BROKEN. C09 O8 is an assumed header offset under Q11's explicit constant clause → BROKEN.
   C09 O9/O10 and C04 O7 are nonfatal wording/pointer defects (PARTIAL-class).
## Unknown
U1 Whether §14.3.3.3's quoted step belongs to the `SingleNameBinding : BindingIdentifier` production as C04:46 states (lesson:70 says "step3"). Not opened here (Q01 seats).
U2 Whether L1 treats self-referential readout/stdout digests (O5) as entry values; the lesson Gate (":97 headers, prose, tables and limitations") suggests yes.

## Smallest safe corrections (not applied)
C04: (a) label the ECMA page digest and the "8 words" count "recorded, not re-derived", or derive both in-entry with command and output (the count needs a stated convention).
 (b) Print `sha256sum readout.py`, `| wc -l | sha256sum` with output, or label them recorded. (c) Derive physical line numbers (`text.split("\n")` without filtering).
 Compare saved `start_line`/`end_line` to them, slice the saved line, and print an explicit equality field for item 11.
C09: print the carrier's prefix/trailer bytes (e.g. `carrier[:2]`, `carrier[-1:]`) and fail unless `b"0x"`/`b"\n"`. Point "each record" claims at all 7 cases or print an all-records field.
Both: extend the inventory to header/§Sources/§Reproduce values. Focused re-review on corrected bytes by an existing fresh-wave seat.

VERDICT: BROKEN — C04 fails Q11 (O3–O6); C09 fails Q11 (O8). Neither is admissible on this frozen revision; C1 K stays 4/14 for these candidates as frozen.
No repair, no admission. No JS/EVM execution, no producer/REA/chain/network. Scratch: `/fast/scratch/hyaku/revenger-r62/R62FCriticInventoryMethod/` (tree, mutJ, mutE, outputs).
Installs: none.
