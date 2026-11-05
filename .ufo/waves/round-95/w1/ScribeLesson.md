# ScribeLesson — round 95, wave revenger-r95-w1, attempt 1

Seat: `ScribeLesson` (registry role `scribe`, axis `coverage`). Lane:
`/home/vgpnk/Projects/shokunin/revenger-shokunin` at freeze
`6e0bf15fed58f357b7fa0c881371ac7616a116f7`. Date: 2026-11-05. **Read-only seat**: no lane file
was written by this seat, no git/jj command was run against the lane, no network beyond the URLs
the task names, no host mutation, no tool install, no subagent dispatch, no `agent://all`.

## What I delivered (inside my wave dir only; the L1 finalises the lane file from it)

| artifact | path (relative to the lane root) |
|---|---|
| round-95 lesson draft | `.ufo/waves/round-95/w1/ScribeLesson/round-95-lesson-draft.md` |
| census receipt (settled, seven commands) | `.ufo/waves/round-95/w1/ScribeLesson/census-seven-settled.log` |
| assimilation collision-check id lists | `.ufo/waves/round-95/w1/ScribeLesson/{reg-ids,staged-ids,collisions}` |
| battery3 reaped-scratch reproduction copy | `.ufo/waves/round-95/w1/ScribeLesson/battery3-repro-SCRATCH-redirected.py` |
| this report | `.ufo/waves/round-95/w1/ScribeLesson.md` |

The draft carries the five sections the task named: `## Gate` (three candidates considered — the
admission candidate with what the decision rests on, and two rejects with reasons and flips, plus
the Q17 note for the Q-map), `## Mistakes` (seven rows: class · evidence pointer · captured-by ·
fix), `## Frontier and census` (the exact census commands and where the before/after logs live),
`## Assimilation` (the frozen collision-check command and the expected none), and `## considerthese`
(proposal 1 adopted, cited with file + date, with the controls as its evidence).

## Behavior

### Gate — what the admission decision rests on, as re-measured by this seat

- **Candidate digest** `476edc36d89ffdcf8cdafabc9cac4fc5dd49f68efe307d05c7db79a919479fb9`,
  recomputed from the lane root with the wave recipe and identical to the raw file sha256 — the
  entry's only `admission-status:` line (line 21, inside the 30-line header window) already reads
  `candidate`, so the normaliser is the identity transform today. `git show 6e0bf15:…` gives the
  same blob sha256 as the working-tree file, so the working tree equals the freeze bytes.
- **Flip-invariance, re-measured on this round's bytes.** Normalising the status line yields the
  same digest whether it reads `candidate` or `admitted` (`476edc36…` both ways) while the raw
  sha256 differs (`c70259fc…`). The L1's single admission flip therefore does **not** re-open the
  digest — **provided the flip is the only byte changed**; any other entry byte re-opens it and
  forces a full vote re-bind (r93 M1). This is the r94 scribe's finding re-confirmed.
- **The two source rows opened this round re-hash and re-span exactly.** S500 body 17010 B,
  sha256 `69fe2245…`, quote *"Source authority vocabulary owned by Evidence and reused by its
  consumers."* at span `[3149,3223)`; S501 body 18784 B, sha256 `f7add6973…`, quote *"Record
  evidence idempotently; conflicting content is rejected."* at span `[2136,2198)`. I verified
  `body[span] == quote` for both, the body sha256 against `fetch_sha256`, and the length against
  `length`. `corpus/audit_source_quotes.py verify --sid S500 --sid S501` on the landing-tree copy
  → `SUMMARY rows=2 verified=2 unreachable=0 unresolved=0`, exit 0.
- **The receipts really are frozen pre-data.** `git ls-tree -r 6e0bf15` lists both receipt JSONs,
  both raw bodies and the fetch log — committed at the freeze commit, before any seat ran.
- **The frozen counter on a copy of the landing tree.** With the C10 row flipped, S500/S501
  appended and the entry status-flipped, every leg passes except the two that need the landing's
  own artefacts: `C1_VOTES=fail` (the vote files are not yet in `reports/round-95/votes/`) and
  `C1_ADMITTED=fail` (the entry still reads `candidate` in the copy). Measured output:
  `C1_K_HELD_BACKED=12/15`, `C1_ROWS_TOTAL/C1_C10_HELD/C1_C10_CITES/C1_ONLY_C10/C1_TRIO/
  C1_REGISTRY/C1_RECEIPTS/C1_PYCACHE/C1_LINT/C1_EMBEDDED/C1_EMBED_NONVACUOUS/C1_SIDS/C1_SOURCES/
  C1_QUOTES = pass`, `C1_ONLY_C10_DIFFS=none`, `C1_REGISTRY_WHY=ok`, `C1_RECEIPTS_WHY=ok`,
  `C1_SOURCES_WHY=ok`, `C1_QUOTES_WHY=ok`. **The counter was run against a scratch copy; I did
  not run the predicate as a verdict.**
