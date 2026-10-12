# Gap audit — expected native-analysis gaps (round 1)

## Scope and evidence

- Inspected the declared fixture at `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum`; `file` output: `ELF 64-bit LSB pie executable, x86-64 ... not stripped` (BuildID `b58042814dad2078cdf09b9cf9f111ccab3a5a69`). SHA-256 observed by local hashing: `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`.
- Read readiness checklist and seed knowledge. Checklist records `which ghidra ida` ABSENT and explicitly says native pseudocode route blocked; layout/inspection routes unaffected. Seed says REA CLI/MCP are also not presently available until acquisition/connection.
- Shell probe during this audit: `which ghidra; which ida; which rea; which npx` returned no paths for the first three and `/home/vgpnk/.local/share/mise/installs/node/latest/bin/npx` for npx. This is corroboration, not a new REA analysis session.
- REA references: `SKILL.md` says native workflow is `open_binary` then focused tools; provider unavailability/unsupported metadata remain unknown rather than false. `references/native-and-artifacts.md` says offline `inspect_binary_layout` can report file-backed sections, symbols, relocations, linkage names and static mitigation inferences independently of a disassembler; addresses/pseudocode are analysis observations, not source.

## Bounded gap expectations (not findings about fixture contents)

1. **Pseudocode / function-level semantic recovery:** absent Ghidra/IDA means no provider-backed decompilation or native function dossier should be claimed. This is an unavailable route, not evidence that the binary has no functions, logic, checksum routine, or recoverable behavior.
2. **Control/data-flow and call relationships:** callers/callees, cross-references, unresolved calls, value-flow summaries and pseudocode are focused native-provider facets (native guide). Without the provider, these remain unknown; do not record empty results or “none found.”
3. **Rich disassembler database context:** function boundaries, disassembler-created names/comments, typed parameters and instruction-to-source interpretation may be unavailable or incomplete. Stripped-vs-not-stripped is not a proxy for any of those capabilities. The `file` result only establishes ELF identity and “not stripped.”
4. **Portable static inventory remains a possible partial route:** once REA CLI/MCP is actually made available, its advertised `inspect_binary_layout` route may establish sections/symbols/relocations/linkage/mitigation facts without Ghidra. Do not imply that this substitutes for pseudocode or semantic recovery. Checklist explicitly marks layout/inspection unaffected by Ghidra absence, while noting pwntools absent may separately block this route on this host.
5. **No REA evidence currently observed in this audit:** no REA session Evidence ID, provider response, or fixture scoring result was produced here. Thus no claim about what REA did or did not detect is warranted. This is a readiness/coverage limitation, not a negative analysis result.

## Reporting language

Use “unavailable on this host / route not run; behavior remains unknown” and identify the blocker (Ghidra/IDA absent, and REA CLI/MCP not yet available per readiness record). Do not say “REA found no functions,” “no checksum logic,” “no calls,” or “the binary lacks X” unless an available analysis actually ran and its bounded search supports that statement. If the route later runs, cite its Evidence ID and distinguish OBSERVATION, INFERENCE, UNKNOWN; report coverage boundaries and any unsupported facets. Do not treat absence of pseudocode as proof the binary is opaque or empty.

## Limitations

This audit did not execute the fixture, install/setup anything, invoke REA, inspect instruction bytes, or inspect source truth. The reported gap list is expected route coverage based on the skill/readiness docs, not scored miss evidence. It does not establish that any particular capability would be exposed by a future provider/version.
