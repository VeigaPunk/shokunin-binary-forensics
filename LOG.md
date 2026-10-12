# revenger append-only log

## Mint 2026-10-12
- Explicit operator directive; no craft round, no verdict or promotion yet.
- Evidence: .shokunin/mints/revenger.md; seed knowledge: corpus/knowledge/seed.md.
- Lane git identity for all round commits: revenger-shokunin <revenger@shokunin.local>.
- Next falsifiable move: declare one axis-move claim, cite before/after, named non-author review, L1 closure.

## Round 1 declaration — coverage (2026-10-12)
- BEFORE: no REA session opened on this host; no scored REA finding on a ground-truth fixture (mint readiness checklist).
- CLAIM: acquire `rea-agents@6.4.0` via npx, open a REA session on `corpus/fixtures/checksum-r1/checksum` built from the local C source, run advertised inspection, and record each finding as OBSERVATION/INFERENCE/UNKNOWN with Evidence IDs, source-truth precision and missed/wrong gap list. AFTER qualifies only with an actual session Evidence ID and scored comparison under `corpus/live/runs/<timestamp>/`. If engine/provider unavailable, record the refusal and judge coverage unchanged; setup is not a pass.
- Owned axes judged: coverage (target), depth and calibration (guardrails). No runtime target execution is authorized beyond fixture compilation; REA static inspection only.
- Wave 1 spec (parallel LEAF workers; all read-only except their individual report files under `.shokunin/revenger/corpus/live/runs/round-1/wave/`):
  | name | role | model | scope | artifact path |
  |---|---|---|---|---|
  | fixture-truth | scout | openai-codex/gpt-6-luna | source truth inventory | `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum.c` |
  | fixture-provenance | reviewer | openai-codex/gpt-6-luna | compiler/build provenance and behavior | `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum` |
  | rea-cli-map | scout | openai-codex/gpt-6-luna | npx CLI supported syntax, no REA session | `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum` |
  | native-route | scout | openai-codex/gpt-6-luna | native provider readiness and static route | `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum` |
  | truth-score | critic | openai-codex/gpt-6-luna | independent scoring rubric | `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum.c` |
  | evidence-ledger | reviewer | openai-codex/gpt-6-luna | Evidence ID discipline checklist | `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum` |
  | scope-sentinel | sentinel | openai-codex/gpt-6-luna | static/no-live-target boundary and scope | `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum` |
  | gap-auditor | critic | openai-codex/gpt-6-luna | expected gaps without Ghidra; bounded claims | `.shokunin/revenger/corpus/fixtures/checksum-r1/checksum` |
- Workers are leaves (no recursive spawning); one writer per report; integrate while running. Wave failures are telemetry, not a reason to erase the round.

