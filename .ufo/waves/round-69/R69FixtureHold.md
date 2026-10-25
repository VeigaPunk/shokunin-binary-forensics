# R69FixtureHold — fixture and live byte hold (round-69)

HOLD-INTACT — `222a7a7..refs/heads/main` moves **zero** bytes under `corpus/live` and `corpus/fixtures`; the five changed corpus paths are build/calibration artifacts only, and the C05 row is still `uncovered` (README unflipped) as the build state requires.

Seat: leaf, read-only. Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Judged at lane tip `refs/heads/main` = `35e12584d37434632fa06a6c2975ab55f29a8d3f`.

## 1. Primary predicate (binding)

Command and actual output:

```
$ git -C /home/vgpnk/Projects/shokunin/revenger-shokunin diff --stat \
    222a7a702529fb60598633ebdf5e1442007bc15d refs/heads/main -- corpus/live corpus/fixtures
EXIT=0            # no output lines at all
```

Byte-level corroboration (stronger than the diff, since it compares content ids not mtimes):

```
$ git rev-parse 222a7a7:corpus/live      -> 74376f31ebae44d94ca904c3850bae4383496d5e
$ git rev-parse main:corpus/live         -> 74376f31ebae44d94ca904c3850bae4383496d5e
$ git rev-parse 222a7a7:corpus/fixtures  -> 865a4e8e9b03ad32df41f98f441bd63230c21c2d
$ git rev-parse main:corpus/fixtures     -> 865a4e8e9b03ad32df41f98f441bd63230c21c2d

$ git ls-tree -r 222a7a7 corpus/live     | sha256sum -> 9794d5f39f30911138ae38ddce272a6cab776c913a0201e1d2434029e6218009
$ git ls-tree -r main     corpus/live     | sha256sum -> 9794d5f39f30911138ae38ddce272a6cab776c913a0201e1d2434029e6218009
$ git ls-tree -r 222a7a7 corpus/fixtures | sha256sum -> c35948b80e2b900cad07d8959ab0a9839e4f80c7b356e205def7c0260ad08cfd
$ git ls-tree -r main     corpus/fixtures | sha256sum -> c35948b80e2b900cad07d8959ab0a9839e4f80c7b356e205def7c0260ad08cfd
```

Hold is non-vacuous: `corpus/live` has 351 tracked files, `corpus/fixtures` has 105 (`git ls-tree -r 222a7a7 corpus/live | wc -l` → 351; `… corpus/fixtures` → 105). Every blob id in both subtrees is identical at both ends.

Per-commit check (no transient touch that a later commit reverted — the endpoint diff alone would hide that):

```
$ git log --oneline --name-status 222a7a7..refs/heads/main -- corpus/live corpus/fixtures
(end)                       # three commits, zero live/fixture names
```

Worktree drift (uncommitted or dropped files under those paths):

```
$ git status --porcelain -- corpus                        -> (empty)
$ git status --porcelain --ignored -- corpus/live corpus/fixtures -> (empty)
```

Only untracked path in the whole lane is `?? .ufo/waves/round-69/assimilation/` (wave scratch, not corpus).

Fixture bytes still equal the values the entry and S041 claim (freshness spot-check, SHA-256 on the lane worktree):

```
05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  corpus/fixtures/apk-r65/fixture.apk
27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  corpus/fixtures/apk-r65/truth.json
eaa9444c5e437c4e2deb68282da6c8a8d5e3555cdbf059544d8a195930c27c1a  corpus/fixtures/apk-r65/generator.py
92e347c35e39c4dba2b05763e0e32af46ff7a66af852b2ab019618eef8c13976  corpus/fixtures/apk-r65/readout.py
```

Identical to the S041 anchors in `corpus/knowledge/round-69-apk-axml-byte-evidence.md` (source line `S041`), and `git show 222a7a7:…fixture.apk | sha256sum` = `git show main:…fixture.apk | sha256sum` = `05d2280f…`.

## 2. Every changed/added path under `corpus` (full diffstat)

```
$ git diff --shortstat 222a7a7 refs/heads/main -- corpus
 5 files changed, 389 insertions(+), 9 deletions(-)

$ git diff --numstat 222a7a7 refs/heads/main -- corpus
1       0       corpus/QUALITY.md
2       0       corpus/SOURCES.md
42      9       corpus/derive_axml_anchors.py
215     0       corpus/knowledge/round-69-apk-axml-byte-evidence.md
129     0       corpus/q15_tree_id_check.py
```

| status | path | one-line reason |
|---|---|---|
| M | `corpus/QUALITY.md` | +1 row `Q15` (stated git object id / tree identity must be re-derived with the command that names it) — the C2 calibration criterion; no existing row edited. |
| M | `corpus/SOURCES.md` | +2 lines: registry row `S047` (own-work, tier A, supersedes `S046`) and its round-69 opening-log line; the C1 source row. |
| M | `corpus/derive_axml_anchors.py` | round-69 extension (+42/−9): `RES_XML_FIRST_CHUNK_TYPE`, `enum_block_bounds()` (:237 open / :263 close, found by `RES_NULL_TYPE` membership), `VALUE_RE` enum values — the 20-line derivation the v4 entry embeds; file mode also flips `100644 → 100755`. |
| A | `corpus/knowledge/round-69-apk-axml-byte-evidence.md` | the C05 fourth-pass candidate (215 lines), `admission-status: candidate` at `:11`; no live/fixture byte is part of it. |
| A | `corpus/q15_tree_id_check.py` | the Q15 checker (129 lines), `--self-test` / `--scan <file>`; read-only (`grep -n "open(\|write_text\|\.write(" → no matches`). |

Nothing deleted (`--name-status` shows no `D`), nothing renamed, and `corpus/README.md` is **not** in the range:

```
$ git diff --name-only 222a7a7 refs/heads/main -- corpus/README.md   -> (empty)
$ grep -n C05 corpus/README.md:34  -> | C05 | Android packages (APK) | — | … | uncovered |
```

So the build-state requirement “README not flipped” holds: C05 is still `uncovered` at the lane tip.

## 3. Findings (adjacent to this seat; all evidenced)

### F1 — MEDIUM — the frozen claims assert a counter pin that `measure-before.log` does not contain (D1/M46 class recurring in this round's own text)
`reports/round-69/claims.md:166-167` reads: “The counter's sha256 is pinned above and in `measure-before.log`”. The named artifact does not carry it:

```
$ grep -c 'sha256'    reports/round-69/measure-before.log -> 0
$ grep -c 'measure.py' reports/round-69/measure-before.log -> 0
$ wc -l reports/round-69/measure-before.log -> 105
```

The pin value itself is honest — `sha256sum reports/round-69/measure.py` = `bca74e6d8b5010aee79886521474f072257ee22ec7ccc24e4186666bdc048377`, exactly the value at `claims.md:11-12`. The defect is the *locator*: a stated provenance claim contradicted by the file it names. This is precisely the class Q15 was created for, appearing in the claims revision, and Q15 does not catch it (§F2/F3).

### F2 — MEDIUM — Q15's ability-to-fail is demonstrated on a hand-normalized line, not on the D1 sentence
The checker's pattern is `PAIR = re.compile(r"`([0-9a-f]{7,40}):corpus`\s*=\s*`([0-9a-f]{40})`")` and `scan()` only inspects lines whose stripped text begins `tree-identity restatement:` or `tree-identity false-sentence:` (`corpus/q15_tree_id_check.py:29,95-104`). The committed D1 fixture says so itself — `reports/round-69/d1-false-sentence.md:14`: “Normalized to the checker's pair syntax:”. The real D1 sentence is prose (`reports/round-68/measure-after.log:102`: “…its corpus/ tree is byte-identical to the earlier measured 14774a2c tree — 51894d15… — and to the receipt commit's…”), and Q15 run over the round-68 lesson that discusses it:

```
$ python3 -B corpus/q15_tree_id_check.py --scan corpus/lessons/round-68.md
Q15_RESTATE_BAD: no false-sentence pair failed (quote does not demonstrate the class)
EXIT=1
```

So claims.md §C2’s “the criterion is shown able to fail on the D1 sentence” is true only of the normalized stand-in; the detector has no reach over prose identity sentences. Fixture facts are otherwise correct — re-derived: `1c34603:corpus → ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`, `dddf147:corpus → 51894d153a6e69487da2a273680d014abd240f61`, `14774a2c:corpus → 51894d153a6e69487da2a273680d014abd240f61`.

### F3 — LOW/MEDIUM — `scan()` conflates “clean file” with “not killed”, so Q15 cannot gate arbitrary corpus docs
A file containing no pair at all exits 1 with `Q15_RESTATE_BAD: no false-sentence pair failed` (observed on `corpus/lessons/round-68.md` and on `reports/round-69/claims.md` above). Q15 therefore only evaluates a file that already plants both a restatement and a false sentence; it cannot be applied as a general criterion over lessons/README/claims — which bounds its calibration reach beyond the single planted pair.

Positive control (verified first-hand, so the legs are live even though the receipt does not record them):
```
$ python3 -B corpus/q15_tree_id_check.py --self-test
Q15_SELFTEST=pass (true sentence verified; false sentence killed)      EXIT=0
$ python3 -B corpus/q15_tree_id_check.py --scan reports/round-69/d1-false-sentence.md
Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)     EXIT=1
```

### F4 — LOW — §C2 attributes `Q15_SELFTEST=pass` / `Q15_FALSE_KILLED=yes` to the committed red-before record, which records `n/a`
`reports/round-69/measure-before.log:24-27`:
```
Q15_PRESENT=no
Q15_SELFTEST=n/a (no checker)
Q15_FALSE_KILLED=n/a (no checker)
Q15_RESTATE_OK=n/a (no checker)
```
The claims (`claims.md` §C2 “Red-before”) list `pass` / `yes` as part of that record, explained as “the checker ships with the claims revision”. Defensible on the base tree `222a7a7`, but the receipt the claims point at does not carry those legs; only §F3's re-run (this seat) substantiates them, and that run is not committed.

### F5 — NOTE — `Q15_RESTATE_OK` cannot be `yes` at the current tip
`git cat-file -e refs/heads/main:corpus/lessons/round-69.md` → `fatal: path … does not exist` (lessons dir ends at `round-68-verifier-spotcheck.md`). C2's predicate is “over the final measured tree”, so this is expected at build time, but the lesson (with its `tree-identity restatement:` pair) must land before the final measurement or C2 reads FALSIFIED.

## 4. Residual risk / verification gaps

- Verdict is pinned to `refs/heads/main = 35e1258` at check time; any later commit could move the hold, so it must be re-run at the final measured tip.
- I did not run the counter (`reports/round-69/measure.py`) — that is the counter-replay seat's scope; the fixture bytes it would read are proved unchanged here, so its `HOLDS_C2_V4`/`C05_SINGLE_V4` legs cannot be perturbed by live/fixture drift.
- No `lsp` server was used: this seat's questions are git-object questions, and the semantic-resolve fallback was `git rev-parse` (a resolver, not grep) plus direct file reads.
- `corpus/derive_axml_anchors.py` mode flip `100644 → 100755` is inside the allowed build change set but is an unremarked bit of the diff; harmless for the hold.

## 5. Tooling record

No installs or upgrades; existing `git`, `sha256sum`, `python3` only. Host-wide pacman pause respected.
