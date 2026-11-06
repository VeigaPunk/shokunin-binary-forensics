# ScoutSourcesR100 — findings (2026-11-05)

Seat: sources scout for claims.md §C2 (`reports/round-100/cap_apk_probe.py`, androguard 4.1.4 `androguard axml` + apktool 3.0.3 `apktool d -s`).
Receipts: `.ufo/waves/round-100/w1/ScoutSourcesR100/` (bodies + `fetch-receipts.md`).

## 1. Opened official sources

### androguard — `androguard axml` CLI (probe leg 1)

- URL: https://androguard.readthedocs.io/en/latest/tools/androaxml.html — accessed 2026-11-05 — HTTP 200 — 8751 bytes — sha256 `6507e7607f8c6d9b149d6a2f76079508b44e1a701510a49939008d855cbc2efc` — snapshot `.ufo/waves/round-100/w1/ScoutSourcesR100/ag-rtd-androaxml.html`.
- Located quote (11 words), body paragraph directly under the page heading `androguard axml - AndroidManifest.xml parser`, snapshot **line 203**:
  > Parse the AndroidManifest.xml from an APK and show/save the XML file.
- Same page's usage block (snapshot lines 204-216) states the option the probe relies on: `-o, --output TEXT  filename to save the decoded AndroidManifest.xml to, default stdout`.
- Version pin: RTD footer stamps the docs build **Revision `eef97351`**; the pinned RST source https://raw.githubusercontent.com/androguard/androguard/eef97351/docs/tools/androaxml.rst (HTTP 200, 205 bytes, sha256 `a091672b7cb4de483657affb7add0290845bd884cefd4308832d2a3e5717c707`, snapshot `ag-androaxml-rst-eef97351.rst`) carries the identical sentence at its **line 5**. No docs tree exists at tag `v4.1.4` (four `docs/**/androaxml.rst` paths probed under the tag all 404), so `eef97351` is the tightest pin that exists; the RTD build is `latest`.
- Supporting tag-pinned receipt: https://raw.githubusercontent.com/androguard/androguard/v4.1.4/README.md (HTTP 200, 4329 bytes, sha256 `3e04d4aa3227689b9b559f67a4cd76421311051c0dcc88866cd40ab932dc3351`), Features list bullet **"Android's binary xml"** (snapshot line 24) — scope support that the installed series handles Android binary XML. Note: the tag README also warns "Documentation contains outdated information - In progress of updating" and names the Github Pages docs as most current.
- Caveat recorded, not hidden: the RTD `latest` build need not byte-match the installed 4.1.4 CLI; the pinned `eef97351` RST sentence is the anchor of record.

### apktool — `apktool d` decode of resources/manifest (probe leg 2)

- URL: https://apktool.org/wiki/the-basics/intro — accessed 2026-11-05 — HTTP 200 — 23480 bytes — sha256 `7e1c418b4572e4bc7738799677a52c848919ba4592c24046a79cce764727cf4f` — snapshot `apktool-wiki-intro.html`. (https://apktool.org/documentation is a 331-byte meta-refresh stub redirecting to this wiki page — snapshot `apktool-org-documentation.html`.)
- Located quote (5 words), the `$ apktool d testapp.apk` console-output block after "That is where Apktool comes into play", snapshot **line 9**:
  > I: Decoding AndroidManifest.xml with resources
