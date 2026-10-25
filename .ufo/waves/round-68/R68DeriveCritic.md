FAILS-OPEN (gate/scheme: checks only fenced-output reproducibility, never anchor truth) / FAILS-CLOSED (derive script itself: exit 2, single error line, no partial table, on every corruption tested)

Seat: L1Revenger68.R68DeriveCritic. Lane tree unmodified — verified after all work:
`bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors.py`
`56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h`
`107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b  corpus/knowledge/round-68-apk-axml-byte-evidence.md`
All corruption work was done in `/tmp/r68-derive-critic/` scratch copies. No tool installs (none needed).

## Axes named (godspeed)

- **A1 script-level input robustness** — does a corrupted input produce exit 2 and no invented line?
- **A2 gate semantics** — does `check_embedded_outputs.py` check anchors, or only that fenced output is reproducible?
- **A3 anchor-of-the-anchor** — what grounds the pin? (single constant inside a mutable script whose own sha256 is cited only in prose)
- **A4 prose-anchor coverage** — are the entry's load-bearing `:NNN` anchors (header, item 4, item 11 sentence) inside the gated surface at all?
- **A5 counter coverage** — does `reports/round-68/measure.py` ever look at the snapshot or the anchors?

## Baseline (pristine scratch copy)

```
$ cd /tmp/r68-derive-critic/base && python3 -B derive_axml_anchors.py
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
17 lines, exit 0; matches `corpus/knowledge/round-68-apk-axml-byte-evidence.md:129-145` byte for byte, and the :245 anchor in `entry:1` and `entry:148` is correct against the pinned original.

Gate on a scratch copy of the whole lane (entry untouched): `checked_blocks=17 problems=0`, `GATE_EXIT=0`.

## The three requested corruptions (scratch copies only)

| # | corruption | script exit | script stdout |
|---|---|---|---|
| 1 | snapshot truncated to 40000 B (`67e0a38b…ebac`) | **2** | `derive_axml_anchors: snapshot digest 67e0a38b806057ee8a97d2f3dc3de5a649970a1c41cfff65b15872bdad85ebac != pinned 56b88bc4…c56f` |
| 2 | one byte changed inside the cited comment word (`the attributes start.` → `The`), file still 86255 B (`6bed1866…88e4`) | **2** | `derive_axml_anchors: snapshot digest 6bed186612b6d796181d858390e0b92df64230833770e49c7ff729a25f8188e4 != pinned 56b88bc4…c56f` |
| 3a | `RES_XML_START_NAMESPACE_TYPE` appended a second time, pin untouched | **2** | digest mismatch (same shape as 1) |
| 3b | same duplicate, pin re-pinned to `02a50f19…c3b8` | **2** | `derive_axml_anchors: enum RES_XML_START_NAMESPACE_TYPE: ambiguous (2 hits at [245, 2367])` |

Supplemental probes of the same failure path:

| # | corruption | exit | stdout |
|---|---|---|---|
| 4 | `struct ResXMLTree_attribute` line deleted, pin re-pinned | **2** | `derive_axml_anchors: struct ResXMLTree_attribute: not found` |
| 5 | `struct ResXMLTree_attrExt` renamed to `…attrExtX` (look-alike left in place), pin re-pinned | **2** | `derive_axml_anchors: struct ResXMLTree_attrExt: not found` |
| 6 | snapshot file absent | **2** | `derive_axml_anchors: snapshot missing: /tmp/r68-derive-critic/c6/snapshots/ResourceTypes.h` |
| 7 | invalid UTF-8 in the last 5 bytes (untouched by any cited symbol), pin re-pinned | 0 | 17 correct lines — `raw.decode(…, errors="replace")` (`derive_axml_anchors.py:81`) absorbs it; harmless **only because** the pin is exact-match, see A3 |

**Does it refuse to print a line it did not find?** Yes, and more strictly than the docstring claims: `main()` accumulates all 17 lines in `out` and prints only after every `find_unique` has succeeded (`derive_axml_anchors.py:84-97`). A failing run emits **exactly one line** — the error. Measured: `cd c3repin && python3 -B derive_axml_anchors.py | wc -l` → `1`. No partial table, no first-hit fallback: `find_unique` (`:64-70`) fails on `not hits` and on `len(hits) > 1` with the hit list in the message. The predicate style also blocks the classic weakening — structs require exact `l.strip() == f"struct {n}"` (`:86`), enums require prefix-with-trailing-space (`:90`), so `struct Res_value;` or `RES_XML_TYPE_EXTRA` cannot be mistaken for the cited symbol.

**A1 verdict: FAILS-CLOSED.** All corruption is caught by the `SNAPSHOT_SHA256` exact-match at `derive_axml_anchors.py:33,79-80` *before* any search runs; the missing/ambiguous/renamed cases are caught independently by `find_unique`. Nothing is printed that was not found.

## Does a corrupted `corpus/snapshots` copy silently make the anchors wrong while the gate passes?

**Yes — but not by corrupting the snapshot alone.** The residual attack has two steps, and I executed both on a scratch lane.

### Demo B — consistent-but-wrong (gate exit 0, anchors wrong, entry self-contradictory)

1. Inserted 3 comment lines after line 1 of the snapshot copy → every cited symbol still occurs exactly once, all line numbers shift +3; new digest `400896fe35ddceac811424e9a928b093fc866bc42c104d99b52330419fead8fc`.
2. Re-pinned `SNAPSHOT_SHA256` in the scratch `derive_axml_anchors.py` (one-line sed, script sha256 changes from `bce497d6…` to whatever).
3. Regenerated only the fenced item-11 output block from the script's new stdout.

```
$ python3 -B corpus/derive_axml_anchors.py
sha256 400896fe35ddceac811424e9a928b093fc866bc42c104d99b52330419fead8fc ResourceTypes.h
struct ResChunk_header : 221
struct Res_value : 290
enum RES_XML_START_NAMESPACE_TYPE : 248          <-- real pinned value is 245
...
SCRIPT_EXIT=0

