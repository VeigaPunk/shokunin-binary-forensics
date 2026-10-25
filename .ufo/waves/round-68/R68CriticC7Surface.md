CLAIM-AFFECTED — a gate that violates its own registry row ("every embedded output line verbatim", SKILL.md:267) reads at target on *every* C1 conjunct (SELFTEST pass, CONTROL 1/1, MUTANT_KILLED 1/1 + ATTRIBUTED 1/1, NEG_SPOOF 1/1 + 0/1, RED_ON_R65 yes, V3_CLEAN yes); C1 cannot distinguish the landed gate from a strictly weaker one, because `_self_test`'s drift fixture is a *single* line. Two secondary findings are also claim-scoped: SKILL.md:268 still registers the pre-repair gate as truth, and `C7_CONTROL_PASS` is structurally inert.

Seat: L1Revenger68.R68CriticC7Surface · lane /home/vgpnk/Projects/shokunin/revenger-shokunin · read-only seat, no production edits.

Artifact hashes (measured this run):
```
b89183bec2fd3b94f5b0acc828a0d3fe16f6a98dde1d7752616da85d08a8e0ca  corpus/check_embedded_outputs.py
19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d  base f165908:corpus/check_embedded_outputs.py (/tmp/r68-surface/base_gate.py)
56b88bc4a34a9cf41323736a7a3ae935e46002515dc6a3f9109b2e408957c56f  corpus/snapshots/ResourceTypes.h (86255 bytes, matches claims.md)
```

## 1. Did the round-68 repair move the detection surface? No — measured, not asserted.

`git show f165908:corpus/check_embedded_outputs.py` diffed against the landed file: **3 hunks, 16 insertions / 13 deletions**, located at docstring `@@ -3,7 +3,9 @@`, docstring `@@ -16,7 +18,9 @@`, and the forged control `@@ -129,21 +133,20 @@`. The third hunk replaces the base's shadowed trailing
`require(not ok(dproblems), MARKER)` (+ the `ok()` helper) with an early `if not caught: print("self-test: drifted entry not caught"); print(MARKER); sys.exit(1)` at `corpus/check_embedded_outputs.py:140-146`, placed **before** the `full_entry` require at `:147-148`.

`parse_blocks` (:47-73), `run_cmd` (:75-81), `drift` (:83-85) and `evaluate` (:87-107) are byte-identical between base and landed.

Behavioural confirmation, all 15 probe entries through both modules (`(problems, checked)` tuples):

| case | base f165908 | landed b89183b | same |
|---|---|---|---|
| A_reordered | `([], 1)` | `([], 1)` | True |
| B_duplicated | `([], 1)` | `([], 1)` | True |
| C_substring | `(['drift entry:3 … alpha'], 1)` | idem | True |
| D_realfull_partial | `([], 1)` | `([], 1)` | True |
| E_emptyout | `([], 1)` | `([], 1)` | True |
| F_cmd_no_out | `([], 1)` | `([], 1)` | True |
| G2_notfirst_drift | `(['drift entry:4 … delta=4'], 1)` | idem | True |
| H2_indent_mixed | `([], 1)` | `([], 1)` | True |
| I2_nospace_mixed | `([], 1)` | `([], 1)` | True |
| L_fence_desync | `([], 1)` | `([], 1)` | True |
| M_dollar_out | `(None, None)` | `(None, None)` | True |
| N_unsupported | `(None, None)` | `(None, None)` | True |
| J_stderr_only | `(['drift entry:3 … alpha=1'], 1)` | idem | True |
| K_trailing_ws | `(['drift entry:3 … alpha=1 '], 1)` | idem | True |
| F_partial | `(['drift entry:4 … delta=4'], 1)` | idem | True |

15/15 identical → the repair changed attribution only, exactly as the claim requires. Every blind spot below therefore also holds for the round-67 gate; the repair neither introduced nor closed any of them.

## 2. The six asked-for surfaces

