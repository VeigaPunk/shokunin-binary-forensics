author: hyaku closure (non-author integrator, @m_opus)
reviewer: CloseMori22, fresh non-author integrator dispatched by Main
verified-at: 2026-10-21
source: .ufo/reports/round-61/revenger.md@6e60ffb4ebec17c42db00156395a5ae2e573bc06; lane 45faeae55d563d3daefce8cee17b3b361b72545b

# Round 61 outside closure — reject the round, retain the separate C2 result

**Status: ok (real landed work); admitted: false; verdict: rejected-honest-stop.**
C1 meets its registered falsifier, not its target. C2 independently improves
under its unchanged holds. Neither C2 nor the fresh wave's completion rescues
C1. No final-state owned-axis harm was demonstrated. No sibling-owned gate,
selftest, Reproduce block, mutation runner, producer, bytecode or JavaScript
was executed by this closure: gate results below are evidence-verified, while
counts, byte comparisons and source checks were independently performed.

## Step-1 conformance

- Report initial filing `2ed86bfd638d8065e4d6d9a168d4ba572cff7cf6` and erratum
  `6e60ffb4ebec17c42db00156395a5ae2e573bc06` both have author
  `revenger-shokunin`. The report has four SHONEN lines: one unchecked and
  three partial. SKILL.md remains absent; the lane is not promotion-ready.
- All eight round landings `e0a4b0c`, `0b6ddf0`, `2e27c6c`, `6e89c249`,
  `0597e53`, `ab580698`, `7a66d224`, `45faeae5` are ancestors of
  `refs/heads/main` (each `git merge-base --is-ancestor` returned 0).
- Before this integrator's sole new lesson: `jj-lane.sh state` showed
  local=remote=`45faeae55d563d3daefce8cee17b3b361b72545b`, ahead=0,
  behind=0, tracked=0, untracked=0; `git status --porcelain` was empty.
- Rendered round prompt contains sections 1–6, the claim/admission contract,
  report/SHONEN contract and campaign addendum. Closure follows the current
  full closure prompt, including this new non-author lesson.
- Report preservation independently checked using the two committed blobs:
  final bytes begin with **all 11,219 original bytes**, byte-exact; final
  length 17,379. Original SHA-256:
  `1374de2e39e57e8720ac7deb89da06e866643b3c34fe56d2709719168e22bbcd`.
  The superseding text is appended; the provisional claims remain historical.
- Two unrelated operator reflection commits in lane history are not round
  accomplishments. Existing missing SKILL/registry debt is not fixed or
  credited here. C2 evidence is not a declaration of full gate conformance.

## C1 — independently re-counted, falsified

Frozen `reports/round-61/claims.md:19–40,85–108` requires Q01–Q11,
a round-opened tier-A source, **in-entry derivations**, survival of attacks,
and backed knowledge files. Four of fourteen is explicitly the falsifier.
Amendment A2 narrows scope; its final timing clarification admits that it
landed with the drafts, not before drafting. No retrospective re-freeze is
accepted.

Plain measurements over committed bytes, not execution of `measure.py`:

```text
git show <revision>:corpus/README.md
select /^\| C[0-9]+ /; count /\| held \|$/; verify named knowledge paths in git ls-tree
cf024192: 14 rows, held/backed 4 (C01,C11,C12,C13); C04/C09 uncovered
0b6ddf0:  14 rows, held/backed 6; C04/C09 provisionally held
7a66d224: 14 rows, held/backed 4; C04/C09 uncovered
45faeae5: 14 rows, held/backed 4; C04/C09 uncovered
```

All fourteen final map statuses equal their base statuses. QUALITY Q11's
entire row is byte-identical base→final; Q12/Q13 were additions, not a
weakening of Q11. Both rejected files remain, with `admission-status:
rejected` and prominent warnings superseding old pass tables. SCORECARD's
final adjudication, README and lesson erratum withdraw provisional credit;
PROVINCE is byte-unchanged and claims no new admitted surface. No files were
deleted between base and final tip.

Independent inspection corroborates the decisive attacks:

- C04 `Limitations` says its block carries edge spans. Extracting just its
  Python block and counting `location|start|span|column` gives **0** matches;
  the printed fields derive no spans. This contradicts the initial Q11 pass,
  regardless of whether the other printed values are correct. See
  `falsify-w3/W3JsOverclaimCritic.md:5–7,39` and the retained entry:80–83.
