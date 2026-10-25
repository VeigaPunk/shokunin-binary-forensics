PASS — Q09 holds on the v4 bytes: every digest/receipt the entry states independently re-derives over exactly the bytes it names, no hash is offered as proof of producer origin, acquisition completeness or a valid interpretation, and the saved records are byte-preserved; the one Q09-adjacent defect is procedural (the v4 §Q-map dropped the Q09 row v3 had), reported as F1.

Seat: L1Revenger69.R69ReviewEntryQ09 · criterion Q09 only · entry
`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/knowledge/round-69-apk-axml-byte-evidence.md`
(216 lines, 35113 bytes; `admission-status: candidate`, line 11) · lane HEAD at review `35e1258` · no file edited.

# Criterion under judgment

`corpus/QUALITY.md` Q09: "A digest or receipt is claimed only for the exact bytes it hashed. It does not establish producer origin, acquisition completeness or authenticity. Saved records stay byte-preserved." Reject when "a hash match is offered as proof of origin, completeness or a valid interpretation" (M11, M13).

C1 (`reports/round-69/claims.md` §C1) makes the wave the decider: "every applicable Q01–Q15 decision of the dispatched wave on the landed v4 bytes is PASS (n/a only with the entry's named reason)". Q09 is applicable here — the entry is digest-dense — and there is no entry-named n/a reason (see F1). This report is the Q09 decision.

# 1. What I ran, and what it printed

All commands from `/home/vgpnk/Projects/shokunin/revenger-shokunin` unless shown otherwise; read-only; nothing installed (`pacman` untouched, no tool added or upgraded).

## 1.1 The six files the entry pins — sha256 of the bytes on disk

```
$ sha256sum corpus/fixtures/apk-r65/fixture.apk corpus/fixtures/apk-r65/truth.json \
    corpus/fixtures/apk-r65/generator.py corpus/fixtures/apk-r65/readout.py \
    corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
$ stat -c '%s %n' corpus/fixtures/apk-r65/fixture.apk
947 corpus/fixtures/apk-r65/fixture.apk
```

Every value matches the anchors in entry lines 6 and 7 and the "947 bytes" of line 23.

## 1.2 The entry's own recheck receipt — stdout digest `507d79f8…`

```
$ python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/revenger-r69-q09-readout.out; echo exit=$?
exit=0
$ wc -l < /tmp/revenger-r69-q09-readout.out
15
$ sha256sum < /tmp/revenger-r69-q09-readout.out
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -
```

The digest is over the stdout byte stream as emitted (trailing newline included). Stripping the newline yields a different digest (`80d65a83…`), so the entry's "15 stdout lines whose SHA-256 is `507d79f8…`" (line 9; line 194) is exactly the bytes the named command prints — not a line-set digest in disguise.

Location independence: the stdout `path` field is a literal repo-relative string (readout.py:45, `path="corpus/fixtures/apk-r65/fixture.apk"`), and a run from a copied tree prints the same bytes:

```
$ cp -r corpus/fixtures /tmp/revenger-r69-q09-tree/ && cd /tmp/revenger-r69-q09-tree && \
    python3 -B fixtures/apk-r65/readout.py | sha256sum
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247  -
```

So `507d79f8…` identifies a well-defined byte stream, not a checkout-dependent serialization — Q09's "exact bytes it hashed" clause is satisfied for this receipt. (Same property the round-65 saved entry asserts at its `recheck:`; see §3.4.)

## 1.3 The anchor derivation receipt — 20 lines, snapshot digest pinned

```
$ python3 -B corpus/derive_axml_anchors.py; echo exit=$?
sha256 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f ResourceTypes.h
struct ResChunk_header : 218
struct Res_value : 287
struct ResStringPool_header : 461
struct ResXMLTree_header : 612
struct ResXMLTree_node : 621
struct ResXMLTree_attrExt : 677
struct ResXMLTree_attribute : 707
enum block open : 237
enum RES_STRING_POOL_TYPE : 239 = 0x0001
enum RES_XML_TYPE : 241 = 0x0003
enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
enum RES_XML_START_NAMESPACE_TYPE : 245 = 0x0100
enum RES_XML_END_NAMESPACE_TYPE : 246 = 0x0101
enum RES_XML_START_ELEMENT_TYPE : 247 = 0x0102
enum RES_XML_END_ELEMENT_TYPE : 248 = 0x0103
enum RES_XML_RESOURCE_MAP_TYPE : 253 = 0x0180
enum block close : 263
comment attributeStart : 686
field attributeStart : 687
exit=0   (20 stdout lines)
```

