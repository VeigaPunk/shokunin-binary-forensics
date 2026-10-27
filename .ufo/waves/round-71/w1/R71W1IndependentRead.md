# R71W1IndependentRead — independent APK byte read, C05 v6 pre-gate, gate exit-2 review

**VERDICT: fixture-level claims HOLD under an independent read (items 1–10, all ten item-14 pins, gate 24 blocks/0 problems, lint 0/0/0/0, real-CLI missing-entry exit 2); wave-1 is not landable as frozen — `claims.md` was rewritten after its receipt to a vote mechanism no committed counter implements, a mutant counter briefly occupied the lane worktree mid-wave, one named C2 red-before receipt is absent, the timeout red-before label contradicts its receipt, and the S052 anchor points at a nonexistent `corpus/lessons/round-71.md`.**

Seat scope: read-only. No lane source edited, no producer run, no `readout.py` execution, no task spawn, no commit/push/jj. Scratch `/fast/scratch/hyaku/revenger-r71/R71W1IndependentRead/` (deleted at return). Tools: `python3 3.14.8` (stdlib `struct`/`zipfile`/`zlib`/`hashlib` only), `sha256sum`, `git` (read-only). Host had no pacman need; nothing installed.

## 1. Method — independent of `readout.py`

Three self-written parsers in scratch, run against the committed fixture path only:

| command | exit |
|---|---|
| `python3 -B indep.py` (ZIP EOCD/CD walk) | 1 — **my** parse bug: unpacked EOCD without the second `H`; not a fixture defect |
| `python3 -B indep2.py` (corrected EOCD + CD + LFH + CRC + zipfile cross-check) | 0 |
| `python3 -B indep3.py` (AXML chunk walk, string pool, resmap, start/end element, namespaces) | 1 — **my** bad offset for end-element `name` (`off+24` for a `off+20` field); values re-read at correct offsets in a follow-up one-liner |
| `python3 -B indep4.py` (dex header: magic, checksum, SHA-1, file_size, header_size, endian_tag) | 0 |
| `sha256sum`/`stat` over the ten `corpus/` files named in item 14 | 0 |

Both exit-1 runs are recorded because neither was a fixture mismatch: every value after the fix agreed with the entry. No `readout.py`, `entry_checks.py`, `generator.py` or `derive_axml_anchors.py` was used to obtain these numbers.

## 2. Independent fixture results (candidate `corpus/knowledge/round-71-apk-axml-byte-evidence.md`)

Archive (`fixture.apk`): 947 bytes, sha256 `05d2280f…afe7d03e` — matches item 1 and `truth.json.image`.

EOCD/CD/LFH, parsed by hand at `eocd_offset 925` (`504b0506`), `cd_offset 737`, `cd_size 188`, `cd_offset+cd_size == 925`, `entries_total 3`, comment 0:

| member | CD off | LFH off | name/extra len | payload off | crc recomputed | sha256 | entry item 3 |
|---|---|---|---|---|---|---|---|
| `AndroidManifest.xml` | 0 | 0 | 19/0 | 49 | `962d075f` | `73d1e0f2…afe9fae4` | exact |
| `classes.dex` | — | 465 | 11/0 | 506 | `2635c82a` | `57cfe887…f8d548c2` | exact |
| `META-INF/MANIFEST.MF` | — | 618 | 19/0 | 668 | `e948d738` | `2e5da249…c403c0a49` | exact |

`zipfile.ZipFile.namelist()` and each `ZipInfo` (`compress_type 0`, `flag_bits 0`, offsets 0/465/618) agree with item 16's printed flags/method. `payload_first16_hex` in item 3 matches byte-for-byte (`03000800a0010000…`, `6465780a30333500…`, `4d616e6966657374…`).

