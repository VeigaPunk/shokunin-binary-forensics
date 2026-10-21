RESULT: COMPLETE

Scope: old round-61 source-log bookkeeping only — W3SrcSearchLog F1–F6 plus the
round-61 build-seat record. Not a C1 entry, source row, gate, admission or README
change. Frozen tree `a3498e25ad87bf756288812d0ea7c474b09433c7`; only copies under
`/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62DebtSearchLog/` were used; no
lane edit, no git/jj mutation.

Frozen check
- `corpus/SOURCES.md` (66 lines) sha256 `aa7b07e12107ab9ef8f0933efd44cd7fcded2f7e5b3e186b2eee55e65bfaab58`,
  equal to the file W3 attacked (`W3SrcSearchLog.md:3`). The old bytes are
  unrepaired, so F1–F6 stand as findings, not history.
- Census over the frozen file: 27 rows; `mined=22 queued=1 rejected=4`; tier
  `A=25 C=2`; S016–S019/S026 mined, S020–S023/S027 mined, S025 rejected; all
  twelve S016–S027 carry `opened=2026-10-21`. W3 HOLDS (a)–(d) re-read and hold.
- `corpus/README.md:33,38`: C04 and C09 both remain `uncovered`. Nothing proposed
  here flips or pre-credits either row.

Inventory of defects (all re-checked against the frozen file and the named seat)
| # | Defect | W3 | Evidence |
|---|---|---|---|
| 1 | C09 line counts do not reconcile: six created rows plus two row-less exclusions against "Identified 7"; S026 sits inside the six while `:58` puts own-work outside its row count | F1 | `SOURCES.md:57-58`; reconcile output below |
| 2 | C09 Solidity "Units and Globally Available Variables" opened, tier-A row drafted, never rowed and never named in Where or exclusions | F2.1 | `SrcKeccakVsSha3.md:11,47`; absent from `:57` |
| 3 | C04 `cjs-module-lexer` and `merve` READMEs opened as supporting sources, no row and no exclusion | F2.2 | `SrcNodeCjsLexer.md:32-35`; absent from `:58` |
| 4 | C04 tag-6.4.0 `javascript-artifact-reconstruction.md` opened; seat says it supports C04's entrypoint mapping; filed family reason says not load-bearing | F2.3 | `SrcReaJsDocs.md:13,42-43` vs `:58` |
| 5 | C04 tag-6.4.0 `javascript-application-workflows.md` opened HTTP 200, never named anywhere in the note | new | `SrcReaJsDocs.md:13`; absent from `:58` |
| 6 | C04 guessed `docs/javascript-applications.md` returned 404; the search log records neither the attempt nor a screening reason | new | `SrcReaJsDocs.md:14`; absent from `:58`/Leads |
| 7 | C09 REA `docs/evm-bytecode.md` exclusion reason is false: tag 6.4.0 (and 6.7.0) were opened too, not only main | F3 | `SrcReaEvmDocs.md:23` vs `:57` |
| 8 | C04 ASAR reason is narrower than its seat: one admissible scope-limit sentence and a queued row draft are dropped; "fixtures are plain directories" is a fixture fact, not a source disposition | F4 | `SrcElectronAsarScreen.md:24,32-34` vs `:58` |
| 9 | S024 line has no identified/screened/included/excluded counts and no stop rationale; C09 Where names no Solidity page, omitting `metadata.html` (S019's page) and the units page | F5 | `SOURCES.md:59,57` |
| 10 | S019 anchors the moving `/en/latest/metadata.html`; the seat recorded `/en/v0.8.37..35/metadata.html` returning 200 with the same shape | F6 | `SOURCES.md:33`; `SrcSolidityMetadataTail.md:45`; `SrcSolidityAbiVersionPin.md:59-62` |
| 11 | C09 stop sentence names S016–S018, but S019 is also mined with `used-by corpus/knowledge/evm-saved-interface-candidates.md` | new | `SOURCES.md:57` vs `:33` |

W3 F2's "three sources" is four documents (the two READMEs are separate); the
build record adds a fifth (workflows). The proposed note counts documents.

Derivation (code + output)
`python3 -B /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62DebtSearchLog/reconcile.py`
```
registry rows: 27 | status mined=22 queued=1 rejected=4 | tier A=25 C=2
C09: 8 documents opened 200; 5 rowed; 1 faithful exclusion; 1 false/narrow; 1 unrecorded
C04: 10 documents opened 200; 4 rowed; 0 faithful exclusion; 2 narrow/family; 4 unrecorded; +1 unopened 404
C09 corrected: identified 8, screened 8, included 5 rows + own-work S026, excluded 3
C04 corrected: identified 11, screened 10, included 4 rows + own-work S027, excluded 6
S024 corrected: identified 1, screened 1, included 1 (S024 rejected), excluded 0 (discovery: https://www.rfc-editor.org/rfc-index.xml)
```
All 19 cited seat-report paths resolve (`exists=True`), and the opener lists on
`:57`/`:58` match the nine and seven build seats exactly. Counts are
document-level (revisions/anchors of one document count once; discovery APIs are
named but not counted; a 404 guess is identified and screened out unopened, as
the 2026-10-19 ISO 403 line did). Counting the ABI page's two revisions
separately would make C09 identified 9; the note states this alternative.

Proposed change (scratch, NOT landed)
- `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62DebtSearchLog/R62DebtSearchLog-correction-note.md`
  holds the complete append-only block for `## Search log`, targeting the three
  round-61 2026-10-21 notes and worded position-independently of the concurrent
  S028–S031 notes (append order is L1's call). It states the convention;
  corrects C09 to 8/8/5+S026/3, C04 to 11/10/4+S027/6, S024 to 1/1/1/0; names
  the units page, the REA tag opens, the two READMEs, workflows, the 404
  attempt and the ASAR scope-limit omission; and records the S019 anchor and
  C09 stop-set gaps as unresolved.
- It edits no old line, creates no row, changes no `status`, `used-by`,
  `## Paths` or README entry, and claims no admission. L1 decides whether to
  land it in `SOURCES.md` or carry the same block in the round-62 lesson.

Unknowns / gaps
- No web source was re-opened here; every HTTP/size/version fact is attributed
  to the named seat report, not re-derived.
- Counts are convention-dependent. The document-level convention is stated; the
  C09 revision-level alternative (9) is disclosed rather than hidden.
- Contract v1 defines no erratum form for `## Search log` prose; the proposal is
  an appended, dated, non-row block. That form is L1's call.
- S019's moving anchor cannot be fixed in place (rule 2 permits only `status`,
  `recheck`, `used-by`); a superseding row would be a registry change beyond
  this bookkeeping ticket. It stays recorded debt.
- The 404 attempt's "lead" status is left as an unopened attempt, not added to
  `## Leads`; that section is unchanged.

Installs: none.