- C09's block prints decoded opcode observations but never searches its
  nine-byte embedded pattern and does not derive the raw 0x5B count or the
  embedded target. Correct external values are insufficient under unchanged
  Q11. See `W3EvmR24Immediate.md:16–21`. The unsupported kasegi citation,
  provider role-label generality and Q13 overcredit remain flagged by the
  final warnings and retained attack reports, not silently repaired.

### The [1,9] correction is true, but not sufficient for Q11

Independent byte search of committed `corpus/fixtures/evm-r24/fixture.raw`:

```text
len(raw)=35
pattern=bytes.fromhex('63deadbeef14601057'); len(pattern)=9
all byte-search starts=[1]; inclusive spans=[[1,9]]; occurrence count=1
```

`truth.json` names that pattern and `[1,9]`; original `LOG.md:289` says
"occur only inside immediate offsets 1–9." The earlier interpretation as two
occurrences was wrong. Corrected candidate:94–96 and lesson M25 carry the
inclusive-span interpretation. The correction does not invent a fixture
change: saved bytes remain unchanged. Its attribution/capture wording and
missing in-entry derivation remain disclosed debt, not a repaired C1.

## C2 — evidence-verified separately, not re-executed

Committed `measure-before.log:5–25,32–45` binds the base `cf024192` snapshot;
`measure-after.log:96–136` binds final measurement `7a66d224`. I independently
parsed the individual MUTANT/HOLD rows rather than accepting aggregate text:

| Committed receipt population | Before | Final |
|---|---:|---:|
| Unmodified controls, exit 0 | 2/2 | 2/2 |
| Mutant b, nonzero with last line `forged receipt command accepted` | 0/2 | 2/2 |
| d2 data forgeries rejected | 2/2 | 2/2 |
| Individual HOLD rows exit 0 | 10/10 | 10/10 |
| Saved calibration subset | 4/4 | 4/4 |

Final b rows name `r47: forged receipt command accepted` and
`r42: forged receipt command accepted`; both exits are 1, not unrelated
crashes. Both control scripts exit 0 and retained d2 rows fail at `receipt`.
The amended measurement source accepts a b kill only with that exact suffix,
and refuses a mutation site count other than one.

Source inspection confirms exactly one command-equality conjunct per
verifier before and after; all five original receipt conditions persist in
`receipt_ok`. The added check deep-copies the already-valid receipt and
changes only its command, then requires rejection through the same predicate.
C2 code is byte-identical initial work `0b6ddf0`→final `45faeae5`:

- `verify_icon_languages.py` SHA-256
  `0f781c6a216bfdaa9cc1ab9b9fe8ae3ab9cb8a79d00ed56c4f94282c80a8efbd`.
- `verify_multi_icon_states.py` SHA-256
  `0179e93f8bec17d5f4b60047f167ad26aa803a84440e98329fd8a8f2ea7a176d`.

`git diff --name-only cf024192 45faeae5 -- corpus/live corpus/fixtures`
prints nothing. Measurement-only final-tip additions do not change C2's
executing code or saved inputs. The remaining receipt conjunct mutations and
other verifiers are explicitly outside this claim. Capabilities added: none;
C2 is a regression guard, not producer authenticity or broad safety.

## Outside discernment spot-check table

The two initial candidate admits were superseded internally before closure;
I still sample one historical admit as required and separately assess the
current rejection. This table is non-author, unlike the lane's waves.

| Item | Lane decision sampled | Re-opened source | Outside verdict | Reason |
|---|---|---|---|---|
| C04 CommonJS candidate | Initial Gate admit | Candidate Reproduce/Provenance/Limitations; unchanged QUALITY Q11 | **disagree with initial admit; agree with final reject** | Claimed span derivations do not exist in its block; success of other derivations cannot satisfy Q11. |
| C09 EVM candidate | Final Gate reject | Candidate block; r24 bytes/truth; original LOG:289 | **agree** | The span is one occurrence, but asserted count/span/target values lack the required in-entry derivations. |
| S024 RFC 3227 | Reject as out-of-province | https://www.rfc-editor.org/rfc/rfc3227.txt, Abstract and §2.1 | **agree** | Live-system incident evidence collection is outside the static shipped-artifact ledger claim; unlike old S008, the successor row actually credits the volatility primitive it quotes. |

