# Round 35 independent PE resource review

**Verdict: PASS — precision 3/3, recall 3/3** against the three resource leaves independently decoded from `pe-r35/fixture.exe`. This is a static byte-level comparison, not a fresh REA run. No extra leaf or omitted reachable leaf appears in the saved `inspection.json` normalized result.

## Reproduce

From the repository root, run:

```sh
python .shokunin/revenger/corpus/live/runs/round-35/reviewer-verify.py
```

The standalone verifier uses only Python's standard library. It independently checks DOS/PE and COFF/optional headers, PE32 data directory, `.rsrc` section RVA-to-file mapping, every reachable type/name/language directory edge, UTF-16LE name length/bytes, data entries, payload ranges and SHA-256. It compares **all** non-prose `normalized_result` fields with those derived from the executable, including artifact path/size/hash, format/machine, directory RVA/ranges, all directory metadata and ranges, ordered resource indexes, identities, entry/data-entry offsets, payload RVAs/offsets/sizes/hashes, `icon_groups` and complete coverage counts. It fails on any mismatch or unexpected field (other than the declared prose `limitations`). The source of expected values is the raw executable, not either `truth.json`.

## Independently decoded facts

- Artifact 1024 bytes, SHA-256 `372cca0e0e1a3510ff4ccf862b2351e6970bb559feb5fb6a30416d34331930f8`; PE32 x86 (`machine=332`). Resource directory RVA 8192 maps to file offset 512, 400 bytes; PE data-directory entry at offset 200, 8 bytes.
- Four reachable directories: offsets/sizes 512/24 (0 named, 1 ID), 536/32 (1 named, 1 ID), 768/32 (0 named, 2 IDs), 592/24 (0 named, 1 ID); all characteristics, timestamps and versions are zero. Six traversed edges, three leaves; none is RT_GROUP_ICON, hence no icon group.
- `10 / A😀B! / 1036`: name bytes `41003dd800de42002100` at 736/12, entry offsets 528, 552, 784 (8 bytes each), data entry 616/16, payload RVA 8352 -> 672/15, SHA-256 `071db9bf3f85c6f8a41884653e2f08a2346af9ce522e2574851e286e5c192229`.
- `10 / A😀B! / 1041`: same name and first two entries, language entry 792/8, data entry 864/16, payload RVA 8576 -> 896/15, SHA-256 `cba2d0e3f4bb58475ef4f760dbc917210e84f90c73a27a8026eba7ef7229821e`.
- `10 / ID 3 / 1033`: entries 528, 560, 608 (8 bytes each), data entry 632/16, payload RVA 8384 -> 704/15, SHA-256 `cc29ca16da56975bf9fb034fbc010e377076ada5df6395622c8ffd9fed19f67e`.
- Code page and reserved fields are zero for all three leaves. Saved result indices/order and every location match traversal order. Coverage `complete`, `examined_entries=6`, `resources=3` agrees with the whole reachable resource tree.

## Baseline and provenance limits

Raw `pe-r34` independently decodes as two leaves (`10 / A😀B! / 1036`, `10 / ID 3 / 1033`), five edges, four directories, directory size 240 at RVA 8192/file offset 512; SHA-256 `28182338af9da23b7dc0d6c1b64b325bb635a25f8b336c1d278884ffa88f2e85`. `pe-r35` retains both leaves and adds the distinct `1041` leaf, one edge, and expands the resource directory to 400 bytes; its name-directory branch points to a new language directory at 768. No saved round-34 inspection is in this review scope, so no claim about earlier REA output is made.

The declared limitations are consistent with static evidence: inventory only; non-icon payload semantics, Windows language fallback, decoded display, and runtime shell/window loading remain unobserved. This check cannot establish runtime behavior or parser behavior on other files.

`producer-receipt.json` reports `npx -y rea-agents@6.4.0 inspect-pe-resources ... --format json`, exit 0 and output SHA-256 `8c8d96db863e0f32b816d526fca3d1df04fb60e0ece5f166781dfc6ccd8988e2`. The saved `inspection.json` bytes hash to `74a45d0c7e25027090a0dfbad27f132dea14cf6b1b8cb447317f8174a7d02e4a`, **not** that receipt hash: the raw command output was not preserved byte-for-byte here. A serialized/reformatted result can still be independently checked for correctness, but the receipt does not cryptographically authenticate this saved JSON. The producer's stderr was combined, and this review does not independently verify the run/exit or package version. `attempt-invalid.json` records `invalid_request` for mismatched name/ID counts, but lacks the attempted input, command and raw stdout/stderr; it is not independently reproducible evidence of negative-case parser behavior. Fixture `truth.json` files describe construction but were not used as the oracle.
