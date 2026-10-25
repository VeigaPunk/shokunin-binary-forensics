#!/usr/bin/env python3
"""Build corpus/knowledge/round-67-apk-axml-byte-evidence.md for revenger r67.

Runs the fixture readout NOW and splices its actual stdout lines into the
entry verbatim (the M39 discipline: never transcribe command output by hand).
Writes only the entry file; fixture bytes are read-only. Scratch tool, not
committed corpus material (the committed artifact is the entry it emits).
"""
import hashlib
import subprocess
import sys
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/revenger-shokunin")
OUT = LANE / "corpus/knowledge/round-67-apk-axml-byte-evidence.md"


def run(*args):
    p = subprocess.run([sys.executable, "-B", *args], cwd=LANE,
                       capture_output=True, text=True, check=True)
    return p.stdout.rstrip("\n").splitlines()


full = run("corpus/fixtures/apk-r65/readout.py")
full_sha = hashlib.sha256(("\n".join(full) + "\n").encode()).hexdigest()
fact = {}


def fact_block(fact_id):
    lines = run("corpus/fixtures/apk-r65/readout.py", "--fact", fact_id)
    assert len(lines) == 1, (fact_id, lines)
    fact[fact_id] = lines[0]
    return f"$ python3 -B corpus/fixtures/apk-r65/readout.py --fact {fact_id}\n{lines[0]}"


for fid in ("archive", "eocd", "member[AndroidManifest.xml]", "member[classes.dex]",
            "member[META-INF/MANIFEST.MF]", "axml_chunk_table", "spec_derived_struct_widths",
            "axml_string_pool", "axml_resource_map", "axml_start_element",
            "axml_start_namespace", "axml_end_element", "axml_end_namespace",
            "dex_declared_header", "jar_manifest"):
    fact_block(fid)

full_lines = "\n".join(f"$ python3 -B corpus/fixtures/apk-r65/readout.py\n{l}" for l in full[:1])
full_block = "$ python3 -B corpus/fixtures/apk-r65/readout.py\n" + "\n".join(full)