AXML member (416 bytes, sha256 `73d1e0f2…`): root `type=0x0003 headerSize=8 size=416`, `size==member`; child chunks exactly at item 4's offsets — `8/0x0001/hs28/size196`, `204/0x0180/hs8/44`, `248/0x0100/hs16/24`, `272/0x0102/hs16/96`, `368/0x0103/hs16/24`, `392/0x0101/hs16/24`; walk lands on 416. String pool: `stringCount 9, styleCount 0, flags 0x0100, stringsStart 64, stylesStart 0`, offsets `[0,10,55,66,76,94,108,122,126]`, strings decode to the nine item-6 values (`android … 1.0`). Resource map: 9 entries, ids `[0×5, 0x0101021b, 0x0101021c, 0, 0]` — matches item 7 and `truth.json`. Start element at 272: `element_name=manifest (index 2), ns=1, attributeStart 20, attributeSize 20, attributeCount 3`; attributes read at `base+16+20+i*20` give `package/com.example.r65` (ns `0xFFFFFFFF`, type `0x03`), `versionCode/1` (ns 0 → `android`, type `0x10`, res_id 16843291), `versionName/1.0` (ns 0, type `0x03`, res_id 16843292) — matches item 8 and the oracle's `axml_declared.attributes`. `0x0100` at 248 = start namespace `android → http://schemas.android.com/apk/res/android`; 368 = end element `ns 0xFFFFFFFF, name_index 2`; 392 = end namespace (prefix 0, uri 1).

dex member (112 bytes, sha256 `57cfe887…`): magic `dex\n035\0`; declared checksum `0x3d120c30` equals `zlib.adler32(body[12:])`; declared 20-byte signature equals `sha1(body[32:])`; `file_size 112`, `header_size 0x70`, `endian_tag 0x12345678`, `link_size/link_off/map_off 0`, string/type id counts 0 — consistent with item 9's printed block (only the four S048-quoted fields are claimed there).

Item-14 pins recomputed with `sha256sum`+`stat` (all ten exact): `fixture.apk 05d2280f… 947`; `truth.json 27303bae… 2466`; `generator.py eaa9444c… 9599`; `readout.py 92e347c3… 11236`; `entry_checks.py 2d4f25f6… 15062`; `derive_axml_anchors.py 74d4c0d9… 4979`; `ResourceTypes.h 56b88bc4… 86255`; `APPNOTE.TXT 0b993022… 174585`; `dex-format.html c0428612… 281157`; `rea-android-applications.md 412d9cb4… 1992`.

Pre-gate state on the worktree: 14 C rows (`grep -c '^| C[0-9]' corpus/README.md`), 8 `| held |$` rows, `C05` row at `corpus/README.md:45` still `uncovered`, candidate `admission-status: candidate` at entry `:12`, §Q-map 16 rows `Q01–Q16` (Q08/Q12 `n/a`, one row each). This is the expected red pre-gate state (K 8/14), not a defect.

## 3. Gate / exit-2 review (read-only runs)

