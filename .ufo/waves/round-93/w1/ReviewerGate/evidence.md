# ReviewerGate evidence — round-93 wave 1, Q-gate on the C08 entry

Final candidate digest this vote binds: `0db16a56fb0c2346d7109999dd6d98123403a52fa67d189112ba5597860593da`.
Seat: ReviewerGate (wave registry member, `kind: spawn`, `role: reviewer`).
Vote artifact: this file (`evidence.md`). Every command below was run by me
on 2026-11-05 from the lane root or my scratch dir
`/fast/scratch/hyaku/revenger-r93/ReviewerGate/`. Lane paths relative to
`/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## 1. Candidate digest history and final binding

- Draft: `.ufo/waves/round-93/w1/ScribeEntry/entry-draft.md`. I sampled it at
  three scribe revisions while the wave was still being written (mtimes
  12:08:56 → 12:14:32 -0300). The draft carries exactly one line matching
  `^admission-status:`, and it is `admission-status: candidate` throughout, so
  the counter digest equals the raw sha256 at every revision I read.
- Revision history (all three recomputed by me with the frozen recipe, and each
  matched the READY then on disk — the scribe refreshed READY in the same
  second as each draft write):
  1. `921563694da4517353199fe49a6e375795d94e7254a07269979303e6b8d1a73d`
     (first READY I read, mid-write);
  2. `03fee3ca6f9c5081123af44c21fb3bb67effa406ec8d5485b907b3c7d1902443`
     (second revision; oracle-fence first lines still `$ $ python3 …`,
     double-dollar typo — the embedded gate refused the block, exit 2,
     `could-not-evaluate: no `$ cmd` blocks or unsupported command`);
  3. final `0db16a56fb0c2346d7109999dd6d98123403a52fa67d189112ba5597860593da`
     (third revision, mtime 12:14:32): both oracle fences now begin
     `$ python3 -B corpus/fixtures/browser-r77/oracle_check.py …` (lines 38 and
     353) — the mechanical defect is fixed at the source (no edit by me), and
     this is the digest my vote binds.
- Final-state verification (`READY` on disk now):
  `sha256=0db16a56fb0c2346d7109999dd6d98123403a52fa67d189112ba5597860593da`.
  MATCH.
- Caveat carried into the vote: if the draft bytes are amended after this vote,
  the digest changes and `C1_VOTES` unbinds (the counter's self-test kills
  sha-mismatched votes). The L1 must land exactly the bytes this digest names.

## 2. S495 — record opening re-run (oracle)

`python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json`

- rc=0; all 18 stdout lines (17 check lines plus the summary) byte-identical to
  the committed opening log's block `reports/round-93/controls/oracle-opening.log`
  (diff of the 18-line oracle block: exit 0; the committed log additionally
  carries a `command:`/`date:` header, an `oracle_exit=0` line and three
  trailing sha256 lines that my rerun file intentionally did not contain).
- Last stdout line: `ORACLE OK (17/17 checks)`.
- My own independent sha256 re-hashes (not copied from the log):
  - `corpus/live/runs/round-77/inspection.json`
    `b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868` — equals
    the frozen pin and the receipt's `stdout_sha256`.
  - `corpus/fixtures/browser-r77/index.html`
    `46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45`.
  - `corpus/fixtures/browser-r77/app.js`
    `fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593`.
- Independently from the oracle, I derived from the committed bytes: the inline
  `<script>` text is `document.title = document.title + " [loaded]";`
  (46 bytes), sha256
  `ee8e9624a274382bf825525637e2db30823eda881461276f6eed7e990b157783`, equal to
  the record's `cdp_hash` for the inline script; app.js is 101 bytes with sha256
  `fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593`, equal to
  its `cdp_hash`; index.html is 316 bytes total. Matches `truth.json` and the
  record (Q03: the expectation side comes from committed bytes, not the record).

## 3. S496 — external row re-fetched and quote located in MY bytes

- URL `https://chromedevtools.github.io/devtools-protocol/`, fetched with curl
  from my scratch dir on 2026-11-05.
- MY fetch: HTTP 200, `content-length: 35462`, `last-modified: Wed, 04 Nov 2026
  04:38:14 GMT`, `etag: "6aeab6b6-8a86"` — identical to the scout receipt.
- MY body sha256 `ba8018bb02f360686cbff23304da8b6e21923a2e012ade273e3f9a2ce1e2fd64`,
  length 35462 — byte-identical to ScoutRecord's committed raw body
  (`quote-receipts/raw/S496.body` re-read and re-hashed: same digest).
