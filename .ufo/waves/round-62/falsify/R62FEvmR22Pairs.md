GRADE: PARTIAL — corpus/knowledge/round-62-evm-dispatch-byte-evidence.md (C09 candidate), r22 candidate-pair / instruction / offset / count slice + the observations-vs-unique-pairs wording

Frozen target: `d97761952be256d145d298022de03091de91d358` (tree `45c4c5da82aae8ca2e44f6e3ed874a33533f54b9`); claim base `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`.
Candidate blob `3e58a91fa8aee579aff7f873ce55061ae8f92cdf`; file sha256 `6a1d394ad92fcaa5344069d1225e428988f1397e80c8968745d7b48bf43fed6e` (working tree == archived tree).
Archive: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive --format=tar --prefix=tree/ -o frozen-d977619.tar d9776195…` → tar sha256 `02883a80818ff7c2546161f7d2a9cc59d95c90300a608a6e09b3ed4a700adfe0`; extracted to `/fast/scratch/hyaku/revenger-r62/R62FEvmR22Pairs/`. Python 3.14.8; TMPDIR=`…/R62FEvmR22Pairs/tmp`. No live corpus/fixture/record byte touched (`git status --porcelain corpus/` → empty).

## Observation — the r22 slice re-derived by my own decoder, not the entry's

`corpus/fixtures/evm-r22/fixture.raw` (34 B, sha256 `94c1790f…1dbe2`) =
`60003560e01c8063aaaaaaaa14601e578063bbbbbbbb14602057000000005b005b00`. Hand-written PUSH-N walk (no reuse of the entry's `walk()`):

```
(0,96,'00') (2,53,'') (3,96,'e0') (5,28,'') (6,128,'') (7,99,'aaaaaaaa') (12,20,'')
(13,96,'1e') (15,87,'') (16,128,'') (17,99,'bbbbbbbb') (22,20,'') (23,96,'20')
(25,87,'') (26,0,'') (27,0,'') (28,0,'') (29,0,'') (30,91,'') (31,0,'') (32,91,'') (33,0,'')
n_instructions 22
JUMPDEST on instruction boundaries: [30, 32]
raw 0x63 offsets: [7, 17]   raw 0x5b offsets: [30, 32]
JUMPI at 15 preceding PUSH1 operand 30 in jd set? True
JUMPI at 25 preceding PUSH1 operand 32 in jd set? True
counts {'0x0':6,'0x14':2,'0x1c':1,'0x35':1,'0x57':2,'0x5b':2,'0x60':4,'0x63':2,'0x80':2}
```

Entry's `## Provenance` stdout for r22 (md:444) parsed: `candidate_pairs_normalized [["0xaaaaaaaa",30],["0xbbbbbbbb",32]]`, `candidate_pairs_raw [["aaaaaaaa",30],["bbbbbbbb",32]]`, `valid_jumpdest_offsets [30,32]`, `raw_0x63_offsets [7,17]`, `raw_0x5b_offsets [30,32]`, `jumpi_with_preceding_push1 [[15,30,true],[25,32,true]]`, 22 instructions, the same opcode counts. **All r22 values match my independent decode.** `corpus/fixtures/evm-r22/truth.json` independently corroborates: `push4_opcode_offset` 7 and 17, `destination_offset` 30 and 32.

## Observation — the observations-vs-unique-pairs wording is CORRECT and the old mistake is gone

- Entry :47-50: "report **4 candidate observations** (`summary.reported_candidate_observations`: r19 one, r21 one, r22 two) over **3 distinct `(selector, bytecode_offset)` pairs** (`summary.distinct_candidate_pairs`, `summary.distinct_pairs`)". Both sets are named separately; no bare "pairs" number anywhere.
- md:449 summary: `reported_candidate_observations 4`, `distinct_candidate_pairs 3`, `distinct_pairs [["0xaaaaaaaa",30],["0xbbbbbbbb",32],["0xdeadbeef",16]]`. Set C is derived from the **tuple set** (`pairs.update((s,o) for s,o in norm)`, md:378), not from per-record lists — the rule the build seat `R62ReviewPairCounts.md:23,34` proposed.
- **No old mistaken "three candidate observations" wording survives.** The rejected round-61 candidate `corpus/knowledge/evm-saved-interface-candidates.md:87` still says "three reported pairs", but that file is byte-preserved rejected text, is not cited by the new entry (`grep` for `evm-saved-interface-candidates` in the new entry → no hit), and the new entry's number for record×pair is 4. The old defect does not carry into this candidate.
- Per-record raw vs normalized counts verified directly from the seven records: every `raw_result.functions` list length equals its `normalized_result.functions` length (r19 1/1, r21 1/1, r22 2/2, r23–r26 0/0), so `summary.raw_and_normalized_pair_counts_equal true` is a true statement about those lists, not a tautology of an empty default.