| check | command | result |
|---|---|---|
| embedded-output gate | `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` | `checked_blocks=24 problems=0`, exit 0 — comfortably over the frozen floor of 17, and matches the README row's "gate 24/24" |
| lint | `python3 -B corpus/lint_entry.py --entry …` | `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, exit 0 (a first invocation without `--entry` returned usage exit 64 — my error, not a finding) |
| gate self-test | `python3 -B corpus/check_embedded_outputs.py --self-test` | exit 0, `SELFTEST OK: … missing-entry and timeout legs passed` |
| missing-entry real CLI | `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/nope.md` (stdout only) | exit 2, `could-not-evaluate: entry not found: corpus/knowledge/nope.md`, `grep -c Traceback` = 0 |

Timeout leg of the frozen C2 predicate (120 s) was **not** exercised by this seat (cost); the self-test's injected 1 s leg plus `check_embedded_outputs.py:114` (`could-not-evaluate: command timed out after {timeout}s:`) and `:300-303` (exit 2) are the code-level evidence.

## 4. Findings (wave-1 advisory)

**F1 — the frozen vote conjunct was rewritten after its receipt, and the rewrite matches nothing committed (high).** `pre-registration.txt` records `Claims SHA-256: 1febae1279…` and `Counter SHA-256: d0d59b79…`. `git show HEAD:reports/round-71/claims.md | sha256sum` = `1febae12…` (matches the receipt); the worktree file is `5b95d343…` (`git status`: modified, `git diff` +3/−3). The three changed sentences are the frozen vote conjunct and its two dependants. What the receipted text says vs the worktree text:

| receipted (HEAD, `1febae12…`) | worktree (`5b95d343…`) |
|---|---|
| counter "parses committed per-seat JSON vote files under `.ufo/waves/round-71/w2-votes/`; each carries a unique seat" | counter "reads …/w2-results.json, binds four named reviewer seats to their assigned Q subsets, and parses their final `output` text" |
| wave-2 seats "each assigned reviewer writes its JSON vote file at the path specified in its task" | reviewers "return their decisions in the orchestrator's `w2-results.json`" |
| control D reaches K 9/14 "but fails the frozen vote-file predicate at `C1_W2_Q_VOTES=0/16`" (no `w2-votes/`) | control D "has no orchestrator `w2-results.json`, so `C1_W2_Q_VOTES=0/16`" |

The committed, receipt-matched counter implements the **first** column, not the second: `git show HEAD:reports/round-71/measure.py` `q_votes()` reads `LANE/'.ufo/waves/round-71/w2-votes'`, requires `path.stem == data['seat']`, `set(decisions) == set(EXPECTED_VOTES[seat])` and values in `('PASS','n/a')`, and returns 0 on any stray file. No committed counter anywhere reads `w2-results.json`. So the worktree claims now describe a vote mechanism that the frozen counter cannot score: 16 correct per-seat files yield `C1_W2_Q_VOTES=0/16` under the amended text's description, and a single `w2-results.json` yields 0 under the frozen code. **Repair (minimal, and the only one that keeps the freeze): revert `claims.md` to `1febae12…`, whose text and the frozen counter agree.** Any switch to `w2-results.json` needs a new counter, which the frozen rule forbids after seats have scored.

**F7 — a mutant counter was live in the lane worktree during wave 1 (high).** `measure.py` worktree state across three reads in this seat: (1) `d0d59b79…` — equals the receipt, `git status` clean; (2) `39e92bab…` with `git diff` +41/−12, adding a `vote_pairs()` regex parser and a `q_votes()` that reads `w2-results.json`; (3) `d0d59b79…` again, `git status` clean. The intermediate version is exactly the design the amended `claims.md` describes, i.e. a mutation-methodology artifact, not a landed change — and it was written into the **lane worktree**, not a fixture copy. Consequence: any wave-1 seat that runs or reads `measure.py` inside such a window scores a predicate no receipt covers; the final measurement must assert `sha256 reports/round-71/measure.py == d0d59b79…` first and abort otherwise. **Repair:** mutation seats must run only in `/fast/scratch/...` copies (as the counter itself already does for its own fixtures), and L1 should add the counter-digest assertion to the final measure step.

**F2 — a named C2 red-before receipt does not exist (medium).** `reports/round-71/claims.md:23` says "Red-before receipts are `controls/C2-missing-before.log` and `controls/C2-timeout-before.log`". `git ls-files` and `ls reports/round-71/controls/` show only `A-…`, `B-…`, `C-…`, `C2-timeout-before.log`, `D-…`. The observation survives in the frozen red-before (`measure-before.log:12` `C2_MISSING_ENTRY_EXIT2=0/1 rc=1 stderr_traceback=yes`), so the repair is one file or one sentence, but as written the claim names an artifact that is absent.

**F3 — the timeout leg's red-before label contradicts its own receipt (medium).** `measure-before.log:13` records `C2_TIMEOUT_EXIT2=0/1 rc=1 stderr_traceback=no`, while `controls/C2-timeout-before.log` ends with a full `subprocess.TimeoutExpired: … timed out after 120 seconds` traceback and `RC=1`. `reports/round-71/build-controls.py:21` builds that log as `p.stdout+p.stderr`, so the `.log` cannot witness the stderr-only property the counter prints, and the counter's `no` is the only stream-specific record. Consequence: `claims.md:23`'s "produces `TimeoutExpired` traceback and exit 1" is attested only by a merged-stream log, and the frozen label is consistent with this leg having gone red for a non-timeout reason (rc 1 is also the drift exit). [INFERENCE] on cause — the base gate's uncaught `TimeoutExpired` should reach stderr. The predicate still demands exit 2 + declared text + no traceback, so this is a premise/prose defect, not a predicate hole. **Repair:** regenerate the red-before with captured streams, or restate the Before sentence as merged-output evidence.

**F4 — dangling evidence anchor in the candidate's newest source row (medium-low).** Entry `:8` (S052) ends "recorded in `corpus/lessons/round-71.md` `## Gate`". `ls corpus/lessons/` = `round-69.md`, `round-70.md`, `round-70-verifier-spotcheck.md` — no `round-71.md` (2026-10-27). The row's other requirements are met: access date `2026-10-27` present, and a ≤25-word located quote exists both in `corpus/SOURCES.md:66` ("MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;") and in item 11's output; `--spec-quotes` prints six phrases as the row states, and I reproduced all six source lines' shape in item 11's block. **Repair:** create the Gate draft (round-71 lesson) carrying that quoted line, or reword the anchor to `corpus/SOURCES.md:66`.

