author: hyaku closure (non-author integrator, @m_zfl)

# revenger round 98 — non-author verifier spot-check (closure)

Lane round: revenger r98 (hyaku run 15, attempt 1). Base `34c56f9f324723cafd56fd57d718065b2ad2da66`,
lane tip `5498390e2faf92e2bbb4fa5d35dbe50b070dbb94`. Report `.ufo/reports/round-98/revenger.md`.
Driver digest (copied from `.ufo/watchdog.log`):
`2026-11-05T17:43:02-03:00 launch revenger round=98 pgid=1638586 driver=hyaku-inline attempt=1`;
`2026-11-05T18:37:13-03:00 complete revenger round=98; hyaku-inline attempt=1`.

Outcome: **status ok, not admitted (rejected-honest-stop)**. C2 verifies; C1 is the lane's own
NOT VERIFIED (honest miss). No axis harmed.

## 1. Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report attribution | `git log --format='%an %ae %H %cI' -- .ufo/reports/round-98/revenger.md` (fleet) | `revenger-shokunin revenger@shokunin.local 9bdd6d3f… 2026-11-05T18:36:31-03:00` (before the 18:37:13 completion line) | ok |
| SHONEN heading | report `## SHONEN` vs `git show 5498390:SHONEN.md \| grep -nE '^\s*- \['` | 4 boxes in SHONEN.md (lines 5, 17, 22, 25), 4 `[~]` lines in the report, same order | ok |
| cited commits are ancestors of `main` | `git merge-base --is-ancestor <h> main` for 34c56f9, 9d49002, cf8a9d4, 0146c0a, 1b76b4d, 5d9b087, af91e9d, f5dc6f8, 5498390 | all 9 `anc` | ok |
| lane pushed, clean | `scripts/hyaku/jj-lane.sh state …/revenger-shokunin` | `branch=main local=5498390… remote=5498390… ahead=0 behind=0 head=detached tracked=0 untracked=0` | ok |
| leftovers | `git status --porcelain` (lane) | empty | ok |
| remote tip | `git ls-remote origin refs/heads/main` | `5498390e2faf92e2bbb4fa5d35dbe50b070dbb94` | ok |
| round commits | `git log --format='%h %an' 34c56f9..5498390` | 8 commits, all `revenger-shokunin` | ok |
| prompt fidelity | `diff templates/round-prompt.md <prompt §1–§5>` | 22 diff lines = 11 placeholder lines substituted (`{{LANE}}`, `{{ROUND}}`, `{{FLEET_ROOT}}`, `{{AXES}}`), no other change; §6 hyaku addendum present (`.ufo/prompts/revenger-round-98.md:141`) | ok |
| gate registry home | `git show 5498390:SKILL.md \| grep -n c1_k_admit_counter7\|forge_reach7` | registry rows at `SKILL.md:622–630` (name, entry command, pinned-value path) | ok |

Conformance defects: none blocking. Note: the report cites amendments by short hash
(`cf8a9d4`, `0146c0a`, `1b76b4d`); all resolve uniquely.

## 2. Claims — re-measured vs evidence-verified

### C1 — coverage, K 13/15 → 14/15 (target); reported NOT VERIFIED

Re-measured (plain counts over committed bytes):
- `git show <c>:corpus/README.md | grep -cE '^\|[[:space:]]*C[0-9]+.*\|[[:space:]]*held[[:space:]]*\|'` → `34c56f9`: **13**, `5498390`: **13**.
- C14 row at `5498390`: `corpus/README.md:61` ends `| partial |`.
- Candidate entry header at `5498390`: `admission-status: candidate`.
- `git diff --stat 34c56f9 5498390 -- PROVINCE.md corpus/QUALITY.md corpus/README.md` → empty.
- `CriticR98.json` decisions: `Q11 FAIL`, `Q16 FAIL` (python json read of `reports/round-98/votes/CriticR98.json`).

