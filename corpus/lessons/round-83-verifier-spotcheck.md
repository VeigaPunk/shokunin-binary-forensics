author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

# revenger round 83 — verifier spot-check (non-author closure)

Lane repo: `C:/Users/jpvei/.zcode/workspace/95b1ba4d-5089-47a4-9fd8-54adebbce2ae/fleet/shokunin-binary-forensics`
(branch `main`). Base `c153e44839ed` → tip `b56d81bd83811b3e122f24cb81352472d2afd554`
(range = exactly 4 commits: `60693f2` carry-in, `28e8c29` freeze, `75298d4`
landing, `b56d81b` adjudication). Report:
`shokunin-clone/shokunin/.ufo/reports/round-83/revenger.md`. All commands below
were run by this verifier (fresh session, not the author); index-free git only.
Scratch working dirs: `scratch/revenger-r83/work/` (recon-pre, recon-post,
ext-base@60693f2, ext-landing@75298d4, ext-tip@b56d81bd, my logs).

## Step-1 conformance

| check | command | observed | result |
|---|---|---|---|
| report committed by lane identity | `git -C <main repo> log --format='%an <%ae> %H' -1 -- .ufo/reports/round-83/revenger.md` | `revenger-shokunin <revenger@shokunin.local> af8f5ce7157f8a53d81959237ef245550e5f1848` | pass |
| report commit touches only its report file | `git diff-tree -r --name-status af8f5ce` | `A .ufo/reports/round-83/revenger.md` (single file) | pass |
| SHONEN heading | read report | `## SHONEN` with one `[~]` line per box (4/4), pointers present | pass (asserted-by-author; see operator note) |
| cited lane commits exist + ancestors of main | `git cat-file -e <h>^{commit}` + `git merge-base --is-ancestor <h> refs/heads/main` for `60693f2`, `28e8c29`, `75298d4`, `b56d81bd`, `c153e448` | all exist, all ancestors | pass |
| branch tip pushed | `git ls-remote origin refs/heads/main` vs `git rev-parse refs/heads/main` | both `b56d81bd8381…` | pass |
| cited work reachable in range | `git rev-list --count c153e44839ed..b56d81bd…` + `git log --format='%h %s'` | 4 commits, all four cited round commits in range with matching subjects | pass |
| dispatch digest | grep `.ufo/watchdog.log` | `2026-11-01T15:03:07-08:00 launch revenger round=83 base=c153e44839ed (zcode run14)` / `2026-11-01T18:24:54-08:00 complete revenger round=83 head=b56d81bd8381 pushed=True` — matches the closure contract's digest | pass |
| dispatch prompt durable | `git log -1 -- .ufo/prompts/revenger-round-83.md` (main repo) | committed `4211cb4c` by revenger-shokunin | pass |
| marker check | report names 4 commits, real work, evidence pointers | not a marker — real report | pass (status ok) |
| write scope / append-only | `git diff-tree -r --name-status c153e448 b56d81bd` | only lane-owned paths; PROVINCE.md / SKILL.md / SHONEN.md absent from the range (byte-unchanged); SCORECARD.md +76/−0 (additions only) | pass |

## Load-bearing check 1 — the seven r82 carry-in receipts

Byte-verified at `60693f2` against the worktree (tip HEAD `b56d81bd`):

```
for f in ag-after.log sweep3-selftest-after.log sweep3-mutant-kill.log \
         sweep3-real-after.log c1-only.log c2-only.log noharm-diff.txt; do
  git show 60693f2ce6b0…:reports/round-82/$f | sha256sum   # blob side
  sha256sum reports/round-82/$f                            # worktree side
done
```

7/7 MATCH (ab918d9416ce…, ac453532a40a…, 6fb40a0823cf…, 7df70651ce8a…,
a0bb189bcb00…, 7c962f3dd6a3…, 3d8edb2cfc2e…). Sanity: the seven are ABSENT
from `c153e448`'s tree (`git ls-tree -r --name-only c153e448 -- reports/round-82`
+ grep → none) and PRESENT at `60693f2` (7). The r82 citations are verifiably
2 path-form + 5 bare-form (`grep` over `.ufo/reports/round-82/revenger.md`).

## Load-bearing check 2 — sweep red/green re-derived from scratch

Reconstruction (no checkout anywhere): two fresh repos via
`git init -b main` + `git fetch <lane-repo> main` + `git update-ref
refs/heads/main <sha>`; disk = exactly the seven receipts at
`reports/round-82/`; fleet root = the main repo (its `.ufo/reports/*/revenger.md`
are the citation corpus).

