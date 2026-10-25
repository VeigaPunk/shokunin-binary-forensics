SCOPE-BLEED — two sentence sets exceed the declared observation scope: (1) the "framework attribute ids" identity claim at `corpus/knowledge/round-68-apk-axml-byte-evidence.md:75` and `:157`, which rests only on the authored fixture and its own oracle and on no `corpus/SOURCES.md` row; (2) the universal "every S038 line number … is machine-derived / printed by a committed derivation script" at entry:1, :4, :125, :148, :156, :182, falsified by the entry's own citations of lines 237 and 244, which `corpus/derive_axml_anchors.py` does not print. The byte values in items 1-10 are sound (re-derived below); the excess is in provenance and identity sentences, plus three limitations the `## Limitations` block omits.

# R68CriticEntryScope — Q10 scope and limitation audit of the C05 v3 candidate

**Findings in detail** — the verdict line above is the summary; the sections below give the counterexample, evidence, impacted axes and smallest safe correction for each finding.

Assigned axis: Q10 (`corpus/QUALITY.md:30`) and the admission-procedure limitation clause (`corpus/QUALITY.md:40-41`). Read-only seat: no file was edited, no git/jj command was run, nothing was written outside this report.

## Commands run and their actual output

Lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

```
$ python3 -B corpus/derive_axml_anchors.py
exit 0, 17 lines:
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

$ python3 -B corpus/fixtures/apk-r65/readout.py
exit 0, 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
   (matches the `recheck:` claim at entry:7 and the §Reproduce claim at entry:196 exactly)

$ sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h \
    corpus/derive_axml_anchors.py corpus/fixtures/apk-r65/{fixture.apk,readout.py,truth.json} \
    .ufo/waves/round-65/source-snapshots/rea-android-applications.md
56b88bc4…c56f  corpus/snapshots/ResourceTypes.h          (== pinned snapshot, 86255 bytes)
56b88bc4…c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
bce497d6…e249  corpus/derive_axml_anchors.py             (== S046 anchor)
05d2280f…f03e  fixture.apk (947 B) | 92e347c3…3976 readout.py | 27303bae…8173 truth.json
412d9cb4…a74c  rea-android-applications.md              (== S043 anchor)
```

All digests the entry states are correct for the bytes they name (Q09 holds). Fixture/oracle/readout bytes are unchanged from round 65.

## F1 — SCOPE-BLEED: "every S038 line number … machine-derived" is false for 237 and 244

Sentences (all in the audited entry):

- entry:1 (S038 row): "chunk-type enum block **lines 237-253** … **every line number above is machine-derived by `corpus/derive_axml_anchors.py` from the pinned snapshot — item 11**". `237` is stated above and is not in the 17-line output.
- entry:4 (S046 row): "scope: the machine derivation of **every** S038 line number this entry cites" (same universal in `corpus/SOURCES.md:61`).
- entry:125: "**Every S038 line number this entry states is printed by a committed derivation script** … — **no spec line number in this entry is transcribed by hand**."
- entry:148: "The chunk-type enum block spans lines **237-253** … **line 244 is `RES_XML_FIRST_CHUNK_TYPE`**." Neither 237 nor 244 is printed by the script.
- entry:156 (Observation): "every spec line number in item 11, derived from the pinned snapshot bytes by a committed script that cannot print a line it did not find."
- entry:182 (Q11 row): "the spec line numbers carry their deriving command and output (item 11, machine-derived, **not transcribed**)."

Evidence that the universal is false:

```
$ grep -n '237\|244' /tmp/r68scope-anchors.txt        # the script's 17-line stdout
1:sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
```

The only textual hit is the sha256 banner, not an anchor line. Script body `corpus/derive_axml_anchors.py:35-53` enumerates 7 structs and 7 enum symbols — `RES_XML_FIRST_CHUNK_TYPE` is absent, and there is no "enum block start" search. So 237 and 244 are hand-read. The cited values are themselves right (`corpus/snapshots/ResourceTypes.h:237` = `enum {`, `:244` = `RES_XML_FIRST_CHUNK_TYPE = 0x0100`), which makes this exactly the M39/M40 "transcribed line number presented as derived" pattern the entry says it repairs — now inside the sentence that claims the repair.

