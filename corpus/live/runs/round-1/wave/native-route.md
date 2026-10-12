# Native route — checksum-r1, round 1

## Recommendation

Shortest supported *no-new-install* static route is `inspect_binary_layout` with the fixture's explicit ELF path. The native guide says this target-free route reports file-backed sections, symbols, relocations, linkage names, and static mitigation inferences without opening a disassembler target. It does not require Ghidra and avoids executing the target. However the standing brief says REA CLI is absent and MCP is not registered; so this route is a recommendation for a connected REA tool environment, not something runnable in this worker. Do not substitute running `npx` or installing engines here: scope prohibits package acquisition and no REA session.

## Artifact and known truth

- `file .shokunin/revenger/corpus/fixtures/checksum-r1/checksum` output: `ELF 64-bit LSB pie executable, x86-64 ... dynamically linked ... not stripped`.
- `sha256sum` output: `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`.
- Source `corpus/fixtures/checksum-r1/checksum.c` defines `rolling_checksum`: seed `0x13579bdfu`, rotate state left 5 bits, XOR each byte plus 17; `rotate_ascii` applies ROT13 to lowercase ASCII; `main` defaults input to `amber` and prints `r1:<transformed>:<8-hex-checksum>`. These are source-grounded expected facts, not REA findings. Binary provenance compiler/flags is not recorded in the inspected fixture files, so do not claim it.

## Readiness and actual route evidence

The remembered readiness table `corpus/knowledge/2026-10-12-rea-readiness-checklist.md` reports `which rea` ABSENT, REA MCP NOT registered, and Ghidra/IDA absent; node v26.11.1/npm 11.20.0 are present. Per REA skill “Connect only when needed,” this worker did not re-run diagnostics. The checklist's engine row says Ghidra absence blocks native pseudocode, while layout/inspection routes are unaffected.

Existing run `corpus/live/runs/20261012T163909Z/artifact-inspection.json` contains successful `inspect_artifact` Evidence `ev_dd509246a007f8e57b150678116da8895e0bea842093bb56aca525f1b886ab2c`, provider `rea-artifact-graph`, root format ELF and matching SHA-256; inventory substep Evidence `ev_ad931089830ba05c0b3d7b1b3b9021826963bd5e66bd5638cfd23c50489309a8` reports one-node artifact graph. This supports format/identity only, not code semantics.

Existing `native-analyze.json` reports `provider_unavailable` for operation `current_document` (auto provider candidates ghidra/hopper/ida): Ghidra `not_configured` (`GHIDRA_INSTALL_DIR` unset; analyzeHeadless/native decompiler unavailable), Hopper launcher missing `/opt/hopper/bin/Hopper`, IDA not configured. This is a concrete blocker for provider-backed native function decompilation. It does not establish layout tool unavailability; the artifact is an existing failed native-analysis attempt, not an `inspect_binary_layout` call.

## Route and boundaries

If/when REA is connected, use target-free `inspect_binary_layout` with the explicit absolute ELF path (prefer its summary output if the binary/response is large); preserve returned Evidence ID and record unsupported/unavailable facts. Compare symbols, imports/relocations and mitigation inferences against C source. If a specific native function's algorithm must be inspected, `open_binary` then focused function tools is the guide's next route, but it requires a configured deep provider here and therefore is not the shortest viable route now. No binary was executed and no provider/package setup or REA session was attempted.

### Limitations

No REA tool call was available in this worker, so no layout Evidence ID or scored REA-vs-truth findings can be reported. No claim about actual REA layout output. The current evidence establishes artifact identity and a failed provider-backed native-analysis attempt only. Fixture source is known, but compiler/flags remain unknown in inspected records.
