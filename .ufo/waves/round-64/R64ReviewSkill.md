# R64ReviewSkill — SHONEN box 1 non-author verification

Reviewer: **revenger-r64.R64ReviewSkill** (non-author; this seat did not draft the candidate).
Candidate: `/tmp/revenger-r64-skill/SKILL.md` — 266 lines, sha256
`6ee10db9dece167c3b9e541fdec4933071fd6153a98146972f0656d89ab157c2`; no
`checklists.md` exists beside it (single merged file, as the brief allows).
Box text being tested (`SHONEN.md:5-6`): "SKILL.md contains real decision tables,
error patterns, checklists, cited sources".

## Verdict

**SHONEN-box-1 `[x]`-ready: no, as submitted.** Three textual defects (F1–F3) must be
corrected; each is a one-line edit in the scratch candidate. With F1–F3 fixed as
specified, the document meets the box on the evidence below and I would sign `[x]`
without a re-draft. F4–F5 are recommended precision fixes.

## Findings

### F1 — Medium, blocking (provenance): false base commit for round-64 artifacts

- Header: `verified-at: 2026-10-24, lane commit 666ea84b… (round-64 claim base). Every
  file, line range and S-id cited below was re-read in the lane tree at that base.`
- §7 last row: `reports/round-64/measure.py` sha256 `b8e68d32…` — "identity of the
  frozen instrument at this base".
