# R68ReviewEntryQ07 — Q07 on the round-68 C05 v3 candidate

FAIL — Q07. Entry line 89 asserts a namespace-resolution *behavior* ("the same constant on `android`-carrying attributes resolves instead through the start-namespace chunk at offset 248") as fact, with no pre-registered hypothesis, no spec-derived ground truth for the resolution rule, and no command that reproduces it; the value it names is contradicted by the entry's own output three lines above (`versionCode`/`versionName` carry `ns_index: 0`, not `0xffffffff`) and by the spec anchor it relies on (S038 `ResourceTypes.h:709-710`: `// Namespace of this attribute.` / `struct ResStringPool_ref ns;` — a string-pool reference).

- criterion: Q07 (predicted parser behavior is a pre-registered hypothesis with spec-derived ground truth, recorded whichever way it falls; reject when a prediction is written as fact, or an unreproduced cause is used as support).
- artifact under review: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md`, sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b` (209 lines), read at its absolute path; no file edited.
- verdict scope: this criterion only, on these bytes. I did not score Q01–Q06, Q08–Q13.

## Evidence commands and actual output

All commands run from `/home/vgpnk/Projects/shokunin/revenger-shokunin`; the entry's own commands were replayed, not trusted.

1. Spec anchors (the entry's item 11 command):

```
$ python3 -B corpus/derive_axml_anchors.py
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum RES_STRING_POOL_TYPE : 239
enum RES_XML_TYPE : 241
enum RES_XML_START_NAMESPACE_TYPE : 245
enum RES_XML_END_NAMESPACE_TYPE : 246
enum RES_XML_START_ELEMENT_TYPE : 247
enum RES_XML_END_ELEMENT_TYPE : 248
enum RES_XML_RESOURCE_MAP_TYPE : 253
comment attributeStart : 686
field attributeStart : 687
EXIT=0
```

17 lines, exit 0 — byte-identical to the block at entry:129-147. Independently of the deriver, the numbered snapshot lines confirm the same values:

```
$ awk 'NR>=244 && NR<=245 {printf "%d:%s\n", NR, $0}' corpus/snapshots/ResourceTypes.h
244:    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245:    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
$ awk 'NR==686 || NR==687 {printf "%d:%s\n", NR, $0}' corpus/snapshots/ResourceTypes.h
686:    // Byte offset from the start of this structure where the attributes start.
687:    uint16_t attributeStart;
```

Snapshot digest/size match the entry's S038/S046 pins: `sha256sum corpus/snapshots/ResourceTypes.h` → `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, `stat -c '%s'` → `86255`; identical to `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`.

2. The readout (entry:189-214) replays byte-for-byte:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/r68q07_readout.out
EXIT=0 ; wc -l → 15 ; sha256sum → 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```

A scripted replay of **every** embedded command in the entry (17 blocks: 16 `readout.py` invocations plus `derive_axml_anchors.py`) compared the entry's block lines to fresh stdout: `blocks with embedded commands checked: 17 mismatches: 0`. The final full-stdout block at entry:198-214 diffs empty against the rerun (15 lines, `DIFF LINES: 0`). So the transcription surface of this candidate is clean; the defect is in the prose claim that sits directly on top of a clean output.

3. The claim at entry:89, quoted exactly:

```
The `0xffffffff` namespace index on `package` and the element itself is recorded as observed and
treated as null by the readout (readout.py:22); the same constant on `android`-carrying attributes
resolves instead through the start-namespace chunk at offset 248, which states prefix index 0
(`android`) and URI index 1 (`http://schemas.android.com/apk/res/android`):
```

4. The output that contradicts it, entry:86 (reproduced by me):

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_element
{... "attributes": [{"data_type": "0x03", ..., "name": "package", "name_index": 3, "ns": null,
 "ns_index": 4294967295, ...}, {"data_type": "0x10", ..., "name": "versionCode", "name_index": 5,
 "ns": "android", "ns_index": 0, ...}, {"data_type": "0x03", ..., "name": "versionName",
 "name_index": 6, "ns": "android", "ns_index": 0, ...}], "classIndex": 0, "element_name": "manifest",
 "element_name_index": 2, "element_ns": null, ...}
```

`0xffffffff` (`ns_index: 4294967295`) occurs only on `package` and on the element (`element_ns_index`); both `android`-carrying attributes carry `ns_index: 0`. The pool string at index 0 is `android` (entry:72: `"strings": ["android", "http://schemas.android.com/apk/res/android", ...]`, and `offsets[0] = 0`).

5. The resolution mechanism the readout actually uses:

```
$ grep -n 'NO_INDEX\|strings\[ans\]\|namespace' corpus/fixtures/apk-r65/readout.py
22:NO_INDEX = 0xFFFFFFFF
178:    for label, ctype in (("start_namespace", 0x0100), ("end_namespace", 0x0101)):
211:            "ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],
219:         element_ns_index=ns_idx, element_ns=None if ns_idx == NO_INDEX else strings[ns_idx],
```

The readout resolves an attribute's `ns` from the **string pool** (`strings[ans]`); it never consults the start-namespace chunk (readout.py:178-184 only *prints* that chunk's prefix/uri pair). The spec agrees:

```
$ awk 'NR>=707 && NR<=710 {printf "%d:%s\n", NR, $0}' corpus/snapshots/ResourceTypes.h
707:struct ResXMLTree_attribute
708:{
709:    // Namespace of this attribute.
710:    struct ResStringPool_ref ns;
```

