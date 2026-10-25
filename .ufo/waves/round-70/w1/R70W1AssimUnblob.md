DRAFT-READY — upstream re-grounding of the three Unblob claims (C3/C4/C5) holds verbatim on 3 of 3 quoted sentences, but two of the three sentences OVERREACH their source ("authoritative"), the C4 quote is a rendered-text paraphrase (not source bytes), and the round-70 quarantine of S054/S099 as "could not be fetched" is FALSE as of 2026-10-25 (both fetched today, digests below) — the package is admissible only after those three repairs.

Seat: `R70W1AssimUnblob` (round 70, hyaku run 7, wave 1 — advisory pre-gate). Lane repo: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Target package entry (READ-ONLY campaign tree):
`/home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/digest-scope-versus-provenance-amendment-2026-10-23.md`
(claims 3–5 = lines 36–54). Rows: `S099` (unblob README) at `/home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md:59`, `S096` (SWGDE 12-F-003-2.0) at `:56`.

## 0. Fetch provenance (all re-fetched by me today, 2026-10-25)

| artifact | URL | result | bytes | sha256 |
|---|---|---|---|---|
| unblob README | `https://raw.githubusercontent.com/onekey-sec/unblob/main/README.md` | HTTP 200, 2026-10-25T21:07:15Z | 7580 (235 lines) | `6544d60f22f7b521f8705b3bba5d47a50e428ccbd3359542708dbd009ccf3716` |
| unblob formats list | `https://unblob.org/formats/` | HTTP 200 | 216890 | — |
| unblob releases API | `https://api.github.com/repos/onekey-sec/unblob/releases?per_page=10` | HTTP 200 | — | latest `26.6.4`, `published_at 2026-06-04T08:52:43Z` (matches S054 row) |
| OWASP FSTM ja | `https://raw.githubusercontent.com/coky-t/owasp-fstm-ja/master/Document/README.md` | HTTP 200 | — | `f9d28d0cf542ea8c436116bc2147374d6a3e3b4ccc2289f4328aa8e4d6fde87d` |
| SWGDE 12-F-003-2.0 | `.../2025-07-12-Core-Competencies-for-Mobile-Device-Forensics-12-F-003-2.0.pdf` | HTTP 200 | 290583 | `593956e1e28b30e00ab3a2195a1baa9494f072043c1ba8e095b6df24053250c1` |
| SWGDE 18-F-002-2.0 | `.../2025-11-20-...-18-F-002-2.0.pdf` | HTTP 200 | 292883 | `6a7217f1e359af6d8f8c3e9bf7062902f8a922c2e9429a1b2ffa43e8af62fd2f` |
| SWGDE 18-F-003-2.0 | `.../2025-08-21-...-18-F-003-2.0.pdf` | HTTP 200 | 767292 | `55446a4eddd1eb788897074c49725db90c3cc84b44a2b7d6f8626de67f56f410` |

No package installed (curl + pdftotext + Python stdlib only) — host pacman transactions remain paused.

## 1. Claim-by-claim verdicts (claims 3–5)

### C3 — "78+ supported formats" — **PRESENT (byte-exact), but the sentence OVERREACHES**

Upstream README `:22`, under heading `## Features`:
`- **78+ supported formats** — archives, compression streams, and file systems including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, 7-Zip, gzip, XZ, LZMA, LZ4, and many more. See the [full list](https://unblob.org/formats/).`

Byte check of the entry's quoted span against the fetched file:
```
python3 - <<'EOF'
up=open('/tmp/revenger-r70-assimunblob-readme.md',encoding='utf-8').read()
q="**78+ supported formats** — archives, compression streams, and file systems including SquashFS, JFFS2, UBI/UBIFS, ext, CPIO, ZIP, 7-Zip, gzip, XZ, LZMA, LZ4, and many more."
print(q in up)
EOF
True
```
The quote ends at a sentence boundary; the trailing `See the [full list](https://unblob.org/formats/).` is upstream's own continuation, not part of the quote. Also upstream's lede `:5` says "unblob parses unknown binary blobs for **78+ archive, compression, and file-system formats**".