- Observed: `git cat-file -e 666ea84b6be2eec2b0359f556ba2429fc9044c36:<path>` returns
  absent for all three of `reports/round-64/claims.md`, `reports/round-64/measure.py`,
  `reports/round-64/measure-before.log`. They were added in
  `3bb430f96cac09feb7269c5c52725127c6f7c463` ("round-64: frozen claims + counting
  probe + red-before do-nothing control"), whose blob digest for `measure.py` is
  exactly `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168`.
  The digest value is right; the base attribution is wrong.
- Harm: this file's authority is provenance. A reader auditing at the stated base
  finds three cited files missing, and §7's "at this base" row is false where it is
  most load-bearing. It is the Q09/Q11 identity-claim class the lane gates on.
- Fix: `verified-at:` names two commits — corpus files at `666ea84b…`, round-64 frozen
  artifacts at `3bb430f…` (measure.py blob sha256 `b8e68d32…`); amend §7's last row to
  "at `3bb430f`". Also, the sweep sentence says "in the lane tree", while §3 cites the
  fleet contract `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` (fleet root, outside the
  lane tree); say "lane tree and the named fleet contract".

### F2 — Medium: wrong `file:line` for the two controls in `verify_multi_icon_states.py`

- §1 row claims forged `command` `:149-151` and forged `stdout_sha256` `:152-154`.
- Observed (`grep -n forged corpus/verify_multi_icon_states.py`): `forged=148`,
  mutation=149, `require`=150, `forged_stdout=151`, mutation=152, `require`=153;
  line 154 is `return data, report, decoded, state`. The claimed range starts one line
  late and ends one line past the control.
- The other three rows are exact: `verify_icon_languages.py` `:118-120` body and
  `:149-151`/`:152-154` controls; `verify_icon_states.py` `:119-123` and `:151-158`;
  `verify_named_multi_icon_states.py` `:16-17` and `:76-78`.
- Fix: `:148-150` and `:151-153`.

### F3 — Medium-low: tier-B row contradicts Q01

- §3 tier table: B may be sole support "only where Q01's scope test passes".
- `corpus/QUALITY.md` Q01 requires every load-bearing claim to rest on a row that is
  tier **A** for that scope; no scope test licenses a B row as sole support of a
  load-bearing claim. As written the cell invites the exact citation Q01 rejects.
- Fix: "No for a load-bearing claim (Q01 requires tier A for the scope); B
  corroborates only."

### F4 — Low: §6.5 void list drops the `C2 d2` conjunct

`reports/round-64/claims.md` §Harms voids on "C2 attributed kills below 2/2 **or d2
below 2/2**"; §6.5's "attributed calibration counts below target" plus holds list never
names `C2_D2_KILLED`, and "outside new round paths" drops the contract's "round-64"
qualifier. Fix: name the d2 condition and "new round-64 paths".

### F5 — Low: bare filename citation

§1 cites "`R64C4MultiPatch.md` records that its seat did not run the self-test"; the
file is `.ufo/waves/round-64/R64C4MultiPatch.md`. Every other citation is a full
repo-relative path; use the full path.

## Passed checks (evidence)

- **Path citations.** 38 backticked lane-path tokens; every `corpus/knowledge/*`,
  `corpus/lessons/*`, `corpus/fixtures/*`, `reports/round-64/*` and root-file citation
  resolves in the lane tree. The single flagged token
  `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` is explicitly labeled "fleet" and exists at
  fleet root — not a lane path claim (folded into F1's wording fix). All 7 cited
  knowledge entries exist; `corpus/fixtures/REPLAY.md`, `corpus/README.md`,
  `corpus/QUALITY.md`, `corpus/SOURCES.md`, `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md`
  exist.
- **S-ids.** 11 cited (S005, S006, S007, S009, S010, S014, S015, S032, S033, S034,
  S035); all present in `corpus/SOURCES.md`, 0 unknown. S036/S037 correctly absent (not
  yet committed to the registry), and the new C07 entry is correctly not cited (it does
  not exist yet).
- **Commands.** The seven §6.2 census commands are byte-identical to
  `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` §Census (7/7 exact match), and all seven run
  clean read-only from the lane root: rows `35`, malformed `0`, tiers `A=33 C=2`,
  statuses `mined=30 queued=1 rejected=4`, duplicates/enum-violations/missing-used-by
  all print nothing. `python3 -B reports/round-64/measure.py TREE` is verbatim at
  `reports/round-64/claims.md:84`; §6.1's exit-code reading matches `measure.py`'s tail
  (`sys.exit(2 if not evaluable else 0 if holds_ok else 1)`, 273 lines) and
  `HOLDS_OK_V2` is indeed not folded (its expression adds `attributed_b`,
  `c3_attributed`, `c4_attributed`). `python3 -B corpus/verify_*.py --self-test` matches
  committed usage (`corpus/knowledge/tool-validation-by-function-and-version.md:142`).
  The fixture recipe `python3 -B generator.py` matches `truth.json`
  `build_recipe.command`.
- **§2 references.** `generator.py` `decode_member` :39-50, `derive_regions` :52-101 and
  build :104-115 (`def main` at 104, `image = bytes(image)` at 113) all match; the
  declared `MEMBERS` block spans 19-36, so the stated :17-35 covers the declaration
  through the second member's closing brace (closing paren at 36) — adequate for a
  "where it is shown" pointer, not counted as a defect. `truth.json` is 73 lines as
  stated.
- **Error patterns.** M33/M34/M35 are at `corpus/lessons/round-63.md:218/219/220`
  exactly; M27/M28 exist in `corpus/lessons/round-62.md`; M36 is correctly sourced to
  `reports/round-64/claims.md` (the round-64 lesson does not exist yet — citing it would
  have been the defect).
- **Actionability.** §1 gives the credit rule and the exact attribution phrase; §2 is a
  step → do → never table with file pointers; §3 encodes the append-only/reject/flip
  rules; §5 reproduces Q01–Q13 (Q08 flagged superseded, matching QUALITY.md's Q11
  supersedes line); §6.1–6.5 are runnable checklists (counter labels and exits, census,
  admission order, replay/regeneration, void conditions). A reader can act on the
  document alone for all three governed acts.
- **Scope limits named.** Five bullets (no producer/readiness claim, no
  origin/completeness/authenticity, no generalization, no gate registry, manual stays
  manual) plus §8, anchored to `PROVINCE.md`, `corpus/README.md:50` "Known gaps" and
  `SCORECARD.md:17` "Rubric boundaries" — all anchors exist.
- **Honest disclosure.** §1 states the two C4 stdout controls are the working-tree fix,
  that `C4_RECEIPT_KILLED_ATTRIBUTED=0/2` is the base value, and that credit is earned
  only when the frozen counter prints `2/2` at the landing commit; it does not claim the
  target.

## Residual risk

- The two C4 controls are **uncommitted** at review time (`git status` shows
  `M corpus/verify_icon_languages.py`, `M corpus/verify_multi_icon_states.py`). The
  landed SKILL describes a commit-time state only if L1 lands those patches in the same
  or an earlier commit; a post-landing reviewer should re-run the frozen counter for
  `C4_RECEIPT_KILLED_ATTRIBUTED=2/2` before the box flip.
- §1's "unguarded" column is a source-reading judgment, not mutation evidence; the M35
  debt for `exit_code`, `fixture_sha256`, `evidence_id` (both scripts) and
  `duration_seconds` (`verify_named_multi_icon_states.py`) remains real until controls
  exist.
- Box 1's wording ("real decision tables…") is satisfied in shape; nothing here asserts
  box 2/3 or promotion.

## Verification gaps

- No `lsp` device is mounted (`xd://lsp` → "No such tool: xd://lsp. Mounted devices:
  ast_edit, debug"), so caller/definition checks used text reads and line-number greps;
  no semantic cross-reference was possible.
- I did not run the four `--self-test` verifiers or the frozen counter (the exec seat
  owns execution; its report predates the candidate). The census commands were executed
  read-only and their outputs are recorded above.
- No tools were installed or updated.

Report: .ufo/waves/round-64/R64ReviewSkill.md
