# Round-92 lesson — C03 admitted on three non-author votes (K 8/15 → 9/15); the C08 legend token corrected; both frozen counters pass while their known forgeries are named

Base = freeze `9402183a9492428fa0064d250746c62a0a2d9ca5` (claims, both counters, six control
receipts committed before any seat ran); landing `2760f32ba2a855a3919d7d93f962754bccd81b7b`;
wave `revenger-r92-w1` (10 seats, one v1 wave, WAVE-DONE received; results
`.ufo/waves/round-92/w1-results.json`). Claims: `reports/round-92/claims.md` (frozen; unchanged
since the freeze). This lesson is the lane's own evidence; a seat this lane dispatched is still
the lane (LEARNING.md).

## Gate

### Admission of `corpus/knowledge/round-92-managed-assembly-metadata-evidence.md` (C03)

- Drafted by `ScribeR92Entry` from the lane's own records and fixtures; its bounded wait for
  `ScoutR92Managed/sources.md` is disclosed in its report. READY digest
  `2c96e633fc730d218560b9693b881ffdeb1244cad5ac77f5fb6626f494306fb6` (admission-status line
  normalised) — recomputed by the L1 and by every voting seat; the `admitted` flip after the
  votes does not change the normalised digest.
- Three non-author votes, all bound to that digest, all 14 PASS / 3 n/a (Q05 no capability
  claim; Q08 superseded by Q11; Q12 no rejected row) / 0 FAIL:
  `reports/round-92/votes/ReviewerR92Gate.json` (ADMIT; 12 source quotes located in re-fetched
  bytes; 11/11 embedded blocks re-run with zero drift; lint 0/0/0/0; embedded 11 blocks 0
  problems), `ReviewerR92Blind.json` (own parser from fixture bytes only — CLI header 512/72,
  root 640 `BSJB`, five streams, row counts M1/T2/MD2/MR1/IM1/A1, assembly `r85-managed`
  2.0.1.5 / `r76-managed` 1.2.3.4 — **zero mismatches** against the entry's stated facts),
  `CriticR92Claims.json` (adjudication addendum: all four oracle commands re-run, fixture
  digests and `rev-parse 9402183a^{commit}` verified; three note-level beyond-quote statements
  recorded in its findings #9, none FAIL-grade).
- L1 adjudication: **admitted**. The counter `reports/round-92/c1_k_admit_counter.py --rev
  2760f32b` prints `C1_VERDICT=pass`, `C1_K_HELD_BACKED=9/15`
  (`reports/round-92/c1-after.log`).
- Editorial erratum (recorded, not fixed in the voted bytes): the entry's `recheck:` header
  line says "the three sibling commands in §8"; the commands live in the unnumbered
  `## Reproduce` section — the credit's substance was verified by all three seats (all four
  oracle commands re-run exit 0; stdout line counts 11/21/48/40). Fix routed to the entry's
  next revision.

### Source openings (CORPUS rule 1; access date 2026-11-05; quotes located in
`.ufo/waves/round-92/w1/ScoutR92Managed/snapshots/`, each quote re-located by two seats)

| id | URL | located quote (≤25 words) | disposition |
|---|---|---|---|
| S491 | ECMA-335 6th ed (June 2012) PDF | "Magic signature for physical metadata : 0x424A5342." (§II.24.2.1) | admit, spec tier A — narrower re-open of S136's source for the C03 fixture scope (W04 duplicate-URL-across-scopes expected and disclosed) |
| S492 | ECMA-335 5th ed (Dec 2010) PDF | same quote (§24.2.1) | admit, spec tier A — corroboration at the previous edition |
| S493 | PE Format, learn.microsoft.com | "208/224 8 CLR Runtime Header The CLR runtime header address and size." | admit, docs tier A — narrower re-open of S009's source (S009 scoped to `.rsrc`) |
| S494 | `MetadataRootBuilder` API, learn.microsoft.com | "Metadata root constitutes of a metadata header followed by metadata streams ( #~ , #Strings , #US , #Guid and #Blob )." | admit, docs tier A — vendor-side stream-set statement; its `#Guid` casing is not silently normalised to the records' `#GUID` |