**Overreach #1 (located):** the entry (`:36`) says upstream "now supplies the **authoritative** figures", and S099's row (`SOURCES.append.md:59`) says "the **authoritative** figures for Unblob 26.6.x". Upstream's README is the project's *self-description*, not an independent authority, and the "78+" is a floor: upstream's own full list at `unblob.org/formats/` enumerates **97 format names** today (99 headings = 1 `h1` "Supported Formats" + 97 `h2` + 1 `h4` "Cookie consent"; `grep -c` of `h2` = 97). Command:
```
python3 - <<'EOF'
import re
s=open('/tmp/revenger-r70-assimunblob-formats.html',encoding='utf-8',errors='replace').read()
hs=re.findall(r'<h([1-6])[^>]*>(.*?)</h\1>',s,re.S)
from collections import Counter; print(Counter(l for l,_ in hs))
EOF
Counter({'2': 97, '1': 1, '4': 1})
```
**Overreach #2 (located):** "now" is unsupported. The README on `main` was last modified **2026-03-04** (`3b470cd1c33e10a3ae977a6caaab5dbcbf2d5ce8` "feat(docs): improve README file"), i.e. it is the *same bytes* for releases 26.3.24 / 26.3.30 / 26.6.4 (2026-03-25 → 2026-06-04). So S099's own recheck warning ("the format count and dependency list change between releases", `SOURCES.append.md:59`) is not evidenced by any observed change, and the entry's temporal "now" framing is unsupported. S099 also points at an unpinned moving branch while asserting the figures are "for Unblob 26.6.x" — the README carries no version marker (the only version string in the file is the PyPI badge at `:8`).

**Verdict C3:** quote PRESENT; claim sentence **OVERREACH** ("authoritative", "now", "26.6.x" on an unpinned branch). Recommend **ADMIT only after rewording** to: "upstream's own README states '78+ supported formats'; the project's published format list enumerated 97 names on 2026-10-25; the README on `main` has not changed since 2026-03-04 and is not digest-pinned".

### C4 — Python/uv/Rust requirement line — **PARAPHRASE (rendered text), substance CONFIRMED**

Upstream README `:100`, under heading `### From source` (a subsection of `## Installation`):
`Requires Python ≥ 3.10, [uv](https://docs.astral.sh/uv/), and a Rust toolchain (for the compiled extensions).`

The entry (`:43`) quotes it as "Requires Python ≥ 3.10, uv, and a Rust toolchain (for the compiled extensions)" — the markdown link is flattened, so the quoted string is **not** in the source bytes:
```
q4="Requires Python ≥ 3.10, uv, and a Rust toolchain (for the compiled extensions)"
print(q4 in up)   # -> False
print("Requires Python ≥ 3.10, [uv](https://docs.astral.sh/uv/), and a Rust toolchain (for the compiled extensions)" in up)  # -> True
```
Substance is independently confirmed today, without the README:
- `pyproject.toml` on `main`: `requires-python = ">=3.10"` (`:37`), `version = "26.6.4"` (`:38`), `[tool.maturin]` `manifest-path = "rust/Cargo.toml"` (`:209`), `module-name = "unblob._rust"` (`:210`), `build-backend = "maturin"` (`:223`).
- installed launcher on this host: `head -1 /home/vgpnk/.local/share/uv/tools/unblob/bin/unblob` → `#!/home/vgpnk/.local/share/uv/tools/unblob/bin/python`; `unblob --version` → `26.6.4`.
- PyPI metadata today: `latest 26.6.4`, `requires_python >=3.10`.

**Overreach (located):** the entry's headline (`:42`) says "Unblob's implementation language is now settled" and attributes it to this sentence. The sentence is a *build-from-source requirement*; it implies rather than states the language. Upstream never writes "Unblob is a Python program". The heading it sits under (`### From source`) is also not named in the entry (S099 row claims the quote lives in "Features" and "Installation" — `From source` is an Installation subsection, so the row's anchor is loose but not wrong).

**Verdict C4:** quote PARAPHRASE (rendered link-flattened); underlying fact CONFIRMED by `pyproject.toml` + launcher shebang. Recommend **ADMIT** with the quote re-rendered from source bytes and the language statement sourced from `pyproject.toml` (tier-A) rather than from a requirements sentence.

### C5 — install dependency line + `unblob --show-external-dependencies` — **PRESENT (byte-exact) for the apt line and for the command; but "the authoritative dependency set" OVERREACHES**

Upstream README `:46`, under `### pip (recommended for most users)` (text above it: "Then install the required external extractor tools. On Ubuntu/Debian:"):
`sudo apt install android-sdk-libsparse-utils e2fsprogs p7zip-full unar zlib1g-dev liblzo2-dev lzop lziprecover libhyperscan-dev zstd lz4`
→ byte check `True`.

