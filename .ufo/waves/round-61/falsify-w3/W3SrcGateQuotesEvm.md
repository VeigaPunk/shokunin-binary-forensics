GRADE: PARTIAL — lessons/round-61.md:55-58 gate quotes for S016–S019 (C1 source gate)

## Method

Archive `ab580698212258a55e43e9bb9bf6ac78c91eae2a` extracted read-only to
`/tmp/revenger-r61w3-SrcGateQuotesEvm` via `git archive`; URLs re-opened 2026-10-21 with
`curl -sSL`; PDF text via `pdftotext`; quotes checked as exact substrings after whitespace
normalization (line wraps only), word count per quote. Lane tree untouched; no bytecode/JS run;
no REA devices; no services. Installs: none (curl, pdftotext, python3 already present).

## Result — every quote is verbatim and ≤25 words

- S016 (`round-61.md:55`): served runtime.py, 69 lines, SHA-256
  `a2801c4169b806a9494707179a9df20170a37a1769596aac56013ddba509aef8`. Quote is exactly
  `runtime.py:29-30` (line 29 ends `...corresponding to`, line 30 `` `PUSH-N` opcodes. ``);
  13 words, 1 occurrence. `git ls-remote` peels `refs/tags/v2.20.0^{}` to
  `2004296f2ffcbcebcd00f41152d33e8dfda0922a`, matching `SOURCES.md:30`. Opcode line claims
  also hold: `instructions/__init__.py` (SHA-256 `49dd6155…b63724`) lines 55/106/109/125 =
  `EQ = 0x14`, `JUMPI = 0x57`, `JUMPDEST = 0x5B`, `PUSH4 = 0x63`. MATCH.
- S017 (`round-61.md:56`): PDF SHA-256 `d67c009c5d5a0542c8288aee3c4d470b3e2dbe6e664f72f00011543608477fa9`
  exactly as the preamble and `SOURCES.md:31`; title page `SHANGHAI VERSION efc5f9a – 2025-02-04`;
  heading `9.4.3. Jump Destination Validity.` at `s017.txt:2816`; form-feed count puts the quote on
  PDF page 15 at `s017.txt:2820`; 19 words, 1 occurrence. § and page MATCH.
- S018 (`round-61.md:57`): page title `Solidity 0.8.37-develop documentation`; h2
  `Function Selector` with anchor `#function-selector` at HTML:203-204; quote at HTML:205-207;
  20 words, 1 occurrence; the section text is identical (whitespace-normalized) to
  `/en/latest/abi-spec.html`, supporting the row's `SOURCES.md:32` "byte-identical" claim. MATCH.
- S019 (`round-61.md:58`): HTTP 200, `last-modified: Tue, 29 Sep 2026 13:01:07 GMT` (row says
  2026-09-29), title `Solidity 0.8.38-develop documentation`, body SHA-256 `3407a364…c9ba64`
  (same bytes a sibling measured). Quote at HTML:184; 19 words, 1 occurrence. Text MATCH.

## Mismatches (both locator/presentation, neither contradicts a claim)

1. `round-61.md:58` states `§Contract Metadata, para 1`. The quote is **not** in paragraph 1.
   Served HTML: `<h1>Contract Metadata` at :176, paragraph 1 is `<p id="index-0">` at :177
   ("The Solidity compiler automatically generates a JSON file…"), a 2-item `<ul>` at :179-183,
   then the quoted paragraph at :184. The quote is the **second** prose paragraph of the section
   (section name itself correct). Exact fix: `para 2`, or "intro paragraph".
2. `round-61.md:56` S017 quote truncates mid-sentence with no ellipsis; the source continues
   `operations and must appear within the explicitly defined portion of the code (rather than in
   the implicitly defined STOP operations that trail it).` (`s017.txt:2820-2823`). Quoted words are
   contiguous and verbatim; the omitted conjunct is a second requirement the entry does not use
   (`evm-saved-interface-candidates.md:123` needs only opcode-0x5B-at-instruction-start). Nit only.
3. `round-61.md:58` S019 quote likewise truncates before `(not necessarily the creation bytecode)
   of each contract` without an ellipsis. The entry asserts nothing about creation bytecode
   (`evm-saved-interface-candidates.md:72`), so this is silence, not contradiction. Nit only.

## Adjacent observation (not the grade basis)

Lesson locator (§Contract Metadata intro) and entry/row locator (§Encoding of the Metadata Hash in
the Bytecode, `SOURCES.md:33`, `evm-saved-interface-candidates.md:1`) differ, but both locations
carry "by default" verbatim: the §Encoding subsection at HTML:359-360 says "The compiler currently
by default appends the IPFS hash (in CID v0) of the canonical metadata file and the compiler version
to the end of the bytecode." The entry's own section anchor is therefore supported; sibling
`W3EvmMetadataCite.md` grades that entry-side citation HOLDS, consistent with this result.

VERDICT: All four gate quotes are genuine, verbatim, single-occurrence and ≤25 words, and S016/S017/S018
sections/lines/pages are exact; only S019's `para 1` is one paragraph off (quote sits in para 2),
plus two unmarked mid-sentence truncations — PARTIAL for the locator nit, no evidence of a broken or
fabricated quote and no Q-criterion failure on quote grounds.
