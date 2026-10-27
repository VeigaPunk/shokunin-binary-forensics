FAIL — Q16’s unguarded-locator enumeration omits `readout.py:203`.

Commands and observed output

- `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0`, exit 0.
- Re-ran the embedded commands for items 1–17, including `entry_checks.py --spec-quotes`, `--zip-layout`, and `--axml-layout`; the captured stdout matched each embedded block. `--spec-quotes` prints the six file/first-line/phrase-presence/phrase `MATCH` rows described in item 11. `--zip-layout` prints 20 stdout lines; lines 16–18 locate the three APPNOTE layouts and the last two compare central/local fixed-part widths as item 12 says. `--axml-layout` prints the listed offset-comparison rows; it does not compare the expression at `readout.py:203`.
- `python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest` → `readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`, exit 0.

Located defect

- `corpus/knowledge/round-71-apk-axml-byte-evidence.md:283-284` says that readout source citations are locators and that the literal subsets compared are only those printed by items 12 and 17; it then enumerates locators-only citations, but omits `readout.py:203`.
- `:284` explicitly cites `readout.py:203` in the inference that its literal `16` is the node header size. The actual source at `corpus/fixtures/apk-r65/readout.py:203` is `aoff = base + 16 + attribute_start + i * attribute_size`. Neither item 12 nor item 17's stdout compares that complete `aoff` expression (item 17 compares individual field-access literals and a manually derived node-width statement). Thus the inference’s cited expression is not covered by the listed comparison output, and the cited locator is not named as unguarded/locators-only. This violates Q16’s requirement that other set members be named unguarded. Q16 row `:314` repeats the locator list and also omits `:203`.

Residual scope checked

- Item 5 (`:64`) accurately says `lineNumber` at `readout.py:189` and `styleIndex` at `:197` are locators-only; those are absent from item 17’s comparisons. Item 11’s stdout-description and item 12’s line positions/width wording match actual stdout. Limitations’ command-output statements checked here are consistent with item 16 and the reproduced outputs.

Report: .ufo/waves/round-71/w2/R71W2Q16Scope.md