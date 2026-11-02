# round-84 verifier spot-check — revenger (hyaku run 23)

author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

Closed at lane tip `5cdebb13713aa20778f3c6b5231c74dd3ba9a590` (branch `main`,
pushed: local `refs/heads/main` == `git ls-remote origin refs/heads/main`).
Base `54a36bca7bc52d528026ca28beb51f4cab98fa69`. This judge did not author
the round; every load-bearing value below was re-derived first-hand from
committed bytes (`git archive <sha> | tar -x` extractions under a fresh
scratch dir; no checkout, no mutating git anywhere; the lane-authored files
were not edited).

## 1. Step-1 conformance

| check | result |
|---|---|
| report committed in fleet repo by lane identity | PASS — `git log --format='%an %H' -1 -- .ufo/reports/round-84/revenger.md` → `revenger-shokunin 554117d171b85826b73fc910b0f4db6fb77b245d` (2026-11-01T22:45:44-0800, after the adjudication commit 2026-11-02T06:34:31Z — landed last) |
| `SHONEN` heading | PASS — `## SHONEN` with four `[~]` lines, each with a resolvable pointer |
| cited lane commits exist and are ancestors of main | PASS — `git merge-base --is-ancestor` OK for `67e1470e5b24`, `45c8b42fe4f7`, `d77f997428b7`, `8e21e8f238dc`, `f3d3902e830c`, `5cdebb13713a`, and base `54a36bca7bc5`; chain is linear `54a36bc → 67e1470 → 45c8b42 → d77f997 → 8e21e8f → f3d3902 → 5cdebb1` |
| lane tip pushed | PASS — local `refs/heads/main` = `5cdebb13713a…` = `ls-remote origin refs/heads/main` |
| round work reachable `54a36bca..5cdebb1` | PASS — all six round commits in `git log` of the range; dispatch/complete digest (orchestrator watchdog): launch 2026-11-01T19:34:56-08:00, complete 2026-11-01T22:45:44-08:00 head=5cdebb13713a pushed=True |
| dispatch prompt carried the contract | PASS — `.ufo/prompts/revenger-round-84.md` embeds the mission/axes binding, claims contract (1–3, distinct axes, falsifiable before→after, lowest-axis rule + stagnation nudge), frontier step, report contract with section order, commit-then-push, push scope, L0, §9 sizing (FRESH-START §7 gate), §10 assimilation, honesty rules |
| report not a marker | PASS — real work: two committed producer records, two instruments, five round commits, receipts; minimum content present (work, landed changes, before→after with counting commands, sources & frontier, trends, SHONEN) |

## 2. Claim re-checks (all RE-MEASURED from committed bytes)

### C1 — coverage, criterion A1v2 3/5 → 5/5 (RE-MEASURED)

Instrument identity: `git show 5cdebb1:reports/round-84/ag_probe2.py | sha256sum`
= `f9772ab1428ebe6e420ef285f2d9a02b26372c5556e8404ba825349f04721990`
(== claims.md erratum pin); freeze-time v2.0 at `45c8b42` =
`6e1c07b568d982331c8ce17e9bdb659178066a68d2f44fa1e1e51fec8a71d1e1` (== frozen pin).

- RED: `PYTHONUTF8=1 python -I -B reports/round-84/ag_probe2.py <archive 54a36bca>/corpus`
  → `A1V2_RECORDED=3/5 score=6.00`, `extract_artifact=unrecorded`,
  `inspect_artifact=unrecorded`, exit 0. Matches committed `ag2-red.log` +
  `ag2-red-v21.log` (values unchanged across v2.0→v2.1, as the erratum states).
- GREEN: same over the landing archive `8e21e8f2` →
  `A1V2_RECORDED=5/5 score=10.00` with `extract_artifact=extract-artifact`,
  `inspect_artifact=inspect-artifact`, exit 0. Matches `ag2-after.log`.
- Frozen holds over the same landing archive: `python -I -B reports/round-82/ag_probe.py`
  → `A1_RECORDED=3/3 score=10.00`; `python -I -B reports/round-81/f_probe4.py`
  → `F4_COVERAGE=10/11 score=9.09`. Both hold, as claimed.
