# R63ReadmeFlipDraft — C06 README flip sentence (draft only, not applied)

## Behaviour

Drafted the exact post-admission replacement line for the C06 coverage-map row
in `corpus/README.md`. **No repository file was edited**: `git status --short --
corpus/README.md` is empty after this seat's work, and the C06 row is still
`partial` on disk (`corpus/README.md:35`). The proposed before/after lines and
the regex/counter evidence are saved at
`.ufo/waves/round-63/build/readme-flip-draft.md`.

## The two lines

Before (current, `corpus/README.md:35`, byte-exact):

```
| C06 | archives (ZIP inventory) | `knowledge/2026-10-12-rea-readiness-checklist.md` (archive-tool row only) | `fixtures/archive-r2`, `nested-r11`, `duplicate-r15` | partial |
```

After (proposed):

```
| C06 | archives (ZIP inventory) | `knowledge/round-63-zip-central-directory-evidence.md` (manual byte-derived central-directory readout of `fixtures/archive-r2/fixture.zip` only; no general ZIP-parser, trailing-bytes, provider-completeness or authenticity claim) | `fixtures/archive-r2`, `nested-r11`, `duplicate-r15` | held |
```

What the line does: flips the status cell `partial` -> `held`; names **only**
the new admitted entry `knowledge/round-63-zip-central-directory-evidence.md`
in the knowledge cell, with a scope parenthetical in the row's existing style
(round-62 C04/C09 precedent); leaves the work-evidence cell
(`fixtures/archive-r2`, `nested-r11`, `duplicate-r15`) **unchanged**; keeps the
14-row denominator; keeps the `| held |` trailing form.

## Regex check (frozen `reports/round-63/measure.py` + `corpus/SCORECARD.md`)

Counter regexes: row `^\| C[0-9]+ `; held `\| held \|$`; status cell
`line.rsplit('|', 2)[-2].strip()`; backing paths `knowledge/[\w.-]+\.md` read
from `split('|')[3]`.

In-memory simulation against the current README text:

```
ROWCOUNT before/after: 14 14
K_HELD before/after: 6 7
after row matches row-regex: True
after row matches held-regex: True
after status cell: held
knowledge paths in cell: ['knowledge/round-63-zip-central-directory-evidence.md']
other rows identical: True
```

Variant re-check (same run, alternative B that keeps the pre-contract
checklist citation alongside the new entry — **not** recommended, offered only
so L1 can see the cost):

```
B rows= 14 held= 7 row_re= True held_re= True status_cell= held nfields= 7
  knowledge_paths= ['knowledge/round-63-zip-central-directory-evidence.md',
                    'knowledge/2026-10-12-rea-readiness-checklist.md']
  others_unchanged= True
```

Variant B also counts (the checklist file exists, so `K_HELD_BACKED` still
passes), but it names two knowledge entries where the C06 row's status should
rest on the newly admitted one; the checklist's own header is
`coverage-map: C14, C02` (not C06), so keeping it in C06's knowledge cell
re-states a pre-contract coverage pointer that the row's `held` status no
longer depends on. Variant A is the recommendation.

Frozen counter on a scratch copy of the base `corpus/` tree with the proposed
line applied and a labeled scratch entry file present
(`/tmp/revenger-r63-readmeflip`, `TMPDIR` lane-owned; repo, git index and
`.ufo` spec/registry untouched):

```
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=7/14
FRESH_ROWS=18/18
C2_CONTROLS_PASS=2/2   C2_RECEIPT_B_KILLED=2/2   C2_D2_KILLED=2/2
HOLD_CALIBRATION=4/4   HOLD_REPLAY=10/10   PROBE_EXIT=0
```

(`C3_RECEIPT_KILLED_ATTRIBUTED=0/2` in that run is expected: the scratch tree
is the base commit, which predates the round-63 C3 verifier patches; C3 is
independent of the README flip and of the C1 admission.)

Ordering fact (same simulation family): the row counts as *backed* only when
the entry file exists in the tree. A README flip without the committed entry
gives `K_HELD=7/14` but `K_HELD_BACKED=6/14` — so the entry file must land in
the same revision as the flip.

## Gates that must precede the flip (not satisfied at drafting time)

1. The entry file does not exist yet. `corpus/knowledge/` at HEAD holds no
   `round-63-zip-central-directory-evidence.md`, and the build-wave gate
   (`.ufo/waves/round-63/build/R63ReviewGateFinal.md` item 1) records the C06
   candidate as **PENDING — FLAG** (premise artifacts only: `build/zip-readout.py`
   / `zip-readout.out`, source snapshots). This draft is a sentence, not an
   admission.
2. No fresh-seat Q01–Q13 pass decisions exist for the candidate (same gate
   item 1). claims.md makes the C06 flip conditional on those decisions
   landing; the K probe measures existence, never quality.
