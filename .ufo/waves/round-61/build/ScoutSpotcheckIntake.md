# ScoutSpotcheckIntake — S008's reject record vs RFC 3227 §2.1 (read-only)

Seat `CloseChousa26.ScoutSpotcheckIntake-10` · base `e0a4b0c4348ef1fade46539f520e94fa140c4d8a` (`git rev-parse HEAD`) · 2026-10-21 · registry `swarm-registry.json` `reportDir` `.ufo/waves/round-61/build` (lane-relative; written there). No lane file edited, no clone, no subagent.

## Axes (godspeed)
- calibration: split the verifier's single "agree" into verdict agreement and record disagreement, and convert the record defect into an admission criterion.
- coverage: adds zero knowledge entries; `K_HELD` stays 4/14 — this intake does not move C1.
- coupling: two appended rows (SOURCES S016, QUALITY Q12); no knowledge-entry criterion changes, so C04/C09 gating under Q01–Q11 is unaffected.
- specificity: the quote is re-fetched, hashed, and the full text searched for the term the flip names.

## 1. The quotation (observed)

Command: `curl -sS https://www.rfc-editor.org/rfc/rfc3227.txt` → HTTP 200, 18,468 bytes, sha256 `32e81a23d3f6093a5968e7d8b1318f96efc5c10c16515dc14d97a19b7f40a6c5` (fetch 2026-10-21).
Revision shown on the page: "Request for Comments: 3227 ... BCP: 55 ... Category: Best Current Practice ... February 2002" (`rfc3227.txt:3-7`).
Location: §2.1 "Order of Volatility", page 4 — heading at fetched line 181, quote at 183-185, the example ordering list at 188-201.
Quote, 24 words, verbatim with wrapped lines joined (the double space after "volatile." is the page's typesetting):

> When collecting evidence you should proceed from the volatile to the less volatile.  Here is an example order of volatility for a typical system.

The list that follows orders host surfaces only (registers/cache; process table, kernel statistics, memory; temporary filesystems; disk; remote logging; network topology; archival media), with no per-artifact read-surface ordering. The reviewer's claim at `corpus/lessons/round-1-verifier-spotcheck.md:13` is correct as written. Full-text check: `grep -ni volatil rfc3227.txt` → `44,162-163,181,183-184,310,314`; only §2.1 defines the ordering.

## 2. Three records disagree (observed)

- `corpus/SOURCES.md:22` — S008 `flip: an entry needs its volatility-ordering primitive specifically`.
- `corpus/lessons/round-1.md:140` — "S008 `recheck` `—` → `on-release`. The flip condition depends on a successor RFC or BCP superseding RFC 3227." That is a source-change flip, already coherent, and not the registry's flip.
- `corpus/lessons/round-1-verifier-spotcheck.md:13` — agree on the verdict, disagree with the record.
- Second defect in the same cell: S008's `anchor` ("Abstract, §1, §3.2", `SOURCES.md:22`) omits §2.1, the section the flip names; the rule-1 quote recorded at `corpus/lessons/round-1.md:77` is from the Abstract only.

Inference: the registry flip fails twice — §2.1 supplies the named primitive, so the condition is already true; and a "needs" condition cannot change a verdict even when the content is absent. The verdict survives: §1 addresses System Administrators ("provide System Administrators with guidelines", `rfc3227.txt:71-72`), and §2.1 gives no device- or artifact-specific acquisition ordering (S005's role, `SOURCES.md:19`).

## 3. What contract v1 allows (observed)

`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:49-51`, rule 2: "Only `status`, `recheck` and `used-by` change in place ... A correction is a new row whose `teaches` opens `supersedes S0NN —`."
⇒ the contract allows a **new superseding row**; a **lesson correction alone cannot** fix `teaches` or `anchor` (both outside the in-place set) and may only log old→new for status/recheck/used-by. Do not invent `superseded` as a status: the contract's census keeps status in `queued|mined|rejected` (`.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`, §Census awk).

## 4. Draft append-only correction — SOURCES S016 (next unused; S015 last, `SOURCES.md:29`), inserted after S015 inside `## Registry`

```
| S016 | RFC 3227 Guidelines for Evidence Collection and Archiving — https://www.rfc-editor.org/rfc/rfc3227.txt | spec | A | what the document states about ordering collection by volatility, as published in 2002 | §2.1 Order of Volatility, p.4, lines 183-185 with the list at 188-201, and §3.2 Collection Steps; RFC 3227 / BCP 55 (February 2002) | supersedes S008 — REJECTED on scope: it is system-administrator incident guidance (§1) and S005 serves the lane acquisition-guidance role; §2.1 already states an example order of volatility for "a typical system" over host surfaces, so S008's recorded flip was already true and could not change a verdict; flip: a successor RFC or BCP superseding RFC 3227, the condition the round log itself recorded | rejected | 2026-10-21 | on-release | corpus/lessons/round-61.md |
```

Validation on a /tmp lane-mirror (row after S015, `knowledge/`, `live/`, `fixtures/` symlinked): `bash scripts/sources-census.sh validate --file /tmp/revenger-r61-ScoutSpotcheckIntake/lane/corpus/SOURCES.md --today 2026-10-21` → `file W04 S016 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes` then `file ok /tmp/revenger-r61-ScoutSpotcheckIntake/lane/corpus/SOURCES.md`, `rc=0`. W04 is the allowed same-URL/different-scope warning; E04 does not arm (scope differs, and `teaches` carries `supersedes S008`). No other code. Appending at EOF instead produced `file E12 S016 row outside Registry section` — position matters.

## 5. Draft QUALITY criterion — Q12 (new class, additive; nothing superseded)

```
| Q12 | A rejection row's `flip` names either a later source change or a scope the reject reason does not already exclude, and a need for content cannot serve as a flip. The row's `anchor` cites the section the reject reason was tested against; the round `## Gate` records the full-text search for the flip. | the flip names content the row itself credits the source with, or only that an entry "needs" it — neither can change the verdict (S008's flip named a volatility-ordering primitive that §2.1 supplies) | M21 (`corpus/lessons/round-61.md`; from `corpus/lessons/round-1-verifier-spotcheck.md:13`) |
```

Shape: `awk -F'|' '/^\| Q[0-9]+ /{print NR, NF}'` → new row NF=6; criteria count 12. `corpus/QUALITY.md:5-6` governs supersession only, so an added class needs no replaced row; Q12 restates no entry rule, leaving Q01–Q11 untouched for C1. The producing class belongs in `corpus/lessons/round-61.md` `## Mistakes` as M21 (evidence: `round-1-verifier-spotcheck.md:13`, `SOURCES.md:22`, `round-1.md:140`); renumber if round 61 minted another M id first.

## 6. Gate record the landing owes (contract rule 1)

One bullet in `corpus/lessons/round-61.md` `## Gate`: S016 URL, access date 2026-10-21, location `§2.1 Order of Volatility, p.4 lines 183-185 (sha256 32e81a23…a6c5)`, the 24-word quote above, and "RFC 3227 / BCP 55 (February 2002); `rfc-index.xml` entry shows current-status BEST CURRENT PRACTICE, is-also BCP55, and no `obsoleted-by`/`updated-by` (fetched 2026-10-21)". Command for the last fact: `curl https://www.rfc-editor.org/rfc-index.xml`, `<rfc-entry><doc-id>RFC3227</doc-id>…` parsed → `obsoleted-by => ABSENT`, `updated-by => ABSENT`, `is-also => BCP55`.

## 7. Adjacent (observed; not duplicated here)

- `corpus/README.md:9` "Q01–Q10" drift is `ScoutReadmeDrift.md` D1; landing Q12 makes the replacement "Q01–Q12".
- No in-place S008 edit is required. If the integrator counts the round lesson as a citer, the only lawful change is `used-by — → corpus/lessons/round-61.md`, logged old→new.
- The fleet-root `.ufo/waves/round-61/build/` (outside the lane) is receiving some sibling reports (e.g. `SimplifierReceiptControl.md`, `ExecEvmOracleR24.md`, 6 files at 12:49) while this lane directory holds 34 including `swarm-registry.json`; the registry's `reportDir` is the lane-relative one used here — the integrator should read both.

## Unknowns
- RFC 3227 errata state: not opened (`rfc-index.xml` carries no `errata-url`; the info page renders errata client-side). It does not affect the quote or the reject.
- Whether the wave's mistakes table takes M21, and whether the integrator lands S016 before or after the C04/C09 rows (S016 must be computed at landing; ids are never reused).

## Installs

None.

VERDICT: S008's reject stands but its recorded flip is false — §2.1 supplies the very volatility-ordering primitive the flip names — so contract v1 requires a new superseding row (S016, `rejected`, flip = a successor RFC/BCP, the flip `round-1.md:140` already logged) plus criterion Q12; a lesson-only correction cannot fix `teaches`.