| # | surface | verdict | code reason (file:line) | measured |
|---|---|---|---|---|
| 1 | reordered embedded output lines | **NOT caught** | `stdout_set = set(stdout.splitlines())` at `:104`; `drift` is membership-only `l not in stdout_set` at `:85` — order is destroyed by the set and never compared | A_reordered (gamma, alpha, beta vs stdout alpha, beta, gamma) → `problems=0 checked=1` |
| 2 | duplicated embedded output lines | **NOT caught** | same set membership (`:104`, `:85`); duplicates in `lines` cannot fail a membership test | B_duplicated (alpha twice) → `problems=0 checked=1` |
| 3 | embedded line that is a SUBSTRING of a real stdout line | **CAUGHT** (drift) | comparison is whole-line equality against the *set of stdout lines* (`:104`), not substring search, so a truncated line is simply absent from the set | C_substring (`alpha` vs `alpha=1`) → `drift entry:3 … alpha`, exit 1 |
| 4 | command whose stdout changes between runs | **NOT caught — and it makes the gate itself nondeterministic** | `run_cmd` at `:75-81` samples stdout exactly once per invocation; there is no stability check, no second run, no recorded comparison between runs | entry quoting `alpha=1` under `random.choice(["alpha=1","alpha=9"])`, 40 invocations → histogram `{0 problems: 21, 1 problem: 19}` |
| 5 | `$ cmd` block whose output is empty | **NOT caught — vacuous pass, and it is counted as verified** | `:62` `if lines[j].strip():` means no output lines are ever appended; `drift([], stdout_set, lineno)` returns `[]` by construction (`:83-85`); `checked += 1` still fires at `:106` | E_emptyout and F_cmd_no_out both → `problems=0 checked=1` |
| 6 | block that is not the first line of the fence | **CAUGHT** | the block start is any fence-internal column-0 `"$ "` line (`:57`), not the fence's first line; preceding prose is skipped by the `i += 1` fallthrough (`:66-67`) | G2_notfirst_drift (prose, then `$ cmd`, then fabricated `delta=4`) → `drift entry:4 … delta=4` |

Two of the six are false-pass surfaces by design, not by accident: (1)/(2) are the *registered* semantics of a set comparison, (4)/(5) are single-sample and vacuous-pass holes.

## 3. Same-class surfaces found while testing (silent skip > loud fail)

| surface | verdict | reason | measured |
|---|---|---|---|
| column-2-indented `$ cmd` (nested list / indented fence) | **NOT caught, silently** | `:57` requires `line.startswith("$ ")` at column 0; an indented block is invisible, and with another clean block present the verdict is still exit 0 | H2_indent_mixed (clean block + indented drifted block) → `problems=0 checked=1` (2 blocks present) |
| `$cmd` without the space after `$` | **NOT caught, silently** | same `:57` prefix test | I2_nospace_mixed → `problems=0 checked=1` |
| 4-backtick fence containing a 3-backtick line | **NOT caught** | `in_fence = not in_fence` on any `line.strip().startswith("```")` (`:52-55`) — parity desync lets a fabricated line fall outside any comparison | L_fence_desync → `problems=0 checked=1` |
| embedded output line that itself begins `$ ` | **downgrades the whole entry to exit 2** | `:61` stops the output scan at `"$ "`, so the line is re-read as a command; a non-python token trips the whitelist at `:76-77` → `(None, None)` at `:100` | M_dollar_out → `(None, None)` |
| one unsupported command anywhere in the entry | **poisons the entire verdict** | `evaluate` returns `(None, None)` on the first unsupported argv (`:100`); there is no per-block partial verdict | N_unsupported (1 clean python block + 1 `grep` block) → `(None, None)` |
| stderr content | **never compared** | `:104` builds the set from `stdout` only (`capture_output=True` collects stderr, unused) | J_stderr_only → drift even though the command printed `alpha=1` to stderr |
| under-quotation (entry omits real stdout lines) | **NOT caught** | the check is one-directional: entry ⊆ stdout. `drift` never asserts stdout ⊆ entry, so any number of real lines — including a diagnostic or footer — can be dropped | D_realfull_partial (1 of 3 real lines) → `problems=0` |

Note on (a): an indented/`$cmd` block that is the *only* block yields `(None, None)` → exit 2, not a false pass. The silent-skip is only exploitable when ≥1 normal block is present, which is the normal case for a 17-block entry.

## 4. Claim impact — the hole is the control's fixture width, not the mutant

The frozen mutant (measure.py:386 `C7_CLAUSE` exactly once → `problems += []`) removes the *only* comparison site (`:105`), so it is genuinely killed and genuinely attributed. That part of C1 is solid.

