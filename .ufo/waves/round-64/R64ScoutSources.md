# R64ScoutSources — report

**Result: S036 is next unused; no binding zipfile-docs reservation. Confidence: high.**

Full evidence: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-64/scout-sources.md`.

- Literal registry search found 35 contiguous rows S001–S035 in `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:15-49`; no S036/S037 row. The only ≥S036 lesson mention is the explicit “next unused id S036” at `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-63-verifier-spotcheck.md:59`.
- Governing rules: `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:16,22,45-48`: a lead is never a row; ids are next-unused and never reused; rows require current-round opening and Gate evidence.
- The named build report explicitly says no zipfile id is reserved: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63SourceZipfileDocs.md:46-50,248-258,391-397`. Its retained template names S034, not S036. Zipfile was opened but excluded, with no registry row.
- The later S036 wording comes from `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/falsify/routed-debt.md:73,156-159` and `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/falsify/W2RoutedDebt.md:113-119`: an update of then-next-unused allocation, not an exception to the registry contract.

**Disposition [INFERENCE]:** first actual compliant registry append wins. Round-64’s REA guide S036 and own-work S037 fit the observed allocation; a future zipfile-docs row uses the next unused id at its own integration (S038 if those two land first without intervening rows). No source admission judgment made.

Remaining unknowns: eventual integration order and admission evidence, outside this id-space recon. No dependency blocks the finding. Evidence gathering was textual/documentary; no exported code/LSP semantic claim. No builds/tests/census run; no tools installed or updated; no production files, wave specs, registry, git/jj state, or index changed. Only the two requested reports were written.

Report: .ufo/waves/round-64/R64ScoutSources.md
