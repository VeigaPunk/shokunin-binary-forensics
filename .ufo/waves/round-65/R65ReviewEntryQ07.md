PASS — Q07: the entry predicts no parser/provider accept, refuse or cause; the absence is explicit at four fenced sites, and each value it does state is a reproducible observation (the entry's own recheck hash matches exactly). Two adjacent Q01-class defects are handed off (entry:71 semantics attributed to S038 that its snapshot does not state; entry:103 dex header layout with no registered spec row) — neither meets Q07's enumerated trigger.

# Seat and bytes under test

- Seat: R65ReviewEntryQ07 (independent leaf, read-only). Criterion text: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/QUALITY.md:19` — "A predicted parser behavior (accept, refuse, cause) is a pre-registered hypothesis with spec-derived ground truth and is recorded whichever way it falls. A cause is stated only once independently reproduced." Reject trigger: "a prediction is written as fact, or an unreproduced cause is used as support."
- Entry: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-65-apk-axml-byte-evidence.md`, sha256 `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7`, `admission-status: candidate` (entry:7).
- Tree: lane HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` ("round-65 verifier spot-check (integrator, hyaku): non-author admit/reject"); read-only `git status --porcelain` over entry, `corpus/fixtures/apk-r65`, `SOURCES.md`, `corpus/lessons/round-65.md` returned 0 lines, so the reviewed bytes are committed-tree bytes, not a working-tree drift.
- Fixture/readout digests recomputed: `fixture.apk` `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (matches entry:19 and `SOURCES.md:55`), `readout.py` `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` (matches entry:162).

# Absence of parser predictions — verified, and explicit

Scan for prediction/validity vocabulary across the whole entry:

```
$ grep -n -i -E "accept|refus|valid|install|predict|hypothes|assum|expect|must|should|would|cause" corpus/knowledge/round-65-apk-axml-byte-evidence.md
6:coverage-map: ... Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture.
55:  5. The fixed structure widths used by the readout are computed by summing the field widths of S038's own struct definitions ... not assumed:
127:- **Unknown** — nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed; the fixture is inert and no producer was called.
131:One authored fixture, ... The dex member is a header only and is intentionally not a valid dex program. Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence.
143:| Q03 | pass | expected values come from the authored oracle ... |
147:| Q07 | pass | no parser-behavior prediction is made or needed; the readout describes observed bytes only. |
148:| Q09 | pass | ... the dex checksum/signature self-consistency is explicitly an inert declared-header property, not validity. |
```

Every hit is a fence or a non-prediction ("not assumed", "expected values", the Q07/Q09 rows). No sentence states that a parser, installer, provider or checker accepts, refuses or is caused to do anything. The fences are four, not one:

- entry:6 coverage-map — "Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture."
- entry:127 §Observation/inference/unknown — "nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed".
- entry:131 §Limitations — "intentionally not a valid dex program"; "would need its own evidence" (hedged evidence requirement, not a behavior claim).
- entry:135 §Cross-lane scope note (Q10) — "this lane ran no provider and makes no readiness claim (Q05 fence)"; Q05 row at entry:145 says the same.

Nothing is predicted, so Q07's "recorded whichever way it falls" has no object: there is no hypothesis table in the entry, and none is required. The only Q07 record is the Q-map row (entry:147), and its decision matches the body on the enumerated trigger.

# The stated values are observations, not predictions

The recheck command in the entry was executed unmodified (read-only: `readout.py` writes nothing — `grep -n -i -E "write|open\(|mkdir|unlink" readout.py` hits only a comment at :50 and the variable name `parsed_entries` at :86):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py
exit=0
15 /tmp/r65q07.out
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/r65q07.out
```

That hash equals entry:5 verbatim (`507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`, 15 lines, exit 0), so every embedded stdout block in items 1–10 is reproducible from the committed fixture, not asserted.

Spot-check of the one construction/format claim that a container reader would depend on (entry:131 "ZIP_STORED with no data descriptors"), read directly from the fixture bytes:

```
$ python3 - <<'EOF'  # offsets: EOCD 925, CD 737; CD flags +8, method +10; LFH flags +6, method +8
...
eocd sig 504b0506
cd_off 737
flags 0x0 method 0
name_len 19 name b'AndroidManifest.xml'
lfh sig 504b0304 lfh flags 0x0 lfh method 0
EOF
```

Method 0 (stored) and GP flags `0x0000` (no bit-3 data descriptor) on both the central-directory and local records — the limitation is a true byte fact, not a prediction. Likewise the typed-value gloss at entry:78 (`0x03` string, `0x10` int) is a spec constant present in the cited snapshot: `.ufo/waves/round-65/source-snapshots/ResourceTypes.h:307` (`TYPE_STRING = 0x03`) and `:327` (`TYPE_INT_DEC = 0x10`); the null-namespace gloss at entry:85 is backed by `:786` ("Returns -1 if no namespace") plus the uint32 `ResStringPool_ref` encoding.

# Findings

No Q07-blocking finding. Adjacent defects that belong to other criteria:

**M1 — MEDIUM (handoff: Q01; Q07 basis is overbroad).** entry:71 states: "Seven entries are `0x00000000` — S038's `ResXMLTree::getAttributeNameResID` semantics make 0 'no resource id'". The cited snapshot does not state that semantics:
- `ResourceTypes.h:792` declares `uint32_t getAttributeNameResID(size_t idx) const;` with no comment (the surrounding comments at :786 and :789-790 cover namespace-id `-1` and the UTF-8 accessors, not resource-id zero).
- The resource-map chunk comment is `ResourceTypes.h:251-253`: "This contains a uint32_t array mapping strings in the string pool back to resource identifiers. It is optional." — no zero semantics.
- The only "0 means" lines in the snapshot are `:914` (ResTable_package id), `:963`/`:965` (ResConfig MCC/MNC) — unrelated structures.
- The registry row's scope is field layout only: `corpus/SOURCES.md:52` ("field layout of the compiled-XML (AXML) chunk, string-pool, node, attribute and value structures").

So the gloss is an AOSP convention imported as fact and attributed to S038, and it is not listed in the entry's own inference layer at entry:126 (which lists the chunk-type, null-index and resource-map-id inferences but not this one). Q07's enumerated trigger (accept, refuse, cause) is not met, so this is not a Q07 reject; under Q01 it is a "claim exceeds what the cited text states" risk. Consequence for this seat: entry:147's basis sentence — "the readout describes observed bytes only" — is one sentence too broad, because entry:71 adds a semantic gloss the readout does not observe.

**M2 — MEDIUM (handoff: Q01).** entry:103 states the dex declared-header semantics: "Its declared checksum `0x3d120c30` equals the Adler-32 recomputed over the bytes from offset 12 on, and its declared 20-byte signature equals the SHA-1 recomputed over the bytes from offset 32 on." No `corpus/SOURCES.md` row registers a dex-format specification: the only registry mention of "dex" as a word is `SOURCES.md:55` (S041, own-work bundle, scope "byte content ... byte/oracle correspondence only"), and S038/S039/S040 are ResourceTypes.h, the REA Android guide, and the CPython zipfile docs. The offsets 12/32 and the hash-exclusion ranges are therefore unregistered spec knowledge used as ground truth. This does not trigger Q07: the entry claims only declared-field self-consistency, explicitly refuses validity (entry:131; Q09 row entry:148), and never says a dex parser/installer accepts the member. Recommended fix before admission: register a dex-format spec row, or move the dex field layout into the entry's inference layer with its actual support.

**M3 — LOW (handoff: Q01/Q11, anchor precision).** entry:53 says the six chunk types "are the values S038's chunk-type enum names at lines 239-250", but `RES_XML_RESOURCE_MAP_TYPE = 0x0180` sits at snapshot `:253` — outside the cited range — even though item 4 (entry:46) and item 7 (entry:71) use `0x0180`. The same range is carried in the registry row `SOURCES.md:52`, so the entry inherits a row-level off-by-three; `RES_XML_TYPE` is at `:241`, start/end namespace at `:245`/`:246`, start/end element at `:247`/`:248` (all inside the range). Fix the range or cite `:253` explicitly.

# Residual risk and verification gaps

- Judgment boundary: Q07's parenthetical enumerates accept/refuse/cause. If L1 reads "parser behavior" broadly enough to include lookup/return-value semantics, M1's sentence (entry:71) becomes a Q07 reject under "a prediction is written as fact", because its cited source does not contain the semantics. My recommendation is Q07 pass on the enumerated trigger with M1 fixed under Q01 before admission; a stricter adjudicator would need to reject Q07 on entry:71, not on anything else.
- I did not re-derive every numeric value in items 1–10 (other seats own Q08/Q11). My evidence that the entry's values are observations rather than predictions is the exact recheck-hash match plus the ZIP method/flags and value-type-anchor spot checks above; that does not certify numeric correctness, only provenance as reproducible observation.
- The candidate is committed at HEAD `8214e4dd`, so the round-end committed-archive measurement can cover it; this report is a Q07 recommendation on entry sha256 `e173e643…`, not an admission.
- Bounds: I made exactly one write (this report), ran no git/jj mutations, and ran only the entry's own read-only readout. No tool installs were needed or performed.
