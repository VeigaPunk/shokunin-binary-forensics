FAIL — Q05 on this entry: the load-bearing capability claim at entry:125 ("**every** S038 line number this entry states is printed by a committed derivation script … no spec line number in this entry is transcribed by hand", repeated in scope form at entry:4 for S046 and in the recheck at entry:7) is false on its own probe: the script's actual stdout is 17 lines and contains **neither 237 nor 244**, while the entry states both (`lines 237-253` at entry:1, :57, :148, :157; `line 244 is RES_XML_FIRST_CHUNK_TYPE` at entry:148). Stated capability outruns the probe that is offered for it. The two *values* are correct against the bytes; the capability claim about the derivation's coverage is not. Second, milder leg: the exit-2 guard claim (entry:4, :7, :125) carries no observed exit or output anywhere in the entry.

Criterion: **Q05** — "A readiness or capability claim carries a probe against the real surface: its command, date and observed exit, output or Evidence ID. Presence, configuration or acquisition is not capability." (`QUALITY.md:27`; lesson classes M01 (`lessons/round-1.md:38`) and M19 (`:56`), both about readiness asserted without a probe.)

Entry under test (`corpus/knowledge/round-68-apk-axml-byte-evidence.md`): 215 lines, sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b`, `admission-status: candidate` (entry:9). Lane tree at `git rev-parse HEAD` = `4232235723cf8d4731a1e7e78ca098b8af953a57`, `git status --porcelain corpus/` empty. Reviewer scope: Q05 only; no other criterion is scored here.

# 1. What the entry claims, and what each claim's probe shows

| claim | entry line(s) | probe carried | verdict |
|---|---|---|---|
| readout: exit 0, 15 stdout lines, sha256 `507d79f8…` | :7 (recheck), :194 (§Reproduce) | command + date 2026-10-24 + observed exit 0 + output digest | **satisfied** — reproduced exactly (§3) |
| derivation: exit 0, 17 lines | :4, :125, :128-145 (embedded stdout), :194 | command + full stdout embedded | **satisfied** — reproduced exactly (§3) |
| snapshot is a byte-exact copy of the pinned snapshot (`56b88bc4…`) | :1, :4, :125 | digest printed as the script's own line 1; digest also pinned in S046 | **satisfied** — reproduced; byte-identical to `.ufo/waves/round-65/source-snapshots/ResourceTypes.h` (§3) |
| "**every** S038 line number this entry states is printed by a committed derivation script … no spec line number in this entry is transcribed by hand" | :125 (claim), :4 (S046 scope), :7 (recheck parenthetical) | the 17-line stdout at :129-145 | **FAILS** — 237 and 244 are stated by the entry and absent from that stdout (§2) |
| "the script refuses to print a line it did not find (a missing or ambiguous symbol is exit 2)" | :4, :7, :125 | none — no command run of the guard, no exit, no output | **fails as carried** — true in fact, but the entry offers no probe (§4) |
| provider route is documented scope only, no readiness claim | :166 (Cross-lane note) | S043 doc scope, explicitly not executed | **satisfied** — correctly fenced; no M01-shaped provider claim |

# 2. The failing leg — the coverage claim is refuted by its own embedded probe

Commands and actual output (lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`):

