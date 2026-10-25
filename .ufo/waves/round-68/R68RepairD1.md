OVERSTATED — the restatements now in committed bytes (LOG.md:925, `corpus/lessons/round-67.md`:130-137, SCORECARD.md:486) claim an abort, a recorded error string and committed per-seat transcripts that the committed bytes do not contain; the same facts are RESTATEMENT-SOUND only in the wording supplied at §4.

# D1 — round-67 routed defect 1: attempt-1 abort evidence (read-only audit)

seat: R68RepairD1 · role: critic · axes read: calibration (evidence standard), depth
bounds observed: no edits outside this file; no git/jj mutation; no seat messaged; tool installs: none.

D1 as routed (`/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/lessons/round-67-verifier-spotcheck.md:219-226`):
the lane rests "all 64 seat transcripts record `stopReason: aborted` / `session_exit: dispose`
(Request was aborted)" on a session-scoped artifact that is not committed. That routing is correct,
and it understates the problem by one item: the lesson also asserts the transcripts *are* committed
(§2.2 below).

## 1 · What the committed bytes actually support

Attempt-1 evidence, all under `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-67/`, all landed in `712ef61`:

| pointer | committed bytes (quoted as printed) |
|---|---|
| `dispatch-start-attempt1.txt:1` | `2026-10-24T21:06:30-03:00` |
| `dispatch-run.log:1` | `Working...` |
| `dispatch-run.log:2` | `All 64 spawned; each agent id equals its member name.` |
| `dispatch-run.log:6-69` | 64-entry JSON map, member name → agentId (`grep -c '": "'` = **64**) |
| `dispatch-run.log:72` | `omp-exit=0` |
| `dispatch-run.log:73` | `2026-10-24T21:07:21-03:00` |
| `dispatcher-prompt.txt:5` (attempt-1 prompt) | `When the task call returns agent ids, print them as one JSON object mapping member name -> agentId, then stop.` |
| `dispatch-start.txt:1` (attempt 2) | `2026-10-24T21:31:45-03:00` |
| `dispatch-run-2.log:3` | `{"reports": 64, "settled": true, "jobs_with_errors": {}, "elapsed_min": 7.4}` |
| `dispatch-run-2.log:6` | `All 64 seats dispatched in one verbatim tool.task call, session held until settlement: 64/64 R67*.md reports on disk at ~7.4 min, zero job-level errors, zero stuck jobs.` |
| `dispatch-run-2.log:7-8` | `omp-exit=0` · `2026-10-24T21:40:25-03:00` |

Derived from those bytes (computed, not copied): attempt-1 span = **51.0 s** (`21:06:30` → `21:07:21`); gap to attempt 2 = 1464 s; attempt-2 span `21:31:45` → `21:40:25` = 520 s.

So the committed bytes support exactly this much, and no more:

1. The task call **did return** all 64 agent ids — one per member name — and the dispatcher printed them (`dispatch-run.log:2`, 64 keys).
2. The attempt-1 dispatcher session then **exited with status 0** 51 s after start (`omp-exit=0`, `21:07:21`). A **clean** exit is what is recorded; no error, no non-zero status, no refusal text is present in that log.
3. The attempt-1 prompt had instructed that session to **stop** as soon as the ids were printed (`dispatcher-prompt.txt:5`). The 51 s exit is therefore *consistent with the prompt as written* and the committed bytes cannot separate "prompt-driven stop, children left running/abandoned" from "session crashed".
4. The 64 seat reports that exist (`ls R67*.md` = **64**) are one complete set, and attempt-2's log claims the same 64 settled at `21:40:25`. No attempt-1-variant report is committed, and **no seat report mentions attempt 1** (`grep -l -i "attempt 1\|attempt-1\|aborted" *.md` → `NONE`).

Negative evidence (the decisive one):

```
$ cd .ufo/waves/round-67 && grep -rl "stopReason\|dead-seats\|Request was aborted" .   →  NONE
$ find . -maxdepth 1 -type f ! -name "R67*.md"   →  14 files, all logs/specs/json; no transcript, no .jsonl
$ find /home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo -name "*transcript*" -o -name "*.jsonl"
    → only .ufo/interactive-sessions/20261015T050057Z/*.jsonl  (2026-10-15, unrelated round)
```

