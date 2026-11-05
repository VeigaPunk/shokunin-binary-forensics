# Round 93 — verifier spot-check (non-author closure)

author: hyaku closure (non-author integrator, @m_zfl)
date: 2026-11-05
lane: revenger, round 93 (hyaku run 15, attempt 1)
report: `.ufo/reports/round-93/revenger.md`; lane base `281a5bad66e844190a570cb35d257c6974749993`;
freeze `02050cb2a6758e3bd9cec696ff0e42df6f23511a`; landing `0723ebd0687291685fa231b9808bbb20b5e49c13`;
adjudication/lane tip `28b5f99b90c1da91ac85d2e6d6aa6ec49efa42e6`.

Dispatch/complete digest (copied from `.ufo/watchdog.log`, mutable):

```
2026-11-05T11:05:13-03:00 launch revenger round=93 pgid=323901 driver=hyaku-inline attempt=1
2026-11-05T12:29:49-03:00 complete revenger round=93; hyaku-inline attempt=1
```

## 1. Conformance

- Report committed on the fleet repo by the lane identity: `git log --format='%an %ae %H' -- .ufo/reports/round-93/revenger.md` → `revenger-shokunin revenger@shokunin.local ae6e910d62188dc1f619282a5a35bd7b74175880`.
- `grep -c '^## SHONEN'` = 1; four `[~]` lines matching the four `SHONEN.md` boxes; no `[x]` anywhere; each `[~]` carries a resolvable pointer.
- Every cited lane commit exists (`git cat-file -t`) and is an ancestor of the branch ref: `git merge-base --is-ancestor <hash> main` holds for `02050cb`, `0723ebd`, `28b5f99` (jj-colocated repo; ancestry tested against `main`, not `@{u}`).
- Pushed and clean: `scripts/hyaku/jj-lane.sh state` → `local=28b5f99b… remote=28b5f99b… ahead=0 behind=0`; `git status --porcelain` empty; `git ls-remote origin refs/heads/main` → `28b5f99b…`.
- All three round commits authored by `revenger-shokunin <revenger@shokunin.local>`; LOG.md carries the "Round 93" entry.
- Prompt fidelity: `.ufo/prompts/revenger-round-93.md` embeds the canonical `templates/round-prompt.md` verbatim after placeholder rendering (115/116 non-empty lines exact; the single difference is the `<{{LANE}}-repo>` placeholder rendered as the literal repo path) plus the hyaku addendum §6 — all five child-lane items and the round-level contract present.
- Wave: one v1 wave, 13 seats (band 8–16), attack share 5/13 = 38.5 %, 1 connector, no residual call; `w1-results.json` shows 13 results, each with nonempty output — no dead seat. Freeze commit `02050cb` (11:03:38 -03) precedes the wave marker `w1.ready.dispatched` (11:48:22 -03): claims frozen before any seat scored.
- Marker rule: the report names real committed work with evidence pointers and checkable hashes — a real report, not a marker.

Conformance defects: none.

## 2. Claims — re-check

### C1 — coverage, knowledge-map ground K (re-measured, not evidence-only)

