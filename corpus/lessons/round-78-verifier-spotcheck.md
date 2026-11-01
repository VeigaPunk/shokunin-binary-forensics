# round-78 verifier spotcheck — revenger (hyaku closure, non-author)

author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-binary-forensics` (branch `main`).
Base `9676f52f627c` → tip `1b3664c887ce8df4fcdf17f489f48daa656acc8c`. Report: `.ufo/reports/round-78/revenger.md`.
All commands below were run by this closure judge at 2026-11-01 against committed bytes
(`git show` / `git archive` extractions; the host's git index was never touched).

## 1. Step-1 conformance — all pass

| check | command | result |
|---|---|---|
| report committed by lane identity | `git -C <fleet root> log --format='%an %ae %H' -1 -- .ufo/reports/round-78/revenger.md` | `revenger-shokunin revenger@shokunin.local 2e4265a90459…` — lane identity ✓ |
| report bytes committed = filed | `diff <(git show HEAD:.ufo/reports/round-78/revenger.md) .ufo/reports/round-78/revenger.md` | IDENTICAL ✓ |
| `SHONEN` heading + per-box lines | `git show HEAD:.ufo/reports/round-78/revenger.md \| grep -nE '^## SHONEN\|^- \[.\]'` | `## SHONEN` at :55 with four `[~]` lines; no `[x]` written by the author (correct — only a non-author writes `[x]`; the four boxes remain non-author-confirmable, r69 V7 routed need stands) ✓ |
| cited commits exist + ancestry | `git merge-base --is-ancestor <h> refs/heads/main` for f042b295, 7f303c3d, b7fee90f, 40a16431, 46c605c6, 1b3664c8, 9676f52f | all ANCESTOR-OK ✓ |
| branch tip pushed | `git ls-remote origin refs/heads/main` vs local `refs/heads/main` | both `1b3664c887ce8df4fcdf17f489f48daa656acc8c` ✓ |
| round work in range | `git log 9676f52f..1b3664c8` | 6 commits, all authored `revenger-shokunin`, matching the report's Landed changes ✓ |

No marker predicate: the report carries work performed, evidence pointers, commit-hash citations, trend verdicts and the SHONEN block — a real report, status `ok`.

## 2. Claim re-checks

### C1 — coverage, criterion P revision (instrument P3) — RE-MEASURED by this judge

