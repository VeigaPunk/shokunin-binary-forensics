# ScribeLesson — round 96, attempt 1 — scoped findings

Seat: `ScribeLesson` (role `scribe`, registry `.ufo/waves/round-96/w1/swarm-registry.json`).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. **Drafting seat — no lane file was
written, edited or deleted.** The only writes are this report, the lesson draft, and the
receipts, all inside this seat's wave dir:
`.ufo/waves/round-96/w1/ScribeLesson/`.

Scratch: `/fast/scratch/hyaku/revenger-r96/ScribeLesson/` — created, used, **deleted** before
yield. Every Python invocation used `python3 -B`; no `__pycache__`/`.pyc` exists under
`corpus/`, `reports/round-93..96` or `.ufo/waves/round-95..96` (verified empty). No tool was
installed. No network was used: every body was re-verified from the committed bytes on disk.

**Deliverable:** `.ufo/waves/round-96/w1/ScribeLesson/lesson-draft.md` — the round-96 lesson
`## Frontier` draft, the `## Gate` sources-block draft, and the per-row `teaches` review.

---

## 1. What the draft contains

1. **`## Frontier` draft** — rows 501 → 504 (S502/S503/S504 appended inside `## Registry`),
   all tier A / `mined` / opened 2026-11-05 / used-by the round-96 entry; the census
   round-start receipt cited with its exit code and the W-code profile; the round-end census
   marked as running after landing; the tier/status histogram delta; the C02 `partial` →
   `held` frontier-row advance; the sourced-claim line.
2. **`## Gate` sources-block draft** — for each of S502/S503/S504: the URL or record path, the
   access date 2026-11-05, a ≤25-word located quote, and the quote's location named precisely
   (body span + line + section/field). The S502/S503 quotes are the receipts' own `quote`
   fields; the S504 quote is the entry function block of the saved decompiled body.
3. **Per-row `teaches` review** — one paragraph per row: whether the `teaches` sentence stays
   inside what that row's quote and anchor ground, with the overreach risks named.

## 2. Behaviour actually executed (all read-only over committed bytes)

