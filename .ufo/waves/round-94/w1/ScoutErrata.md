# Round 94 — ScoutErrata report

Seat: `ScoutErrata` (registry role `scout`). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Tip under test: `060a8e87d6de6b31f91b58524ab0fcad88ae5431`. Read-only seat — no lane file
edited, no git/jj write command run, no SOURCES.md row created or changed.

Scope: cite-back and erratum-pin sweep for the frozen C1 claim's entry
(`corpus/knowledge/round-72-tool-landscape.md`).

Full table: `.ufo/waves/round-94/w1/ScoutErrata/cite-back-sweep.md`.

## What was checked

1. **S-id extraction.** Whole-entry collection with the counter's own rule
   (`\bS\d{3,}\b`) yields **48** distinct sids. The task's expected 46 are the ids with a
   `corpus/SOURCES.md` row at the tip; the extras are `S498`/`S499`, this round's two new
   drift-check rows that the frozen claims' §2b says the L1 appends at landing.
2. **Cite-back truth, 46 rows.** For each sid the `used-by` pointer was resolved to
   **committed** bytes at the tip (`git show HEAD:<pointer>`) and searched with a
   word-bounded pattern. The census only tests pointer *existence*, so a pointer whose bytes
   never name the sid would be drift (r86 sweep class M42).
3. **Erratum pins.** `S427` and `S428` were re-fetched at the URL/revision named in each
   row's anchor cell and each row's quote was located in the fetched bytes.
4. **Digest reproduction.** The normalised-entry sha256 was recomputed independently of the
   counter.

## Results

- **Cite-back: 46 OK / 0 drift.** Every `used-by` pointer's committed bytes name their sid.
  No r95 rule-2 pointer drop is proposed.
- **`S498` / `S499`: ROW-ABSENT** at the freeze tip — the expected pre-landing state, not
  drift. Landing precondition for the frozen `C1_SOURCES` leg: `status=mined`, `tier=A`,
  `opened=2026-11-05`, `used-by` containing `knowledge/round-72-tool-landscape.md`.
- **`S427` quote — located yes**, pinned README line 5:
  `… 118 repos, each one read and security-graded by [Agent Skills Hub …]`.
  Cross-check: the old `S071` anchored phrase `Each repo is read and security-graded` is
  still **absent** from the pinned README, so the r73 supersession is still needed and the
  erratum's wording is still accurate.
- **`S428` quote — located yes**, `arxiv.org/abs/2403.05286v3` abstract element at line 124
  (also in `og:`/`twitter:` meta at lines 30 and 34):
  `… traditional tools like Ghidra often produce results that are difficult to read and execute.`
  Cross-check: the old `S082` anchored behavioral-deviation sentence is still **absent** from
  the LLM4Decompile v3 abstract page, so the erratum's "that sentence belongs to
  AutoDecompiler (S083)" still holds.
- **Erratum section byte-identical**: `## Round-73 source-attribution erratum` is 771 bytes and
  identical at the tip and at the round-93 base `9876cb38`; introduced by `d4ab332`, unchanged
  since. The frozen "erratum section stays byte-identical" claim holds.
- **Supplementary (authorised REA URLs only).** Re-checked the two pending new rows' declared
  scopes against the pinned revision `0cd7ef45…` and at `main`: the S498 scope sentence
  (native binaries / JavaScript / Electron / .NET / websites / evidence / limitations, plus the
  `How REA works` heading) and the S499 approval-boundary sentence (`Setup previews
  configuration changes and asks for approval before applying them.`, installation.md line 4)
  are present at both revisions. **No scope drift observed.**

## Digest (vote binding)

```
01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3
```

Reproduced from the worktree entry and from `git show 060a8e8:…` after normalising every
`^admission-status: (candidate|admitted|rejected)$` line to `admission-status: candidate`.
The file carries exactly one `admission-status:` line, value `candidate`, at line 11 — inside
the 15-line header window. The counter prints the same digest
(`C1_VOTES=votes dir missing digest=01d5105…`) and it is in
`.ufo/waves/round-94/w1/ExecFrozen/freeze-state-digest.txt`.

**Every vote file for round 94 must carry**
`"candidate_sha256": "01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3"`.

## Not verified here / left to owners

- `S498`/`S499` `corpus/SOURCES.md` rows (L1 owns SOURCES.md; this seat did not create them).
- `reports/round-94/quote-receipts/` (absent at the tip) — the `C1_QUOTES` leg's receipts
  (L1/ExecReceipts own these).
- The `C1_VOTES` leg itself (votes do not exist yet at the freeze tip; expected).

## Bounds honoured

Wrote only `.ufo/waves/round-94/w1/ScoutErrata/cite-back-sweep.md` and this report file.
Scratch `/fast/scratch/hyaku/revenger-r94/ScoutErrata` created with `mkdir -p`, used with
absolute paths, and deleted before this report. Network limited to the two pinned r73 erratum
URLs and the two `github.com/morluto/rea` raw files named by the task/entry. No sudo, no
sysctl, no pacman, no installs, no lane/fleet writes, no subagent dispatch.
