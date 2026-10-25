# R70W2OraclePerturb — independent-reader perturbation of the apk-r65 fixture (Q03/Q04)

**PARSER-NOTICES-EACH** — all five mandated perturbations of a copy of `corpus/fixtures/apk-r65/fixture.apk` are noticed
(`readout.py` changes a printed fact and/or exits non-zero; `entry_checks.py --oracle` exits 1 with a located `MISMATCH`
for P1/P2/P3; the entry-level embedded-output gate reads `problems=6..23` for all five), **with two named caveats**:
(C1) the dex `header_size` perturbation is noticed *only* by digest/consistency conjuncts — no credited command compares
the declared `header_size` with the S048-quoted `112`, and a container-consistent re-stamp hides it completely from
`--oracle` (34 MATCH, exit 0); (C2) `entry_checks.py --container` exits 0 and prints three `MATCH` lines on **every**
perturbed archive, including the truncated-EOCD and the wrong-local-header-offset probes — it is not an integrity check.
Neither caveat is a false statement on the landed bytes; both are Q13-list candidates (details in Findings).

Frozen target: lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`. Entry bytes read via
`git -C …/revenger-shokunin show 17ee7f87…:corpus/knowledge/round-70-apk-axml-byte-evidence.md`; fixture bundle extracted
with `git archive 17ee7f87… corpus/fixtures/apk-r65 corpus/knowledge/round-70-apk-axml-byte-evidence.md corpus/SOURCES.md | tar -x -C /tmp/revenger-r70-R70W2OraclePerturb/land`.
Fixture sha256 in the landed tree `05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e` = base
`3f5edbc2…` fixture sha256 (unchanged, `git show … | sha256sum`). Nothing in the lane was written.

## Method

`cp -r` of the landed bundle per probe; **one** byte (or one truncation) changed per copy; every later command run from
`/tmp/revenger-r70-R70W2OraclePerturb/probe/<P>/corpus` with the copied, unmodified `readout.py` and `entry_checks.py`
(`cwd` is the lane-root analogue, so the scripts' own relative paths resolve inside the copy). Offset discovery used a
throwaway `struct` walk, then each offset was verified against the surrounding bytes before use:

```
$ python3 - (original bytes)
P1 orig bytes 195..215: b'e\x00\x0f\x0fcom.example.r65\x00\x0b'      # u16len/u8len = 15,15; string[4]
P2 orig 277..289: 000000001b0201011c020101                          # little-endian 0x0101021b @281
P3 orig 538..546: 7000000070000000                                  # file_size 112 @538, header_size 112 @542
P5 orig 840..848: 0000a401d1010000                                  # CD local-header offset 465 @844
```

| probe | mutation (absolute file offset) | semantic target |
|---|---|---|
| P1 | byte 199 `0x63`→`0x64` | one char of AXML string[4] `com.example.r65` → `dom.example.r65` (AXML 150 = payload 49 + string-pool 8 + stringsStart 64 + rel 76 + 2) |
| P2 | byte 281 `0x1b`→`0x1c` | resource-map id of `versionCode` `0x0101021b` → `0x0101021c` |
| P3 | byte 542 `0x70`→`0x78` | dex `header_size` 112 → 120 |
| P4 | truncate last 22 bytes | EOCD record removed (947 → 925 bytes) |
| P5 | byte 844 `0xd1`→`0xd2` | central-directory local-header offset of `classes.dex` 465 → 466 |
| P5b (extra) | bytes 844-847 ← `struct.pack("<I",618)` | same field → 618, pointing at `META-INF/MANIFEST.MF`'s *valid* local header |

Post-mutation diff check: `P1 diffs at [199] len 947`, `P2 diffs at [281]`, `P3 diffs at [542]` — exactly one byte each.

## Results — mandated probes

### P1 — AXML string-pool byte flip

```
readout exit=0 lines=15
  "strings": [… "dom.example.r65" …]                        # fact changed, no exit signal
oracle exit=1 mismatches=3 matches=34
  MISMATCH image.sha256: readout='c9aa2ea4…' oracle='05d2280f…'
  MISMATCH AndroidManifest.xml.sha256: readout='5081982c…' oracle='73d1e0f2…'
  MISMATCH axml.strings: readout=[…'dom.example.r65'…] oracle=[…'com.example.r65'…]