Setup (all from committed bytes): `git archive 1b3664c887ce8…` extracted to a scratch tree;
`git show 9676f52f:reports/round-75/province_probe2.sh` extracted as the base P2 bytes
(P2 is byte-identical base↔tip — `cmp` clean). Stale fixture built per the committed
harness's own construction: tip `PROVINCE.md` bytes with the `[present on this host,
2026-11-01: CDP browser surface …]` block replaced by the sentinel
`[absent on this host: cdp-browser]`, scaffolded with `.git` + `corpus/training/bounty-triage/MODULE.md`.

| run | command | observed | expected (report) | match |
|---|---|---|---|---|
| A. P2 false-pass from BASE bytes | `bash <base>/province_probe2.sh <fixture-stale>` | exit 0, `P2_SURFACES_RESOLVED=11/11 UNRECORDED_ABSENT=0 STALE_RECORDS=0 P2_SCORE=10.0`, no browser line | `p3-before.log` | ✓ reproduced |
| B. P3 flags the fixture | `bash <tipx>/reports/round-78/province_probe3.sh <fixture-stale>` | exit 1, `cdp-browser  STALE-RECORD (…)`, `P3_SURFACES_RESOLVED=11/12 UNRECORDED_ABSENT=0 STALE_RECORDS=1 P3_SCORE=9.2` | `p3-after.log` run 1 | ✓ |
| C. P3 passes the tip | `bash <tipx>/reports/round-78/province_probe3.sh <tipx>` (archive bytes, committed PROVINCE.md) | exit 0, `cdp-browser PRESENT`, `P3_SURFACES_RESOLVED=12/12 UNRECORDED_ABSENT=0 STALE_RECORDS=0 P3_SCORE=10.0` | `p3-after.log` run 2 | ✓ |
| D. committed negctl end-to-end | `cd <tipx> && bash reports/round-78/p3_negctl.sh <lane-dir>` | `P2_NEGCTL_STALE_BROWSER_FLAGGED=0/1`, `P3_NEGCTL_STALE_BROWSER_FLAGGED=1/1` (exit 1, attributed cdp-browser STALE-RECORD), `P3_NEGCTL_UNRECORDED_PRESENT_GREEN_BY_DESIGN=ok`, `P3_NEGCTL_UNRECORDED_ABSENT_LEG=not-claimable`, `P3_POSITIVE_CONTROL=pass`, `P3_NEGCTL_VERDICT=green`, exit 0 | `p3-negctl-run.log`, `tip-verification.log` | ✓ |

Instrument pins re-hashed from committed bytes: `province_probe3.sh` sha256
`bde7ecd04ed8f9b7b2326f7e8fd7c4d129da73b7c3ad3ee6ef185b06bf77e1f4` (matches the report pin);
`p3_negctl.sh` sha256 `a7f0f6fd846784802a68011a1d3a6c56da660d35c473765bb47145c260a1f54f`
(matches the corrected pin). P3 "carries the eleven v2 checks byte-identically" verified by
diff: the only deltas are the header comment block, the twelfth `check "cdp-browser" …` line,
`total=11→12`, and the `P2_→P3_` summary prefix — all eleven original `check` lines are absent
from the diff. P3 false-passes nothing: the only fixture state it accepts green is the one the
probe's semantics declare green (a PRESENT surface with no record), and that boundary is
disclosed in the harness output itself (`not-claimable`), not claimed as a kill. No PROVINCE.md
byte changed: blob `bd7cd320342c…` identical at base, tip, and across the correction.

### C2 — calibration, gate-registry registration — RE-MEASURED + row conformance checked

Counting commands re-run on committed bytes:

- `git show f042b295:SKILL.md | sed -n '/^## Gate registry/,/^## [^G]/p' | grep -cE '^\| name \|'` → **3**; same at base 9676f52f → **3** (before-state, `registry-before.log` matches).
- Same at tip `1b3664c8` → **5**; `git show 1b3664c8:SKILL.md | grep -cE 'reports/round-7[67]/(gate|receipt)_probe'` → **2** (after-state, `registry-after.log` matches; before counts 3/0).

Row conformance against PROTOCOL.md §Gate standard (S449, re-opened — see §3): the two new
rows (`receipt_probe` criterion R; `gate_probe` criterion G) each carry the full field set —
name; kind `gate` with the explicit can-fail statement (red exit 1 / green exit 0); entry
command with cwd; verdict map (0 green, 1 red, undeclared nonzero → could-not-evaluate);
self-test field; pinned-value path (S445/S444 + payload paths, with probe-bytes sha256 pins);
write scope; owner. The self-test disposition is honest in both rows: "none exposed — routed
debt of this registration, recorded honestly … NOT satisfied and is not claimed", with the
two-evidences clause carried by the committed r76/r77 red/green log pairs and the
producer-coupling note recorded. The registry note routes the criterion-instrument class
question (P/F/counters) as unsettled — no exemption claimed. No criterion score moved
(C 5.0, N/R/G 10.0 held) — the disclosed boundary matches the SCORECARD row. The claimed
0→2 / 3→5 deltas and the honest no-selftest disclosure both verify.

### b7fee90f — disclosed post-freeze correction — ordering verified

- Freeze `f042b295` (08:23Z) committed `p3_negctl.sh` at sha256 `68b78ea1cc4075f6…2fd9d17` — exactly the superseded pin the report names — together with the red-before `p3-before.log` (blob present at the freeze commit). **Correction after the red ✓.**
- `b7fee90f` (08:32Z, parent 7f303c3d) changes exactly 2 files: `p3_negctl.sh` (+8/−3) and `corpus/lessons/round-78.md` (+3/−1) = +11/−4, matching the report; the diff is precisely the LEG4 fix `bash "$P3"` → `bash "$P3" "$L"` plus its disclosure comment. **Disclosed ✓.**
- Predicate bytes unaffected: P3 blob `5770a8f446693f1f…` identical freeze↔tip; `PROVINCE.md` blob `bd7cd320…` identical across the correction; the red-before logs untouched. **Freeze instrument unchanged ✓.**
- This judge's run D above executed the corrected instrument from `git archive` tip bytes — the extraction context in which the defect was visible — and LEG4 passes against the target tree.

## 3. Discernment spot-check (non-author)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S449 (fleet `PROTOCOL.md` §Gate standard, checkout `57fa881f`) | ADMIT, tier A | `git -C <fleet root> show 57fa881f:PROTOCOL.md` — `## Gate standard` at :375; delivery paragraph :418-421 | **agree** | the pinned checkout exists; the located quote "closure grades no gate conformant until its registry row exists at the lane's registry home" is present verbatim (wrapped across :420-421), 16 words ≤25; the row genuinely grounds C2's registration duty |
| S450 (r77 routed items, committed) | ADMIT, tier A | `<lane>/corpus/lessons/round-77.md` :130-135 + `round-77-verifier-spotcheck.md` :156-166 at tip bytes | **agree** | the quote "The P2 province probe's surface list predates the browser record" is verbatim at round-77.md :132 (10 words ≤25); the spotcheck anchor resolves to the registration routing; the row genuinely grounds C1 |
| F android ruled out (hard gate on caller-supplied `REA_JADX_MCP_JAR`) | REJECT (candidate claim ruled out) | live re-probe: `echo ${REA_JADX_MCP_JAR:-UNSET}` → UNSET; `command -v jadx` → not on PATH; `ls ~/tools/jadx*` → none; S448 receipt row present at tip | **agree** | a do-nothing control reaches the identical state — the route is genuinely blocked, the reject is honest and correctly sized |