The first line's digest is computed by the script over the file it read (`derive_axml_anchors.py:105-108`: `raw = path.read_bytes(); digest = hashlib.sha256(raw).hexdigest(); if digest != SNAPSHOT_SHA256: fail(...)`), and equals `sha256sum`'s output for `corpus/snapshots/ResourceTypes.h` in §1.1. The wave-snapshot digest claimed at entry line 6 matches too:

```
$ sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
$ stat -c '%s %n' corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
86255 corpus/snapshots/ResourceTypes.h
86255 .ufo/waves/round-65/source-snapshots/ResourceTypes.h
```

Two equal digests establish equal bytes (the "byte-exact copy" claim of entry line 6); they do not establish where those bytes came from, and the entry does not use them that way.

The entry's receipt claim "(exit 2 on a missing or ambiguous symbol)" (line 6) and the script's "(exit 2 if a cited symbol is missing or ambiguous)" (line 9) hold, tested on a scratch copy under `/tmp/revenger-r69-q09/` (lane untouched):

```
# one byte appended to the snapshot copy
derive_axml_anchors: snapshot digest 00ab5901e715a07ab07b76fd29ae3849a6c778294458e5fd64677de25507da24 != pinned 56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f
exit=2
# ENUMS extended with RES_XML_NO_SUCH_TYPE
derive_axml_anchors: enum RES_XML_NO_SUCH_TYPE: not found
exit=2
```

So the receipt the entry credits is the script's own refusal, not a claim about the snapshot's origin.

## 1.4 Independent recomputation of the member and dex digests (not via the readout)

```
$ python3 - <<'PY'   # zipfile / zlib / hashlib only
AndroidManifest.xml len 416 sha256 73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4 crc32 962d075f compress_type 0
classes.dex len 112 sha256 57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2 crc32 2635c82a compress_type 0
META-INF/MANIFEST.MF len 69 sha256 2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49 crc32 e948d738 compress_type 0
dex adler32 bytes[12:] = 0x3d120c30
dex sha1 bytes[32:] = a5fc7bea8fa9ffaa52243540c8026066511b9fce
PY
```

These match entry lines 37 (CRC-32 recompute for all three members, "payload bytes"), 109 (declared checksum over offset 12 on, declared signature over offset 32 on) and the `member[...]` fact lines. All three members are STORED (`compress_type 0`), so payload bytes = member bytes = uncompressed bytes; there is no second byte sequence a reader could take these digests to cover.

## 1.5 Embedded outputs vs live stdout — byte equality, not just value equality

Comparing every fenced block in the entry against the live stdout above, by exact string, one JSON line per fact:

```
line 27  archive: MATCH
line 34  eocd: MATCH
lines 41/43/45  member[AndroidManifest.xml] / member[classes.dex] / member[META-INF/MANIFEST.MF]: MATCH
line 56  axml_chunk_table: MATCH
line 65  spec_derived_struct_widths: MATCH
line 74  axml_string_pool: MATCH
line 81  axml_resource_map: MATCH
line 88  axml_start_element: MATCH
line 95  axml_start_namespace: MATCH
lines 102/104  axml_end_element / axml_end_namespace: MATCH
line 113  dex_declared_header: MATCH
line 122  jar_manifest: MATCH
lines 200-214  (full-stdout block, fence at 198/215): all 15 facts MATCH
```

And the full-stdout block is byte-identical to the hashed stream:

```
$ python3 -  # entry lines 200-214 (the 15 JSON lines; 199 is the "$ python3 …" prompt)
sha256("\n".join(entry lines 200-214) + "\n") = 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
sha256(actual stdout)                        = 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
```

So the saved record in the entry is byte-preserved against the stream whose digest the entry states. The single-fact form is also a real receipt:

```
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd | wc -l
1   (exit 0; the line is present verbatim in the full stdout)
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact 'member[META-INF/MANIFEST.MF]'
{"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", …}   (present verbatim in the full stdout)
```

## 1.6 Third-party re-derivation of every embedded block (registered gate)

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-69-apk-axml-byte-evidence.md
checked_blocks=17 problems=0
exit=0
```

The registered gate re-runs each `$ ` command in the entry and requires every embedded output line to appear verbatim in that command's stdout (`parse_blocks:57-65`, `run_cmd:72-80`, `drift:83-85`, membership in `set(stdout.splitlines())`). Exit 0 over 17 blocks — the 15 per-item fact blocks plus the full-stdout block and the derivation block — is an independent machine check, beyond my hand diff in §1.5, that the entry's saved outputs are byte-preserved against the commands that produce them. (Split cross-check with the portable spelling `grep -c '^\$ ' …` gives 17 total, 16 readout invocations, 1 derivation; the unescaped `'^$ '` happens to agree on this host — `grep grep (pi-uu-grep) 0.2.0`, where a mid-pattern `$` is literal — but is not portable.) Q09 note: this gate checks reproduction, not provenance; the entry nowhere cites it as evidence of origin, and the digest it would re-derive is the same `507d79f8…` stream verified in §1.2.

# 2. Origin / completeness / authenticity sweep

Every sentence in the entry that carries a digest or a receipt, and what it is used to establish:

| entry line | claim | scope actually claimed | hash-as-origin? |
|---|---|---|---|
| 6 (S047) | `derive_axml_anchors.py` sha256 `74d4c0d9…`, 20 lines over snapshot sha256 `56b88bc4…`, exit 2 on missing/ambiguous symbol | bytes of those two files; count of printed lines; refusal behaviour | no — and both digests verified (§1.1), both behaviours verified (§1.3) |
| 7 (S041) | fixture sha256 `05d2280f…` (947 bytes), truth.json `27303bae…`, generator.py `eaa9444c…`, readout.py `92e347c3…` | bytes of those four files | no; all four verified (§1.1). Origin is claimed by the row's own scope ("own-work, tier A"), not by the digest. |
| 8 | "the fixture, oracle and readout bytes are the round-65 claim-tree bytes, unchanged since `c7b7cf98`" | byte identity of saved records | a byte-preservation claim, verified in §3; no origin inference |
| 9 | readout exits 0, prints 15 lines whose SHA-256 is `507d79f8…` | the stdout byte stream | no; verified exactly (§1.2) |
| 19 | script "saved verbatim" as readout.py (sha256 `92e347c3…`) | the one file's bytes | the "verbatim" claim is corroborated operationally: running that file reproduces the embedded output byte-for-byte |
| 23 | archive 947 bytes, SHA-256 `05d2280f…`, "read from the file's bytes" | the file's bytes | no |
| 37 | every member's stated CRC-32 equals recomputed CRC-32 over payload bytes; walk end cursor = EOCD offset | payload bytes; cursor arithmetic | no — verified independently (§1.4; EOCD fact `737+188=925`, `parsed_entries 3 = total_entries_cd 3`) |
| 48 | MANIFEST.MF begins `4d616e69666573742d` = ASCII `Manifest-` (9 bytes) | the member's bytes | no; it is the first nine bytes of the payload whose sha256 the same block pins (line 45: `2e5da2495f3d…`) |
| 109 | declared checksum `0x3d120c30` = Adler-32 over offset 12 on; declared signature = SHA-1 over offset 32 on; end of line: "These are declared-header self-consistency facts about one inert member; dex validity is not claimed" | explicit byte ranges and an explicit non-claim | no — the entry states the exclusion itself |
| 127-150 | item 11 credit bounded to "exactly the numbers the command prints" (paragraph 127; derivation output lines 130-150) | the 20 printed lines | no |
| 157 | "readout values agree with it on every shared field … the committed bytes are hash-pinned above" preceded by "Regenerating the fixture from `generator.py` … is not re-run by this entry" | field-by-field agreement between two records; hash pins bytes | no — this is the Q09-correct posture: regeneration is explicitly not claimed and the hash is not offered as evidence that the generator produced the bytes. I checked the enumerated fields: image sha256/size, three members' local-header offsets (0/465/618), sizes (416/112/69), CRC-32s, the nine strings, the three attribute rows and the two non-zero ids all agree with `truth.json`; the member `sha256` values the oracle also carries (`73d1e0f2…`, `57cfe887…`, `2e5da249…`) agree too. |

No sentence offers a hash match as proof of who produced the bytes, that the archive is complete as acquired, or that a record's interpretation is valid. The two strongest candidate readings both fail to materialise:
- "the byte-exact copy of the pinned snapshot (same sha256 as the row's snapshot)" (line 6) asserts sameness of bytes only — which a digest does establish — and I verified both copies are 86255 bytes with `56b88bc4…`.
- "read from the file's bytes" (line 23) and "captured from the named command's actual stdout" (line 8) are process statements; neither is offered as hash-derived, and both are corroborated by reproduction (§1.5).

# 3. Saved records stay byte-preserved

## 3.1 The claim-tree files (entry line 8: "unchanged since `c7b7cf98`")

```
$ for p in corpus/fixtures/apk-r65/{fixture.apk,truth.json,readout.py,generator.py}; do
    git rev-parse c7b7cf98:$p; git rev-parse HEAD:$p; git cat-file blob c7b7cf98:$p | sha256sum; sha256sum $p; done
