# CriticR95 — round-95 w1 report (attack + vote)

## Digest binding (verified)

Working-tree entry bytes == freeze-commit bytes; sha256 ==
`476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9` == normalized vote
digest (the entry's only status line is already `admission-status: candidate`) ==
`.ufo/waves/round-95/w1/ExecFrozen/digest.txt`. Votes bind consistently.

## C2 attack results — 7 new forged trees beyond the frozen eleven (all `python3 -B`, v4 fixture via `_fixture`, run with `--tree`)

| attack | rc | failing legs | verdict |
|---|---|---|---|
| A1 body-swap-stale-log (receipt re-bound, fetch-log stale) | 1 | C1_RECEIPTS (`S500:fetch-log-line-missing`; quotes ok) | killed |
| A2 symlink artifact escaping wave dir | 1 | C1_VOTES (`artifact resolves outside wave dir`) | killed |
| A3-old used-by redirected to superseded entry (path exists) | 1 | C1_SOURCES (cite-back-missing ×2) | killed |
| A3-both used-by names superseded AND real entry | 0 | — | SURVIVED (observation) |
| A4 orphan knowledge file, byte-identical except indented status | 0 | — | **SURVIVED (routed finding)** |
| A5 escaped `\|` in SOURCES teaches cell | 1 | C1_SIDS + C1_SOURCES (row silently dropped by parse_sources) | killed |
| A6 duplicate JSON keys in a receipt | 1 | C1_RECEIPTS (strict hook) | killed |

Positive control reproduced in every run (unmutated fixture: `C1_VERDICT=pass`,
`digest=476edc…79fb9`, `C1_K_HELD_BACKED=12/15`). Receipts with verbatim counter stdout:
`.ufo/waves/round-95/w1/CriticR95/receipts/A1..A6*.json`; full method and per-attack
detail: `.ufo/waves/round-95/w1/CriticR95/findings.md`.

## Routed to r96 (per the frozen kill rule — frozen bytes untouched)

1. **A4**: no v4 leg enumerates `corpus/knowledge/`; an unreferenced second entry file
   with a malformed (indented) `admission-status` line passes all 24 legs. Suggested
   close: reject any `knowledge/*.md` outside the coverage-row fileset union whose bytes
   contain a `STATUS_ANY` match (or widen lint to enumerate the directory).
2. **A3-both**: new-row cite-back check is substring-based; a used-by cell may co-name the
   superseded entry. Informational — the real cite-back is still present.
3. Disclosed, NOT routed: a fully-consistent post-hoc receipt+log rewrite passes
   `C1_RECEIPTS` by construction — this is the disclosed limit sentence in claims.md C1
   (non-author re-fetch / non-author closure remain the only real proof). The forged
   stale-log variant IS killed (A1).

## Vote (C1 trio)

`vote.json` + artifact `evidence.md` (sha256
`a0180e2f6e1154de3554174907805b59e43efc8b6303982b7db97c042882f9ee`) in this seat dir.
Decisions: PASS Q01/Q02/Q04/Q09/Q10/Q11/Q16; n/a Q03/Q05/Q06/Q07/Q08/Q12/Q13/Q14/Q15/Q17
with vocabulary-checked reasons. Receipts/re-entry bytes inspected before deciding; no
disagreement with the entry's §Q-map.

## Bounds compliance

`python3 -B` everywhere (verified 0 `__pycache__` under corpus/, reports/round-95/,
.ufo/waves/round-95/); git only read-only (`show`/`cat-file`/`archive`/`ls-tree`); no lane
file edited; no network; no installs; scratch `/fast/scratch/hyaku/revenger-r95/CriticR95`
deleted on exit (counter scratch redirected there via `HYAKU_SCRATCH`).