New row S024's located quote was re-opened verbatim in §2.1:
"When collecting evidence you should proceed from the volatile to the less
volatile." (13 words, ≤25.) The source does contain the ordering primitive;
its rejection rests on scope, not absence of that primitive. This does not
endorse every branch of Q12's successor-flip condition.

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root
/home/vgpnk/Projects/shokunin revenger` returned 0 (`revenger ok`), with one
W04 for S024's scoped duplicate RFC URL. Independent row count: **15→27**;
final census A25/C2, mined22/queued1/rejected4. Source-row count growth does
not turn C1's rejected candidates into coverage.

## Three-wave accounting and preserved evidence

- Validated dispatch task arrays independently counted **68+65+66=199**;
  all names distinct within and across waves; no explicit model parameters.
- Actual dead-session transcript `CloseChousa26.jsonl` has the r61 accepted
  spawns 68 at 15:42:13Z and 65 at 16:08:47Z. Its earlier 2-seat spawn at
  14:25:26Z belongs to the earlier chousa closure, not revenger r61. The
  build's nine cap refusals spent no accepted seats.
- Original falsify set: 65 actual seat transcripts, all contain host-abort
  errors, **0 lane reports**. Of their session .md files, 54 are empty and
  11 contain only interrupted progress/cancellation fragments. They remain
  dead; none is credited as a completed report.
- Fresh replacement transcript has one actual eval/task spawn of 66 at
  16:42:01Z. A bash result earlier echoing "Spawned 65" reads old evidence;
  it is not another dispatch. The new task payloads are not identical to
  any old task, use new identities and attack corrected integrated `ab580698`
  rather than original `6e89c249`. Subject overlap is not erased: both
  waves concern C04/C09/C2, but the fresh design attacks concrete integrated
  assertions and was explicitly authorized by Main. It does not revive or
  replace the original deaths.
- Reports: 68 build, 0 old falsify, 66 fresh. All 66 fresh report hashes
  equal `falsify-w3/adjudication.json`; independent grade recount matches
  **30 HOLDS / 31 PARTIAL / 5 BROKEN**. These are advisory, not votes to admit.
- Report erratum preserves its filed prefix; rollback deleted no files.
  Counterexample provenance and the 65-death receipt remain committed.
- This closure attempted three read-only reviewer slices; the host refused
  all three at the 100-job cap. No closure reviewers spawned and no extra
  round seats are claimed. I completed the checks directly.

## Axis and trend verdicts

| Axis | Verdict | Evidence |
|---|---|---|
| coverage | unchanged; C1 falsified | 4/14 backed both ends; all map statuses restored |
| calibration | improved narrowly | C2 attributed 0/2→2/2 committed receipts and unchanged holds |
| depth | unchanged | no new admitted knowledge or widened semantic claim |
| operability | unchanged | saved controls/replays preserved in committed evidence; no gate execution by closure |
| freshness | unchanged | no new producer execution or current-release claim |
| adjacency | unchanged | PROVINCE unchanged; rejected cross-lane citations are not new ground |

Trends: **expansion unchanged**, **quality improved** (C2's separate guard,
unchanged saved inputs and enforced candidate rejection), **discernment
improved narrowly** (outside review corroborates the corrected source rejection
and final Q11 decisions, while disagreeing with the historical admits).
No axis gain compensates for C1's failed target: the whole round is rejected.

## Routed defects

1. Keep C04/C09 uncovered until a future separately declared candidate meets
   unchanged Q11; derive or accurately label the missing spans/counts/targets.
   Do not treat this closure's byte checks as missing in-entry derivations.
2. Carry the false kasegi citation, Electron-role semantics, Q13 overcredit,
   source search-log counts/dispositions, S019 anchor, Q12 successor-flip
   weakness and M25 attribution/capture defects named by the final erratum.
   Retained rejection warnings prevent current admission, not future reuse.
3. Keep the K probe's existence-only/non-target-status blind spots separate
   from admission and the two-script C2 guard separate from other clauses.
4. Existing SKILL/registry absence, prior F03 verdict-vs-STALE discrepancy
   and operator-owned ADJ-06 arbitration remain open. No promotion is implied.

No tools installed or updated by this integrator. The filed report separately
records fresh-seat ephemeral tooling; no acquisition is credited as capability.
