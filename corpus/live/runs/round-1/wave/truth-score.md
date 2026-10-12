# Round 1 truth-score criteria — checksum fixture

## Source truth and scoring unit

The independent oracle is the authored C source, not ELF metadata. Source lines below define the behaviors (truth atoms); score only explicit semantic claims in REA findings. Count one claim per atom per finding set, deduplicating paraphrases. A claim is correct only when it matches the atom's full scope and qualifiers. A partially true but materially overbroad claim is incorrect (false positive), not a fractional hit. Evidence about file format, symbols, sections, architecture, or compiler properties is artifact metadata, not behavioral recovery and earns no behavioral true positive.

Truth atoms (all supported by `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum.c`):

| ID | Ground-truth behavior | Source |
|---|---|---|
| T1 | If at least one argument is supplied, use `argv[1]`; otherwise use literal `amber`. | 23–24 |
| T2 | Transform input byte-wise until NUL or 127 bytes; write a NUL terminator at the stopping index. | 14–20 |
| T3 | Only lowercase ASCII `a`–`z` is rotated by 13 positions modulo 26; every other byte is copied unchanged. | 17–19 |
| T4 | Checksum starts at unsigned 32-bit `0x13579bdf`; for each byte, rotate state left 5 (equivalently combine left shift 5/right shift 27 in uint32) then XOR byte plus 17. | 5–11 |
| T5 | Checksum covers the transformed string up to `strlen` (excluding its terminating NUL). | 27–28 |
| T6 | Output format is `r1:<transformed>:<8 lowercase hex digits>
`; process returns 0. | 27–29 |

## Precision / recall protocol

Use only behavior claims in the REA session's retained/exported Evidence. Map each to T1–T6, classify `supported`, `contradicted`, or `not addressed`, and retain the exact Evidence ID and claim excerpt. A stated unknown/limitation is not a claim and is not an error. Metadata and structural observations should be reported separately, never included in either behavioral numerator or denominator.

- **Behavioral precision** = supported explicit behavioral claims / all explicit behavioral claims. A contradicted or materially overgeneralized claim is a false positive. If there are no explicit behavioral claims, precision is N/A (not 100%).
- **Behavioral recall** = truth atoms supported by at least one explicit, correct behavioral claim / 6. A general hint such as “contains strings” does not cover an atom. Claims inferred solely from ELF metadata do not cover atoms.
- Report both fractions and counts; do not collapse them to a single score. Give each atom at most one recall credit even if repeated. Keep evidence completeness separate: no Evidence ID means a hypothesis, excluded from scored findings.
- For partial source matches, either split into independently falsifiable subclaims before scoring all findings, or mark the atom not covered and describe the omission; do not quietly grant partial credit. For wrong behavior, record the counterclaim as a precision error and leave the relevant truth atom uncovered.
- Static-analysis evidence can support a behavioral inference, but must remain labeled inference, not observed execution. Source is the oracle; this assessment does not establish that the compiled artifact is byte-for-byte behaviorally identical to source under every platform/compiler condition.

## Current evidence / present scoring status

`corpus/live/runs/20261012T163909Z/artifact-inspection.json` records top-level Evidence ID `ev_dd509246a007f8e57b150678116da8895e0bea842093bb56aca525f1b886ab2c`; its nested inventory Evidence ID is `ev_ad931089830ba05c0b3d7b1b3b9021826963bd5e66bd5638cfd23c50489309a8`. The top-level result identifies an ELF of SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`, inventory says one materialized executable node and no child entries. It retains an unexplored branch: format-specific analysis requires `open_binary`. These are artifact observations only; they support none of T1–T6.

`corpus/live/runs/20261012T163909Z/native-analyze.json` is an error record, not an Evidence ID/finding: `provider_unavailable`, auto candidates Ghidra/Hopper/IDA rejected. Ghidra is not configured, Hopper launcher missing, and IDA MCP not configured. Therefore current behavior-finding set is empty: precision N/A; recall 0/6 for this recorded inspection (coverage not achieved), not evidence that REA is incapable of recovering behavior. Do not count the failed native operation as six missed findings unless the round's scoring denominator explicitly treats each source atom as a probe opportunity; under this fixed rubric it is a coverage gap, reported separately.

## Bounded limitations and source commands

Source line inventory was obtained by reading `checksum.c` with Python `enumerate(read_text().splitlines(), 1)`. The readiness checklist records `which rea` ABSENT and the expected native engines absent; this wave did not run the target, invoke REA, install anything, or independently verify compiler/build provenance. The artifact inventory's own limitation says it does not claim format-specific semantics or execute the artifact. Consequently this rubric defines the oracle and scoring method; it does not claim successful behavioral analysis. No disassembly/pseudocode Evidence IDs were present in the reviewed JSON outputs.
