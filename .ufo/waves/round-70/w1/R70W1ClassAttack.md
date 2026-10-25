GAPS — the six classes are not sound: 11 constructible misses and 7 false-positive states were demonstrated on real lane bytes (base `3f5edbc`, repaired-clean scratch tree, and target `aa1842fa`), and `SELF_MUTANTS_KILLED=6/6` still passes because both mutant suites plant only the canonical defect per class.

# R70W1ClassAttack — attack on `corpus/self_assessment_check.py` (C2 calibration)

seat: `R70W1ClassAttack` (critic, wave 1) · date 2026-10-25 · no lane file written; all mutation on `/tmp` copies
(scratch removed at the end of this run: `/tmp/revenger-r70-R70W1ClassAttack`)
tool under attack: `git -C …/revenger-shokunin show aa1842fac199aa524930e5565ed3715de5f84c6d:corpus/self_assessment_check.py`,
sha256 `6a24baa158ec168e3d4315d91c8a9e35481976c065bb8323b5a61f4b665c90fb` (identical at base `3f5edbc`: the tool is new in round 70)
trees: `base` = `git archive 3f5edbc…`, `tgt` = `git archive aa1842fa…`, `clean0` = base with the nine known mismatches repaired
by hand (SM1 range → Q01–Q15, four names added to README, box 1 → `51809 bytes`/`a12fb8e2`, seat ids in box 1 → external,
`erratum: e1d22caf -> 3f5edbc`), which is the C2 after-state *shape* the claim must reach.

## Baseline reproduction (the claim's own before/after numbers)

```
$ python3 -B self_assessment_check.py --root base --lane <lane>
SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0   SELF_MISMATCH=9   exit=1      # = claims.md "Before"
$ python3 -B self_assessment_check.py --root tgt  --lane <lane>
SM1=1 SM2=7 SM3=2 SM4=1 SM5=1 SM6=0   SELF_MISMATCH=12  exit=1      # = control H (treated tools on unrepaired base)
$ python3 -B self_assessment_check.py --root clean0 --lane <lane>
SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0   SELF_MISMATCH=0   exit=0
$ python3 -B self_assessment_check.py --self-test          → SELFTEST OK: … exit=0
```

So the tool's own calibration gate is green *and* the frozen predicate's mechanical side is reachable. The attack below is on
what the six predicates can see, not on whether they currently fire.

## Method

Each probe is a `cp -r` of `base`/`clean0`, one mutation, then
`python3 -B self_assessment_check.py --root <copy> --lane <lane>`. A probe is a **MISS** when the mutated tree is genuinely
wrong and the class reads `0`; a **FALSE POSITIVE** when the tree is genuinely right and the class reads `>0`. Every mutation
was asserted applied before scoring (e.g. `applied=True` checks on the mutated line). Line numbers are the tool's, from
`show aa1842fa:corpus/self_assessment_check.py`.

## SM1 — README index range (`:55-61`)

| probe | mutation | expected | observed |
|---|---|---|---|
| MISS | delete the `\| Q07 \|` row from `QUALITY.md` (index claims Q01–Q15, table has 14 criteria) | 1 | **0** |
| MISS | append a new criterion as `\|Q16\| … \|` (no space after the pipe) | 1 | **0** |
| FALSE POSITIVE | README writes the correct range with an em dash: ``Q01—Q15`` | 0 | **1** |

Cause: `:57` `^\| Q(\d+) \|` parses only one spelling and `:61` compares `max(ids)` only — a gap is invisible; `:59`'s
`Q01[–-]Q` (`:58`) accepts en dash/hyphen but not em dash, so a correct index in another typographic form is red.
Tightening (one line, keeps the predicate): `ids` from `^\|\s*Q(\d+)\s*\|`, range from `Q01[–—-]Q(\d+)`, and
`return 0 if int(m.group(1)) == max(ids) and len(set(ids)) == max(ids) else 1`.

## SM2 — README index coverage (`:64-73`)

| probe | mutation | expected | observed |
|---|---|---|---|
| MISS | add unnamed `corpus/embedded_outputs.py` (its name is a **substring** of the README-named `check_embedded_outputs.py`) | 1 | **0** |
| MISS | add `corpus/.tools/x.py` (hidden dir, excluded at `:71`) | 1 | **0** |
| MISS | add unnamed `corpus/verify_notes.py` — excused by the literal glob at `:69` although it is not a verifier | 1 | **0** |
| MISS | add unnamed `corpus/tool.PY` (`:68` `p.suffix == ".py"`, case-sensitive) | 1 | **0** |
| MISS (scope) | add `corpus/knowledge/new_tool.py` (nested; docstring scopes to top level) | 1 | **0** |
| FALSE POSITIVE | README names the directory as `` `snapshots` `` instead of `` `snapshots/` `` | 0 | **1** |

