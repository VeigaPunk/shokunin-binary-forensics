# R64ReviewSkillCites

Seat: `revenger-r64.R64ReviewSkillCites` — citation existence sweep of the SKILL
candidate, per brief `.ufo/waves/round-64/briefs/R64ReviewSkillCites.md`.

## What was swept

`/tmp/revenger-r64-skill/SKILL.md` (264 lines, landed 2026-10-24 01:20; the path
was absent at the start of the window, so two sibling seats earlier returned
dependency findings). Extraction via `/tmp/revenger-r64-cites/sweep.py`; every
load-bearing anchor then verified manually. Read-only; no repo writes beyond the
two authorized wave files.

## Findings by severity

1. **Medium — mislocated anchors (phantom-adjacent):** `SKILL.md:26` and `:32`
   cite bare `README.md` "Frontier"/"Known gaps"; the lane-root README has
   neither section (they live at `corpus/README.md:59` / `:50`). `SKILL.md:24`
   already cites `corpus/README.md` for the same anchors, so the bare form is a
   stale path, not a different file.
2. **Low-medium — "at this SKILL's base" overclaims:** `SKILL.md:8` and the §7
   `measure.py` row assert all cited paths exist at claim base `666ea84b`, but
   `reports/round-64/{claims.md,measure.py,measure-before.log}` are all absent
   at that commit (`git cat-file -e` fails ×3); they are pre-registration
   commits. The cited `measure.py` sha256 (`b8e68d32…`) verifies against the
   working-tree file, not a base blob.
3. **Low — stale line anchors:** §1 `verify_multi_icon_states.py` forged
   controls cited `:149-151`/`:152-154`; actual `:148-150`/`:151-153`
   (attribution phrases themselves correct; `R64C4MultiPatch.md` agrees).
4. **Informational:** zero URL citations (§7 deliberately restates none); all 15
   cited S-ids registered in `corpus/SOURCES.md` (none rejected-status);
   `corpus/lessons/round-64.md` and `.ufo/waves/round-64/sources-rows-draft.md`
   do not exist, but the candidate never cites them — M36 is correctly sourced
   to `claims.md` (which names M36 at its §131).

## Verified consistent

- All §7 knowledge/lessons/corpus paths exist at `666ea84b` (22 paths checked
  via `git cat-file -e`); all four `receipt_ok` conjunct tables, control line
  ranges and attribution phrases match file bytes; `truth.json` 73 lines and the
  exact key shapes the SKILL claims; all seven §6.2 census commands run clean
  from the lane root with the claimed outputs (rows 35, malformed 0, no
  duplicates/enum/missing-paths); `measure.py` tail confirms exit 0/1/2
  semantics and `HOLDS_OK_V2` not folded into the exit code; SOURCES contract
  file and its cited rule numbers (1, 2, 6, §Census) exist and match.

## Residual risk

- §3 tier-B gloss ("only where Q01's scope test passes") can read weaker than
  Q01's tier-A-for-scope requirement — wording risk, not a phantom.
- `claims.md` freezes counter cwd as `/`; SKILL says "from the lane root" —
  practice demands the lane root; noted as a doc-level deviation.
- S007 cited while still `queued` — exists, but should not be promoted to
  load-bearing.

## Tooling

No installs (none needed). Scratch kept under `/tmp/revenger-r64-cites/`
(sweep.py + sweep-out.json) for re-runs after any candidate revision.

Report: .ufo/waves/round-64/R64ReviewSkillCites.md
