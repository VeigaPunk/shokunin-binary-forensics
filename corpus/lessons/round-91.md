# Round-91 lesson — the self-assessment gate reads where the lane states its numbers; the lane can now measure message↔tree conformance

Base `f6356ffb8b665bddc5ee2cfac81443c1300b59bf`; freeze
`b13aac756ac33aa5245c13966c624de4370206d0` (claims, the 21-case battery, 11 rule
mutants, both counters, three red-before logs); wave evidence
`d509e982844d31bd26f3cb96e1a663e7d36f2ca8`; landing = the commit that carries this
file. Two claims, frozen in `reports/round-91/claims.md`: C1 calibration (SM6 v3
reads the stated cell; `SM6_MISCLASS` v2 5/22 → target 0/22, 11/11 rule mutants
killed) and C2 operability (commit-message↔tree capability; target
`CAP_MESSAGE_TREE=pass`). This lesson is the lane's own evidence, not outside
admission; a seat this lane dispatched is still the lane.

## Gate

### Fixed inputs and controls (committed at the freeze, before any build seat ran)

- C1 reds: v2 `corpus/self_assessment_check2.py` scores `SM6_MISCLASS=5/22`
  (`reports/round-91/c1-red-v2.log`, all five in the lane's own row format:
  R03, R04, R05, R06, R08); v1 `11/22` (`c1-red-v1.log`). Both reds use the same
  frozen counter, so the target is unreachable by doing nothing.
- C2 red: the instrument is absent (`CAP_PRESENT=0`, `CAP_MESSAGE_TREE=fail`,
  `reports/round-91/c2-red-absent.log`).
- C1 battery labels: 21 cases labelled by hand from the frozen rule before any
  implementation existed; an independent seat re-derived **21/21** as forced and
  found `reference` 0/21 and all 11 frozen mutants killed
  (`.ufo/waves/round-91/w1/ExecR91BatteryX.md`).
- C2 planted-miss control: the frozen probe builds its own three-commit fixture
  and requires the instrument to exit 0 on the clean range and exit 1 naming
  `missing/r91.txt` on the dirty one; a stub that prints a pass line fails it
  (`cap_probe.py` leg 3).
- Held-out check (not part of the claim): 22 fresh real-format cases, labels
  hand-derived and scored against the frozen `reference` before v3 was scored —
  v3 0/22, v2 5/22 (`.ufo/waves/round-91/w1/ReviewerR91C1.md`).

### Source openings (CORPUS rule 1; access date 2026-11-04; quotes re-checked against the fetched bytes in `.ufo/waves/round-91/l1/sources/`)

| id | URL | located quote (≤25 words) | disposition |
|---|---|---|---|
| S488 | https://git-scm.com/docs/git-log | pretty formats table: "`%B` raw body (unwrapped subject and body)" | admit, docs tier A — grounds reading the whole message with one specifier |
| S489 | https://git-scm.com/docs/git-cat-file | DESCRIPTION: "-e Exit with zero status if `<object>` exists and is a valid object." | admit, docs tier A — grounds the per-commit path existence test |
| S490 | https://www.conventionalcommits.org/en/v1.0.0/ | Specification: "A description MUST immediately follow the colon and space after the type/scope prefix." | admit, docs tier A — grounds reading subject *and* body, not the subject only |

Fetch receipts: `.ufo/waves/round-91/l1/sources/{git-log,git-cat-file,conventional-commits}.txt`
(HTML fetched with `curl` on 2026-11-04 and reduced to text with an inline
strip-tags pass; the text is the committed receipt and every quoted sentence is
located in it); each quote was located in the fetched text before the row was
written. No existing row
changed status, recheck or used-by this round. New rows S488–S490 enter `mined`,
`opened 2026-11-04`, `recheck 2027-02-02`, `used-by corpus/lessons/round-91.md`.

### Assimilation and considerthese

**Assimilation: none.** The `merge/revenger/` package's 155 staged ids collide
155/155 with this lane's registry (`comm -12` = 155; `.ufo/waves/round-91/assimilation/collisions`) —
mass id drift, which a read-only check cannot fix; nothing was adopted and an L0
question was appended (`revenger | round-91`). The collision guard was proved
able to fail on a scratch registry with an indented row (`assimilation/guard/guard-proof.log`:
`indented_row_detected=1`).

`considerthese/2026-11-04.md` proposal 4 (message-versus-tree check on window
commits) is C2's ground, opened through this lane's own bar: the instrument was
built, its self-test plants a miss, and its first real run measured the lane's
own history rather than restating the reflection. Proposals 1, 2, 3 and 5 stay
unimplemented.

## Mistakes