$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
checked_blocks=17 problems=0
GATE_EXIT=0
```

The resulting entry contradicts itself on its own page and the gate reports a clean pass:
- `entry:1` header still says `RES_XML_START_NAMESPACE_TYPE` **:245**;
- `entry:139` (fenced) now says `enum RES_XML_START_NAMESPACE_TYPE : 248`;
- `entry:148` prose still says "is line **245**; line 244 is `RES_XML_FIRST_CHUNK_TYPE`".

Read the gate's mechanism (all line pointers below are against `corpus/check_embedded_outputs.py` sha256 `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca`, the version present in the lane when this seat read it): `evaluate()` (`check_embedded_outputs.py:88-107`) parses only fenced `$ cmd` blocks, runs the command, and requires each embedded line to be a member of `set(stdout.splitlines())` (`drift()`, `:83-85`). It never hashes the snapshot, never hashes the script, never parses prose, and never compares against the AOSP bytes. It is a **reproducibility/consistency** check between the entry and the *current tree*, not an anchor check. Because `reports/round-68/measure.py:439-445` defines `C7_V3_CLEAN = (rc == 0)` from exactly that `--entry` invocation, the counter's C7 leg inherits the same blindness: on the Demo B tree it would print `C7_V3_CLEAN=yes`.

### Demo A — the gate does not check anchors even with a pristine snapshot

Restored the real `56b88bc4…` snapshot and the real script, then changed **only prose** — `entry:1` header `**:245**` → `**:244**` and `entry:148` "is line **245**" → "is line **244**" — i.e. re-injected the exact round-65/round-67 M40/M44 defect this entry is built to repair:

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
checked_blocks=17 problems=0
GATE_EXIT=0
```

The `:244` defect is invisible to the gate. The class the C7 gate was registered to catch is only caught where the entry repeats itself inside a fence.

### Demo C — the script identity anchor (S046) is unchecked

`entry:4` and `corpus/SOURCES.md:61` cite `corpus/derive_axml_anchors.py` sha256 `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`. Appending one comment line to the scratch script (`830f78a1…` → `92218886…`, output unchanged) leaves the gate green: `checked_blocks=17 problems=0`, `GATE_EXIT=0`, while the cited sha256 is stale. Nothing in the corpus or the counter hashes the script.

