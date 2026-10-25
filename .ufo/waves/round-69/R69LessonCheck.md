# R69LessonCheck — round-69 lesson / mistake-class requirements

**REQUIREMENTS-STATE** — `corpus/lessons/round-69.md` does not exist, and two committed
forward references (`corpus/QUALITY.md:27` → M48, `corpus/knowledge/round-69-apk-axml-byte-evidence.md:153`
→ M49) already bind what it must contain; every requirement below is derived from committed bytes,
and two of my probes show the Q15 legs are satisfiable vacuously unless the lesson is written with
the constraints in §3.

lane: revenger · lane repo `/home/vgpnk/Projects/shokunin/revenger-shokunin` · tip
`35e1258` (`round-69: wave preparation …`) · read-only; **nothing edited** except this report.

## 1 · Axes

| axis | how this seat touches it |
|---|---|
| **calibration** (primary) | C2's Q15 criterion + the two mistake rows that give it provenance; found one live M48-class instance *inside the round's own pre-registration* (§5 F1) |
| coverage (adjacent) | M49's evidence is the C1 claim surface (v4 entry + S047 + derivation); the lesson's census block is the frontier-step obligation in `reports/round-69/claims.md:227-231` |

## 2 · Tree state (what exists, what does not)

```
$ ls corpus/lessons/round-69.md corpus/knowledge/round-69*
ls: cannot access 'corpus/lessons/round-69.md': No such file or directory
corpus/knowledge/round-69-apk-axml-byte-evidence.md

$ git cat-file -e 35e1258:corpus/lessons/round-69.md
fatal: path 'corpus/lessons/round-69.md' does not exist in '35e1258'
```

So the lesson is a **required deliverable of this round that has not landed**; the counter already
encodes it: `reports/round-69/measure.py:170-178` prints
`Q15_RESTATE_OK=n/a (no round-69 lesson)`, and the base receipt confirms it
(`reports/round-69/measure-before.log:25`).

Committed references that make the lesson's content non-optional:

| pointer | text (abridged) | consequence |
|---|---|---|
| `corpus/QUALITY.md:27` | `\| Q15 \| … \| M48 (lessons/round-69.md) \|` | M48 must exist in the lesson or the criterion's origin dangles |
| `corpus/knowledge/round-69-apk-axml-byte-evidence.md:153` | "…the enum-block bound at :263 is what the round-68 v3 candidate's "237-253" range statement missed (**M49**)" | M49 must exist, or the C1 entry carries a dangling pointer |
| `corpus/SOURCES.md:92` | "…the v4 candidate's load-bearing spec anchors and enum values (the M40/M44 and **M49** classes)…" | a second M49 forward reference |

Lesson structure obligations, from the fleet docs (read-only):
`LEARNING.md:69-72` — every `corpus/lessons/round-<N>.md` carries `## Gate`; a round that mines
mistakes adds `## Mistakes`. `CORPUS.md:171-178` — one row per mistake, columns
**class · evidence pointer · captured-by · fix**, class drawn from the nine-term vocabulary at
`.ufo/waves/kaika-w1/mistakes.md:448` (`vacuous`, `survivor`, `stale-premise`, `reference-drift`,
`number-drift`, `scope`, `attribution`, `landing`, `provider`).
`CORPUS.md:180-184` — a fix counts only with a committed red-before in which **the same command
exits non-clean for the named reason**, the fix as the only delta.

## 3 · Mistake classes round 69 should mine

Both candidates are **required**, in this order.

### M48 — identity-sentence-without-re-derivation (primary; class token `attribution`)

Row fields the lesson must carry, each resolvable:

- **class** — `attribution` (from the nine-term vocabulary): a tree identity attributed to an
  object that does not carry it. (`number-drift` is the weaker fit; M47 already owns that token at
  prose level for r68.)
- **evidence pointer** — `reports/round-68/measure-after.log:102` (the false sentence, ≤25-word
  located quote) **plus** the commands that contradict it and their actual output. Re-derived by
  this seat, verbatim:

```
$ git rev-parse 1c34603:corpus   → ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7
$ git rev-parse 14774a2c:corpus  → 51894d153a6e69487da2a273680d014abd240f61
$ git rev-parse dddf147:corpus   → 51894d153a6e69487da2a273680d014abd240f61
$ git diff --name-only 14774a2c 1c34603 -- corpus/
corpus/lessons/round-68.md
```

  The D1 sentence claims the `1c34603` tree is `51894d15…`; it resolves to `ddc6a4f6…`. The diff
  shows the honest restatement's content: **only `corpus/lessons/round-68.md` differs between the
  two measured trees** (this is the exact fix wording at
  `corpus/lessons/round-68-verifier-spotcheck.md:175`).
  Second pointer for the row: `reports/round-69/d1-false-sentence.md` (the committed normalized
  pair fixture).
