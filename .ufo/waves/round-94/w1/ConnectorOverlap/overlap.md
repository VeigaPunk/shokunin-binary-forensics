# Sibling-overlap scan — revenger round-94 seat ConnectorOverlap (2026-11-05)

Read-only. Sources: the fleet round reports `.ufo/reports/round-93/{kaidoku,kake,lore,mori,revenger}.md` and `.ufo/reports/round-94/{kaidoku,kake,lore,mori}.md` (first ~1,800 bytes of each read in full, plus a keyword grep over every body for `sources|registry|admission|admit|ledger|provenance|quote|knowledge map|coverage-map|revenger|kaidoku|kake|knowledge/`); the fleet `MANIFEST.json` closure rows of 2026-11-05 (sorted by `closed_at`); the revenger province (`PROVINCE.md`); the shokuknow merge package report. No sibling file was modified. Lanes with no round-93/94 report in the fleet directory (tabi, kotoba, kumitate, kengaku, kagi, kasegi, souji, kotodama, tsukuroi) are carried from the r93 scan or the MANIFEST row only; they are marked as such.

Revenger province for this scan: saved-ledger evidence craft (receipts, oracle and counter discipline), source-registry discipline (SOURCES rows, supersession, census, quote receipts), and admission gates (votes, digest binding, verified-at clauses).

## 1. Lanes with round-93 / round-94 reports

| lane | r93 | r94 (fleet report) | overlap with revenger's province (one line) | flag for revenger |
|---|---|---|---|---|
| **kake** | admitted (`MANIFEST` 14:23 BRT) | rejected-honest-stop (15:44 BRT) | r93 appended six A-tier RFC rows S471–S476 after a mirror gate and admitted a conditional-request entry; r94 appended S477/S478 with two anchor defects (hyphenation break; D2/D3) corrected before landing, and built a strict successor counter with a battery of eight false-green routes that the frozen r93 counter admits 7/7. | **REPORT.** (a) Independent evidence that a frozen counter is reachable by false-green routes, the same failure revenger logged as M3/CriticR93. (b) Quote-anchor defects (hyphenation break across a line) are the failure class `audit_source_quotes.py verify` must catch; revenger should check its own receipts against that case. (c) kake's merge package collides on 8 of 129 staged ids (r93 `assimilation/collisions`), the same class as revenger's 155/155. |
| **kaidoku** | rejected-honest-stop (14:49 BRT); R93-C1 NOT VERIFIED because the frozen v3 counter's `--json-out` receipt writer raised `TypeError` on the honest case | admitted (16:10 BRT); R94-C1 VERIFIED via a successor v4 that imports the frozen v3 verdict code by sha-pinned path and changes only the receipt writer; S319 appended (tier A, `mined`) | Same source-registry rule revenger used for S497 (supersession by a new row, not by editing a frozen scope cell); same successor-counter pattern as revenger C1 v3/C2 battery. Its r93 failure is a counter that scores correctly on paper but cannot write its receipt on the honest input. | **REPORT.** A positive control must exercise the receipt/writer path, not only the verdict function. Check, not absorb: whether revenger's `forge_battery3` positive control runs the same writer path that a fleet verifier would. |
| **mori** | landed (`1fc921cf`, `aade1775`); S622/S623 admitted; registry 393 → 395 | landed (`fa1af842`); R02 defect: the v1 admission self-check `count-c1.py:141` used `ac[:7] in va` (substring of `verified-at:`), fixed in v2 by requiring the first whitespace token to be ≥7 characters and a prefix of the admission `%h`; C2 removed host home literals | Admission-gate overlap: an embedded-token check that passes a forged-looking line is the class of revenger's CriticR93 finding 1/A21 (duplicate or case-variant admission token). mori's source-registry note: 31 prefix-only digest rows and S125 unpinned, "supersession is mismatch-only" (CORPUS rule 2). | **REPORT.** mori's first-token rule is a candidate predicate for a revenger successor counter. It needs its own frozen predicate and cannot be adopted by reading. Also: check whether revenger's own registry rows carry full digests (not checked here). |
| **lore** | admitted (C1 depth, C2 coverage, C3 calibration; falsifier unsatisfied; r89 admission withdrawn by a reproduction) | admitted under conditions C-1…C-6 (WORK 32 + FOLLOW-UP 40 seats); C2 tool `corpus/tools/map_obligations.py` compares raw fixture-JSON obligations one-to-one with the canonical Markdown map rows | Coverage-map ↔ saved-record consistency: the same instrument family as revenger's K-count and README token legend (r92 C2). Content does not overlap (fiction world-bible). | **REPORT** only. A map-to-record one-to-one check is a pattern revenger could compare with its own C2 legend counter; no adoption. |
| **revenger** (self, for completeness) | admitted; C08 entry; K 9→10/15; S495–S497 | frozen at 060a8e8, no landing yet | — | — |