entry = f"""source: S038 — AOSP `ResourceTypes.h` (binary resource/XML format structures) — https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h (spec, tier A; row mined round 65, **re-opened 2026-10-24 by this entry's author** from the committed snapshot) — scope: the field layout, chunk-type enum values and fixed struct sizes of the compiled-XML (AXML) chunk stream for one authored binary `AndroidManifest.xml` — anchors: `struct ResChunk_header` (line 218); chunk-type enum block **lines 237-253**: `RES_STRING_POOL_TYPE` :239, `RES_XML_TYPE` :241, `RES_XML_START_NAMESPACE_TYPE` :244, `RES_XML_END_NAMESPACE_TYPE` :246, `RES_XML_START_ELEMENT_TYPE` :247, `RES_XML_END_ELEMENT_TYPE` :248, and `RES_XML_RESOURCE_MAP_TYPE` :253 (0x0180 — inside the enum block, unlike the round-65 draft's :239-250); `struct ResStringPool_header` (line 461); `struct ResXMLTree_header`/`ResXMLTree_node` (lines 612, 621); `struct ResXMLTree_attrExt` (line 677; its `attributeStart` field comment "Byte offset from the start of this structure where the attributes start." at lines 685-687); `struct ResXMLTree_attribute` (line 707); `struct Res_value` (line 287); pinned tag `android-15.0.0_r1`; snapshot `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` sha256 `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, 86255 bytes
source: S043 — supersedes S039 — REA reverse-engineer-anything skill reference, "Android application artifacts" (docs, tier A; row mined round 66) — route-scope sentences only: what the `inspect_android_package` family is documented to take and return per rea-agents-6.5.0; not provider execution and not the fixture bytes — anchor: snapshot `.ufo/waves/round-65/source-snapshots/rea-android-applications.md` **lines 7-8** ("Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence."), sha256 `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c` — the round-65 draft cited "line 5", which is `older server.`
source: S045 — Android DEX format specification (AOSP, source.android.com) — https://source.android.com/docs/core/runtime/dex-format (docs, tier A, **opened 2026-10-24 by this entry's author**) — scope: the declared `header_item` field semantics of one authored `classes.dex` member (magic, checksum, signature, file_size, header_size, endian_tag); not dex program validity — anchor: "File layout" → `header_item` field table: checksum "adler32 checksum of the rest of the file (everything but magic and this field)"; signature "SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)"; header_size "must be 0x70 (112) bytes (v40 or earlier)"; `ENDIAN_CONSTANT = 0x12345678`; snapshot `.ufo/waves/round-67/source-snapshots/dex-format.html` sha256 `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`, 281157 bytes
source: S041 — Authored apk-r65 bundle — `corpus/fixtures/apk-r65/fixture.apk`, `corpus/fixtures/apk-r65/truth.json`, `corpus/fixtures/apk-r65/generator.py`, `corpus/fixtures/apk-r65/readout.py` (own-work, tier A; row mined round 65) — scope: the byte content of this one authored fixture, its declared oracle and its readout script, at the round-65 claim tree (bytes unchanged since) — anchors: fixture sha256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` (947 bytes), truth.json sha256 `27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173`, readout.py sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`
verified-at: 2026-10-24 (round-67 re-derivation; the fixture, oracle and readout bytes are the round-65 claim-tree bytes, unchanged since `c7b7cf98`; every output line below was captured from the named command's actual stdout at build time, never transcribed by hand — the round-65 draft's entry:41 transcription drift is the M39 class this entry repairs)
recheck: `python3 -B corpus/fixtures/apk-r65/readout.py` from the lane root — exits 0 and prints 15 stdout lines whose SHA-256 is `{full_sha}` (re-derived 2026-10-24 at this entry's build); the per-value form `python3 -B corpus/fixtures/apk-r65/readout.py --fact '<id>'` prints the single JSON line for one named fact. The stdout carries only repo-relative paths, never the extraction root.
coverage-map: C05 (`corpus/README.md`, Android packages (APK)) — the container members, the binary-AXML `AndroidManifest.xml` and the `classes.dex` declared header of one authored APK fixture, read out byte by byte against the authored oracle. Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture.
admission-status: candidate — round-66 routed re-gate of the falsified round-65 candidate (repairs are text-level only: entry:41 hex pair, S038 enum anchor to :253, S043 route anchor lines 7-8, item-8 provenance sentence, item-9 dex spec row S045, Q08 Q-map row, dangling `### Code` pointer removed); the dispatched round-67 wave's named fresh seats decide Q01–Q13 on these bytes; the README C05 row flips only on an all-criteria pass (`reports/round-67/claims.md`)

# Binary AXML manifest, container members and dex declared header of one authored APK — C05

Scope. One authored APK, `corpus/fixtures/apk-r65/fixture.apk`, and the authored oracle that declares it, `corpus/fixtures/apk-r65/truth.json`. The analysis is **manual**: a Python standard-library script reads the archive's bytes with `struct` and walks the ZIP central directory, the compiled-XML chunk stream, and the dex header directly. Nothing is extracted to disk, nothing is executed, no producer is called, no network is used, and no verifier source is read. The ZIP container field offsets are the APPNOTE 6.3.10 fixed record widths already mined as S032 (central directory header) and S034 (local file header); the AXML field offsets are computed from S038's own struct field lists in item 5 below.

## Observation

Every numbered item below is produced by the readout in §Reproduce. The script is saved verbatim as `corpus/fixtures/apk-r65/readout.py` (sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`) and each block below shows the exact command with the output it printed at this entry's build.

**Archive and container**

1. The archive is **947 bytes** with SHA-256 `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, read from the file's bytes.

```
{fact_block("archive")}
```

2. The end-of-central-directory signature `504b0506` is located at file offset **925**; its record states **3** central-directory entries, a central directory of **188** bytes starting at offset **737**, and `737 + 188 == 925`, so the central directory ends exactly where the end-of-central-directory record begins.

```
{fact_block("eocd")}
```

3. Walking the three central-directory records (46-byte fixed part per S032 §4.3.12) and their local headers (30-byte fixed part per S034 §4.3.7) selects three members; every member's stated CRC-32 equals the CRC-32 recomputed over its payload bytes, and the walk's end cursor equals the end-of-central-directory offset. Each member's `payload_offset` is derived by the readout as `local_header_offset + 30 + name_length + extra_length` from the S034 §4.3.7 field list (readout.py:99-105), not assumed:

```
{fact_block("member[AndroidManifest.xml]")}
{fact_block("member[classes.dex]")}
{fact_block("member[META-INF/MANIFEST.MF]")}
```

The `META-INF/MANIFEST.MF` payload begins `4d616e69666573742d` — ASCII `Manifest-`, the 16-byte prefix of `Manifest-Version: 1.0` (the round-65 draft recorded a 15-byte `4d616e696673742d…` pair at its entry:41; the deriving command prints the 16-byte pair, which is the value above).

**Compiled XML (AXML) member**

4. The `AndroidManifest.xml` payload begins `0300 0800 a001 0000` — chunk type `0x0003` (`RES_XML_TYPE`), headerSize 8, total size **416**, equal to the member's uncompressed size. The child chunks are walked from offset 8 by adding each chunk's size, and the walk ends exactly at 416:

```
{fact_block("axml_chunk_table")}
```

The six chunk types in the table — `0x0001` string pool, `0x0180` resource map, `0x0100` start namespace, `0x0102` start element, `0x0103` end element, `0x0101` end namespace — are the values S038's chunk-type enum block names at **lines 237-253** (string pool :239, start/end namespace :244/:246, start/end element :247/:248, resource map `RES_XML_RESOURCE_MAP_TYPE` :253). The `headerSize` column — 28, 8, 16, 16, 16, 16 — equals the fixed struct sizes derived in item 5 for the string pool and the XML node chunks.

5. The fixed structure widths used by the readout are computed by summing the field widths of S038's own struct definitions (two `uint16` plus one `uint32` for `ResChunk_header`; five `uint32` after the chunk header for `ResStringPool_header`; and so on), not assumed:

```
{fact_block("spec_derived_struct_widths")}
```

The derived 20-byte `ResXMLTree_attrExt` size is the `attributeStart` value observed in the start-element chunk in item 8, and the derived 20-byte `ResXMLTree_attribute` size is the observed `attributeSize`.

6. The string-pool chunk (offset 8, size 196) declares **9** strings, **0** styles, flags **`0x00000100`** — bit `0x100` set, the UTF-8 flag position the readout tests (`flags & 0x100`, readout.py:166) — with string data starting 64 bytes into the chunk. The nine strings, decoded as length-prefixed UTF-8 from the offsets the pool states, are:

```
{fact_block("axml_string_pool")}
```

7. The resource-map chunk (offset 204, size 44) holds one `uint32` per string. Seven entries are `0x00000000` and the entries for `versionCode` and `versionName` are **`0x0101021b`** and **`0x0101021c`** — exactly the two framework attribute ids the fixture's authored oracle declares for those strings (`truth.json` `axml_declared.resource_ids`), which is the correspondence this entry claims; the all-zero entries are recorded as observed, and no framework-wide semantics for a zero entry is claimed from this fixture:

```
{fact_block("axml_resource_map")}
```

8. The start-element chunk at offset 272 names the element `manifest` with no namespace, `attributeStart` **20**, `attributeSize` **20**, `attributeCount` **3** — all equal to the derived sizes of item 5. Provenance of the attribute location: S038's `struct ResXMLTree_attrExt` (line 677) "Appears header.headerSize bytes after a `ResXMLTree_node`", so the attrExt starts at `chunk_base + 16` (the derived 16-byte node header, item 5); its `attributeStart` field is "Byte offset from the start of this structure where the attributes start" (snapshot lines 685-687), so attribute *i* is at `chunk_base + 16 + attributeStart + i * attributeSize` — the readout's own derivation (readout.py:200-203). The three attributes read there are `package="com.example.r65"` (typed `0x03` string), `android:versionCode=1` (typed `0x10` int, resource id `0x0101021b`) and `android:versionName="1.0"` (typed `0x03` string, resource id `0x0101021c`):

```
{fact_block("axml_start_element")}
```

The `0xffffffff` namespace index on `package` and the element itself is recorded as observed and treated as null by the readout (readout.py:22); the same constant on `android`-carrying attributes resolves instead through the start-namespace chunk at offset 248, which states prefix index 0 (`android`) and URI index 1 (`http://schemas.android.com/apk/res/android`):

```
{fact_block("axml_start_namespace")}
```

The end-element chunk (offset 368) names `manifest` again, and the end-namespace chunk (offset 392) closes the same prefix/URI pair; all four node chunks carry `lineNumber` 1:

```
{fact_block("axml_end_element")}
{fact_block("axml_end_namespace")}
```

**dex declared header**

9. The `classes.dex` payload's first eight bytes are `6465780a30333500` — the magic `dex\\n035\\0`. Its declared checksum **`0x3d120c30`** equals the Adler-32 recomputed over the bytes from offset 12 on — S045's `header_item` table declares the checksum "adler32 checksum of the rest of the file (everything but magic and this field)" — and its declared 20-byte signature equals the SHA-1 recomputed over the bytes from offset 32 on (S045: "SHA-1 signature (hash) of the rest of the file (everything but magic, checksum, and this field)"). The header's declared `file_size` and `header_size` are both 112 — S045: `header_size` "must be 0x70 (112) bytes (v40 or earlier)" for this `035` magic — and the endian tag is `0x12345678`, S045's `ENDIAN_CONSTANT`. These are declared-header self-consistency facts about one inert member; dex validity is not claimed:

```
{fact_block("dex_declared_header")}
```

**Text manifest**

10. The `META-INF/MANIFEST.MF` payload is 69 bytes of ASCII whose first line is `Manifest-Version: 1.0` with one blank-line-separated section:

```
{fact_block("jar_manifest")}
```

## Comparison with the authored oracle

The oracle `truth.json` declares the image digest and size, the three members with their measured offsets, sizes and CRC-32 values, the declared AXML string table, attribute table and resource-map ids, and the build recipe. The readout values agree with it on every shared field: image sha256 and size (item 1), the three members' local-header offsets, payload sizes and CRC-32 values (item 3), the nine strings, the three attribute rows and the two non-zero resource ids (items 6-8). Regenerating the fixture from `generator.py` in a scratch directory on this host was round-65 evidence (S041) and is not re-run by this entry; the committed bytes are hash-pinned above.

## Observation / inference / unknown

- **Observation** — every value in items 1-10: read directly from the committed bytes by the §Reproduce script, which runs with the Python standard library only.
- **Inference** — that the six AXML chunk types and three fixed `headerSize` values are the ones S038's enum block (lines 237-253) and struct field lists name and size; that the two non-zero resource-map entries are the framework `versionCode`/`versionName` ids the fixture generator declared (`truth.json`); that the dex header's declared checksum, signature, size and endian fields agree with S045's declared field semantics for this one member. Each inference cites its byte evidence and its registry anchor, and each is scoped to this fixture.
- **Unknown** — nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed; the fixture is inert and no producer was called.

## Limitations

One authored fixture, one manifest shape (a single element with three attributes), UTF-8 string pool only, no CDATA, no nested elements, no styles. The container is ZIP_STORED with no data descriptors, so the byte walk does not exercise split archives, spanned records or compression. The dex member is a header only and is intentionally not a valid dex program. Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence.

## Cross-lane scope note (Q10)

The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S043 only; this lane ran no provider and makes no readiness claim (Q05 fence). The kaidoku/revenger ADJ-06 overlap and fleet `l0-questions.md:42` remain reported-not-absorbed, unchanged from round 64.

## §Q-map

| criterion | decision | basis |
|---|---|---|
| Q01 | pass | every load-bearing layout claim rests on S038 (tier A for AXML scope; row mined r65, re-opened 2026-10-24 from the committed snapshot by this entry's author) for AXML scope; the dex declared-header claims rest on S045 (tier A, opened 2026-10-24 this round); route scope rests on S043 (tier A, mined r66); container offsets rest on S032/S034 (registry tier A, mined round 63) and the fixture's own bytes (S041, own-work tier A). No tier-C support. |
| Q02 | pass | header carries `source:` (S038, S043, S045, S041 with URLs/paths, pinned anchors and snapshot digests), `verified-at:`, `recheck:` (command plus stdout SHA-256 re-derived at build), and names coverage row C05. |
| Q03 | pass | expected values come from the authored oracle, from S038-derived struct widths, and from S045's declared field semantics — all fixed outside the record under test; nothing is copied from a saved producer record. |
| Q04 | pass | no tool claim: the readout is manual standard-library byte analysis, labeled manual; the only tool named is Python itself, used as the reader, not credited with a result. |
| Q05 | pass | no readiness or capability claim is made; §Cross-lane scope note fences the provider route to S043 documentation scope. |
| Q06 | pass | every fixture premise was byte-verified against the built fixture in round 65 (S041, readout re-derived at this entry's build); the generator is not re-run by this entry and the committed bytes are hash-pinned. |
| Q07 | pass | no parser-behavior prediction is made or needed; the readout describes observed bytes only. |
| Q08 | superseded by Q11 | QUALITY.md:23 — Q08 is historical; this map applies Q11 (applying Q08 instead would itself be a Q11 failure, round-66 adjudication table). |
| Q09 | pass | digests are claimed only for the exact bytes hashed; no origin, completeness or authenticity claim; the dex checksum/signature self-consistency is explicitly an inert declared-header property, not validity. |
| Q10 | pass | scope is one fixture, one operation (manual readout), one artifact version; the §Limitations and §Cross-lane scope note name what is not claimed. |
| Q11 | pass | every count, offset, identifier and digest carries its deriving command and output in §Observation (items 1-10); the fixed struct constants carry their S038 field-list derivation (item 5); the attribute location carries its attrExt-relative provenance (item 8); every embedded output line was captured from the command's actual stdout at build time. No recorded value is presented as re-derived. |
| Q12 | n/a | no rejected source row is written by this entry. |
| Q13 | n/a by construction | no verifier, recheck command, comparison tool or automatic checker is credited or introduced beyond the entry's own readout recheck, and no value is presented as covered by any other check. |

## Reproduce

From the lane root, with the round-65 corpus tree (bytes unchanged through round 67):

```sh
python3 -B corpus/fixtures/apk-r65/readout.py
```

Exit 0; 15 stdout lines; their SHA-256 is `{full_sha}` (re-derived 2026-10-24). Single-fact form: `python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd`. The script is saved verbatim as `corpus/fixtures/apk-r65/readout.py` (sha256 `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976`) and reads only `fixture.apk` beside it.

Full stdout as printed at this entry's build (every line also appears in the per-item blocks above):

```
{full_block}
```
"""

OUT.write_text(entry, encoding="utf-8")
print("wrote", OUT, len(entry), "bytes")
print("full stdout sha256", full_sha)
