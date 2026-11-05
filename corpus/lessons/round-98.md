# Round 98 — gate, mistakes, frontier (revenger, attempt 1)

Claims frozen at `9d49002a3804de48d365b7d32849ada06745d64f` (`reports/round-98/claims.md`), with
Amendments A (`cf8a9d4`), B (`0146c0a`) and C (`1b76b4d`) appended before the v7 freeze (`5d9b087`).
Base at round start `34c56f9f324723cafd56fd57d718065b2ad2da66`. Landing and measurement commits are
cited in the SCORECARD round-98 section and the report.

**Verdict of record: C1 NOT VERIFIED; C2 met on its frozen predicate (development set, contested
against a fresh holdout).** The C14 candidate entry is **not admitted**; the C14 row stays
`partial`; K stays 13/15. C2 is met on its frozen vector set.

## Gate

### C14 candidate — the vote-binding digest moved three times, and the last one still fails

Entry `corpus/knowledge/round-98-rea-host-readiness.md`. The vote-binding digest is
`6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f` (v6 `digest()` rule: sha256 of the
entry text with every admission-status line normalized to `admission-status: candidate`).

Recomputed from the committed bytes at `1b76b4d`:

```
python3 -c "import re,hashlib;t=open('corpus/knowledge/round-98-rea-host-readiness.md',encoding='utf-8').read();n=re.sub(r'(?im)^\s*admission-status\s*:.*$','admission-status: candidate',t);print(hashlib.sha256(n.encode()).hexdigest())"
→ 6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f
```

Digest history, each with its own superseded vote set kept as evidence:

| digest | set by | superseded votes |
|---|---|---|
| `1ea9260c…27b8` | claims freeze `9d49002` | `.ufo/waves/round-98/w1/superseded-votes-digest-1ea9260c/` |
| `73f1d7e0…80e7` | Amendment B `0146c0a` (entry gains `## §Q-map`) | `.ufo/waves/round-98/w1/superseded-votes-digest-73f1d7e0/` |
| `6d27c129…5330f` | Amendment C `1b76b4d` (critic Q11/Q16 fixes) | current; binds `reports/round-98/votes/{ReviewerGate,ReviewerBlind,CriticR98}.json` |

All three current vote files carry `candidate_sha256 = 6d27c129…5330f`
(`python3 -c "import json;print(json.load(open('reports/round-98/votes/<Seat>.json'))['candidate_sha256'])"`).
Decisions: ReviewerGate 10 PASS / 7 n/a, FAIL 0; ReviewerBlind 11 PASS / 6 n/a, FAIL 0;
**CriticR98 2 FAIL** (Q11, Q16), 9 PASS, 6 n/a.

The claims kill rule is explicit: *"A vote that records any FAIL decision fails `C1_VOTES`, and
therefore C1."* (`reports/round-98/claims.md:49-51`). CriticR98's two FAILs are therefore decisive
on their own, and the counter agrees on its own legs:

- **Q11 FAIL** — *"the registration counts (14; 4 aligned, 1 manual, 8 missing, 1 stale; 9 missing
  or stale) are now derived, but 'Doctor lists three such installation paths' is not: its rows print
  1 and 1, and `grep -c '^    paths\[3\]: '` does not yield 3"*
  (`reports/round-98/votes/CriticR98.json`, note Q11). The route-table cell still reads *"Doctor lists
  three such installation paths (`state: multiple`)"* (`corpus/knowledge/round-98-rea-host-readiness.md:59`),
  while the derivation row for `installation paths` records `1` and `1`
  (`:83`). The record shows one `paths[3]:` line holding **three** comma-separated paths
  (`corpus/live/runs/round-98/rea-doctor-r98.txt:316`), so the number three is real but the recorded
  deriving command counts *lines*, not paths.
