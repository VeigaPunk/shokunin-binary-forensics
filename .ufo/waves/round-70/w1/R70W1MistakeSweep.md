DRAFT-READY — the reference-drift class has exactly one instance in the lane's committed r67–69 text (SCORECARD.md:557 `e1d22caf`, live at the round-70 tip), its hash form is captured by the round-70 SM5 class (shown able to fail) and its command form is captured by **nothing**; one row below is ready to paste into `corpus/lessons/round-70.md` `## Mistakes`.

# R70W1MistakeSweep — revenger round-70 wave 1

Seat: `R70W1MistakeSweep` (scout) · date 2026-10-25 · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`
Frozen inputs read: `reports/round-70/claims.md` (blob `ee0bd50…` at both `dbacce2` and tip `aa1842f`), `reports/round-70/measure.py` (sha256 `488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76`, confirmed by re-hash — see §1), `corpus/lessons/round-69-verifier-spotcheck.md` §6 (V1–V7), `corpus/lessons/round-69.md` `## Mistakes` (M48/M49/M50).
Targets read at tip `aa1842fac199aa524930e5565ed3715de5f84c6d`; base comparisons at `3f5edbc206351232a3d2d801334dd930499ccaf5`.
**No file was edited.** All mutation/tamper work happened on copies under `/tmp/revenger-r70-MistakeSweep*` (deleted on return).

---

## 0. The candidate under test

The seat brief names V1/V2/V4 from `corpus/lessons/round-69-verifier-spotcheck.md` §6:

| spot-check id | defect | class | round-70 status |
|---|---|---|---|
| V1 | uncommitted lane-authored leftover at closure | `landing` | partly repaired; **the r69 tip itself carries a truncated seat report** (§4) |
| V2 | non-resolving cited hash (`e1d22caf`) | `reference-drift` / `attribution` | **still live at the round-70 tip** (§2) |
| V4 | printed counting command does not run from the printed cwd | `reference-drift` / `attribution` | **still live; captured by no lane tool** (§3) |

I swept the lane's committed round-67..69 `reports/`, `SCORECARD.md` and `corpus/lessons/round-6*.md` for **every** instance of the class, then attributed each instance.

---

## 1. Frozen-input integrity (so the sweep below is anchored)

```console
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse HEAD
aa1842fac199aa524930e5565ed3715de5f84c6d
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin log --oneline -3
aa1842f round-70: build — C05 v5 candidate (admission-status: candidate, README unflipped) …
dbacce2 round-70: pre-registration — claims … frozen counter, eight control receipts, red-before …
3f5edbc round-69 verifier spot-check (integrator, hyaku): non-author admit/reject

$ sha256sum /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-70/measure.py
488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76  .../reports/round-70/measure.py
$ git rev-parse dbacce2:reports/round-70/claims.md aa1842fac199aa524930e5565ed3715de5f84c6d:reports/round-70/claims.md
ee0bd5082c0a5dc4826a3e8c1b43f6243168c86f
ee0bd5082c0a5dc4826a3e8c1b43f6243168c86f        # claims.md is byte-identical pre-registration → tip
```

Counter runs from **any** cwd (the r70 counter docstring says "Run it by absolute path with any cwd"):

```console
$ cd / && TMPDIR=/tmp python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-70/measure.py <tip-tree>
K_HELD_BACKED=8/14 score=5.7
C05_STATUS=uncovered
C05_SINGLE_V5=no
V5_ENTRY_PRESENT=yes
V5_ADMITTED_MARKED=no
C1_GATE=checked_blocks=22 problems=0 exit=0 ok=yes
C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
HOLDS_C1_V5=no
SM1=1 … SM5=1 … SELF_MISMATCH=12 exit=1
HOLDS_C2_V5=no
EMB_R68=checked_blocks=17 problems=0 exit=0 … HOLDS_C3_V1=yes
HOLD_REPLAY=10/10   GATE_SELFTEST=exit 0
EXIT=1
```

---

## 2. SWEEP B — every commit citation in the lane's committed r67–69 text, resolved in BOTH repos

