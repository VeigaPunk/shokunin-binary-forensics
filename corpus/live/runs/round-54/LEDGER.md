# Round 54 — Unicode named icon group, declared size mismatch

## Fixture and route
- Base: `corpus/fixtures/pe-r52/fixture.exe` SHA-256 `9297adec215ef401538dad04f06e249a41d3747e14b996a837164a2dde3d070d`. Derived `corpus/fixtures/pe-r54/fixture.exe` SHA-256 `3c5a50e5cf3e4242b228a228e4ac0e58d413b3851538210e280d7bd50b9e64b7`, 1024 bytes. Byte comparison finds only offset 846 changed `0x30`→`0x2f` (48→47 in group image declared size); `corpus/fixtures/pe-r54/truth.json` documents construction. No execution.
- Route: static `inspect-pe-resources` through `npx -y rea-agents@6.4.0`, command/exit0/stdout hash in `producer-receipt.json`, complete response in `inspection.raw.json`. Evidence `ev_f015502b774219fa3491150c7c2ac1c592c0c099227642d43b4962e555920d24`; reported subject SHA matches actual fixture.

## Source-scored statements
- OBSERVATION (fixture bytes and saved Evidence `ev_f015502b774219fa3491150c7c2ac1c592c0c099227642d43b4962e555920d24`): PE32+ resource leaves are RT_ICON ID1 / language1033 / 48-byte payload at 768 and RT_GROUP_ICON named `A😀B!` (UTF-16LE `41003dd800de42002100` at 736) / language1033 / 20-byte payload at 832. REA reports two resources (2/2 identity against constructed fixture, zero extra reported).
- OBSERVATION (fixture bytes and saved Evidence `ev_f015502b774219fa3491150c7c2ac1c592c0c099227642d43b4962e555920d24`): sole group image's resource ID remains 1; reported candidates `[0]`, same-language index `0`, and size_matches `false` for declared 47 vs actual 48. Group image relationship precision 1/1, recall 1/1; size flag 1/1 on this fixture. Baseline r52 Evidence `ev_b9b5ec033d76da151ad5ce0c052e821130fe4aec6613fc6c2fbdcc48dec03c66` reports true with 48 declared.
- INFERENCE: REA's static table matching retains a candidate when declaration size differs; this does not imply an OS would load the resource.
- OBSERVATION (independent non-author reviews `byte-oracle.md` and `result-review.md`): both derived r54 truth from PE bytes and compared saved Evidence; initial offset errors were corrected before acceptance. `result-review.md` checks the receipt SHA-256 against saved stdout bytes.
- UNKNOWN: rendering, decoding, OS resource language fallback, arbitrary PE handling, native disassembler readiness, and producer-origin authentication of a saved CLI receipt.