`ns` is a `ResStringPool_ref` — an index into the string pool — not an index that "resolves through" `ResXMLTree_namespaceExt`. S038 gives no rule under which an attribute namespace is obtained from the namespace chunk, and the entry cites no S038 line for such a rule.

6. Provenance of the sentence (context, not my evidence base): the identical sentence is inherited verbatim from the rejected round-67 candidate (`corpus/knowledge/round-67-apk-axml-byte-evidence.md:88`), while the round-65 candidate had a different, more defensible subject — "the `android` namespace prefix resolves through the start-namespace chunk at offset 248" (`round-65-apk-axml-byte-evidence.md:85`). The round-68 build changed this sentence not at all (its declared deltas are the `:245` anchors, the 686/687 anchors, item 11, the snapshot copy, and the status line), so the defect rides through unchanged.

7. Checked and clean under Q07 (so the FAIL is one clause, not the whole entry):

- Spec-anchored hypothesis with recorded outcome (the good pattern): entry:82 derives `attribute i = chunk_base + 16 + attributeStart + i * attributeSize` from S038:677/686/687, and the observed `attributeStart 20` / `attributeSize 20` / `attributeCount 3` (entry:86) is the recorded outcome, matching the derived 20/20 struct sizes (entry:63).
- Cause claim reproduced independently: entry:147 "That one-line off-by-one is what falsified the round-65 and round-67 drafts (M40/M44)". The r67 candidate wrote `start/end namespace :244/:246` (`round-67-apk-axml-byte-evidence.md:56`), the pinned snapshot has `245` (evidence 1), and the r67 candidate's own status line records the Q02 FAIL on that value (`round-67-apk-axml-byte-evidence.md:8`). The cause is reproduced from records external to this entry.
- Tool-refusal claim verified (out of Q07 scope — a tool property, not a parser prediction, but it shows the entry's refusal claims are real): a `/tmp` copy of `corpus/derive_axml_anchors.py` pointed at a snapshot with `RES_XML_START_NAMESPACE_TYPE` removed printed `derive_axml_anchors: enum RES_XML_START_NAMESPACE_TYPE: not found` and exited 2, as entry:125-127 claims.

## The entry lines at issue, and the correct values

- Line 89, first wrong clause: "**the same constant** on `android`-carrying attributes". Wrong value: implies the two Android attributes carry `0xffffffff`. Correct value, printed by the entry's own command: `ns_index: 0` for both `versionCode` (entry:86, third object) and `versionName` (entry:86, fourth object); `0xffffffff` appears only on `package` (`ns_index: 4294967295`) and on the element.
- Line 89, second wrong clause: "**resolves instead through the start-namespace chunk** at offset 248". Wrong value: a resolution rule in which the attribute namespace is obtained from the namespace chunk. Correct value: the readout (readout.py:211) and the spec (S038:709-710, `struct ResStringPool_ref ns;`) resolve the attribute namespace as the *string-pool* entry at `ns_index`; here index 0 = `android`. The start-namespace chunk records a separate observation — `prefix_index 0` = `android`, `uri_index 1` = `http://schemas.android.com/apk/res/android` (entry:93, reproduced) — which is what the `--fact axml_start_namespace` line actually prints and nothing more.
- Consequence the entry should record instead of explaining away: under S038:709-710 the fixture's `ns_index: 0` points at the pool string `android`, a prefix, while the namespace URI is pool string 1. That is an authored-fixture property (or an unknown), to be recorded as observed; inventing a resolution-through-the-namespace-chunk rule to make the URI appear is exactly the "prediction written as fact" Q07 rejects.
- If a resolution rule is to be claimed at all, Q07 requires: a pre-registered hypothesis, an S038 anchor for the rule, and a probe whose accept/refuse outcome is recorded. Neither is present.

Not my criterion (flagged for the Q11 seat, not scored here): the same sentence carries a value the named command does not print — no command prints `0xffffffff` on an `android`-carrying attribute, and no command prints any attribute resolving through the namespace chunk. Also observed, not evidence for my verdict: the entry's own `## §Q-map` row says "Q07 | pass | no parser-behavior prediction is made or needed; the readout describes observed bytes only" (entry:178), which is contradicted by entry:89 on these bytes.

## Residual risk and verification gaps

- Scope dispute, stated honestly: if the adjudicator reads Q07's "parser behavior" as only the rea/`inspect_android_package` provider surface, entry:89 is then a false value claim under Q11 rather than a Q07 prediction — but either way the bytes are not clean, and the Q07 row's stated basis ("no parser-behavior prediction is made") is false as written. I judge AXML namespace resolution to be parser behavior (it is what a consumer does with the `ns` field), so Q07 FAIL.
- I did not run an Android/AXML parser, so I do not claim what a real device parser does with this fixture; the finding rests only on the entry's own output, the entry's own readout code, and the pinned S038 bytes, all of which I re-derived.
- I did not read `corpus/README.md`, `SCORECARD.md`, the counter, or other seats' results; no README flip was checked (not my criterion).
- No tool installs or upgrades were performed, so nothing to record under the tooling directive.

Report path (relative to the lane repo, as required): `.ufo/waves/round-68/R68ReviewEntryQ07.md` → written at `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-68/R68ReviewEntryQ07.md`. No other file was written; `corpus/`, `reports/`, the lane Git/jj state and `/tmp` scratch only.
