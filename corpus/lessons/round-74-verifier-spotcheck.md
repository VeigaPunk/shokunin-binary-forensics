# Round 74 verifier spot-check — revenger (hyaku)

author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

Closed 2026-11-01T03:49Z against lane tip `bbbce158035f8295344a3af5eea4b15e850cb12e`
(branch `main`, local == `ls-remote origin`), base `85db6abefae7b706cf5583ab24eefbcbd28a4f01`.
I did not author the round; every command below was run by me at closure time. Per the host
note, only index-free git was used; nothing in the lane repo or fleet root was mutated.

## 1. Step-1 conformance — PASS

| check | command | result |
|---|---|---|
| report committed by lane identity | `git -C <fleet> log --format='%an %H' -1 -- .ufo/reports/round-74/revenger.md` | `revenger-shokunin 44d57e2c0bd87256c451afd46b9575f8d2246ec6` |
| `SHONEN` heading | read of committed report | `## SHONEN` at line 48, four `[~]` lines with evidence pointers |
| cited hashes exist + ancestry | `git rev-parse` + `git merge-base --is-ancestor <h> refs/heads/main` | `c9f490cd6b06…`, `704be4dcec7a…`, `e302492bcc82…`, `bbbce158035f…` all ok |
| branch tip pushed | `git ls-remote origin refs/heads/main` vs `git rev-parse refs/heads/main` | both `bbbce158035f8295344a3af5eea4b15e850cb12e` |
| round work in range | `git log 85db6ab..bbbce15` | exactly the 4 cited commits, all authored `revenger-shokunin` (2026-11-01T03:09Z–03:21Z, inside the dispatch window) |
| dispatch/complete digest | `.ufo/watchdog.log` lines 15/34 | matches the contract digest verbatim (`launch revenger round=74 base=85db6abefae7` 18:58:01-07:00; `complete … head=bbbce158035f pushed=True` 20:24:49-07:00) |
| LOG.md round entry | `git diff-tree -r -p 85db6ab bbbce15 -- LOG.md` | single appended round-74 entry, append-only |
| SHONEN.md untouched, no new `[x]` | `git diff-tree 85db6ab bbbce15 -- SHONEN.md` | empty (file last touched r70); all marks `[~]` |

## 2. The mid-round defect and its repair — repair VERIFIED byte-exact

The self-caught defect is real: `c9f490c` (treecommit called with directory arguments, whose
paths are files) **deleted** the inherited freeze's `reports/round-74/claims.md`,
`reports/round-74/measure-before.log`, `reports/round-74/measure.py` and landed **none** of the
quote-audit receipts (`git diff-tree -r --name-status 85db6ab c9f490c`: exactly 3 `D` under
`reports/round-74/`). The repair `704be4d` re-listed all 111 files explicitly.

Byte-identity of the restored freeze, re-verified by me (`git ls-tree` blob hashes):

| file | base `85db6ab` | `c9f490c` | `704be4d` | `bbbce15` |
|---|---|---|---|---|
| `reports/round-74/claims.md` | `6fd54b03` | ABSENT | `6fd54b03` | `6fd54b03` |
| `reports/round-74/measure-before.log` | `eff51d4d` | ABSENT | `eff51d4d` | `eff51d4d` |
| `reports/round-74/measure.py` | `50f8aae0` | ABSENT | `50f8aae0` | `50f8aae0` |
| `corpus/audit_source_quotes.py` | `6a552c76` | `6a552c76` | `6a552c76` | `6a552c76` (never deleted) |
| `reports/round-73/measure.py` | `b354acbd` | `b354acbd` | `b354acbd` | `b354acbd` (never deleted) |

sha256 of the two pinned instruments at `bbbce15` re-derive the freeze pins exactly:
`72c6938a7e27631f…dcc58743f` (`corpus/audit_source_quotes.py`) and
`ff2e52bdd6705bfb…5296e4ea6` (`reports/round-74/measure.py`).
Repair contents counted by me: 51 `*.receipt.json` + 51 `raw/*.body` + 3 origs
(`S081.orig.pdf`, `S379.orig`, `S381.orig`) + 3 restored freeze files + 3 province
artifacts = 111, matching the report. Net base→final tree delta: 113 `A`, 6 `M`, **0 `D`** —
nothing else was lost. Nit: `measure.py` came back mode `100644` vs `100755` at base (bytes
identical; the instrument is invoked `python -B …`, so no operational impact).

## 3. Claim re-checks

### C1 — coverage, new bounded criterion P (province surface accuracy) — RE-MEASURED, verifies

I rebuilt both states in a scratch fixture from committed bytes (base `PROVINCE.md` and final
`PROVINCE.md`, the committed probe blob `da1e3664` — unchanged `704be4d`→`bbbce15` — plus the
lane repo's `.git` and `corpus/training/bounty-triage/MODULE.md` so the two worktree surfaces
behave identically) and ran `bash province_probe.sh <fixture>` myself:

- before: `PROVINCE_SURFACES_RESOLVED=4/11 UNRECORDED_ABSENT=7 P_SCORE=3.6`, exit **1**
- after: `PROVINCE_SURFACES_RESOLVED=11/11 UNRECORDED_ABSENT=0 P_SCORE=10.0`, exit **0**

