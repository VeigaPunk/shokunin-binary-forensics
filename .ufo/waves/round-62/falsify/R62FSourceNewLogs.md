GRADE: PARTIAL — corpus/SOURCES.md round-62 `## Paths` + `## Search log` (new S028–S031 notes) at d977619

Frozen target: revenger-shokunin `d97761952be256d145d298022de03091de91d358` (claimbase `5bd4a90f`, pre-registration `a3498e25`). `git archive d977619 | sha256sum` = `4b52df49bbd6349d6ac8c45c4f7d73d9e7125c7f719950e89818cad21dc8cebc`; archived `corpus/SOURCES.md` sha256 `5c13831b8b64b1a2d715fc4031415750d92af4daf3ef8021c91a8912b5d66bbe` (byte-identical to live). Scratch `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FSourceNewLogs/`. No production edit; HEAD unchanged; `git status --porcelain` shows only pre-existing falsify dispatch files.

## HOLDS (verified)

1. **Aggregate 4 / 4 / 4 / 0 reconciles.** `SOURCES.md:66` "Identified 2, screened 2, included 2 rows (S028, S031), excluded 0."; `:67` "Same document-set unit: identified 2, screened 2, included 2 rows (S029, S030), excluded 0." → 2 = 2 + 0 each, 4 = 4 + 0 aggregate; matches `R62SourceLogPlan.md:48-51` "Aggregate S028–S031: 4 / 4 / 4 / 0 → 4 = 4 + 0 ✔". The 4 included rows are exactly S028–S031. **No double numbering**: each id occurs exactly 3× (`grep -o|wc -l` = 3 each) on distinct lines — registry row, one Paths bullet, one search note (S028:42,55,66 · S029:43,56,67 · S030:44,56,67 · S031:45,55,66); census duplicate-ids empty.
2. **Census clean; delta = 4 rows.** Baseline `a3498e25` → `rows 27 | tier.A 25 | tier.C 2 | mined 22 queued 1 rejected 4`; `validate` → `W04 S024` only, `ok`, exit 0. Candidate `d977619` → `rows 31 | tier.A 29 | tier.C 2 | mined 26 queued 1 rejected 4 | missing 0`; `validate` → `W04 S024`, `W04 S028`, `W04 S029`, `ok`, `VALIDATE_EXIT=0`. Malformed 0, enum violations 0, missing used-by 0. Diff `a3498e25→d977619` on `corpus/SOURCES.md` = 9 insertions / 0 deletions (pure append; rule 2 preserved — S016/S022/S026/S027 used-by byte-identical to baseline).
3. **Stop rationale scoped to the new entries.** `:66` "byte-boundary definitions and the selected primary byte/record inputs cover the narrow entry scope."; `:67` "semantic roles plus the source/record data cover the narrow correspondence claim; no Node loader, Electron-role or export-binding claim is proposed." Neither claims coverage of the rejected round-61 entries.

## F1 (High) — 404 / additional-HTTP-doc treatment inconsistent inside one Search log section

