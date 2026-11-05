# SOURCES append block — round 94 (S498, S499)

Seat `ScribeLesson`. These are the **two rows to append** to `corpus/SOURCES.md` in the
revenger lane. Nothing else in `corpus/SOURCES.md` changes: append-only, and no existing
row's `status`, `recheck` or `used-by` cell is edited in place this round.

## Append point

Append **inside the `## Registry` section**, immediately after the last existing row
(`| S497 | …`) and before the `## Paths` heading (line 516 at the freeze tip
`060a8e87d6de6b31f91b58524ab0fcad88ae5431`). The rows are row-shaped Markdown; they must
not land outside the `## Registry` section (`E12` in the census).

## The two rows

```markdown
| S498 | REA root README, drift-check re-open — https://raw.githubusercontent.com/morluto/rea/main/README.md (docs, tier A, opened 2026-11-05) | docs | A | the REA repository's own declared inspection scope re-opened read-only at main commit fe677f6cf9853fb12490dfb8ef23ccae3a551049 on 2026-11-05 as a drift check of S054's scope cell: the same binary, application and runtime inspection families and the same evidence-and-limitations boundary; not tool capability, host readiness, tool accuracy or completeness | README.md overview paragraph, line 65 at main commit fe677f6cf9853fb12490dfb8ef23ccae3a551049 (2026-11-05); body 30064 bytes sha256 cb5b40c5752a403fbe20be9af2c08b5ca915c033af142f6f57af227cbaa2b6ba; the same bytes are served at the pinned commit URL https://raw.githubusercontent.com/morluto/rea/fe677f6cf9853fb12490dfb8ef23ccae3a551049/README.md — "REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and websites." | drift-check result: no drift — the 2026-11-05 re-open of S054's source at main commit fe677f6c… found the declared scope unchanged (same inspection families, same evidence-and-limitations wording, same 38-row family table), so S054's scope cell still describes the current README and the r72 tool-landscape role table still rests on that scope; the added Kuna native-analysis engine name is a provider addition inside an unchanged family | mined | 2026-11-05 | on-release | corpus/knowledge/round-72-tool-landscape.md |
| S499 | REA installation and setup docs, drift-check re-open — https://raw.githubusercontent.com/morluto/rea/main/docs/installation.md (docs, tier A, opened 2026-11-05) | docs | A | the REA setup documentation's own setup-preview and approval statements re-opened read-only at main commit fe677f6cf9853fb12490dfb8ef23ccae3a551049 on 2026-11-05 as a drift check of S075's scope cell: the preview-then-approve ordering and the approval boundary on configuration changes; not evidence of installation or readiness on this host | docs/installation.md lead paragraph, line 4 at main commit fe677f6cf9853fb12490dfb8ef23ccae3a551049 (2026-11-05); body 115812 bytes sha256 f05249e642a40562e8f2f1eee8ec23d56401f4b5884ba665c02f9730d8de2267; the same bytes are served at the pinned commit URL https://raw.githubusercontent.com/morluto/rea/fe677f6cf9853fb12490dfb8ef23ccae3a551049/docs/installation.md — "Setup previews configuration changes and asks for approval before applying them." | drift-check result: no drift — the 2026-11-05 re-open of S075's source at main commit fe677f6c… found the approval statement byte-identical at the same span and every approval heading unchanged, so S075's scope cell still describes the current installation docs and the r72 tool-landscape setup row still rests on that scope; the revision adds approval-adjacent detail (unattended --yes approval route, pre-approval macOS version check, dry-run approval path, readiness-check table) but never bypasses the approval boundary | mined | 2026-11-05 | on-release | corpus/knowledge/round-72-tool-landscape.md |
```

## Row facts (why each cell is what it is)

