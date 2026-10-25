# R68QmapSelfCheck — Q-map self-consistency of the C05 v3 candidate

**FAIL — the §Q-map's Q11 and Q13 verdicts are contradicted by the entry's own bytes, and 12 of 13 rows are byte-identical to the rejected r67 candidate, leaving the Q01/Q02 bases stale for the v3 deltas.**

Entry under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md`
(215 lines; §Q-map at `:168`, 13 rows at `:172-184`). Read-only seat: nothing written outside this file.

## Impacted axes

- **C2 (coverage)** — `reports/round-68/claims.md` §C2 pass branch requires "every applicable Q01–Q13
  decision of the dispatched wave on the landed v3 bytes is PASS (n/a only with the entry's named
  reason)". If Q11 is FAIL on these bytes (finding 1), the frozen kill rule fires: README C05 stays
  `uncovered`, the file is marked `rejected`, C2 is FALSIFIED — no re-target.
- **Q-map authority drift** — the map is the entry's own claim about its quality; a map that says
  `pass` where the bytes say otherwise is the M20 class ("a recorded value is presented as
  re-derived"), one round after the anchor class (M40/M44) was supposedly closed.

## Commands run (all read-only; no git/jj mutation, no writes into corpus/)

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
exit=0 ; lines=17
```

This reproduces entry item 11's embedded block verbatim. `17` lines = 1 sha line + 16 symbols.
`grep -cE ': (244|237|263)$'` over that output → **0**.

```
$ python3 -B corpus/fixtures/apk-r65/readout.py | sha256sum
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -      (15 lines, exit 0)
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
checked_blocks=17 problems=0      exit=0
```

Entry recheck claims reproduce exactly (fixture/oracle/readout/snapshot bytes also hash as pinned:
`05d2280f…`, `27303bae…`, `92e347c3…`, `56b88bc4…`, and the `.ufo` pinned snapshot is the same
`56b88bc4…`; rea snapshot `412d9cb4…`, its line 5 is `older server.` and lines 7-8 are the quoted
sentence — S043's anchor is true).

```
$ awk 'NR>=230 && NR<=300 && (/^enum/ || /^}/) {print NR": "$0}' corpus/snapshots/ResourceTypes.h
235: };
237: enum {
263: };
```

The chunk-type enum block opens at **237** and closes at **263**, not at 253.

## Finding 1 (admission-blocking) — Q11: the row's `pass` is a false universal about the entry's own numbers

- Entry `:125` (item 11): "**Every S038 line number this entry states is printed by a committed
  derivation script** … no spec line number in this entry is transcribed by hand."
- Entry `:148`: "The chunk-type enum block spans lines **237-253** … line **244** is
  `RES_XML_FIRST_CHUNK_TYPE`."
- The same `237-253` span is stated at `:1` (S038 header anchor), `:50` (item 4), `:157` (§Inference).
- Script output (above): no `237`, no `244`, no `263`; `derive_axml_anchors.py`'s `ENUMS` tuple
  (`corpus/derive_axml_anchors.py:45-53`) has no `RES_XML_FIRST_CHUNK_TYPE` and no block-bound symbol.
  So `:244` and the span bounds are **transcribed by hand**, and the span is **wrong as stated**
  (block = 237-263; `:253` is `RES_XML_RESOURCE_MAP_TYPE`, the last cited enumerator, not the block end).
- Q11's reject rule (`corpus/QUALITY.md:23`): "a value is correct when re-derived but the entry
  carries no derivation". Here the value `:244` *is* correct (`sed -n '244p'` →
  `RES_XML_FIRST_CHUNK_TYPE = 0x0100`) but carries no in-entry derivation, and `:125` presents it as
  machine-derived. The Q11 basis sentence (`:182`, "the spec line numbers carry their deriving
  command and output (item 11, machine-derived, not transcribed)") is therefore **not supported by
  the entry's bytes**. This is the only row the v3 round changed (see Finding 4) — the one new
  sentence is the one that is false.

## Finding 2 (admission-blocking) — Q13: `n/a by construction` is contradicted by the entry's `recheck:` line

- Q13's criterion (`QUALITY.md:25`) applies to "a verifier or recheck command … credited in an entry".
- The v3 entry **does** credit a second command: `:7` `recheck:` names
  `corpus/derive_axml_anchors.py` first; `:125`/`:148` credit it as "the capture that makes it
  mechanical"; `:194` repeats it ("exit 0, 17 lines, one per cited symbol (item 11)" — itself false:
  17 lines / 16 symbols, and not one per *cited* number).