**F5 — preservation and census hold (informational).** `corpus/SOURCES.md` row count 51 at base `b7abcd8` → 52 now (census command reproduced verbatim), and `git status --porcelain` reports no modification under `corpus/`, so the five earlier rejected C05 entries are byte-preserved. HEAD `18200a4` ("round-71: build v6 candidate and gate exit-2 cases") contains the candidate; at first read only `claims.md` was dirty, and `measure.py` went dirty and clean again inside this seat's window (F7).

**F6 — the frozen counter's provenance root is unguarded (medium, attack on the frozen conjunct).** `q_votes()` accepts any JSON file at `.ufo/waves/round-71/w2-votes/` whose basename equals one of the four `EXPECTED_VOTES` names (`measure.py:42-47`) and whose `decisions` cover that seat's four Qs with `PASS`/`n/a`. Nothing binds a vote file to wave-2 provenance: no commit boundary, no nonce, no seat-run identity beyond the filename. The four seat names are printed in the frozen counter and in the wave-1 dispatch, so any seat with lane write access could pre-write four well-formed vote files before wave 2 and drive `C1_W2_Q_VOTES=16/16` with zero wave-2 decisions. The directory does not exist yet (`.ufo/waves/round-71/` holds `sources-s052/`, `w1/`, `w1-dispatch.json`, `w1-spec.json`, `w1.ready*` — no `w2-votes/`), so the mitigation is procedural and cheap: L1 asserts the directory is absent at wave-1 close, lands wave-2 vote files only in the adjudication commit, and records that commit id beside the final measure. Note also that the frozen parser accepts only lowercase `n/a` (`value not in ('PASS','n/a')`), so a reviewer writing `N/A` scores 0 — a real wave-2 trap worth stating in the seat tasks.

## 5. Repairs recommended before the final candidate

1. Revert `claims.md` to the receipted `1febae12…` text (it matches the frozen counter) — F1 is the only finding that touches the frozen contract itself, and reverting is the only repair that keeps the freeze.
2. Assert `sha256 reports/round-71/measure.py == d0d59b79…` at the start of the final measure and confine mutation runs to scratch — F7.
3. At wave-1 close, confirm `.ufo/waves/round-71/w2-votes/` is absent, and state the lowercase-`n/a` requirement in every wave-2 vote task — F6.
4. Add `controls/C2-missing-before.log` at the named path, or correct the sentence — F2.
5. Regenerate or restate the C2 timeout red-before — F3.
6. Create `corpus/lessons/round-71.md` `## Gate` or fix the S052 anchor — F4.
No fixture, gate or counter change is warranted: byte evidence, pins, gate 24/0, lint 0/0/0/0 and the real-CLI exit-2 missing-entry leg all reproduce.

## 5b. Post-report verification — A1 landing (checked after L1's restoration)

Re-read after L1 reported the restoration:

| item | state | evidence |
|---|---|---|
| F1 | **resolved** | `sha256sum reports/round-71/claims.md` = `1febae12…` = receipt; the three amended sentences are gone |
| F6 (parser half) | **resolved** | `q_votes()` back to `LANE/'.ufo/waves/round-71/w2-votes'`, `path.stem == seat`, exact per-seat Q set, `('PASS','n/a')`; the w2-results/vote_pairs variant is gone |
| A1 | **verified as documented** | counter now `fbd81050…`; `git diff reports/round-71/measure.py` is one line — probe entry `$ python3 -B sleeper_r71.py` → `$ python3 -B corpus/sleeper_r71.py`; `pre-registration.txt` diff is purely additive (one appended A1 paragraph naming `measure-amendment-A1.md`, `fbd81050…`, unchanged claim hash); `reports/round-71/measure-amendment-A1.md` exists (1579 bytes) |
| F3 | **confirmed and explained by A1** | A1 states the old probe path ran from `TREE` and produced drift ("command exited 2") instead of the timeout — exactly the non-timeout red my F3 flagged from `measure-before.log:13 rc=1 stderr_traceback=no`; `R71W1Sentinel` §F1 independently reproduced it |
| F7 | **superseded** | the lane counter now carries only the documented A1 delta; the transient mutant window remains the reason to assert the counter digest at final measure |
| F2 | **open** | `controls/C2-missing-before.log` still absent; `controls/` holds `A-…, B-…, C-…, C2-timeout-before.log, D-…` |
| F4 | **open** | `corpus/lessons/round-71.md` still absent while entry `:8` cites it |

**F8 (new, high) — the frozen red-before receipt is currently empty.** `stat reports/round-71/measure-before.log` = `0 bytes`, mtime `2026-10-27 12:26:27`, while `git show HEAD:…` holds the 48-line receipt (K 8/14, `C2_MISSING_ENTRY_EXIT2=0/1`, `C2_TIMEOUT_EXIT2=0/1`, ten `HOLD … exit=0` rows, `HOLD_REPLAY=10/10`, `HOLDS_OK_V8=yes`, `MEASURE_EXIT=0`). `pgrep -af measure.py` shows the replacement in flight: pid 3833310 running `reports/round-71/measure.py /fast/scratch/hyaku/revenger-r71/L1-prereg-rerun/tree`, with the shell redirecting its output into this file (a redirected run truncates at start and leaves 0 bytes until the writer flushes/exits; the 120 s timeout leg dominates its runtime). A1 states the red-before "is re-run … and replaces the prior receipt", so this is a replacement in progress, not lost data — HEAD still holds the 48 lines — but until the re-run lands, `pre-registration.txt`'s Red-before line and every control comparison point at an empty file. Two requirements before wave 2: (a) the regenerated file must exist and be non-empty with `MEASURE_EXIT=0`, and (b) because it is produced after wave-1 seats scored, its values should be diffed against the HEAD receipt and any movement other than the timeout leg labelled in A1 (`C2_TIMEOUT_EXIT2` may legitimately change its *reason*, but must stay red on base).

## 6. Not verified / limits

Item 15 (`readout.py` 15 stdout lines + `507d79f8…`) and item 3's `payload_offset` literal were not re-executed (no-`readout.py` seat rule); they are corroborated only indirectly by the matching pins and my direct parse. The 120-second production timeout leg, `measure.py`'s full counter run, and any wave-2 vote file are outside this seat. No new external source row was opened by this report; source quotes above are lane files read 2026-10-27.

## Appendix — scratch receipts (copied here before scratch deletion)

Parser sources (94 lines total, stdlib only) were removed with the scratch dir; their digests are recorded so the run is identifiable: `indep.py 7b631999…b919e3`, `indep2.py 7748eaef…6be911b`, `indep3.py eaa00aca…0657f076f1d0`, `indep4.py dc3a4947…36c52d31f`.