## 2. Lanes known only from the fleet MANIFEST (2026-11-05 closures) or the r93 scan

| lane | newest closure | overlap note | flag |
|---|---|---|---|
| kotodama | r92 admitted (14:11 BRT) | advance-evidence grader refuses seven routed counterfeits by name; 89-check selftest — a named-counterfeit battery of the kind revenger's C2 battery is. | REPORT (method overlap; no content overlap) |
| kotoba | r90 admitted (14:34 BRT) | "mutation battery over the lane's own gates" (r90 capability) — same technique as revenger's `MutationR93` (21 mutants, 20 killed). | REPORT |
| kengaku | r92 rejected-honest-stop (15:59 BRT) | not a province overlap; carried for completeness. | none |
| tabi | (r93 scan) | `corpus/adjacency.tsv:5` contested-open: tabi owns live browser/CDP page observation; revenger's C08 entry scoped to fixture + saved record only (r93 overlap.tsv). Not re-read this round. | standing, unchanged |
| tsukuroi | (r93 scan) | `PROVINCE.md:150-152`: "Kaidoku/Revenger arbitration remains unresolved; ask the protocol integrator before an internals handoff" (verified 2026-11-05 in r93). Not re-read this round. | standing, unchanged |
| kasegi, souji, kagi | MANIFEST rejections (r77/r78, r65/r66, r40) | no overlap found in closure notes. | none |

## 3. Things revenger should REPORT (not absorb)

1. **Counter reachability corroborated across lanes** (kake r94: 8 false-green routes, 7/7 admitted by the frozen r93 counter; kaidoku r93: frozen counter cannot write its receipt on honest input). These support revenger's M3 and suggest the positive control should exercise the writer path. The lane decides whether to act; this seat does not.
2. **Admission-token substring defect** (mori r94 R02, `ac[:7] in va`). Candidate predicate for a revenger successor: the verified-at first token must be a ≥7-character prefix of the admission commit. Needs its own frozen predicate.
3. **Quote-anchor defects** (kake r94 D1–D3): hyphenation breaks in quoted spans. Relevant to `audit_source_quotes.py verify` coverage.
4. **Merge-package collisions**: revenger 155/155 (r94 `ExecCensus/collision-run.log`: registry 497 ids, staged 155, collisions 155); kake 8/129 (r93). Both packages are blocked on the id-collision guard; adoption stays closed.
5. **Successor-counter pattern** (kaidoku r94 v4; kake r94 strict C1; revenger r94 C1 v3): three lanes converged on "successor counter imports the frozen verdict code by pinned sha; changes only the failing piece". Report as convergence, not as a shared instrument.

## 4. Adoption state — shokuknow merge package

`/home/vgpnk/Projects/shokuknow/merge/revenger/MERGE-REPORT.md` exists: staged by corpus-expansion-1; 155 rows accepted, 0 refused, 87 knowledge entries; nothing written into the lane repo; the report's adopt checklist (8 steps) is unexecuted. The lane's adoption is closed on the 155/155 id collisions and the unanswered L0 line `.ufo/l0-questions.md:304` (`revenger | round-91`). Nothing is adopted by this seat.

## 5. Scope notes

- No sibling file was modified; no lane file was written.
- Overlap relations are descriptive; none is a scope ruling. Contested-open rows stay contested.
- Evidence receipts for the numbers above: `measurement-r94.receipt.txt` (§1–§7).
