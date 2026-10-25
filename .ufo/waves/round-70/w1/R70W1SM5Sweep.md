# R70W1SM5Sweep — named-unmeasured self-assessment mismatch sweep

**Verdict: FALSIFIED-class findings reported — 6 named-unmeasured classes detected outside SM1–SM6 (2 high, 2 medium-high, 2 medium); all six SM classes re-derive at base, and the in-flight repair tip 17ee7f8 already zeros SELF_MISMATCH=0.**

Sweep scope: `SCORECARD.md` (Round 61+ sections), `SHONEN.md`, `corpus/README.md`, `LOG.md` tail, at the frozen round-70 candidate target `aa1842fac199aa524930e5565ed3715de5f84c6d`. Evidence: every command below run by me; paths absolute in the lane repo except where noted.

---

## 1. Classification baseline — the six SM classes re-derive exactly

Counted by the frozen checker, base `3f5edbc` (reproduced with the committed checker on my base extraction):

```
SM1=1 SM2=4 SM3=2 SM4=1 SM5=1 SM6=0 → SELF_MISMATCH=9 exit=1
```

- SM1=1: README `QUALITY.md` index line says "Q01–Q13"; QUALITY.md max Q id = Q15.
- SM2=4: unnamed corpus/*.py `q15_tree_id_check.py`, `derive_axml_anchors.py`, `check_embedded_outputs.py` + dir `snapshots/`.
- SM3=2: SHONEN box 1 quotes `39098 bytes` and `sha256 bfd92057…` for SKILL.md; current bytes are 51809 / `a12fb8e2…`.
- SM4=1: SHONEN box 1 `[x]` names lane seat `revenger-r64.R64ReviewSkill`.
- SM5=1: SCORECARD:557 backs `e1d22caf` (see §4: it is a one-character typo of a resolving commit).
- SM6=0: last SCORECARD K line `8/14` == README held rows = 8.

Candidate tree `aa1842f` scores `SELF_MISMATCH=12` (SM2=7: +`lint_entry.py`, `self_assessment_check.py`, `derive_axml_anchors_r68.py`). In-flight repair tip `17ee7f8` scores `SELF_MISMATCH=0 exit=0`. The wave-1 integration has already repaired all six SM classes.

---

## 2. Findings outside SM1–SM6 (named-unmeasured)

### F1 — HIGH. SCORECARD.md:321 cites verifier seat `W2ReviewSeparability` that never existed
`SCORECARD.md:320-322`: "Claim separation verified by named seat `W2ReviewSeparability` (build) and `W2VerifySeparabilityFinal` (falsify)".

```bash
find .ufo -name 'W2ReviewSeparability*'        # empty
git log --all --pretty=format: --name-only | grep -i W2ReviewSeparability   # empty: never a file
git show 98ad3a0:.ufo/waves/round-63/build-spec.json | grep -o 'R63[A-Za-z0-9_]*' | grep -i separ
# → R63ReviewSeparability   (the actual build seat; report exists at .ufo/waves/round-63/build/R63ReviewSeparability.md)
git show 35f750c:.ufo/waves/round-63/falsify-spec.json | grep -o 'W2[A-Za-z0-9_]*' | grep -i separ
# → W2VerifySeparabilityFinal   (exists at .ufo/waves/round-63/falsify/W2VerifySeparabilityFinal.md)
```
The build seat named in the scorecard is a phantom: no spec, no report, never in history. SM4 counts only SHONEN `[x]`-box lane seats; SM5 counts only commit hashes — no SM class audits SCORECARD citation seams * report files. STILL PRESENT at in-flight tip `17ee7f8` (`SCORECARD.md:321` unchanged).

### F2 — HIGH. SHONEN.md:23 asserts a README C07 parenthetical that never existed
`SHONEN.md:22-23`: "Entry `## Cross-lane scope note (Q10)` + README C07 parenthetical report-not-absorb ADJ-06 (fleet `.ufo/l0-questions.md:42` open)".

```bash
grep -c 'ADJ-06' corpus/README.md        # 0 (at aa1842f and at 17ee7f8)
git log --all -S 'ADJ-06' --cor/README.md   # empty → ADJ-06 never in README at any commit
sed -n '36p' corpus/README.md            # actual C07 row: no ADJ-06, no "report-not-absorb"
sed -n '42p' /home/vgpnk/Projects/shokunin/.ufo/l0-questions.md   # correct fleet pointer (ADJ-06 question)
```
Half the citation is true (fleet L0 question #42 is the tsukuroi ADJ-06 arbitration). The README half is false — the README C07 row has never contained ADJ-06 at any commit. Not counted: SM3 counts SHONEN quoted *digests* only; SM4 counts `[x]`-box lane-seat *authorship* only; box 4 is `[~]`. STILL PRESENT at `17ee7f8`.

### F3 — HIGH (at the frozen candidate; already repaired in-flight). README.md:52-53 Known gaps: "SKILL.md and AGENTS.md are absent ... no gate registry exists"
At `aa1842f`:
```bash
stat -c '%s' SKILL.md          # 51809  → SKILL.md EXISTS
sha256sum SKILL.md             # a12fb8e2...
sed -n '272p' SKILL.md         # "## Gate registry (registry home; PROTOCOL.md §Gate standard)"
sed -n '276,277p' SKILL.md     # name=check_embedded_outputs, kind=gate
```
Both halves false: SKILL.md exists (51809 B) and a gate registry exists registering `check_embedded_outputs` as a gate (also SKILL.md:346). AGENTS.md is genuinely absent,never in history). This is prose in the README index — no SM class checks file-existence prose (SM2 checks only corpus/*.py and corpus/*/ dir names; SM1 the Q-range). **Already repaired in the in-flight wave-1 integration** `17ee7f8` (README lines 59–61: "`AGENTS.md` is absent … `SKILL.md` exists and carries a `## Gate registry`"), so this is a true mismatch at the frozen candidate that the current wave has already closed.

