PASS — Q10: every finding in `corpus/knowledge/round-68-apk-axml-byte-evidence.md` is scoped to one authored APK fixture, one manual stdlib readout, pinned spec versions and named inputs, and the kaidoku/revenger ADJ-06 contest is reported (fleet `.ufo/l0-questions.md:42`) rather than absorbed; no single-fixture observation is stated as a universal.

# R68ReviewEntryQ10 — Q10 on the C05 v3 candidate

Seat: `L1Revenger68.R68ReviewEntryQ10` · criterion: **Q10 only** ("A finding is scoped to the observed family, operation, version and input. Cross-lane contested scope is reported, not absorbed." reject when "one family's observation is stated as a universal").
Record under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-68-apk-axml-byte-evidence.md` (215 lines, `admission-status: candidate`).
No file was edited. No git/jj mutation was run. No subagent was spawned.

## Verdict

**PASS.** The four scope dimensions hold on the bytes, and the cross-lane fence resolves to a live fleet ledger item that the entry does not absorb. Adjacent defects exist but none of them is carried by Q10 (listed under §Adjacent observations with their own criterion ids, not as Q10 verdicts).

## Evidence (my own re-derivation, not the entry's Q-map)

### E1 — operation scoping is true: manual, stdlib, single input, no producer/network

`entry:13` claims: *"The analysis is **manual**: a Python standard-library script reads the archive's bytes with `struct` … Nothing is extracted to disk, nothing is executed, no producer is called, no network is used, and no verifier source is read."*

```
$ grep -nE "^import|^from" corpus/fixtures/apk-r65/readout.py
13:import hashlib
14:import json
15:import struct
16:import sys
17:import zlib
18:from pathlib import Path

