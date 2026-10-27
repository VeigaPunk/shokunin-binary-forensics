BLOCK — lesson outline is drafted and evidence-backed, but the frozen-contract bytes moved (worktree `reports/round-71/{claims.md,measure.py}` no longer hash to the pre-registration receipt) and two v6 Q16 sentences still state an unsupported whole-set credit (`:283`, `:314`); repair before the final candidate lands.

Axes: coverage (C05 v6 pre-gate text), freshness (new source row S052 + archived-inference boundary), calibration (outside-spot-check decisions re-derived). Read-only seat: no lesson edit, no lane-source write, no counter edit, no install.

This is an **outline for `corpus/lessons/round-71.md`**, not the lesson. Section skeleton and the facts each section must carry; L1 writes the file.

---

## Gate — draft outline

### Source rows opened this round (CORPUS.md rule 1: URL or command, access date, located quote)

- **S052 (new, own-work tier A).** `corpus/SOURCES.md:66`; command `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes`, re-run by this seat 2026-10-27 → exit 0, six `MATCH` lines. `sha256sum corpus/fixtures/apk-r65/entry_checks.py` → `2d4f25f6894ac86ced3c9986abd7cdbcf4c6d2aab477cda6dc515585c129b1f9`.
  - Access date: **2026-10-27** (row `opened` 2026-10-27, `recheck` 90d).
  - Located quote (the row's own recorded line, 11 words): `MATCH dex-format.html: first line 5035, folded phrase present=True: uint ENDIAN_CONSTANT = 0x12345678;`
  - Scope as written: output shape only (file, first-line number, phrase-presence flag, searched phrase), "not the raw source line". Confirmed by the re-run: e.g. `MATCH rea-android-applications.md: first line 7, …` and `MATCH dex-format.html: first line 5949, …` — a line number plus the searched phrase, no raw source line.
  - Row/lesson link gap to note: the row's anchor says the output is "recorded in `corpus/lessons/round-71.md` `## Gate`", but its `used-by` cell names only `corpus/knowledge/round-71-apk-axml-byte-evidence.md`; when the lesson lands, the append-only `used-by` field needs the lesson path added.
- No other source row was opened this round; C1's entry re-cites S038/S049/S048/S032/S034/S047/S041 (entry header lines 1–7).
- Census: `.ufo/waves/round-71/census-before.txt` — base `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f`, row count **51**, `revenger ok`, CENSUS_EXIT=0, five W04 duplicate-url notes (S024, S028, S029, S034, S048). Current file rows: `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → **52** (the S052 append). `census-after.txt` was **not** produced by this seat; L1 must run and commit it.

### Pre-gate state observed at the candidate bytes (advisory; not a vote)

- `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0`, **GATE_EXIT=0**.
- `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0`, **LINT_EXIT=0**; Q-map rows: 16 (`grep -cE '^\| Q[0-9]{2} \|'`).
- Entry header `admission-status: candidate` (`corpus/knowledge/round-71-apk-axml-byte-evidence.md:12`); README C05 still `uncovered` (`corpus/README.md:45`).
- Lesson must state these as pre-gate observations only; `HOLDS_C1_V6` cannot read yes until the wave-2 vote conjunct exists.

### Admission decisions (QUALITY.md Q01–Q16) — advisory wave-1 draft

The lesson's admission table must record at least one explicit **REJECT**, not only passes. Proposed content (all grounded, line numbers on the v6 candidate):

| Q | draft decision | observed basis |
|---|---|---|
| Q01–Q15 | pass (advisory) | item 11 wording matches stdout (`:120` vs the six `MATCH` lines); item 12's "output lines 16-18 of 20 … last two lines" matches the numbered stdout (see below); Q13 names the forged-block survivor (`:311`); Q15 states no git id (`:313`) |
| Q16 | **REJECT as written — repair needed** | `:314` says "No unguarded literal is credited", while `:283` itself names five locators-only citations (`readout.py:22`, `:76`, `:166`, `:211`, `:233-248`) and item 17 compares only AXML layout literals. `:283` also opens with "every count, offset, identifier and digest in items 1-17 is printed by the command above it", which sweeps in the manually transcribed APPNOTE widths that the same sentence later labels manual. Non-author seat `R71W1Prose.md:10-11,22` located both; this seat re-read `:283` and `:314` verbatim. |

### Outside-spot-check decisions (at least one admit and one reject, re-derived)

| # | outside item | decision | re-derivation |
|---|---|---|---|
| 1 | Round-70 non-author spot-check (`corpus/lessons/round-70-verifier-spotcheck.md:25-26`, routed defect at `:93`): `measure-after.log` omits the ten per-script `HOLD` rows | **ADMIT** | `grep -c 'HOLD ' reports/round-70/measure-after.log` → **0** while `HOLD_REPLAY=10/10` is at `:34`; `reports/round-71/measure-before.log` prints **10** `^HOLD ` rows (`grep -c` → 10) |
| 2 | Same spot-check `:94`: at the round-70 tip `C1_LINT` reads `LINT_QMAP=1 ['Q16']` | **ADMIT** | `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-70-apk-axml-byte-evidence.md` → `LINT_QMAP=1 ['Q16']`; v6 → `LINT_QMAP=0` |
| 3 | Wave-1 non-author `R71W1Prose.md:8,19`: item 12's fenced block "contain[s] 21 output lines (not 20)", so "of 20" is unsupported | **REJECT as stated** | `python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout` → **20** lines: 1–3 fixed-part sums, 4–15 twelve offset `MATCH` lines, **16–18** the three APPNOTE locators, **19–20** the two fixed-part width comparisons. The count of 21 includes the `$ python3 …` command line at candidate `:156`; entry prose `:153` ("output lines 16-18 of 20 … last two lines") is correct for the output set and needs no change on this point |
| 4 | `R71W1Prose.md:10-11`: `:283`/`:314` overclaim | **ADMIT (matches Q16 REJECT above)** | verbatim re-read of candidate `:283`, `:314`; gate at 24/24 does not read prose |

Lesson wording to use: the lesson quotes the outside item, states admit/reject, names the command and the line it re-derives, and does not upgrade an inference into a measurement (item 3 is the worked example of an outside count being off by the command line).

---

## Mistakes — draft outline

### M58 — receipt omission (assigned to this round's lesson by the pre-registration)

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M58 | receipt omission (a receipt drops rows its own predecessor prints, so a replay-dependent reader cannot see the per-checker outcomes) | `reports/round-70/measure-after.log`: `HOLD_REPLAY=10/10` at `:34`, `grep -c 'HOLD '` → **0**; `reports/round-71/measure-before.log`: ten `^HOLD <name> exit=…` rows (`grep -c '^HOLD '` → 10). Recorded by the non-author spot-check at `corpus/lessons/round-70-verifier-spotcheck.md:25-26` and routed at `:93` | round-70 non-author closure spot-check (@m_sonnet) | round-71 counter prints every verifier `HOLD <name> exit=…` row (observed in the red-before receipt); the pre-registration restates the routed window, so the lesson cites the receipt, not the label |

Teaches line: the label (`HOLD_REPLAY=10/10`) and the rows are different evidence — a footer aggregate can pass while the routed receipt is unreplayable; the fix is in the receipt, not in the predicate.

### Proposal-1 ledger (considerthese/2026-10-26.md proposal 1; mine only proposal 1)

Compact table to paste into the lesson; "held" means the adopted form still worked at the next gate this seat could observe.

| proposal (source line) | adopted? | evidence | held at next gate |
|---|---|---|---|
| 2026-10-24 #1 hex/ASCII sanity pass | no observed adoption | no entry-wide hex→ASCII checker: `grep -n 'ASCII' corpus/lint_entry.py` hits only the self-test fixture text (`:118`, `:149`) | — |
| 2026-10-24 #2 provider-refusal line | not found in lane lessons | `grep -n 'refus' corpus/lessons/round-70.md` → only `:104` (assimilation gate note), no per-round refusal line | — |
| 2026-10-24 #3 claim hit-rate ledger | adopted, round 70 | `corpus/lessons/round-70.md:131-137` | partially: its own two derivations disagree on 2 of 18 rows (`:133-137`), and the stricter reading is quoted (11/18) |
| 2026-10-25 #1 routed-repair carry-through | adopted as a seat | `.ufo/waves/round-70/w2/R70W2ConnRoutedCarry.md` header: "ALL-CARRIED … zero UNAPPLIED" | yes for v5.1; round-71 routed items (`:119/:152/:282/:310`) are the next carry-through set |
| 2026-10-25 #2 generate items from stdout | adopted | `.ufo/waves/round-70/build-entry.py` (24021 B) | yes: v6 keeps the blocks and `checked_blocks=24 problems=0`, GATE_EXIT=0 (`:9` says blocks retained byte-for-byte) |
| 2026-10-25 #4 Q-map completeness | adopted as lint | `corpus/lint_entry.py` (8909 B); `LINT_QMAP=1 ['Q16']` on the r70 entry, `0` on v6 | yes — instrument flags a real missing row and clears the v6 map |
| 2026-10-25 #5 cross-pass disagreement ledger | no observed adoption | no such ledger found in `corpus/lessons/` | — |
| 2026-10-26 #1 adoption ledger (this proposal) | adopted in this lesson | this section | n/a (first use) |
| 2026-10-26 #2 Q16 prose pre-read of open candidates | adopted in practice | wave-1 seat `.ufo/waves/round-71/w1/R71W1Prose.md` read the candidate's command-behaviour sentences and located `:283`, `:314` | yes — it found two defects the 24/24 gate cannot see |
| 2026-10-26 #3 one stated reading for hit-rate claims | adopted | `corpus/lessons/round-70.md:133-137` names both readings and leads with the stricter one | yes at the only round where it applies so far |
| 2026-10-26 #4 per-role seat yield | no observed adoption | no per-role yield table in `corpus/lessons/` | — |

Ledger shape to keep: proposal → adopted (yes/no) → evidence path → held at next gate. The pattern in the arrows is the lesson: instruments and lint checks land and hold; reporting/style proposals do not get adopted.

### Provisional mistake rows (L1 assigns ids and decides inclusion)

| draft id | class | evidence | why it belongs |
|---|---|---|---|
| M59 (provisional) | frozen-contract drift after pre-registration (the worktree copies of the frozen files no longer hash to the receipt) | receipt `reports/round-71/pre-registration.txt` records `Counter SHA-256: d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c` and `Claims SHA-256: 1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5`; `git show HEAD:reports/round-71/measure.py | sha256sum` and `git show HEAD:reports/round-71/claims.md | sha256sum` reproduce both; the worktree reads `39e92babebc5b3550f01583e360ea77211e0f0f2b9af45725d70acd1c1affcec` (measure.py, mtime 12:23:18, `git diff --stat` 41 insertions/12 deletions) and `5b95d343b7f2e5c228d22f7de4dd4d43cb9b1844e4709969d07129c6acc1d19b` (claims.md, 3/3), with `git status --porcelain` showing both modified | the frozen predicate and the vote-parsing conjunct were reworded in the worktree after the receipt was recorded; the receipt's digests are the only reproducible pre-scoring anchor. Reported, not adjudicated |
| M60 (provisional) | prose-claim drift recurrence (Q16 class, same as M53) | candidate `:283` universal "every count … is printed by the command above it" beside the same sentence's manual-width and locators-only qualifiers; `:314` "No unguarded literal is credited" contradicts `:283`'s own locator list | the frozen repair list bounded literal credit, but the summary sentences that close the section were not re-read against it; exactly the class Q16 was added for |

---

## Observed evidence (commands actually run by this seat)

| command | observed |
|---|---|
| `sed -n '1,60p' corpus/knowledge/round-71-apk-axml-byte-evidence.md` | header `admission-status: candidate` (`:12`); S038/S049/S048/S032/S034/S047/S041 rows; `verified-at: 2026-10-27` (`:9`) |
| `python3 -B corpus/fixtures/apk-r65/entry_checks.py --spec-quotes` | exit 0, six `MATCH` lines, incl. `first line 5035 … uint ENDIAN_CONSTANT = 0x12345678;` |
| `python3 -B corpus/fixtures/apk-r65/entry_checks.py --zip-layout \| wc -l` | 20 |
| `python3 -B corpus/check_embedded_outputs.py --entry <v6>` | `checked_blocks=24 problems=0`, GATE_EXIT=0 |
| `python3 -B corpus/lint_entry.py --entry <v6>` / `<r70>` | v6 `LINT_QMAP=0/Q14=0/Q15=0/HEADER=0`, LINT_EXIT=0; r70 `LINT_QMAP=1 ['Q16']` |
| `grep -c 'HOLD ' reports/round-70/measure-after.log` / `grep -c '^HOLD ' reports/round-71/measure-before.log` | 0 / 10 |
| `sha256sum corpus/fixtures/apk-r65/entry_checks.py` | `2d4f25f6…c129b1f9` |
| `git status --porcelain reports/round-71/` | ` M reports/round-71/claims.md`, ` M reports/round-71/measure.py`, `?? reports/round-71/__pycache__/` (not this seat's: no `measure.py` run occurred; `__pycache__` was already present) |
| `git log -1 --format='%H %s'` | `18200a4b18e8dfce291a74028a9012ce4401ca10 round-71: build v6 candidate and gate exit-2 cases` |

## Conflicts for the canonical Rust judge (verbatim, unadjudicated)

1. Pre-registration receipt (`reports/round-71/pre-registration.txt`): `Counter SHA-256: d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c` and `Claims SHA-256: 1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5`.
2. Worktree at measurement: measure.py `39e92bab…`, claims.md `5b95d343…`; `git show HEAD:…` reproduces both receipt digests, so the committed bytes are the pre-registered ones and the **working tree** carries post-receipt edits to the C1 vote conjuncts ("parses committed per-seat JSON vote files under `.ufo/waves/round-71/w2-votes/`" → "reads `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-71/w2-results.json`, binds four named reviewer seats…"), the kill-rule landing order, and control D's failure text.
3. Counter bytes changed again during this seat's run (`a86c6a95…` at 12:2x → `39e92bab…`), mtime `2026-10-27 12:23:18`.
4. Independent report conflict, not a code conflict: `R71W1Prose.md:8` counts 21 output lines for item 12; the command prints 20 and the candidate's `:153` count is right (see outside item 3).

## Out of scope / not done

- No `corpus/lessons/round-71.md` written; no lane source, README, SCORECARD, SOURCES or fixture edited.
- No `census-after` run; no wave-2 vote files; no counter run or edit; no git/jj mutation; no installs (none needed).
- Not verified: live re-fetch of any source URL; `R71W1Prose`'s other five correction items (`:283` wording is admitted, but its replacement text is L1's to choose); SHONEN promotion checkability.

Report: .ufo/waves/round-71/w1/R71W1LessonDraft.md