The gap is upstream of the mutant: `_self_test`'s drifted fixture quotes **one** line (`:118-127`: `clean_line`/`drifted_line`, one line each), and `caught` (`:140-146`) only requires that this one line be flagged. Any detector that compares the first embedded line of each block passes `caught`, hence passes the self-test, hence satisfies every attribution label — while ignoring all further lines, contradicting SKILL.md:267 ("every embedded output line verbatim").

Demonstrated with a single-character-class weakening, `for l, out_lineno in lines if l not in stdout_set]` → `... in lines[:1] if ...` (`:85`), then the counter's **verbatim** mutant and spoof clauses applied to that weakened file:

```
A. weakened gate text contains MARKER: True
B. C7_SELFTEST           exit=0 pass=True
   C7_CONTROL_PASS        1/1
C. C7_MUTANT      exit=1 killed=True attributed_last_line=True  last='drifted entry output accepted'
C. C7_NEG_SPOOF   exit=1 killed=True attributed_last_line=False last='drifted entry output accepted (spoofed)'
D. C7_RED_ON_R65_CANDIDATE=yes exit=1 :: checked_blocks=15 problems=1
E. C7_V3_CLEAN(weakened)=yes exit=0 :: checked_blocks=17 problems=0
F. partial-drift under real     : exit=1 :: checked_blocks=1 problems=1
F. partial-drift under weakened : exit=0 :: checked_blocks=1 problems=0
```

Every C1 conjunct reads at target for a gate that misses drift past line 1 of every block — and C2's `C7_V3_CLEAN=yes` conjunct reads clean under it too.

The weakening is conservative for the red label only by accident of fixture shape: every block in the r65 candidate is single-line (`output-line-counts=[1]*15`), so the M39 drift is a first line. It does not generalise.

Exposure on the actual claimed artifact — `corpus/knowledge/round-68-apk-axml-byte-evidence.md`, per-block quoted-line counts:
```
17 blocks, counts = [1]*15 + [17, 15], 0 empty blocks, 47 quoted lines total
  block at entry line 128, 17 quoted lines, cmd = python3 -B corpus/derive_axml_anchors.py
      first: sha256 56b88bc4…c56f ResourceTypes.h
      last : field attributeStart : 687
  block at entry line 199, 15 quoted lines, cmd = python3 -B corpus/fixtures/apk-r65/readout.py
```
The 17-line block at **entry:128 is item 11, the machine-derived anchors** — the `RES_XML_START_NAMESPACE_TYPE : 245`, `:686`, `:687` lines that C2's whole admission rests on. Under a first-line-only detector only the sha256 header is enforced; the 16 anchor lines are free. 32 of 47 quoted lines (68%) in the admitted candidate sit outside what C1 can pin. Reordering (surface 1) is also live on these two blocks under the *landed* gate: a permutation of the 16 anchor lines still reads clean.

And the controls do not catch it: `C7_CONTROL_PASS` is `c7_selftest_ok and C7_MARKER in c7_gate.read_text(...)` (measure.py:408) — a source-text containment test, not a reachability test. It read `1/1` on the base tree where the marker was shadowed dead code (`reports/round-68/measure-before.log:75`, restated at `:106`), proving it cannot detect shadowing. It also reads `1/1` for the weakened gate above. It adds no discriminating power to C1.

## 5. Secondary finding — the registered row still describes the pre-repair gate