Cause: `:69` `p.name in readme` is a raw substring test; `:71` drops dot-dirs; `:68` is case-sensitive; `:70`
`f"{p.name}/"` demands a trailing slash.
Tightening (one line): `named = re.search(rf"(?<![\w.-]){re.escape(p.name)}(?![\w-])", readme)`; `p.suffix.lower() == ".py"`;
`elif p.is_dir():` (no dot exclusion); dir test `f"{p.name}/" in readme or named`.
Note: the `verify_*.py` glob abuse at `:69` is **by design** (README names the family) and cannot be closed by a name test —
a tightened rule would need a capability probe (e.g. the file accepting `--self-test`), which the four legacy
`verify_icon*.py`/`verify_multi_icon_states.py` files would then fail (`grep -L -- --self-test base/corpus/verify_*.py` →
4 files). Recorded as a residual, not fixed by a one-liner.

## SM3 — SHONEN quoted digests (`:90-106`)

| probe | mutation | expected | observed |
|---|---|---|---|
| MISS | box names **two** files and quotes one file's size for both: `` `SKILL.md` (7003 bytes) and `corpus/README.md` (7003 bytes) `` (README is 7003, SKILL.md 51809) | 1 | **0** |
| MISS | digest on a non-file: `` `corpus/gone_script.py` (39098 bytes, sha256 `bfd92057`) `` | 2 | **0** (`:99` `if not files: continue` skips the box) |
| MISS | the stale `39098 bytes` / `bfd92057` moved into a continuation line indented by **one** space | 2 | **0** (`boxes()` `:81` requires two spaces) |
| MISS | delete `SKILL.md` — `required()` `:154` does not list `SKILL.md` (docstring says TREE holds it); the tree is scored, not refused with exit 2 | exit 2 | **exit 1, SM3=2** (caught only by accident: box 1 happens to quote SKILL.md) |
| FALSE POSITIVE | a provenance box quoting the pinned **historical** bytes: `` `SKILL.md` provenance: at r64 the bytes were 39098 bytes, sha256 `bfd92057` `` | 0 | **2** |

Cause: `:96-98` collects *all* named files and `:101/:105` accept a match against **any** of them; `:99` treats
"no resolvable file named" as "nothing to check" rather than as a mismatch; there is no historical/pinned escape.
Tightening (two short lines, still one predicate): attribute each quoted value to the **nearest preceding** file token
(`toks = [(m.start(), m.group(1)) …]; near(pos) = last token before pos`), and count a quoted value with `near() is None`
as a mismatch. Prototyped: `SM3a 0→1`, `SM3b 0→2`, `SM3c 0→2`, `SM3e` unchanged at 2 (correctly still red: an unpinned
historical value is a mismatch under this predicate — if provenance boxes are wanted, the escape must be an explicit
`pinned:` marker, which the frozen predicate does not have).

## SM4 — SHONEN verifier authorship (`:109-111`)

| probe | mutation | expected | observed |
|---|---|---|---|
| MISS | verifier named `RevengerR64.ReviewSkill` (capital R, no hyphen) | 1 | **0** |
| MISS | verifier named `revenger_r64_ReviewSkill` (underscores) | 1 | **0** |
| FALSE POSITIVE | box 1 keeps the **external** verifier and merely cites the seat's report path `.ufo/waves/round-64/R64ReviewSkill.md` | 0 | **1** |