## Observation — every inventory row resolves; all 68 field references resolve

Machine audit of the 67 `## Evidence inventory` rows (md:216-282): each named field was fetched from a fresh run and compared to the printed value — **0 mismatches**. Every one of the 68 distinct `` `case.field` `` references in the entry resolves to a real printed field (only the literal placeholder `summary.field` in the path-convention sentence is unresolved, by design). The entry's own `## Reproduce` block, extracted verbatim as `readout.py` (sha256 `740f321e97e28d7f11b4a58e106f054447a284519c59487398752bc87cd37eeb`), re-run on the frozen archive exits 0 with empty stderr and stdout sha256 `aff3efda…235bf`, byte-identical to the `## Provenance` block; the 8 JSON lines in md:442-449 each `==` my run's line for that case. `git diff --name-only a3498e25… d9776195… -- corpus/fixtures corpus/live` → empty, so the recorded base and the frozen state read the same bytes.

## Finding 1 (material, Q11) — the r19 carrier `0x`-prefix claim is asserted, not derived

Entry :55-57: "r19's carrier is a 39-byte **`0x`-prefixed ASCII hex file** (`r19.carrier.bytes`, `r19.carrier.sha256`)". The two cited fields print only `bytes`, `file`, `sha256` — no field carries the `0x` prefix or the trailing byte; the file's actual bytes are `30 78 … 30 0a`. The readout decodes with a hard-coded `carrier[2:-1]` / `r19[2:-1]` (md:365-366, :368), a 2-byte header and 1-byte trailer never printed or asserted. QUALITY.md:23 Q11: "Constants such as header offsets are derived, not assumed."

My own counterexample on an archived copy (scratch `mut/`, repo untouched): r19 fixture rewritten `0x6000…005b00\n` → `zz6000…005b00!` (same length). `python3 -B readout.py mut` → exit 0, stderr 0 bytes; **r19 decoded hex, instructions, instruction_opcode_counts, valid_jumpdest_offsets, raw_0x63_offsets, raw_0x5b_offsets, jumpi_with_preceding_push1, pattern, recorded, record, candidate_pairs_* all UNCHANGED**; the other six case lines and the summary identical. Only `carrier.sha256` and the subject/artifact digest scopes changed (→ `no_local_byte_string`). Inference: the digest-scope change shows the carrier bytes changed; nothing in the printed output distinguishes a `0x` prefix from any other two-byte header. A correct value without its claimed in-entry derivation fails Q11; the value is also not labelled recorded (`recorded.artifact.encoding=hex` is a producer label, and it stayed `hex` under my mutation). Minimal correction: print `carrier[:2]` / `carrier[-1:]` (or the full carrier hex) in each case object and cite those fields at :56, or drop "`0x`-prefixed" from the prose and label the slice constants as recorded authoring premises. (Sibling seat `R62FEvmDigestLabels.md` reports the same clause as BROKEN/Q11; my counterexample is independent — different mutation, same conclusion.)

## Finding 2 (non-fatal, Q11 inventory completeness) — inventory rows under-name their own claim labels

