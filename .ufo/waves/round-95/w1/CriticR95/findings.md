# CriticR95 findings — round-95 w1 (C2 live falsification + C10 admission review)

Seat: CriticR95 (critic) · 2026-11-05 · lane: revenger-shokunin
Frozen bytes verified before any run: working-tree entry sha256 ==
`git show 6e0bf15fed58f357b7fa0c881371ac7616a116f7:corpus/knowledge/round-95-evidence-ledger-discipline.md` sha256 ==
`476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`; because the entry's only
status line already reads `admission-status: candidate`, the normalized vote digest is the
same value, and it matches `.ufo/waves/round-95/w1/ExecFrozen/digest.txt` (checked after landing).

## Method

Seven NEW forged admission trees (beyond the frozen eleven named vectors and the 22
self-test deltas in `reports/round-95/claims.md` C1). Each attack is a `python3 -B` script
under `attacks/` that imports the frozen counter
(`reports/round-95/c1_k_admit_counter4.py`) as a module, builds the honest
admission-shaped fixture with its `_fixture(work)`, applies one mutation, runs the counter
end-to-end with `--tree`, and records rc + failing legs + verbatim counter stdout to a
receipt under `receipts/`. Counter scratch was redirected into this seat's scratch tree
via `HYAKU_SCRATCH` (deleted on exit; receipts carry the full stdout, so nothing depends
on the ephemeral fixture paths). Every leg below was exercised on the honest fixture first:
unmutated runs print `C1_VERDICT=pass` with `digest=476edc36…79fb9` — positive control
reproduced each time.

## Results

| # | attack (shape) | rc | failing legs | verdict |
|---|---|---|---|---|
| A1 | body swapped after fetch-log commit; receipt re-bound to new body; log names old sha (a) | 1 | C1_RECEIPTS (`S500:fetch-log-line-missing`; `C1_QUOTES_WHY=ok`) | killed |
| A2 | vote artifact = symlink from the seat's own dir to a file outside the wave dir (b) | 1 | C1_VOTES (`artifact resolves outside wave dir`) | killed |
| A3-old | S500/S501 used-by cell REPLACED by the superseded `knowledge/2026-10-29-rea-evidence-ledger-discipline.md` (exists in fixture corpus) (c) | 1 | C1_SOURCES (cite-back-missing ×2) | killed |
| A3-both | used-by cell names superseded entry AND the real entry (c variant) | 0 | — | **SURVIVED — routed observation** |
| A4 | second knowledge file byte-identical to the admitted entry except indented status line; zero references (d) | 0 | — | **SURVIVED — routed finding for r96** |
| A5 | S500 teaches cell carries escaped `\|` pipe (e) | 1 | C1_SIDS + C1_SOURCES (`parse_sources` drops the row: S500 unseen) | killed |
| A6 | duplicate JSON key (`fetched_at` ×2) in S500.receipt.json (extra) | 1 | C1_RECEIPTS (strict-JSON hook) | killed |

Receipts: `receipts/A1-body-swap-stale-log.json`, `receipts/A2-symlink-artifact-escape.json`,
`receipts/A3-usedby-redirect-old.json`, `receipts/A3-usedby-redirect-both.json`,
`receipts/A4-orphan-shadow-entry.json`, `receipts/A5-escaped-pipe-sources.json`,
`receipts/A6-receipt-dupkeys.json`.

## Routed to r96 (survivors — never a reason to edit frozen bytes)

1. **A4 — no leg enumerates `corpus/knowledge/`.** An unreferenced second entry file with a
   malformed (indented) `admission-status` line passes ALL 24 legs (`C1_VERDICT=pass`,
   `C1_K_HELD_BACKED=12/15` in `receipts/A4-orphan-shadow-entry.json`). C1_ADMITTED, lint,
   embedded, sids, quotes and the digest all read only the named ENTRY path; C1_ONLY_C10
   compares only coverage rows. Suggested close shape for r96: a leg that rejects any
   `corpus/knowledge/*.md` file outside the union of coverage-row filesets whose bytes
   contain a `STATUS_ANY` match — or lint widened to enumerate the directory. Severity:
   low-moderate (the orphan cannot self-admit — the coverage map stays the admission
   authority — but a stray admitted-looking file can mislead downstream tooling and the
   r96 counter should close it).
2. **A3-both — cite-back check is substring-based, exclusivity unenforced.**
   `check_sources` accepts a used-by cell naming the real entry AND the superseded entry
   (`ENTRY_REL in r[10]`). Informational: the real cite-back is present, so nothing
   load-bearing is hidden; a strict close would require the used-by fileset to resolve and
   the superseded knowledge path to be absent from new-row used-by cells.

## Disclosed residual, NOT re-routed

A1's sharper cousin — swap the body AND rewrite receipt + fetch-log fully consistently —
passes `C1_RECEIPTS` by construction: the leg checks the committed bytes' honesty fields
and cannot order commits. This is exactly the disclosed limit sentence in
`reports/round-95/claims.md` C1 ("a non-author re-fetch and the non-author closure remain
the only real proof of opening"), so it is a disclosed limit, not a new survivor. The
variant actually forged (receipt re-bound, log stale) IS caught — the log sub-check
(`sid` ∩ `fetch_sha256` per line) is the only thing standing, and it held.

## Vote

Part 2 (vote) is recorded in `vote.json` with artifact `evidence.md`, bound to candidate
digest `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`. Decisions:
PASS Q01/Q02/Q04/Q09/Q10/Q11/Q16; n/a Q03/Q05/Q06/Q07/Q08/Q12/Q13/Q14/Q15/Q17, each n/a
carrying a ≥6-token reason with a Q cross-reference (vocabulary-checked). The entry's own
§Q-map was read only AFTER my per-criterion pass; disagreements: none.

## Bounds compliance

All Python invocations used `python3 -B` (scripts, counter subprocesses, digest recipe);
no git write commands anywhere (only `git show` / `git cat-file` / `git archive` /
`git ls-tree` reads); no lane file edited; counter/battery/votes written only by their
frozen owners; scratch tree `/fast/scratch/hyaku/revenger-r95/CriticR95` deleted on exit;
no network used (attack fixtures are synthetic; no URL fetched).
