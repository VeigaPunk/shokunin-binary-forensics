PASS — Q09 on the landed candidate bytes: every digest in the entry is claimed only for the bytes it actually hashed (all 17 digest-bearing values re-derived independently, zero mismatch), item 14's fence sentence is present and correct in kind, and the saved records are byte-preserved; the three residual defects I found are receipt-scoping (Q11) and gate-credit (Q13) defects, not digest-scope defects, and I do not convert them into a Q09 FAIL.

Seat `R70W2GateQ09` · wave 2 (falsify) · fresh seat, no wave-1 file read before this verdict was formed · target `corpus/knowledge/round-70-apk-axml-byte-evidence.md` at lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`, entry sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31` (`git show 17ee7f8…:<path> | sha256sum`) · criterion Q09 only (`corpus/QUALITY.md:2` of the Q08-Q11 block) · no file edited, no package installed, no tool upgraded, scratch deleted.

Criterion as frozen: *"A digest or receipt is claimed only for the exact bytes it hashed. It does not establish producer origin, acquisition completeness or authenticity. Saved records stay byte-preserved."* Failure mode: *"a hash match is offered as proof of origin, completeness or a valid interpretation."*

## Method (nothing taken from the entry's §Q-map)

`D=$(mktemp -d /tmp/revenger-r70-R70W2GateQ09-XXXX)`; `git -C <lane> archive 17ee7f8… corpus | tar -x -C "$D"`; all commands run from `$D` (repo-relative paths, so stdout is comparable to the embedded lines). Tamper tests ran on `cp -r $D/corpus /tmp/revenger-r70-R70W2GateQ09-tamper/corpus`.

## Q09 clause 1 — every digest is claimed only for the bytes it hashed: verified

