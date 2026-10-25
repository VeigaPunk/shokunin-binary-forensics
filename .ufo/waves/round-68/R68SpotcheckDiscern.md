# R68SpotcheckDiscern — outside-discernment spot-check (adjudication aid, not a verdict)

**AGREE / AGREE** — both spot-checks agree with the bytes: S046's recorded anchor `enum RES_XML_START_NAMESPACE_TYPE : 245` is a verbatim line of the script's actual stdout and both digests in the row match disk, and the entry's tier-A claim that `RES_XML_START_NAMESPACE_TYPE` is snapshot line 245 (with line 244 naming a *different* constant, `RES_XML_FIRST_CHUNK_TYPE`) is confirmed in both the pinned round-65 snapshot and the committed corpus copy. No discordance found; two calibration notes (quote form, and one non-anchor `:244` residual class that is *not* a defect) are recorded below.

Lane: read-only. Nothing in `corpus/`, `reports/`, `.git`, or the jj state was written, and no git/jj mutation was run. No tool was installed or upgraded (none needed).

---

## Check A — S046 row vs the script's actual output (AGREE)

Source row: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:61` — S046, own-work, tier A, opened 2026-10-24; claims script sha256 `bce497d6…e249`, **17 output lines**, snapshot copy sha256 `56b88bc4…c56f` (86255 bytes), located quote ``enum RES_XML_START_NAMESPACE_TYPE : 245``.

### A1. Digests on disk vs the row

```
$ sha256sum corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h \
      .ufo/waves/round-65/source-snapshots/ResourceTypes.h
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h

$ wc -c corpus/snapshots/ResourceTypes.h
86255 corpus/snapshots/ResourceTypes.h
```

- script digest == row's script digest (byte-for-byte, both places the digest is cited: the row at `SOURCES.md:61` and the entry's `source: S046` header at `corpus/knowledge/round-68-apk-axml-byte-evidence.md:4`).
- snapshot digest == row's pinned digest, and it is **the same digest as the lane's pinned round-65 snapshot** → the "byte-exact copy" claim in the row is true on disk.
- 86255 bytes == the row's stated size.
- Only two files in the repo cite this script digest; neither carries a stale value:
  `$ grep -rn bce497d6…e249 --include='*.md' --include='*.py' .` → `corpus/knowledge/round-68-apk-axml-byte-evidence.md:4`, `corpus/SOURCES.md:61` (plus two sibling wave reports quoting it: `R68SnapshotFidelity.md:49`, `R68FixtureHold.md:84`).

### A2. The located quote in the actual stdout

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && python3 -B corpus/derive_axml_anchors.py
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

$ wc -l < stdout
17
```

- Line 11 of the real stdout is exactly ``enum RES_XML_START_NAMESPACE_TYPE : 245`` → the row's located quote is present verbatim; **AGREE**.
- **17** stdout lines → matches the row's "17 output lines" exactly.
- Exit 0.

### A3. The load-bearing property ("never prints a line it did not find") — probed, holds

I did **not** take the docstring's word for it. Probes ran on a throwaway copy under `/tmp` (deleted afterwards); `corpus/` was never touched.

- **Missing symbol** — copy + injected `ResThisSymbolDoesNotExist`:
  `derive_axml_anchors: struct ResThisSymbolDoesNotExist: not found` → exit **2**, no line number printed.
- **Ambiguous symbol** — copy with a second `RES_XML_START_NAMESPACE_TYPE` line injected into the snapshot and the copy's pinned digest updated to match, so the ambiguity path (not the digest guard) is the one exercised:
  `derive_axml_anchors: enum RES_XML_START_NAMESPACE_TYPE: ambiguous (2 hits at [245, 246])` → exit **2**, no line number printed.
- Same copy at the unmodified bytes → exit 0 with identical output → the derivation is location-independent (`Path(__file__).resolve().parent`), so a corpus-tree copy and the lane tree derive the same table.
- Predicates are unique, i.e. line 245 is a *unique* hit and not a first-hit mask (`corpus/derive_axml_anchors.py:47-55`, enum predicate `l.strip().startswith(name + " ")`; `find_unique` fails on `len(hits) > 1`):

```
RES_XML_START_NAMESPACE_TYPE predicate-hits [245]
RES_XML_END_NAMESPACE_TYPE predicate-hits [246]
RES_XML_FIRST_CHUNK_TYPE predicate-hits [244]
comment hits [686]
```
  Note the snapshot contains the token `RES_XML_START_NAMESPACE_TYPE` twice (245 and the nested-enum *usage* at 736); the `startswith` predicate excludes the 736 usage, which is why 245 is unique rather than "ambiguous". This is the intended discrimination, not a masked ambiguity.

### A4. Calibration note on the quote form (not a defect)

`grep -c 'enum RES_XML_START_NAMESPACE_TYPE : 245' corpus/snapshots/ResourceTypes.h` → **0**. The row's "located quote" is a *derived-output* form (`enum` is a projection word; the bytes at 245 read `    RES_XML_START_NAMESPACE_TYPE      = 0x0100,`), so it locates a line **in the script's stdout**, not in the AOSP bytes. That is consistent with what the row names as its source (the derivation script, not the header), and the underlying fact is independently verified in the bytes (Check B). Recording it here so a future reader does not treat the S046 quote as a greppable byte citation of `ResourceTypes.h` — verification of the *fact* must go through `grep -n '^    RES_XML_START_NAMESPACE_TYPE'` (244/245 boundary), as in Check B.

