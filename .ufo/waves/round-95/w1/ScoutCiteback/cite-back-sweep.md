# ScoutCiteback — S-id token sweep and used-by state for the frozen C1 entry (round 95, w1)

Seat: `ScoutCiteback` (role `scout`, axis `coverage`). Read-only: no lane file was edited.

Target entry: `corpus/knowledge/round-95-evidence-ledger-discipline.md`
(working-tree bytes == freeze commit `6e0bf15fed58f357b7fa0c881371ac7616a116f7` bytes;
sha256 `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`).

Digest recipe (from the lane root, verbatim as specified in the wave spec):

```
PYTHONUTF8=1 python3 -B -c "import hashlib,re;t=open('corpus/knowledge/round-95-evidence-ledger-discipline.md',encoding='utf-8').read();n=re.sub(r'(?im)^\s*admission-status\s*:.*$','admission-status: candidate',t);print(hashlib.sha256(n.encode('utf-8')).hexdigest())"
```

→ `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`

The entry's `admission-status:` line is the single occurrence in the file (line 21, inside the
30-line header window). Its value is already `candidate`, so the normalizer is a no-op on this
entry and the normalized digest equals the raw file sha256. Cross-check: `ExecFrozen`'s
`digest.txt` carries the same value.

## 1. Token sweep

Token regex and normalization are copied from the frozen counter
(`reports/round-95/c1_k_admit_counter4.py:318` `collect_sid_tokens`,
`:322` `norm_sid`) so the sweep answers exactly the `C1_SIDS` question:

- collect: `re.findall(r"\bS\s?\d{2,}[a-z]?\b", text)`
- normalize: strip all inner whitespace, then strip ONE trailing `[a-z]`

17 distinct tokens, all in the `S\d{3}` form. No spaced form (`S 500`), no suffix form
(`S500a`), no 2-digit form. Registry row existence is read with the counter's own
`parse_sources` (strict: `^ {0,3}\|[ \t]*S[0-9]{3,}[ \t]*\|` and exactly 11 cells).

| token | normalized id | registry row exists? | status / tier / opened | current used-by cell | resolves? |
|---|---|---|---|---|---|
| S002 | S002 | yes | mined / A / 2026-10-19 | `corpus/knowledge/seed.md, corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md, corpus/knowledge/round-95-evidence-ledger-discipline.md` | yes |
| S096 | S096 | yes | mined / A / 2026-10-29 | `corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md, corpus/knowledge/round-95-evidence-ledger-discipline.md` | yes |
| S097 | S097 | yes | mined / A / 2026-10-29 | same shape (2026-10-29 entry + r95 entry) | yes |
| S098 | S098 | yes | mined / A / 2026-10-29 | same shape | yes |
| S099 | S099 | yes | mined / A / 2026-10-29 | same shape | yes |
| S100 | S100 | yes | mined / A / 2026-10-29 | same shape | yes |
| S101 | S101 | yes | mined / A / 2026-10-29 | same shape | yes |
| S102 | S102 | yes | mined / A / 2026-10-29 | same shape | yes |
| S103 | S103 | yes | mined / A / 2026-10-29 | same shape | yes |
| S104 | S104 | yes | mined / A / 2026-10-29 | same shape | yes |
| S105 | S105 | yes | mined / B / 2026-10-29 | same shape | yes |
| S106 | S106 | yes | mined / A / 2026-10-29 | same shape | yes |
| S107 | S107 | yes | mined / B / 2026-10-29 | same shape | yes |
| S108 | S108 | yes | mined / A / 2026-10-29 | same shape | yes |
| S109 | S109 | yes | mined / B / 2026-10-29 | same shape | yes |
| S500 | S500 | **yes — in the working tree only** (absent at the freeze commit) | mined / A / 2026-11-05 | `corpus/knowledge/round-95-evidence-ledger-discipline.md` | yes |
| S501 | S501 | **yes — in the working tree only** (absent at the freeze commit) | mined / A / 2026-11-05 | `corpus/knowledge/round-95-evidence-ledger-discipline.md` | yes |