| run | command (all `PYTHONUTF8=1 python -B`) | observed | exit |
|---|---|---|---|
| RED v3 | `reports/round-82/orphan_sweep3.py --lane recon-pre --fleet <main repo>` | `CITED=267 COMMITTED=247 LANDABLE_ORPHANS=2 ABSENT=18`; orphans = `reports/round-82/ag-after.log` + `reports/round-82/noharm-diff.txt` (the only path-cited forms) — **2 of 7**, five bare-cited invisible | **1** |
| RED v4 | `reports/round-83/orphan_sweep4.py --lane recon-pre --fleet <main repo> --format full` | **9 orphan rows covering all 7 files** (ag-after.log and noharm-diff.txt each cited in 2 forms → 9 rows); `SWEEP_BARE_TOKENS matched=156` | **1** |
| GREEN v3 | same over recon-post (HEAD=`60693f2`) | `LANDABLE_ORPHANS=0` | **0** |
| GREEN v4 | same over recon-post | `LANDABLE_ORPHANS=0` | **0** |
| REAL tree | v4 over the lane worktree at tip | `CITED=699 COMMITTED=687 LANDABLE_ORPHANS=0 ABSENT=12`, `SWEEP_CORPUS fleet-reports=24 lessons=47` | **0** |

My basis lines differ from the committed receipts' (v3 recon committed basis
`CITED=254 COMMITTED=247 LANDABLE_ORPHANS=2 ABSENT=5`; real-tree committed
`CITED=677 … fleet-reports=23 lessons=46`) — expected per-revision-corpus
movement (the r83 report has since landed in the fleet root; the adjudication
added the lesson), disclosed in the receipts' own headers. Every load-bearing
value reproduces exactly: LANDABLE_ORPHANS 2→0, exit 1→0, 9 rows / 7 files.
Committed wave receipts `sweep-pre-landing.log` / `sweep-post-landing.log`
match the report's quoted values.

## Claim C1 (coverage — A1 2/3 → 3/3) — RE-MEASURED

| step | command | observed |
|---|---|---|
| before | `python -B reports/round-82/ag_probe.py <ext-base 60693f2>/corpus` | `A1_RECORDED=2/3 score=6.67`, `decode_interface_builder=unrecorded` (matches committed `ag-red.log`) |
| after | `python -B reports/round-82/ag_probe.py <ext-landing 75298d4>/corpus` | `A1_RECORDED=3/3 score=10.00`, `decode_interface_builder=round-83` (matches committed `ag-after.log`) |
| oracle | `python -I -B <ext-landing>/corpus/fixtures/app-r83/oracle_check.py truth.json corpus/live/runs/round-83/inspection.json <ext-landing>/corpus/fixtures/app-r83/R83Sample.app` | `ORACLE byte-derived 26/26, hypothesis 18/18` + `ORACLE OK (44/44 checks)`, exit 0 |
| producer record | read `receipt.json` (committed landing) | command `rea decode-interface-builder corpus/fixtures/app-r83/R83Sample.app --format json`, exit_code 0, stderr_bytes 0, Evidence `ev_260481425d1a…0610f8`, fixture shas `1bb04ef8…319e` / `f0746e35…315e` / `7953ce25…566` — all match the report |
| regen byte-identical | `python -I -B build_app.py --out <scratch>` | 18/18 SELFCHECK; all three built files sha-identical to the committed fixture bytes |
| instrument integrity | sha256 worktree vs tip/freeze blobs | v4 `f520f8d69875…c2ea701`, v3 `af64b4c5…b8748`, ag_probe `22be124b…a08a5` — worktree == freeze == tip |
| separability | read committed `c1-only.log` / `c2-only.log` | c1-only: v4 ABSENT + `A1_RECORDED=3/3` + `ORACLE OK (44/44)`; c2-only: fixture ABSENT + `SWEEP_SELFTEST=pass` + `A1_RECORDED=2/3` — claims separable as frozen |
| no-harm | committed `noharm-diff.txt` + own diff-tree | protected paths empty on `28e8c29..75298d4`; 11 files, additions only; v1/v2/v3 instruments + f_probe4 + ag_probe absent from the range; FRESH_ROWS 12+6 = 18/18 |

**C1 verdict: verified — coverage improved.** A1 saturates at 3/3 as reported.

## Claim C2 (calibration — orphan_sweep v4) — RE-MEASURED

