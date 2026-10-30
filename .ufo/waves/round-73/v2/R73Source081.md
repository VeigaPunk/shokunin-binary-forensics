# R73Source081 — source audit, row S081

Seat: R73Source081 (reviewer, axes: coverage, source accuracy) · wave round-73 v2 · 2026-10-30
Scope: SOURCES.md row S081 only. No other source admission; no edits to any corpus/shared/sibling/fleet file.

## Assigned row (observation)

`corpus/SOURCES.md:95`:

```
| S081 | Augmenting Decompiler Output with Learned Variable Names and Types — https://www.usenix.org/system/files/sec22-chen-qibin.pdf | paper | A | The USENIX Security 22 paper's claim about compiler information loss and its model evaluation; not output from current tools | Abstract, pp. 4327 onward, 31st USENIX Security Symposium, 2022; "comments, variable names, and custom variable types are technically impossible to recover." | Decompiler output does not in general preserve original identifiers/types; learned suggestions are not original source truth and require independent validation | mined | 2026-10-27 | on-release | corpus/knowledge/round-72-tool-landscape.md |
```

Round-72 lesson Gate (`corpus/lessons/round-72.md`): S081 ADMIT, tier A, abstract quote "comments, variable names, and custom variable types are technically impossible to recover." — scope "the paper's compilation-information-loss statement and study; not a claim about any one current decompiler."
Round-72 outside spot-check (`corpus/lessons/round-72-verifier-spotcheck.md`, extra sample): ADMIT, "quoted string found verbatim". Round-73 Gate (`corpus/lessons/round-73.md`) routes quote defects for S071/S082 only (superseded by S427/S428); no routed defect names S081.

## Independent re-open (observation)

- Fetch: `curl -sSL --max-redirs 15` → HTTP **200**, 716,780 bytes, `application/pdf`, 0 redirects, 2026-10-30.
  sha256 `e1c3e8bbdb18150ba9a3326c1469174208305369bb01a5d04f94b1f9b5858288`; pdfinfo: 18 pages, letter, produced 2022-07-21 (iText).
- `pdftotext` rendering (whitespace-normalized): the string
  `comments, variable names, and custom variable types are technically impossible to recover.`
  is a **contiguous verbatim substring, 2 occurrences** — abstract (p. 1) and §1 restatement. Full sentence: "Decompilers are able to deterministically reconstruct structural properties of code, but comments, variable names, and custom variable types are technically impossible to recover."
- Abstract also confirms scope anchors: compilation "irrevocably destroys some information"; system DIRTY (DecompIled variable ReTYper); evaluation "recovering the original names written by developers 66.4% of the time and the original types 75.8% of the time."
- Title/authors/venue match the row: Qibin Chen, Jeremy Lacomis, Edward J. Schwartz, Claire Le Goues, Graham Neubig, Bogdan Vasilescu (CMU/SEI); "Proceedings of the 31st USENIX Security Symposium, August 10–12, 2022".

## Located quote (≤25 words) — access 2026-10-30

> "comments, variable names, and custom variable types are technically impossible to recover."

URL: https://www.usenix.org/system/files/sec22-chen-qibin.pdf (abstract, p. 1; proceedings pp. 4327 ff.). 11 words; verbatim confirmed.

## Field-by-field comparison

| field | row/lesson value | re-open finding |
|---|---|---|
| located quote | "comments, variable names, and custom variable types are technically impossible to recover." | VERBATIM in cited PDF (normalized whitespace only). Agree. |
| scope | paper's compiler-information-loss claim + its own model evaluation; not current-tool output | Abstract states both the information-loss claim and DIRTY's 66.4%/75.8% dataset evaluation. Scope exact. Agree. |
| tier | A | Primary published paper at canonical USENIX proceedings URL. Agree. |
| used-by | `corpus/knowledge/round-72-tool-landscape.md` | Present (`DIRTY S081` row: "compilation loses names/types and evaluates learned suggestions against its dataset"; limit "a prediction may be plausible but not original"). Agree. |
| rejection flip | none — disposition ADMIT/mined | No flip required; not a rejected row. Agree. |

## Disposition (inference)

**AGREE** with the source disposition: S081 ADMIT, tier A, mined, scope and used-by as recorded; no superseding row proposed for S081 (nothing to supersede). The round-72 spot-check's "verbatim" finding for S081 is independently reproduced. Routed-quote defects for S071/S082 belong to seats R73Source071/R73Source082 (S427/S428 already appended in `corpus/lessons/round-73.md` Gate); this seat makes no other admission.

## Network/source failures

None. Single fetch attempt succeeded (HTTP 200). No other sources contacted.

## Hygiene

Read-only outside this report. Scratch `/fast/scratch/hyaku/revenger-r73/R73Source081/` (fetched PDF + text extracts) cleaned after this report was written; receipts (status, size, sha256, page count, verbatim-substring result) recorded above. No installs this seat; no pacman transaction (host pause respected). Lane-internal seat only; not an outside discernment verifier.