- **captured-by** — `none` at the time (no QUALITY criterion covered tree ids; r68's Q14 stops at
  hex byte counts — `corpus/QUALITY.md:26`); the detector is the non-lane closure
  `corpus/lessons/round-68-verifier-spotcheck.md:168` (R68-D1, medium). Do **not** write `Q15` here
  as if it predated the defect — Q15 is this round's fix, not the catcher.
- **fix, shown able to fail** — Q15 (`corpus/QUALITY.md:27`) + `corpus/q15_tree_id_check.py`.
  The ability-to-fail receipt is the red-before → target pair on the same command:
  `Q15_FALSE_KILLED=n/a (no checker)` (`reports/round-69/measure-before.log:24`) → target `yes`;
  run directly, the D1 fixture is killed:

```
$ python3 -B corpus/q15_tree_id_check.py --scan reports/round-69/d1-false-sentence.md --lane /home/vgpnk/Projects/shokunin/revenger-shokunin
Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)      # exit 1
$ python3 -B corpus/q15_tree_id_check.py --self-test
Q15_SELFTEST=pass (true sentence verified; false sentence killed)       # exit 0
```

- **second instance the lesson should also carry** (found by this seat, same class, inside the
  round's own frozen text) — `reports/round-69/claims.md:137-140` says "On the base tree:
  … `Q15_SELFTEST=pass` and `Q15_FALSE_KILLED=yes`", while the base-tree receipt it names prints
  `n/a (no checker)` at `reports/round-69/measure-before.log:23-24`. Both values are true at the
  claims revision `e1d22ca` (verified on that archived tree: self-test exit 0; D1 scan exit 1) and
  false at the base tree. This is the M48 class applied to the criterion that exists to catch it.
  Record it as a second evidence pointer/instance line; **do not edit claims** (frozen).

### M49 — enum-block-bound number-drift (secondary; class token `number-drift`)

- **class** — `number-drift`.
- **evidence pointer** — `corpus/knowledge/round-68-apk-axml-byte-evidence.md:57`, `:148`, `:157`
  state the chunk-type enum block "lines 237-253"; the block closes at 263. Grounds:
  `corpus/snapshots/ResourceTypes.h:237` = `enum {`, `:263` = `};`; the derivation prints both
  bounds (`corpus/derive_axml_anchors.py`, sha256
  `74d4c0d94c6955d4c707afba7ca1b804dccae58170ba44caa98a1ab24b2a83aa`, 20 stdout lines, exit 0):

```
$ python3 -B corpus/derive_axml_anchors.py | grep -nE 'enum block|FIRST_CHUNK'
9:enum block open : 237
12:enum RES_XML_FIRST_CHUNK_TYPE : 244 = 0x0100
18:enum block close : 263
```

  The repaired surface: `corpus/knowledge/round-69-apk-axml-byte-evidence.md:59`, `:153` and the
  re-embedded block `:139`/`:148`.
- **captured-by** — `Q11`/`Q04` (`corpus/QUALITY.md:22-25`), exercised by the round-68 wave seats
  `R68ReviewEntryQ11` and `R68ReviewEntryQ04` (named at
  `corpus/knowledge/round-68-apk-axml-byte-evidence.md:9`), on the M40/M44 lineage.
- **fix, shown able to fail** — S047 (`corpus/SOURCES.md:61`) + the extended derivation. A
  one-command differential, run by this seat, that exits non-clean on the v3 entry and clean on the
  v4 entry (same command, entry as the only delta):

```
$ python3 -B - <<'PY'   # enumerate `enum block ... lines N-M` claims, compare to the derivation
… stated ranges per file vs derived (237,263) …
corpus/knowledge/round-68-apk-axml-byte-evidence.md: stated [(237, 253)] derived (237,263) -> FAIL exit 1
corpus/knowledge/round-69-apk-axml-byte-evidence.md: stated [(237, 263)] derived (237,263) -> PASS exit 0
```

**No third class is warranted.** The other r69-eligible candidates are already owned: M46
(`corpus/lessons/round-68.md:96`, registry drift) and M47 (`:97`, prose number-drift) were mined
last round, and the enum-bound defect above is their *instance* (hence M49, not a new criterion).

## 4 · The two tree-identity lines — exact parser contract

`corpus/q15_tree_id_check.py` is the arbiter (`Q15_RESTATE_OK`). Its rules, read from the source
and confirmed by probing:

1. Lines are matched only when `line.lstrip()` starts with the literal prefix
   `tree-identity restatement:` or `tree-identity false-sentence:` (`scan()`, lines 101-110).
   Prose-only statements are ignored → a lesson that states the ids in prose fails
   (**probed**: exit 1, `Q15_FALSE_KILLED: all false-sentence pairs failed`).
2. Pairs must be backticked with the exact shape `` `SHORT:corpus` = `FULL40HEX` `` —
   `PAIR` regex line 28, lowercase hex, `SHORT` = 7–40, RHS exactly 40.
3. **At least one** `tree-identity restatement:` line is required (`restate_count == 0` → exit 1).
4. **Every** restatement pair is resolved with `git -C <lane> rev-parse <short>:corpus`; any
   mismatch → exit 1.
5. **At least one** `tree-identity false-sentence:` pair must fail (no failing pair → exit 1).

Verified template shape (this exact file scanned clean, exit 0):

```
tree-identity restatement: `14774a2c:corpus` = `51894d153a6e69487da2a273680d014abd240f61`; `dddf147:corpus` = `51894d153a6e69487da2a273680d014abd240f61`; `1c34603:corpus` = `ddc6a4f6aea51ef34e0b7669832ff1a9cb2023f7`; only `corpus/lessons/round-68.md` differs between the first and third.
tree-identity false-sentence: `1c34603:corpus` = `51894d153a6e69487da2a273680d014abd240f61`
```

Three constraints the template encodes, each earned by a probe:

- the restatement must cite **commits that exist and predate the lesson commit** — a commit cannot
  contain its own hash, so never cite the lesson commit's tree id; `222a7a7:corpus` =
  `2c45edaf870fa0b35936114f34a51767dba67ed3` and `35e1258:corpus` =
  `7aeabf218889dee89036de808573aacf11bd6e69` are optional stable extras;
- the restatement line must contain **at least two resolvable pairs** — see §5 F3, a
  restatement line with zero parsable pairs passes vacuously;
- the false-sentence pair must name a commit that **exists and resolves to a different id**
  (`1c34603` → `ddc6a4f6…` vs claimed `51894d15…`) — see §5 F3, an absent commit also passes.

## 5 · Findings

**F1 (MEDIUM, calibration) — the round's own pre-registration contains an M48-class sentence.**
`reports/round-69/claims.md:137-140` presents `Q15_SELFTEST=pass` / `Q15_FALSE_KILLED=yes` as
base-tree states; the base receipt for the same tree prints
`Q15_SELFTEST=n/a (no checker)` / `Q15_FALSE_KILLED=n/a (no checker)`
(`reports/round-69/measure-before.log:23-24`). Re-derived on the claims revision
(`git archive e1d22ca corpus reports/round-69`): self-test exit 0, D1 scan exit 1 — so the values
hold for `e1d22ca`, not for the named base. This does not touch C2's frozen predicate (which reads
counter labels on the final tree), but it is exactly the class M48 records and should appear in the
lesson as a second instance with its own pointer. Claims stay unedited (frozen before measurement).