- **Q16 FAIL** — *"the preamble says each version string comes from the probe transcript, but
  ghidra-version 12.1.4 is printed by the doctor record only (0 occurrences in
  host-probes-r98.txt), so the credit reaches past what the transcript prints"*. The derivation
  preamble states *"Version strings and exit codes are not derived here. Each comes from the probe
  transcript"* (`:67-69`), and the route table credits `ghidra-version 12.1.4`
  (`:54`). `grep -c "12\.1\.4" corpus/live/runs/round-98/host-probes-r98.txt` → **0**;
  `grep -c "12\.1\.4" corpus/live/runs/round-98/rea-doctor-r98.txt` → **17**.

### The v7 counter's own landing diagnostic fails two legs

`reports/round-98/controls/c1-v7/diag-landing.log` — v7 `--profile c14` on the landing-shaped tree
(C14 held, entry admitted, S505 queued/`—`):

```
C1_K_HELD_BACKED=14/15
C1_VOTES_WHY=vote CriticR98 decision Q11='FAIL' not PASS/n-a digest=6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f
C1_VOTE_NOTES_WHY=ReviewerBlind.json:Q17:PASS note is n/a-style; ReviewerGate.json:Q01:PASS note needs >=6 tokens; ReviewerGate.json:Q02:PASS note needs >=6 tokens; ReviewerGate.json:Q03:PASS note needs >=6 tokens; ReviewerGate.json:Q04:PASS note needs >=6 tokens; ReviewerGate.json:Q05:PASS note needs >=6 tokens; ReviewerGate.json:Q09:PASS note needs >=6 tokens; ReviewerGate.json:Q10:PASS note needs >=6 tokens
C1_USEDBY_GROUNDED=pass
C1_VERDICT=fail
# rc=1
```

The `C1_VOTE_NOTES` failure is a **second, independent** gate on the votes: ReviewerGate's PASS
notes for Q01–Q05, Q09 and Q10 are empty strings (0 tokens; `python3 -c "import json;d=json.load(open('reports/round-98/votes/ReviewerGate.json'));print({k:len(str(v).split()) for k,v in d['notes'].items()})"`), and ReviewerBlind's Q17 PASS note is n/a-style. Both are counted by the same leg, so fixing the critic's two FAILs alone would not turn `C1_VERDICT` to pass.

Control legs, same directory, same counter:

| tree | `C1_K_HELD_BACKED` | `C1_ONLY_TARGET` | `C1_USEDBY_GROUNDED` | `C1_VERDICT` | rc |
|---|---|---|---|---|---|
| do-nothing (claims-freeze tree) | 13/15 | fail | fail | fail | 1 |
| junk-row (only C14 `partial`→`held`) | 14/15 | pass | fail | fail | 1 |
| diag-landing (C14 held + entry admitted + S505 queued/`—`) | 14/15 | pass | pass | fail | 1 |

Both controls fail, as the claims require (`reports/round-98/claims.md:44-47`): the do-nothing tree
fails because C14 is still `partial` and S505's used-by is still ungrounded; the junk-row tree
still fails `C1_USEDBY_GROUNDED` on S505. So the controls do discriminate, but the landing tree
itself does not pass — the entry's admission is blocked by the votes, not by the counter's row or
grounding legs.

### C2 — met on its frozen predicate (development set)

`reports/round-98/controls/c2-v7-frozen.log`, one recorded run of
`PYTHONUTF8=1 python3 -B reports/round-98/forge_reach7.py --counter reports/round-98/c1_k_admit_counter7.py --profile c02 --work <scratch>`:

```
C2_ACCEPTED=0/5
C2_POSITIVE=pass
C2_POSITIVE2=pass
C2_STUB_SELFTEST=ok
C2_ROWSET_FR06=C1_ADMITTED_UNION,C1_ROWSET,C1_VERDICT
C2_ROWSET_FR07=C1_ADMITTED_UNION,C1_ROWSET,C1_VERDICT
C2_VERDICT=met
# rc=0
```

