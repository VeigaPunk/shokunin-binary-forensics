FAIL — Q16: the checked-literal scope is stated, but cited `readout.py` literals outside items 12/17 are not individually named unguarded; the Observation's locator list is incomplete.

## Scope and axes

Audited final v6 entry `corpus/knowledge/round-71-apk-axml-byte-evidence.md` against the frozen Q13/Q14/Q16 wording and W1 repairs. Axes: command/stdout accuracy; observed/recorded/inferred/unknown boundaries; unguarded-literal accounting; Q13 gate-survivor honesty; stale round-70 prose.

## Evidence / exact lines

- Candidate entry is 324 lines, still `admission-status: candidate` at line 12. Frozen candidate file matched HEAD/worktree in the checked path; task candidate commit is `4c1eeaee88fd07e442f1bd546faf77be3957d390`; lane HEAD was `c6e284c6583fa3502754361f411b66646880ba02` (freeze commit). No source edits made.
- Baseline gate in scratch copy: `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0`.
- `--spec-quotes` produced six `MATCH` rows. Each includes snapshot file, first-line number, `folded phrase present=True`, and searched phrase; none is a raw source line. Entry lines 120, 144–150 accurately describe/render this shape (line 120's prose omits the presence flag, but does not falsely assert a different shape; S052 header line 8 includes it).
- `--zip-layout` produced 20 stdout lines: three fixed-width sums, twelve literal matches, three `MATCH APPNOTE` locator rows, then central/local fixed-part comparisons. Entry line 153 accurately says stdout lines 16–18/20 locate the layouts and the final two compare widths. W1's earlier 21-line concern does not reproduce on this output.
- `--axml-layout` output matches the 23 lines embedded at 255–278: five width-array comparisons, one node-width statement, and 17 offset comparisons. Entry line 251 describes the AXML comparison; line 314 appropriately limits credit to printed offsets.
- Observation line 283 is materially bounded: command blocks “record” displayed counts/offsets/identifiers/digests; item 13 is selected oracle comparison; items 3/5/12/17 use manual widths/sums; and it says only item-12/17 literal subsets are compared. Inference/unknown lines 284–285 distinguish deductions and disclaim provider/install/program-validity claims. Coverage/header lines 11, 16, 293 and limitations line 289 are similarly scoped. Item 13 lines 179–216 specifies comparison fields and explicitly limits the oracle's authority.

### Located Q16 defect — FAIL

Q16 criterion in `corpus/QUALITY.md:28` requires every non-printed member of a credited set to be named unguarded. Entry line 283 names only these locators-only: `readout.py:22, :76, :166, :189, :197, :211, :233-248`. But other cited readout source locations/literals are outside the item-12/17 printed-comparison sets and are not named as locators-only/unguarded, including:

- Entry line 40 cites `readout.py:105` and credits the payload-offset formula. Item 12 compares local-header fixed width and lengths at offsets 26/28, but not the full payload-offset expression (`:105`); the AXML list in item 17 is irrelevant.
- Entry line 64 cites `readout.py:51-58` (manual width transcription); line 68 prints widths/sums, but does not compare these source literals against `ResourceTypes.h` at runtime. They are correctly called manual, yet are not listed among Q16's locators-only/non-compared members.
- Entry line 73 cites `readout.py:155-168`; item 17 compares only selected string-pool header offset literals, not the string-offset loop/source expressions at `:155-168`. The displayed strings are observations, not source-literal comparisons.
- Entry line 87 cites `readout.py:203` (`aoff` expression), which is explicitly labeled as an inference; item 17 checks several AXML offsets but not the complete `aoff` expression. Line 283's locator-only list omits `:203`.

Thus the broad line-283 characterization—“`readout.py:N` citations are source locators”—does not satisfy Q16's explicit requirement to name every remaining member unguarded. The Q16 row at line 314 lists only specified locators plus item-12/17 checked subsets, leaving the above citations unaccounted for. This is a located prose defect, not a challenge to the frozen predicate.

### Q13 / Q14 and stale-copy audit

- Q13 line 311 explicitly names all three surviving classes: one-way deletion, superset output, and a different in-tree echo script printing fabricated lines. Scratch rechecks against the current gate reproduced each with exit 0 / `checked_blocks=24 problems=0`; for the forged case the baseline command was replaced by an in-tree `echo71.py` printing the embedded line. Gate mechanism `check_embedded_outputs.py:188-190` confirms stdout-set containment only. The entry labels them unguarded and credits no verifier, so no Q13 overclaim found.
- Q14 line 312 aligns with `corpus/QUALITY.md:26`: prose does not pair a quoted hex run with a byte count or ASCII rendering. Numeric hex values and `b"PK\\x05\\x06"` citations are not accompanied by such a byte-count/ASCII claim; counted signature bytes are command output at lines 37 and 223. PASS.
- The v6 prose has legitimate round-70 references at lines 9, 12, 311 and in the explicit historical comparison in its verified-at line; no obsolete r70 clause found. The stale Q13 citation `R70W2EntryMutants` is historical provenance for the mutation class, not presented as a current-round measurement; my fresh scratch probes reproduced it.

## Smallest safe correction

Do not change the claim or comparison predicate. In the Q16 support prose (Observation line 283 and map line 314), explicitly name additional cited source locations not compared by item 12/17—including `readout.py:51-58`, `:105`, `:155-168`, and `:203`—as locators/manual/inference-only, or narrow the corresponding citations/claims to the exact printed subsets. Re-score only under the frozen process; this seat made no edits and casts no reviewer vote.

## Commands and scratch

- Baseline and Q13 deletion/superset/forged mutations: `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` in `/fast/scratch/hyaku/revenger-r71/R71W2ProseCritic/tree` → each `checked_blocks=24 problems=0`.
- Output-shape probes: `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes`, `--zip-layout`, `--axml-layout`; results summarized above.
- Source evidence: `corpus/QUALITY.md:25-28`; gate `corpus/check_embedded_outputs.py:153-195`; W1 context `.ufo/waves/round-71/w1/R71W1Prose.md:8-15`, `.ufo/waves/round-71/w1/R71W1GateQ13Q16.md:22-45`.
- Scratch directory removed before return.

Report: `.ufo/waves/round-71/w2/R71W2ProseCritic.md`