### F4 — MEDIUM-HIGH. README.md:34 C05 row names only the r65 rejected candidate; r67/r68/r69 rejected candidates are unrepresented
```bash
ls corpus/knowledge/ | grep 'round-6[5-9]-apk'   # round-65, -67, -68, -69 present (all admission-status: rejected, coverage-map C05)
grep -c 'round-67\|round-68\|round-69' corpus/README.md   # 0
```
README's coverage-map C05 row names `knowledge/round-65-apk-axml-byte-evidence.md` as the retained rejected candidate while three more retained rejected C05 candidates exist and are named nowhere in the README. README's own `knowledge/` index bullet says the dir "retains clearly marked rejected candidates (each carries an `admission-status: rejected` header)" — the map is the only enumeration, and it is three rounds stale. SM2 inspects corpus/*.py and corpus/*/ dir names only, not corpus/knowledge/*.md contents.

### F5 — MEDIUM. README.md:14 lessons/ index enumerates 4 of 21 lesson files
```bash
ls corpus/lessons/ | wc -l        # 21
grep -n 'lessons/' corpus/README.md   # line 14 names only: 2026-10-12-r1-provider-gap.md, round-1.md, round-1-verifier-spotcheck.md, round-61.md
```
Rounds 62–69 lessons (8 files) and all 9 `round-NN-verifier-spotcheck.md` files are absent from the index enumeration. SM2's rule stops at "every top-level corpus/*.py file and every corpus/*/ directory named" — it does not descend into corpus/lessons/ contents, and the index line's apparent enumeration is never checked.

### F6 — MEDIUM (calibration class). SCORECARD quoted file digests are never re-derived against tip bytes
```bash
git show f6ea2932:corpus/knowledge/round-63-zip-central-directory-evidence.md | sha256sum   # b2660e60…e0086 (matches SCORECARD:329)
sha256sum corpus/knowledge/round-63-zip-central-directory-evidence.md                       # tip: 73d9a4d1…
git show 8c27f1b:corpus/knowledge/round-64-firmware-region-byte-evidence.md | sha256sum    # 9bf21e50…e0ebf (matches SCORECARD:397)
sha256sum corpus/knowledge/round-64-firmware-region-byte-evidence.md                       # tip: b4f470f3…
git show 8c27f1b:corpus/verify_icon_languages.py | sha256sum    # a2fd347e… (matches SCORECARD:401)
sha256sum corpus/verify_icon_languages.py                       # tip: 2bf9b5fe…
git show 8c27f1b:corpus/verify_multi_icon_states.py | sha256sum  # 9345cb8c… (matches SCORECARD:402)
sha256sum corpus/verify_multi_icon_states.py                     # tip: 09c50774…
```
The SM3 class checks SHONEN's quoted digests against current bytes (and counts the stale SKILL.md pair). No class applies the same check to SCORECARD's four quoted file digests — all four now name bytes absent from the tip (entries edited by the r66 stale-candidate header repair; verifiers patched in r65/r66). Per-round sections are historical, hence MEDIUM confidence; the lane's own SM3 precedent (treating the SKILL.md quote as a real mismatch) argues the SCORECARD digests are the same defect shape in an unscanned location.

