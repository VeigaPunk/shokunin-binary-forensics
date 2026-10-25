PASS — Q07: no sentence in the landed entry predicts a parser's accept/refuse/cause; item 8 (the Q07 repair site) describes only this readout's arithmetic and namespace resolution, every clause resolving to a verified source literal, and the one spec semantic it leans on (`attributeStart` counted from the attrExt start) is printed by item 11.

seat: R70W2GateQ07 (fresh, wave 2) · target: `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` (`admission-status: candidate`) · criterion judged: Q07 only (`corpus/QUALITY.md:19`) · base for no comparison needed · bytes judged are the commit's bytes, extracted with `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd corpus SHONEN.md SCORECARD.md SKILL.md | tar -x -C /tmp/revenger-r70-R70W2GateQ07` (scratch, deleted after this report).

Q07 as frozen: *"A predicted parser behavior (accept, refuse, cause) is a pre-registered hypothesis with spec-derived ground truth and is recorded whichever way it falls. A cause is stated only once independently reproduced. | reject when: a prediction is written as fact, or an unreproduced cause is used as support."*

## 0. Re-derivation of every embedded output (the ground for everything below)

All 24 `$` commands in the entry were re-run from the extraction, each embedded line compared with that command's actual stdout:

```
$ python3 - <<'EOF'   # per-command comparison harness (scratch)
... for each "$ cmd" line: subprocess.run(cmd); embedded lines must be in stdout.splitlines()
EOF
line 26: OK rc=0 embedded=1 actual=1 :: readout.py --fact archive
line 33: OK ... line 35: OK ... line 42: OK ... line 44: OK ... line 46: OK ...
line 57: OK ... line 66: OK ... line 75: OK ... line 82: OK ... line 89: OK ...
line 91: OK ... line 93: OK ... line 95: OK ... line 104: OK ... line 113: OK ...
line 122: OK rc=0 embedded=20 actual=20 :: corpus/derive_axml_anchors.py
line 143: OK rc=0 embedded=6 actual=6 :: entry_checks.py --spec-quotes
line 155: OK rc=0 embedded=20 actual=20 :: entry_checks.py --zip-layout
line 181: OK rc=0 embedded=34 actual=34 :: entry_checks.py --oracle
line 221: OK rc=0 embedded=10 actual=10 :: entry_checks.py --pins
line 237: OK rc=0 embedded=1 actual=1 :: entry_checks.py --stdout-digest
line 244: OK rc=0 embedded=3 actual=3 :: entry_checks.py --container
line 253: OK rc=0 embedded=24 actual=24 :: entry_checks.py --axml-layout
cmds: 24 bad: 0
$ python3 -B corpus/fixtures/apk-r65/readout.py | sha256sum ; ... | wc -l
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -
15
```
Item 15's `readout stdout: 15 lines, sha256 507d79f8…` is therefore an observed value, not a transcription. No statement in the entry about *what the readout printed* is unsupported (Q07's first sentence concerns predictions; the observation half is fully reproducible).

## 1. Item 8 (entry:86) — the prime suspect — describes the readout, and every clause resolves

```
$ awk 'NR==22||NR==166||NR==203||NR==211 {printf "%d: %s\n", NR, $0}' corpus/fixtures/apk-r65/readout.py
22: NO_INDEX = 0xFFFFFFFF
166:          utf8=bool(flags & 0x100), sorted_flag=bool(flags & 0x1),
203:         aoff = base + 16 + attribute_start + i * attribute_size
211:             "ns_index": ans, "ns": None if ans == NO_INDEX else strings[ans],
```

| entry:86 clause | type | evidence (reproduced) |
|---|---|---|
| "the readout computes `aoff = base + 16 + attribute_start + i * attribute_size` (`readout.py:203`)" | readout behavior | `readout.py:203` is that literal, above |
| "the literal 16 equals the chunk's declared `headerSize` in item 4 and the `node_header_size` item 5 sums (an inference, labeled in the inference section)" | labeled inference | item 4 prints `{"headerSize": 16, "offset": 272, "size": 96, "type": 258}`; item 5 prints `"node_header_size": 16`; line 283 (b) is the label |
| "S038's comment on `attributeStart` … says the offset is counted from the start of the attrExt structure" | spec-derived ground truth | item 11 prints `comment attributeStart : 686` and the `--spec-quotes` line `MATCH ResourceTypes.h: first line 686, folded phrase present=True: Byte offset from the start of this structure where the attributes start` — both re-run above |
| "The readout resolves each attribute's namespace prefix string by indexing the string pool directly with the attribute's own `ns_index` (`readout.py:211`, `strings[ans]`; `NO_INDEX` 0xFFFFFFFF at `readout.py:22` resolves to null)" | readout behavior | both literals above; printed result `"ns": "android", "ns_index": 0` / `"ns": null, "ns_index": 4294967295` (item 8, re-run) |
| "The start-namespace chunk is printed as a separate fact and the readout does not consult it when resolving attribute namespaces" | negative readout behavior | `grep -n "start_namespace\|ns_uri\|namespaces\|prefix" corpus/fixtures/apk-r65/readout.py` → only `178: for label, ctype in (("start_namespace", 0x0100), ("end_namespace", 0x0101)):`, `180: prefix = u32(axml, ch["offset"] + 16)`, `183: prefix_index=prefix, prefix=strings[prefix],`; the start-element path `readout.py:190-215` never references that block |

