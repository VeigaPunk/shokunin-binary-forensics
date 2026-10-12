# Round 1 REA native fixture attempt — 20261012T163909Z

## Route and scope

Target: `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/checksum-r1/checksum`; SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`. Local C fixture and build recipe: `../../../fixtures/checksum-r1/README.md`. Static REA calls only. No fixture execution, unrelated installation, MCP registration, or target runtime action.

Commands (from repository root):

1. `npx -y rea-agents@6.4.0 analyze /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/checksum-r1/checksum --format json` → exit 1; full response `native-analyze.json`, stderr `native-analyze.stderr`.
2. `npx -y rea-agents@6.4.0 inspect-artifact /home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/checksum-r1/checksum --format json` → exit 0; full response `artifact-inspection.json`, stderr `artifact-inspection.stderr`.

The CLI manages an ephemeral target per invocation; command 1 attempted native open but **did not establish an active native provider session**. The provider refusal is a failure result, not Evidence ID-backed native analysis. Command 2 is provider-neutral artifact inspection, **not** a substitute for an opened native session.

## Evidence ledger: OBSERVATION / INFERENCE / UNKNOWN

| class | finding | REA Evidence ID | truth check / boundary |
|---|---|---|---|
| OBSERVATION | Root artifact format ELF; SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`; 16160 bytes | `ev_ad931089830ba05c0b3d7b1b3b9021826963bd5e66bd5638cfd23c50489309a8` (nested under `ev_dd509246a007f8e57b150678116da8895e0bea842093bb56aca525f1b886ab2c`) | `sha256sum`, `file`, binary size agree; three atomized metadata findings match |
| OBSERVATION | One root node/occurrence, zero child edges | `ev_ad931089830ba05c0b3d7b1b3b9021826963bd5e66bd5638cfd23c50489309a8` | Correct for the single standalone ELF file; it does not establish no dynamically linked dependencies or embedded payloads |
| INFERENCE | A native analysis provider would be needed for function-level behavior | `ev_ad931089830ba05c0b3d7b1b3b9021826963bd5e66bd5638cfd23c50489309a8` (`unexplored_branches[0]`) | Next probe, not an observed function or code path |
| UNKNOWN | Function boundaries, checksum algorithm, ROT13 behavior, default string and printed output as REA-derived findings | no native Evidence ID: `native-analyze.json` reports `provider_unavailable` | Known from source only; REA did not recover them |

## Scored comparison (declared denominator)

- **Artifact-level precision:** 4/4 checked observation groups match independently established truth: ELF format, binary SHA-256, byte size, and standalone root with no archive children. No false REA artifact claim was scored. This is *not* precision of reverse-engineered behavior.
- **Behavioral recall:** 0/6 source-truth atoms supported by REA findings, using the independently defined rubric in `../round-1/wave/truth-score.md`: argument/default selection, NUL/127 bound, lowercase-only ROT13, checksum seed and step, checksum over transformed bytes, and output/return. No behavior finding was proposed. Behavioral precision is **N/A (zero proposed behavior findings)**, not 0% or 100%. Metadata cannot earn behavioral recall.
- **Gap / wrong list:** All six behavioral truth atoms remain unexamined by native REA analysis due to no native provider (a coverage gap, not six failed findings from a completed analysis). No wrong REA behavior inference was made. `analyze` returned `provider_unavailable` with Ghidra `not_configured` (requires `GHIDRA_INSTALL_DIR`), Hopper `executable_missing`, IDA `not_configured`; see `native-analyze.json`. The root-inspection branch explicitly calls for `open_binary`, not proof of a native open.

## Round-1 claim status

**Unmet.** Acquisition and artifact inspection worked, but the claimed native REA session and function-level score did not. Coverage is not claimed improved on the specified axis move. Only provider-neutral identity coverage was established; do not upgrade that to native readiness. Next attempt requires a caller-supplied supported native provider, or a new separately declared route/axis claim, without silently installing Ghidra/IDA/Hopper.