| # | check | result |
|---|---|---|
| 1 | candidate digest re-derived from the lane root with the task's exact command | `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923` — **matches** the frozen value |
| 2 | working-tree entry bytes vs freeze-commit `ff767436…` bytes (`git show` \| `sha256sum`) | **identical**; raw file sha256 equals the normalized digest (the status line is already `candidate`) |
| 3 | S502/S503 receipt `fetch_sha256` vs committed body sha256 | **match** both (`c818ee34…3cc24`, `b5f17fdf…96ccc`); lengths 38167 / 35095 match the receipts' `length` |
| 4 | `corpus/audit_source_quotes.py verify --sid S502 --sid S503` | `verified=2 unreachable=0 unresolved=0`, exit 0 |
| 5 | quote location inside each committed body | S502 body chars 26309–26411 = **line 425**, section `## DOS MZ with Ghidra` (heading line 418); S503 body chars 257–389 = **line 3**, the frontmatter `description:` value; S504 `codeable-decompiled.c` **lines 6–10** |
| 6 | quote word counts (lane whitespace-split rule) | S502 = 12, S503 = 17, S504 = 6 — all ≤ 25 |
| 7 | census round-start receipt content + a live re-run of the identical driver command | receipt: 21 W01 + 13 W04 + `ok`, 0 E-codes, **no literal `rc=` line** (the r95 receipt has one); re-run: **rc 0**, identical 21/13/1 profile |
| 8 | census row/tier/status counts | rows 501, tier A 452 / B 21 / C 28, mined 465 / queued 16 / rejected 20 → 504 / A 455 / mined 468 after the three appends |
| 9 | coverage map read: 15 rows, C02 status `partial`, and which cells name each admitted entry | C02 cell 2 names `knowledge/seed.md` + `knowledge/2026-10-12-rea-readiness-checklist.md`; the new entry is named in **no** coverage cell; the other four admitted entries sit in C15 / C03 / C08 / C10 |
| 10 | the frozen counter's `C1_SOURCES` used-by rule vs the census's E11 resolution, measured **both directions** on the counter's own fixture tree | **the two instruments disagree** — see finding F-S1 below |
| 11 | `git status --porcelain` at finish | only `?? .ufo/waves/round-96/` (this wave's own dir) — no lane file touched |

## 3. Gates this seat did not cross

- **No lane write.** `corpus/` (incl. `SOURCES.md`, `README.md`, `lessons/`), `reports/`,
  `SCORECARD.md`, `LOG.md`, `SKILL.md`, `README.md`, `PROVINCE.md` — all untouched.
- **No git/jj write.** `git show` / `git status` only (read-only provenance).
- **No touch of** `.ufo/state`, `.ufo/watchdog.log`, the fleet repo, sibling lanes, `shokuknow`.
- **No vote file.** The frozen vote shape is scoped to ReviewerGate / ReviewerBlind / CriticR96;
  this seat is `scribe`.
- **No subagent dispatch** (leaf member; the one labrat probe allowance was not needed).
- **Scratch deleted**; receipts copied into the wave dir first.

## 4. Findings

### F-S1 — BLOCKING: the frozen counter and the census require *different* `used-by` cell forms for the three new rows

The frozen `C1_SOURCES` leg requires the new rows' `used-by` cell to be **exactly**
`knowledge/round-96-native-analysis-sessions.md` (corpus-relative; `ENTRY_REL`,
`reports/round-96/c1_k_admit_counter5.py:34-35`, enforced at `:374-383` by set-equality on the
comma-split cell). The fleet census resolves the same cell against the **lane root**
(`scripts/sources-census.sh:560-569`, roster dirs at `:452-497`), so on disk the path must be
`corpus/knowledge/round-96-native-analysis-sessions.md`.

Measured both directions on scratch fixture trees built by the counter's own `_fixture()`
(`receipts/usedby-form-conflict.log`):

| `used-by` cell | frozen counter | fleet census (`validate`) |
|---|---|---|
| `knowledge/round-96-native-analysis-sessions.md` (bare) | `C1_SOURCES=pass`, `C1_VERDICT=pass`, **rc 0** | **rc 1** — 3× `E11 S50{2,3,4} missing used-by knowledge/…` |
| `corpus/knowledge/round-96-native-analysis-sessions.md` (prefixed) | **rc 1** — `C1_SOURCES_WHY=S502:usedby-exclusivity:[…]`, `C1_VERDICT=fail` | **rc 0**, 0 E-codes |

Third option excluded by measurement: rows appended at file end draw 3× `E12 … row outside
Registry section` from the census, so the rows must sit inside `## Registry` regardless.

Every one of the lane's **501 existing rows** uses the lane-root-relative `corpus/…` form and
the census is green on all of them today (0 E-codes fleet-wide: 5084 rows, 0 missing). The
counter's own positive fixture writes the **bare** form
(`reports/round-96/c1_k_admit_counter5.py:628-641`, row builder at `:639-641`). The frozen
counter's positive control and the lane's 501-row convention therefore point opposite ways,
and no single cell value satisfies both instruments.

**Why this matters now:** the claims' kill rule is explicit — "Any leg fails ⇒ C1 **not
verified**" — while the census is the Frontier/§2b instrument. Whichever form the L1 lands,
one authoritative instrument goes red, and the round-96 lesson must record which. The L1 must
choose and record it; this seat does not decide (the counter is frozen; the census lives outside
the lane). The draft's Frontier assumes the counter wins for the **predicate** and records the
census consequence as the census line; **the L1 may decide the other way** — the alternative
makes `C1_VERDICT=fail`, a recorded miss. Route to r97 as a cross-instrument conflict.

### F-S2 — ADVISORY: the S502 receipt pins one quote; the entry's route table cites two S502 sections

The entry's route table cites `## Native targets` **and** `## DOS MZ with Ghidra` under S502,
but the S502 receipt's `quote` field pins only the CLI file-offset sentence from the latter
(body chars 26309–26411, line 425). The `## Native targets` clauses the entry paraphrases
("addresses and recovered pseudocode are analysis observations, not original source"; "provider
unavailability and unsupported metadata remain unknown rather than false") are grounded by a
**different, unlocated** span: body chars 17777–17942, body lines 290–292, 20 words, section
`## Native targets` (heading at line 285) — quoted in the draft §2b and located there.

Two notes for the L1: (a) the frozen `C1_RECEIPTS` / `C1_QUOTES` legs iterate
`RECEIPT_ROW_IDS = ("S502", "S503")` only
(`reports/round-96/c1_k_admit_counter5.py:42`, `:385-398`), so **adding a second receipt for
the same sid is the risky move** (the audit tool loads one receipt per sid); the recommended
route is to cite the second span as a located span of the already-verified S502 body — same
body, same revision, same sha256; (b) the draft's S502 `teaches` sentence is deliberately
written to claim only what the pinned quote grounds, so the row stays inside its own evidence.

### F-S3 — ADVISORY (precision): the census round-start receipt carries no literal `rc=` line

`reports/round-96/controls/census-round-start.log` ends with the driver's `revenger ok …`
marker and 0 E-codes; it has **no** literal `rc=0` line, unlike the r95 receipt
(`reports/round-95/controls/census-round-start.log`, last line `rc=0`). The exit code is
therefore an inference from the driver's own semantics (`scripts/sources-census.sh:803-806`:
exit 1 on any E-code, else exit 0) plus the absence of any E-code — not a quoted line. The
draft's Frontier says "exit 0" and names the `ok` marker; a live re-run of the identical command
returns rc 0 with the identical 21 W01 + 13 W04 profile (`receipts/census-roundstart-rerun.log`).
If the L1 wants a literal rc in the receipt, that is a control-log edit at the L1's discretion;
this seat did not touch the frozen receipt.

### F-S4 — ADVISORY: the `used-by` exclusivity leg applies only to the three new rows

`check_sources` enforces the used-by set-equality only for `NEW_ROW_IDS = ("S502","S503","S504")`
(`reports/round-96/c1_k_admit_counter5.py:41`, `:374-383`); the other 498 mined rows' used-by
cells are not re-checked for that form, so the landing edit touches only the three new rows.
The draft's Frontier line "Rows touched old→new: none" is correct for this round (no existing
row's used-by changes), and it matches the append-only rule (`CORPUS.md` rule 2: only `status`,
`recheck` and `used-by` change in place, each logged old→new in the round lesson).

