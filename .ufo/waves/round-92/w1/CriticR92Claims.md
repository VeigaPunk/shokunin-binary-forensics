# CriticR92Claims report (round 92, attempt 1, w1)

Full ranked findings: `.ufo/waves/round-92/w1/CriticR92Claims/findings.md`. Reproducer: `.ufo/waves/round-92/w1/CriticR92Claims/forge.py`; receipt: `.ufo/waves/round-92/w1/CriticR92Claims/forge-receipt.txt`.

## Ranked
1. [High] C2 predicate does not check the token: C08 -> `partial`, `held`+`knowledge/seed.md`, or a trailing cell all give `C2_VERDICT=pass`; so does the intended `uncovered`. Frozen fix: add an exact-token leg and fail controls.
2. [High] C2 passes when the only C08 saved record (`corpus/live/runs/round-77/inspection.json`) is deleted with the token still `frontier`. Frozen fix: pin the record's sha and require it present.
3. [High] C1 full forgery (stub entry, invented SOURCES row dated 2026-11-05, two invented votes, README flip) passes all 12 legs. Only sha binding and fence presence bite. Frozen fix: vote provenance tied to wave artifacts and the registry, SOURCES receipts.
4. [High] C1 accepts `n/a` for all 17 Q; all-`n/a` votes pass. Frozen fix: require PASS for all, or justified `n/a`.
5. [Medium] C2 probe runs from the lane working tree and imports from `reports/round-66/` first; a shadow `tempfile.py` forged the labels to pass. cwd and TMPDIR are not the gap. Currently clean. Frozen fix: run the probe from the rev archive with `python3 -I`.
6. [Medium] `C1_EMBEDDED` passes a fenced `$` block with zero output lines (`check_embedded_outputs.py` drift check, lines 153–155, 189–191). Fix in the corpus gate: require output lines.
7. [Medium] `C1_SOURCES` trusts self-declared `mined` and `2026-11-05`; no receipt check.
8. [Low] Claims overstate predicates (token and scope not measured).
9. [Not evaluated] Entry scope review: no entry, no READY; bounded wait (40 × 30 s, `bg_5160`) timed out.
10. [Info] K==9 equality interacts with C2 (C08 held would make K 10 if C03 also lands); no C1 bypass.
11. [Info] `SKILL.md` and `.gitignore` modified in the working tree by others; neither counter reads them; no vote or entry path ignored.

No frozen file under `reports/round-92/` was edited. No git mutation. No tool installed. Scratch removed.
