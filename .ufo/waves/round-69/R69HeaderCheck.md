FAIL — header block is five-part complete and its runnable `recheck:`/`coverage:` claims reproduce exactly, but on the current bytes `verified-at:` carries an unguarded git object id (Q15's literal failure, wave-confirmed), six header digests carry no in-entry derivation (Q11's letter), two `source:` rows misstate their own registry status/opener and the S032 row omits the EOCD anchor the entry uses, and the new `admission-status:` omits the Q11/Q08 FAILs while §Q-map still claims `pass` on three criteria the same line rejects.

# R69HeaderCheck — entry header block of the C05 v4 candidate

Seat `L1Revenger69.R69HeaderCheck` · fresh leaf, non-author · 2026-10-25 · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`
Criterion lens: Q02 (`corpus/QUALITY.md:14`) and Q11 (`corpus/QUALITY.md:23`), cross-read against Q15 (`corpus/QUALITY.md:27`), Q14 (`:26`) and claims `reports/round-69/claims.md` §C1 (`:58`) / `## Admission order (binding)` (`:172`).
Read-only seat: no edit outside this report; no git write of any kind; **no tool installed or upgraded** (pacman paused host-wide, no transaction attempted; `python3` 3.14, `git`, `sha256sum` already present). Scratch `/tmp/revenger-r69-*` deleted before return.

## 0. Bytes under test — and a mid-run change I must disclose

The entry changed twice while this seat ran. All five header lines are judged on the **current** bytes:

```
$ sha256sum corpus/knowledge/round-69-apk-axml-byte-evidence.md
a43fc907461e2d7939aa50950cbbd044a47ae4df08ca3d7aaf646032e9257656
$ wc -l -c corpus/knowledge/round-69-apk-axml-byte-evidence.md
    215   35750 corpus/knowledge/round-69-apk-axml-byte-evidence.md
$ git rev-parse HEAD:corpus/knowledge/round-69-apk-axml-byte-evidence.md
00402958f673fc55ed738664d60f2e543eb73129          # build blob (35113 B, sha c1e7eaac…, the bytes Q02/Q15 seats cite)
$ git status --porcelain corpus/knowledge/round-69-apk-axml-byte-evidence.md
M  corpus/knowledge/round-69-apk-axml-byte-evidence.md   # staged, not committed
$ git diff --numstat HEAD -- corpus/knowledge/round-69-apk-axml-byte-evidence.md
1  1  corpus/knowledge/round-69-apk-axml-byte-evidence.md
```

The single changed line is `:11` (`admission-status: candidate …` → `... rejected …`). **Lines 1-10 are byte-identical to the build blob** (one-line insertion/deletion diff), so every finding below on lines 1-10 applies equally to the bytes the Q01-Q15 seats reviewed. mtime `2026-10-25 07:18:56 -0300`; not authored by this seat.

## 1. Line-by-line verdicts

Reference anchors: `corpus/SOURCES.md` rows S032`:46`, S034`:48`, S038`:52`, S041`:55`, S043`:57`, S046`:60`, S047`:61`; `corpus/README.md:34` (C05 row).

### `:1 source: S038` — PRESENT, tier/scope correct, re-open only partly recorded → PARTIAL
Row exists (`SOURCES.md:52`: type `spec`, tier `A`, status `mined`, date `2026-10-24` = round 65 — `SOURCES.md:89` ties 2026-10-24 to round 65). Scope matches the row ("field layout … chunk, string-pool, node, attribute and value structures … this tag only"). Anchors: `struct ResChunk_header :218`, enum block `:237-:263`, member lines `:239/241/244/245/246/247/248/253`, structs `:287/461/612/621/677/707`, `attributeStart` `:686/687`, snapshot `56b88bc4…` 86255 B — **every one of the 20 printed lines resolves** (probe in §2). Note: the claim "**re-opened 2026-10-25 by this entry's author**" is corroborated only by `SOURCES.md:92`'s S047 log line ("the bytes are the S038 snapshot re-opened from the repository"); the S038 row itself still reads `mined` / `2026-10-24` and carries no re-open note.

### `:2 source: S043` — PRESENT, tier correct, **status word wrong** → FAIL (accuracy)
Row `SOURCES.md:57`: type `docs`, tier `A`, status **`queued`**, date `2026-10-24`; `supersedes S039` ✓; anchor lines 7-8 and sha `412d9cb4…` ✓ (both verified by grep of the row). The entry says "row **mined** round 66". The registry record for round 66 (`SOURCES.md:90`) is explicit: "included 3 rows (S042 mined own-work, S043 **queued** supersedes S039, S044 **queued** …)". "mined" is not this row's status.