- **Votes.** Two filed in the wave at drafting time, both binding the digest above:
  `ReviewerGate` (reviewer) PASS 8 / n-a 9, `ReviewerBlind` (reviewer) PASS 7 / n-a 10;
  `CriticR95` (critic) had not filed. The frozen `C1_VOTES` leg needs ≥2 accepted votes; the
  third is the lane's to land. I re-hashed `ReviewerBlind/derivation.md` and it matches the
  value its vote declares (`62e125f3…`), and both artifacts name their seat and the digest.

### Mistakes

Seven rows in the draft. The M1-class candidate the task named is confirmed and reproduced:
the frozen `reports/round-94/forge_battery3.py --stage full` mkdtemps under its own `SCRATCH`
constant without creating it. I reproduced the `FileNotFoundError` from `tempfile.mkdtemp` on a
lane-shaped copy of the frozen file with the constant pointed at a missing root (copy kept in my
wave dir as the receipt). It is closed by provisioning around the frozen bytes, not by editing
them, and the counter-scratch rule is routed for a later freeze.

The other six rows are this round's own artifacts: the helper-only V03 registry delta that the
self-test caught before the freeze; the red-v3 fixture shape mismatch (a body-editing delta moves
the digest the fixture's votes bind); the v3 registry mutant that survives v3 and dies on v4; the
`cb5c26f`-vs-`6e0bf15` revision mislabel in the SKILL.md registry note; the S500/S501 rows written
without a closing pipe (census `E01 fields=10`); and the C10 coverage cell naming extra
`knowledge/*.md` paths against the exact-one-file `C1_C10_CITES` leg.

### Frontier, census, assimilation, considerthese

- **Census commands and log locations** are in the draft, verbatim from `SKILL.md` §6.2 plus the
  fleet driver. Before: `reports/round-95/controls/census-round-start.log` (committed at freeze,
  exit 0, 0 E, 21 W01 + 13 W04 — and it carries **no row count**, so the claims' "rows 499" is the
  freeze-registry size the seven commands derive separately). After: `reports/round-95/controls/
  census-round-end.log`, **not yet written** — the L1 writes it at landing.
- **Measured on the landing tree** (my receipt `census-seven-settled.log`, run from the lane root
  at 2026-11-05T14:51:27-03:00): rows **499 → 501**; tier `A=450 B=21 C=28` → `A=452 B=21 C=28`;
  status `mined=463 queued=16 rejected=20` → `mined=465 queued=16 rejected=20`; malformed 0;
  duplicate ids none; enum/tier-inflation none; mined rows with a missing `used-by` path none.
  Rows touched: 15 (S002, S096–S109), `used-by` cell only — no `status`, `tier`, `opened` or
  `recheck` changed; verified cell-by-cell against the freeze blob.
- **Assimilation: none.** I re-ran the frozen §10 collision check read-only: `reg-ids` 501,
  `staged-ids` 155, `collisions` 155 — and `collisions` is byte-identical to `staged-ids`
  (sha256 `18ff1510…`), so every staged id already exists in the registry. The `ExecCensus` seat
  measured the same three files independently with identical counts and identical sha256. L0
  `revenger | round-91` stays open.
- **considerthese: proposal 1 of `considerthese/2026-11-05.md` is adopted**, cited with file and
  date, with `reports/round-95/controls/` (five files, all committed at the freeze) as its receipt
  set and this round's M2 as the in-round instance of it. Proposal 2 was re-measured by the
  connector seat over r94–r95 (12 of 12 = 100 % headline; 8 of 12 = 67 % sibling reading) and is
  **not adopted** — a criterion needs its own frozen predicate. The draft also records the
  adoption's honest coverage: no-work base PRESENT, id-edited copy PARTIAL (12 of 22 deltas have
  only the aggregate `pass` line), stub-control ABSENT, fitted-table ABSENT, non-independent-vote
  copy ABSENT (the disclosed residual).

## Touched surfaces

**Written (my wave dir only):**

- `.ufo/waves/round-95/w1/ScribeLesson/round-95-lesson-draft.md` (new)
- `.ufo/waves/round-95/w1/ScribeLesson/census-seven-settled.log` (new)
- `.ufo/waves/round-95/w1/ScribeLesson/{reg-ids,staged-ids,collisions}` (new)
- `.ufo/waves/round-95/w1/ScribeLesson/battery3-repro-SCRATCH-redirected.py` (new)
- `.ufo/waves/round-95/w1/ScribeLesson.md` (this report, new)

