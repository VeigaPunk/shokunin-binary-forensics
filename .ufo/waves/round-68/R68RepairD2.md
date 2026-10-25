# R68RepairD2 — routed defect D2: gate vs probe classification audit

**RECONCILE-AS-SPECIFIED** — but the reconciliation is larger than the routed item says: the
authoritative registry row itself is split (`kind | gate` at `SKILL.md:265` vs "this probe" at
`SKILL.md:273`), the SKILL scope section still denies any registry exists (`SKILL.md:31`), and the
row's own self-test field still asserts the round-67 shadowing that the landed gate no longer has
(`SKILL.md:268`). Direction (registry wins, prose follows) is right; the lesson's premise that the
row "satisfies §Gate standard" is false on two checkable fields (verdict map omits `64`; the pinned
digest is not verified by the gate).

Lane: revenger · repo `/home/vgpnk/Projects/shokunin/revenger-shokunin` · read-only audit, no
production file touched; all mutation tests ran on `/tmp/d2-scratch/` copies.
**Tool installs: none** (python3 only).

## 1 · Which classification each source carries

| source | kind it carries | pointer | quoted text |
|---|---|---|---|
| authoritative registry row | **gate** | `SKILL.md:265` | `\| kind \| gate (committed, re-runnable verdict script this lane owns) \|` |
| same registry row, family note | **probe** | `SKILL.md:273` | `… the ten-verifier census and HOLD_REPLAY=10/10 denominator are frozen and this probe does not join them (claims.md §C2)` |
| gate's own docstring | **gate** | `corpus/check_embedded_outputs.py:6` | `Registered gate (SKILL.md `## Gate registry`, kind `gate`): a committed,` |
| SKILL scope limit | **no gate registry at all** | `SKILL.md:31` | `- **No gate registry.** No verifier here is a registered gate; a green `--self-test` is` |
| r67 frozen pre-registration | **probe** | `reports/round-67/claims.md:102` | `- Registry: the gate registers in `SKILL.md` (this lane's registry home) as a **probe** with` |
| r67 report prose | **probe** | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-67/revenger.md:14` | `New registered probe `corpus/check_embedded_outputs.py` outside the frozen ten-verifier replay family` |
| r67 report prose | **probe** | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-67/revenger.md:20` | `` `SKILL.md` `## Gate registry` row (probe; verdict map 0/1/2; …) `` |
| r67 report trend prose | **probe** | `/home/vgpnk/Projects/shokunin/.ufo/reports/round-67/revenger.md:63` | `the C7 probe landed but its registered attribution claim proved false` |
| r67 lesson carrier item | **probe** | `corpus/lessons/round-67.md:145` | `verbatim-output-diff gate now EXISTS as the C7 probe (its attribution defect is item 2)` |
| r68 pre-registration | **gate** (no probe usage) | `reports/round-68/claims.md:39`, `:199` | `## C1 — calibration: the C7 attribution repair …` / `The round-67 routed defects D1–D4 (abort-evidence strength, gate-vs-probe reconciliation, …)` |

`grep -n "probe\|kind \|gate-vs-probe" reports/round-68/claims.md` prints exactly one line —
`199:The round-67 routed defects D1–D4 (abort-evidence strength, gate-vs-probe` — so the round-68
pre-registration does **not** itself classify the instrument; it only carries the repair as a
registered (unscored) item. The conflict is round-67 prose + `SKILL.md:31/:273` against
`SKILL.md:265` and the gate's docstring.

## 2 · PROTOCOL's rule, in one sentence

`PROTOCOL.md` **`## Gate standard`** (`:375`; rule at `:376-379`): *"A **gate** is a committed,
re-runnable verdict script a lane owns: it reads surfaces, compares them against expected values
persisted in its own repo, and returns a verdict. A tool that cannot fail is a **probe**, and is
registered as one."* — i.e. the discriminator is **can it return a failing verdict**, not how it is
used or how much the round credits it.