Cause: `:111` matches the whole box body, not the verifier clause; the two seat spellings in `:111` are the only ones recognised.
**Repair pressure (most important SM4 finding):** the honest C2 repair of box 1 is to name a non-author verifier — but if the
box keeps its (true) citation of the seat's report, SM4 stays `1`. Demonstrated: on `clean0`, renaming only the verifier
(`revenger-r64.R64ReviewSkill` → `SomeoneOutside`) left `SM4=1`; it fell to `0` only after also renaming the cited report path
`R64ReviewSkill.md` → `OutsideReview.md`. The class therefore pushes the repair toward **deleting provenance**.
Tightening (one line): `m = re.search(r"Named non-author verifier:\s*`([^`]+)`", text)` and test the seat pattern on
`m.group(1)` only, with `(?i:revenger[-_]?r\d+[._]\w+)|(?<![A-Za-z0-9_])R\d{2}[A-Z]\w+`. Prototyped: `SM4a 0→1`,
`SM4b 0→1`, `SM4c 1→0`, `clean0` stays 0.

## SM5 — SCORECARD commit citations (`:114-134`)

| probe | mutation | expected | observed |
|---|---|---|---|
| MISS | `Pre-registration \`DEADBEE\`` (uppercase hex; `:124` is lowercase-only) | 1 | **0** |
| MISS | `commit: \`bbbbbbb\`` (colon after the introducer; `:124` requires `\s+`) | 1 | **0** |
| MISS | `commits \`bbbbbbb\`` (plural) | 1 | **0** |
| MISS | erratum whose good value resolves but is an **unrelated** commit: `Pre-registration \`bbbbbbb\`` + `erratum: \`bbbbbbb\` -> \`3f5edbc\`` | 1 | **0** |
| FALSE POSITIVE | 40-hex sha256 prefix after `base`: ``base `488f95aa1d502cbb20b7303e1d773f0101397a0b` is a sha256 prefix of measure.py`` | 0 | **1** |
| FALSE POSITIVE | fenced example: a code block containing ``the token tip `deadbeef0` must resolve`` | 0 | **1** |
| FALSE POSITIVE (usage) | run without `--lane` on an extraction (the docstring's own `--root TREE` workflow): `python3 -B tgt/corpus/self_assessment_check.py --root tgt` | 1 | **9** (`SELF_MISMATCH=20`) — every citation red because the default lane is the extracted tree |

Cause: `:124` hex class and introducer set; `:123` builds a **global** `bad → good` map and `:131` accepts any resolving
`good`; nothing strips fenced blocks; the default `--lane` at `:235` is `Path(__file__).parents[1]`, i.e. the extraction, so
the documented archive workflow silently reds all nine citations.
Tightenings: `[0-9a-fA-F]` and `(?i:pre-registration|pre[- ]?registration|\bbases?\b|\btips?\b|\bcommits?\b)\s*:?\s*`
(prototyped: `SM5a 0→1`, `SM5c 0→1`, `SM5d 0→1`); strip fenced blocks with `re.sub(r"```.*?```", "", text, flags=re.S)`
(kills the fenced FP). The erratum hole has **no intent-preserving one-liner**; the minimal mechanical rule is
`if good.startswith(bad)` before `excused[bad] = good` — prototyped: the wrong-commit erratum is no longer excused
(`SM5b 0→1`) and the cost is that a genuine typo-correction erratum no longer works: on `clean0` my synthetic
`erratum: e1d22caf -> 3f5edbc` is itself rejected (`SM5=1`), i.e. the repair must either cite the true commit or correct the
citation in place. That is the correct pressure, but it must be stated before the author writes the erratum.
The 40-hex sha256-after-`base` collision is a **writing constraint**, not a checker bug that a one-liner fixes: SCORECARD
must not introduce a digest with `base`/`tip`/`commit` immediately before it.

## SM6 — SCORECARD K statement (`:137-146`)

| probe | mutation | expected | observed |
|---|---|---|---|
| MISS | two K statements on one line, the **first** wrong: `` `K_HELD_BACKED` 9/14 → 9/14 · `K_HELD_BACKED_STRICT` 8/14 → 8/14`` (README held = 8) | 1 | **0** |
| MISS | current value wrong but a trailing historical number is right: `K_HELD_BACKED 8/14 → 9/14 (was 8/14)` | 1 | **0** |
| FALSE POSITIVE | correct README with trailing whitespace on one held row (`\| held \|  `) | 0 | **1** |

Cause: `:144` takes `nums[-1]` of the whole line — the last number, not the last *statement's* target; `:140`
`\| held \|$` demands an exact trailing form (no trailing whitespace allowed).
Tightening (one line each): `head = last[-1].split("K_HELD_BACKED_STRICT")[0]` then
`stmts = re.findall(r"K_HELD_BACKED[^0-9]*(\d+)/14(?:\s*(?:→|->)\s*(\d+)/14)?", head)`, current = `stmts[-1][1] or stmts[-1][0]`;
held count `re.search(r"\|\s*held\s*\|\s*$", l)`. Prototyped: `SM6a 0→1`, `SM6b 0→1`, `SM6c 1→0`.

## Why the frozen calibration conjunct still reads green

`SELF_MUTANTS_KILLED=6/6` (claims.md C2) is computed from **one canonical defect per class**, planted independently in
`reports/round-70/measure.py:72-104` (`build_self_fixture`): SM4's defect is the exact string `revenger-r64.R64ReviewSkill`
(`:89`), SM5's is the unresolvable `deadbee0123` (`:93`) — no erratum, no uppercase, no `commit:` form — and SM6's is a single
`8/14 → 9/14` (`:94`) — one statement, no second `K_` token. The tool's own `self_test` (`:177`) plants the same six canonical
shapes. Neither suite exercises a hidden dir, a substring collision, a two-file box, a non-file digest, an alternative seat
spelling, an erratum, or a two-statement line. So `SELF_CLEAN_FIXTURE=0` + `6/6` is a true statement about the *mutants*, not
about the classes: it is satisfiable by a checker with every gap above. The claim's sentence "the checker is shown able to
fail" is therefore true only for the canonical defect set.

## Prototype of the tightenings (evidence they are safe)

`/tmp/…/tight.py` re-implements only the six predicates with the tightenings above; same CLI.
`frozen` = tool at `aa1842fa`, `tight` = prototype, same trees, same `--lane`:

```
tree     frozen                              tight
base     SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0  SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0   (non-regressive)
tgt      SM1=1 SM2=7 SM3=2 SM4=1 SM5=1 SM6=0  SM1=1 SM2=7 SM3=2 SM4=1 SM5=1 SM6=0   (non-regressive)
clean0   SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0  SM1=0 SM2=0 SM3=0 SM4=0 SM5=1 SM6=0   (only the erratum rule differs)
```
Probe outcomes under `tight` (each `frozen→tight`, expected in brackets): SM1a `0→1`[1], SM1b `0→1`[1], SM1c `1→0`[0],
SM2a `0→1`[1], SM2b `0→1`[1], SM2d `0→1`[1], SM2f `1→0`[0], SM3a `0→1`[1], SM3b `0→2`[2], SM3c `0→2`[2],
SM4a `0→1`[1], SM4b `0→1`[1], SM4c `1→0`[0], SM5a/c/d `0→1`[1], SM6a `0→1`[1], SM6b `0→1`[1], SM6c `1→0`[0].
Residuals the prototype does **not** fix (recorded, not silently dropped): `verify_*.py` glob abuse (needs a capability
probe), the 40-hex-sha256-after-`base` collision, and the `--lane` default (a repair would have to make `--lane` mandatory or
fail closed with exit 2 when the root is not inside the lane).

## Impacted axes

C2 only (calibration). C1/C3 predicates do not read this tool; the counter's `HOLDS_C2_V5` reads
`SELF_MISMATCH`/`SELF_CLEAN_FIXTURE`/`SELF_MUTANTS_KILLED` and is unaffected by these gaps being *present* (it is currently
red anyway: `SELF_MISMATCH=12` on the target bytes). The kill rule is untouched: the frozen predicate is not edited by any
proposal above; each tightening is a change to the **tool's** bytes, which C2 explicitly allows ("the checker's bytes are
re-attacked by a mutation-tester seat in wave 2").

## Smallest safe correction (in priority order)

1. **SM4 clause-scoped match** (`Named non-author verifier:` capture only) — without it the C2 repair either keeps a red
   class or deletes the seat-report citation from box 1; this is the one gap that actively corrupts the repair.
2. **SM3 nearest-file attribution + count the unresolvable-file case** — closes the two-file mask and the "digest on a
   non-file" skip in one predicate.
3. **SM6 statement-scoped number** (`split("K_HELD_BACKED_STRICT")[0]`, arrow-target) — the landed SCORECARD already carries
   `K_HELD_BACKED` and `K_HELD_BACKED_STRICT` on one line (`SCORECARD.md:565`), so this class is one edit away from blind.
4. **SM1 gap test + em-dash range**, **SM2 word-boundary/case/dot-dir**, **SM5 fenced-block strip + case-insensitive hex +
   optional colon** — each one line, each prototyped non-regressive on base/target.
5. State the erratum rule (`good.startswith(bad)`) and the `--lane` requirement in the tool docstring **before** the author
   writes the SM5 repair, so the erratum is not written to the weaker rule.

## Not findings (checked, clean)

* `git cat-file -e <h>^{commit}` is the right resolve primitive; a blob/tree id is correctly rejected.
* The tool writes nothing outside its temp dirs; `--self-test` leaves no artefact in the tree (`python3 -B`, `tempfile`).
* Exit contract: a root lacking `corpus/README.md`/`QUALITY.md`/`SHONEN.md`/`SCORECARD.md` exits 2
  (`required()` `:153-156`); a root lacking only `SKILL.md` does not (see SM3 MISS 4).
* Reading order/imports: stdlib only (`hashlib`, `re`, `subprocess`, `sys`, `tempfile`, `pathlib`); no network, no mutation.

## Tooling record

No install or upgrade was made (host pacman transactions paused; `python3` and `git` already present). No lane or fleet file
was written; every mutation ran on a `/tmp/revenger-r70-R70W1ClassAttack` copy, and the scratch tree was deleted before this
report was written.
