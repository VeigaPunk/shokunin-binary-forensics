# ScribeLessonR100 — findings (revenger round 100, wave w1, seat ScribeLessonR100)

Seat: scribe. Drafts only; the L1 integrates. Nothing outside the two draft files and this file was
written; `corpus/` was not touched.

## Files written

| path | what |
|---|---|
| `.ufo/waves/round-100/w1/ScribeLessonR100/round-100-lesson.md` | full draft of `corpus/lessons/round-100.md` — `## Gate` (C1, C2, the two new SOURCES rows, census), `## Mistakes` (M21, M22), `## Frontier`, `## considerthese` |
| `.ufo/waves/round-100/w1/ScribeLessonR100/sources-rows.md` | the exact registry rows S508 and S509 to append, with the derivation table and the census dry-run |
| `.ufo/waves/round-100/w1/ScribeLessonR100/census-dryrun.log` | receipt of the scratch census dry-run over a copy of the registry with the two rows appended |
| `.ufo/waves/round-100/w1/ScribeLessonR100.md` | this file |

## What the drafts assert (and where each fact was re-derived)

**Gate.** C1: the frozen v8 (`sha256 620dfca9…3581`) accepts **12/12** of the round-99 fresh holdout
(`reports/round-100/controls/c1-do-nothing-v8.log`: `HOLDOUT99 accepted=6/6` twice,
`C1_DO_NOTHING … verdict=not-met`; the same receipts are `reports/round-99/controls/post-freeze/holdout99-v8-{c02,c14}.log`,
sha256 `45c8d2db…` / `c1f76e2e…`). The new harness reproduces that shape on the same counter
(`.ufo/waves/round-100/w1/ExecHarness9/v8.log`: `R100_ACCEPTED=12/12`, both controls `control-ok`,
`R100_STUB_SELFTEST=ok`, `R100_VERDICT=not-met`, `harness_rc=1`; harness sha256 `3acdd3a9…bdd362`).
The target run on the frozen v9 is left as `<<L1: …>>`.

C2: fixture digest re-derived — `sha256sum corpus/fixtures/apk-r65/fixture.apk` →
`05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, equal to `truth.json`'s
`image.sha256`. Decoder versions observed: `androguard, version 4.1.4` and `3.0.3` (both rc 0).
Capability-row count 4 at `0350014d` (`reports/round-100/controls/c2-base-capability-rows.log`).

**S508 / S509** — quotes taken from the scout's saved bodies and re-verified by the scribe
(`grep -c -F` → 1 occurrence in each body):

| row | URL | accessed | quote (words) | location |
|---|---|---|---|---|
| S508 | `https://androguard.readthedocs.io/en/latest/tools/androaxml.html` | 2026-11-05 | "Parse the AndroidManifest.xml from an APK and show/save the XML file." (11) | body line 203 of `ag-rtd-androaxml.html` (8751 B, sha256 `6507e760…c2efc`); same sentence at line 4 of the pinned RST `…/androguard/eef97351/docs/tools/androaxml.rst` (205 B, sha256 `a091672b…7c707`) |
| S509 | `https://apktool.org/wiki/the-basics/intro` | 2026-11-05 | "I: Decoding AndroidManifest.xml with resources" (5) | body line 9 of `apktool-wiki-intro.html` (23480 B, sha256 `7e1c418b…7cf4f`); same line at line 28 of `apktool-wiki-intro.mdx` (1626 B, sha256 `f640bbff…6cad8`); version pinned by the v3.0.3 release page (sha256 `3356d86d…8c77`) |

Both are ≤ 25 words, both live in the scout's receipts under
`.ufo/waves/round-100/w1/ScoutSourcesR100/` (twelve HTTP-200 bodies + `fetch-receipts.md`). The
status/used-by old→new lines are in the draft's `## Gate` (both rows new; `mined`,
`used-by corpus/lessons/round-100.md`).