## Round 1 result — 2026-10-12, claim unmet
- Fixture source and build provenance: `corpus/fixtures/checksum-r1/README.md`, binary SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`.
- `npx -y rea-agents@6.4.0 analyze <absolute fixture path> --format json`: exit 1 `provider_unavailable` (Ghidra/Hopper/IDA rejected), full diagnostic at `.shokunin/revenger/corpus/live/runs/20261012T163909Z/native-analyze.json`. Provider-neutral `inspect-artifact` succeeded and returned IDs `ev_dd509246a007f8e57b150678116da8895e0bea842093bb56aca525f1b886ab2c` and `ev_ad931089830ba05c0b3d7b1b3b9021826963bd5e66bd5638cfd23c50489309a8` for metadata only (`.shokunin/revenger/corpus/live/runs/20261012T163909Z/LEDGER.md`).
- Independent leaf wave: eight reports in `corpus/live/runs/round-1/wave/`, including `truth-score.md` rubric; all completed. Source behavioral recall 0/6, precision N/A; no opened native session. Artifact-level observation groups 4/4 checked correct; separate from behavior.
- Per-axis verdicts: coverage **unchanged** relative to claimed native end-to-end readiness (artifact inventory is a narrower partial gain, not the declared move); depth **unchanged** (no native code analysis); calibration **improved** (independent scoring rubric plus explicit provider-failure boundary and Evidence ID ledger). The incidental calibration improvement is retained; the declared coverage axis move is **not admitted**. Do not promote native readiness or claim round-1 end-to-end success. Further coverage progression halted until provider readiness or a newly declared route claim.

## Round 2 declaration — coverage (2026-10-12)
- This is a **new provider-neutral archive-inventory route**, not a rerun of round-1 native-session claim. BEFORE: no REA inspection of a locally built archive fixture with known member names, content digests, and sizes.
- CLAIM: run `inspect-artifact` on `corpus/fixtures/archive-r2/fixture.zip`, score all returned root and member identities against an independently recorded ZIP manifest, and log Evidence IDs. AFTER counts as coverage improvement only if both member identities and root identity match truth; report any extraction/semantic gap separately. The ZIP is not executed and no native provider is installed.
- Owned axes: coverage target; depth and calibration guardrails. The eight-worker wave from round 1 is closed; round 2 uses a single direct REA inspection plus independent host ZIP manifest comparison, no sublanes dispatched. Commit then report; no push or main merge.

## Round 2 result — 2026-10-12, provider-neutral archive route
- `inspect-artifact` on `.shokunin/revenger/corpus/fixtures/archive-r2/fixture.zip` succeeded; Evidence IDs `ev_5cc39f356009773bb3d8a214ec39536a99f0799f6709f4cd7bb3badb33c6cf7d` and `ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b`; full result `.shokunin/revenger/corpus/live/runs/20261012T164246Z/artifact-inspection.json` and comparison `.shokunin/revenger/corpus/live/runs/20261012T164246Z/LEDGER.md`.
- Before: no fixture ZIP had REA Evidence-ID-backed root+member inventory. After: root SHA/format/size and two member path/hash/size identities match `truth.json`, identity precision 3/3 and recall 3/3. Re-run the independent check command in `LEDGER.md` -> `True True`.
- Per-axis verdicts: coverage **improved** for the newly declared provider-neutral archive inventory route; depth **unchanged** (no function analysis); calibration **unchanged** (r1 behavioral rubric retained, no overclaim). Admit this route-specific round, but native-session readiness from r1 remains blocked. Next falsifiable move could target extraction identity or JavaScript static semantics if a known-source fixture warrants it; no automatic escalation to live targets.

## Round 3 declaration — depth (2026-10-12)
- BEFORE: provider-neutral fixture inspections gave identity only; no REA static semantic claim had been compared with known source.
- CLAIM: on a small authored JavaScript application tree, run `analyze-javascript-application` (not native session), identify one cited REA Evidence-backed static semantic relationship (e.g., module import/export or literal string) matching known source, and name what syntax analysis cannot prove. AFTER counts as depth improvement only if an actual semantic claim, not mere file inventory, is correctly checked against source. Keep runtime behavior UNKNOWN.
- Owned axes: depth target, coverage and calibration guardrails. No workers needed for the bounded known-source fixture; no target code execution. Commit work then report, no push or merge.

## Round 3 result — 2026-10-12, static JavaScript relationships
- `analyze-javascript-application` on `corpus/fixtures/js-r3/` returned Evidence ID `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`; full output `.shokunin/revenger/corpus/live/runs/20261012T164357Z/analysis.json`; ledger `.shokunin/revenger/corpus/live/runs/20261012T164357Z/LEDGER.md`.
- Before: no REA static semantic graph scored against authored source. After: `index.js` named imports `rot13` and `checksum` resolve to `transform.js`, and package main maps to `index.js`, all 3/3 bounded relationships matching authored source; ledger's comparison command prints `True`. These are static inferred relationships, not runtime behavior.
- Per-axis verdicts: depth **improved** for source-derived static relationships; coverage **unchanged** on native-session readiness and other formats; calibration **unchanged** because runtime and dynamic unknowns stay explicit. Admit this route-specific depth move, without promoting native readiness or declaring end-to-end unknown-target verification.