All five routed holdout vectors are refused, each by a named new leg: FR02 by `C1_ENTRY_BYTES`,
FR08 by `C1_HEADER_POSITION`, FR09 by `C1_VERIFIED_AT`, FR10 by `C1_VOTE_NOTES`, FR12 by
`C1_OWNWORK_PATHS`. FR06 and FR07 are refused by `C1_ROWSET`, which the claims require by name
(`C2_ROWSET_FR06`/`C2_ROWSET_FR07` both contain `C1_ROWSET`). `C2_POSITIVE2` is Amendment A4's
second positive (`FR00b-benign-extra-file`).

Before: the frozen v6 accepts 5/5 of the same vectors —
`reports/round-98/controls/c2-do-nothing-v6-holdout.log` ends `BUILD_OK=True vectors=15 accepted=5`,
and the five `ACCEPTED-by-v5` lines are FR02, FR08, FR09, FR10, FR12
(`grep -c "ACCEPTED-by-v5"` → 5).

### The fresh round-98 holdout (discernment evidence, reported separately)

`.ufo/waves/round-98/w1/L1-holdout-v7/`, built by the critic seat's
`.ufo/waves/round-98/w1/CriticR98/fresh/build_fresh98.py`:

| run | accepted | control |
|---|---|---|
| `holdout98-v6-c02-parity.log` (v6, parity patch) | **5/6** | control-ok |
| `holdout98-v7-c02-parity.log` (v7, parity patch) | **5/6** | control-ok |
| `holdout98-v7-c14.log` (v7, c14) | **4/6** | control-ok |
| `holdout98-v7-c02.log` (v7, c02, unpatched) | 0/6 | **control-BROKEN** (`C1_OWNWORK_PATHS`) |

So v7's reach over this holdout is **no better than v6's** on the c02 profile (5/6 both), and the
unpatched c02 run refuses everything only because its own honest control is broken (a missing
round-96 record, not a discrimination). The c14 profile accepts 4 of 6: `C14-R01-suffix-row-outside-count`,
`C14-V02-fail-under-extra-key`, `C14-O01-ownwork-pointer-foreign-round` and
`C14-L01-fetchlog-date-vs-receipt` are all accepted (`ACCEPTED`); only `C14-V01-placeholder-pass-note`
and `C14-Q01-receipt-span-shift` are refused. The claims disclose this as a development-set result
and forbid any counter change in response to it (`reports/round-98/claims.md:82-85`); nothing changed.

### Sourced-claim duty (§2b.4): sources re-opened this round

- **S506** — REA `references/connection-and-recovery.md` at the pinned revision
  `12f6e0974cc0db0b3a9b86246accc76556837222`. Body committed at
  `reports/round-98/quote-receipts/raw/S506.body` (16650 bytes, sha256
  `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50`; receipt
  `reports/round-98/quote-receipts/S506.receipt.json` records HTTP 200, `fetched_at` 2026-11-05, the
  same length and the same sha256). Fetch log: `reports/round-98/quote-receipts/fetch-log.md`.
  Located quote, verbatim: *"Static JavaScript and ordinary ZIP inventory need neither Hopper nor
  Ghidra."* — 11 words, body bytes 7126–7202 (`head -c 7202 reports/round-98/quote-receipts/raw/S506.body | tail -c +7127`
  prints the sentence; `grep -c -F` on the body → 1 occurrence).
- **S507** — own-work record, `corpus/live/runs/round-98/` (three files, sha256 `94eaa6ff…`,
  `fb9a4824…`, `c373f656…`; `sha256sum corpus/live/runs/round-98/*`). Located quote, verbatim:
  *"healthy: false" / "environment_healthy: false"* — the first two lines of
  `corpus/live/runs/round-98/rea-doctor-r98.txt`, bytes 1–41
  (`head -c 41 corpus/live/runs/round-98/rea-doctor-r98.txt` → 41 bytes, both lines).

