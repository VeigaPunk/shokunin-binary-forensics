FAIL — Q15 on the round-69 C05 v4 entry: the only stated git object id (`c7b7cf98`, entry line 8) carries an unguarded tree-identity sentence with no deriving command anywhere in the entry, and the entry's §Q-map has no Q15 row at all. The three mandated instrument checks are met literally (row present and structurally well-formed, self-test pass, D1 scan non-zero), but the D1 scan's non-zero is over-determined and the counter's `Q15_FALSE_KILLED` leg cannot distinguish a killed false pair from a file that contains none.

criterion: Q15 (`corpus/QUALITY.md:27`) · entry under test: `corpus/knowledge/round-69-apk-axml-byte-evidence.md`, sha256 `c1e7eaac9dba4c77e578c788755dec3e3499fd8795ad0e479c51b5be7deb11d5`, blob `00402958f673fc55ed738664d60f2e543eb73129` at HEAD `35e12584d37434632fa06a6c2975ab55f29a8d3f` · instrument: `corpus/q15_tree_id_check.py`, sha256 `7d074f98cb7f9ff2be4c17e6b97e60ac8d660c827a32009d85a35df50639d276`, 129 lines · lane root `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## 1. Mandated checks

### 1a. QUALITY row present and well-formed — PRESENT, with a dangling lesson pointer

```
$ grep -n '^| Q15 ' corpus/QUALITY.md
27:| Q15 | A stated git object id or tree identity is re-derived with the command that names it; a sentence asserting `X:corpus` equals a hash must resolve under `git rev-parse X:corpus`. | an identity sentence is asserted without the deriving command, or the named object resolves to a different value (r68 `measure-after.log:102` calling the `1c34603` corpus tree byte-identical to the `14774a2c` tree when the command prints different tree ids) | M48 (`lessons/round-69.md`) |
```

Structure is well-formed: four columns, a reject clause grounded on the exact D1 evidence, and the row is the only change to the file —

```
$ git diff da02261^ da02261 -- corpus/QUALITY.md
1 file changed, 1 insertions(+), 0 deletions(-)   # @@ -24,6 +24,7 @@ +| Q15 | ...
```

— so Q01–Q14 are untouched (no supersession, no rewrite; `corpus/QUALITY.md` blob `3f7a138d85f641ec74c594ad2ed7bcacc5263994` at HEAD).

**Defect (medium, well-formedness):** the `lesson` cell cites `M48 (lessons/round-69.md)` but that file does not exist at the measured tree:

```
$ ls corpus/lessons/round-69.md
ls: cannot access 'corpus/lessons/round-69.md': No such file or directory   (exit 2)
$ ls corpus/lessons/ | tail -3
round-68-verifier-spotcheck.md
round-68.md
round-68-verifier-spotcheck.md
$ grep -c 'M4[67]' corpus/lessons/round-68.md
2
```

M46/M47 live in `round-68.md`, so M48 is an unallocated number and the intended target is coherent — but a normative criterion row in `QUALITY.md` pointing at a non-existent lesson row is a dangling citation at this tree. It resolves only when `corpus/lessons/round-69.md` lands (claims.md §Frontier step). At the final measured tree it must resolve, else the row is malformed by its own `lesson` contract.

### 1b. `--self-test` — PASS

```
$ python3 -B corpus/q15_tree_id_check.py --self-test
Q15_SELFTEST=pass (true sentence verified; false sentence killed)
exit=0
```

The self-test exercises the algorithm against a fixed resolver (`q15_tree_id_check.py:61-77`): one true line must verify, one false line must be rejected, both by exact pair accounting. Its fixed map value `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7` agrees with the live object store (see §5), so the fixture is not self-contradictory.

### 1c. `--scan` on D1FIX — exits non-zero, but not for the reason claimed

```
$ python3 -B corpus/q15_tree_id_check.py --scan reports/round-69/d1-false-sentence.md
Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)
exit=1
```

The requirement "must exit non-zero" is met. The exit is over-determined, though: that message and the `return False` come from the `restate_count == 0` branch (`q15_tree_id_check.py:103-105`), i.e. the file fails partly because it carries a false-sentence line **and no restatement line**. See §2.

## 2. Defect: `Q15_FALSE_KILLED` is gameable (high, calibration)

`reports/round-69/measure.py:161-166` reduces the whole D1 check to the process exit code:

```
161:    d1 = TREE / "reports/round-69/d1-false-sentence.md"
163:        rc, last = run(TREE, "q15_tree_id_check.py", "--scan", "reports/round-69/d1-false-sentence.md", "--lane", LANE)
165:        q15_false_killed = rc != 0
```

Three scratch fixtures I wrote under `/tmp/revenger-r69-q15/` (now deleted) produce the same `rc != 0`, hence the same `Q15_FALSE_KILLED=yes`:

```
=== true-as-false.md ===   # the D1 pair corrected to the TRUE hash, no restatement
Q15_RESTATE_BAD: no false-sentence pair failed (quote does not demonstrate the class)
exit=1
=== empty.md ===           # no tree-identity line at all
Q15_RESTATE_BAD: no false-sentence pair failed (quote does not demonstrate the class)
exit=1
=== restate-only.md ===    # one correct restatement, no false-sentence line
Q15_RESTATE_BAD: no false-sentence pair failed (quote does not demonstrate the class)
exit=1
```

So `Q15_FALSE_KILLED=yes` is satisfied by a fixture that does **not** quote a defensible false pair (including an empty file). The C2 "ability-to-fail receipt" is therefore not guarded by its own instrument — the same class as the C7 gameability carried as D5. The scan itself does distinguish the cases on stdout (`Q15_RESTATE_BAD: no false-sentence pair failed` vs `Q15_FALSE_KILLED: ...`), so the fix is local: either match the stdout branch, or give the checker distinct exit codes (false pair not killed ≠ restatement bad ≠ no false pair present).

Positive controls confirming the restatement leg is real (so the gap is the false-kill leg only):

```
=== pos.md ===  # true restatement + D1 false pair
Q15_RESTATE_OK=yes (every restatement pair re-derived; false-sentence pair killed)
exit=0
=== neg.md ===  # wrong restatement + D1 false pair
Q15_RESTATE_BAD line 1: `1c34603:corpus` claimed 51894d153a6e69487da2a273680d014abd240f61 resolved ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7
exit=1
```

## 3. Defect: the Q15 FAIL on the entry's own bytes (high, coverage gate)

Entry line 8 states a git object id and a content identity across it:

> `verified-at: 2026-10-25 (round-69 re-derivation; the fixture, oracle and readout bytes are the round-65 claim-tree bytes, unchanged since `c7b7cf98`; …)`

The entry carries **no** deriving command for that object:

```
$ grep -cin 'git' corpus/knowledge/round-69-apk-axml-byte-evidence.md
0
$ grep -n 'rev-parse\|git ' corpus/knowledge/round-69-apk-axml-byte-evidence.md
(no output)
```

The `recheck:` line (entry line 9) names only `corpus/derive_axml_anchors.py` and `corpus/fixtures/apk-r65/readout.py`; §Reproduce (lines 186-200) likewise. Q15's reject clause, first half, fires: *"an identity sentence is asserted without the deriving command."* So Q15 = **FAIL for this entry**, on line 8 — and the entry does not even record a Q15 decision: `§Q-map` (lines 173-184) carries rows for Q01, Q02, Q04, Q05, Q07, Q11, Q13, Q14 only; **no Q15 row**. claims.md §C1 requires "every applicable Q01–Q15 decision … is PASS", so the entry is not gate-complete as landed, independent of my verdict.

Re-derivation of the value the entry owes (read-only, lane store):

```
$ git log -1 --format='%H %s' c7b7cf98
c7b7cf98ddeecbd5464e47396f224e6384b78905 round-65: candidates — apk-r65 fixture+readout, C05 candidate entry, S038-S041 rows, C5 forged-evidence controls, lesson+wave spec (no README flip)
$ git rev-parse c7b7cf98:corpus/fixtures/apk-r65 HEAD:corpus/fixtures/apk-r65
dd6615e67342a020fbd28b720ede0bf55f9d14c7
dd6615e67342a020fbd28b720ede0bf55f9d14c7
$ git diff --stat c7b7cf98 HEAD -- corpus/fixtures/apk-r65
(no output, exit 0)
$ for f in fixture.apk truth.json generator.py readout.py; do git rev-parse c7b7cf98:corpus/fixtures/apk-r65/$f HEAD:corpus/fixtures/apk-r65/$f | tr '\n' ' '; echo; done
b62216a955a4b130b67b7f8d35806abf07be92fa b62216a955a4b130b67b7f8d35806abf07be92fa
d6b8c5cb348a1bb97f0c6d4dce692e1f1297a504 d6b8c5cb348a1bb97f0c6d4dce692e1f1297a504
aea5de72eeac84d1a4b1da3ed5b0c76af64187c3 aea5de72eeac84d1a4b1da3ed5b0c76af64187c3
0fcb1d859b3fcebad600ad5bc141cc0c0dd35bc8 0fcb1d859b3fcebad600ad5bc141cc0c0dd35bc8
```

Correct value the sentence needs to carry: `c7b7cf98:corpus/fixtures/apk-r65` = `dd6615e67342a020fbd28b720ede0bf55f9d14c7`, identical to HEAD's, with all four file blobs unchanged. **The sentence is true but unguarded** — so this is the derivation-absence half of the reject rule, not the "resolves to a different value" half. The fix is a one-line addition in the entry, e.g. `git rev-parse c7b7cf98:corpus/fixtures/apk-r65` = `dd6615e6…` (same as `HEAD:`), plus a Q15 row in §Q-map deciding it.

Same class, unguarded, lower weight:

- entry line 188: "with the round-65 corpus tree (bytes unchanged through round 69)" — a tree-content assertion with no id and no command.
- entry line 11: "The round-65, round-67 and round-68 candidates keep every byte." — content-identity across three commits, no id, no command (this one matters for claims.md §Void conditions, which void the round if prior candidates were altered, so the claim is load-bearing for the round's validity).

## 4. Defect: the row's stated reach exceeds the instrument (medium, Q13 shape)

`QUALITY.md:27` states the rule generally ("a stated git object id or tree identity is re-derived with the command that names it"), but the instrument only scores lines that begin with the bespoke prefixes `tree-identity restatement:` / `tree-identity false-sentence:` and only the pair syntax `` `<7-40 hex>:corpus` = `<40 hex>` `` (`q15_tree_id_check.py:34,79-105`). It returns a verdict on exactly those two line types, and the counter runs it on exactly two paths (`measure.py:158-178`: `corpus/lessons/round-69.md`, `reports/round-69/d1-false-sentence.md`). It gives **no** verdict on the defect class in ordinary entry prose:

```
$ python3 -B corpus/q15_tree_id_check.py --scan corpus/knowledge/round-69-apk-axml-byte-evidence.md
Q15_RESTATE_BAD: no false-sentence pair failed (quote does not demonstrate the class)
exit=1
```

That exit 1 is a statement about the file lacking the prefix, **not** a finding about the entry's line 8 — the same exit would occur for an entry with no identity sentence at all. Therefore Q15 as written must not be credited as mechanized for knowledge entries by this checker (Q13); the row should name the instrument and its scope (lesson normalized lines only), or the criterion needs an entry-level command requirement enforced by review rather than by the scan. As written, a fresh-seat Q15 PASS on a future entry would rest entirely on human re-derivation.

## 5. Positive: the D1 fixture is honest

The ability-to-fail target is real and the fixture quotes it accurately:

```
$ git rev-parse 1c34603:corpus dddf147:corpus 14774a2c:corpus
ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7   # 1c34603 — NOT 51894d15…
51894d153a6e69487da2a273680d014abd240f61   # dddf147
51894d153a6e69487da2a273680d014abd240f61   # 14774a2c
$ sed -n '102p' reports/round-68/measure-after.log
final measured commit: 1c3460336d14e9bbe64778f826a07bdd996ce39b (the correction commit; its corpus/ tree is byte-identical to the earlier measured 14774a2c tree — 51894d153a6e69487da2a273680d014abd240f61 — and to the receipt commit's, verified with git rev-parse <commit>:corpus)
```

`reports/round-69/d1-false-sentence.md`'s normalized pair `` `1c34603:corpus` = `51894d15…` `` reproduces the round-68 sentence's assertion and is contradicted by `git rev-parse 1c34603:corpus`, exactly as the fixture says. No value in the fixture is wrong.

## 6. Residual risk / verification gaps

- `Q15_RESTATE_OK` is unmeasurable at HEAD: `corpus/lessons/round-69.md` is absent, so `measure.py:170-178` prints `Q15_RESTATE_OK=n/a (no round-69 lesson)`. Note the structural consequence for C2: `scan()` requires **both** `restate_count > 0` **and** at least one failing false-sentence pair in the same file (`q15_tree_id_check.py:79-105`). A clean lesson carrying only the corrected restatement exits 1 and yields `Q15_RESTATE_OK=no`; the round-69 lesson must therefore embed the D1 false line as well to reach `yes`. The C2 author should confirm that is intended (it is consistent with a single-file "ability-to-fail + restatement" receipt, but it is not obvious from claims.md §C2).
- I judged Q15 only. Other criteria (Q01–Q14, C7, counter replay) are other seats' scope; I did not edit any file, and no README status was touched by me.
- Evidence base: HEAD `35e1258`, build commit `da02261`, worktree clean except the untracked `.ufo/waves/round-69/assimilation/` directory (not mine, not touched).
- Tooling: nothing installed or upgraded (no package transactions attempted; the host-wide pacman pause was irrelevant to this seat). Scratch `/tmp/revenger-r69-q15/` deleted.
