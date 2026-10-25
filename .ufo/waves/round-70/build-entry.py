#!/usr/bin/env python3
"""Round-70 v5 entry generator (revenger L1). Renders
corpus/knowledge/round-70-apk-axml-byte-evidence.md. Every fenced `$ cmd` block is
produced by RUNNING the command and pasting its stdout: no embedded output line is
typed by hand (M39 class). Run from the lane root:

    python3 -B .ufo/waves/round-70/build-entry.py [--status candidate|admitted]
"""
import re
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "corpus/knowledge/round-70-apk-axml-byte-evidence.md"
RD = "python3 -B corpus/fixtures/apk-r65/readout.py"
EC = "python3 -B corpus/fixtures/apk-r65/entry_checks.py"
DERIVE = "python3 -B corpus/derive_axml_anchors.py"
STATUS = "candidate"
if "--status" in sys.argv:
    STATUS = sys.argv[sys.argv.index("--status") + 1]


def run(cmd):
    argv = shlex.split(cmd)
    p = subprocess.run([sys.executable, "-B", *argv[2:]], cwd=str(ROOT), capture_output=True, text=True)
    if p.returncode != 0:
        raise SystemExit(f"command failed ({p.returncode}): {cmd}\n{p.stderr}")
    return p.stdout.rstrip("\n")


def block(*cmds):
    parts = ["```"]
    for c in cmds:
        parts.append(f"$ {c}")
        parts.append(run(c))
    parts.append("```")
    return "\n".join(parts)


def sub(match):
    return block(*[c.strip() for c in match.group(1).split("&&")])