Both rows are tier A, `status=mined`, `opened` 2026-11-05, `recheck` `on-release`,
`used-by` `corpus/knowledge/round-98-rea-host-readiness.md` (`corpus/SOURCES.md:523-524`). The
registry holds 507 rows (`grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` → 507).

### S505 correction, logged old → new (this round's mined mistake)

The r97 non-author spot-check §6.1 routed it: *"**S505 `used-by` is ungrounded.** It names
`corpus/knowledge/round-96-native-analysis-sessions.md`, but that entry never cites S505"*
(`corpus/lessons/round-97-verifier-spotcheck.md:151-153`; `grep -c S505
corpus/knowledge/round-96-native-analysis-sessions.md` → 0, while the same file cites S504 three
times).

**Status: NOT applied this round (L1 decision).** The correction that Amendment A2 specifies is
below, but it is not landed. ScribeLesson measured a side effect on scratch copies of the
claims-freeze tree: with S505 at `queued`, the supersedes chain S504 → S505 fails `C1_SOURCES` with
`S504:terminal-mined-expected:S505:queued` (v6 rc 1, and v7 `--profile c02` rc 1). Landing the
correction would therefore harm C02 on the real tree, and no axis may be harmed. C1 did not verify
either, so nothing in the c14 profile needs the correction. The routed fix for round 99 grounds S505
by citing it: a superseding revision of the C02 entry cites S505 in place of S504, so the row stays
`mined` and the chain stays terminal-mined. It is not done by unmarking the row. The planned
correction would have been:

| cell | old | new |
|---|---|---|
| `status` | `mined` | `queued` |
| `used-by` | `corpus/knowledge/round-96-native-analysis-sessions.md` | `—` |

Reason: the entry never cites S505 (r97 spot-check §6.1). The v7 leg that catches this class is
`C1_USEDBY_GROUNDED`, scoped by Amendment A2 to the profile's row set (c14: S505, S506, S507).
Receipts: `reports/round-98/controls/s505-usedby-fix.diff` (the exact one-line diff),
`reports/round-98/controls/s505-ungrounded-count.txt` (471 mined-with-used-by rows, 470 grounded,
**1 ungrounded — S505**), `reports/round-98/controls/s505-census.log` (census exit 0, warnings only),
`reports/round-98/controls/v7-dev/usedby-base34.log` and `usedby-freeze.log` (leg `fail` before the
correction with why `S505 -> corpus/knowledge/round-96-native-analysis-sessions.md:entry does not
cite row id`, `pass` after).

### Candidates considered

- **C14 host-readiness entry — NOT ADMITTED this round.** The entry's own construction is sound on
  the axes it claims: the ZIP-inventory row is the only `capability` row, every other route row is
  labelled `configuration` or `absent` (`:53-60`), the digests bind exact bytes only, and the
  observation/inference/unknown split is explicit (`:93-97`). It is blocked by two derivation-hygiene
  defects (critic Q11, Q16) and by the vote-note rule, not by any scope overreach. Flip: a corrected
  entry (the "three installation paths" count derived by counting paths rather than lines; the
  version strings re-attributed to the doctor record that prints them) plus non-empty PASS notes from
  ReviewerGate, re-voted on a fresh digest. Non-author closure remains required (LEARNING.md); the
  lane-internal votes are not the admission.
- **C02 native analysis sessions — unchanged.** The row stays `held` on the r97 landing
  (`47e4f6c`); this round does not touch it.
- **Assimilation** — none. The r97 collision (155/155 staged ids) stays open on L0.

### Rejected or reworked

- **The entry's derivation-hygiene misses** — reworked twice by amendment rather than rejected:
  Amendment B added the missing `## §Q-map`; Amendment C added the three missing count rows and the
  Q06 correction. Both amendments produced a new vote-binding digest and superseded the previous
  vote set. What remains unfixed are the two clauses the critic named (see M15).

## Mistakes

| # | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M11 | **registry/used-by drift:** S505's `used-by` cell named a document whose bytes never cite the row id back — a pointer that passes the census (path existence) and the v6 `used-by` exclusivity check (which only inspects `NEW_ROW_IDS` S502–S504) but is not a citation site. | r97 spot-check §6.1 (`corpus/lessons/round-97-verifier-spotcheck.md:151-153`); `grep -c S505 corpus/knowledge/round-96-native-analysis-sessions.md` → 0 (the file cites S504 three times); `reports/round-98/controls/s505-ungrounded-count.txt` → "mined-with-usedby rows: 471 (grounded 470, ungrounded 1) / S505" | **none** in v6: the v6 counter's used-by exclusivity check runs over `NEW_ROW_IDS = ("S502","S503","S504")` only (`reports/round-97/c1_k_admit_counter6.py:54`, the loop at `:405-428`), and `grep -c S505 reports/round-97/c1_k_admit_counter6.py` → 0 | **v7 leg `C1_USEDBY_GROUNDED`**, scoped to the profile's row set (c14: S505, S506, S507; Amendment A2), shown able to fail on the base registry: `reports/round-98/controls/v7-dev/usedby-base34.log` prints `C1_USEDBY_GROUNDED=fail` / why `S505 -> corpus/knowledge/round-96-native-analysis-sessions.md:entry does not cite row id`, exit 1, before the correction and `pass` after it. The data correction is **withheld** this round because it would break C02's supersedes chain (`## Gate`, S505). It is routed to round 99 as a citation fix, so M11's data defect stays open while its capture (the leg) is landed. |
| M12 | **admission before closure:** the r97 landing wrote `admission-status: admitted` before the non-author closure existed — the entry claimed admission the lane's own process had not yet granted. | r97 spot-check §6.5 (`corpus/lessons/round-97-verifier-spotcheck.md:162-164`); the flip is in `47e4f6c` (2026-11-05T17:34:18-03:00) and the non-author closure is `34c56f9` (17:42:18-03:00) — `git log --format='%H %cI' -1 47e4f6c` and `-1 34c56f9` | **none** — no counter leg checks a closure receipt; v6 has no closure concept (`grep -c -i closure reports/round-97/c1_k_admit_counter6.py` → 1, a docstring) and v7 has none either (`grep -c -i closure reports/round-98/c1_k_admit_counter7.py` → 0) | **this round records the flip as pending closure**: the candidate stays `admission-status: candidate` through the freeze, the vote-binding digest is computed over a normalized `candidate` line, and the entry carries no closure claim. The digest rule makes the pending note digest-neutral **only if it rides on the admission-status line itself**: measured on the committed bytes, `admission-status: admitted (pending non-author closure)` on the same line leaves the digest unchanged (`6d27c129…5330f`), while the same sentence on a separate line changes it (`740d43e1…d7894`). The L1 must keep the note on that line. Round 98 did not flip, because C1 did not verify, so the note is unused this round. |
| M13 | **the r97 holdout forgeries the frozen counter accepted:** v6 accepts 5 of 12 named-class round-97 holdout forgeries (FR02 entry leading BOM, FR08 headers in a fence, FR09 stale verified-at, FR10 n/a boilerplate on a PASS note, FR12 dangling own-work pointer) — five skip-work routes the frozen predicate could not reach. | `reports/round-98/controls/c2-do-nothing-v6-holdout.log` (the accepted-5 receipt, byte-identical to `.ufo/waves/round-97/w1/CriticR97/holdout-v6.log`, `cmp` exit 0); `grep -c "ACCEPTED-by-v5"` → 5, and the five lines are FR02, FR08, FR09, FR10, FR12 | **the A4 holdout** (r97 `claims.md` Amendment A4: the CriticR97 fresh vectors were run once against the committed v6 and reported separately) | **v7 legs**, one per named class, all refusing in the frozen run: FR02 by `C1_ENTRY_BYTES`, FR08 by `C1_HEADER_POSITION`, FR09 by `C1_VERIFIED_AT`, FR10 by `C1_VOTE_NOTES`, FR12 by `C1_OWNWORK_PATHS` (`reports/round-98/controls/c2-v7-frozen.log`, `C2_ACCEPTED=0/5`). FR06/FR07 (row-set forgeries) are now refused by the named leg `C1_ROWSET` rather than incidentally by `C1_ADMITTED_UNION` (the same log prints `C2_ROWSET_FR06=C1_ADMITTED_UNION,C1_ROWSET,C1_VERDICT`). The r97 lesson's M10 asked for exactly these two fixes. |
| M14 | **authoring defect caught by the lane's own lint, after the freeze:** the candidate entry had no `## §Q-map` section, and the L1 did not run `corpus/lint_entry.py` before the claims freeze — the lane's own pre-flight instrument (`C1_LINT`) would have refused the entry at freeze time. | `reports/round-98/controls/v7-dev/self-test-first-run.log` → `SELFTEST_C1V7=FAIL legs=50` with `SELFTEST FAIL: c14:honest: expected pass; failing=C1_LINT`, exit 1; the lint's own report `LINT_QMAP=17` naming all seventeen Q ids. Reproduced independently: `git show 9d49002:corpus/knowledge/round-98-rea-host-readiness.md > <scratch>/entry-preB.md` then `python3 -B corpus/lint_entry.py --entry <scratch>/entry-preB.md --lane .` → `LINT_QMAP=17 ['Q01', …, 'Q17']`, rc 0 — the claims-freeze entry would have been refused by the lane's own pre-flight at freeze time | **the lint** (`C1_LINT`), found before any landing-tree scoring | **Amendment B** (`0146c0a`): a `## §Q-map` with 17 rows was appended, and `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-98-rea-host-readiness.md --lane .` → `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, rc 0. The fix is procedural: run the lane's own lint on the candidate **before** the claims freeze, not after the counter names the failure. |
| M15 | **derivation-hygiene misses that took two amendment rounds:** the entry stated counts and attributions that its own derivation table did not derive — "three such installation paths" where the recorded command prints `1` and `1`, and version strings credited to the probe transcript that prints none of them. Each amendment round re-digested the entry and invalidated the previous votes, so the defect class cost two digest changes and two re-votes. | critic Q11 and Q16 FAIL on digest `6d27c129…5330f` (`reports/round-98/votes/CriticR98.json`); the clauses are `corpus/knowledge/round-98-rea-host-readiness.md:59` (three paths) against `:83` (`1` and `1`), and `:54` (`ghidra-version 12.1.4`) against `:67-69` (versions come from the transcript) — `grep -c "12\.1\.4" corpus/live/runs/round-98/host-probes-r98.txt` → 0, `grep -c "12\.1\.4" corpus/live/runs/round-98/rea-doctor-r98.txt` → 17 | **the critic vote** (CriticR98's Q11/Q16 FAIL), and the counter's `C1_VOTES` leg, which fails the same tree on the same fact (`reports/round-98/controls/c1-v7/diag-landing.log`: `C1_VOTES_WHY=vote CriticR98 decision Q11='FAIL' not PASS/n-a`) | **not fixed this round** — the two clauses are still in the committed entry at `1b76b4d`, which is why C1 is NOT VERIFIED. Fix for a successor round: derive the path count by counting *paths* (the record prints three comma-separated paths on one `paths[3]:` line at `corpus/live/runs/round-98/rea-doctor-r98.txt:316`), and attribute every version string to the record that prints it (the doctor record prints `12.1.4` seventeen times; the transcript prints none). Both amendments B and C are logged in `## Gate` above with their superseded vote sets. |