### `:3 source: S045` — PRESENT, tier correct, **opener misattributed** → FAIL (accuracy)
Row `SOURCES.md:59`: type `docs`, tier `A`, status `mined`, date `2026-10-24`; scope (declared `header_item` semantics of one member; not dex validity) and quote text match. But the entry says "**opened 2026-10-24 by this entry's author**"; `SOURCES.md:91` records the opener of S045 as **`L1 revenger-r67`** (round-67 C05 re-gate source opening), not the round-69 author. Also "opened" vs the row's `mined`.

### `:4 source: S032` — PRESENT, tier correct, **scope under-declared for what the entry uses** → FAIL (coverage of the header)
Row `SOURCES.md:46`: type `spec`, tier `A`, status `mined`, date `2026-10-23` (round 63). Row scope *does* cover both records: "central directory file header **and end-of-central-directory record** field layout … §4.3.3, §4.3.12, **§4.3.16**, §4.4.7, §4.4.10-4.4.12, §4.4.16, **§4.4.21-4.4.22**". The entry's line declares only "central directory file header field layout … `§4.3.12` (46-byte fixed part) — the walk in item 3". But **item 2 reads the EOCD record's fields** (`readout.py:78-80`: `cd_size = u32(apk, eocd+12)`, `cd_off = u32(apk, eocd+16)`, `total_entries = u16(apk, eocd+10)`), i.e. the `§4.3.16`/`§4.4.21-22` layout, and that anchor appears nowhere in the entry. The header's only ZIP-spec credit does not name the anchor for a claim the entry makes.

### `:5 source: S034` — PRESENT, tier and scope exact → PASS
`SOURCES.md:48`: `spec`, `A`, `mined`, `2026-10-23`; scope `§4.3.7`, 30-byte fixed part, name length offset 26, extra-field length offset 28 — the entry states exactly these, and the derivation it credits is the code at `readout.py:99-105` (`payload_off = lh_off + 30 + lh_name_len + lh_extra_len`, `:105`).

### `:6 source: S047` — PRESENT, every stated number reproduced → PASS
`SOURCES.md:61`: `own-work`, `A`, `mined`, `2026-10-25` = round 69 ✓. Script sha `74d4c0d9…` ✓, "20 output lines" ✓, snapshot sha `56b88bc4…` ✓ (both copies identical, 86255 B), "exit 2 on a missing or ambiguous symbol" ✓ — probed, not asserted:

```
$ python3 -B corpus/derive_axml_anchors.py | wc -l; echo exit=$?
20
exit=0
$ sha256sum corpus/derive_axml_anchors.py corpus/snapshots/ResourceTypes.h .ufo/waves/round-65/source-snapshots/ResourceTypes.h
74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa  corpus/derive_axml_anchors.py
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  .ufo/waves/round-65/source-snapshots/ResourceTypes.h
# scratch copy of the script, snapshot truncated → digest guard fires, exit 2
derive_axml_anchors: snapshot digest 114db156… != pinned 56b88bc4…
# scratch copy, one symbol renamed → "not found" branch, exit 2
derive_axml_anchors: enum RES_XML_BOGUS_TYPE: not found   (exit=2)
```

### `:7 source: S041` — PRESENT, all four digests true, **no in-entry derivation** → Q11 letter FAIL
`SOURCES.md:55`: `own-work`, `A`, `mined`, `2026-10-24` ✓. All four pins re-derived and equal, both now and at the named claim tree:

```
$ for f in fixture.apk truth.json generator.py readout.py; do git show c7b7cf98:corpus/fixtures/apk-r65/$f | sha256sum; done
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e   (947 B)
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976
```

