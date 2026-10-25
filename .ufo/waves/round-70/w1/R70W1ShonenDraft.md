DRAFT-READY — box 1 rewritten as honest lane attestation with no quotable digest/size (points at the pinned r64 commit), box 3's "census 4/4" mislabel corrected; checker on a scratch copy reads SM3=0 SM4=0, box count 4.

# R70W1ShonenDraft — C2 repair draft, SHONEN.md (SM3, SM4)

Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Target text: `SHONEN.md` as at
`3f5edbc206351232a3d2d801334dd930499ccaf5` (`git show 3f5edbc:SHONEN.md`). Checker:
`corpus/self_assessment_check.py` (present in the working tree; **absent at the base commit** —
`git show 3f5edbc:corpus/self_assessment_check.py` → `fatal: path ... exists on disk, but not in
'3f5edbc...'`, which is the C2 base control `A`). No lane file was edited; every trial ran on
`git archive 3f5edbc corpus SHONEN.md SCORECARD.md SKILL.md` extractions under
`/tmp/revenger-r70-R70W1ShonenDraft*` (deleted before return). No tool installed; no pacman call.

## 1. Audit of all four boxes against observed repo state

| box | names a verifier? | verifier a lane seat? | quoted digest/size matches current bytes? | pointers resolve? | verdict |
|---|---|---|---|---|---|
| 1 `[x]` | yes, `revenger-r64.R64ReviewSkill` | **yes** — lane cohort seat (`.ufo/waves/round-64/cohort.json:263` `"name": "R64ReviewSkill"`, `role: reviewer`; `.ufo/waves/round-64/plan-validated.json:391` `"kind": "spawn"`) | **no** — quotes `39098 bytes` + `sha256 bfd92057…`; current `SKILL.md` is `51809` B / `a12fb8e2…` | yes (see below) | **mismatch → SM3=2, SM4=1** |
| 2 `[~]` | `R64ReviewRecord` (lane seat, box is `[~]` so SM4 ignores) | n/a for SM4 | no quoted value | yes | **holds, keep** |
| 3 `[~]` | `R64ExecSkillRun` (lane seat, `[~]`) | n/a | no quoted value | yes | **prose mismatch only → corrected** (§3) |
| 4 `[~]` | none ("no outside verifier this round") | n/a | no quoted value | yes | **holds, keep** |

Evidence for the table (commands as run, output verbatim):

```
$ cd /home/vgpnk/Projects/shokunin/revenger-shokunin && sha256sum SKILL.md && stat -c '%s bytes' SKILL.md
a12fb8e2507dd5de956676d4c3536cf113466d214001c95259ec5d6e583df161  SKILL.md
51809 bytes
$ git -C .../revenger-shokunin show cab8085a5fe4e222090edb223755ac1d747386db:SKILL.md | wc -c
39098
$ git -C .../revenger-shokunin show cab8085a5fe4e222090edb223755ac1d747386db:SKILL.md | sha256sum
bfd92057e71541cc1d93a9812cb350d69fcb5524df57b24153364d6c11b0a9dd  -
```

So the quoted pair is *accurate for the r64 bytes* and *stale for the current bytes*: the SM3 limb
is a drift defect, not a fabrication. `cab8085` is the commit that landed `SKILL.md` (`git log
--oneline -- SKILL.md` → `cab8085 2026-10-24 round-64: C1 admission ... SKILL.md landed`), and the
seat's report signs exactly those bytes: `.ufo/waves/round-64/R64ReviewSkill.md:9-12` "Landed lane
artifact .../SKILL.md — 39098 bytes, sha256 `bfd92057e715…`", verdict `[x]`-ready: yes.

Pointer resolution (all four boxes):

```
EXISTS .ufo/waves/round-64/R64ReviewSkill.md
EXISTS .ufo/waves/round-64/R64ReviewRecord.md
EXISTS .ufo/waves/round-64/R64ExecSkillRun.md
EXISTS .ufo/waves/round-64/R64ConnectorOverlap.md
EXISTS .ufo/waves/round-64/R64ReviewSkillCites.md
EXISTS reports/round-64/measure-after.log
EXISTS corpus/live/runs/promotion-review-r5.md
EXISTS corpus/live/runs/round-63
```

Box 2 content check: `reports/round-64/measure-after.log:1-5` prints `K_HELD=8/14`,
`K_ROW C07 status=held`, `SAVED_RECORDS=59`; `.ufo/waves/round-64/R64ReviewRecord.md:9`
`Verdict: record verified.`, `:20-22` Evidence-ID re-derivation; `corpus/live/runs/round-63/` holds
`inspection.json`, `receipt.json`, `LEDGER.md`, `oracle_check.py`, `stdout.raw`; LOG.md:865 records
the end-to-end run ("Firmware fixture + real REA run landed (Evidence ev_aae7529f…, oracle ORACLE
OK)"). Box 2 is honest → keep unchanged.

