# SOURCES rows S508 / S509 — draft for the L1 to append (round 100)

Append-only: two new rows, inserted after the last registry row (`| S507 |`, `corpus/SOURCES.md:524`).
Column order is the contract-v1 order: `id | source | kind | tier | scope | anchor | teaches | status
| opened | recheck | used-by`. No `|` inside any cell. 11 columns ⇒ NF = 13.

Both sources were opened this round by ScoutSourcesR100; receipts (twelve HTTP-200 bodies with
sha256 digests, plus `fetch-receipts.md`) are in `.ufo/waves/round-100/w1/ScoutSourcesR100/`, and
the scout's findings are `.ufo/waves/round-100/w1/ScoutSourcesR100.md`. Every quote below is
verbatim from a saved receipt body and was re-verified by the scribe with `grep -c -F` (1 occurrence
each).

Draft status `mined` with `used-by corpus/lessons/round-100.md` — the lesson cites both row ids.
If the L1 appends the rows before that lesson file exists on disk, use `status=queued` /
`used-by=—` here and flip them afterwards (the flip is logged old → new in the lesson's
`## Gate`): the census's E11 check reads the used-by path from disk and would print an E-code for a
`mined` row whose path is absent.

---

## S508 — androguard `axml`

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S508 | androguard `axml` — AndroidManifest.xml parser — https://androguard.readthedocs.io/en/latest/tools/androaxml.html | docs | A | the `androguard axml` CLI's own stated function at docs build `eef97351` (parse AndroidManifest.xml from an APK and show/save the decoded XML); not output fidelity, resource-table completeness or AXML spec conformance | docs page heading `androguard axml - AndroidManifest.xml parser`, paragraph "Parse the AndroidManifest.xml from an APK and show/save the XML file." at body line 203 (8751 bytes, sha256 `6507e7607f8c6d9b149d6a2f76079508b44e1a701510a49939008d855cbc2efc`); pinned RST `docs/tools/androaxml.rst` at commit `eef97351` line 4 (205 bytes, sha256 `a091672b7cb4de483657affb7add0290845bd884cefd4308832d2a3e5717c707`); accessed 2026-11-05 | The `androguard axml` tool's own documentation states it parses an APK's AndroidManifest.xml and shows or saves the decoded XML, which is the behaviour the round-100 capability probe compares against `truth.json`. | mined | 2026-11-05 | on-release | corpus/lessons/round-100.md |

- **Located quote** (11 words, ≤ 25), verbatim: *"Parse the AndroidManifest.xml from an APK and
  show/save the XML file."* — body line 203 of
  `.ufo/waves/round-100/w1/ScoutSourcesR100/ag-rtd-androaxml.html`; the same sentence at line 4 of
  `.ufo/waves/round-100/w1/ScoutSourcesR100/ag-androaxml-rst-eef97351.rst` (the pinned RST at
  commit `eef97351`). `grep -c -F` on each body → 1.
- **Access date** 2026-11-05; URL as above; HTTP 200; bytes and sha256 as above.
- **Version pin / caveat (stated, not hidden):** the RTD build stamps revision `eef97351` and the
  build is `latest`; no `docs/**/androaxml.rst` path exists at tag `v4.1.4` (four probed URLs 404),
  so `eef97351` is the tightest pin that exists. The `latest` docs need not byte-match the
  installed 4.1.4 CLI; the pinned RST sentence is the anchor of record.
- **Distinctness:** no androguard row and no `androguard.readthedocs.io` URL exists in the
  registry before this round (`grep -c -i androguard corpus/SOURCES.md` → 0).

## S509 — Apktool wiki `apktool d`

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S509 | Apktool wiki, The Basics: Introduction — https://apktool.org/wiki/the-basics/intro | docs | A | the official wiki's `apktool d` decode demonstration (a compiled AndroidManifest.xml is malformed when merely inflated; after `apktool d` it is human-readable XML); not output fidelity to pre-compile form, not rebuild validity | wiki console block after "That is where Apktool comes into play", line "I: Decoding AndroidManifest.xml with resources" at body line 9 (23480 bytes, sha256 `7e1c418b4572e4bc7738799677a52c848919ba4592c24046a79cce764727cf4f`); source mdx `wiki/the-basics/intro.mdx` @ `main` line 28 (1626 bytes, sha256 `f640bbffc53506ffcb4cad53e2f131b7acc5c8a0fc1b34411bbf409a43e6cad8`); installed version pinned by the v3.0.3 release page (tag `v3.0.3`, released 2026-07-20); accessed 2026-11-05 | The project's own wiki shows `apktool d` decoding a compiled AndroidManifest.xml into readable XML, which is the second decoder the round-100 capability probe compares against `truth.json`. | mined | 2026-11-05 | on-release | corpus/lessons/round-100.md |

