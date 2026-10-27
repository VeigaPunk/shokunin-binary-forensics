PASS — final-tip reproduction matched the frozen outputs; item 15 count/digest and all eight checker flags pass.

Seat: R71W2Reproduce · final committed tip `c6e284c6583fa3502754361f411b66646880ba02` (candidate `4c1eeaee88fd07e442f1bd546faf77be3957d390` plus wave-freeze additions). Replayed from a `git archive HEAD` scratch tree; the v6 entry blob and `corpus/fixtures/apk-r65` tree are identical at candidate and final tip. No source changes made.

Commands and outputs:
- Reproduce command `python3 -B corpus/fixtures/apk-r65/readout.py`: exit 0, stdout 15 lines, stderr 0 lines.
- Item 15 `python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest`: exit 0; exact stdout `readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`. Independently hashing the captured bare readout stdout gives the same SHA-256.
- Eight `entry_checks.py` flags, each run separately: `--pins`, `--eocd`, `--oracle`, `--zip-layout`, `--axml-layout`, `--container`, `--spec-quotes`, `--stdout-digest`; all exited 0. Key exact outputs: `--eocd`: `eocd signature bytes at offset 925: 504b0506 (4 bytes)`; `--spec-quotes`: six `MATCH` lines (including `dex-format.html: first line 5035` and `ResourceTypes.h: first line 686`); `--stdout-digest`: as above.
- All 24 `$`-prefixed embedded commands in the entry were executed against the archived final tip; all exited 0. `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` reports `checked_blocks=24 problems=0`, exit 0.
- Re-derived counts from command stdout, excluding `$` command lines: item 11 `--spec-quotes` = 6 stdout lines; item 12 `--zip-layout` = 20 (three fixed-part lines + 12 offset matches + three APPNOTE locator lines + two width comparisons; the latter two are stdout lines 19–20, while lines 16–18 are the APPNOTE layout locators); item 13 `--oracle` = 34; item 14 `--pins` = 10; item 15 `--stdout-digest` = 1; item 16 `--container` = 3; item 17 `--axml-layout` = 24. Thus the line-count references describe stdout, not the `$` command line.
- C2 missing-entry direct CLI probe: exit 2; stdout `could-not-evaluate: entry not found: corpus/knowledge/definitely-missing-r71.md`; stderr 0 bytes.
- C2 production-timeout direct CLI probe: exit 2 after 120.04 s; stdout `could-not-evaluate: command timed out after 120s: python3 -B corpus/sleeper_r71.py`; stderr 0 bytes.

Residual risk / verification gaps: none found in the reproduction scope. These checks do not make a Q decision or modify the frozen C1/C2 predicates.

Report: `.ufo/waves/round-71/w2/R71W2Reproduce.md`