Box 4 content check: `corpus/knowledge/round-64-firmware-region-byte-evidence.md:201`
`## Cross-lane scope note (Q10)`; `corpus/README.md:43` C07 row carries the scope parenthetical;
fleet `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:42` exists, names ADJ-06
("arbitrate the kaidoku/revenger shipped-artifact overlap before an ADJ-06 analysis is routed"),
carries no `L0 ANSWER` on that line, and `tsukuroi-shokunin/PROVINCE.md:51` still reads
`protocol integrator — kaidoku/revenger ownership unresolved`; `PROVINCE.md` last commit is
`522b89e 2026-10-15 round-1`, so "no province sentence edited" holds since r64. Box 4 is honest →
keep unchanged.

## 2. Exact replacement text — box 1

```
- [~] SKILL.md contains real decision tables, error patterns, checklists, cited sources
  Lane attestation, not a non-author check: the named verifier `revenger-r64.R64ReviewSkill` is a
  seat this lane dispatched (`.ufo/waves/round-64/cohort.json`; report
  `.ufo/waves/round-64/R64ReviewSkill.md`), and it re-stated `[x]`-ready = YES on the round-64
  bytes of `SKILL.md`, which resolve with `git -C <lane> show cab8085a5fe4e222090edb223755ac1d747386db:SKILL.md`
  (`<lane>` = this repository; size and digest come from piping that command to `wc -c` and
  `sha256sum`, and neither is quoted here, so neither can drift). The current `SKILL.md` has no
  outside confirmation; routed need: a non-lane reviewer re-confirming the CURRENT bytes
  (round-69 verifier spot-check V7, `corpus/lessons/round-69-verifier-spotcheck.md` §6). Citation
  sweep 0 phantoms (`R64ReviewSkillCites`); checklists executed verbatim with observed exits
  matching promises (`R64ExecSkillRun` transcript). Historical checks in
  `corpus/live/runs/promotion-review-r5.md` remain narrower history only.
```

Why this is honest and SM-clean:

- `[x]` → `[~]`: the verifier is a lane-dispatched seat, i.e. lane attestation, exactly the r69 V7
  ruling (`corpus/lessons/round-69-verifier-spotcheck.md:§6` "V7 — SHONEN box 1. The `[x]` rests on
  `revenger-r64.R64ReviewSkill`, a *lane-dispatched* seat, which the promotion gate counts as lane
  attestation (`[~]`)"). Dispatch is on record: `cohort.json:263-268` + `plan-validated.json:391`.
- No byte count and no digest are quoted for `SKILL.md`, so SM3 has nothing to drift; the r64 bytes
  are addressed by commit (`cab8085a5fe4e222090edb223755ac1d747386db`), which is immutable and
  resolves to `39098` B / `bfd92057…` (commands in §1).
- "re-stated on the final bytes" is replaced by "on the round-64 bytes": the seat signed the r64
  merge, not the current `51809` B / `a12fb8e2…` file. That was the second half of the stale claim.
- The routed need is stated as a need (non-lane reviewer re-confirming the CURRENT bytes), not as
  done work; it names V7 as its origin.

## 3. Exact replacement text — box 3 (mismatch found in the audit)

Box 3 read `(census 4/4, replay 10/10, oracle ORACLE OK, counter exit 0)`. The executed census is
**ten** verifier scripts, not 4/4; the `4/4` belongs to `HOLD_CALIBRATION`. Transcript:
`.ufo/waves/round-64/exec-skill-run.md:31` "Observed: ten verifier rows in name order, all
constituent exits `0`; `CALIBRATION 4 / 4 score= 10.0`; `REPLAY 10 / 10`; wrapper exit `0`", with
`VERIFIER_CENSUS_EXIT=0` at `:46` and ten `verify_*.py exit=0` lines at `:34-43`;
`reports/round-64/measure-after.log:44-45` `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`. The r64
`SKILL.md` promise is "all ten verifiers" (`git show cab8085:SKILL.md` line 208: "Census C ...
runs all ten verifiers from the corpus tree and prints every exit code"; line 284 "## 1. Verifier
census — ten saved-ledger replay verifiers").

```
  `SKILL.md` runnable sections executed by `R64ExecSkillRun` (verifier census: ten scripts,
  every exit 0; CALIBRATION 4/4; REPLAY 10/10; oracle ORACLE OK; counter exit 0); no
  independent outside instruction verifier.
```

Boxes 2 and 4 stay byte-identical. Box count stays 4.

## 4. Verification of the draft (scratch copy, checker output)

Base tree, unmodified (`git archive 3f5edbc corpus SHONEN.md SCORECARD.md SKILL.md`):

```
SM1=1  SM2=4  SM3=2  SM4=1  SM5=1  SM6=0
SELF_MISMATCH=9   EXIT=1
```

Scratch tree with **both** replacement blocks applied (box 1 + box 3), same command
(`python3 -B corpus/self_assessment_check.py --root <scratch> --lane /home/vgpnk/Projects/shokunin/revenger-shokunin`):

```
SM1=1
SM2=4
SM3=0
SM4=0
SM5=1
SM6=0
SELF_MISMATCH=6
EXIT=1
```

`grep -cE '^- \[( |x|~)\] ' SHONEN.md` on the patched copy → `4`. So this draft removes exactly
SM3=2 and SM4=1 and nothing else; SM1/SM2/SM5 remain for the seats that own them (README Q-range,
README index coverage, SCORECARD `e1d22caf` erratum) — `SELF_MISMATCH` therefore reads 6, not 0,
in a tree carrying only this repair, which is the expected separable-tree value for C2's SHONEN
component.

## 5. Findings

- **F1 (SM3, 2 mismatches) — located defect.** `SHONEN.md` box 1 at `3f5edbc` quotes
  `39098 bytes` and `sha256 bfd92057…a9dd` for `SKILL.md`; the file at `3f5edbc`, `aa1842f` and in
  the working tree is `51809` B / `a12fb8e2…` (§1 commands). The values are r64-accurate, so the
  repair is a re-point at commit `cab8085`, not a correction of the number.
- **F2 (SM4, 1 mismatch) — located defect.** Box 1 is `[x]` while its named verifier
  `revenger-r64.R64ReviewSkill` is a lane-dispatched seat (`cohort.json:263`,
  `plan-validated.json:391`); the `[x]` is lane attestation, which the promotion gate scores `[~]`
  (r69 spot-check V7).
- **F3 (prose, not an SM class) — located defect.** Box 3's `census 4/4` contradicts the executed
  transcript (ten scripts, exit 0; `CALIBRATION 4/4`) — §3. Fixed by the box 3 text; no SM class
  counts it, so the checker stays silent on it either way (stated as a limit below).
- **F4 (latent SM4 trap, informational).** The replacement box 1 still names `R64ReviewSkillCites`,
  which matches the SM4 regex `\bR\d{2}[A-Z]\w+`. It is harmless while the box is `[~]`; if a later
  round flips box 1 to `[x]` before an outside reviewer signs the current bytes, SM4 fires on it.
  That is the intended behaviour (the box would again be lane-only), recorded so the flip is not
  made by accident.
- **F5 (observed, not mine).** The working tree already carries a sibling's `SHONEN.md` edit
  (`git diff 3f5edbc -- SHONEN.md` → 12 insertions, 8 deletions) whose box 1 is substantively the
  same repair; scoring that in-flight text on a scratch tree also reads `SM3=0 SM4=0`
  (`SELF_MISMATCH=6`, box count 4). Two deltas from my draft, for the integrator to reconcile:
  it cites the r64 commit as `git show cab8085a5fe4e222090edb223755ac1d747386db:SKILL.md` without
  `-C <lane>` (runs only from the lane root), and it does not cite the dispatch receipt
  (`cohort.json`). It leaves box 3's `census 4/4` untouched, so it keeps F3.

## 6. Known limits

- SM3 is a byte-drift detector, not a prose checker: F3 (a label naming the wrong count) scores 0
  under it, so a `SELF_MISMATCH=0` tree does not by itself prove the boxes' wording is true. Box 3's
  correction is evidence-checked by hand here, not by the tool.
- "No province sentence edited" (box 4) was checked at file granularity (`PROVINCE.md` last
  commit `522b89e 2026-10-15`), not sentence by sentence.
- The checker at `3f5edbc` does not exist; all base readings use the working-tree checker
  (`corpus/self_assessment_check.py`, 10829 B, mtime 17:48) against archived trees, which is the
  documented invocation (read-only, `--root` + `--lane`).
- I did not edit `SHONEN.md` or any other lane file; the integrator applies §2/§3.

Scratch `/tmp/revenger-r70-R70W1ShonenDraft*` removed; no writes outside this report.
