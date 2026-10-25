DEFECT — the corpus path surface is tracked, inside the 1 MiB rule and artifact-free (509 tracked = 509 on disk, no `__pycache__`), but `corpus/README.md` is stale in four places (criteria range still `Q01–Q13` after this round's Q15 row; `snapshots/`, `derive_axml_anchors.py`, `check_embedded_outputs.py`, `q15_tree_id_check.py` named nowhere; the `knowledge/` bullet cannot describe this round's `admission-status: candidate`), and two round-69 operability defects make C2's `Q15_FALSE_KILLED=yes` unreachable under the frozen invocation and non-separating if reached.

Seat: `L1Revenger69.R69CorpusPathHygiene` (read-only; nothing in the repo was written except this report). Base `222a7a7`, measured tip `35e12584d37434632fa06a6c2975ab55f29a8d3f`. No tool installs or upgrades; no `git`/`jj` mutation (only `git log/diff/ls-files/ls-tree/archive/rev-parse` reads); scratch `git archive` trees lived at `/tmp/revenger-r69-hyg*` and are removed.

## Axes

1. Tracked-ness and size of every corpus path this round touched.
2. Untracked/ignored artifact leakage (`__pycache__`, editor droppings) and index currency.
3. Operability of the round-69 build state the corpus now carries (`QUALITY.md` Q15 + `q15_tree_id_check.py` + the C05 v4 candidate) under the claims' own frozen counter invocation.

## 1. Corpus inventory and this round's additions — CLEAN

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin ls-files corpus/ | sort | wc -l
509
$ git -C .../revenger-shokunin diff --name-status 222a7a7..HEAD -- corpus/
M	corpus/QUALITY.md
M	corpus/SOURCES.md
M	corpus/derive_axml_anchors.py
A	corpus/knowledge/round-69-apk-axml-byte-evidence.md
A	corpus/q15_tree_id_check.py
```

Five paths, all tracked at HEAD, both additions at mode `100644`/`100755` in `git ls-tree -r -s HEAD`:

```
100755 ec424adf…	corpus/derive_axml_anchors.py      (M, 51 insertions)
100755 68295734…	corpus/q15_tree_id_check.py        (A, 129 insertions)
100644 00402958…	corpus/knowledge/round-69-apk-axml-byte-evidence.md  (A, 215 insertions)
```

Round-69's chassis-pinned `admission-status: candidate` is present at `corpus/knowledge/round-69-apk-axml-byte-evidence.md:11`, which is the mandated build state (claims.md §C1: the README C05 row is **not** flipped); `corpus/README.md:34` correctly still reads `| C05 | … | — | … | uncovered |`.

## 2. Size versus the 1 MiB directory-commit rule — COMPLIANT

```
$ git ls-tree -r -l HEAD -- corpus/ | awk '$4>=1048576' | wc -l
0
$ git ls-tree -r -l HEAD -- corpus/ | sort -k4 -rn | head -3
364740  corpus/live/runs/round-7/comparison-request.json
342689  corpus/live/runs/round-14/trace-request.json
342688  corpus/live/runs/round-18/trace-request.json
$ git ls-tree -r -l HEAD -- corpus/ | awk '{s+=$4} END {print s}'
4772428
```

Largest corpus file 356 KiB; this round's largest addition 34.3 KiB (`round-69-…-evidence.md`), smallest 4.9 KiB (`derive_axml_anchors.py`). Nothing approaches the per-file 1 MiB skip threshold (rule text as carried by the seat contract and quoted in `.ufo/waves/round-68/R68CorpusPathHygiene.md:43`).

## 3. Untracked / ignored artifacts — CLEAN

```
$ git status --porcelain -uall --ignored -- corpus/
(no output)
$ find . -name '__pycache__' -not -path './.git/*' ; find . -name '*.pyc' -not -path './.git/*'
(no output)
$ find corpus -type f \( -name '*.orig' -o -name '*.rej' -o -name '*~' -o -name '*.bak' -o -name '*.tmp' -o -name '*.swp' -o -name '.DS_Store' \)
(no output)
$ git ls-files -s corpus/ | awk '$1=="120000"' | wc -l
0
```

`git ls-files corpus/ | wc -l` = 509 and `find corpus -type f | wc -l` = 509, so the corpus working tree contains exactly the tracked set: no untracked, no ignored. `.gitignore` holds only `.ufo/interactive-sessions/`; there is no `.gitattributes`, so no eol/filter hazard on the snapshot bytes. Running the Q15 checker with `-B` (as the counter does) left no bytecode behind — re-verified with the status command above after every run.

## 4. DEFECT (corpus index) — `corpus/README.md` is stale, four specifics

`corpus/README.md` is the coverage map Q02 (`corpus/QUALITY.md:12`) forces every entry to name, and its `## Index` enumerates what may live under `corpus/`. It has not been touched since round 66 (`git log --oneline -1 -- corpus/README.md` → `a4c712a`; `git diff --stat a4c712a..HEAD -- corpus/README.md` → empty), so it did not absorb round-68's two new paths either. Round-68's hygiene seat routed exactly this and it is still open.