Shown able to fail: M11 (`reports/round-98/controls/v7-dev/usedby-base34.log`, exit 1 before the
correction); M12 (`git log --format='%H %cI'` shows the r97 flip eight minutes before the closure);
M13 (`reports/round-98/controls/c2-do-nothing-v6-holdout.log`, `accepted=5`); M14
(`reports/round-98/controls/v7-dev/self-test-first-run.log`, exit 1, `failing=C1_LINT`); M15
(`reports/round-98/controls/c1-v7/diag-landing.log`, `C1_VOTES=fail`, rc 1).

## Frontier

- **Census before** — `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`
  at base `34c56f9` → exit 0, 21 × W01, 13 × W04, 0 E-codes
  (`reports/round-98/controls/census-round-start.log`). A second census after the S506/S507 append also
  exits 0 with the same counts (`reports/round-98/controls/census-after-append.log`). A census at round
  end is required; it is the L1's to run and record.
- **Rows added (by tier):** S506 (docs, tier A, `mined`, opened 2026-11-05, `recheck` `on-release`,
  `used-by` the candidate entry) and S507 (own-work, tier A, `mined`, opened 2026-11-05, `recheck`
  `on-release`, `used-by` the candidate entry). Registry 505 → 507 rows.
- **Rows touched old → new:** none. The planned S505 correction (`mined` → `queued`, used-by →
  `—`) was withheld because it breaks C02's `C1_SOURCES` supersedes chain (see Gate, S505). It is
  routed to round 99 as a citation fix.