| entry line(s) | claimed value | my re-derivation | result |
|---|---|---|---|
| 27 (item 1) | archive `05d2280f…d03e`, 947 bytes | `sha256sum corpus/fixtures/apk-r65/fixture.apk` → `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, `stat -c %s` → `947` | match |
| 43/45/47 (item 3) | member `sha256` + `crc32` per member | independent walk (own `struct` script, not the readout): payload slice at `lho+30+name_len+extra_len`, `sha256(payload)` → `73d1e0f2…fae4` / `57cfe887…48c2` / `2e5da249…0a49`, `crc32` → `962d075f` / `2635c82a` / `e948d738` | match; the hashed span is the payload (`readout.py:117` `sha256=hashlib.sha256(payload)`) |
| 105 (item 9) | dex `0x3d120c30`, `a5fc7bea8fa9ffaa52243540c8026066511b9fce` | own recompute over the S048-quoted spans: `adler32(dex[12:]) = 0x3d120c30`, `sha1(dex[32:]) = a5fc7bea8fa9ffaa52243540c8026066511b9fce`; declared fields identical | match |
| 123 (item 11) | `sha256 56b88bc4…c56f ResourceTypes.h` | `sha256sum corpus/snapshots/ResourceTypes.h` → `56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f` | match |
| 222-231 (item 14) | ten digests + ten sizes | `sha256sum` on all ten paths + `stat -c %s` → every digest and every size identical to the printed line (e.g. `2d4f25f6…b1f9 15062 bytes entry_checks.py`, `c0428612…d9f4 281157 bytes dex-format.html`) | match, 10/10 |
| 238 (item 15) | `15 lines, sha256 507d79f8…d247` | `python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/…-stdout.txt`; `wc -l` → `15`; `sha256sum` → `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`; also reproduced from two other cwds (`/tmp`, `$D/corpus/fixtures`) with the same digest | match |
| 182-198 (item 13) | `MATCH … readout=… oracle=…` digest pairs | `truth.json` declares `image.sha256 = 05d2280f…d03e` and the three member sha256 values; both sides of every printed pair equal those declarations | match |

The digests are computed, not embedded: one-byte flip at offset 500 of a **copy** of `fixture.apk` changes the pin line to `sha256 37dd8addb541b83706f7d40d190092caf95e2651bd4e5546ae266a38fa52d246 947 bytes corpus/fixtures/apk-r65/fixture.apk`, and `--stdout-digest` then exits non-zero with no printed line (the readout exits 1, `check=True` propagates). A hardcoded table would not move.

No prose-only digest: a scan for full 64-hex runs outside a code fence returns `[]` (20 such runs, all inside fenced command blocks). Every digest the entry states therefore carries the command that printed it.

## Q09 clause 2 — no digest offered as proof of origin / acquisition completeness / a valid interpretation

Fences present on the bytes I read:

- entry:218 (item 14): *"a digest identifies exactly these bytes; it does not establish who produced them, that a copy was faithfully fetched, or that it is the upstream's current text"* — the required disclaimer, in the item that owns the digest list.
- entry:101 (item 9): the dex declared-vs-recomputed match *"shows the member's header is internally consistent, and nothing about dex program validity follows"*.
- entry:178 (item 13): agreement with `truth.json` *"shows the readout parses what the generator wrote; it does not show that a declared value … is the Android framework's value for its name"* — the oracle half is labelled a build declaration, not an authenticity proof.
- entry:284 (Unknown): no install/signature/dex-validity/provider claim; *"whether the upstream document has since changed is not checked"*.
- entry:8: the builder `.ufo/waves/round-70/build-entry.py` is named and *"its digest is not claimed"* — an undigested producer is declared as undigested rather than dressed in a hash.
- entry:4 (S032): *"from the committed snapshot copy …, digest printed in item 14; whether it still equals the upstream's current text is not claimed"* — this is the repaired form of the wave-1 circular-support clause, and it now holds.

Header lines 1-7 were checked individually for a digest pointer that resolves: `:1`→`228`, `:2`→`231`, `:3`→`230`, `:4`/`:5`→`229`, `:6`→`227`+`228`, `:7`→`222-226`. Every pointer lands on the digest of the file that line names. No header line claims a digest proves origin.

## Q09 clause 3 — saved records stay byte-preserved: verified

The three snapshots are **new files** at this commit (`git diff --name-status 3f5edbc… 17ee7f8…` → `A corpus/snapshots/APPNOTE.TXT`, `A corpus/snapshots/dex-format.html`, `A corpus/snapshots/rea-android-applications.md`, `A corpus/fixtures/apk-r65/entry_checks.py`), so preservation had to be checked against the earlier records, not assumed:

```
$ git show 3f5edbc…:.ufo/waves/round-63/source-snapshots/appnote.txt      | sha256sum
0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6   ( = corpus/snapshots/APPNOTE.TXT )
$ git show 3f5edbc…:.ufo/waves/round-67/source-snapshots/dex-format.html | sha256sum
c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4   ( = corpus/snapshots/dex-format.html )
$ git show 3f5edbc…:.ufo/waves/round-65/source-snapshots/rea-android-applications.md | sha256sum
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c   ( = corpus/snapshots/rea-android-applications.md )
$ git show 3f5edbc…:.ufo/waves/round-65/source-snapshots/ResourceTypes.h | sha256sum
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f   ( = corpus/snapshots/ResourceTypes.h )
```

and the four S041 files plus `derive_axml_anchors.py` hash identically at base `3f5edbc…` and at landed `17ee7f8…` (`readout.py 92e347c3…`, `truth.json 27303bae…`, `generator.py eaa9444c…`, `fixture.apk 05d2280f…`, `derive_axml_anchors.py 74d4c0d9…`), which is the receipt behind entry:19 *"saved verbatim"*.

Mechanical context re-run by me (context, not evidence for Q09): `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0`, exit 0.

## Located residual defects — real, but not Q09 (routed; they do not carry my verdict)

1. **entry:3 (S048), acquisition claim with a mismatched receipt — Q11, not Q09.** The clause *"who re-fetched the live page and compared it with the committed snapshot `corpus/snapshots/dex-format.html`, digest printed in item 14; the live page differs from the snapshot only in page-chrome lines"* points at item 14's digest `c0428612…d9f4` (281157 bytes), which is the **snapshot's** digest; `corpus/SOURCES.md:62` records the live page as `281161 bytes, sha256 d72efc551a4d69be6d29a3aebb4ea9fca67935832893ca2779c8e67a6e468598`. The digest is scoped honestly (it hashes the snapshot, the bytes it hashed), so Q09's first sentence is not violated — but the diff-scope claim is prose-only inside the entry, and `grep -n '^\$ ' <entry> | grep -c generator`-style checks confirm no command in the entry prints the live digest or the diff. Same class as wave-1's routed "circular support" defect, narrowed and still open. Smallest safe correction, replacing the parenthetical clause of entry:3: *"row opened 2026-10-25 by this entry's author, who re-fetched the live page (`281161 bytes, sha256 d72efc55…8598`, recorded in the S048 row of `corpus/SOURCES.md`) and compared it with the committed snapshot `corpus/snapshots/dex-format.html` (`281157 bytes, sha256 c0428612…d9f4`, item 14); the live page differs only in a per-request CSP nonce and one devsite loader line — that comparison is a recorded author act, not re-derived by any command in this entry"*. The S049 line (entry:2) is the same shape but its live digest equals the snapshot's (`412d9cb4…`, `corpus/SOURCES.md:63`), so it is true yet still receipt-less inside the entry.
2. **entry:218, set description — Q11 (count), not Q09.** *"the ten files under `corpus/` that the commands above read"* over-includes `corpus/fixtures/apk-r65/generator.py`: no command above item 14 reads it (`grep -n '^\$ ' <entry> | grep -c generator` → `0`; the file is only hashed by item 14's own `--pins`, and entry:7/entry:178 say the entry does not re-run it). Over-inclusion, not a missing receipt, so the pin set is complete for what the commands read; the sentence should read *"the ten files under `corpus/` this entry pins (nine read by the commands above, plus `generator.py`, hashed only)"*.
3. **entry:3's member `sha256` span is unstated — tightening, not a defect.** The printed member `sha256` is the payload slice (`readout.py:117`), and because `method=0` for all three members the payload equals the member content, so no value is misattributed; item 3's prose says only that the payload's CRC-32 is recomputed. One clause ("the `sha256` field is the digest of that payload slice") would remove the reading that it covers the whole local record.
4. **entry:8/entry:9 credit `check_embedded_outputs.py` and `lint_entry.py` without pinning their bytes — Q13, not Q09.** No digest is offered for them, so Q09 is untouched; the credit claim is the gate/lint seat's business.

## Kill-rule statement

This PASS is on Q09 alone, on the landed bytes, and it does not override any mechanical label (`C1_GATE`, `C1_LINT`, `HOLDS_C1_V5`, `A1_C1`) — those are the counter's and the L1's to read. Items 1-4 above are handed to the Q11 and Q13 seats with their corrected sentences; if a Q11 seat finds entry:3's live-diff claim defective, that FAIL is Q11's and must be argued on Q11's text, not on Q09's. I found no wrong digest value, no digest claimed for bytes it did not hash, no digest offered as proof of origin or authenticity, and no byte-preservation drift, so Q09 has no kill-rule input from this seat.

Scratch: `/tmp/revenger-r70-R70W2GateQ09-*` (extraction, tamper copy, stdout capture, entry copy) deleted before return.