container exit=0   → 3 MATCH lines
```
Noticed: readout (fact), `--oracle` (**semantic** `axml.strings`, not digest-only).

### P2 — resource-map id of `versionCode`

```
readout exit=0 → "ids": […"0x0101021c","0x0101021c"…], "nonzero": {"versionCode": "0x101021c", …}
oracle exit=1 mismatches=3 matches=34
  MISMATCH image.sha256 / MISMATCH AndroidManifest.xml.sha256
  MISMATCH axml.resource_ids: readout=[…'0x0101021c'…] oracle=[…'0x0101021b'…]
container exit=0   → 3 MATCH
```
Noticed: **semantic** `axml.resource_ids`.

### P3 — dex `header_size` 112 → 120

```
readout exit=0 → {"header_size": 120, "file_size": 112, "header_bytes": 112,
                  "checksum_matches": false, "signature_matches": false, …}
oracle exit=1 mismatches=2 matches=34
  MISMATCH image.sha256 / MISMATCH classes.dex.sha256
container exit=0   → 3 MATCH
```
Noticed — but **only by digests plus two printed booleans**. No comparison in `--oracle` covers any dex field
(`entry_checks.py:123-166` compares image, per-member ZIP fields, `axml.strings`, `axml.resource_ids`, attributes — nothing
from `dex_declared_header`). Auxiliary probe (digest-neutralised, see Findings F1) makes this explicit.

### P4 — EOCD truncated

```
readout exit=1 lines=3
  {"eocd_offset": -1, "offset_of_start_of_cd": 2694196487, "size_of_central_directory": 1599952992,
   "total_entries_cd": 0, "cd_end_equals_eocd_offset": false}          # printed before the crash
  File "…/readout.py", line 119, in main
    assert cursor == eocd, (cursor, eocd)
  AssertionError: (2694196487, -1)
oracle exit=1 mismatches=0 matches=0
  subprocess.CalledProcessError: Command '[…readout.py'] returned non-zero exit status 1
container exit=0   → no output at all
```
Noticed: uncaught `AssertionError` (non-zero exit) and the printed `eocd_offset: -1`; `--oracle` propagates via
`check=True`. `--container` prints nothing and exits 0.

### P5 / P5b — central-directory local-header offset

```
P5  readout exit=1 → File "…/readout.py", line 98, assert apk[lh_off:lh_off+4] == b"PK\x03\x04"
                      AssertionError: local header classes.dex
    oracle  exit=1 → CalledProcessError
    container exit=0 → MATCH AndroidManifest.xml / MATCH classes.dex / MATCH META-INF/MANIFEST.MF
P5b readout exit=1 → File "…/readout.py", line 104, assert lh_name == name
                      AssertionError: ('META-INF/MANIFEST.MF', 'classes.dex')
    oracle  exit=1 → CalledProcessError
    container exit=0 → 3 MATCH
```
Noticed by `readout`/`--oracle` (assert at `readout.py:98` and the name cross-check at `:104`). P5b is the stronger probe:
the offset points at a *structurally valid* local header, so only the name cross-check (`:104`) catches it.

## Entry-level recheck also notices all five

Full `corpus/` copied to `/tmp/revenger-r70-R70W2OraclePerturb/gate`, fixture replaced per probe, then
`python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md`:

```
BASELINE gate exit=0 :: checked_blocks=24 problems=0
P1 gate exit=1 :: checked_blocks=23 problems=7   (drift entry:27 archive line, :43 member line, :76 string pool, :90 start element …)
P2 gate exit=1 :: checked_blocks=23 problems=7   (… :83 axml_resource_map line …)
P3 gate exit=1 :: checked_blocks=23 problems=6   (… :105 dex_declared_header line, :181 `--oracle` exited 1)
P5 gate exit=1 :: checked_blocks=6  problems=19  (entry:26/33/42/44 `readout.py … exited 1`)
P4 gate exit=1 :: checked_blocks=6  problems=23  (… entry:36 embedded eocd line missing …)
```
So the fixture bytes are pinned at entry level by the embedded-output gate (item 1's archive line and each member line),
independently of the oracle's semantic coverage. Lane tree untouched: baseline gate on the real tree is
`checked_blocks=24 problems=0` (read-only run from the lane root).

## Independent decoder on the ORIGINAL bytes (no shared code with `readout.py`)

`python3 3.14.8` + stdlib `zipfile`/`hashlib`/`struct` (fresh code, not the readout):

```
1. size 947 sha256 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
2. zipfile entries 3, eocd rfind 925 (cd 737..925 = 188 bytes)
3. AndroidManifest.xml: hdr_off=0  csize=416 usize=416 crc=962d075f method=0 flags=0x0000 extra=0
   payload sha256=73d1e0f2e67c1b6210a8a2b5c741328adaf13ff31d5a21419ca36718afe9fae4 first16=03000800a001000001001c00c4000000
   classes.dex:          hdr_off=465 csize=112 usize=112 crc=2635c82a method=0 flags=0x0000 extra=0
   payload sha256=57cfe8878be74cad8bbc5e409b0964d4b13c35e8783d931ef7366881f8d548c2 first16=6465780a30333500300c123da5fc7bea
   META-INF/MANIFEST.MF: hdr_off=618 csize=69  usize=69  crc=e948d738 method=0 flags=0x0000 extra=0
   payload sha256=2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49 first16=4d616e69666573742d56657273696f6e
   (payload_offset = hdr_off+30+name_len+extra: 49 / 506 / 668 — matches item 3)