- **4a** `corpus/README.md:9` says `admission criteria Q01–Q13 (Q11 supersedes Q08)`; `corpus/QUALITY.md` now carries Q14 (`:26`, round-68) and Q15 (`:27`, round-69). `grep -nE '^\| Q1[3-5] \|' corpus/QUALITY.md` → 3 rows. The index undercounts the admission bar by two rows, and this round's Q15 is the one the criterion registry was extended with.
- **4b** this round's new script is unnamed. The only script bullet is `corpus/README.md:17` — `` `verify_*.py` — saved-ledger replay verifiers (`--self-test`) `` — and `corpus/q15_tree_id_check.py` matches neither the glob nor the described role (it is a sentence checker over markdown, not a ledger replay).
- **4c** round-68's two additions are still unnamed: `grep -n 'snapshots\|derive_axml\|check_embedded' corpus/README.md` → no match, while `corpus/snapshots/ResourceTypes.h` (86,255 B) is the pinned spec snapshot the round-69 S047 row derives from and `corpus/check_embedded_outputs.py` is the registered C7 gate the claims name.
- **4d** the `knowledge/` bullet (`corpus/README.md:11-13`) describes only admitted entries plus `admission-status: rejected` candidates, but this round's file is `admission-status: candidate` — the only such header in the tree (`grep -l '^admission-status: candidate' corpus/knowledge/*.md` → 1 file). Read literally, a clean-flag flip would have to launder the candidate as "admitted".

