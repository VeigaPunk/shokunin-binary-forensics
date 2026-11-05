# ConnectorR92Overlap — round 92 wave 1 report

Full evidence: `.ufo/waves/round-92/w1/ConnectorR92Overlap/overlap.md` (sibling hit table with verdicts, commands, collision list). Read-only; nothing edited in any sibling; the merge package was not executed.

## Findings

1. **C03 (managed) sibling overlap.** Kaidoku holds the same artifact class and REA verb (`inspect-managed-artifact`, dnfile/dncil IL method) in `corpus/knowledge/2026-10-13-managed-assemblies.md`, `2026-10-13-r4-11-managed-unlock.md`, `2026-10-13-r4u-04-dnfile-il.md`, `2026-10-13-pe-surface.md`, and in its PROVINCE. Adjacent (host artifacts vs authored fixtures), not a duplicate row.
2. **C08 (browser/Electron) sibling overlap.** Tabi owns CDP session discipline (about 40 knowledge files, `PROVINCE.md`); kaidoku owns CDP runtime observation and Electron ASAR analysis. Province-level overlap; C08 must be scoped to the lane's own browser-r77 record (S447).
3. **ECMA-335 ownership.** Lane S136 is the only ECMA-335 registry row in any repo (PDF URL). No sibling registers it; kaidoku cites it in prose without a row. A new C1 row for the same PDF duplicates S136 (W04 duplicate-URL class). Landing-page rows (staged S057/S146) are a standard-level duplicate. The frozen "opened this round" wording conflicts with the append-only registry contract (`opened` cannot change in place); the L1 must reconcile.
4. **Cross-repo URL duplicates.** Lane S299 == tabi S002 (CDP index); lane S297/S298 == kaidoku S012/S014 (Electron fuses, ASAR integrity); lane S009 == kaidoku S100 and S102 (PE format, a kaidoku-internal duplicate).
5. **considerthese proposal 1 (command run exactly as given).** Kind: `book=6 docs=108 talk=3 dataset=17 community=22 spec=66 paper=61 tool=118 code=34 own-work=55 total=490`. Tier: `A=441 B=21 C=28`. Own-work share, whole registry: 55/490 = 11.2 %. Window (opened ≥ 2026-11-01): 48 rows, own-work 39 (81.2 %). The 2026-11-04 file's "51 of 479" figure is stale and not reproduced.
6. **Merge collision.** Staged `SOURCES.append.md` (155 rows, S047–S201) against the lane registry (490 rows, S001–S490): 155 shared ids (`comm -12`), 0 staged-only ids, 0 identical rows, 3 primary-URL collisions (S147=S009, S089=S136, S056=S045/S048). Adoption closed this round; nothing adopted.

## Defects and limits

- No defect in any frozen file was found in this seat's read.
- Lexical-only sibling hits (M7, B5-type term collisions) were not opened; they are marked unverified in overlap.md.
- No checks were run beyond read-only greps, counts and `comm`; no sibling script was executed.

## Tools

None installed. Scratch `$HYAKU_SCRATCH/revenger-r92/ConnectorR92Overlap/` used for URL extraction and removed before yield.