- **Located quote** (5 words, ≤ 25), verbatim: *"I: Decoding AndroidManifest.xml with resources"* —
  body line 9 of `.ufo/waves/round-100/w1/ScoutSourcesR100/apktool-wiki-intro.html`; the same line
  at line 28 of `.ufo/waves/round-100/w1/ScoutSourcesR100/apktool-wiki-intro.mdx`. `grep -c -F` on
  each body → 1.
- **Access date** 2026-11-05; URL as above; HTTP 200; bytes and sha256 as above.
  `https://apktool.org/documentation` is a 331-byte meta-refresh stub that redirects to this wiki
  page (snapshot `apktool-org-documentation.html`); the release pin is
  `https://github.com/iBotPeaches/Apktool/releases/tag/v3.0.3` (HTTP 200, 178774 bytes, sha256
  `3356d86d4f9b37ceb9384eefa03466215fbc6c54e5d36b39979a0abe1a508c77`).
- **Gap stated plainly:** no page documenting `apktool d -s` (`--no-src`) was located (three probed
  URLs 404), so no `-s` quote is claimed; the `-s` behaviour is observation-only, from the probe's
  own run.
- **Distinctness:** S509 is distinct from S059 (the Apktool *repository* row, README commit
  `0312d21`, opened 2026-10-27) — different URL, different scope, no supersession. No `apktool.org`
  URL exists in the registry before this round (`grep -c 'apktool\.org' corpus/SOURCES.md` → 0).

---

## Row-by-row derivation (for the L1's audit)

| cell | S508 | S509 | why |
|---|---|---|---|
| `id` | S508 | S509 | next unused ids at `0350014d`: 507 rows, max id S507 |
| `kind` | `docs` | `docs` | both are official project documentation pages; contract enum `spec · docs · paper · code · tool · dataset · talk · book · community · own-work` |
| `tier` | A | A | tier A is scoped to the row's scope: the tool's own documentation is primary for "what the tool says it does" (matches S058/S059 style); neither scope is a general claim about Android/APK correctness |
| `status` | mined | mined | cited by `corpus/lessons/round-100.md` (this round's lesson, which quotes both rows and their receipts) |
| `opened` | 2026-11-05 | 2026-11-05 | the round in which the source was opened |
| `recheck` | on-release | on-release | a decoder release re-opens the scope; same cadence as S059 |
| `used-by` | `corpus/lessons/round-100.md` | `corpus/lessons/round-100.md` | the lesson cites both ids; a `corpus/`-prefixed path that exists after the landing commit |

**Do not add `reports/round-100/cap_apk_probe.py` to `used-by` as it stands.** The frozen v8
counter's `C1_USEDBY_GROUNDED` leg prefixes any non-`corpus/` used-by path with `corpus/` before it
looks for the citing file (`reports/round-99/c1_k_admit_counter8.py:740-742`), so
`reports/round-100/cap_apk_probe.py` would be looked for at `corpus/reports/round-100/cap_apk_probe.py`
and the leg would fail. The probe as it stands cites neither row id
(`grep -c "S508\|S509" reports/round-100/cap_apk_probe.py` → 0), so it is not a citing path yet.
`SCORECARD.md` is likewise not a lesson or knowledge entry and is not a `used-by` value.

## Dry-run over the census (scribe, scratch copy — the lane tree was not modified)

Full receipt: `.ufo/waves/round-100/w1/ScribeLessonR100/census-dryrun.log`. A scratch copy of
`corpus/SOURCES.md` with these two rows appended after `| S507 |`, plus a placeholder
`corpus/lessons/round-100.md` (the used-by path must exist on disk for the census's E11 check on a
`mined` row):

```
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' <scratch>/corpus/SOURCES.md
509
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' …
0                                                              # malformed rows
$ scripts/sources-census.sh validate --root <scratch> <scratch>/revenger-shokunin | grep -E "S508|S509"
(no output)                                                    # findings for the two new rows: 0
```

Expected histograms after the append (re-derivable from the committed registry):
tier `A=460 B=21 C=28`; status `mined=473 queued=16 rejected=20`; rows 509. The lane's real
registry was not touched by this seat (sha256
`af0acc09c56c38b9f00b18286cb9140160b533060e6fc52d2e9d5011e068745b` before and after).
