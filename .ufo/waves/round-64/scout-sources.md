# R64ScoutSources — source id-space recon

Axes: identifier correctness; documentary traceability; zero production-file churn.

## Finding

**S036 is the next unused registry id in the inspected working-tree snapshot. No zipfile-docs reservation blocks its use for the round-64 REA firmware guide. Confidence: high.**

The governing contract does not provide lead reservations. The operational disposition is **first actual, contract-compliant registry use wins**, not first mention in a lead, contingency template, lesson, or routed note. This disposition is an inference from the explicit rules below, not a verbatim contract phrase.

## Observed evidence

1. **Current allocation.** Literal search of `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md` with `^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|` returned the contiguous 35 rows S001–S035. The registry ends with S034 (APPNOTE local-header scope) at line 48 and S035 (saved round-2 archive ledger) at line 49. No S036 or S037 registry row was found.

2. **Lessons do not spend S036.** Literal search of `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons` for `\bS0(3[6-9]|[4-9][0-9])\b|\bS[1-9][0-9]{2,}\b` returned only `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-63-verifier-spotcheck.md:59`: “next unused id S036”. That is a routed narrative mention, not a registry row. The separate S036/S037 search over the registry and lessons likewise found only that lesson mention.

3. **Binding contract.** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:3` binds the frozen fleet contract. `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:16` states: “a lead is not evidence and never a row”. Line 22 defines ids as “the next unused; never reused”. Lines 45–48 require opening the source in the round that writes its row, with the round lesson recording URL, access date, and a located ≤25-word quote. Neither a lead nor a previously opened but excluded source creates a row or consumes an id.

4. **REA was explicitly a lead.** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md:77-82` is `Leads (unopened)`. Its firmware-guide bullet says “read by the scout, not yet a row; open it when the firmware family is claimed”. It carries no S-id.

5. **The zipfile build report did not reserve S036.** `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63SourceZipfileDocs.md:46-50` explicitly says no id is reserved for a zipfile-docs row. Lines 248–258 call its contingency row not needed and not to be landed; the retained future-use note and template actually name S034, not S036. Lines 391–397 repeat that the excluded docs have no row and no reserved id. Importantly, zipfile was opened and screened out, rather than literally remaining unopened; this still did not consume an id.

6. **Where the S036 wording arose.** `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/falsify/W2RoutedDebt.md:113-119` updates the template’s stale S034 suggestion because S034 and S035 subsequently landed; it identifies S036 as the then-next-unused id. `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/falsify/routed-debt.md:73` says a future zipfile-docs row “must take S036”; lines 156–159 repeat that forward-looking wording. The same line 73 says “no zipfile-docs row exists or is pending”. Thus the wording describes the allocation available at that snapshot; treating it as a perpetual reservation would contradict both the governing contract and the build report’s explicit no-reservation statement.

7. **Historical precedent agrees.** `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-63.md:143-158` records that excluding zipfile left S033 free for own-work, withdrew an earlier S034 reservation, and later updated the actual allocation to S032–S035. Actual rows, not contingency numbering, determined the next id.

## First-use-wins disposition

The opening order named in `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md:41-49,127-128` is consistent with the inspected registry: append the opened REA firmware-guide row as **S036**, then the opened firmware own-work bundle as **S037**, with the required Gate evidence. A later zipfile-docs row must receive the next unused id **when it actually lands**; if these two rows land first and nothing else intervenes, that would be **S038**, not S036. No historical row or frozen round-63 report needs editing to implement this interpretation.

## Bounds and remaining unknowns

This is documentary/textual evidence, not language-server semantic proof; no exported code contract was traced. Source quality, fresh opening evidence, Q01–Q13 admission, and eventual integration are outside this seat’s question and were not assessed. Future next-id availability depends on intervening actual registry appends; no unresolved prerequisite blocks this finding.

Only the two assigned round-64 report paths were written. No corpus/registry/lesson/spec/index/git/jj mutation; no builds, tests, or census execution; no tool installs or updates.
