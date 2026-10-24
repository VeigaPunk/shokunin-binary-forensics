# R65ReviewEntryQ10 — Q10 + cross-lane review of the C05 candidate

PASS — Q10 holds: the finding is scoped to one authored fixture (947 B, sha256 `05d2280f…`), one operation (manual stdlib byte readout) and a digest/version pin; ADJ-06 is reported-not-absorbed with no sibling file cited as support; no provider readiness claim exists; only LOW pointer/precision findings below.

Seat: leaf reviewer, read-only. Target: `corpus/knowledge/round-65-apk-axml-byte-evidence.md` (162 lines, sha256 `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7`). Contract read in full first: `reports/round-65/claims.md` (C1 scope at `:28-31`).

## What I verified (commands + actual output)

1. **One fixture, one operation.** Entry `:11` — "One authored APK, `corpus/fixtures/apk-r65/fixture.apk` … The analysis is **manual** … Nothing is extracted to disk, nothing is executed, no producer is called, no network is used". Entry `:131` — "One authored fixture, one manifest shape …". No second fixture, no provider call, no batch scope.
2. **Frozen bytes match the build state.** `sha256sum corpus/fixtures/apk-r65/*` →
   `fixture.apk 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e`, `truth.json 27303bae…`, `generator.py eaa9444c…`, `readout.py 92e347c3…` — identical to the entry header `source: S041` anchors and to the wave build state.
3. **Readout reproduces.** `python3 -B corpus/fixtures/apk-r65/readout.py` → exit 0, 15 lines, stdout sha256 `507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247`, matching the header `recheck:` and `## Reproduce`. `--fact eocd` printed exactly item 2's values (`eocd_offset 925`, `offset_of_start_of_cd 737`, `size_of_central_directory 188`, `parsed_entries 3`, `cd_end_equals_eocd_offset true`).
4. **No provider run exists for this round.** `ls corpus/live/runs/` → rounds `57 58 59 6 63 7 8 9`; `find corpus/live/runs -maxdepth 1 -name '*65*'` → nothing. So entry `:135` "this lane ran no provider" is consistent with the saved-record surface.
5. **Q05 fence holds.** Provider appears only as (a) S039 documented-scope citation in the header and `:135`, (b) the coverage-map exclusion (`:6` "provider (`inspect_android_package`) readiness or output"), (c) `:127` "any provider's behavior is claimed" (negated), (d) the Q05 row `:145`. No readiness, presence, or capability assertion anywhere. Q05 row says "no readiness or capability claim is made", which is a legitimate pass under `corpus/QUALITY.md:17` (the criterion only fires on a readiness/capability claim).
6. **ADJ-06 reported, not absorbed.** Entry `:135` — "The kaidoku/revenger ADJ-06 overlap and fleet `l0-questions.md:42` remain reported-not-absorbed, unchanged from round 64." `grep -E 'kaidoku-shokunin|tsukuroi-shokunin'` over the entry → no sibling lane file is cited as support; no ownership sentence; no province text touched. Substantively a report, not an absorption.
7. **C1's declared disclaimers all appear somewhere in the entry.** install/signing → `:6`, `:127`; dex validity → `:131` ("intentionally not a valid dex program"), `:127`; provider completeness → `:6` ("readiness or output"), `:127`; authenticity → `:148` (Q09 row "no origin, completeness or authenticity claim").
8. **Build state consistent.** `corpus/README.md:34` still `| C05 | … | frontier |`; entry header `admission-status: candidate`. No premature flip (matches claims §Admission order step 3). `grep -rln 'C05 (' corpus/knowledge/` → only this entry, so the C05 ground has no competing admitted entry.

## Findings by severity

### LOW-1 — Cross-lane note asserts the disposition but does not name the contested sibling surface
Entry `:135` names "the kaidoku/revenger ADJ-06 overlap" generically and cites no sibling pointer. The actual contested surface for this row is live and specific: `kaidoku-shokunin/PROVINCE.md:56` lists **"APK surface (full)"** with `inspect-android-package` (jadx-headless-mcp 0.7.1), `decode-android-resources`, and the `REA_JADX_MCP_JAR` pin (`:26,:127`); the recipient remains unnamed per `tsukuroi-shokunin/PROVINCE.md:51` — "protocol integrator — kaidoku/revenger ownership unresolved".

