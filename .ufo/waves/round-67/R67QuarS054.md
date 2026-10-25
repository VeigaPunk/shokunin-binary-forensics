UNVERIFIED-REACHABLE — fetch of https://source.android.com/docs/core/runtime/dex-format succeeded (HTTP 200, 0 redirects); all three staged anchors verified verbatim in the fetched bytes, so the staged quote material is reachability-confirmed (row itself stays `unverifiable-unreachable` per its PROSE-CLASS standing — this report supplies the reachability + anchor evidence behind that verdict, not a held claim).

# Seat
R67QuarS054 — quarantine hand-check, wave-4 item 10. Campaign register row **S054** (round round1), PROSE-CLASS / unchecked family: no quote was ever checked, verdict `unverifiable-unreachable`.

# Register-ID resolution (important for the judge)
The campaign (pre-remap) id `S054` does not equal the staged id `S054`. Per `/home/vgpnk/Projects/shokuknow/lanes/revenger/ID-REMAP.md:22` — `| round1 | S054 | S055 |` — campaign round1 row `S054` was renumbered to staged **S055** at packaging (staged rows shifted so no staged id collides with lane-registry ids; lane registry ends at S045).
- Campaign row **S054** → staged row **S055** in `/home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md:16` → `https://source.android.com/docs/core/runtime/dex-format` — matches the URL named in this seat's brief. ✔
- The literal staged row `S054` (`SOURCES.append.md:15`) is the **jadx v1.5.6 GitHub release** (a different source, campaign S053 per `ID-REMAP.md:21`); a round-blind `S054` lookup would check the wrong row. Verified, not assumed.
- Same underlying source also exists in the lane registry as **S045** (per goal context: dex declared-header row, used-by the C1 v2 entry; a sibling seat owns that check — out of scope here, noted only for identity).

# Staged row cells (extracted verbatim, `SOURCES.append.md:16`, id `S055`)
- cited source: `Android Open Source Project, "Dalvik executable format" — https://source.android.com/docs/core/runtime/dex-format`
- class/grade: `spec | A`
- scope: `the .dex container format as published by AOSP, and specifically what the .dex format does not define`
- **anchor cell**: `page title "Dalvik executable format" and § dalvik.annotation.Signature; page footer "Last updated 2026-10-09 UTC"`
- quote-reason cell: `ground claims about the .dex format in the published spec rather than in a decompiler's rendering of it`
- provenance: `mined | 2026-10-23`; re-check: `180d — re-open the AOSP page and re-read the "Last updated" date`
- used-by: `corpus/knowledge/android-dex-format-scope.md, corpus/knowledge/android-decompilation-is-a-lossy-transformation.md`

# Fetch evidence (2026-10-24, this host)
- Command: `curl -sL --max-redirs 15 -o source.bin -w '%{http_code}' 'https://source.android.com/docs/core/runtime/dex-format'`
- Result: `HTTP=200`; `url_effective=https://source.android.com/docs/core/runtime/dex-format` (0 redirects, HEAD re-check `curl -sIL` → 200, `num_redirects=0`)
- Bytes: **281,161** (≤ 2 MB → saved)
- sha256: `f02de46b4b813827b6c447e6acbdfea64e315f12e92ef3f4fbc530831b9e2b57`
- Artifact: `.ufo/waves/round-67/quarantine/S054/source.bin` (under `/home/vgpnk/Projects/shokunin/revenger-shokunin/`)

# Anchor checks (fixed-string, `grep -F` / `grep -o` against fetched source.bin)
1. **Page title — VERIFIED.** `<title>Dalvik executable format &nbsp;|&nbsp; Android OS core topics &nbsp;|&nbsp; Android Open Source Project</title>`; `<h1 class="devsite-page-title">` body = `Dalvik executable format`.
2. **§ `dalvik.annotation.Signature` — VERIFIED.** Literal `dalvik.annotation.Signature` occurs 2×, including the section anchor `id="dalvik-signature" data-text="dalvik.annotation.Signature" tabindex="-1">dalvik.annotation.Signature` — the named section id/string is present in the fetched page.
3. **Footer "Last updated 2026-10-09 UTC" — VERIFIED.** `Last updated 2026-10-09 UTC.` occurs verbatim (once as rendered text, once embedded in page data); `2026-10-09` occurs 2×.

All staged anchors confirmed reachable and verbatim-present as of the fetch timestamp; the staged freshness note ("re-open and re-read the Last updated date") is satisfied in kind — the page still stamps `2026-10-09 UTC`, unchanged since the row was mined on 2026-10-23.

# Bounds compliance / tools
- `/home/vgpnk/Projects/shokuknow` touched read-only (grep/read only; no writes, no campaign tools).
- Writes confined to `.ufo/waves/round-67/quarantine/S054/source.bin` and this report.
- No tools installed or updated (stock `curl` 8.x, `sha256sum`, `grep` sufficed); pacman guard honored — no pacman transaction attempted.
- No git/jj mutations, no peer messaging, no subagents.

# Out of scope / limits
- No quote was checked (by design — PROSE-CLASS row; the verdict above asserts reachability + anchor presence only, not content correctness).
- Lane-registry S045 (same URL, lane-side row for the C1 v2 candidate) is a sibling seat's surface; not re-verified here.
- Snapshot-vs-live comparison with `.ufo/waves/round-67/source-snapshots/dex-format.html` not performed (not asked for; the snapshot is the C1-provenance artifact, separate from this quarantine check).
