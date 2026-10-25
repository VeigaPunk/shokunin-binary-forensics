ADMIT — both SWGDE items bear on shipped-artifact evidence ledgers (digest discipline and the lane's own digest-scope entry), so the Frontier custody bullet admits them; per-claim boundaries and flips below.

Seat: R70W2AssimScope · 2026-10-25 · assimilation scope gate (adjacency, coverage). Read-only; no file edited; no /tmp scratch created (nothing to delete). Wave-1 reports (`.ufo/waves/round-70/w1/`) were NOT read before this verdict was formed.

## Method

Opened today, hashes recorded:

```
$ sha256sum /home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/swgde-custody-authority-and-normative-scope.md \
             /home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/digest-scope-versus-provenance-amendment-2026-10-23.md
6aca33bb68a888231fdc66245da822e6d9577b5a968e4a7a7cafb9b13eaf421b  swgde-custody-authority-and-normative-scope.md
16c10b1a59a13f2f257bff5056283a0a93d73815b7ffb3e33870952615e8f29e  digest-scope-versus-provenance-amendment-2026-10-23.md
```

Deciding rule texts read this seat: `PROVINCE.md:3-7` ("Owns: reverse engineering of shipped artifacts … with an evidence-ledger discipline: every conclusion separates observation, inference, and unknown, and cites Evidence IDs") and the landed Frontier bullet `17ee7f87:corpus/README.md:84-86`:

> Evidence custody beyond fixity: collection and transfer records
> (SWGDE collection/acquisition guidance) — adjacent to this province; enter only
> as it bears on shipped-artifact evidence ledgers.

The bullet declares the *surface* adjacent; the gate question per item is whether that item *bears on shipped-artifact evidence ledgers*. `corpus/QUALITY.md` Q10 (scope to the observed family/scope, cross-lane contested scope reported not absorbed) is the adjacent criterion applied.

## Item 1 — `swgde-custody-authority-and-normative-scope.md` → ADMIT-IN-SCOPE

Deciding sentences: `PROVINCE.md:3-7` (evidence-ledger discipline is part of what the province owns) + Frontier bullet above. The entry clears the bullet's "bears on shipped-artifact evidence ledgers" test on three of its six claims:

- Claim 3 (`swgde-custody-authority-and-normative-scope.md:33-39`): acquisition hash vs verification hash — "A corpus entry about a digest must therefore say which of the two it reports" — this is the lane's own Q09 discipline (`corpus/QUALITY.md`: "A digest or receipt is claimed only for the exact bytes it hashed. It does not establish producer origin, acquisition completeness or authenticity.").
- Claim 4 (`:40-45`), the located quote opened today:

  > "This bears directly on the Android scope: a digest taken from a live mobile
  > acquisition cannot be compared with a digest taken from a packaged APK, and a
  > corpus entry asserting digest equality across two acquisitions of one device
  > would be wrong."

  The Android scope is the lane's C05 surface — the round's own target — so the claim names its bearing explicitly, not by inference.
- Claim 6 (`:56-59` region): corroboration-by-second-tool bears on Q04/Q10 tool-claim scoping.

Claims 1-2 of the entry (should/shall wording; the data-integrity definition, `:17-32`) are custody-paperwork guidance and would NOT clear the bullet alone — see boundary below.

**Boundary (would-be REJECT) + flip:** if the digest-bearing claims 3-5 were dropped and only claims 1-2 remained, the item is REJECT-ADJACENT (pure custody-transfer formality, no bearing on shipped-artifact ledgers). Flip: a SWGDE revision that ties the custody-transfer fields to artifact fixity/digest records consumed by an evidence ledger re-admits it (a change to the source, per QUALITY Q12's flip rule).

## Item 2 — claims 1-2 of `digest-scope-versus-provenance-amendment-2026-10-23.md` → ADMIT-IN-SCOPE (pair)

Deciding sentences: same PROVINCE + Frontier bullet. The pair's load-bearing claim is claim 2 (`:31-35`), the located quote opened today:

> "the *general* collection document (18-F-002) says custody documentation
> "should" be contemporaneous, while the *mobile* document (18-F-003) says it
> "shall" be — a stricter control in the scope where the artifact is not a
> stable file."

This anchors the lane's existing `corpus/knowledge/digest-scope-versus-provenance.md` (present in the landed tree: `git ls-tree 17ee7f87 corpus/knowledge/` lists it) — the digest-as-identity-vs-witness distinction is shipped-artifact ledger discipline (Q09), so the amendment bears on shipped-artifact evidence ledgers through the entry it amends.

Claim 1 (`:19-27`, the 12-F-003 §5.1-5.8 competency headings) is admissible **only as the authority anchor** for claim 2's scope assignment: it supplies the third document the mobile scope leans on and carries SWGDE's citation rule ("Any reference or quote from a SWGDE document must include the version number (or creation date) of the document…", `:25-27`), which the lane's `source:`/`verified-at:`/`recheck:` header format mirrors — a ledger-citation discipline bearing. Mined alone (headings cartography, no ledger consequence), claim 1 is REJECT-ADJACENT.

**Flip for that standalone reject:** a 12-F-003 revision whose competency clauses prescribe ledger-content requirements for acquisition records (what a record must contain, not which competencies an examiner holds) puts it in scope. **Flip for the pair:** a SWGDE revision harmonizing should/shall across 18-F-002/18-F-003 withdraws claim 2's anchor; the pair then loses its bearing and flips to REJECT-ADJACENT unless a successor document preserves the scope-asymmetric normative word.

## Coverage / leakage checks (landed bytes, commands run)

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin ls-tree --name-only 17ee7f87… corpus/knowledge/ | grep -icE "swgde|digest"
1        # the one match is corpus/knowledge/digest-scope-versus-provenance.md — no SWGDE entry admitted
$ git -C … show 17ee7f87…:corpus/README.md | grep -n -iE "swgde"
85:  (SWGDE collection/acquisition guidance) — adjacent to this province; enter only
```

- No SWGDE entry leaked into the landed corpus and no SWGDE row was added to the README — consistent with the frozen rule "never as a README flip (the C05 row stays single-entry under C1)" (`reports/round-70/claims.md`, Frontier step section).
- The on-disk lesson still carries unfilled generator slots: `corpus/lessons/round-70.md:60` `@@ADMISSION@@`, `:64` `@@ASSIMILATION@@` (also `:88` `@@LEDGER@@`, `:92` `@@ROUTED@@`; file mtime 2026-10-25 18:41). Expected pre-integration state per the frozen landing order (wave 2 decides, then one revision fills the lesson and flips README); my two decisions above are the inputs that slot consumes. Recorded as a dependency, not a defect.

## Residual risk and verification gaps

1. `coverage-map: SWGDE` (custody entry `:9`; amendment `:8` names `SWGDE, C07`) anchors to a surface for which no README map row exists — the only README SWGDE text is the Frontier bullet. When the integrator fills `@@ASSIMILATION@@`, the entry's coverage anchor should name the Frontier bullet (`corpus/README.md:84-86`), or Q02's "names the coverage-map row it fills" has no row to resolve against. Scope-gate consequence: none (admission under the theme is never a README flip).
2. I judged scope from the two markdown entries; I did not re-fetch the underlying SWGDE PDFs (their `recheck: 365d` with `verified-at: 2026-10-23` is inside the window, and the entries' own verdicts already record retrieval digests). A PDF-text mismatch would be a Q01/Q03 finding for a full QUALITY gate, not an adjacency one.
3. Amendment claims 3-5 (Unblob figures/language/dependencies, `coverage-map: …, C07`) are outside my assigned claims 1-2 and were not gated.
4. Wave-1 assimilation record not cross-checked: `.ufo/waves/round-70/w1/` was left unread before this verdict per seat discipline; the verdict above is derived solely from PROVINCE.md, the landed Frontier bullet, QUALITY.md, and the two opened documents.