| step | command | observed |
|---|---|---|
| selftest | `python -B reports/round-83/orphan_sweep4.py --selftest` | 13 `=ok` legs, `SWEEP_SELFTEST=pass`, exit 0 |
| mutant kill | `sed '87s/BARE_TOKEN_CLASSIFICATION = True/… = False/'` → `--selftest` on the mutant | diff vs committed v4 = exactly one changed line (87); mutant exits 1, last line `selftest: bare-filename classification drifted (bare-token class)` |
| red/green | see table above | v3 red 2-of-7 exit 1 → v4 red 9 rows / 7 files exit 1 → both green 0 exit 0 at HEAD=`60693f2` |
| falsifiability | read v4 selftest source | `SWEEP_SELFTEST_BARE_MUTANT_FLAGGED` asserts the disabled twin MUST disagree with the bare-orphan vector — the vector can fail |
| real tree | v4 over lane worktree at tip | `LANDABLE_ORPHANS=0` exit 0 (basis movement disclosed above) |

**C2 verdict: verified — calibration improved** (capability supersession, no
new capability row claimed — consistent with SCORECARD).

## Mined mistakes — all six verified real

| # | mistake (lesson `## Mistakes`) | verification performed |
|---|---|---|
| 1 | LEB128 varint drafting (terminator-bit is the inverse) | `preprobe-app-shape.log` probe 2 carries the real parser rejection (`NIBArchive variable integer is too long`) + probe 3 terminator-bit decode; `build_app.py` documents the inversion and reads terminator-bit varints |
| 2 | check-from-intent (SELFCHECK wrong, bytes right; 211-byte constant) | committed generator contains no `211` constant (`grep -cE '\b211\b'` → 0); sizes re-derived by regen = 213/79 |
| 3 | count-from-intent ×2 (282→313 plist bytes; 7507→9012 stdout bytes) | committed `claims.md` says 313; `LEDGER.md` says 9012; actual `inspection.json` = 9012 bytes (`wc -c`) |
| 4 | CRLF-mutant (mutant must derive from committed LF bytes) | committed `orphan_sweep4.py` has 0 CR bytes; my own one-substitution mutant from those bytes differs by exactly line 87 |
| 5 | separability-tree base error | committed c1-only/c2-only receipts carry the corrected pre-freeze-base states (v4 ABSENT / fixture ABSENT respectively) |
| 6 | killed-run census receipt artifact (false exit 1 with clean ok output) | committed `.ufo/waves/round-83/census-round-start-sanctioned.log` IS the killed run's output: 21 W01 + 10 W04, zero E, verdict `ok` — preserved as the evidence |

## Discernment spot-check (external, this verifier)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S462 (declared interface-builder surface) | ADMIT | `PYTHONUTF8=1 rea decode-interface-builder --help` on this host | **agree** | help header prints the quoted sentence verbatim: "Decode compiled storyboard and nib archives from an app bundle" (9 words); `--schema` shows the declared budget options |
| S463 (installed parser source) | ADMIT | `sed -n '28p' AppData/Roaming/npm/node_modules/rea-agents/dist/artifacts/apple/NibArchive.js` | **agree** | line 28 contains exactly `throw new TypeError(`Unsupported NIBArchive format version ${formatVersion}`)` (10 words); grounds the fixture-layout derivation |
| S464 (producer record + fixture) | ADMIT | my own oracle/probe re-runs over the landing archive | **agree** | record is real, exit 0, oracle 44/44 re-derives from committed bytes |
| macho/signature providers | ruled out | `PYTHONUTF8=1 rea capabilities` | **agree** | those provider groups print `available: false` / `availability_code: unsupported_host` while `rea-artifact-graph` prints `available: true` |
| F android family | ruled out | `echo $REA_JADX_MCP_JAR`, `command -v jadx`, `ls ~/tools` | **agree** | env UNSET, jadx not on PATH, `~/tools` = downloads/ + ghidra only — the hard gate stands |
| S465 basis quote | (row anchor) | committed `v3-prelanding-recon.log` | **agree** | quote `CITED=254 COMMITTED=247 LANDABLE_ORPHANS=2 ABSENT=5` matches the committed receipt |

Census (duty-3 command): literal form `sources-census.sh validate --root <fleet
root> revenger` → exit 2 (`revenger	missing …/shokunin-clone/shokunin/revenger-shokunin/corpus/SOURCES.md`)
— the disclosed r74–r82 lineage, not a new failure. Sanctioned explicit-dir
form `sources-census.sh validate <lane-repo> --root <fleet root>` → **exit 0,
31 W (21 W01 + 10 W04, same disclosed classes), 0 E, verdict `ok`** — matches
the round's receipts and independently settles the killed-run's disputed exit.