- The Q13 basis (`:184`) says "no verifier, recheck command, comparison tool or automatic checker is
  credited or introduced **beyond the entry's own readout recheck**" — the derive command is not the
  readout recheck, and it is credited. The row is also a copy of r67's wording, which predates the
  derive command's existence.
- Counterexample that the credited command cannot guard the clause: the registered gate compares
  **fenced blocks only** (`corpus/check_embedded_outputs.py:parse_blocks`, only lines starting `$ `).
  Two mutations of a `/tmp` copy of the entry:

```
== prose-only mutation (":244 is RES_XML_FIRST_CHUNK_TYPE" -> "line 999 is ...") ==
checked_blocks=17 problems=0      exit=0        <-- prose anchor is UNGUARDED
== fenced-block mutation ("RES_XML_START_NAMESPACE_TYPE : 245" -> ": 244") ==
drift entry:139 embedded output line not in recheck stdout: enum RES_XML_START_NAMESPACE_TYPE : 244
checked_blocks=17 problems=1      exit=1
```

So the correct Q13 decision is `pass`, **with the unguarded clause named** (prose anchors at `:1`,
`:50`, `:148`, and the block extent), as the round-64 entry did ("The recheck command is a
reproducibility aid, not a gate", `corpus/knowledge/round-64-firmware-region-byte-evidence.md:221`).
`n/a by construction` asserts the criterion cannot apply, which is false on these bytes.

## Finding 3 — Q01/Q02 bases are stale r67 sentences (registry-contradicted)

- Q01 (`:172`): "the dex declared-header claims rest on S045 (tier A, **opened 2026-10-24 this
  round**)". `corpus/SOURCES.md:59` records S045's `used-by` as
  `corpus/knowledge/round-67-apk-axml-byte-evidence.md`, and the r67 entry's own header
  (`:3`) says S045 was "opened 2026-10-24 by this entry's author" — i.e. opened in **round 67**, not
  this round. The sentence is true of the r67 entry and was copied unchanged.
- Q01 also **omits S046**, the only row opened in round 68 (`SOURCES.md:61`, `used-by` `—`) and the
  row that carries the very anchors Q11 relies on.
- Q01's "row mined r65, **re-opened 2026-10-24 by this entry's author**" (S038) has no registry
  record: `SOURCES.md:13` has no re-open column; S038's row reads `mined | 2026-10-24 | on-release |
  corpus/knowledge/round-65-apk-axml-byte-evidence.md`. The re-open is a phrase, not a recorded state.
- Q02 (`:173`): basis enumerates `source:` rows "S038, S043, S045, S041" — the header now carries
  **five** `source:` lines, including **S046 at `:4`** (verified: `grep -c '^source:'` → 5). The
  criterion itself is nonetheless satisfied (`source:` ×5, `verified-at:` `:6`, `recheck:` `:7`,
  `coverage-map: C05` `:8`), so the verdict stands but the basis understates the header.

## Finding 4 — 12/13 rows are byte-identical to the rejected r67 candidate

```
$ diff <(sed -n '/^## §Q-map/,/^## Reproduce/p' corpus/knowledge/round-67-apk-axml-byte-evidence.md) \
       <(sed -n '/^## §Q-map/,/^## Reproduce/p' corpus/knowledge/round-68-apk-axml-byte-evidence.md)
