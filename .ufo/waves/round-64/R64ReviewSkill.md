# R64ReviewSkill — SHONEN box 1 non-author verification (final)

Reviewer: **revenger-r64.R64ReviewSkill** (non-author; this seat did not draft the candidate).
Candidate reviewed as the merged pair the brief allows:

- `/tmp/revenger-r64-skill/SKILL.md` — 271 lines, 25591 bytes, sha256
  `31c3f99df2b7717f5a586e790f00b42884ee2ce05a8cad267b8c64165a424e72`
- `/tmp/revenger-r64-skill/checklists.md` — 227 lines, 13506 bytes, sha256
  `07cdfdafd2ed557ed8f21b19c531e1f900284708e3302de10a6a443600f7b8db`
- Landed lane artifact `/home/vgpnk/Projects/shokunin/revenger-shokunin/SKILL.md` —
  39098 bytes, sha256
  `bfd92057e71541cc1d93a9812cb350d69fcb5524df57b24153364d6c11b0a9dd`; verified to be
  exactly `31c3f99d…` + one `"\n"` + `07cdfdaf…` (39098 = 25591 + 1 + 13506).

Box text (`SHONEN.md:5-6`): "SKILL.md contains real decision tables, error patterns,
checklists, cited sources". Any later edit to either file invalidates this signature; the
digests above are the reviewed bytes.

## Verdict

**SHONEN-box-1 `[x]`-ready: yes**, re-stated on the final bytes — component blobs
`31c3f99d…` + `07cdfdaf…` and the landed merge `bfd92057…`. Both files meet the box:
three real decision tables, four error patterns mapped to catching checks, five runnable
checklists, a fully resolved citation set, and named scope limits. Three non-blocking
refinements are listed below; none misdirects a reader to a false claim, and none affects
a command.