fixture.apk   blob b62216a9… at c7b7cf98 = blob b62216a9… at HEAD; blob sha256 05d2280f… = worktree 05d2280f…
truth.json    blob d6b8c5cb… = d6b8c5cb…; blob sha256 27303bae… = 27303bae…
readout.py    blob 0fcb1d85… = 0fcb1d85…; blob sha256 92e347c3… = 92e347c3…
generator.py  blob aea5de72… = aea5de72…; blob sha256 eaa9444c… = eaa9444c…
$ git log --oneline c7b7cf98..HEAD -- corpus/fixtures/apk-r65/
(no output — no commit touched the directory since the round-65 claim tree)
```

## 3.2 The snapshot copy

```
$ git log --oneline --all -- corpus/snapshots/ResourceTypes.h
3cacffd
4232235 round-68: build — … AXML anchor derivation script + pinned snapshot copy …
```

Only the round-68 build and one follow-up commit touch it; no round-69 commit does, and its bytes equal the round-65 wave snapshot (§1.3).

## 3.3 Round-69 does not rewrite prior rejected candidates or frozen bytes

```
$ git diff --stat 222a7a7..HEAD -- corpus/knowledge/round-65-apk-axml-byte-evidence.md \
    corpus/knowledge/round-67-apk-axml-byte-evidence.md corpus/knowledge/round-68-apk-axml-byte-evidence.md \
    corpus/fixtures corpus/snapshots
