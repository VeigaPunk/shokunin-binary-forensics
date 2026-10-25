# R70W1EntryChecksMut — entry_checks.py subcommand mutation calibration

SURVIVORS — all three comparison subcommands (--oracle, --zip-layout, --spec-quotes) killed their assigned mutants with MISMATCH + exit 1, but three subcommands (--pins, --eocd, --stdout-digest) have no failure path in code (unconditional `return 0`); they are derivation printers whose detection lives in an external byte-comparison, and `--eocd` additionally went output-unchanged under 4 of 5 probes.

Seat: R70W1EntryChecksMut · Round 70 wave 1 (advisory, pre-gate) · 2026-10-25
Target: `corpus/fixtures/apk-r65/entry_checks.py` (scratch copy only; lane bytes untouched — evidence below).
Scratch: `/tmp/revenger-r70-R70W1EntryChecksMut/` with the same relative layout (`corpus/fixtures/apk-r65/`, `corpus/snapshots/` all four files it reads, `corpus/derive_axml_anchors.py`). Deleted before returning.

## Baseline (pristine scratch, before any mutation)

All six subcommands: exit 0, zero MISMATCH lines (full outputs in the transcript; abridged):

```
$ cd /tmp/revenger-r70-R70W1EntryChecksMut
$ for c in pins eocd oracle zip-layout stdout-digest spec-quotes; do python3 -B corpus/fixtures/apk-r65/entry_checks.py --$c; echo "exit=$?"; done
--pins exit=0          (9 sha256 lines, matches lane byte hashes)
--eocd exit=0          ("eocd signature bytes at offset 925: 504b0506 (4 bytes)")
--oracle exit=0        (28 MATCH lines, 0 MISMATCH)
--zip-layout exit=0    (14 MATCH lines, 0 MISMATCH; local 30 / central 46 / eocd 22)
--stdout-digest exit=0 ("readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247")
--spec-quotes exit=0   (6 MATCH lines, 0 MISMATCH)
```

Baseline green → the probes below are interpretable (a baseline failure would have been inconclusive, not a kill).

## Probes (each applied to the scratch copy, then restored)

### M1 — one width in LOCAL_HEADER: `("signature", 4)` → `("signature", 3)` (entry_checks.py:48)

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout
local fixed part: 29 bytes (sum of the transcribed field widths)
MISMATCH local.crc32: spec offset 13, readout.py literal `u32(apk, lh_off + 13)` present=False
MISMATCH local.compressed_size: spec offset 17, ... present=False
MISMATCH local.uncompressed_size: spec offset 21, ... present=False
MISMATCH local.name_length: spec offset 25, ... present=False
MISMATCH local.extra_length: spec offset 27, ... present=False
MISMATCH local.fixed_part: spec width 29, readout.py literal `lh_off + 30` present=True
exit=1
```
KILLED by `--zip-layout` (6 MISMATCH, exit 1). Cross-check: `--oracle` under M1 exit 0, 0 MISMATCH — no cross-talk.

### M2 — readout.py literal `eocd + 12` → `eocd + 13` (readout.py:78, `cd_size = u32(apk, eocd + 13)`)

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout
MISMATCH eocd.cd_size: spec offset 12, readout.py literal `u32(apk, eocd + 12)` present=False
exit=1
```
KILLED by `--zip-layout` (exit 1). Side observations: `--oracle` exit 0 (cd_size is printed by readout but not compared to truth.json — the oracle does not pin that field); `--stdout-digest` exit 0 but its printed digest changed `507d79f8…` → `f6124f12d6df4038bb7373a226b56742e3fc51ea497f7457a94ca9d8555a3a5a`, i.e. detectable only by diffing the printed line against the entry's embedded value, not by the subcommand itself.

### M3 — one byte of fixture.apk flipped (offset 510, `0x30`→`0x31`, inside the classes.dex stored-data region)

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --oracle
MISMATCH image.sha256: readout='b071350bac159920c81bff5a50cb14a82b8c658a2326be64621e76b4946ff7d9' oracle='05d2280f…'
MISMATCH classes.dex.sha256: readout='62c3cd4f79664704b90477587c685d63462749b4dfa6cbf6a236f33d66052bcd' oracle='57cfe887…'
exit=1
```
KILLED by `--oracle` (2 MISMATCH, exit 1). Side observations: `--eocd` exit 0, output byte-identical (flip far from the EOCD signature); `--pins` exit 0 but the fixture.apk line now prints `b071350b…`; `--stdout-digest` exit 0, digest changed to `4169285e…`. Note: `MATCH classes.dex.crc32: readout='2635c82a'` despite the flipped content — the crc32 fact is copied from the stored local-header field, not recomputed from member bytes; only the sha256 facts are recomputed, which is what caught this flip.

### M4 — one quoted phrase in dex-format.html: `must be 0x70 (112) bytes` → `(113)` (snapshot line 5981)

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes
MISMATCH dex-format.html: first line 5981, folded phrase present=False: must be 0x70 (112) bytes (v40 or earlier)
exit=1
```
KILLED by `--spec-quotes` (1 MISMATCH, exit 1). Other 5 quotes still MATCH — no cross-talk.

