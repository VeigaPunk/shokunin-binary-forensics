# ScoutCiteback — round 95, w1 (scout, axis: coverage)

**Scope:** S-id token sweep and used-by state for the frozen C1 claim's entry
(`corpus/knowledge/round-95-evidence-ledger-discipline.md`), plus a three-row anchor
spot-check. Read-only seat: no lane file, no git/jj write, no scratch left behind.

Full table: `.ufo/waves/round-95/w1/ScoutCiteback/cite-back-sweep.md`

## Verdict

**No unresolved S-id token in the landing tree — the `C1_SIDS` leg will pass at
`--rev <landing>`.** 17 distinct tokens, all `S\d{3}`, all resolving to registry rows.

Candidate digest (recipe verbatim from the lane root, `python3 -B`):
`476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`
— identical to the raw file sha256 (the single `admission-status:` line, at line 21 inside
the 30-line header window, already reads `candidate`, so the normalizer is a no-op), and
identical to `ExecFrozen`'s `digest.txt`.

## Findings

1. **All 17 tokens resolve; no spaced or suffix forms.** The sweep uses the frozen
   counter's own `collect_sid_tokens` (`\bS\s?\d{2,}[a-z]?\b`) and `norm_sid` (strip inner
   whitespace, strip one trailing `[a-z]`), so it answers exactly the `C1_SIDS` question.
   Registry existence read with the counter's strict `parse_sources` (11 cells, no dupes).
   Tokens: S002, S096–S109, S500, S501.

2. **State-dependent, not a defect — `S500`/`S501` are absent at the freeze commit.**
   The freeze-commit registry has 499 rows and no `S500`/`S501` line; they exist only in
   the **uncommitted working tree** (501 rows). The counter materializes the registry from
   the tree it is given, so `--rev <landing>` is the only form where `C1_SIDS` can pass —
   and that is the frozen predicate. Reading the freeze commit alone will show
   `S500:unresolved`/`S501:unresolved`; that is the landing dependency, not a token defect.

3. **Used-by: all 17 cite-backs are single appends; no row already named the entry at
   freeze** (0 occurrences of `round-95-evidence-ledger-discipline.md` in the freeze-commit
   `corpus/SOURCES.md`; 0 rows carry the path twice in the working tree). Old → new cell
   per row is in the sweep table. The append-only rule holds: on the 15 pre-existing rows
   only the `used-by` cell changed — no `status`, `tier`, `opened` or `recheck` was touched
   — and `used-by` staying non-empty keeps `mined` correct. Every `used-by` path on every
   `mined` row resolves repo-relatively (0 missing).

4. **Supersession chains are clean.** The registry has 26 supersession edges; none of the
   17 cited sids is a superseded source. Each is its own terminal and each terminal status
   is `mined`. `REJECTED_OK` is empty and the entry cites no rejected row (the r74-rejected
   artifact it supersedes is a *knowledge file*, not a registry row).

5. **All three spot-checked anchors located.**
   - **S104** (APU abstract) — **yes**, via the committed local receipt
     `reports/evidence-ledger-2026-10-29/apu-abstract.txt`; the arXiv anchor is outside the
     permitted network set, so it was not re-fetched. The body carries *"specifies six
     necessary conditions: … visible residual unknowns, actionability, and temporal
     maintenance"* — the anchor's quoted fragment is present verbatim and the `teaches` cell
     ("explicit residual unknowns among accountable-partial-understanding conditions") is
     supported.
   - **S106** (Schum/Tecuci/Boicu chain of custody) — **yes**, via the committed local
     receipt `reports/evidence-ledger-2026-10-29/schum-p2.txt`; the DOI anchor is outside
     the permitted network set. The anchor quote is present verbatim, and the `teaches`
     cell's two halves are grounded on the same page (processing alters evidence; custody
     tracks "the persons or devices having access … the time at which they had such access,
     and what they do to the original evidence").
   - **S108** (`ecl_` claim status schema) — **yes**, re-fetched live at the pinned commit
     (permitted URL, HTTP 200, 4655 bytes, sha256 `3844e788c6ed7032627450abdd5e24b9d2a3b90c03db7e53338c1567dc51685f`).
     The anchor's **L14–27 is line-exact**: L15 `evidenceCompletionStatusSchema = z.enum([`
     with `"pass"/"fail"/"unsupported"/"truncated"/"unknown"` at L16–L20; L24
     `evidenceCompletionRecordSchema` with `claim_id` (L25), `status` (L26),
     `evidence_ids: …min(1)` (L27); the `ecl_` prefix at L82. The `teaches` cell is fully
     supported.

