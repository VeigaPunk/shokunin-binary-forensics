# Fleet round-1 scribe record — report/LOG/SCORECARD map, SHONEN boxes, commits, inherited defects

Role: `ReplayScribe` (scribe). Scope: sole write `reports/round-1/scribe.md`; every other
path read-only. No producer calls, no fixture execution, no build/lint/test/formatter run,
no commits or pushes, no delegation. This record maps what integration must produce and
names inherited defects; it contains **no** result of the repaired verifier, because this
scribe did not run it (contract: parent runs acceptance once after integration).

Evidence discipline below: **[OBSERVED]** = read from a named path/command in this session;
**[INFERENCE]** = conclusion drawn from those observations; **[UNKNOWN]** = not established.

## 0. Inputs read (authority order)

- `reports/round-1/brief.md` (authority; re-read after a live edit — the *Live round
  clarification* section corrected coverage to a fixed **eight**-family proxy and preserved
  the inherited 3/7 count as originally measured). [OBSERVED]
- `reports/round-1/baseline.txt` (36 lines; failure + two counting commands + census). [OBSERVED]
- `reports/round-1/dispatch.json` (inherited intent, 9 members) and
  `reports/round-1/batch-receipt.json` (live receipt, `observed_spawn_count: 9`). [OBSERVED]
- `LOG.md` (729+ lines; fleet round-1 declaration now at `LOG.md:723`),
  `SCORECARD.md` (13 lines), `SHONEN.md` (8 lines), `PROVINCE.md` (25 lines),
  `README.md` (22 lines). [OBSERVED]
- Fleet authority: `/home/vgpnk/Projects/shokunin/PROTOCOL.md`, `AXES.md`, `CORPUS.md`,
  `MISSION.md`, `templates/round-prompt.md`. [OBSERVED]
- Lane code/fixtures: `corpus/verify_named_multi_icon_states.py` (97 lines) plus the three
  sibling PE-state verifiers; `corpus/fixtures/pe-r55|56|57/fixture.exe` (each 1536 B);
  `corpus/live/runs/round-55|56|57/{inspection.raw.json,receipt.json}`;
  `corpus/live/runs/round-58/reviewer.md`; `corpus/fixtures/REPLAY.md`;
  `reports/round-59/*`. [OBSERVED]
- Not read: any peer report contents (planner/critic were still landing at write time), the
  remaining ~50 run directories beyond targeted greps, and any producer output. [UNKNOWN by omission]

## 1. Required report sections — ordered map

Two contracts apply simultaneously; the stricter reading wins for closure.

**A. Report path, name, ordering (PROTOCOL.md "Round-robin rounds" + round-prompt §5).**
1. Path/name: `.ufo/reports/round-<N>/<id>.md` in the fleet repo, `<id>` = roster id
   (`revenger` for this lane). A file under another name does not satisfy the contract.
2. Commit-before-report: the lane report **lands last** and cites the child-repo commit that
   carries the round's work; a hash the repo does not contain fails, a non-ancestor hash at
   closure is a conformance defect (`git merge-base --is-ancestor <hash> HEAD`).
3. The commit that adds the report carries the lane identity; a later fleet-level sweep is
   recorded as an attribution defect, never repaired by rewriting history.
4. Lane-round write scope for this dispatch: `reports/round-1/**` inside the lane repo for
   the scribe; parent owns LOG/SCORECARD/docs/commits (brief "Roles and ownership").

**B. Required sections, in this order (round-prompt §4).**
1. **Work performed** — one bullet per work item, each with an evidence pointer
   (path:line, command output, or commit hash).
2. **Landed changes** — every change tied to a `LOG.md` entry *and* to the commit hash that
   carries it.
3. **Before → after measurements** — one per claim, each with its counting command and the
   commit it was measured against.
4. **SHONEN** — one line per `SHONEN.md` box; `[x]` only with a named non-author verifier,
   `[~]` with a resolvable evidence pointer, `[ ]` if untouched.

**C. Minimum content (PROTOCOL.md "Minimum content").** work performed + evidence pointers;
changes landed in the child repo each tied to a `LOG.md` entry; cross-domain evidence
encountered with its owning domain; a `SHONEN` checklist under a **`SHONEN` heading** (the
heading itself is required — same facts elsewhere do not satisfy the contract; a report
missing it is a conformance defect *and* disqualified as promotion evidence for that lane).

