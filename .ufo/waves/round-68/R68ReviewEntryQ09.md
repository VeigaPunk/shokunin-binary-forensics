PASS — Q09 on `corpus/knowledge/round-68-apk-axml-byte-evidence.md`: every digest/receipt in the entry is claimed for the exact bytes it hashes (all 12 digest statements re-derived here, byte-identical), no hash match is offered as proof of producer origin, acquisition completeness or authenticity, and every saved record is byte-preserved.

Seat: `L1Revenger68.R68ReviewEntryQ09` (reader/attacker, not the author). Reviewed bytes: `corpus/knowledge/round-68-apk-axml-byte-evidence.md`, 215 lines, sha256 `107e2d7483e57e64476ead408f2eb793f41e3eea5e3c96407763eadca6dfea5b` (worktree, tracked in `git ls-files`). Frozen contract read first: `reports/round-68/claims.md` §C2, then `corpus/QUALITY.md` (Q09 row: "reject when a hash match is offered as proof of origin, completeness or a valid interpretation"). The entry's own `## §Q-map` Q09 row was **not** used as evidence.

All commands run from `/home/vgpnk/Projects/shokunin/revenger-shokunin`. No tool installs, no writes outside this file.

## 1. The criterion

`corpus/QUALITY.md:31` — "A digest or receipt is claimed only for the exact bytes it hashed. It does not establish producer origin, acquisition completeness or authenticity. Saved records stay byte-preserved."

Four separable tests, all executed: (a) every digest actually hashes the bytes it is attached to; (b) no origin claim rides on a hash; (c) no completeness/authenticity claim rides on a hash or checksum; (d) prior saved records are unchanged.

## 2. Every digest in the entry, re-derived from the bytes

| entry pointer | claimed value | command run | observed |
|---|---|---|---|
| L1, L4, L129 | `ResourceTypes.h` sha256 `56b88bc4…c56f`, 86255 B, "committed byte-exact as `corpus/snapshots/ResourceTypes.h` (same sha256)" | `sha256sum corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h; wc -c` | both `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f`, both `86255` |
| L2 | S043 snapshot sha256 `412d9cb4…a74c` | `sha256sum .ufo/waves/round-65/source-snapshots/rea-android-applications.md` | `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`; the quoted sentence is at lines 7-8 (`sed -n '5,9p'` → `5:older server.`, `7:Start with \`inspect_android_package\` on the caller's APK path for package`, `8:identity, manifest declarations, coverage, and inline Evidence. Use`) |
| L3 | S045 snapshot sha256 `c0428612…d9f4`, 281157 B | `sha256sum` + `wc -c` on `.ufo/waves/round-67/source-snapshots/dex-format.html` + `grep -c` for each quoted string | hash and size match; `adler32 checksum of the rest of the file` → 1 hit, `SHA-1 signature` → 1 hit |
| L4 | derive script sha256 `bce497d6…e249`, "17 output lines" | `sha256sum corpus/derive_axml_anchors.py; python3 -B corpus/derive_axml_anchors.py \| wc -l` | `bce497d6c0f5767fd7a94f7d9f6a7adb3d70f9df656028a8d080e050d1f1e249`; 17 lines, exit 0 |
| L5 | fixture `05d2280f…d03e` (947 B), `truth.json` `27303bae…8173`, `readout.py` `92e347c3…3976` | `sha256sum corpus/fixtures/apk-r65/{fixture.apk,truth.json,readout.py}; wc -c fixture.apk` | all three match; fixture is `947` bytes |
| L6, L9 | "the round-65 claim-tree bytes, unchanged since `c7b7cf98`" | `git show c7b7cf98:corpus/fixtures/apk-r65/<f> \| sha256sum` for all three files | `05d2280f…`, `27303bae…`, `92e347c3…` — identical to the worktree values |
| L7, L194 | readout stdout receipt: exit 0, **15 stdout lines**, sha256 `507d79f8…d247` | `python3 -B corpus/fixtures/apk-r65/readout.py > f; wc -l f; sha256sum f`; then sha256 of the entry's own §Reproduce block | `exit=0`, `15 /tmp/r68q09-readout.out`, `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`; the entry's 15-line block (prompt line excluded) is **byte-identical** to the live stdout and hashes to the same `507d79f8…` |
| item 1 block (L25) | archive `sha256 05d2280f…`, `bytes 947` | independent `hashlib.sha256(open(...).read())` | `05d2280f…`, len `947` |
| item 3 blocks (L39/L41/L43) | member sha256 `73d1e0f2…`, `57cfe887…`, `2e5da249…`; crc32 `962d075f/2635c82a/e948d738`; payload offsets 49/506/668 | independent central-directory walk with `struct` (no readout.py), hashing each payload slice | `('AndroidManifest.xml',49,416,416,'73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4',0x962d075f)`, `('classes.dex',506,112,112,'57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2',0x2635c82a)`, `('META-INF/MANIFEST.MF',668,69,69,'2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49',0xe948d738)` — each digest is over exactly the payload bytes it is attached to |
| L107 (item 9) | dex declared checksum `0x3d120c30` = Adler-32 over `body[12:]`; declared signature = SHA-1 over `body[32:]`; file_size/header_size 112; endian `0x12345678` | independent `zlib.adler32(body[12:])`, `hashlib.sha1(body[32:])`, `struct.unpack` | `0x3d120c30`; `a5fc7bea8fa9ffaa52243540c8026066511b9fce`; `112 / 112`; `0x12345678` — the recomputation ranges are exactly the ones the entry states |
| L129 (item 11 output) | 17-line derivation table | `python3 -B corpus/derive_axml_anchors.py` vs the entry's fenced block | 17 vs 17 lines, `identical: True` (byte compare, prompt line excluded) |