| class | evidence pointer | captured-by | fix (shown able to fail?) |
|---|---|---|---|
| **message/tree citation drift, committed by this round's own author** — the wave-evidence commit `d509e98` cites `ufo-wave-policy.json`, a fleet-root script that is not in the lane tree | `.ufo/waves/round-91/w1/ExecR91RealRun/real-run-table.md` row 1 (`git cat-file -e d509e98:ufo-wave-policy.json` → fatal; `git log --all -- '*ufo-wave-policy.json'` empty) | the C2 instrument built in the same round — its real run reported it as the range's only genuine mismatch (`MESSAGE_TREE commits=23 cited=25 misses=9`) | rule: cite a fleet-root script by its absolute path in prose, never as a bare lane-relative token; the instrument is now the standing check. **Able to fail: yes** — it failed on the author within the hour |
| **freeze inconsistency** — C2's description said "backticked" paths while probe leg 4 required `cited >= 20`; the range has 0 backticks and 8 `.log` tokens, so a strictly backticked reading cannot reach the threshold and the landed instrument reads path-shaped tokens backticked or bare | `.ufo/waves/round-91/w1/ReviewerR91C2.md` H1; erratum appended to `reports/round-91/claims.md` | none pre-freeze: no control scored "would a spec-faithful reading pass?" — the planted-miss fixture used backticked tokens, where both readings coincide | erratum names the defect; predicate, legs, kill rule and range unchanged. **Able to fail: no instrument yet** — routed to r92: a leg that runs the instrument over a range with zero backticks and asserts the cited count against both readings |
| **battery rule version 1 mislabelled R02** — reading the last `N/D` in the stated cell took `C15_HELD_BACKED 0/1 → 0/1` instead of the token-adjacent pair | `reports/round-91/sm6_battery_v3.py` R02; the sanity run before the freeze printed the label mismatch | the L1's own pre-freeze sanity run over `mutants.reference` | rule step 4 changed to "token-adjacent first, last-in-region fallback" **before** the freeze; battery then scored `reference` 0/21 and v2 5/22. **Able to fail: yes** — the corrected rule is what the mutants are built against, and M12/M13/M14 die on it |
| **frozen counter admits a skip-work control (C1)** — the 21-case battery is enumerable, so a lookup table keyed on the case text passes without reading the stated cell | `CriticR91Claims/receipts/impl_fit_hardcoded.py`, `c1-fit-hardcoded.log` (same four verdict lines as the real v3) | none pre-freeze: the round's own `claims.md` kill rule said "a control that meets the target means the battery is wrong", but the control was not built before data | post-freeze successor `reports/round-91/c1_counter2.py` adds 40 run-time-generated cases: landed v3 `RANDOM_MISCLASS=0/40`, the fitted control 18/40. **Able to fail: yes** — red on the control, green on the implementation |
| **frozen probe admits three stubs (C2)** — the planted path is the guessable literal `missing/r91.txt`, and the real leg ignores the exit code and the miss count | `CriticR91Claims/receipts/stubD.py`, `stubE.py`; `probe-stubD`/`probe-stubE` receipts | none pre-freeze; the same §9 rule was available and not applied to the probe itself | successor `reports/round-91/cap_probe2.py` (random absent path, worktree-vs-tree leg, `commits` and exit cross-checks): stubA/stubD/stubE all `CAP2_VERDICT=fail`, landed instrument pass. **Able to fail: yes** |
| **two scribe seats died producing nothing** (`ScribeR91Sources`, `ScribeR91Skill`: empty final output, no wave files) | `agent://ScribeR91Sources`, `agent://ScribeR91Skill` transcripts; no `.ufo/waves/round-91/w1/ScribeR91*` directories exist | no criterion; seat death is reported, not replaced | the L1 did the source openings and the lesson itself, with the fetch receipts committed under `.ufo/waves/round-91/l1/sources/`. Recorded, not hidden |

## Outside verification

No `[x]` and no non-author credit is asserted. The closure should sample: the
S488–S490 admits against the fetched bytes, the C1 battery's R03/R04/R05/R06/R08
labels, the C2 description defect (ReviewerR91C2 H1) and the erratum's claim that
predicate/legs/range are unchanged, and should re-derive both frozen counters
over the landing tree.

## Final measurements (adjudication; landing = the commit carrying this file)

| counter | base / control | landing | frozen target | verdict |
|---|---|---|---|---|
| `SM6_MISCLASS` (v2 → v3) | 5/22 (v2, red) · 11/22 (v1) | **0/22** (v3) | 0/22 | **MET on the frozen counter; contested** — a 21-entry lookup table also passes it (C1-1) |
| `MUTANTS_KILLED` (11 frozen rule mutants) | 11/11 with the reference rule | **11/11** | 11/11 | MET |
| `REAL_SELF_MISMATCH` | 1 (new file not yet in the README index) | **0** | 0 | MET (the 1 was the round's own integration gap, fixed in the landing) |
| `CAP_MESSAGE_TREE` | fail (instrument absent) | **pass** | pass | **NOT VERIFIED** — `stubD`/`stubE` also pass (C2-2/C2-3); the successor `cap_probe2.py` kills them and passes the landed instrument (unclaimed) |
| held-out 22 cases (unclaimed) | v2 5/22 | v3 **0/22** | — | corroboration, not the frozen rule |
| attributed impl mutants (unclaimed) | — | 11 killed / **6 survived** of 17 | — | disclosed limit; eight rule elements have no discriminating case |

Receipts: `reports/round-91/c1-after.log`, `reports/round-91/c2-after.log`,
`reports/round-91/holds.log`; wave evidence under
`.ufo/waves/round-91/w1/`.