But the entry contains **zero** deriving commands for any digest: `grep -c sha256sum` = 0, `grep -c "git show"` = 0. Six digests are prose-only: `truth.json 27303bae…`, `generator.py eaa9444c…`, `readout.py 92e347c3…`, `derive_axml_anchors.py 74d4c0d9…`, REA snapshot `412d9cb4…`, dex snapshot `c0428612…` (the fixture `05d2280f…` and the ResourceTypes snapshot `56b88bc4…` *are* printed by `--fact archive` and by the derivation's first line). Contrast the held C07 precedent, which is the corpus's own template: `round-64-firmware-region-byte-evidence.md:31-37` prints `git show 666ea84b…:<file> | sha256sum` with output for exactly this reason.

### `:8 verified-at:` — round correct, byte identity true, two factual errors → FAIL
Date `2026-10-25` is round-69 (`claims.md:3`). The byte-identity clause is true: all four `c7b7cf98` blobs hash to the current files (above). The "captured from actual stdout, never transcribed" clause is true: all **20/20** derivation lines and **15/15** readout lines are verbatim in the entry (`python3` substring check, 0 miss). The round-65 drift citation is true: `round-65-apk-axml-byte-evidence.md:41` prints `4d616e696673742d…` = 30 hex chars = 15 bytes = `Manifst-Version` (dropped `e`). The `:244` citation is true: `round-67-apk-axml-byte-evidence.md:1` places `RES_XML_START_NAMESPACE_TYPE` at `:244` (actual `:245`).

Defects:
1. **Q15's literal failure.** `c7b7cf98` is a stated git object id; it carries no deriving command anywhere in the entry. `QUALITY.md:27` failure mode: "an identity sentence is asserted without the deriving command". Value happens to be correct (verified above) — that is exactly Q11/Q15's "correct but unguarded" branch. Wave-corroborated: `.ufo/waves/round-69/R69ReviewEntryQ15.md:1` FAIL.
2. **The repair sentence is false for Q14.** "the round-68 v3 candidate's **five** Q FAILs (Q04/Q05/Q07/Q11/Q13) are repaired" — `corpus/lessons/round-68.md:15-18` lists FAIL at Q04/Q05/Q07/Q08/Q11/Q13 **and `:62` records Q14 failing too** ("Q14 fails on line 46 …"). So the count is six criteria, and Q14 is not repaired on these bytes: `:48` still reads "a 15-byte `4d616e696673742d…` pair" (16 hex chars, not 2×15=30) — the same defect class `/R69ReviewEntryQ14.md:1` FAILs on.

### `:9 recheck:` — both commands exist, run, and their stated shapes reproduce → PASS
```
$ python3 -B corpus/derive_axml_anchors.py      # exit 0, 20 lines (cited symbols + bounds + attributeStart)
$ python3 -B corpus/fixtures/apk-r65/readout.py # exit 0, 15 lines
$ python3 -B corpus/fixtures/apk-r65/readout.py | sha256sum
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247   # equals the pinned value
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd ; echo exit=$?
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, …}
exit=0
```
"The stdout carries only repo-relative paths, never the extraction root" ✓ (the only path printed is `corpus/fixtures/apk-r65/fixture.apk`). No defect.

### `:10 coverage-map:` — row exists, label matches, status honest → PASS
`corpus/README.md:34` is the C05 row, surface "Android packages (APK)" (exact string match), status cell `uncovered`. The "Not covered" list (install/signature, dex validity, provider readiness, general parser behavior) matches the body's Limitations. No overclaim. Registry note (not a header falsehood): the row's knowledge column is `—` and its evidence cell names only `knowledge/round-65-apk-axml-byte-evidence.md`; the round-67/68/69 candidates are unlisted. That is the pre-flip state the claim requires, but a flip reviewer should know the README does not yet know the v4 file exists.

### `:11 admission-status:` — verdict true, summary selective → PARTIAL FAIL
True parts: `rejected` matches the wave; four named FAIL seats are real (`R69ReviewEntryQ05/Q07/Q14/Q15.md:1`); "the README C05 row stays `uncovered`" matches `README.md:34` (unmodified — `git status --porcelain corpus/README.md` empty); both pointers resolve (`corpus/lessons/round-69.md:31 ## Gate`, `:156 ## Routed forward`); "the round-65, round-67 and round-68 candidates keep every byte" ✓ (last touches `a4c712a` / `712ef61` / `14774a2`; the staged diff touches only the round-69 entry).

False/incomplete parts, measured against the wave's actual decisions (all 15 seat reports on disk, Q01-Q15):
- FAIL seats: **Q05, Q07, Q08 (applied as Q11), Q11, Q14, Q15** — the line names only Q05/Q07/Q14/Q15 and **silently omits the Q11 FAIL**, which is the substantive one (`R69ReviewEntryQ11.md:1`: `504b0506` at `:30`, the 46/30-byte widths at `:37`, and the oracle-agreement sentence carry values with no derivation) and the Q08 seat that failed under it.
- PASS seats: Q01, Q02, Q03, Q04, Q06, Q09, Q10, Q13; Q12 n/a — the line says "Passing on Q01, Q04, Q06, Q10; Q12 n/a", omitting four passing criteria.
- The hedge "Every other decision … recorded in `corpus/lessons/round-69.md` `## Gate`" keeps this a partial summary rather than a false one, but for a header whose whole function is the true state, a 4-of-6 fail list that skips Q11 is not the true state.
- **Entry-internal contradiction:** §Q-map (`:177-184`) still says `pass` for Q05, Q07 and Q14 and has **no Q15 row**, while `:11` says those same criteria failed. The adjudication replaced the status line without reconciling the map it is judged by.

Also checked, because it is in the same line's family: any claim that `reports/round-69/claims.md §C1` holds an "admission order" — it does not; the order is the separate top-level `## Admission order (binding)` (`claims.md:172`). The build-time text (`candidate … claims.md §C1 admission order`) had that dangling sub-pointer; the current text no longer does.

## 2. Findings by severity

| # | sev | finding | evidence |
|---|---|---|---|
| F1 | HIGH | `:8` states git object id `c7b7cf98` with no deriving command → Q15 literal fail (claim is *true*: all four blobs at that commit hash to current bytes) | `QUALITY.md:27`; `R69ReviewEntryQ15.md:1`; `git show c7b7cf98:… \| sha256sum` above |
| F2 | HIGH | `:8` "five Q FAILs (Q04/Q05/Q07/Q11/Q13) are repaired" omits Q14 from the round-68 record and is false for Q14 on these bytes | `corpus/lessons/round-68.md:62`; entry `:48`; `R69ReviewEntryQ14.md:1` |
| F3 | MED | `:11` decision summary omits the Q11 (and Q08-applied-under-Q11) FAILs and four passing criteria | all 15 `R69ReviewEntryQ*.md:1` (Q01-Q15); entry `:11` |
| F4 | MED | §Q-map still `pass` for Q05/Q07/Q14 and has no Q15 row — contradicts `:11`'s own rejection grounds | entry `:177-184` vs `:11` |
| F5 | MED | `:4` S032 scope names only `§4.3.12`, while item 2 reads EOCD fields whose anchor is `§4.3.16`/`§4.4.21-22` (present in the row, absent from the entry) | `SOURCES.md:46`; `readout.py:78-80`; entry `:30` |
| F6 | LOW | `:2` says S043 "row mined round 66"; the row's status is `queued` | `SOURCES.md:57` field 9; `SOURCES.md:90` |
| F7 | LOW | `:3` says S045 "opened 2026-10-24 by this entry's author"; registry opener is `L1 revenger-r67` | `SOURCES.md:91`; `SOURCES.md:59` |
| F8 | LOW | six header digests (truth.json, generator.py, readout.py, derivation script, REA snapshot, dex snapshot) have no command+output; held C07 entry derives its digests this way | entry `:1-7` (0×`sha256sum`, 0×`git show`); `round-64-firmware-region-byte-evidence.md:31-37` |

Divergence to record honestly: `R69ReviewEntryQ02.md:1` PASSes the header (it checks id existence, tier and digest equality; Q02's failure mode is a *missing* header or a bare-homepage anchor, so F5-F7 do not trigger it) and `R69ReviewEntryQ11.md:1` FAILs Q11 on `:30`/`:37`/oracle prose while accepting the header digests. F8 is therefore a strictness *divergence* with the Q11 seat, not a second independent verdict; F1-F4 are not covered by any seat's stated grounds and stand on their own.

## 3. Residual risk and verification gaps

- **Q15 checker cannot see this defect.** `corpus/q15_tree_id_check.py` scans only lines beginning `tree-identity restatement:` / `tree-identity false-sentence:` in the round-69 lesson (module docstring, `PAIR = re.compile(r"…:corpus` = `…")`). `Q15_RESTATE_OK=yes` can therefore be true while `entry:8`'s git object id remains unguarded. Passing the counter is not evidence the entry is clean.
- I did not re-fetch or re-derive the AOSP `ResourceTypes.h` bytes (no network use); the S038 anchors are verified only against the committed pinned snapshot `56b88bc4…`, which is what S047 derives from. Any snapshot-vs-upstream divergence is outside this seat.
- The S043 REA snapshot was not opened; only its registry digest/line citation was matched.
- The counter failure reported independently (`R69ReadmeFlipCheck.md`: `measure.py` `NameError`, exit 1) is outside this scope and was not re-run here.
- Not verified by this seat: whether the adjudication will commit the staged `:11` change, or reconcile §Q-map. Until it does, the working tree carries a rejected status over a Q-map that claims all-pass on three rejected criteria.
