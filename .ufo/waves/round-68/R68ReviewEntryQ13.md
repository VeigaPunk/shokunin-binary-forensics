FAIL — Q13: the entry credits `corpus/derive_axml_anchors.py` with "every S038 line number this entry cites" (entry:1, :4, :7, :125, :194) while its own run prints no line for two cited S038 numbers, `237` and `244` (both cited at entry:1/:57/:148/:157 and :148); falsifying those two clauses leaves the command's stdout byte-identical and the entry's registered gate clean (`checked_blocks=17 problems=0`, exit 0), so the credit survives deletion. The Q-map row `Q13 | n/a by construction` (entry:184) is therefore a wrong decision, not a bounded credit.

Seat: L1Revenger68.R68ReviewEntryQ13 (fresh, non-author). Reviewed bytes:
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md`
(215 lines; `admission-status: candidate`). Read-only: no repo file edited, no git/jj mutation, no fixture/live/snapshot write.

## Criterion, as applied

QUALITY.md Q13 (`corpus/QUALITY.md`): "A verifier or recheck command is credited in an entry only for the clauses whose deletion its own run is shown to detect; other clauses are named as unguarded." Reject when "an entry cites a verifier as guarding a value whose check survives deletion".

Q13 applies here because the entry credits recheck commands with a stated coverage scope. It does not merely re-run a manual readout (the round-62 `n/a` shape, `corpus/lessons/round-62.md:256`): the derive script is credited as the guard that makes anchor transcription impossible —

- entry:4 (S046 row): "the machine derivation of **every S038 line number this entry cites**"
- entry:7 (`recheck:`): "`python3 -B corpus/derive_axml_anchors.py` … (**every S038 line number this entry cites**; exits 2 if a cited symbol is missing or ambiguous)"
- entry:125 (item 11 opening): "**Every S038 line number this entry states is printed** by a committed derivation script … The script refuses to print a line it did not find"
- entry:148: "the derivation above is the capture that makes it mechanical"
- entry:194 (§Reproduce): "exit 0, **17 lines, one per cited symbol**"
- entry:1 (`source:` S038 anchors): "**every line number above is machine-derived** by `corpus/derive_axml_anchors.py` from the pinned snapshot — item 11"

## Evidence — commands re-run by this seat, actual output

### 1. The credited recheck run (entry:127-145 block vs live stdout)

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
```

17 stdout lines = 1 digest line + 16 symbol lines. Diffed against the entry's embedded block (entry:128-145): **byte-identical** apart from the `$ python3 …` prompt line I stripped —

```
$ sed -n '128,145p' <entry> > /tmp/block ; python3 -B corpus/derive_axml_anchors.py > /tmp/derive ; diff /tmp/block /tmp/derive
1d0
< $ python3 -B corpus/derive_axml_anchors.py
```

So the embedded block is faithfully captured (not a transcription defect); the defect is the **scope of the credit**, not the block.

### 2. Coverage set: 18 cited S038 numbers, 16 printed, 2 unguarded

Distinct S038 line numbers the entry states (prose + header, excluding the embedded block itself):
`218, 237, 239, 241, 244, 245, 246, 247, 248, 253, 287, 461, 612, 621, 677, 686, 687, 707` (18).
Printed by the run: the 16 symbols above. Not printed: **`237`** and **`244`**.

```
cited 18 derived-of-cited 16 unguarded [237, 244]
```

Snapshot bytes at those lines (correct values, but not derived by the credited command):

```
$ awk 'NR==237||NR==244{printf "%d|%s\n",NR,$0}' corpus/snapshots/ResourceTypes.h
237|enum {
244|    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
```

Structural cause: `corpus/derive_axml_anchors.py:33-51` hard-codes `STRUCTS` (7 names) and `ENUMS` (7 names); `RES_XML_FIRST_CHUNK_TYPE` is **not** in `ENUMS` (`grep -n RES_XML_FIRST_CHUNK_TYPE corpus/derive_axml_anchors.py` → no match), and the script has no output line for the enum-block span (`out` is built only from `STRUCTS`, `ENUMS`, one comment, one field; `derive_axml_anchors.py:84-98`).

