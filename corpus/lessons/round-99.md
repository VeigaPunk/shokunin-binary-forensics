# Round 99 — gate, mistakes, frontier (revenger, hyaku run 15, attempt 1)

Base `3d054a98e3fa768e63b631665a2372fadb51a77a`. Claims frozen at `7e6edd4db649f99c425daa46a91edbbd18a6e27c`;
Amendment A at `61e27feb4e8099af7f9bf41fbf69e223354f691e`; Amendment B (the single candidate amendment) at
`9ddd38ac8baef67d689ac36fa233aaaef35b1703`; v8 freeze at `01266760d9918b868f7cd8a25dd5cf6e1052d193`.
Landing = the commit that carries this file (hash in the report). Drafted by ScribeLessonR99
(`.ufo/waves/round-99/w1/ScribeLessonR99/round-99-lesson-draft.md`), integrated by the L1.

**Verdicts of record (lane-internal; admission is the non-author closure's):**
- C1 coverage, K 13/15 → **14/15**: v8 `--profile c14r99` on the landing tree prints
  `C1_K_HELD_BACKED=14/15`, `C1_VERDICT=pass`, rc 0. Controls after the v8 freeze: do-nothing `fail`,
  junk-row `fail`. Votes on digest `246d09a8…`: VoterGateR99, VoterBlindR99, CriticR99, 0 FAIL.
- C2 calibration, r98 holdout **9/12 → 0/12** accepted (v7 → v8), both controls `control-ok`, stub ok,
  twelve `C2_VECTOR` lines, `C2_VERDICT=met`. Development set; the fresh round-99 holdout is accepted
  **12/12** by v8 (no generalization).

## Gate

### C14 candidate — the r98 → r99 edit

Entry `corpus/knowledge/round-98-rea-host-readiness.md`. The only change between base and freeze is
this entry (`git diff --stat 3d054a98 7e6edd4 -- corpus/knowledge/round-98-rea-host-readiness.md` →
1 file, 17 insertions, 10 deletions; five hunks at `@@ -64,4 +64,7`, `-69,3 +72,3`, `-83 +86,5`,
`-125 +132`, `-130 +137`). Full diff: `.ufo/waves/round-99/w1/ScribeLessonR99/candidate-diff-r98-to-r99.diff`.

| change | where (freeze tree) | what the record now shows |
|---|---|---|
| "three installation paths" row | `:89` (was `:83`) | `installation paths ("three")` counts paths: `grep '^    paths\[3\]: ' … \| sed 's/^    paths\[3\]: //' \| tr ',' '\n' \| grep -c .` → `3`; `installation state` (`:90`), `grep -c '^    state: multiple' …` → `1` |
| ghidra scope-check names | `:86` (new) | eight names, `ghidra ghidra-platform ghidra-architecture ghidra-installation ghidra-version ghidra-headless ghidra-native_decompiler ghidra-java` |
| doctor-printed versions | `:87` (new) | `ghidra-version` detail `12.1.4`, `ghidra-java` detail `21.0.13`, both credited to the doctor record and derived by command |
| engine and jadx classifications | `:88` (new) | `hopper`, `ida-registration`, `kuna-installation` = `missing_analysis_engine`; `jadx` = `healthy` |
| preamble | `:64-74` | two versions credited to the doctor record and derived; the remaining version strings credited to the probe transcript |
| Q11 and Q16 PASS notes | `:132`, `:137` | amended to name the path-count row and the doctor-attributed versions |

Derivation rows: 17 at base, 21 at freeze (python diff over the derivation table: added 5, removed 1).
The route-table cell at `:59` still reads "Doctor lists three such installation paths", which is now
derived at `:89`.

**Vote-binding digest (v7 `digest()` rule: sha256 of the entry text with every admission-status line
normalized to `admission-status: candidate`).** Recomputed by the scribe from the committed bytes:

```
python3 -c "import re,hashlib,subprocess;old=subprocess.run(['git','show','3d054a98e3fa768e63b631665a2372fadb51a77a:corpus/knowledge/round-98-rea-host-readiness.md'],capture_output=True,text=True).stdout;new=open('corpus/knowledge/round-98-rea-host-readiness.md',encoding='utf-8').read();d=lambda t:hashlib.sha256(re.sub(r'(?im)^\s*admission-status\s*:.*$','admission-status: candidate',t).encode()).hexdigest();print(d(old));print(d(new))"
6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f   (base, r98 1b76b4d)
36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5   (freeze 7e6edd4)
```

The digest moved from `6d27c129…5330f` to `36cc6ac2…fce5`, so every r98 vote (superseded) is void for
r99. Both `admission-status` lines read `admission-status: candidate` at base and at freeze.

**Lint.** `reports/round-99/controls/lint-candidate-freeze.log` records `LINT_QMAP=0 LINT_Q14=0
LINT_Q15=0 LINT_HEADER=0`, rc 0, written at the freeze. The scribe did not re-run it.

**S506 re-open** (`reports/round-99/quote-receipts/S506-reopen-r99.txt`). URL at pinned revision
`12f6e09`; `fetched_at=2026-11-05T18:43:20-03:00`; `http=200`; `bytes=16650`; sha256
`ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50`, byte-identical to the committed
body (`cmp=identical`). Located quote, 11 words, 76 bytes, verbatim: *"Static JavaScript and ordinary
ZIP inventory need neither Hopper nor Ghidra."* Counts: `grep -c -F` on
`reports/round-98/quote-receipts/raw/S506.body` → `1`; `head -c 7202 … | tail -c +7127` prints the
sentence (span 7126–7202, as in `S506.receipt.json`).

**S507 re-hash** (`reports/round-99/controls/s507-reopen-r99.txt`). The three saved records
`corpus/live/runs/round-98/{host-probes-r98.txt,rea-doctor-r98.txt,rea-inspect-artifact-archive-r2.txt}`
re-hash to `94eaa6ff…`, `fb9a4824…`, `c373f656…`, equal to the r98 values. Located quote: *"healthy:
false"* / *"environment_healthy: false"*, bytes 1–41 of `rea-doctor-r98.txt` (`head -c 41` → 41 bytes,
both lines).

