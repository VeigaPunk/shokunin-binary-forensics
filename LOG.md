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