**Exact fix** (append-only, touches no coverage status, so it cannot trip the claims' void condition "a README status change other than C05"):

```diff
-- `QUALITY.md` — admission criteria Q01–Q13 (Q11 supersedes Q08), each citing its mistake class.
+- `QUALITY.md` — admission criteria Q01–Q15 (Q11 supersedes Q08), each citing its mistake class.
 - `knowledge/` — admitted domain entries (the map below names each one); also
   retains clearly marked rejected candidates (each carries an
-  `admission-status: rejected` header), which are evidence, not admitted knowledge.
+  `admission-status: rejected` header) and `admission-status: candidate` entries
+  awaiting a wave gate, which are evidence, not admitted knowledge.
 - `lessons/` — `2026-10-12-r1-provider-gap.md`; `round-1.md` (fleet round-1 gates and the mined `## Mistakes` table); `round-1-verifier-spotcheck.md` (integrator-written outside check of round 1); `round-61.md` (round-61 gate, mistakes and source changes).
 - `fixtures/` — authored known-truth inputs (byte-oracle fixtures; `fixtures/REPLAY.md`).
 - `live/runs/` — saved REA outputs, receipts and non-author reviews per historical round.
 - `verify_*.py` — saved-ledger replay verifiers (`--self-test`); census command in `SCORECARD.md` (C).
+- `derive_axml_anchors.py` — machine derivation of the AXML anchors the C05 entries cite from `snapshots/` (exit 2 on a missing or ambiguous symbol).
+- `check_embedded_outputs.py` — C7 gate: re-runs every embedded command block and diffs its committed output (`--self-test`; `SELFTEST OK` on a clean tree).
+- `q15_tree_id_check.py` — Q15 checker (`--self-test`, `--scan <md> [--lane <path>]`): re-derives each `` `<hash>:corpus` = `<hash>` `` pair with `git rev-parse`; read-only.
+- `snapshots/` — pinned spec snapshots (`ResourceTypes.h`, AOSP android-15.0.0_r1) read by `derive_axml_anchors.py`.
```

The `lessons/` bullet (`:14`) is also stale by eight rounds (it names rounds 1 and 61 only; `ls corpus/lessons/` holds `round-61`…`round-68` plus six spot-checks). Generalizing it (“one `round-N.md` gate/mistakes record plus `round-N-verifier-spotcheck.md` per round from 61 on”) is the durable fix, but it is round-61-era debt, not this round's.

## 5. BLOCKER (operability, C2) — `Q15_FALSE_KILLED` is unreachable under the frozen invocation

The counter reads the D1 fixture from the measured tree:

```
reports/round-69/measure.py:161   d1 = TREE / "reports/round-69/d1-false-sentence.md"
reports/round-69/measure.py:162   if d1.is_file():
reports/round-69/measure.py:163-164   rc, last = run(TREE, "q15_tree_id_check.py", "--scan",
                                                  "reports/round-69/d1-false-sentence.md", "--lane", LANE)
reports/round-69/measure.py:165       q15_false_killed = rc != 0
reports/round-69/measure.py:167-169   else: … print("Q15_FALSE_KILLED=n/a (no d1 fixture)")
```

but the claims' invocation contract builds the tree from `corpus` alone (`claims.md` §Frozen counter: `git archive <commit> corpus | tar -x -C <tree>`). Reproduced at HEAD:

```
$ mkdir -p /tmp/revenger-r69-hyg/tree && git archive HEAD corpus | tar -x -C /tmp/revenger-r69-hyg/tree
$ ls -1 /tmp/revenger-r69-hyg/tree
corpus
$ test -f /tmp/revenger-r69-hyg/tree/reports/round-69/d1-false-sentence.md && echo PRESENT || echo ABSENT
ABSENT
```

So the after-run prints `Q15_FALSE_KILLED=n/a (no d1 fixture)`. C2's frozen predicate requires `Q15_FALSE_KILLED=yes` (`claims.md:131`, kill rule `:144-146`), so **C2 is falsified by the harness, not by the evidence**, however clean the work is. `Q15_SELFTEST` and `Q15_RESTATE_OK` are unaffected (the checker and the lesson both live under `corpus/`; verified: `python3 -B corpus/q15_tree_id_check.py --self-test` from the archived tree prints `Q15_SELFTEST=pass`, exit 0).

**Exact fix** (no counter edit — `measure.py`'s sha256 is pinned — and no claim edit): archive the fixture's directory too, and say so in the after-run receipt.

```sh
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive <final-tip> corpus reports/round-69 | tar -x -C <tree>
```

Verified end to end on the same commands the counter issues, from a tree built that way:

```
$ ls -1 /tmp/revenger-r69-hyg/tree2
corpus
reports
$ python3 -B corpus/q15_tree_id_check.py --self-test
Q15_SELFTEST=pass (true sentence verified; false sentence killed)      exit 0
$ python3 -B corpus/q15_tree_id_check.py --scan reports/round-69/d1-false-sentence.md --lane /home/vgpnk/…/revenger-shokunin
Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)      exit 1
```

which is exactly the `rc != 0` the counter maps to `Q15_FALSE_KILLED=yes`. While the lesson is still absent (`corpus/lessons/round-69.md` → `No such file or directory`), `Q15_RESTATE_OK=n/a` is correct and expected; the lesson must land in the same revision as the flip, as `claims.md` §Frontier step requires.

## 6. FINDING (calibration, non-blocking) — `Q15_FALSE_KILLED` does not separate "killed" from "did not demonstrate"

With the fixture present, `q15_tree_id_check.py` exits 1 for **both** outcomes, because `scan()` returns `False` when a false-sentence quote demonstrates the class (`corpus/q15_tree_id_check.py:103-105`, `restate_count == 0`) and also when it does not (`:99-101`, `not false_found_bad`). The counter's `rc != 0` therefore reads `yes` either way. Demonstrated with a quote whose pair actually resolves:

```
$ printf 'tree-identity false-sentence: `1c34603:corpus` = `ddc6a4f6…`\n' > /tmp/…/true-quote.md
$ python3 -B corpus/q15_tree_id_check.py --scan /tmp/…/true-quote.md
Q15_RESTATE_BAD: no false-sentence pair failed (quote does not demonstrate the class)   exit 1
$ python3 -B corpus/q15_tree_id_check.py --scan reports/round-69/d1-false-sentence.md
Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)                      exit 1
```

Same class as the D5 C7-gameability item: a label satisfiable by a non-demonstration. It cannot be repaired here (`measure.py` frozen; editing `q15_tree_id_check.py` would change the checker the counter runs mid-round). Route it forward: the after-run receipt and adjudication must quote the checker's own stdout line (`Q15_FALSE_KILLED: …` vs `Q15_RESTATE_BAD: …`), and the round-70 counter should key on the `Q15_FALSE_KILLED:` prefix rather than the exit code.

## 7. FINDING (claims versus receipt) — the C2 red-before prose contradicts its own receipt

`reports/round-69/claims.md:137-140` reads: "**Red-before (committed history).** On the base tree: `Q15_PRESENT=no` … `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes` (the checker ships with the claims revision and the D1 fixture is committed as evidence of the defect class)." The committed red-before receipt says otherwise, because the checker and fixture post-date `222a7a7`:

```
$ grep -n Q15 reports/round-69/measure-before.log
22:Q15_PRESENT=no
23:Q15_SELFTEST=n/a (no checker)
24:Q15_FALSE_KILLED=n/a (no checker)
25:Q15_RESTATE_OK=n/a (no checker)
```

Both labels are `n/a` on the base tree; the parenthetical describes the claims/build revision, and the sentence it is appended to says "on the base tree". This is the Q15/M48 class in the round's own declaration. `claims.md` is frozen, so do not edit it: record the erratum in the round-69 lesson's `## Mistakes` (class "control description stated from intent, contradicted by the committed receipt"), cite `measure-before.log:23-24`, and let the adjudication rest on the receipt.