`:67` counts two 404 URL attempts as **excluded 0**: "two guessed short-form mirror URLs returned 404 and were discarded unopened, not counted as opened source sets." The **same commit's** third new note `:68` counts an unopened 404 attempt as identified *and* excluded: "C04 corrected identified 11, screened 10, included 4 external rows plus own-work S027, excluded 6 opened documents plus one unopened 404 attempt." The round's own convention for that note is `R62DebtSearchLog.md:50` "a 404 guess is identified and screened out unopened, as the 2026-10-19 ISO 403 line did" — and the file's ISO line `:60` does count it: "Identified 8, screened 7 (ISO/IEC 27042 catalog returned HTTP 403, kept as a lead)". One file, one section, one commit → three different 404 treatments (`:60` identified; `:61` "excluded unopened"; `:67` excluded 0). `:67`'s `excluded 0` contradicts the convention its own sibling new note states and applies.
*Inference:* a reader reconciling "how many URL attempts, what became of each" gets mutually exclusive answers; `excluded 0` is not derivable under the convention the same commit states. Minimal correction: state the 404 rule inside `:66`/`:67` (or adopt `:68`'s); the counts need not change if the rule is declared per note.

## F2 (High) — opener/open accounting under-reports the actual build source opening reports

- `:67` credits "Openers: R62SourceEcma, R62SourceJsOwn, R62JsEntry; exact fetches/quotes in their build reports." But the round has **another** source-opening seat for the same documents: `R62SourceRevisions.md` (in `build-assignments.json` and `build-dispatch.json`), which opened tc39.es/ecma262/, `/2026/`, `/2027/` and the es2026 / es2026-errata tagged `spec.html` revisions. `grep -rn "SourceRevisions" corpus/ | wc -l` = 0, in `corpus/lessons/round-62.md` = 0 → **credited nowhere in corpus or lesson**.
- The two 404s `:67` names have **no opener record**: `grep -c 404 R62SourceEcma.md` = 0; its "Opened" list holds three 200-status URLs. The only occurrence is the seat that authored the note text, `R62SourceLogPlan.md:56-57` "plus two guessed short-form chapter URLs that returned HTTP 404 and were discarded unopened" — self-attributed, no URL, status line or digest.
- The one 404 actually opened against the ECMA document is `R62SourceRevisions.md:30` "/2027/ -> HTTP 404; git ls-remote --tags tc39/ecma262 | grep -c es2027 -> 0"; `/2027/` and `/2026/` appear **nowhere** in `corpus/` (`grep -rn "2027/" corpus/ | wc -l` = 0), and `/2026/` ("Draft ECMA-262 / March 31, 2026", sha256 `0119d5a2…`, `R62SourceRevisions.md:40`) is an opened document absent from `:67`'s Where clause.
*Inference:* the new Where / Additional-opens clauses are not a complete account of this round's ECMA and execution-specs opens. Minimal correction: name the opens (or fold them into the stated set) and credit the seat that made them.

## F3 (Medium) — S029 lands on S022's URL and quote ground; no disposition of the review

`R62ReviewSourcesContract.md` (in-round reviewer): "**S029 … — DO NOT MINT as reserved.** S022's scope already is 'evaluation of destructuring binding patterns and the separation of ImportDeclaration from scripts, this draft only' (§14.3.1.3, §14.3.3.3, §16.2.2, quote 'Set value to ? GetV(value, propertyName).'). A second row at that URL for that ground is a rule-4 duplicate plus a third W04. Instead re-open the draft this round … and append the C04 entry to **S022's** used-by; the lesson should record that the reserved id went unused." Landed: S029 exists at the same URL with the same §14.3.3.3 quote; `S022 => corpus/knowledge/commonjs-destructured-require-edges.md` is byte-identical to baseline (no used-by append); `grep -rn "DO NOT MINT\|rule-4 duplicate\|ReviewSourcesContract" corpus/` = 0 → no disposition anywhere. Census records the consequence as `W04 S029 duplicate url tc39.es/ecma262 across scopes` (exit 0, warning only). Also S029's anchor carries "§14.3.1.3 BindingEvaluation", but `grep -c "14\.3\.1" R62SourceEcma.md` = 0 (and 0 within the lesson's cited range `R62SourceEcma.md:12-39`); its only in-round derivation is uncredited `R62SourceRevisions.md:45`.

## F4 (Medium, adjacent column) — landed recheck contradicts the in-round revision analysis

`R62SourceRevisions.md:56-58` "Recheck `180d` … `on-release` is wrong for a tag-pinned scope"; `:61` "`on-release` alone never becomes due"; `:64` "recheck `90d` against the draft-date string and the three clause ids". Landed recheck: S028 `on-release`, S029 `on-release` (S030/S031 `90d`). The contradicting analysis sits in the uncredited seat (F2), so the contradiction is invisible in the corpus.

## F5 (Low) — two incompatible counting conventions coexist in one section, unreconciled