6. **Both new-row receipts are honest on their committed bytes.** S500 re-hashes to
   `69fe22454e4dd4721aeba2c697dc8cf414f3be4630c3d41db491821f39465b8f` (17010 bytes) and
   S501 to `f7add697322f37d7a7d69fde5e8e2c3d625344b67fb1ca32dc52dbe6bb103dac` (18784 bytes);
   lengths match, quotes present, spans byte-exact. `audit_source_quotes.py verify --sid
   S500 --sid S501` → `verified=2 unreachable=0 unresolved=0`, rc 0. The re-opened bodies
   confirm the entry's drift-check claims: the S098 anchor lines (`L122–128`, `L148–149`)
   and the S096 anchor lines (`L53`, `L58–77`, `L399–401`) are all still exact at the pinned
   commit, and `record` remains idempotent with conflicting-content rejection — **no
   drift**, exactly as the entry asserts.

7. **Minor observation, no action, not escalated:** the S500 registry row's anchor cell
   describes "`sourceAuthority`-era vocabulary"; the string `sourceAuthority` does not
   occur in the pinned body (0 hits — the real identifiers are `evidenceAuthoritySchema` and
   the L121 comment "Source authority vocabulary owned by Evidence and reused by its
   consumers."). The meaning is unambiguous and the row is tier A / `mined` /
   correctly cite-backed. The row is on the L1's landing write surface, not this seat's.

## Cross-checks reproduced (read-only, with the counter's own regexes)

`C1_ROWS_TOTAL` 15 ✓ · `C1_C10_HELD` ✓ · `C1_C10_CITES` (fileset exactly
`["knowledge/round-95-evidence-ledger-discipline.md"]`) ✓ · `C1_K_HELD_BACKED` **12/15** ✓
(held: C01, C03, C04, C06, C07, C08, C09, C10, C11, C12, C13, C15; non-held: C02
`partial`, C05 `uncovered`, C14 `partial`) · `C1_ONLY_C10` ✓ (diffed all 15 rows against
`git show cb5c26f:corpus/README.md`, the counter's `FREEZE_REV`: no non-C10 row differs,
C10 does) · `C1_SIDS` ✓ · `C1_SOURCES` ✓ · `C1_QUOTES` ✓ · `C1_PYCACHE` ✓ (no
`__pycache__`/`.pyc` under `corpus/`, `reports/round-95/`, `.ufo/waves/round-95/`; every
Python call in this seat used `python3 -B`).

`C1_ADMITTED` still reads **fail** at this stage, by design: the file's single
`admission-status:` match (line 21, within the 30-line header window) is still `candidate`;
the landing flips it to `admitted`. Exactly one match file-wide, so the H1/F10 wide-anchor
close holds.

## Confidence / remaining unknown

High confidence on findings 1–3 and 5–6: each was reproduced mechanically with the
counter's own code paths, by re-fetching at the pinned commit, or by re-hashing committed
bytes. High confidence on finding 4 (literal string search over the committed body).

**Remaining unknown:** the landing's `used-by` and `admission-status` bytes are not frozen
at the time of this sweep — they live in an uncommitted working tree. The final digest and
the final `C1_ADMITTED` value are landing-time facts this seat cannot confirm from here.

**Bounds honoured:** all writes confined to
`.ufo/waves/round-95/w1/ScoutCiteback/` and the scratch
`/fast/scratch/hyaku/revenger-r95/ScoutCiteback/` (deleted on exit). No lane file, no git
or jj write, no fleet-repo or sibling-lane touch, no `agent://all`, no subagent dispatch.
Network limited to the two permitted hosts (`raw.githubusercontent.com/morluto/rea` for the
S108 anchor; `github.com/morluto/rea` referenced by the cited rows). No tools installed.