Evidence-verified (lane-owned gate `c1_k_admit_counter7.py`, not executed here — §Gate standard):
- `controls/c1-v7/diag-landing.log`: `C1_K_HELD_BACKED=14/15`, `C1_VOTES_WHY=vote CriticR98 decision Q11='FAIL'…`, `C1_VOTE_NOTES_WHY=ReviewerBlind.json:Q17…; ReviewerGate.json:Q01…`, `C1_VERDICT=fail`.
- Controls: `do-nothing.log` 13/15 fail; `junk-row.log` 14/15 fail (`C1_TARGET_CITES=fail`).
- Self-test: `controls/selftest-v7-frozen.log` → `SELFTEST_C1V7=OK legs=55`, `# rc=0`, measured at clone `5d9b087`.
- Frozen bytes: `git diff --stat 5d9b087 5498390 -- reports/round-98/c1_k_admit_counter7.py reports/round-98/forge_reach7.py reports/round-98/forgeries7` → empty; counter sha256 `59c9930ae864ce826e9f468b4b76bdef33de7ae5e6760eda4d88db4eab2e8548` (matches the report's `59c9930a…`).

Ruling: reported value 13/15 → 13/15 **matches**. The claim did not verify; the lane stopped honestly
(no flip, candidate kept). Coverage axis **unchanged**.

### C2 — calibration, v6 accepts 5/5 routed r97 holdout forgeries → v7 `c02` 0/5

Evidence-verified (lane-owned harness/gate; not executed here):
- `controls/c2-v7-frozen.log` (header: clone detached at `5d9b087`): `C2_ACCEPTED=0/5`, `C2_POSITIVE=pass`,
  `C2_POSITIVE2=pass`, `C2_STUB_SELFTEST=ok`, `C2_ROWSET_FR06=C1_ADMITTED_UNION,C1_ROWSET,C1_VERDICT`,
  `C2_ROWSET_FR07=` same, `C2_VERDICT=met`, `# rc=0`. Committed in `f5dc6f8`, after the `5d9b087` freeze.
- Before: `controls/v7-dev/harness-v6.log` → `C2_ACCEPTED=5/5`, `C2_VERDICT=not-met`, `rc=0`;
  `controls/c2-do-nothing-v6-holdout.log` ends `BUILD_OK=True vectors=15 accepted=5`.
- Single-run outputs (r97 routed item 6.2) are all printed in the one log: confirmed.

Ruling: reported 5/5 → 0/5 **matches**. Calibration **improved** on the frozen predicate. Caveat kept:
development-set result; the fresh r98 holdout shows parity, not gain (c02 5/6 under v6 and v7; c14 4/6),
per the lane's own `L1-holdout-v7/` logs as reported.

### No-harm (owned axes)

- `SCORECARD.md` diff `34c56f9..5498390`: append-only (one `## Round 98` section, 23 added lines, 0 removed).
- C02 held on the landing tree: `controls/measured-at-landing/c02-landing-f5dc6f8.log` → `C1_K_HELD_BACKED=13/15`,
  `C1_VERDICT=pass`; `v6-landing-f5dc6f8.log` → same (evidence-verified).
- S505 correction withheld rather than landed, because it would break C02's S504 → S505 chain — a no-harm call I agree with.

### Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| coverage | unchanged | README held 13 → 13; C14 `partial`; candidate not admitted |
| calibration | improved | C2 frozen-run log 0/5 vs v6 5/5, positives pass, self-test OK (evidence-verified) |
| depth | unchanged | no admitted entry changed |
| freshness | unchanged | no admitted entry re-verified |
| operability | unchanged | SKILL.md gained probe/registry blocks only |
| adjacency | unchanged | PROVINCE.md byte-unchanged |

## 3. Discernment spot-check

| item | lane decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S506 row (curation admit, `mined`, tier A) | admit | `curl -sSfL https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/connection-and-recovery.md` → 16650 bytes, sha256 `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50`; `grep -c -F` of the quote → 1; `head -c 7202 \| tail -c +7127` prints the sentence | agree | pinned revision, byte-identical to the receipt; quote verbatim at the stated bytes; the scope cell limits it to what the reference states |
| C14 candidate `round-98-rea-host-readiness.md` | reject (not admitted; critic Q11/Q16 FAIL) | `corpus/live/runs/round-98/rea-doctor-r98.txt`: `grep -c '^    paths\[3\]: '` → 1 (line 316 holds three comma-separated paths); entry `:83` derivation records `1` and `1`; `grep -c '12\.1\.4'` → host-probes-r98.txt **0**, rea-doctor-r98.txt **17**; entry `:67-69` credits version strings to the probe transcript | agree | the number three is true, but the recorded derivation does not print it (Q11); the 12.1.4 version is attributed to a transcript that never prints it (Q16). Both are real derivation-hygiene defects under the lane's own §Q bar |
| S505 used-by correction | reject (withheld) | `git show 5498390:corpus/knowledge/round-96-native-analysis-sessions.md \| grep -c S505` → 0; `grep -c S504` → 3 | agree | S505's used-by is indeed ungrounded; unmarking it would break the C02 chain; routing a grounding-by-citation fix is the right call |

New SOURCES row check: S507 (`corpus/SOURCES.md:524`) quote `healthy: false` / `environment_healthy: false`
— 4 words (≤25). `git show 5498390:corpus/live/runs/round-98/rea-doctor-r98.txt | head -c 41` prints
exactly those two lines. S506 quote: 11 words (≤25), verified above.

Census: `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
→ exit 0, `21 × W01`, `13 × W04`, 0 E-codes, `revenger ok …/corpus/SOURCES.md`. Rows
`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md`: `34c56f9` 505 → `5498390` 507.

## 4. Trend verdicts

- **expansion: unchanged** — no entry admitted; K 13 → 13; S506/S507 are pending ground for a candidate.
- **quality: unchanged** — no admitted entry superseded or re-verified.
- **discernment: improved** — the outside spot-check agrees with the gate on an admit (S506) and two
  rejects (C14 candidate, S505 correction); v7 refuses the five routed forgeries by named legs. Caveat:
  the fresh holdout shows no generalization (c02 5/6 v6 = v7).

## 5. Routed defects (lane must fix in r99)

1. C14 candidate: derive "three installation paths" with a command that prints 3 (count paths, not lines) — Q11.
2. C14 candidate: attribute `ghidra-version 12.1.4` to the doctor record, or fix the preamble — Q16.
3. Vote notes: ReviewerGate PASS notes Q01–Q05, Q09, Q10 are empty, ReviewerBlind Q17 is n/a-style (`C1_VOTE_NOTES`); re-vote on a fresh digest.
4. S505: ground by citation through a superseding C02 entry revision (still ungrounded: 0 mentions).
5. mutate7 self-test baseline exited 3 while `selftest-v7-frozen.log` reports OK — reconcile the two before citing a self-test detector number; `d-host` survivor still open.
6. v8 legs for r98 holdout survivors (c02 V01, V02, E01, E02, E03; c14 R01, V02, O01, L01).
7. Carried: M4 `claude-red-re-bridge.md` index-or-reject; M7 SCORECARD line; L0 assimilation id collision (155/155).

Operator note: the four SHONEN boxes are all `[~]` and look checkable by a non-author from committed
evidence (probe blocks run on a clean clone, `rea` trial reproduced, PROVINCE unchanged); promotion is operator-owned.