- Oracles re-run over committed bytes:
  `python -I -B corpus/fixtures/arc-r84/oracle_check.py truth.json corpus/live/runs/round-84/inspect-artifact/inspection.json R84Sample.zip`
  → `ORACLE OK (36/36 checks)` exit 0; extract sibling →
  `ORACLE OK (31/31 checks)` exit 0. BYTE checks re-derive from the fixture
  (observed in output: per-entry names/sizes/shas, root sha == fixture sha);
  HYP checks are the pre-registered Q07 predictions; producer-internal ids
  FORM-only — the oracle's own printed check list confirms this split.
- Producer receipts: `inspect` `exit_code 0`, `stderr_bytes 0`,
  Evidence `ev_753cfca9daf92857826b62400bd2f4b09ba6cbb4670fd449e3250c246ca138ba`;
  `extract` `exit_code 0`, `stderr_bytes 0`,
  Evidence `ev_07e34a9493848c91095a3355069907df24449999088c87a558b45f8d33c77467`;
  both `fixture_sha256` = `f1f983ef…bc59`. stderr files on disk: 0 bytes each.
- Fixture: `R84Sample.zip` 508 bytes, sha256
  `f1f983eff6823a4ba23d714b25b69ca8e64484ddc00ec24043210311d729bc59`;
  `truth.json` 1445 B / `0dcdf82c…4703`; `build_zip.py` 6637 B /
  `03ddcbdc…230f`; `oracle_check.py` sha `230c359c…5969` — all match claims.md pins.
  Regen: `python -I -B build_zip.py selfcheck <scratch>/R84Sample.zip` →
  `SELFCHECK 17/17` exit 0 and the rebuilt bytes are byte-identical to the
  committed blob (`cmp` clean, same sha256).
- Denominator disclosure re-opened live: `rea capabilities` → provider
  `rea-artifact-graph`: triple + `extract_artifact,inspect_artifact` all
  `available: true`; `inspect_asset_catalog` `available: false`
  `availability_code: unsupported_host` — exactly five available operations.
- **Erratum correction ordering verified (pre-after-run):** `ag_probe2.py`
  exists only at `45c8b42` (v2.0, 05:20:05Z) and `f3d3902` (v2.1, 05:46:05Z);
  the landing commits `d77f997`/`8e21e8f2` (records land) precede the
  correction; `claims.md` delta at `f3d3902` is append-only (0 lines removed,
  16 added — the ERRATUM section); `ag2-red-v21.log` (red re-run) lands with
  the correction; `ag2-after.log` and `c1-only.log` first appear at
  adjudication `5cdebb1` (06:34:31Z) — after the correction. The c1-only
  separability dry-run catching the scan-shape defect before any after-run
  receipt is consistent with the committed ordering; mined in the lesson
  Mistakes row 1.

**C1 verdict: verified — coverage improved (3/5 6.00 → 5/5 10.00 on the
registered v2.1 instrument; holds A1 3/3, F4 10/11 re-printed).**

### C2 — calibration, orphan_sweep v5 supersession (RE-MEASURED)

Instrument identity: committed blob re-hashed =
`d9a7ba174ce3c30a4414fcebe8e074ea00d58bfce4cfbf2c2cdb76f888ca46cb` (== pin);
v4 blob at tip unchanged `f520f8d69875d1ca83eb8daeddbffecb5f471bf5f5e6aba43bd97029fc2ea701`
(the FULL sha per corrections.md; the r83 surfaces' `…9701` suffix drift is
real — see §5).

- Selftest from the committed blob: 18 `=ok` legs + `SWEEP_SELFTEST=pass`,
  exit 0 — reproduces `sweep5-selftest-after.log`.
- Three frozen one-substitution sed mutants (recipes in claims.md), each
  verified one-substitution by diff, each re-run: exit 1 with the attributed
  last line — `selftest: bare-filename classification drifted (bare-token
  class)` / `selftest: unmatched-absent recording drifted (unmatched-absent
  class)` / `selftest: log-corpus collection drifted (log-corpus class)`.
  Reproduces `sweep5-mutant-kill-after.log`.
