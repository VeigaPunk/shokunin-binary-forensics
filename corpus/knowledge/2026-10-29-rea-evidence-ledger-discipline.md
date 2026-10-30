source: S096 — REA EvidenceLedger, https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/application/investigation/EvidenceLedger.ts — class header and `record`/`clear`, commit 12f6e0974cc0db0b3a9b86246accc76556837222
source: S098 — REA Evidence schema, https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidence.ts — `confidence` and `authority` fields, same commit
source: S100 — REA evidence workflows reference, https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/evidence-workflows.md — residual-unknown and absence rules, same commit
source: S097 — REA residual-unknown domain, https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/residualUnknown.ts — `resolutionSchema` verified branch, same commit
source: S099 — REA evidenceBundle qualification, https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidenceBundle.ts — `evidenceQualifies` / `validateVerifiedResolution`, same commit
source: S102 — REA issue #73, https://github.com/morluto/rea/issues/73 — Correctness section (closed)
source: S103 — REA issue #21, https://github.com/morluto/rea/issues/21 — Scope / Acceptance (closed)
source: S101 — REA issue #50, https://github.com/morluto/rea/issues/50 — Outcome / Acceptance / Non-goals (closed)
source: S108 — REA evidenceCompletionLedger, https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidenceCompletionLedger.ts — claim status schema, same commit
source: S104 — Accountable partial understanding (APU), https://arxiv.org/abs/2610.26799v1 — abstract conditions list, 2026-10-19
source: S106 — Schum/Tecuci/Boicu chain-of-custody paper, https://doi.org/10.1080/08850600802698259 — pp. 298–319 definition of custody transformations (opened via author PDF)
source: S107 — Agentic Binary Reverse Engineering survey, https://www.richards.ai/papers/security-agentic-binary-reverse-engineering-state-of-the-art-architecture-bench — evidence/reporting-layer sentence, page dated 2026-05-01
source: S105 — Epistemic Deconstructor README, https://cdn.jsdelivr.net/gh/NikolasMarkou/epistemic-deconstructor@main/README.md — deliverable framing (method lead, not REA schema)
source: S109 — Immersive sensemaking for binary RE, https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2026.1613269/abstract — citation_abstract (compounded uncertainty), DOI 10.3389/frvir.2026.1613269, 2026-02-18
source: S002 — installed REA skill, `~/.agents/skills/reverse-engineer-anything/SKILL.md` — finding-ledger rule (lines 313–314 / 350)
verified-at: 2026-10-29 — local REA checkout `~/.local/share/rea` at commit 12f6e0974cc0db0b3a9b86246accc76556837222; issues #21/#50/#73 opened earlier the same day; APU HTML, Schum PDF, Richards page, ED README, and Frontiers abstract page opened 2026-10-29. Installed skill `evidence-workflows.md` sha256 `2bdee98a…` differs from checkout `f44b68ac…` (71 vs 126 lines); S100 pins the checkout. No REA MCP analysis run.
recheck: `git -C ~/.local/share/rea rev-parse HEAD`; re-open the blob URLs at that commit; re-open issue pages and arXiv/DOI destinations if a claim moves.
coverage-map: C10 — evidence-ledger discipline (Evidence IDs; observation/inference/unknown)
admission-status: candidate

# REA evidence-ledger discipline — observation, residual unknown, qualification

## Scope

This entry states what REA's own Evidence v2 / EvidenceLedger / residual-unknown sources require for a finding to stay ledger-bound. It is documentation of those contracts at commit `12f6e0974cc0db0b3a9b86246accc76556837222`, plus adjacent methodology sources that reinforce the same separation of observation, claim, and unknown. It does not claim a successful REA run on this host, does not prove any target behavior, and does not treat a hash, receipt, or decompiler string as authenticity or source identity (Q09 / PROVINCE).

## Ledger layers the sources actually name

| Layer | What the cited source establishes | Boundary |
|---|---|---|
| Evidence record | S098/S103: each record carries subject digest/format, provider, parameters, raw/normalized results, `confidence` ∈ {observed, derived, inferred}, `authority`, limitations, locations, and an `evidence_id`. | The vocabulary is REA's schema, not a claim that a given tool output was observed here. |
| Session EvidenceLedger | S096/S101: a session-owned in-memory set records successful analyses, deduplicates by Evidence ID, rejects conflicting content, and clears when the owning session closes; limits error instead of silent eviction. | Non-goals explicitly exclude DB persistence and cloud sync (S101). Export/import is a separate bundle path. |
| Residual unknown | S097/S100/S102: unresolved questions are revisioned records with supporting/contradicting Evidence IDs, required authority/confidence/environment, recommended probes, and a resolution that is verified only with qualifying evidence. | `verified` needs ≥1 evidence id (S097). Inference cannot satisfy an observed-authority requirement (S102; S099 rank check). |
| Verifier completion ledger | S108: a separate `ecl_` ledger binds each `claim_id` to status ∈ {pass, fail, unsupported, truncated, unknown} and ≥1 Evidence ID. | This is claim-completion bookkeeping for a verifier, not a substitute for residual unknowns. |
| Agent working rule | S100/S002: cite Evidence IDs; preserve limitations/coverage; do not treat a miss in partial Evidence as absence; export before session close when retention is required. | Skill/workflow text directs the agent; it is not itself an Evidence record. |