Census re-run by this judge:

- Literal contract form `bash <fleet-root>/scripts/sources-census.sh validate --root <fleet-root> revenger` → **exit 2**, `revenger missing …/shokunin-clone/shokunin/revenger-shokunin/corpus/SOURCES.md` — exactly the disclosed old-host layout defect (r74–r78 operator-side lineage; status-neutral, stays routed).
- Sanctioned explicit-lane-dir form (documented at SKILL.md :617-623) → **exit 0**, final line `ok …/fleet/shokunin-binary-forensics/corpus/SOURCES.md`, exactly **31 W** warnings (21× W01 tierC-mined, 10× W04 duplicate-url) — matches the disclosed "31 W, disclosed W01/W04 classes".
- Row counts: `git show 9676f52f:corpus/SOURCES.md | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` → 448; same at tip → 450 (+S449, S450) ✓. Both new rows are grammar-conformant (13 columns, pipe-free cells, enum-legal kind `docs`/`own-work`, status `mined`, resolvable used-by paths).

## 4. No-axis-harmed check

- `git diff-tree -r --numstat 9676f52f 1b3664c8` → 20 files, **+892/−0** (matches the report's range total); through the correction `9676f52f..b7fee90f` → 8 files, **+551/−0** (matches; the −4/−2 per-commit negatives are same-round edits of round-authored files only).
- Protected paths (corpus/knowledge, corpus/README.md, SHONEN.md, PROVINCE.md, P2/f_probe/receipt_probe/gate_probe) — my own `git diff-tree --name-only 9676f52f b7fee90f -- <paths>` is **empty**; frozen instrument blobs identical at tip (`8760ae57`, `ea42e6c2`, `7b51a021`, `58816812` — match `noharm-diff.txt`).
- SCORECARD diff is a pure 51-line append (round-78 section); holds receipts (`holds.log`: F 7/8 exit 0, FRESH_ROWS 18/18; `tip-verification.log`: same at the tip receipt commit) — evidence-verified, K 8/15 untouched.
- Separability receipts re-read (`c1-only.log`: negctl green with registry still 3/0; `c2-only.log`: registry 5/2 with P2 still 11/11) — consistent with the claim structure; C1 was additionally re-measured end-to-end by this judge.

## 5. Per-axis verdicts (closure grades; agree with the report and SCORECARD)

| axis | verdict | evidence |
|---|---|---|
| coverage | **improved** | C1 re-measured: the criterion P instrument went from blind (`P2_NEGCTL_STALE_BROWSER_FLAGGED=0/1`, reproduced from base bytes) to attributed kill (`P3_NEGCTL_STALE_BROWSER_FLAGGED=1/1`) on the exact r77-routed defect class, red-before committed at freeze; score honestly held 10.0→10.0 at 11→12 surfaces (moved quantity is the caught class, not the score); K/F unchanged (blocked/gated routes not attempted) |
| calibration | **improved** | C2 re-measured: registered instruments 3→5, probe-path rows 0→2; both rows carry the full §Gate-standard field set with the honest no-selftest routed debt; no score smoothing (C 5.0, N/R/G 10.0 held, disclosed) |
| depth | unchanged | no claim; no engine readiness claimed (Q05 discipline held) |
| operability | unchanged | frozen instruments byte-identical; the round's own instruments re-ran green from bare archive bytes (this judge reproduced) |
| freshness | unchanged | FRESH_ROWS 18/18 hold receipt; no knowledge bytes changed |
| adjacency | unchanged | PROVINCE.md blob identical base↔tip; no cross-domain absorption |

## 6. Trend verdicts (closure grades; agree with the report)

- **expansion — unchanged.** Zero `corpus/knowledge/` bytes changed in the range (my protected-path diff-tree); K stays 8/15 (blocked route honestly not attempted); no capability row (P3/negctl are instrument revisions of an existing criterion — correctly not claimed as new capabilities).
- **quality — improved.** The coverage criterion's instrument demonstrably catches a defect class it was blind to (re-measured red→green with an attributed kill line), and the two criterion gates now carry registered verdict maps, pinned values, write scopes and owners per the §Gate standard — with their actual gaps (no self-test mode) recorded rather than smoothed; no admitted entry failed any re-check (F 7/8, FRESH 18/18, P2's clean-lane hold re-shown).
- **discernment — improved.** Four real defects mined in one round (`corpus/lessons/round-78.md` `## Mistakes`), three self-caught before the freeze and one by the mandated committed-bytes receipt; the post-freeze instrument change is a disclosed correction commit with predicate bytes proven unaffected (verified in §2); boundaries disclosed as boundaries (`not-claimable` leg, held scores, routed self-test debt); the spot-check sample above agrees on both admits and the reject.