---

## Check B — the entry's tier-A anchor claim vs the pinned snapshot bytes (AGREE)

Claim: `corpus/knowledge/round-68-apk-axml-byte-evidence.md:1` — "chunk-type enum block **lines 237-253**: … `RES_XML_START_NAMESPACE_TYPE` **:245**", and `:135` (item 11) — "`RES_XML_START_NAMESPACE_TYPE` is line **245**; line 244 is `RES_XML_FIRST_CHUNK_TYPE`".

```
$ grep -n 'RES_XML_START_NAMESPACE_TYPE\|RES_XML_FIRST_CHUNK_TYPE' \
      .ufo/waves/round-65/source-snapshots/ResourceTypes.h
244:    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
245:    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
734:        FIRST_CHUNK_CODE = RES_XML_FIRST_CHUNK_TYPE,
736:        START_NAMESPACE = RES_XML_START_NAMESPACE_TYPE,

$ sed -n '244p;245p' .ufo/waves/round-65/source-snapshots/ResourceTypes.h
    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
    RES_XML_START_NAMESPACE_TYPE      = 0x0100,
```

Identical output from the committed corpus copy `corpus/snapshots/ResourceTypes.h` (same sha256, so byte-identical by construction).

- `RES_XML_START_NAMESPACE_TYPE` **is** line 245 → **AGREE**.
- Line 244 **does** name a different constant, `RES_XML_FIRST_CHUNK_TYPE` → **AGREE**; the entry's own item-11 sentence is correct, and the r67 `:244` off-by-one (M40/M44) is genuinely repaired.
- Enum block bounds sanity: `sed -n '237p;253p'` → `enum {` and `RES_XML_RESOURCE_MAP_TYPE         = 0x0180,` → the header's "lines 237-253" span is correct at both ends.
- The two supporting S038 anchors item 8/11 rely on also land where claimed: `sed -n '686p;687p'` → `// Byte offset from the start of this structure where the attributes start.` and `uint16_t attributeStart;` — matching the script's `comment attributeStart : 686` / `field attributeStart : 687`.

---

## Corroborating check: the entry's embedded derivation output is byte-exact

Item 11 embeds the command and its output (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:127-146`, fence opens at 127, command at 128, closing fence at 146). Extracting the fenced block programmatically and diffing against the captured stdout:

```
embedded 17 actual 17
byte-exact: True
stripped-equal: True
diffs: []
trailing-ws embedded: []
```

So the registered embedded-output gate is being fed a block that is byte-identical to what the script actually prints on this tree — no transcription drift in the block the C1 gate would re-check. (Running `corpus/check_embedded_outputs.py` itself is C1's seat; I neither ran nor modified it.)

## Residual `:244` scan on the entry (no live stale anchor)

`grep -n ':244' corpus/knowledge/round-68-apk-axml-byte-evidence.md` → exactly **2** hits, both repair narrative, neither an anchor assertion:

- `:6` (verified-at) — "the round-67 draft's `:244` anchor is the M40/M44 class this entry repairs…"
- `:9` (admission-status) — "the round-67 v2 candidate's two `:244` anchors are corrected to `:245`…"

The three live mentions of the constant all point at 245 (`:1` header `** :245**`, `:57`, and the embedded output line). No residual `:244` anchor.

## Q-map spot-read (auxiliary, not my assigned check)

`QUALITY.md:20` defines Q08, `QUALITY.md:23` opens "Q11 | Supersedes Q08." The entry's `## §Q-map` row `:179` maps Q08 to "superseded by Q11" rather than silently passing it — consistent with the registry text I read; whether the *rest* of the Q-map holds is the Q02/Q03/Q05/Q06/Q08/Q10/Q11/Q12 seats' call, not mine.

## Scope, and what I did not check

- **Checked:** S046's own anchor + both digests + output-line count + the negative/ambiguous exit paths; the entry's `RES_XML_START_NAMESPACE_TYPE` :245 / :244 claim in the pinned bytes; the entry's embedded block byte-exactness; residual `:244` scan; Q08/Q11 supersession text.
- **Not checked (other seats own these):** C7 mutant/spoof attacks, `check_embedded_outputs.py` behaviour, `readout.py` / fixture oracle agreement, the C05 admission decision itself, C1/C2 frozen-predicate replay, counter replays, the `reports/round-68/measure.py` run.
- **Absent dependency, recorded not resolved:** the brief cites an r67 spot-check of `S055`/`S060` as precedent; neither row exists in this lane's `corpus/SOURCES.md` (`grep -n 'S055\|S060' corpus/SOURCES.md` → no match), so the precedent document itself was not available to compare form against. This does not affect either verdict above — the checks were made against the bytes directly.
- `/home/vgpnk/Projects/shokuknow` was not written, read-modified, or fetched from.