- Corroborating prose on the same page (snapshot lines 7, 10): "If you tried to view `AndroidManifest.xml`. You'd be left viewing a malformed file." → "Viewing `AndroidManifest.xml` again results in something much more human readable" followed by the decoded `<?xml version="1.0" encoding="utf-8" …` block. This is exactly the probe's premise: binary AXML in, XML out.
- Version-pin receipt for the installed version: https://github.com/iBotPeaches/Apktool/releases/tag/v3.0.3 — accessed 2026-11-05 — HTTP 200 — 178774 bytes — sha256 `3356d86d4f9b37ceb9384eefa03466215fbc6c54e5d36b39979a0abe1a508c77` — snapshot `apktool-release-v303.html`. Confirms: title "Release v3.0.3 · iBotPeaches/Apktool", tag `v3.0.3` (line 422/431), release datetime `2026-07-20T10:37:54Z` (line 582), release blog https://apktool.org/blog/apktool-3.0.3.
- Wiki source mdx (byte-pinned copy of the quote's source): https://raw.githubusercontent.com/iBotPeaches/apktool.org/main/wiki/the-basics/intro.mdx — HTTP 200 — 1626 bytes — sha256 `f640bbffc53506ffcb4cad53e2f131b7acc5c8a0fc1b34411bbf409a43e6cad8` — snapshot `apktool-wiki-intro.mdx`; quote sits at **line 20** there. `main` is a moving branch; the hash pins the accessed bytes, not a version. The mdx console sample still shows an Apktool 2.0.0-era banner ("I: Using Apktool 2.0.0 on testapp.apk") — the decode claim is the project's own doc, not a 3.0.3-specific statement.
- Gap, stated plainly: a dedicated flag page documenting `apktool d -s` (`--no-src`) was not located — three probed URLs (`/wiki/the-basics/cli`, `/docs/cli`, `/docs/the-command-line-interface`) all 404. No `-s` quote is claimed. The probe's `-s` behavior needs its own observed receipt (ExecApkProbe's run), not a doc quote.

## 2. Local decoder confirmation (no installs performed; nothing installed this round)

```
$ androguard --version   → "androguard, version 4.1.4"   (rc 0)
$ apktool --version      → "3.0.3"                        (rc 0)
$ which -a androguard apktool
  /home/vgpnk/.local/bin/androguard
  /home/vgpnk/.local/bin/apktool
  /usr/bin/apktool
```

- androguard channel: **uv tool**. `uv tool list` → `androguard v4.1.4`; `/home/vgpnk/.local/bin/androguard` is a symlink to `/home/vgpnk/.local/share/uv/tools/androguard/bin/androguard` (uv-managed entry point calling `androguard.cli.cli:entry_point`).
- apktool channel: **official release jar** (not uv, not the distro package). `/home/vgpnk/.local/bin/apktool` is a 75-byte POSIX sh wrapper:
  `exec java -jar "$HOME/.local/opt/apktool/apktool_3.0.3.jar" "$@"`
  PATH resolves `~/.local/bin/apktool` before `/usr/bin/apktool`, so the jar at `~/.local/opt/apktool/apktool_3.0.3.jar` is what runs — matching the C2 frozen version 3.0.3.
- Implication for the probe contract: decoder paths resolve via PATH, so a PATH-shim test can shadow either; the `--androguard`/`--apktool` overrides bypass the wrapper itself.

## 3. Existing SOURCES.md rows (census E04 duplicate-URL guard)

Registry: **507 rows, max id S507** (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 507; max-id awk → S507). ScribeLessonR100 must re-derive the next unused id at write time.

- **S059** — `Apktool — https://github.com/iBotPeaches/Apktool` | tool | A | mined | 2026-10-27 | README commit `0312d212c713c9ebc568b7d9295eec0f47858bfa`; quote "It can decode resources to nearly original form and rebuild them after making some modifications". This is the repo row; my two proposed URLs are distinct from it.
- **No androguard row exists** (`grep (?i)androguard|apktool|ibotpeaches` over SOURCES.md → S059 only).
- Duplicate-URL check for the new rows: `grep apktool\.org|readthedocs\.io|androguard` over SOURCES.md returns only unrelated rows (construct/devicetree readthedocs); neither `https://androguard.readthedocs.io/en/latest/tools/androaxml.html` nor `https://apktool.org/wiki/the-basics/intro` is registered. I could not locate an "E04" error-id definition in the lane tree (`scripts/sources-census.sh` absent at 05e854c); the substantive check (URL absence) is done above by command.

## 4. Proposed rows for ScribeLessonR100

