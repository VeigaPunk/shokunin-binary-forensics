DIVERGE — no further revenger data rows exist beyond the 24 quoted + 2 never-checked rows; the "27" is a grep artifact, and the register's `## By lane` summary is NOT mismatched (24 = 24) while two other internal defects are real (Totals 324 vs 301 spans; ids offset +2 from the lane registry).

# R69QuarD — quarantine register hand-check, wave 4 (adoption closed)

Read-only. Register: `/home/vgpnk/Projects/shokuknow/.ufo/waves/corpus-expansion-1/absent-defect-register.md`
sha256 `5afe1810a6c3d62f37987b575a954f5b1197daa23005d4bb2f1d982f64bad833`, 375 lines, 50.0 KB-class.
Nothing in the campaign tree or the lane repo was written. Scratch under `/tmp/revenger-r69-quarantine/` (deleted before return). No package installs (host pacman paused; nothing needed).

## 1. Slice re-derivation (the assigned question)

`grep -c '^| \`revenger\`' absent-defect-register.md` → **27 lines**. That 27 is not 27 data rows:

| what | count | pointer |
|---|---|---|
| revenger rows in `## Rows` (ABSENT table) | **24** | lines 147–170 |
| revenger row in `## By lane` summary (`| \`revenger\` | 24 |`) | 1 | line 237 |
| revenger rows in `## Rows whose quotes were NEVER CHECKED` | **2** (round1 S054, round3 S099) | lines 359–360 |
| total lines matched by the naive grep | 27 | — |

So the revenger slice is **26 rows with lane+round+S-id cells** (24 quoted + 2 never-checked) and **zero rows remain beyond** the already-named set. Labeled by what the register itself says, the 24 quoted rows are all that "§Rows" contains; the two never-checked rows cannot carry a quote verdict from the register (no quote column).

### Row count and the `## By lane` summary — measured, not assumed
- `## Rows` data rows: **194** (line-based parse) = Totals line "rows with at least one ABSENT quote: **194**" ✓
- `## By lane` rows: 19 lanes, sum **194** ✓
- Per-lane table vs summary, lane-by-lane diff: **NONE** (script output `lane-level diff (main - summary): NONE`). Revenger: table **24**, summary **24**.
- **The `## By lane` "mismatch" premise is falsified.** The register is internally consistent on row counts.
- Register's class column: every one of the 194 is `payload-absent`; Totals `payload-absent 194` ✓.

### One real Totals mismatch (found while counting)
- Totals prose: "ABSENT quotes: **324**".
- The `## Rows` table yields `194 rows + 107 <br> separators = **301** spans` (line-based count, unaffected by unescaped pipes). Difference **23**.
- This is a `Totals`-vs-table discrepancy, not a By-lane discrepancy. Not my lane's rows to fix; recorded as a finding.

## 2. Per-row verdicts (26 revenger rows)

Method: `curl -sL --max-redirs 15 -m 40` with `-D` headers, body saved per row under `/tmp/revenger-r69-quarantine/<round>-<S-id>/body.bin`; every span searched in (a) raw bytes, (b) utf-8 decode, (c) HTML-stripped + entity-unescaped, (d) NFKC, (e) `pdftotext` text for `%PDF` bodies, (f) response headers, plus whitespace-normalized retry. Verdict classes per assignment. `PRESENT(ws)` / `PRESENT(reflow)` mean the span exists only after insignificant-whitespace normalization — recorded distinctly because a literal-fold ABSENT there is a quote-shape defect, not a fabrication.

`reg id` = register's id cell; `lane id` = the id the same source carries in `/home/vgpnk/Projects/shokuknow/lanes/revenger/...` today.