Scratch `/fast/scratch/hyaku/revenger-r95/ScribeLesson/` — created, used, and **deleted before this
yield** (receipts copied into the wave dir first). Every Python invocation used `python3 -B`.

**Not touched:** any lane file (`corpus/`, `reports/`, `SKILL.md`, `README.md`, `SCORECARD.md`,
`LOG.md`, `PROVINCE.md`, `QUALITY.md`, `claims.md`), `.ufo/state`, `.ufo/watchdog.log`, the fleet
repo, sibling lanes, `/home/vgpnk/Projects/shokuknow` (read once, read-only), `~/.local/bin` or
any PATH directory. No git/jj write command was run anywhere. No sudo, no sysctl, no pacman, no
tool install, no network.

**Note on the working tree.** When I started, the lane already carried the L1's in-flight
integration edits (`corpus/README.md`, `corpus/SOURCES.md`, `corpus/lessons/round-94.md`,
`corpus/lessons/round-95.md`, `SKILL.md` modified/untracked). I did not write them and did not
revert them; the sentinel's audit reaches the same conclusion ("the most likely writer is the L1
integrator"). My scratch tree at
`/fast/scratch/hyaku/revenger-r95/ScribeLesson/tree/` was a **byte copy of the lane taken at
14:38:11** (`cp -a`, preserving the lane's mtimes; the copy's ctime is the copy time) — it is the
sentinel's "ScribeLesson scratch tree", and the lane bytes matching it is a copy artifact, not
evidence that this seat wrote the lane.

## Out of scope (deliberately not done)

