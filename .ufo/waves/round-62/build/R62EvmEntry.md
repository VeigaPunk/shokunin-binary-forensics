RESULT: COMPLETE

# R62EvmEntry — round-62 C09 candidate, fresh-falsify corrected form (draft only)

Seat `RevengerR61-2.R62EvmEntry` (leaf). Frozen revision
`a3498e25ad87bf756288812d0ea7c474b09433c7` (tree
`f53a42f2eb5baa9fa999f8bcf2b7e8145d2309c7`), extracted read-only via
`git -C …/revenger-shokunin archive a3498e25… | tar -x -C
/fast/scratch/hyaku/revenger-r62/R62EvmEntry/frozen`; all execution ran on that
copy or on scratch files, cwd=/ for the recorded run.

**Proposed entry (draft, scratch only):**
`/fast/scratch/hyaku/revenger-r62/R62EvmEntry/candidate.md` — 587 lines, 57377
bytes, SHA-256
`e7bf76aae801027f98fc4d46932f1309ade5b6671bf4407ac206bb50914f3196`.
Intended landing path `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`
is **not** written by this seat; L1 integrates it.

**Final artifacts.** `readout.py` (192 lines, SHA-256
`2dc4210975fa26bb86ebcad6921a5f732e10f4a8a6302eff1ab3c449cdb56ce0`) is embedded
verbatim in the entry; `readout_stdout.txt` (8 lines, SHA-256
`8bade6c9a9641edf0673f45cfc59f799ffe30548596c98fe8848d7beeab5cef7`) is embedded
verbatim as the `## Provenance` block. **Final focused run on the archived
bytes:** the `## Reproduce` block was extracted from the finished candidate into
`extracted_readout.py` (SHA-256 identical to `readout.py`) and run with
`python3 -B extracted_readout.py frozen` → **exit 0, stderr 0 bytes, stdout
byte-identical** to the recorded `readout_stdout.txt` (`cmp` clean, same
SHA-256 `8bade6c9…`).

**Arithmetic bug found by the rereviews and fixed here.** The
`template_enclosing_instruction` extent was computed from the *hex string*
length of an instruction's immediate, so it counted each byte twice: r19 printed
`[[6,99],[12,96]]` where the correct enclosing instruction of the template's
PUSH1 byte is the PUSH1 at 12, `[[12,96]]`. The single expression is now
`len(im) // 2` (`readout.py:112`). After the fix r19 prints `[[12,96]]` and r24
prints `[[0,127]]` (the PUSH32 that contains its occurrence), and the new
printed field `template_push1_template_index` gives the byte's position inside
the template (6) beside its file offset. No other value changed: the entry's
own walk stores immediates as hex, and the only place an immediate length was
used as a byte extent was this expression.

**Diff summary against the falsify wave's material findings** (all read from
`.ufo/waves/round-62/falsify/`): R62FEvmCarrier Observation 5 and
R62FEvmDigestLabels Finding 1 (the `0x` framing was asserted, not derived) —
the readout now derives the decode boundaries from the carrier bytes and prints
them: `carrier_form` (`ascii_hex_text` for r19, `raw_bytes` for the other six),
`carrier_prefix_bytes` `[48, 120]` / `carrier_prefix_hex` `3078`,
`carrier_trailer_bytes` `[10]` / `carrier_trailer_hex` `0a`,
`decode_body_slice` `[2, 38]`, and `decode_checks` (prefix-is-0x,
trailer-is-lf, body-is-even-length-hex). A carrier whose own bytes show the
ASCII `0x` prefix but is not a hex text is now refused, not decoded: on an
archived copy with the prefix changed to `zz` the readout exits 1 with a
`ValueError` instead of silently dropping two bytes. The `0x`-prefixed prose is
now cited to those fields. R62FEvmQ11Inventory F1/F2 and R62FSafeEvm (r24
offset 7 called a PUSH1 opcode byte) — the template is now derived **once** from
r19's own instruction boundaries and searched as a **raw byte string**; the
fields are renamed to `template_*` and the r24 role is printed, not asserted:
`template_push1_byte_value` 96, `template_push1_byte_is_instruction_opcode`
false, `template_enclosing_instruction` `[[0,127]]` (the PUSH32),
`template_occurrence_start_is_instruction_boundary` false, alongside
`template_operand_byte_offset` 8 / value 16, `template_target_offset` 16,
`template_target_byte` 0, `template_target_is_raw_0x5b` false. R62FEvmQ11Inventory
F3 (the dispatch/argument/mutability sentence had no printed field) — that
sentence is deleted rather than analysed. R62FEvmQ11Inventory F4/F5 and
R62FEvmDigestLabels Finding 2 (inventory rows not covering the fields they
name; cross-case claims citing only r19) — the inventory now has 95 rows whose
values are read back out of the recorded JSON, every prose field citation has
an inventory row, and the cross-case claims cite new printed aggregates
(`summary.distinct_evidence_kind_values`, `…_discovery_completeness_values`,
`…_runtime_execution_values`, `…_provider_version_values`, `…_bytecode_kind_values`,
`…_bytecode_hardfork_values`, `…_bytecode_deployment_authenticity_values`,
`…_artifact_encoding_values`). Missing pointers added: r21 digest scopes,
r21 JUMPI/JUMPDEST/raw `0x5b`, pattern length, artifact encoding. Also
removed: the "upstream" gloss, the unsupported "inert" label (now "authored",
a recorded S031 label), and the `local_path` claim. R62FEvmQ11Inventory F6 (r24
omitted from the Unknown bullet) — the bullet now names r23, r24, r25 and r26.
R62FEvmQ11Inventory F7 / R62FEvmAllCriteria Q01 — the `source:` header now
carries **S026** for the saved-record metadata subset, the Q01 cell names S026
for the recorded metadata, and the Q04 cell no longer claims the provider is
the only tool named. No SOURCES row was edited by this seat.