Applying it: `corpus/check_embedded_outputs.py` exits `1` with a stable finding-id on real drift, so
it is not "a tool that cannot fail", so `kind | gate` (`SKILL.md:265`) is the correct classification
and every `probe` in round-67 prose is a misclassification. §Gate standard **Registry** (`PROTOCOL.md:398-406`)
additionally makes the lane's `SKILL.md` this row's home — which makes `SKILL.md:31` ("No gate
registry. No verifier here is a registered gate") a stale self-contradiction, and §Gate standard
**Delivery** (`PROTOCOL.md:418-423`) grades gates against that row's existence.

## 3 · Does the round-68 instrument still qualify after the repair? (scratch test, as required)

Copies made with `cp corpus/check_embedded_outputs.py /tmp/d2-scratch/{base,mut,spoof,uncond}.py`
(lane file sha256 `b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca`; lane file never
edited). Mutants applied to the **copies** only, with the frozen regexes from
`reports/round-68/claims.md:62-68` (`grep -c` of the comparison call printed `1`).

| run | command | observed |
|---|---|---|
| unmutated self-test (control) | `cd /tmp/d2-scratch && python3 -B base.py --self-test` | `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired` · `exit=0` |
| **frozen mutant** (comparison → `problems += []`) | `python3 -B mut.py --self-test` | `self-test: drifted entry not caught` / `drifted entry output accepted` · `exit=1` — **last line == MARKER, attributed** |
| **frozen negative control** (mutant + `MARKER = "…(spoofed)"`) | `python3 -B spoof.py --self-test` | `self-test: drifted entry not caught` / `drifted entry output accepted (spoofed)` · `exit=1` — `last.endswith(MARKER)` **false**, not attributable |
| entry mode, real drift | `python3 -B base.py --entry drifted.md` | `drift entry:3 embedded output line not in recheck stdout: {"fact": "a", "v": 9}` / `checked_blocks=1 problems=1` · `exit=1` |
| entry mode, clean | `python3 -B base.py --entry clean.md` | `checked_blocks=1 problems=0` · `exit=0` |
| entry mode, unsupported command | `python3 -B base.py --entry unsupported.md` | `could-not-evaluate: …` · `exit=2` |
| entry mode, no `$ cmd` blocks | `python3 -B base.py --entry noblocks.md` | `could-not-evaluate: …` · `exit=2` |
| usage | `python3 -B base.py` | `exit=64` |

So: **yes, it qualifies** — it fails in both modes (so not a probe under the §Gate standard), and
after the repair its own self-test kill is attributable to the registered marker, satisfying
§Gate standard **Self-test** (`PROTOCOL.md:385-389`: isolated temp fixtures, asserts exit code and a stable
expected finding-id — the `drift entry:` prefix and the marker). The round-67 defect was attribution
quality *inside* the self-test, not the ability to return a verdict — which is exactly why the prose
that downgraded it to `probe` was never justified by the §Gate standard.

### Residual, name it rather than hide it

`uncond.py` = frozen mutant **plus** an unconditional `print(MARKER)` on the not-caught path:
observed `drifted entry output accepted` / `self-test: drifted entry not caught` /
`drifted entry output accepted` · `exit=1` → the endswith rule reads **attributed**, though the
marker did not come from the verified branch. The r68 negative control (marker **text** spoof) does
not close this: the endswith rule is necessary, not sufficient — the already-routed
"endswith-attribution asymmetry" (`corpus/lessons/round-67.md:145`). It does not falsify C1's frozen
predicate (that mutant is not the frozen mutant) but the report must not claim more than
"reachable and exact-text checked".

## 4 · `§Gate standard` conformance gaps the reconciliation must also carry

1. **Verdict map omits a code the gate exits.** `SKILL.md:267` declares `0 · 1 · 2` only; the gate
   exits `64` on usage (`corpus/check_embedded_outputs.py:167-168`, observed `exit=64` above).
   §Gate standard **Verdict** (`PROTOCOL.md:380-384`): "every other code a gate exits (`2`, `3`, `64`, …) is
   declared in its registry entry and mapped onto `clean | failed | could-not-evaluate`". Unmapped,
   `64` reads as could-not-evaluate by default — benign in effect, still an undeclared code.
2. **The pin is prose, not verified.** `SKILL.md:269` pins `corpus/knowledge/round-65-apk-axml-byte-evidence.md`
   sha256 `cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a` with expected verdict
   exit 1 naming entry:41. I re-hashed that file: `cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a`
   — **matches**. But `grep -n "hashlib\|sha256" corpus/check_embedded_outputs.py` returns nothing
   (`grep-rc=1`): the gate never hashes its input, so §Gate standard **Two evidences** (`PROTOCOL.md:390-397`,
   "the gate verifies those digests before comparing verdicts: an edited snapshot is
   `snapshot_tampered` (could-not-evaluate)") has no in-gate mechanism. Today's pin is true by
   re-hash, but an edit to the frozen entry yields a *compared* verdict, never `snapshot_tampered`.
3. The row otherwise satisfies the §Gate standard field list: name `:264`, kind `:265`, entry command
   `:266`, verdict map `:267`, self-test spelling `--self-test` `:268`, pinned-value path `:269`,
   write scope `:271` (read-only, argv list, no shell), owner `:272`.

## 5 · Exact conflicting sentences (file:line) the report must reconcile

- `revenger-shokunin/SKILL.md:265` — `| kind | gate (committed, re-runnable verdict script this lane owns) |` (**authoritative, correct**)
- `revenger-shokunin/SKILL.md:273` — `… this probe does not join them (claims.md §C2)` (**wrong kind, same row**)
- `revenger-shokunin/SKILL.md:31` — `- **No gate registry.** No verifier here is a registered gate; a green `--self-test` is` (**stale: a registry row exists at this very file**)
- `revenger-shokunin/SKILL.md:268` — `…the trailing forged-drift control's marker `drifted entry output accepted` is structurally shadowed by that earlier require and can never fire … reorder fix routed` (**stale after the repair: my mutant run prints it as the last line**)
- `revenger-shokunin/reports/round-67/claims.md:102` — `- Registry: the gate registers in `SKILL.md` (this lane's registry home) as a **probe** with`
- `/home/vgpnk/Projects/shokunin/.ufo/reports/round-67/revenger.md:14`, `:20`, `:63` — `New registered probe …` / `row (probe; verdict map 0/1/2; …)` / `the C7 probe landed …`
- `revenger-shokunin/corpus/lessons/round-67.md:145` — `verbatim-output-diff gate now EXISTS as the C7 probe (its attribution defect is item 2)`

## 6 · Reconciliation the round-68 report must make

1. **State the kind once, from the §Gate standard discriminator**: `kind = gate`, because the
   instrument returns a failing verdict (entry mode `exit 1` + stable `drift entry:N`; self-test
   mutant `exit 1` + marker) — quote `PROTOCOL.md:375-379`.
2. **Do not edit `reports/round-67/claims.md`.** It is a frozen pre-registration (append-only);
   PROTOCOL §Evidence standard: "A falsified claim in an append-only file gets a named correction
   entry in the lane's next round — appended, never rewritten." Record a **named correction entry**
   in the r68 report/lesson that supersedes `:102` and, per "Corrections sweep every mention", the
   four other prose occurrences (`revenger.md:14/:20/:63`, `lessons/round-67.md:145`).
3. **Fix `SKILL.md` in place** (lane-owned instruction file, already edited at r67 adjudication):
   `:273` "this probe" → "this gate"; `:31` "No gate registry. No verifier here is a registered
   gate" → "no `verify_*.py` verifier is a registered gate; the one registered gate is
   `check_embedded_outputs` (`## Gate registry`)" while **keeping** the clause "a green `--self-test`
   is replay evidence, not admission" (that clause is right and independent of kind); and rewrite
   `:268` to the post-repair measured truth (self-test `exit 0` unmutated; frozen mutant `exit 1`
   with `drifted entry output accepted` as the **last** line; spoof-marker control not attributable;
   cite this scratch receipt).
4. **Complete the row's §Gate standard fields** the classification imports: add `64` → could-not-
   evaluate to the verdict map, and either add in-gate digest verification of the pinned entry
   (hashlib against the recorded sha, `snapshot_tampered` → exit 2) or state in the row that the pin
   is registry-prose-level and that §Gate standard "Two evidences" digest verification is an
   **unmet clause** — do not let the row's `kind | gate` imply a conformance it lacks.
5. **Do not re-score `C7_MUTANT_KILLED_ATTRIBUTED` on this audit.** Kind is a registry field, not an
   axis claim; C1's frozen predicate stands as the measurement, and the verdict map change in (4)
   must not be presented as a new capability.

## 7 · Impacted axes and smallest safe correction

- **calibration** — the instrument is scored under C1/C8, and a `probe` label would let a later
  round credit it as replay evidence instead of a verdict, changing the credit path (`SKILL.md` §1
  Q13 discipline).
- **quality** — `SKILL.md:31/:268/:273` are lane-instruction claims that are now false; left
  unmarked they are exactly the "found stale and left unmarked" condition.
- **coverage** — not impacted; D2 touches no knowledge entry, no README row, no C05 status.
- **Smallest safe correction**: the five in-place `SKILL.md` sentence edits in §6.3 + the named
  correction entry in §6.2, plus the two field completions in §6.4. No gate code change is required
  for C1; the digest check is the only code-shaped item and can be declared-unmet instead.

## 8 · Counterexample tested and rejected

Strongest attack available: "the repaired instrument is still a probe because its *self-test* — the
only thing the round measures — was never able to fail for the right reason, and a marker printed
unconditionally satisfies the same rule." Rejected as a classification argument: on the §Gate
standard the discriminator is whether the tool can return a **failing verdict** on its real surface,
and entry mode does so reproducibly (`exit 1`, `drift entry:3`, `checked_blocks=1 problems=1`) while
`exit 2`/`0` carry the other two verdict classes. The unconditional-print run is a genuine limitation
of the **attribution rule** (row §3), not of the kind — it is reported as a named limitation, not
folded into the kind decision.
