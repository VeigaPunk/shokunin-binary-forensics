# R70W1AssimSwgde — assimilation scope check: SWGDE custody guidance vs. the shipped-artifact evidence ledger

ADMIT-IN-SCOPE — the SWGDE custody/scoping material is *partly* in scope for a shipped-artifact evidence ledger
(§13/§14 of 18-F-002 and §3/§4 of 18-F-003 name how a custody/digest claim must be scoped), so one entry is
admissible as a **narrowed** amendment to the lane's held C13 row; but the *package* entry
`swgde-custody-authority-and-normative-scope.md` as written is **REJECT-ADJACENT**, and the amendment's
claim 2 rests on a premise the lane's own bytes contradict. Four located defects below.

Scope of this seat: package entry `swgde-custody-authority-and-normative-scope.md`, and SWGDE claims 1–2 of
`digest-scope-versus-provenance-amendment-2026-10-23.md`, both read-only under
`/home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/`. No file in the lane or the
campaign tree was edited.

---

## 0. What I did

Re-opened all three cited SWGDE PDFs myself today (2026-10-25), extracted the text, and located the
`shall`/`should` distinction in the source bytes myself. Digests are of the bytes I fetched today.

```
$ curl -sSL -o 2025-11-20-...-Collection-18-F-002-2.0.pdf https://www.swgde.org/wp-content/uploads/2025/12/2025-11-20-Best-Practices-for-Digital-Evidence-Collection-18-F-002-2.0.pdf
$ curl -sSL -o 2025-08-21-...-Acquisition-18-F-003-2.0.pdf https://www.swgde.org/wp-content/uploads/2025/09/2025-08-21-Best-Practices-for-Mobile-Device-Evidence-Collection-Preservation-Handling-and-Acquisition-18-F-003-2.0.pdf
$ curl -sSL -o 2025-07-12-...-Forensics-12-F-003-2.0.pdf https://www.swgde.org/wp-content/uploads/2025/09/2025-07-12-Core-Competencies-for-Mobile-Device-Forensics-12-F-003-2.0.pdf
$ sha256sum *.pdf
0beb1a51c5af349e70bda9906bee2f9cd9aa05ee329b697625cbadad4f5ea5b7  2025-01-13-...-Cloud-Service-Providers-23-F-004-1.1.pdf
593956e1e28b30e00ab3a2195a1baa9494f072043c1ba8e095b6df24053250c1  2025-07-12-Core-Competencies-for-Mobile-Device-Forensics-12-F-003-2.0.pdf
55446a4eddd1eb788897074c49725db90c3cc84b44a2b7d6f8626de67f56f410  2025-08-21-...-Acquisition-18-F-003-2.0.pdf
6a7217f1e359af6d8f8c3e9bf7062902f8a922c2e9429a1b2ffa43e8af62fd2f  2025-11-20-...-Collection-18-F-002-2.0.pdf
```

Tools: `curl` 8.23.0, `pdftotext`/`pdfinfo`/`pdftoppm` (poppler 26.08.0), `python3` 3.14.8 — all pre-installed,
nothing installed or upgraded (pacman transactions are paused host-wide).

**The located quote of the `shall`/`should` distinction** (both halves, with sections):

| document | section | page | text |
|---|---|---|---|
| 18-F-002-2.0 | §14 "Documentation" | PDF p.8 / printed "Page 6 of 8" | "The chain of custody documentation **should** be contemporaneous to the collection and include a description or unique identifier for the evidence, the date and time of receipt, and reflect all transfers." |
| 18-F-003-2.0 | §4.1 "Documentation" | PDF p.7 / printed "Page 5 of 22" | "The chain of custody documentation **shall** be contemporaneous and include a description of item(s), unique identifier(s), and the date/time of receipt or transfers. The record **shall** fully identify each person (e.g., name, title, signature) taking possession of an item." |

Location command (verbatim, both halves):

```
$ pdftotext -layout 2025-11-20-...-18-F-002-2.0.pdf - | grep -n 'chain of custody documentation should'
322:The chain of custody documentation should be contemporaneous to the collection and include a description or unique identifier for the evidence, the date and time of receipt, and reflect all transfers.
$ pdftotext -layout 2025-08-21-...-18-F-003-2.0.pdf - | grep -n 'chain of custody documentation shall'
259:The chain of custody documentation shall be contemporaneous and include a description of
```