**D. Five child-lane items** the dispatched prompt must embed verbatim (PROTOCOL.md; template
§4–§5): report path and filename; commit-before-report ordering; the `SHONEN` heading
requirement; the commit-hash citation rule; the lane's write scope. This dispatch's operative
text is `reports/round-1/brief.md` + the task ticket, which carry all five. [OBSERVED]

**E. Marker vs report.** A contentless completion marker at the report path closes nothing;
a short report naming a real committed round-work hash is `ok` + a minimum-content defect;
no work + no pointer + no resolvable commit = `failed`. [OBSERVED: PROTOCOL.md, round-prompt §4 marker rule]

## 2. SHONEN box map (all four boxes)

`SHONEN.md` carries exactly four boxes, all currently `[x]`, plus a closing no-promotion
paragraph. Required rendering after integration: one line per box **under a `SHONEN` heading**
in the round report, with the marker grammar of §1B4.

| # | line | box (compressed) | current `[x]` verifier cited | gap / what integration must decide |
|---|---|---|---|---|
| 1 | `SHONEN.md:3` | real decision tables / error patterns / checklists with cited sources | non-author `revenger-promotion-review` (`corpus/live/runs/promotion-review-r5.md`) against `corpus/knowledge/2026-10-12-rea-readiness-checklist.md` + r1 refusal | PROTOCOL box-1 bar names a **`SKILL.md`** decision table + error-pattern list + checklist. `SKILL.md` does not exist at repo root (`ls -a .`; README.md:11 discloses "absent on lanes still in shonen seed form"). The box rests on `corpus/knowledge` content instead — materiality is a promotion-gate question, not this round's D1 fix. |
| 2 | `SHONEN.md:4` | end-to-end domain task executed and logged; non-author verifier required | `revenger-r1-r3-independent-reviewer` + `revenger-promotion-review`; r2 `ev_cc681c2a…`, r3 `ev_4a93276c…` | Box is explicitly scoped to fixture-scoped provider-neutral ZIP inventory + static JS; it does **not** assert r1 native session or runtime. Unchanged by this round. |
| 3 | `SHONEN.md:5` | instructions executable without oral context for fixture recreation and saved-result verification | non-author `fixture-replay-review` (`corpus/live/runs/round-5-review.md`), assessed by `revenger-promotion-review` | The cited instruction text (`corpus/fixtures/REPLAY.md` steps 1–4) still names `.shokunin/revenger/corpus/...` paths that do not resolve in this checkout. The relocated-replay round is the first work that can re-support this box; until then the `[x]` is stale against repo state. |
| 4 | `SHONEN.md:6` | no cross-domain bleed; `PROVINCE.md` remains accurate for reviewed rounds 1–5 | `revenger-promotion-review` (path/round check) | `PROVINCE.md:25` still says "Only writes `.shokunin/revenger/**` and its own reports." No `.shokunin/` directory exists in this checkout. In its current bytes the box's "PROVINCE remains accurate" clause is falsified; parent repairs the write path or re-scopes the clause. |

Closing paragraph (`SHONEN.md:8`): evidence checks, **not** a rank promotion; native readiness
not established (r1 `provider_unavailable`); `SHONEN.md` stays; no `MANIFEST.json` edit implied.
[OBSERVED]

**Author-side limit (hard).** Every reviewer named in §2 was dispatched by the lane
(PROTOCOL: "a subagent the lane dispatched is still the lane"), and this round's L2 batch is
likewise author-side (`batch-receipt.json` `independence` field; brief "Roles and ownership").
Our dispatched roles can therefore contribute at most `[~]` pointers with named authors;
`[x]` requires a **non-author verifier outside the lane**. Do not render any box `[x]` on the
strength of this batch, and do not cite this scribe record as an outside spot-check.

## 3. LOG field map (append-only)

**Fleet round-1 declaration — already written by the parent** at `LOG.md:723-729` (worktree;
`git status` shows ` M LOG.md`). Observed field order and content:
`## Fleet round-1 declaration — relocated saved-ledger replay`, then bullets:
- `Authority:` fleet `MISSION.md:38-60`, `AXES.md:25-39`; not a renumbering of historical r1–r60; baseline commit.
- `Motivation:` the inherited failure (`baseline.txt:4-23`), the defect site
  (`corpus/verify_named_multi_icon_states.py:57-70` at baseline), and the frozen historical
  corpus path.
- `Single claim:` pin historical producer path independently; replay from lane root, unrelated
  CWD, copied corpus with spaces/non-ASCII; no fixture/Evidence/receipt rewrite; forgeries must still fail.