9. magic 6465780a30333500 ver 035 checksum 0x3d120c30 adler32_ok True sha1_ok True
   file_size 112 header_size 112 endian 0x12345678 len 112
```

Two independent third-party decoders (already installed; nothing installed this round):

- `apktool 3.0.3` (`/usr/bin/apktool`, `apktool d -f -s -o out fixture.apk`, exit 0) →
  `<manifest package="com.example.r65" n0:versionCode="1" n0:versionName="1.0" xmlns:android="http://schemas.android.com/apk/res/android" xmlns:n0="android" />`
- `androguard` (uv tool, `~/.local/share/uv/tools/androguard`) → `get_xml()` identical in content; chunk headers in its
  own walk: `type=258 header_size=16 size=96 @0x110 (=272)`, `type=259 16/24 @0x170 (=368)`, `type=257 16/24 @0x188 (=392)`
  — equal to item 4's table rows at 272/368/392; `m_resourceIDs` = `0x0,0x0,0x0,0x0,0x0,0x101021b,0x101021c,0x0,0x0`
  — equal to item 7's `ids` array and its two non-zero entries.

Items 1-9 checked one by one against these decoders: **1** ✓ (size/sha256), **2** ✓ (EOCD offset 925, 3 entries, cd 737+188=925),
**3** ✓ (three offsets, sizes, CRCs, sha256s, payload_offsets, first-16 hex), **4** ✓ (chunk offsets/types/sizes via androguard's
independent walk), **5** (struct widths: manual by design — the *resulting* offsets are confirmed by the two decoders parsing the
same chunks), **6** ✓ (flag 0x100 UTF-8: both decoders read the pool as UTF-8 and decode the same 9 strings; `readout.py:166`
is the cited `flags & 0x100` line, verified by reading the file), **7** ✓ (androguard `m_resourceIDs` exact match), **8** ✓
(three attributes, values and the `ns_index 0 → "android"` quirk, see F4), **9** ✓ (fresh independent parse of all declared dex
header fields).

## Findings (located)

**F1 — depth: the dex declared `header_size` has no machine-checked expected value (Q03/Q13 boundary).**
With the mandated probe ("adjust nothing but the bytes") the change is caught only by `image.sha256` and
`classes.dex.sha256`. I then built the archive a real dex writer would produce — `header_size` byte still `0x78`, adler32
re-stamped over `dex[12:]`, SHA-1 re-stamped over `dex[32:]`, local+central CRC and `truth.json` re-stamped to the new
payload — and **every credited command stayed green**:

```
readout --fact dex_declared_header
  {"checksum_matches": true, "signature_matches": true, "header_size": 120, "file_size": 112, "header_bytes": 112, …}