15c15
< | Q11 | pass | … the fixed struct constants carry their S038 field-list derivation (item 5); the attribute location …
> | Q11 | pass | … the fixed struct constants carry their S038 field-list derivation (item 5); the spec line numbers carry their deriving command and output (item 11, machine-derived, not transcribed); the attribute location …
```

Only Q11 changed. The Q-map was not re-derived against the v3 deltas (new item 11, new S046 row, new
`admission-status:`, new item-11 prose) — which is why Q01 still attributes S045 to "this round",
Q02 still lists four sources, and Q13 still measures "the entry's own readout recheck". A self-check
that is generic prose passes any entry; these three rows were checkable and are false.

## Per-row verdicts

| row | entry line | basis pointer resolves in the entry? | verdict |
|---|---|---|---|
| Q01 | :172 | `SOURCES.md` S038/S043/S045/S032/S034/S041 all exist tier A (`:46,48,52,55,57,59`) — but S045 "opened … this round" is contradicted by `SOURCES.md:59`; S046 (`:4`) omitted; S038 "re-opened" is unrecorded | **PASS on tier/scope (carried-row precedent r63/r65) / basis false** |
| Q02 | :173 | `:1-5` sources, `:6` verified-at, `:7` recheck, `:8` coverage-map C05 — all present | **PASS / basis stale (omits S046 at `:4`)** |
| Q03 | :174 | item 5 (`:59`) derived widths + `truth.json` oracle + S045 table quote (`:107`) — all in entry | PASS |
| Q04 | :175 | `:12-13` scope paragraph says "The analysis is **manual**"; no product tool claimed | PASS |
| Q05 | :176 | `## Cross-lane scope note (Q10)` at `:164` fences the provider route | PASS |
| Q06 | :177 | readout bytes hash-pinned (`:7`, `:194`) and reproduce (stdout `507d79…`); generator non-rerun disclosed | PASS |
| Q07 | :178 | no accept/refuse prediction; §Inference `:157` labels the spec mapping as inference | PASS |
| Q08 | :179 | `QUALITY.md:23` is the Q11 row and states "Supersedes Q08" — pointer resolves; "superseded by Q11" is precedent (r62 `:346`, r63 `:729`, r64 `:216`) but is neither PASS nor n/a under claims.md §C2's predicate | **adjudication item (vocabulary)** |
| Q09 | :180 | every digest re-hashed here: `05d2280f…`, `27303bae…`, `92e347c3…`, `56b88bc4…` (corpus copy = `.ufo` pinned copy), `412d9cb4…`, stdout `507d79…` | PASS |
| Q10 | :181 | `§Limitations` `:160` + `§Cross-lane scope note` `:164` | PASS |
| Q11 | :182 | item 11 (`:125`) does **not** print `:237`, `:244`, `:263`; `:148` span is wrong (block = 237-263); gate is block-only (prose mutation exit 0) | **FAIL** |
| Q12 | :183 | no rejected source row is written here — S039's supersession is recorded at `SOURCES.md:57` (round 66), the entry only restates it at `:2` | n/a holds |
| Q13 | :184 | `:7`/`:125`/`:194` credit a second recheck command; the credited command's own run cannot detect a wrong prose anchor (prose mutation exit 0) | **FAIL as decided (n/a is wrong; correct: pass with unguarded clause named)** |

Rows marked `n/a` that should not be: **Q13**. Q12's `n/a` is correct.

## Secondary (not admission-blocking on their own)

- `:59` item 5: "computed by summing the field widths of S038's own struct definitions … not
  assumed" — the widths are a literal table in `corpus/fixtures/apk-r65/readout.py:52-59`
  (`{"ResChunk_header": [w16, w16, w32], …}`); only the sums are computed. Under Q11's letter
  ("Constants such as header offsets are derived, not assumed") the summands are recorded, not
  derived. Same class as Finding 1, smaller blast radius (the values are correct).
- `SOURCES.md:52` S038 anchor says "chunk-type enum **:239-250**"; the entry says **237-253**; the
  bytes say **237-263**. Three artifacts, three spans — none derived.
- `SOURCES.md:61` S046 scope repeats the false universal: "the machine derivation of **every**
  AOSP `ResourceTypes.h` line number the round-68 C05 candidate cites". Fixing the entry prose
  without extending the script leaves the registry row false.
- `:194` "17 lines, one per cited symbol" — 17 lines, 16 symbols, and not one per cited number.

## Smallest safe correction (pre-flip, keeps every other byte)

1. Extend `corpus/derive_axml_anchors.py`: add `RES_XML_FIRST_CHUNK_TYPE` to `ENUMS`, plus two block
   bound lookups (`enum {` at 237, `};` at 263) — the script already refuses ambiguity, so this is
   mechanical. Then re-derive and update: entry `:1`, `:50`, `:148`, `:157` (`237-253` → `237-263`),
   the embedded block, `:194` line count, `SOURCES.md:52`/`:61` spans and line counts.
2. Alternatively (smaller): narrow `:125` to "every **cited symbol** is printed; the block bounds and
   the `:244` contrast are recorded from the snapshot", and drop `237-253` from `:148`/`:157` (keep
   per-symbol anchors, which are derived). Either way Q11's basis (`:182`) then becomes true.
3. Q13 (`:184`): replace `n/a by construction` with `pass`, naming the unguarded clause — the derive
   script's exit-2 guards symbol presence only; neither command compares prose numbers to output
   (evidence: prose mutation exit 0, block mutation exit 1).
4. Q01 (`:172`): "S045 … opened round 67 (`SOURCES.md:59`)"; add S046 (opened this round); drop or
   register the S038 "re-opened" phrasing. Q02 (`:173`): add S046, and cite `:1-5`.
5. Adjudicator only: decide whether `superseded by Q11` satisfies claims.md §C2's "is PASS (n/a only
   with the entry's named reason)" — precedent says yes; the frozen predicate's letter says it is
   neither.

## Tooling

No installs or upgrades were needed or performed for this seat (no pacman/uv/npm/cargo transaction).

## Report

`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-68/R68QmapSelfCheck.md`
