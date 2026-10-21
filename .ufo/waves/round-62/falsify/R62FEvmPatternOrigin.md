GRADE: HOLDS
target: corpus/knowledge/round-62-evm-dispatch-byte-evidence.md (C09 candidate)
frozen revision: d97761952be256d145d298022de03091de91d358 (git archive -> own scratch)
candidate sha256: 6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e
attack: trace r24 searched-pattern construction from r19 instruction boundaries
(PUSH4..JUMPI inclusive); exact hex/length vs original byte arrays; does code
assume 9 bytes rather than derive; is embedded PUSH1 operand/target read an
actual byte comparison, not a truth-intent shortcut.
scratch: /fast/scratch/hyaku/revenger-r62/R62FEvmPatternOrigin

## Observation (commands + exact output)

1. Entry reproduce block re-run on frozen archive (cwd=/, TMPDIR=<scratch>/tmp):
   `python3 -B readout-entry.py /fast/scratch/hyaku/revenger-r62/R62FEvmPatternOrigin`
   exit 0; `diff recorded-stdout.txt actual-stdout.txt` -> empty: the entry's
   `## Provenance` stdout is byte-for-byte its own `## Reproduce` code's output.
2. Frozen fixture identities: sha256(evm-r19/fixture.hex)=
   294e6fd2e041d5bea0558a26c1e399eddccf71bc0d279d398a4c0e915517b827;
   sha256(evm-r24/fixture.raw)=
   b69834e0ef786e3c001b2c833c8c0388acc017de14d06110cfa85d4948685d93 — equal the
   entry's `r19.carrier.sha256`/`r24.carrier.sha256`. r19 decoded
   `60003560e01c63deadbeef14601057005b00`; r24 raw `7f63deadbeef14601057`+23×00+`5000`.
3. Independent trace (own walk implementation, independent-trace.py, no code shared
   with the entry) exact output: r19 first PUSH4 opcode offset [6]; first JUMPI
   opcode offset [14]; `INDEPENDENT pattern slice r19[6:15] hex=63deadbeef14601057
   length=9`; `r19 bytes[6:15] == pattern: True`; `r24 bytes[1:10] == pattern: True`;
   `r19 occurrences: [6] inclusive spans: [[6, 14]]`; `r24 occurrences: [1]
   inclusive spans: [[1, 9]]`; `r24 embedded PUSH1: in-pattern index=6
   opcode_offset=7 operand_offset=8`; `r24 operand byte value=16 target_offset=16
   target_byte=0 raw_0x5b_cmp=False`; `ALL INDEPENDENT CHECKS AGREE WITH ENTRY RUN`
   (asserts against entry-run r24.pattern/summary JSON passed).
4. No hardcoded length: `grep -n '\b9\b' readout-entry.py` -> no match (exit 1);
   length arises only from slice end `code[p4[0]:ji[0] + 1]` (candidate :338) and
   `len(pattern)` (:344, :346, :417). r19 has exactly one PUSH4 ([6]) and one
   JUMPI ([14]) instruction, so `p4[0]`/`ji[0]` are unambiguous.
5. Embedded reads, candidate :352-357: PUSH1 located by `pattern.index(P1)` in the
   actual pattern bytes; operand byte read `code[po+1]`; target byte read `code[ov]`
   bounds-checked; boolean `embedded_target_is_raw_0x5b=(tb == JD)`, JD=0x5B — a
   runtime comparison on the read byte. Sensitivity proof (in-memory copies only):
   target byte -> 0x5B flips the comparison True; operand byte -> 0x11 moves the
   target offset to 17 (byte there 0). No hardcoded boolean, no precomputed set
   membership, no skipped branch: not a truth-intent shortcut.
6. r24 occurrence is a raw-byte substring fact, not an instruction boundary (walk
   gives [[0,127,imm],[33,80,""],[34,0,""]]); the entry keeps raw vs instruction
   facts apart and claims occurrence/span/length only as raw-byte facts.

## Attack answers

Construction from r19 boundaries: derived, not assumed (prose :101-103 matches
r19[6:15] exactly; derivation code :333-338). Hex/length vs original byte arrays:
exact match on both arrays, spans [[6,14]]/[[1,9]], counts 1/1 match
`r24.pattern.*`/summary. Assumes 9 bytes? No. Embedded operand/target: actual byte
reads plus actual `== 0x5B` comparison, demonstrably byte-sensitive.

## Inference

The three attack questions resolve in the candidate's favor; r24 pattern claims are
true in-entry derivations with printed output (Q11 satisfied for these values).
Non-material wording observations, no criterion failure, for L1 only:
(a) :101-102/:192 "the files' own bytes" (plural) — derivation uses r19's bytes
only; code comment :334 correctly says "the file's own"; true as a class statement
(authored bytes vs saved fields), loose distributively; no value corrupted.
(b) :221 inventory row "pattern bytes and length" names `summary.pattern_hex` only;
the length's printed field is `summary.pattern_length` ("pattern_length":9 in the
same summary object). Both values derived and printed in-entry, so Q11 substance
holds; a one-row split would make the pointer exact. Neither rises to
BROKEN/PARTIAL ("contradiction/missing requirement" not met).

## Unknown

- Whether fresh-wave Q11 seats weight the :221 row pointer as a defect is an L1
  adjudication; this seat records it as non-material wording.
- Out of scope: provider/record-field authenticity, empty-pair cause, other cases'
  occurrences beyond the byte comparisons reported above.

VERDICT: attack falsified no claim; candidate HOLDS on pattern-origin, length
derivation, and embedded operand/target semantics. No repair proposed (observations
are optional polish, listed only). Installs: none performed.
