CONTAINED on the tracked-diff safety fence (no source/fleet/sibling/route or fixture-byte change, gate still read-only, no execution broadening, ADJ-06 fence intact) — but **not frozen**: the working tree has post-receipt edits to both `reports/round-71/claims.md` and `reports/round-71/measure.py` (SHA mismatch against `pre-registration.txt`), repointing C1 vote evidence to a single orchestrator-written `w2-results.json`; and the frozen C2 counter leg is unreachable because its probe entry declares `$ python3 -B sleeper_r71.py` while the sleeper is written to `corpus/sleeper_r71.py` (`drift entry:2 command exited 2` in 0.03s → `C2_TIMEOUT_EXIT2` can never be 1/1).

Seat R71W1Sentinel · round 71 wave 1 · 2026-10-27 · read-only over lane source; scratch `/fast/scratch/hyaku/revenger-r71/R71W1Sentinel/` (deleted) · no lane-source edits.

# 1. Scope / safety fence — CONTAINED

Base `b7abcd8` → HEAD `18200a4`, tracked diff 22 files (`git diff --stat b7abcd8..HEAD`, +2545 −22). Every tracked path is inside the lane (`git diff --name-only b7abcd8..HEAD`): `SKILL.md`, `PROVINCE.md`, `corpus/README.md`, `corpus/SOURCES.md`, `corpus/check_embedded_outputs.py`, `corpus/knowledge/round-71-apk-axml-byte-evidence.md`, `reports/round-71/**`, `.ufo/waves/round-71/**`. No source checkout, sibling lane, fleet-root tracked file or route/config file is touched (`git -C /home/vgpnk/Projects/shokunin status --porcelain -- LOG.md SCORECARD.md MANIFEST.json` → empty).

