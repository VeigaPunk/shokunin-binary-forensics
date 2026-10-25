# R67ReviewEntryQ02 — fresh-seat Q02 decision on the landed v2 C05 candidate

Q02 FAIL (exact-anchor violation: `corpus/knowledge/round-67-apk-axml-byte-evidence.md:1` and `:56` anchor `RES_XML_START_NAMESPACE_TYPE` at snapshot line 244; in the entry's own pinned, hash-matched snapshot it is at line 245 — line 244 is `RES_XML_FIRST_CHUNK_TYPE`.)

Entry under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-67-apk-axml-byte-evidence.md` (committed, clean; entry + S045 snapshot landed in `7668510` "round-67: build — C05 v2 candidate …"). Criterion: `corpus/QUALITY.md:14` (Q02: `source:` S### row/URL/path + exact anchor, `verified-at:`, `recheck:`, coverage-map row named; fail = "any header is missing or the anchor is a bare homepage"). Decision made on committed bytes; I am not the author.

## The failing fact (file:line + command + actual output)

Claim (entry:1, header `source: S038` anchors; repeated entry:56, item 4 "start/end namespace :244/:246"):

> `RES_XML_START_NAMESPACE_TYPE` **:244**

Pinned snapshot (entry:1 itself pins `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 bytes — I re-hashed: both match, so this is the exact file the anchor must resolve against):

```
$ grep -nE '^\s*(RES_[A-Z_]+_TYPE)\s*=' .ufo/waves/round-65/source-snapshots/ResourceTypes.h
244:    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245:    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
```

Line 244 is a different named enum constant. The anchor does not resolve to the identifier it names — not exact. Attribution: the retained r65 candidate contains **zero** `:244` occurrences (`grep -c ':244' corpus/knowledge/round-65-apk-axml-byte-evidence.md` → 0) and cites the enum as a bare `:239-250` span; the per-type line list is newly introduced by the v2 header's claimed "re-opened 2026-10-24 … from the committed snapshot" re-derivation, and one of its seven line mappings was mis-transcribed — the M39 transcription-drift class, this time in the anchor dimension of the header whose exactness the round-66 routing was supposed to establish. Under Q02's "exact anchor" requirement this is a FAIL; the kill rule then applies to C05 (stays `uncovered`, entry → rejected, C1 FALSIFIED) per `reports/round-67/claims.md`.

## What was checked and passed (evidence)

- **Header completeness** — all required headers present: four `source:` lines (S038/S043/S045/S041, each with a full URL or repo path — none a bare homepage), `verified-at: 2026-10-24` (entry:5, with base commit `c7b7cf98`), `recheck:` with command + stdout sha256 (entry:6), `coverage-map: C05` naming `corpus/README.md` (entry:7).
- **Registry rows exist, tier A** — `corpus/SOURCES.md:52` S038 (spec/A), `:57` S043 (docs/A, corrected "snapshot lines 7-8 (S039 cited line 5 — wrong)"), `:55` S041 (own-work/A), `:59` S045 (docs/A, appended this round).
- **Snapshot integrity** — sha256/size all match the entry's pins: ResourceTypes.h `56b88bc4…` 86255 B; `.ufo/waves/round-67/source-snapshots/dex-format.html` `c0428612…` 281157 B; `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` `412d9cb4…`. `git status --porcelain` over all snapshot dirs, `corpus/fixtures/apk-r65`, and the entry file: empty (clean).
- **S043 anchor exact** — raw lines 5-9 of the rea snapshot: the quoted `Start with \`inspect_android_package\` … inline Evidence.` sentence spans exactly lines 7-8; line 5 is literally `older server.`, exactly as the entry's r65-drift note says.
- **S045 anchor exact** — all four quoted field texts verbatim in dex-format.html: checksum `:5949-5950` ("adler32 checksum of the rest of the file (everything but magic and this field)"), signature `:5956-5957` ("SHA-1 signature (hash) … magic, checksum, and this field"), header_size `:5981-5982` ("must be 0x70 (112) bytes" + "(v40 or earlier)"), `:5035` `uint ENDIAN_CONSTANT = 0x12345678;`. The surrounding `:5940-6000` table is the magic/checksum/signature/file_size/header_size/endian_tag field table — the `header_item` table the anchor names.
- **S038 enum span and load-bearing anchor exact** — `struct ResChunk_header` :218; block :237-253 as claimed; **`RES_XML_RESOURCE_MAP_TYPE = 0x0180` at :253 exactly** (the routed repair); STRING_POOL :239, XML :241, END_NAMESPACE :246, START_ELEMENT :247, END_ELEMENT :248 — six of seven sub-anchors exact (the seventh is the FAIL above). Struct anchors: `Res_value` :287, `ResStringPool_header` :461, `ResXMLTree_header`/:612, `_node` :621, `attrExt` :677, `_attribute` :707 — all exact.
- **S041 hashes exact** — fixture.apk `05d2280f…` (947 bytes measured), truth.json `27303bae…`, readout.py `92e347c3…`: all three re-hashed, all match entry:4.
- **recheck re-derived by this seat** — `python3 -B corpus/fixtures/apk-r65/readout.py` from the lane root: exit 0, 15 stdout lines, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247` — byte-identical to the header's claimed value (entry:6).
- **Coverage row exists and is not flipped** — `corpus/README.md:34`: C05 "Android packages (APK)", status `uncovered`, knowledge column names only the retained rejected r65 candidate — consistent with the build state (flip belongs to the L1 post-adjudication, not this seat).

## OFF-criterion defects

- **OFF**: `corpus/SOURCES.md:52` — the S038 registry row still carries the superseded r65 span "chunk-type enum :239-250" while entry:1 declares the row "re-opened 2026-10-24 … from the committed snapshot" with the corrected :237-253; registry anchor and the citing entry's anchor now disagree. Registry staleness (Q02 judges the entry's header, hence OFF here) — any later file citing S038's *row* anchor gets the wrong span.
- **OFF (minor)**: entry:1 anchors the attrExt `attributeStart` comment "at lines 685-687"; the quoted sentence is exactly line 686 of the pinned snapshot (the 3-line window contains it, so it locates — contrast :244, which misses its target).

## Residual risk / verification gaps

- I did not re-derive the AXML/dex observation **values** (items 1-10) — that surface belongs to the Q11/C7 seats; my recheck re-run validates only the header's `recheck:` contract (exit 0, 15 lines, stdout digest).
- I did not grep the literal `header_item` heading in dex-format.html; the field table at :5940-6000 is unambiguous by its fields.
- Tooling directive record: no tools installed or updated by this seat (no pacman/uv/npm activity; nothing to log).
- This verdict is a recommendation to the adjudicator, not an admission; per the frozen kill rule a Q FAIL on the v2 bytes routes C05 to stay `uncovered` and the entry to be marked rejected — L1's call, on these committed bytes.
