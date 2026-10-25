DIVERGE — of the 8 register rows that exist for my lane slice, 4 are misclassified (S107 literal PRESENT, S111 PRESENT under JSON re-serialization, S113 PRESENT at the same article's canonical URL, S108 a whitespace-fold artifact of real source); only S094, S095, S098 survive as ABSENT, S099 is UNVERIFIED-REACHABLE with its "unreachable" premise falsified, and S100 has no `revenger` row at all.

# Quarantine register hand-check — lane `revenger`, wave 4 (adoption closed)

Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
(READ-ONLY campaign tree; not edited.)
Counter-report: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-69/R69QuarC.md`.

## 0. Slice derivation (rows whose lane cell is `revenger`, round + S-id present)

```
$ awk '/^\| `revenger`/{print NR": "$0}' absent-defect-register.md   # 24 revenger rows at L147-170, L359-360
$ grep -n "S100" absent-defect-register.md
269:| `chousa` | round3 | S100` | the gate block named no locator, so no quote was checked | #### Gate — S100 |
294:| `game-dev-2d` | round4 | S100` | the cited source could not be fetched, so no quote was checked | https://docs.godotengine.org/en/4.7/classes/class_%40globalscope.html |
```

Assigned S-ids that resolve to a `revenger` row: S094 (L164), S095 (L165), S098 (L166), S099 (L360,
never-checked section), S107 (L167), S108 (L168), S111 (L169), S113 (L170). **S100 has no `revenger`
row** (only `chousa` L269 and `game-dev-2d` L294) — nothing to check, no verdict possible.

## 1. Method

For each row: `curl -sL --max-redirs 15` the cited URL, save bytes under
`/tmp/revenger-r69-quarantine/<S-id>/`, then search the quoted span in the raw bytes plus these
renderings: UTF-8 / GB18030 decode, NFC, NFKC, HTML-unescape, tag-stripped text, whitespace-collapsed
(`\s+`→` `) of each, and for PDFs `pdftotext` default / `-layout` / `-raw` (plus collapsed and NFKC
of each) = 20 renderings per PDF, 11 per text source; JSON sources additionally re-serialized with
`json.dumps` (parse-level rendering); code sources additionally fold to whitespace-free. All eight
cited URLs returned HTTP 200 on 2026-10-25T10:14Z. Scratch removed at close (only my own 8 S-id
directories + my `rows.json`; a sibling seat's S053–S093 directories were left untouched).

## 2. Per-row verdicts

```
S094 ABSENT  (verbatim) cover/TOC span is a '/'-joined composite; the four fragments are on page 1 but the span is in 0 of 20 renderings, incl. decompressed XMP
S095 ABSENT  "ILSpy"/"decompiler"/"Privacy Policy" occur 0 times in an 80-page, fully text-layered FFRI PDF (4,120,207 B)
S098 ABSENT  quoted tokens `apkanalyzer`, `description`, `keywords` each occur 0 times in the 10-commit GitHub API JSON — mismatched-source row
S099 UNVERIFIED-REACHABLE  fetch now succeeds (HTTP 200, 280,121 B) but the register records no quote for this row ("unreachable" premise falsified)
S100 NO-ROW  no `revenger` S100 row exists in the register; S100 appears only for `chousa` and `game-dev-2d`
S107 PRESENT quote found literally at byte 992 (line 26) of generate.py — register wrong
S108 PRESENT (fold) same statement present at generate.mjs lines 6-9, reflowed over 4 lines + trailing comma; literal one-line span absent, matches at char 171 under whitespace-free fold — fold artifact, not fabrication
S111 PRESENT all three quotes present in the parsed-JSON re-serialization at char 864 / 1063 / 20999 (`predicateType` at /dist/attestations/provenance) — register wrong
S113 PRESENT all three quotes present verbatim (raw bytes 721 / 931 / 25643) at the same article's canonical URL; the cited `ch/reader/...` path serves an empty template — register wrong
```

### S094 — `absent-defect-register.md:164` — ABSENT (verbatim), composite not fabrication

URL `https://www.swgde.org/wp-content/uploads/2025/09/2025-07-12-Core-Competencies-for-Mobile-Device-Forensics-12-F-003-2.0.pdf`
→ HTTP 200, 290,583 B, sha256 `593956e1e28b30e00ab3a2195a1baa9494f072043c1ba8e095b6df24053250c1`, 11 pages.

- Q0 `Scientific Working Group on Digital Evidence / Core Competencies for Mobile Device Forensics / SWGDE 12-F-003-2.0 / Vers` → 0 hits in 20 renderings; also 0 in `qpdf --qdf --object-streams=disable` output (XMP block present, 1,770 B, `dc:title` only) and 0 for the slash-joined substrings `Digital Evidence / Core`, `12-F-003-2.0 / Vers`.
- Q1 `5.1 Legal Considerations and Ethical Standards 5.2 Foundational … 5.4 Collection, Seizu` → 0 hits; whitespace-free fold also -1.
- Underlying text *is* in the document, which is why "fabrication-class" overstates the defect: page 1 (`layout.txt:1-4`) has the four cover lines separately; the section-5 TOC (`layout.txt:74-77`) puts dotted leaders and page numbers between the heading numbers and titles; `layout.txt:153-157` lists the same headings as `•` bullets without numbers. The register span is a slash-joined search-snippet shape ending mid-word (`Vers` + `Version: 2.0 (7/12/2025)` at `layout.txt:90`).

### S095 — `:165` — ABSENT

URL `https://www.ffri.jp/assets/files/research/research_papers/Embedded.pdf` → HTTP 200, 4,120,207 B,
sha256 `32318d4eb22bd979ae3e3055d64f9020eb33a1ce4c9f3940a6cccf9deab753b3`, 80 pages.

- `ILSpy is the open-source, cross-platform .NET assembly browser and decompiler.` → 0 of 20 renderings.
- `Privacy Policy for ILSpy` → 0 of 20 renderings.
- Component check: `grep -c ILSpy|decompiler|Privacy Policy|.NET assembly` over `layout.txt` = 0/0/0/0; binary `grep -a -c ILSpy` = 0, `decompiler` = 0.
- No scanned-page escape hatch: per-page `pdftotext` char counts p1..p80 range 55–4,500 (every page carries a text layer), total 60,700 chars.
- Document is "組み込みシステムのセキュリティ" (Fourteenforty Research Institute) — an unrelated ILSpy doc-page snippet. ABSENT stands.

### S098 — `:166` — ABSENT

URL `https://api.github.com/repos/morluto/rea/commits?path=docs/readme/README_zh.md&per_page=10` →
HTTP 200, 69,784 B, sha256 `8b0b207ac6cbb79c524a73c165176766f9157b5466665f0d144002afd61398f8`, a 10-element
commit array (messages e.g. `docs(i18n): add complete Romanian README (#7026)`).

- `apkanalyzer` 0, `description` 0, `keywords` 0 over 11 renderings (raw counts: 0/0/0). Only `readme` 8 / `README` 4 occur.
- The three quoted tokens look like a package-metadata or apkanalyzer-docs fragment; the cited commit-list JSON contains none of them. ABSENT stands.

### S099 — `:360` (never-checked section) — UNVERIFIED-REACHABLE

URL `https://developer.android.com/tools/apkanalyzer` → **HTTP 200**, 280,121 B, sha256
`bf64784ccc1f1cfbf96a18246fb194bd3f60bb9a484c8f954e43ffd1892d96ad`; visible text 16,398 chars with
`apkanalyzer` ×8 and `APK Analyzer` ×4 — the real doc page.

The row's haystack cell is prose (`the cited source could not be fetched, so no quote was checked`), so
the register records **no quote to match**. The row's class premise ("could not be fetched") is now
false; there is nothing to confirm or refute, hence UNVERIFIED-REACHABLE rather than ABSENT. (Note the
row's S-id cell is also malformed — `S099`` with a stray trailing backtick, L360.)

### S100 — NO-ROW

No `| \`revenger\` | … | S100 …` line exists. Both S100 entries belong to other lanes (L269 `chousa`,
L294 `game-dev-2d`). Recording as a slice-derivation finding, not a verdict.

### S107 — `:167` — PRESENT (register wrong)

URL `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/scripts/fixtures/firmware/generate.py`
→ HTTP 200, 1,873 B, sha256 `32625e04658d57739f2c1102c8fd029778b88c4905740ed124277b16d8048275`.

Quoted span `image = b"REA firmware fixture\n".ljust(64, b"\xff") + compressed + b"\x00" * 128`
(**byte offset 992, line 26, 81 bytes**) — found literally in the raw file, 33 renderings:

```
context: ip.compress(buffer.getvalue(), mtime=0)
image = b"REA firmware fixture\n".ljust(64, b"\xff") + compressed + b"\x00" * 128
(root / "firmware.bin").write_bytes(image)
```

The quote is present verbatim in the tagged upstream file. The register's "payload-absent" is wrong for
this row; the only wrinkle is that the register escaped the Python escapes (`\\n`, `\\xff`, `\\x00`) —
after one level of unescaping (the variant printed above) it matches exactly.

### S108 — `:168` — PRESENT under whitespace-free fold (literal single-line absent)

URL `https://raw.githubusercontent.com/morluto/rea/rea-agents-6.7.0/scripts/fixtures/firmware/generate.mjs`
→ HTTP 200, 1,179 B, sha256 `9bea82e92e5462bbaf524161105b79c1845c95d5062d826732b402a9c5351a5c`.

- Literal span `const root = resolve(process.env.REA_FIRMWARE_FIXTURE_ROOT ?? "_reference/firmware-integration/generated",);` → -1 in all 11 renderings (including `\s+`→` `, which yields `resolve( process.env…generated", );`).
- Source lines 6-9 are the same statement, reflowed:

```
const root = resolve(
  process.env.REA_FIRMWARE_FIXTURE_ROOT ??
    "_reference/firmware-integration/generated",
);
```

- Whitespace-free fold of the whole file matches the quote at **char 171**.

Disposition: the register's single-line span is a reflow of real source (trailing comma inside
`resolve(...)` preserved, line breaks and indentation dropped). This is a fold gap, not a fabricated
quote; counted as PRESENT-with-caveat, never as fabrication-class.

### S111 — `:169` — PRESENT (register wrong)

URL `https://registry.npmjs.org/rea-agents/6.7.0` → HTTP 200, 22,380 B, sha256
`ae3429d52774e39bda4f8c9ba9aa141b26901ec65f82a394e540ed9cc479c236` (npm packument for `rea-agents@6.7.0`).

All three quoted spans are in the document; the raw body is compact JSON (`"engines":{"node":…`,
`"_nodeVersion":"24.18.0"`), the register quotes the spaced form, which is the standard
`json.dumps(body)` rendering:

| quote | charoff in `json.dumps(body)` | raw-body key |
|---|---|---|
| `"engines": {"node": "^22.19.0 || ^24.11.0 || >=26.0.0"}` | 1063 | `"engines":{"node":"^22.19.0 \|\| ^24.11.0 \|\| >=26.0.0"}` |
| `"_nodeVersion": "24.18.0"` | 20999 | `"_nodeVersion":"24.18.0"` |
| `"predicateType": "https://slsa.dev/provenance/v1"` | 864 | at `/dist/attestations/provenance/predicateType` |

`json.dumps(body, indent=2)` would *not* match (nested object expands) — the register's span corresponds
to the default-separator re-serialization. Content is present; the 11 folds evidently did not include a
JSON re-serialization.

### S113 — `:170` — PRESENT (register wrong; locator/rendering defect)

Cited URL `https://www.jos.org.cn/ch/reader/view_abstract.aspx?file_no=5651&flag=1` → HTTP 200,
29,818 B, sha256 `ad0309245abce946f87ddd8deb8b510cdd9bc218bfebbd57459d0dfcccb1af07` — **but it is an
empty server template**: visible text 761 chars, `摘要 : 关键词 : DOI： 分类号 : 基金项目: Abstract : Key words :`
all blank, no title, `程序分析`/`研究进展`/`张健` = 0. Control `file_no=5650` returns the same 29,818 B
empty template, so the `ch/reader/` path is generically unpopulated, not article-specific.

The same article (id 5651) at the site's canonical reader path **does** carry the quotes:

- `https://www.jos.org.cn/jos/ch/reader/view_abstract.aspx?file_no=5651&flag=1` → 302 to
  `https://www.jos.org.cn/jos/article/abstract/5651`, HTTP 200, 56,819 B,
  sha256 `c71a37c7ae2277c587c62ea15acb6c6863b1515cff8e984145757df675412a02`.

All three quoted spans verbatim in the raw bytes:

| quote | byte offset | visible text |
|---|---|---|
| `介绍了若干基本程序分析技术（抽象解释、数据流分析、基于摘要的分析、符号执行、动态分析、基于机器学习的程序分析等），特别是最近10余年的研究进展.` | 721 | charoff 1474 |
| `进而介绍了针对不同类型软件（移动应用、并发软件、分布式系统、二进制代码等）的分析方法.` | 931 | charoff 1546 |
| `张健,张超,玄跻峰,熊英飞,王千祥,梁彬,李炼,窦文生,陈振邦,陈立前,蔡彦.程序分析研究进展.软件学报,2019,30(1):80-109` | 25643 | charoff 2504 |

Abstract window (cleaned text): `摘要: 在信息化时代，人们对软件的质量要求越来越高.程序分析是保障软件质量的重要手段之一…`
— the quoted sentences are the paper's own abstract. So the row's ABSENT is a fetch/locator defect
(site serves an unpopulated template at the cited path), not a fabricated quote.

## 3. Tally (my 9 assigned S-ids)

| verdict | count | rows |
|---|---|---|
| PRESENT (register wrong) | 4 | S107 (literal, byte 992), S111 (JSON re-serialization, 864/1063/20999), S113 (canonical article URL, bytes 721/931/25643), S108 (whitespace-free fold at char 171 — reflow, not fabrication) |
| ABSENT (fabrication-class confirmed) | 3 | S094 (composite span, 0/20 renderings + XMP), S095 (0/20 renderings, 80 pages all text-layered), S098 (0/11 renderings) |
| UNVERIFIED-REACHABLE | 1 | S099 (HTTP 200, no quote recorded to check; "unreachable" premise false) |
| NO-ROW | 1 | S100 (no `revenger` S100 row in the register) |

Register-line counts checked: L164, L165, L166, L167, L168, L169, L170, L360. Slice is complete for
every `revenger` row in my assigned id set.

**Calibration note for the register's owner:** 4 of 8 real rows in this slice are false positives of
two mechanical kinds — (a) whitespace/formatting folds (S108, S111), which need a JSON re-serialization
and a whitespace-free fold, and (b) locator defects (S113) where the cited URL serves an empty template
while the same document is reachable at a sibling path. S094 is a third kind: a snippet-shaped composite
whose fragments all exist in the source, so "payload-absent / fabrication" overstates it. Genuine
fabrication-class: S095 and S098 (quoted strings with zero character-level presence in a fully
text-layered source).

## 4. Hygiene

- No installs/upgrades (nothing needed: `curl`, `pdftotext`, `qpdf`, `pdfinfo`, `python3` already present); no pacman transaction attempted.
- No writes outside this file and `/tmp/revenger-r69-quarantine/<S-id>/`; the register and campaign tree were read-only. No git/jj commands run.
- Scratch `/tmp/revenger-r69-quarantine/{S094,S095,S098,S099,S107,S108,S111,S113}` and `rows.json` deleted before return (sibling seat's S053–S093 artefacts untouched).