`unblob --show-external-dependencies` occurs at upstream `:59` (pip section), `:97` (from-source section) and `:161` (Full CLI reference: `--show-external-dependencies    List required external tools and their status.`).

**Overreach (located):** the entry (`:48`) says "Unblob's external-extractor dependency set is the authoritative one", and quotes only the apt line. That apt line is **one platform's, one-install-path's** list; upstream documents four other paths (Docker "bundles all extractors", Kali `sudo apt install unblob`, Nix, from source) plus a separate SquashFS extra (sasquatch, upstream `:49-52`). The set upstream itself calls authoritative is the tool's own report. I ran it today (this also closes the entry's own remaining probe):
```
/home/vgpnk/.local/share/uv/tools/unblob/bin/unblob --show-external-dependencies ; echo EXIT=$?
```
→ `EXIT=0`, 15 tools: `7z ✓  debugfs ✓  fsck.erofs ✗  jefferson ✗  lz4 ✓  lziprecover ✗  lzop ✗  partclone.restore ✗  sasquatch ✗  sasquatch-v4be ✗  simg2img ✓  ubireader_extract_files ✗  ubireader_extract_images ✗  unar ✗  zstd ✓`

The report and the apt line disagree in both directions: the report includes `jefferson`, `partclone.restore`, `ubireader_extract_files/images`, `fsck.erofs`, `sasquatch(-v4be)` which the apt line does not install, while the apt line's `unar` is **missing on this host** and `lzop`/`lziprecover` are missing too. So the host is not at upstream's stated apt set, and the apt set is not the dependency set.

**Verdict C5:** apt line PRESENT; command PRESENT; "authoritative dependency set" **OVERREACH**. Recommend **ADMIT** only as: "upstream's Ubuntu/Debian apt line is one install path; the tool's own `--show-external-dependencies` is the authoritative list — on this host (2026-10-25) 5 of 15 are present, `unar` (in the apt line) absent".

### Cross-claim: the entry's own "Observed host state" (`:56-58`) is now stale
The entry says `unblob --show-external-dependencies` "was not run in this round and is recorded as a remaining probe". I ran it (above): it succeeds, exit 0, and shows the host does **not** satisfy upstream's apt line (`unar`, `lzop`, `lziprecover` absent). Also `/usr/bin/7z` on this host is a 37-byte wrapper (`#!/bin/sh` / `exec /usr/lib/7zip/7z "$@"`) rather than the binary, though `7z` reports "7-Zip 26.04 (x64)" — the entry's "present at `/usr/bin/7z` (7-Zip 26.04)" is version-correct but path-imprecise.

## 2. Scope judgment against PROVINCE.md (read 2026-10-25)

PROVINCE.md: the lane "Owns: reverse engineering of shipped artifacts — native binaries, managed assemblies, Electron/JavaScript packages, Android APKs, archives, **firmware**, browser/Electron runtime evidence — using the REA skill and its toolset"; host engines include "Binwalk/Unblob"; it "Refuses: harness/evidence auditing…". The lane's own `corpus/README.md:85` already marks "Evidence custody beyond fixity: collection and transfer records (SWGDE collection/acquisition guidance) — **adjacent to this province**; enter only as it bears on shipped-artifact evidence ledgers."

| claim | subject | scope verdict | rationale |
|---|---|---|---|
| C1 (`:14-27`) | SWGDE 12-F-003-2.0 mobile-device-forensics competency framework, §5.1–§5.8 | **ADJACENT / GENERIC** | Verified verbatim today (`12f003.txt:74-81` headings 5.1 Legal Considerations and Ethical Standards → 5.8 Presentation and Testimony; `Version: 2.0 (7/12/2025)` at `:90`; cover rule "Any reference or quote from a SWGDE document must include the version number (or creation date)…" present at p.1). But a mobile-forensics *competency* framework is generic to the lane's firmware/APK reverse-engineering province and names no lane artifact. |
| C2 (`:29-35`) | SWGDE 18-F-002 "should" vs 18-F-003 "shall" custody wording, used to anchor the C13 digest-scope distinction | **ADJACENT** (usable only as it bears on the C13 entry) | Both quotes verified today: 18-F-002 "The chain of custody documentation should be contemporaneous to the collection…" (`18f002.txt:322`) vs 18-F-003 "The chain of custody documentation shall be contemporaneous and include a description of item(s)…" (`18f003.txt:259`). It supports the existing C13 row (`corpus/README.md` C13 = fixity and provenance) but adds no new lane ground; `corpus/README.md:85` treats SWGDE custody as adjacent. |
| C3 | unblob supported-format count | **IN-SCOPE, narrowly** — as firmware-route tooling metadata bearing on whether a shipped firmware artifact can be extracted (C07 / host-readiness C14) | Not as "an authoritative figure" (see §1). The lane's C07 row is already held by `knowledge/round-64-firmware-region-byte-evidence.md`; C14 (`knowledge/2026-10-12-rea-readiness-checklist.md`) is `partial`. |
| C4 | unblob implementation language | **IN-SCOPE, narrowly** (same C07/C14 host-route frame) | Confirmed by `pyproject.toml` + installed shebang. |
| C5 | unblob external-extractor dependency set | **IN-SCOPE** (host prerequisite contract for the firmware extraction route) | Highest-value claim of the three: it is directly the "which binaries must be on PATH for `unblob`" ground the lane's C14/C07 rows lack, and it is checkable on this host. |