Consequence: Q11 ("recorded value presented as re-derived") and Q13 ("a verifier is credited only for the clauses its own run detects") both fail on this entry's own self-description, and the "no spec line number is transcribed by hand" statement is the unguarded clause. Q10 impact: a coverage claim about the verifier that generalises from 17 printed symbols to "every".

## F2 — SCOPE-BLEED: "framework attribute ids" is a framework-wide identity claim sourced from the fixture's own oracle

- entry:75 (item 7, Observation section): "exactly the two **framework attribute ids** the fixture's authored oracle declares for those strings (`truth.json` `axml_declared.resource_ids`), which is the correspondence this entry claims".
- entry:157 (Inference): "the two non-zero resource-map entries are the **framework** `versionCode`/`versionName` ids the fixture generator declared (`truth.json`)".

The only witness is the authored record under test:

```
$ read corpus/fixtures/apk-r65/truth.json    # axml_declared
"attributes": [ {"data":4,"data_type":3,"name_idx":3,"ns_idx":4294967295,"raw_value_idx":4}, … ],
"resource_ids": ["0x00000000","0x00000000","0x00000000","0x00000000","0x00000000",
                 "0x0101021b","0x0101021c","0x00000000","0x00000000"],
```

No name, no provenance, no `android.R.attr` reference. The attribute *names* (`versionCode`, `versionName`) are the fixture's own authored string-pool entries (entry:67 output). And no source row establishes the id→attribute mapping:

```
$ grep -n '0101021b\|0101021c\|attribute id\|android.R.attr\|framework attribute' corpus/SOURCES.md
(no output)
```

S038 defines struct layout and the `res_id` field only; it contains no framework attribute-id table. The entry fences only the *zero* entries ("no framework-wide semantics for a zero entry is claimed from this fixture", entry:75) and leaves the non-zero identity — the one that actually needs a framework-scope witness — unfenced. On Q03's independence test this is circular: the "correspondence" is between two authored artifacts written by the same generator.

Scope verdict: an Android-framework-wide fact asserted from "one authored fixture" (the exact axis the brief names). Smallest safe correction: reword to "the two non-zero resource-map ids the fixture's authored oracle declares (`0x0101021b`, `0x0101021c`)" and add to `## Unknown` that no source in this entry establishes they are the framework's `android:versionCode`/`android:versionName` ids; alternatively open an AOSP framework attribute-id row and cite it (an evidence upgrade, not a text patch).

## F3 — cross-lane note cites S043 beyond that row's anchor and declared scope

- entry:2 (S043 row): scope is "route-scope sentences only: what the `inspect_android_package` family is documented to take and return … anchor: … **lines 7-8**".
- entry:166 (Q10 note): "The provider route (`inspect_android_package`, **JADX prerequisites**) is documented scope from S043 only".

Verified anchor content:

```
$ awk 'NR>=7 && NR<=8' .ufo/waves/round-65/source-snapshots/rea-android-applications.md
Start with `inspect_android_package` on the caller's APK path for package
identity, manifest declarations, coverage, and inline Evidence. Use
$ grep -n -i jadx .ufo/waves/round-65/source-snapshots/rea-android-applications.md
16:The provider requires a separately supplied headless JADX MCP JAR 0.7.1 and
17:Java 17 or newer. …
```

The JADX prerequisite sentence is at snapshot:16-17 — outside the cited anchor (7-8) and outside the row's declared "take and return" scope. The Q10 obligation ("contested cross-lane scope is reported, not absorbed") is satisfied in form — the note reports rather than absorbs — but the reported content is attributed to a row that does not cover it. Smallest safe correction: cite snapshot lines 16-20 for the prerequisite clause and widen the S043 scope sentence to "take/return and host prerequisites", or delete "JADX prerequisites" from entry:166.

## F4 — Limitations block omits three premises its own Q10 row leans on

