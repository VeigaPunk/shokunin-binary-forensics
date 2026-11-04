# ScribeR90Sources — round 90 w1 report (revenger lane)

Seat: scribe, leaf. Lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` at HEAD `c7767789fe9e96bcc0d50656ad4bdce69ba3a3a9` (= freeze commit). Read first: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-90/claims.md` (C2 "Sourced" clause :90-95). Judged axis: coverage (sources for C2 oracle v2 legs).

## Behaviour
Opened three official sources and one community candidate, recorded verbatim ≤25-word located quotes, drafted 4 SOURCES.md rows (3 docs + 1 own-work supersession of S481) and the round lesson's `## Gate` table (12 lines: 11 admit, 1 reject).

## Deliverables (all absolute)
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScribeR90Sources/rows.md` — 4 drafted 11-column rows (`S4xx-a..d`; natural landing ids S483–S486, registry ends at S482), S481 status note, optional search-note line.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScribeR90Sources/gate-table.md` — id | URL/path | access date | located quote | disposition.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScribeR90Sources/receipts/fetch-log.md` — URLs, HTTP codes, raw byte counts, raw sha256, fetch time 2026-11-04T22:01:55Z.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScribeR90Sources/receipts/excerpt-manifest.md`, `excerpt-etree.md`, `excerpt-versioning.md` — ±300-char context around each quote from the tag-stripped fetched bytes.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScribeR90Sources/receipts/so-api.json`, `so-api-answers.json` — Stack Exchange API bodies for the rejected candidate.

## Commands / gates (exercised)
- `curl -sSL -A 'Mozilla/5.0'` with `TMPDIR=/fast/scratch/hyaku/revenger-r90/ScribeR90Sources`: manifest-element 200 (316553 B), elementtree 200 (208339 B), versioning 200 (323481 B), stackoverflow q/2097813 HTML 403 (Cloudflare "Just a moment..."); api.stackexchange.com 2.3 question+answers 200.
- Quote check (Python): all 13 quotes found as exact substrings of the whitespace-collapsed, tag-stripped text; word counts 9–22 (all ≤25).
- Row check: every drafted row has exactly 12 `|` (11 cells); every gate line 6 `|`; no `|` inside a cell.
- D1: `reports/round-89/rejected-android-record/receipt.json:20` = `"stdout_sha256": "01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76"` (run1; run2 at :28 = `5bbdd189…`). `git show 6ce41aa:corpus/live/runs/round-89/receipt.json | sha256sum` and `git show c7767789:reports/round-89/rejected-android-record/receipt.json | sha256sum` both = `0afe9eea35bfc1b3cb7b82c8bd3a22de0f7cf26c1ec0f449ff7b7b49b6fada1f`; `corpus/live/runs/round-89` no longer exists (moved by bd575ca), so S481's anchor is dead → S4xx-d `teaches` opens `supersedes S481 —`.
- Registry facts: status vocabulary in `corpus/SOURCES.md` is mined 447 / queued 16 / rejected 19; superseded rows keep their status (S039, S046 stay `mined`), so S481 should stay byte-unchanged.

## Findings
- F1 (scope limit, [INFERENCE] about untested behaviour): the manifest reference says `xmlns:android` "is always set to \"http://schemas.android.com/apk/res/android\"" and lists `android:versionCode`/`android:versionName`. The real producer text (battery P1, r89 record) binds `ns1:`/`ns2:` to the literal URI `android`, and oracle v2 (`corpus/fixtures/apk-r65/oracle_check2.py:12-14`) accepts `versionCode`/`versionName` "any namespace prefix". Battery F5 covers a duplicate under `ns3="other"`; no frozen case covers a root whose ONLY `versionCode` sits in a foreign namespace. By the docstring v2 would accept it. Not a kill against the frozen battery; proposal only: name this in the C2 "Not claimed"/limits text or a future battery case. Instruments not edited.
- F2: the Android reference also states (package attr) "In the Gradle-based build system, starting with AGP 7.3, don't set the package value in the source manifest file directly." — the `package` leg is sound only for the built/merged APK manifest the producer decodes (true for fixture.apk), not for source manifests. Row S4xx-a scope says so.
- F3: Python docs page fetched is the 3.15.2 build; the comment-skipping behaviour is version-stable text but recheck 2027-02-02 covers drift.

## Touched surfaces
Only `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScribeR90Sources/` and the trailer `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-90/w1/ScribeR90Sources.md`. No lane file edited, no git mutation, no commit/push.

## Out of scope
Assigning final S-ids, editing `corpus/SOURCES.md` / the lesson, judging C1/C2.

## Tooling
No tools installed or upgraded (curl, python3, git already present).

## Scratch
`/fast/scratch/hyaku/revenger-r90/ScribeR90Sources` deleted after receipts were copied.

VERDICT: C2's sourced clause is satisfiable — 3 official sources opened 2026-11-04 with located verbatim quotes, 4 rows (incl. supersedes S481) and a 12-line Gate table (1 reject) drafted; one scope-limit finding (namespace-agnostic version legs).
