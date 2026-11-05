# Round 92 — ConnectorR92Overlap: sibling overlap and considerthese measurement

Seat: ConnectorR92Overlap (connector, leaf). Read-only over the lane and every sibling repo. Nothing was edited, committed or run from the merge package. Lane commit read: 9402183a (claims frozen there).

Scope key: C03 = managed (.NET/CLI) assemblies; C08 = browser/Electron runtime evidence (revenger `corpus/README.md` coverage map rows 50 and 55, both `frontier`).

## 1. Province boundaries (read first)

| repo | PROVINCE.md claim that touches the lane's scope |
|---|---|
| revenger-shokunin | `PROVINCE.md` L3-5: owns "managed assemblies, Electron/JavaScript packages … browser/Electron runtime evidence" |
| kaidoku-shokunin | `PROVINCE.md` L137: "Managed IL (two-tool map)" — `inspect-managed-artifact` via `dnfile 0.18.0` + `dncil 1.0.2`; L139 and L55: "Runtime observation verbs" / "Runtime observation (CDP)" — self-launched CDP targets; L51 Electron/ASAR |
| tabi-shokunin | `PROVINCE.md` L3-9: "browser & web-interaction craft"; owns "CDP session discipline (endpoints, targets, screenshot/DOM evidence capture)" |

Consequence: C03 and C08 are both claimed by at least one sibling province. The lane's C03 and C08 claims are only separable by artifact class (authored fixtures and saved REA records), not by topic.

## 2. Sibling hits — managed (.NET/CLI) assemblies (C03)

Search: `*-shokunin/corpus/knowledge/` and `*-shokunin/corpus/SOURCES.md` for ECMA-335, PE-CLI, BSJB, CLI metadata, managed assembly, dnfile, dncil, dnlib, Cecil, ILSpy, dnSpy, CIL. Hits were counted per file.

| # | sibling path | what it is | overlap with C03 | verdict |
|---|---|---|---|---|
| M1 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-managed-assemblies.md` (24 pattern hits) | r1 host census: `dotnet` host, ~341 framework DLLs, Pinta 36 managed DLLs, Mono.Cecil on disk | Same artifact class (managed PE/CLI), host artifacts not authored fixtures | **overlap, adjacent scope.** No row duplication. The C1 entry must not cite it as evidence: it is a sibling's own-work, not a lane SOURCES row |
| M2 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4-11-managed-unlock.md` (49 hits) and `2026-10-13-r4u-04-dnfile-il.md` (29) | dnfile/dncil unlock; full IL analysis over Mono.Cecil.dll; machine-field census (196 × 0x14c, 181 × 0xfd1d) | Same method class as lane's `inspect-managed-artifact` records (S446) | **overlap, adjacent.** Kaidoku holds the dnfile method; the lane holds REA-producer records on authored fixtures. No duplicate row |
| M3 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-pe-surface.md` (12 hits) | cites ECMA-335 §II.25.2.2 ("0xfd1d = ECMA pure-IL machine marker"), marked "INFERRED-doc, not re-derived locally" | Same standard the C1 entry would cite | **overlap, unregistered citation.** Kaidoku cites ECMA-335 in prose with no SOURCES row (see §3) |
| M4 | `kaidoku-shokunin/PROVINCE.md` L137 | "Managed IL (two-tool map)" | Province-level claim on C03 | **overlap, province level** (see §1) |
| M5 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r4-16-frontier-rescan.md` (8), `2026-10-14-r14-01-queue-b-residual.md` (13) | frontier rescan and queue residual mentioning managed/.NET | Topic mention | **no overlap in substance** (managed term appears as a frontier or queue item; not opened in full this pass) |
| M6 | `mado-shokunin/corpus/SOURCES.md` S401 and the win32/dotnet trees (L712) | Microsoft Learn `System.Windows.Forms.Screen` and dotnet API reference | .NET *API* docs, not CLI/ECMA-335 or PE-CLI artifact formats | **no overlap** with C03 |
| M7 | `kotoba`, `mori`, `tsukuroi`, `kumitate`, `kama`, `kotodama`, `tabi` knowledge and SOURCES, 1–3 pattern hits each | lexical matches (pattern includes `CIL`, `.NET`, `dotnet`) | Not opened in this pass | **no overlap judged from the lexical hit alone; not verified by reading** |

Lane-internal (not sibling) C03-scope rows, for the W04 check: revenger S061 (ILSpy), S068 and S434 (dnSpyEx; S434 supersedes S068), S399 (OALABS dnlib notebook), S282 (ReadyToRun BOTR), S136 (ECMA-335), S446 and S469 (own-work REA managed records).

## 3. ECMA-335 and PE-CLI registry ownership (item 2)