**Mistakes.** M21 — the r99 report's end-census line dropped the 13 × W04 class its own log
records; fix = `reports/round-100/census_line_check.py`, shown able to fail: run by the scribe on
the r99 report + r99 census log it prints `CENSUS_LINE_CHECK=fail missing=W04`, rc 1 (matching
`.ufo/waves/round-100/w1/ExecControlsR100/census-r99-fail.log`); its clean case prints
`CENSUS_LINE_CHECK=pass missing=none`, rc 0. M22 — r99's do-nothing control ran on `61e27feb`
while the claims named the claims-freeze commit `7e6edd4`; fix = the r100 claims name the base
`0350014d` (`reports/round-100/claims.md:3`) and the control logs print it
(`reports/round-100/controls/c2-base-capability-rows.log:1`).

**Frontier.** Rows 507 → 509; tier A 458 → 460; mined 471 → 473; capability rows 4 → 5; the r99
routed items 1/4/5 addressed, 2/3/6 carried; considerthese — no proposal adopted.

## Counting-command outputs (all re-run by this seat)

```
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md          → 507
$ awk -F'|' '… && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md                 → 0
$ tier histogram   → A=458 B=21 C=28
$ status histogram → mined=471 queued=16 rejected=20
$ grep -c W01 reports/round-99/controls/census-round-end.log                     → 21
$ grep -c W04 reports/round-99/controls/census-round-end.log                     → 13
$ grep -cP "\tE[0-9]" reports/round-99/controls/census-round-end.log             → 0
$ grep -c W01 reports/round-100/controls/census-round-start.log                  → 21
$ grep -c W04 reports/round-100/controls/census-round-start.log                  → 13
$ grep -cP "\tE[0-9]" reports/round-100/controls/census-round-start.log          → 0
$ awk '/^## Capabilities/{f=1;next} …' SCORECARD.md | wc -l                      → 4
$ grep -c -i androguard corpus/SOURCES.md                                        → 0
$ grep -c 'apktool\.org' corpus/SOURCES.md                                       → 0
$ sha256sum corpus/fixtures/apk-r65/fixture.apk → 05d2280f…d03e (= truth.json image.sha256)
$ python3 -B reports/round-100/census_line_check.py --report <r99 report> --log <r99 census log>
  CENSUS_LINE_CHECK=fail missing=W04                                              (rc 1)
```

Scratch dry-run (registry copy with S508/S509 appended, lane untouched): 509 rows, malformed 0,
census findings for S508/S509 **0**, tier `A=460 B=21 C=28`, status `mined=473 queued=16
rejected=20`; the lane's real `corpus/SOURCES.md` sha256 is `af0acc09c56c38b9f00b18286cb9140160b533060e6fc52d2e9d5011e068745b`
before and after this seat.

## Exit codes observed

- `census_line_check.py` on the r99 report: **rc 1** (`fail missing=W04`).
- `census_line_check.py` on the synthetic report: **rc 0** (`pass missing=none`).
- `scripts/sources-census.sh validate` over the scratch registry: **rc 1** overall (pre-existing
  E11s for every `mined` row whose used-by path is absent from the scratch copy — an artifact of the
  scratch tree holding only `SOURCES.md`), **rc 0** for the real lane tree at
  `/home/vgpnk/Projects/shokunin`; the new rows produce **zero** findings in either tree.
- `androguard --version` → 0; `apktool --version` → 0.

## Findings the L1 must decide on

1. **`used-by` must be a `corpus/`-prefixed citing file.** The frozen v8 leg
   `C1_USEDBY_GROUNDED` (`reports/round-99/c1_k_admit_counter8.py:740-742`) rewrites any non-`corpus/`
   used-by path to `corpus/<path>` before looking for it. So `reports/round-100/cap_apk_probe.py`
   as a used-by value resolves to a nonexistent path. The draft therefore uses
   `corpus/lessons/round-100.md` (this lesson names S508 and S509). The probe itself cites neither
   id at draft time (`grep -c "S508\|S509" reports/round-100/cap_apk_probe.py` → 0) — re-check at the
   instrument freeze.
