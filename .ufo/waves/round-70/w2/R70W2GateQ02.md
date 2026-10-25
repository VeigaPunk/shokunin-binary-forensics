PASS — Q02 holds on the landed candidate bytes: the entry opens with seven `source:` rows (lines 1-7) each resolving to a tier-A `corpus/SOURCES.md` row with a non-homepage anchor, plus `verified-at:` (line 8), `recheck:` (line 9) and `coverage-map: C05` (line 10); every named recheck command exists and exits 0 from a clean `git archive` extraction, and the gate re-runs all 24 `$` blocks (`checked_blocks=24 problems=0`).

Seat: R70W2GateQ02 · wave 2 (falsify) · fresh seat, criterion Q02 only · judged bytes: `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin show 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd:corpus/knowledge/round-70-apk-axml-byte-evidence.md` (322 lines, sha256 `819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31`).

## Bytes and stability

Extraction used for every run below:

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd | tar -x -C /tmp/revenger-r70-GateQ02
$ sha256sum corpus/knowledge/round-70-apk-axml-byte-evidence.md
819efcb8e2f6065c6b73456ed24502fe0b4e9751c94366e5a6c3f3b4990b4c31  corpus/knowledge/round-70-apk-axml-byte-evidence.md
$ wc -l < corpus/knowledge/round-70-apk-axml-byte-evidence.md
322
```

The entry is not in the working-tree mutating set; the archive extraction is the judged artifact. Scratch `/tmp/revenger-r70-GateQ02` deleted before return.

## Q02 — criterion text (QUALITY.md:16)

> The entry opens with `source:` (its `S###` row, URL or path, exact anchor), `verified-at:` (date or commit) and `recheck:` (the command or citation that re-verifies it), and names the coverage-map row it fills (`corpus/README.md`). | reject when: any header is missing or the anchor is a bare homepage

### 1. Provenance trio present, entry opens with `source:`

```
$ awk 'NR<=8{print NR": "substr($0,1,120)}' corpus/knowledge/round-70-apk-axml-byte-evidence.md
1: source: S038 — AOSP `ResourceTypes.h` (binary resource/XML format structures) — https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h (sp
2: source: S049 — supersedes S043 — REA reverse-engineer-anything skill reference, "Android application artifacts" — https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/re
3: source: S048 — supersedes S045 — Android DEX format specification (AOSP, source.android.com) — https://source.android.com/docs/core/runtime/dex-format (docs, tier A; row opened 2026-10-25 by this entry's author, who re-f
4: source: S032 — PKWARE APPNOTE.TXT 6.3.10 — .ZIP File Format Specification — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row opened 2026-10-23 and mined round 63; re-opened 2026-10-25 by thi
5: source: S034 — PKWARE APPNOTE.TXT 6.3.10 — https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT (spec, tier A; row opened 2026-10-23 and mined round 63, scoped re-open 2026-10-25 by this entry's author from the sa
6: source: S047 — supersedes S046 — AXML anchor derivation (own-work, tier A; row opened 2026-10-25, round 69; re-opened 2026-10-25 by this entry's author by running it) — scope: the printed S038 line numbers and enum value
7: source: S041 — Authored apk-r65 bundle — `corpus/fixtures/apk-r65/fixture.apk`, `truth.json`, `generator.py`, `readout.py` (own-work, tier A; row opened 2026-10-24 and mined round 65) — scope: the byte content of this on
8: verified-at: 2026-10-25 (round-70 build; every output block below was produced by running the command printed above it in this same build and pasting its st
```

```
$ grep -nE '^(verified-at|recheck|coverage-map|admission-status):' corpus/knowledge/round-70-apk-axml-byte-evidence.md
8:verified-at: 2026-10-25 (round-70 build; ...
9:recheck: from the lane root, `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` ... `python3 -B corpus/fixtures/apk-r65/readout.py` (item 15 prints its line count and digest) and the `entry_checks.py` flags named in items 2, 11-14 and 16-17
10:coverage-map: C05 (`corpus/README.md`, Android packages (APK)) — ...
11:admission-status: candidate
```

Seven `source:` rows at lines 1-7, then `verified-at:` line 8 (date form), `recheck:` line 9, `coverage-map:` line 10. `grep -cE '^source: S[0-9]{3} '` = 7.

### 2. Every `source:` row resolves to a tier-A registry row