The Amendment-B digest supersedes this one (below).

### Amendment A — S505 grounded by citation (registry row, logged old → new)

ReviewerClaimsR99 F1: v7/v8 `c14` check `C1_USEDBY_GROUNDED` over S505, and S505's `used-by` named an
entry that never cites it, so C1 was unreachable through the declared surface. The r98 correction
(`mined → queued`) harms C02 (`S504:terminal-mined-expected:S505:queued`). Applied instead:

| row | cell | old | new |
|---|---|---|---|
| S505 | `used-by` | `corpus/knowledge/round-96-native-analysis-sessions.md` | `corpus/lessons/round-97.md` |

Reason: `corpus/lessons/round-97.md` introduced S505 and cites it (`grep -cw S505 corpus/lessons/round-97.md`
→ 3); status stays `mined`, the S504 → S505 chain stays terminal-mined. Evidence before landing:
`reports/round-99/controls/amendA-s505-scratch.log` (v7 `c02` pass, K 13/15, rc 0; v7 `c14`
`C1_USEDBY_GROUNDED=pass`; census ok). This closes the r97 spot-check §6.1 / r98 routed defect 4 without
touching C02's entry or votes.

### Amendment B — the single candidate amendment (VoterGateR99 Q16 FAIL)

VoterGateR99 voted Q16 FAIL on `36cc6ac2…`: the "scope-check classes" output cell was not the command's
stdout (`.ufo/waves/round-99/w1/superseded-votes-digest-36cc6ac2/VoterGateR99.json`). CriticR99 reported the
same row plus the S507 "exit 1", the unprinted "of 8" denominator, the substep status not tied to its
operation, underived member labels and root digest, and a causal clause stated as observation, before
casting any vote. ScoutReopenR99 found the same class (its §3 MISMATCH and G1).