Plain measurement re-implemented over committed bytes (the counter's rule: coverage rows `^\| C[0-9]+ ` with 5 cells; held-backed = status `held` and every `knowledge/<file>.md` named in the knowledge cell exists):

```
python3 (git show <rev>:corpus/README.md; git ls-tree -r --name-only <rev> corpus/)
281a5bad: rows=15 K_HELD_BACKED=9/15 C08_status=uncovered
0723ebd0: rows=15 K_HELD_BACKED=10/15 C08_status=held
28b5f99b: rows=15 K_HELD_BACKED=10/15 C08_status=held
```

Matches the reported 9/15 (6.0) → 10/15 (6.7); arithmetic checks (9/15 = 0.60, 10/15 = 0.667). Do-nothing control: `controls/c1v2-do-nothing.log` at `0723ebd` shows `C1_C08_HELD=fail`, `C1_VERDICT=fail` — a no-work tree does not pass. Full leg list in `reports/round-93/c1-after.log` at `28b5f99b`: all 17 legs pass, verdict pass.

Vote binding re-derived independently: the counter's normalized digest is `sha256` of the entry with `admission-status: <state>` rewritten to `candidate`. Recomputed over the landed entry bytes at `28b5f99b` → `1304008c5a0aff9dbb9af09967e12caeef028b1ca52e14dac7b8fe0247e43647`, equal to the `candidate_sha256` in all three vote files (`ReviewerGate`, `ReviewerBlind`, `CriticR93`; each all-PASS/n-a). The votes bind the final committed bytes, not an earlier draft.

**C1 verdict: met — re-measured.**

### C2 — calibration, reach of the counting instruments (evidence-verified)

Lane-owned frozen instruments (`forge_battery.py`, both v2 counters at freeze `02050cb`): per the protocol's gate standard, the committed evidence is verified; the sibling's gate was not executed. Committed evidence, all confirmed at the named revisions:

- Red-before: `controls/battery-v1-only.log` → `V1_REACH_C2=5/5`, `BATTERY_VERDICT=pass` (v1 counter reachable by the five C2-side classes).
- Freeze-time full battery: `controls/battery-full.log` → `V2_KILLS=9/9`, `POS_C1V2=pass`, `POS_C2V2=pass`, `DO_NOTHING_C2=fail`, `R92_RECEIPTS=4/4`, `BATTERY_VERDICT=pass`.
- Post-landing re-run: `reports/round-93/battery-after-full.log` at `28b5f99b` → identical values, `BATTERY_VERDICT=pass`.
- Self-test tally: `controls/selftest-c1v2.log` → `SELFTEST_C1V2=pass kills=registry,artifact-sha,all-na,na-reason`; `controls/selftest-c2v2.log` → `SELFTEST_C2V2=pass kills=record-sha,trailing-cell`.
- Do-nothing: `controls/c2v2-do-nothing.log` → `C2_VERDICT=fail`.
- Frozen predicate identity: `claims.md` lines 57 and 103 state `C1_VERDICT=pass` / `BATTERY_VERDICT=pass` — the same sentence as the counter code and the receipts; no post-scoring rule change (mutation battery separately recorded: 20 killed, 1 equivalent, 0 survived).

**C2 verdict: met on the frozen predicate — evidence-verified.** Contested-but-scoped, honestly reported by the lane: CriticR93's 12 findings show the counters remain reachable by forgeries outside the nine frozen classes; the landed entry is not among the reachable forgeries; the limitation is mined as M3 and routed to r94 (C1 v3 with the critic's closes as frozen predicates). The claim as frozen ("nine routed classes killed") is exactly what the committed battery evidence shows.

### No axis harmed