Census facts that bind the cells (fleet `/home/vgpnk/CORPUS.md` §SOURCES.md, frozen contract v1):
- **used-by**: contract wording is "repo-relative paths of the knowledge entries or lessons citing the row, comma-separated, or `—`"; the frozen census machine-check verifies existence only for `mined` rows ("mined rows whose used-by paths do not exist — must print nothing"). So: **`SCORECARD.md` is not a census-accepted used-by value** (it is neither a knowledge entry nor a lesson); **`reports/round-100/cap_apk_probe.py` is accepted** as a repo-relative path provided the file exists on the tree when the census runs. If rows are written before the probe lands, use `status=queued`, `used-by=—` and flip to `mined` + path later (flips of status/used-by are the in-place-mutable cells).
- Tier: official project docs = A "for that scope" (matches S058/S059 style); Q02 requires the anchor to be a located section, not a bare homepage — both rows use located lines.
- recheck: `on-release` fits (a decoder release re-opens scope), consistent with S059.

Proposed **S508** (androguard):
- source: `androguard axml — AndroidManifest.xml parser — https://androguard.readthedocs.io/en/latest/tools/androaxml.html`
- kind: `docs` · tier: `A`
- scope: the `androguard axml` CLI's own stated function at docs build `eef97351` (parse AndroidManifest.xml from an APK, print/save decoded XML, `-o`/`-r` options); not output fidelity, resource-table completeness, or AXML spec conformance
- anchor: snapshot `.ufo/waves/round-100/w1/ScoutSourcesR100/ag-rtd-androaxml.html` sha256 `6507e760…` line 203; pinned RST `…/androguard/eef97351/docs/tools/androaxml.rst` sha256 `a091672b…` line 5; accessed 2026-11-05
- teaches: supports `reports/round-100/cap_apk_probe.py`'s androguard leg: "Parse the AndroidManifest.xml from an APK and show/save the XML file." (11 words)
- status `mined` · opened `2026-11-05` · recheck `on-release` · used-by `reports/round-100/cap_apk_probe.py`

Proposed **S509** (apktool):
- source: `Apktool wiki, The Basics: Introduction — https://apktool.org/wiki/the-basics/intro`
- kind: `docs` · tier: `A`
- scope: the official wiki's `apktool d` decode demonstration (unzipped AndroidManifest.xml is malformed; after `apktool d` it is human-readable XML); not output fidelity to pre-compile form, not rebuild validity
- anchor: snapshot `.ufo/waves/round-100/w1/ScoutSourcesR100/apktool-wiki-intro.html` sha256 `7e1c418b…` line 9; source mdx `wiki/the-basics/intro.mdx` @ main sha256 `f640bbff…` line 20; release-pin receipt `.ufo/waves/round-100/w1/ScoutSourcesR100/apktool-release-v303.html` (tag v3.0.3, 2026-07-20); accessed 2026-11-05
- teaches: supports `reports/round-100/cap_apk_probe.py`'s apktool leg: "I: Decoding AndroidManifest.xml with resources" (5 words)
- status `mined` · opened `2026-11-05` · recheck `on-release` · used-by `reports/round-100/cap_apk_probe.py`
- distinct from S059 (repo URL) — no E04 collision; if the L1 prefers one Apktool row, S509 supersedes nothing and complements S059's repo-scope.

## 5. Open questions

1. `E04` error-id definition not found in the lane tree at 05e854c — flagged; the URL-uniqueness check it names was performed manually (§3).
2. No version-pinned androguard docs exist at tag v4.1.4; `eef97351` (the RTD build revision) is the tightest pin. If CriticR100 wants tag-exact docs, the tag README's Features bullet is the only tag-pinned sentence.
3. `apktool d -s` flag documentation: not located on apktool.org (3 probed URLs 404). Recommend ExecApkProbe/ReviewerCapR100 treat `-s` behavior as observation-only, never doc-quoted.

No installs or upgrades performed (operator tooling directive: nothing needed; decoders already present via uv tool and official jar).
Scratch `/fast/scratch/hyaku/revenger-r100/ScoutSourcesR100/` deleted before yield; all receipts live in the wave dir.