`## Limitations` (entry:162) correctly states: one authored fixture; one manifest shape (single element, three attributes, no nesting/CDATA/styles); UTF-8 string pool only; ZIP_STORED, no data descriptors; dex member is a header only and not a valid dex program; generalization needs its own evidence. That covers the brief's one-fixture / one-shape / UTF-8 / ZIP_STORED / dex-header axes. Missing:

1. **No ZIP64 path.** The EOCD walk is the classic 22-byte record only — `corpus/fixtures/apk-r65/readout.py:76-86`: `rfind(b"PK\x05\x06")`, `size` at +12, `cd_off` at +16, `entries` at +10, no EOCD64 locator, no central-directory-64. A ZIP64 archive is a different record stream; item 2's `737 + 188 == 925` and item 3's cursor-equality assertion are properties of a classic single-disk, uncompressed archive and are not stated as such. (`screen: 947 - 925 = 22`, so no archive comment either — also unstated.)
2. **Resource-map identity unestablished** (F2) is not carried into Limitations/Unknown.
3. **Struct widths are hand-entered literals, not a snapshot derivation** — see F5.

## F5 — item 5's "computed … from S038's own struct definitions, not assumed" overstates the artifact

- entry:59: "The fixed structure widths used by the readout are computed by summing the field widths of S038's own struct definitions (two `uint16` plus one `uint32` for `ResChunk_header`; five `uint32` after the chunk header for `ResStringPool_header`; and so on), **not assumed**"; entry:13 repeats "computed from S038's own struct field lists in item 5 below".
- The artifact: `corpus/fixtures/apk-r65/readout.py:52-59` is a literal `widths = { … }` of integer lists; `:60` `sum(w)` sums *those literals*; `:62` emits the constant string `source_anchor="S038 ResourceTypes.h struct field lists"`. The only file the script reads is the APK (`:44 apk = APK.read_bytes()`; `grep -n "open(\|ResourceTypes"` returns comments only). No command compares the literals to the snapshot.

The literals are in fact faithful to the snapshot (spot-checked: `ResChunk_header` 2+2+4 at :218-222; `ResStringPool_header` = chunk header + five `uint32` = 28 at :461-480; `ResXMLTree_node` 16 at :621; `ResXMLTree_attrExt` 20 at :677; `ResXMLTree_attribute` 20 at :707; `Res_value` 8 at :287) — so this is the Q11 "recorded presented as re-derived" pattern, not a wrong value. Smallest safe correction: label item 5 "widths hand-transcribed from S038's field lists into `readout.py:52-59`; the command sums the recorded widths", or extend `derive_axml_anchors.py` to print each struct's field-type list from the snapshot so the claim becomes checkable.

## F6 — cited/derived line 253 lies outside S038's registered anchor range

`corpus/SOURCES.md:52` registers S038's anchor as "chunk-type enum **:239-250**"; the entry cites `RES_XML_RESOURCE_MAP_TYPE` :253 at entry:57 and derives 253 in item 11 (253 > 250). The row's *scope* ("chunk-type enum values … this tag only") covers it, so this is a registry-anchor width defect, not a tier defect. Smallest safe correction: widen the S038 anchor list to `:237-253` in `SOURCES.md` (registry owner), or drop the `:253` label — the readout prints `type: 384`, so the enum name is not load-bearing.

## Axes the entry does hold (checked, not assumed)