So the `shall`/`should` distinction is **real and located** in the source bytes, at §14 of 18-F-002-2.0 and
§4.1 of 18-F-003-2.0. Both are **Final Approved Documents**, not drafts (18-F-002-2.0: approved 11/18/2025,
`Version: 2.0 (11/20/2025)`; 18-F-003-2.0: approved 6/27/2025, `Version: 2.0 (8/21/2025)`).

---

## 1. Adjacency verdict — the deciding PROVINCE sentence

**Deciding sentence** (`PROVINCE.md:3-7`, read with `PROVINCE.md:19-23`):

> "Owns: reverse engineering of shipped artifacts — native binaries, managed assemblies,
> Electron/JavaScript packages, Android APKs, archives, firmware, browser/Electron runtime
> evidence — using the REA skill and its toolset, **with an evidence-ledger discipline: every
> conclusion separates observation, inference, and unknown, and cites Evidence IDs.**"

and the refusing clause (`PROVINCE.md:22`): "**harness/evidence auditing** (harness-integrity,
gate-evidence, rlm-dispatch)".

**The README Frontier bullet that decided it** (`corpus/README.md:84-86`, the lane's own words):

> "- Evidence custody beyond fixity: collection and transfer records
>   (SWGDE collection/acquisition guidance) — **adjacent to this province; enter only
>   as it bears on shipped-artifact evidence ledgers.**"

That bullet is the lane's own pre-registered adjacency test, and it is a *conditional* admit, not a blanket
refusal: SWGDE custody guidance may enter **only as it bears on shipped-artifact evidence ledgers**.

**Applying the test per claim** (the six falsifiable claims of the package entry,
`swgde-custody-authority-and-normative-scope.md:16-56`):

| claim | line | bears on a shipped-artifact ledger? | verdict |
|---|---|---|---|
| 1. `shall`/`should` custody control + "a corpus entry that cites 'SWGDE' without naming the document and its normative word is imprecise" | :16-26 | **Yes** — the lane already cites SWGDE in two admitted entries; the second half is a citation-hygiene rule the lane's own `QUALITY.md` Q01/Q02 already implements | ADMIT (narrowed) |
| 2. Data-integrity definition has a named authority (18-F-002 §6) | :27-32 | **Yes** — it is the vocabulary for what the lane's own fixity/provenance row C13 asserts | ADMIT (narrowed) |
| 3. Acquisition hash ≠ verification hash (18-F-002 §13) | :33-39 | **Yes, strongly** — this is exactly C13's subject ("fixity and provenance (digest scope, receipts versus origin)", `corpus/README.md:49`) | ADMIT |
| 4. A mobile artifact's digest is not a stable identity (18-F-003 §3) | :40-45 | **Partly** — it is scoped to *live mobile extraction*, which the lane does not do; but it states the scope rule the lane's APK digests depend on | ADMIT only as a scope-limit, not as a mobile-forensics claim |
| 5. Provider-produced data is verified, not trusted (23-F-004 §11) | :46-50 | **No** — cloud-provider legal-demand acquisition is a different domain; and see D3, the document is watermarked ARCHIVED | REJECT-ADJACENT |
| 6. Corroboration by a second tool is expected (18-F-003 §3) | :51-56 | **Yes** — the lane's whole method is independent re-derivation (`readout.py` + `entry_checks.py` + `truth.json` oracle) | ADMIT (narrowed) |

**Verdict on the package entry `swgde-custody-authority-and-normative-scope.md`: REJECT-ADJACENT as an
entry**, because (a) claim 5 is out-of-domain and its source is withdrawn (D3), (b) claim 4's mobile-extraction
scope is a different family from the lane's packaged-APK digests, and (c) the lane already holds the C13 row
this material would feed (`corpus/README.md:49`, status `held`) — so it is an **amendment to a held row, not a
new coverage row**. It cannot be a README flip (round-70 `claims.md`: the C05 row stays single-entry under C1).

**Verdict on the amendment entry's SWGDE claims 1–2 (`digest-scope-versus-provenance-amendment-2026-10-23.md:19-35`):**

- **Claim 1 (12-F-003 §5.1–§5.8 competency headings + SWGDE's own citation rule) — ADMIT-IN-SCOPE, but only
  its citation-rule half.** The §5 heading list is a *competency framework for mobile-device forensics
  practitioners* (`5.4 Collection, Seizure, and Preservation`, `5.8 Presentation and Testimony`) — a different
  domain from shipped-artifact RE; the lane refuses "harness/evidence auditing" and does not train examiners.
  The citation rule it carries — "Any reference or quote from a SWGDE document must include the version number
  (or creation date) of the document and also indicate if the document is in a draft status" (verified at
  18-F-002-2.0 cover, PDF p.1) — *does* bear on the lane, which cites SWGDE in `corpus/SOURCES.md:17` (S003)
  and `:19` (S005).
- **Claim 2 ("the lane's digest-scope distinction is now anchored on the right side of each scope") —
  REJECT: the premise is false against the lane's own bytes.** See D1.

---

## 2. Located defects

### D1 (claim-2 premise) — the amendment attributes a phrase to the lane's C13 entry that the lane's C13 entry does not contain

`digest-scope-versus-provenance-amendment-2026-10-23.md:30-31` asserts:

> "The lane's existing entry argues that a digest is an identity in one scope and a witness in another."

The lane's `corpus/knowledge/digest-scope-versus-provenance.md` says no such thing. Its claim 1 is:

> "A digest equality claim holds only over the exact byte sequence hashed." (`:15-17`)

— a *fixity* claim, not an identity-vs-witness framing. The phrase appears nowhere in the lane:

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin
$ grep -c 'identity in one scope' corpus/knowledge/digest-scope-versus-provenance.md
0
$ grep -c 'witness in another' corpus/knowledge/digest-scope-versus-provenance.md
0
$ git log --all --oneline -S 'identity in one scope'
(no output — never present in lane history)
```

The phrase's only occurrence in the whole campaign tree is the amendment's own text:
`/home/vgpnk/Projects/shokuknow/lanes/revenger/round3/KNOWLEDGE-PROPOSED.md:333`. And the base entry the
amendment amends is **not in the merge package** — the package ships only the amendment:

```
$ ls /home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/ | grep -i digest-scope
digest-scope-versus-provenance-amendment-2026-10-23.md
```

so the amendment, as staged, lands with a `ground:` pointer to a file that is not in the package and whose
quoted framing the lane's copy does not use. The amendment is a valid *addendum* to C13's content, but its
claim-2 sentence must be rewritten against the lane's actual text (e.g. "the lane's C13 entry scopes a digest
equality claim to the exact bytes hashed and excludes origin/completeness/custody") — and its SWGDE support is
then **18-F-002 §13** (acquisition hash vs verification hash), *not* the `shall`/`should` custody contrast,
which is about *documentation of custody records*, not about digest scope. That is a content error in the
amendment's own reasoning: the `shall`/`should` contrast it offers as support for a digest-scope claim is
about chain-of-custody documentation, which the lane's C13 entry explicitly excludes
(`corpus/knowledge/digest-scope-versus-provenance.md:98-99`: "The entry does not address chain-of-custody
transfer records; custody is a separate proposed surface").

### D2 (adjacency) — the package entry's claim 4 crosses the province line as written

`swgde-custody-authority-and-normative-scope.md:40-45`:

> "**A mobile artifact's digest is not a stable identity.** … This bears directly on the Android scope: a
> digest taken from a live mobile acquisition cannot be compared with a digest taken from a packaged APK …"

The lane's Android surface (C05, `corpus/README.md:41`) is a **packaged** APK
(`corpus/fixtures/apk-r65/fixture.apk`) — never a live extraction. The lane's own C05 v5 candidate
(`aa1842f:corpus/knowledge/round-70-apk-axml-byte-evidence.md`) has **no** device/live/extraction/custody
wording at all (grep for `device|live|extraction|physical|custody|SWGDE` over the candidate: 0 hits), and its
`## Limitations` (`:237-239`) scopes to "One authored fixture" while `## Cross-lane scope note (Q10)`
(`:241-243`) fences provider claims. So claim 4's own comparison ("a digest taken from a live mobile
acquisition cannot be compared with a digest taken from a packaged APK") states a true and *useful* scope
rule — but the lane has no live-mobile-acquisition side to compare against, so **as a corpus entry about
mobile artifacts it is adjacent**; only its scope-limit half ("a packaged APK's digest identifies the
packaged bytes, not the device's state") belongs in this lane.

### D3 (freshness / source status) — the merge package cites a withdrawn document as `mined` with no note

`SOURCES.append.md:47` (S087) records SWGDE 23-F-004-1.1 with status `mined` and recheck "365d — re-fetch and
re-read its version date", and `swgde-custody-authority-and-normative-scope.md:46-50` builds claim 5 on its
§11 quote. But the PDF as published is **watermarked ARCHIVED**. The document's own §14 History says so:

```
$ grep -n 'ARCHIVED' 2025-01-13-...-23-F-004-1.1.pdf.txt
740:                  10/17/2025                  Added ARCHIVED watermark.
```

and the watermark is on every page (rendered page 2 shows a diagonal red "ARCHIVED"; the extracted text
carries the letters `ED / IV / H / C / AR` interleaved with the body text on pages 1,2,3,5,8,10 — the
signature of a diagonal watermark, 3–5 fragments per page). No `ARCHIVED` mention exists anywhere in the
merge package or in `lanes/revenger/round2/` (grep: 0 hits).

Two consequences: (a) claim 5 must not be admitted at all — it rests on a withdrawn document; (b) more
importantly, this is a **process defect in the merge package's row-gate practice**: the S087 gate in
`lanes/revenger/round2/SOURCES-PROPOSED.md:299` recorded size + sha256 but no draft/withdrawal status, while
SWGDE's own cover rule (quoted by the merge entry itself at `swgde-custody-...md:8`) requires that a reference
"indicate if the document is in a draft status". The lane's `QUALITY.md` Q01 requires the row to be tier A *for
that claim's scope*; an ARCHIVED document cannot support a normative claim.

### D4 (adjacency + coverage) — the package entry's `coverage-map:` names a row the lane does not have, and neither entry would move a counter

`swgde-custody-authority-and-normative-scope.md:9` says `coverage-map: SWGDE`, and the amendment
`digest-scope-versus-provenance-amendment-2026-10-23.md:8` says `coverage-map: SWGDE, C07`. The lane's map
(`corpus/README.md:37-50`) has 14 rows, C01–C14, and **no SWGDE row**:

```
$ grep -cE '^\| C[0-9]+ .*SWGDE' corpus/README.md
0
$ grep -cE '^\| C[0-9]+ ' corpus/README.md
14
```

The lane's SWGDE surface is a **Frontier bullet**, not a map row (`corpus/README.md:84-86`), and the surface it
would actually feed is **C13** (`corpus/README.md:49`, `held`) — not C07 (firmware images, `:43`), which the
amendment's `coverage-map:` also names without any firmware content in claims 1–2. The lane also rejects the
amendment's `S096` id space outright: the merge package's first staged id is S047 (`MERGE-REPORT.md:7`) and
the lane already holds S047–S049 for different documents (`corpus/SOURCES.md:61-63`), so the by-document
renumbering obligation recorded in `corpus/lessons/round-67.md:23-25` applies to any adoption.

### D5 (gate completeness) — neither merge entry carries the lane's admission-bar fields

Both merge entries lack `admission-status:` (grep over all 87 package entries: 0 hits — the lane's own
`corpus/README.md:12-14` and `QUALITY.md` Q11/Q12 machinery, and the C05 v5 candidate's
`admission-status: candidate`, depend on that header), and neither separates observation / inference / unknown
nor names a limitation:

```
$ grep -n -i 'limitation\|inference\|unknown\|## QUALITY\|## Gate' swgde-custody-...md digest-scope-...md
(no output in either file)
```

The lane's own admitted C13 entry has all four sections (`## Observation` `:50`, `## Inference` `:68`,
`## Unknown` `:80`, `## Limitations` `:91`), and `QUALITY.md`'s "Admission procedure" step 3 requires
"observation, inference, and unknown, and names at least one limitation". Both merge entries would also fail
the lane's `recheck:` requirement as written: entry A's `recheck:` (`:8`) is a *policy* ("365d — re-fetch each
document and re-read its version date"), not a command that re-verifies anything, and the digests it relies on
("their retrieval digests are recorded in the row gates", `:58`) live in the **campaign tree**
(`lanes/revenger/round2/SOURCES-PROPOSED.md:285,299,315`) — the merge package itself contains no digest for
any of the three PDFs (grep for the three sha256 values across `/home/vgpnk/Projects/shokuknow/merge/revenger/`:
0 hits).

---

## 3. Verdict on the two named items

1. **`swgde-custody-authority-and-normative-scope.md` — REJECT-ADJACENT.** Claim 5 is out-of-domain and
   rests on an ARCHIVED document (D3); claim 4's mobile-extraction framing crosses the province line as
   written (D2); the `coverage-map: SWGDE` row does not exist in the lane (D4); and the material that *does*
   bear (claims 1–3, 6) belongs to the lane's already-held **C13** row, so this is an amendment, not a new
   coverage row. A narrowed replacement scoped to C13 and free of claim 5 would be ADMIT-IN-SCOPE.

2. **`digest-scope-versus-provenance-amendment-2026-10-23.md`, SWGDE claims 1–2 — ADMIT-IN-SCOPE for the
   citation-rule half of claim 1 only; REJECT for claim 2 as written** (D1: the premise does not match the
   lane's C13 bytes, and the `shall`/`should` contrast offered as support is about custody documentation, which
   C13 explicitly excludes). The 12-F-003 competency-framework half of claim 1 is a different domain
   (mobile-device-forensics examiner competencies) and should not enter this lane. Claims 3–5 of that file are
   Unblob/firmware and are outside this seat's scope.

---

## 4. Exact pointers

| what | where |
|---|---|
| `shall` half, 18-F-003-2.0 §4.1 | `/tmp` fetch `2025-08-21-…18-F-003-2.0.pdf`, pdftotext line 259; PDF page 7; sha256 `55446a4e…` |
| `should` half, 18-F-002-2.0 §14 | fetch `2025-11-20-…18-F-002-2.0.pdf`, pdftotext line 322; PDF page 8; sha256 `6a7217f1…` |
| SWGDE cover citation rule | 18-F-002-2.0 PDF p.1, lines 31-33 of extracted text |
| ARCHIVED watermark | 23-F-004-1.1 §14 History, extracted line 740; visual on rendered PDF p.2 |
| deciding PROVINCE sentence | `/home/vgpnk/Projects/shokunin/revenger-shokunin/PROVINCE.md:3-7`, `:19-23` |
| adjacency bullet | `corpus/README.md:84-86` |
| C13 row (the row this would feed) | `corpus/README.md:49` |
| lane C13 entry + its exclusions | `corpus/knowledge/digest-scope-versus-provenance.md:15-17`, `:93-99` |
| lane's own SWGDE rows | `corpus/SOURCES.md:17` (S003), `:19` (S005); lead at `:98` |
| merge package entries | `/home/vgpnk/Projects/shokuknow/merge/revenger/knowledge/corpus/knowledge/` (READ-ONLY) |
| merge source rows | `/home/vgpnk/Projects/shokuknow/merge/revenger/SOURCES.append.md:46-48`, `:56` |
| campaign-tree row gates (with the digests) | `/home/vgpnk/Projects/shokuknow/lanes/revenger/round2/SOURCES-PROPOSED.md:280-320`, `round3/SOURCES-PROPOSED.md:112-135` |

## 5. Open items I could not settle

- Whether the lane wants a `SWGDE` coverage row at all: `README.md:37-50` currently has 14 rows C01–C14 and
  round-70's `claims.md` freezes `README_ROWS=14` for C2. Adding a row would move that count; the
  custody material is arguably better folded into the existing **C13** row. That is an L1 decision, not mine.
- Whether the C05 v5 candidate should carry an explicit "packaged APK digest ≠ device-state digest" sentence
  (D2). The candidate is frozen for wave 1; a wording change there is wave-2/gate territory.
- The full merge-package review (87 entries) was not mine; I checked only the two SWGDE items named plus the
  `SOURCES.append.md` SWGDE rows and the archive-tree id space.
