UNVERIFIED-REACHABLE — fetch succeeded (HTTP 200, 280121 bytes); staged row S099's own anchors are NOT in the fetched bytes because staged S099 cites a different URL (GitHub API REA commits); the staged row that cites register S099's URL is S100, and all of its page anchors verify.

# R67QuarS099 — quarantine hand-check, register row S099 (round3, prose-class)

## Register row (the verdict under test)
`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/assimilation/register-rows.json:177-183`:
```json
"S099": {
  "round": "round3",
  "class": "the cited source could not be fetched, so no quote was checked",
  "url": "https://developer.android.com/tools/apkanalyzer",
  "quotes": "",
  "note": "prose-class row (register unchecked family; staged-row quote checked separately)"
}
```
Register quotes cell is EMPTY — nothing was ever checked for this row → `unverifiable-unreachable`, not fabrication. Confirmed also in `.ufo/waves/round-67/assimilation/quarantine-slice:26` and `reports/round-67/claims.md:22-23`.

## Fetch receipt (2026-10-24)
```
curl -sL --max-redirs 15 https://developer.android.com/tools/apkanalyzer
http_code      = 200
url_effective  = https://developer.android.com/tools/apkanalyzer (no redirect to different host)
size_download  = 280121 bytes  (<= 2MB → saved)
sha256         = fe83dc05611c5927130c38f6e177ff7c6d2876150840cba5ea88fc98efa41aae
saved          = .ufo/waves/round-67/quarantine/S099/source.bin
```
**The register's unreachable claim is now STALE**: the source fetched cleanly on 2026-10-24. The prose-class verdict `unverifiable-unreachable` stands as the register's historical finding, but the reachability basis ("could not be fetched") no longer holds.

## Staged-row anchor extraction
Staged row S099 — `/home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md:60` — cites a DIFFERENT URL:
`https://api.github.com/repos/morluto/rea/commits?path=docs/readme/README_zh.md&per_page=10`
Its anchor/quote cells: commit `520f8e8042c39833fb1656d3e55fb2896bff43a5`, `2026-10-23`, `"fix(runtime): align remaining Node security pins and setup guidance (#6316)"`, `Refs #6480`, path `docs/readme/README_zh.md`.

The staged row that cites THIS URL is **S100** — `SOURCES.append.md:61`: `"apkanalyzer" — Android Developers — https://developer.android.com/tools/apkanalyzer`, anchors: page `<meta name="description">` and `<meta name="keywords">`.

## Anchor checks against fetched bytes (fixed-string, `grep -cF`)

Staged S099 anchors vs apkanalyzer bytes — all ABSENT (as expected, URL mismatch):
```
520f8e8042c39833fb1656d3e55fb2896bff43a5                                       0
fix(runtime): align remaining Node security pins and setup guidance (#6316)    0
Refs #6480                                                                   0
docs/readme/README_zh.md                                                     0
morluto                                                                      0
api.github.com                                                               0
```

Page anchors vs fetched bytes — all PRESENT:
- `<title>apkanalyzer &nbsp;|&nbsp; Android Studio &nbsp;|&nbsp; Android Developers</title>` — verified.
- `<h1 class="devsite-page-title">` → text `apkanalyzer` (source.bin:8874-8875) — verified.
- Footer `Last updated 2026-03-05 UTC.` — verified (2 occurrences).
- `<meta name="description" content="Learn about the APK Analyzer and how you can reduce the time you spend debugging issues.">` — verified (this is staged-S100's anchor).
- `<meta name="keywords" content="apkanalyzer,APK analysis,command-line tool,Android development,APK size,DEX files,manifest,resources,APK comparison,debugging">` — verified (staged-S100's anchor).
- Supporting strings: `apkanalyzer`×36, `APK Analyzer`×6, `manifest`×15, `command-line tool`×1.

## ID-mapping note (coverage)
Register S099 ↔ staged S100; register S098 ↔ staged S099 — a consistent one-position offset between the register's row numbering and the staged append file's numbering for this pair. This matches the documented "by-document renumber obligation" (`reports/round-67/claims.md:24-25`, `corpus/lessons/round-67.md:14-15`) — a renumber drift to record, not an error in either document.

## Verdict detail
`UNVERIFIED-REACHABLE`: the cited source for register S099 is reachable today, and every anchor named for the apkanalyzer URL (in staged row S100) verifies byte-for-byte. The staged row literally named S099 anchors to a different source and its strings are absent from these bytes — consistent with the register note that its S099 quote was checked separately and found in none of them.

Bounds kept: wrote only this report + `quarantine/S099/source.bin` under `.ufo/waves/round-67/`; `/home/vgpnk/Projects/shokuknow` read-only; no installs.