### M5 — one truth.json value: `"size": 947` → `"size": 948` (truth.json:72)

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --oracle
MISMATCH image.size: readout=947 oracle=948
exit=1
```
(First M5 run piped through `head` and showed a BrokenPipeError traceback; re-run clean to a file: exit=1, exactly 1 MISMATCH at line 2 of the output.) KILLED by `--oracle`.

## Per-subcommand verdict (code-level, entry_checks.py line anchors)

| subcommand | failure path | probe result |
|---|---|---|
| `--oracle` | `return 1 if bad else 0` (:148) | KILLED M3, M5 (MISMATCH + exit 1) |
| `--zip-layout` | `return 1 if bad else 0` (:168) | KILLED M1, M2 (MISMATCH + exit 1) |
| `--spec-quotes` | `return 1 if bad else 0` (:191) | KILLED M4 (MISMATCH + exit 1) |
| `--pins` | unconditional `return 0` (:106) | SURVIVOR — no MISMATCH branch exists; output changes only when a pinned file changes (M3: fixture hash line changed) |
| `--eocd` | unconditional `return 0` (:113) | SURVIVOR — strictest: output unchanged under M1/M2/M4/M5; only an EOCD-signature corruption (or content at the rfind hit) could change it |
| `--stdout-digest` | unconditional `return 0` (:175) | SURVIVOR — no failure branch; digest line changed under M2/M3, detectable only by external diff |

So: the three *checking* subcommands each can fail and each killed its class; the three *printing* subcommands cannot fail by themselves. This is coherent with the entry's design (the embedded values the printers produce are meant to be re-derived and byte-compared by an external gate), but as a standalone calibration statement: `--pins`, `--eocd`, `--stdout-digest` are the survivors, and `entry_checks.py` itself is not in its own `PINS` tuple (entry_checks.py:33-43), so a defect inside entry_checks.py is caught only by the `--zip-layout`/`--spec-quotes`/`--oracle` self-checks (M1 confirms that works).

Verdict name per tasking: **SURVIVORS** — list: `--pins`, `--eocd`, `--stdout-digest` (cannot print MISMATCH / exit 1 by construction).

## Restoration evidence

After the final restore, every scratch file hash equals the lane file hash (all 10 files checked):

```
OK  corpus/fixtures/apk-r65/entry_checks.py 68b1124fff206cc43c957cc3eb4e203c03a622ee4fd010075c884fe333e56049
OK  corpus/fixtures/apk-r65/readout.py      92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976
OK  corpus/fixtures/apk-r65/truth.json      27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173
OK  corpus/fixtures/apk-r65/fixture.apk     05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e
OK  corpus/fixtures/apk-r65/generator.py    eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a
OK  corpus/derive_axml_anchors.py           74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa
OK  corpus/snapshots/APPNOTE.TXT            0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6
OK  corpus/snapshots/dex-format.html        c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4
OK  corpus/snapshots/rea-android-applications.md 412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c
OK  corpus/snapshots/ResourceTypes.h        56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f
```

Pristine re-run after all restorations: all six subcommands exit 0, 0 MISMATCH. Lane target untouched:
`68b1124fff206cc43c957cc3eb4e203c03a622ee4fd010075c884fe333e56049  /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/apk-r65/entry_checks.py` (same hash as before the wave). No lane file written; no git-mutating command run; no packages installed.

## Advisory notes for wave 1 (not kill-rule inputs)

1. The three printer subcommands rely on an external consumer to compare their output against the entry's embedded values. If the C05 entry (or the C3 gate) does not byte-pin the `--stdout-digest` value `507d79f8…` and the `--pins` lines, a readout/fixture drift of the M2/M3 class would be visible in printer output but fail nothing — the M3-style detection currently rests entirely on `--oracle`'s recomputed sha256 facts.
2. `--oracle`'s crc32 comparisons are header-transcribed, not content-recomputed (M3 evidence above): a stale-crc-with-clean-content tamper class is outside `--oracle`'s reach today. Out of scope to change here; recorded as a located behavior with output evidence.
