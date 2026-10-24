# R64SkillDraft — SHONEN box-1 SKILL draft

## Behavior

Drafted the SHONEN box-1 candidate at
`/tmp/revenger-r64-skill/SKILL.md` (271 lines, 25,577 bytes,
sha256 `d66b19d7b7dbbf9cdad337244781cd016b488274eb663bcfde8fba781c328f6c`).

It answers `SHONEN.md` box 1 ("real decision tables, error patterns, checklists, cited
sources") with:

- **§1 decision table** — the four `receipt_ok` conjunct tables
  (`verify_icon_languages.py`, `verify_multi_icon_states.py`, `verify_icon_states.py`,
  `verify_named_multi_icon_states.py`), each conjunct marked guarded/unguarded against the
  in-script forgeries actually present, including the round-64 C4 `stdout_sha256` control
  and the attributed-endswith rule.
- **§2 decision table** — fixture authoring discipline transcribed from
  `corpus/fixtures/firmware-r63/generator.py` (`decode_member`, `derive_regions`, `main`)
  plus the `truth.json` shape and the M33 pre-probe.
- **§3 decision table** — SOURCES tier rules (A/B/C, `community` never A, scope-bounded
  tier, append-only, rejected-row quote+flip) from the contract restated by
  `corpus/SOURCES.md`.
- **§4 error patterns** — M33 stale premise, M34 counter substitution, M35 residual
  unguarded clause, M36 self-assessment drift, each mapped to the check that catches it
  and to the committed row (`round-63.md:218-220`; `reports/round-64/claims.md` for M36).
- **§5 admission checklist** — Q01–Q13 with reject triggers (Q08 marked superseded by
  Q11) and the QUALITY.md admission procedure.
- **§6 checklists** — frozen-counter usage and labels/exit codes, the seven census
  commands verbatim, the claims.md admission order, replay/regeneration commands, and the
  round-close void gate.
- **§7 cited sources** — only committed lane paths and S-ids, no URLs restated.
- **§8** — failure modes of the SKILL itself.

Scope is the lane's saved-ledger evidence craft only; `PROVINCE.md` refusals, README
"Known gaps" (no gate registry; SKILL/AGENTS previously absent) and SCORECARD rubric
boundaries are named as limits.

## Commands run and outcomes

All read-only; no product code, verifier, counter, or git/jj state was changed.

| command | outcome |
|---|---|
| `git log -2 --format='%H %s'` (lane root) | HEAD `a3d063f29b93ad1f0b7eab78652c552685b84d89` (wave-spec/64 briefs); parent `3bb430f96cac09feb7269c5c52725127c6f7c463` (frozen claims + probe + red-before); claim base `666ea84b…` present in history |
| `sha256sum reports/round-64/measure.py corpus/fixtures/firmware-r63/firmware-r63.bin corpus/fixtures/firmware-r63/truth.json` | `b8e68d326c28690274be98ac35a518970d84aa8b9892b5736450a776210b9168`, `bdfe9f46e8f2137194d11265262bd68d8c5c8805694edce7ab2fa3d55a8510be`, `9663f90b2b9f29c5beb621e554ed7584eedf5e77d4785f26a453e70dbd5a65e6` |
| `git show 666ea84b:corpus/README.md \| grep -cE '^\| C[0-9]+ '` | `14` coverage rows, consistent with the K denominator |
| `git show 666ea84b:corpus/SOURCES.md \| grep -cE '^\| S[0-9]{3} \|'` | `35` registry rows; S036/S037 are **not** committed, so the draft does not cite them |
| citation sweep (Python, lane root): extract every backticked `corpus/…`/`reports/…` path from the draft, test existence | 24 lane-relative paths, **0 missing**; 7 cited knowledge entries all exist; 11 S-ids cited (S005, S006, S007, S009, S010, S014, S015, S032, S033, S034, S035) all present in `corpus/SOURCES.md` |
| census-block verbatim diff (Python): extract the `sh` block from the fleet contract's `## Census` and from draft §6.2, compare line lists | 14 lines each, **identical: True**; 7 commands present |
| line-reference reads (`read`/`sed -n`) | `verify_icon_languages.py` receipt_ok :118-120, forged command :149-151, forged stdout :152-154; `verify_multi_icon_states.py` :121-123, forged command :148-150, forged stdout :151-153 (re-verified by `grep -n forged` and by `R64ReviewSkill` F2); `verify_icon_states.py` receipt_ok :119-123, forged fixture :151-158; `verify_named_multi_icon_states.py` receipt_ok :16-17, forged command :76-78; `generator.py` MEMBERS :17-35, `decode_member` :39-49, `derive_regions` :52-101, build :104-113; `truth.json` 73 lines; `round-63.md` M33/M34/M35 at :218/:219/:220; `SCORECARD.md` census C and `SHONEN.md` box 1 read in full |
| `wc -l -c` / Python size re-check on the draft | final: 271 lines, 25,577 bytes, sha256 `d66b19d7…c328f6c` |
| `git status --porcelain` (read-only) | no path of mine in the lane working tree; only pre-existing sibling working-tree edits (`corpus/verify_icon_languages.py`, `corpus/verify_multi_icon_states.py`, `LOG.md`) and sibling reports. This seat's outputs are the scratch draft and this report, nothing else |

First citation sweep flagged two non-path strings: the glob `corpus/verify_*.py` and the
fleet-root contract. Both were rewritten (verifier family enumerated by name; fleet
contract marked external with its absolute fleet path), and the re-sweep is clean.

**Not run, not claimed:** no verifier `--self-test`, no frozen counter, no census
execution, no generator regeneration, no fixture/record change, no commit/push, no
git/jj mutation, no tool install.

## Gates

This seat produced no gate result. The draft's guard status is sourced, not produced
here: `reports/round-64/measure-before.log` prints `C4_RECEIPT_KILLED_ATTRIBUTED=0/2`
with both mutant self-tests green, so the control insertion (§1 rows 1–2) is necessary
but its 2/2 credit belongs to the frozen counter at the landing commit. The draft never
asserts 2/2.

## Touched surfaces

- New scratch artifact: `/tmp/revenger-r64-skill/SKILL.md` (lane-owned scratch; L1 lands
  it only after a named non-author pass).
- This report: `.ufo/waves/round-64/R64SkillDraft.md`.
- Nothing else written; `corpus/`, `reports/`, `LOG.md`, README, SCORECARD and the lane
  Git index untouched by this seat.

## Findings

1. **Absent dependency — round-64 lesson draft.** `corpus/lessons/round-64.md` does not
   exist and `/tmp/revenger-r64-lesson/round-64.md` was absent at read time. M36 is
   therefore sourced to the committed `reports/round-64/claims.md` §C1/§Frontier and the
   red-before receipt; the draft cites no absent path. The lesson seat's draft, when it
   exists, can carry the fuller M36 row without changing the SKILL's citation set.
2. **C4 controls landed but unverified at their own seats.** Both M35 scripts carry the
   forged-`stdout_sha256` control in the working tree (`verify_icon_languages.py:152-154`,
   `verify_multi_icon_states.py:151-153`). `.ufo/waves/round-64/R64C4MultiPatch.md` explicitly records that
   its self-test was **not run**; `R64C4LangPatch.md` records one green run of
   `verify_icon_languages.py`. Red-before remains 0/2. The SKILL states exactly this and
   defers credit to the frozen counter.
3. **Residual unguarded conjuncts remain, by design of this round's claim.** No in-script
   forgery exists for `exit_code`, `fixture_sha256` (in the two language scripts),
   `evidence_id`, or `duration_seconds`; `stdout_sha256` stays unguarded in
   `verify_icon_states.py` and `verify_named_multi_icon_states.py`. The SKILL lists them
   as unguarded per Q13 rather than silently crediting them — the C2 claim covers only the
   two scripts it names.
4. **S036/S037 were absent from the committed registry.** At this seat's read the
   committed registry (`666ea84b`/`3bb430f`) held 35 rows and the draft cites none of
   S036/S037, so no citation can be phantom. A later sibling/L1 working-tree edit
   appended S036/S037 (37 rows) and amended `claims.md`'s `HOLDS_OK_V2` wording; those
   changes are not mine and were not used as SKILL evidence. If L1 lands them, the
   sources table can add the rows without touching any decision table.
5. **Fleet-root dependency is external.** `.ufo/waves/kaika/SOURCES-CONTRACT-v1.md` is
   outside the lane repo; the draft marks it external with its absolute fleet path so a
   citation sweep does not count it as a lane path.
6. **Sibling reviews were racing the draft.** `R64CriticSkill.md` correctly reports the
   candidate was missing when that seat ran (path not found). The draft now exists; I
   messaged `revenger-r64.R64CriticSkill` (with a corrected sha256 after a typo in my
   first note) and `revenger-r64.R64ReviewSkill` that it is available. Their verdicts are
   not in this report and no SHONEN box is flipped by it.
7. **No installs or updates** were made (pacman was not invoked, per the host pause).

## Corrections after non-author attack (`R64CriticSkill`)

The critic returned three material findings against draft
sha256 `29172a6e…5989f10` and one follow-up against `23e61e72…558c9f9`; all four were
reproduced and accepted. The draft was corrected and re-hashed; no script, test or
counter was run for any of this.

| finding | reproduction (read-only) | fix in the draft |
|---|---|---|
| L6 false base provenance: `666ea84b` does not contain `reports/round-64/claims.md` | `git -C <lane> cat-file -e 666ea84b:reports/round-64/claims.md` → **exit 128**; same for `measure.py`; both exit 0 at `3bb430f`; base scripts have **0** `forged_stdout` occurrences while the working tree has them | header `verified-at:` now splits provenance: corpus/SCORECARD/SHONEN/PROVINCE at `666ea84b`; `reports/round-64/*` at `3bb430f`; the two §1 control ranges at the uncommitted working tree on `a3d063f2`. §1, §6.4 and the measure.py hash row were reworded to match |
| L79/L207 regeneration in place would overwrite the frozen r63 fixture and truth | `generator.py:149` `IMAGE_PATH.write_bytes(image)`, `:150` `TRUTH_PATH.write_text(...)`; the recipe embeds `zlib.ZLIB_RUNTIME_VERSION` (:131) and `platform.python_version()` (:133), so a different interpreter changes truth metadata even with identical payloads; claims.md §Harms voids on changed fixture bytes | §2 "reproduce" and §6.4 now require copying the fixture directory to `/tmp/revenger-r64-*` and regenerating there, then byte-comparing; in-place generation is named as a void condition |
| L96 tier B could be read as sole support on scope match, contradicting Q01's tier-A requirement | `corpus/QUALITY.md` Q01: "Each load-bearing claim rests on a `corpus/SOURCES.md` row that is tier A for that claim's scope" | tier-B cell now reads "never sole support for a load-bearing claim — corroboration beside a tier-A row only" |
| L152-154 counter invocation described as lane-root; claims.md §Counting requires `cwd=/` | `reports/round-64/claims.md` §Counting: "on a committed `git archive <commit> corpus` tree, cwd=/, TMPDIR under lane-owned scratch" | §6.1 and the header `recheck:` now require `cwd=/`, the probe by absolute lane path and an absolute `TREE`, `TMPDIR` under the same lane-owned scratch, and state that a lane-root invocation is not the registered measurement |

Post-correction checks (final draft `d66b19d7…c328f6c`, 271 lines, 25,577 bytes):
lane-relative citation sweep 24/24 present; the fleet contract absolute path exists;
11 cited S-ids all in `corpus/SOURCES.md`; census block still byte-identical (14 lines);
host Python 3.14.8 / zlib 1.3.2 match the recorded recipe, but the draft no longer relies
on that matchup.

## Corrections after named-verifier review (`R64ReviewSkill`)

The named verifier reviewed a 266-line candidate at sha256 `6ee10db9…ab157c2` and returned
**NOT `[x]`-ready as submitted** with three line fixes (their report:
`.ufo/waves/round-64/R64ReviewSkill.md`). That hash is an intermediate state of the
scratch file — it sits between my two correction batches and matches neither the pre-fix
`29172a6e…` nor the current candidate. Handling:

| finding | status | action |
|---|---|---|
| F1 false base provenance + "identity … at this base"; sweep sentence should say "lane tree and the named fleet contract" | already corrected before the review was read | header now splits `666ea84b` / `3bb430f` / working tree; §7 row reads "committed at `3bb430f`, unchanged at `a3d063f`/working tree"; the sweep sentence names the lane tree **and** the fleet contract |
| F2 multi_icon_states control line ranges off by one | genuine defect in the reviewed state | confirmed by `grep -n forged`: forged command `:148-150`, forged stdout `:151-153`; §1 row and this report corrected |
| F3 tier B "sole support on scope match" contradicts Q01 | already corrected before the review was read (critic finding 3) | tier-B cell now forbids sole support for load-bearing claims |
| F4 (recommended) name the C2 d2 conjunct in §6.5 | applied | §6.5 now names `C2_RECEIPT_B_KILLED_ATTRIBUTED` 2/2 **and** `C2_D2_KILLED` 2/2, C3 2/2, C4 2/2 after landing, and "new round-64 paths" |
| F5 (recommended) cite `R64C4MultiPatch.md` in full | applied | §1 status cites `.ufo/waves/round-64/R64C4MultiPatch.md` |

The reviewer separately reports executing the seven census commands clean (35 rows,
malformed 0, empty duplicate/enum/missing output) and confirms the counter's exit
semantics. That is their execution, not this seat's; I reran only the text-identity diff
of the census block and the path/S-id sweeps. No box flip follows from this report: a
fresh verdict on the current hash is the verifier's to give.

### Late precision fix (`HOLDS_OK_V2` legend conjunct)

While the reviewer's report was in flight, a sibling/L1 working-tree edit amended
`reports/round-64/claims.md`'s `HOLDS_OK_V2` wording to add
`README_TOKEN_LEGEND_MISMATCH == 0`. I did not use that uncommitted edit as evidence: the
committed `measure.py` at `3bb430f` already computes `holds_ok_v2` with its own
`len(mismatch) == 0` conjunct, and the writer's earlier reading of the probe shows it.
§6.1 now names the conjunct and keeps the statement that V2 is a diagnostic label not
folded into the exit code. Draft re-hashed (`d66b19d7…c328f6c`, 271 lines); sweep
unchanged: 24/24 lane-relative paths, 11/11 S-ids, census block identical.

## Out of scope (explicit)

No landing, README/C07 flip, knowledge entry, lesson file, counter run, verifier edit,
commit, push, or SHONEN box flip. `SHONEN.md` box 1 stays `[ ]` until a named non-author
verifier passes; L1 owns integration.

## Artifact paths

- Draft: `/tmp/revenger-r64-skill/SKILL.md` (sha256 above).
- Report: `.ufo/waves/round-64/R64SkillDraft.md`.

Report: .ufo/waves/round-64/R64SkillDraft.md