(no output)
```

(For the record: the round-65 candidate differs from `c7b7cf98` by one line — its `admission-status:` header, changed in the round-66 adjudication commit `a4c712a`, not in this round. That is a documented status change, not a silent byte rewrite, and it does not touch the file's `recheck:` or anchors.)

## 3.4 The saved receipt from round 65 still reproduces

`corpus/knowledge/round-65-apk-axml-byte-evidence.md:5` (saved record, byte-preserved) states the same 15-line stdout digest `507d79f8…` for the same command. It reproduces today from the current tree (§1.2). A four-round-old saved receipt that still re-derives against unchanged bytes and unchanged script is the strongest available evidence for the Q09 "saved records stay byte-preserved" leg.

# 4. Findings

**F1 (P1, admission procedure — not a Q09 value error).** The v4 §Q-map (lines 177-184) has eight rows: Q01, Q02, Q04, Q05, Q07, Q11, Q13, Q14. Q09 is absent — as are Q03, Q06, Q10, Q12. (v3 also carried a Q08 row marked "superseded by Q11"; neither candidate carries a Q15 row.) The v3 candidate carried a full map including:

```
corpus/knowledge/round-68-apk-axml-byte-evidence.md:180
| Q09 | pass | digests are claimed only for the exact bytes hashed; no origin, completeness or authenticity claim; the dex checksum/signature self-consistency is explicitly an inert declared-header property, not validity. |
```

`diff` of the two maps' ids: `3d2 < | Q03`, `6d4 < | Q06`, `8,10d5 < | Q08 / | Q09 / | Q10`, `12d6 < | Q12`, `13a8 > | Q14`. `corpus/QUALITY.md` §Admission procedure step 1 is "Apply every criterion. A criterion marked `n/a` names why it cannot apply" — v4 supplies neither a Q09 row nor an n/a reason, and `reports/round-69/claims.md` §C1's delta list (items 1-9) does not authorise dropping map rows. Consequence: Q09 is applicable and **PASS** on these bytes (§1-§3, decided here), so C1's "every applicable Q01–Q15 decision of the dispatched wave … PASS" clause is not violated by the omission; but admission under QUALITY.md cannot be completed from the entry as written until the row is restored (v5) or the adjudicator explicitly accepts wave decisions in place of the entry's map. Correct value: a `| Q09 | pass | … |` row as v3:180 had, restated for the v4 changes (S047 derivation receipt, item 11's bounded credit).

**F2 (P1 for the Q11 seat, cross-criterion).** Four digests are stated only in header prose, with no deriving command or output inside the entry: `truth.json` `27303bae…` (line 7), `generator.py` `eaa9444c…` (line 7), `readout.py` `92e347c3…` (lines 7, 19, 194), `derive_axml_anchors.py` `74d4c0d9…` (line 6). All four are correct (§1.1), and each is scoped to the file named beside it, so Q09 is unaffected. But v4's Q11 row (line 182) claims "every count, offset, identifier and digest carries its deriving command and output" — that universal is false for these four. This is the Q11 seat's call; reported here only because the same sentence is the entry's evidence that Q09's scope discipline is exercised. The Q11 seat independently reproduced the locator sweep (`.ufo/waves/round-69/R69ReviewEntryQ11.md`, leg (d)) and reports the same four lines `[7] [7] [7,19,194] [6]`, with Q09 unaffected — as decided here: the values are correct and each digest is scoped to the file named beside it.

**F3 (P3 residual).** Line 8's "every output line below was captured from the named command's actual stdout at build time, never transcribed by hand" is a process assertion with no committed capture log. It is not a Q09 defect (no digest is offered as its proof), and it is corroborated by byte-exact reproduction of all 15 readout lines and all 20 derivation lines today (§1.2-§1.5). If a receipt is wanted for the capture itself, the reproducible `507d79f8…` digest is that receipt; no such receipt is cited.

# 5. Residual risk and verification gaps

- **Member `sha256` byte range is implicit.** The entry's `sha256` fields for members do not label their range; for this fixture it cannot mislead (all three members are STORED, `compress_type 0`, so payload = member = uncompressed bytes, and the readout emits equal `compressed_size`/`uncompressed_size`). If a deflated member or a data descriptor were ever added, the unqualified `sha256` would become a Q09/Q14 scope ambiguity. No misreading is possible on these bytes; noted, not scored FAIL.
- **The entry's own Q09 row does not exist** (F1). My PASS is the wave's Q09 decision; no entry-side self-assessment backs it.
- **`truth.json` agreement is stated as "every shared field" with a partial enumeration** (line 157 lists offsets/sizes/CRC-32 but not the member `sha256` the oracle also carries). I checked the unlisted field too and it agrees (`73d1e0f2…`/`57cfe887…`/`2e5da249…` in `truth.json` members vs the readout lines), so the universal holds today; the enumeration is incomplete, the claim is not false.
- **Not verified here (out of Q09 scope):** `corpus/README.md` C05 status (still `uncovered` per the entry's own line 11 and claims.md §C1 admission order), counter/V-label behaviour, and the Q04/Q05/Q07/Q11/Q13/Q14/Q15 decisions — other seats.

# 6. Scratch cleanup

`/tmp/revenger-r69-q09*` (readout stdout copies, derive-script scratch copy, copied fixture tree) removed before returning. No file in the lane or fleet was written; no git/jj mutating command was run at any point.

Tool installs/upgrades: none.