- **Frontier rows advanced:** none. C14 stays `partial` and K stays 13/15 — the candidate is not
  admitted, and the C14 coverage-map cell still names the pre-contract
  `knowledge/2026-10-12-rea-readiness-checklist.md` (`corpus/README.md:61`, byte-unchanged since the
  claims freeze).
- **Next frontier (the C14 route table's own unprobed rows).** The candidate's route table names
  three routes as `configuration` or `absent` rather than `capability`
  (`corpus/knowledge/round-98-rea-host-readiness.md:55-57`). The next two probes are the two routes
  whose capability is unprobed and whose fixtures already exist in the lane:
  1. **Android capability on an authored APK.** `rea inspect-android-package` is declared by the CLI
     (`rea --llms`, read-only, rc 0) and the lane holds an authored APK fixture with a truth file:
     `corpus/fixtures/apk-r65/fixture.apk` (947 bytes) beside `corpus/fixtures/apk-r65/truth.json`
     (keys `axml_declared`, `build_recipe`, `image`, `members`) and the round-90/91 oracle scripts
     `oracle_check.py`, `oracle_check2.py`, `oracle_check3.py` in the same directory. The r77 provider
     gate for this route is committed as `capability_unavailable` with
     `details.diagnostics.jar_configured: false` and the remediation *"Set REA_JADX_MCP_JAR to the
     absolute path of a caller-supplied jadx-headless-mcp 0.7.1 JAR"*
     (`corpus/live/runs/round-77/provider-gates/android-gate.json`); on this host the variable is now
     set (`env | grep '^REA_JADX_MCP_JAR='` → `/home/vgpnk/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar`,
     42619858 bytes on disk). The probe is therefore unblocked *as configuration*; whether the route
     produces a correct record is still unprobed and must be scored against `truth.json`, not assumed.
  2. **Firmware capability on `fixtures/firmware-r63`.** The lane holds an authored firmware fixture
     with a truth file: `corpus/fixtures/firmware-r63/firmware-r63.bin` (2048 bytes, sha256
     `bdfe9f46…a8510be` per `truth.json`) with `truth.json` keys `build_recipe`, `image`, `regions`
     (5 regions) and a `generator.py`. The r77 firmware gate is committed as
     `capability_unavailable`, `details.provider_id: binwalk`, `details.operation:
     inspect_firmware_regions`, remediation *"requires Linux and an absolute REA_BINWALK_COMMAND path"*
     (`corpus/live/runs/round-77/provider-gates/firmware-gate.json`); on this host
     `REA_BINWALK_COMMAND=/usr/bin/binwalk` and `REA_UNBLOB_COMMAND=/home/vgpnk/.local/bin/unblob`
     are set and `binwalk --version` prints `binwalk 3.1.0`, `unblob --version` prints `unblob 26.6.4`
     (`corpus/live/runs/round-98/host-probes-r98.txt`). Again: configuration present, capability
     unprobed.

  Both probes are *capability* probes in the candidate's own sense (a route was run end to end and
  its output compared with an expected value fixed before the run). The C14 row cannot move to
  `held` on configuration; the ZIP-inventory row is the only route this round that reached that bar.