entry_checks.py --oracle      → exit 0, mismatches=0 matches=34
entry_checks.py --container   → exit 0
entry_checks.py --stdout-digest → exit 0 ("readout stdout: 15 lines, sha256 244b0f1a…")
```
The only surviving expected value for `header_size` is the S048 phrase item 11 locates
(`dex-format.html:5981`, "must be 0x70 (112) bytes") — a **reader** comparison. The entry states this honestly:
item 9 says the four S048 fields "are compared with those phrases" (not by a verifier), and item 13 enumerates the
oracle's comparisons without dex. So this is **not a false credit and not a Q03 FAIL** (Q03 permits "from a
specification"), but it *is* an unguarded clause class the entry's Q13 row does not name: Q13's "Unguarded clauses,
named" lists only (a) deleted embedded output lines and (b) a corrupted flag whose output is a superset. Candidate text
for the Q13 row if a judge wants it: *"a container-consistent change to any dex declared field other than checksum/signature
is compared with no expected value by any credited command"*.

**F2 — `--container` prints `MATCH` on corrupted archives.** On P5 it printed
`MATCH classes.dex: local flags=0x0000 method=0; central flags=0x0000 method=0; bit 3 (data descriptor) clear; oracle method 0`
while reading the flags/method bytes at `lh+6 = 472`, i.e. **inside `AndroidManifest.xml`'s payload** — a false `MATCH`
about a member whose local header is not at the recorded offset. On P4 (no EOCD) it printed nothing and exited 0. Item 16's
claim ("flags and compression method of every local and central record, read from the archive bytes and compared with the
oracle's declared method") is literally true for the intact fixture, and item 16 credits no integrity clause, so this is not
a Q13 false credit; it is a limitation the entry does not name (its Limitations paragraph names compression/split/spanned
records, not corrupted-offset input). The command is *not* a substitute for `readout.py`'s asserts at `:98`/`:104`/`:119`.

**F3 — positive: the fixture is pinned at entry level.** All five perturbations raise the entry's own gate to
`problems=6..23` (table above), because item 1's archive line and every member line are embedded and re-derived by
`check_embedded_outputs.py`. The oracle's dex coverage gap (F1) is therefore not exploitable on the landed entry unless the
container digests in `truth.json` were also edited — which the gate would then flag on item 14's pin lines.

**F4 — the `ns_index 0` quirk is in the bytes, not a readout artifact.** apktool 3.0.3 decodes
`xmlns:n0="android"` with `n0:versionCode`/`n0:versionName`, and androguard decodes `xmlns:ns0="android"` with
`ns0:versionCode` — both independently binding the attribute namespace to the literal string `android` (string 0, the
prefix) exactly as item 8 prints `"ns": "android", "ns_index": 0`. The entry's Limitations sentence stating this is
corroborated, not contradicted.

## Q-decisions this seat can carry (Q03/Q04)

- **Q03 pass.** Every expected value that fires on a perturbed byte is derived outside the record under test:
  `truth.json`'s AXML half is the generator's build declaration (`generator.py:37-61` `STRINGS`/`ATTRIBUTES`/`RESOURCE_IDS`,
  written at `:226`; the member half is `parse_members(apk)` at `:194`), and the dex expected value is a printed spec line
  (item 11). No expected value is copied from `readout.py`, and `truth.json` is not used as its own locator. F1 is an
  automation gap, not a copied expectation.
- **Q04 pass.** No third-party tool is credited anywhere in the entry; the readout is labelled manual standard-library
  analysis (items 3, 5, 12, 17), and no tool version or function is generalized. The independent decoders I ran agree with
  items 1-9 but are cited by nothing in the entry, so no credit is at stake.

## Confidence and residuals

- High for the five mandated probes: each was a one-byte (or one-truncation) change on a byte-identical copy, and every
  command's exit status and `MISMATCH`/`MATCH` line is quoted above.
- Medium-high for F1: it needs a re-stamped archive, which is outside the mandated "adjust nothing but the bytes" probe.
  It is stated as an *auxiliary* probe with its construction shown, and it does not falsify any sentence in the entry.
- Residual: `readout.py`'s `assert`-based detection (P4/P5) disappears under `python3 -O`; the entry's recheck commands
  and item 15's `check=True` all use `python3 -B` without `-O`, so the credited behaviour is the behaviour on the
  documented command line. Not a finding against the landed bytes, recorded for completeness.
- No lane file was written or edited; no git/jj mutating command ran in any repo. Tools used, all pre-installed, none
  installed or upgraded this round: `apktool 3.0.3` (`/usr/bin/apktool`), `androguard` (uv tool,
  `~/.local/share/uv/tools/androguard`), `python3 3.14.8`. Scratch `/tmp/revenger-r70-R70W2OraclePerturb` deleted after
  this report.