| cell | S498 | S499 | basis |
|---|---|---|---|
| kind | `docs` | `docs` | the registry's `kind` enum; the re-opened sources are the project's own documentation |
| tier | `A` | `A` | primary/authoritative for the declared scope — the project's own README and installation docs at a pinned commit |
| status | `mined` | `mined` | both are cited by `corpus/knowledge/round-72-tool-landscape.md` (its `source:` header lines) |
| opened | `2026-11-05` | `2026-11-05` | the access date of both re-opens |
| recheck | `on-release` | `on-release` | symbolic cadence — the re-check belongs to the next upstream release, matching the sibling rows S054/S075 |
| used-by | `corpus/knowledge/round-72-tool-landscape.md` | `corpus/knowledge/round-72-tool-landscape.md` | the citing entry; the path is repo-relative and exists on disk (`E11`-clean) |

**Scope of the claim.** Each row is a *drift-check re-open* of an already-registered
source (S498 → S054, S499 → S075) at `main` commit
`fe677f6cf9853fb12490dfb8ef23ccae3a551049` on 2026-11-05. Both scope cells say what the
re-opened document's own text establishes and what it does not. Neither row supersedes
an older row: the drift check found **no drift**, so no older scope cell is corrected
and the contract's rule-2 `supersedes S0NN —` form does not apply.

**Both `teaches` cells state the drift-check result explicitly** — the row's one grounded
learner benefit is the drift verdict plus the boundary it preserves. Two variants were
drafted (no-drift and drifted); the scout's verdict is `no-drift` for both rows
(`.ufo/waves/round-94/w1/ScoutReopen/drift-verdicts.md`, independently corroborated by
`ExecReceipts` on byte-identical re-fetch), so the **no-drift variant is the one
appended**. The drifted variant is recorded below for the L1's reference only — it is
**not** appended, because appending it would assert a drift finding the receipts do not
support.

## The not-appended drifted variant (reference only — do NOT append)

If a future re-open of the same two sources *does* find drift, the drifted `teaches` text
for each row is the following. These are **not** part of the append block above.

- S498 (drifted): `drift-check result: drift — the 2026-11-05 re-open of S054's source at main commit fe677f6c… changed the declared scope (the scope sentence and the family table are no longer byte-identical to the S054 anchor), so S054's scope cell no longer describes the current README and the r72 tool-landscape role table must be re-grounded against the new text`
- S499 (drifted): `drift-check result: drift — the 2026-11-05 re-open of S075's source at main commit fe677f6c… changed the approval statements (the located sentence is no longer byte-identical to the S075 anchor), so S075's scope cell no longer describes the current installation docs and the r72 tool-landscape setup row must be re-grounded against the new text`

## Validation performed on these exact bytes

- `awk -F'|' 'NF!=13 {print NR}'` over the two lines → **prints nothing** (each row has
  11 cells → `NF=13` under the census's parser, which counts the leading and trailing
  empty fields).
- No literal or escaped `|` inside any cell (checked cell by cell).
- The located quotes are ≤25 words: S498 = 18 words, S499 = 11 words.
- The located quotes are byte-identical to the receipt quotes and appear at the recorded
  spans in the committed bodies (re-verified: `body[s:e] == quote`, body sha256 matches
  `fetch_sha256`, body length matches `length`, for both sids).
- Full census dry-run on a scratch copy of the lane tree with these two rows appended:
  **exit 0, 21 W01 + 13 W04, 0 E**, 499 rows — the same W/E counts as the freeze tip and
  no new warning from the appended rows.
- Full frozen-counter dry-run (`reports/round-94/c1_k_admit_counter3.py --tree …`) on a
  scratch tree with these two rows appended, the C15 row flipped to `held`, and the
  entry's status line flipped to `admitted`: `C1_SOURCES=pass`, `C1_QUOTES=pass`,
  `C1_C15_HELD=pass`, `C1_ADMITTED=pass`, `C1_ONLY_C15=pass`, `C1_LINT=pass`,
  `C1_EMBEDDED=pass`, `C1_EMBED_NONVACUOUS=pass`, `C1_K_HELD_BACKED=pass` (11/15),
  `C1_TRIO=pass`, `C1_C15_CITES=pass`, `C1_ROWS_TOTAL=pass`. The only failing leg in the
  dry-run was `C1_VOTES`, which needs ≥2 accepted vote files in `reports/round-94/votes/`
  — the L1's landing step, not this row set's.
