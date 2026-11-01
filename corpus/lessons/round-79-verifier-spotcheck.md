author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

# revenger round 79 — non-author verifier spot-check (closure)

Closed against lane HEAD `abc522d2f7c06cbf641afcf99475299586aae207` (branch tip, pushed;
`ls-remote origin refs/heads/main` returns the same hash). Base `c205ef83ca3f`, freeze
`34c2c5a1dc7`, landing `95e50032a64`. All re-measurements below were run by this closure
judge from committed bytes only (`git archive <commit> | tar -x` into a scratch dir — no
worktree checkout; the host's git index was never touched; no mutating git anywhere).

## 1. Step-1 conformance

| check | result |
|---|---|
| report committed in fleet repo by lane identity | OK — `git log --format='%an %H' -1 -- .ufo/reports/round-79/revenger.md` → `revenger-shokunin cf582d855b8ffd632cf095c826cccba09be58c93` |
| `SHONEN` heading | OK — `## SHONEN` with four `[~]` lines, one per box, each with a resolvable pointer; no author `[x]` |
| cited lane commits exist and are ancestors of `refs/heads/main` | OK — `c205ef83ca3f`, `34c2c5a1dc7`, `95e50032a64`, `abc522d2f7c0` all `cat-file -e` + `merge-base --is-ancestor` = OK |
| lane tip pushed | OK — local `refs/heads/main` = `abc522d2f7c0…` = `ls-remote origin refs/heads/main` |
| cited work reachable `c205ef83..abc522d2` | OK — three commits, all authored `revenger-shokunin` (freeze / landing / adjudication) |
| dispatch/complete digest vs `.ufo/watchdog.log` | OK — line 156 `2026-11-01T01:44:09-08:00 launch revenger round=79 base=c205ef83ca3f (zcode run14)`; line 177 `2026-11-01T03:22:30-08:00 complete revenger round=79 head=abc522d2f7c0 pushed=True` |
| marker vs report | real report — work performed, evidence pointers, landed changes tied to LOG.md, checkable hashes |
| prompt fidelity | dispatched prompt embeds the operative contract (mission/axes binding, L2 floor with host disclosure, commit-then-push ordering, push scope, L0 channel, report path, SHONEN requirement, hash-citation rule, write scope) — no missing item observed |

## 2. Claim C1 — coverage: ninth F family `native-authenticode` (re-measured)

Instrument identity: `sha256 reports/round-79/f_probe2.py` at `abc522d2` =
`0be0d8b5ac131963f273e296c6c2822d277614d634db25b559256f4744e4cc12` = the freeze pin in
`claims.md` (unchanged landing→final). The eight round-1 families + predicate are
repr-equal to `reports/round-76/f_probe.py` (`e15a43af…`, verified by dict compare: 8
common entries byte-equal, exactly one addition `native-authenticode: {inspect_pe_certificates}`).

Before→after, re-run by this judge (commands as in `claims.md`, over `git archive` corpora):

| run | command | observed |
|---|---|---|
| before | `python -B reports/round-76/f_probe.py <base>/corpus` | `F_COVERAGE=7/8 score=8.75` |
| before | `python -B reports/round-79/f_probe2.py <base>/corpus` | `F2_COVERAGE=7/9 score=7.78`, native-authenticode absent |
| after | `f_probe.py <landing>/corpus` | `F_COVERAGE=7/8 score=8.75` (frozen eight hold) |
| after | `f_probe2.py <landing>/corpus` | `F2_COVERAGE=8/9 score=8.89`, `F2_FAMILIES=[… 'native-authenticode']`, counter carries `inspect_pe_certificates: 1` |

Both outputs byte-match the committed receipts `f2-before.log` / `f2-after.log`.

Identity oracle re-run from committed bytes:
`python -B oracle_check.py truth.json <landing>/corpus/live/runs/round-79/inspection.json fixture.dll`
→ `ORACLE OK (27/27 checks)`, exit 0. Chain verified: `fixture.dll` sha256
`813778b9d97cf74f2aa5ba1c963cecba5c91ba72adebc08b50d7ec8b3196cf80` = `truth.json` = receipt
`fixture_sha256` = record `subject.digest.sha256`; `inspection.json` sha256
`317b0b744f6d18725387cedc73085edb6b197c22de800e2ba731842397447b79` = receipt
`stdout_sha256`; `evidence_id` `ev_3701e3a16f9581ec…52fcc` matches; stderr 0 bytes; exit 0.
Regen: `python -B generator.py regen-check.dll && cmp fixture.dll regen-check.dll` →
byte-identical; the generator's self-check re-derives every oracle-checked premise from the
built bytes (no network/exec primitives in the generator — inert structural bytes only).
Producer reproduction (bonus, read-only static run on the committed fixture): every
substantive field of a fresh `rea inspect-pe-certificates` run (format, machine, table,
entries, coverage, subject digest, operation, provider `rea-pe-certificates`) equals the
committed record; the envelope `evidence_id` differs per-run as designed (the committed
run's id is pinned by its receipt).

Denominator-risk disclosure pre-run: `f_probe2.py` header ("A tree with the eight old
families held and the new family absent scores 7/9 (7.78) - LOWER than the frozen
instrument's 7/8 (8.75)") and `claims.md` §Boundary, both committed at freeze `34c2c5a1`
BEFORE the landing/adjudication after-runs. Verified present at the freeze commit.

Separability re-derived by this judge from constructed trees (matches `c1-only.log` /
`c2-only.log`): C1-only (base + fixture/record + f_probe2) → `F2_COVERAGE=8/9` with the
selftest probe still red (0/2 ×3, exit 1); C2-only (base + v2 instruments, no record) →
selftest probe green (2/2 ×3, exit 0) with `F2_COVERAGE=7/9`.

**C1 verdict: verified — coverage improved.**

## 3. Claim C2 — calibration: §Gate-standard self-tests for both gates (re-measured)

Instrument identity at `abc522d2` (all = freeze pins, all unchanged landing→final):
`gate_probe2.sh` `e2b71649faf34000…aead`, `receipt_probe2.sh`
`076cdb67a4bb1dc5…d9d9`, `selftest_probe.sh` `4126af12767d1968…2e1e`; v1 bytes frozen:
`gate_probe.sh` `a594b57f…`, `receipt_probe.sh` `9315f8d8…`.

`bash reports/round-79/selftest_probe.sh <gate> <receipt>`, re-run by this judge:

| pair | SELFTEST_MODE_PRESENT | SELFTEST_MUTANT_KILLED_ATTRIBUTED | USAGE_EXIT64 | exit |
|---|---|---|---|---|
| v1 (base archive) | 0/2 | 0/2 | 0/2 | 1 (red) |
| v2 (final archive) | 2/2 | 2/2 | 2/2 | 0 (green) |

Both runs match `selftest-before.log` / `selftest-after.log`. Visible selftest legs re-run:
gate2 → `GATE_SELFTEST_COMPARATOR_EQUAL=ok`, `…_MUTANT_FLAGGED=ok`,
`…_FIELD_MISSING_FLAGGED=ok`, `GATE_SELFTEST=pass`, rc 0; receipt2 →
`RECEIPT_SELFTEST_LLMS_VERDICT=ok`, `_TOKEN_CHECK=ok`, `_NEGCTL_LOGIC=ok`,
`RECEIPT_SELFTEST=pass`, rc 0 — the stable finding-ids asserted by the SKILL.md registry
rows. Hermeticity: the counting instrument's selftest legs run with the producer's
directory stripped from PATH (no producer call). The sed mutants are byte-changing
(`cmp -s` guard) and die with the attributed last lines
`selftest: blind comparator accepted mutated receipt` /
`selftest: per-leg receipt verdict accepted any count`, exit 1. Unrecognized forms exit 64.

Plain-mode no-drift, re-run by this judge (both over the final archive AND in the lane
worktree): `diff <(gate_probe.sh) <(gate_probe2.sh)` → empty, `diff <(receipt_probe.sh)
<(receipt_probe2.sh)` → empty — criterion G/R verdict bytes did not move (G green; R green
with the LEG4 negative control firing identically under v1 and v2:
`RECEIPT_LEG4=S444_MISMATCH_FLAGGED (base row records 'prints 0'; actual llms leg prints 2)`.
Note: LEG4 prints FAIL/red when run from a bare `git archive` extraction (no `.git` for its
`git show` base-row read) — identical for v1 and v2 at base and final, so no drift and no
harm; in the lane tree both print green). Registry: both v2 rows landed in SKILL.md
`## Gate registry` with verdict maps declaring the usage exit 64, self-test spelling
`--selftest`, committed expected finding-ids, the two-evidences pair, write scope, owner —
the v1 rows stand for the v1 bytes.

**C2 verdict: verified — calibration improved (routed r78 self-test debt closed by
supersession, not re-pinned).**

## 4. No owned axis harmed

- Full-range `diff-tree -r --name-status c205ef83..abc522d2`: 28 files — only LOG.md,
  SCORECARD.md, SKILL.md, corpus/SOURCES.md modified, each a PURE APPEND (0 removed lines
  each by diff grep); 24 files added. Landing range touches only SKILL.md + SOURCES.md
  among tracked files plus new artifacts — protected paths (knowledge, README, verifiers,
  SHONEN, PROVINCE, LOG, SCORECARD, P2/P3, f_probe, receipt/gate v1, r71 counter) empty
  base→landing, matching `noharm-diff.txt`.
- Freshness hold re-run: `grep -cE '^\| [FK][0-9]+ .*\| (holds|STALE)' corpus/knowledge/seed.md corpus/knowledge/2026-10-12-rea-readiness-checklist.md`
  → 12 + 6 = 18/18, exit 0. K 8/15 not re-run (no README/knowledge byte changed —
  confirmed by file list); P3 not re-run (probe + PROVINCE bytes unchanged — confirmed).
- SCORECARD round-79 section carries per-row counting commands, measured commits, and the
  honest boundary (numerator+denominator move together; no capability row added).
- SOURCES rows re-counted: 450 (base) → 453 (final), `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`.

## 5. Discernment spot-check (non-author)

Census re-run by this judge: contract literal form
(`sources-census.sh validate --root <fleet-root> revenger`) → exit 2
(`revenger missing …/revenger-shokunin/corpus/SOURCES.md`) — the disclosed r74–r79
old-host-layout lineage; the consolidation L0 line landed at `.ufo/l0-questions.md:248`.
Sanctioned explicit-lane-dir form (SKILL.md §4a) → **exit 0, 31 W, `ok`** — matches the
committed `census-after.log` (21 W01 + 10 W04, the same disclosed classes).

| item | decision | re-opened source (this judge's own re-open) | agree/disagree | reason |
|---|---|---|---|---|
| S451 admit (own-work producer record, tier A) | ADMIT | re-ran the oracle over committed fixture/truth/record → `ORACLE OK (27/27)`; sha chain receipt↔record↔fixture all equal; regen byte-identical; fresh producer run reproduces every substantive field | **agree** | the record is a real current-producer observation of authored bytes; tier A own-work is correctly scoped (structural identity only, no signature verification claimed) |
| S452 admit (fleet PROTOCOL §Self-test/§Verdict, tier A) | ADMIT | `git show 57fa881f2b8e:PROTOCOL.md` — quote "Every gate exposes a self-invocation mode over isolated fixtures (temp trees, no network, no live-tree write)" found verbatim at line 385; 18 words ≤ 25 | **agree** | quote exact, located, at the pinned checkout; the narrower-scope re-open of S449 is disclosed and cites path+hash (no new W04) |
| S453 admit (producer capability surface, tier A) | ADMIT | re-ran `rea capabilities` live — `inspect_macho`/`inspect_plist`/`list_architectures`/`inspect_signature` all `available: false`, `availability_code: unsupported_host`, "Native macOS utilities require macOS." | **agree** | the availability boundary is exactly as rowed; correctly grounds both the ruling-out and the authenticode route |
| macho/signature F-family route | REJECT (ruled out) | same live `rea capabilities` re-open | **agree** | surface genuinely absent on win32; a do-nothing control reaches the identical state — correctly not claimed |
| F android route | REJECT (ruled out) | re-probed: `REA_JADX_MCP_JAR` UNSET, no jadx on PATH, no `~/tools/jadx*` | **agree** | hard gate unchanged; S448 receipt stands; correctly not claimed |
| K admissions (C05/C10/C15) | REJECT (ruled out) | `.ufo/l0-questions.md:233` — the r74 L0 stands unanswered (no operator reply after it) | **agree** | the wave Q-review surface is absent; honest stop, not silence |

## 6. Trend verdicts (this judge's, with evidence)

- **expansion: improved** — a ninth in-province F family moved from uncovered to held
  through a real, oracle-checked current-producer record on a newly-authored fixture
  (F2 7/9→8/9; v1 7/8 held byte-identically); the ground is documented by mined row S451.
  K untouched, honestly disclosed as operator-blocked — not a trade.
- **quality: improved** — both criterion gates superseded by stronger, §Gate-standard
  self-verifying instruments with attributed kills and a declared usage map, v1 bytes
  frozen with zero verdict drift (plain-mode byte-equal, re-run twice by this judge);
  FRESH_ROWS 18/18 re-verified; no admitted entry failed any re-check.
- **discernment: improved** — three real mistakes mined with captures (`## Mistakes`:
  E12 row position caught by the round-end census; dwLength misalignment and
  observation-as-premise truth draft both self-caught before any committed byte); the
  denominator risk was disclosed at freeze, pre-run; boundaries stated as boundaries; this
  outside spot-check agrees with every sampled gate decision (3 admits, 3 rejects).

## 7. Per-axis verdicts (agree with the closure JSON)

| axis | verdict | basis |
|---|---|---|
| coverage | **improved** | C1 verified (re-measured end-to-end) |
| calibration | **improved** | C2 verified (re-measured end-to-end) |
| depth | unchanged | no claim; no engine readiness claimed (Q05 boundary honest) |
| operability | unchanged | no claim; v1 criterion instruments byte-identical |
| freshness | unchanged (hold verified) | FRESH_ROWS 18/18 re-run by this judge, exit 0 |
| adjacency | unchanged | no cross-domain absorption; ADJ-06 unchanged; PROVINCE untouched |

## 8. Routed defects for the lane next round (all status-neutral; none bars admission)

1. **Number drift in `corpus/lessons/round-79.md` §Census**: the paragraph says round-end
   "32 W", but the committed receipt it cites (`reports/round-79/census-after.log`) and the
   lesson's own §Gate paragraph both say **31 W** (21 W01 + 10 W04 — this judge re-counted
   the receipt and re-ran the sanctioned census: 31 W, exit 0). Correction owed as an
   appended erratum/correction entry next round, never an in-place rewrite.
2. **SHONEN boxes remain `[~]`** (asserted-by-author) with no named non-author verifier —
   the r69 routed need for outside re-confirmation of the CURRENT bytes stands. Flagged
   for the operator's promotion review; per the closure contract this judge does not write
   `[x]`. (The four boxes look non-author-checkable on the current committed bytes.)
3. Carry-in, operator-side, not a lane defect: the closure contract's literal census form
   exits 2 on this host layout every round since r74; the consolidation L0 line landed
   (l0-questions.md:248); the sanctioned explicit-lane-dir form (SKILL.md §4a) exits 0.

## 9. Closure statement

Both declared claims re-measured green by the non-author closure judge from committed
bytes; no axis harmed; trends improved×3; conformance clean except the status-neutral
routed defects above. **revenger round 79: admitted.**