- **Landing.** The L1 owns `corpus/README.md`, `corpus/SOURCES.md`, `corpus/lessons/round-95.md`,
  the entry's admission-status flip, `reports/round-95/votes/`, `reports/round-95/controls/
  census-round-end.log`, `SCORECARD.md` and `LOG.md`. I touched none of them.
- **Verifying the claims.** I exercised the frozen instruments against copies; I did not run
  either claim's predicate as a verdict and I did not edit any frozen byte.
- **The residual routes** in the draft (pycache surface list, byte-exact digest binding, the
  atlas's stale "C10 candidate" pointer). Each is routed, not fixed — two of them are frozen-byte
  changes that need the next successor freeze.

## Findings for the canonical judge

1. **The `C1_ADMITTED` leg and the digest normaliser use DIFFERENT anchors — a whitespace alias
   exists on the vote binding.** `STATUS_ANY = re.compile(r"(?i)\s*admission-status\s*:")`
   (counted case-insensitively over the whole file) versus the digest's
   `re.sub(r"(?im)^\s*admission-status\s*:.*$", "admission-status: candidate", text)`. Measured on
   a file whose status line is `  admission-status: admitted` (two-space indent)
   and one whose status line is column-0 `admission-status: admitted` are **different bytes**
   (raw sha256 `3ac552a364c00db0d4381ffc37b7e490a13fa748ac03b2408f1a5a29434b3d6a` for the
   indented variant vs `c70259fc5da3435c0817bf1acb605844df65e0d6d8d5c4179eee7512a9767bba` for the
   column-0 one) but produce the **same** vote digest `476edc36…`, and the frozen `C1_ADMITTED`
   leg accepts the indented form (it strips and
   lowercases the matched line). A second status line anywhere in the file is still caught —
   I verified a body-line `admission-status: rejected` makes `C1_ADMITTED=fail` — so this is a
   narrow whitespace alias, **not** a duplicate-status hole. **The digest is therefore not a
   byte-identity witness**, and the lesson's Gate should say so rather than presenting the binding
   as byte-exact. Route: pair the digest with a raw-bytes sha256 in the next successor freeze.
2. **`C1_PYCACHE` covers three of the lane's Python surfaces, and the one place it does not cover
   currently holds a `.pyc`.** `check_pycache` scans `corpus`, `reports/round-95` and
   `.ufo/waves/round-95` only. `reports/round-94/__pycache__/c1_k_admit_counter3.cpython-314.pyc`
   (46897 B, mtime 2026-11-05 14:23:14 — before any seat spawned) is there now. I reproduced the
   mechanism exactly: importing the frozen counter by path with
   `importlib.util.spec_from_file_location` + `exec_module` **without `-B`** writes
   `reports/round-94/__pycache__`; **with `-B`** it writes nothing. The frozen r93/r94 instrument
   dirs are the two surfaces a successor counter is most likely to import, and they are the two the
   leg never checks — so the leg is green on a dirty dir. The residue is gitignored (tracked bytes
   unaffected) and the L1 should delete it before landing. Route: extend the leg's surface list.
3. **The round-start census log does not carry the row count the claims attribute to it.**
   `reports/round-95/claims.md` §Frontier step reads *"Census round start (pre-freeze): exit 0,
   rows 499 (`controls/census-round-start.log`)"*; the committed log holds the driver's warning
   lines, the `ok` line and `rc=0`, and `grep -c 'rows'` over it is **0**. The number 499 is
   correct — it is the freeze commit's registry size, which the seven-command run derives
   (`git show 6e0bf15:corpus/SOURCES.md | grep -cE …` → 499) — but the cited log does not print
   it. This is the r94 M7 class again (a census figure attributed to a log that does not print
   it). The connector seat reached the same reading independently. The lesson's Frontier section
   therefore cites the seven-command measurement for the row count and the driver log only for
   the exit code and warnings.
4. **`C1_REGISTRY` and the other routed closes are real legs now — the r94 M6 wording overreach
   did not recur.** I diffed the leg names: the counter defines 17 `legs[...]` entries and every
   one of them is named in `claims.md`; the only claims-side token with no leg is `C1_OPENS`, and
   the claims text says explicitly *"There is NO `C1_OPENS` leg"* — a negative statement, not an
   overreach. `C1_REGISTRY` exists as its own leg (counter line 470), so the r94 lesson M6 close
   holds.
5. **The C10 flip is one byte, and the C10 cell had to be trimmed to make the leg pass — both
   constraints are now visible.** `C1_C10_CITES` compares the cell's parsed knowledge-file set for
   **equality** with `[knowledge/round-95-evidence-ledger-discipline.md]`, so the pre-existing
   `knowledge/seed.md` pointer and the superseded 2026-10-29 pointer had to leave that cell.
   `corpus/knowledge/seed.md` still declares `coverage-map: C02, C10, C12, C14` and still exists
   as the pre-contract reminder; the admitted entry keeps that pointer in its own Limitations
   section, which is where the reader finds it. The L1 should not "fix" the seed.md header —
   the frozen leg forbids the alternative.
6. **One stale cross-candidate pointer remains, and it is deliberately not fixed here.**
   `corpus/knowledge/round-73-re-resource-atlas.md:434` still calls the 2026-10-29 file the *C10
   candidate*; after this admission that description is out of date. The file is
   `admission-status: candidate` (not admitted) and the corrections rule forbids in-place
   rewrites of filed bytes, so the fix belongs in an appended dated correction at the round that
   admits the atlas. The frozen Q17 sweep is green over the landing tree
   (`reports/round-90/source_path_check.py --root .` → `SOURCE_PATH_DEAD=0`,
   `SOURCE_PATH_MALFORMED=0`, `SOURCE_PATH_EXCUSED=1` (S481 by S486), exit 0), so nothing is a dead
   path.
7. **The M6-class census defect and the "transient" reading disagree — the evidence favours the
   defect.** The `ExecCensus` seat attributed its rc-1 census run (`E01 S500 fields=10`,
   `E01 S501 fields=10`) to a concurrent writer. The settled evidence is that the rows were
   written **without a trailing pipe** — my own malformed-row awk counted 2 rows at NF=12 (i.e.
   10 fields) at 14:36:36, and 0 at 14:40 after the fix. Either way the receipt a census claim
   cites must be the settled run; the red run is kept as the red-before. The L1's M6 row records
   the defect; the lesson should keep both facts.
8. **The r94 lesson's own C-a/C-b/C-d routed defects are discharged, one of them visibly.**
   `corpus/lessons/round-94.md` carries the appended `C-r95-1` correction (the S499 word count:
   13 → 11; the quote itself is verbatim) and the r94 `## Gate` still records **no** rejected
   candidate — so the r95 Gate's two rejects are the discharge of C-a, and the r94 Gate's absence
   of a reject stays as filed.

## Artifact paths

- `.ufo/waves/round-95/w1/ScribeLesson/round-95-lesson-draft.md` — the lesson draft
- `.ufo/waves/round-95/w1/ScribeLesson/census-seven-settled.log` — seven-census receipt (settled)
- `.ufo/waves/round-95/w1/ScribeLesson/reg-ids` / `staged-ids` / `collisions` — collision-check ids
- `.ufo/waves/round-95/w1/ScribeLesson/battery3-repro-SCRATCH-redirected.py` — M1 reproduction copy
- `.ufo/waves/round-95/w1/ScribeLesson.md` — this report

Scratch `/fast/scratch/hyaku/revenger-r95/ScribeLesson` was removed before this yield.
