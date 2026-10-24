PASS-WITH-REQUIRED-EDITS — the admission commit must (a) flip row C05 at corpus/README.md:34 and (b) delete or rewrite the stale `## Frontier` C05 bullet at corpus/README.md:69-70; the pre-existing C07 Frontier bullet at :63-66 is already stale against row C07's `held` status (debt, not introduced this round — see finding 3).

## Scope exercised

Read: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/README.md` (legend :21-26, coverage map :28-44, `## Known gaps` :50-57, `## Frontier` :59-74), `/home/vgpnk/Projects/shokunin/revenger-shokunin/PROVINCE.md` (lane-root, 33 lines), `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md` (C1 :19-30, admission order :110-123, frontier conformance :125-134), `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure.py` (K/ROW_OPS/legend-mismatch block :28-86, C5 block :259-306, HOLDS_OK_V3 :330-331), candidate entry header `corpus/knowledge/round-65-apk-axml-byte-evidence.md` (first ~30 lines), `corpus/SOURCES.md:52-55` (S038/S039/S040/S041 all present).

## Finding 1 — what still asserts C05 is recordless/groundless

Legend (`corpus/README.md:21-26`): `frontier` = "no knowledge and no saved record"; `uncovered` = "work evidence exists but no admitted knowledge entry"; "Work evidence is not knowledge: fixture and run records stay in `fixtures/` and `live/runs/`."

Exactly two corpus/README.md strings still carry C05 as unexplored:

- `corpus/README.md:34` — `| C05 | Android packages (APK) | — | — | frontier |`. The `frontier` token plus the `—`/`—` cells assert no knowledge and no saved record. Correct **right now**: `grep -rl 'inspect_android_package' corpus/live/runs/` → 0 files (ROW_OPS `{'C05': {'inspect_android_package'}}` at measure.py:65 finds nothing; `README_TOKEN_LEGEND_MISMATCH` stays 0, consistent with `measure-before.log`). The candidate entry itself does not falsify `frontier` — it is `admission-status: candidate` (entry header, line ~9), and a candidate/rejected file is explicitly "not coverage" per the legend.
- `corpus/README.md:69-70` — `## Frontier` bullet: "C05 Android — REA `inspect_android_package`; jadx 1.5.6 is present; needs an authored APK fixture." **Already half-stale today**: the fixture exists — `ls corpus/fixtures/apk-r65/` → `fixture.apk` (947 B, sha256 `05d2280f…03e` per claims.md :21-24), `generator.py`, `truth.json`, `readout.py`. "needs an authored APK fixture" asserts a blocker that no longer exists.

**Required Frontier edit, admit path (frozen order step 3, claims.md :118-119 — `frontier → held` naming only the new entry, same revision):**
1. Row :34 → `held`, knowledge cell naming only `knowledge/round-65-apk-axml-byte-evidence.md` (scope-paren in the C06/C07 row style: manual byte-derived readout of `fixtures/apk-r65/fixture.apk` only; no install/signing/dex-validity/provider-completeness/authenticity claim), evidence cell naming `fixtures/apk-r65`. "No other README row changes" (claims.md :28) constrains **rows**, not the section bullets; the SCORECARD itself routes "`## Frontier` C05 prose refresh at admission time (with the row flip, same revision)" (SCORECARD.md:454, grep-confirmed).
2. Bullet :69-70 → **delete the bullet** (recommendation). Rationale: section header :61 reads "Ground being explored and not yet held" — a `held` row cannot keep a bullet. A rewrite keeping residual provider-readiness notes ("jadx 1.5.6 present; `inspect_android_package` provider route unprobed") would rename unheld depth, not frontier; deletion is the clean minimal move and matches how held rows are absent from the list (C01, C04, C06, C09 have no bullets). If L1 prefers keeping the provider note, reword to drop "needs an authored APK fixture" and reframe as provider readiness on the held row's unheld depth — never re-assert fixture absence.
3. `## Frontier` ordering survives deletion: list becomes C07(stale—finding 3), C03, C08, custody; "nearest first" ordering is unaffected by removing C05.

**Required edit, falsification path (`frontier → uncovered`, claims.md :27, :119):**
1. Row :34 status → `uncovered`; evidence cell must name the work evidence that makes `frontier` false under the legend: `fixtures/apk-r65` plus the retained rejected candidate `knowledge/round-65-apk-axml-byte-evidence.md` (C04 row :33 shows the retained-rejected naming convention).
2. Bullet :69-70 → rewrite, not delete: `uncovered` ground is still "not yet held," so the bullet stays but must drop "needs an authored APK fixture" (the fixture exists); it should describe the residual step (successful gated admission over the landed fixture, or provider probing).
3. `README_TOKEN_LEGEND_MISMATCH` stays 0 either way: `uncovered` rows are not in the probe's frontier check (measure.py :80-83 keys on `cols[-1] == "frontier"`).

## Finding 2 — Known gaps section (:50-57)

No C05/APK content. Two bullets only: SKILL.md/AGENTS.md absent-debt (:52-53) and the pre-contract seed/checklist re-gate debt (:54-57). **No edits required** by this claim. `grep -n 'apk\|Android' corpus/README.md` → only lines 34, 69-70 (verified above).