The round-64 precedent named exactly these kinds of surfaces: `corpus/knowledge/round-64-firmware-region-byte-evidence.md:203` cited fleet `.ufo/l0-questions.md:42`, `tsukuroi-shokunin/PROVINCE.md:51`, kaidoku's firmware/archive surface and provider-pin registry lines. Round-65 says "unchanged from round 64" without citing that entry's §Cross-lane scope note, so a reader must reconstruct which surfaces are unabsorbed. This is report-completeness, not absorption — no sibling scope is claimed, so Q10's "reported, not absorbed" still holds. Recommended (non-blocking) delta: add the kaidoku `PROVINCE.md:56` APK-surface pointer and `:26`/`:127` provider-pin lines as explicit non-absorbed ground, plus the round-64 entry path for "unchanged".

### LOW-2 — `l0-questions.md:42` is unresolvable as written
Entry `:135` writes fleet `` `l0-questions.md:42` ``. `ls /home/vgpnk/Projects/shokunin/l0-questions.md` → `ls: cannot access 'l0-questions.md': No such file or directory`. The real file is `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md`, and its line 42 is the tsukuroi round-1 question: "… arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is rou…" — correct line, missing path component. Lane precedent writes "fleet `.ufo/l0-questions.md:42`" (`corpus/knowledge/round-64-firmware-region-byte-evidence.md:203`; `SHONEN.md:23`). `corpus/lessons/round-64-verifier-spotcheck.md:77` already routed "`l0-questions.md:42` ADJ-06 reference wording" as bounded LOW debt; this entry repeats the imprecision rather than closing it.

### LOW-3 — §Limitations is narrower than C1's declared fence; the Q10 row overstates it
C1 (`reports/round-65/claims.md:28-31`) declares "no install, signing, dex-validity, provider-completeness or authenticity claim". §Limitations (`:131`) states one fixture/manifest shape/UTF-8/no CDATA/nested/styles, ZIP_STORED with no data descriptors (split/spanned/compression unexercised), dex-header-only, and generalization. It does **not** itself name install, signing, provider or authenticity; those live in the front-matter coverage-map (`:6`), §Observation/inference/unknown (`:127`), Q09 row (`:148`) and the cross-lane note (`:135`). The entry-level fence is therefore complete, but the Q10 row basis `:149` ("the §Limitations and §Cross-lane scope note name what is not claimed") is a slight overstatement of what §Limitations alone says. Precision nit, not a missing fence.

## Residual risk

- The note's brevity relative to round 64 could be read as weakening the recorded non-absorption if the round-64 entry is not carried alongside; the disposition itself is intact.
- Any edit to `:135` or `:149` invalidates this Q10 decision and needs a fresh delta re-confirm (same rule as `corpus/lessons/round-64-verifier-spotcheck.md:77`).
- Nothing here blocks C1 admission: no absorbed sibling scope, no readiness claim, scope is single-fixture/single-operation, and the readout reproduces from committed bytes.

## Verification gaps

- No `lsp` device is mounted in this seat (`xd://lsp` → "No such tool: xd://lsp. Mounted devices: ast_edit, debug"), and Markdown corpus prose has no language server; all caller/pointer checks are text/line citations verified by `awk`/`grep` plus file reads, not semantic resolution. This is the recorded unavailability, not an empty cold result.
- I did not run `reports/round-65/measure.py` (outside this seat's Q10 remit; C2 and counter attribution are other seats' cards). I did re-run the entry's own frozen recheck, which is the only command the entry itself bets its values on.
- I did not re-derive truth.json's oracle fields beyond the digest match and `build_recipe.python_version` read ("3.14.8", determinism string "Byte-for-byte reproducible with the recorded Python version").

## Tool installs

None. No package manager or install was run (pacman host-wide pause respected); Python 3.14.8 was already present and used only as the readout interpreter.

## Verdict

**PASS** for Q10 and cross-lane scope. Three LOW findings (unnamed sibling APK surface, `.ufo/`-less `l0-questions.md:42` pointer, §Limitations narrower than the Q10 row's basis), none of which falsifies the scoping, the ADJ-06 report-not-absorb disposition, or the Q05 provider fence.