- Red pair over ONE tree (committed receipts): `v4-invisible-red.log` —
  `SWEEP_BARE_TOKENS matched=302 unmatched_skipped=1408`, `CITED=705`,
  no bare-token row for `v4-postlanding-recon.log` (the only instrument row
  naming the token is the PATH-form absent row at line 637, from the r83
  verifier lesson's path-form citation — see defect note D1);
  `v5-red-unmatched-absent.log` — same tree, line 973
  `SWEEP absent v4-postlanding-recon.log | bare-token unmatched: no file
  named v4-postlanding-recon.log under HEAD or the working tree`,
  `unmatched_recorded_absent=47`, `SWEEP_CORPUS fleet-reports=24 lessons=48
  log=1`, `CITED=987` — the 705→987 and 13→60 (13+47) movements verify.
- Real-tree receipt `sweep5-real-after.log`: row 974
  `SWEEP committed v4-postlanding-recon.log | bare-token normalized:
  reports/round-83/v4-postlanding-recon.log`, no absent row names it;
  `LANDABLE_ORPHANS=3` exit 1 with the three conservative-ambiguity rows
  (`c1-only.log`, `c2-only.log`, `noharm-diff.txt` vs their committed
  r81/r82/r83 twins), corrected by the appended post-run note — the honest
  expectation for a pre-adjudication-text tree, exactly as disclosed.
- **Judge's own committed-tree sweep at closure** (committed blob, lane
  worktree at tip + fleet root): exit 0,
  `SWEEP committed v4-postlanding-recon.log | bare-token normalized: reports/round-83/v4-postlanding-recon.log`,
  `SWEEP_CORPUS fleet-reports=25 lessons=49 log=1`,
  `CITED=1024 COMMITTED=964 LANDABLE_ORPHANS=0 ABSENT=60`,
  `ORPHAN_SWEEP_LANDABLE=0`. The load-bearing values (LANDABLE_ORPHANS=0,
  ABSENT=60, exit 0, token committed) reproduce. The absolute CITED/COMMITTED
  differ from the report's post-adjudication prose values (1015/955, basis
  fleet-reports=24) by exactly the post-adjudication basis movement: the r84
  report itself landed in the fleet repo (554117d1, 06:45Z) after the
  adjudication (06:34Z), moving fleet-reports 24→25 — the instrument's
  basis-line-first discipline discloses this by design (see defect note D2).

**C2 verdict: verified — calibration improved (v5 changes 7–8 in the
standing instrument, selftest- and mutant-checked, both routed r83 gaps
machine-caught; no criterion score moved, none claimed).**

### Carry-in at 67e1470 (VERIFIED, full provenance)

- `reports/round-83/v4-postlanding-recon.log` landed at `67e1470`; header
  discloses the regeneration recipe (fresh scratch repo, HEAD = `60693f2`
  via fetch+update-ref, no checkout; disk = exactly the seven r82 carry-in
  receipts extracted from `60693f2`'s tree; instrument = the COMMITTED v4
  blob with the full sha; basis movement fleet-reports 23→24, lessons=0).
- Tail: `SWEEP_CORPUS fleet-reports=24 lessons=0`,
  `CITED=423 COMMITTED=405 LANDABLE_ORPHANS=0 ABSENT=18`,
  `ORPHAN_SWEEP_LANDABLE=0`, `exit_code=0` — the load-bearing values the
  five citing surfaces carry reproduce.
- `.ufo/waves/round-84/carryin-byteverify.log`: 7/7 MATCH; all seven short
  shas (`ab918d9416ce`, `ac453532a40a`, `6fb40a0823cf`, `7df70651ce8a`,
  `a0bb189bcb00`, `7c962f3dd6a3`, `3d8edb2cfc2e`) cross-checked against the
  r83 lesson pins — identical.
- `reports/round-84/corrections.md`: correction 1 names the five
  `f520f8d6…9701` drift sites (fleet report ×1 — orchestrator-committed,
  corrected by pointer; `corpus/lessons/round-83.md` ×2 at lines 125/186;
  `SCORECARD.md:1183`; `LOG.md:1178`) — grep confirms 2/2/1/1 lane-side
  occurrences; the true suffix `…c2ea701` re-derived by this judge's own
  hashing. Correction 2 resolves the `census-round-start-sanctioned2.log`
  pointer three ways; this round's exit-0 re-run receipt is committed
  (21 W01 + 10 W04 — re-counted by this judge, see §4). Correction 3 is the
  regeneration itself. Append-only, no in-place rewrite of any r83 surface.
- Round-start census receipts landed in the same commit
  (`.ufo/waves/round-84/census-round-start-{sanctioned,literal}.log`).

### No-harm (RE-DERIVED)

- `git diff-tree -r --numstat 45c8b42 8e21e8f2` → 15 files (1 M
  `corpus/SOURCES.md` + 14 A), **704 insertions, 0 deletions** — additions
  only, matching `noharm-diff.txt`.
