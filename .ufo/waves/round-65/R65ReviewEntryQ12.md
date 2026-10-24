# R65ReviewEntryQ12 — Criterion Q12 (rejected source rows)

**PASS** — Q12 is correctly `n/a` for the C05 candidate (it writes and cites no rejected source row), and no S038–S041 row is a rejected row lacking reason+flip; two minor non-Q12 defects found (Q08 row missing from the Q-map; dangling `§Sources` pointer).

Seat: `R65ReviewEntryQ12` (read-only leaf, no subagent dispatch). Reviewed at lane HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0`, claim base `3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f`. Frozen contract read first: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/claims.md` (kill rule / predicate / admission order taken from that file, not from the wave prompt).

Bytes anchored by this review (tracked files unmodified in the worktree; `git status --porcelain` lists only other seats' untracked reports):

```
e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7  corpus/knowledge/round-65-apk-axml-byte-evidence.md
ef839dcbe2e3aeb64820adfd6b3b8db569a9d3b0eea716c51a48fcb8ea70d38e  corpus/SOURCES.md
9fc7eb3fe326dda0cfa2390699af536aa880f684d80cbd92bf85814309d0349f  corpus/README.md
```

## What Q12 requires (frozen text)

`corpus/QUALITY.md:24`:

> | Q12 | A rejected source row states a reject reason grounded in a located quote, and its `flip` names a change to the source (a successor or revision) or a scope the reject reason does not exclude. | the flip asks for content the row already credits the source with, so it can never change the verdict (S008, superseded by S024) | M21 (`lessons/round-61.md`) |

The row-shape rule it enforces is `SOURCES-CONTRACT-v1.md:34-35`: a rejected row's `teaches` cell reads `REJECTED: <reason>; flip: <what would change the verdict>`. Q12's subject is **source rows**; the README coverage-map vocabulary (`frontier`/`held`/`uncovered`) is not in Q12's scope.

## 1. The Q-map says Q12 is n/a — confirmed

`corpus/knowledge/round-65-apk-axml-byte-evidence.md:151` (Q-map block opens at `:137`):

```
| Q12 | n/a | no rejected source row is written by this entry. |
```

`od -c` on that line shows no hidden marker (plain `| Q12 | n/a | no rejected source row is written by this entry. |\n`). The `n/a` names why the criterion cannot apply, satisfying `QUALITY.md:29` ("A criterion marked `n/a` names why it cannot apply"). Lane precedent uses the same disposition: `round-62-…evm…:228` (`n/a | No rejected source row is cited as support`), `round-63-…zip…:733`, `round-64-…firmware…:220` (`n/a (no rejected source row cited)`).

The basis is true on the bytes, three independent ways:

1. The entry writes no rejected row: its only status marker is `:7 admission-status: candidate …`, and `grep -c 'admission-status: rejected'` over the entry → `0`. `grep -in 'reject\|flip'` over the entry returns only `:7` (the README-flip sentence) and `:151` (the Q12 row itself).
2. The entry cites no rejected row as support: distinct `S###` ids in the entry → `S032 S034 S038 S039 S041`; registry statuses of all five are `mined` (`corpus/SOURCES.md:52` S038, `:53` S039, `:55` S041, S032/S034 status cells `mined`). S040 (`queued`, `:54`) is deliberately not cited — the entry rests its format-level claims on S032/S034, matching `claims.md` C1 ("S040 = CPython zipfile docs" opened-and-held, non-load-bearing).
3. The entry introduces no registry rows at all: the source lines in its header (`:1` S038, `:2` S039, `:3` S041) are `source:` citations, not appended rows.

## 2. No S038–S041 row is a rejected row lacking reason+flip — confirmed

`git diff --numstat 3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f..HEAD -- corpus/SOURCES.md` → `4  0  corpus/SOURCES.md` (four insertions, **zero deletions**): the round is append-only, so no pre-existing rejected row's `teaches`/`flip` text and no `status` cell was edited in place.

The four appended rows and their status column (field 8 of the contract's 11-column row):

```
S038 mined | S039 mined | S040 queued | S041 mined
```

None carries a `REJECTED` marker (`'REJECTED' in row` → `False` for each), so none owes a reason+flip; `S040` is `queued`, a legal status under `SOURCES-CONTRACT-v1.md:36` (`queued · mined · rejected`) and owes nothing under `:34-35`.

Registry-wide invariant (the rows Q12 governs), at HEAD:

```
rejected rows: ['S008', 'S012', 'S024', 'S025']
lacking reason or flip: NONE
```

Each of the four has both `REJECTED:` (reason) and `flip:` (source change) in its `teaches` cell. S008 is the Q12 anti-pattern row named by `QUALITY.md:24`; it is retained, not rewritten, and its correction is recorded in S024 ("supersedes S008 — REJECTED: …"), introduced at `0b6ddf0` (round 61), i.e. outside the round-65 diff.

The contract's own census, run read-only from the lane root (`SOURCES-CONTRACT-v1.md:69-90`) — actual output:

```
rows: 41
malformed(NF!=13) must be 0: 0
status histogram: mined=35 queued=2 rejected=4
dup ids (must be empty):
enum violations (must be empty):
mined used-by missing paths (must be empty):
```

## Findings

### Minor 1 — Q-map has no Q08 row (procedural, not a Q12 failure)

The Q-map block (`:137`–`:152`) carries 12 rows: Q01–Q07, Q09–Q13. `grep -c '^| Q08' corpus/knowledge/round-65-apk-axml-byte-evidence.md` → `0`. Every earlier entry records the supersession explicitly instead of dropping the row: `round-64-…firmware…:216` (`| Q08 | Superseded by Q11 — … |`), `round-63-…zip…:729`, `round-62-…evm…:224`, `commonjs-destructured-require-edges.md:203`, `evm-saved-interface-candidates.md:190`. This matters only because `claims.md` C1 requires "all-criteria (Q01–Q13) admission" and the entry's own `:7` says "independent Q01–Q13 review": with Q08 silently absent, a Gate recording an "all criteria" pass cannot be reconciled row-by-row against the entry. The wave itself dispatches no Q08 seat (`wave-spec.json`, 12 `R65ReviewEntryQ0*/Q1*` seats), consistent with Q08 being superseded by Q11 (`QUALITY.md:23`: "Supersedes Q08") — so the omission is cosmetic-to-procedural, changes no value, and does not touch Q12. Already recorded independently by `R65ScribeGate.md:38`. Recommended insertion before the Gate: `| Q08 | superseded by Q11 | — |`.

### Minor 2 — dangling `§Sources` pointer in the S041 source line (Q02-adjacent, not Q12)

`corpus/knowledge/round-65-apk-axml-byte-evidence.md:3` ends its registry reference with "row text in §Sources". The entry has no `§Sources` section (headings: `:9` title, `:13` Observation, `:119` Comparison with the authored oracle, `:123` Observation / inference / unknown, `:129` Limitations, `:133` Cross-lane scope note, `:137` §Q-map, `:154` Reproduce), and `corpus/SOURCES.md` has no `## Sources` heading either (headings: `:1` title, `:11` Registry, `:57` Paths, `:68` Search log, `:83` Leads). The resolvable pointer is `corpus/SOURCES.md:55`. Impact is bounded: S041's anchors are given inline as four sha256 digests plus the fixture path, so the row stays locatable; this is a documentation defect for the Q02 seat, not a Q12 condition.

### Informational — observed states that agree with the frozen admission order

- `corpus/README.md:34` at HEAD is `| C05 | Android packages (APK) | — | — | frontier |` — no premature flip; the flip is L1's after an all-criteria fresh-seat pass (`claims.md` §Admission order 1–3).
- The entry is `admission-status: candidate` (`:7`), so the frozen counter's rejected-marker scan (`admission-status: rejected`) finds nothing in this file (`grep -c` → `0`); Q12's disposition therefore cannot perturb `K_HELD` in either direction.
- S024's `teaches` cell prefixes `supersedes S008 — ` before `REJECTED:`, a literal deviation from `SOURCES-CONTRACT-v1.md:34`'s shape. It is pre-existing (`0b6ddf0`, round 61), outside the round-65 diff, and carries a well-formed reason+flip; no action in this round.

## Residual risk

- Entry-scoped conclusion: Q12 was assessed against the entry that is the C1 candidate. A later commit could append rejected rows to `corpus/SOURCES.md`; re-check with the exact commands above (`git diff --numstat <base>..<tip> -- corpus/SOURCES.md` must stay append-only, and the rejected-row reason+flip audit must stay `NONE`).
- The registry-wide rejected-row check verifies the presence and shape of reason+flip, not that each reject reason is a well-grounded located quote. The four rejected rows are all outside the round-65 diff (S008/S012/S024/S025 predate the claim base), so their quote-grounding is carried, not re-derived here.
- S040 landing as `queued` rather than load-bearing is only as safe as the entry's abstention: the entry cites S040 nowhere (verified by the distinct-id set). If a later edit cites S040 for a format-level claim, `claims.md`'s "non-load-bearing" premise for that row breaks — Q01's problem, not Q12's, but it would ride on the same row.

## Verification gaps

- **No LSP device is exposed to this seat**: `read xd://lsp` → `No such tool: xd://lsp. Mounted devices: ast_edit, debug.` All references/definition/diagnostic work above is therefore literal `grep`/`awk`/`python3` over committed bytes — the documented text fallback, not semantic proof. No markdown symbol server exists for these registry tables in any case.
- The frozen counter (`reports/round-65/measure.py`) was **not** run here; it is not needed for Q12 (the entry writes no rejected marker), and counter/measurement verdicts are other seats' remit.
- I did not re-open S008/S012/S024/S025 against their upstream documents; only their registry cells were audited.

## Tooling

No tools installed or upgraded in this seat (read-only review; no pacman/uv/npx used).