- md:221 row "pattern bytes and length" cites `summary.pattern_hex` only; the length 9 asserted at :102 lives in `summary.pattern_length` (printed 9), uncited.
- md:239 row "r19 artifact bytes and encoding" gives 39 for `r19.recorded.artifact.bytes`; the encoding value `hex` is printed but uncited.
- md:241 cites one field (`r19.recorded.bytecode.kind`) for three fields across seven records, while :134-135 asserts `kind`, `deployment_authenticity` and `hardfork` are all `unknown`; all 21 values are printed and all are `unknown`.
- md:250-252 inventory r21 with three rows (carrier sha256, subject scope, candidate pairs) while :123-126 draws an inference over r19/r21/r22 citing only `r19.jumpi_with_preceding_push1` and `r22.jumpi_with_preceding_push1`; no `r21.jumpi_with_preceding_push1` / `r21.valid_jumpdest_offsets` row exists, and the r21 carrier-is-raw premise at :61-63 follows from the readout's `CASES` `enc="raw"` constant (md:305-306, :366) rather than from a printed field.
- :51 "(upstream)" glosses `raw_result`; that gloss holds only per the record's own `limitations[1]`, which is neither printed nor cited. Label it recorded or drop it.

## Inference

- The r22 slice **holds**: every r22 instruction offset, opcode count, JUMPDEST offset, raw 0x63/0x5b offset and candidate pair re-derives from the fixture bytes and the saved record exactly as printed, and the entry's 4-vs-3 observation/pair distinction is correct, set-named and tuple-derived — the old "three candidate observations" defect is absent.
- The file as a whole **does not hold**: Finding 1 is a real Q11 gap in the r19 carrier-format sentence. Since Q11 applies to every asserted value in the entry, C09 admission is blocked at this hash on that clause regardless of the r22 slice passing.

## Unknown

- Whether the provider's `bytecode_offset` means a JUMPDEST, a PUSH1 operand or a PUSH4 site is left open by the entry and stays open here (consistent only on these bytes).
- Why r23, r25 and r26 report no pair remains unassigned; I propose no rule and assert no cause.
- No verifier is credited as a guard by the entry and none was run by me; `corpus/verify_evm_evidence.py` covers r19 only and was not executed (no producer call, no fixture execution).
- S028 line anchors were re-opened read-only by me at tag v2.20.0 (`runtime.py` sha256 `a2801c41…aef8`, `instructions/__init__.py` sha256 `49dd6155…7eeb`, both matching the S028 row): every cited line is exact (instructions/__init__.py :55 EQ=0x14, :104 STOP=0x00, :106 JUMPI=0x57, :109 JUMPDEST=0x5B, :118 POP=0x50, :121 PUSH0=0x5F, :122 PUSH1=0x60, :125 PUSH4=0x63, :153 PUSH32=0x7F; runtime.py :22 def, :28, :29-30, :64 push_data_size).

## Residual risk / verification gaps

- Finding 2's rows are individually supported by the printed output; the defect is the entry's own self-claim at md:200 ("names the field and the value for each claim"), not a wrong value. It is Q11 wording, not a contradiction.
- Sibling seats cover adjacent slices (`R62FEvmAllCriteria` PARTIAL, `R62FEvmDigestLabels` BROKEN/Q11, `R62FEvmNoGuard` HOLDS, `R62FEvmPatternOrigin` HOLDS, `R62FEvmOpcodeSources` HOLDS, `R62FCriticInventoryMethod` BROKEN/inventory-method). I did not re-audit their scopes beyond what my r22/counts audit needed.

VERDICT: **PARTIAL** — the assigned r22 slice (both candidate pairs, all instruction/raw-0x63/raw-0x5b/JUMPDEST offsets, counts, and the observations-vs-unique-pairs wording) **holds** with primary evidence, and the old mistaken "three candidate observations" wording is **absent**; but the entry fails Q11 as a whole on the r19 `0x`-prefixed carrier claim (Finding 1, independently counterexample-tested), so I do not recommend C09 admission at this hash. Minimal correction is named for Finding 1 only; no repair made, no admission claimed.
Installs: none — `python3` 3.14.8, `git`, `curl`, `tar`, `sha256sum` were already present. Writes: this report only, plus scratch under `/fast/scratch/hyaku/revenger-r62/R62FEvmR22Pairs/` (archive, extracted tree, `mut/` counterexample copy, outputs). No repo, git index, history or fleet file mutated.