Fix: a stated cell rule (one code span per stdout line, annotation only after an em dash) and a
regenerated 29-row derivation table; a new instrument `reports/round-99/controls/deriv_check.py` re-runs
every row. **Shown able to fail:** the claims-freeze entry → `DERIV_ROWS=21 DERIV_MISMATCH=7`, rc 1; the
amended entry → `DERIV_ROWS=29 DERIV_MISMATCH=0`, rc 0 (`reports/round-99/controls/amendB-deriv-check.log`).
New digest `246d09a8cf6523ab380f88f7945f220338c27e31f8b43ba876bbd0a9a8d746da`.

Registry row changed in the same amendment, logged old → new:

| row | cell | old | new |
|---|---|---|---|
| S507 | `teaches` (fragment) | `the \`rea doctor\` receipt (CLI 6.7.0, exit 1)` | `the \`rea doctor\` receipt (CLI 6.7.0; its exit code 1 was observed in the L1 session and is not a line of the record)` |

Reason: the doctor record prints no exit line (`grep -c exit corpus/live/runs/round-98/rea-doctor-r98.txt` → 0),
and the entry itself credits the exit code to the session.

Votes on `246d09a8…` (`reports/round-99/votes/`): VoterGateR99 10 PASS / 7 n/a / 0 FAIL; VoterBlindR99
11 PASS / 6 n/a / 0 FAIL; CriticR99 12 PASS / 5 n/a / 0 FAIL. The superseded `36cc6ac2…` votes are kept in
`.ufo/waves/round-99/w1/superseded-votes-digest-36cc6ac2/`. VoterBlindR99 observed that the entry's own
§Q-map Q13 rationale ("no verifier is credited") is stale against the new Q11/Q16 rows, which credit
`deriv_check.py`; it scored Q13 on substance (PASS). Not fixed: no amendment remained. Routed to r100.

### C1 — measured after the v8 freeze

| tree | command | result |
|---|---|---|
| do-nothing (archive of `61e27feb`) | `reports/round-99/controls/make_c1_controls_r99.sh reports/round-99/c1_k_admit_counter8.py <work>` | `C1_CONTROL_DONOTHING=fail`, counter rc 1 |
| junk-row (same, C14 cell `held` only) | same run | `C1_CONTROL_JUNKROW=fail`, counter rc 1 |
| landing | `PYTHONUTF8=1 python3 -B reports/round-99/c1_k_admit_counter8.py --profile c14r99 --tree <landing archive>` | `C1_K_HELD_BACKED=14/15`, `C1_VERDICT=pass`, rc 0 |

Receipts: `reports/round-99/controls/post-freeze/`.

**C02 no-harm, and a rule miss.** The claims carried r98's A1 diagnostic rule: "no harm to C02 when … every
failing c02 leg is `C1_ONLY_TARGET` naming only C14". On the landing tree v8 `--profile c02` fails
**two** legs: `C1_ONLY_TARGET` (`C1_ONLY_TARGET_DIFFS=C14`) and `C1_K_HELD_BACKED` (K = 14, while the c02
profile pins 13). The second is the C14 flip itself, so the rule as written is not met (M19). The C02
bytes are unharmed: the same landing tree with only the two C14 flip lines reverted (README C14 row and
the entry's admission line) passes v8 `c02` and v7 `c02` (`C1_VERDICT=pass`, K 13/15, rc 0;
`post-freeze/landing-c14unflipped-c02{,-v7}.log`), and the C02 README row is byte-identical to the base.

### C2 — measured after the v8 freeze

`reports/round-99/controls/post-freeze/c2-v8-frozen.log` (clean clone at `01266760`): twelve `C2_VECTOR`
lines, each refused by its named v8 leg (V01 `C1_VOTES_GLOB`, V02 `C1_NA_REASON`, E01 `C1_RECHECK_CMD`,
E02 `C1_HEX_CLAUSES`, E03 `C1_COVMAP_ROW`, R01(c14) `C1_ROW_IDS`, V02(c14) `C1_DECISION_KEYS`, O01
`C1_OWNWORK_ROUND`, L01 `C1_FETCHLOG_DATE`; the three v7-refused vectors stay refused), `C2_ACCEPTED=0/12`,
`C2_CONTROL_C02=control-ok`, `C2_CONTROL_C14=control-ok`, `C2_STUB_SELFTEST=ok`, `C2_VERDICT=met`, rc 0.
No regression: `forge_reach7.py --counter <v8> --profile c02` → `C2_ACCEPTED=0/5`, both positives pass,
met (`noreg-forge7-v8-c02.log`); `--self-test` → `SELFTEST_C1V8=OK legs=98`, rc 0 (`selftest-v8-frozen.log`).