TEMPLATE = r"""source: S038 — AOSP `ResourceTypes.h` (binary resource/XML format structures) — https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h (spec, tier A; row opened 2026-10-24 and mined round 65; re-opened 2026-10-25 by this entry's author from the committed snapshot `corpus/snapshots/ResourceTypes.h`, digest printed in item 14) — scope: the struct layout and chunk-type enum values of the compiled-XML (AXML) chunk stream for one authored binary `AndroidManifest.xml`; not the behavior of any parser — anchors: every S038 line number and enum value this entry states is printed by the item-11 command, none is typed by hand
source: S049 — supersedes S043 — REA reverse-engineer-anything skill reference, "Android application artifacts" — https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md (docs, tier A; row opened 2026-10-25 by this entry's author, who re-fetched the raw file and compared it byte for byte with the committed snapshot `corpus/snapshots/rea-android-applications.md`, digest printed in item 14) — scope: the route-scope sentence only, what `inspect_android_package` is documented to take and return in that text; not provider execution and not the fixture bytes — anchor: the quoted sentence is located by the item-11 `--spec-quotes` command (first line 7)
source: S048 — supersedes S045 — Android DEX format specification (AOSP, source.android.com) — https://source.android.com/docs/core/runtime/dex-format (docs, tier A; row opened 2026-10-25 by this entry's author, who re-fetched the live page and compared it with the committed snapshot `corpus/snapshots/dex-format.html`, digest printed in item 14; the live page differs from the snapshot only in page-chrome lines) — scope: the declared `header_item` field semantics of one authored `classes.dex` member (checksum, signature, header_size, endian_tag); not dex program validity — anchors: the four quoted phrases are located by the item-11 `--spec-quotes` command; the `header_item` field table is under the heading "Items and related structures" and `ENDIAN_CONSTANT` under "Bitfield, string, and constant definitions"
source: S032 — PKWARE APPNOTE.TXT 6.3.10 — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row opened 2026-10-23 and mined round 63; re-opened 2026-10-25 by this entry's author from the committed snapshot copy `corpus/snapshots/APPNOTE.TXT`, digest printed in item 14; whether it still equals the upstream's current text is not claimed) — scope: the record layouts of §4.3.12 central directory file header and §4.3.16 end of central directory record for one authored ZIP archive, whose heading and field line numbers in the snapshot are printed by item 12; the field widths are MANUALLY transcribed in `corpus/fixtures/apk-r65/entry_checks.py` and the item-12 command sums them; no ZIP-parser or provider behavior is claimed
source: S034 — PKWARE APPNOTE.TXT 6.3.10 — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row opened 2026-10-23 and mined round 63, scoped re-open 2026-10-25 by this entry's author from the same snapshot) — scope: §4.3.7 local file header only: the fixed part and the file-name and extra-field length offsets the `payload_offset` derivation in item 3 rests on (item 12 prints the section's heading and field line numbers)
source: S047 — supersedes S046 — AXML anchor derivation (own-work, tier A; row opened 2026-10-25, round 69; re-opened 2026-10-25 by this entry's author by running it) — scope: the printed S038 line numbers and enum values listed in item 11, read from the pinned snapshot bytes; not the layout facts themselves, which rest on S038 — anchor: `corpus/derive_axml_anchors.py` and `corpus/snapshots/ResourceTypes.h`, digests printed in item 14
source: S041 — Authored apk-r65 bundle — `corpus/fixtures/apk-r65/fixture.apk`, `truth.json`, `generator.py`, `readout.py` (own-work, tier A; row opened 2026-10-24 and mined round 65) — scope: the byte content of this one authored fixture, its declared oracle and its readout script — anchors: the four digests printed in item 14, which also prints the digest of `entry_checks.py`; this entry does not re-run `generator.py`
verified-at: 2026-10-25 (round-70 build; every output block below was produced by running the command printed above it in this same build and pasting its stdout, by `.ufo/waves/round-70/build-entry.py` (outside `corpus/`; its digest is not claimed); the embedded-output gate `corpus/check_embedded_outputs.py --entry` and the lint `corpus/lint_entry.py --entry` both ran on the built bytes)
recheck: from the lane root, `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` (re-runs every `$` command below and requires every embedded line in its stdout; credited only for that clause), `python3 -B corpus/fixtures/apk-r65/readout.py` (item 15 prints its line count and digest) and the `entry_checks.py` flags named in items 2, 11-14 and 16-17
coverage-map: C05 (`corpus/README.md`, Android packages (APK)) — the container members, the binary-AXML `AndroidManifest.xml` and the `classes.dex` declared header of one authored APK fixture, read out byte by byte and compared field by field with the authored oracle. Not covered: install/signature verification, dex validity or execution, provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior beyond this fixture.
admission-status: {STATUS}

# Binary AXML manifest, container members and dex declared header of one authored APK — C05

Scope. One authored APK, `corpus/fixtures/apk-r65/fixture.apk`, and the authored oracle that declares it, `corpus/fixtures/apk-r65/truth.json`. The analysis is **manual**: a Python standard-library script reads the archive's bytes with `struct` and walks the ZIP central directory, the compiled-XML chunk stream and the dex header. No archive member is extracted or executed, nothing is fetched and no producer is called at recheck time (the recheck commands run only the committed standard-library scripts named below).

## Observation

Every numbered item is produced by the command printed above its output. The readout script `corpus/fixtures/apk-r65/readout.py` is saved verbatim; its digest is item 14's.

**Archive and container**

1. The archive is a single file whose size and SHA-256 the readout computes from its bytes:

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact archive }}

2. The end-of-central-directory record is located by the readout's search for the four signature bytes (`readout.py:76`, constant `b"PK\x05\x06"`); the second command (`entry_checks.py`) locates the same signature on its own and prints the four bytes at the offset it finds, which equals the readout's offset. The record states the central-directory entry count, size and start offset, and the readout compares the start plus the size with the record's own offset:

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd && python3 -B corpus/fixtures/apk-r65/entry_checks.py --eocd }}

3. The readout walks each central-directory record and its local header (record widths and field offsets are **recorded** from APPNOTE and checked against the readout source by item 12, not derived from the archive), reads each member's payload at `payload_offset = local_header_offset + 30 + name_length + extra_length` (`readout.py:105`) and recomputes its CRC-32:

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact member[AndroidManifest.xml] && python3 -B corpus/fixtures/apk-r65/readout.py --fact member[classes.dex] && python3 -B corpus/fixtures/apk-r65/readout.py --fact member[META-INF/MANIFEST.MF] }}

Item 10's command prints the `META-INF/MANIFEST.MF` member's first line; item 16's command prints the general-purpose flags and compression method of every record.

**Compiled XML (AXML) member**

4. The readout walks the child chunks from the root chunk's own `headerSize` by adding each chunk's `size`; the table below is what it printed. The numeric `type` values are decimal here: 1 is `0x0001`, 384 is `0x0180`, 256 is `0x0100`, 258 is `0x0102`, 259 is `0x0103` and 257 is `0x0101`:

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_chunk_table }}

Item 11 prints the S038 enum lines carrying those hexadecimal values. The value `0x0100` is shared in that block by `RES_XML_FIRST_CHUNK_TYPE` and `RES_XML_START_NAMESPACE_TYPE`, so the chunk at offset 248 is identified as the start-namespace chunk by the item-8 `axml_start_namespace` fact, not by its value alone; the other five correspondences are inferences from matching values, labeled so in the inference section.

5. The fixed structure widths the readout prints are a **manual transcription** of S038's struct field lists (`readout.py:51-58`), labeled manual and not read from `ResourceTypes.h` at run time; the readout prints the constants and their sums, and item 17's command checks that the literal read offsets in the readout source match sums of these widths:

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact spec_derived_struct_widths }}

The summed `attr_ext_attribute_start` 20 and `attribute_size` 20 are the values the start-element chunk states in item 8.

6. The string-pool chunk's header values and the strings the readout decodes from the offsets the pool states (`readout.py:155-168`; the UTF-8 flag position tested is `flags & 0x100`, `readout.py:166`):

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_string_pool }}

7. The resource-map chunk's printed size less its printed header size (item 4: 44 less 8) is 36 bytes, which is 9 times 4 — one `uint32` per string — and the readout prints the entries and the non-zero ones keyed by string (the array layout is S038's; its source line is not among the lines item 11 prints). The two non-zero ids are compared with the oracle's declared ids in item 13; the zero entries are recorded as observed and no meaning for a zero entry is claimed:

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_resource_map }}

8. The start-element chunk's printed `attributeStart`, `attributeSize` and `attributeCount` and its three attributes. Where the attributes are read: the readout computes `aoff = base + 16 + attribute_start + i * attribute_size` (`readout.py:203`), where `base` is the chunk's offset; the literal 16 equals the chunk's declared `headerSize` in item 4 and the `node_header_size` item 5 sums (an inference, labeled in the inference section). S038's comment on `attributeStart` (quoted and located by item 11) says the offset is counted from the start of the attrExt structure. The readout resolves each attribute's namespace prefix string by indexing the string pool directly with the attribute's own `ns_index` (`readout.py:211`, `strings[ans]`; `NO_INDEX` 0xFFFFFFFF at `readout.py:22` resolves to null). The start-namespace chunk is printed as a separate fact and the readout does not consult it when resolving attribute namespaces:

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_element && python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_start_namespace && python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_end_element && python3 -B corpus/fixtures/apk-r65/readout.py --fact axml_end_namespace }}

**dex declared header**

9. The `classes.dex` member's declared header values and their recomputations, exactly as the readout prints them (`readout.py:233-248`). The four declared fields S048's quoted phrases cover — checksum, signature, header_size and endian_tag (located by item 11) — are compared with those phrases; `magic`, `format_version`, `file_size` and `header_bytes` are printed without a quoted S045 phrase and no semantics are claimed for them. A match between a declared value and its recomputation shows the member's header is internally consistent, and nothing about dex program validity follows:

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact dex_declared_header }}

**Text manifest**

10. The `META-INF/MANIFEST.MF` member's byte count, first line and section count as the readout prints them:

{{ python3 -B corpus/fixtures/apk-r65/readout.py --fact jar_manifest }}

**Spec anchors and recorded layouts (machine-derived where stated)**

11. Every S038 line number and enum value this entry states is printed by the committed derivation, which searches the pinned snapshot bytes for each cited symbol; its credit is bounded to exactly the lines it prints (the output below is the complete set). The second command locates each quoted spec phrase (S038's `attributeStart` comment, S049's route sentence, four S048 phrases) in its committed snapshot copy, tags stripped and whitespace folded, and prints the raw line the phrase's first words start on:

{{ python3 -B corpus/derive_axml_anchors.py && python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes }}

12. The ZIP field offsets the readout uses are summed here from the **manually transcribed** APPNOTE field widths (`entry_checks.py`, `LOCAL_HEADER`, `CENTRAL_HEADER`, `EOCD`) and each is compared with the literal in the readout source; the last three lines print where each record layout sits in the snapshot (heading line and the first and last transcribed field lines). The widths are recorded, the sums, the line numbers and the presence checks are derived:

{{ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout }}

13. The readout's facts compared with the authored oracle `truth.json`, which `generator.py` emits; the comparison covers the image digest and size; per member the local-header offset, compressed size, uncompressed size, CRC-32 and SHA-256; the AXML strings and resource ids; and per attribute the name index, namespace index, raw-value index, data type and data. The oracle's `image.path` and member `name` values are used as keys and not compared, and member `method` is compared by item 16's command. The oracle's AXML values are the generator's own build declaration, so agreement shows the readout parses what the generator wrote; it does not show that a declared value (for example the two resource ids) is the Android framework's value for its name. One line per compared field, every line printed:

{{ python3 -B corpus/fixtures/apk-r65/entry_checks.py --oracle }}

14. Digests and sizes of the ten files under `corpus/` that the commands above read, recomputed from bytes, including the script that prints items 2 and 11-17 (a digest identifies exactly these bytes; it does not establish who produced them, that a copy was faithfully fetched, or that it is the upstream's current text):

{{ python3 -B corpus/fixtures/apk-r65/entry_checks.py --pins }}

15. The readout's complete stdout, counted and hashed:

{{ python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest }}

16. The general-purpose flags and compression method of every local and central record, read from the archive bytes and compared with the oracle's declared method:

{{ python3 -B corpus/fixtures/apk-r65/entry_checks.py --container }}

17. The AXML field offsets the readout source uses, compared with sums of a second manual transcription of S038's struct widths (itself compared with the widths the readout prints):

{{ python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout }}

## Observation / inference / unknown

- **Observation** — every count, offset, identifier and digest in items 1-17 is printed by the command above it from the committed bytes. Items 3, 5, 12 and 17 depend on manually transcribed widths, each labeled where it is used; the `readout.py:N` line citations are source locators checked by reading the file, and the literals they concern are compared in items 12 and 17.
- **Inference** — (a) a printed chunk `type` value equals the value of the S038 enum line item 11 prints for the named constant; (b) the literal 16 in `readout.py:203` is the start-element chunk's declared `headerSize` (item 4) and the summed node width (item 5); (c) the two non-zero resource-map entries are the two ids `truth.json` declares (item 13); (d) the dex header's declared checksum, signature, size and endian fields agree with S048's field semantics as quoted. Each inference cites its byte evidence and is scoped to this fixture.
- **Unknown** — nothing about install validity, signature blocks, dex program validity or any provider's behavior is claimed; the fixture is inert and no producer was called. The ZIP APPNOTE layouts are recorded from a snapshot; whether the upstream document has since changed is not checked.

## Limitations

One authored fixture, one manifest shape (a single element with three attributes), UTF-8 string pool only, no CDATA, no nested elements, no styles. The container is stored with no data-descriptor flag set (item 16 prints each record's flags and method), and the readout reads no compression method or flag byte itself, so the walk does not exercise compression, split archives or spanned records. The dex member is a header only and is not a valid dex program (the generator's own docstring, `generator.py:8`). The two namespaced attributes carry `ns_index` 0, which items 6 and 8 print as the string `android` (the prefix), while string 1 is the namespace URI; that is a property of these authored bytes, and no conformance of the fixture to any producer's output is claimed. `readout.py:49-50` still comments that widths are "computed here ... not assumed"; the widths are a manual transcription (item 5), and the comment is the readout's own wording, not this entry's claim. Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence.

## Cross-lane scope note (Q10)

The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S049 only; this lane ran no provider and makes no readiness claim (Q05 fence). The kaidoku/revenger ADJ-06 overlap (fleet `.ufo/l0-questions.md:42`, open) stays reported, not absorbed: the kaidoku lane's APK content-graph inventory and Android decode axis (`kaidoku-shokunin/corpus/README.md:27` and `:29`) are not restated, and this entry claims none of that surface.

## §Q-map

| criterion | decision | basis |
|---|---|---|
| Q01 | pass | each load-bearing layout claim rests on a tier-A row for its own scope: S038 (AXML layout, re-opened this round), S048 (dex header semantics), S032/S034 (ZIP records), S047 and S041 (own-work, byte-derived), S049 (route scope only). No tier-C row supports a claim. |
| Q02 | pass | the header carries `source:` for S038, S049, S048, S032, S034, S047 and S041 with anchors, `verified-at:`, `recheck:` and `coverage-map:` naming C05. |
| Q03 | pass | expected values come from the archive bytes, from the authored oracle `truth.json` (emitted by `generator.py`, not by the readout), or from a printed spec line (item 11); item 13 labels the oracle's AXML half as the generator's own build declaration and claims parse fidelity only, never that a declared value is a framework value. None is copied from the record under test. |
| Q04 | pass | no tool claim: the readout is manual standard-library byte analysis, the widths are labeled manual (items 5, 12), and the derivation script's credit is bounded to the lines it prints (item 11). |
| Q05 | pass | no readiness or capability claim and no refusal path described; the provider route is fenced to S049's documented scope (header, Limitations, cross-lane note); the one exit-status sentence (Reproduce: `Exit 0`) is probed by item 15, whose `--stdout-digest` runs the readout with `check=True`, so a non-zero readout exit prints no line. |
| Q06 | pass | the fixture premises are digest-printed from the built bytes (item 14); the entry does not re-run the generator and says so in the S041 header line. |
| Q07 | pass | no parser-behavior prediction is made; the namespace sentence in item 8 describes how this readout resolves this fixture, by the cited source lines. |
| Q08 | n/a | superseded by Q11 in `corpus/QUALITY.md`; the Q11 row below carries the decision. |
| Q09 | pass | every digest is claimed only for the bytes it hashed; item 14 lists the ten `corpus/` files the commands read (including the checker script) and says a digest does not establish production, faithful fetching or currency; the builder script outside `corpus/` is named as undigested. |
| Q10 | pass | scope is one fixture; cross-lane contested scope is named at the note above and not absorbed. |
| Q11 | pass | every count, offset, identifier and digest carries its deriving command and output in items 1-17; the recorded values (APPNOTE and AXML widths) are labeled manual where used; the APPNOTE and snapshot line numbers are printed by items 11-12; `readout.py:N` citations are labeled source locators. |
| Q12 | n/a | this entry writes no rejected-source row. |
| Q13 | pass | the embedded-output gate is credited only for the clause that every embedded line appears in its command's stdout; the `MATCH`/`MISMATCH` lines are credited only for the comparisons each prints. **Unguarded clauses, named:** deleting an embedded output line is not detected (the comparison is one-directional), and a command whose flag is corrupted still passes if its output is a superset of the embedded lines (the readout degrades an unknown flag to its full dump); the entry credits no verifier for either. |
| Q14 | pass | no prose byte count is attached to a hex run; every hex string is printed inside a command block, and the only counts beside hex there are command output. |
| Q15 | pass | this entry states no git object id; identity statements are file digests printed by item 14. |

## Reproduce

From the lane root:

```sh
python3 -B corpus/fixtures/apk-r65/readout.py
```

Exit 0 and 15 stdout lines; item 15's command prints their count and digest and runs the readout with `check=True`. Single-fact form: `python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd`. The eight derivation flags of `corpus/fixtures/apk-r65/entry_checks.py` are `--pins`, `--eocd`, `--oracle`, `--zip-layout`, `--axml-layout`, `--container`, `--spec-quotes` and `--stdout-digest`.
"""


def main():
    text = TEMPLATE.replace("{STATUS}", STATUS)
    text = re.sub(r"\{\{ (.+?) \}\}", sub, text)
    OUT.write_text(text, encoding="utf-8")
    print(f"wrote {OUT} ({len(text)} bytes)")


if __name__ == "__main__":
    main()