`corpus/QUALITY.md:27` also cites `M48 (lessons/round-69.md)`, a file that does not exist at this tree. That is a legitimate build-state dangling pointer (the lesson is written at adjudication) and it is what `Q15_RESTATE_OK` forces; no action now, but the row is unbacked until the lesson lands.

## 8. Verified clean (no action)

- `git diff --stat 222a7a7..HEAD -- corpus/fixtures/ corpus/live/` → empty: the round-65 fixture bytes and every saved run are untouched, satisfying the void condition on changed fixture/live bytes.
- prior rejected candidates keep every byte: `round-65` blob `d68e21b2…`, `round-67` `be6de1b1…`, `round-68` `8b95fd13…` identical at `222a7a7` and `HEAD` (`git rev-parse <c>:<path>`).
- the new entry's own pins re-derive: `sha256sum corpus/derive_axml_anchors.py` = `74d4c0d9…4b2a83aa` (stated S047), `corpus/snapshots/ResourceTypes.h` = `56b88bc4…8957c56f` (stated S047, and identical to `.ufo/waves/round-65/source-snapshots/ResourceTypes.h`), `corpus/fixtures/apk-r65/{fixture.apk,truth.json,generator.py,readout.py}` = `05d2280f…`, `27303bae…`, `eaa9444c…`, `92e347c3…`, exactly the four values quoted in the entry's S041 line.
- every path the new entry references resolves (`corpus/derive_axml_anchors.py`, `corpus/snapshots/ResourceTypes.h`, the four `fixtures/apk-r65` members, `corpus/README.md`, `corpus/lessons/round-68.md`, `reports/round-69/claims.md`, three `.ufo/waves/round-6{5,7}/source-snapshots/*`) — 12/12 exist.
- `grep -cE '^\| C[0-9]+ ' corpus/README.md` = 14: the denominator the claims freeze is intact.
- `corpus/QUALITY.md:27` Q15 row present and matched by the counter's `^\| Q15 \|` regex (`measure.py:153`).
- the Q15 checker is read-only (docstring `corpus/q15_tree_id_check.py:27`, and `--self-test`/`--scan` write nothing: `git status --porcelain corpus/` empty afterwards).

## Blocker

Section 5 is the one that needs a decision before the after-run: with `corpus`-only archiving, C2 cannot read `yes` and dies on a path, one line of `<tree>` construction away from correct. Section 4's fix is safe to land in the same revision (no coverage status touched).
