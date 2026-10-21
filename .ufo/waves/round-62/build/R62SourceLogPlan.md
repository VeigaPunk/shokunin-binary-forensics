RESULT: COMPLETE

# R62SourceLogPlan — append-only `## Paths` / `## Search log` entries for S028–S031

Scope: the two SOURCES prose sections only (S028–S031 row texts come from the
four source seats; L1 inserts them). **No corpus byte edited.** No README row
flipped: C04 and C09 remain `uncovered`. No admission, no K count claimed. The
draft entries, the full 73-line command output and the census runs are scratch
files, not in this report.

## Behavior (scratch proposal for L1)

`…/RevengerR61-2.R62SourceLogPlan/SOURCES-append-proposal.md` (sha256
`2a224d01df27a37e552a9f7e5e165cbe1434ad721244edd5dd51cb75ebb0e4b7`): Insert A =
2 `## Paths` bullets after `SOURCES.md:50`; Insert B = 2 `## Search log` notes
after `SOURCES.md:59`; nothing else touched. Applied to a scratch copy for
validation only: `…/corpus/SOURCES-proposed-final.md` (sha256 `9eaf1c7f…`).

## Evidence (frozen scratch; full output in scratch `verify_out.txt`)

```
$ python3 -B verify_sources_028_031.py    # exit 0, 73 lines; sha256 14231daf…
S028 EQ 55: EQ = 0x14 | JUMPI 106: JUMPI = 0x57 | JUMPDEST 109: JUMPDEST = 0x5B | PUSH4 125: PUSH4 = 0x63
S028 runtime def line 22 | boundary 60: elif Ops.PUSH1.value <= current_opcode.value <= Ops.PUSH32.value:
S028 runtime 29-30 raw: "* The jump destination shouldn't be part of the data corresponding to" | '`PUSH-N` opcodes.'
   # the 13-word quote equals this only after stripping the docstring bullet marker "* "
S029 single-page 7629271 B sha256 06db92a8…f27d7f; q029a 4 occurrences (13.15.5.3, 13.15.5.6, 14.3.3.3 ×2)
S029 q029b 2 occurrences, both under 16.2.1.7 — Table 54 and adjacent Table 56
S030 js-r3 imports 3 total / 2 named (edge 4 'rot13', edge 10 'checksum') / 1 unnamed (edge 9)
S030 js-r7-v2 imports 2 total / 1 named (edge 9 'rot13') / 1 unnamed (edge 2)
S031 round-19 limitations index of gate quote: [4]   # same index in all seven records; quote 17 words
$ bash scripts/sources-census.sh validate --file …/SOURCES-proposed-final.md --today 2026-10-21
file	W04 S024 (pre-existing) | W04 S028 (same URL as S016) | W04 S029 (same URL as S022) — across scopes
file	ok	…/SOURCES-proposed-final.md                      VALIDATE_EXIT=0
$ diff corpus/SOURCES.md corpus/SOURCES-proposed-final.md | grep -c '^<'   →  0   (pure insert)
$ census --file …/SOURCES-proposed-final.md → rows 31, tier.A 29, tier.C 2, mined 22, queued 5, rejected 4
```

Re-opened here: `api.github.com` ref/tags → tag object `67f038c8…` → tag
`v2.20.0`, tagger 2026-02-19T19:06:01Z → commit `2004296f…`, committed
2026-02-19T19:01:27Z; both raw files at the tag ref hash identical to the
commit fetch. ECMA-262 fetched twice → same sha256 `06db92a8…`, `last-modified:
Mon, 19 Oct 2026 16:26:52 GMT`, version line "Draft ECMA-262 / October 16,
2026". Live `corpus/SOURCES.md` 66 lines, sha256 `aa7b07e1…` (unchanged).

## Count reconciliation (aggregate 4 / 4 / 4 / 0)

