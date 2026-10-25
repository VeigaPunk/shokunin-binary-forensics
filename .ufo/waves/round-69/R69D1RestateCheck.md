RESTATEMENT-SPECIFIED — the D1 sentence is reproducible and its correction is fully determined: the restatement pairs `1c34603:corpus`=`ddc6a4f6…`, `14774a2c:corpus`=`51894d15…`, `dddf147:corpus`=`51894d15…` all resolve under `git rev-parse`, the quoted false pair `1c34603:corpus`=`51894d15…` fails, and `corpus/q15_tree_id_check.py` parses both forms — but the lesson MUST carry both lines (a restatement-only lesson exits 1), and the checker has a vacuous-pass hole on the restatement line.

Seat: L1Revenger69.R69D1RestateCheck · lane /home/vgpnk/Projects/shokunin/revenger-shokunin · 2026-10-25
Scope: read-only re-derivation (no lane edit, no git mutation; scratch under /tmp/revenger-r69-d1restate, deleted).

## 1. Re-derivation (the naming command, verbatim)

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse 1c34603:corpus
ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin rev-parse dddf147:corpus
51894d153a6e69487da2a273680d014abd240f61
```

Full identities (exit=0 each):

| rev | resolved |
|---|---|
| `14774a2c:corpus` | `51894d153a6e69487da2a273680d014abd240f61` |
| `dddf147:corpus` | `51894d153a6e69487da2a273680d014abd240f61` |
| `1c34603:corpus` | `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7` |
| `1c34603` | `1c3460336d14e9bbe64778f826a07bdd996ce39b` |
| `dddf147` | `dddf1479ad7ba4e4124b02c0a0e32edf399e4c95` |
| `14774a2c` | `14774a2c3cd3918364f211e08009f9f327b4c7b3` |

Ancestry (`git merge-base --is-ancestor`): `14774a2c` → `dddf147` → `1c34603`, linear. `14774a2c:corpus` and `dddf147:corpus` are the SAME tree; `1c34603:corpus` differs.

**The falsehood is substantive, not a label slip.** `git diff --stat 14774a2c 1c34603 -- corpus/`:
```
 corpus/lessons/round-68.md | 7 ++++---
 1 file changed, 4 insertions(+), 3 deletions(-)