- **Lane owner of ECMA-335 (CLI):** `revenger-shokunin/corpus/SOURCES.md` **S136**, `spec | A`, opened **2026-10-29**, recheck on-release, used-by `corpus/knowledge/round-73-re-resource-atlas.md`. Primary URL: `https://ecma-international.org/wp-content/uploads/ECMA-335_6th_edition_june_2012.pdf`. It is the only ECMA-335 row in the lane (the only lane row that names ECMA-335 in its source cell; S136 is the only lane row with the PDF URL).
- **Sibling owners of ECMA-335:** none. A case-insensitive search for `ECMA-335`, `ECMA 335`, `PE-CLI` and `BSJB` over every `*-shokunin/corpus/SOURCES.md` returns only revenger rows. Kaidoku cites ECMA-335 in knowledge prose (M3) with no registry row.
- **PE format spec (adjacent):** lane **S009** = `learn.microsoft.com/en-us/windows/win32/debug/pe-format`. Kaidoku registers the same URL twice: `kaidoku-shokunin/corpus/SOURCES.md` **S100** and **S102** (a sibling duplicate inside one registry).
- **Would a new C1 row duplicate S136?** Yes, if the C1 entry adds a row for the same PDF. The PDF URL is already registered as S136 (exact URL match, W04 duplicate-URL class). The lane's own staged package also carries it as S089 (see §5). A row for the landing page (`https://www.ecma-international.org/publications-and-standards/standards/ecma-335/` or `https://ecma-international.org/publications-and-standards/standards/ecma-335/`, the staged S057 and S146) is a different URL for the same standard: a standard-level duplicate, not a URL duplicate.
- **Constraint the L1 must reconcile:** the frozen C1 text requires that cited rows were "opened this round (2026-11-05)". The registry contract (SOURCES.md header) says rows are append-only and only `status`, `recheck` and `used-by` change in place, so S136's `opened` cannot be advanced. Options are a logged re-open in the round lesson, or a new row (which duplicates S136). This seat does not decide it; it is a defect risk for the L1.

Other cross-repo duplicate URLs in the C08 and CDP scope (W04 class, sibling-level):

- CDP index: lane **S299** `https://chromedevtools.github.io/devtools-protocol/` == `tabi-shokunin/corpus/SOURCES.md` **S002** (exact URL, different row purpose: tabi cites the scope and `/json/*` endpoints, the lane cites the scope statement). The lane's own rows have no internal duplicate for it.
- Electron fuses and ASAR integrity: lane **S297** `…/tutorial/fuses` and **S298** `…/tutorial/asar-integrity` == `kaidoku-shokunin/corpus/SOURCES.md` **S012** (fuses) and **S014** (asar-integrity) (exact URLs).

## 4. Sibling hits — browser / CDP / Electron evidence (C08)

Pattern: CDP, DevTools, remote-debugging, BiDi, WebDriver, Playwright, Puppeteer, Electron, asar, Chromium, Chrome. 157 knowledge files across siblings match; the per-file top hits are listed.