Additionally every per-item `--fact` command was re-run (15 invocations) and each printed **byte-identical** the JSON line the entry embeds: `per-fact commands rerun: 15 mismatches: 0`.

## 3. No origin / completeness / authenticity claim rides on a hash

The reject trigger of Q09 is absent; four fences are in the bytes:

- **L107 (item 9), verbatim:** "These are declared-header self-consistency facts about one inert member; dex validity is not claimed." The checksum/signature match is named self-consistency, not validity and not authenticity.
- **L1**, the snapshot digest is attached only to copy identity: "committed byte-exact as `corpus/snapshots/ResourceTypes.h` (same sha256) so the anchor derivation below runs from any corpus tree".
- **L4 (S046 row):** "scope: the machine derivation of every S038 line number this entry cites, read from the pinned snapshot bytes; **not the layout facts themselves, which rest on S038**". The digest therefore does not stand in for upstream fidelity of the AOSP document.
- **L152:** "Regenerating the fixture from `generator.py` in a scratch directory on this host was round-65 evidence (S041) and is **not re-run by this entry**; the committed bytes are hash-pinned above." Producer origin is attributed to a prior round's run and labelled not-re-run; the hash is used only to pin which bytes were analysed. The registry side also holds: `corpus/fixtures/apk-r65/generator.py` hashes to `eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a`, exactly the S041 row value (`corpus/SOURCES.md:55`).

The only structural "completeness" statement is byte-walked, not hash-derived: item 2's EOCD record at offset 925 with `total_entries_cd=3`, `size_of_central_directory=188`, `offset_of_start_of_cd=737` — my independent parse gives `entries/total/size/off: (3, 3, 188, 737)`, signature `504b0506` at 925, `925+22 == 947` with **0 trailing bytes** after the EOCD record. No checksum is offered for archive completeness.

## 4. Saved records stay byte-preserved

- `git status --porcelain corpus/knowledge corpus/fixtures corpus/snapshots corpus/SOURCES.md` → empty. The only untracked path anywhere under `corpus/` is `corpus/__pycache__/check_embedded_outputs.cpython-314.pyc` (mtime 03:29, a bytecode cache left by a sibling seat importing the gate, not a record and not created by this seat — every command this seat ran used `python3 -B`); no tracked corpus file is modified (`git status --porcelain` shows only untracked `??` wave reports plus that cache).
- Prior candidates keep their bytes: `round-65-apk-axml-byte-evidence.md` still cites the enum block as "lines 239-250" and contains `:244` count 0; `round-67-apk-axml-byte-evidence.md` still carries its 3 `:244` occurrences with the two substantive anchors at its lines 1 and 56.
- The new `corpus/snapshots/ResourceTypes.h` is byte-identical to the pinned snapshot (`56b88bc4…`, 86255 B) — a copy, not a rewrite. `corpus/derive_axml_anchors.py` hard-fails on a digest mismatch (`SNAPSHOT_SHA256` pin, `corpus/derive_axml_anchors.py:35-43`), i.e. the digest is used as an identity guard, which is Q09's permitted use.