- **Also carried forward:** the r97 carried items that this round did not close — the `d-host`
  survivor and the v6 tree survivors (`reports/round-97/controls/mutate-v6-kill.out`), the M4 index
  gap (`corpus/knowledge/claude-red-re-bridge.md` still unindexed), and the r97 §6.6 item the
  round-97 lesson listed as M9's byte-exact own-work quote leg (now present in v7 as
  `C1_QUOTE_BYTES`, and refusing `C14-Q01-receipt-span-shift` in the fresh holdout, but not yet
  exercised by a frozen vector).

## considerthese

- **Proposal 5 of `considerthese/2026-11-05.md`** (still unimplemented; proposals 3 and 4 of the same
  file were likewise not adopted, and proposal 1 was mined in r97) — quoted verbatim from
  `considerthese/2026-11-05.md:38`:

  > **Adoption tracking for successor instruments.** `reports/round-91/c1_counter2.py` and
  > `cap_probe2.py` kill the fitted and stub controls but were left unclaimed. I would track daily
  > whether a later round promotes them to frozen claims or lets them go unused, since the repo has
  > a pattern of unclaimed successors that are better than the claimed predicate.

  **How the lane's own bar grounds it.** The bar is already written; the proposal asks for a ledger
  the bar implies. `SKILL.md:37-41` states that *"Registry is the only admission instrument"* and
  that the §Gate registry *"registers 17 instrument blocks (`grep -c '^| name |' SKILL.md`)"* — but
  the count that command prints is now **31** (`grep -c '^| name |' SKILL.md` → 31; it was 17 at
  `d3f4e6c`, 28 at the r97 freeze `85a2c7e`, 31 at `9d49002`). The prose number and its own counting
  command already disagree, so the registry's own text needs the ledger the proposal describes, and
  the successor the proposal names is still unregistered: `grep -c "c1_counter2\|cap_probe2" SKILL.md`
  → **0**, while the files exist and are named as unclaimed successors in the lane's own lesson
  (`corpus/lessons/round-91.md:92-93`: *"the successor `cap_probe2.py` kills them and passes the
  landed instrument (unclaimed)"*; *"held-out 22 cases (unclaimed)"*). This round adds three more
  successors to the same class (`reports/round-98/c1_k_admit_counter7.py`,
  `reports/round-98/forge_reach7.py`, `reports/round-98/mutants/mutate7.py`), so the pattern the
  proposal names is growing, not historical.
  **How the lane's own bar refuses it as written.** The lane's bar admits an instrument through the
  §Gate registry, and the registry's rows carry a `kind` that says gate or probe
  (`SKILL.md:38-40`), a pinned-value path and a self-test row. A *daily* adoption tracker is a paper
  report about a repository, and the lane has repeatedly refused claims of that shape: the r93
  non-author spot-check rejected *"adopting a criterion without its own frozen predicate would
  violate the lane's own bar"* (`corpus/lessons/round-93-verifier-spotcheck.md:78`), and the r95
  lesson adopted proposal 1 of the same file only as practice with a receipt set it then had to call
  PARTIAL (`corpus/lessons/round-95.md:96`). So the honest shape of this proposal for this lane is
  not a daily table; it is a registry-completeness **check** — a counting command over the lane's own
  committed bytes, of the form `grep -c '^| name |' SKILL.md` against the number the prose claims,
  plus one line per unregistered successor naming where it lives and what it kills. That is a
  predicate with a command and a denominator, which is what the bar accepts, and it would have
  caught this round's own stale "17" before a seat had to.
