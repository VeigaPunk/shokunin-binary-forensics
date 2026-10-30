# R73Source058 — frozen C10 coverage admission, source audit S058 (JADX)

Seat: R73Source058 · reviewer role · axes: coverage, source accuracy · leaf member (no subagent dispatch).
Assignment scope: SOURCES.md row S058 only. No other source admission. No row edited, no superseding row written (S071/S082 are outside this seat; round-73 lesson already carries S427/S428 for them, not audited here). Read-only besides this report. No installs, no builds, no target execution.

## Located quote and pin

- Row: `corpus/SOURCES.md:72` — `| S058 | JADX — https://github.com/skylot/jadx | tool | A | … | README.md "JADX" and "Main features", commit f2d8496e9ab766acc942484c1e483843979f1260, accessed 2026-10-27; "Please note that in most cases jadx can't decompile 100% of the code, so errors will occur." | … | mined | 2026-10-27 | on-release | corpus/knowledge/round-72-tool-landscape.md |`
- Lesson Gate row: `corpus/lessons/round-72.md:17` carries the same quote (identical text). Consistent.
- Cited primary URL: https://github.com/skylot/jadx
- Cited pin: commit `f2d8496e9ab766acc942484c1e483843979f1260`.
- Re-opened by me: 2026-10-30 (access date) via
  `https://raw.githubusercontent.com/skylot/jadx/f2d8496e9ab766acc942484c1e483843979f1260/README.md` → HTTP 200, 18599 bytes, sha256 `985d05ae3ba2a4756db29b7c3560be09e248e6559e2bb5176f3d28560cc4a7e4`.
- Pin existence: `https://api.github.com/repos/skylot/jadx/commits/f2d8496e9ab766acc942484c1e483843979f1260` → HTTP 200; committer date 2026-10-10T23:26:39Z; message "docs: update readme downloads and input formats, fix grammar (PR #2993)". Observation.

## Verbatim comparison (markup-normalized only)

Located quote (17 words, ≤25 ✔):

> "Please note that in most cases jadx can't decompile 100% of the code, so errors will occur."

Pinned README bytes, line 19 (inside a `> [!WARNING]` block):

```
> Please note that in most cases **jadx** can't decompile 100% of the code, so errors will occur.<br />
```

Result: **MATCH after normalizing markup only** (the `**` emphasis around `jadx` and the trailing `<br />` removed). The raw byte-exact substring does not match because of the bold markers, so the quote is verified only under the normalization above. Observation.

Locator check: heading `## JADX` (line 3) and `**Main features:**` (line 22) both present, matching the row's "README.md "JADX" and "Main features"" locator. The Main features bullet list is at lines 23–26.

## Scope, tier, used-by, flip

- **Scope (row):** "The project's README declaration for DEX/APK and Java bytecode outputs, plus its stated decompilation limitation."
  - Limitation half: agree. The pinned README states the limit verbatim (above).
  - DEX/APK half: agree. Line 16: "Command-line and GUI tools for producing Java source code from Android Dex and APK files"; line 23: "decompile Dalvik bytecode to Java code from APK, dex, aab, apks, apkm, xapk and zip files".
  - **"Java bytecode outputs": disagree (wording defect).** The README lists Java bytecode as an *input*: line 24, "also decompile Java bytecode (jar, class, aar) and smali files". The output the README names is Java source code (line 16). The phrase "Java bytecode outputs" misstates direction. It narrows nothing load-bearing for admission, but a reader could take JADX to emit bytecode. Observation (text), inference (reader confusion).
- **Tier A:** agree. Official maintainer repository (skylot/jadx). Observation.
- **Used-by:** `corpus/knowledge/round-72-tool-landscape.md:26` ("Need Android/APK output views | JADX S058; Apktool S059 | …"). Token S058 present in the entry; the row points at the correct file. Agree.
- **Entry paraphrase drift (not a located quote):** the entry at line 26 says JADX "warns that many cases do not decompile completely." The README says "in most cases … can't decompile 100% of the code". "Many" is weaker than "most". The row's Teaches column ("may be incomplete") also softens "in most cases". Both are minor understatements of the limit, not contradictions. Observation (text), disagree on the strength word only.
- **Rejection flip:** none stated in the row and none needed; status `mined` / ADMIT tier A is consistent with a verbatim limit at the pin. I agree with the disposition.

## Disposition

**Agree** with ADMIT, tier A, status `mined`, limitation retained (round-72 lesson Gate row and registry row).

Disagree only on two wording points, neither of which changes admission:
1. Scope phrase "Java bytecode outputs" should read as input to a Java-source output (README line 24 vs line 16). Fix would need a NEW superseding row (rows are append-only); I did not write one.
2. The entry's "many cases" and the row's "may be incomplete" understate the README's "in most cases". Fix would be a wording edit in the entry, not in this seat's scope.

Round-72 spot-check (`corpus/lessons/round-72-verifier-spotcheck.md:68`) reported the same quote as verbatim and agreed; my independent re-open agrees on the quote and disagrees only on the scope wording above.

## Cross-references (ID namespace)

- `grep '^| S058' corpus/SOURCES.md` → exactly one row (no duplicate in the registry).
- `corpus/lessons/round-67.md:35` and `round-69.md:151` use "S058" for a different campaign-register source (rea.tools/ja, ABSENT). These are a separate register numbering, not this row. Observation; residual namespace risk, not a defect of this row.
- `reports/round-72/shortlink-dispositions.md:28` (t.co → skylot/jadx) records a duplicate of S058, no duplicate row added. Consistent.

## Network and source failures

None this session. Both fetches (raw README, commit API) returned HTTP 200. No fallback or paraphrase was needed.

## Residual risk / unknowns

- Whether `f2d8496` was the README tip on 2026-10-27 is not proven; the row's locator is the pinned commit itself, which exists. Unknown, immaterial.
- Fetched README and API JSON treated as data only; no embedded instruction followed.

## Tools and cleanup

- Installs/updates: none. Pacman paused host-wide; only `curl` (existing) used.
- Receipt: pinned README (18599 bytes, sha256 above) written to scratch `/fast/scratch/hyaku/revenger-r73/R73Source058/jadx-README-f2d8496.md`; key lines reproduced verbatim in this report (lines 14, 16, 19, 22–24). Scratch directory removed after this report was written.
- No builds, lints or tests run (none requested).
