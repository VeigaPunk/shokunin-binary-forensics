# CriticR93 — attack pass on round-93 C1 (K admit) and C2 (calibration)

Scope: read-only attack on the frozen v2 counters (`reports/round-93/c1_k_admit_counter2.py`,
`reports/round-93/c2_legend_counter2.py`, `reports/round-93/forge_battery.py`) and the
claims in `reports/round-93/claims.md`. Lane HEAD 02050cb. No frozen file edited. No git
mutation. No install. Every attempt ran the counter with `--tree` on a tree built in scratch
from `git archive 281a5bad66e844190a570cb35d257c6974749993` (the freeze base), with the
round-93 wave registry copied in. Counter outputs are under `receipts/`.

Reproduce (scratch is created by the scripts; they never write the lane):

    S=/fast/scratch/hyaku/revenger-r93/CriticR93
    mkdir -p "$S" && cp .ufo/waves/round-93/w1/CriticR93/attacks/*.py "$S"/
    python3 -B "$S"/attacks.py all     # A0-A20 (C1 and C2 verdicts per attempt)
    python3 -B "$S"/attacks2.py        # A21-A27 and A23 control
    python3 -B "$S"/attacks3.py        # H0 honest real-tools control, R1-R9 real-tools bypasses
    HYAKU_SCRATCH="$S/hs" python3 -B reports/round-93/c1_k_admit_counter2.py --tree "$S/trees/R9-all-bypasses"

Each script prints one line per attempt: `NAME: rc= verdict= failing=<legs>`.

## Ranked findings

### 1. [HIGH] C1 verdict passes on a tree whose entry header says `admission-status: rejected`

Repro (real lint and real embedded checker, no stubs):

    python3 -B "$S"/attacks3.py    # prints R1-dup-status-real: verdict=pass
    HYAKU_SCRATCH="$S/hs" python3 -B reports/round-93/c1_k_admit_counter2.py --tree "$S/trees/R1-dup-status"

Output (receipt `receipts/R1-dup-status-real.txt`, `R9-all-bypasses-real.txt`): every leg
`pass`, `C1_K_HELD_BACKED=10/15`, `C1_VERDICT=pass`. The entry header line is
`admission-status: rejected`; a second `admission-status: admitted` sits in a fenced block.

Cause: `legs["C1_ADMITTED"] = bool(re.search(r"^admission-status: admitted$", text, re.M))`
scans the whole file, not the header. The digest normalises every status line, so a vote on
the candidate bytes stays valid. The real `lint_entry.py` passes the forged entry (`C1_LINT=pass`
in R1 and R9), so nothing in the lint leg catches the duplicate line.

This is the answer to claim check 2a: yes, 10/15 is reached with a rejected entry named in
C08 and the verdict passes. A rejected header alone (no second line) is killed by C1_ADMITTED
(attempt A11), so the bypass is the duplicate line.

Close (frozen file; report, do not edit): match the status on the first status line of the
header only, and reject any file with more than one `admission-status:` line.

### 2. [HIGH] The C1 vote registry is self-attested; the battery's F1 kill is incidental

Repro: `python3 -B "$S"/attacks.py all` → `A3-forged-registry: verdict=pass`.
`A3b-f1-shape-no-artifact: verdict=fail failing=C1_VOTES` (the battery F1 shape).

Forgery: add `FabA`/`FabB` to `.ufo/waves/round-93/w1/swarm-registry.json` (the file is in
the counted tree, and the same wave's members can write it), add votes from those seats with
`artifact_path` pointing at junk bytes in their own dirs. C1_VOTES passes.

The battery's F1 is killed only because its votes have no `artifact_path`/`artifact_sha256`
(`forge_battery.py` F1 builds votes without those keys). Add the two fields and F1's forgery
passes. The claim's "F1 full forgery" class is therefore not killed in general; it is killed
in one shape. Calibration claim: nine classes rejected is true for these nine trees, not for
the classes as named.

Close (frozen; report): authenticate the registry (committed-tree provenance or a pin); the
counter cannot prove seat identity from a file the same wave can write.

### 3. [HIGH] One real seat is counted as several distinct seats; author self-votes and role mismatches pass

Repro: `python3 -B "$S"/attacks2.py` → `A21a-case-dup-seat: pass`, `A21b-space-dup-seat: pass`;
`python3 -B "$S"/attacks3.py` → `R3-case-dup-seat-real: pass`
(`C1_VOTE_SEATS=ReviewerGate,reviewergate`).
`python3 -B "$S"/attacks.py all` → `A28-author-self-vote: pass` (`ScribeEntry`, registry role
`scribe`, votes `reviewer` on its own entry: seats `ReviewerGate,ScribeEntry`);
`A29-role-mismatch: pass` (`ExecOracle`, registry role `executor`, votes `critic`).

Cause: distinctness is `seat not in seen` on exact strings; the vote's `role` is only checked
to be `reviewer|critic` and is never compared with the registry role; the entry author is never
excluded. The r92 finding 3 close asked for a non-author check; claims.md does not state a
non-author requirement for votes, and the counter does not enforce one.

Close (frozen; report): canonicalise seat names (case-fold, strip) and require distinct
canonical seats; require `vote.role == registry[seat].role` and seat != entry author.

### 4. [HIGH] Vote artifact binding is a sha equality, with no content and no path containment

Repro (real tools): `python3 -B "$S"/attacks.py all` → `A1-shared-artifact: pass`,
`A4-empty-artifact: pass`, `A5-registry-as-artifact: pass`;
`python3 -B "$S"/attacks.py all` → `A2-traversal: pass`; `attacks3.py` → `R7-traversal-real: pass`.

- A1: two distinct seats, one shared artifact file and sha.
- A2/R7: `.ufo/waves/round-93/w1/../../../../corpus/SOURCES.md` passes
  `startswith(".ufo/waves/round-93/")` and resolves outside the wave dir.
- A4: zero-byte artifacts for both votes.
- A5: `swarm-registry.json` as the review artifact.

Cause: `art_ok` checks `startswith` (lexical), `is_file`, and sha equality. Nothing checks the
artifact is distinct per seat, is inside the wave dir after resolution, is non-empty, or
mentions the candidate digest.

Close (frozen; report): resolve the path and require containment in the seat's own wave dir;
require one artifact per seat; require non-empty content that names the candidate digest.

### 5. [HIGH] C1_OPENS does not pin the oracle: a forged `oracle_check.py` re-derives the tail

Repro: `python3 -B "$S"/attacks.py all` → `A6-forged-oracle: pass`
(`corpus/fixtures/browser-r77/oracle_check.py` replaced by one line that prints the tail);
`attacks3.py` → `R6-forged-oracle-real: pass` (every other leg honest, real tools).
`A6b-truth-json-touched: pass` (oracle input `truth.json` rewritten, unpinned).

Cause: `check_opens` pins the record and the two fixture HTML/JS files only. The oracle script
and `truth.json` are executed or read without a pin, and the check is a string match on the
last stdout line. The claim says the counter "re-runs the round-77 oracle ... re-hashes ...
both fixture files"; that is only true for the record and the two fixtures.

Close (frozen; report): pin `oracle_check.py` and `truth.json` sha256 in `check_opens`; compare
the oracle's own stdout against an expected full output, not just the last line.

### 6. [MEDIUM] Source citations are checked only in the 15-line header window

Repro: `python3 -B "$S"/attacks.py all` → `A9-body-source: pass`; `attacks3.py` →
`R2-body-source-real: pass`. The entry body (after line 15) cites `S901`, a SOURCES row with
status `rejected`, opened `2026-10-02`, and used-by another file. C1_SOURCES and C1_QUOTES pass.

Cause: `s_ids = ... re.findall(... , "\n".join(head))` with `head = text.splitlines()[:15]`.
`C1_SOURCES` also accepts any self-declared `opened` date equal to `2026-11-05` with no log;
`controls/oracle-opening.log` is not read by any leg. Attempt A8 (header row opened 2026-11-04)
kills, so the date check works for header rows only.

Close (frozen; report): collect S-ids from the whole entry, not the header.

### 7. [MEDIUM] The embedded-output legs are defeated by a whitespace-only output or a mixed fence

Repro: `python3 -B "$S"/attacks2.py` → `A27-ws-output: pass`; `attacks3.py` → `R5-ws-output-real: pass`
(real checker prints `checked_blocks=1 problems=0` for a block whose only output line is spaces).
`A14b-mixed-fence: pass`; `attacks3.py` → `R4-mixed-fence-real: pass` (one honest ``` block
plus a fabricated `~~~` block). A14 (tilde-only, no ``` block) is killed: the real checker
exits 2 (fail-closed), so the `~~~` bypass needs an honest ``` block beside it.

Cause: the counter's `C1_EMBED_NONVACUOUS` counts raw lines (`len(lines) < 2`) and the real
checker's `parse_blocks` ignores whitespace-only lines and `~~~` fences. The r92 finding 6 close
is therefore partial.

Close (frozen; report): count non-blank output lines per block; reject `~~~` fences that
contain a `$ ` line.

### 8. [MEDIUM] C2 leg `C2_ONLY_C08` has no committed control; C2's positive accepts an empty entry

- Kill exists, but only in my attack: `python3 -B "$S"/attacks.py all` → `A15-second-row-c2`
  (`attacks.py` moves C02 to held beside the honest C08):
  `C2_ONLY_C08=fail`, the only failing leg, `C2_VERDICT=fail`. The committed self-test kills only
  `record-sha` and `trailing-cell`; the battery's F5-F9 never move a second row. Leg unexercised
  by any committed control. Answer to claim check 2b: a tree with C08 held and a second row moved
  is rejected (A15). Not reachable in my attempts, but the leg has no committed kill.
- `A16-zero-byte-entry-c2: pass`. `C2_C08_TOKEN` only checks that the cited file exists, so a
  zero-byte entry passes. This is token-level; the C2 claim says "C08 not flagged" and should
  say so (see wording W8).

### 9. [MEDIUM] Q-gate `n/a` reasons are unconstrained

Repro: `python3 -B "$S"/attacks.py all` → `A17-vacuous-na: pass`; `attacks3.py` →
`R8-vacuous-na-real: pass` (one PASS and sixteen `n/a` with reason `-`, both seats).

Cause: `str(notes.get(q, "")).strip()` is non-empty. The claim's "reasoned n/a" is a
non-empty-string test.

Close (frozen; report): require a minimum reason length or a reference to a Q-map row.

### 10. [MEDIUM] The K line is not admission-gated; only the verdict is

- `A11-rejected-k`: `C1_K_HELD_BACKED=10/15` printed; verdict fail via `C1_ADMITTED`.
- `A12-seed-k` (no entry file at all; C08 held citing `knowledge/seed.md`): `C1_K_HELD_BACKED=pass`
  and `C1_K_HELD_BACKED=10/15`; verdict fail via other legs.

Any reader of the K line alone sees 10/15 without an admitted entry. The predicate is the
verdict (correct); the K line should not be quoted as the coverage move.

### 11. [MEDIUM] Real-tools coverage: the positive control stubs lint and the embedded checker

`forge_c1_tree` and the self-test both replace `corpus/lint_entry.py` and
`corpus/check_embedded_outputs.py` with `sys.exit(0)`. Under the real tools, an honest-shaped entry
fails: `attacks.py` / `A18-real-tools` → `C1_LINT=fail`, `C1_EMBEDDED=fail` (the entry lacks the
`## §Q-map` rows Q01-Q17 and an embedded `$` block). `attacks3.py` → `H0-honest-real-c1: pass`
(entry with a Q-map and one oracle block). So a real-tools positive exists only in this scratch
fixture; `POS_C1V2` never runs real lint. The claim phrase "honest-shaped admission fixture
passes every leg" is true only with the stubs. See W7.

### 12. [LOW, process] The wave registry is untracked at lane HEAD

`git cat-file -e 02050cb…:.ufo/waves/round-93/w1/swarm-registry.json` → absent; `git status` shows
`?? .ufo/waves/round-93/`. `C1 --rev` archives `.ufo/waves/round-93`, so the honest state cannot
pass until the L1 commits the wave bytes including the registry. This is a landing gate, not a
counter defect. It also makes F2 worse: the registry is only as trustworthy as its write scope
(sentinel audit).

## Claim checks requested in the attack brief

- (a) 10/15 without an admitted entry: **yes, verdict pass** (R9, R1, A10: header rejected,
  duplicate `admission-status: admitted` line). The K leg alone is 10 with no entry (A12).
- (b) POS passes while a second row moves: **not reachable in my attempts** (A15 killed by
  `C2_ONLY_C08`), but that leg has no committed control (finding 8).
- (c) Battery F3 and blanket refusal: deleting the registry does **not** kill `POS_C1V2`. The
  self-test writes its own registry into its own temp root and never reads the lane registry;
  `battery --stage full` printed `POS_C1V2=pass` in my run. On the honest tree,
  registry deletion (A19) kills C1 only (`C1_VOTES=fail`) and leaves C2 passing (`A19-no-registry-c2:
  pass`). C2 has no blanket refusal; the C1 refusal is the frozen intent.

## Attempts: counter kills and passes

Kills (counter returned fail): A3b (F1 shape, no artifact), A7 (stale fixture sha in opens with a
correct record sha), A8 (S-row opened one day off), A11 (rejected header, K printed 10), A12 (no
entry), A13 (lowercase seats against registry case), A14 (tilde-only fence, real checker fail-closed),
A15 (second row moved, `C2_ONLY_C08`), A19 (registry absent, C1 only), A23 (external header row, no
receipt, `C1_QUOTES`), and the real-tools A18 (thin entry, `C1_LINT`/`C1_EMBEDDED`).

Passes (not caught; each explained above): A1, A2, A3, A4, A5, A6, A6b, A9, A10, A16 (C2), A17,
A21a, A21b, A27, A28, A29, A14b, A20 (benign control: an extra lowercase key with honest votes),
H0 (honest real-tools control: pass, as intended), R1-R9 (R9 with C2: pass).

Total attempts: 40+ runs across A0-A29, A14b, A21a/b, H0, R1-R9 (scripts in `attacks/`).

## Wording (r92 finding 8 class): claims.md states more than the counters measure

- W1. "backed by ONE admitted entry": C1_ADMITTED reads any line in the file (finding 1).
- W2. "and any external row the entry cites, fetched this round with `audit_source_quotes.py`-format receipts":
  the quote leg reads header rows only (finding 6).
- W3. "the counter re-runs the round-77 oracle ... re-hashes the record and both fixture files": the oracle
  script and `truth.json` are unpinned (finding 5).
- W4. "C1_VOTES (≥2 distinct registry seats ... reasoned n/a, ≥1 PASS ...)": distinct is exact-string,
  reasoned is non-empty, registry membership is self-attested (findings 2, 3, 9).
- W5. Kill rule "votes are not bound to committed wave artifacts": binding is sha equality only (finding 4).
- W6. "Score 6.0 → 6.7" on "K_HELD_BACKED=10/15": the K leg passes with no entry (finding 10).
- W7. "honest-shaped admission fixture passes every leg" (POS_C1V2): true only with lint and embedded stubbed
  (finding 11).
- W8. "C2 ... C08 not flagged" / "moves frontier -> uncovered" class: C2 checks the token shape and the file
  existence, not the content (finding 8).
- W9. "the routed successor counters kill the routed forgery classes" / "V2_KILLS=9/9": F1 and F2 are killed in one
  shape each (finding 2, finding 9 F2 all-n/a); the classes as named are not all rejected.
- W10. "the honest state still passes — no blanket refusal": demonstrated only on fixtures (H0, A0), not on the
  landed tree, which does not exist yet (scribe draft not landed at this writing).
- W11. "Q10 scope": no counter enforces entry scope; it is reviewer-judged only.
- W12. "round-77 record ... opened 2026-11-05 by re-running the oracle — round-start opening output committed as
  controls/oracle-opening.log": no leg reads `controls/oracle-opening.log`; the opened date is self-declared
  (finding 6).

## Controls run in scratch (frozen files, read-only)

- `c1_k_admit_counter2.py --self-test` → `SELFTEST_C1V2=pass kills=registry,artifact-sha,all-na,na-reason`.
- `c2_legend_counter2.py --self-test` → `SELFTEST_C2V2=pass kills=record-sha,trailing-cell`.
- `forge_battery.py --stage full` → `V1_REACH_C2=5/5; V2_KILLS=9/9; POS_C1V2=pass; POS_C2V2=pass; DO_NOTHING_C2=fail; BATTERY_VERDICT=pass`.
- `forge_battery.py --stage v1-only` → `V1_REACH_C2=5/5; BATTERY_VERDICT=pass`.

The battery is green in my environment, as frozen. Its nine classes are real; the findings above
are about what the nine classes do not cover.
