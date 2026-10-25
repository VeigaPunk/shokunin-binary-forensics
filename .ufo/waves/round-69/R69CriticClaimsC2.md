DEFECT — C2's frozen predicate is satisfiable without the D1 restatement it claims to measure, its "ability to fail" label is exit-code-only (an empty fixture scores `yes`), its red-before sentence contradicts the receipt it cites, and the instrument bytes it relies on are unpinned.

Seat: L1Revenger69.R69CriticClaimsC2 (leaf critic, no dispatch). Lane `35e1258`, clean worktree (`git status --porcelain` → only `?? .ufo/waves/round-69/assimilation/`). Counter sha256 `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` = the pin at `reports/round-69/claims.md:6` (recomputed: `sha256sum reports/round-69/measure.py`). No tools installed; no files written outside this report and `/tmp/revenger-r69-c2` (deleted).

## The five assigned checks

| # | check | result | evidence |
|---|---|---|---|
| 1 | Q15 criterion row exists and is well-formed | PASS (with caveat V4) | `corpus/QUALITY.md:27` — 4-column row, id `Q15`, criterion, non-vacuous reject clause, lesson `M48 (lessons/round-69.md)`; added by `da02261` (`git show da02261 -- corpus/QUALITY.md` → one `+` row). Reject clause pointer resolves: `awk 'NR==102' reports/round-68/measure-after.log` prints exactly the D1 sentence. Caveat: the cited lesson does not exist yet (`ls corpus/lessons/round-69.md` → ENOENT; `grep -rn M48 corpus/lessons/` → ∅), so the row's provenance is dangling at this commit and no counter label checks it. |
| 2 | Checker self-test passes | PASS | `python3 -B corpus/q15_tree_id_check.py --self-test` → `Q15_SELFTEST=pass (true sentence verified; false sentence killed)`, exit 0. The self-test's "true" hash is real: `git rev-parse 1c34603:corpus` = `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`, matching `q15_tree_id_check.py:66`. |
| 3 | D1 fixture killed (`--scan` exit non-zero) | PASS, honestly earned at this commit | `python3 -B corpus/q15_tree_id_check.py --scan reports/round-69/d1-false-sentence.md` → `Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)`, `scan_d1_exit=1`. Fixture ids re-derived: `git rev-parse 1c34603:corpus`=`ddc6a4f6…`, `git rev-parse dddf147:corpus`=`51894d153a6e69487da2a273680d014abd240f61`, `git rev-parse 14774a2c:corpus`=`51894d15…` — the quoted false pair (`1c34603`↦`51894d15…`) is genuinely false. **But see V2**: the counter cannot distinguish this kill from a stub. |
| 4 | Red-before cannot reach `Q15_PRESENT=yes` without the row | PASS on the label; the claim's red-before *sentence* is false | `git show 222a7a7:corpus/QUALITY.md \| grep -c '^\| Q15'` → `0`; `reports/round-69/measure-before.log:22` → `Q15_PRESENT=no`. **Contradiction**: `claims.md:129-131` states red-before has `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes`; the receipt it cites reads `Q15_SELFTEST=n/a (no checker)` / `Q15_FALSE_KILLED=n/a (no checker)` (`measure-before.log:23-24`), because `git cat-file -e 222a7a7:corpus/q15_tree_id_check.py` → *absent* (checker + D1 fixture first appear at `e1d22ca`: `git show --stat e1d22ca`). See V1. |
| 5 | Restatement verification honest (re-derives via `git rev-parse`) | FAIL | No mechanism ties `Q15_RESTATE_OK` to the D1 sentence. See V3/V5: an unrelated pair, a pair-free line, and a fabricated false-sentence all produce `Q15_RESTATE_OK=yes`. |

## Vacuity / untestable clauses (each reproduced)

All reproductions ran from the lane root with the committed checker (`git rev-parse HEAD:corpus/q15_tree_id_check.py` = `6829573435e707bc6fdad9123d590841501f721c`; `sha256sum corpus/q15_tree_id_check.py` = `7d074f98cb7f9ff2be4c17e6b97e60ac8d660c827a32009d85a35df50639d276`) and `--lane /home/vgpnk/Projects/shokunin/revenger-shokunin` (the same flag the counter passes at `measure.py:164,173`).