- **Fixture bytes unchanged.** `git diff --stat b7abcd8..HEAD -- corpus/fixtures` → empty. `corpus/knowledge` changes are additive only: `git diff --name-only b7abcd8..HEAD -- corpus/fixtures corpus/knowledge` prints exactly `corpus/knowledge/round-71-apk-axml-byte-evidence.md`, so the five retained rejected candidates stay byte-preserved.
- **Gate stays read-only.** The only write calls in `corpus/check_embedded_outputs.py` are `write_text` at `:200,211,214,217,238,243,249,266,277,279`, all under the `TemporaryDirectory` at `:292`; no write, unlink or rmtree outside it. Verified no new symlink leaves the tree (`find . -type l -newermt 2026-10-26` → empty).
- **Command execution not broadened.** The diff touches `run_cmd`/`evaluate`/`main` only through the timeout parameter and a `CannotEvaluate` class. `confined()`/`inside()` (`:79-97`) are byte-unchanged (still `python3 [-B] <relative in-tree script>`; no `-c`/`-m`, no absolute or `..`, no escaping symlink), the argv whitelist at `:106-108` is unchanged, and `main()` accepts only `--self-test` / `--entry <path>` / usage-64 — **no `--timeout` or other new CLI surface** (`:289-307`).
- **Landing order respected.** v6 entry carries `admission-status: candidate` (`corpus/knowledge/round-71-apk-axml-byte-evidence.md:12`); `corpus/README.md` C05 status is still `uncovered` and its knowledge column still `—`.
- **C05 v6 pre-gate, re-measured:** `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `checked_blocks=24 problems=0`, `EXIT=0`, matching the README's `gate 24/24` (all 24 declared commands are lane-relative `corpus/fixtures/apk-r65/*` paths, so confinement holds).
- **ADJ-06 fence holds.** Entry `:291-293` keeps the round-70 wording: provider route documented scope from S049 only, no readiness claim, kaidoku/revenger overlap "reported, not absorbed", kaidoku `corpus/README.md:27,:29` not restated. `PROVINCE.md` makes no ownership claim; `grep -c ADJ-06 corpus/README.md` remains 0 (per SHONEN.md:28) and the coverage row adds no ADJ-06 parenthetical.

# 2. Findings

## F0 — HIGH (contract integrity): the frozen counter and frozen predicate were edited after the pre-registration receipt
`reports/round-71/pre-registration.txt` binds two SHA-256 values; both still match the committed tip `18200a4` but not the working tree:
```
$ git show 18200a4:reports/round-71/measure.py | sha256sum
d0d59b79652dae9d65796493f703470dc4d4998ec607cb25a41aed939f38d06c   # = registered counter
$ git show 18200a4:reports/round-71/claims.md | sha256sum
1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5   # = registered claims
$ sha256sum reports/round-71/measure.py reports/round-71/claims.md
39e92babebc5b3550f01583e360ea77211e0f0f2b9af45725d70acd1c1affcec  reports/round-71/measure.py
5b95d343b7f2e5c228d22f7de4dd4d43cb9b1844e4709969d07129c6acc1d19b  reports/round-71/claims.md
$ git status --porcelain -- reports/round-71/pre-registration.txt reports/round-71/claims.md reports/round-71/measure.py
 M reports/round-71/claims.md
 M reports/round-71/measure.py
```
`pre-registration.txt` is unmodified, so it still certifies bytes that are no longer the ones on disk; the wave-1 reports already on disk cite the pre-change instrument.

The edit changes the C1 **vote-evidence mechanism and the kill rule** (`git diff -- reports/round-71/claims.md`), which claims.md itself declares frozen: "Frozen predicates, counter and kill rules below may not change after any seat scores."
- Old predicate: "The counter parses committed per-seat JSON vote files under `.ufo/waves/round-71/w2-votes/`; each carries a unique seat and its assigned Q decisions." Old counter (`HEAD:measure.py` `q_votes`) enforced `root.glob('*.json')`, `path.stem == seat`, `data.get('seat')` known, `set(decisions) == set(expected)`, and `value in ('PASS','n/a')`.
- New predicate: "The counter reads `/home/vgpnk/Projects/shokunin/revenger-shokunin/.ufo/waves/round-71/w2-results.json`, binds four named reviewer seats to their assigned Q subsets, and parses their final `output` text as either JSON-wrapped votes or plain `Qnn: PASS|n/a|FAIL` lines."
- New kill rule: "the four assigned reviewers return their decisions in the orchestrator's `w2-results.json`" (was: "each assigned reviewer writes its JSON vote file at the path specified in its task").
- Control D's declared behaviour was rewritten to match ("has no orchestrator `w2-results.json`, so `C1_W2_Q_VOTES=0/16`").

Exploit path (vote laundering, no tooling needed): write one file, `.ufo/waves/round-71/w2-results.json` (absent today — `ls` → "No such file or directory"), of the form `{"lane":"revenger","round":71,"wave":"w2","results":[{"name":"R71W2Q01Q04","agent":"reviewer","output":"Q01: PASS\nQ02: PASS\nQ03: PASS\nQ04: PASS"}, …four seats…]}`. `q_votes()` (`measure.py:68-91`) then returns 16 with **zero** committed seat votes and **zero** independent authors: it no longer checks file stems, no longer requires the decisions object to equal the assigned set, does not reject an omitted `status` (`str(result.get('status','completed'))` defaults to completed), and `vote_pairs` (`:48-66`) accepts ANY text or JSON containing `Qnn: PASS` — including a seat report that quotes a PASS verdict in order to refute it. A single writer therefore satisfies the conjunct that control D existed to keep red, and the absolute host path in the predicate means the evidence is machine-local prose rather than committed in-repo bytes.

Impact: the registered instrument (`d0d59b7…`) and the running instrument (`39e92ba…`) disagree, so `C1_W2_Q_VOTES=16/16` no longer means what the receipt says it means; any wave-2 measurement taken now is against an unreceipted counter, and `HOLDS_C1_V6` becomes satisfiable by the orchestrator alone. Wave-1 seat reports that quote `C1_W2_Q_VOTES=0/16` describe the old semantics.

Smallest remediation: revert both working-tree files to the registered bytes (`git checkout -- reports/round-71/measure.py reports/round-71/claims.md`), or — if the `w2-results.json` mechanism is genuinely wanted — record a **new** pre-registration receipt (claims SHA + counter SHA + the changed vote rule) before any wave-2 seat scores, keep the per-seat `path.stem == seat` binding and the exact-Q-set check, and drop the free-text `Qnn: PASS` fallback. Do not leave `pre-registration.txt` certifying superseded bytes.

## F1 — HIGH (C2 operability): the counter's timeout leg never exercises a timeout
`reports/round-71/measure.py:129-132` builds the live fixture as
```
d=scratch/'timeout-fixture'; shutil.copytree(tree/'corpus',d/'corpus')
(d/'corpus/sleeper_r71.py').write_text('import time\ntime.sleep(300)\n')
slow=d/'corpus/knowledge/round-71-timeout-probe.md'
slow.write_text('```\n$ python3 -B sleeper_r71.py\nfinished\n```\n')
```
but `gate_cli(d, …)` runs with `cwd=d` (`measure.py:40`), and the gate resolves the declared script against that cwd (`corpus/check_embedded_outputs.py:111-112`, `cwd=str(cwd)`). `sleeper_r71.py` is at `d/corpus/sleeper_r71.py`, so the child exits 2 immediately and `evaluate` records a *drift* instead of raising on timeout (`:183,186-187`).

Evidence (exact measure.py fixture reproduced in scratch):
```
$ python3 -B corpus/check_embedded_outputs.py --entry $S/c2/corpus/knowledge/round-71-timeout-probe.md
drift entry:2 command exited 2: python3 -B sleeper_r71.py
checked_blocks=0 problems=1
EXIT=1        real 0m0.029s
```
So `timed.returncode==2` and `'could-not-evaluate: command timed out after 120s:' in timed.stdout` (`measure.py:135`) are both false → `C2_TIMEOUT_EXIT2=0/1` → `HOLDS_C2_V1=no` **even with the gate repair landed**. The 300-second sleeper never starts, so the leg cannot even fail by outer timeout; it fails fast and silently.

Exploit path (frozen-predicate, not execution): a final tip that satisfies the gate behaviour and the self-test still reports `HOLDS_C2_V1=no`, i.e. the round's own instrument turns a landed repair into a red. Conversely, nothing here produces a false green: the broken leg lowers the score only.

Impact: C2's predicate is unreachable as frozen; wave-2 scoring against this counter falsifies C2 for a fixture bug rather than a behaviour defect. Also inconsistent with the red-before receipt, which used a *root*-level script (`sleeper.py`) and therefore did reach the 120s limit (`reports/round-71/controls/C2-timeout-before.log`, `subprocess.TimeoutExpired: Command '['/usr/bin/python3', '-B', '-B', 'sleeper.py']' timed out after 120 seconds`, `RC=1`) — before and after fixtures disagree.

Smallest remediation: change the probe entry at `measure.py:132` to `$ python3 -B corpus/sleeper_r71.py` (or write the sleeper to `d/'sleeper_r71.py'`). Verified sufficient: with that one-token change the gate blocks on the sleeper (`timeout 4 …` → `EXIT=124`, i.e. the gate is waiting) and the classification fires — `g.evaluate(entry, Path('.'), timeout=1)` → `could-not-evaluate: command timed out after 1s: python3 -B corpus/sleeper_r71.py`; the default-120 string is the same f-string (`check_embedded_outputs.py:114`). Counter is frozen only after a seat scores, so this repair belongs in wave 1 (claims.md: "Wave 1 is advisory pre-gate; repair before the final candidate lands").

## F2 — LOW (fail-soft): exit 2 pre-empts located drift findings
`evaluate` accumulates `problems` per block (`check_embedded_outputs.py:183-190`) but the new `CannotEvaluate` from a later block propagates out of the loop, and `main()` prints only the could-not-evaluate line (`:297-300`), discarding every `drift entry:N …` already found.

Evidence (scratch fixture: block 1 drifts, block 2 sleeps 5s; `evaluate(entry, '.', timeout=1)`):
```
MASKED-DRIFT -> could-not-evaluate: command timed out after 1s: python3 -B sleeper.py
```
The block-1 drift is never printed. No false green (exit 2 fails C1's `checked_blocks>=17 and problems==0` and the counter's `gate_ok`), and the retained-entry `EMB_*`/pin labels are unaffected because pins are checked before the command runs.

Exploit path: an entry that gains one slow declared command silently loses its located findings; a reviewer reading exit 2 cannot tell "nothing evaluated" from "drift found in blocks 1..k, then a slow command".

Smallest remediation: wrap the per-block `run_cmd` call (`:183`) in `try/except CannotEvaluate`, append a `drift entry:{lineno} command timed out` problem (or collect the exception and print accumulated problems before exiting 2). Two lines; does not alter the declared exit-2 texts the C2 predicate pins.

## F3 — LOW (hygiene/adjacency): 6.4 MB untracked duplicate of `corpus/` inside the lane
`.ufo/waves/round-71/sources-s052/validate/corpus/` is an untracked full copy of `corpus/`: 538 files, 6.4 MB (`du -sh`), including `fixtures/`, `knowledge/`, `snapshots/` and a gate copy that is byte-identical to HEAD (`sha256sum` → `05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8` for both). Copied fixture bytes match tracked bytes (`fixtures/apk-r65/fixture.apk` `05d2280f…`, `entry_checks.py` `2d4f25f6…`, `generator.py` `eaa9444c…`), so no byte is altered — but the tree is duplicate fixture material inside a lane that claims "no fixture-byte change", and it is the S052 seat's evidence copy living in the repo instead of `/fast/scratch/hyaku/revenger-r71/<seat>/` as the wave spec requires.

Impact: today none on the tracked tree or on the frozen census — the counter's replay denominator is non-recursive (`reports/round-71/measure.py:145`, `(tree/'corpus').glob('verify_*.py')`), so the second `verify_*.py` family under `.ufo/` cannot inflate `HOLD_REPLAY`. The risk is integration-time: `git status --porcelain` lists it as untracked (not ignored), so a single `git add -A` before the final candidate would commit a second corpus, second fixtures and a second gate. The fleet has already lost a tree that way (`git -C /home/vgpnk/Projects/shokunin log -1 f47ad6ba` → "repair: restore fleet tree deleted by stray commit 35b91714", 2026-10-25).

Smallest remediation: delete `.ufo/waves/round-71/sources-s052/validate/corpus/` before the final candidate, keeping only the committed `validate.log` and the `corpus/SOURCES.md` row receipt; never stage the lane with `git add -A`.

## F4 — LOW (undeclared diff line): `PROVINCE.md` REA pin bump
`PROVINCE.md` is 1+/1− in this round (`git diff --numstat b7abcd8..HEAD -- PROVINCE.md` → `1 1`): base `b7abcd8` has `npx -y rea-agents@6.4.0`, HEAD has `6.5.0` (`PROVINCE.md:19`). Neither `claims.md` nor `pre-registration.txt` names `PROVINCE.md`, so a boundary-doc source pin moved outside the frozen claim set, even though C2's controls say "No change is made to route/global config".

Assessment: admissible in substance, declared nowhere. The pin is real and not fabricated — registry read 2026-10-27, `https://registry.npmjs.org/rea-agents` returns `"dist-tags":{"latest":"6.8.0"}` with `6.5.0` and `6.4.0` both present in `versions`. It is lane-local (not global routing) and consistent with S049's `rea-agents-6.5.0` snapshot, so the risk is audit coverage, not correctness: wave-2 Q10/provenance reviewers were given no claim line to cite for it, and peer `R71W1ProvincePin.md` read the *post-change* file ("the current province pin is already 6.5.0") and so could not see that this round produced it — a base-blob comparison (`git show b7abcd8:PROVINCE.md`) is what distinguishes the two.

Smallest remediation: add one line to `claims.md` "Frontier, sources and preservation" naming the `PROVINCE.md` 6.4.0→6.5.0 pin correction and its S049 basis, or revert the line to keep the frozen diff minimal.

# 3. Source access row for the Gate draft (opened this round)
- `registry.npmjs.org/rea-agents` (npm registry metadata, accessed 2026-10-27): located quote `"dist-tags":{"latest":"6.8.0"}`; `versions` contains `6.5.0` and `6.4.0`. Use: only to test whether `PROVINCE.md:19`'s `rea-agents@6.5.0` pin is a real published version; it is not evidence of REA behaviour, provider reachability or fixture bytes.

# 4. Not claimed
No verification of the C1 prose repairs, Q-map rows, lint result, source quotes or SCORECARD arithmetic (other seats); no run of the full counter; no judgement of the round. No subagent dispatch, no installs or pacman transactions. Scratch receipts for F1/F2 are reproduced as command output above; the scratch tree is deleted.

# 5. Integrator response received (not a ruling by this seat)
L1 `RevengerR71` replied in-session 2026-10-27: it will make the narrow counter-fixture path correction (F1) before any wave-2 scoring and record it as a pre-wave2 amendment, and asked that the finding and probe evidence be preserved (they are, §F1). After this seat's F0 evidence, L1 agreed the results-JSON parser was an unsafe post-ready change and will restore the pre-registration predicate/counter bytes (per-seat `w2-votes` files) while keeping only the sleeper-path correction. This seat's final note to L1: the restore-plus-one-hunk state still differs from the registered counter SHA, so the sleeper repair needs its own recorded line (new `measure.py` sha256 + the statement that the only delta is the probe entry path) before any wave-2 seat scores; verification is `git show 18200a4:reports/round-71/claims.md | sha256sum` = `1febae1…` and `git diff HEAD -- reports/round-71/measure.py` showing only the probe-path hunk. Line references in §F1 identify the code as it stood at the time of review; the amendment will shift them.