**F2 (LOW, evidence durability) — the red-before receipt has no exit line.**
`grep -c EXIT reports/round-69/measure-before.log` = **0**; the file ends at line 105
(`HOLDS_OK_V6=yes`), while the round-68 after receipt carried `EXIT=0`
(`reports/round-68/measure-after.log:99`). The lesson must not assert the red-before counter's exit
code; only the final measured tree's exit is admissible (`claims.md:145-148`).

**F3 (MEDIUM, calibration gameability) — both Q15 legs are satisfiable vacuously.** Probed against
the committed checker:

| probe | why it matters | result |
|---|---|---|
| `tree-identity restatement: see the receipt above (no pair stated)` + a real false-sentence line | restatement with **zero pairs** | **exit 0** (`Q15_RESTATE_OK=yes`) — no re-derivation happened |
| false-sentence pair naming an **absent commit** (`deadbee:corpus` = `51894d15…`) | `check_line` records `actual=None` as a failure | **exit 0** — the "ability to fail" receipt need not quote D1 at all |
| restatement pair that resolves to a different id (`222a7a7:corpus` = `51894d15…`) | real mismatch | exit 1, `Q15_RESTATE_BAD line 1 … resolved 2c45edaf…` |
| no false-sentence line at all | missing defect receipt | exit 1, `no false-sentence pair failed` |
| only a false-sentence line | no restatement | exit 1, `Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)` |

