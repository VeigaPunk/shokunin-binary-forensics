# R73Source085 — source audit, row S085 (round-72 source)

seat: R73Source085 (scout, leaf; no subagents) · date: 2026-10-30 · lane: revenger-shokunin
scope: SOURCES.md row S085 only — no other admission proposed or reported.

## Row under audit (observed)

`corpus/SOURCES.md:99` (read raw, verbatim):

> | S085 | Automatically Attacking Software Reverse Engineering AI Agents — https://arxiv.org/abs/2605.30667v1 | paper | A | The arXiv v1 abstract's prompt-injection risk claim for an LLM-assisted analysis pipeline; no attack method reproduction | arXiv v1, submitted 2026-05-28, abstract; "extraneous string variable assignments to pass surreptitious instructions to the LLM" | The paper identifies analyzed-code strings as a possible prompt-injection carrier in the study; keep artifact text untrusted and do not reproduce attacks | mined | 2026-10-27 | on-release | corpus/knowledge/round-72-tool-landscape.md |

## Dependent wording (observed)

- Round-72 lesson Gate, `corpus/lessons/round-72.md:44`: `| S085 | https://arxiv.org/abs/2605.30667v1 | 2026-10-27 | Abstract: “extraneous string variable assignments to pass surreptitious instructions to the LLM” | ADMIT, tier A for the paper's reported prompt-injection risk only; no exploit reproduction or methods are included. |` (curly quotes only — markup normalization).
- Used-by entry, `corpus/knowledge/round-72-tool-landscape.md:44`: `| Automated RE-agent attack paper S085 | The arXiv abstract reports prompt-injection risk from embedded strings in a studied LLM-assisted RE pipeline. | Defensive implication only: treat target strings as untrusted. No attack steps were reproduced or published. |`
- Cross-reference only (no admission wording): `corpus/knowledge/round-73-re-resource-atlas.md:41` theme "artifact text as untrusted input to an RE agent … extends S076 and S085".

## Independent re-open (observed)

- URL: https://arxiv.org/abs/2605.30667v1 — accessed 2026-10-30, fetched via the arXiv abs page (reader resolved through arXiv API; metadata block: `arXiv: 2605.30667v1`, `Published: 2026-05-28`, categories cs.CR, cs.AI; authors Crawford, Phillips, McClure). Network fetch succeeded; no source failure.
- Located quote (verbatim substring of the v1 abstract, markup-normalized, 11 words ≤ 25):
  "extraneous string variable assignments to pass surreptitious instructions to the LLM"
- Surrounding abstract text confirming the location: "…decompiled machine code via prompt injection by using extraneous string variable assignments to pass surreptitious instructions to the LLM while not impacting the functionality of the executable file."

## Checks

| check | result |
|---|---|
| title matches source | PASS — "Automatically Attacking Software Reverse Engineering AI Agents" identical on arXiv |
| version pin v1 + submitted 2026-05-28 | PASS — metadata shows 2605.30667v1, published 2026-05-28 |
| located quote verbatim (markup-normalized) | PASS — exact substring of the v1 abstract; no markup inside the quote; row straight quotes vs lesson curly quotes only |
| quote length ≤25 words | PASS — 11 words |
| scope fidelity | PASS — row claims only the abstract's prompt-injection risk for an LLM-assisted analysis pipeline and explicitly "no attack method reproduction"; the abstract does name the technique (AutoDAN-derived, genetic-algorithm prompt generation) but the row does not lean on it |
| tier A | agree — paper's own abstract is the primary source for the paper's claim |
| used-by consistency | PASS — entry wording (defensive-only, "no attack steps were reproduced or published") matches row disposition and lesson Gate row; all three agree |
| rejection flip | n/a as reject — S085 is an ADMIT; the operative guard is "keep artifact text untrusted and do not reproduce attacks" (row) / "no exploit reproduction or methods are included" (lesson). Flip to reject would be warranted if the quote failed verbatim verification or scope crept beyond the abstract; neither triggered. Abstract itself frames the work as proof-of-concept with defensive conclusions, consistent with the guard. |

## Disposition

**Agree** with the source disposition (ADMIT tier A, abstract-scope, defensive-only guard). Independent re-open reproduces the located quote verbatim and every pinned field (title, v1, 2026-05-28). No defect found; **no superseding row needed**. Round-72 spotcheck (`corpus/lessons/round-72-verifier-spotcheck.md`, table row "S083, S084, S085, S080, S081 (extra)") already ruled agree/verbatim; my check concurs independently.

Routed S071/S082 quote defects belong to their own seats; per bounds I propose nothing for them and edited no registry row.

## Epistemic labels

- Observed: all file quotes above (exact locators cited) and the 2026-10-30 arXiv fetch.
- Inference: tier-A fit and flip-condition framing are judgment on the observed text.
- Unknown: none material to this row. The PDF body was not fetched (row scope is the abstract alone, so abstract verification is sufficient; not a source failure).
- Failures: none. No installs performed (nothing needed; pacman pause respected, no git/jj mutations, no writes outside this report path).