**V1 — `claims.md` §C2 red-before is contradicted by its own receipt (calibration, high).**
`claims.md:127-132` describes red-before as `Q15_PRESENT=no`, `Q15_RESTATE_OK=n/a`, `Q15_SELFTEST=pass`, `Q15_FALSE_KILLED=yes`, and reasons that "the checker ships with the claims revision". The receipt is `n/a`/`n/a` (`measure-before.log:23-24`) because the measured base tree is `222a7a7`, one revision *before* `e1d22ca` where the checker first exists. Two of the four red-before values in the frozen text are wrong, with the parenthetical reasoning naming precisely why they are unattainable. This is the Q15/M46-M47 defect class occurring inside the claim that declares Q15. The control itself still sits below target, so C2's *mechanical* pass is unaffected — the honesty sentence is what fails.

**V2 — `Q15_FALSE_KILLED` measures "non-zero exit", not "the D1 pair was contradicted" (evidence, high).**
`measure.py:163-166` sets `q15_false_killed = rc != 0`. `scan()` returns non-zero for three unrelated reasons (`q15_tree_id_check.py:96,101,105`), so any degenerate fixture scores `yes`:
- `: > /tmp/.../empty.md` → `Q15_RESTATE_BAD: no false-sentence pair failed…`, exit 1 → counter would print `Q15_FALSE_KILLED=yes`.
- A false-sentence pair naming a commit that does not exist (`deadbeef:corpus`) with a correct restatement → exit 0, i.e. a *resolution error* (`resolve()` → `None`) is scored identically to a *contradicted identity*.
No void condition pins the fixture: `claims.md:188-192` freezes `corpus/live`/`corpus/fixtures` bytes, and `reports/round-69/d1-false-sentence.md` is a new file outside both; `grep -n sha256 reports/round-69/claims.md` shows a pin only for `measure.py` (line 6). The D1 fixture's bytes are therefore rewritable between red-before and after-measurement with no void trigger.

**V3 — `Q15_RESTATE_OK` passes on a restatement line with zero parseable pairs (evidence, high).**
`scan()` increments `restate_count` for any `tree-identity restatement:` prefix and only fails on pairs it parsed (`q15_tree_id_check.py:91-96`). Reproduced:
```
tree-identity false-sentence: `1c34603:corpus` = `51894d15…`
tree-identity restatement: the `1c34603` corpus tree equals the receipt tree, verified by command.
→ Q15_RESTATE_OK=yes (every restatement pair re-derived; false-sentence pair killed)   exit=0
```
A restatement written in exactly the defect form Q15 rejects (identity asserted, no `git rev-parse` pair) is scored as verified. The same hole swallows a shortened claimed hash, since `PAIR` requires a 40-hex right-hand side (`q15_tree_id_check.py:45`).

**V4 — `Q15_PRESENT` accepts a structurally empty row (presence, medium).**
`measure.py:153` matches only `^\| Q15 \|`. Verified against the counter's own regex: `| Q15 |`, `| Q15 | | | |`, `| Q15 |  |  |  |` all match. The predicate's "the criterion row exists" is therefore not "a well-formed criterion row exists"; the well-formedness half of the assignment has no mechanical guard.

**V5 — `Q15_RESTATE_OK` does not require the D1 sentence to be restated at all (evidence, high).** Two independent counterexamples:
- Unrelated pair: `tree-identity restatement: \`222a7a7:corpus\` = \`2c45edaf…\`` (plus the D1 false-sentence line) → `exit=0`, `Q15_RESTATE_OK=yes`. Nothing anchors the restatement to `1c34603`/`dddf147`.
- Correct restatement *without* a false-sentence line → `Q15_RESTATE_BAD: no false-sentence pair failed`, `exit=1`. So the pass branch silently requires a second, undocumented conjunct (the lesson must embed a deliberately false sentence) while not requiring the D1 restatement. The claim's text (`claims.md:125`) states neither.
- Corollary (already independently reported by `R69D1RestateCheck.md:1`, same conclusion, different seat): a lesson that restates D1 correctly can still read `Q15_RESTATE_OK=no`.

**V6 — the Q15 instrument's identity is unpinned (instrument integrity, medium).**
`measure.py:156-173` executes the checker **from the measured tree**, but nothing freezes that file: no sha256 in `claims.md` (only `measure.py`), none in the wave spec (`grep -rn "q15_tree_id_check" .ufo/waves/round-69/*.py/*.json` → task text only), and `q15_tree_id_check.py` is not covered by any void condition. Replacing it changes all four Q15 labels while leaving the pinned counter byte-identical. Same for the D1 fixture (V2). Digests for post-hoc pinning: checker blob `6829573435e707bc6fdad9123d590841501f721c`, sha256 `7d074f98…d276`; fixture blob `7d0286976f16ed25c9c2bfeb7a33e473d8bf9c4c`, sha256 `637278b2…2466`.

