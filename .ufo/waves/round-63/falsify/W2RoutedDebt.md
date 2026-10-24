# W2RoutedDebt — routed-debt reconciliation (round-63 falsify wave, attempt 1)

Seat: `revenger-r63.W2RoutedDebt` (scribe, calibration axis).
Date: 2026-10-24.
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## Deliverable

| item | value |
|---|---|
| routed-debt table (the deliverable the round report consumes) | `.ufo/waves/round-63/falsify/routed-debt.md` |
| this seat report | `.ufo/waves/round-63/falsify/W2RoutedDebt.md` |
| rows in the table | **13** (D1–D5 the five named items; D6–D11 the build wave's other routed-debt handovers; D12–D13 this seat's own findings) |
| dispositions assigned | 6 rows fixed-this-round, 6 rows bounded-future, 3 rows explicitly-unresolved — D4 and D5 carry a **split** disposition (D4: screen fixed / id note bounded; D5: receipt pin fixed / corollary unresolved), so the three counts overlap on those two rows and do not sum to 13 |
| tip under attack at read time | `98ad3a0cb26c78b95f94535897b61c7a73113428` (the tip advanced **seven times** during this seat: `db55bd6` → `aaa0463` → `3af3acb` → `34cfa24` → `f6c618b` → `f6ea293` → `98ad3a0`; the last is the round's final integration commit) |

The table is the deliverable; this report states what was found, what was
verified, and what could not be settled.

## What was collected

All five items named in the assignment, plus every other routed-debt handover
present in the build-wave reports and the committed lesson:

| row | item | disposition | owner |
|---|---|---|---|
| D1 | M35 residual unguarded `stdout_sha256` receipt conjunct (widened by the falsify wave from one script to **both**) | bounded-future | next round's revenger L1 |
| D2 | C07 `frontier`-token legend staleness | bounded-future | next round's revenger L1 (claims author) |
| D3 | `HOLDS_OK` contract-wording drift (D1) | bounded-future | next round's contract author + this round's adjudicator |
| D4 | S033-screen recording (zipfile-docs screen-and-exclusion + its forward id note) | fixed-this-round (screen) / bounded-future (id note) | next round's source-opener seat |
| D5 | Evidence-ID transplant corollary | fixed-this-round (receipt pin) / explicitly-unresolved (the corollary) | round report author / **unassigned** for the mechanism |
| D6 | round-62 closure defect (a) — `measure-after.log` beside the report claim | fixed-this-round (committed in `98ad3a0`) | closed |
| D7 | sibling scope on archives/firmware (ADJ-06 open) | explicitly-unresolved | fleet operator (ADJ-06) |
| D8 | outside spot-check for round 63 | explicitly-unresolved | independent closure seat |
| D9 | `C2_RECEIPT_B_KILLED_ATTRIBUTED` printed but absent from `holds_ok` | bounded-future | this round's L1 + next round's contract author |
| D10 | search-log count convention for the own-work row | fixed-this-round (accepted-as-is, recorded) | closed |
| D11 | LEDGER "zero padding" wording leak (L2) | fixed-this-round | closed |
| D12 | **new** — lesson id-paragraph / search-log counts vs the tip's registry | fixed-this-round (all three halves marked at `34cfa24`) | closed |
| D13 | **new** — the tip moved seven times under the falsify wave; byte-pinned findings need re-anchoring | bounded-future | falsify adjudicator + L1 |

## Verification performed (all re-run by this seat)

- **Every pointer opened.** A script walked every backticked `path:line` pointer
  in the table and checked that the file exists, the line is in range, and the
  line is non-empty: **all pointers resolve** (79 pointers over 32 files). One
  pointer was wrong on the first pass (`.ufo/waves/round-63/build/R63LessonDraft.md:275`
  — that file is 162 lines at build commit `2a34e45`) and was corrected to
  `:88-96`.
- **Every digest re-derived, not trusted.** `git show 98ad3a0:corpus/live/runs/round-63/receipt.json | sha256sum` = `e930a549…5c6b94d`; the committed LEDGER pin at `:26` now matches it (it was `…5c6b94b` at `db55bd6` — the falsify wave's `W2AttackRecordForgery` located that mis-key and `aaa0463` fixed it).
- **The `HOLDS_OK` drift re-derived from code**, not from the report: `reports/round-63/measure.py:179-181` vs `reports/round-61/measure.py:111` — three added conjuncts (`killed_b == 2`, `c3_controls == 2`, `fresh == 18`), so `reports/round-63/claims.md:97` ("same definitions as the round-61 probe") is strictly false for `HOLDS_OK` alone.
- **The M35 debt re-confirmed on tip bytes**: `corpus/verify_icon_states.py:121` and `corpus/verify_named_multi_icon_states.py:17` still carry the `stdout_sha256` conjunct; the verifiers are byte-unchanged between `db55bd6` and `3af3acb` (`git diff --stat` empty).
- **The registry re-censused** with the seven commands of
  `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md:71-81`
  run against `98ad3a0:corpus/SOURCES.md`: rows **35**, malformed **0**, tier
  A=33/C=2, status mined=30/queued=1/rejected=4, duplicate ids **none**, enum
  and tier-inflation violations **none**, mined `used-by` paths missing **none**.
- **The entry's S-id census at the tip**: `S032 ×14 / S033 ×12 / S034 ×17 /
  S035 ×12` (at `98ad3a0`; `35` registry rows, ending at S035).

## Findings worth the round report's attention

1. **Two of the five named items have no row in the committed lesson's routed-debt
   table.** The committed `corpus/lessons/round-63.md:295-301` carries five rows
   (closure defect (a), `HOLDS_OK` drift, `stdout_sha256`, sibling scope,
   outside spot-check) — **C07's legend staleness (D2) and the Evidence-ID
   transplant corollary (D5) are in none of them**, and neither appears anywhere
   in the committed corpus (`grep -c "C07" corpus/lessons/round-63.md` = 0;
   `grep -c -i "transplant\|preimage" corpus/lessons/round-63.md` = 0). They
   live only in build-wave and falsify-wave reports. **The round report must
   carry D2 and D5 explicitly or they drop out of the round record entirely.**
2. **D5's mechanism has no owner.** The transplant corollary can be *stated*,
   but no bounded mechanism is named for closing it: `measure.py` and
   `oracle_check.py` read neither the receipt nor the Evidence ID
   (`grep -n "receipt\|evidence_id" corpus/live/runs/round-63/oracle_check.py`
   → no hit), and no ledger digest binds `LEDGER.md` to `inspection.json`.
   The falsify wave re-verified this independently (`W2AttackRecordForgery.md:41`)
   and showed the only stopper is *cross-row* reconciliation at adjudication —
   a process stopper, not an artifact check.
3. **The tip moved seven times under the falsify wave** (`db55bd6` → `aaa0463` →
   `3af3acb` → `34cfa24` → `f6c618b` → `f6ea293` → `98ad3a0`). Several falsify findings were measured on
   pre-correction bytes; one of them (the entry's "No third source is cited") has
   already been **fixed** by `3af3acb` (entry `:682` now reads "No fifth source
   is cited: S032, S033, S034 and S035 above are this entry's complete registry
   basis"). Adjudication must be anchored to the final commit (D13).
4. **D12 is now closed at the tip, by the round's own commits.** The three
   places where the lesson's draft-time counts disagree with the landed registry
   all carry an explicit UPDATE marker as of `34cfa24`/`f6ea293`: the id-allocation
   paragraph (`corpus/lessons/round-63.md:152-157`), the search-log note (`:250`),
   and (already at `3af3acb`) the entry's source sentence (`:682`). The
   draft-time sentences are retained rather than rewritten, per the append-only
   rule — the markers are the record. The round report should quote the registry
   census, not the lesson's numbers.
5. **D6 is discharged at the final tip.** Commit `98ad3a0` lands
   `reports/round-63/measure-after.log` and `reports/round-63/final-verification.json`
   as **tracked** files. I read the committed log: it records
   `FINAL_TIP=f6ea293…`, `K_HELD=7/14 score=5.0`, `K_ROW C06 status=held`,
   `K_HELD_BACKED=7/14`, `F_COVERAGE=5/8 score=6.2`, `F_FAMILIES=[… firmware …]`,
   `FRESH_ROWS=18/18`, `C2_RECEIPT_B_KILLED_ATTRIBUTED=2/2`,
   `C3_CONTROLS_PASS=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`,
   `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`, `PROBE_EXIT=0`.
   The round-62 closure defect requires this output committed **beside the report
   claim**, which `98ad3a0` does. **Caveat:** the log's `FINAL_TIP` is `f6ea293`
   (the C06-flip commit it measured) while the commit carrying the log is
   `98ad3a0` — correct ordering, but a reader expecting the log to name its own
   commit will see `f6ea293`. Two falsify seats had flagged the earlier absence
   (`W2ClaimsAdmission.md:151`, `W2RerunAllCounters.md:350`).
6. **D3's reading discipline is met by the committed receipt.** The committed
   `measure-after.log` prints `C3_CONTROLS_PASS=2/2` (line 25) and
   `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` (line 26) as **separate lines** — exactly
   what the committed lesson's D3 disposition cell demands ("`HOLDS_OK` alone
   does not prove C3"). The wording drift itself is in a frozen file and is
   unchanged.
7. **D4's forward id note moved twice.** `.ufo/waves/round-63/build/R63SourceZipfileDocs.md:254-255` says
   a future zipfile-docs row would take **S034**; S034 and S035 have since
   landed, so the next unused id is **S036** — and no registry row or
   build/falsify report mentions S036 (`git show 98ad3a0:corpus/SOURCES.md | grep -c "S036"` → 0;
   the only hits under `corpus/` and `.ufo/waves/round-63/` are in this seat's own
   two files, which name it as the next unused id), which is itself the finding.
   The ready-made row text is retained in that report's §7.

## Calibration notes (the judgement axis of this seat)

- No disposition was upgraded on the strength of a report's own assertion.
  Where a build report said a debt was closed, the closure was re-derived from
  bytes (D11's padding wording, D5's receipt pin, D4's screen record).
- Two dispositions are deliberately **narrower** than the source reports':
  - D4 is recorded as *split* — the screen decision is discharged, the id note
    is not — rather than as one blanket "closed".
  - D5 is recorded as *split* — the falsify wave's receipt-pin defect is
    genuinely fixed at the tip, but the transplant corollary it came from is
    not recorded and has no mechanism.
- "Bounded-future" is used only where a **specific action and a named owner**
  both exist. D2's owner is the next round's claims author, D3's is the contract
  author, D1's is the next round's calibration seat, D6's is this round's L1.
  Where no owner exists (D5's mechanism, D7's cross-lane question) the row is
  marked explicitly-unresolved instead of being dressed up as bounded.
- Two of the five named items (D2, D5) turned out to be **absent from the
  committed lesson's routed-debt table** — a routing failure in the build wave's
  own hand-over, not a disagreement with it.

## Touched surfaces

- `.ufo/waves/round-63/falsify/routed-debt.md` (new) — the routed-debt table.
- `.ufo/waves/round-63/falsify/W2RoutedDebt.md` (new) — this report.

Nothing else was written. No product code, judge, contract, counter, manifest,
spec, registry, lesson, entry or ledger file was touched; no git/jj mutation,
no commit, no push, no publish, no deploy; no target was executed; no other
runtime invoked; `~/.omp/agent/config.yml` untouched; no model arguments set.

## Tooling

No tool was installed or upgraded. No `pacman` transaction (the host pacman gate
is paused host-wide — the operator's tooling directive is superseded by that
pause for this lane). No `uv tool install`, no `npx`, no binary download.
Read-only tooling used, all already present: `git` (read-only: `rev-parse`,
`log`, `show`, `ls-tree`, `diff`, `status`), `grep`, `sed`, `awk`, `sha256sum`,
and the already-present Python 3 standard library (`hashlib`/`json` for the
census and pointer checks).

## Cleanup

Scratch `/tmp/revenger-r63-routeddebt/` (two small helper scripts and one
committed-registry snapshot used for the census) is removed after this report
lands.

## Out of scope / not done

- No admission decision, no Q01–Q13 judgement of the entry, no README flip, no
  claim that C1, C2 or C3 passes — those belong to the other falsify seats and
  to L1.
- No verdict on whether the falsify seats' findings survive the tip's later
  commits: this table records which findings were measured on which bytes so
  the adjudicator can do that (D13); it does not re-adjudicate them.
- D2 asserts staleness *by the README legend's own definition*; it does not
  assert that the legend is the contract's wording (it is `corpus/README.md`'s).
- D12 and D13 are this seat's own findings, not build-wave handovers; they are
  labelled as such and kept in separate rows so the build-wave rows stay a
  faithful reconciliation.

## Artifact paths

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/falsify/routed-debt.md`
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-63/falsify/W2RoutedDebt.md`