### A5 — the counter never looks at the snapshot or the anchors

`grep -n "ResourceTypes\|snapshots\|SNAPSHOT" reports/round-68/measure.py` → no match. `HOLDS_C2_V3` (`measure.py:114-117`) is row-text/coverage accounting only; the only anchor-adjacent leg is `C7_V3_CLEAN`, which is the gate exit code. So within the counted surface (`git archive <commit> corpus`) there is **no** comparison of `corpus/snapshots/ResourceTypes.h` against `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` — the pinned original is outside the extracted tree by construction.

## Where the truth actually rests

Two things currently keep the anchors honest, and neither is the gate:

1. **The pin constant is exact-match and the build verifies the original first.** `derive_axml_anchors.py:33,79-80` makes any byte change a hard exit 2, and `.ufo/waves/round-68/build-r68.py:28-29,56-60` hashes `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` against `56b88bc4…` **before** writing `corpus/snapshots/ResourceTypes.h` (`:57` is the `die` on mismatch, `:60` the copy write). So at build time the copy provably equals the pinned AOSP bytes (independently re-confirmed by me: both files hash to `56b88bc4…`, 86255 B).
2. **The wave's independent re-derivation.** The dispatched anchor seat is told to derive from the pinned original, not from the entry (`.ufo/waves/round-68/build-wave-spec.py:128`). I did that myself: the pinned original gives `struct ResChunk_header` :218 and `enum RES_XML_START_NAMESPACE_TYPE` :245 — so **the landed v3 anchors are correct today**; Demo B is a latent guard defect, not a present error. `corpus/README.md:34` also still shows C05 `uncovered`, consistent with the brief.

Impacted axes: A2 (gate semantics — fail-open), A3 (anchor-of-the-anchor is a single mutable constant), A4 (prose anchors ungated, Demo A), A5 (counter blind). A1 is clean.

## Counterexample that survives, stated as an attack

`corpus/snapshots/ResourceTypes.h` + `derive_axml_anchors.py:33` + the fenced item-11 block are three files that can be made mutually consistent around wrong bytes, and every mechanical check in the round-68 surface — the C7 gate, `C7_V3_CLEAN`, `HOLDS_C2_V3` — stays green. The frozen C2 pass predicate (`reports/round-68/claims.md` pass branch: `C7_V3_CLEAN=yes` + "every applicable Q decision PASS") therefore **cannot distinguish "machine-derived" from "machine-derived from substituted bytes"**. Q11 as written ("the spec line numbers carry their deriving command and output (item 11, machine-derived, not transcribed)") is satisfied by Demo B. The only thing standing between the corpus and that state is that the derivation seat reads the `.ufo` original — a process fact, not a predicate.

## Smallest safe correction (does not touch frozen artifacts)

Make the entry's own existing digest prose the second pin, so no single file edit can turn the table:

1. Add to the gate's entry mode (or a two-line pre-check in `check_embedded_outputs.py --entry`, which is already registered and already outside the `verify_*` census, `check_embedded_outputs.py:6-11`) a required assertion:
   - `sha256(corpus/derive_axml_anchors.py)` equals the sha256 the entry cites at `entry:4` / `SOURCES.md:61`, and
   - `sha256(corpus/snapshots/ResourceTypes.h)` equals the digest printed by the derivation **and** the digest cited at `entry:1`/`entry:4`/`SOURCES.md:52`.
   Demo C shows the first is unchecked today; Demo B is defeated by it, because re-pinning the script changes the script hash the entry names, and the second assertion then also fails unless the snapshot is restored.
2. Leave `reports/round-68/measure.py` frozen (no new verifier — the ten-verifier census and `HOLD_REPLAY=10/10` stay untouched).
3. Do **not** propose gating prose; instead, record in the C2 admission criteria that the anchors are accepted only on the independently derived values from `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` (my run: 218 / 287 / 461 / 612 / 621 / 677 / 707 and 239 / 241 / **245** / 246 / 247 / 248 / 253, comment 686, field 687 — identical to the landed table), so a later byte substitution is caught by a value the gate never sees.

No `Report:` trailer edits were made outside this file; no git/jj mutation, no corpus edit, no family message.