```
$ for id in S038 S049 S048 S032 S034 S047 S041; do printf "%s " $id; grep -cE "^\| $id \|" corpus/SOURCES.md; done
S038 1
S049 1
S048 1
S032 1
S034 1
S047 1
S041 1
```

Registry locators (from `grep -nE '^\| ?S0(32|34|38|41|47|48|49)\b' corpus/SOURCES.md`), tier column read from the same rows:

| entry line | S-id | SOURCES.md line | tier |
|---|---|---|---|
| 1 | S038 | 52 | A (spec) |
| 2 | S049 | 63 | A (docs) |
| 3 | S048 | 62 | A (docs) |
| 4 | S032 | 46 | A (spec) |
| 5 | S034 | 48 | A (spec) |
| 6 | S047 | 61 | A (own-work) |
| 7 | S041 | 55 | A (own-work) |

Each of those rows also registers this entry in its `used-by` column, e.g. `sed -n '46p' corpus/SOURCES.md` ends `… corpus/knowledge/round-63-zip-central-directory-evidence.md, corpus/lessons/round-63.md, corpus/knowledge/round-70-apk-axml-byte-evidence.md`; same for S034 (:48), S038 (:52, `corpus/knowledge/round-70-apk-axml-byte-evidence.md`), S041 (:55), S047 (:61), S048 (:62), S049 (:63). The two rows the entry marks superseded (S043 :57, S045 :59) also exist, so the `supersedes` names in lines 2/3/6 resolve too.

URL strings match the registry byte-for-byte (`grep -c -- "$url"` on both files): S032 2/2, S034 2/2, S038 1/1, S048 1/2 (registry row plus its live-refetch note), S049 1/1.

### 3. No anchor is a bare homepage; every URL resolves

```
$ for u in <the four header URLs>; do curl -s -o /dev/null -w '%{http_code} %{size_download}' -L --max-time 25 "$u"; done
200 874785  https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h
200 1992  https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md
200 281161  https://source.android.com/docs/core/runtime/dex-format
200 174585  https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT
```

All four are deep file/page locators (a tagged source file, a tag-pinned raw markdown file, a section page, a `.TXT` spec), not a homepage. The two own-work rows (S047 line 6, S041 line 7) carry paths plus digest anchors rather than URLs.

The live fetches also re-derive the header's provenance claims, not just resolvability:

```
$ curl -sL <S049 url> -o live-rea.md; sha256sum live-rea.md corpus/snapshots/rea-android-applications.md
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  live-rea.md
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  corpus/snapshots/rea-android-applications.md      # 1992 bytes both
$ sha256sum live-appnote.txt corpus/snapshots/APPNOTE.TXT
0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6  (both)
$ diff <(tr -d '\r' < live-dex.html) <(tr -d '\r' < corpus/snapshots/dex-format.html) | grep -c '^[<>]'
4        # the two pairs are the per-request CSP nonce and the devsite loader line — "page-chrome lines" as line 3 states
```

Exact anchors are machine-located and independently confirmed against the pinned snapshots:

```
$ sed -n '387p;511p;632p' corpus/snapshots/APPNOTE.TXT
   4.3.7  Local file header:
   4.3.12  Central directory structure:
   4.3.16  End of central directory record:
$ sed -n '686,687p' corpus/snapshots/ResourceTypes.h
    // Byte offset from the start of this structure where the attributes start.
    uint16_t attributeStart;
$ sed -n '7p' corpus/snapshots/rea-android-applications.md
Start with `inspect_android_package` on the caller's APK path for package
```

These match the entry's stated anchors: line 1 "printed by the item-11 command", line 2 "first line 7", line 3 "four quoted phrases … item-11 `--spec-quotes`", lines 4/5 "heading and field line numbers … printed by item 12", lines 6/7 digests printed by item 14. Lines 4 and 5 do not use the literal word `anchors:` but carry the located anchor the criterion requires (section + printed heading/field line numbers), and neither URL is a homepage, so the reject clause does not trigger.

### 4. `recheck:` commands exist and run (clean extraction, lane-root form)

```
$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md; echo exit=$?
checked_blocks=24 problems=0
exit=0
$ grep -c '^\$ ' corpus/knowledge/round-70-apk-axml-byte-evidence.md
24
```

`checked_blocks=24` equals the 24 `$` blocks in the entry, so the gate's "re-runs every `$` command below" clause in line 9 covers every embedded command, including the item-11 derivation and item-15 `--stdout-digest` block.