**FINDING 1 (state-dependent, not a defect in the entry):** `S500` and `S501` do **not**
exist in `corpus/SOURCES.md` at the freeze commit `6e0bf15`. The freeze-commit registry has
**499** rows and `git show 6e0bf15:corpus/SOURCES.md` contains no `S500`/`S501` line
(`grep -cE '^\|S[0-9]{3,}\|'` → 499; `grep -E '^\| S50[01] '` → empty). They exist only in
the **uncommitted working tree**, where the registry has **501** rows.

Consequence: the `C1_SIDS` leg reads `corpus/SOURCES.md` from the tree it materializes.
Materialized from the freeze commit it would fail with `S500:unresolved` /
`S501:unresolved`; materialized from the landing tree it passes. The frozen predicate is
`c1_k_admit_counter4.py --rev <landing>`, so the landing tree is the one that counts — and
in the landing tree both rows are present, `mined`, tier A, opened `2026-11-05`, with the
cite-back in `used-by`. **This is the expected landing-time dependency, not a token defect.**
No token in the entry is unresolvable in the landing tree.

Note the token count is stable either way: the entry cites S500/S501 by id in prose
("the observed/derived/inferred confidence enum", "the source-authority vocabulary"),
so the ids are in the text regardless of registry state.

**FINDING 2 (supersession chain — clean):** the counter's `check_sources` resolves each
cited sid to a supersession terminal and requires the terminal to be `mined`. The full
supersession map in the registry is 26 edges (e.g. `S008→S024`, `S136→S497`); **none** of
the 17 cited sids is a superseded source of any edge. Every cited sid is its own terminal
and every terminal status is `mined`. `REJECTED_OK` is the empty set and the entry cites
no rejected row (the r74-rejected artifact it supersedes is a *knowledge file*, not a
registry row — see the entry's §Supersession). So the `C1_SOURCES` terminal check passes
for all 17.

## 2. Landing used-by update preview

The counter's `C1_SOURCES` leg requires, for the two new rows only:

```python
if ENTRY_REL not in r[10]:
    fails.append(f"{sid}:cite-back-missing")
```

with `ENTRY_REL = "knowledge/round-95-evidence-ledger-discipline.md"` — a **substring**
test against the `used-by` cell. The working tree satisfies it: S500's and S501's
`used-by` cells are exactly `corpus/knowledge/round-95-evidence-ledger-discipline.md`,
which contains `knowledge/round-95-evidence-ledger-discipline.md`.

Old cell → new cell, per cited row (the L1 applies this; this seat only previews):

| row | old used-by cell (freeze commit `6e0bf15`) | new used-by cell (working tree) | already names the entry? |
|---|---|---|---|
| S002 | `corpus/knowledge/seed.md, corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md` | `corpus/knowledge/seed.md, corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md, corpus/knowledge/round-95-evidence-ledger-discipline.md` | no (at freeze) / yes (in tree) |
| S096–S109 (14 rows) | `corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md` | `corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md, corpus/knowledge/round-95-evidence-ledger-discipline.md` | no (at freeze) / yes (in tree) |
| S500 | (row does not exist at freeze) | `corpus/knowledge/round-95-evidence-ledger-discipline.md` | n/a — new row |
| S501 | (row does not exist at freeze) | `corpus/knowledge/round-95-evidence-ledger-discipline.md` | n/a — new row |

**Flagged rows whose used-by already names the entry:** none at the freeze commit — the
freeze-commit `corpus/SOURCES.md` contains **0** occurrences of
`round-95-evidence-ledger-discipline.md`. All 17 citations in the working tree are
therefore single appends, not duplicates. Verified: **0** rows contain the r95 entry path
more than once, and **17** rows mention it (15 pre-existing + S500 + S501).

**Append-only discipline:** the SOURCES contract v1 allows only `status`, `recheck` and
`used-by` to change in place. The working-tree diff touches **only** the `used-by` cell of
S002 and of S096–S109 (`git diff corpus/SOURCES.md` — every other cell on those 17 lines
is byte-identical), plus the two appended rows. No `status`, `tier`, `opened` or `recheck`
was altered on any pre-existing row. `used-by` values stay `mined` (the contract's rule:
`mined` = cited by ≥1 path in `used-by`), so no status flip is owed.

**Path existence (the contract's census check):** every `used-by` path on every `mined`
row resolves as a repo-relative path from the lane root — 0 missing. This matters because
the contract's used-by paths are repo-relative (`corpus/knowledge/…`), whereas the
counter's `ENTRY_REL` is corpus-relative (`knowledge/…`); the corpus-relative form is a
substring of the repo-relative form, so both the counter leg and the census check pass on
the same bytes.

## 3. Anchor spot-checks against the `teaches` cells

Three rows, anchor vs. what the anchor actually points at.

### S104 — Accountable partial understanding (APU) — **located: yes**
- Registry anchor: `arXiv abs/2610.26799v1 abstract, published 2026-10-19; "visible residual unknowns, actionability, and temporal maintenance."`
- Registry `teaches`: *Agent systems need explicit residual unknowns among accountable-partial-understanding conditions.*
- The arXiv anchor is **not** a URL in the permitted network set, so it was checked against
  the committed receipt `reports/evidence-ledger-2026-10-29/apu-abstract.txt`. That body
  contains, verbatim: *"It then defines accountable partial understanding (APU) and
  specifies six necessary conditions: bounded scope with explicit assumptions, inspectable
  evidence, assigned responsibility, visible residual unknowns, actionability, and temporal
  maintenance."*
- The anchor's quoted fragment is present and contiguous. The `teaches` cell is supported:
  "visible residual unknowns" is one of the enumerated six conditions, and the row's `scope`
  cell ("APU abstract's six necessary conditions including visible residual unknowns") is
  confirmed by the same sentence.
- The entry's own adjacent-methodology row ("Names "visible residual unknowns" among six
  necessary conditions for accountable partial understanding") is consistent with the
  source.
- **located: yes** (via the committed local receipt; the anchor URL was not re-fetched —
  out of the permitted network set).

### S106 — Schum/Tecuci/Boicu chain of custody — **located: yes**
- Registry anchor: `Schum, Tecuci, Boicu, IJICI 22:298–319 (2009); p.2 author-PDF quote opened 2026-10-29; "the evidence received by the analyst is not the same as the original evidence provided by its source."`
- Registry `teaches`: *Intermediate processing can change evidence before the analyst sees it; custody tracks those acts.*
- The DOI anchor is **not** in the permitted network set; checked against the committed
  receipt `reports/evidence-ledger-2026-10-29/schum-p2.txt` (p.2 author-PDF text).
- The quoted sentence is present verbatim: *"This can mean that the evidence received by
  the analyst is not the same as the original evidence provided by its source."*
- The `teaches` cell's two halves are both grounded in the same page: (a) *intermediate
  processing can change evidence* — "the original evidence … is processed in a variety of
  ways"; (b) *custody tracks those acts* — "a chain of custody refers to the persons or
  devices having access to the original source evidence, the time at which they had such
  access, and what they do to the original evidence when they had access to it."
- The entry's S106 row ("Chain of custody tracks who/what accessed original evidence, when,
  and what they did to it; the analyst may not receive the original") tracks the source
  closely and does not overreach (it makes no PE-acquisition-SOP claim).
- **located: yes** (via the committed local receipt).

### S108 — REA `ecl_` claim status schema — **located: yes**
- Registry anchor: `` `evidenceCompletionStatusSchema` and `evidenceCompletionRecordSchema` L14–27; commit 12f6e0974cc0db0b3a9b86246accc76556837222 ``
- Registry `teaches`: *Each verifier claim binds a status to at least one Evidence ID in an `ecl_` ledger.*
- This anchor **is** a permitted-network URL (github.com/morluto/rea at the pinned commit),
  so it was fetched raw:
  `GET https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/src/domain/evidenceCompletionLedger.ts`
  → **HTTP 200**, 4655 bytes, sha256 `3844e788c6ed7032627450abdd5e24b9d2a3b90c03db7e53338c1567dc51685f`.
- Line-exact confirmation:
  - L14 `/** Terminal outcome recorded for one verifier claim. */`
  - L15 `export const evidenceCompletionStatusSchema = z.enum([`
  - L16–L20 `"pass"`, `"fail"`, `"unsupported"`, `"truncated"`, `"unknown"`
  - L21 `]);`
  - L23 `/** Strict evidence-linked result for one verifier claim. */`
  - L24 `export const evidenceCompletionRecordSchema = z.strictObject({`
  - L25 `claim_id: claimIdSchema,`
  - L26 `status: evidenceCompletionStatusSchema,`
  - L27 `evidence_ids: z.array(evidenceIdSchema).min(1),`
  - L82 `` `ecl_${digestCanonicalValue({ records }, "Completion ledger")}` `` — the `ecl_` prefix
- The anchor's line range **L14–27** is exact: it opens on the doc comment at L14 and ends
  on the last field of the record schema at L27.
- The `teaches` cell is fully supported: `claim_id` ↦ `status` (a `pass`/`fail`/
  `unsupported`/`truncated`/`unknown` enum) ↦ `evidence_ids` with `.min(1)` (≥1 Evidence
  ID), all inside a ledger whose records are hashed with the `ecl_` prefix. The entry's row
  ("status ∈ {pass, fail, unsupported, truncated, unknown} and ≥1 Evidence ID") matches the
  source exactly, including the enum members and the arity constraint.
- **located: yes** (anchor re-fetched live at the pinned commit).

## Supporting checks on the two new rows (S500 / S501)

Both receipts re-hash to their recorded `fetch_sha256`, and the quoted spans are exact:

| row | receipt `fetch_sha256` | committed body re-hash | length | quote present | span byte-exact |
|---|---|---|---|---|---|
| S500 | `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f` | match | 17010 = recorded 17010 | yes | yes |
| S501 | `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac` | match | 18784 = recorded 18784 | yes | yes |

`corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts reports/round-95/quote-receipts --sid S500 --sid S501`
→ `SUMMARY rows=2 verified=2 unreachable=0 unresolved=0`, rc 0.

The re-opened bodies confirm the drift-check claims the entry makes:

- **S500** (`evidence.ts`, the S098 source, same pinned commit): L148
  `confidence: z.enum(["observed", "derived", "inferred"])` and L149
  `authority: evidenceAuthoritySchema` — the S098 anchor line numbers (`L122–128`,
  `L148–149`) still hold exactly, and L121 carries the comment *"Source authority
  vocabulary owned by Evidence and reused by its consumers."* The `confidence` enum and the
  authority vocabulary are unchanged: **no drift**, as the entry's ledger table asserts.
  The entry's broader field list ("subject digest/format, provider, parameters,
  raw/normalized results, … limitations, locations, and an `evidence_id`") is grounded:
  `subject` carries `digest: { sha256: … }` + a `format` discriminator, and the base schema
  has `evidence_id`, `provider`, `parameters`, `raw_result`, `normalized_result`,
  `confidence`, `authority`, `limitations`, `locations`.
- **S501** (`EvidenceLedger.ts`, the S096 source, same pinned commit): L58
  `/** Record evidence idempotently; conflicting content is rejected. */`, L59
  `record(input: Evidence)`, L71 `if (existing === evidence) return ok("duplicate")`,
  L72–74 `recordsAgree(existing, evidence) ? ok("duplicate") : err(new EvidenceIntegrityError("Conflicting evidence record"))`,
  L77 `return ok("added")`, L399–401 the `clear()` block. The S096 anchor
  (`L53` class comment, `L58–77` record, `L399–401` clear) is still exact, and `record`
  remains idempotent with conflicting-content rejection: **no drift**, as the entry asserts.

**Minor observation (not a finding, no action):** the S500 registry row's anchor cell
describes the vocabulary as "`sourceAuthority`-era vocabulary"; the string `sourceAuthority`
does not occur in the pinned body (0 hits — the actual identifiers are
`evidenceAuthoritySchema` and the L121 comment "Source authority vocabulary owned by
Evidence and reused by its consumers."). The meaning is unambiguous and the row is
`tier A`/`mined`/correctly cite-backed, and the entry's own text says "the source-authority
vocabulary", which matches the source comment. Recorded as an observation only; the row is
part of the L1's landing write surface, not this seat's.

## Cross-checks on the legs this sweep bears on

Reproduced with the counter's own regexes/parsers against the working tree (read-only; the
counter itself was not run and no lane file was written):

- `C1_ROWS_TOTAL` = 15 → pass
- `C1_C10_HELD` (`corpus/README.md` C10 cell 4 == `held`) → pass
- `C1_C10_CITES` (`row_fileset(crow[2]) == ["knowledge/round-95-evidence-ledger-discipline.md"]`
  and the entry file exists) → pass (fileset is exactly that one path)
- `C1_K_HELD_BACKED` = **12** / 15 → pass (held rows: C01, C03, C04, C06, C07, C08, C09,
  C10, C11, C12, C13, C15; non-held: C02 `partial`, C05 `uncovered`, C14 `partial`)
- `C1_ONLY_C10` → pass: diffed the 15 coverage rows against `git show cb5c26f:corpus/README.md`
  (the counter's `FREEZE_REV`); **no** non-C10 row differs, and C10 does differ from base
- `C1_SIDS` → pass in the landing tree (all 17 tokens resolve)
- `C1_SOURCES` → pass (all terminals `mined`; S500/S501 `mined`/A/`2026-11-05`/cite-back
  present)
- `C1_QUOTES` → pass (see above)
- `C1_ADMITTED` → currently **fails** by design at this stage: the entry's single
  `admission-status:` line (line 21, within the 30-line header window) still reads
  `candidate`; the landing flips it to `admitted`. Exactly one match file-wide, so the
  H1/F10 wide-anchor close holds.
- `C1_PYCACHE` → pass: no `__pycache__` / `.pyc` under `corpus/`, `reports/round-95/` or
  `.ufo/waves/round-95/`. Every Python invocation in this seat used `python3 -B`.

## Findings summary

1. **No unresolved S-id token in the landing tree.** All 17 distinct tokens normalize to
   registry ids; the `C1_SIDS` leg will pass at `--rev <landing>`.
2. **State-dependent, not a defect:** `S500`/`S501` are absent from the freeze-commit
   registry (499 rows) and present only in the uncommitted working tree (501 rows). The
   counter reads the registry from the tree it materializes, so `--rev <landing>` is the
   only form in which `C1_SIDS` can pass — which is the frozen predicate anyway. Anyone
   reading the freeze commit alone will see `S500:unresolved`/`S501:unresolved`; that is
   the landing dependency, not a token defect.
3. **No row's used-by already named the entry at freeze** (0 occurrences in the freeze
   commit), so all 17 cite-backs are single appends; **0** rows carry the r95 entry path
   twice. The append-only rule is respected: only `used-by` changed on pre-existing rows.
4. **S500's anchor cell names "`sourceAuthority`"**, a string absent from the pinned body
   (the real identifiers are `evidenceAuthoritySchema` and the L121 comment). Cosmetic;
   the row is L1-owned. Noted, not escalated.
5. **All three spot-checked anchors located.** S104 and S106 confirmed against the committed
   local receipts (`reports/evidence-ledger-2026-10-29/apu-abstract.txt`,
   `…/schum-p2.txt`) — their anchors are not fetchable under the permitted network set.
   S108 re-fetched live at the pinned commit (HTTP 200); its L14–27 anchor is line-exact
   and its `teaches` cell is fully supported by the source.
6. **Both new-row receipts are honest on their committed bytes:** re-hash matches, length
   matches, quote present, span byte-exact, and `audit_source_quotes.py verify` returns
   `verified=2 unreachable=0 unresolved=0`.

Confidence: **high** for findings 1, 2, 3, 5, 6 (each reproduced mechanically with the
counter's own code paths or by re-fetching at the pinned commit); **high** for finding 4
(literal string search over the committed body).

Remaining unknown: the landing's `used-by`/`admission-status` bytes are not yet frozen —
they live in an uncommitted working tree at the time of this sweep, so the final digest
and the final `C1_ADMITTED` value are landing-time facts this seat cannot confirm.
