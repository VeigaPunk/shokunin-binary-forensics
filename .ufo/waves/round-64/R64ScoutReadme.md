# R64ScoutReadme — findings

Axes: complete enumeration (14/14), legend/evidence fidelity, zero production mutation.

## Result

**C07 is the only observed README row-token contradiction. Its token must be `uncovered` at this snapshot, not `frontier`; `held` requires the later independent all-criteria admission.** No contradiction was found for the other 13 rows. Current tokens: held 7, partial 3, frontier 4.

The complete 14-row table, including knowledge, saved-record and fixture observations for every row, is saved at:
`/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/scout-readme.md`.

## Direct evidence

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/README.md:21-26` defines frontier as no knowledge and no saved record; uncovered as work evidence without admitted knowledge. Line 36 currently marks C07 frontier with empty evidence cells.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py:55-60` maps C03 to `inspect_managed_artifact`, C05 to `inspect_android_package`, C07 to `inspect_firmware_regions`, and C08 to the three browser-runtime operations. Lines 63–75 inspect top-level saved-record operations and apply the frontier rule.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-63/inspection.json` directly parses to operation `inspect_firmware_regions`, Evidence `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`, provider Binwalk 3.1.0. It records zlib regions at 512 and 1024.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/fixtures/firmware-r63/` contains the binary, generator and truth file; truth records a 2048-byte image. No round-64 firmware knowledge file was present in the complete knowledge listing when audited.
- Literal operation-field search across all saved JSON found only that C07 file among the six registered ROW_OPS names. No matching managed, Android or runtime operation was observed. Complete fixture listing likewise showed no authored fixture on those three surfaces. Static JavaScript/Electron-role labels are not browser-runtime evidence.

## Historical admission trace

All seven held rows have an existing, scoped admitted entry, not merely an existing path:

- C01/C11/C12/C13: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-1.md:94-124` records admissions and the critic-driven re-gate.
- C04/C09: `/home/vgpnk/Projects/shokunin/revenger-shokunin/LOG.md:842-853` records independent exact-hash reviews and final admission; older retained candidates are explicitly rejected.
- C06: `/home/vgpnk/Projects/shokunin/revenger-shokunin/LOG.md:867-873` and `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-63-verifier-spotcheck.md:28` record the independent admission condition and authorized held flip. Its entry still has a stale `admission-status: candidate` header at line 8; that metadata inconsistency does **not** show that the later admission failed or make the README row contradictory.

C02/C10/C14 retain pre-contract knowledge and therefore fit partial despite existing work evidence. Held is existential: the admitted C04 and C06 scopes need not cover runtime, nested archives or duplicate-entry behavior.

## Confidence and remaining unknowns

**High confidence** in the 14-row source audit and C07 inference. Repository inventory/operation searches are bounded negative evidence, not universal proof of no possible work outside the lane. Final round-64 C07 admission is a future dependency not observed or awaited; this leaf supplies no admission verdict and makes no production edit.

LSP was unavailable: `xd://lsp` returned `No such tool`, listing only ast_edit/debug devices. ROW_OPS definition/use were traced by direct source reads; grep is literal fallback, not semantic language-server proof. The JSON selector could not parse the round-59 record's escaped lone surrogate; raw source supplied its operation/Evidence ID, and the tool issue was reported.

No provider, test suite or frozen counter was run; historical verification results are cited artifacts, not newly exercised checks. No Git/JJ operations, production edits, tool installations or other orchestration were performed. No scratch was created.

Report: .ufo/waves/round-64/R64ScoutReadme.md