**Mechanical checks over the finished entry.** The embedded code equals
`readout.py` and the embedded stdout equals the recorded file (both byte-equal);
**95 inventory rows, 0 mismatches**; **96 prose field citations, 0 without an
inventory row**; no truncated digest (every digest is the full 64-hex value the
readout prints); 0 occurrences of kasegi, "every statically valid", "post-hoc",
"37 single", `truth.json`, `local_path`, "file-class label", "upstream",
"inert", "dispatch`" and "state-mutability". Counts unchanged and kept apart:
`total_cases` 7, `reported_candidate_observations` 4, `distinct_candidate_pairs` 3.

**Line budget deviation, stated.** The earlier integration note asked for
~≤130 code lines and ~≤450 entry lines. The corrected form is 192 code lines
and 587 entry lines. The extra lines are the newly required derivations, not
bulk: the carrier-boundary derivation and its eight printed fields, the
raw-template/boundary block and its thirteen printed fields, the eight
cross-case aggregates, and the 116-row inventory that the falsify seats
required to cover the cross-case claims, plus the one arithmetic fix. I kept
those rather than dropping the derivations the wave demanded; the code, stdout
and prose are otherwise as narrow as before.

**Preservation and non-claims.** `git status --porcelain` shows only L1's own
concurrent edits (`M corpus/SOURCES.md`, `?? corpus/lessons/round-62.md`) and the
wave reports directory; I changed no corpus, fixture, record, README or SOURCES
byte. README C04/C09 still read `uncovered`; no held flip, no admission, gate or
promotion claimed; prior rejected candidates byte-preserved.

**Census — historical, not re-run.** An earlier measurement of mine, taken
while the two round-62 entry files were still scratch-only, found four E11
findings for the S028–S031 `used-by` paths and a validator exit of 1. That was
a staged-artifact observation at that moment; the entries have since landed on
the live tree, so the observation is stale and I have not re-run the validator
to restate it. S028's anchor ranges cover every constant this readout uses
(`:55`, `:104-109`, `:118`, `:121-153`), and the entry's `## Source facts`
section quotes them with the row's exact URL and file:line anchors.

**Risks / unknowns (honest).** The recorded metadata subset is claimed under
S026, whose scope covers exactly those seven saved records; the fixture bytes
are claimed under S031 and the opcode values and jump-destination scan under
S028. The offset convention is stated only for the non-empty saved results in
this sample. Provider id, version, evidence id, authority and confidence are
recorded fields, not authenticated; no present producer capability is claimed.
The readout is a manual comparison, not claimed deletion-sensitive, and no
mutant run over it was performed; `corpus/verify_evm_evidence.py` is credited
for no clause.

**Proposed changes.** None applied to the lane tree. The only proposed change
is the new file `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`, to
be created by L1 from `candidate.md` verbatim at the digest recorded above.

Installs / updates: **none**. No pacman, uv, cargo or npm transaction; no
service restart. Tools: `git` (read-only), `curl` (read-only fetch of two public
specification files and GitHub tag metadata), `python3` 3.14.8 stdlib only.