**V7 — the fifth pass-branch conjunct is non-discriminating (calibration, low).**
`claims.md:132` lists "the counter's exit code is 0" in C2's pass branch, but the counter's exit is `sys.exit(2 if not evaluable else 0 if holds_ok else 1)` (`measure.py:557`) over `holds_ok` only; no `q15_*` term appears in it (`grep -n Q15 reports/round-69/measure.py` → lines 151-182 only). The red-before tree already exits 0 (`measure-before.log` tail: `HOLDS_OK_V6=yes`), so the conjunct is satisfied by the do-nothing control and separates nothing. Harmless but should not be presented as claim evidence.

## Clauses that can never fail / can pass vacuously — summary

- "`Q15_RESTATE_OK=yes` (the lesson's restated tree-identity sentence re-derives…)" — passes with a pair-free line (V3), an unrelated pair (V5), and fails a correct-only restatement (V5).
- "`Q15_FALSE_KILLED=yes` (the checker flags the committed D1 false-sentence fixture)" — true of any non-zero exit, incl. an empty file (V2); the fixture's bytes are unpinned (V2/V6).
- "`Q15_PRESENT=yes` (corpus/QUALITY.md carries the Q15 row)" — true of an empty row (V4).
- "The criterion is shown able to fail on the D1 sentence and to pass the restated sentence" — the `--scan` corpus never contains both forms in the fixture set (the D1 fixture carries only the false line; the lesson must carry both), so the "pass the restated sentence" half is only ever demonstrated on the same file that must also carry a false sentence (V5).
- The claim's red-before description (V1) is not testable against the named receipt and is false against it.

## Impacted axes

- calibration: C2 is the calibration claim; V1 is a fresh instance of the class C2 exists to catch, and V2/V3/V5 mean the two evidence labels can read `yes` without the claimed content. A pass read would credit calibration for a mechanism that cannot separate the defect from a stub. **This is the axis to report first.**
- coverage: none — C1's labels (`K_HELD_BACKED`, `C05_SINGLE_V4`, `HOLDS_C2_V4`, `C7_V4_CLEAN`) are unaffected; no Q15 artifact feeds them (`measure.py:36-150` vs `:151-182`).
- discernment: V5's silent second conjunct (the lesson must embed a false sentence) is a predicate the wave's Q15 reviewers were not told about; a reviewer reading `claims.md` alone would grade the lesson wrong in both directions.

## Smallest safe corrections (no claim rewrite, no counter edit)

The counter is sha-pinned and "never edited after this revision" (`claims.md:166-167`), and `claims.md` is frozen, so the fixes are report-level this round plus one round-70 instrument fix:

1. **Erratum, not an edit**: the round-69 lesson/report must carry `erratum: claims.md §C2 red-before reads Q15_SELFTEST=pass / Q15_FALSE_KILLED=yes; the receipt (measure-before.log:23-24) reads n/a (no checker) — the prose is wrong, the control is still below target.` Do not hand-edit the frozen claims.
2. **Make `Q15_FALSE_KILLED` reason-bearing without touching the counter**: the wave's after-run record must quote the scan's stdout line and the failing pair (`1c34603:corpus` claimed `51894d15…` resolved `ddc6a4f6…`), so the receipt is not exit-code-only. Record the fixture digest (`637278b2…2466`) and checker digest (`7d074f98…d276`) in the round report/ledger now, so a later edit is detectable.
3. **Lesson content, stated as a requirement**: `corpus/lessons/round-69.md` must carry (a) a `tree-identity restatement:` line for the D1 pair `1c34603:corpus`=`ddc6a4f6…` **with the pair syntax** (a pair-free line is vacuous, V3), and (b) one `tree-identity false-sentence:` line, and (c) the `M48` label its QUALITY row cites. A Q15 reviewer should check all three by hand, since the predicate does not.
4. **Round-70 (instrument)**: pin `sha256(corpus/q15_tree_id_check.py)` and `sha256(reports/round-<n>/d1-*.md)` in the claims' frozen section; make `scan()` fail a `tree-identity restatement:` line with zero parsed pairs and require ≥1 restatement pair naming a caller-supplied expected commit (`--expect <short>`); make the counter's `Q15_FALSE_KILLED` require the `Q15_FALSE_KILLED: all false-sentence pairs failed` marker **and** a non-`None` resolved value, not `rc != 0`; tighten `Q15_PRESENT` to a row with a non-empty criterion cell (V4). This is a new instrument, not a repair of the frozen one, and must be registered as a routed defect (D6) rather than slipped in.

Scope note: these are claim-shape findings on the build state; nothing here judges C1, and no verdict is offered on the C05 v4 bytes (other seats own that).
