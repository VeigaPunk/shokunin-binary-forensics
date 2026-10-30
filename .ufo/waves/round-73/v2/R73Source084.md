# Round 73 wave v2 — Seat R73Source084 source audit (S084)

Seat: R73Source084 (leaf reviewer, lane-internal; not an outside discernment verifier)
Assigned row: **S084** only. No other source admission; no corpus/shared/sibling writes; no edits to any
registry or lesson file (read-only besides this report).
Round-72 routed quote debt (S071/S082 misattribution/paraphrase) is owned by their own round-73 seats;
per append-only policy a superseding row would be proposed by those seats, never an edit. Out of my scope.

## Verdict

**AGREE** with the round-72 disposition for S084: ADMIT, tier A, scoped to the proposed representation
and stated evaluation. Quote verified verbatim (normalizing markup only).

## Row under audit (observation)

`corpus/SOURCES.md:98`:

> | S084 | ALT4Decompile — https://arxiv.org/abs/2509.14646v2 | paper | A | The arXiv v2 abstract's proposed assembly-to-loop-structure representation and stated evaluation only | arXiv v2, last revised 2026-08-25, abstract; "we construct a C-aligned Abstract Loop Tree (ALT)" | This paper describes one technique and reported benchmarks; source-code inference remains a hypothesis requiring byte/behavior oracles | mined | 2026-10-27 | on-release | corpus/knowledge/round-72-tool-landscape.md |

Lesson Gate row (`corpus/lessons/round-72.md:43`): S084 … v2 abstract:
"we construct a C-aligned Abstract Loop Tree (ALT)" | ADMIT, tier A for the proposed representation,
not its generalization beyond its evaluation.

## Re-open of the primary source (observation)

- URL reopened: https://arxiv.org/abs/2509.14646v2 (exact cited pin; no shortcut/mirror).
- Access date: **2026-10-30**.
- Fetched HTML, 43,261 bytes, sha256 `03e14ce1076cb4b8e2219b1cda715099cc8fc775f98e367adeb8efb5a0d70cc3` (copy kept in seat scratch during audit, cleaned after this report).
- Page title: "[2509.14646v2] ALT4Decompile: Inferring C-aligned Abstract Loop Tree for LLM-Based Binary Decompilation".
- Dateline: "[Submitted on 18 Sep 2025 (v1), last revised 25 Aug 2026 (this version, v2)]" — matches the row's "last revised 2026-08-25".
- Identity: paper + v2 match the row; no redirect to a different arXiv id.

## Located quote check (observation)

Row quote (8 words, ≤25): **"we construct a C-aligned Abstract Loop Tree (ALT)"**

Raw abstract text (LaTeX inline markup preserved):

> "Specifically, we construct a C-aligned \underline{\textbf{A}}bstract \underline{\textbf{L}}oop \underline{\textbf{T}}ree (ALT) based on specific jump patterns of Assembly …"

The row's wording is an exact substring once markup only is normalized
(`\underline{\textbf{A}}`→`A`, likewise L, T); **no wording, scope, or semantic drift**. This independently
confirms the round-72 verifier spot-check note ("S084 contains LaTeX markup around the same words").

## Scope / tier / used-by / flip

- **Scope (agree):** the abstract proposes ALT4Decompile ("refactors assembly to closely resemble C
  language structure") and a stated evaluation ("Evaluated against 12 baselines … 70.4% test case pass
  rate on Decompile-Eval, a 10.6% improvement"). The row's bound — representation + stated evaluation
  only, benchmarks not generalized — matches. The row's caution that source-code inference remains a
  hypothesis requiring byte/behavior oracles is consistent with the abstract-only evidence.
- **Tier A (agree):** primary source is the paper's own arXiv abstract.
- **Used-by (agree):** `corpus/knowledge/round-72-tool-landscape.md:43` cites
  "LLM4Decompile S082; AutoDecompiler S083; ALT4Decompile S084" with the cluster caution not to compare
  across tasks/datasets/metrics or translate abstracts into tool readiness; the registry used-by cell
  matches.
- **Rejection flip:** n/a — S084 is ADMIT; no flip condition attaches.

## Classification

- Observation: fetched page bytes, title, dateline, raw + normalized quote text, entry citation at line 43.
- Inference: none needed; all checks are direct text comparisons.
- Unknown: nothing material; PDF body was not re-fetched (row is abstract-scoped, so not required).

## Network / source failures

First curl attempt errored writing only because the seat scratch directory did not yet exist; the
immediate retry after `mkdir -p` fetched the page successfully (HTTP 200 content, 43,261 bytes).
**No source-access failure.** No tools installed this seat.

## Receipt

S084 located quote re-verified verbatim (markup-only normalization) at the pinned v2 URL on 2026-10-30;
AGREE with ADMIT tier A disposition and its scope/used-by cells; no superseding row proposed for S084;
no file outside this report written; scratch cleaned.