| # | sibling path | what it is | overlap with C08 | verdict |
|---|---|---|---|---|
| B1 | `tabi-shokunin/PROVINCE.md` L3-12 and `corpus/knowledge/` (≈40 files: `chrome-cdp-loopback-round-44/45`, `chrome-cdp-teardown-round-46(-corrected)`, `webview2-cdp-loopback-round-48`, `webdriver-bidi-*`, `browser-surface-census`, `playwright-accessible-locators-and-snapshots`, `webmcp-*`, `chrome-remote-debugging-profile-boundary`) | browser-driving journey lane; CDP session discipline, Chrome/Edge/WebView2 loopback recordings | Same evidence class (saved CDP runtime evidence in a browser) | **overlap, high.** Tabi owns CDP discipline; C08 must be scoped to the lane's own REA `inspect-web-page` record on `browser-r77` (S447, own-work), not to CDP discipline generally |
| B2 | `tabi-shokunin/corpus/SOURCES.md` S002, S021, S061, S004 | CDP viewer (S002 URL = lane S299), Chrome DevTools for agents, Playwright CDPSession, remote_debugging_server.cc | Source overlap | **overlap.** S002 is a W04 cross-repo duplicate of S299 (§3) |
| B3 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-runtime-observation.md` (26 hits), `2026-10-13-r4-08-observe-verbs.md` (17), `2026-10-13-r4-16-frontier-rescan.md` (18) | self-launched CDP / V8-inspector targets; observe verbs | Same runtime-observation class as C08 (REA CDP provider) | **overlap, high.** Kaidoku PROVINCE L55 and L139 claim the same REA verbs (`inspect-web-page`, `list_browser_targets`, `observe-web-session`) |
| B4 | `kaidoku-shokunin/corpus/knowledge/2026-10-13-r3-renderer-asar.md` (19), `2026-10-13-asar-surface.md` (45), `2026-10-13-r4-05-signal-asar.md` (23), `2026-10-13-r4-06-1password-asar.md` (23), `2026-10-13-r3-typora-signal.md` (23), `2026-10-13-r4-15-appimage-inner.md` (30) | Electron ASAR and renderer analysis of shipped apps (Obsidian, Signal, 1Password, Typora) | Electron runtime and packaging class (C08 names "Electron") | **overlap, adjacent.** Judged from file names, the PROVINCE Electron/ASAR row and the r3-renderer-asar head (opened); the rest not opened. C08 is runtime evidence; these are packaged-artifact analyses. Electron fuses and ASAR integrity rows are shared by URL (§3) |
| B5 | `kagi-shokunin/corpus/knowledge/cdp-bridge-1password.md` and `kagi-shokunin/corpus/SOURCES.md` S069, S070 | 1Password Credential Broker (OIDC workflow); the name "cdp-bridge" is not browser CDP | Term collision only | **no overlap.** S069/S070 are 1Password docs (row titles read) |
| B6 | `kotoba-shokunin/corpus/knowledge/sibling-overlap-census-round74.md` | the fleet's standing sibling-overlap census (20 repos, re-read at frozen heads) with `check_sibling_census.py` | Prior art; not a C03/C08 hit | reference only: the census format used for this seat's verdicts |

Lane-internal C08 status: no revenger knowledge file is about CDP or Electron runtime evidence; S447 (own-work, browser-r77) is the only lane record in scope. C08 is therefore a candidate for `uncovered`, not for `held`, which matches the claim.

## 5. Merge package collision (item 4)

Path: `/home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md` (read-only; no script run).

- Lane registry `corpus/SOURCES.md`: 490 rows, ids S001–S490 contiguous, 0 duplicate ids, 490 unique ids.
- Staged `SOURCES.append.md`: 155 rows, ids S047–S201, 0 duplicate ids.
- `comm -12` of the two id sets: **155 shared ids** (every staged id already exists in the lane). `comm -13` (staged-only ids): **0**.
- Rows with the same id and the same source-cell prefix (first 40 characters): **0**. The shared ids name different sources, so the staged file cannot be appended as-is.
- Primary-URL collisions (first URL in the source cell): 3 staged rows, all matching existing lane rows:
  - staged S147 (PE Format) == lane S009;
  - staged S089 (ECMA-335 PDF) == lane S136;
  - staged S056 (AOSP dex-format) == lane S045 and S048.
- The merge package's own header (`MERGE-REPORT.md`: "lane registry currently holds 46 rows; first staged id is S047") is stale against the lane at 9402183a.
- Adoption is closed this round: no row from the staged file is adopted and nothing is merged.

## 6. considerthese proposal 1 measurement (item 3)

Command run exactly as given, against `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md`:

```
kind: book=6 docs=108 talk=3 dataset=17 community=22 spec=66 paper=61 tool=118 code=34 own-work=55  total=490
```

Tier (fifth cell, same awk with `$5`): `A=441 B=21 C=28 total=490`.

Own-work share, whole registry: **55 / 490 = 11.2 %**. External rows: 435.

Per-window cut (proposal 1 asks for new rows per window). The window is taken as rows whose `opened` column (`$10`) is ≥ 2026-11-01, which is the date granularity of the considerthese window (2026-11-01 10:25 BRT onward). Opened dates: 2026-11-01 = 23 rows, 2026-11-02 = 14, 2026-11-04 = 11.

- Window total 48; kind: docs=8, community=1, own-work=39; tier: A=47, C=1.
- Window own-work share: **39 / 48 = 81.2 %**; external rows in window: 9.

Stale figure in the considerthese file: `considerthese/2026-11-04.md` states "own-work is now 51 of 479 rows" and "26 of 26 new SOURCES rows in the window are own-work". The lane at 9402183a has 490 rows and 55 own-work rows. The file's counts predate 11 rows and cannot be reproduced; its 26/26 figure is not reproduced by the opened≥2026-11-01 cut (39/48). This is reported as a discrepancy, not corrected.

## 7. Verdict summary

- C03 sibling overlap: kaidoku holds the same artifact class and REA verb (`inspect-managed-artifact`, dnfile method) on host artifacts; adjacent, not duplicate. ECMA-335 is owned in the lane by S136 only; no sibling registers it; a new C1 row for the same PDF duplicates S136 (W04).
- C08 sibling overlap: tabi (CDP discipline, ~40 knowledge files) and kaidoku (CDP runtime observation, Electron ASAR) overlap the browser/Electron scope at province level. Two cross-repo exact URL duplicates (S299 = tabi S002; S297/S298 = kaidoku S012/S014).
- Collision count: 155 shared ids (S047–S201), 0 identical rows, 3 primary-URL collisions. Adoption closed this round; nothing merged.
- Unverified: M5, M7 and B5 were judged from match context, not read in full. No command output in this file was produced by a sibling script.