### 3. Deletion/alteration sensitivity — the two clauses are unguarded by every credited check

Proven parts of the credit (so the FAIL is scoped, not blanket): the run **does** exit 2 on a missing or ambiguous cited symbol —

```
# copy of corpus in /tmp, RES_XML_START_NAMESPACE_TYPE line removed, pin updated
$ python3 -B derive_axml_anchors.py
derive_axml_anchors: enum RES_XML_START_NAMESPACE_TYPE: not found
EXIT_missing=2

# copy with the RES_XML_END_ELEMENT_TYPE enum line duplicated, pin updated
$ python3 -B derive_axml_anchors.py
derive_axml_anchors: enum RES_XML_END_ELEMENT_TYPE: ambiguous (2 hits at [248, 249])
EXIT_ambiguous=2
```

Falsifying the two unguarded clauses survives everything:

```
# /tmp/r68q13mutA: entry:148 changed to "spans lines 236-253" and "line 244 is `RES_XML_TABLE_TYPE`"
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
checked_blocks=17 problems=0
EXIT_MUTANT_A=0
```

(the derive command's own stdout cannot change — it never reads the entry and has no line for 237/244).

Control that the *embedded block* is guarded (so the gate is real and the finding is specifically about the prose clauses):

```
# /tmp/r68q13mutB: embedded block line "enum RES_XML_START_NAMESPACE_TYPE : 245" -> ": 244" (the exact r67 defect)
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
drift entry:139 embedded output line not in recheck stdout: enum RES_XML_START_NAMESPACE_TYPE : 244
checked_blocks=17 problems=1
EXIT_MUTANT_B=1
```

Baseline (unmutated): `checked_blocks=17 problems=0`, `EXIT_BASELINE=0`.

### 4. Readout recheck credit is honest where measured

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/out ; echo EXIT=$?; wc -l < /tmp/out; sha256sum /tmp/out
EXIT=0
15
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  /tmp/out
```

Matches entry:7 and entry:194 exactly (15 lines, `507d79f8…`). Digests also match: `corpus/snapshots/ResourceTypes.h` = `56b88bc4…` (86255 bytes), `corpus/derive_axml_anchors.py` = `bce497d6…`, `corpus/fixtures/apk-r65/readout.py` = `92e347c3…`.

## Entry lines at issue, with the exact wrong value and the correct value

| entry line | assertion (credited clause) | wrong value | correct value |
|---|---|---|---|
| 4 (S046 row) | "the machine derivation of **every** S038 line number this entry cites" | every = 18/18 | 16/18: `237` and `244` are not derived by that script |
| 7 (`recheck:`) | derive script covers "**every** S038 line number this entry cites" | same | scope it to "the 16 symbols it prints (list); `237`/`244` are recorded from the snapshot, unguarded" |
| 125 (item 11 opening) | "**Every** S038 line number this entry states is printed by a committed derivation script" | every | 16 of 18; `237` and `244` are not printed |
| 148 | "The chunk-type enum block spans lines **237**-253 … line **244** is `RES_XML_FIRST_CHUNK_TYPE`" | the *derivation status* of 237 and 244 (values themselves are correct) | add `enum RES_XML_FIRST_CHUNK_TYPE : 244` to the script's `ENUMS` (`derive_axml_anchors.py:43-51`) and an enum-block-span line (`enum block : 237-253`), or label both numbers "recorded, not derived" |
| 157 | "S038's enum block (**lines 237-253**)" | 237 unguarded | same fix |
| 184 (Q13 row) | "**n/a by construction** — no verifier, recheck command … credited … beyond the entry's own readout recheck" | n/a (self-contradictory: it names the credited readout recheck and the derive recheck above) | Q13 applies; decision must be `pass` **only** after the credit is bounded (or the script extended) and `237`/`244` are named unguarded |
| 194 | "exit 0, **17 lines, one per cited symbol**" | 17 lines are 1 digest + 16 symbols; the entry cites 18 S038 numbers | "17 stdout lines = 1 snapshot-digest line + 16 symbol lines; `237` and `244` are not derived" |
| 148/125 | "the derivation above is the capture that makes it mechanical" | the capture covers 16/18 cited numbers | bound the sentence, or extend the script |

Related (adjacent Q11 surface, reported but not claimed as my criterion): the same `237`/`244` values are correct yet carry no derivation, so entry:125's "no spec line number in this entry is transcribed by hand" is also false for them.

## Secondary finding (same criterion, lower severity)

entry:7 credits the per-value form "`--fact '<id>'` prints the single JSON line for one named fact". A wrong/absent id is silent:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact nosuchfact; echo EXIT=$?; python3 -B … --fact nosuchfact | wc -l
EXIT=0
0
```

`--fact eocd` (the instance cited at entry:194) does print its one line (verified). So the form's run cannot detect a deleted or mistyped fact id; the credit should say "exits 0 with empty stdout for an unknown id — the id is not checked", or the aggregate 15-line hash is the only guard.

## Residual risk

- LOW: this FAIL is about credit scope, not about wrong anchor values. `237` (`enum {`) and `244` (`RES_XML_FIRST_CHUNK_TYPE`) are both correct on the pinned snapshot — verified directly above — and every printed anchor (218, 239, 241, 245, 246, 247, 248, 253, 287, 461, 612, 621, 677, 686, 687, 707) was re-derived live in this seat. The r67 `:244`→`:245` repair itself holds.
- LOW: the fix is mechanical and small (two `ENUMS`/span additions to the derive script, or five scope-sentence edits plus a `Q13` row rewrite). Since the script's stdout is embedded verbatim in the entry, extending the script changes a gate-checked block and must be done with the block updated in the same revision.
- OUT OF SCOPE but coupled: if the wave adjudicates Q13 FAIL on these bytes, claims.md §C2's kill rule applies (`the C05 row stays uncovered`, entry marked `rejected`). I make no admission recommendation beyond this criterion.

## Verification gaps

- I did not re-run the counter (`reports/round-68/measure.py`) or the census; no Q13 decision depends on them.
- `corpus/check_embedded_outputs.py --self-test` printed its docstring and exited 0 in my invocation (flag not handled the way I passed it); the C7 surface is the C7 seats' criterion, so I used `--entry` only.
- The `describe`/`--fact` coverage above is limited to the ids I exercised (`eocd`, an unknown id); I did not enumerate every fact id.
- No independent second derivation of the AXML anchors from the upstream URL was made (no network); the pinned snapshot bytes plus the live script run are the ground truth used.

## Tooling record

No installs or upgrades. Used only `python3` (stdlib), `git archive` into `/tmp` copies, `awk`/`diff`/`sha256sum`. Pacman host-wide pause respected: no `-S`/`-Sy`/`-Syu`/`-U`/`-R` was issued. All mutation experiments ran on `/tmp/r68q13*` copies; the lane tree was never written.

## Reproduce this seat's checks

```sh
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
python3 -B corpus/derive_axml_anchors.py | wc -l          # 17 (1 digest + 16 symbols)
python3 -B corpus/fixtures/apk-r65/readout.py | sha256sum # 507d79f8…  (15 lines)
awk 'NR==237||NR==244{printf "%d|%s\n",NR,$0}' corpus/snapshots/ResourceTypes.h
grep -n "RES_XML_FIRST_CHUNK_TYPE" corpus/derive_axml_anchors.py   # no match -> 244 not derived
# deletion sensitivity of the two clauses (copy tree in /tmp, never the lane):
#   falsify entry:148 (237->236, RES_XML_FIRST_CHUNK_TYPE->RES_XML_TABLE_TYPE)
#   python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md
#   -> checked_blocks=17 problems=0  (survives)
```