```
`diff -rq` over the two archived trees reports exactly one differing file, `corpus/lessons/round-68.md`. So `reports/round-68/measure-after.log:102` ("its corpus/ tree is byte-identical to the earlier measured 14774a2c tree — 51894d15… — and to the receipt commit's") is false on the tree-identity clause: `1c34603`'s corpus is `ddc6a4f6…`, and it is NOT byte-identical to either of the two trees it names.

**What IS true, and must survive into the restatement.** I ran the pinned round-68 counter on both archived trees (read-only):
```
git archive 14774a2c corpus | tar -x -C /tmp/.../t14774a2c   → counter exit=0
git archive 1c34603  corpus | tar -x -C /tmp/.../t1c34603    → counter exit=0
diff out-14774a2c.txt out-1c34603.txt → exit 0, 0 diff lines
```
Counter stdout is byte-identical across the two trees (the `determinism:` clause at `measure-after.log:110` holds); the trees are not identical. The correct sentence therefore separates *stdout identity* from *tree identity* instead of asserting the latter.

## 2. The two sentences the round-69 lesson must carry

Required form (both lines, in `corpus/lessons/round-69.md`):

```text
tree-identity false-sentence: `1c34603:corpus` = `51894d153a6e69487da2a273680d014abd240f61`
tree-identity restatement: `1c34603:corpus` = `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`; `14774a2c:corpus` = `51894d153a6e69487da2a273680d014abd240f61`; `dddf147:corpus` = `51894d153a6e69487da2a273680d014abd240f61`
```

- **Quoted false sentence** (pairs that fail): the D1 claim normalized to checker syntax, `1c34603:corpus` = `51894d15…`. Verified failure: resolves to `ddc6a4f6…`.
- **Restatement** (pairs that resolve): `1c34603:corpus` = `ddc6a4f6…` — the correction commit's corpus tree; `14774a2c:corpus` = `dddf147:corpus` = `51894d15…` — the measured/adjudicated tree and the receipt commit's tree are the same tree. Prose must state that the corpus trees differ by exactly `corpus/lessons/round-68.md` and that the counter **stdout** is byte-identical.

Do NOT put the false pair on the restatement line (see §4 probe C), and do not write the restatement as `1c34603:corpus` = `51894d15…` with a caveat — the checker reads the pair, not the caveat.

## 3. Checker parses both forms — confirmed by execution

Checker: `corpus/q15_tree_id_check.py` sha256 `7d074f98cb7f9ff2be4c17e6b97e60ac8d660c827a32009d85a35df50639d276`.
Parser: `PAIR = re.compile(r"`([0-9a-f]{7,40}):corpus`\s*=\s*`([0-9a-f]{40})`")` (`:33`), line dispatch on `tree-identity restatement:` / `tree-identity false-sentence:` (`scan()`, `:89-107`).

```
$ python3 -B corpus/q15_tree_id_check.py --self-test
Q15_SELFTEST=pass (true sentence verified; false sentence killed)      exit=0
$ python3 -B corpus/q15_tree_id_check.py --scan reports/round-69/d1-false-sentence.md \
      --lane /home/vgpnk/Projects/shokunin/revenger-shokunin
Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)     exit=1
```
The committed fixture (`reports/round-69/d1-false-sentence.md`, sha256 `637278b2a3bec105f967892155f06779658cb3ca833ab2516c63076b06da2466`) therefore ships the false line in the exact form the lesson must quote. Counter hook: `reports/round-69/measure.py:163-166` (`Q15_FALSE_KILLED = rc != 0`), `:172-175` (`Q15_RESTATE_OK = rc == 0`), `--lane LANE` passed explicitly so the archived-tree scan still resolves against the lane object store (`LANE` = `:30`).

## 4. Probe matrix (actual output, scratch files in /tmp)

| probe | content | exit | last line |
|---|---|---|---|
| A | required dual-line form above | **0** | `Q15_RESTATE_OK=yes (every restatement pair re-derived; false-sentence pair killed)` |
| B | restatement line only, no false-sentence line | 1 | `Q15_RESTATE_BAD: no false-sentence pair failed` |
| C | restatement carries the false pair + false line | 1 | `Q15_RESTATE_BAD line 1: ... claimed 51894d15... resolved ddc6a4f6...` |
| D | `tree-identity restatement:` written as prose (`git rev-parse 1c34603:corpus` …), + false line | **0** | `Q15_RESTATE_OK=yes` ← **vacuous pass** |
| E | d1 false line only | 1 | `Q15_FALSE_KILLED: all false-sentence pairs failed` |
| F | restatement with full 40-char rev `1c3460336…:corpus` | 0 | `Q15_RESTATE_OK=yes` (PAIR accepts 7–40 hex) |
| G | restatement names `deadbeef:corpus` | 1 | `Q15_RESTATE_BAD ... resolved None` |
| J | bare `tree-identity restatement:` (zero pairs) + false line | **0** | `Q15_RESTATE_OK=yes` ← **vacuous pass** |
| H | false line in prose (no parsable pair) | 1 | `Q15_RESTATE_BAD: no false-sentence pair failed` |
| I | false line whose pair actually resolves | 1 | `Q15_RESTATE_BAD: no false-sentence pair failed` |

Conclusion: both required forms parse and the specified pair assignments are correct (A is green, C is red). **B is the trap for the scribe seat**: a lesson that only restates (the natural reading of C2's wording) fails, because `scan()` demands both a clean restatement line *and* at least one failing false-sentence pair in the same file (`:104-112`).

## 5. Findings

**F1 (medium, calibration instrument — vacuous pass).** `scan()` increments `restate_count` on the prefix alone and never requires ≥1 *parsable* pair on a restatement line; with zero pairs `ok=[] bad=[]`, so probe D and probe J both score `Q15_RESTATE_OK=yes`. The mechanical gate is weaker than the Q15 criterion text (`QUALITY.md:27` requires re-derivation with the command that names it). A lesson can satisfy `Q15_RESTATE_OK=yes` without any re-derivation at all on the restatement line. Fix (not made, read-only seat): fail when a `tree-identity restatement:` line yields `len(ok_pairs)==0`. Note this is the same gameability class as D5, which claims.md explicitly leaves open and non-pre-empted — so it does not void C2 as written, but it means `Q15_RESTATE_OK=yes` alone is not proof the sentence was re-derived.

**F2 (low-medium, label specificity).** `measure.py:165` sets `Q15_FALSE_KILLED` from `rc != 0` only, so a *malformed* fixture (probes H, I: no failing pair at all) also earns `Q15_FALSE_KILLED=yes`, with the diagnostic reason visible only in the truncated `::` tail. The "ability-to-fail receipt" is therefore satisfied by fail-open as well as by correct killing. The committed fixture happens to be correct (§3), so the label is true today, but the label does not entail it.

**F3 (medium, spec/checker mismatch the lesson must know).** claims.md C2 states only that "the lesson's restated tree-identity sentence re-derives"; it never says the lesson must also quote the false sentence. Per §4 probe B, restatement-only ⇒ exit 1 ⇒ `Q15_RESTATE_OK=no` ⇒ C2 FALSIFIED under the frozen kill rule. The dual-line requirement is discoverable only by reading `scan()`. This must be honoured by the scribe seat and is worth stating in the lesson (and in any later QUALITY wording), not left implicit.

**F4 (informational, content precision).** The falsehood is a real byte difference (`corpus/lessons/round-68.md`, +4/−3), not just a mis-copied hash; a restatement that merely swaps in `ddc6a4f6…` without recording that the *counter stdout* is byte-identical (verified: diff exit 0) loses the true half of the round-68 claim and invites the opposite overclaim.

Nothing here voids C2's frozen predicate: `Q15_PRESENT=yes` is already real (`corpus/QUALITY.md:27`), `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes` are reproducible, and `Q15_RESTATE_OK` is currently `n/a` because `corpus/lessons/round-69.md` does not exist yet — consistent with the committed red-before state.

## 6. Residual risk / verification gaps

- `Q15_RESTATE_OK` is unverified green until the lesson exists; this seat cannot pre-score it without writing the lesson (out of scope: read-only).
- The checker resolves against the live lane object store at measurement time (`--lane LANE`), not against the archived tree; if the lane's objects are repacked/pruned between archive and measurement, resolution could change. Not exercised here — objects are present and resolving.
- Object-id short forms could become ambiguous if the lane grows colliding 7-char prefixes; `rev-parse` would then error and the pair would read as failing. Not observed (all three short revs resolve uniquely today).
- I did not audit the counter's other labels; `reports/round-69/measure.py` sha256 `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377` matches claims.md and is untouched by me.

## 7. Scope, tooling, cleanliness

- Wrote exactly one file: this report. No edit to `corpus/`, `reports/`, README, or any other wave artifact; no git/jj mutation; no subagents; no agent://all traffic.
- Tool installs: none needed (python3 stdlib + git only). No pacman/uv/npx action.
- Scratch `/tmp/revenger-r69-d1restate` (11 probe files, 2 archived trees, 3 counter outputs) deleted before return.
