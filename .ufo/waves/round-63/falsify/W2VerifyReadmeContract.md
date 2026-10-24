# W2VerifyReadmeContract — README contract pre-flip verification

**Seat:** `revenger-r63.W2VerifyReadmeContract` (leaf, no dispatch)
**Axes attacked:** coverage (C1 / K counter input) — the README coverage-map row that the
C1 admission would flip, and the flip draft that specifies the flip.
**Lane tip attacked:** `db55bd6488e24e956df5818ae34c2a043d7ddc12`
("round-63: C1 candidate entry (H1-H7/N1-N3 corrected), SOURCES S032+S033, round-63
lesson; README still partial pending falsify wave")
**Base compared:** `55bcb6e1aeb4d42923a4e98db6580f67142b41ac` (claim base)
**Frozen counter:** `reports/round-63/measure.py`, sha256
`3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908`, byte-identical at
`54ab973` (freeze commit) and at the tip (`git log --oneline -- reports/round-63/measure.py
reports/round-63/claims.md reports/round-63/measure-before.log` → only `54ab973`).

## Verdict

**PASS on the three mechanical questions asked; the flip is nevertheless NOT APPLICABLE yet.**

1. `corpus/README.md` at the tip has exactly **14** C-rows, **C06 still ends `| partial |`**,
   and the file is **byte-identical to the base** `55bcb6e`
   (sha256 `7ccd8d4484db710800a34a0b3718c8f73523e5c5666359e81e2f44ddbaca7ab6` on both sides —
   stronger than row-level: not one byte of the README changed since the claim base).
2. The flip draft `.ufo/waves/round-63/build/readme-flip-draft.md` proposes **exactly one**
   changed row (C06), names **only** `knowledge/round-63-zip-central-directory-evidence.md`
   in the knowledge cell (the only `knowledge/[\w.-]+\.md` match), and preserves the
   trailing `| held |` form (matches `\| held \|$`).
3. On a `/tmp` tree built from the tip commit, applying that one line **with the committed
   entry file** gives `K_HELD=7/14` **and** `K_HELD_BACKED=7/14`, `PROBE_EXIT=0`,
   `HOLDS_OK=yes`.

The flip sentence is correct and counter-ready. **The flip must not land yet**: the committed
entry at the tip still carries `admission-status: candidate`, and the committed entry bytes
contain a **false printed output** that I reproduced independently (Q11 failure) — so the
named fresh-seat Q01–Q13 pass decisions that claims.md makes a precondition do not exist for
these bytes.

## Evidence — Q1: README pre-flip state (committed bytes)

| check | command / source | observed |
|---|---|---|
| README byte-identical to claim base | `git show 55bcb6e:corpus/README.md \| sha256sum` vs `git show db55bd6:corpus/README.md \| sha256sum` | both `7ccd8d4484db710800a34a0b3718c8f73523e5c5666359e81e2f44ddbaca7ab6` |
| README diff base→tip | `git diff 55bcb6e db55bd6 -- corpus/README.md` | **empty** (no output) |
| row count | `git show db55bd6:corpus/README.md \| grep -cE '^\| C[0-9]+ '` | **14** |
| row ids | parsed from the same bytes | C01…C14, set equal to base, **0 rows differing** |
| C06 trailing form | same bytes | `| C06 \| archives (ZIP inventory) \| … \| partial \|` → ends `\| partial \|` |
| row shape | all 14 rows | 7 pipe-separated fields each (unchanged by the draft) |
| working tree vs tip | `sha256sum corpus/README.md` | `7ccd8d44…` = tip → **I did not edit the README** |
| row id set / held rows at tip | counter on the unflipped tree | `K_HELD=6/14` (C01, C04, C09, C11, C12, C13) |

No other row's text changed vs `55bcb6e` — confirmed at whole-file byte level, not only row
level. `git status --porcelain` at the end of this seat shows **no** `corpus/README.md`
entry; the only dirty paths are other seats' build/falsify drafts.

## Evidence — Q2: the flip draft flips ONLY C06

Source: `.ufo/waves/round-63/build/readme-flip-draft.md` (tracked at the tip, blob
`057801f080885b285282d63ed9c4872d7fd4a9ff`, worktree sha256
`167566d1e17cb4106c0461472aaa7c33f7f572e71570d4f3776de6a32b4e4035`).

- The draft contains **exactly two** lines matching `^\| C[0-9]+ `, and **both are C06**
  (the "Before" and the "After"). No other map row appears in the draft at all.
- The "Before" line is **byte-exact** against the committed `corpus/README.md:35` at the tip
  (compared programmatically, `before matches readme: True`).
- Field-level diff of before→after (`split('|')`, 7 fields each):

  | field | 0 | 1 (`C06`) | 2 (surface) | 3 (knowledge) | 4 (work) | 5 (status) | 6 |
  |---|---|---|---|---|---|---|---|
  | result | SAME | SAME | SAME | **DIFF** | SAME | **DIFF** | SAME |

  Only the knowledge cell and the status cell change. Surface text and the work-evidence
  cell (`fixtures/archive-r2`, `nested-r11`, `duplicate-r15`) are untouched.
- Knowledge cell after flip:
  `` `knowledge/round-63-zip-central-directory-evidence.md` (manual byte-derived central-directory readout of `fixtures/archive-r2/fixture.zip` only; no general ZIP-parser, trailing-bytes, provider-completeness or authenticity claim) ``
  - `re.findall(r'knowledge/[\w.-]+\.md', cell)` → **exactly one** path:
    `knowledge/round-63-zip-central-directory-evidence.md` — the only knowledge entry named.
  - The cell also contains the non-`.md` path `fixtures/archive-r2/fixture.zip`; the frozen
    backing regex `knowledge/[\w.-]+\.md` does not match it, so the counter's backing check is
    unaffected (verified empirically below).
  - The path form is corpus-relative (`knowledge/…`), matching every other row and matching the
    counter's resolution `(TREE / "corpus" / p).is_file()`.
- Trailing form: after-line **ends `| held |`**; `re.search(r'\| held \|$', after)` → True;
  status cell `after.rsplit('|', 2)[-2].strip()` → `held`; row regex `^\| C[0-9]+ ` → True.

## Evidence — Q3: flipping it + the committed entry on a /tmp tree

Tree source: `git archive db55bd6 corpus | tar -x -C <scratch>` (three private copies).
The flip line was applied by exact string replacement of the draft's own "Before" line —
no hand-typed line, so what was applied is literally the draft's "After" line.
Scratch root: `/tmp/revenger-r63-readmecontract/` (lane/round-owned, removed after this
report). `TMPDIR=/tmp/revenger-r63-readmecontract/tmp` for all counter runs.

| tree | README | entry file | `K_HELD` | `K_HELD_BACKED` | `K_ROW C06` | exit |
|---|---|---|---|---|---|---|
| `tree_noflip` | committed tip bytes | present | **6/14** | 6/14 | `partial` | 0 |
| `tree_flip` | tip bytes + draft's after-line | present (committed) | **7/14** | **7/14** | `held` | **0** |
| `tree_noentry` | tip bytes + draft's after-line | **deleted** | 7/14 | **6/14** | `held` | 0 |

Full `tree_flip` counter output (frozen `reports/round-63/measure.py`):

```
K_HELD=7/14 score=5.0
K_ROW C06 status=held
K_HELD_BACKED=7/14
F_COVERAGE=5/8 score=6.2
F_FAMILIES=['native-static', 'javascript', 'archives', 'firmware', 'evm']
FRESH_ROWS=18/18
C2_CONTROLS_PASS=2/2
C2_RECEIPT_B_KILLED=2/2
C2_D2_KILLED=2/2
C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2
C3_CONTROLS_PASS=2/2
C3_RECEIPT_KILLED_ATTRIBUTED=2/2
HOLD_CALIBRATION=4/4
HOLD_REPLAY=10/10
HOLDS_OK=yes
PROBE_EXIT=0
```

Independent confirmation that the flip touches nothing else: comparing the 14 rows of
`tree_noflip` against `tree_flip`, **exactly 1 row differs** (C06) and **0 non-C06 rows
differ**; held rows after the flip are `C01, C04, C06, C09, C11, C12, C13` (6 → 7); all
14 rows still have 7 pipe-separated fields.

**Ordering claim (draft F1) independently confirmed:** the same flip with the entry file
removed yields `K_HELD=7/14` but `K_HELD_BACKED=6/14` — a README flip without the committed
entry in the same revision is *not* backed.

**Draft's own simulation claims re-checked against the real counter:** the draft states
`ROWCOUNT before/after: 14 14` and `K_HELD before/after: 6 7` — confirmed (6/14 → 7/14).
The draft's in-memory `other rows identical: True` is confirmed by the row-level diff above.

## Findings

- **F1 (BLOCKING for the flip; independent reproduction).** The committed entry at the tip
  prints a **false word count**. `corpus/knowledge/round-63-zip-central-directory-evidence.md`
  line 291–292 runs
  `printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w`
  and prints `8`. I ran that exact command: it prints **7**
  (`local file header signature 4 bytes (0x04034b50)` = 7 whitespace-separated words; the
  sibling command for `end of central dir signature 4 bytes (0x06054b50)` legitimately prints
  8, and `file name length 2 bytes extra field length 2 bytes` prints 10 — both match the
  entry). One printed output in the committed entry is therefore false → the entry's own
  Q11 self-row ("pass") is not supportable for these bytes. The falsify wave's
  `W2AttackEntryQ11` reports the same defect independently; my run is a separate
  reproduction from the committed bytes. **Consequence: the flip cannot be admitted now.**
- **F2 (BLOCKING for the flip).** The entry header at the tip still reads
  `admission-status: candidate — drafted in the round-63 build wave for independent Q01–Q13
  review; the README C06 status flip is L1's and follows the fresh-seat decisions`
  (line 6 of the file). The round-62 precedent for an admitted file is
  `admission-status: admitted — recorded round-62 Gate decision in corpus/lessons/round-62.md,
  after exact-hash fresh review`. The README legend defines `held` as "at least one **admitted**
  knowledge entry covers the ground". So a `held` row naming a `candidate` file would
  contradict the legend; the flip and the header change belong in the same admission act.
- **F3 (routing, L1).** `corpus/lessons/round-63.md:158` still describes the C06 candidate as
  "**candidate drafted in seat scratch — not landed, not admitted**" with
  "full candidate at `/tmp/revenger-r63-entry/candidate.md`". That is **stale against the
  tip**: the file *is* landed at `corpus/knowledge/round-63-zip-central-directory-evidence.md`,
  and I verified the landed blob is **byte-identical** to that scratch file
  (both sha256 `a0158e99d3fa4b3cec132e03f5738015c39ca3abb56437ae1bab81e88f2d1b53`).
  The lesson's own recorded digest for the candidate (`dcfe131cbf833c90ba956a54eeadbd46314f829e88f5528b52d7baad6c8ff193`)
  is **not** the landed digest — the recorded revision trail no longer matches the committed
  bytes. The lesson's candidate-status row must be refreshed (and the named fresh-seat
  decisions recorded) before any flip. Note the working tree already carries an uncommitted
  edit to `corpus/lessons/round-63.md` (another seat's), so L1 should reconcile, not overwrite.
- **F4 (draft text — reconcile before flipping).** The draft's parenthetical is **not** the
  admitted entry's own wording, and the two disagree in both directions:
  - the parenthetical disclaims "**trailing-bytes**" — the committed entry contains **no**
    occurrence of the word "trailing" at all (`grep -ni trailing` → 0 hits);
  - the entry's own Limitations 31 disclaims "a general ZIP-parser claim, a **ZIP64** claim, a
    **compression-method-semantics** claim, or a provider-completeness or authenticity claim"
    — the parenthetical omits ZIP64 and compression-method semantics;
  - the parenthetical says "central-directory readout", while the entry's `coverage-map:`
    header claims "the **local header**, central directory and end-of-central-directory
    records of one authored ZIP fixture".
  Round-62 finding F3 (recorded in the draft itself) says the **entry's wording wins
  verbatim**. L1 should reconcile the parenthetical against the entry's `coverage-map:` header
  and `## Limitations` before writing the line.
- **F5 (draft text — consistency with the round-62 precedent; advisory).** After the flip the
  C06 row would keep the work-evidence cell `fixtures/archive-r2`, `nested-r11`,
  `duplicate-r15`, but the entry explicitly refuses the latter two ground
  (Limitations 33: "This entry covers the `fixtures/archive-r2` ground of C06 only. The C06 row
  also lists `fixtures/nested-r11` and `fixtures/duplicate-r15`; neither is examined here.").
  The round-62 held rows carry an explicit exclusion marker in the work cell for exactly this
  case — C04: "`…`; shape/semantic work is outside the new entry" — while the draft's C06
  after-line has no such marker and leaves the work cell untouched. Either add the equivalent
  exclusion note to the C06 row or accept, explicitly, that the knowledge-cell parenthetical
  carries the scope alone. (This is a text-consistency observation, not a counter finding:
  the counter prints 7/14 either way, and claims.md's void condition is "any README status
  change other than C06", which a C06-cell note does not violate.)
- **F6 (two-draft hazard for L1).** Two distinct artifacts exist and they differ:
  `.ufo/waves/round-63/build/readme-flip-draft.md` (sha256 `167566d1…`) is the clean
  **variant A**; `.ufo/waves/round-63/build/R63ReadmeFlipDraft.md` (sha256 `9ebceb0a…`) is the
  seat report and additionally offers a **"variant B"** that would name **two** knowledge
  entries in the C06 cell (the new entry plus `knowledge/2026-10-12-rea-readiness-checklist.md`).
  Both files' C06 before/after lines are byte-identical, so there is no ambiguity about the
  sentence itself — but L1 must take the line from **variant A only**. Variant B would also
  restate a pre-contract pointer whose own `coverage-map:` header reads `C14, C02`, not C06.
- **F7 (receipt completeness, minor).** The frozen-counter excerpt printed in
  `readme-flip-draft.md` shows only `K_HELD`, `K_ROW`, `K_HELD_BACKED`, `FRESH_ROWS`,
  `HOLD_CALIBRATION`, `HOLD_REPLAY`, `PROBE_EXIT` — the `C2_*`/`C3_*` and `F_*` lines are
  absent, and the sibling report explains the gap: that run was on the **base** tree, which
  predates the round-63 C3 verifier patches (`C3_RECEIPT_KILLED_ATTRIBUTED=0/2` there).
  My run is on the **tip** tree and prints `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`,
  `F_COVERAGE=5/8`, `HOLDS_OK=yes`. Nothing in the draft is contradicted; the excerpt is simply
  incomplete, and the tip-tree numbers supersede it for the flip decision.
- **F8 (out-of-scope, recorded not acted).** The README legend's `frontier` = "no knowledge and
  **no saved record**" makes C07's `frontier` token legend-stale at the tip, because
  `corpus/live/runs/round-63/inspection.json` (operation `inspect_firmware_regions`,
  evidence_id `ev_aae7529fd55b90cd55804cd45bff0fecd837dfaca3e2a132fbe9d161080ed259`) is now
  committed. claims.md forbids any README status change other than C06 this round, so C07 is
  correctly left untouched; routed debt for the next round. (The build-wave draft reaches the
  same conclusion independently.)

## Out of scope / untouched by this seat

- `corpus/README.md` — **not edited** (sha256 unchanged, `git status` clean for that path).
- No admission, no quality verdict of my own on Q01–Q13, no flip, no claim that C1 passes.
- No git/jj mutation, no commit, no index write, no `.ufo` spec/registry/MANIFEST edit, no
  fleet-repo or sibling-lane write, no target execution.
- I did not adjudicate the other falsify seats' Q-decisions; F1 and F2 are stated as the
  mechanical precondition facts I observed on committed bytes.

## Tooling

Tool/version/channel/reason: **no tool installed or updated.** Python 3 standard library
only (`re`, `pathlib`, `hashlib` via `sha256sum`, `git archive`/`git show`/`git diff`).
No `uv tool`, `npx`, or official-binary install; **no pacman transaction** (pacman is paused
host-wide). `python3 --version` was not re-pinned — the stdlib-only use requires nothing
beyond the interpreter already present.

## Artifact paths

- This report: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/falsify/W2VerifyReadmeContract.md`
- Draft under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/readme-flip-draft.md`
  (sha256 `167566d1e17cb4106c0461472aaa7c33f7f572e71570d4f3776de6a32b4e4035`)
- Sibling seat report (variant B hazard): `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/build/R63ReadmeFlipDraft.md`
  (sha256 `9ebceb0a84a9cbd39f3fa936902cd02cc510bc3c0e8e38e1af64fb93a2c905c7`)
- Scratch (disposable, removed after this report): `/tmp/revenger-r63-readmecontract/`
  (`tree_flip/`, `tree_noflip/`, `tree_noentry/`, `tmp/`)
- Not touched (another seat's scratch): `/tmp/revenger-r63-entry/`
