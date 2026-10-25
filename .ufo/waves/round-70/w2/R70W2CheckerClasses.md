GAPS — the tightened checker scores 0 on the landed tree, but every class SM1–SM6 still has at least one real-mismatch miss and (except SM2) at least one correct-state false positive, built from new constructions on scratch copies of the landed bytes; and SM3/SM4 are *vacuous* on the landed tree, so the C2 zero is only half-calibrated.

Seat R70W2CheckerClasses · round-70 wave 2 (falsify) · lane `revenger-shokunin` · target bytes `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd` (landed), base `3f5edbc206351232a3d2d801334dd930499ccaf5`, pre-reg `dbacce212d798d1ec5bb59e03ff91d577eed0283`. Checker under attack: `corpus/self_assessment_check.py` sha256 `82e59fce5647f27727644d121dd73641bc14a7bb3293d7e54f2070b0db0335cc` (working tree clean at the landed commit; frozen for this wave). I did not open `.ufo/waves/round-70/w1/` before forming this verdict.

## 1. Vector at each commit (real lane trees, `git archive` extractions in scratch)

```
$ for t in base pre landed; do python3 -B corpus/self_assessment_check.py --root /tmp/revenger-r70-R70W2CheckerClasses/$t --lane <lane>; done
base   SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0  SELF_MISMATCH=9   exit=1
pre    SM1=1 SM2=7 SM3=2 SM4=1 SM5=1 SM6=0  SELF_MISMATCH=12  exit=1
landed SM1=0 SM2=0 SM3=0 SM4=0 SM5=0 SM6=0  SELF_MISMATCH=0   exit=0
$ python3 -B corpus/self_assessment_check.py --self-test   -> SELFTEST OK, exit=0
```
The base vector reproduces C2's declared `before` (1/4/2/1/1/0 = 9) exactly, and `dbacce21` reproduces the `H` control (12). The landed 0 is real for the four classes that have subjects.

## 2. New per-class probes (21 probes; each is a scratch copy of the landed tree, one mutation)

Harness: `/tmp/revenger-r70-R70W2CheckerClasses/probe.py` (imports the frozen checker, `evaluate()` per copy; `--lane` = the lane repo, read-only). `MISS` = a real mismatch scored 0; `FP` = a correct state scored ≥1.