SOURCES.md census at tip: 465 rows, malformed 0, tier A=417 B=21 C=27,
mined=430 queued=16 rejected=19 — matches the report's stated histogram; rows
S462–S465 sit inside `## Registry` with used-by = claims.md + round-83 lesson.

## Per-axis verdicts

| axis | verdict | evidence |
|---|---|---|
| coverage | **improved** | A1 2/3 → 3/3 re-measured on the registered instrument; K 8/15 and F4 10/11 unchanged as disclosed |
| calibration | **improved** | v4 supersession fully re-derived (selftest, mutant, red/green, real tree) |
| depth | unchanged | no SKILL byte in the range; no depth claim |
| operability | unchanged | instruments run from committed bytes (re-verified), no new operability move claimed |
| freshness | unchanged | 18/18 holds re-verified from `noharm-diff.txt` |
| adjacency | unchanged | ADJ-06 unchanged; no cross-domain absorption observed |

No axis harmed: `git diff-tree` over the range shows additions only;
PROVINCE/SKILL/SHONEN byte-unchanged; no other lane touched.

## Trend verdicts

- **expansion: improved** — the artifact-graph family's last unrecorded
  declared operation now carries a real, oracle-checked producer record
  (re-measured 2/3 → 3/3); no knowledge admission claimed or attempted (K
  route operator-blocked, re-checked not bypassed).
- **quality: improved** — A1 completed on its frozen instrument (blob-verified
  unchanged); the demonstrated citation-form blind spot became machine-caught
  inside the standing instrument with a falsifiable red/green and
  mutation-checked vectors; no admitted entry failed a re-check.
- **discernment: improved** — six real mistakes mined with verifiable evidence
  (all six checked above); this external spot-check agrees with every sampled
  gate decision (2+ admits, 2 rejects re-opened).

## Routed defects (status-neutral; the lane must fix next round)

1. **Unlanded cited receipt (the carry-in class recurring in this round's own
   artifacts):** `reports/round-83/v4-postlanding-recon.log` is cited by the
   report, SCORECARD.md, LOG.md, `corpus/lessons/round-83.md` and SOURCES row
   S465 — but is absent from the committed tree AND the worktree. The
   underlying state is real (this verifier re-derived the post-landing green
   0/exit-0 from a fresh reconstruction), so the claim stands; the pointer does
   not resolve. Fix next round: land the receipt via treecommit explicit paths,
   or append an erratum naming the citation superseded by a re-run receipt.
   Related instrument gap worth a future registered v5 vector: a bare-cited
   token matching NOTHING is skipped as `unmatched_skipped` rather than
   recorded absent — this defect is invisible to v4 by construction (same
   family as the already-routed LOG.md corpus blind spot).
2. **Short-form sha pin drift (number-drift — the very class mined this
   round):** the committed v4 blob is
   `f520f8d69875…bd97029fc2ea701` (suffix `…c2ea701`), but five prose surfaces
   pin the abbreviated suffix `f520f8d6…9701` (report, lesson ×2, SCORECARD,
   LOG). The freeze-time FULL-sha pin in `reports/round-83/claims.md` is
   correct; v3's `af64b4c5…b8748` and ag_probe's `22be124b…a08a5` short pins
   verify. Fix next round: correction entry replacing the abbreviated suffix
   with the claims.md full sha (append-only; never rewrite).
3. **Census receipt pointer:** `reports/round-83/census-after.log` names
   `census-round-start-sanctioned2.log` (the exit-0 re-run) which is not
   committed (the killed run's output IS committed). This verifier re-ran the
   sanctioned census (exit 0), so the value is settled; commit the re-run
   receipt or amend the pointer next round.

## Operator notes

- SHONEN box 2 (end-to-end domain task) is now non-author-verified as
  re-runnable from committed bytes (this closure re-ran the oracle and both
  probes; exit 0 / 44/44 / A1 3/3). Box 3 similarly (selftest 13/13, mutant
  attributed, regen byte-identical — all re-run). The lane's own `[~]` marks
  stand; per protocol only a non-author may write `[x]` — this verifier
  records the observations here and writes no box. The operator may treat this
  file as the non-author verification record for boxes 2 and 3.
- Conformance defects above do not bar admission (protocol: status-neutral).

**Closure: every declared claim verified; no axis harmed → admitted.**
