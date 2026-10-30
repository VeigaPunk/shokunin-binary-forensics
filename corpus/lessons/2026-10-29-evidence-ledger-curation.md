# 2026-10-29 — evidence-ledger source curation (interactive)

author: REA_EvidenceLedger_impl (omp subagent) · interactive Main dispatch, not a hyaku round · local REA pin `12f6e0974cc0db0b3a9b86246accc76556837222` · no REA tool execution.

## Gate — C10 EvidenceLedger sources

### New rows opened this day (CORPUS.md SOURCES rule 1)

All rows below were opened on **2026-10-29**. Quotes are ≤25 whitespace-delimited words with locations. New IDs append only; no prior row's `status`/`recheck`/`used-by` was rewritten except where this lesson logs an append to `used-by` for S002.

| S | source URL / path | opened | located quote (≤25 words) | decision and scope |
|---|---|---|---|---|
| S096 | https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/application/investigation/EvidenceLedger.ts | 2026-10-29 | L53: “Session-owned set of immutable evidence records.” | ADMIT, tier A for the session ledger type and record/import/clear contract at this commit only. |
| S097 | https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/residualUnknown.ts | 2026-10-29 | L66–70 verified branch requires `evidence_ids` with `.min(1)` | ADMIT, tier A for verified-resolution shape; not automatic truth. |
| S098 | https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidence.ts | 2026-10-29 | L148–149: `confidence: z.enum(["observed", "derived", "inferred"])` with `authority` | ADMIT, tier A for Evidence v2 confidence/authority vocabulary at this commit. |
| S099 | https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidenceBundle.ts | 2026-10-29 | L552–555: `inferred: 1, derived: 2, observed: 3` rank gate in `evidenceQualifies` | ADMIT, tier A for qualification ranks and authority matching used by verified resolutions. |
| S100 | https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/evidence-workflows.md | 2026-10-29 | “Only qualifying observed evidence can verify a resolution.” | ADMIT, tier A for agent-facing residual-unknown and absence rules at this commit. |
| S101 | https://github.com/morluto/rea/issues/50 | 2026-10-29 | Acceptance: “Memory and record-count bounds return typed truncation/limit errors rather than evicting evidence silently.” | ADMIT, tier A for closed ledger outcome/non-goals (in-memory, no DB). |
| S102 | https://github.com/morluto/rea/issues/73 | 2026-10-29 | Correctness: “Inference cannot satisfy observed authority.” | ADMIT, tier A for residual-unknown correctness contract. |
| S103 | https://github.com/morluto/rea/issues/21 | 2026-10-29 | Acceptance: “Secrets and arbitrary environment values never enter evidence.” | ADMIT, tier A for Evidence envelope fields and export hygiene. |
| S104 | https://arxiv.org/abs/2610.26799v1 | 2026-10-29 | Abstract: “visible residual unknowns, actionability, and temporal maintenance.” | ADMIT, tier A for APU's stated conditions; not a REA API. |
| S105 | https://cdn.jsdelivr.net/gh/NikolasMarkou/epistemic-deconstructor@main/README.md | 2026-10-29 | README: “validated predictive model with parameter uncertainty bounds, not a summary document.” | ADMIT, tier B method lead for persisted black-box investigation; never sole REA-schema support. PSYCH tier not adopted. |
| S106 | https://doi.org/10.1080/08850600802698259 (author PDF opened) | 2026-10-29 | p.2: “the evidence received by the analyst is not the same as the original evidence provided by its source.” | ADMIT, tier A for custody-as-transformation teaching; not PE acquisition procedure. |
| S107 | https://www.richards.ai/papers/security-agentic-binary-reverse-engineering-state-of-the-art-architecture-bench | 2026-10-29 | “evidence and reporting layer that records claims, supporting observations, tool outputs, uncertainty, and validation status.” | ADMIT, tier B survey vocabulary for agentic RE architectures; not a run receipt. |
| S108 | https://github.com/morluto/rea/blob/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidenceCompletionLedger.ts | 2026-10-29 | L14–27: claim statuses `pass`/`fail`/`unsupported`/`truncated`/`unknown` with `evidence_ids` | ADMIT, tier A for verifier completion-ledger schema at this commit. |

| S109 | https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2026.1613269/abstract | 2026-10-29 | citation_abstract: “suffering from compounded uncertainty and lack of full automation.” | ADMIT, tier B cognitive-RE survey adjacency; not REA schema and not VR-method adoption. Promoted from Leads after full abstract open. |

### Existing row touch

- S002 re-opened for the skill's finding-ledger lines (“Every conclusion must distinguish observations, inferences, and unknowns.”). `used-by` gains the new knowledge path; no other fields changed. Logged here per append-only rule for `used-by`.

### Skill vs checkout drift

- Installed `~/.agents/skills/reverse-engineer-anything/references/evidence-workflows.md` sha256 `2bdee98a843d018cf850c706111bb74c459ba8640da00799e9208122e4d5ab80` (71 lines).
- Checkout pin used by S100: `f44b68acc6ebaa60c1f5d0670e4f9ff7212d351a0ecc6e6ca77ce38b9177ea57` (126 lines) at `12f6e09`. Receipt: `reports/evidence-ledger-2026-10-29/skill-vs-checkout-evidence-workflows.txt`.

### Candidate knowledge

`corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md` — `admission-status: candidate`. C10 remains `partial` until a later admit gate. Receipts: `reports/evidence-ledger-2026-10-29/`.

### Search log (bounded)

2026-10-29, C10 EvidenceLedger discipline. Query: primary REA ledger/residual-unknown/Evidence v2 contracts plus obscure epistemic/custody methodology that connects without importing live-target offense. Where: local `~/.local/share/rea` at `12f6e09`, GitHub issues #21/#50/#73, arXiv 2610.26799, Schum 2009 CoC PDF, Richards agentic-RE survey page, Epistemic Deconstructor README via jsDelivr. Identified 14, screened 14, included 14 rows (S096–S109), excluded 0 registry rows. Continuation: Frontiers abstract opened in full and promoted to S109; skill-vs-checkout evidence-workflows hash drift recorded (S100 pins checkout). Stop: executable schema anchors plus issue contracts were pinned; adjacent methodology kept non-sole for REA claims. Opener: REA_EvidenceLedger_impl.

## Mistakes

None newly minted this interactive pass. Carry-forward reminder: do not treat catalog/survey prose (S107) or third-party skill READMEs (S105) as REA schema authority.