---

## 3. False positives considered and excluded

- `SCORECARD.md:157` `f27b5f1a92af4f05081e7992925e30d621fff1c0` — inside the "Imported scorecard — historical, not current" section (pre-Round-61, outside SM5's `## Round 61` window); references the pre-restructure `.shokunin/revenger` layout; no commit exists under that hash in lane or fleet; not actionable (excluded).
- `SCORECARD.md:557` `e1d22caf` — SM5 counts it (=1) as unresolvable. Verified: `e1d22caf` fails `git cat-file -e 'e1d22caf^{commit}'` (rc=128) while `e1d22caa` and the full hash `e1d22caaf9a2fdc4c1c13d1f4a8a6813e7b07968` resolve to the round-69 pre-registration commit (LOG.md:954 carries the full hash). So this is a one-character typo (`e1d22caf` → `e1d22caa`), not a missing commit; the in-flight erratum at SCORECARD.md:605 already excises it.
- `504b0506` — ZIP EOCD magic, not a commit; SM5 correctly does not match it (prompt: "a sha256 prefix is not a commit").
- Wave seat counts re-derive: r63 build 32 + falsify 32 = 64; r64 spec spawn=64 (R64CriticC4's report is in `briefs/R64CriticC4.md`); r65/r67/r68/r69 spec counts 64 and 64 report files each (r67's 65th file is `adjudication-drafts.md`, a non-seat draft).
- SOURCES census "15 rows … at `35b2e8b`" validates (`git show 35b2e8b:corpus/SOURCES.md | grep -cE '^\| S[0-9]+ '` → 15); tip = 47 rows, consistent with the r69 "rows 46 → 47" progression.
- README "Rows 14" → `grep -cE '^\| C[0-9]+ ' corpus/README.md` = 14; held rows = 8 = last SCORECARD K_HELD_BACKED 8/14 (SM6 = 0).
- Host-tool claims re-derive TRUE at aa1842f: binwalk 3.1.0, unblob 26.6.4 (`~/.local/bin/unblob`), jadx 1.5.6, dotnet on PATH reporting no SDK. The earlier apparent unblob absence was a PATH artifact (non-login shell without `~/.local/bin`) — rechecked with the repo's own recheck environment.

---

## 4. Checker-design gap surfaced (SM4 vacuous [x] box)

The SM4 class counts an `[x]` box only if the named verifier matches a lane-seat pattern. A `[x]` box whose verifier name is dropped/blank scores 0 (vacuous pass):
```python
"- [x] something entirely new\n  no verifier named at all\n" → sm4 = 0
```
Under C2's kill rule ("the checker must be shown able to fail"), this means a repaired SHONEN box could be made `[x]` with no verifier and still pass SM4. Not a current mismatch (box 1 still names the seat), but relevant to the C2 repair's honesty constraint.

---

## 5. Summary verdict

- **Six SM classes at base: reproduced exactly** (SELF_MISMATCH=9), so the C2 "before" figure and class boundaries are trustworthy.
- **Wave-1 integration tip 17ee7f8** already drives all six classes to 0 (SELF_MISMATCH=0, exit 0).
- **Named-unmeasured true mismatches outside SM1–SM6: 6 classes (2 high, 2 medium-high, 2 medium)** — F1 phantom SCORECARD seat `W2ReviewSeparability` (unfixed at 17ee7f8), F2 SHONEN→README ADJ-06 parenthetical claim (unfixed at 17ee7f8), F3 README "SKILL.md absent / no gate registry" (fixed in-flight at 17ee7f8), F4 README C05 row omits r67/r68/r69 rejected candidates, F5 lessons/ index enumerates 4/21 files, F6 SCORECARD quoted file digests stale (4 instances).
- The six SM classes do not cover: SCORECARD named-seat citation existence, SHONEN cross-file prose citations, README file-existence/registry prose, README coverage-map knowledge entries, corpus subdirectory index content, and SCORECARD file-digest currency.

Targets: `SCORECARD.md:321`, `SHONEN.md:23`, `corpus/README.md:34,52-53,14`, `SCORECARD.md:329,397,401-402`. All evidence above is command-produced; sha256 where relevant.