$ grep -n "APK = \|APK.read_bytes" corpus/fixtures/apk-r65/readout.py
20:ROOT = Path(__file__).resolve().parent
21:APK = ROOT / "fixture.apk"
44:    apk = APK.read_bytes()
```

No `subprocess`, `socket`, `urllib`, `requests`, `zipfile`, and no `open(` for writing; the string `truth.json` does not occur in the script (`mentions truth.json: False`). So the readout operation is in-memory over exactly one named input, `fixture.apk`, digest `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` / `92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976` script — both equal `corpus/SOURCES.md:55` (S041) and `entry:1`/`entry:17`. The operation dimension is not over-claimed: the readout never reads the oracle it is compared against.

### E2 — version scoping is stated and pinned for every spec the entry uses

`entry:1` pins S038 to `refs/tags/android-15.0.0_r1` plus snapshot sha256; `corpus/SOURCES.md:52` scopes that row *"this tag only"*; `SOURCES.md:46`/`:48` pin APPNOTE **6.3.10** (matching `entry:13` "APPNOTE 6.3.10 fixed record widths"); `SOURCES.md:57` pins `rea-agents-6.5.0`; S045 carries its own snapshot digest. Two committed copies of the snapshot are byte-identical:

```
$ sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
$ stat -c '%s %n' corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
86255 corpus/snapshots/ResourceTypes.h
86255 .ufo/waves/round-65/source-snapshots/ResourceTypes.h
```

### E3 — input version is true: fixture bytes unchanged since round 65

`entry:6`: *"the fixture, oracle and readout bytes are the round-65 claim-tree bytes, unchanged since `c7b7cf98`"*; `entry:9`: *"unchanged since round 65"*.

```
$ git diff --stat c7b7cf98..HEAD -- corpus/fixtures/apk-r65/
(no output)
$ git log --oneline -- corpus/fixtures/apk-r65/
c7b7cf9 round-65: candidates — apk-r65 fixture+readout, C05 candidate entry, S038-S041 rows, C5 forged-evidence controls, lesson+wave spec (no README flip)
```

The version claim is a byte claim about the named commit, and it holds.

### E4 — the spec line numbers this verdict relies on re-derive to the entry's values

```
$ python3 -B corpus/derive_axml_anchors.py   # exit 0, 17 lines
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
```

Byte-compared against `entry:127`–`146` (the 17 output lines are `entry:129`–`145`): the 17 output lines are identical (the entry block adds only the `$ python3 -B corpus/derive_axml_anchors.py` prompt line at `entry:128`). `sha256sum corpus/derive_axml_anchors.py` = `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`, equal to `entry:4` (S046). I also read the snapshot directly: line 244 is `RES_XML_FIRST_CHUNK_TYPE` and 245 is `RES_XML_START_NAMESPACE_TYPE`.

```
$ python3 -B corpus/fixtures/apk-r65/readout.py   # exit 0, 15 lines, stderr empty
$ sha256sum /tmp/q10_readout.txt
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```

That is exactly the `recheck:` contract at `entry:7` and `entry:194`.

### E5 — cross-lane contested scope is reported, not absorbed

`entry:166` (§Cross-lane scope note):

> The provider route (`inspect_android_package`, JADX prerequisites) is documented scope from S043 only; this lane ran no provider and makes no readiness claim (Q05 fence). The kaidoku/revenger ADJ-06 overlap and fleet `l0-questions.md:42` remain reported-not-absorbed, unchanged from round 64.

The pointer resolves, and the contest is real and still open:

```
$ awk 'NR==42' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md
tsukuroi | round-1 | Ratify the explicitly steered fleet round-1 namespace … and arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed? …
```

No resolution is recorded on that line, so "reported-not-absorbed / unchanged" is accurate. The other side of the contest is live: `revenger-shokunin/PROVINCE.md:3` ("Owns: reverse engineering of shipped artifacts") and kaidoku's corpus carries the provider-side APK knowledge (`kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-apk-inventory.md:103`: `"provider_id": "jadx"`, `operation: "inspect_android_package"`). The entry takes none of it: `entry:166` fences the provider to S043 documentation scope and `entry:8` fences "provider (`inspect_android_package`) readiness or output". No kaidoku observation is restated as this entry's own.

### E6 — no observation is stated as a universal

Family, operation, version and input are fenced at the points where a reader would over-generalize:

- `entry:13` — "One authored APK … one authored binary", manual, no producer.
- `entry:75` — "the all-zero entries are recorded as observed, and **no framework-wide semantics for a zero entry is claimed from this fixture**".
- `entry:8` — coverage-map: "Not covered: install/signature verification, dex validity or execution, provider … readiness or output, **general AXML or ZIP-parser behavior beyond this fixture**".
- `entry:162` — "Generalization to other APKs, other AXML producers or the `inspect_android_package` provider would need its own evidence."

The only `all`-scoped sentences in the file are about the three members of *this* archive (`entry:35`) or an explicit disclaimer. Nothing states one fixture's behaviour as an AXML/ZIP/dex universal.

### E7 — no coverage row is silently absorbed

```
$ grep -n "C05" corpus/README.md
34:| C05 | Android packages (APK) | — | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` … | uncovered |
```

The row is still `uncovered` and does not name this file, consistent with `entry:9` (`admission-status: candidate`) and the frozen order in `reports/round-68/claims.md` §C2. The entry's own `coverage-map` (entry:8) names C05 without claiming it is filled.

## Findings

**Blocking Q10 findings: none.**

Ordered adjacent observations, each with the criterion that actually carries it — **not** Q10 verdicts, and none of them changes this verdict:

1. **[medium · Q11/Q08]** `entry:1`, `entry:57` and `entry:148` call lines **237-253** "the chunk-type enum block" (`entry:148` verbatim: "The chunk-type enum block spans lines 237-253"). In the pinned snapshot the `enum {` opens at **237** and the closing `};` is at **263** (`awk` read of `corpus/snapshots/ResourceTypes.h:237-263`). The substantive point — that `RES_XML_RESOURCE_MAP_TYPE` at :253 is *inside* the enum, unlike the round-65 draft's `:239-250` — is true, because 253 < 263. But the stated span is 10 lines short of the block it names, and no command prints any span: item 11 derives 7 individual symbols only. If the span is meant literally, the correct value is **237-263**; if the intent is "the range of the cited string-pool/XML chunk-type lines", that is what the text should say.
2. **[medium · Q04/Q11]** `entry:17`: *"Every numbered item below is produced by the readout in §Reproduce."* Item 11 is produced by `corpus/derive_axml_anchors.py`, not by `readout.py` — `entry:125` says exactly that. §Reproduce names both commands, so the reader can recover the truth, but the preamble credits one script with another script's output.
3. **[low · Q11]** `entry:68`: "bit `0x100` set, the UTF-8 flag position the readout tests (`flags & 0x100`, readout.py:166)". The value and the pointer are correct (`readout.py:166` is `utf8=bool(flags & 0x100)`; snapshot `ResourceTypes.h:479-480` is `// String pool is encoded in UTF-8` / `UTF8_FLAG = 1<<8`), but `UTF8_FLAG` is not one of the 17 derived anchors, so this spec constant carries no in-entry derivation.
4. **[low · Q01/Q02]** `entry:3` says S045 was "opened 2026-10-24 **by this entry's author**"; `corpus/SOURCES.md:91` records `Opener: L1 revenger-r67`. The round-68 author did not open that row.
5. **[low · Q10-adjacent, reported]** `entry:4` cites **S046** as the anchor-derivation row; `corpus/SOURCES.md:99` records *"S046 collides with the shokuknow package's staged S046 space; the by-document renumber obligation (recorded in round 67) stands — the lane's own ids follow the document."* The contest is reported in the lane registry (the place S### ids are defined) but not restated in the entry's `source:` row. Because the entry makes no shokuknow claim and the collision is an identifier-space contest rather than a finding-scope contest, Q10's "reported, not absorbed" requirement is satisfied at lane level; the cross-lane resolution hazard for a reader looking up "S046" remains.
6. **[environmental, not a criterion]** Working tree carries untracked `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc` (9356 bytes, mtime `2026-10-25 03:29`), produced by a seat running the C7 gate without `-B`. It does not affect `git archive`-based counting, but it must not be committed: `reports/round-68/claims.md` §Void conditions allow exactly one new corpus path (`corpus/snapshots/`). I did not touch it (it is not mine and may be another seat's).

## Residual risk

- **Tag-content identity is not verified.** I proved the two committed snapshot copies are byte-identical and 86255 bytes, matching `entry:1`/`entry:4` and `SOURCES.md:52`. I did **not** verify those bytes are the `android-15.0.0_r1` content (no network; origin is the domain Q09 explicitly excludes). The entry's version scoping therefore rests on the pin it states, which is the correct posture, not on a re-fetch.
- **The Q-map Q10 basis under-describes the entry** (`entry:181`: "one fixture, one operation (manual readout), one artifact version"). The entry actually runs two operations over two inputs — the readout over `fixture.apk`, and the anchor derivation over `corpus/snapshots/ResourceTypes.h`. Both are scoped where they are stated (`entry:13`, `entry:125`), so the criterion holds; only the self-map summary is incomplete. I did not treat the self-map row as evidence for this verdict.

## Verification gaps

- `generator.py` was not re-run (the entry states it is not; round-65 evidence only).
- Kaidoku's provider corpus was surveyed by `grep` (filenames and line heads), not read end to end; the ADJ-06 *status* was verified at the fleet ledger (`.ufo/l0-questions.md:42`), not by re-adjudicating it — outside this seat's authority.
- No network access was used, so no upstream AOSP/DEX page was re-fetched.

## Entry lines at issue

`1` (S038 tag + "enum block 237-253" + snapshot pin), `3` (S045 opener attribution), `4` (S046 row / id collision not restated), `6` (`verified-at` "unchanged since c7b7cf98"), `7` (recheck contract — exact), `8` (coverage-map fences), `9` (admission-status candidate), `13` (Scope: family/operation/version/input), `17` (preamble over-attributing item 11), `57` (chunk-type → enum block 237-253), `68` (UTF-8 flag position), `75` (framework-wide disclaimer), `127`–`146` (item 11 block; 17 output lines at 129–145, byte-identical to my run), `148` (enum block span restated with the :245/:244 correction), `152` (oracle comparison), `162` (§Limitations generalization fence), `166` (§Cross-lane scope note: ADJ-06 + `l0-questions.md:42`), `181` (Q10 self-map row).

No tool was installed or upgraded for this seat.