- Protected instruments `orphan_sweep[1-4].py`, `ag_probe.py`, `f_probe4.py`
  absent from the full range name-list (`54a36bc..5cdebb1`) — verified empty.
- `PROVINCE.md` diff `45c8b42..5cdebb1` — empty (0 lines).
- `SCORECARD.md` diff `54a36bc..5cdebb1` — append-only round-84 section
  (no prior content touched).
- `LOG.md` delta across the round: 0 deleted lines (append-only).
- Freshness hold: `grep -cE '^\| [FK][0-9]+ .*\| (holds|STALE)'` → seed.md 12
  + readiness 6 = 18/18 (matches `noharm-diff.txt` FRESH_ROWS).
- Landing-no-op story verified: `d77f997` carried ONLY `corpus/SOURCES.md`
  (the treecommit directory-args no-op — mined); `8e21e8f2` lands the 14
  fixture/record files explicitly.
- Separability receipts read: `c1-only.log` (base `67e1470` + C1 files only:
  A1v2 5/5 + oracles OK, v5 ABSENT) / `c2-only.log` (base + v5 only: selftest
  pass, fixture/records/ag_probe2 ABSENT) — causally separable as frozen.

## 3. Per-axis verdicts

| axis | verdict | evidence |
|---|---|---|
| coverage | **improved** | C1 re-measured: A1v2 3/5 (6.00) → 5/5 (10.00); F4 10/11 hold re-printed (android hard-gate re-derived: `REA_JADX_MCP_JAR` UNSET, no jadx on PATH — this judge's own probes agree); K 8/15 untouched |
| calibration | **improved** | C2 re-measured: v5 selftest 18/18, three attributed mutant kills, red pair + resolved token, judge's own sweep LANDABLE_ORPHANS=0 exit 0 |
| depth | unchanged | no claim; `corpus/knowledge/` untouched in the range; no engine-readiness claim (Q10 scope notes intact) |
| operability | unchanged | no capability row added; instruments run from committed bytes (verified above) — the standing capability, superseded in place |
| freshness | unchanged | 18/18 hold rows re-counted; knowledge files untouched |
| adjacency | unchanged | PROVINCE byte-unchanged (diff empty); records scoped to the observed family/operations/authored input; ADJ-06 unchanged |

## 4. Discernment spot-check (non-author, outside)

Sample: 3 admits (all three new SOURCES rows — the round opened only admits)
+ 2 rejects (the round's §7 ruling-outs, the Gate's reject-shaped decisions;
the Gate table itself carries no rejected source rows this round).

| item | decision | re-opened source (this judge, first-hand) | agree/disagree | reason |
|---|---|---|---|---|
| S466 provider surface | ADMIT (tier A, own-work) | ran `rea capabilities` + `rea extract-artifact --help` live | **agree** | the ≤25-word Gate quote "Extract regular contents of supported artifacts; DMG extraction is unavailable" (10 words) prints verbatim in the --help summary; capabilities prints the five-operation available set with `inspect_asset_catalog` unsupported_host — the A1v2 denominator is real |
| S467 producer records + fixture | ADMIT (tier A, own-work) | oracle re-runs over committed bytes (36/36, 31/31 exit 0); receipt fields + stderr sizes re-read; regen byte-identity re-run | **agree** | the records exist, are oracle-checked, and every pinned sha/Evidence id matches; tier A own-work is the correct scope |
| S468 unmatched-bare-citation class | ADMIT (tier A, own-work) | read both red receipts; located the quoted row (v5-red line 973) verbatim | **agree** | the class evidence is real (v4 skips the bare token, v5 records it) and grounds exactly the C2 move it claims |
| F android family | REJECT (ruled out — hard-gated) | `echo ${REA_JADX_MCP_JAR:-UNSET}` → UNSET; `command -v jadx` → not found (this judge's own fresh probes) | **agree** | S448's standing disposition holds on this host; F4's 10/11 honest exception is correct, and declining to claim F was right |
| macho/signature providers | REJECT (ruled out — unsupported_host) | `rea capabilities` live: native-macos groups `available: false` `unsupported_host` | **agree** | the families are unavailable on this host; ruling them out (not claiming them) is honest calibration |

Census: contract-literal form (`validate --root <fleet-root> revenger`)
→ exit 2 `missing …/revenger-shokunin/corpus/SOURCES.md` (the lane's repo
dir is `shokunin-binary-forensics` — the disclosed r74–r84 literal-form
lineage); sanctioned explicit-lane-dir form → **exit 0, verdict `ok`**
(21 W01 + 10 W04 re-counted, zero E — identical composition to the round's
round-start receipt and census-after.log). SOURCES registry: 468 rows
(counting command `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
corpus/SOURCES.md`), 0 malformed (NF=13), S466–S468 sit inside `## Registry`
directly after S465 (lines 483–485, before `## Paths` at 487) — the E12 ×3
placement defect is resolved in the adjudication as disclosed.

## 5. Trend verdicts

- **expansion: improved** — A1v2 3/5 → 5/5 re-measured (record ground the
  r81/r82 scorecards named "available-but-unrecorded" now held, sourced by
  mined rows S466+S467); F hard-gated unchanged; K untouched. Consistent
  with the r80–r83 closure precedent for criterion-move rounds.
- **quality: improved** — the registration carries a pre-run denominator
  disclosure (re-opened live), a byte-vs-hypothesis oracle split, a
  separability pair, and a no-harm receipt — all re-derived; the two routed
  instrument gaps became selftest+mutant-checked v5 classes; the
  instrument's own scan-shape defect was caught by the round's
  separability machinery before any after-run receipt (ordering verified).
  No admitted entry failed a re-check.
- **discernment: improved** — seven mined mistakes verified real against
  committed evidence (the v2.0 scan-shape catch with verified commit
  ordering; the `d77f997`-carries-only-SOURCES.md landing no-op verified
  from the commit tree; the S468 NF defect resolved — 0 malformed rows
  re-counted; the census timeout, heredoc truncation, count-from-intent
  (claims.md carries the measured 6637) rows all receipted); the real-tree
  receipt's expected-GREEN disagreement is corrected by a post-run note in
  the receipt itself. Outside spot-check (this document): 5/5 agree.

## 6. Routed defects for next round (all status-neutral)

- **D1 — report prose imprecision.** The report's C2 bullet says v4 shows
  "ZERO instrument rows name the bare-cited `v4-postlanding-recon.log`";
  `v4-invisible-red.log` line 637 does record the token's PATH-form twin
  (`SWEEP absent reports/round-83/v4-postlanding-recon.log`, cited by the
  r83 verifier lesson). Zero holds only of the bare-token class —
  `claims.md` states this exactly ("its PATH-form twin … WAS recorded, as
  an absent row"). Fix: future prose quotes the class precisely or cites
  claims.md's wording. Substance unaffected; the red/green contrast
  verifies.
- **D2 — post-adjudication sweep absolutes live only in report prose.**
  `CITED=1015 COMMITTED=955` (basis fleet-reports=24) appears in the
  report's C2 bullet and CLOSURE-PREP but in no committed lane receipt; the
  closure-time re-run over the current trees prints CITED=1024
  COMMITTED=964 with basis fleet-reports=25 (the r84 report joined the
  fleet corpus after the adjudication). The per-revision-corpus rule
  absorbs this, but the CLOSURE-PREP absolute is not reproducible verbatim
  at any later date. Fix: land the post-adjudication verification receipt
  as a committed file next round (the lane already does this for every
  other receipt).
- **D3 — literal census form vs repo dir name.** The contract's literal
  census command resolves the revenger registry at
  `<root>/revenger-shokunin/corpus/SOURCES.md`, which does not exist (the
  lane repo dir is `shokunin-binary-forensics`), so the literal form exits
  2 while the sanctioned explicit-lane-dir form exits 0. Disclosed lineage
  r74–r84; operator-side if the conf-id→dir mapping is ever consolidated.
- **D4 — SHONEN boxes.** All four boxes look fully checkable by a
  non-author at `5cdebb1` (SKILL.md unchanged with cited tables; the
  end-to-end task is oracle-checked and committed; instruments run from
  committed bytes with declared exits; PROVINCE byte-unchanged). This
  judge wrote no `[x]` (non-author `[x]` is a promotion-review act, not a
  closure act) — surfaced for the operator to direct the r69-outstanding
  review (`corpus/lessons/round-69-verifier-spotcheck.md` routed need).

**Closure: status ok, admitted=true.** Both claims re-measured first-hand;
no axis harmed; the seven r83 carry-in receipts' regeneration provenance
verified in full; the pre-after-run erratum ordering verified from commit
metadata and append-only diffs.