## 7. Routed defects / notes (all status-neutral; none bars admission)

1. **Census literal form exits 2 on this host** (old-host `<root>/<id>-shokunin/` layout). Re-produced by this judge; r74–r78 lineage; operator-side `scripts/` routing continues; the sanctioned explicit-lane-dir form (SKILL.md :617-623) is the working form and exits 0.
2. **Neither registered gate exposes a self-test mode** — honestly recorded as routed debt in both new registry rows (not claimed satisfied). Adding one means a superseding instrument revision, not an edit of the pinned bytes (the rows say this).
3. **Criterion-instrument registration class question (P/F/counters)** — routed, not settled (SKILL.md registry note); next registering round should settle it.
4. **Criterion C repair** (two failing replay verifiers, `r47: artifact` / `r55 artifact`) — routed since r75, re-confirmed failing this round by the lane; stays routed.
5. **SHONEN boxes** remain `[~]` author-assertion with the r69 non-author-confirmation need standing; all four boxes are checkable by a non-author review of current bytes — operator may schedule that review; this judge wrote no `[x]` (per the promotion gate, and per the r77 spotcheck note that keeps all four boxes open).
6. Cosmetic: S449's anchor `:375-420` spans the §Gate-standard section; the quoted sentence itself wraps across :420-421 at the pinned checkout — immaterial, both endpoints resolve.

Closure entry: `admitted=true`, verdict `admitted`, lanes `{"revenger": "ok"}` — every claim verified (C1 and C2 re-measured by this judge from committed bytes; holds evidence-verified) and no axis harmed.