Consequence: `Q15_RESTATE_OK=yes` / `Q15_FALSE_KILLED=yes` do **not** by themselves prove C2's
"shown able to fail and to pass". The lesson must therefore be written with the §4 template's
stricter shape (≥2 resolvable restatement pairs; the false pair is the real D1 mapping), and the
checker hardening — require `len(ok) >= 1` per restatement line and `actual is not None` for the
false leg — belongs in the round's routed list, not in this seat's edits.

**F4 (INFO) — the lesson cannot self-reference its own tree id** (see §4). Any restatement citing
the lesson commit will be unresolvable at measurement time and will turn `Q15_RESTATE_OK` to `no`.

**F5 (INFO) — M48's number is taken.** `corpus/QUALITY.md:27` already binds Q15 to `M48`; a lesson
row numbered otherwise (M46b, M50, …) leaves the criterion's origin unresolvable, which is itself a
`reference-drift` defect.

**F6 (INFO, frontier-step census) — before/after is already measurable and clean.** Required
command and both readings (row counts from the committed registries; the live validate run is the
"after" form):

```
$ git show 222a7a7:corpus/SOURCES.md | grep -cE '^\| S[0-9]{3} '   → 46   (S047 absent: 0)
$ git show 35e1258:corpus/SOURCES.md | grep -cE '^\| S[0-9]{3} '   → 47
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
CENSUS_EXIT=0
```

The lesson must paste both outputs with their exit codes, in the shape of
`corpus/lessons/round-68.md:66-90` (there: 45 → 46). Here: **46 → 47**, same four disclosed W04s,
no W03 (S047's `used-by` is populated, `corpus/SOURCES.md:61`).

## 6 · Commands this seat ran (all read-only, all on committed bytes)

| command | observed |
|---|---|
| `ls corpus/lessons/round-69.md` | absent |
| `git cat-file -e 35e1258:corpus/lessons/round-69.md` | fatal: does not exist |
| `git rev-parse {14774a2c,dddf147,1c34603,222a7a7,35e1258}:corpus` | `51894d15…`, `51894d15…`, `ddc6a4f6…`, `2c45edaf…`, `7aeabf21…` |
| `git diff --name-only 14774a2c 1c34603 -- corpus/` | `corpus/lessons/round-68.md` |
| `python3 -B corpus/q15_tree_id_check.py --self-test` | `Q15_SELFTEST=pass`, exit 0 |
| `… --scan reports/round-69/d1-false-sentence.md --lane …` | exit 1, `Q15_FALSE_KILLED: all false-sentence pairs failed (defect receipt)` |
| 5 draft-lesson scans (good / no-false / no-restate / bad-restate / absent-commit / zero-pair) | 0 / 1 / 1 / 1 / **0** / **0** — see §5 F3 |
| `git archive e1d22ca corpus reports/round-69 \| tar -x -C /tmp/…` then checker self-test + D1 scan | exit 0 / exit 1 (claims-revision values confirmed) |
| `python3 -B corpus/derive_axml_anchors.py` | exit 0, 20 lines, `enum block open : 237` (:9), `enum block close : 263` (:18) |
| `sha256sum corpus/derive_axml_anchors.py` | `74d4c0d9…b2a83aa` = S047's pin |
| M49 differential (v3 vs v4 stated ranges) | v3 `[(237,253)]` **FAIL exit 1**; v4 `[(237,263)]` **PASS exit 0** |
| `scripts/sources-census.sh validate --root … revenger` | exit 0, 47 rows, 4 W04, no W03 |
| `grep -c EXIT reports/round-69/measure-before.log` | 0 |

## 7 · Touched surfaces, out-of-scope, limits

- **Touched**: this file only. No edit to `corpus/` (lesson, QUALITY, entries, SOURCES), no git/jj
  mutation, no subagents, no `agent://all`.
- **Out of scope / not done**: the lesson itself is not written (assignment: "Do not edit
  anything"); the full counter was not re-run (its Q15 legs were exercised directly and its
  red-before receipt read as committed); checker hardening for F3 is routed, not applied.
- **Limits**: F3's two vacuous-pass holes are demonstrated on the committed checker with
  synthetic lesson files, not on the real lesson (it does not exist); F1 is a prose/pointer
  contradiction and does not by itself falsify C2, whose frozen predicate reads counter labels on
  the final measured tree.
- **Tool installs/upgrades**: none (pacman paused host-wide; no install needed).
- Scratch `/tmp/revenger-r69-lc` deleted before return.
