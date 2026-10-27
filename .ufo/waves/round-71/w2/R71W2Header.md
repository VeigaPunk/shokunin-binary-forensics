# R71W2Header — W2 re-review: v6 provenance trio / S052+S053 source rows, entry Gate/source anchors

**VERDICT: PASS** — S052's output quote, S053's rejected-source quote and flip, all cited paths, and the source rows' scope/tier verify on the final candidate bytes (`4c1eeaee88fd07e442f1bd546faf77be3957d390`); no C1-relevant defect located. Two minor notes (N1 stale lesson bullet at post-candidate tip `a16e6cb`; N2 transient hash-resolution race during concurrent jj exports) — neither touches a frozen predicate, target or kill rule. No vote file written (not a vote seat); no source edits; no tools installed.

## Final bytes established

- `git rev-parse --verify 4c1eeaee88fd07e442f1bd546faf77be3957d390^{commit}` → `4c1eeaee88fd07e442f1bd546faf77be3957d390` (goal hash genuine; abbreviated `4c1eeae` resolves to the same sha).
- HEAD moved under review (reflog, all `export from jj`): `4c1eeae` → `c6e284c` "freeze fresh falsification wave" (only `.ufo/waves/round-71/w2-*` dispatch files) → `a16e6cb` "curate sources and record frontier mistakes" (only `corpus/SOURCES.md` 4 lines + `corpus/lessons/round-71.md` 2 lines, see N1).
- Entry bytes candidate↔worktree identical: `diff <(git show 4c1eeae:corpus/knowledge/round-71-apk-axml-byte-evidence.md) corpus/knowledge/round-71-apk-axml-byte-evidence.md` → empty (`ENTRY_BYTES_IDENTICAL`).

## S052 — output quote and scope (own-work, tier A, mined)

Command, lane root, final bytes: `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes` → **exit 0, exactly six `MATCH` lines**. Binding check: `git diff --stat b7abcd8 4c1eeae -- corpus/fixtures/apk-r65/entry_checks.py corpus/snapshots/` → empty; `entry_checks.py` sha256 `2d4f25f6894ac86ced3c9986abd7cdbcf4c6d2aab477cda6dc515585c129b1f9` identical at base `b7abcd8` and worktree — the row's "stdout at lane base `b7abcd8…`" binding is sound and my fresh run reproduces it.

Registered quote (SOURCES:66 anchor = lesson Gate `corpus/lessons/round-71.md:7`, 12 words): `MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;`
Verified byte-verbatim: my fresh stdout line 5; entry item-11 block `corpus/knowledge/round-71-apk-axml-byte-evidence.md:149`; entry header S052 anchor (entry:8) points to exactly this item-11 line and to the lesson `## Gate` (heading at lesson:3) — both resolvable, no dangling anchor.

Scope/tier vs claims: output shape is exactly file, first-line number, phrase-presence flag, searched phrase; no raw source line printed. Item-11 prose (entry:120) describes the same shape per the frozen round-70 repair. Six MATCH phrases = 1 S038 + 1 S049 + 4 S048, matching the row's "six cited AOSP/REA snapshot phrases"; the four dex line numbers (5949/5956/5981/5035) independently reproduce S048's registered live lines. Header carries 8 `source:` rows: the seven claims-frontier retained tier-A rows (S038/S049/S048/S032/S034/S047/S041) + new S052 (own-work, tier A) — claims' retained list intact. Q-map Q01/Q02 descriptions (entry:299-300) match header bytes.

## S053 — rejected-source quote and flip (docs, tier A, rejected)

Live fetch 2026-10-27: `curl -sSL https://docs.python.org/3/library/zipfile.html` → 200, **139,782 bytes**, sha256 `e5eaebbea4ebde68e4759d94d54add4241968068f28996367cd07fb0d8ef9378`.
- Title: `zipfile — Work with ZIP archives — Python 3.15.2 documentation` — matches the row/lesson anchor's 3.15.2 binding (`<title>` at fetched head; S044's superseded 3.15.1 snapshot was the same 139,782-byte length, consistent with a version-string-only change).
- 14-word quote `This module provides tools to create, read, write, append, and list a ZIP file.` verbatim present (3 occurrences); introduction under `<h1>` `zipfile — Work with ZIP archives` ✓ (lesson `corpus/lessons/round-71.md:10`, 14 words ≤25-word Gate limit; S052 quote 12 words ≤25 ✓).

Flip verified: `corpus/SOURCES.md:67` status=`rejected`, opened `2026-10-27`, recheck=`on-release`, teaches="supersedes S044 — REJECTED: not load-bearing for C05 …"; S053 is **not** used by the entry (entry `grep -c zipfile` = **0** — the rejection reason "the entry makes no Python `zipfile` API claim" is byte-true; layout rests on APPNOTE S032/S034 per `corpus/SOURCES.md:80`). S044 left untouched (`corpus/SOURCES.md:58`, status still `queued`) — consistent with the registry's supersession convention (S040/S043/S045/S046 all keep pre-supersession statuses) and lesson:10 "the existing S044 row was not edited". Census 51→53 ✓ (53 `^| S` rows counted; lesson:19).

## No dangling path

`corpus/fixtures/apk-r65/entry_checks.py` (executed) ✓ · `corpus/snapshots/dex-format.html` ✓ · `corpus/lessons/round-71.md` ✓ · used-by `corpus/knowledge/round-71-apk-axml-byte-evidence.md` ✓ · `.ufo/waves/round-71/sources-s052/` and `sources-s053/` with `validate/` + `validate.log` receipts ✓ (lesson:19 names the `validate.log` files, present).

## Landing-order guardrails intact

`admission-status: candidate … wave-2 Q01–Q16 decisions pending` (entry:12), no rejected marker; `corpus/README.md:45` C05 = `uncovered`, v6 named as sixth-pass candidate "wave-2 votes pending, no coverage credit" — frozen kill-rule pre-adjudication state respected.

## Notes (minor, located)

- **N1** — At post-candidate tip `a16e6cb` the S053 `used-by` cell flips `— → corpus/lessons/round-71.md` (logged old→new at `corpus/lessons/round-71.md:19`, SOURCES-contract compliant), but the Gate bullet `corpus/lessons/round-71.md:10` still reads "S053 remains a rejected row with `used-by=—`" — stale at the tip. At the candidate bytes (what W2 votes bind) row and bullet were self-consistent (`used-by=—` both). Bookkeeping only; no predicate element references S053's used-by. Recommend folding the bullet fix into the adjudication revision if C1 passes.
- **N2** — Twice during review a concurrent jj export produced transient `fatal: bad revision '4c1eeaee88…'` for an object that `rev-parse`/`cat-file` prove present (reflog: two `export from jj` moves mid-review). Retries resolve; no repo defect located. Flagged for L1: the counter reads committed tree state while jj operations run; a retry guard on hash resolution would harden measurement runs.

## Limits

Single live fetch of the docs URL at review time; no re-run of the C1 gate/lint counter or of other seats' Q checks; N1 judged against the SOURCES contract text only; scratch `/fast/scratch/hyaku/revenger-r71/R71W2Header/` removed at close.

Report: .ufo/waves/round-71/w2/R71W2Header.md