Delta-confirm: the change from the previously signed `d66b19d7…` is **exactly two lines**
in `SKILL.md` (scope bullets `README.md` → `corpus/README.md` for "Frontier" and "Known
gaps"); `diff` against the signed copy shows 2 insertions / 2 deletions and nothing else,
`checklists.md` is untouched, and the landed file is the byte-concatenation of the two
final blobs. The other two routed citation nits — the `verified-at` base split and the
multi-script control ranges — were already fixed in the signed `d66b19d7…`; both are
re-verified present in the landed bytes.

Revision note: my first pass reviewed the intermediate `6ee10db9…` and found three defects
(false `verified-at` base, multi-script control ranges off by one, tier-B "sole support"
row contradicting Q01). All three are fixed in `b3b0af1d…` and carried unchanged into the
reviewed `d66b19d7…` (whose delta is only the §6.1 `HOLDS_OK_V2`
`README_TOKEN_LEGEND_MISMATCH` clause), together with F4 (d2 conjunct) and F5 (bare
filename), as described in the verification matrix.

## Verification matrix (all re-checked on the reviewed bytes)

### Cited sources and paths

- Every lane-relative path cited by either file resolves in
  `/home/vgpnk/Projects/shokunin/revenger-shokunin`: 7 knowledge entries, 5 lessons,
  3 firmware fixture files, `corpus/{README,QUALITY,SOURCES}.md`,
  `corpus/fixtures/REPLAY.md`, `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md`, the three
  `reports/round-64/*` files, `.ufo/waves/round-64/R64C4MultiPatch.md`. Zero missing.
- Fleet contract: `SKILL.md` §3 cites it by absolute path
  `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` and states it is
  outside the lane; the file exists and its lines 67-80 are exactly the seven-command
  census block cited by `checklists.md` §4b.
- S-ids: 11 distinct (S005, S006, S007, S009, S010, S014, S015, S032, S033, S034, S035);
  all exist in `corpus/SOURCES.md`; zero unknown. S036/S037 are correctly not cited (not
  yet committed), and the not-yet-existing C07 entry is correctly not cited.
- Line anchors spot-verified against the bytes: `corpus/lessons/round-63.md:218/219/220`
  are M33/M34/M35; M27/M28 exist in `corpus/lessons/round-62.md`;
  `corpus/README.md:21-26` is the status legend (line 25 carries "Work evidence is not
  knowledge"); `corpus/QUALITY.md:32-33` is admission step 3; `PROVINCE.md:6-7` is the
  observation/inference/unknown rule; `reports/round-64/claims.md:84` carries the frozen
  counter string; `SCORECARD.md:29-30` says the census probe exits 0 even when verifiers
  fail; `corpus/live/runs/round-63/LEDGER.md` O6, O10, I1, U4–U6 exist and are quoted
  accurately; `round-63-verifier-spotcheck.md:31` carries the paired-member oracle markers.

### Commands

- Seven-command census block in `checklists.md` §4b: **13/13 lines byte-identical** to the
  fleet contract's `## Census` block (comments included). Executed read-only from the lane
  root: rows `35`, malformed `0`, tiers `A=33 C=2`, statuses `mined=30 queued=1
  rejected=4`, duplicate/enum/missing-used-by output empty — matching the document's
  zero/empty promises.
- Census C block in `checklists.md` §1: **8/8 lines byte-identical** to
  `SCORECARD.md:35-42`.
- Oracle command `python3 -B corpus/live/runs/round-63/oracle_check.py` is verbatim from
  `LEDGER.md:110`; defaults at `oracle_check.py:11-12`, `REGION`/`MISMATCH`/`ORACLE
  OK`/`ORACLE MISMATCH` output and exit 1 are as promised by the code (`:206-225`); the
  paired-member marker ordering matches.
- Frozen-counter usage: `checklists.md` §3 quotes `claims.md:84` verbatim and gives the
  committed round-63 invocation byte-identical to
  `.ufo/waves/round-63/falsify/W2FinalIndependent.md:148-149`; `measure.py:22-23` usage
  message and `:273` exit expression match the documented semantics, and `HOLDS_OK_V2`
  is indeed not folded into the exit code. `SKILL.md` §6.1's added claim that
  `HOLDS_OK_V2` also requires `README_TOKEN_LEGEND_MISMATCH == 0` matches `measure.py`'s
  `holds_ok_v2` expression (`len(mismatch) == 0`), while the exit expression tests only
  `holds_ok`.
- Fixture recipe `python3 -B generator.py` matches `truth.json`
  `build_recipe.command`; generator line anchors `39-49`, `52-101`, `104-113`, `:131`,
  `:133`, `:149-150` all land on the claimed statements.
- `python3 -B corpus/verify_*.py --self-test` matches committed usage
  (`corpus/knowledge/tool-validation-by-function-and-version.md:142`).
- Fleet checker `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` exists
  (read-only, fleet-owned); its documented exit codes are at header lines 16-18 as cited,
  and W04's meaning in the script ("same URL across scopes") matches `checklists.md` §4a.

### Decision tables, error patterns, checklists, scope

- §1 gives the credit rule, exact attribution phrase, frozen control shape, and an
  explicit "not yet earned" status for C4; the four rows match the current sources
  (`icon_languages` 118-120 / 149-151 / 152-154; `multi_icon_states` 121-123 / 148-150 /
  151-153; `icon_states` 119-123 / 151-158; `named_multi_icon_states` 16-17 / 76-78).
- §2's fixture table was hardened correctly: it now warns that running `generator.py` in
  place rewrites the frozen fixture and truth, and that interpreter/zlib versions enter
  the truth — a real void-condition hazard.
- §3 tier table is consistent with Q01 (B never sole support for a load-bearing claim).
- §4 maps M33–M36 to concrete checks; M36 is correctly sourced to the round-64 contract
  (the round-64 lesson does not exist yet).
- §5 reproduces Q01–Q13 with Q08 flagged superseded; §6.1–6.5 are runnable checklists
  whose labels and void conditions match `claims.md` §Counting/§Harms, including
  `C2_RECEIPT_B_KILLED_ATTRIBUTED` and `C2_D2_KILLED` and "new round-64 paths".
- Scope limits are named in five bullets plus §8 (no producer/readiness, no
  origin/completeness/authenticity, no generalization, no gate registry, manual stays
  manual), anchored to existing PROVINCE/README/SCORECARD headings.

## Non-blocking refinements

1. `checklists.md` §4a cites `reports/round-64/claims.md:127-129` for "census exit 0,
   35 rows, four disclosed W04s"; the four-W04 parenthetical continues on line 130, so
   the range should be `:129-130`.
2. `checklists.md` §4b cites the fleet contract as `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:67-80`
   (a fleet-root path written without its root). `SKILL.md` §3 now uses the absolute path;
   using the same absolute form in the checklist would make it resolvable from any cwd.
3. `SKILL.md`'s `verified-at` still describes the §1 control ranges as "at the uncommitted
   working tree on top of `a3d063f`". L1 committed the C2/C4 patches in `671e3a18`, so the
   clause is now stale in the opposite direction; the ranges themselves stay correct
   against the committed blobs (`icon_languages` forged-stdout `152-154`,
   `multi_icon_states` `151-153`, both verified from `git show 671e3a18:…`). If the header
   is touched again, name `671e3a18`.

## Landed artifact

`/home/vgpnk/Projects/shokunin/revenger-shokunin/SKILL.md` (39098 bytes, sha256
`bfd92057…`) is byte-exactly `31c3f99d…` + `"\n"` + `07cdfdaf…`; `root.startswith(SKILL)`
and `root.endswith(checklists)` both hold. Re-running the sweep on the landed bytes: zero
bare `README.md` references, "Frontier"/"Known gaps" anchors correct, multi ranges correct,
`3bb430f` provenance present, `HOLDS_OK_V2` mismatch clause present, census block present,
14 S-ids all registered, and the only non-resolving path token is item 2 above (fleet
contract by lane-relative spelling; the file exists at fleet root and §3 cites it
absolutely).

## Residual risk

- The two C4 stdout controls are **committed** as of `671e3a18` (verified from the
  committed blobs at `icon_languages:152-154` and `multi_icon_states:151-153`; the working
  tree is clean for `corpus/verify_*.py`). `SKILL.md` §1 correctly claims no credit: the
  box flip and C2's target still require the frozen counter to print
  `C4_RECEIPT_KILLED_ATTRIBUTED=2/2`.
- The frozen `reports/round-64/claims.md` was amended once by L1 in `671e3a18` (one hunk:
  `HOLDS_OK_V2` wording now names the attributed-count substitution plus
  `README_TOKEN_LEGEND_MISMATCH == 0`). The frozen-counter line (`:84`) and its command are
  unchanged; the SKILL's §6.1 wording matches the amended text.
- §1 "unguarded" judgments are source-reading conclusions, not mutation evidence; the M35
  debt for `exit_code`, `fixture_sha256`, `evidence_id` (both scripts) and
  `duration_seconds` (`verify_named_multi_icon_states.py`) remains real until controls
  exist.

## Verification gaps

- No `lsp` device is mounted (`xd://lsp` → "No such tool: xd://lsp. Mounted devices:
  ast_edit, debug"), so checks used reads, line-number greps and line-range diffs; no
  semantic cross-reference was available.
- I did not execute the four `--self-test` verifiers or the frozen counter (the exec seat
  owns runnable execution; its filed report predates the candidate). The census commands
  and the `sources-census.sh` documentation were read/executed read-only as recorded.
- No tools were installed or updated.

Report: .ufo/waves/round-64/R64ReviewSkill.md