- Quote `"It allows tools to instrument, inspect, debug, and profile Chromium,
  Chrome, and other Blink-based browsers."` — 15 ≤ 25 words, 108 chars:
  - located in MY fetched bytes at raw span 3410–3528 (unique full match); the
    receipt span 3408–3526 covers the same 108 chars starting at the preceding
    sentence-ending `. ` two bytes earlier; the two spans overlap on every
    quote character;
  - the verifier's own rule (`norm(body[span]) == norm(quote)`, whitespace
    collapse) checked by me on MY bytes at the receipt span: PASS;
  - full normalized-body containment in MY body: PASS.
- Anchor verified in MY bytes: second sentence of the `landing-hero` intro
  paragraph, directly after "The <b>Chrome DevTools Protocol (CDP)</b> is a
  JSON-based protocol that connects debug and automation targets (such as
  browsing contexts and workers) with trusted debug and automation clients."
  No bare homepage-only anchor. `ms.date` marker: absent from the page.
- Receipt comparison: no drift — same body sha256, same length, same headers,
  same quote, same span under the counter's normalisation, verdict `verified`.
- Round-73 supporting procedure applied: only the inside-delimiters text was
  compared against the source; the word count alone was not treated as
  attribution.
- Tooling channel recorded: curl (curl 8.x system binary, preinstalled; no
  install this session — pacman paused, uv unused).

## 4. Corpus gates over the draft