Contrast, from the same repo: round-61 *did* commit the per-seat abort record —
`.ufo/waves/round-61/falsify/dead-seats.json:17` `"last_error": "Request was aborted"` plus
`report_in_lane` / `session_output_bytes` / `assistant_turns` per seat. Round-67 committed no such
file. The string `Request was aborted` **does not occur anywhere in round-67's committed bytes**;
"abort" appears in round-67 only in lane prose (`LOG.md:925`, `SCORECARD.md:486`,
`corpus/lessons/round-67.md:131`).

## 2 · Is the round-68 restatement at that strength?

**There is no round-68 report to check.** `/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/`
holds `audio.md, game-dev-2d.md, kotoba.md, kotodama.md` — no `revenger.md`; the lane's
`reports/round-68/` holds only `claims.md`, `measure.py`, `measure-before.log`. The round-68 build
commit `4232235` (`git show 4232235 | grep -i "abort\|attempt 1\|stopReason"` → no output) contains
**no** attempt-1 restatement, and `LOG.md` has no round-68 entry yet. So D1 is **not yet closed and
not yet re-broken** — the report is where it will either be closed or inherited.

What would be inherited if the report copies the existing lane prose (both are over-strength):

- `LOG.md:925` — "all 64 seats aborted at +51 s (dispatcher session exit disposed the child jobs; 0 seat work, error `Request was aborted` — recorded, no replacement seats)".
  *"aborted"*, *"disposed the child jobs"*, *"0 seat work"* and *"error `Request was aborted` — recorded"* are all **absent** from the committed bytes; the committed exit line is `omp-exit=0`.
- `corpus/lessons/round-67.md:130-137` — "aborted every one at +51 s … (`stopReason: aborted` / `session_exit: dispose` in all 64 seat transcripts, zero reports, zero seat work) … Both attempts are committed as wave evidence (`dispatch-run.log`, `dispatch-run-2.log`, `dispatch-start-attempt1.txt`, **per-seat transcripts under the runtime session dir**)".
  The final clause is a **second, independently checkable falsehood**: the transcripts are *not* committed (§1 negative evidence); no committed artifact even names the runtime session dir, so a non-author cannot locate them. This is worse than the spot-check's §7 item 1 recorded — it is not merely "a session-scoped artifact used as a pointer", it is claimed to be in the wave evidence.
- `SCORECARD.md:486` — "attempt 1 aborted by the dispatcher exit — 0 seat work". Same class: cause-attribution and a seat-work count neither of which the bytes carry.

Every clause of the round-67 prose that goes beyond §1 must not be carried into `revenger.md`.
The lane's falsification and the wave's admissibility do **not** depend on it: the wave's 64 reports,
the second-dispatch timing and the "same taskCall, no replacement" claim (verifiable:
`taskCall.json` sha256 `cf0a111b…5afa`, 64 keys, registry 64 members) all stand on committed bytes.

Footnote (byte-level, not D1-blocking): `dispatch-run-2.log:3` self-reports `elapsed_min: 7.4` while
the file's own timestamps span 8.7 min (520 s). "~7.4 min" is the dispatcher's polled figure; a
report quoting wall-clock must say 8.7 min or say "the dispatcher self-reported 7.4 min".

## 3 · What a non-author still cannot verify from committed bytes

1. `stopReason: aborted` / `session_exit: dispose` for any of the 64 attempt-1 seats — no transcript, digest, or jobs listing is committed (`grep`/`find` in §1); no committed path names the runtime session dir.
2. The literal error string `Request was aborted` for round-67 — present in committed bytes only for round-61. Claiming it for round-67 is an uncredited borrow from another round.
3. **Causality** — that the runtime *disposed* the children because the dispatcher exited. Bytes give temporal adjacency (+51 s) and a prompt that said "then stop"; they cannot distinguish disposal, abandonment, or the seats simply never starting work.
4. **"0 seat work"** — no committed per-seat artifact distinguishes "spawned, no work" from "never started"; the only support is the lane's contemporaneous note in `dispatcher-prompt-2.txt:3` ("Attempt 1 failed: the dispatcher exited right after spawning and the runtime disposed all 64 child jobs") — an L1 assertion, correct in spirit, but not a resolvable observation.
5. That no attempt-1 report was produced and later overwritten by attempt 2 — git stores no per-attempt mtimes; the reports are a single consistent set with no attempt-1 mention, which is *consistent with*, not proof of, "zero reports".