| reg id | lane id | http | bytes | verdict | evidence |
|---|---|---|---|---|---|
| r1 S053 | S055 | 200 | 14981 | **ABSENT** | jadx v1.5.6 release JSON; `Dalvik executable format` and `Last updated 2026-10-09 UTC` are dex-format-page text, not release JSON |
| r1 S055 | S057 | 200 | 90253 | **PRESENT** | span at byte **2336** in `<meta name="description">` |
| r1 S058 | S060 | 200 | 61099 | **ABSENT** | rea.tools/ja title = `REA-コーディングエージェントのリバースエンジニアリング`; `ファームウェア` count **0**; none of the 3 JP titles |
| r1 S060 | S062 | 200 | 57634 | **ABSENT** | crifan jadx page; `[原创]安卓逆向的核心流程` absent |
| r1 S061 | S063 | **502** | 5638 | **UNREACHABLE** | kanxue error page; no quote checked — register's class `payload-absent` is wrong here |
| r1 S062 | S064 | 200 | 446522 | **ABSENT** | arxiv full-text HTML, title `Android App Feature Extraction: …`; none of `cell):`, `On Impact of Semantically Similar Apps in Android`, `In our experiments` |
| r1 S063 | S065 | 200 | 41461 | **ABSENT** | arxiv **abs** landing page only; body-text spans absent from it |
| r1 S064 | S066 | 200 | 41372 | **ABSENT** | arxiv abs; `87%` absent |
| r2 S075 | S077 | 200 | 10289 | **ABSENT** | `analysis.mjs`; `Caller` occurrence count **0** |
| r2 S081 | S083 | 200 | 494 | **ABSENT** | `test-vectors.json` holds TOTP vectors + `"source": "…rfc6238.html#appendix-B"`; the 3 quotes are RFC 6238 prose |
| r2 S083 | S085 | 200 | 6521217 | **PARTIAL(1/3)** | `filename=ApiDemos-debug.apk` present **in `Content-Disposition` header**; the two SWGDE spans are not in an APK |
| r2 S085 | S087 | **404** | 148736 | **UNREACHABLE** | swgde 2026/05 PDF path 404s; class `payload-absent` wrong |
| r3 S087 | S089 | 200 | 4982145 | **ABSENT** | ECMA-335 PDF (pdftotext); JP `Ildasm.exe (IL 逆アセンブラー) - .NET Framework` absent from EN spec |
| r3 S089 | S091 | 200 | 63884 | **ABSENT** | MS docs; both `Re:birth the fidb…`, `Ready To Run` absent |
| r3 S090 | S092 | 200 | 6015111 | **ABSENT** | JSAC 2026 PDF (pdftotext); AOT span absent |
| r3 S092 | S093 | 200 | 1073057 | **ABSENT** | cjc PDF (pdftotext); both Chinese spans absent |
| r3 S093 | S094 | 200 | 731467 | **ABSENT** | seg.nju PDF (pdftotext); all 3 spans absent |
| r3 S094 | S096 | 200 | 290583 | **ABSENT** | SWGDE core-competencies PDF (pdftotext); both spans absent |
| r3 S095 | S097 | 200 | 4120207 | **ABSENT** | FFRI `Embedded.pdf`; `ILSpy` absent |
| r3 S098 | S100 | 200 | 69784 | **ABSENT** | GitHub commits API array; `apkanalyzer` absent — the 3 quotes are README frontmatter keys, not commit-listing fields |
| r4 S107 | S109 | 200 | 1873 | **PRESENT** | exact span at byte **992** (`image = b"REA firmware fixture\n".ljust(64, b"\xff") …`) |
| r4 S108 | S110 | 200 | 1179 | **PRESENT(reflow)** | quote is a 4-line `const root = resolve( / process.env… ?? / "…", / );`; literal false, whitespace-removed true |
| r4 S111 | S113 | 200 | 22380 | **PRESENT(ws)** | actual `"engines":{"node":"^22.19.0 \|\| ^24.11.0 \|\| >=26.0.0"}` (no space after `:`); also `"_nodeVersion":"24.18.0"`, `"predicateType":"https://slsa.dev/provenance/v1"` present |
| r4 S113 | S115 | 200 | 29818 | **ABSENT** | jos.org abstract page; all 3 spans absent |
| r1 S054 (never-checked) | S056 | 200 | 280951 | **PRESENT(anchors)** | dex-format page: `Dalvik executable format` @**5009**, `dalvik.annotation.Signature` @**224736**, `Last updated 2026-10-09 UTC` @**254931** |
| r3 S099 (never-checked) | S101 | 200 | 279743 | **PRESENT(anchors)** | apkanalyzer page: `name="description"` @**4979**, `name="keywords"` @**6234**, `apkanalyzer` @**2183** |

### Tally (my rows)
- 24 quoted rows: **PRESENT 4** (2 literal: S055, S107; 2 normalization-only: S108 reflow, S111 ws) · **PARTIAL 1** (S083 — header-carried filename only) · **UNREACHABLE 2** (S061 502, S085 404) · **ABSENT 17**.
- 2 never-checked rows: now **HTTP 200**, registry anchors **PRESENT**; the register's "could not be fetched" is stale for both.
- Register's own class says `payload-absent` for all 24; my measured class disagrees on **3** rows: 2 unreachable (S061, S085) + 4 source/quote mismatches that are not fabrications of the quoted text (S081, S098, S111, S108 — wrong locator or reflow/whitespace shape).

