FAIL — Q07, single sentence: entry:91 states a namespace-resolution *mechanism* the readout does not implement (readout.py:211 resolves `ns` as `strings[ns_index]`, never through the start-namespace chunk) and attributes `0xffffffff` to attributes whose bytes carry `0`; the trailing "not a prediction about any other parser" fence does not repair a false observation of this readout.

seat: L1Revenger69.R69ReviewEntryQ07 · criterion: Q07 only · target:
`corpus/knowledge/round-69-apk-axml-byte-evidence.md` (215 lines, sha256
`c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`) ·
`admission-status: candidate` · judged on the landed v4 bytes, no edit made.

## Criterion as registered (`corpus/QUALITY.md` Q07)

> A predicted parser behavior (accept, refuse, cause) is a pre-registered hypothesis
> with spec-derived ground truth and is recorded whichever way it falls. A cause is
> stated only once independently reproduced.
> **reject when**: a prediction is written as fact, or an unreproduced cause is used
> as support.

Assignment sub-test: the namespace-resolution sentence must read as an observation
of this readout on this fixture, not a prediction about other parsers.

## R1 — the entry's own commands reproduce byte-identically (baseline is sound)

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/revenger-r69-q07-full.out
exit=0
15 /tmp/revenger-r69-q07-full.out
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/revenger-r69-q07-full.out
```

```
$ python3 -B corpus/derive_axml_anchors.py
exit=0 ; wc -l => 20
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
...
enum block open : 237
enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
...
enum block close : 263
comment attributeStart : 686
field attributeStart : 687
```

Both match the entry's `recheck:` claim (15 lines / `507d79f8…`) and item 11's
20-line block exactly, and the pinned hashes hold:

```
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py   (= S047)
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h (= S047/S038)
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
```

So the Q07 failure below is **not** transcription drift (M39 class). It is a prose
claim about the instrument that the instrument's own source contradicts.

## R2 — the offending bytes: `entry:91` (item 8)

```
The `0xffffffff` namespace index on `package` and the element itself is recorded as
observed and treated as null by the readout (readout.py:22); the same constant on
`android`-carrying attributes is resolved by this readout through the start-namespace
chunk at offset 248, which states prefix index 0 (`android`) and URI index 1
(`http://schemas.android.com/apk/res/android`) — an observation of how this readout
resolves this fixture's bytes, not a prediction about any other parser:
```

Two defects, both inside the clause that calls itself "an observation of how this
readout resolves this fixture's bytes".

### Defect 1 — "the same constant on `android`-carrying attributes" is not in the bytes

Byte re-derivation over the AXML payload (`payload_offset` 49, length 416; chunk base
272; `attributeStart` 20, `attributeSize` 20, count 3 — offsets `base+16+20+i*20`, the
same formula readout.py:203 uses):

```
$ python3 -B -   # struct.unpack_from("<III", axml, off) per attribute
payload_len 416 element_ns_index 4294967295 attributeStart 20 attributeSize 20 count 3
attr0 off=308 ns_index=4294967295 (0xffffffff) name_index=3 raw_index=4   # package
attr1 off=328 ns_index=0 (0x00000000) name_index=5 raw_index=7            # versionCode
attr2 off=348 ns_index=0 (0x00000000) name_index=6 raw_index=8            # versionName
start_ns prefix_index 0 uri_index 1  end_ns prefix_index 0 uri_index 1
```

The command the entry itself prints agrees:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_element
... {"name": "package", ..., "ns": null, "ns_index": 4294967295, ...},
    {"name": "versionCode", ..., "ns": "android", "ns_index": 0, ...},
    {"name": "versionName", ..., "ns": "android", "ns_index": 0, ...} ...
```

Only `package` (and the element, `element_ns_index` 4294967295) carry
`0xffffffff`. The two `android`-carrying attributes carry **`ns_index` 0**. The
stated value `0xffffffff` on android-carrying attributes is printed by no command and
is contradicted by every one of them. Correct value: `ns_index` **0** on both
`android` attributes (and `0xffffffff` only on `package` and on the element).

### Defect 2 — the stated resolution path is a cause the readout never performs

`readout.py` in full — the only mentions of prefix/uri in the instrument:

```
$ grep -n "prefix\|uri\b\|uri_index\|ns_table\|namespace" corpus/fixtures/apk-r65/readout.py
178:    for label, ctype in (("start_namespace", 0x0100), ("end_namespace", 0x0101)):
180:        prefix = u32(axml, ch["offset"] + 16)
181:        uri = u32(axml, ch["offset"] + 20)
183:             prefix_index=prefix, prefix=strings[prefix],
184:             uri_index=uri, uri=strings[uri])
```

The start-namespace chunk is read into its **own** fact (`axml_start_namespace`,
:178-184) and then dropped. The attribute path is:

```
$ sed -n '203,217p' corpus/fixtures/apk-r65/readout.py
203:        aoff = base + 16 + attribute_start + i * attribute_size
204:        ans = u32(axml, aoff)
...
210:        attrs.append({
211:            "ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],
```