## 4 · The sentence a round-68 report may use (and nothing stronger)

> **Dispatch attempt 1** (`dispatch-start-attempt1.txt` `2026-10-24T21:06:30-03:00` → `dispatch-run.log` `omp-exit=0` at `2026-10-24T21:07:21-03:00`, 51 s): the task call returned all 64 agent ids, one per member name (`dispatch-run.log:2`, 64 keys), and the dispatcher session then exited cleanly (exit status 0) — the attempt-1 prompt had told it to stop once the ids were printed (`dispatcher-prompt.txt:5`). Attempt 1 committed no seat report and no per-seat error record; the per-seat `stopReason`/`session_exit` values are **not committed and are not claimed here**. **Attempt 2** re-dispatched the byte-identical `taskCall.json` (same 64 names, same order; sha256 `cf0a111b…`) from `21:31:45` to settlement at `21:40:25` (`dispatch-run-2.log` `omp-exit=0`; `{"reports": 64, "settled": true, "jobs_with_errors": {}, "elapsed_min": 7.4}` — wall clock 8.7 min), producing the 64 committed `R67*.md` reports. No replacement seat was spawned: the registry is 64 members and the report set is 64 files.

Forbidden in the round-68 report (each unsupported by committed bytes): "all 64 seats aborted";
"error `Request was aborted` — recorded"; "`stopReason: aborted` / `session_exit: dispose` in all
64 seat transcripts"; "the runtime disposed the child jobs" stated as fact; "per-seat transcripts
committed as wave evidence"; bare "0 seat work". If the causal reading is wanted at all it must be
tagged, e.g. "as observed live by the L1 at dispatch time; not committed — [INFERENCE]".

## 5 · Smallest safe correction

One edit, no artifact needed: replace the round-shape sentence in `corpus/lessons/round-67.md`:130-137
with §4's wording (and drop the parenthetical claiming the transcripts are committed), and make
`LOG.md:925` and `SCORECARD.md:486` read "attempt 1 exited cleanly +51 s after the ids were printed;
no attempt-1 report or per-seat error record is committed" instead of "aborted … 0 seat work …
error `Request was aborted` — recorded". If the lane wants the strong claim in a future round, the
cheap evidence is a committed redacted digest: one line per seat with `stopReason`/`session_exit`
copied from the runtime session dir at dispatch time (`round-61`'s `dead-seats.json` is the shape).

Impacted axes: **calibration** (evidence standard; the overstated clause is the only calibration
liability in D1 — no counter label, hold, or gate result depends on it) and **depth** (a reader
cannot reconstruct attempt 1 from the report today). Not impacted: coverage, C1/C2 predicates,
`reports/round-68/measure.py` sha256 `0de4eb6f…7766`, the 64-seat wave count and its no-replacement
claim.

## Evidence index (sha256, all re-hashed by this seat)

```
86ab5342defb697a74594c5122d4baabc44f56b7d34ae4caf9e7d369feb5f850  dispatch-start-attempt1.txt
ecc09eecee100d152dcf36108e3932dbf8b4f5cf51defae0dfeb6543d9397be8  dispatch-run.log
5cdd3ea91a064b1634da33458dbaa0d5eb246626849be7ae8c584fe78958ec69  dispatcher-prompt.txt
9b6820a3ab4109ad46f901494553d3035e7e8e5e079223d3ec98508363856780  dispatch-start.txt
d5c1da24ddc4711c5bf69ced09020dcf7193798cd7a86d8848cd5116618347cc  dispatcher-prompt-2.txt
7af598129cbb2a2a3f5d401143b7121d5f77b4a0998c41ed9f19760f7d89312a  dispatch-run-2.log
cf0a111b4b63356a19a0335eab96f64ee0f43b1016f9fe2368a494bc11ad5afa  taskCall.json
```

residual: the runtime session dir referenced by `corpus/lessons/round-67.md:136` is not named in any
committed file, so this seat could not open the transcripts even as live state; nothing in this
report depends on them.
