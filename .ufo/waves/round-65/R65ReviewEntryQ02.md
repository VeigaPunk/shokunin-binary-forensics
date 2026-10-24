FAIL — header's S039 line anchor and S038 enum range do not resolve to the named text, and one transcribed output line (MANIFEST.MF `payload_first16_hex`) differs from the frozen recheck command's actual output; every other Q02 sub-item passes and all snapshot digests match.

Seat: R65ReviewEntryQ02 (fresh-seat Q02 on the round-65 C05 candidate entry). Read-only; no production edits. Tooling: no installs performed (none needed). `lsp` is not in this seat's toolset and the target is Markdown, so all checks below are byte/line checks against the named artifacts, not semantic LSP queries.

# Target

- Entry: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md` (162 lines; header lines 1–7, §Q-map Q02 row at line 142, §Reproduce at 154–162)
- Contract: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md` (read in full first; C1 only concerns this entry)
- Snapshots: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-65/source-snapshots/{ResourceTypes.h,rea-android-applications.md,zipfile-docs.html}`

# Sub-item verdicts

| # | Q02 sub-item | Verdict | Evidence |
|---|---|---|---|
| 1 | `source:` rows with URLs/paths | PASS | Entry:1 S038 URL `…/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h` + pinned tag; entry:2 S039 repo path `skills/reverse-engineer-anything/references/android-applications.md` at tag `rea-agents-6.5.0`; entry:3 S041 four fixture paths. Registry rows exist and are dated `2026-10-24 \| on-release`: `corpus/SOURCES.md:52,53,55`. |
| 2 | Snapshot digests | PASS | Recomputed equals header claim for every digest: `sha256sum` of `ResourceTypes.h` = `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` (86255 bytes); `rea-android-applications.md` = `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` (34 lines, `grep -c ''` = 34); S041 fixture `05d2280f…d03e` (947 bytes), truth.json `27303bae…8173`, generator.py `eaa9444c…7c1a`, readout.py `92e347c3…3976`. |
| 3 | Exact anchors (struct names + line numbers) exist in snapshot bytes | **FAIL (partial)** | 7/7 struct anchors are exact in `ResourceTypes.h` at the cited lines: 218 `struct ResChunk_header`, 287 `struct Res_value`, 461 `struct ResStringPool_header`, 612 `struct ResXMLTree_header`, 621 `struct ResXMLTree_node`, 677 `struct ResXMLTree_attrExt`, 707 `struct ResXMLTree_attribute`. Two anchor defects below (F2, F3), plus anchor-coverage gap F4. |
| 4 | `verified-at:` | PASS | Entry:4 `2026-10-24` with the regeneration claim; independently reproduced: `python3 -B generator.py` in `/tmp/r65q02gen` printed `fixture.apk 947 bytes sha256 05d2280f…d03e` and wrote `truth.json` sha256 `27303bae…8173` — byte-identical to the committed pair. Host `python3 --version` = `Python 3.14.8`, matching the claim. |
| 5 | `recheck:` with command AND stdout sha256 | PASS for the header line / **FAIL for verbatimness of the reproduced output** | Command run from lane root: exit 0, 15 lines, `sha256sum` = `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — exactly the header value. Re-run from `/tmp` with an absolute script path gave an identical file (`diff` clean), confirming the "any checkout" claim; output contains no `/home`, `/tmp`, `/var` paths (`grep -c` = 0); `--fact eocd` prints the single claimed JSON line, exit 0. However the entry's item-3 MANIFEST.MF line is not the command's output (F1). |
| 6 | `coverage-map:` row C05 named | PASS | Entry:6 `coverage-map: C05 (`corpus/README.md`, Android packages (APK))`; `corpus/README.md:34` is `| C05 | Android packages (APK) | — | — | frontier |` — named, and still `frontier` (unflipped, as the frozen admission order requires). |

Overall Q02 recommendation: **FAIL** until F1–F3 are corrected (all are text-only; no fixture byte, oracle, readout or digest changes are implied — those all verify).

# Findings by severity

## F1 (medium — blocks the entry's own verbatim-evidence claim)
Entry line 41 quotes a MANIFEST.MF readout line whose `payload_first16_hex` is not what the frozen recheck command prints:

```
entry:41   "payload_first16_hex": "4d616e696673742d56657273696f6e"   # 15 bytes -> b'Manifst-Version'
readout:6  "payload_first16_hex": "4d616e69666573742d56657273696f6e" # 16 bytes -> b'Manifest-Version'
```

Direct fixture check: `python3 -c "print(open('corpus/fixtures/apk-r65/fixture.apk','rb').read()[668:684])"` → `b'Manifest-Version'`. The entry drops the `65` pair (the `e`), so the quoted value contradicts the actual member bytes *and* the header's own stdout digest (`507d79f8…` is the digest of the true output, which cannot contain the quoted 15-byte hex). Every other one of the 15 reproduced JSON lines is set-equal to the real stdout (`sort` both, `diff` yields only this pair); the ordering also differs (the entry lists per-fact outputs in item order, stdout prints `spec_derived_struct_widths` second), which is minor. Item 10's prose (`Manifest-Version: 1.0`) is correct, so the defect is isolated to line 41.