## 5. Findings outside this criterion's carry (reported, not used to change the Q09 verdict)

- **F1 (hand to the Q02/Q11 owner; unbacked history claim, not a digest claim).** Entry **L148**: "That one-line off-by-one is what falsified the round-65 and round-67 drafts (M40/M44)." The round-65 draft cannot have been falsified by a `:244` anchor: `grep -c ':244' corpus/knowledge/round-65-apk-axml-byte-evidence.md` → `0` (and `:245` → `0`); it cited the enum as the block "lines 239-250". Its own `admission-status` (`round-65-apk-axml-byte-evidence.md:7`) and `corpus/README.md:34` record the rejection as **Q02/Q06/Q11** on the `entry:41 payload_first16_hex` transcription drift. `corpus/derive_axml_anchors.py:5-8` repeats the same misattribution. Correct statement: round-67 failed on the `:244` anchor; round-65 failed on the entry:41 transcription drift plus the 239-250 block range (which excludes `RES_XML_RESOURCE_MAP_TYPE` at `:253`). Q09 is not triggered because no digest is offered for this sentence; it is an unpointed historical assertion.
- **R1 (receipt framing unstated).** The `507d79f8…` digest is over the 15 program output lines LF-joined with a trailing LF; hashing the displayed fence **including** the prepended `$ python3 -B corpus/fixtures/apk-r65/readout.py` line gives `238b5d7c1eff03046bd9dae78fa0e7cef4635dfd445cead27ff53d78340e3b48`. The entry says "15 stdout lines", which is recoverable, but the byte framing (prompt excluded, trailing newline included) should be stated. No overclaim; a reproducibility gap only.
- **R2 (upstream correspondence).** `corpus/snapshots/ResourceTypes.h` ↔ AOSP tag `android-15.0.0_r1` rests on the round-65 fetch; the digest establishes copy identity only. The entry's S046 scope ("not the layout facts themselves") already disclaims this, so no Q09 violation, but a reader must not read `56b88bc4…` as upstream authenticity. Recommend one explicit sentence: the snapshot was not re-fetched this round.
- **R3 (word "signature").** `signature_matches: true` / `signature_sha1` could be misread as cryptographic authentication; the fence says "not validity". Recommend widening it to "not authenticity or validity".
- **R4 (oracle agreement).** L152's "The readout values agree with it on every shared field" is a same-author consistency check between the readout and the authored `truth.json` (S041, own-work); the entry labels the oracle authored and does not claim independence, so it is not an origin claim — but it must not be cited as independent validation.

## 6. Verification gaps of this seat

- I did not exercise `derive_axml_anchors.py`'s exit-2 branches (missing/ambiguous symbol) because that requires mutating the snapshot, which is read-only for this seat; the entry's claim about that behaviour (`L7`, `L125`) is **unverified by me**.
- I did not re-run `generator.py` (the entry states it is not re-run; it was not run here either).
- The environment had no `lsp` server bound to this corpus, so caller/definition checks for this markdown entry are not applicable; the equivalents used are byte commands plus `grep`/`git show`, each recorded above.

## Verdict

**Q09 PASS** for `corpus/knowledge/round-68-apk-axml-byte-evidence.md` on these bytes. Every digest and the one stdout receipt reproduce byte-for-byte against the live command output, none of them is offered as evidence of origin, acquisition completeness or authenticity, and the saved records (r65 fixture/oracle/readout at `c7b7cf98`, r65 and r67 candidates) are byte-preserved. Residual risks R1-R4 and out-of-criterion finding F1 above do not implicate Q09; F1 is a real defect for the seats carrying Q02/Q11.

Report: .ufo/waves/round-68/R68ReviewEntryQ09.md
