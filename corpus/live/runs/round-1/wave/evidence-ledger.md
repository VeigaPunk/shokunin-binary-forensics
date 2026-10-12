# Round 1 evidence-ledger schema and evidence inventory

## Ledger schema (one row per claim)

| field | required content |
|---|---|
| Claim / comparison | Atomic statement, question tested, and (for source comparison) exact source construct and corresponding REA claim. |
| Classification | `OBSERVATION` (directly encoded in cited record/source), `INFERENCE` (reasoned interpretation), or `UNKNOWN` (not established); do not promote inference to observation. |
| Evidence ID(s) | Exact `ev_…` IDs for REA-derived claims. Cite source file plus line range for source truth; non-REA provenance records are explicitly labeled local/source evidence, not REA Evidence IDs. |
| REA result | Finding verbatim or compact normalized-result fact; operation/provider, subject SHA-256, coverage and limitations. |
| Ground truth / comparison | Source fact; status `match`, `partial`, `miss`, `contradiction`, or `not comparable`; explain the comparison boundary. A missing finding is a miss only within an inspected/covered question, otherwise unknown. |
| Confidence / residual | Confidence justified by evidence type; unresolved question, needed authority/route, and bounded search scope. |

Rule: a claim without a stable Evidence ID is a hypothesis, not an REA finding (seed.md, “Verification discipline”; REA SKILL.md, “Work summary-first”). Preserve limitations and incomplete coverage; do not claim static inspection observed execution. Compatible complete page sets are needed for equivalence/absence claims (references/evidence-workflows.md, “Use comparisons with complete, compatible page sets”).

## Available round evidence (read-only inventory)

| ID / source | OBSERVATION | INFERENCE / comparison status | UNKNOWN / limitation |
|---|---|---|---|
| `ev_dd509246a007f8e57b150678116da8895e0bea842093bb56aca525f1b886ab2c` (`corpus/live/runs/20261012T163909Z/artifact-inspection.json`) | `inspect_artifact`; provider `rea-artifact-graph` v1. Subject `checksum`, SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`; format ELF. | Evidence establishes the artifact identity/format only. It does not report checksum semantics or source correspondence. | Record says bounded static hypotheses only; no format-specific semantics. One child inventory substep, one retained observation; unexplored branch calls for `open_binary`. |
| `ev_ad931089830ba05c0b3d7b1b3b9021826963bd5e66bd5638cfd23c50489309a8` (nested inventory evidence in same JSON) | Inventory: one materialized ELF, 16,160 bytes; same SHA-256; no child entries. `coverage.status=complete-within-substeps`. | No child-container finding is not a finding about program behavior. | Inventory-only; `open_binary` not run, format-specific branch unexplored. |
| `native-analyze.json` (no Evidence ID) | Output is an error record: `provider_unavailable`; requested provider `auto`; candidates Ghidra/Hopper/IDA rejected (Ghidra not configured; Hopper executable missing; IDA not configured). | This failed attempt is not analysis evidence and cannot be scored as an REA finding. It documents blocked deep native route. | No native function/decompiler evidence was produced. Do not fabricate/cite an Evidence ID for this error. |
| `checksum.c:6-13,16-23,26-34` (source truth, not REA evidence) | Source defines 32-bit rolling state initialized `0x13579bdf`, rotate-left by 5 then XOR byte+17; ASCII lowercase ROT13 limited to 127 characters; default input `amber`; output format `r1:%s:%08x`. | These are source-derived expectations for later scoring; they are not verified behavior of the compiled artifact by execution or REA. | Build provenance/compiler/flags and source-to-binary correspondence are not established by this ledger. No target execution performed. |

## Comparison protocol for later findings

1. Bind each candidate finding to its Evidence ID and exact REA operation/coverage. Keep parent and substep IDs distinct.
2. Match to a precise source statement/range; score only semantically comparable findings. Mark partial matches narrowly (e.g. transform identified, length bound omitted).
3. Mark a covered source fact absent from relevant complete evidence as `miss`; if the route/record is incomplete or never examined that facet, use `UNKNOWN`, not a miss. Mark incompatible or contradicted semantics `contradiction` and cite both sides.
4. Report counts only with denominator: comparable source facts in the declared analysis scope. Do not infer global precision/recall from inventory-only evidence. Retain provider failure as route-coverage limitation, not a negative result.

## Limits of this worker report

No session/tool calls, binary execution, setup, or installs were performed. The available artifact-inspection records and source were read locally. This report defines a ledger and inventories evidence; it does not claim the round’s required REA session or scored comparison is complete.