**Fresh round-99 holdout** (CriticR99 `build_fresh99.py`, run once by the L1 after the freeze):
v8 accepts **6/6** c02 and **6/6** c14 (`post-freeze/holdout99-v8-{c02,c14}.log`), the same as v7
(`.ufo/waves/round-99/w1/CriticR99/fresh/holdout99-*-v7.log`). The C2 gain is a development-set gain.
One class, C14-N3 (a derivation count row edited to print 15 where the record prints 14), is exactly what
`deriv_check.py` refuses but no counter leg runs — routed to r100.

### Census

Round start: exit 0, 21 × W01, 13 × W04, 0 E-codes (`reports/round-99/controls/census-round-start.log`).
Round end: see `reports/round-99/controls/census-round-end.log`.

## Mistakes

| # | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| M16 | **count by lines, not paths:** the r98 route table stated "Doctor lists three such installation paths", and the row that should derive it counted `paths[3]:` *lines*. The record prints three comma-separated paths on one line, so the recorded command printed `1` against a claimed `3`. | `reports/round-99/controls/q11-paths-old-vs-new.log`: old `grep -c '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt` → `1`; new `grep '^    paths\[3\]: ' corpus/live/runs/round-98/rea-doctor-r98.txt \| sed 's/^    paths\[3\]: //' \| tr ',' '\n' \| grep -c .` → `3`. Re-run by the scribe with the same two outputs. Captured in r98 by the critic's Q11 FAIL (`reports/round-98/votes/CriticR98.json`; `corpus/lessons/round-98-verifier-spotcheck.md:109`). | CriticR98 vote Q11 (digest `6d27c129…`) | the **path-counting derivation row** (`:89`). Shown able to fail: the old command prints `1`, so the old row cannot back a `3`; the new row prints `3`. |
| M17 | **version credited to a transcript that does not print it:** the r98 preamble said each version string "comes from the probe transcript". `ghidra-version 12.1.4` appears zero times in `host-probes-r98.txt` and seventeen times in the doctor record. | `reports/round-99/controls/q16-version-attribution.log`: `grep -c -F <version>` per record — `12.1.4` host-probes `0`, doctor `17`; `21.0.13` host-probes `3`, doctor `3`; `6.7.0` host-probes `1`, doctor `11`. Re-run by the scribe. | CriticR98 vote Q16 (digest `6d27c129…`) | the **attribution**: `12.1.4` and `21.0.13` are credited to the doctor record and derived by command (`:87`, `:72-74`); the transcript is credited only for strings it prints (`6.7.0`, `1.5.6`, `3.1.0`, `26.6.4`). Shown able to fail: the `12.1.4` count against the transcript is `0`, so the old credit fails by the same command. |
| M18 | **seat-name collision across rounds:** the r98 re-vote messages were addressed to `ReviewerGate` and `ReviewerBlind`, the seat names of earlier rounds, not the r98 instances `ReviewerGate-6` and `ReviewerBlind-5`. The earlier-round seats declined and wrote nothing, so the re-vote silently reached no r98 seat. | `.ufo/waves/round-99/w1/ScribeLessonR99/m18-seat-name-collision.txt`: `for f in .ufo/waves/round-9*/w1/swarm-registry.json; do …; done` lists `round-93,94,95,96,98: ReviewerGate,ReviewerBlind` and `round-97: ReviewerGate` (six registries); the r98 report line is `/home/vgpnk/Projects/shokunin/.ufo/reports/round-98/revenger.md:36`. | **none** (the r98 report recorded it by hand; no check, no lint, no roster test) | **round-suffixed seat names in r99** (`VoterGateR99`, `VoterBlindR99`, `CriticR99`, and the rest of the twelve members of `.ufo/waves/round-99/w1/swarm-registry.json`, none of which appears in the list above). Shown able to fail: the same command finds the r98 names in six registries, so the name test rejects reuse. |
| M19 | **no-harm rule copied without re-deriving it for a K move:** r99's claims reused r98's A1 rule ("every failing c02 leg is `C1_ONLY_TARGET`"), written when the c14 flip had not landed. A landed flip also moves K, and the c02 profile pins `HELD_TARGET=13`, so `C1_K_HELD_BACKED` fails by construction. | `reports/round-99/controls/post-freeze/landing-c02-diag.log` (`C1_ONLY_TARGET_DIFFS=C14`, `C1_K_HELD_BACKED=14/15` → leg `fail`, rc 1) versus `landing-c14unflipped-c02.log` (pass, rc 0) | none — the rule was frozen as a sentence, never run on a landing-shaped tree before the freeze | a no-harm rule for a profile is run once on a landing-shaped scratch tree before the claims freeze, and names every leg the target move is expected to fail; for c02 under a C14 flip that set is `C1_ONLY_TARGET` and `C1_K_HELD_BACKED`. Shown able to fail: the r99 receipt above |
| M20 | **output cells normalized by hand (Q16 class, recurring):** the r98/r99 candidate's derivation cells dropped prefixes, padding and path columns that the commands print, while the preamble claimed verbatim stdout. Three seats found it independently; the r98 critic had passed the same rows. | `reports/round-99/controls/amendB-deriv-check.log` (7 mismatches on the claims-freeze entry); `.ufo/waves/round-99/w1/superseded-votes-digest-36cc6ac2/VoterGateR99.json` Q16 | a FAIL vote (human), no instrument | `reports/round-99/controls/deriv_check.py` (re-runs each row, compares with the cell under the entry's stated rule); shown able to fail 7 → 0 |