```
$ python3 -B indep2.py
eocd_off 925 disks 0 0 entries_this 3 entries_total 3 cd_size 188 cd_off 737 comment 0
cd_off+cd_size 925 ==eocd True
CD[0] 'AndroidManifest.xml' flags=0x0000 method=0 crc=962d075f csz=416 usz=416 lhoff=0 | LFH name='AndroidManifest.xml' flags=0x0000 meth=0 crc=962d075f payload_off=49 csz=416 | crc_recomp=962d075f sha256=73d1e0f2…afe9fae4 first16=03000800a001000001001c00c4000000
CD[1] 'classes.dex' flags=0x0000 method=0 crc=2635c82a csz=112 usz=112 lhoff=465 | LFH name='classes.dex' flags=0x0000 meth=0 crc=2635c82a payload_off=506 csz=112 | crc_recomp=2635c82a sha256=57cfe887…f8d548c2 first16=6465780a30333500300c123da5fc7bea
CD[2] 'META-INF/MANIFEST.MF' flags=0x0000 method=0 crc=e948d738 csz=69 usz=69 lhoff=618 | LFH name='META-INF/MANIFEST.MF' flags=0x0000 meth=0 crc=e948d738 payload_off=668 csz=69 | crc_recomp=e948d738 sha256=2e5da249…c403c0a49 first16=4d616e69666573742d56657273696f6e
cd_walk_end 925
zipfile.namelist ['AndroidManifest.xml', 'classes.dex', 'META-INF/MANIFEST.MF']
   AndroidManifest.xml 416 416 962d075f 0 0 0 / classes.dex 112 112 2635c82a 465 0 0 / META-INF/MANIFEST.MF 69 69 e948d738 618 0 0
EXIT=0

$ python3 -B indep3.py
root type=0x0003 headerSize=8 size=416 size==member True
  off=8 type=0x0001 headerSize=28 size=196 | off=204 type=0x0180 headerSize=8 size=44 | off=248 type=0x0100 headerSize=16 size=24
  off=272 type=0x0102 headerSize=16 size=96 | off=368 type=0x0103 headerSize=16 size=24 | off=392 type=0x0101 headerSize=16 size=24
pool stringCount=9 styleCount=0 flags=0x0100 stringsStart=64 stylesStart=0 utf8=True
offsets [0, 10, 55, 66, 76, 94, 108, 122, 126]
strings ['android', 'http://schemas.android.com/apk/res/android', 'manifest', 'package', 'com.example.r65', 'versionCode', 'versionName', '1', '1.0']
resmap off 204 entries 9 ids ['0x00000000'×5, '0x0101021b', '0x0101021c', '0x00000000', '0x00000000']
start_el off=272 ns=1 name_idx=2 attributeStart=20 attributeSize=20 attributeCount=3 idIdx=0 classIdx=0 styleIdx=0 name=manifest
  attr0 ns=4294967295(None) name=3(package) raw=4(com.example.r65) data_type=0x03 data=4
  attr1 ns=0(android) name=5(versionCode) raw=7(1) data_type=0x10 data=1
  attr2 ns=0(android) name=6(versionName) raw=8(1.0) data_type=0x03 data=8
chunk 0x0100 off=248 line=1 prefix=android uri=http://schemas.android.com/apk/res/android
end_element off=368 type=0x0103 hs=16 size=24 line=1 ns=4294967295 name_idx=2
end_namespace off=392 type=0x0101 hs=16 size=24 line=1 prefix=0 uri=1

$ python3 -B indep4.py
dex len 112 sha256 57cfe887…f8d548c2 magic b'dex\n035\x00'
checksum=0x3d120c30 (adler32 body=3d120c30) ; full-file adler32=439e0e9e
signature a5fc7bea8fa9ffaa52243540c8026066511b9fce sha1(body)= a5fc7bea…6511b9fce match True
file_size=112 header_size=0x70 endian_tag=0x12345678
link_size=0 link_off=0 map_off=0 ; string_ids_size=0 string_ids_off=0 type_ids_size=0 type_ids_off=0
EXIT=0

$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/nope.md   (stdout only)
could-not-evaluate: entry not found: corpus/knowledge/nope.md
EXIT=2   ; grep -c Traceback missing.log = 0

$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed
EXIT=0
```
