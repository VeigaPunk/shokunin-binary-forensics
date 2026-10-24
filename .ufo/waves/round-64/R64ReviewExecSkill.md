# R64ReviewExecSkill — non-author review of the operability probe

Reviewed artifact: `.ufo/waves/round-64/exec-skill-run.md` (sha256
`c1447614642091d26e369f1f190b9dffab88bd90b04dd1f5bd7d2260ba8ddee8`, mtime
2026-10-24 01:17:17 -0300) and its seat report `.ufo/waves/round-64/R64ExecSkillRun.md`
(sha256 `87c87319f09c67820ec74c08bf40fdb55a8e5abbc26cd30442ebe2e742e8f05c`), both untracked
at review time. Review clock 2026-10-24T04:19:40Z. Verdict below is a recommendation only.

## Verdict

**NOT CONFIRMED — the transcript contains no executed checklist evidence.** It is a
correct and honest *dependency return*, not an operability run: zero commands were read
from a SKILL candidate, zero were executed, and zero observed exits/outputs exist to
compare against promised outcomes (`exec-skill-run.md:3-10`). SHONEN box 3 ("Instructions
executable by an agent without oral context", `SHONEN.md:9-10`) cannot be evidenced by
this artifact; marking it `[x]` on this run would repeat exactly the author-side-only
weakness the box already records. The seat complied with its brief's fallback ("if absent
at your deadline record the dependency and return") and did not guess or substitute
commands — that is the correct behavior, and it is still not operability evidence.

## Findings by severity

### F1 — High, blocking: no checklist was executed, so no promise is confirmed
`exec-skill-run.md:10` states the census, oracle and frozen-counter commands "could not be
read and were not executed; no command exit codes or last lines are available". The brief
required verbatim execution of those three commands with observed exit codes and last
lines (`briefs/R64ExecSkillRun.md:14`). The document-level question — "do observed
exits/outputs match the promised outcomes?" — has no evidence on either side. This is the
sole reason the verdict cannot be positive.

### F2 — High, confirmed dependency: the candidate really is absent
Independently reproduced at review time, not taken from the transcript:

- At the probe's clock the directory did not exist — the transcript records
  `Path not found: /tmp/revenger-r64-skill` (`exec-skill-run.md:8`); the directory's own
  mtime is 01:19, after the 01:17 probe. At review time (04:20Z) it exists and is
  **empty**: `ls` shows only `.`/`..`, no `SKILL.md`, no `checklists.md`.
- `find` over the lane (unbounded) and `/tmp` (depth ≤4) for `SKILL.md`/`checklists.md`
  finds **no round-64 candidate**; the only `SKILL.md` hits are unrelated earlier-round
  files (`/tmp/r50-revB/SKILL.md`, `/tmp/kotoba-r63-*/SKILL.md`).
- `checklists.md` — the second half the drafting brief names
  (`briefs/R64SkillChecklists.md:14`) — is also absent from the lane (unbounded find) and
  from `/tmp` (depth ≤4).
- Independent seat `R64CriticSkill.md:13` reached the same dependency through the same
  path.

Timeline nuance, observed at review time: `/tmp/revenger-r64-skill/` **now exists but is
empty** (directory mtime 2026-10-24 01:19, after the probe's 01:17 run). So the probe's
negative was true when taken and the dependency is live — a scribe has started but no
candidate bytes existed at 04:20Z. This strengthens, rather than weakens, the finding that
box 3 has no evidence yet: the probe is not stale, the artifact simply never existed.

So the absence claim in the transcript is true, and no better-evidenced candidate exists
elsewhere in the lane. The blocker is upstream (no scribe output), not a probe mistake.

### F3 — Medium: the transcript cannot establish *when* the absence held, nor its search breadth
- No UTC timestamp, nonce or deadline marker appears in the content; the only clock
  evidence is the file mtime. A reader cannot distinguish "absent at the seat's deadline"
  from "probe raced the scribe by seconds", and L1 cannot date the dependency for the
  round report.
- The probe searched exactly one path and its parent (`exec-skill-run.md:5-8`). It did not
  search the lane for an already-integrated copy (e.g. `corpus/SKILL.md`, root `SKILL.md`)
  or for `checklists.md`. My sweep shows no such copy existed, so the conclusion survives
  — but the artifact alone under-evidenced its own negative. A one-line `find` + `date -u`
  receipt would have closed both gaps at zero cost.

### F4 — Medium: the two success signals that any operability document must promise are not exit codes, and the run never tested them
This is the concrete promise trap the absent document would have had to resolve, and the
run confirmed neither side:

1. **Verifier census.** The repo-side command itself carries the caveat: "The census probe
   exits 0 even when constituent verifiers fail; inspect every printed exit code"
   (`SCORECARD.md:29-30`, command block `SCORECARD.md:34-43`). A SKILL promise of "exit 0"
   would therefore be false-green. Executed verbatim from lane root at review time:
   exit `0`, all ten verifiers printed `exit=0`, `CALIBRATION 4 / 4 score= 10.0`,
   `REPLAY 10 / 10`. The green outcome is real but only visible in the *printed* lines.
2. **Frozen counter.** `reports/round-64/measure.py:273` exits
   `2 if not evaluable else 0 if holds_ok else 1` — keyed to `HOLDS_OK` (v1), **not**
   `HOLDS_OK_V2`. At red-before the counter exits `0` while `HOLDS_OK_V2=no`
   (`measure-before.log:46-47`). A SKILL promise of "counter exit 0 ⇒ round green" would
   be false at base. The document must promise the named labels
   (`K_HELD_BACKED`, `README_TOKEN_LEGEND_MISMATCH`, `C4_RECEIPT_KILLED_ATTRIBUTED`,
   `HOLDS_OK_V2`), never the exit code alone.

### F5 — Low, positive: the transcript's cited reference data is accurate and correctly labeled
The ten baseline lines quoted at `exec-skill-run.md:16-21` appear **verbatim** in
`reports/round-64/measure-before.log` (checked line-exact for
`K_HELD_BACKED=`, `K_HELD_BACKED_STRICT=`, `K_ROW C07`,
`README_TOKEN_LEGEND_MISMATCH=`, `C4_CONTROLS_PASS=`, `C4_RECEIPT_KILLED_ATTRIBUTED=`,
`HOLD_CALIBRATION=`, `HOLD_REPLAY=`, `HOLDS_OK=`, `HOLDS_OK_V2=`), and they are explicitly
labeled "saved baseline observations, not results of commands executed for this probe"
(`exec-skill-run.md:23`). No quotation drift and no result laundering.

### F6 — Low, unverifiable but uncontradicted: "no mutations / no installs"
`exec-skill-run.md:23` and `R64ExecSkillRun.md:5-7` assert no tests, formatters,
mutations or installs. This cannot be proven from the artifact. Observed lane delta at
review time (`git status --porcelain`, 73 entries) is consistent with a live wave rather
than this probe: untracked `.ufo/waves/round-64` seat reports (including this seat's two),
the two M35 verifier files modified in the working tree by the C4 seats, and an `M LOG.md`
from another seat. `git diff --stat -- corpus/live corpus/fixtures` is empty, so no
live/fixture byte moved — nothing attributable to this probe. No install was recorded by
it; none was needed.

## Promises the run did not confirm (enumerated from the drafting briefs)

The candidate itself makes no promises — it does not exist. The table below therefore
enumerates the promises the drafting briefs require it to make; every one was left
unconfirmed by the run, and each is independently feasible on today's tree (last column).

| # | Promised item (source) | Run evidence | My independent observation |
|---|---|---|---|
| 1 | Verifier census command + promised outcome (`briefs/R64SkillChecklists.md:14`) | none | green: exit 0, 10/10 printed `exit=0`, CALIBRATION 4/4, REPLAY 10/10 |
| 2 | Firmware oracle `python3 -B corpus/live/runs/round-63/oracle_check.py` (`briefs/R64SkillChecklists.md:14`; promised text `corpus/live/runs/round-63/LEDGER.md:110` — `# ORACLE OK, exit 0`) | none | green: exit 0, five `REGION` lines `…=OK`, last line exactly `ORACLE OK` |
| 3 | Frozen-counter usage `python3 -B reports/round-64/measure.py TREE` over a committed git-archive tree (`briefs/R64SkillChecklists.md:14`) | none | reproduces red-before **byte-identically**: my run on `/tmp/revenger-r64-base` has sha256 `8116b216…` equal to `measure-before.log`, exit 0 |
| 4 | SOURCES census command (`briefs/R64SkillChecklists.md:14`) | none | not executed by me either (outside the three commands my brief names) — gap |
| 5 | Evidence-ledger discipline section per `PROVINCE.md` (`briefs/R64SkillChecklists.md:14`) | none | `PROVINCE.md` exists at lane root; content not assessed (no candidate) |
| 6 | "Every command copied verbatim from files that exist in the repo" (`briefs/R64SkillChecklists.md:14`) | none | unverifiable without the document; and item 1's own source carries the exit-code caveat in F4 |

Base-tree identity for item 3: `/tmp/revenger-r64-base/corpus/README.md` sha256
`f583bd25ed7a367914cad82443b3c09126c3fb5102284898483cd28024b7c01c` equals
`git show 666ea84:corpus/README.md` (read-only), and the tree contains no round-64
knowledge entry. The counter was run with `TMPDIR` under lane-owned scratch. Logs:
`/tmp/revenger-r64-review-execskill/{census-base.log,measure-base.log}`.

## Residual risk

1. The SKILL candidate may land after this review. Box 3 evidence must then be probed on
   the **landed** text (and on the final-tip tree), not on a scratch draft — a later draft
   can silently change the commands that were never run here.
2. The census run at 01:17 was against a working tree carrying the in-flight C4 edits
   (`verify_icon_languages.py:152-153`, `verify_multi_icon_states.py:152-153`); it is green
   now but is not the final-tip measurement, and the frozen counter must still be replayed
   on the committed archive at final.
3. Both reviewed artifacts are untracked; only L1 integration makes them durable. An
   untracked transcript can be lost without a trace.

## Verification gaps

- No `lsp` device/tool exists in this runtime (inventory: read, bash, edit, eval, glob,
  grep, task, wait, web_search, write), so no semantic reference/definition/diagnostics
  checks were possible; none were required for markdown artifacts. Code-side behavior was
  checked by **execution** instead, which is the stronger evidence for an operability
  question.
- The SOURCES census command was not executed (outside the three named commands).
- `checklists.md` absence is asserted from path search, not from a producer report; no
  scribe seat report exists at `.ufo/waves/round-64/R64SkillDraft.md` or
  `R64SkillChecklists.md` at review time.

## Bounds

Read-only apart from writing this report. No git/jj mutation, no commit, no index touch,
no fleet/sibling/registry edits. Small logs under `/tmp/revenger-r64-review-execskill`
(lane-owned prefix). No tools installed or upgraded.

Report: `.ufo/waves/round-64/R64ReviewExecSkill.md`