## Finding 3 — C07 Frontier bullet accuracy (pre-existing staleness)

`corpus/README.md:63-66`: "C07 firmware — REA `inspect_firmware_regions` / `extract_firmware` need caller-supplied Binwalk 3.1.x and Unblob 26.6.x; the host has binwalk 3.1.0 and unblob 26.6.4 (`.ufo/waves/kaika-r1/scout-freshness.md`). Presence is not readiness: an authored known-truth firmware fixture is the next probe."

Two of three claims are stale:

- Section header :61 ("not yet held") vs row :36 — C07 is `held` since round 64 (`knowledge/round-64-firmware-region-byte-evidence.md`). A held row is listed as frontier ground.
- "an authored known-truth firmware fixture is the next probe" — done: `corpus/fixtures/firmware-r63/` (`firmware-r63.bin`, `generator.py`, `truth.json`) and the r63 run `corpus/live/runs/round-63/inspection.json` (operation `inspect_firmware_regions`, binwalk 3.1.0) both exist; the r64 entry was admitted over exactly this evidence.
- Still accurate residue: the caller-supplied Binwalk 3.1.x / Unblob 26.6.x requirement and host versions (binwalk 3.1.0, unblob 26.6.4 — consistent with `.ufo/waves/kaika-r1/scout-freshness.md:19-20` and `corpus/live/runs/round-63/inspection.json` provider fields).

History: this staleness was *created by the round-64 flip* (row held, bullet left behind). R63ReadmeFlipDraft explicitly deferred it: "C07's `frontier` token becomes legend-stale… routed as debt for the next round's claims" (`.ufo/waves/round-64/R63ReadmeFlipDraft.md:128-132,161-162`); the r64 flip retired the token but not the bullet.

**Recommendation for the admission commit:** conservative reading of "No other README row changes" (claims.md :28) permits fixing the C07 bullet — it is a section bullet, not a row. Two defensible options:
- (a) Fix in the same revision (correctness-first): delete the C07 bullet, or reword to name the *actual* residual frontier (engine-validation depth: unblob 26.6.4 found zero chunks in the same image binwalk parsed — R63LedgerFirmware ledger I5; signature-scan coverage limits). Deletion risks losing the unheld-depth note; a one-line reword keeps it honest.
- (b) Minimal-scope reading: land only the C05 row+bullet edit and route the C07 bullet as named debt in `corpus/lessons/round-65.md` (the claim's routed-debt convention, claims.md :133-134). This preserves a deliberately minimal README diff.
Either way it is **reported, not silently left**: an admission commit that publishes an updated README while leaving a bullet claiming held-C07 "is the next probe" reads as a frontier-map defect.

## Finding 4 — PROVINCE.md pointer and content

- README :4 says "Province: `PROVINCE.md`" but the file is at **repo root** `/home/vgpnk/Projects/shokunin/revenger-shokunin/PROVINCE.md`, not under `corpus/`. Historical docs cite it the same way (e.g. `kaidoku-shokunin/PROVINCE.md:…` repo-relative), so the pointer is a repo-relative convention, not a defect — noted for completeness only.
- PROVINCE.md :3-8 owns "Android APKs… firmware" under shipped-artifact RE with evidence-ledger discipline — the C05 byte-readout sits inside the owned ground; no province conflict. `Refuses:` (:19-23) bars live-target execution/DRM/asset claims; the candidate's no-install/no-execution/manual-readout scope is compliant. No PROVINCE edits required.

## Finding 5 — other stale-adjacent text (non-blocking notes)

- Entry header `admission-status: candidate` (`round-65-apk-axml-byte-evidence.md` line ~9) must flip to the admitted marker on admission — in scope of the entry file, not README; flagged so the Q-gate seats/L1 pair the flips (entry text itself says the flip "is L1's").
- SOURCES rows S038 (:52), S039 (:53), S040 (:54, CPython zipfile docs), S041 (:55, own-work bundle naming all four fixture paths + sha256 `05d2280f…`) are appended and consistent with claims.md :129-132 and the build state.
- `## Frontier` C03 (:67-68), C08 (:71), custody (:72-74) bullets remain accurate; untouched.

## Open gaps / dependencies

- Whether L1 folds the C07 bullet fix into the admission commit or routes it as round-66 debt — an adjudication decision, not resolved by the frozen contract's text alone ("No other README row changes" names rows, not bullets; SCORECARD.md:454 names only the C05 prose refresh).
- The legend predicate for `frontier` ("no saved record") counts `live/runs` records only; the apk-r65 fixture is `fixtures/` work evidence, so under a strict reading C05 could arguably be `uncovered` already at candidate-landed state (fixture + unadmitted candidate exist). The frozen order (:112-114) deliberately keeps it `frontier` until the wave decides — consistent, since the flip lands in the admission revision. Not a defect; recorded as the legend-vs-order nuance.

No tools installed or upgraded; no writes outside this report; pacman untouched.

Report: .ufo/waves/round-65/R65ScoutFrontier.md
