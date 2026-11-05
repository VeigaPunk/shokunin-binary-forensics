# ScoutS136 — round 93, routed defect 4: the S136 supersedes correction row

**Axis:** calibration. **Lane:** `/home/vgpnk/Projects/shokunin/revenger-shokunin`
(freeze commit `02050cb2a6758e3bd9cec696ff0e42df6f23511a`).

## What I produced

1. `.ufo/waves/round-93/w1/ScoutS136/supersedes-draft.md` — the drafted row text
   (S497), the fetch receipt, the located quote with its line number, and the
   lane-tool self-check outputs.
2. `.ufo/waves/round-93/w1/ScoutS136/Ecma-335-Augments.md` — the fetched body,
   committed as evidence (69577 bytes, sha256 `1e6e225aa41cd1ccf957b3c13ec4682fc6be2265327c3632f2e8fa01279b0828`).
3. `.ufo/waves/round-93/w1/ScoutS136/quote-receipts/S497.receipt.json` +
   `quote-receipts/raw/S497.body` — a `revenger-quote-audit-v1` receipt
   (verdict `verified`, span 39–115) for the lane's own quote auditor.

Nothing outside my wave dir was written: `corpus/SOURCES.md`, `corpus/README.md`,
`corpus/knowledge/**`, `reports/round-92/**`, `reports/round-93/**` and the
fleet-root files are untouched (`git status --porcelain` shows only
`?? .ufo/waves/round-93/`). No mutating git/jj command was run.

## The row

Id **S497** — the registry maximum is S494; `claims.md` reserves S495 (round-77
CDP record) and S496 (CDP doc) for the sibling scout seat ScoutRecord, which it
confirmed by message, so S497 is the first free id after them. 11 columns, no `|`
inside any cell, `kind docs`, `tier A` **for the addendum's own scope only**,
`teaches` opens exactly `supersedes S136 —`, `status mined`, `opened 2026-11-05`,
`recheck 180d`, `used-by —`.

## Fetch evidence (this round)

- URL (pinned): `https://raw.githubusercontent.com/dotnet/runtime/b22bfee2010118c58ae143c3b8a1aaee3d0c8c4c4/docs/design/specs/Ecma-335-Augments.md`
- HTTP **200**, 2026-11-05, 69577 bytes, sha256 `1e6e225a…`; blob at that commit
  `6a929a15f286e5c0f95e92050d7eece7e819fddf`; commit authored 2026-10-18T00:55:49Z.
- `…/main/…` returns byte-identical bytes; identical to the r92 snapshot
  `.ufo/waves/round-92/w1/ScoutR92Managed/snapshots/Ecma-335-Augments.md`.
- Located quote (14 words): "This is a list of additions and edits to be made in ECMA-335 specifications." — **line 3** of the saved body, chars 39–115, byte-exact slice.

## Self-checks run (lane tools, on a scratch copy — the lane file untouched)

- `audit_source_quotes.py verify --sid S497` → `S497 terminal=S497 state=verified (ok)`,
  `SUMMARY rows=1 verified=1 unreachable=0 unresolved=0`, exit 0.
- `audit_source_quotes.py chains --range 130-140` → `S136 -> S497`, `TERMINALS=11/11`.
- Registry census on the scratch copy: 495 rows, malformed 0, duplicate ids none,
  enum violations none, mined rows with missing `used-by` path none.

## Defects / discrepancies found (no frozen file was modified)

1. **The task brief's background URL is wrong.** It says r92's scout opened
   `https://github.com/dotnet/ecma-335/blob/main/docs/Ecma-335-Augments.md`
   (HTTP 200, blob `6a929a15…`, commit `b22bfee2`). The repo `dotnet/ecma-335`
   does not exist: `github.com/dotnet/ecma-335`, its `/blob/main/…` page, and the
   GitHub API for the repo/commit/tree all return **404**. The blob sha and
   commit in the brief are real but belong to **`dotnet/runtime`**, path
   `docs/design/specs/Ecma-335-Augments.md` — which is the URL the r92 scout
   actually recorded (`ScoutR92Managed/sources.md:176`) and the URL S136's own
   scope cell names. My row uses the verified `dotnet/runtime` URL.
2. **S136's scope cell points at a LEADS line that does not exist.** It says the
   addendum is "unopened — see LEADS", but the `## Leads (unopened)` section
   (lines 589–596) has no bullet about the addendum — the pointer is dangling.
   The new row supplies the rule-2 correction the r92 spot-check demanded.
3. **Receipt location vs counter expectation.** `c1_k_admit_counter2.py` reads
   receipts from `reports/round-93/quote-receipts/`, while both scout seats wrote
   theirs under their wave dirs (`ScoutS136/quote-receipts/S497.*`,
   `ScoutRecord/quote-receipts/S496.*`). The L1 must copy both into
   `reports/round-93/quote-receipts/` (with `raw/`) or the C1_QUOTES leg cannot
   see them.
4. **`status mined` with `used-by —`** is unique in the registry (every other
   `mined` row names a citing path). SOURCES rule 1 puts the round-93 lesson's
   `## Gate` in charge of citing the new row, so the L1 should set
   `used-by corpus/lessons/round-93.md` when it lands that lesson.
5. **Chain effect of the correction.** `supersedes S136 —` makes S497 the terminal
   of S136 in `audit_source_quotes.py` chains. No S136 receipt exists anywhere, so
   nothing regresses; landing the S497 receipt keeps S136-scoped verification
   resolvable.

## Tooling

No tool was installed or upgraded (nothing needed installing; `curl`, `python3`
and the lane's own scripts sufficed). `curl` and the GitHub REST API were used
read-only for the fetch and the commit/blob pinning.