```
$ python3 -B corpus/fixtures/apk-r65/readout.py; echo exit=$?
exit=0      # 15 lines; sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
$ python3 -B corpus/fixtures/apk-r65/readout.py --fact eocd
{"cd_end_equals_eocd_offset": true, "eocd_offset": 925, "fact": "eocd", "offset_of_start_of_cd": 737, "parsed_entries": 3, "size_of_central_directory": 188, "total_entries_cd": 3}
exit=0
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --stdout-digest
readout stdout: 15 lines, sha256 507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
exit=0
```

The readout stdout hash matches the entry's item-15 line exactly. Every `entry_checks.py` flag named in the `recheck:` line (items 2, 11-14, 16-17) and item 15's flag was run; all exit 0:

```
--eocd            exit=0   "eocd signature bytes at offset 925: 504b0506 (4 bytes)"
--spec-quotes     exit=0   6 MATCH lines (rea :7; dex :5949/:5956/:5981/:5035; ResourceTypes.h :686)
--zip-layout      exit=0   3 width sums + 12 offset MATCH + 3 APPNOTE line-range MATCH + 2 fixed-part MATCH
--oracle          exit=0   40 MATCH lines, no MISMATCH
--pins            exit=0   10 sha256 lines (fixture.apk 05d2280f…, readout.py 92e347c3…, …)
--container       exit=0   3 MATCH lines
--axml-layout     exit=0   5 transcription MATCH + 16 offset MATCH
--stdout-digest   exit=0   (above)
$ python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md
LINT_QMAP=0
LINT_Q14=0
LINT_Q15=0
LINT_HEADER=0
exit=0
```

`--pins` values equal the digests registered in the corresponding SOURCES rows (S038 snapshot `56b88bc4…`, S032/S034 APPNOTE `0b993022…`, S048 snapshot `c0428612…`, S049 snapshot `412d9cb4…`, S041 `05d2280f… / 27303bae… / eaa9444c… / 92e347c3…`), so each anchor resolves to the same bytes the registry pins.

### 5. Coverage-map row named and resolvable

Entry line 10: `coverage-map: C05 (`corpus/README.md`, Android packages (APK))`.

```
$ grep -n 'C05' corpus/README.md
41:| C05 | Android packages (APK) | — | `fixtures/apk-r65`; retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (…) | uncovered |
```

The named row exists, its description matches the entry's parenthetical, and it is still `uncovered` at the landed commit (landing step 1 respected).

## Observations (not Q02 failures; routed for other seats)

- **Wording gap in `recheck:` (line 9).** The enumeration "`entry_checks.py` flags named in items 2, 11-14 and 16-17" omits item 15's `--stdout-digest`. No command is unrechecked: item 15's block is one of the 24 the gate re-runs (`checked_blocks=24`), and `readout.py` is named separately. Q02 asks that recheck commands exist and run, and they do; this is a completeness-of-enumeration nit for Q11/Q13, not a Q02 defect.
- **S048's registry row records a live-page digest that is unstable** (`corpus/SOURCES.md:62`: live page sha256 `d72efc55…`); my refetch of the same URL hashed `ba5482c8…` (281161 bytes both). The entry's line 3 claims only "the live page differs from the snapshot only in page-chrome lines" (verified: 4 diff lines, nonce + loader), and claims no live digest, so the entry's bytes are clean; the row's recorded live digest is the unstable artifact.
- **Wave-1 advisory on typed APPNOTE ranges is repaired in the landed bytes.** `.ufo/waves/round-70/w1/R70W1PreQ01Q02.md` flagged "387-398" / "511-531" typed into `source:` line 4 and item 12. In the landed bytes those numbers appear only as command output (`entry:171-173`: `MATCH APPNOTE 4.3.7: heading line 387, transcribed field lines 389-399`, `4.3.12 … 522-538`, `4.3.16 … 634-646`); the `source:` line 4 and item 12 prose (`entry:152`) point at the command instead. Independent `sed -n '387p;511p;632p'` on the snapshot confirms the headings and the transcribed ranges start/end where the output says.
- Verdict formed before reading `.ufo/waves/round-70/w1/`; the wave-1 file was consulted only for this cross-check, not for the decision.

## Decision

**Q02 = PASS** on `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd:corpus/knowledge/round-70-apk-axml-byte-evidence.md`. No located defect; this PASS does not override any mechanical label and is one of the Q01-Q15 conjuncts C1 requires.

Tools used: `git` (read-only), `python3` 3.x stdlib scripts from the extraction, `curl`. No installs, no pacman, no git writes.
