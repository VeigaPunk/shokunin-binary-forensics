# R73Source082 — source audit, row S082

Seat: R73Source082 (critic, axes: coverage, source accuracy) · wave round-73 v2 · 2026-10-30
Scope: SOURCES.md row S082 only. No other source admission; no edits to any corpus/shared/sibling/fleet file (read-only production; this report is the sole write).

## Assigned row (observation)

`corpus/SOURCES.md:96`:

```
| S082 | LLM4Decompile: Decompiling Binary Code with Large Language Models — https://arxiv.org/abs/2403.05286v3 | paper | A | The paper's v3 abstract and its own model/benchmark claims only, not general decompiler accuracy or present-day capability | arXiv v3, last revised 2024-10-22, abstract; "The resulting code may appear readable or even compile successfully, yet still deviate from the behavior of the original binary." | Readability and compilation are not behavioral equivalence; this is a paper-stated risk, not a measured result for the lane | mined | 2026-10-27 | on-release | corpus/knowledge/round-72-tool-landscape.md |
```

Round-72 lesson Gate (`corpus/lessons/round-72.md:41`): S082 ADMIT, tier A, v3 abstract quote "The resulting code may appear readable or even compile successfully, yet still deviate from the behavior of the original binary." Round-72 outside spot-check (`corpus/lessons/round-72-verifier-spotcheck.md:72`): **disagree** — quote absent from LLM4Decompile abstract and PDF (`deviate`/`may appear` greps empty); stated verbatim in AutoDecompiler S083's abstract (`arxiv.org/abs/2606.16162v2`); row's `mined` status not supported by that quote. Round-73 Gate (`corpus/lessons/round-73.md:14,17,23`) records append-only superseding rows S427 (S071) and S428 (S082), accessed 2026-10-30, committed in `d4ab332` ("round-73: honest stop (attempt 2)… land attempt-1 frontier files").

Entry wording: the used-by candidate `corpus/knowledge/round-72-tool-landscape.md:86-92` carries an explicit "Round-73 source-attribution erratum" (candidate remains unadmitted; S082 quote misattributed; S428 supersedes for the abstract's motivation only; behavioral-equivalence assertion not supported). `corpus/lessons/round-72.md:96-101` carries the matching erratum; old row/Gate bytes preserved as historical.

## Independent re-open (observation)

- Fetch 1: `https://arxiv.org/abs/2403.05286v3` → HTTP 200, 43,987 bytes HTML, 2026-10-30 (UTC), single attempt. sha256 of fetched page `d09e10b4898b25b981f139fbb871b883fa2ef24a9032397c57d96767f1dc1893`. Page metadata: "[v3] … last revised 22 Oct 2024 (this version, v3)" — matches the row's revision date.
- Abstract text (markup stripped, whitespace-normalized) contains the opening sentence "Decompilation aims to convert binary code to high-level source code, but traditional tools like Ghidra often produce results that are difficult to read and execute." and benchmark claims (HumanEval/ExeBench re-executability, vs GPT-4o and Ghidra). Substring tests: `deviate` → **absent**; `may appear readable` → **absent**; `difficult to read and execute` → **present**. The row's located quote is therefore NOT in the cited v3 abstract.
- Fetch 2: `https://arxiv.org/abs/2606.16162v2` (AutoDecompiler, S083's source) → HTTP 200, 44,662 bytes. Its abstract contains: "Consequently, the generated code may appear readable or even compile successfully, yet still deviate from the behavior of the original binary and mislead downstream analysis." Closest source of the misattributed sentence located — but note it reads "the **generated** code", not "The **resulting** code", and continues "and mislead downstream analysis"; so even the spot-check's "verbatim in S083" wording is one word off (observation, minor; the misattribution finding itself stands).
- Fetch 3: `https://arxiv.org/abs/2403.05286` (latest) → version list shows [v1],[v2],[v3] only; v3 is the current latest. No version drift; the v3 pin remains live. Latest abstract also lacks `deviate` and keeps the Ghidra-motif sentence.

## Located quote (≤25 words) — access 2026-10-30

> "traditional tools like Ghidra often produce results that are difficult to read and execute."

URL: https://arxiv.org/abs/2403.05286v3 (v3 abstract, opening sentence; last revised 2024-10-22). 14 words; verbatim confirmed in my own fetch.

## Field-by-field comparison

| field | row/lesson value | re-open finding |
|---|---|---|
| located quote | "The resulting code may appear readable or even compile successfully, yet still deviate from the behavior of the original binary." (attributed to v3 abstract) | ABSENT from cited v3 abstract (`deviate` and `may appear readable` both empty). Disagree with row-as-executed; quote was never supported by the cited source. |
| scope | v3 abstract's own model/benchmark claims only | Abstract does state its motivation (Ghidra readability/executability limits) and its HumanEval/ExeBench claims; that narrower scope is supportable, but only with a real quote. Partially agree. |
| tier | A | Primary paper at canonical arXiv URL; tier A is right for the paper itself. Agree. |
| used-by | `corpus/knowledge/round-72-tool-landscape.md` | Present; entry now carries the round-73 erratum disowning the behavioral-equivalence use. Agree with handling. |
| rejection flip | none (disposition ADMIT/mined) | No flip needed if the row is superseded rather than re-decided. The behavioral-equivalence claim must not be re-pointed at S083 either: S083's sentence is its own paper-stated risk, scoped to its study. |

## Superseding row (the seat's routed defect)

**DISAGREE with S082's executed disposition; AGREE with the corrective disposition already landed as S428** (`corpus/SOURCES.md:443`, Gate at `corpus/lessons/round-73.md:14`):

```
| S428 | LLM4Decompile — https://arxiv.org/abs/2403.05286v3 | paper | A | Correction of S082 source attribution: abstract's stated motivation, not behavioral-equivalence evidence | v3 abstract opening sentence, accessed 2026-10-30; "traditional tools like Ghidra often produce results that are difficult to read and execute." | supersedes S082 — The abstract motivates the authors' model by readability/executability limits; the behavioral-deviation quote belongs to AutoDecompiler S083, not this paper. | mined | 2026-10-30 | on-release | corpus/lessons/round-73.md |
```

My independent fetch confirms S428's quote verbatim (14 words, opening sentence) and its scope/limit cells as written. **I propose NO new S429 row:** the routed debt is already resolved by an append-only superseding row whose content my own re-open reproduces; a second superseding row would be a duplicate authority and registry churn against the predicate's no-duplicate-ids guard. Had S428 not existed, the row above is exactly what this seat would have proposed (same URL, same quote, same scope, `supersedes S082`, status `mined`, recheck `on-release`, used-by `corpus/lessons/round-73.md`). Old S082 row and the round-72 Gate/lesson bytes stay historical, never edited — consistent with the entry erratum and the round-72 lesson erratum; I endorse that preservation.

## Predicate / axis note (inference)

S082 sits outside the S096–S109 set the frozen C10 predicate mines; adding or omitting a superseding row here does not move C10_HELD_BACKED counting, provided registry ids stay unique. This report changes no files, admits no source, and is lane-internal — not an outside discernment verdict.

## Network/source failures

None. All three fetches succeeded on first attempt (HTTP 200, sizes above). No paywall, no redirect chain, no robot block observed.

## Hygiene

Read-only outside this report. Tooling: system `curl 8.x` + `python3` (stdlib only) — no installs this seat; no pacman transaction (host-wide pause respected); scratch `/fast/scratch/hyaku/revenger-r73/R73Source082/` removed after receipts (status, sizes, sha256, substring results, version list) were recorded above. No git/jj mutations, no child tasks, no background jobs.