```sh
python3 -B corpus/derive_axml_anchors.py; echo "EXIT=$?"
```
```
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

```sh
python3 -B corpus/derive_axml_anchors.py | wc -l                      # 17
python3 -B corpus/derive_axml_anchors.py | grep -E ': (237|244)$' || echo "NEITHER 237 NOR 244 PRINTED"
```
```
17
NEITHER 237 NOR 244 PRINTED
```

Printed set: `{218, 287, 461, 612, 621, 677, 686, 687, 707, 239, 241, 245, 246, 247, 248, 253}` + the digest line. Stated-but-unprinted: **237** and **244**.

Entry lines at issue (verbatim fragments):

- `:125` — "11. Every S038 line number this entry states is printed by a committed derivation script that searches the pinned snapshot bytes for each cited symbol — **no spec line number in this entry is transcribed by hand**."
- `:4` — S046 scope: "the machine derivation of **every** S038 line number this entry cites, read from the pinned snapshot bytes".
- `:7` — recheck parenthetical: "(`python3 -B corpus/derive_axml_anchors.py` … **every S038 line number this entry cites**; exits 2 if a cited symbol is missing or ambiguous)".
- `:148` — "The chunk-type enum block spans lines **237-253** … **line 244 is `RES_XML_FIRST_CHUNK_TYPE`.**"
- `:1` (S038 source row) and `:57`, `:157` — repeat "chunk-type enum block **lines 237-253**".

Which numbers are wrong: **none of the numeric values.** Both are correct against the pinned bytes:

```sh
sed -n '237p;244p' corpus/snapshots/ResourceTypes.h
```
```
enum {
    RES_XML_FIRST_CHUNK_TYPE          = 0x0100,
```

What is wrong is the **capability claim**, and its correct value/statement is one of:

1. **Derive them (preferred, keeps the round-68 invariant).** Extend `corpus/derive_axml_anchors.py` with two predicates that are unique in these bytes — `^enum \{` matches exactly once (line 237) and the declarative `RES_XML_FIRST_CHUNK_TYPE          = 0x0100,` matches exactly once (the bare symbol does **not**: it also occurs at line 734 as `FIRST_CHUNK_CODE = RES_XML_FIRST_CHUNK_TYPE,`, `grep -c` = 2, so a naive symbol search would be ambiguous and exit 2). Re-embed the resulting 19-line stdout and update every "17 output lines"/"17 lines" occurrence (`:4`, `:7`, `:125` block, §Reproduce). Then `:125`, `:4` and `:7` become true as written.
2. **Narrow the claim.** Restate `:125`/`:4`/`:7` as "the 16 symbols in item 11's table plus the snapshot digest are printed by the script; `237` (the `enum {` line) and `244` (`RES_XML_FIRST_CHUNK_TYPE`) are recorded from the pinned snapshot bytes at `corpus/snapshots/ResourceTypes.h` and are not printed by it" — i.e. label them recorded, not derived, exactly as Q11's last clause requires.

Either repair is textual/mechanical; the defect is that the entry currently asserts a derived status it does not show. This is precisely the M01/M19 shape the criterion targets: the *presence* of a committed derivation script (and of a passing run for other symbols) is being taken as capability for the whole class of anchors the entry states.

# 3. Positive legs that do satisfy Q05 (so the FAIL is narrow, not a blanket rejection)

```sh
out=$(python3 -B corpus/fixtures/apk-r65/readout.py); rc=$?
printf '%s\n' "$out" | wc -l; printf '%s\n' "$out" | sha256sum; echo "EXIT=$rc"
```
```
15
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -
EXIT=0
```
Exactly the 15 lines / exit 0 / digest the entry claims at `:7` and §Reproduce — no transcription drift.

```sh
sha256sum corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h corpus/fixtures/apk-r65/readout.py corpus/fixtures/apk-r65/fixture.apk
.ufo/waves/round-65/source-snapshots/ResourceTypes.h
```
```
bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
```
Every digest S046/`source:` states matches the bytes; `corpus/snapshots/ResourceTypes.h` is committed (`git ls-files corpus/snapshots/` → `corpus/snapshots/ResourceTypes.h`), so the derivation also runs from a `git archive` tree — that capability claim (claims.md §C2 item 4, "so the derivation runs from any corpus tree") holds.

Not an M19 case: the `generator.py` re-run is **disclosed** as round-65 evidence and explicitly "*is not re-run by this entry*" (`:152`), and no current value rests on it (the fixture digest is probed now at `:21`). That disclosure is the correct treatment; no finding here.

# 4. Second leg — the exit-2 guard is claimed but never probed in the entry

The entry asserts the guard three times (`:4`, `:7`, `:125`) with no command run, exit code or output for it. Presence of the code path is not capability under Q05. I probed it on scratch copies under `/tmp` (lane files untouched), pinning the digest to the mutated bytes so the digest guard would not mask the symbol guards:

```sh
# variant A: RES_STRING_POOL_TYPE renamed away
python3 -B /tmp/q05b/d_A.py; echo "EXIT=$?"
# variant B: RES_XML_RESOURCE_MAP_TYPE duplicated
python3 -B /tmp/q05b/d_B.py; echo "EXIT=$?"
# variant C: unmodified-pin script against a byte-modified snapshot
python3 -B corpus/derive_axml_anchors.py; echo "EXIT=$?"
```
```
derive_axml_anchors: enum RES_STRING_POOL_TYPE: not found
EXIT=2
derive_axml_anchors: enum RES_XML_RESOURCE_MAP_TYPE: ambiguous (2 hits at [253, 254])
EXIT=2
derive_axml_anchors: snapshot digest 05018d3d2ec5a19a21c7e8827b34c783a6c9cd356b3663a757abf37c40af47b6 != pinned 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f
EXIT=2
```

So the guard is real and it does refuse to print a partial table (variant A fails on the 9th symbol with no table emitted). The claim is therefore **true but unprobed** — the repair is to embed one of these runs (command + observed exit 2 + its one-line stderr/stdout message) in item 11, not to retract anything. That is Q05's positive requirement: "its command, date and observed exit, output". Without it, a reader cannot distinguish this guard from an exit-2-on-anything path.

# 5. The entry's own Q05 row is wrong in its stated basis

`:176` — `| Q05 | pass | no readiness or capability claim is made; §Cross-lane scope note fences the provider route to S043 documentation scope. |`

The provider fence is correct and deserves credit, but "no … capability claim is made" is false: the entry makes capability claims about two committed scripts (exit 0 / line counts / output digests, and the exit-2 guard) and about the derivation's coverage of *every* stated anchor. A Q05 decision resting on the premise "no capability claim exists" is not a Q05 pass; the criterion has to be applied to the claims that do exist, which is what §2 and §4 do.

# 6. Cross-check against the sibling anchor seat (divergence is real, not a contradiction)

`.ufo/waves/round-68/R68AnchorDerive.md:1` heads PASS and credits "*every* … line number … **reproduced exactly by `corpus/derive_axml_anchors.py`** (exit 0, 17 lines)"; its own table then confirms `237` and `244` by **direct line extraction** (`:76`, `:79`, `:95`, `:111`) — i.e. its PASS is a statement about the **values**, which I independently confirm as correct. It leaves `:244` unaddressed as to *provenance*. My finding does not contest the values; it contests the entry's claim that the script prints them. Both statements are true simultaneously: values correct (Q03/Q11 territory), capability claim over-broad (Q05).

# 7. Consequence and residual risk

- Per `reports/round-68/claims.md` §C2 kill rule, a Q FAIL on the v3 bytes is fatal to C2 as frozen: the C05 row stays `uncovered`, the v3 entry is marked `admission-status: rejected`, and C2 is reported FALSIFIED. I am not applying that rule — I am reporting the single criterion decision it keys on. The repair in §2 is small and does not touch fixture, oracle or readout bytes.
- Residual risk not scored here (reported, not absorbed): the behavioural claims "Nothing is extracted to disk, nothing is executed, no producer is called, no network is used" (`:13`) are supported only by the readout's output digest, which does not by itself evidence the absence of network access — a Q13-style credit question for whichever seat owns it. The scan-able script is committed (`92e347c3…`), so this is checkable, not unknown.
- Verification limits: I ran the entry's two recheck commands and three negative-control variants; I did not run the round-68 counter (out of scope, another seat) and did not read the pinned AOSP bytes remotely — the snapshot is the lane's pinned primary record and its digest matches the pin.
- Tooling record: no tool was installed, upgraded or removed for this review (no pacman/uv/npm transactions; host-wide pacman pause respected). Commands used were `python3` (stdlib), `sha256sum`, `sed`, `grep`, `git ls-files`/`rev-parse`/`status` (read-only queries only; no git/jj mutation).