## 3. Additional located defects in the package (advisory, wave-1)

1. **The round-70 quarantine of S054/S099 as unfetchable is factually wrong (both fetched today).**
   `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-70/assimilation/quarantine-slice` ends with:
   ```
   S054`   the cited source could not be fetched, so no quote was checked 
   S099`   the cited source could not be fetched, so no quote was checked
   ```
   (staged ids S047–S201; `staged-ids` file, and merge-tree `SOURCES.append.md` S054 = Unblob release API, S099 = unblob README — same numbering, per `lanes/revenger/ID-REMAP.md`.) Today both URLs return HTTP 200 (digests in §0; releases API confirms `26.6.4` / `published_at 2026-06-04T08:52:43Z`, exactly the S054 row) and the three quotes in claims 3–5 verify against the fetched bytes. **Repair for the L1:** reclassify S054/S099 as fetched-and-verified (with the digests pinned), not quarantined; otherwise C3–C5 admit nothing and the entry's dependency on S099 is silently dropped.
2. **Dangling `REJECTIONS.md` pointer inside the merge package.** `knowledge/corpus/knowledge/firmware-extraction-toolchain-ja.md:32` records the FSTM Unblob error as "a rejection (`REJECTIONS.md` R-05)"; `find /home/vgpnk/Projects/shokuknow/merge -name REJECTIONS.md` → **no such file anywhere in the merge tree**. The pointer resolves only in the campaign lane (`/home/vgpnk/Projects/shokuknow/lanes/revenger/REJECTIONS.md:43-45`), and even there the id is ambiguous: `lanes/revenger/round2/REJECTIONS.md:41-43` has a *different* R-05 ("REA's own `docs/` directory…"). The amendment's claim-4 phrase "the round-2 rejection" therefore resolves, under per-round numbering, to the wrong rejection. Repoint to a file+id that exists in the shipped package (or carry the quote inline).
3. **The "supersedes the 300+ figure" claim does not satisfy R-11's own flip condition.** R-11 (`lanes/revenger/REJECTIONS.md:97-99`) rejected the community "300+ formats" figure with the flip *"a source that ties the specific figure to a specific pinned build with a digest"*. The entry's support for the supersession is S099 = the README on branch `main` — **unpinned, undigested, version-free** (the only version string in the file is the PyPI badge at `:8`). The claim-3 sentence therefore asserts a supersession that its own cited source cannot deliver under the rejection's stated condition; the claim needs a digest-pinned README (tag `26.6.4`) or must be reworded as "a different, first-party figure exists", not "supersedes". (Independently: the README's `78+` has not changed since commit `3b470cd1`, 2026-03-04 — `git`-free check: `https://api.github.com/repos/onekey-sec/unblob/commits?path=README.md&per_page=3` → newest `3b470cd1c33e10a3ae977a6caaab5dbcbf2d5ce8` 2026-03-04, "feat(docs): improve README file" — i.e. the same bytes across releases 26.3.24 / 26.3.30 / 26.6.4.)
4. **"the round-2 rejection" is mis-attributed.** Claim 4 (`:42`) says the FSTM/Unblob-Rust rejection is "the round-2 rejection". The located rejection is **R-05 in `lanes/revenger/REJECTIONS.md:43-45`** — the root `corpus-expansion-1` (round 1) file, the same file that holds R-11. `lanes/revenger/round2/REJECTIONS.md:41-43` R-05 is a different subject entirely ("REA's own `docs/` directory as a source of the browser-route document set"); no round-2 file mentions the FSTM Unblob line. The same round-1 R-05 is what `firmware-extraction-toolchain-ja.md:32` cites. Repoint the citation to `REJECTIONS.md` R-05 (round 1), or quote the rejection inline.
5. **The FSTM is mischaracterized as saying Unblob "is a Rust implementation".** Fetched FSTM `:1062`: `- [Unblob](https://github.com/onekey-sec/unblob) - Rust による高速化パフォーマンスを備えた 30 以上のフォーマットをサポートする最新の抽出スイートです` — i.e. "the latest extraction suite supporting 30+ formats, with **Rust-accelerated performance**". It does not say "a Rust implementation". The same mischaracterization is asserted in `firmware-extraction-toolchain-ja.md:29` ("the document's Unblob entry describes Unblob as a Rust implementation — which is false") and repeated in the amendment's claim 4 (`:44-47`, "the Japanese FSTM's description of Unblob as a Rust implementation is a garbled version of a true fact"). The Japanese wording is actually *compatible* with upstream's "Rust toolchain (for the compiled extensions)", so the "garbled version of a true fact" reasoning and the R-05 rejection premise both rest on a quote the source does not contain. Recommend the entry quote the Japanese line itself and state the correction at that granularity.
6. **`coverage-map: SWGDE, C07` names a row that does not exist in the lane's map.** `grep -cE '^\| C[0-9]+ ' corpus/README.md` → 14 (C01–C14); the only `SWGDE` occurrence in that file is the frontier bullet at `:85`. Lane QUALITY Q02 requires naming the coverage-map row the entry fills — for a lane-adopted copy this must be `C13` (fixity/provenance, the entry it amends) and/or `C07`/`C14`; "SWGDE" must be dropped or defined.
7. **The entry's `recheck:` field mixes two horizons** (`:7`: "365d — re-fetch the SWGDE document …; re-read the unblob README on `main` at 90d") whereas the two rows carry 365d (S096) and 90d (S099) separately. Minor, but the lane's Q02 wants one recheck per source horizon.
8. **The base entry the amendment amends exists in the lane but not in the merge package.** `corpus/knowledge/digest-scope-versus-provenance.md` is present in the lane (source lines S005/S006/S014/S015, `coverage-map: C13`) and absent from `/home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/` (87 files there; no `digest-scope-versus-provenance.md`). A package-only adoption would carry an unresolvable "ground" pointer; adoption must be made against the lane copy.

