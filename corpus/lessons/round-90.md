# Round-90 lesson — a gate's own denominator, and an android record whose counter is weaker than its evidence

Base `77574c99845ab6662812bd6a88def1e72bf8d71b`; freeze
`c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9` (claims, four instruments, two
batteries with hand labels, red receipts). Two claims, frozen in
`reports/round-90/claims.md`: C1 calibration (SM6 v2, `SM6_MISCLASS` 7/14 →
target 0/14), C2 coverage (android record, `C2_CONJUNCTS` → target 6/6 with
F4 10/11 → 11/11). This lesson is the lane's own evidence, not outside
admission; a seat this lane dispatched is still the lane.

## Gate

### Fixed inputs and controls (all committed at or before the freeze unless marked)

- C1 red: v1 `corpus/self_assessment_check.py` over the base archive scores
  `SM6_MISCLASS=7/14` (`reports/round-90/c1-red-v1-battery.log`) and
  `SELF_MISMATCH=1` (SM6) while the lane's K statement is true — 15 map rows,
  8 held, last K line `K_HELD_BACKED=8/15` (`reports/round-90/c1-real-label.log`).
- C2 reds: F4 `10/11` at base (`reports/round-90/c2-red-f4.log`); oracle v1
  misjudges 5/9 battery cases (`reports/round-90/c2-red-v1-battery.log`).
- C2 controls run after the freeze and before any producer run:
  no-record tree `C2_CONJUNCTS=1/6` (`reports/round-90/c2-control-norecord.log`);
  copy-r89 tree `5/6`, K6 fails (`reports/round-90/c2-control-copy89.log`).
- NOT run before the freeze, although claims.md names the class in prose:
  the id-edited copy and the stubbed-instrument tree. CriticR90Claims ran both
  after the freeze and both reach 6/6 (see Mistakes M-b).

### Source openings (CORPUS rule 1; access date 2026-11-04; quotes re-checked by the L1 against the fetched bytes)

| id | URL / path | located quote (≤25 words) | disposition |
|---|---|---|---|
| S483 | https://developer.android.com/guide/topics/manifest/manifest-element | description: "The root element of the AndroidManifest.xml file. It must contain an <application> element and specify xmlns:android and package attributes." | admit, docs tier A — grounds the root-element and `package` legs of oracle v2/v3 |
| S483 | same | attributes › package: "The value of the package attribute in the APK's manifest file represents your app's universally unique application ID." | admit (second locator) |
| S484 | https://docs.python.org/3/library/xml.etree.elementtree.html (Python 3.15.2 docs) | Parsing XML note: "Currently, this module skips over any XML comments, processing instructions, and document type declarations in the input." | admit, docs tier A — grounds "comments/PIs are not root attributes"; NB the internal DTD subset still applies ATTLIST defaults (ForgeryR90Probe N03/N04), so v3 refuses any DOCTYPE |
| S484 | same | Comment(): "Note that XMLParser skips over comments in the input instead of creating comment objects for them." | admit (second locator) |
| S485 | https://developer.android.com/studio/publish/versioning | Version settings › versionCode: "A positive integer used as an internal version number." | admit, docs tier A, corroborating |
| S486 | `reports/round-89/rejected-android-record/receipt.json` | `:20` — "stdout_sha256": "01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76" | admit, own-work tier A — `supersedes S481` (whose path died at the r89 relocation, D1) |
| S487 | https://stackoverflow.com/questions/2097813/how-to-parse-the-androidmanifest-xml-file-inside-an-apk-package | question body: "This file appears to be in a binary XML format." | **reject** (community, tier C): about decoding binary AXML, silent on root-element semantics; flip: an oracle leg that decodes AXML from the APK itself — then open a primary AOSP source |