`:66` declares "Unit: one proposed registry document set, not one HTTP request."; `:68` declares "Document-level convention: revisions/anchors of the same document count once; own-work bundles are additional included registry rows; discovery APIs are not separate documents." *Inference:* under `:68`'s rule the round-62 numbers shift (own-work bundles leave identified/screened; API responses stop being documents), so 4/4/4/0 is valid only under the set-unit and is not comparable with the adjacent `:68` figures; neither note cross-references the other's convention.

## F6 (Low) — the plan seat's description of its own notes does not match the landed text

`R62SourceLogPlan.md:57-58` "Each note carries Query, Where, date, counts, **negative sweep**, Stop rationale and openers." Landed `:66`/`:67` carry **no** negative sweep — `grep -n "Negative sweep" corpus/SOURCES.md` hits only lines 61 and 63. Not a rule-5 breach on its own (neither new note makes a negative source claim), but the build report's account of the notes is inaccurate.

## Unknown / verification gaps

- `corpus/scripts/sources-census.sh` does not exist in this lane; the validator used was `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`, run on the archived copy only.
- No after-census record (rows 31 / W04 ×3) in `corpus/lessons/round-62.md` or the round-62 LOG landing, though `reports/round-62/claims.md:66` requires "record census before and after" (before: LOG.md:823 "Census ok exit0, same S024 W04"; after: absent). I measured it above; it is unlogged. Not scored (outside the assigned target).
- I opened no network source; every fact above is read from the committed tree or archived copy. Whether the two short-form 404 mirror URLs genuinely returned 404 is unverified by me.

## VERDICT

PARTIAL. The declared aggregate 4 identified / 4 screened / 4 included / 0 excluded is arithmetically correct, matches the 4 new rows, the census is clean (validate exit 0), there is no row double-numbering, and both stop rationales are scoped to the new entries. But 404 / additional-HTTP-doc treatment is inconsistent across notes landed in this very commit (F1); the opener and extra-opens accounting does not match the round's actual build source opening reports — one source-opening seat uncredited, two opened documents and one recorded 404 omitted, two 404s self-attributed without an opener record (F2); and S029 is minted over S022's quote ground with the in-round "DO NOT MINT" recommendation left undispositioned (F3). No repair and no admission performed; both candidate entries remain `uncovered` and uncounted. Installs or updates: none (no pacman/uv/npm/cargo transaction; read-only `git archive`, `grep`, `awk`, and the fleet census script on the archived copy only).

---

# Rereview — committed revision `47511b213bf556022869fa104a4bda9d7c9a3b95`

