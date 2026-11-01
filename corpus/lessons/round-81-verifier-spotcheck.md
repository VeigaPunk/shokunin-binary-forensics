author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

# revenger round 81 — verifier spot-check (non-author closure judge)

Closed against lane tip `b2fc6bbb195c6029ac2ce6a51e6e376ec0001c4a` (branch
`main`, pushed), base `081f032fda9502ebfbceb295d7e097dd8803bce1`. I authored
nothing in this round; every number below was re-derived by me from committed
bytes (`git archive <sha> | tar -x` into a judge scratch tree, then executed
outside any repo) or re-opened live. Verdict: **both claims verify, no axis
harmed — admitted.**

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report committed by lane identity | `git -C <fleet> log --format='%an %H' -1 -- .ufo/reports/round-81/revenger.md` | `revenger-shokunin 12692ff56faf…` | OK |
| SHONEN heading | grep on the report | `## SHONEN` + 4 `[~]` lines | OK |
| cited commits exist + ancestors | `git merge-base --is-ancestor <c> refs/heads/main` for `081f032`, `8261a24c`, `88b7e7ce`, `b330049b`, `b2fc6bb` (+ carry-in cites `ef7d3ee3`, `b1e0c60e`) | all ANCESTOR-OK | OK |
| branch tip pushed | `git ls-remote origin refs/heads/main` vs `rev-parse refs/heads/main` | both `b2fc6bbb195c…` | OK |
| round work in `081f032..b2fc6bb` | `git log --oneline <base>..<tip>` | exactly the 4 declared commits (freeze/landing/adjudication/correction) | OK |
| dispatch/complete digest | grep `.ufo/watchdog.log` | `2026-11-01T08:37:01-08:00 launch revenger round=81 base=081f032fda95 (zcode run14)` / `2026-11-01T11:01:06-08:00 complete revenger round=81 head=b2fc6bbb195c pushed=True` — matches the closure brief verbatim | OK |
| marker rule | report content | substantive: real work, evidence pointers, checkable hashes | real report, not a marker |

## 2. Claim re-checks

### C1 — coverage: eleventh F family via a real keyed-archive producer record — RE-MEASURED, VERIFIES

Pins (sha256sum over extracted committed bytes): `f_probe4.py`
`4d871971…6a3c7` ✓; `fixture.plist` 210 bytes `f0e02e64…37785c` ✓;
`inspection.json` 3174 bytes `83fe4046…348fcf` ✓; frozen `f_probe3.py`
`9441640dc0ff…14b418` byte-equal base↔tip ✓; v1 `orphan_sweep.py`
`f21f5e3d…1890b` byte-equal ✓.

- Oracle, mine: `python -B oracle_check.py truth.json inspection.json
  fixture.plist` (all three from `git archive` bytes) → `ORACLE OK (27/27
  checks)`, exit 0.
- Producer reproduction, mine: `rea inspect-keyed-archive <fixture> --format
  json` on the committed fixture → exit 0, stderr 0 bytes; byte-diff vs the
  committed record confined to per-run metadata (`evidence_id`, input-path
  fields); `normalized_result` identical; oracle over MY fresh record →
  `ORACLE OK (27/27 checks)`. The committed record is a genuine producer
  output on the committed fixture bytes.
- Probes, mine (extraction of the named commit, probes from the tip):

| probe | base `081f032` corpus | landing `88b7e7ce` corpus |
|---|---|---|
| `f_probe.py` (v1) | `F_COVERAGE=7/8 score=8.75` | `7/8 8.75` (hold) |
| `f_probe2.py` | `F2_COVERAGE=8/9 score=8.89` | `8/9 8.89` (hold) |
| `f_probe3.py` | `F3_COVERAGE=9/10 score=9.00` | `9/10 9.00` (hold) |
| `f_probe4.py` | `F4_COVERAGE=9/11 score=8.18` (artifact-graph absent) | `F4_COVERAGE=10/11 score=9.09`, `artifact-graph` in `F4_FAMILIES` |

  Matches `f4-before.log` / `f4-after.log` and the SCORECARD row exactly.
- Envelope: `receipt.json` exit 0, stderr 0 bytes, Evidence
  `ev_6eb77fb0…02af4b73` (form `ev_<64hex>`, oracle-checked) ✓.
- S457 re-opened: `rea --llms` prints the row's quote verbatim —
  "Inspect a Foundation keyed archive as an object-reference graph";
  `rea capabilities` shows provider `rea-artifact-graph` (quote is 9 words,
  ≤25 ✓).

### C2 — calibration: orphan_sweep v2 supersession — RE-MEASURED, VERIFIES

