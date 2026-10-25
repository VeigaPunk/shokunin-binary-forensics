OPENED-QUOTE-PRESENT — the live S043 source re-opened today (2026-10-25) is **byte-identical** to the lane's committed snapshot and the C05 entry's route quote is present at live lines 7-8; the S043 citation itself is sound. Three **advisory** registry-bookkeeping findings follow (none is a defect in the candidate's bytes; wave-1 findings are not kill-rule inputs).

Seat: `R70W1OpenS043` · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin` · wave 1 of 2 (build / pre-gate), round 70 (hyaku run 7) · judged on freshness + coverage · no file edited except this report.

---

## 0. Method and provenance (what was fetched, when, how)

All fetches 2026-10-25, `curl` + Python stdlib only, no package installed (see §7).

```
$ date -u +%Y-%m-%dT%H:%M:%SZ
2026-10-25T21:07:14Z
```

The registry row read first (`corpus/SOURCES.md:57`), per assignment:

```
$ grep -n "S043" corpus/SOURCES.md
57:| S043 | REA reverse-engineer-anything skill reference, "Android application artifacts" — morluto/rea at tag rea-agents-6.5.0, `skills/reverse-engineer-anything/references/android-applications.md` | docs | A | route-scope sentences only: … | tag rea-agents-6.5.0 (npm package rea-agents@6.5.0); the `Start with inspect_android_package` sentence at snapshot lines 7-8 (S039 cited line 5 — wrong), the "The provider requires" paragraph at :16; snapshot sha256 412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c, 34 lines | supersedes S039 — same scope and tier; … | queued | 2026-10-24 | on-release | — |
```

Full row cells (11 columns, NF=13, contract-valid): `status=queued`, `opened=2026-10-24`, `recheck=on-release`, `used-by=—`.

---

## 1. Verdict on the primary question: OPENED-QUOTE-PRESENT, byte-identical

### 1a. Live fetch of the pinned tag — HTTP 200, 1992 bytes, sha256 `412d9cb4…afa74c`

The repo path at tag `rea-agents-6.5.0` is `.agents/skills/…` (see §1b for why the registry's `skills/…` form 404s):

```
$ curl -sS -L --max-time 60 -w '\nHTTP=%{http_code} SIZE=%{size_download}\n' \
    -o rea-live.md \
    'https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md'
HTTP=200 SIZE=1992
$ sha256sum rea-live.md
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  rea-live.md
$ wc -lc rea-live.md
  34 1992 rea-live.md
```

Fetch time: **2026-10-25T21:07:25Z** (immediately after the 21:07:14Z clock read above).

### 1b. The registry row's own path 404s at the tag it names

```
$ curl -sS -L --max-time 45 -w '\nHTTP=%{http_code}\n' -o /dev/null \
    'https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/skills/reverse-engineer-anything/references/android-applications.md'
HTTP=404
$ curl -sS -L --max-time 45 -w 'HTTP=%{http_code}\n' -o /dev/null \
    'https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md'
HTTP=200
```

The tag's full git tree confirms there is **no** top-level `skills/` path in the repo:

```
$ curl -sS 'https://api.github.com/repos/morluto/rea/git/trees/3b79af28e80785afce9f5998d8f03289402a1847?recursive=1' -o tree65.json
$ python3 -c "import json;t=json.load(open('tree65.json'));print('truncated',t['truncated']));print([e['path'] for e in t['tree'] if e['path'].endswith('android-applications.md')])"
truncated False
[('.agents/skills/reverse-engineer-anything/references/android-applications.md', '896f15f85efaa03503eacfd598bed7db6bf791ea', 1992)]
$ python3 -c "import json;t=json.load(open('tree65.json'));print('any path starting skills/:',[e['path'] for e in t['tree'] if e['path'].startswith('skills/')])"
any path starting skills/: []
```

`skills/…` is the **npm package** layout (`package/skills/…` in the tarball), which is how the round-65 lesson opened it (`npm pack rea-agents@6.5.0`). So the bytes are right; the *label* on the path is wrong for the repo it names. → finding F1.

### 1c. Byte-identity against the lane's committed snapshot and the npm package

```
$ sha256sum corpus/snapshots/rea-android-applications.md
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  corpus/snapshots/rea-android-applications.md
$ diff -u corpus/snapshots/rea-android-applications.md rea-live.md && echo "DIFF: byte-identical"
DIFF: byte-identical
```

Committed at the candidate commit `aa1842fac199aa524930e5565ed3715de5f84c6d`:

```
$ git show aa1842fac199aa524930e5565ed3715de5f84c6d:corpus/snapshots/rea-android-applications.md | sha256sum
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  -
```

The git **blob** id of the lane's copy equals the upstream blob id at the tag — content identity at the object level, not just the digest:

```
$ git hash-object corpus/snapshots/rea-android-applications.md
896f15f85efaa03503eacfd598bed7db6bf791ea
```

Second, independent channel — the npm tarball for the same pinned version:

```
$ curl -sS -L --max-time 90 -w 'HTTP=%{http_code} SIZE=%{size_download}\n' -o rea-agents-6.5.0.tgz 'https://registry.npmjs.org/rea-agents/-/rea-agents-6.5.0.tgz'
HTTP=200 SIZE=5634033
$ sha256sum rea-agents-6.5.0.tgz
531717a06e92ca651aab52691190f916fac044272c01f875e22c5e293218e699  rea-agents-6.5.0.tgz
$ tar xzf rea-agents-6.5.0.tgz -C npm package/skills/reverse-engineer-anything/references/android-applications.md
$ sha256sum npm/package/skills/reverse-engineer-anything/references/android-applications.md
412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  npm/package/skills/reverse-engineer-anything/references/android-applications.md
```

npm registry confirms the version exists and that 6.5.0 is not latest: `dist-tags.latest = 6.8.0`.

**Verdict: byte-identical.** The lane's committed snapshot is a faithful, reproducible copy of the upstream file at the pinned tag, and the npm member agrees.

---

## 2. The quote the C05 entry relies on — located at the live source

The entry's item 11 embeds the S043 quote (candidate bytes `corpus/knowledge/round-70-apk-axml-byte-evidence.md:144`):

> `MATCH rea-android-applications.md: first line 7, folded phrase present=True: Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.`

Live source, numbered (`rea-live.md`, identical to the snapshot):

```
 1  # Android application artifacts
 2
 3  Use the connected server's advertised Android tools. Repository main and npm
 4  4.1.0 include this family. A skill installation alone cannot add it to an
 5  older server.
 6
 7  Start with `inspect_android_package` on the caller's APK path for package
 8  identity, manifest declarations, coverage, and inline Evidence. Use
 9  `search_android_classes` to find candidates, `inspect_android_class` for one
10  class's members, `inspect_android_method` for decompilation, and
11  `trace_android_references` for incoming static references. Each call takes its
12  own APK path and explicit selectors; do not open a native session first.
13  Choose an `overload_index` from the class inventory when methods are ambiguous
14  instead of guessing.
15
16  The provider requires a separately supplied headless JADX MCP JAR 0.7.1 and
17  Java 17 or newer. `REA_JADX_MCP_JAR` selects the absolute JAR path; `JAVA_HOME`
```

**Located quote (17 words, ≤ 25)** — "Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence." — under the heading `# Android application artifacts` (line 1), **spanning live lines 7-8**, first words on line 7. This matches the S043 row's anchor exactly ("at snapshot lines 7-8") and the entry's `first line 7`.

The row's second anchor, "The provider requires" paragraph **at :16**, is also confirmed live (line 16 above) — the JAR 0.7.1 / Java 17 prerequisite the S043 scope cell and the entry's Q05 fence both rest on.

S039's superseded "line 5" is confirmed wrong at the live source: line 5 is `older server.`

Independent re-derivation with the entry's own checker (run from the lane root, read-only):

```
$ python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes
MATCH rea-android-applications.md: first line 7, folded phrase present=True: Start with `inspect_android_package` on the caller's APK path for package identity, manifest declarations, coverage, and inline Evidence.
MATCH dex-format.html: first line 5949, …
MATCH dex-format.html: first line 5956, …
MATCH dex-format.html: first line 5981, …
MATCH dex-format.html: first line 5035, …
MATCH ResourceTypes.h: first line 686, …
exit=0
```

The embedded output at entry line 144 is reproduced verbatim by the command printed above it.

---

## 3. The other three committed snapshots vs the live sources (assignment §"compare with the lane's committed snapshot")

| snapshot | live source fetched today | result |
|---|---|---|
| `corpus/snapshots/rea-android-applications.md` | `raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/…/android-applications.md` | **byte-identical** (`412d9cb4…`, 1992 B) |
| `corpus/snapshots/ResourceTypes.h` | `android.googlesource.com/…/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h?format=TEXT` (base64-decoded) | **byte-identical** (`56b88bc4…`, 86255 B) |
| `corpus/snapshots/APPNOTE.TXT` | `pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT` | **byte-identical** (`0b993022…`, 174585 B) |
| `corpus/snapshots/dex-format.html` | `source.android.com/docs/core/runtime/dex-format` | **DIFFERS — non-semantic, and the live page is not byte-reproducible** (see 3c) |

### 3a. ResourceTypes.h

```
$ curl -sS -L 'https://android.googlesource.com/platform/frameworks/base/+/refs/tags/android-15.0.0_r1/libs/androidfw/include/androidfw/ResourceTypes.h?format=TEXT' -o rt.b64
$ base64 -d rt.b64 > rt-live.h && sha256sum rt-live.h && wc -c rt-live.h
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  rt-live.h
86255 rt-live.h
$ diff -q rt-live.h corpus/snapshots/ResourceTypes.h && echo "RESOURCETYPES: byte-identical"
RESOURCETYPES: byte-identical
```

### 3b. APPNOTE.TXT

```
$ curl -sS -L -o appnote-live.txt 'https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT'
$ sha256sum appnote-live.txt
0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6  appnote-live.txt
$ diff -q appnote-live.txt corpus/snapshots/APPNOTE.TXT && echo "APPNOTE: byte-identical"
APPNOTE: byte-identical
$ sed -n '387,398p;632,640p' appnote-live.txt
   4.3.7  Local file header:
      local file header signature     4 bytes  (0x04034b50)
      …
   4.3.16  End of central directory record:
      end of central dir signature    4 bytes  (0x06054b50)
```

The three APPNOTE line ranges the entry cites (387-398, 511-531, 632-646) are the right sections in the live bytes (`4.3.7 Local file header`, `4.3.12 Central directory structure`, `4.3.16 End of central directory record`).

### 3c. dex-format.html — DIFFERS, but only in per-request chrome

Three successive live fetches today produce three different digests and two different sizes — the page is **not** byte-reproducible:

```
$ for i in 1 2 3; do curl -sS -L -o d$i.html 'https://source.android.com/docs/core/runtime/dex-format'; echo "fetch$i $(sha256sum d$i.html | cut -c1-16) $(wc -c < d$i.html)"; done
fetch1 5203bb8bbafcfb86 281161
fetch2 0f48c6c5365b0e5d 281157
fetch3 e2c2251a73d2603a 281161
```

Each differs from the committed snapshot `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4` (281157 B) in exactly **two** lines out of 8957 — a per-request CSP nonce and a feature-flag string:

```
$ diff corpus/snapshots/dex-format.html d2.html
8946c8946
< <script nonce="R1GN4pA7+nDrYJ/dulpbEJ8pQlLBzr">
---
> <script nonce="vbdULVbgAmQU7zuo3zvp2vt7dY+2W5">
8951c8951
<     'https://www.gstatic.com/devrel-devsite/prod/…/androidsource/js/app_loader.js', '[7,"en",null,…"Profiles__enable_developer_profile_benefits_ui_redesign",…'
---
>     'https://www.gstatic.com/devrel-devsite/prod/…/androidsource/js/app_loader.js', '[7,"en",null,…"DevPro__enable_devsite_captcha",…'
```

**No spec content differs.** The four phrases the entry quotes still land on the same live lines the entry prints:

```
$ grep -n "adler32 checksum of the rest of the file" dex-live.html   → 5949
$ grep -n "SHA-1 signature (hash) of the rest of the file" dex-live.html → 5956
$ grep -n "must be 0x70 (112) bytes" dex-live.html                  → 5981
$ grep -n "ENDIAN_CONSTANT = 0x12345678" dex-live.html              → 5035
```

Same line numbers as entry lines 145-148. Consequence for freshness: **a future live re-open of S045 can never reproduce the snapshot digest** (`c0428612…`), because the live page varies per request; the snapshot digest is a commitment to the committed bytes only. The entry already says exactly this for ZIP ("The ZIP APPNOTE layouts are recorded from a snapshot; whether the upstream document has since changed is not checked", line 146 of the entry) and item 14's sentence says a digest "does not establish … that they are the upstream's current text" (entry:209) — so the entry is honest, but its Unknown bullet names only the ZIP document; S045's live source has the same property and is not named. → advisory note A3.

---

## 4. Freshness of the pin itself

The pinned tag is three releases behind, and one release landed **today**:

```
$ curl -sS 'https://api.github.com/repos/morluto/rea/tags?per_page=100' | python3 -c "…"
rea-agents-6.8.0 160d821ac9a0310afcb8d1fc427862dd6508add5
rea-agents-6.7.0 27dc42d10249f0410904a75c0997842eb03b931c
rea-agents-6.6.0 2c4338db1fdb7773e05376301c558cff2a0b4b80
rea-agents-6.5.0 3b79af28e80785afce9f5998d8f03289402a1847
$ for s in 160d821a… 3b79af28…; do … ; done
160d821ac9a0 2026-10-25T08:35:15Z chore(main): release rea-agents 6.8.0 (#5004)
3b79af28e807 2026-10-14T12:31:45Z chore(main): release rea-agents 6.5.0 (#1693)
```

Content drift of the same file across those tags (sha256 of the raw file at each tag):

```
rea-agents-6.5.0  412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c  1992
rea-agents-6.6.0  67a9237d76a5b736640c6404f5e1fe01d83369848142feb7e11d78f4a5e62732  2125
rea-agents-6.7.0  67a9237d76a5b736640c6404f5e1fe01d83369848142feb7e11d78f4a5e62732  2125
rea-agents-6.8.0  24ecaa1798eb4f28…                                       2584
```

What changed: 6.6.0 added `REA_JADX_OPERATION_TIMEOUT_MS`; 6.8.0 rewrote the provider-prerequisite paragraph ("Use `rea doctor --provider jadx --json` to check the JADX configuration …", "Java and the headless JADX MCP JAR remain caller-supplied"). **The quote the C05 entry relies on is unchanged at every tag** (`grep -n "Start with \`inspect_android_package\`"` → line 7 in 6.5.0, 6.6.0, 6.8.0), and "JADX MCP JAR 0.7.1 / Java 17 or newer" persists at line 16 in 6.8.0 too. So the entry's route-scope claim is not falsified by the newer releases — but the row's `recheck=on-release` cadence now has a live trigger (6.8.0 today) that the registry does not record.

Host-installed copy is *newer* than the registry pin:

```
$ sha256sum ~/.agents/skills/reverse-engineer-anything/references/android-applications.md
67a9237d76a5b736640c6404f5e1fe01d83369848142feb7e11d78f4a5e62732  …
$ grep -n 'rea-agents@' ~/.agents/skills/reverse-engineer-anything/SKILL.md | head -3
33:npx -y rea-agents@6.7.0 <command> [args] --json
```

i.e. the installed skill carries the 6.6.0/6.7.0 content, not the pinned 6.5.0 content. The entry scopes S043 strictly "per rea-agents-6.5.0", so this does not falsify anything; it is recorded because a freshness reader should know the pin and the host install differ.

---

## 5. ADVISORY findings (wave-1; not kill-rule inputs; none contradicts the candidate's bytes)

### F1 — the S043 registry row names a repo path that does not exist in the repo it names, and carries no canonical URL

* Location: `corpus/SOURCES.md:57`, `source` cell — "REA reverse-engineer-anything skill reference, "Android application artifacts" — morluto/rea at tag rea-agents-6.5.0, `skills/reverse-engineer-anything/references/android-applications.md`".
* Evidence: the path 404s at the tag — `curl …/rea-agents-6.5.0/skills/reverse-engineer-anything/references/android-applications.md` → `HTTP=404`; the file actually lives at `.agents/skills/reverse-engineer-anything/references/android-applications.md` → `HTTP=200`; the tag's tree has **no** `skills/` path at all (`any path starting skills/: []`). `skills/…` is the npm-tarball layout (`package/skills/…`).
* Same mislabel in: `corpus/lessons/round-65.md:13` ("morluto/rea, `skills/…`") and `corpus/lessons/round-66.md:13`; the sibling rows `corpus/SOURCES.md:53` (S039) and the round-65/67/68/69 entry headers repeat it. Compare `corpus/SOURCES.md:50` (S036), which does carry the canonical URL `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/docs/firmware-analysis.md`.
* Contract shape (`/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, "Shape" section): "`source` — title — canonical URL or DOI (a repo path or command for `own-work`)". S043 is `kind=docs`, so a canonical URL is the expected form; the row has a path only, and that path 404s against the repo it names. 16 of 47 rows lack a URL, but 15 of those are `kind=own-work` (path/command allowed) — S043 and S039 are the `docs` rows among the URL-less ones.
* Repair shape (advisory): a **new** superseding row (contract rule 2 — corrections are new rows) carrying the canonical URL `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.5.0/.agents/skills/reverse-engineer-anything/references/android-applications.md` (verified today: HTTP 200, sha256 `412d9cb4…afa74c`, 1992 B) plus the npm member path; or, if the L1 prefers not to add a row, the entry's S043 header gains the canonical URL so the citation resolves without the mislabeled row path.

### F2 — S043's `status`/`used-by` were never updated although four entries cite it; the census cannot see this

* Location: `corpus/SOURCES.md:57` — `status=queued`, `used-by=—`, at every commit from `a4c712a` (round-66) through `da02261` (round-69) and at the candidate commit `aa1842`:

```
$ for c in $(git log --format=%H -12 -- corpus/SOURCES.md); do … git show $c:corpus/SOURCES.md | grep "^| S043 " | awk -F'|' '{print $9" "$12}'; done
queued   —      (a4c712a, round-66)
queued   —      (7668510, round-67)
queued   —      (4232235, round-68 build)
queued   —      (14774a2, round-68 adjudication)
queued   —      (da02261, round-69)
$ git show aa1842…:corpus/SOURCES.md | grep "^| S043" | awk -F'|' '{print "status="$9" used-by="$12}'
status= queued  used-by= —
```

* But it is cited by four knowledge entries: `corpus/knowledge/round-67-apk-axml-byte-evidence.md:2`, `round-68-…:2`, `round-69-…:2`, `round-70-…:2` (the candidate, whose Q01 row at :249 counts "S043 (route scope only)" as load-bearing).
* Contract: "`status` — `queued` (opened, worth mining) · `mined` (cited by ≥1 path in `used-by`)"; "`used-by` — repo-relative paths of the knowledge entries or lessons citing the row". S043 is cited by ≥1 path and is still `queued` with `—`. Sibling rows cited by the same candidate carry pointers (S038 → `corpus/knowledge/round-65-apk-axml-byte-evidence.md`, S045 → `round-67-…`, S047 → `round-69-…`), so the inconsistency is specific to S043.
* The fleet census is blind to it: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin --today 2026-10-25` prints only the four known W04s for revenger and `ok` — the only pointer check is W03 "mined with used-by = —", which cannot fire for a `queued` row that is in fact cited:

```
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/… across scopes
revenger	W04	S029 duplicate url tc39.es/ec262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/…/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
```

* Repair shape (advisory, and it interacts with the frozen landing plan): the frozen `reports/round-70/claims.md` §Frontier says only "the S045 row's `used-by` re-pointed old→new at admission". Four of the seven rows the candidate cites carry `used-by` pointers at **rejected** candidates — S038 → round-65 (rejected), S041 → round-65 (rejected), S045 → round-67 (rejected), S047 → round-69 (rejected) — and S043 carries none at all although it is cited four times. At admission the whole cited set should be re-pointed (contract rule 2: each old→new logged in the round lesson). `corpus/lessons/round-70.md` does not exist yet, so there is currently no log to check the old→new transitions against.
* Second, smaller inconsistency in the same family: `corpus/lessons/round-68.md:136` states "`S038`/`S043`/`S041` still carry `used-by` pointers at rejected candidates". For S043 that prose is not supported by the registry at that same commit (`14774a2`): S043's `used-by` is `—` there and at every earlier commit. S038 and S041 do carry such pointers; S043 does not.

### F3 — the candidate's S043 header names no upstream URL/path, so the route-scope citation resolves only through the mislabeled registry path

* Location: `corpus/knowledge/round-70-apk-axml-byte-evidence.md:2` (candidate bytes, identical to `aa1842…`: `git diff aa1842… -- corpus/knowledge/round-70-apk-axml-byte-evidence.md` is empty). The line reads "… (docs, tier A; row opened 2026-10-24, `queued` before this entry; re-opened 2026-10-25 by this entry's author from the committed snapshot `corpus/snapshots/rea-android-applications.md`, digest printed in item 14) — scope: … per rea-agents-6.5.0 … — anchor: the quoted sentence is located by the item-11 `--spec-quotes` command (first line 7)".
* Comparison inside the same header block: the S038 line (:1) carries `https://android.googlesource.com/…` and the S045 line (:3) carries `https://source.android.com/docs/core/runtime/dex-format`; the S043 line carries **no upstream URL and no upstream path**, only the local snapshot path, while pinning the version in prose ("per rea-agents-6.5.0").
* No falsity: the line says re-opened "from the committed snapshot", not from the live source, and the snapshot is byte-identical to the live source (§1), so the entry's own claim is true. The gap is resolvable-ness: a reader following entry:2 → S043 row → repo path lands on a 404 (F1).
* Also worth noting for Q01/Q02 phrasing only (not a defect I assert): the candidate header itself records S043 as "`queued` before this entry", i.e. the candidate knowingly leans on a row the registry has not marked `mined` — see F2.

---

## 6. What is NOT wrong (explicitly cleared, so wave 2 need not re-derive it)

* The S043 quote is present at the live source, at the line the entry prints, under the heading the row names. OPENED-QUOTE-PRESENT.
* The committed snapshot equals the live tag file, the npm 6.5.0 member, and the upstream git blob id (`896f15f8…`). Item 14's pin `412d9cb4… 1992 bytes corpus/snapshots/rea-android-applications.md` (entry:221) is correct and re-derivable.
* The entry's item-11 `--spec-quotes` output is reproduced verbatim by the command printed above it (exit 0) — including the S043 line and the five other phrase matches.
* The candidate's bytes are unchanged from the attacked commit: `git diff aa1842fac199aa524930e5565ed3715de5f84c6d -- corpus/knowledge/round-70-apk-axml-byte-evidence.md` → empty.
* The other three snapshots are byte-identical to their live sources, except dex-format.html's two lines of per-request chrome (§3c), which do not move any quoted phrase or line number.
* The C05 README row is still `uncovered` and the entry still `admission-status: candidate` — the landing order in `claims.md` is intact (`corpus/README.md:41`, `entry:11`).

---

## 7. Tools, versions, channels

No installation was performed; nothing was installed, upgraded or removed (all pacman transactions are PAUSED host-wide, and none was needed). Used: `curl` (system binary), `python3` standard library only (`hashlib`/`json`/`re`/`difflib` via stdlib), `git` read-only (`show`, `log`, `ls-tree`, `diff`, `hash-object` — no mutating command was run in the lane or the fleet). Scratch lived in `/tmp/revenger-r70-openS043/` and was deleted before returning.

---

## 8. Remaining unknowns (not resolvable from this seat)

* Whether the L1 wants a superseding S-row for the corrected canonical URL (F1) or prefers the URL added to the candidate's S043 header line — a decision for the L1/scribe, not a defect this seat can settle.
* Whether the round-70 admission revision is intended to re-point `used-by` for all seven cited rows or only S045 as the frozen claims text says (F2); the frozen contract text names one row, the contract's own status definition implies all of them.
* Whether the `on-release` recheck for S043 is meant to be discharged by a re-open against 6.8.0 (whose route sentence and JAR/Java prerequisite text are unchanged, per §4) before admission.
* `corpus/lessons/round-70.md` does not exist yet, so no old→new status/used-by log exists for this round to be checked against; the S043 correction (F1/F2) should be logged there when the lesson is written.