- `Imported SCORECARD scores were unassigned.` + the bounded calibration proxy `10 × runnable
  cross-record PE state verifiers / 4`, before 1/4 (2.5), expected after 2/4 (5.0), non-global;
  coverage proxy separately counted, not runtime readiness; r59 halt preserved.
- `Dispatch:` one native call, nine roles, `batch-receipt.json` as actual receipt, `dispatch.json`
  as intent; host routing, no model params; L2 = author-side.

**Still required (missing at write time) [OBSERVED as absent]:**
- A `## Fleet round-1 result …` entry. Convention from the historical rounds: result heading
  with outcome phrase, then bullets — (a) input facts with SHA-256/byte length/byte-level delta;
  (b) producer/verifier command + exit + Evidence IDs + stdout SHA + saved paths; (c) the
  non-author leaf reports by name; (d) `- Per-axis verdicts:` improved/unchanged/harmed per axis
  with narrowness qualifier and admit/not-admitted; (e) `UNKNOWN:` list; (f) push/merge statement.
- A telemetry/correction entry if any sub-lane command fails (pattern: `## Round 58
  implementation telemetry`, `Round 59 falsification/telemetry`) — the scan is append-only and
  the *brief's* "Live round clarification" (coverage 7→8 families) belongs in LOG as a declared
  correction, since LOG currently carries only the six-family-era rubric sentence. **[INFERENCE]**
  that this correction is required for LOG/SCORECARD consistency; the brief states it as binding.
- Corrections are appended, never rewritten in place (PROTOCOL + CORPUS: "Corrections are new entries").

**LOG conventions integration must imitate (observed in r55–r60 entries):** ISO-8601 UTC
timestamps on declaration/result headings; `BEFORE:`/`CLAIM:` on one bullet; `Owned axes:`
target + guardrails + explicit no-execution/no-push boundary; a `Wave spec before spawning`
table `| name | role | model | scope | artifact path |` — **note**: historical tables hardcode
model aliases (e.g. `openai-codex/gpt-6-luna`), which the fleet round-1 contract forbids
("no model parameters/config edits"; host taxonomy routing) — so the round-1 wave spec must name
roles and routes, not model aliases. Every result entry ends `No push or merge.`

## 4. SCORECARD field map

Contract (`AXES.md` "SCORECARD.md contract"): `axes` → axis name → **score 0–10** → evidence
pointer → last-change round; `planned` → the single next axis-move; `retired` → axes retired
with justification. Round-prompt §2.5 adds: record the **new score, the evidence pointer, the
counting command, and the commit it was measured against**.