- Selftest, mine: `python -B orphan_sweep2.py --selftest` (extracted tip,
  outside any repo) → 7 legs `ok` (clean, planted-orphan, absent, line-ref,
  dir-style, masked-absent negative, `SWEEP_SELFTEST_MUTANT_FLAGGED=ok`) +
  `SWEEP_SELFTEST=pass`, exit 0. Unrecognized form → exit 64 ✓. `--format
  summary` prints its filter statement in-output ✓.
- Real tree, mine (`--lane <lane-worktree> --fleet <fleet-root> --format
  full`): exit 0, full output (369 SWEEP lines), `SWEEP_CORPUS
  fleet-reports=22 lessons=43`, `CITED=369 COMMITTED=357
  LANDABLE_ORPHANS=0 ABSENT=12`. My citation corpora grew by two files after
  the adjudication receipt (the fleet round-81 report and the round-81
  lesson joined the scanned set; the receipt's own header names its basis
  `fleet-reports=21 lessons=42`, `CITED=357 COMMITTED=345`) — the
  verdict-bearing values (ABSENT=12, LANDABLE_ORPHANS=0, exit 0) are
  identical in both, which is precisely the per-revision-corpus discipline
  the new header enforces.
- Supersession substance, mine: v1 over the same real tree prints NO
  `SWEEP_CORPUS` line and dispositions both named artifacts `absent`
  (`corpus/knowledge/round-68-apk-axml-byte-evidence.md:57,:148,` and
  `corpus/lessons/round-64`) while v2 classifies both `committed` (the
  latter with `normalized: corpus/lessons/round-64.md committed`); both
  files confirmed committed at the tip (`git ls-tree`). 2 false absents → 0.
- Carry-in root-cause (344/357/358), mine — reproduced EXACTLY with the v1
  tokenizer over reconstructed corpora:

| corpus (lessons @ + fleet reports) | v1 CITED | verdict values |
|---|---|---|
| `ef7d3ee3` (r80 landing, 40) + fleet minus round-80 | **344** | committed=330, absent-class total 14, LANDABLE_ORPHANS=0 |
| `b1e0c60e` (r80 receipt completion, 41) + fleet through round-80 | **357** | (the r80 receipt's basis) |
| `8261a24c` (freeze, 42) + fleet through round-80 | **358** | (the r81 red receipt `CITED=358 COMMITTED=344 ABSENT=14`) |

  The quoted-vs-receipted r80 drift is corpus membership, exactly as the
  erratum states; verdict values identical in all corpora.

### Correction `b2fc6bb` (CRLF) — RE-MEASURED, VERIFIES

- `git cat-file blob` CR-byte counts: tip LOG.md = **0** (LF restored);
  landing `88b7e7ce` = 0; adjudication `b330049b` = **1167** (the disclosed
  whole-file rewrite).
- LOG.md landing→tip numstat: `10 0` — 0 deleted, 10 added lines (the 9-line
  entry + 1 blank separator); byte-level diff shows no deletions. Append-only
  property held.
- `diff-tree 88b7e7ce..b2fc6bb`: LOG.md, SCORECARD.md,
  `corpus/lessons/round-81.md` (Mistakes row 6) + the adjudication receipt
  logs — the declared scope, nothing else.

### No-harm — VERIFIED

`diff-tree -r --name-only 081f032..b2fc6bb` over protected paths
(knowledge, corpus README/QUALITY, verifiers, SKILL, SHONEN, PROVINCE,
pre-r81 fixtures, frozen instruments) → empty except the declared LOG.md
append. SCORECARD.md: 85 insertions / 0 deletions (append-only). SHONEN.md:
four `[~]` lines, no `[x]` written. Separability receipts (`c1-only.log`
oracle exit 0 with v2 absent; `c2-only.log` F2 8/9 with f_probe4 absent)
consistent with my own probe outputs.

## 3. Per-axis verdicts

| axis | verdict | evidence |
|---|---|---|
| coverage | **improved** | C1 re-measured: 9/11 (8.18) → 10/11 (9.09) on the registered F4 instrument over the landing archive; frozen v1/F2/F3 holds reproduce byte-identically; K untouched (no README/knowledge byte changed) |
| calibration | **improved** | C2 re-measured: selftest 7/7 + attributed mutant kill; 2 false absents → 0 on the real tree; count-basis header present; exits 0/1/64 verified |
| depth | unchanged | no claim; no engine readiness claimed (Q05 scope note held) |
| operability | unchanged | no claim; instruments I ran all executed as declared |
| freshness | unchanged | FRESH_ROWS hold not re-claimed (knowledge bytes untouched — no-harm verified) |
| adjacency | unchanged | PROVINCE.md byte-untouched; Q10 scope note in the LEDGER accurate |

## 4. Discernment spot-check table

| item | decision | re-opened source (mine) | agree/disagree | reason |
|---|---|---|---|---|
| S457 capability surface | ADMIT (tier A own-work) | `rea --llms` (quote verbatim) + `PYTHONUTF8=1 rea capabilities` | **agree** | the artifact-graph decode group is real, `available: true` on this host, and in no F3 family set — the row teaches exactly what C1 routed onto |
| S458 producer record | ADMIT (tier A own-work) | fresh `rea inspect-keyed-archive` run on the committed fixture + oracle 27/27 over my fresh record | **agree** | record fully reproducible; every oracle-checked fact derives from the built bytes (Q06 discipline held under adversarial re-run) |
| macho/signature families (S453 lineage) | REJECT route (unsupported_host) | `rea capabilities` → `availability_code: unsupported_host`, "Native macOS utilities require macOS." | **agree** | hard host gate, not a taste rejection; F4's honest exception (10/11, not 11/11) correctly preserved |
| F android (S448 receipt) | REJECT route (hard-gated) | `REA_JADX_MCP_JAR` UNSET; no jadx on PATH; `~/tools` = downloads/ + ghidra only | **agree** | gate genuinely absent on this host; ruling-out re-confirmed |
| census | round end | sanctioned explicit-lane-dir form re-run by me | **agree** | exit 0, 31 W = 21 W01 + 10 W04 (the same disclosed classes), zero E-findings; literal form exit 2 (disclosed r74–r81 lineage) reproduced |

L0 re-read: `.ufo/l0-questions.md:233` (r74 dispatch-surface question) —
still unanswered; correctly routed around, never treated as answered.

## 5. Trend verdicts

- **expansion — improved (agree).** An eleventh in-province F family with a
  real, oracle-checked current-producer record; frozen holds v1 7/8, F2 8/9,
  F3 9/10 re-measured unchanged; no knowledge admission attempted on a
  blocked route.
- **quality — improved (agree).** Byte-derived identity oracle verified
  under an adversarial fresh-record re-run; the standing hygiene instrument
  now closes its own named false-disposition and receipt classes with an
  attributed mutant kill and a machine-checkable count basis; no admitted
  entry failed any re-check.
- **discernment — improved (agree).** Six mistakes mined with captures
  (lesson `## Mistakes` rows 1–6), two caught before any committed byte, the
  r80 drift root-caused to exact reproduced numbers (344/357/358), the CRLF
  rewrite caught by the mandated post-commit diff check and repaired in-round
  by an append-only correction; the denominator risk disclosed pre-run.

## 6. Defects found (status-neutral; routed to the lane for next round)

1. **Red-grep count off as pasted.** The parser-artifact counting command
   quoted in the report, `claims.md`, and the SCORECARD round-81 C2 row —
   `grep -cE '^SWEEP absent (corpus/knowledge/round-68-apk-axml-byte-evidence\.md:57|corpus/lessons/round-64) '`
   (note the trailing space inside the pattern) — returns **1**, not the
   stated **2**: the multi-ref token prints as `…evidence.md:57,:148,`, so
   the first alternative can never be followed by a space. Without the
   trailing space the count is 2. The SUBSTANCE verifies (my own v1 run
   misdispositions exactly those two committed files as absent; v2
   classifies both committed), so this is a counting-command fidelity
   defect only. Fix next round: repin the grep without the trailing space,
   or count `^SWEEP absent corpus/knowledge/round-68` + `^SWEEP absent corpus/lessons/round-64` separately.
2. **Correction numstat phrasing.** The `b2fc6bb` LOG bullet and report say
   "diff vs the landing = 0 deleted / 9 added"; the raw numstat is `10 0`
   (9 content lines + 1 blank separator). Byte-level verification confirms
   the substance (0 deletions, LF endings restored), so this is a phrasing
   precision item only.
3. **Receipt-vs-regrown-corpus comparison rule (no lane action needed).**
   My v2 re-run prints `CITED=369` on a grown corpus (basis 22/43) vs the
   receipt's `CITED=357` (basis 21/42) with identical verdict values — the
   `SWEEP_CORPUS` header resolved the ambiguity by design. Standing
   reminder: compare basis lines first, never bare CITED values across
   corpora.

## 7. Routed items already on the lane's queue (unchanged, not re-routed)

Criterion R extension; criterion N's mutation-killed attribution pair;
criterion C repair (§9 sizing, unchanged r78–r80); F android hard-gate
(caller-supplied `REA_JADX_MCP_JAR`); K wave-Q-review surface (blocked on
the r74 L0, still unanswered); census literal form (operator-side).

## 8. SHONEN note for the operator

All four boxes remain `[~]` (asserted-by-author) with resolvable pointers;
no `[x]` was claimed and none is due from me as a matter of the lane's own
round. The boxes continue to look checkable by a non-author reviewer
(SKILL.md decision tables, the round's end-to-end producer task logged in
LOG.md with pointers, executable instructions — this closure re-executed
them, PROVINCE accuracy byte-verified); the outstanding promotion review
remains operator-side, as the r79/r80 closures already noted.