### F-S5 — ADVISORY: the S503 pin and the installed copy are different documents

The pinned S503 body at `12f6e09` declares `metadata.version: "49"`; the installed
`~/.agents/skills/reverse-engineer-anything/SKILL.md` declares `version: "42"` and pins
`rea-agents@6.7.0` (S002's row). The two files are not the same bytes (35095 B pinned vs
23437 B installed; the same divergence exists for S502's file, 38167 B vs 18911 B). The Gate
block cites the **pinned** body and the draft's S503 `teaches` sentence says "declared scope",
so the row cannot be read as a statement about the installed copy. The entry's Unknown section
discloses the drift; the Gate block should not restate it as a fact about the installed skill
beyond "at revision `12f6e09`".

## 5. Out-of-scope items (not this seat's call)

- The used-by form choice (F-S1) — the L1's; it decides whether `C1_VERDICT` or the census
  goes red.
- The `## Gate` reject record and the mined mistake row that `claims.md`'s Frontier step
  requires — other seats' drafts; this seat drafted only the source-openings block.
- The `## Mistakes` mined row(s) — the L1's.
- The round-end census run, the landing of `corpus/lessons/round-96.md`, and the three
  `SOURCES.md` rows — the L1's.

## 6. Artifact paths

- Lesson draft (the deliverable): `.ufo/waves/round-96/w1/ScribeLesson/lesson-draft.md`
- This report: `.ufo/waves/round-96/w1/ScribeLesson.md`
- Receipts (all inside this seat's wave dir):
  - `.ufo/waves/round-96/w1/ScribeLesson/receipts/census-roundstart-rerun.log`
  - `.ufo/waves/round-96/w1/ScribeLesson/receipts/usedby-form-conflict.log`
  - `.ufo/waves/round-96/w1/ScribeLesson/receipts/quote-locations.log`