Command (scratch `/tmp/revenger-r70-MistakeSweep-commitcites2.py`): for every file under `reports/round-{67,68,69}/`, `corpus/lessons/round-{67,68,69}*.md`, `SCORECARD.md` **at base `3f5edbc`**, extract every token matching
`(?i:pre-registration|\bbase\b|\btip\b|\bcommit\b|\bancestor\b|unchanged since)\s*[`(]*`?([0-9a-f]{7,40})`` and test `git cat-file -e <h>^{commit}` in the lane repo **and** in the fleet repo.

```console
$ python3 /tmp/revenger-r70-MistakeSweep-commitcites2.py
=== SWEEP B (final): every COMMIT-CITATION token, resolved in BOTH repos ===
  [RESOLVES-NOWHERE] SCORECARD.md:557  e1d22caf
      Pre-registration `e1d22caf` (claims + frozen counter `reports/round-69/measure.py` sha256
```

**One instance in the whole committed r67–69 lane corpus.** It is *live at the round-70 tip* (the tip's SCORECARD.md is byte-identical on that line):

```console
$ git grep -n 'e1d22caf' aa1842fac199aa524930e5565ed3715de5f84c6d -- reports/ corpus/ SCORECARD.md
aa1842f:SCORECARD.md:557:Pre-registration `e1d22caf` (claims + frozen counter `reports/round-69/measure.py` sha256
aa1842f:corpus/lessons/round-69-verifier-spotcheck.md:133:  `e1d22caf`; `git rev-parse e1d22caf` fails …
aa1842f:reports/round-70/claims.md:79:`e1d22caf`, which does not resolve; SM6=0) —

$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse --verify e1d22caf
fatal: Needed a single revision
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse e1d22caa
e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968      # the real pre-registration commit
```

The other two mentions (`round-69-verifier-spotcheck.md:133` and `round-70/claims.md:79`) are *deliberate quotations of the defect* — they name the bad token to describe it, not to locate a commit. **Only `SCORECARD.md:557` is a false locator.**

### Who catches it

- `corpus/QUALITY.md` — **no criterion**. Q15 (`QUALITY.md:27`) covers "a stated git object id or tree identity", and its mechanical form `corpus/q15_tree_id_check.py` scans only `` `tree-identity …:` ``-prefixed `` `<hex>:corpus` = `<40hex>` `` pairs in a *lesson* file. `SCORECARD.md:557` is neither.
- `corpus/self_assessment_check.py` (round-70 C2, new this round) — **yes, for the hash form**: `sm5()` reads `SCORECARD.md` from `## Round 61` on and counts a backticked 7–40-hex token introduced by `pre-registration|base|tip|commit` that does not resolve under `git cat-file -e <h>^{commit}`.

Proof that SM5 fires **on exactly this line** (scratch copy of the tip tree; the lane file was not touched):

```console
$ python3 -B <tip-tree>/corpus/self_assessment_check.py --root <tip-tree> --lane <lane>
SM1=1 SM2=7 SM3=2 SM4=1 SM5=1 SM6=0
SELF_MISMATCH=12        exit=1
# scratch: replace the token at SCORECARD.md:557 with the resolving e1d22caa
$ python3 -B <tip-tree>/corpus/self_assessment_check.py --root <scratch-tree> --lane <lane>
SM1=1 SM2=7 SM3=2 SM4=1 SM5=0 SM6=0
SELF_MISMATCH=11        exit=1     # SM5 1 → 0; the drop is attributable to that one line
# scratch: keep the bad token and append the erratum form the checker honours
$ …                                    # → SM5=0, SELF_MISMATCH=11
```

And the checker's own self-test exercises the class (so the fix is not merely a label):

```console
$ python3 -B <tip-tree>/corpus/self_assessment_check.py --self-test
SELFTEST OK: clean 0; six planted defects each scored exactly their class; erratum excuses only a resolving correction
exit=0
```

---

## 3. SWEEP A — every printed command naming a lane-relative path: does it run from the cwd the document prints?

Command (scratch): join `\` continuation lines, track the nearest preceding `cd X`, and resolve each `reports/…|corpus/…|.ufo/…` path under that cwd.

```console
$ python3 /tmp/revenger-r70-MistakeSweep-locator_lint3.py /home/vgpnk/Projects/shokunin/.ufo/reports/round-67/revenger.md <lane>
LOCATOR_LINT_FAIL=0        exit=0
$ python3 /tmp/revenger-r70-MistakeSweep-locator_lint3.py /home/vgpnk/Projects/shokunin/.ufo/reports/round-68/revenger.md <lane>
LOCATOR_LINT_FAIL=0        exit=0
$ python3 /tmp/revenger-r70-MistakeSweep-locator_lint3.py /home/vgpnk/Projects/shokunin/.ufo/reports/round-69/revenger.md <lane>
UNRESOLVED /home/vgpnk/Projects/shokunin/.ufo/reports/round-69/revenger.md:77  cwd=/  path=reports/round-69/measure.py
    cd / && TMPDIR=/tmp/revenger-r69-reg-tmp python3 -B   reports/round-69/measure.py "$T"
LOCATOR_LINT_FAIL=1        exit=1
$ python3 /tmp/revenger-r70-MistakeSweep-locator_lint3.py <lane-SCORECARD-at-tip> <lane>
LOCATOR_LINT_FAIL=0        exit=0
$ python3 /tmp/revenger-r70-MistakeSweep-locator_lint3.py <lane-reports/round-69/claims.md-at-base> <lane>
LOCATOR_LINT_FAIL=0        exit=0
```

**Running the r69 printed command verbatim reproduces the failure** (this is V4, still unfixed at fleet HEAD):

```console
$ T=$(mktemp -d /tmp/rev-r69-reg-XXXX); git -C revenger-shokunin archive 579bb6e… corpus | tar -x -C "$T"
$ cd / && TMPDIR=/tmp/revenger-r69-reg-tmp python3 -B \
    reports/round-69/measure.py "$T"
python3: can't open file '//reports/round-69/measure.py': [Errno 2] No such file or directory
exit=2
```

The r67 and r68 fleet reports print the **absolute** path after `cd /` and therefore run — the defect is a round-69 regression, not a lane-wide convention.

### Who catches it

- `corpus/QUALITY.md` — **no criterion**. Grep for `cwd|working directory|resolve` returns only Q15's *tree-identity* resolve rule; nothing states that a printed command must execute from the cwd the document prints.
- `corpus/self_assessment_check.py` — **no**. `sm5()` reads `SCORECARD.md` only, and only commit tokens; `grep -n claims` over the checker, `corpus/entry_checks.py` and `corpus/lint_entry.py` returns **0** for every one of them — **no lane tool opens `reports/round-*/claims.md` at all**:
  ```console
  $ for f in corpus/self_assessment_check.py corpus/entry_checks.py corpus/lint_entry.py; do
      printf '%s: ' "$f"; git show aa1842f:$f | grep -c 'claims.md'; done
  corpus/self_assessment_check.py: 0
  corpus/entry_checks.py: 0
  corpus/lint_entry.py: 0
  ```
- The r69 counter's own `measure.py` — **no**; it never prints or validates an invocation contract.
- `captured-by: none` for the command form. The r69 spot-check **V4** named it in prose (`round-69-verifier-spotcheck.md:140`) and `corpus/lessons/round-69.md` `## Routed forward` **does not carry it** (`grep -i 'absolute|cwd|restate the command'` over the routed-forward block → no hit), so nothing in the lane's written rules owns it.

### Additional located fact (same class, new round)

`reports/round-70/claims.md` (frozen, blob `ee0bd50…`) has **no `## Frozen counter` section** — the first pre-registration in r67–r70 to omit it:

```console
$ for c in 67 68 69 70; do printf 'round-%s: ' $c; git show aa1842f:reports/round-$c/claims.md | grep -c '^## Frozen counter'; done
round-67: 1
round-68: 1
round-69: 1
round-70: 0
```

Its only printed counter command is the cwd-less relative `sha256sum reports/round-70/measure.py` (`claims.md:7`), which resolves from the lane root only:

```console
$ cd /home/vgpnk/Projects/shokunin && sha256sum reports/round-70/measure.py
sha256sum: reports/round-70/measure.py: No such file or directory (os error 2)   exit=1
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && sha256sum reports/round-70/measure.py
488f95aa1d502cbb20b7303e1d773f0101397a0bd45cee69c9fb389651c88c76  reports/round-70/measure.py
```

The *instrument* is immune (absolute-path docstring, verified running from `/` in §1), so this is a **publication** defect, not an operability one — but it is the same class and it is in the round's own frozen text.

---

## 4. SWEEP C — the `landing` class: what actually landed at the r69 tip

The r69 spot-check V1 named an uncommitted leftover. The r70 pre-registration commit message says it "resolves the inherited r69 R69CounterReplay leftover". The bytes show the sweep went further than "uncommitted": **the r69 tip commit carried a truncated draft.**

```console
$ git -C <lane> log --format='%h %ad %cd %s' --date=iso -1 db956ec
db956ec 2026-10-25 07:25:52 -0300 2026-10-25 07:26:29 -0300 round-69: wave evidence — final bytes of the remaining late seat reports
$ git -C <lane> rev-parse db956ec:.ufo/waves/round-69/R69CounterReplay.md dbacce2:.ufo/waves/round-69/R69CounterReplay.md
65a53cc5061e8b81c5010541a5b20cb748c2830d
9af7d9fca49124128f7fcb6c1b5c988ffb6dfb34
$ git -C <lane> show db956ec:.ufo/waves/round-69/R69CounterReplay.md | wc -c
36956
$ git -C <lane> show dbacce2:.ufo/waves/round-69/R69CounterReplay.md | wc -c
37510
```

Line 464 is the only differing line, and the r69-tip version **ends mid-sentence**:

```console
$ diff <r69-tip blob> <r70-pre-registration blob> | head -4
464c464
< … (an entry quoting a single line of the derivation stdout → `checked_blocks=1 problems=0` rc=0), confirming no reverse check exists. Caveat on the superset form:
---
> … — `.ufo/waves/round-69/R69ReviewC7Gate.md:460-466`, "The one-way direction is **measured, not assumed**": an entry quoting a single line of the 20-line derivati…
```

So `db956ec` — whose subject is *"final bytes of the remaining late seat reports"* — did **not** contain the final bytes of `R69CounterReplay.md`; a *later* round's commit (`dbacce2`, the round-70 pre-registration) landed the complete text. That is the V1 pattern recurring one level up: the seat file was swept by a sibling commit, exactly what the spot-check forbade ("do not leave it for a sibling commit to sweep").

`captured-by: none`. No criterion or tool in the lane checks that a seat report's committed blob equals the bytes the seat wrote, or that a commit whose subject says "final bytes" actually contains them. The round-70 pre-registration repaired it *by hand*, in the middle of the next round's frozen pre-registration.

**Current landing state at the round-70 tip** (no tracked leftovers; the untracked files are the in-flight round-70 wave build, not a defect yet). *Re-measured at 18:16 while the L1's C2 repair was in flight — see the concurrency note below:*

```console
$ git -C <lane> status --porcelain -uall
?? .ufo/waves/round-70/assimilation/collisions
?? .ufo/waves/round-70/assimilation/guard-collisions
?? .ufo/waves/round-70/assimilation/guard-reg-ids
?? .ufo/waves/round-70/assimilation/quarantine-slice
?? .ufo/waves/round-70/assimilation/reg-ids
?? .ufo/waves/round-70/assimilation/staged-ids
?? .ufo/waves/round-70/build-w1-spec.py
?? .ufo/waves/round-70/w1-dispatch.json
?? .ufo/waves/round-70/w1-plan-validated.json
?? .ufo/waves/round-70/w1-plan.err
?? .ufo/waves/round-70/w1-run.err
?? .ufo/waves/round-70/w1-spec.json
?? .ufo/waves/round-70/w1.ready
?? .ufo/waves/round-70/w1.ready.dispatched
?? .ufo/waves/round-70/w1/swarm-registry.json
$ git -C <lane> status --porcelain | grep -c '^ M'
0
```

---

## 5. THE MINE ROW (ready to paste into `corpus/lessons/round-70.md` `## Mistakes`)

Format follows `corpus/lessons/round-69.md` `## Mistakes` (id | class | evidence pointer | captured-by | fix).

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M51 | `reference-drift` / `attribution` — a **published locator that does not resolve**: a cited commit token that names no object, and a printed command that does not execute from the cwd the document prints | (a) `SCORECARD.md:557` — "Pre-registration \`e1d22caf\`"; `git rev-parse --verify e1d22caf` → `fatal: Needed a single revision`; the real commit is `e1d22caa`; the line is **byte-identical at base `3f5edbc` and at tip `aa1842f`** (live defect). (b) `.ufo/reports/round-69/revenger.md:77-78` — "cd / && … python3 -B reports/round-69/measure.py \"$T\"" run verbatim → `python3: can't open file '//reports/round-69/measure.py'`, **exit 2**; the r67/r68 fleet reports print the absolute path and run. (c) `reports/round-70/claims.md:7` prints the cwd-less relative `sha256sum reports/round-70/measure.py` (fails from the fleet root) and the file has **no `## Frozen counter` section** (r67/r68/r69 each have one). | (a) the round-70 C2 class **SM5** of `corpus/self_assessment_check.py` (`sm5()`, `SCORECARD.md` from `## Round 61` on) — the only mechanical capture; shown able to fail: SM5=1 on the tip tree, SM5=0 after correcting that one line in a scratch copy, `--self-test` exits 0 with a planted defect scoring exactly SM5. (b) and (c) **none** — no `QUALITY.md` criterion states that a printed command must run from the printed cwd (`grep -i 'cwd\|working directory'` → only Q15's tree-identity rule); `corpus/entry_checks.py`, `corpus/lint_entry.py` and `corpus/self_assessment_check.py` each contain **0** occurrences of `claims.md`, so no lane tool opens the pre-registration; the r69 spot-check named V4 in prose but `corpus/lessons/round-69.md` `## Routed forward` does not carry it. | (a) **shipped and killable**: re-state the citation as `e1d22caa` (or append the checker's honoured `erratum: \`e1d22caf\` -> \`e1d22caa\`` line) — demonstrated: SELF_MISMATCH 12→11, SM5 1→0. (b)+(c) **routed, not repaired here**: a cwd-aware locator lint that resolves every printed relative path against the cwd the document itself prints (scratch prototype at `/tmp/revenger-r70-MistakeSweep-locator_lint3.py`, deleted on return) — shown able to fail: `LOCATOR_LINT_FAIL=1 exit=1` on the r69 fleet report line 77 and `LOCATOR_LINT_FAIL=0 exit=0` on the r67/r68 reports and on the lane's own `SCORECARD.md`/`claims.md`; not landed in the lane, and no claim this round covers it. |

### Notes for the L1 (not part of the row)

- The row's fix column names one fix that is **shown able to fail** (SM5) and one that is **routed only** (the locator lint). The prompt's rule — "a fix counts only once shown able to fail" — is met for the SM5 half and is explicitly *not* claimed for the lint half; the lint prototype lives in `/tmp` and is deleted, so it must be re-derived by whoever lands it.
- The r70 pre-registration **already counts (a) as SM5=1** in its "Before" receipt (`claims.md:79`, `reports/round-70/before-treated-tools-on-base.log`), so the row documents a defect the round is already driving to 0 rather than a new one. I re-derived that receipt independently: running the tip's checker against a base tree gives `SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0 SELF_MISMATCH=9 exit=1` — identical to the committed receipt, and identical to `claims.md:73-79`'s prose.
- A separate, second defect is **not** in the row above because it is a different class: the `landing` sweep (§4). If the L1 wants a second row, it is: `M52 | landing | SCORECARD-independent: db956ec's subject "final bytes of the remaining late seat reports" is false for `.ufo/waves/round-69/R69CounterReplay.md`, whose committed blob at the r69 tip is 36956 B and ends mid-sentence at :464 ("Caveat on the superset form:"), while the complete 37510 B blob landed only at dbacce2 (the round-70 pre-registration) | captured-by: none — no criterion or tool compares a committed seat blob with the bytes the seat wrote | fix: routed; a landing check that every `.ufo/waves/round-NN/*.md` blob at the round tip equals the worktree copy would be shown able to fail by the same blob pair 65a53cc / 9af7d9f`.
- **Not a finding** (checked and cleared, recorded so wave 2 does not re-raise it): the round-70 candidate entry states **no** git object id — `grep -c 'c7b7cf98' <v5 entry>` → **0**, and its §Q-map Q15 row reads "this entry states no git object id" — so `claims.md:35`'s phrasing "the \`c7b7cf98\` identity derived" describes an *intent* the entry satisfies by **dropping** the identity rather than by deriving it. That phrasing is loose, but it is not a false locator in the entry itself, and `c7b7cf98` **does** resolve in the lane (`git rev-parse c7b7cf98` → `c7b7cf98ddeecbd5464e47396f224e6384b78905`). Flagged for wave-2 Q15 review as wording, not as a located defect.
- The other 16 unresolved 7–12-hex tokens in the r67–69 text are **file sha256 prefixes** (`0de4eb6f…`, `7933c060…`, `a12fb8e2…`, `bfd92057…`, `c0428612…`, `74d4c0d9…`, `56b88bc4…`, `bce497d6…`, `5afe1810…`, `05d2280f…`, `507d79f8…`, `9345cb8c…`, `9bf21e50…`, `a2fd347e…`, `a59914e9…`, `b2660e60…`) or **payload hex** (`504b0506`, `573742d`), not commit citations. I re-hashed the ones naming files: `reports/round-67/measure.py` → `7933c060…` ✓, `reports/round-68/measure.py` → `0de4eb6f…` ✓, `reports/round-69/measure.py` → `bca74e6d…` ✓, `reports/round-70/measure.py` → `488f95aa…` ✓, `corpus/derive_axml_anchors.py` → `74d4c0d9…` ✓, `corpus/derive_axml_anchors_r68.py` → `bce497d6…` ✓, `corpus/snapshots/ResourceTypes.h` → `56b88bc4…` ✓, `.ufo/waves/round-67/source-snapshots/dex-format.html` → `c0428612…` ✓. `SKILL.md` is cited twice (`bfd92057…` for the r64 bytes, `a12fb8e2…` for the current 51809 B) — at base the live bytes hash to `a12fb8e2507d…`/51809 B, so the `bfd92057…` citation is a correctly-scoped *historical* reference (the r64 bytes), not drift. **No digest in the r67–69 text is wrong.**

---

## 6. Concurrency note (read before acting on §4's landing state)

The `git status --porcelain | grep -c '^ M'` count in §4 was **0 at 18:16 when the sweep ran**. It is **4 now**, and the four are the L1's in-flight C2 repair (mtimes 18:07–18:08, i.e. *before* my report was written at 18:16 — so my §4 reading was already stale by the time I filed):

```console
$ git -C <lane> status --porcelain | grep '^ M'
 M SHONEN.md
 M SKILL.md
 M corpus/README.md
 M corpus/self_assessment_check.py
$ for f in SHONEN.md SKILL.md corpus/README.md corpus/self_assessment_check.py; do stat -c '%y  %n' $f; done
2026-10-25 18:07:54  SHONEN.md
2026-10-25 18:08:34  SKILL.md
2026-10-25 18:08:37  corpus/README.md
2026-10-25 18:08:12  corpus/self_assessment_check.py
```

**These are the L1's edits, not mine** — I created exactly one file in the lane (`.ufo/waves/round-70/w1/R70W1MistakeSweep.md`, untracked) and edited nothing else.

One of them touches the instrument my mined row names as the fix, so I re-ran the row's kill leg against the **live** working-tree checker (the L1's only change to it is `sm3`'s size regex: `r"(\d[\d,]*) bytes"` → `r"(?<![\w-])(\d[\d,]*) bytes"` — `sm5` is untouched):

```console
$ python3 -B <tip-tree>/corpus/self_assessment_check.py --root <tip-tree> --lane <lane>   # live checker
SM5=1
SELF_MISMATCH=12
$ python3 -B <live>/corpus/self_assessment_check.py --self-test
SELFTEST OK: clean 0; six planted defects each scored exactly their class; erratum excuses only a resolving correction
exit=0
# scratch copy of the tip tree with SCORECARD.md:557 corrected to e1d22caa
$ python3 -B <live>/corpus/self_assessment_check.py --root <scratch-tree> --lane <lane>
SM5=0
SELF_MISMATCH=11
```

**The mined row's fix (M51 column 5) still holds against the live checker**: SM5=1 on the tip tree, SM5=0 after correcting that one line in a scratch copy, self-test exit 0. The `landing` sweep in §4 stands on committed history (`db956ec` vs `dbacce2` blobs) and is unaffected by the working tree.

## 7. Unresolved / out of scope

- The r69 spot-check's V5/V6/V7 (counter regression, derivation reformat, SHONEN box 1) are other classes; not swept here.
- The fleet repo's `SCORECARD.md` (73649 B) is a **different file** from the lane's (71077 B, sha256 `5f92e084…`) and carries **0** revenger `e1d22c` hits — the locator defect is lane-local.
- I did not check whether the r69 fleet report's line 77 is *also* present in any other fleet round's report beyond r67/r68 (all three were run; only r69 fails).
- No tool was installed (Python stdlib + `git` only); no pacman/uv/npm transaction was made.

Tooling record: no installs; no version/channel notes required.