2. **E11 ordering.** The census reads a `mined` row's used-by path from disk. If the rows land
   before `corpus/lessons/round-100.md` exists, use `queued`/`—` and flip afterwards, logging the
   flip in the lesson's old→new table.
3. **`<<L1: …>>` placeholders** in the draft mark only post-freeze/post-landing values: the C1
   target run and its three no-regression conjuncts, the C2 probe lines and control logs, the
   round-end census, the verdicts, and the instrument-freeze/landing hashes.
4. **C2 does not probe REA.** The r99 lesson's "Android capability on `corpus/fixtures/apk-r65/`"
   frontier item is taken by r100 in a different sense (two third-party decoders vs authored truth).
   REA's `inspect_android_package` route and the firmware capability on
   `corpus/fixtures/firmware-r63/` remain unprobed; the draft says so explicitly.
5. **Considerthese: nothing adopted.** Proposal 4's producer-attribution census has no frozen
   predicate in `reports/round-100/claims.md` (`grep -c 'producer-attribution'` → 0) and is carried
   to r101 unchanged.
6. **The claim requires the probe to cite the round-100 SOURCES rows; the probe does not yet.**
   `reports/round-100/claims.md:65-67` says "the row **and the probe** cite round-100 SOURCES rows
   for androguard and apktool opened this round (the round's sourced claim)", and the kill rule
   (`:100-101`) says "a capability row that does not cite a round-100 opened source → C2 **not
   verified**". The capability row is the L1's to write (it must cite S508/S509), but the probe
   currently contains no row id: `grep -c "S508\|S509" reports/round-100/cap_apk_probe.py` → 0, and
   `grep -c -i "source" reports/round-100/cap_apk_probe.py` → 0. Since the probe's bytes are not
   frozen yet, ExecApkProbe can still add the citation (a docstring line naming S508/S509 and the
   two source rows' scope). The L1 should check this at the instrument freeze; if the probe never
   cites them, the claim's own "the row and the probe cite" wording is unmet.
   Note the interaction with item 1: even if the probe cites the ids, the probe path still cannot be
   a `used-by` value, because `C1_USEDBY_GROUNDED` would look for
   `corpus/reports/round-100/cap_apk_probe.py`. `corpus/lessons/round-100.md` is the correct
   used-by value, and the lesson draft cites both ids.
7. **The probe leaves `androguard.log` in its working directory.** `git status --porcelain` in the
   lane shows two untracked logs that appeared during this wave:
   `androguard.log` (lane root, 44908 bytes, 19:50–19:52) and
   `corpus/fixtures/apk-r65/androguard.log` (4988 bytes, 19:39). Their content is androguard's
   DEBUG log of the AXML parse of the fixture (string-pool and attribute lines, including the
   tampered `versionName='1.1'` runs), i.e. the decoder writes its log into the cwd it was launched
   from. `androguard --version` alone writes nothing (verified in an empty scratch dir), so the
   leak comes from the `androguard axml` invocation, not from the version probe. If the probe runs
   with the lane root or the fixture dir as cwd, the log lands in the lane tree — the round's
   `git status` is then dirty and an untracked file sits inside `corpus/` (a frozen directory). The
   fix belongs to ExecApkProbe's probe: launch the decoder with `cwd=<scratch>` (or redirect the
   log), so nothing is written outside `--work`. I did not delete or edit either log: they are
   another seat's run artifacts and the L1 may want them as evidence.

## Out of scope / not done

- No `corpus/` write; no git mutation of any kind (`git status`/`log`/`show` only).
- No scored run: the C1 target run on the frozen v9 and the C2 target run on the landing tree were
  not executed (pre-freeze, and they are the L1's).
- No install or upgrade performed; nothing was needed (androguard 4.1.4 via uv tool, apktool 3.0.3
  via an official release jar were already present — channels as recorded by the scout).
- Scratch `/fast/scratch/hyaku/revenger-r100/ScribeLessonR100/` deleted before yield; the census
  receipt was copied into the wave dir first.