Run from the lane root on the draft (revision history in §1; the gate line
below shows the FINAL revision, after the scribe's own §7 fix):

- `python3 -B corpus/lint_entry.py --entry <final draft> --lane .`
  → `LINT_QMAP=0  LINT_Q14=0  LINT_Q15=0  LINT_HEADER=0`, exit 0.
- `python3 -B corpus/check_embedded_outputs.py --entry <final draft>`
  → `checked_blocks=2 problems=0`, exit 0 (the mid-write revision 2 refused
  with exit 2; recorded in §7).

## 5. Embedded `$ `-block and `transcript —` block re-runs (my mechanical gate)

The draft has two `$ `-marked replayable blocks (item 1 and `## Reproduce`,
both the oracle command) and seven `transcript — python3 -B -c '…'` one-liner
blocks. The gate refuses to replay `python3 -c` (`run_cmd` confines argv[0] to
`python3|python|sys.executable`; `confined()` requires the first non-`-` arg to
be a relative in-tree script with no `..` and no symlink escape) — so I re-ran
each declared transcript command by hand and diffed:

| block | command (abbreviated) | rc | verdict |
|---|---|---|---|
| item 1 T1 | `python3 -B -c 'import json,re;d=json.load(open("corpus/live/runs/round-77/inspection.json"));…'` | 0 | 5/5 output lines verbatim match |
| item 2 T2 | `python3 -B -c 'import json;d=…; n=d["normalized_result"]; …'` | 0 | 10/10 verbatim |
| item 3 T3 | `python3 -B -c 'import json,pathlib;…'` | 0 | 4/4 verbatim |
| item 4 T4 | `python3 -B -c 'import hashlib,json,pathlib,re;…'` | 0 | 5/5 verbatim |
| item 5 T5 | `python3 -B -c 'import hashlib,pathlib;…'` | 0 | 9/9 verbatim — exact argv extracted with shlex from the fence's `transcript —` line and re-executed; stdout compared line by line against the nine embedded lines, all OK, no extra lines, rc 0 |
| item 6 T6 | `python3 -B -c 'import json;print(json.dumps(json.load(open("corpus/fixtures/browser-r77/truth.json"))["volatile_not_compared"],indent=1))'` | 0 | 6/6 verbatim |
| item 6 T6b | `python3 -B -c 'import json;d=json.load(open("corpus/live/runs/round-77/inspection.json"));…'` | 0 | 3/3 verbatim |
| `$ ` oracle (item 1 + §Reproduce) | `python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json` | 0 | 17/17 check lines + `ORACLE OK (17/17 checks)` verbatim |

8 distinct commands re-run; no embedded-output drift anywhere.

The entry-side honesty of the declared gate strategy is verified: the §1
reading rule claims the gate refuses `python3 -c` one-liners and replays `$ `
blocks; the committed gate code (`parse_blocks`, `confined`, `run_cmd`) does
exactly that — no guard-credit overreach (Q13/Q16 spot-checked).

## 6. Q-map decisions carried

The draft's own `## §Q-map` states Q01–Q17 rows; Q08 is explicitly superseded
by Q11 (QUALITY.md is normative here); Q05 (no capability claim made) and Q12
(no rejected source row cited) are n/a with reasons; all others are PASS per
my independent verification in §§2–5. My vote mirrors that, and the digest
history (§1) plus the mid-write gate refusal (§7) are recorded here rather
than smoothed over.

## 7. Mechanical gate over the final draft (was a defect in revision 2; resolved)

At draft revision 2 (`03fee3ca…`) both oracle fences began

```
$ $ python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json
```

Per the entry's own §1 reading rule and `check_embedded_outputs`' spec, the
first line of a replayable block must be exactly `$ ` + the argv; the doubled
`$ ` left a literal `$` as argv[0], which `run_cmd` refuses (argv[0] outside
`python3|python|sys.executable`) → `could-not-evaluate: no `$ cmd` blocks or
unsupported command`, exit 2 — which would have forced `C1_EMBEDDED=fail` and
`C1_VERDICT=fail` on the landing tree.

At the final revision (`0db16a56…`, mtime 12:14:32) the scribe fixed both
fences to

```
$ python3 -B corpus/fixtures/browser-r77/oracle_check.py corpus/fixtures/browser-r77/truth.json corpus/live/runs/round-77/inspection.json
```

(lines 38 and 353; single `$`, then the argv; verified by my line dump). I
re-ran the full gate chain on those bytes:

- `python3 -B corpus/lint_entry.py --entry <final draft> --lane .`
  → `LINT_QMAP=0  LINT_Q14=0  LINT_Q15=0  LINT_HEADER=0`, exit 0;
- `python3 -B corpus/check_embedded_outputs.py --entry <final draft>`
  → `checked_blocks=2 problems=0`, **exit 0** (both oracle blocks replayed
  clean; the seven `transcript —` blocks stay outside the gate by its own
  confinement rule, which the entry's §1 reading rule declares honestly).

Both fences' embedded 18 output lines are covered verbatim by my own oracle
re-run (fence@37 and fence@352, zero uncovered lines). The entry passed every
criterion of the embedded gate once fixed; the seven transcript one-liners were
verified by me mechanically as §5 records.

## 8. Explicitly not checked (no claim made)

- The post-land state of the C08 row in `corpus/README.md` (pre-land only:
  C08 `uncovered`, knowledge cell `—`, K_HELD_BACKED 9/15 — matches the frozen
  claims' "before" and the committed do-nothing control).
- Other seats' votes in `reports/round-93/votes/`.
- `forge_battery.py` / `c2_legend_counter2.py` internals (C2 side — CriticR93
  and MutationR93 hold that attack lane).
- The landed `corpus/SOURCES.md` S495/S496 rows (I verified the quotes the two
  rows carry, via oracle re-run + my own S496 fetch and span check; the landed
  row byte shapes are the L1's write surface, not mine).

## 9. Post-revision re-check — the L1's landed revision `53083246…fb1` (2026-11-05)

The L1 amended the entry after my first-binding vote (digest `0db16a56…`):
(a) removed the underived sentence "The stdout line count of the oracle block
is 18." (draft lines ~374–375; Q11/Q16 gap the critic routed); (b) removed the
"(15 words)" parenthetical from the S496 paragraph; (c) set
`admission-status: admitted`; (d) landed the bytes at
`corpus/knowledge/round-93-browser-cdp-runtime-evidence.md`. Lands differ from
the draft only by: the admission-status line (`candidate` → `admitted`) and
those two sentence removals — verified by line-level diff (draft 375 lines →
landed 374; all content lines otherwise equal).

- Recomputed (counter recipe, admission-status line normalised to candidate):
  `53083246d5528eab8682f5938e4f1b0967683ae883499d15d702d9f671bd1fb1` — equals
  the L1's stated normalized digest. Raw sha256 of the landed bytes
  (`admission-status: admitted` as-is): `f62390c9a192777e39a1bfb5d4bd07f0f50cbb6735c81ebe69659594b85d4787`.
- Q11 re-check of the removal: the deleted sentence credited the oracle block
  with a stdout line count no command in the entry prints (the oracle prints
  its own `ORACLE OK (17/17 checks)` summary, which is the count basis the
  entry keeps); removal restores the §Q16 rule that a credited number is only
  one the command prints. No other derivation moved; the §5 provenance table
  row that previously carried the count claim needed no line (deleted with the
  sentence, table intact at 8 rows).
- Q16 re-check of the "(15 words)" removal: the word count was my own measure
  (15 words confirmed by me in §3, ≤25) but the entry had no command printing
  "15 words"; removing the parenthetical leaves only the located quote and the
  anchor. S496 paragraph now reads `Located quote used here: "It allows tools
  …"` — no count claim, same quote bytes, same anchor sentence (landing-hero,
  second sentence after the CDP JSON description). My §3 byte verification
  (span, 14-word-after-trim characterization above stands as my own evidence,
  not part of the entry text) is unchanged.
- Gates re-run on the LANDED bytes:
  - `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-93-browser-cdp-runtime-evidence.md --lane .`
    → `LINT_QMAP=0  LINT_Q14=0  LINT_Q15=0  LINT_HEADER=0`, exit 0 (§Q-map 17
    rows present in the landed file).
  - `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-93-browser-cdp-runtime-evidence.md`
    → `checked_blocks=2 problems=0`, **exit 0** (both `$ ` oracle fences replay;
    both open with a single `$ `).
- Header S-ids in the first 15 lines: exactly `S495` and `S496`; both rows are
  now in the landed `corpus/SOURCES.md` (S495 line 512, S496 line 513, peer
  row S497 line 514), status/opened/used-by check delegated to the counter,
  not my claim here.
- `audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts
  reports/round-93/quote-receipts --range 495-497`: `S496 verified (ok)`,
  `S497 verified (ok)`, `S495 state=unresolved (receipt missing/unreadable:
  S495.receipt.json)` — expected, because S495 is own-work with no `http` in
  its source cell and needs no receipt (my §5 check; matches ScoutRecord's own
  scope note); the counter's C1_QUOTES leg is over EXTERNAL header rows only.
- The §1 revision history and §7's double-`$` defect record above still speak
  about the pre-land draft revisions — both kept for the audit trail; the
  binding digest for the landed tree is the §9 recomputed value in my rewritten
  vote.
- Re-binding: votes rewritten at
  `reports/round-93/w1/ReviewerGate/vote.json` with
  `candidate_sha256 = 53083246d5528eab8682f5938e4f1b0967683ae883499d15d702d9f671bd1fb1`,
  notes for Q11 and Q16 updated for the removals, `artifact_path` unchanged,
  and `artifact_sha256` = sha256 of this file after this append.

## 10. Second re-bind — verified-at clause rescoped (final digest `1304008c…647`, 2026-11-05)

The L1 further amended the entry: the `verified-at:` byte-identity claim is
now scoped to `corpus/live` and `corpus/fixtures` only ("git diff --quiet
02050cb2a6758e3bd9cec696ff0e42df6f23511a -- corpus/live corpus/fixtures is
silent, so the saved records and fixtures read here are byte-identical at
that commit; the corpus index and registry files changed at the round-93
landing and are not claimed identical").

- Q15 re-check (the clause's own deriving commands, run by me):
  - `git rev-parse 02050cb2a6758e3bd9cec696ff0e42df6f23511a^{commit}` →
    `02050cb2a6758e3bd9cec696ff0e42df6f23511a` (rc 0);
  - `git diff --quiet <oid> -- corpus/live` → silent, rc 0;
  - `git diff --quiet <oid> -- corpus/fixtures` → silent, rc 0;
  - `git diff --quiet <oid> -- corpus` → rc 1 (NOT identical — the whole-corpus
    identity sentence would have been false after the landing; the rescope
    fixes exactly that, so Q15 moves from truth-dependent to true).
- The recomputed normalized digest (admission-status line → candidate) of the
  landed bytes: `1304008c5a0aff9dbb9af09967e12caeef028b1ca52e14dac7b8fe0247e43647`
  — equals the L1's stated value; raw sha256
  `1fc006560dd543bcb28990cd9530260f7851766b99e69057c7c9e05f225fbe5e`.
- Gates re-run on the re-scoped bytes: lint `0/0/0/0` exit 0;
  `check_embedded_outputs` `checked_blocks=2 problems=0` exit 0.
- Vote re-bound: `candidate_sha256 = 1304008c…647`, notes Q02/Q15 updated,
  artifact_path unchanged, artifact_sha256 = sha256 of this file after this
  append.