EVM note: identified 2, screened 2, included 2 rows (S028, S031), excluded 0
→ 2 = 2 + 0 ✔. CommonJS note: identified 2, screened 2, included 2 rows
(S029, S030), excluded 0 → 2 = 2 + 0 ✔. Aggregate S028–S031: 4 / 4 / 4 / 0
→ 4 = 4 + 0 ✔. Unit stated in the notes: one candidate = one document set that
could become one row; extra URLs of an already-counted candidate are named per
note ("Additional opens not proposed as rows") instead of inflating counts —
EVM: `instructions/control_flow.py` (3,124 B, scope check only) and the
tag-ref / tag-object / commit API endpoints; JS: the two `ecmascript-…`
multipage chapter files, plus two guessed short-form chapter URLs that returned
HTTP 404 and were discarded unopened. Each note carries Query, Where, date,
counts, negative sweep, Stop rationale and openers.

## Gates and findings

- **F1 (old-log arithmetic) pre-empted** by the stated unit + per-note
  reconciliation. The round-61 notes are **not** rewritten: F1–F6 belong to
  `R62DebtSearchLog`'s block (agreed with that seat 2026-10-21 — old-line
  correction theirs, round-62 notes mine, no content conflict).
- **E11 sequencing (L1's call).** S028/S030/S031 as `mined` with the candidate
  paths as `used-by` → **E11 ×3, exit 1**: the two
  `corpus/knowledge/round-62-*.md` entries do not exist in the frozen tree.
  Land `queued` with `used-by: —`, flip to `mined` + path in the same round,
  old→new logged in the lesson (contract rule 2).
- **E04 trap.** S029 with S022's scope text copied verbatim → `E04 … within
  scope`, exit 1; S029's scope must stay narrower (language semantics only).
  W04 (shared URLs under different scopes) is expected; S024's W04 unchanged.
- **Quote-locating caveats (not previously reported).** S029's §14.3.3.3 quote
  holds U+00A0 after `?` — a byte-exact ASCII search returns 0 in the fetched
  bytes — and occurs 4× in the single page (2× in §14.3.3.3); the second quote
  occurs 2×, in Table 54 **and** adjacent Table 56, so the table number is part
  of the anchor, not decoration.
- **Anchor drift.** S028's `source` URL is the rendered GitHub tree page, whose
  size moved across three fetches (239,683 / 239,684 / 239,693 B); the row
  anchors the two pinned raw files by SHA-256 instead.

## Touched surfaces

Written: this report and scratch under
`/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62SourceLogPlan/`. Read-only:
`corpus/SOURCES.md`, `corpus/README.md`, `corpus/QUALITY.md`, the round-61
lessons, `reports/round-62/claims.md`, the round-61 `W3SrcSearchLog.md` and the
sibling seat reports. Live `corpus/` and `reports/` unchanged: `git status
--porcelain -- corpus reports` → empty. No producer, bytecode, fixture JS, RPC
or third-party target ran; no prior rejected entry is cited as support.

## Proposed changes (scratch, for L1)

1. Apply Insert A + Insert B from `SOURCES-append-proposal.md` (append-only;
   0 lines removed, verified on a copy).
2. Land S028–S031 `queued` with `used-by: —`; flip to `mined` + `used-by` in
   the round the candidate entries land, old→new in the lesson.
3. Keep S029's scope distinct from S022's; carry the U+00A0 and Table 56
   caveats into the lesson `## Gate`.

## Unknowns

- Whether L1 wants one combined note instead of two; counts hold either way,
  but the text is written as two bounded searches (one per candidate).
- The `## Paths` bullets assert order S028→S031 and S029→S030; if L1 reuses
  S016/S022 instead of adding S028/S029, the bullets must be re-ided.
- S030/S031 `used-by` depend on the final landing paths of the two candidates.

Installs or updates: none (no pacman, no uv/npm/cargo, no network install).
Network reads only: github.com, raw.githubusercontent.com, api.github.com and
tc39.es public documents, read-only, digests recorded above.