Current file state [OBSERVED]: 13 lines; preamble `SCORECARD.md:3-4` ("Scores remain unassigned
without a quality rubric; a row count is a measurement, not a score or verdict"); table header
`:6`; three rows `:8` (depth), `:9` (coverage), `:10` (calibration), each score cell
`unmeasured`; `planned:` `:12`; `retired: none.` `:13`.

Required after integration:
- calibration row: score `5.0` with the counting command
  (`python3 -B corpus/verify_named_multi_icon_states.py` plus the four-script census) and the
  work-commit hash; last change = fleet round-1.
- coverage row: corrected **eight-family** presence proxy `4/8 ≈ 5.0` (same seven families plus
  `inspect_evm_interface`), keep the inherited 3/7 as "as originally measured" per the brief's
  live clarification; counting command from `baseline.txt` with the EVM family added.
- depth row: retained but marked unchanged/wrong-fit for this assignment (brief: "historical
  depth retained, retired as wrong-fit for this lane assignment"); the `retired:` line must carry
  the justification if depth is actually retired — the two statements must not contradict.
- every carried-forward row command that still reads `.shokunin/revenger/corpus/...` is stale in
  this checkout (see D3) and must be rewritten to the lane-root path or annotated.
- `planned:` must name this round's successor move (single), replacing the current
  `planned: r60 (devin) …` text.

## 5. Commit map

- Lane identity for round commits: `revenger-shokunin <revenger@shokunin.local>` (`LOG.md:5`
  Mint entry). [OBSERVED] 36 of the last 40 commits carry it.
- Subject convention: `revenger r<NN>: <what changed>` (e.g. `a37e63c revenger r58: verify named
  icon states across saved evidence`; `a9f6f67 revenger r59: retain falsified malformed-name
  refusal`). r60 used `7b24897 revenger r60 (devin): named resource-type fixture — coverage improved, verified`.
- Baseline / start-of-round HEAD: `286033c5f2b1683fb538e86e15667709bb49b054`, subject
  `Revert "HOURS.md: craft-hours ledger opened (§Craft-hours canon)"`, author `ci <ci@local>`.
  Above it: `6587d32` (HOURS, reverted), `176e8d4` (README lane card), `7b24897` (r60).
- Remote: `origin https://github.com/VeigaPunk/shokunin-binary-forensics.git` — the lane's own
  remote; pushes limited to it and the fleet repo.
- Required this round: (1) work commit(s) carrying the verifier repair + any parent-owned doc
  repairs, authored by the lane identity; (2) report commit(s) under `reports/round-1/`;
  (3) the report's cited hash must be an ancestor of `HEAD` at closure. [OBSERVED rule, PENDING execution]

## 6. Inherited defects (named, with evidence pointers)

**D1 — frozen historical producer path vs current-path identity (in scope: the one move).**
`corpus/verify_named_multi_icon_states.py` sets `ROOT=Path(__file__).resolve().parent` (:6) and
derives `fixture=ROOT/f'fixtures/pe-r{r}/fixture.exe'`; it then compares that current path with
saved strings at `:58`/`:63` (`expected` artifact path), `:67` (`normalized_result.artifact`),
and `:69-70` (expected `receipt['command']`). Saved records hold
`/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus/fixtures/pe-r55/fixture.exe`
in both `corpus/live/runs/round-55/inspection.raw.json` and `…/receipt.json`. Result:
`exit 1`, `AssertionError: r55 artifact` (`baseline.txt:4-6`). Line numbers here are against the baseline
revision `286033c5f2b1683fb538e86e15667709bb49b054`; the implementation lane modified this file
in the worktree while this record was being written (see §8, "touched surface"). [OBSERVED] `:70` would fail next
(`r55 receipt`) once `:67` passes, so a fix touching only the artifact comparison is incomplete
**[INFERENCE]** from reading the assert order. The brief's bar — "never accept a path by copying
it out of the field under test" — excludes the trivial repair of reading `artifact.path` back
out of the saved JSON, and also excludes reusing the saved `command` string as the expectation.

**D2 — same defect class in two sibling rubric scripts (out of scope by brief).**
`corpus/verify_multi_icon_states.py:130` (`artifact==dict(path=str(fixture)…)`) fails
`r42: artifact`; `corpus/verify_icon_languages.py:127` fails `r47: artifact`;
`corpus/verify_icon_states.py:131-132` compares only `artifact['sha256']`/`bytes`, so it passes.
`baseline.txt` counting command shows `REPLAY 7/10` and the three PE-state exits. Only the named
verifier may change this round (brief: expected 8/10), so D2 remains open debt after round-1.

**D3 — old write path asserted in lane docs/commands.** `PROVINCE.md:25` claims writes under
`.shokunin/revenger/**`; no `.shokunin/` directory exists here. SCORECARD rows and many LOG
result bullets still cite `.shokunin/revenger/corpus/...` commands, and `corpus/fixtures/REPLAY.md`
steps 1–4 do the same. 136 files under the lane contain the historical `prymeagnt` path. [OBSERVED]

**D4 — unassigned SCORECARD scores, no rubric.** `SCORECARD.md:3-4`, rows `:8-10` = `unmeasured`.
[OBSERVED]

**D5 — missing craft/index files.** `CORPUS.md` layout requires `corpus/README.md` (index:
coverage map, known gaps, frontier) and `corpus/QUALITY.md`; neither exists (`ls corpus`;
`ls corpus/QUALITY.md` → No such file). `README.md:13-14` asserts `QUALITY.md` "(the admission bar)"
is part of `corpus/` — the claim does not resolve. `corpus/lessons/` holds only
`2026-10-12-r1-provider-gap.md`, which carries no `## Gate` section and is not named
`round-<N>.md`; neither `corpus/knowledge/*.md` file carries the required
`source:` / `verified-at:` / `recheck:` lines (`grep` over both files returned no matches).
`SKILL.md` is absent (README.md:11 discloses this). Parent owns "corpus admission lesson/index".
[OBSERVED]

**D6 — r60 attribution defect.** Commit `7b24897` is authored by
`games-engine-mechanics-shokunin <games-engine-mechanics@shokunin.local>`, not the lane identity;
`LOG.md`'s Mint entry fixes the lane identity. History is never rewritten to fix attribution —
record it in the round notes. [OBSERVED]

**D7 — declared intent vs live roster.** `dispatch.json` declares nine seats including
`ReplayScenarios`; `batch-receipt.json` reports `observed_spawn_count: 9`; the peer roster visible
to this scribe at write time lists seven subagents (`ReplayPlanner`, `ReplayConnector`,
`ReplayImplementation`, `ReplayScout`, `ReplayReviewer`, `ReplayCritic`, `ReplayInputLedger`) plus
`Main`, and `reports/round-1/scenarios.md` was absent from the directory listing
(landed at that moment: `planner.md`, `critic.md`). [OBSERVED snapshot; bounded] This states an
observation about roster/output visibility, not a claim that the seat was never spawned.

**D8 — halted calibration criterion (preserve).** r59's malformed-UTF-16 refusal prediction was
falsified (`LOG.md:713-717`; `ev_8ab30e10…` succeeded where refusal was predicted) and calibration
progression was halted pending a newly declared criterion or operator ruling. The round-1
repeatability proxy must not be presented as regrading r59. [OBSERVED]

**D9 — coverage proxy taxonomy gap (measurement repair).** The inherited seven-family presence
proxy omits the already-recorded EVM surface (`inspect_evm_interface`, 7 saved records in
`baseline.txt`). Brief's live clarification fixes the proxy at eight families: before `4/8 = 5.0`,
preserving 3/7 as originally measured. [OBSERVED]

**D10 — wave-spec table convention vs no-model-params contract.** Historical wave tables name
model aliases; the fleet round-1 contract routes by host taxonomy with no model parameters.
[OBSERVED, LOG:55x/r700s tables]

## 7. Metadata repair vs a second axis move

The round is **one** axis move: calibration, measured by the declared repeatability proxy
(1/4 → 2/4 of the four cross-record PE state ledgers; 7/10 → 8/10 of the ten-verifier census).
Everything in D3, D4, D5, D6, D9 is **required metadata/record repair**, not an additional axis
move: it restores accuracy of `PROVINCE.md`, `README.md`, `SCORECARD.md`, `LOG.md` and the corpus
index to the current checkout, and it must not be scored as depth/coverage gain. D1 is the single
axis move's substance (the verifier repair); D2 is explicitly excluded from this round; D7/D8/D10
are record/telemetry items. Any claim that coverage improved this round would be a second axis
move and is **not** declared in the brief.

## 8. Minimal author-side assessment

[INFERENCE], from reading `corpus/verify_named_multi_icon_states.py:55-73` and the saved records —
not from execution: pinning one independently chosen historical path constant and using it for
both the expected `normalized_result.artifact` (`:58`/`:67`) and the expected receipt `command`
(`:69-70`) is necessary for the saved r55–r57 checks to reach the later assertions (order, byte
deltas, both forged-claim rejections at `:90-96`), while continuing to read fixture bytes from the
present corpus and to keep the hardcoded Evidence IDs/digests (`EXPECT` at `:55`:
r55 `41c0132a…`/`ev_db785aec…`, r56 `911f96b3…`/`ev_44be7fd7…`, r57 `71d11fba…`/`ev_068eb9b6…`).
The Evidence IDs are path-sensitive (`ev = f(content, path, params)` — r60 verifier finding,
`reports/round-59/r59-devin-verifier.md`), which is precisely why the *historical* path must be the
pinned identity rather than any current path. Sufficiency is **[UNKNOWN]**: I did not run the
verifier, and the acceptance set (unrelated CWD, copied corpus under spaces/non-ASCII path,
historical-path and receipt-command forgeries) is the parent's single post-integration run.

**Touched surface observed at write time (unverified).** `git status` shows
` M corpus/verify_named_multi_icon_states.py` — the only corpus change in the worktree — with
`git diff --stat` = 1 file changed, 9 insertions(+), 7 deletions(-). The diff adds
`HIST=Path('/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/corpus')` with the comment
that it is "identity for saved artifact paths/receipt commands only, never read through it", and
routes `hist=HIST/f'fixtures/pe-r{r}/fixture.exe'` into the normalized-result artifact expectation,
the `r{r} artifact` assertion, the receipt `command` expectation, and the forged-control call,
while fixture bytes continue to come from `ROOT/f'fixtures/pe-r{r}/fixture.exe'`. That shape matches
the brief's two prohibitions (no path copied out of the field under test; no rewrite of saved
records) **[INFERENCE from the diff text]**; whether it exits 0 is **[UNKNOWN]** here — this scribe
did not run it. No LOG/SCORECARD/README/PROVINCE/corpus-index repair is visible in `git status` yet,
so D3/D4/D5/D9 remain open at write time.

## 9. Ready evidence checklist (integration gate)

State markers: **[OBSERVED]** already true in the repo at baseline/write time; **[PENDING]**
requires the parent's post-integration run or write; **[NOT CLAIMED]** explicitly outside this
round and must not be asserted anywhere.

- [OBSERVED] C1 baseline failure and root cause: `baseline.txt:4-6` exit 1 `r55 artifact`;
  defect sites `corpus/verify_named_multi_icon_states.py:58,63,67,69-70`; frozen saved path in
  `corpus/live/runs/round-55/{inspection.raw.json,receipt.json}`.
- [OBSERVED] C2 historical inputs present and unmodified at baseline: `pe-r55/56/57/fixture.exe`
  1536 B each; digests `41c0132a…`, `911f96b3…`, `71d11fba…` (`EXPECT` + LOG r55–r57 results);
  Evidence IDs above; `receipt.json` present for r55/56/57 (`producer-receipt.json` for the
  sibling rounds).
- [PENDING] C3 lane-root acceptance: `python3 -B corpus/verify_named_multi_icon_states.py`
  exit 0 with its PASS line (baseline line was `PASS: 139 positive checks; 2/2 forged claims
  rejected` before relocation — the count may differ legitimately only if checks were added, which
  the brief forbids as "extra feature").
- [PENDING] C4 unrelated-CWD run and a copied corpus under a path containing spaces and non-ASCII
  characters, with the same exit 0 (real CLI execution, no mocks).
- [PENDING] C5 unchanged-history census after the repair: no diff to `corpus/fixtures/**`,
  `corpus/live/runs/**` (fixtures, `inspection.raw.json`, `receipt.json` bytes/hashes).
- [PENDING] C6 forgery rejections still fail: r56 candidate-index forgery and r57 size-match
  forgery (verifier `:90-96`), the round-58 reviewer's name-location and ancestor-entry-location
  challenges, **plus** the newly required historical-artifact-path and receipt-command forgeries.
- [PENDING] C6b verifier diff reviewed by the parent for scope: the only worktree change is the
  pinned `HIST` constant and its four use sites (§8 touched surface); no saved JSON, receipt or
  fixture byte is modified (`corpus/fixtures/**`, `corpus/live/runs/**` clean in `git status`).
- [PENDING] C7 counting commands with the measured commit: four-script rubric 2/4 (=5.0) and
  ten-verifier census 8/10; eight-family coverage presence 4/8 preserved alongside the inherited 3/7.
- [PENDING] C8 LOG result entry (+ telemetry/correction entries) and SCORECARD cells carrying
  score, evidence pointer, counting command and commit hash; `planned:`/`retired:` reconciled.
- [PENDING] C9 SHONEN block under a `SHONEN` heading, one line per box; `[~]` with pointer for
  author-side evidence, `[x]` only with a named **non-author** verifier outside the lane; box 3/4
  caveats from §2 recorded.
- [PENDING] C10 doc repairs: `PROVINCE.md:25` write path, `README.md:13-14` corpus claim,
  `corpus/README.md` + `corpus/QUALITY.md` (create or correct the claim), first
  `corpus/lessons/round-1*.md` admission lesson with a `## Gate` section, `corpus/fixtures/REPLAY.md`
  path updates.
- [PENDING] C11 commit + attribution: work commit authored `revenger-shokunin
  <revenger@shokunin.local>`; report commit under `reports/round-1/`; cited hash ancestor of `HEAD`;
  r60 attribution defect (D6) recorded in the round notes, not rewritten.
- [NOT CLAIMED] producer authentication, REA rerun, PE/EVM execution, native provider readiness,
  portability of the toolchain, any promotion or outside-discernment verdict, and any regrade of
  the halted r59 criterion.

## 10. Evidence limits of this record

Read-only static inspection plus data-only census (directory listings, `grep`, `git log/status`,
line counts). No verifier run, no CLI acceptance, no producer call, no fixture execution, no
build/lint/test/formatter. All line numbers are against the worktree at write time
(`LOG.md` was being appended by the parent concurrently: it grew from 729 to 730 lines and the
fleet round-1 declaration sat at `:723` when cited). Peer reports were not read for content;
their existence is cited only as an observation about files present at that moment. This record
grants no promotion, no outside spot-check and no independent verification of any sibling's work.