Rereview of the F1–F6 findings against the committed correction. Subject: revenger-shokunin
`47511b213bf556022869fa104a4bda9d7c9a3b95` ("round-62: preserve 64 fresh attacks and original drafts;
bounded Q11 corrections pending exact-hash independent re-review"), parent `d97761952be256d145d298022de03091de91d358`.
`git archive 47511b2 | sha256sum` = `daac8a90918a4994a4c5850bbf8fb8fc6d7dd2b9b8337cbecf0909115935667d`;
tree hash `45f00420d18f57a52fc7f08e79a14ceff59d8446862338d65ed2e638b68a4c96`; `corpus/SOURCES.md` sha256
`e517ec939b820c3e4d3c982aa015a7cde496f7174f869d8633d66423d8639139`, `corpus/lessons/round-62.md` sha256
`3553e21a1620cd3207b5dc9ba8ca98adf87e42bfc137ef12f5a6127f29ec1c5f`. Read-only; scratch
`/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62FSourceNewLogs/rereview/`. No edit, no new source claim, no admission.

**Scope of the change (verified).** `corpus/SOURCES.md` differs from `d977619` by exactly two hunks: the S026
row's `used-by` cell, and one appended note at `:69` inside `## Search log` (`:58` section → `:71` `## Leads`).
`:66`, `:67`, `:68` are byte-identical to `d977619` (per-line `diff` = IDENTICAL) — the earlier notes are
preserved, not rewritten. Row-level: exactly one old row touched (`grep -cE "^[-+]\| S[0-9]"` = 2 = S026 old+new);
field-by-field comparison of the 13 cells shows **only the `used-by` cell changed** (scope/anchor/teaches/status/
recheck/opened identical) — rule-2 legal. The lesson logs the old→new pair: "`corpus/knowledge/evm-saved-interface-
candidates.md` → that same retained path plus `corpus/knowledge/round-62-evm-dispatch-byte-evidence.md`,
`corpus/lessons/round-62.md`". All three targets exist; census `validate` → `W04 S024`, `W04 S028`, `W04 S029`,
`ok`, exit 0; `rows 31 | tier.A 29 | tier.C 2 | mined 26 queued 1 rejected 4 | missing 0`. README C04/C09 remain
`uncovered`; both candidates remain `admission-status: candidate`.

**F1 (404 / additional-HTTP-doc treatment) — RESOLVED.** The appended `:69` note now states the rule inside
the Search log section: "Failed URL attempts are excluded before the source-set count, with their reported
dispositions retained here rather than called successful sources." That is the minimal correction I named
(state the 404 rule inside `:66`/`:67`); the counts need not change, and did not. `:68`'s document-level convention
is untouched and now reads alongside an explicit statement that the two units differ.

**F2 (opener / extra-opens accounting) — RESOLVED.** `:69` names the missing seat and its opens: "Additional
opener R62SourceRevisions opened /2026/, es2026/es2026-errata versions and recorded /2027/ HTTP404; these belong
to the S029 specification-version set, were not selected as extra authorities, and were omitted from the earlier
opener list." `grep -rn "SourceRevisions" corpus/` = 2 hits (SOURCES.md:69, lesson:177) — the seat is now credited.
The two short-form 404s are now labeled as unverified rather than asserted: "The two short-form mirror 404s were
self-reported by R62SourceLogPlan without complete URL/status receipts and are unverified here." `/2027/` and
`/2026/` now appear in corpus. This matches my F2 evidence exactly (`R62SourceEcma.md` 404-count = 0; the only
404 receipt is `R62SourceRevisions.md:30`).

**F3 (S029 over S022; undispositioned duplicate-row objection) — RESOLVED as a decision, with one nit.**
`:69` records the disposition: "S029 was retained as a scoped companion after considering R62ReviewSourcesContract's
duplicate-row objection, not as discovery of a new document." Lesson:185-187 repeats it and adds "it does not
supersede S022 or claim discovery of a new document." The objection is now dispositioned rather than silent, which
was the defect I raised; S022's `used-by` is unchanged and still lists only the round-61 entry, so the reviewer's
preferred used-by append was *not* adopted — a deliberate L1 choice, now disclosed. **Nit (unresolved):** S029's
anchor cell still carries "§14.3.1.3 BindingEvaluation" while the lesson's S029 pointer remains
"`R62SourceEcma.md:12-39`" (`grep -c "14\.3\.1" R62SourceEcma.md` = 0, incl. in that range). The label is
nonetheless derivable from a committed byte: `.ufo/waves/round-62/source-snapshots/ecma-statements.html` contains
"14.3.1.3</span> RS: BindingEvaluation" (1 match), so the value is snapshot-backed but the lesson's stated
derivation pointer still does not reach it. Non-load-bearing (the candidate entry uses only the §14.3.3.3 quote),
so I do not treat it as a break.

**F4 (recheck cadence) — RESOLVED as a disclosed choice.** Lesson:190-193: "Recheck choices are legal cadences, not
claimed drift-detection capabilities: 90d for the fixed saved-data sources, on-release for the specification
re-opens. The revision scout's preference for periodic pin checks is retained as a recommendation, not a completed
freshness fix." That answers my F4: the values are legal cadences, no drift-detection capability is claimed, and
the contrary recommendation is retained openly rather than dropped. My earlier point that the contradicting analysis
sat in an uncredited seat is also cured by F2's disposition (the seat is now credited).

**F5 (two incompatible counting conventions unreconciled) — RESOLVED.** `:69`: "The 4/4/4/0 total counts proposed
registry document sets, including own-work sets; it is not an HTTP-attempt total and is not comparable with the
historical external-document counts." The non-comparability is now stated in the file rather than left to inference.

**F6 (plan seat's description of its own notes inaccurate) — PARTIALLY RESOLVED; nit remains.** The inaccuracy was
in `R62SourceLogPlan.md:57-58` ("Each note carries … negative sweep …"). That build report is an immutable
wave artifact and was **not** rewritten (correctly so — build reports are historical). But `grep -rn "negative sweep"
corpus/` = 0 at this revision: neither `:69` nor the lesson records that the landed `:66`/`:67` carry no sweep, so
the discrepancy between the plan seat's self-description and the landed notes is still undispositioned in the corpus.
Low severity (no negative claim is made by either note, so rule 5 is not breached), but it remains an open nit.

**Additional dispositions I checked (not part of F1–F6, credited to other seats).** `:69` also withdraws the S024
historical stopping-event attribution and corrects the REA main/tag reason to "incomplete, not wholly false: the
producing tag was also opened" — verified against the round-61 report `SrcReaEvmDocs.md:23` ("Tag files:
`rea-agents-6.4.0` HTTP 200 … `rea-agents-6.7.0` HTTP 200 … byte-identical"). The lesson adds that the S026
re-open is for "literal saved metadata scope; it is not evidence of actual producer origin", with the located quote
`"evmole@0.9.3"` verified present in `corpus/live/runs/round-19/inspection.json` (1 match). The new C09 entry's
`source:` header now cites S026 for the recorded metadata ("recorded metadata and identifiers below are that row's
scope, not S031's") — consistent with the S026 used-by append. The lesson also states the M27 precision correction
("the old C04 **Python block**, not the entire old entry, printed no span-location derivation") and that "No lexical
token inventory is treated as a Q11 pass." These are outside my lane's F1–F6; I verified only that they are recorded
and do not contradict the committed bytes.

**Still-open verification gaps (carried, both outside the graded target).**
- After-census still unlogged: `grep -c "rows 31\|W04" corpus/lessons/round-62.md` = 0 and the new LOG section
  adds no census line, though `reports/round-62/claims.md:66` requires "record census before and after" (before:
  LOG.md:823). I measured the after-state (rows 31, tier.A 29, W04 ×3, validate exit 0) and it remains unlogged.
- `corpus/scripts/sources-census.sh` still does not exist in this lane; the validator used was
  `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh`, on the archived copy only.

## REREVIEW VERDICT

**GRADE: HOLDS (nits: 2 open, 0 material).** All six findings are dispositioned in committed bytes: F1, F2, F4 and
F5 by the appended `:69` clarification plus the lesson's `### Source-log and mistake precision dispositions`;
F3 by the recorded L1 decision to retain S029 as a scoped companion after considering the duplicate-row objection.
The 4/4/4/0 totals, the four new rows, the absence of row double-numbering, the stop rationales and the census
result (validate exit 0) all survive the correction unchanged, and the change is append-only with a single
rule-2-legal `used-by` edit whose old→new pair is logged. Two low-severity nits remain open and are recorded here
rather than treated as breaks: (N1) S029's anchor retains "§14.3.1.3 BindingEvaluation" while the lesson's cited
derivation range does not contain it (value is snapshot-backed; pointer imprecise, non-load-bearing); (N2) the
plan seat's "each note carries … negative sweep" self-description remains undispositioned in the corpus. Neither
affects a counted value, a row, or an admission. No edit performed, no new source claim, no admission; both
candidates remain `admission-status: candidate` and README C04/C09 remain `uncovered`. Installs or updates: none
(read-only `git archive`, `grep`, `awk`, `diff`, and the fleet census script on the archived copy only).