with `NO_INDEX = 0xFFFFFFFF` at `readout.py:22`. So the readout resolves an
attribute's `ns` by **direct string-pool indexing** (`strings[ans]`), and for
`ans == 0` that is `strings[0]` = the literal string `android` (string pool:
`"offsets": [0, 10, 55, …]`, `"strings": ["android", …]`; `strings` is appended in
index order at readout.py:155-163). The URI
`http://schemas.android.com/apk/res/android` is **never** used to resolve any
attribute; it appears only in the separate namespace fact. There is no
prefix→URI table, no lookup, and no consultation of offset 248 on the attribute
path — `grep` finds no other occurrence.

Correct statement: `versionCode`/`versionName` carry `ns_index` **0**, which the
readout reports as the string-pool entry at index 0 — the literal `android` (a
prefix string, not a URI) — via `strings[ans]` (readout.py:211). The
start-namespace chunk at 248 (`prefix_index` 0, `uri_index` 1) is emitted as its own
fact and is **not** consulted by the attribute path; the prefix/URI pairing is an
observation of two facts printed side by side on this fixture, not a resolution the
readout performs.

### Why this is Q07 and not merely a Q11 numeric slip

The sentence is a **mechanism claim** ("resolved … through the start-namespace
chunk"), i.e. a *cause* in the criterion's sense, offered as support for item 8's
namespace narrative. It was never reproduced: the independent reproduction
(`grep` + `sed` on the instrument, plus the raw attribute bytes above) contradicts
it. Q07's reject condition — "an unreproduced cause is used as support" — is met
exactly. The assignment's sub-test is also met: the sentence does **not** read as an
observation of this readout on this fixture, because the observation it states is
false of this readout.

Note the two readings, both failing: if "the same constant" = `0xffffffff`, Defect 1
kills it; if it is read loosely as "index 0", Defect 2 still kills it (no
start-namespace consultation exists). There is no reading under which the clause is
true.

The half of the clause that *is* satisfied: the anti-generalization fence ("not a
prediction about any other parser") is present, and no accept/refuse prediction about
other parsers appears anywhere in the entry. The only sentences that mention parser
scope at all are the fences at :4 (`no ZIP-parser or provider behavior is claimed`),
:10 (`general AXML or ZIP-parser behavior beyond this fixture`), :77 (`no
framework-wide semantics for a zero entry is claimed from this fixture`) and the Q07
row at :181; the only mechanism attribution is :91. The
v4 repair named in `reports/round-69/claims.md` §C1 item 6 added that fence but left
the false mechanism and false constant in place — a scoping clause does not convert
a wrong observation into an observation.

## Implicated entry lines

- **:91** (item 8, second paragraph) — the two defects above. **This is the FAIL.**
- **:181** (Q-map row) — `| Q07 | pass | no parser-behavior prediction is made or
  needed; … the namespace-resolution sentence is explicitly scoped to how this
  readout resolves this fixture (item 8). |` — not accepted as evidence per the
  assignment, and its basis is contradicted by readout.py:211. Must be rewritten
  after :91 is corrected; "scoped to how this readout resolves" is precisely the
  claim that fails.
- :84-96 (item 8) is otherwise clean: `attributeStart` 20 / `attributeSize` 20 /
  count 3 / `manifest` / `element_ns` null and the attrExt provenance (line 677,
  686, 687) all reproduce against the emitted output and the 20-line derivation.

## Smallest safe correction

1. Rewrite entry:91's second clause (everything after "readout.py:22)") to:

   > the two `android`-carrying attributes carry namespace index **0**, which this
   > readout reports as the string-pool entry at that index — `strings[0]` =
   > `android` (readout.py:211) — while the start-namespace chunk at offset 248
   > (`prefix_index` 0, `uri_index` 1) is emitted as its own separate fact
   > (readout.py:178-184) and is not consulted on the attribute path; the
   > prefix/URI pairing is therefore an observation of two printed facts on this
   > fixture, not a resolution this readout performs and not a prediction about any
   > other parser.

2. Rewrite the :181 Q07 basis to the corrected observation (drop "explicitly scoped
   to how this readout resolves this fixture" as if scoping alone discharged the
   criterion; name the corrected mechanism).
3. No fixture, oracle, readout or derivation bytes need to change — the values are
   already printed correctly; only the prose and the Q-map row misstate them.

## Axis impact

- **coverage (C1)** — `reports/round-69/claims.md` §C1 frozen predicate requires
  "every applicable Q01–Q15 decision of the dispatched wave on the landed v4 bytes is
  PASS". A Q07 FAIL on the v4 bytes triggers the **kill rule**: C05 stays
  `uncovered`, the v4 entry is marked `admission-status: rejected` (retained as
  evidence, every other byte kept), and C1 is reported **FALSIFIED** — honest stop,
  no repaired acceptance condition. Ground K remains 8/14.
- **calibration (C2/Q15)** — untouched by this finding; Q15's own predicate set is a
  separate claim and this seat makes no statement about it.
- Not in scope here and not judged: Q04/Q05/Q11/Q13/Q14 on this entry (other seats),
  the counter labels, the C7 gate.

## Reproducibility of this review

Read-only throughout: two `python3 -B` runs (readout, derivation), one inline
`python3 -B` byte read of `fixture.apk` (no write), `grep`/`sed`/`sha256sum` on the
lane tree. No file in the lane was created, edited or staged; no git command that
writes was run. Scratch `/tmp/revenger-r69-q07-*` deleted before return. No tool was
installed or upgraded (none needed).