Shown able to fail: M16 (`q11-paths-old-vs-new.log`, 1 vs 3); M17 (`q16-version-attribution.log`); M18
(`.ufo/waves/round-99/w1/ScribeLessonR99/m18-seat-name-collision.txt`; r99 seats are round-suffixed and
the r99 re-vote messages reached the r99 seats); M19 and M20 as above.

## Frontier

- **Census.** Before exit 0; after: see the report.
- **Rows.** 507 → 507 (no row added). Rows touched old → new: S505 `used-by` (Amendment A), S507
  `teaches` fragment (Amendment B). S506 re-opened this round at its pinned revision (2026-11-05T18:43:20-03:00,
  http 200, 16650 bytes, sha256 `ce2d122b…`, byte-identical; `reports/round-99/quote-receipts/S506-reopen-r99.txt`;
  ReviewerClaimsR99 and ScoutReopenR99 re-fetched it independently, identical). S507 records re-hashed equal
  and re-produced live byte-identical by ScoutReopenR99 (`rea doctor` rc 1, `rea inspect-artifact` rc 0).
- **Frontier row advanced:** C14 `partial → held` (pending the non-author closure).
- **Next probes, still unprobed.** Android capability on `corpus/fixtures/apk-r65/` and firmware capability on
  `corpus/fixtures/firmware-r63/`: configured on this host, capability unprobed (ScribeLessonR99 draft).
- **Assimilation.** `merge/revenger/` present; 155/155 staged ids collide with the 507-row registry
  (ScoutReopenR99 `collision-check-r99.log`), unchanged since r97. Stays on L0; nothing adopted.
- **Routed to r100:** (1) the fresh r99 holdout (12/12 accepted by v8), with a leg that runs `deriv_check.py`
  for C14-N3; (2) the entry's stale §Q-map Q13 rationale; (3) `d-host` (killed by the v8 self-test only,
  `MUTANT_KILL_V8=154/309` tree, `MUTANT_SELFTEST_V8=285/309`, MutationR99); (4) M4 `claude-red-re-bridge.md`
  index-or-reject; (5) the producer-attribution census (considerthese below).