`SKILL.md:268` (the row C1's build state names) is unchanged round-67 text and now asserts two falsehoods about the landed gate:

- "the drifted-case `require` at `_self_test` carries the frozen-mutant kill" — after the repair the drifted case is an `if not caught:` branch (`:140-146`), and the base's trailing `require` is gone; there is no `require` carrying it;
- "the trailing forged-drift control's marker `drifted entry output accepted` is structurally shadowed by that earlier require and **can never fire**" — the landed gate fires it, and `C7_MUTANT_KILLED_ATTRIBUTED=1/1` is exactly that firing.

`grep -n 'round-68\|r68\|2026-10-24' SKILL.md` returns no round-68 gate-registry edit (hits at :6, :268, :332, :487 only). The registered authority for the gate therefore contradicts the measured gate at precisely the value C1 is scoring. C1's frozen pass branch contains no obligation to correct the row — only the kill rule does ("The gate's registry row is then corrected to state the measured truth") — so a C1 PASS leaves a registered artifact stating the opposite of the result. The round-68 negative control is likewise undocumentable from the row.

## 6. Impacted axes

- **calibration (C1)** — primary. The `C7_MUTANT_KILLED_ATTRIBUTED=1/1` conjunct measures *attribution plumbing*, not detection semantics; the predicate is satisfiable by a gate that fails SKILL.md:267. C1 as frozen is not falsified by this, but its 1/1 is not evidence that the registered detection surface holds.
- **coverage (C2)** — consequential. `C7_V3_CLEAN=yes` inherits the same non-discrimination, and 32/47 of the admitted candidate's quoted lines (incl. the 16 machine-derived anchors at entry:128) are outside what the C1 control constrains. This does not impugn the landed v3 bytes — the landed gate compares all 47 lines, and it reads `checked_blocks=17 problems=0 exit=0` on them — it means the *clean-comparison* conjunct is weak evidence.
- **provenance / registry truth** — SKILL.md:268.

## 7. Smallest safe correction (routed, NOT applied — read-only seat)

Not applicable to this round's pass branch: the counter and the predicate are frozen and already pre-registered, so adding a case now would change the measured rule after seats scored. Route to the next round's gate work, or record as a limitation in the same way r67 recorded its shadowing limitation in SKILL.md:268:

1. **Gate self-test (~6 lines, `_self_test` at `:118-148`), the real fix.** Add a `partial.md` fixture whose block quotes two lines: the first *correct*, the second fabricated. Require it to be caught, in the **attributed** form (same `print(MARKER); sys.exit(1)` shape as `:142-145`) so a first-line-only or truncated-comparison mutant dies on `C7_SELFTEST` itself — i.e. C1 fails for the weakened gate, with no new counter label and no change to any existing conjunct. A `print(MARKER)`-attributed partial-drift branch also keeps `C7_MUTANT_KILLED_ATTRIBUTED` semantics intact.
2. **Registry row (`SKILL.md:268`)**, independent of the claim's verdict: replace the "can never fire" correction with the measured statement (marker is the last line of the failed self-test; the drifted case is an `if not caught:` branch at `:140-146`), and record the round-68 negative control. A row that says the opposite of the gate should not outlive the round either way.
3. If detection-coverage is to be scored rather than annotated, the honest additional conjunct is a *multi-line* drift fixture inside the existing self-test — not a new counter label, since every `C7_*` label is frozen and `HOLD_*` denominators must not move.

Deliberately **not** recommended: "fix" surfaces 1/2 (order, duplication) by asserting sequence. That is a semantic change to the registered verdict map and to every existing admitted entry; a set-membership gate is a legitimate, documented design. The defect is that C1 cannot tell that design from a truncated one — fixing the control is strictly cheaper and harms no axis.

## 8. Scope of this finding — what it does not say

- The landed gate is **not** broken: it compares all 47 quoted lines of the v3 candidate (`checked_blocks=17 problems=0`), catches the M39 drift (`entry:41`), and its mutant kill is genuinely attributed — the frozen mutant removes the sole comparison site at `:105` and the marker fires as the last line (`:144`).
- No blind spot in §2/§3 makes the **frozen** mutant survive: the mutant deletes the call, so fixture width is irrelevant to it. C1's kill is real; only its *discrimination* is thin.
- Nothing here touches corpus/live, corpus/fixtures, the snapshot, the README C05 row or the counter.

## 9. Reproduction

All probes in `/tmp/r68-surface/` (outside the lane): `reader.py`, `probe.py`, `probe2.py`, `c1labels.py`, `compare.py`, `v3blocks.py`, `base_gate.py`, `weak/g_weak.py`, and the case entries `A_reordered.md … N_unsupported.md`. Entry-mode invocations read-only over the lane:

```sh
cd /home/vgpnk/Projects/shokunin/revenger-shokunin
python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-68-apk-axml-byte-evidence.md   # checked_blocks=17 problems=0, exit 0
git show f165908:corpus/check_embedded_outputs.py > /tmp/r68-surface/base_gate.py && diff -u /tmp/r68-surface/base_gate.py corpus/check_embedded_outputs.py
python3 -B /tmp/r68-surface/compare.py        # 15/15 identical base vs landed
python3 -B /tmp/r68-surface/c1labels.py       # weakened gate: all C1 labels at target, partial drift missed
```

Tooling: none installed or upgraded (python3 stdlib only). No pacman/uv/npx transaction was run. No git/jj mutation was run — `git show` read only. No file outside this report was written; `/tmp/r68-surface/` is scratch and may be deleted.