## 4. Recommended admit / reject (per claim) and overall

| claim | recommendation |
|---|---|
| C3 (format count) | **REJECT as written / ADMIT after rewrite.** Drop "authoritative" and "now"; state the upstream self-description, the 97-name list observed today, and the 2026-03-04 README commit; pin the README digest; name it as a C07/C14 tooling row. |
| C4 (language) | **ADMIT after repair.** Quote the requirement line with the link markup or cite `pyproject.toml` (`[tool.maturin]`, `module-name = "unblob._rust"`) for the language statement; name the `### From source` heading. |
| C5 (dependency set) | **ADMIT after repair.** Replace "the authoritative one" with the observable: upstream's Ubuntu/Debian apt line (one path) versus `unblob --show-external-dependencies` (the tool's own 15-tool list), with today's host result (5 present, `unar`/`lzop`/`lziprecover` absent). This is the most useful claim for C14/C07. |
| C1/C2 (SWGDE half) | **DO NOT ADMIT into this lane's ground as new coverage** — ADJACENT (`corpus/README.md:85`); at most cross-reference the already-held C13 entry. The SWGDE quotes themselves are verified and sound. |

**Overall package recommendation:** *conditional admit after three repairs* — (a) un-quarantine S054/S099 (both fetch; digests pinned), (b) rewrite C3 and C5 to drop "authoritative", (c) re-render the C4 quote from source bytes and source the language claim from `pyproject.toml`. With (a)–(c) the Unblob half (C3/C4/C5) is a sound, tier-A, checkable C07/C14 tooling row; without them it must not land, because the two "authoritative" sentences are the only load-bearing claims and both overreach a project's self-description.

## 5. What I did not do
- Did not edit any file (package, lane, campaign tree) — read-only verification only.
- Did not run any campaign tool in `/home/vgpnk/Projects/shokuknow`; only `git log`/`git show`/`grep` reads there.
- Did not verify the SWGDE-side wording of `swgde-custody-authority-and-normative-scope.md` beyond the two custody sentences and 12-F-003 §5 headings quoted above (that file is a separate package entry).
- Scratch files live under `/tmp/revenger-r70-assimunblob-*` and were deleted before returning.
