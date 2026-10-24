NOT-FALSIFIED — README row C05 has been `frontier` continuously and byte-identically since it was introduced by the a7acc20 freeze commit; no prior knowledge file, fixture ground, or saved `inspect_android_package` record exists on this surface, so `round-65-apk-axml-byte-evidence.md` is the first knowledge text on that ground with no prior partial text to contradict.

# Scope
Seat: coverage-ground check — `git log -p -- corpus/README.md` for the C05 line (read-only), confirm `frontier` continuously since the map's `a7acc20` freeze, and confirm first-knowledge status.

# Evidence

## 1. C05 row origin — introduced at the freeze commit itself
`git log --format='%h %s' -S '| C05 |' -- corpus/README.md` returns exactly one commit:

```
a7acc20 round-1: quality bar, pre-admission coverage map, mined mistakes
```

At a7acc20 the row was born as `frontier` (`git show a7acc20:corpus/README.md:30`):

```
| C05 | Android packages (APK) | — | — | frontier |
```

## 2. Zero row mutations since the freeze; byte-identical to HEAD
`git log -p -- corpus/README.md | grep -nE '^[+-]\| C05'` yields exactly one diff line — the `+` addition at a7acc20. Every later appearance of C05 in diffs is unchanged context (seen while C04/C06/C07 rows mutated around it: C04 held→uncovered→held across 0b6ddf0/7a66d22/0651c7c, C06 partial→held at f6ea293, C07 frontier→held at cab8085).

Byte-identity check:

```
$ diff <(git show a7acc20:corpus/README.md | sed -n 30p) <(git show HEAD:corpus/README.md | sed -n 34p)
IDENTICAL
sha256 df899a34d0b57ca43a81ac01088483c5b1a5e70c18171b75f835bdfae9a50a57 (both)
```

Row value at every sampled commit (a7acc20, 35b2e8b, 0b6ddf0, 7a66d22, 0651c7c, cab8085, c7b7cf9, 5a2e7a0, 6f1761a, 5b4d29e, 8214e4d=HEAD): `— | — | frontier` in both the knowledge and work-evidence columns. Line number drifted 30→31→34 only because neighbouring rows' text grew.

## 3. The only C05-adjacent README change was a notes-section sentence, not the row
At 35b2e8b (round-61 build) the "open coverage" notes sentence was reworded from `— C05 Android — REA inspect_android_package; needs an authored APK fixture.` to `… jadx 1.5.6 is present; needs an authored APK fixture.` (current `corpus/README.md:69-70`). This is environmental tooling info under the table, not knowledge, not a saved record, and does not touch the row or its status semantics.

## 4. No prior knowledge or fixture file on the C05 ground
```
$ git log --all --format='' --name-only -- corpus/knowledge/ | sort -u | grep -iE 'apk|android|axml|aapt'
corpus/knowledge/round-65-apk-axml-byte-evidence.md        ← the round-65 candidate itself; nothing else, ever
$ git log --all --format='' --name-only -- corpus/fixtures/ | sort -u | grep -iE 'apk|android'
corpus/fixtures/apk-r65/{fixture.apk,generator.py,readout.py,truth.json}   ← all added at c7b7cf9
$ git log --all --format='%h %s' -- corpus/fixtures/apk-r65
c7b7cf9 round-65: candidates — apk-r65 fixture+readout … (no README flip)
```
`git show --stat c7b7cf9` confirms that commit touched fixture + knowledge + SOURCES/lesson files only — README is absent from its stat, consistent with "no README flip".

## 5. `frontier` is legend-correct for C05 — no hidden saved record (contrast C07/M36)
Legend `corpus/README.md:24` defines `frontier` = "no knowledge and no saved record". `grep -rlni 'android' corpus/live/` returns **zero files**; the only `APK`/`apk` hits in `live/runs` are inside a caveat sentence of unrelated ZIP-inventory records ("Bytes after the central directory, including an APK Signing Block … are not occurrences") in `20261012T164246Z/artifact-inspection.json`, `round-11/inner-inspection.json`, `round-11/outer-inspection.json` — all with `operation: inspect_artifact`/`inventory_artifact`, none `inspect_android_package`. So unlike C07's M36 drift (saved `inspect_firmware_regions` record under a `frontier` label, lessons/round-64.md:182), C05's `frontier` label is accurate.

## 6. Candidate entry is consistent with first-knowledge status
`corpus/knowledge/round-65-apk-axml-byte-evidence.md` header carries `coverage-map: C05` and `admission-status: candidate`; there is no earlier entry, retained rejected candidate, or pre-contract text naming C05 to contradict it. `grep -rn 'C05' corpus/lessons/` shows only round-65 lesson/spotcheck prose describing this pending admission — no earlier C05 episode.

# Observed vs inference
- Observed: all file contents, diffs, sha256s, commit list, and greps above.
- Inference: "no prior partial text" rests on (a) knowledge-column `—` unchanged since creation, (b) no other knowledge filename ever matching the surface, (c) no `android`/`inspect_android_package` saved record under `live/runs/`. Together these cover the places the legend allows prior text or records to live.

# Remaining unknowns
- jj working-copy commits (empty-subject `3393680`, `eeb3d78`, `9324a6e` visible via `--all`) contain fixture paths; they are ephemeral index states, not landed history, and do not affect the row's continuity. Working tree `git status` shows only untracked `.ufo/` wave files — README clean.
- Whether the candidate *should* be admitted is the Q01–Q13 seats' question, not this seat's; this report only confirms the ground was empty.

Report: .ufo/waves/round-65/R65ScoutC05Ground.md