The mutate7 baseline exit 3 (r98 routed defect 5) is reconciled: mutate7's `SELFTEST_PASS` regex expected
`=pass` while the counter prints `=OK`, so a passing counter was classed as a baseline failure; mutate8 accepts
`=OK|=pass` and exits 3 only on a real failure (shown on a forced-FAIL copy, rc 3) (`.ufo/waves/round-99/w1/MutationR99.md` §1).

## considerthese

**Proposal 4 of `considerthese/2026-11-05.md`** (not mined in r97 or r98; r98 recorded proposals 3 and 4
as "likewise not adopted") — quoted verbatim from `considerthese/2026-11-05.md:37`:

> **Upstream drift watch for the tool the lane tests.** Round 89 evidence puts the host at `rea` 6.7.0
> and the registry's latest at 6.8.0. I can read the public changelog read-only each day and list
> operations or format changes the lane has no oracle-checked record for.

**How the lane's own bar refuses it as written.** A daily changelog reader is a paper report about an
upstream product. The lane refused that shape before (the r93 spot-check: "adopting a criterion without
its own frozen predicate would violate the lane's own bar", `corpus/lessons/round-93-verifier-spotcheck.md:78`).

**What the lane's own committed bytes and host show now.** The proposal's premise is observed, but in
the lane's records, not upstream. Measured by the scribe (`.ufo/waves/round-99/w1/ScribeLessonR99/proposal4-measurements.txt`):

| measurement | command | output |
|---|---|---|
| live records naming `rea 6.8.0` | `grep -rl 'rea 6\.8\.0' corpus/live/runs/ \| wc -l` | `15` (rounds 76–85) |
| doctor records with `cli_package_version: 6.7.0` | `grep -rl 'cli_package_version: 6\.7\.0' corpus/live/runs/ \| wc -l` | `2` (`round-96/rea-doctor-r96.txt`, `round-98/rea-doctor-r98.txt`) |
| doctor records with `cli_commands: 153` / `175` | `grep -rl 'cli_commands: 153' …` / `… 175` | `2` / `0` |
| S444 records the 6.8.0 manifest as `cli_commands: 175` | `grep -n 'cli_commands: 175' corpus/SOURCES.md \| cut -c1-60` | `459:` (S444) |
| PROVINCE says 6.8.0 is installed | `grep -n 'installed on this host at 6.8.0' PROVINCE.md` | `22:` (2026-10-31) |
| host binary | `rea --version`; `…/rea-agents/package.json` version | `6.7.0`; `6.7.0` |

The records name two producers. Fifteen live files, from rounds 76 to 85 (the 6.8.0 era the records
themselves name), say `rea 6.8.0`; the two doctor records (r96, r98) say `6.7.0` and 153 commands.
Nothing in the committed bytes dates the change, and the scribe did not establish the cause.

**Operation census against the installed manifest** (the proposal's "no oracle-checked record" test):
153 declared commands (`rea --llms` on this host, saved at `.ufo/waves/round-99/w1/ScribeLessonR99/rea-llms-6.7.0-host.txt`);
30 distinct recorded `operation` names across `corpus/live/runs/`; 22 have a declared kebab twin; 8 have
none in 6.7.0 (`current_document`, `get_android_manifest`, `get_app_info`, `inspect_pe_certificates`,
`inventory_artifact`, `load_apk`, `open_binary`, `rea_jvm_status`); 131 declared commands have no recorded
operation. The 8 include `inspect_pe_certificates`, which S453 records as a 6.8.0 surface, so the records
were made by a producer the installed manifest does not declare.

**How it lands.** Not as a daily tracker. As a counting predicate over committed bytes and the host, with a
denominator, which is what the bar accepts. Proposed for r100 with its own frozen predicate, not adopted:
`producer-attribution census`. A live record's producer version must equal the `cli_package_version` of the
doctor record captured in the same round, or the record is labelled with the version it names, not the
host's current version. The census above is its first run: none of the 15 `6.8.0` records has a
same-round doctor record naming 6.8.0. The proposal's operation-coverage half is the 22/8/131 split above,
and it lands as a Frontier count, not a criterion, until a round freezes it.