Both runs match the committed `province-before.log` / `province-after.log` line-for-line.
`PROVINCE.md` diff is exactly the described correction: dated `[absent on this host,
2026-10-31 …]` records for REA skill dir / ghidra / ida / jadx / binwalk-unblob / pwntools /
`~/Projects/gamez/research`, and the write-scope rename to `fleet/shokunin-binary-forensics`.
Boundary honesty holds: K `8/15` unchanged (`c10-disposition.log`), README C10 row still
`partial`, no coverage-map row moved, no admission claimed.

### C2 — calibration, inherited frozen QA criterion (quote fidelity) — EVIDENCE-VERIFIED + INDEPENDENTLY RE-MEASURED, verifies

Committed evidence verified (I did not execute the sibling's counter, per contract):
`reports/round-74/measure-after.log` names the measured revision `704be4d`, pins the frozen
counter sha `ff2e52bd…4ea6` (= the freeze pin, re-derived by me), and records
`QA_VERIFIED=42/42 QA_MANUAL_VERIFIED=9/9 QA_VERIFIED_TOTAL=51/51 QA_UNRESOLVED=0/51
QA_NEGCTRL=pass QA_TARGET=yes`, counter exit 0. The frozen `measure-before.log` (freeze
inherited, base `c7008577`) records `0/51, QA_NEGCTRL=n/a, QA_TARGET=no`; I confirmed the
before state is mechanically entailed: `c7008577` (ancestor of main) carries **no**
`.ufo/waves/round-74/quote-audit/` tree, 428 registry rows, S427/S428 present. The tip
re-confirmation claim is entailed too: counter inputs (`corpus/SOURCES.md`,
`.ufo/waves/round-74/`) are byte-identical `704be4d`→`bbbce15`.

Independent re-measurement with my own script (not the lane's counter), over
`git archive bbbce15 corpus/SOURCES.md .ufo/waves/round-74`:

- **All 51 receipts** (`51 × S*.receipt.json` + `raw/*.body`): sha256(body) == `fetch_sha256`,
  byte length == `length`, whitespace-normalized quote present in body AND equal to
  `body[span.start:span.end]` → **51 ok, 0 bad**.
- Receipt census: all 51 `verdict: verified`, all `schema: revenger-quote-audit-v1`, all 51
  carry the disclosed `seat: revenger-r74-L1 (no seat surface on this host…)`.
- Negative control: `Each repo is read and security-graded` (S071 historical drift quote) is
  **absent** from `raw/S427.body` — PASS, independently.
- Registry: contract census commands over base/final blobs → **428 → 442**; S429–S442 all open
  `supersedes S0NN …`, `mined`, `used-by: corpus/lessons/round-74.md`; supersedes chains resolve
  (`S071→S427`, `S082→S428`, my own terminal resolution); 0 duplicate ids, 0 malformed rows
  (NF check), 0 enum violations, no tier inflation.
- `SOURCES.md` diff: exactly 14 added rows + 3 modified rows (S062/S068/S094) — "none else
  changed" is accurate. The three flips change only `teaches` + `status`
  (`mined`→`rejected`), each with a located-quote reason naming its successor, logged old→new
  in the lesson (see defect note 3).

Live re-opens (3, all HTTP 200, **byte-identical** to the committed bodies): radare2 README at
`6ac96f5` (S431), OWASP mastg README at `41c6b74` (S438), repositum.tuwien.at record
`20.500.12708/150118` (S343). The two misquote findings reproduce exactly: in the pinned
radare2 README, "command-line hexadecimal editor" belongs to line 16 ("The **radare** project
started as a simple command-line hexadecimal editor focused on forensics.") — the quoted r2
sentence (line 17) says "full-featured low-level command-line tool"; the pinned mastg README
bolds the title and has no leading "The".

### Holds / no harmed axis — VERIFIED

- `SCORECARD.md` diff is append-only (one new round-74 section; no prior row edited).
- My own sweep of protected corpus paths base→final (README map, live, fixtures, prior admitted
  knowledge, r70–r73 lessons): only `corpus/knowledge/2026-10-29-rea-evidence-ledger-discipline.md`
  changed, and only the line `admission-status: candidate` → `admission-status: rejected` — the
  frozen r73 kill rule's prescribed disposition. `reports/round-73/*` byte-untouched.
- Do-nothing control for the C10 disposition, re-derived: `.ufo/waves/round-73/votes/` is empty
  in the final tree (0 vote files), README C10 = `partial`, candidate `rejected`, K `8/15`
  per the committed `c10-disposition.log` (r73 counter evidence-verified, not executed).
- No exploratory claim was declared (report addendum), so no `unprovable-but-better`
  judgment is owed; both claims verify as measured/evidence.

## 4. Discernment spot-check (outside, non-author) — 3/3 AGREE

| item | decision (lane) | re-opened source | verifier verdict | reason |
|---|---|---|---|---|
| S431 (supersedes S062) | ADMIT correction | live `raw.githubusercontent.com/radareorg/radare2/6ac96f5…/README.md` → HTTP 200, byte-identical to `raw/S431.body` | **agree** | corrected 20-word quote verbatim at the recorded span; the old "hexadecimal editor" attribution is a real misquote (precedes the quoted sentence) |
| S438 (supersedes S094) + S094 flip | ADMIT correction + REJECT | live `raw.githubusercontent.com/OWASP/mastg/41c6b74…/README.md` → HTTP 200, byte-identical to `raw/S438.body` | **agree** | old leading-"The" quote absent from pinned bytes; corrected sentence with bolded title verbatim; reject reason is quote-grounded and names the successor |
| S343 re-open | existing row held, no correction | live `repositum.tuwien.at/handle/20.500.12708/150118` → HTTP 200, byte-identical to `raw/S343.body` | **agree** | the row's quote verifies verbatim at its registered location; no correction needed |

Newly-written `SOURCES.md` rows re-opened: S431 and S438 (table above). Their `## Gate` quotes
are ≤25 words (20 and 12) and verbatim in the pinned bytes.

Census: the literal contract command `sources-census.sh validate --root <fleet> revenger`
exits **2** (`revenger  missing …/shokunin-clone/shokunin/revenger-shokunin/corpus/SOURCES.md`)
— the old `<root>/<lane>-shokunin/` layout this host does not have; the lane disclosed exactly
this. The host-adapted explicit-lane-dir form (sanctioned by the script's own selftest,
`validate --root <fleet> <lane-dir>`) exits **0**, `ok`, 31 W (10 W04, 21 W01), 0 E — matching
the committed `census-after.log` line-for-line. The reported round-start census (28 W = 8 W04 +
20 W01) is entailed: end census minus the three new-row warnings (+W04 S429, +W04 S430,
+W01 S437).

## 5. Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| coverage | **improved** | C1 criterion P re-measured 3.6→10.0 (probe + dated-absent records); instrument-level only, K honestly unchanged |
| calibration | **improved** | C2 QA criterion 0/51→51/51, re-derived independently at byte level with negative control |
| depth | unchanged | no claim; SKILL bytes untouched (`git diff 85db6ab..bbbce15 -- SKILL.md` empty) |
| operability | unchanged | no claim; existing gates/fixtures untouched |
| freshness | unchanged | no claim; instruments exercised on new host without byte change (sha pins re-derived) |
| adjacency | unchanged | no claim; PROVINCE refuses-clause intact; no sibling scope absorbed |

Trends: **expansion unchanged** (no admitted knowledge entry; K 8/15; registry growth is not
admission), **quality unchanged** (no admitted entry re-checked; the 14 corrections are
registry-class per the r73 precedent), **discernment improved** (this closure's outside
spot-check agrees with the gate on admits and rejects — LEARNING.md's improved condition; the
lane itself honestly recorded `unchanged` pending this check, and its self-caught defects are
logged, not credited).

## 6. Defects and routed items (all status-neutral)

1. **[verified, repaired] Mid-round landing defect**: `c9f490c` deleted three freeze files and
   landed none of the receipts; repair `704be4d` restored byte-identical content (see §2).
   Residual nit: `measure.py` mode `100755`→`100644` (bytes identical, no operational impact).
2. **Census literal command is host-broken** (exits 2 expecting `<root>/revenger-shokunin/`):
   routed to the operator — the census tool's default layout predates this host's
   `fleet/shokunin-binary-forensics` lane dir; the explicit-dir form works and is selftest-sanctioned.
3. **In-place `teaches` edits accompany the three status flips** (S062/S068/S094): SOURCES
   contract v1 rule 2 names only `status`/`recheck`/`used-by` as in-place-mutable, but the same
   contract's rejected-row shape (`REJECTED: <reason>; flip: …`) forces the reason into
   `teaches` — an internal contract tension to resolve contract-side; the changes were logged
   old→new in the lesson, and all quote corrections themselves landed only as superseding rows.
4. **Self-test tally is report-pasted only**: the counter/auditor self-test
   (`self-test: ok (7/7 legs)`, exit 0) has no dedicated committed receipt file; the tally is
   hermetic and independently re-runnable, and the counter's frozen verdict was re-derived
   independently here, so the claim stands.
5. **L1-authored receipts** (no seat surface on this host) disclosed on all 51 receipts and in
   the report/lesson; MISSION's ≥8-L2 floor unmet-and-disclosed with L0 filed
   (`revenger | round-74`, `.ufo/l0-questions.md` line 233). Routed: K moves (C05/C10/C15)
   stay blocked until the operator rules on the dispatch surface — the SCORECARD `planned`
   section correctly does not re-declare them.
6. **S442's 27,645,192-byte source PDF is not committed** (URL, HTTP 200, length and metadata in
   the receipt; re-derivation by public refetch + the named `pdftotext` command) — disclosed in
   the lesson; noted as an evidence-weight caveat, not a defect of the verdict.
7. **Operator note**: SHONEN.md's four boxes are `[~]` and remain non-promotable by a
   non-author as-is; the standing r69-V7 routing (outside re-confirmation of current SKILL.md
   bytes) is still owed, and the lane's report says so.