## 3. Findings (calibration, ranked)

**F1 — the "27" is a grep artifact, and the summary is not mismatched.** 24 `## Rows` rows + 1 `## By lane` summary line + 2 never-checked rows = 27 grep hits (register lines 147–170, 237, 359–360). Table-vs-summary per-lane diff is empty for all 19 lanes and the totals both read 194. Any downstream claim of a "By lane summary mismatch" for revenger is false. Pointer: register lines 25–231, 232–254, 256–366.

**F2 — Totals prose over-counts quotes by 23.** "ABSENT quotes: 324" vs 194 rows + 107 `<br>` = 301 spans. Pointer: register line 20–21 vs the §Rows block. Reproduce: `python3 -c "…"` over lines 26–231 (194 rows, `<br>` total 107).

**F3 — revenger ids in the register do not resolve against the lane registry; the offset is +2, not the +1 the remap table implies.** All 26 rows resolve at `reg id + 2` in `lanes/revenger/**/SOURCES-PROPOSED.md` (jadx r1 S053→S055; ECMA page S055→S057; analysis.mjs r2 S075→S077; test-vectors S081→S083; APK S083→S085; SWGDE S085→S087; ECMA PDF r3 S087→S089; MS docs S089→S091; JSAC S090→S092; commits API S098→S100; apkanalyzer S099→S101; generate.py r4 S107→S109; generate.mjs S108→S110; npm S111→S113; jos S113→S115). `lanes/revenger/ID-REMAP.md` lists a uniform `X → X+1` chain (155 rows, S046→S047 …), which lands one row short: e.g. lane file S053 is `binwalk 3.1.0`, not the jadx row the register cites. A reader resolving register `round+id` literally reads the wrong source. Register line 147 vs `lanes/revenger/SOURCES-PROPOSED.md:80,90,101`; `lanes/revenger/ID-REMAP.md:20-21`.

**F4 — one revenger row is not parseable as a table row.** Register line 169 (r4 S111) embeds `^22.19.0 || ^24.11.0 || >=26.0.0` with unescaped `|` inside the code span; GFM splits cells there, so the quote cell truncates at `^22.19.0` for any pipe-splitting reader (this is why a naive parser reports a truncated span). The content is present in the payload under whitespace normalization, so the row is PRESENT, not fabricated.

**F5 — cross-row quote mixing (r1 S061 vs r1 S062).** S061's middle span `Android App Feature Extraction: A review of approaches for malware and app similarity detection` is the `<title>` of the **S062** cited page (fetched bytes, title tag), while S062's spans are absent from its own page. Quotes were attached to the wrong rows; neither is a byte-fabrication.

**F6 — quoted text lives upstream of the cited artifact (r2 S081, r3 S098).** S081's three spans are RFC 6238 prose; the cited `test-vectors.json` (494 B) only carries `"source": "…rfc6238.html#appendix-B"`. S098's spans (`apkanalyzer`, `description`, `keywords`) are README_zh frontmatter keys; the cited commits API returns commit metadata only (`grep apkanalyzer` → 0).

**F7 — two rows the register classifies `payload-absent` are simply unreachable today.** kanxue 502 (5638 B) and the swgde 2026/05 PDF 404 (148736 B). The register's class legend forbids calling those fabrications; its own row text ("cited source … all checked") asserts a fetch that does not succeed now. Class should be `unreachable`. Register lines 151, 158.

**F8 — two never-checked rows are checkable now.** Both `source.android.com/docs/core/runtime/dex-format` and `developer.android.com/tools/apkanalyzer` return HTTP 200 (280951 / 279743 B) and both lane-registry anchors (S056 dex-format: title + `dalvik.annotation.Signature` + `Last updated 2026-10-09 UTC`; S101 apkanalyzer: `meta description` + `meta keywords`) are present at the byte offsets above. The register's "could not be fetched" is a stale reachability class for both.

## 4. Confidence and limits
- ABSENT on HTML/JSON rows: high (raw + 4 renderings searched; the pages' titles confirm identity).
- ABSENT on PDF rows (S087, S090, S092, S093, S094, S095): medium — the searched rendering is `pdftotext` default; CJK glyph reflow or embedded-font extraction could hide a span, so these are "absent under pdftotext", not "proven absent from the document".
- `[INFERENCE]` The +2 id offset is measured for 26/26 rows but its cause (a second renumber after the register was generated, or the register reading a pre-staging ids file) is not established from the bytes I read; I did not read the generator `absent-defect-register.py`.
- The register was not modified; adoption remains closed; wave-4 in force.