3. Source rows S032/S033 are not yet in `corpus/SOURCES.md` (gate item 5) and
   `corpus/lessons/round-63.md` (M33, Gate quotes, search log) does not exist
   (gate item 6); both are landing prerequisites for the sourced C1 claim.
4. The parenthetical scope is provisional. Round-62 finding F3: the row
   parenthetical must be reconciled with the admitted entry's own
   `coverage-map:` header and `## Limitations`; if the entry's wording
   differs, the entry's wording wins verbatim. The scope words used here
   (byte-derived central-directory readout of `fixtures/archive-r2/fixture.zip`
   only; no general ZIP-parser, trailing-bytes, provider-completeness or
   authenticity claim) follow the frozen C1 scope sentence in
   `reports/round-63/claims.md` and the scout's finding that CRC-32, local
   offsets and EOCD exist in the bytes only (absent from `truth.json` and from
   the saved record).

## Other map rows — verification that none needs changing

- All 14 `| C` rows parse; every row keeps 7 pipe-separated fields; the
  simulated flip changes exactly one line and leaves the other 13 byte-identical
  (`others_unchanged=True`).
- C2 (firmware saved record) and C3 (verifier calibration) require no map-row
  text: `corpus/README.md` carries no per-round firmware row cell, and
  claims.md makes "any README status change other than C06" a void condition.
- Denominator unchanged at 14 (`grep -cE '^\| C[0-9]+ ' corpus/README.md` = 14).
- **Observation for L1 (not a change):** the README legend defines `frontier`
  as "no knowledge and no saved record" and `uncovered` as "work evidence exists
  but no admitted knowledge entry". Once C2 lands a firmware saved record under
  `corpus/live/runs/round-63/`, C07's status token `frontier` becomes stale
  against that legend. claims.md forbids any README status change other than
  C06 this round, so C07 is deliberately left untouched here; this is routed
  debt for the next round's claims, not a defect in the C06 flip sentence.

## Out of scope / untouched

- `corpus/README.md` (not edited — the flip is L1's, post-admission).
- The candidate entry body, its Q01–Q13 self-check, SOURCES rows S032/S033,
  `corpus/lessons/round-63.md`, `corpus/SCORECARD.md` (its K row/verdict), the
  firmware fixture/record/oracle, and the C3 verifier patches — all owned by
  other seats/L1.
- No admission, no quality verdict, and no claim that C1 or C2 or C3 passed.
- No git/jj mutation, no commit, no `.ufo` spec/registry/MANIFEST edit, no
  fleet-repo or sibling-lane write, no target execution.

## Findings

- F1. Ordering is load-bearing: the entry file must be committed in the same
  revision as the README flip, else the row does not back
  (`K_HELD=7/14`, `K_HELD_BACKED=6/14`).
- F2. The row's `held` status rests on the newly admitted entry alone. The
  pre-contract checklist citation (`knowledge/2026-10-12-rea-readiness-checklist.md`,
  `coverage-map: C14, C02`) was the pre-admission `partial` basis; naming it
  alongside the new entry (variant B) would keep counting but misstates which
  entry carries the row. Variant A recommended.
- F3. The parenthetical is provisional until the admitted entry's own
  `coverage-map:`/`## Limitations` exist (round-62 F3 applies); entry wording
  wins.
- F4. This draft cannot be applied at this moment: gate items 1, 5 and 6 of
  `R63ReviewGateFinal.md` are PENDING (no candidate entry, no S032/S033 rows,
  no lesson), and the falsify wave's named Q01–Q13 decisions have not landed.
- F5. C07's `frontier` token becomes legend-stale once C2's saved record
  lands; left untouched by design (claims.md void condition), routed as debt.

## Touched surfaces

- `.ufo/waves/round-63/build/readme-flip-draft.md` (new): proposed before/after
  lines, regex check, ordering notes.
- `.ufo/waves/round-63/build/R63ReadmeFlipDraft.md` (new, this report).
- Scratch only: `/tmp/revenger-r63-readmeflip/` (copy of the base `corpus/`
  tree via `git archive HEAD corpus`, one flipped README, one labeled stub
  entry file, one counter run) — lane/round-owned under the sanctioned
  `/tmp/revenger-r63-*` prefix; remove on landing.

Tool/version/channel/reason: no tool installed or updated (Python 3 stdlib
only — `re`, `pathlib`, `tar`, `git archive`; no `uv tool`/`npx`/official
binary install; no pacman transaction, which is paused host-wide).

## Artifact paths

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/readme-flip-draft.md`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63ReadmeFlipDraft.md`
- `/tmp/revenger-r63-readmeflip/` (scratch, disposable)