## Qualification rule (load-bearing)

For a residual unknown marked `resolution.disposition = "verified"`, S099's `evidenceQualifies` requires:

1. the resolution Evidence ID is also in `supporting_evidence_ids`;
2. the Evidence exists and is not a residual-unknown mutation record;
3. if `required_authority` is set, Evidence.authority matches it;
4. Evidence.confidence ranks at least as high as `required_confidence`, with rank `inferred=1 < derived=2 < observed=3`;
5. environment fields match when `required_environment` is set;
6. contradicting Evidence IDs must be empty (S099 `validateVerifiedResolution`).

S100 states the agent-facing compression of (4): only qualifying observed evidence can verify a resolution when observation is what the unknown requires.

## Adjacent methodology (non-REA schema)

| Source | Bounded teaching | How to use with C10 |
|---|---|---|
| S104 APU | Names “visible residual unknowns” among six necessary conditions for accountable partial understanding. | Reinforces keeping unknowns explicit under agentic delegation; not a REA API. |
| S106 Schum et al. 2009 | Chain of custody tracks who/what accessed original evidence, when, and what they did to it; the analyst may not receive the original. | Custody/transform awareness for derived artifacts and tool pipelines; does not admit a finding by itself. |
| S107 Richards survey | Describes an “evidence and reporting layer that records claims, supporting observations, tool outputs, uncertainty, and validation status.” | Architecture vocabulary for agentic RE; survey prose is not a run receipt. |
| S105 Epistemic Deconstructor | Positions the deliverable as a validated predictive model with uncertainty bounds, persisted so context loss cannot erase the investigation. | Method lead for black-box hypothesis/falsification loops; out-of-province PSYCH tier and live probing are not adopted. |
| S109 Frontiers immersive sensemaking | Abstract frames binary RE as cognitively demanding under compounded uncertainty with incomplete automation. | Cognitive-process adjacency for why residual unknowns matter; not a VR adoption or REA schema. |

## Observation, inference, unknown

**Observation:** at commit `12f6e09`, the cited REA TypeScript modules and skill reference define the fields and checks above; issues #21/#50/#73 state the matching product contracts; the adjacent papers/README state the quoted methodological claims in the Gate.

**Inference:** a lane that keeps every conclusion tied to Evidence IDs, separates observation/inference/unknown, and refuses to “verify” an observed-authority unknown with inferred Evidence is implementing REA's documented discipline rather than inventing a parallel epistemology.

**Unknown:** whether this host's currently registered REA MCP build matches `12f6e09` byte-for-byte in every Evidence path (the installed skill `evidence-workflows.md` already differs in bytes/line-count from the pinned checkout copy); whether any particular target investigation's unknowns are correctly resolved; whether APU/Schum/Richards/ED/Frontiers improve fixture scores — none were executed as oracles here.

## Limitations

- Documentation-only: no `record`/`record_unknown`/`export_evidence_bundle` call was made for this entry.
- Issue text is product intent; the TypeScript anchors are the executable contract at the pinned commit.
- S105 is a third-party skill README (tier B method lead), never sole support for a REA schema claim.
- Seed.md's C10 note remains the pre-contract reminder; this candidate is the sourced expansion.

## §Q-map

| Q | decision | entry evidence / boundary |
|---|---|---|
| Q01 | PASS | Load-bearing ledger rules cite tier-A REA code/issues (S096–S103, S108) at stated scopes; S104/S106/S107/S109 are adjacent methodology; S105 is not sole support. |
| Q02 | PASS | Headers list S-IDs, URLs/paths, anchors, `verified-at`, `recheck`, `coverage-map`. |
| Q03 | n/a | No byte oracle / expected fixture values. |
| Q04 | PASS | No tool run is credited; schema statements are from named source files. |
| Q05 | n/a | No host capability claim. |
| Q06 | n/a | No authored fixture is used. |
| Q07 | n/a | No parser-behavior prediction is offered. |
| Q08 | n/a | Historical criterion superseded by Q11, applied below. |
| Q09 | PASS | No digest offered as origin/authenticity. |
| Q10 | PASS | Scoped to REA EvidenceLedger discipline and named adjacent texts. |
| Q11 | PASS | Identifiers are source-anchored (`evidence_id`, enums, issue numbers); no re-derived byte counts. |
| Q12 | n/a | No rejected row is load-bearing for this entry's claims. |
| Q13 | n/a | No verifier command is credited as guarding this prose. |
| Q14 | n/a | No hex string carries a byte-length assertion. |
| Q15 | source pin, not independently re-derived | The REA commit identifiers locate external source bytes; no lane-tree identity is asserted. External object resolution remains a review obligation, not a green lane-lint claim. |
| Q16 | PASS | Each claim stays inside the cited schema/issue/paper sentence; no run output is invented. |