Fix: replace the hex with `4d616e69666573742d56657273696f6e`. Also bears on Q11 (a quoted deriving output that the deriving command does not print) — noted, not judged here.

## F2 (medium-low — anchor does not resolve)
Entry:2 cites S039 "anchor: line 5 (`Start with inspect_android_package ...`)". In the named snapshot, line 5 is `older server.`; the unique quote is at line 7:

```
$ grep -n 'Start with `inspect_android_package`' .ufo/waves/round-65/source-snapshots/rea-android-applications.md
7:Start with `inspect_android_package` on the caller's APK path for package
```

`corpus/SOURCES.md:53` repeats "line 5", so both the entry header and the registry row carry the same off-by-two. The snapshot is byte-identical to the npm-package member (`.ufo/waves/round-65/R65SnapshotManifest.md:18`, `BYTE_COMPARE=identical`), so line 5 is wrong against upstream too, not a re-wrapping artifact. Fix: line 5 → line 7 in both places (or state "upstream/snapshot line 7").

## F3 (low — named constant outside the cited range)
Entry:1 and body line 53 cite S038's "chunk-type enum … (lines 239-250)" and body line 53 attributes all six observed chunk-type values, including `0x0180`, to that range. `RES_XML_RESOURCE_MAP_TYPE = 0x0180` is at line 253:

```
$ sed -n '236,253p' …/ResourceTypes.h   # enum { at 237; RES_XML_TYPE 241; …; RES_XML_RESOURCE_MAP_TYPE 253
```

Five of the six named types do fall in 239-250; the resource-map type is three lines outside. Fix: `(lines 241-253)` or cite `RES_XML_RESOURCE_MAP_TYPE` at `:253` separately.

## F4 (low — header anchor list omits two body attributions)
The body attributes two load-bearing constants/semantics to S038 with no line anchor anywhere: `UTF8_FLAG` (entry:64; snapshot line 480) and `ResXMLTree::getAttributeNameResID` (entry:71; snapshot line 792). Neither appears in the header's anchor list (entry:1). Fix: add `ResStringPool_header` flags enum `UTF8_FLAG` `:480` and `getAttributeNameResID` `:792`.

## F5 (low — dangling internal pointers)
- Entry:3 S041 says "row text in §Sources"; the entry has no `§Sources`/`## Sources` section (headings: Observation, Comparison with the authored oracle, Observation / inference / unknown, Limitations, Cross-lane scope note (Q10), §Q-map, Reproduce). The intended target is `corpus/SOURCES.md:55`.
- Entry:15 says "the script is the `### Code` block of that section … and the same lines appear in the full 15-line stdout reproduced there", but §Reproduce (entry:154-162) contains only a one-line `sh` block and no `### Code` block, no script body and no 15-line stdout block (`grep -n '### Code'` finds nothing). The script is only at `corpus/fixtures/apk-r65/readout.py`.
- Entry:11 says the struct field lists are "in item 2 below"; the derivation is item 5 (entry:55).

# Positive controls run

- Snapshot provenance: `.ufo/waves/round-65/R65SnapshotManifest.md:17-19` records re-fetch receipts (googlesource `?format=TEXT` decode, `npm pack rea-agents@6.5.0` extraction, docs.python.org fetch) each `BYTE_COMPARE=identical`. I did not re-fetch (no network step in this seat); all line checks therefore assume those receipts.
- Fixture regeneration is deterministic on this host: `/tmp/r65q02gen` run reproduced both `fixture.apk` and `truth.json` at the committed digests.
- `readout.py` is cwd-independent: `ROOT = Path(__file__).resolve().parent` (readout.py:20) and the printed path is a literal repo-relative string (readout.py:45); the `/tmp` run reproduced the 15 lines and the header digest.
- README C05 is untouched (`frontier`), matching build state and the frozen admission order.

# Residual risk

- Anchor verification is against the wave-65 snapshots, not a fresh network fetch; a bad snapshot capture would propagate. Mitigated by the manifest's byte-compare receipts and by the S038 snapshot's line numbers matching all seven struct anchors exactly.
- The entry's container claims rest on registry rows S032/S034, which the header does not restate (only S038/S039/S041). I confirmed the APPNOTE snapshot (`appnote.txt`, sha256 `0b9930…cd6`, 174585 bytes) lines 387-399 are §4.3.7 and sum to the claimed 30-byte fixed part, and registry rows `SOURCES.md:46,48` carry the 46-byte/30-byte scopes; a header omission, not an evidence failure.
- I judged only Q02. F1 also implicates Q11's "recorded value presented with its deriving command" test; Q01/Q03–Q13 and the C2 axis are outside this seat.

# Verification gaps

- No `lsp` device was available in this seat's toolset; Markdown has no applicable server here, so grep/awk over exact bytes was the fallback for all line-anchor claims.
- Did not re-fetch S038/S039/S040 from the network; provenance is taken from `R65SnapshotManifest.md` and digest equality with the header/registry.
- Recommend (not an edit) that the admission gate add an automated verbatim diff of the entry's fenced JSON lines against the recheck stdout — F1 is exactly the class of defect that only that diff catches.