The scout's three cautions were applied: the entry scopes `v4.0.30319` as the version the
producer reported (not an ECMA requirement); the GUID-heap casing difference is named; the
S136/S009 rows stay untouched and the new rows carry the narrower scopes. The scout also
opened the ECMA-335 Augments addendum (S136's LEADS line says "unopened") — recorded below
under Registry corrections. No existing row changed `status`, `recheck` or `used-by` this
round; four new rows enter `mined`, `opened 2026-11-05`, `recheck 180d`.

### C2 adjudication (C08 legend token)

`ExecR92Legend` independently reproduced the frozen probe over the committed corpus
(`README_TOKEN_LEGEND_MISMATCH=2 rows=['C03','C08']`) and audited the round-77 CDP record: no
rejection or quarantine marker exists, receipts exit 0, so it is work evidence and the
legend-correct token is `uncovered`. The landing flips the token; the counter over the landing
prints `C2_VERDICT=pass`, `C2_LEGEND_MISMATCH=0 rows=[]`, `C2_K_HELD=9/15
C2_K_HELD_BACKED=9/15` (`reports/round-92/c2-after.log`) — the after-state is strictly
stronger than the declared `rows=['C03']` because C03 cleared in the same landing.

### Producer trial (not an admission input; evidence only)

`ExecR92Producer` re-ran the real producer twice under `npx rea-agents@6.8.0` (host has
6.7.0; channel and reason recorded): run1 and run2 are byte-identical to each other, and
neither is byte-identical to the committed record — the diffs are exactly `evidence_id` (the
known path-sensitive field: the trial ran the fixture from scratch, so the path digest
differs) and the local-path fields. No content field differs. This bounds the entry's claims:
the committed records are records of their own runs, not byte-reproducible artifacts.

### Assimilation and considerthese

**Assimilation: none.** The `merge/revenger/` package remains in mass id drift (155/155
collisions, r91) and the L0 question (`revenger | round-91`) is unanswered; nothing adopted.
The wave-4 quarantine-first duty that r91 skipped **was performed this round**:
`ScoutR92Quarantine` hand-checked all 26 register rows (slice `.ufo/waves/round-92/w1/
ScoutR92Quarantine/verdicts.tsv`): 24 `candidate-present` (every quoted span located
verbatim in a fetched document), 2 `unverifiable`, 0 `refuse-absent`. Adoption stays closed
pending the operator's ruling; the register itself was not modified. The scout also observed
an off-by-one pattern in register rows (a row's quoted span sometimes lives in the URL the
next row cites) — recorded as an observation about the campaign's register, not a lane
defect.

`considerthese/2026-11-04.md` proposal 1 (own-work vs external share) is mined, not adopted
as a criterion: ConnectorR92Overlap measured `own-work=55` of `490` rows (11.2%) with the
declared awk command at round start; after this round's four external-source rows the share
is `own-work=55` of `494` (11.1%). Per-window split by kind lands with the lesson citing
`considerthese/2026-11-04.md` + 2026-11-05.

## Mistakes

| class | evidence pointer | captured-by | fix (shown able to fail?) |
|---|---|---|---|
| **M36 recurrence: a coverage token contradicted the saved records for two rounds while the check that catches it ran in no standing battery.** C03 said `frontier` with four oracle-checked records on disk; C08 said `frontier` with the round-77 record on disk; the frozen probe printed `README_TOKEN_LEGEND_MISMATCH=2 rows=['C03','C08']` at the freeze and nobody had run it since round 66 | `reports/round-92/controls/c2-do-nothing.log` (2 rows at base); `reports/round-66/measure.py:92` (the probe's own rule); r91 round receipts never ran it | none — no round-close step ran the probe; M36's own fix was applied in round 66 and then not re-armed | fix = registered `c2_legend_counter` as a probe in the SKILL gate registry (round-92 row) so the check has a home and a frozen entry command; red-before is the do-nothing control (2 rows), green-after `reports/round-92/c2-after.log` (0 rows). **Able to fail: yes** — the do-nothing receipt fails it |
| **The wave-4 quarantine-first duty was skipped in r91** (this lane's first round under the assimilation item adopted nothing but never hand-checked its 26-row register slice; `grep -c -i quarantin corpus/lessons/round-91.md` → 0) | `corpus/lessons/round-91.md` (0 mentions); `ScoutR92Quarantine/verdicts.tsv` (26 verdicts this round) | none — the duty had no standing reminder once adoption was refused | fix = the 26 verdicts landed this round; the lesson now records the duty as owed at every round that touches the package, adopted or not. **Able to fail: yes** — the r91 grep is the failing state and this round's verdicts file is the passing state |
| **Both round-92 frozen counters are reachable by forgeries the controls did not model** (a full C1 forgery — stub entry + fabricated votes with the right sha + invented `mined` row — passes 12/12 legs; all-`n/a` votes pass; C2 accepts any non-frontier C08 token, C08-`held`-with-seed, a trailing-cell token, and deletion of the only C08 record; a working-tree `reports/round-66/tempfile.py` would shadow the probe's stdlib import) | `.ufo/waves/round-92/w1/CriticR92Claims/findings.md` findings 1–5 with receipts (`c1-forge-full`, `c2-del-r77`, shadow-probe); `MutationR92Counters/mutants.md` (C1 21 built / 1 killed pre-READY, survivors with kill-recipes Demo A–D; C2 7 built / 4 killed) | the claims' own §9 doctrine required skip-work controls before freeze — the six committed controls were the cheapest then-known, and the critic's forgeries are the next-cheapest class; the falsification worked as designed | fix (routed to r93, recipes named, frozen files untouched per the kumitate r42 rule): C1 counter v2 — votes must name a `.ufo/waves/round-92/` review artifact whose sha matches, seat must exist in `w1/swarm-registry.json`, no all-`n/a` votes, `audit_source_quotes.py verify` on cited rows; C2 counter v2 — `C2_C08_TOKEN` leg (status exactly `uncovered`), `C2_C08_RECORD` leg (pin `corpus/live/runs/round-77/inspection.json` sha), probe run via `git archive REV` + `python3 -I`; controls `c2-partial`, `c2-held-seed`, `c2-trailing-cell`, `c2-del-r77`, Demo A–D. **Able to fail: yes** — the critic's receipts are the red state; the survivor kill-recipes were demo-verified in scratch |

## Corrections (old → new, append-only discipline)

- **D9 (r91 spotcheck): dead receipt pointer.** `reports/round-91/c2-after.log` does not
  exist; the C2 after-run lives in `reports/round-91/c1-after.log` (`-- C2 frozen probe`
  section, lines 9–13). Fixed in place only where the lane's living file allowed:
  `SKILL.md` registry row `message_tree_check` `measured-against` now cites
  `c1-after.log -- C2 frozen probe section` and names the correction (old → new logged
  here). The filed r91 records (`SCORECARD.md` round-91 rows, `corpus/lessons/round-91.md`
  receipts line) stay byte-frozen per the filed-report rule; this lesson and the r92
  SCORECARD section are their correction.
- **D2 (r91 spotcheck): record headings contradicting the round's verdict.** The r91 LOG
  heading says "(C1 verified)" and "(C2 capability, verified)" while the r91 report, lesson
  and SCORECARD rows say C1 contested and C2 NOT VERIFIED. LOG.md is append-only: the
  correction is the r92 LOG entry, which names the superseded heading. SCORECARD gets a
  correction row in its r92 section.
- **D4 (r91 spotcheck): frozen round shape not reconciled.** r91's claims said 12 seats;
  13 ran. Reconciled here: the r91 wave was 13 seats, attack share 4/13 (30.8%); the
  `w1/swarm-registry.json` milestone strings stay byte-frozen (committed wave evidence is
  not rewritten) and this lesson is the reconciliation. This round's shape (10 seats) was
  frozen in `claims.md` before dispatch and matches `w1-results.json` (10 results, no dead
  seats).
- **D5 (r91 spotcheck): report overstated the C2 control set** — two stubs (stubD, stubE)
  passed the frozen probe, not three (stubA failed it). Corrected here; the r91 bytes stay.
- **D8 (r91 spotcheck): untracked `reports/round-91/__pycache__/`** removed this round;
  `__pycache__/` added to `.gitignore`.
- **S136 scope cell (frozen by SOURCES rule 2).** S136's scope cell says the .NET
  `Ecma-335-Augments.md` addendum is "unopened — see LEADS"; that cell is not one of the three
  in-place-mutable cells (`status`, `recheck`, `used-by`), so the row's bytes are unchanged.
  The correction of record is this bullet: `ScoutR92Managed` opened the addendum (HTTP 200,
  blob `6a929a15…`, commit `b22bfee2`, 2026-10-18). The addendum's content (heap-size limits,
  metadata merging, module initializers) is exercised by no lane record, so no superseding row
  is created and the addendum stays a lead, now opened.

## Final measurements (adjudication; landing `2760f32b`)

| counter | base / control | landing | frozen target | verdict |
|---|---|---|---|---|
| C1 `c1_k_admit_counter.py --rev` | do-nothing fail, junk-stub fail (`controls/c1-*.log`) | **C1_VERDICT=pass**, `C1_K_HELD_BACKED=9/15`, 3 vote seats bound to `2c96e633…` | pass, 9/15 | **MET on the frozen counter; contested** — the critic's full forgery also passes it (findings 3–4); the vote files are wave-transcript-backed, and the §9 successor counter is routed |
| C2 `c2_legend_counter.py --rev` | do-nothing `rows=['C03','C08']` fail; junk-held, junk-deleted fail; **positive control passes** (`controls/c2-positive.log`) | **C2_VERDICT=pass**, `rows=[]`, `K_HELD==K_HELD_BACKED=9/15` | pass | **MET on the frozen counter; contested** — `partial`/`held`+seed/trailing-cell/record-deletion also pass it (findings 1–2, 5); successor routed |
| producer trial | — | run1==run2 byte-identical; both differ from the committed record only in `evidence_id` + local-path fields | — | evidence for the entry's limits, not a claim |
| census | round start exit 0 (31 W01/W04, 0 E) | round end: see `reports/round-92/census-round-end.log` | exit 0 | recorded in the report |

Receipts: `reports/round-92/c1-after.log`, `c2-after.log`, `controls/`,
`.ufo/waves/round-92/w1/` (wave evidence, committed at the landing).