| probe | class | want | frozen checker | direction |
|---|---|---|---|---|
| duplicate stale index line: line 9 correct `Q01–Q15` + a second `` - `QUALITY.md` — admission criteria Q01–Q13 `` | SM1 | 1 | **0** | MISS |
| correct range written `Q01 - Q15` (spaced hyphen) | SM1 | 0 | **1** | FP |
| correct range written with figure dash `Q01‒Q15` (U+2012) | SM1 | 0 | **1** | FP |
| checker named only inside a fenced block (prose index entry deleted) | SM2 | 1 | **0** | MISS |
| checker named only as `reports/round-70/self_assessment_check.py` (a different file) | SM2 | 1 | **0** | MISS |
| stale size split across a line break: `` Landed `SKILL.md` (39098\n  bytes) `` (real size 54975) | SM3 | 1 | **0** | MISS |
| correct bytes inside a fenced example (`` `SKILL.md` (39098 bytes) # sample output ``) | SM3 | 0 | **1** | FP |
| `- [X]` box naming `revenger-r64.R64ReviewSkill` | SM4 | 1 | **0** | MISS |
| `[x]` box, `Named non-author verifier: RevengerR70.` (the author L1 itself) | SM4 | 1 | **0** | MISS |
| `[x]` box, `Named non-author verifier: none.` + seat cited next line | SM4 | 1 | **0** | MISS |
| `[x]` box, `named non-author verifier: Someone Outside.` (lower case) | SM4 | 0 | **1** | FP |
| introducer with a parenthetical: `` The pre-registration (frozen before scoring) `bbbbbbb` `` | SM5 | 1 | **0** | MISS |
| 41-hex non-resolving token after `commit` (`{7,40}` cap) | SM5 | 1 | **0** | MISS |
| erratum written with `→` instead of `->` (correction still resolves) | SM5 | 0 | **1** | FP |
| erratum written `- **erratum**:` (indented, bold) | SM5 | 0 | **1** | FP |
| 9 held rows but stale `8/14`: C03 `frontier`→`held` **and** C06 `held` + annotation column (counts cancel) | SM6 | 1 | **0** | MISS |
| correct state, held row carries a trailing annotation column (`\| held \| note \|`) | SM6 | 0 | **1** | FP |
| correct state, fenced historical log line `K_HELD_BACKED 7/14` after the real line | SM6 | 0 | **1** | FP |
| correct state, last K line reads `K_HELD_BACKED_STRICT 8/14; K_HELD_BACKED 8/14` | SM6 | 0 | **1** | FP |

Totals: 12 MISS, 8 FP (one probe, `sm3b`, scored as declared by luck — see §4). No SM2 FP found inside the time box; SM2's defect is one-directional (undercount).

## 3. Smallest safe correction, and proof it is a fix (not a narrowing)

A scratch derivative (`/tmp/revenger-r70-R70W2CheckerClasses/sac_tight.py`, lane file untouched) with exactly these one-line tightenings:

- SM1 (`:58`): `re.search` → `re.findall(r"…Q01\s*[–—‒−-]\s*Q(\d+)")`, and `all(int(x) == max(ids) for x in ms)` — every index line must agree, and dash/spacing variants are the same state.
- SM2 (`:66-69`): strip fenced blocks before `named()`, and require the token to be either bare or `corpus/`-prefixed: `(?:(?<=corpus/)|(?<![\w./-]))`.
- SM3 (`:102-104`): strip fenced blocks and `re.sub(r"\s+", " ", text)` per box — a value split across a line break is the same claim.
- SM4 (`:86`, `:133-135`, `:124`): box state `[ |x|X|~]`, `(?i:Named non-author verifier)`, reject a clause starting `none`, and `SEAT` also matches bare `revenger[-_]?r\d+` (catches the author L1).
- SM5 (`:149`, `:154`, `:157`): erratum regex accepts `→`/`=>` and optional `- `/`**` decoration; introducer allows `[^`\n]{0,40}` before the token; hex width `{7,64}`.
- SM6 (`:178-182`): strip fenced blocks; count held rows with `\|\s*held\s*\|` (annotation column allowed); remove `K_HELD_BACKED_STRICT <n>/14` occurrences instead of truncating at the first `STRICT`.

Verification of the derivative:
```
21/21 probes now score exactly their declared class and total (0 MISS, 0 FP)
python3 -B sac_tight.py --self-test -> SELFTEST OK, exit=0
base 1/4/2/1/1/0 = 9 · pre 1/7/2/1/1/0 = 12 · landed 0/0/0/0/0/0 = 0   (unchanged)
```
So the fixes neither weaken the frozen `before` receipts nor the landed zero. They are tightenings of the same six class definitions, admissible under the A1 tighten-only rule.

## 4. Two findings about the landed zero itself

1. **SM3 and SM4 are vacuous on the landed bytes.** `SHONEN.md` at `17ee7f87` has **0** `[x]` boxes (`grep -c '^- \[x\]' SHONEN.md` → `0`) and **0** quoted `N bytes` / `sha256` values (the only `N bytes`-shaped text is "round-64 bytes", which the `(?<![\w-])` guard correctly skips). Base `SHONEN.md:5` was `- [x] …` quoting `39098 bytes` / `bfd92057…`; landed `SHONEN.md:5` is `- [~] …` and its text says "none is quoted here, so none can drift". The state is honestly described, but the C2 repair reached `SM3=0, SM4=0` by **removing the subjects**, not by supplying current values or a non-author verifier: `SELF_MISMATCH=0` cannot distinguish "verified clean" from "nothing left to check" for those two classes, and the only evidence the classes *can* fail is the synthetic self-test fixture. This is a saturation risk for C2, not a mismatch: the classes must keep at least one live subject, e.g. re-quote the current `SKILL.md` (54975 bytes, sha256 `f4f1ca95…`) and require the `[x]`/`[~]` split to be explicit.
2. **A real landed-byte mismatch that no class sees:** `corpus/README.md:23` documents the tool as "classes SM1–SM6; `--root`, `--self-test`", but `--root` refuses to run without `--lane` (`corpus/self_assessment_check.py:314`: `usage: --lane <repo> is required with --root …`). The index therefore advertises a usage that exits 64 — a self-assessment/repo-state disagreement inside the tool's own doc row, scored 0 by all six classes. The class set is not closed over the lane's own tool documentation (a seventh class, or fold into SM2 as "the usage form named in the index must be runnable").

## 5. Notes

- Attribution in SM3 is nearest-preceding-token, so a correct value can pass for the wrong reason: in `sm3b`/`sm3c` the value `54975 bytes` (correct) was attributed to an earlier `SKILL.md` token and scored 0 although the value itself had no adjacent file token. The FP direction is real (fenced example, §2) but this particular shape is not.
- No tool was installed; everything ran on Python 3 stdlib (`python3 -B`) plus read-only `git archive`/`git cat-file` against the lane. No mutating git/jj command was issued; the lane working tree was never written.
- Scratch (`/tmp/revenger-r70-R70W2CheckerClasses/`) deleted after this report.

Verdict: **GAPS** (6 classes; 12 misses + 8 false positives; tightening set in §3 verified to close all 21 probes without moving the 9 / 12 / 0 receipts).