| axis from the brief | evidence |
|---|---|
| one authored fixture | readout reads only `corpus/fixtures/apk-r65/fixture.apk` (`readout.py:44`); 15-line stdout sha256 `507d…d247` matches entry:7; items 1-10 are byte values of those 947 bytes. Exception: F2's framework-identity sentence. |
| one manifest shape | entry:162 ("a single element with three attributes… no CDATA, no nested elements, no styles"); chunk table entry:53-55 shows one start/end element and one namespace pair, all `lineNumber` 1. |
| UTF-8 string pool only | entry:63 output `"flags": "0x00000100"`, `"utf8": true`; test at `readout.py:166` (`flags & 0x100`); UTF-16 pools not exercised and the limitation says so. |
| ZIP_STORED | entry:162 ("ZIP_STORED with no data descriptors"); compressed == uncompressed per member (416/416, 112/112, 69/69 in item 3). Caveat: F4.1 (no ZIP64). |
| dex header only | entry:162 ("a header only and is intentionally not a valid dex program"); item 9 claims declared-field agreement with S045, explicitly "the dex header's declared checksum, signature, size and endian fields agree with S045's declared field semantics **for this one member**" (entry:157). |
| manual standard-library analysis | entry:13 labels the analysis manual; readout uses `struct`/`hashlib` only and calls no producer. Caveat: F5 (spec-derived widths are transcribed literals). |
| no provider call | entry:13 "no producer is called"; entry:158; entry:166 "this lane ran no provider and makes no readiness claim (Q05 fence)". Holds in substance; F3 is the anchor defect on the report sentence. |
| cross-lane contested scope | entry:166 keeps kaidoku/revenger ADJ-06 and fleet `l0-questions.md:42` reported-not-absorbed, unchanged from round 64. Holds. |

Item 11's block is itself internally consistent with the frozen derivation output (`derive_axml_anchors.py` exit 0, 17 lines, snapshot sha pinned and matching), and the entry's headline `:245` correction is correct — the defect is the two line numbers the entry states *beside* the derived ones while claiming they are all derived.

## Impacted axes

- **Q10** — the self-grade at entry:181 ("pass") is wrong on F2 (framework identity from one authored fixture) and F4 (limitations do not name the ZIP64/rg-id/width-transcription premises); entry:166 also over-attributes its route sentence (F3).
- **Q11** — F1 (237/244 stated as machine-derived), F5 (widths stated as derived from S038 while hand-transcribed).
- **Q13** — F1: `derive_axml_anchors.py` is credited with guarding clauses (237, 244) its own run does not detect; deleting those literals from the script would not change a single derived line.
- **Q01/Q02 (adjacent, other seats' axis)** — F3 anchor scope and F6 anchor range; also, S032/S034 are load-bearing for item 3 but appear only in body prose (entry:13) and the Q-map (entry:172), not in the `source:` header block (F6 is the same class for S038's anchor width).
- **Q03** — F2's "correspondence" is between the fixture and its own authored oracle.

## Smallest safe corrections (no fixture bytes, no counter, no readout change)

1. entry:1/:4/:125/:148/:156/:182 + `SOURCES.md:61`: either delete the universal ("every line number"), or replace "lines 237-253" with the derived single anchor `:253` and drop the contrast sentence "line 244 is `RES_XML_FIRST_CHUNK_TYPE`" (both non-load-bearing), or add `RES_XML_FIRST_CHUNK_TYPE` and an enum-block-start search to `ENUMS` and re-capture the 19-line stdout — then the universal is true as written.
2. entry:75/:157: demote "framework attribute ids" to "the two non-zero resource-map ids the authored oracle declares", and put the framework identity in `## Unknown`; or open an AOSP framework attribute-id row.
3. entry:166: cite snapshot lines 16-20 for "JADX prerequisites" and widen S043's scope, or remove the phrase.
4. entry:162: add "classic 22-byte EOCD only — no ZIP64/EOCD64 and no archive comment exercised (`readout.py:76-86`)" and "struct widths are hand-transcribed literals (`readout.py:52-59`), not snapshotted".
5. entry:59/:13: relabel item 5 as recorded-from-S038 rather than computed-from-S038 (or make the widths derivable from the snapshot).
6. `SOURCES.md:52`: widen S038's anchor to `:239-253` (or drop the `:253` citation).

Effects: no fixture byte, no readout line, no frozen `reports/round-68/measure.py` digest, and no C1 artifact is touched by any of these; items 1-10 and the `507d…d247` recheck survive unchanged. Until 1 and 2 are fixed, the Q10 and Q11 rows at entry:181-182 must not stand as `pass`.

## Tooling

No install or upgrade was performed or needed; pacman is paused host-wide per the orchestrator ruling and nothing here required it. All evidence above was produced with the repo's own scripts plus `python3 -B`, `sha256sum`, `grep`, `awk`, `nl`.