No clause of item 8 asserts what an AXML parser (Android's `ResXMLTree`, aapt, apktool, JADX) does with these bytes; the v4 wording that described parser-side namespace-stack resolution is gone and replaced by the readout's own index arithmetic, which I verified line by line.

## 2. The inference list (entry:283) is labeled, and each item carries byte evidence

`(a)` chunk `type` value equals the printed S038 enum line — labeled inference, item 4 (`entry:61`) already refuses value-alone identification; `(b)` the literal 16 — see table above; `(c)` the two non-zero resource-map ids equal `truth.json`'s — item 13 prints `MATCH axml.resource_ids: readout=[…'0x0101021b', '0x0101021c'…] oracle=[…]` (re-run); `(d)` the dex header fields agree with S048's quoted semantics — item 11 prints the four `MATCH dex-format.html` phrases (re-run). Item 7 (`entry:79`) refuses a meaning for the zero resource-map entries; `entry:101` says a declared/recomputed match "shows the member's header is internally consistent, and nothing about dex program validity follows". Nothing here is a prediction written as fact.

## 3. Falsification attempts that failed (recorded so no seat re-litigates them)

- **A — treat `entry:288` "is not a valid dex program (the generator's own docstring, `generator.py:8`)" as a refuse prediction.** Rejected as a Q07 finding: the sentence is a conformance statement about the artifact, not an assertion about what a parser will do, and it is spec-derivable and true — `sed -n '6014,6020p' corpus/snapshots/dex-format.html` prints `map_off … offset from the start of the file to the map item. The offset, which must be non-zero`, and the fixture's header has `map_off 00000000 0` (my `zipfile`+`struct` read of `classes.dex`, bytes 52-55). See note N1 — it is a Q01/Q10/Q11 form problem, not mine.
- **B — treat item 8 as parser prose.** Rejected by the table in §1.
- **C — look for an unlabeled prediction in the inference list.** Rejected: all four are under `- **Inference** —` with byte evidence and a fixture scope.
- **D — look for an unreproduced *cause* (M12 class).** The only causal sentence is `entry:288` "the readout reads no compression method or flag byte itself, so the walk does not exercise compression, split archives or spanned records" — verified true: `grep -n "method\|compress\|zlib" corpus/fixtures/apk-r65/readout.py` returns only `17:import zlib` (used for `crc32`/`adler32` at `:115-116`, `:241-242`), the AXML pool `flags` at `:152`/`:165`/`:166`, and the payload slice `:106 payload = apk[payload_off:payload_off + compressed_size]` — no ZIP method/flag read, no decompression call. Independently reproduced.
- **E — look for provider/parser readiness prose.** `entry:1` ("not the behavior of any parser"), `entry:4` ("no ZIP-parser or provider behavior is claimed"), `entry:10` ("Not covered: … provider (`inspect_android_package`) readiness or output, general AXML or ZIP-parser behavior"), `entry:292` ("this lane ran no provider and makes no readiness claim") — fences, not predictions.

## 4. Cross-criterion notes (located, for the Q01/Q03/Q10/Q11/Q13 seats — NOT Q07 decisions)

- **N1 — `entry:288`, Q01/Q10/Q11.** "The dex member is a header only and is not a valid dex program (the generator's own docstring, `generator.py:8`)." The invalidity half is a conformance conclusion whose in-entry support is author prose, and the entry's own fences say validity is not covered (`entry:10`), does not follow from the checks (`entry:101`), and is not claimed (`entry:284`). I confirmed the conclusion is true and spec-derivable (S048 snapshot `dex-format.html:6014-6018` `map_off … must be non-zero`; fixture `map_off = 0x00000000`). Smallest safe correction (prose only, no block changes): print the `map_off` derivation, or attribute the sentence in reported speech — "the generator's docstring declares the member header-only and not a valid dex program (`generator.py:8`); this entry does not test validity."
- **N2 — `entry:72`, Q11 (and a Q04/Q13 look).** "the UTF-8 flag position tested is `flags & 0x100`, `readout.py:166`" — `0x100` is S038's `UTF8_FLAG = 1<<8` (`sed -n '474,482p' corpus/snapshots/ResourceTypes.h` → `UTF8_FLAG = 1<<8`), and item 11 does not print it: `python3 -B corpus/derive_axml_anchors.py | grep -c UTF` → `0`, while `entry:1` promises "every S038 line number and enum value this entry states is printed by the item-11 command". The number itself is a readout literal and verified at `readout.py:166`; whether the flag's *semantics* counts as an "S038 enum value this entry states" is the Q11 seat's call. Related: `readout.py:157-160` decodes every string as UTF-8 unconditionally (`axml[base + 2:base + 2 + u8len].decode("utf-8")`) — the printed `utf8` field reports the flag and does not branch the decoder, which a Q04/Q13 seat may want to weigh against item 6's wording.
- **N3 — `entry:61`, Q03.** "the chunk at offset 248 is identified as the start-namespace chunk by the item-8 `axml_start_namespace` fact, not by its value alone" — that fact is produced by the same value match (`readout.py:178` `for label, ctype in (("start_namespace", 0x0100), ("end_namespace", 0x0101)):` → `:181 ch = next(c for c in chunks if c["type"] == ctype)`), so it cannot be the independent identifier the sentence claims. The chunk's payload does corroborate (printed `prefix: "android"`, `uri: "http://schemas.android.com/apk/res/android"`), and item 11 prints both `RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100` and `RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100`. Reported, not decided.

## 5. Decision

Q07 = **PASS** on the landed bytes. It is a PASS on the criterion only; it does not override any mechanical label, and it does not touch C1's other conjuncts. Nothing here is a kill-rule input. Notes N1-N3 are handed to the seats that own Q01/Q03/Q10/Q11/Q13 — each is located (`entry:LINE` + reproduced command output) and none is a Q07 parser-behavior prediction.

Tooling: no install or upgrade used — `git` (read-only `archive`/`show`), `python3` 3.14.8 stdlib only. No lane file, report, or git object was written; all mutations (none) stayed in `/tmp/revenger-r70-R70W2GateQ07`, deleted before returning.