- `git diff 281a5bad 28b5f99b -- SCORECARD.md` → 43 insertions, 0 deletions (append-only round-93 section; no prior row edited).
- `git diff 281a5bad 28b5f99b -- PROVINCE.md corpus/QUALITY.md` → empty.
- `git diff 02050cb 28b5f99b -- corpus/live corpus/fixtures` → empty (the new entry's `verified-at` byte-identity clause re-verified).
- Other coverage criteria: base-only holds (`K 9/15, F4 11/11, M 3/3, A1v2 5/5`), not re-run at landing, no claim — unchanged, no harm observed.

## 3. Discernment spot-check (LEARNING.md, non-author)

| item | decision | re-opened source / check | agree/disagree | reason |
|---|---|---|---|---|
| S495 admit (own-work, tier A) | admit | re-ran `python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json` → `ORACLE OK (17/17 checks)`, exit 0; `sha256sum` record = `b045a4eecf2d77…` (matches the receipt pin) | agree | the record's identity facts re-derive today from committed bytes; scope correctly limited to the authored fixture + one saved record |
| S496 admit (CDP docs, tier A) | admit | fetched https://chromedevtools.github.io/devtools-protocol/ → HTTP 200, 35462 B, sha256 `ba8018bb02f3…` = receipt; quote "It allows tools to instrument, inspect, debug, and profile Chromium, Chrome, and other Blink-based browsers." (16 words) present in the landing-hero intro, 2nd sentence | agree | quote located, ≤25 words, digest matches; scoped to the protocol's self-description only |
| S497 admit (ECMA-335 addendum, tier A) | admit | fetched the pinned `dotnet/runtime@b22bfee2` raw URL → HTTP 200, 69577 B, sha256 `1e6e225aa41c…` = receipt; line 3 = "This is a list of additions and edits to be made in ECMA-335 specifications."; `teaches` opens `supersedes S136 —`; S136 row byte-identical base..tip | agree | rule-2 supersession done by new row, not by editing the frozen S136 scope cell |
| Draft rejection Q11 (underived count) | reject → fixed | final entry carries `## 5. Provenance` mapping every count/identifier/digest to a named stdout line with its expectation side; no uncounted numeric prose remains | agree | the reject was warranted and the fix landed before admission |
| Draft rejection Q15 (unscoped byte-identity clause) | reject → fixed | final `verified-at:` scopes the byte-identity clause to `corpus/live corpus/fixtures` and acknowledges the registry changed at landing; clause re-verified (`git diff --quiet 02050cb… -- corpus/live corpus/fixtures` silent) | agree | scoping is exactly right; the registry did change at landing |
| considerthese proposal 2 not adopted | reject (defer) | `considerthese/2026-11-05.md` proposal 2 mined as an r89–r92 measurement (8/8 contested/not verified), no QUALITY criterion added | agree | adopting a criterion without its own frozen predicate would violate the lane's own bar; deferred to r94 with a measurement baseline |

Sample: 3 admits re-opened (≥1 required), 3 rejects sampled (≥1 required) — 6/6 agree. Census at closure: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger` → exit 0, 0 E, 21 W01 + 13 W04 (matches the round-end census receipt).

## 4. Per-axis verdicts and trends

| axis | verdict | evidence |
|---|---|---|
| coverage (K) | improved | 9/15 → 10/15 re-measured over committed bytes; C08 `uncovered` → `held`; do-nothing control fails |
| calibration | improved | frozen nine-class battery: v1 reach 5/5 → v2 kills 9/9, positives retained, do-nothing fails, selftests pass; evidence-verified; reach beyond the nine still open (M3, routed r94) |
| depth | unchanged | no claim; PROVINCE/QUALITY byte-unchanged; SKILL gained 3 gate-registry rows only |

Trends: **expansion improved** (one admitted entry on uncovered coverage-map ground, citing mined S495/S496); **quality improved** (r92 entry revision applied per the r92 spot-check defects — recheck pointer and beyond-quote labelling landed at `0723ebd`; the new entry's two gate-caught defects fixed before admission; no admitted entry fails its re-check — oracle re-run by this verifier, exit 0); **discernment improved** (this non-author spot-check agrees with the gate on all sampled admits and rejects — LEARNING.md's improved condition; the report's own `unchanged` was honest at write time because no outside check existed yet).

## 5. Routed items / notes

- Routed forward (already lane-recorded, carried): C1 v3 successor counters must freeze the critic's closes — exactly one `admission-status:` line; seat-name canonicalization; author/role checks; artifact distinctness; oracle sha pinning; non-vacuous fenced blocks (M3, findings 1–12).
- Clarification, not a defect: the report's before→after table says the battery was "run at 0723ebd0"; the run happened against the landing tree and its receipt logs are committed at `28b5f99b` (the report's Landed-changes table states this correctly).
- Open L0 `revenger | round-91` (assimilation id collisions 155/155) still unanswered; the lane routed around it (assimilation: none).
- SHONEN: all four boxes are checkable by a non-author on the current bytes; no `[x]` was written by this verifier (promotion review is operator-owned).