Fetch receipts: `.ufo/waves/round-90/w1/ScribeR90Sources/receipts/`. Row
status/recheck/used-by changes: none to existing rows (S481 stays
byte-unchanged; superseded by S486's `teaches`). New rows S483–S487 enter with
the status/recheck shown in `corpus/SOURCES.md`.

### Assimilation and considerthese

**Assimilation: none** (no `merge/revenger/` theme taken; no shokuknow file
read or written). `considerthese/2026-11-04.md` proposal 1 (report new rows by
kind and tier; flag zero-external windows) is applied to this round's own
rows: 5 new rows = 3 external docs tier A (S483–S485) + 1 own-work tier A
(S486) + 1 rejected community tier C (S487); external additions are non-zero.
Proposals 2–5 stay unimplemented.

## Mistakes

| class | evidence pointer | captured-by | fix (shown able to fail?) |
|---|---|---|---|
| reference drift — relocation not swept (r89 D1): `bd575ca` moved the android record but S481's `source` and the readiness checklist `:67` kept the old path | `corpus/SOURCES.md` S481; `corpus/knowledge/2026-10-12-rea-readiness-checklist.md:67`; red `.ufo/waves/round-90/w1/ExecR90SourceCheck/red.log` (`SOURCE_PATH_DEAD=1`, S481) | none before (r89 non-author spot-check D1); new QUALITY Q17 | S486 `supersedes S481`, appended dated correction in the checklist; `reports/round-90/source_path_check.py` — **able to fail: yes**, red over base names S481 and selftest 10/10 legs pass |
| reference drift, repeated by the fix itself: the first draft of S486 carried the dead old path in backticks in its own `source` cell | `source_path_check.py --root .` before the edit printed `DEAD S486 corpus/live/runs/round-89/receipt.json` (`SOURCE_PATH_DEAD=2`) | `source_path_check` (Q17's machine check) | old path rewritten as prose ("the old S481 path"); re-run `EXCUSED S481 by S486`, `SOURCE_PATH_DEAD=0` — the check caught its own author |
| asserted-but-absent table (r89 D2): the r89 lesson's Gate claimed a source-opening table it did not carry | `corpus/lessons/round-89.md:69-74` | r89 spot-check D2; CORPUS rule 1 | this lesson carries the table inline above; not machine-checked (able to fail: no instrument) |
| un-receipted count (r89 D3): "SM2 1 → 0" quoted without a receipt | `SCORECARD.md` r89 routed (3) | r89 spot-check D3; Q11 | receipt landed `reports/round-90/d3-sm2-receipt.log` (base `SM2=1`, tip `SM2=0`, checker sha `82e59fce…`) |
| M-a — oracle v2 matched tag/attribute LOCAL names (chosen to tolerate the producer's `ns1:`/`ns2:` prefixes) instead of the authored expanded names, so a foreign-namespace root, `x:package`, `android:package`, versions bound to another URI and DTD-default attributes all pass | `.ufo/waves/round-90/w1/ForgeryR90Probe/report.md` (40 cases, 7 in-scope + 3 strict + 2 adjacent false greens); `reports/round-90/oracle2-vs-forgery-probe.log` `FALSE_GREEN=12` | none pre-freeze: the frozen 9-case battery had no namespace or DTD case; caught post-freeze by seat ForgeryR90Probe and mutation seat MutR90Oracle (O1/O2/O8 survive the battery) | unclaimed `oracle_check3.py`: exact expanded names from truth.json `ns_idx`, DOCTYPE refusal, two adjacent legs — `FALSE_GREEN=0` over the same 40 (`reports/round-90/oracle3-vs-forgery-probe.log`); **fitted, not held out** (designed after reading the cases) |
| M-b — §9 control named, not built: claims.md stated "hand-edited distinct ids would pass K6" as a limit instead of building that control before freezing; and `c2_counter.py` runs the instruments found inside the TREE without checking `instrument-pins.log` | `.ufo/waves/round-90/w1/CriticR90Claims/receipts/c2-controls.log` (ctl-idedit and ctl-stub both `C2_CONJUNCTS=6/6`); `pins-controls.log` | prompt §9 ("build the cheapest control that skips the claimed work … if it meets the target, the counter or target is wrong") — not applied by the author | next frozen C2 predicate: (i) verify landing-tree instrument digests against the freeze pins; (ii) require rea's own `parseEvidence` id consistency. (ii) shown able to fail this round: the id-edited control is `REJECTED … identifier does not match its record`, the landed runs `ID_CONSISTENT` (`reports/round-90/c2-evidence-id-check.log`); (i) not yet shown |
| M-c — C1's battery tests the forgery only in a format the lane never writes (a bare appended `K_HELD_BACKED 8/14` line); in the lane's own row format v2 reads the evidence-pointer cell and not the stated before→after cell | `.ufo/waves/round-90/w1/CriticR90Claims/receipts/c1-realformat-counterexample.log`; `.ufo/waves/round-90/w1/ReviewerR90C1/step3-fg-probe.log` (8/21 probe shapes false green); MutR90SM6 4/11 mutants survive | none pre-freeze; CriticR90Claims, ReviewerR90C1, MutR90SM6 post-freeze | routed: a next SM6 revision must read the stated cell of the row (or require the K row to state its after-side next to the token) and the battery must carry real-format rows; not built this round |

## Outside verification

No `[x]` and no non-author credit is asserted. The closure should sample the
S483/S484 admits and the S487 reject, the C2 controls (critic's ctl-idedit /
ctl-stub), and re-derive both frozen counters over the landing tree.

## Final measurements (adjudication; landing `abd1394bc612b224381fba29b7b2175a88a108a7`)

| counter | base / control | landing | frozen target | verdict |
|---|---|---|---|---|
| `SM6_MISCLASS` (v1 → v2) | 7/14 (v1, base and landing) | **0/14** (v2) | 0/14 | **MET**; axis label and real-format blind spot contested (M-c, CriticR90Claims Q2) |
| v2 `SELF_MISMATCH` over the landing tree | v1: 1 (SM6) | **0** | 0 (kill b) | holds; SM1–SM5 equal to v1 |
| `C2_CONJUNCTS` | 1/6 no-record; 5/6 copy-r89 | **6/6** | 6/6 | predicate met; **NOT VERIFIED** — ctl-idedit and ctl-stub also 6/6 (M-b) |
| `F4_COVERAGE` | 10/11 | **11/11** | 11/11 (K1) | moved on a real producer record (exact stdout, `ID_CONSISTENT`), not provable by the frozen counter alone |

Receipts: `reports/round-90/c1-after-v2-battery.log`, `reports/round-90/c2-after.log`,
`reports/round-90/holds.log`. Round end census: see the round report.
