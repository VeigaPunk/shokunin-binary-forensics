# R71W2CounterClaim — W2 counter/amendment hash & vote-parser review

**VERDICT: PASS — no C1/C2-blocking defect.** Frozen claim bytes, both amendments and the A2 counter are byte-identical across live worktree, HEAD `c6e284c`, and the extracted `git archive HEAD`; A1/A2 source deltas match exactly what the amendments register; the committed `q_votes` parser is fail-closed on all 18 mutation cases; votes bind to committed TREE bytes only (no fake result directory, no live-lane leak). C1 labels on HEAD today are structurally `C1_W2_Q_VOTES=0/16` → `HOLDS_C1_V6=no` because no vote files are committed yet — that is the designed pre-adjudication state, not a defect; final measurement is L1's post-vote step.

## Hashes (recomputed, live == HEAD == archive)

| File | sha256 (worktree) | sha256 (`git show HEAD:`) | Matches registered |
|---|---|---|---|
| `reports/round-71/claims.md` | `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5` | same | claims frozen hash (A1/A2) ✓ |
| `reports/round-71/measure.py` | `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61` | same | A2 counter hash ✓ |
| `reports/round-71/pre-registration.txt` | `6f1d045037c5263e17ec6678634eba8a61b7794b1defd0f7f5a18b06934add2b` | same | — |
| `reports/round-71/measure-amendment-A1.md` | `251d6379edef214da9e06a0cdf651a345363f04e9eba8ca20e5e69078ade3293` | same | — |
| `reports/round-71/measure-amendment-A2.md` | `1550fdb23ca5edf72d6810af51bdcb2c6cb784fc734a8fdcece0f8985d4db838` | same | — |
| `.ufo/waves/round-71/vote-parser-control.txt` | `00c92903f4c0fc59d0b5e8af23c0d37fdc1fda2fe0f965a67ad4c5bc17ebdf4d` (committed) | same | A2 probe receipt ✓ |

- `git status --porcelain`: only untracked `w2.ready*` flags and `__pycache__/`; zero tracked modifications. HEAD `c6e284c` ("freeze fresh falsification wave") has candidate `4c1eeae` as ancestor (`git merge-base --is-ancestor` → yes).
- Worktree vs HEAD diff for `reports/round-71/` and `.ufo/waves/round-71/`: empty.

## A1/A2 delta verification (blob history, not prose)

- `git rev-parse <c>:reports/round-71/measure.py` + `git cat-file blob | sha256sum`: `18200a4`→`d0d59b79…`, `da4f1ee`→`fbd81050…` (A1), `4c1eeae`→`718daa96…` (A2), `c6e284c`→`718daa96…` (no churn after A2).
- A1 diff `d0d59b79→fbd81050` is exactly one line: `'```\n$ python3 -B sleeper_r71.py\nfinished\n```\n'` → `'```\n$ python3 -B corpus/sleeper_r71.py\n…'` (measure.py:103 today) — matches A1's "timeout fixture path only".
- A2 diff `fbd81050→718daa96` is exactly: docstring archive contract, `unique_object` `object_pairs_hook` (raises on duplicate key), `q_votes(tree)` reading `Path(tree)/'.ufo/waves/round-71/w2-votes'` instead of live `LANE`, `if not isinstance(data,dict): return 0`, and the `q_votes(tree)` call site — matches A2 claims 1–2. No other deltas.

## Vote parser behavior (empirical, against the committed archive's own module)

Method: `git archive HEAD | tar -x` into scratch, `importlib`-loaded `tree/reports/round-71/measure.py` (sha `718daa96…` inside archive), `q_votes()` probed on synthetic `w2-votes/` dirs. 18/18 OK (`probe-out.txt`):

- `valid_16_pass`=16; one `n/a`=16 (PASS/n/a accepted, `N/A` wrong case→0).
- Rejected to 0 (each): duplicate top-level key; duplicate key inside `decisions` (`object_pairs_hook`); non-object root `[1,2]` and `"hello"` (no exception — receipt not truncated); filename/stem ≠ seat (`R71W2Q01Q03.json` carrying seat `R71W2Q01Q04`); extra `Q17`; missing `Q12`; `FAIL` value; unassigned stray seat file; cross-seat duplicate `Q01`; non-JSON garbage (covers Markdown-fenced bodies — same `json.loads` `ValueError` path); non-UTF-8 bytes; missing `seat` key; valid votes only in a nested subdir (glob is non-recursive); absent directory.
- Strictness is all-or-nothing by construction: any one malformed/foreign file returns 0/16, so a `PASS`-with-one-poisoned-file cannot masquerade as partial credit. Matches the frozen predicate "missing, malformed or failed votes keep `HOLDS_C1_V6=no`".

## No fake result directory / committed-bytes binding

- The only `w2-votes` reader is `q_votes` at `measure.py:57`, rooted at `Path(tree)/…` — the TREE argument, never the live lane. `grep -n 'w2-votes|results|LANE' reports/round-71/measure.py`: no precomputed results file is read anywhere.
- Empirical binding: `q_votes(extracted_HEAD_tree)=0` (no votes committed; `git ls-tree -r HEAD | grep -c w2-votes` = 0) while the live lane also has none; planting a valid fake set **only inside the extracted copy** → 16 with the live lane still votes-free. The counter cannot be fed by a live or scratch directory.
- `git archive HEAD .ufo/waves/round-71/vote-parser-control.txt` succeeds — tracked `.ufo` paths survive archiving, so L1's final archive command can carry the committed vote directory as A2 requires. Counter `__main__` fails closed: non-TREE arg → exit 2; uncaught exception → exit 2 (`COUNTER_ERROR`).
- Counter scratch is `HYAKU_SCRATCH/revenger-r71/counter`, `rmtree`d in `finally`; the timeout leg copies TREE corpus into its own scratch fixture (never mutates TREE).
- `.ufo/waves/round-71/w2-votes/` does not exist at review time — nothing fake to reject; `vote-parser-control.txt` is a committed probe receipt, not a vote source.

## C1/C2 labels on the final committed archive

- No final-candidate measure log exists yet (`reports/round-71/` holds only `measure-before.log` + controls A–D; `.ufo/waves/round-71/w2/` has only registry/draft files). Final measurement is L1's post-vote adjudication step by the frozen landing order.
- Structural labels on HEAD today (empirically): votes absent → `C1_W2_Q_VOTES=0/16` → `HOLDS_C1_V6=no`. C1 conjunction (measure.py:88–89) requires K=9/14 ∧ strict=9 ∧ `C05_STATUS=held` ∧ knowledge column == `knowledge/round-71-apk-axml-byte-evidence.md` ∧ v6 admitted ∧ gate ≥17 blocks/0 problems ∧ lint 0 ∧ votes 16. C2 (measure.py:100–108): missing-entry exit 2 + `could-not-evaluate: entry not found:` + no traceback ∧ 120s timeout exit 2 + registered text + no traceback ∧ `--self-test` 0 with named legs. A1's corrected fixture path (`corpus/sleeper_r71.py`, :103) is present so the timeout leg reaches the production 120s limit.

## What the counter cannot authenticate (honest limits)

1. **Vote authorship.** The only identity check is the self-declared `seat` string vs filename (`path.stem != seat`, :63). Nothing cryptographically binds file bytes to the authoring agent; any lane writer could produce all four files. This is exactly A2's registered disclaimer ("structural receipts, not cryptographic identity proof") — confirmed in code.
2. **Measured-commit identity.** The counter trusts the TREE handed to it; that TREE == the final candidate commit rests on L1's logged `git archive` invocation, not on anything measure.py verifies.
3. **Decision sincerity.** 16/16 structural PASS says nothing about whether reviews were actually performed — that is what the four reviewer reports + spotcheck are for.
4. **Exit code semantics.** Exit 0/1 tracks `HOLDS_OK_V8` only (`return 0 if holds else 1`, :168); C1/C2 verdicts are read from printed labels. Consistent with the pre-registration exit contract, but a reader must not equate exit 0 with C1/C2 passing.

## Findings (severity-ordered)

- **No High/Medium findings.**
- **Low (docstring/behavior mismatch, no label impact):** docstring says "Reads only TREE and lane git objects" (measure.py:4), but :149 executes `LANE/'reports/round-70/measure.py'` from the **live worktree** (`spec_from_file_location`) for `SELF_CLEAN_FIXTURE`/`SELF_MUTANTS_KILLED`. Verified byte-identical to HEAD right now (`r70_measure_live_eq_committed=True`), and it feeds no C1/C2 label, so no effect on adjudication — but if the worktree dirtied post-freeze, the counter would execute non-committed code. `--lane` on lint (:96) and self_assessment (:143) is git-objects-only per those tools' own docs (`git cat-file -e`), which does match the docstring.

## Residual risk & verification gaps

- The 120s C2 timeout leg and full `HOLDS_OK_V8` replay were not re-executed by this seat (Q-reviewers/L1 run the full counter; ~150s+ leg excluded from this hash/parser lane). Base-red receipts and label logic were verified by source read + probe, not by a fresh full-candidate run.
- First probe run had a fixture bug (missing `.json` suffix); all 18 cases re-run clean after fix — recorded for calibration honesty.

## Commands (representative)

- `git rev-parse HEAD; git status --porcelain; git merge-base --is-ancestor 4c1eeae… HEAD`
- `sha256sum reports/round-71/{claims.md,measure.py,pre-registration.txt,measure-amendment-A1.md,measure-amendment-A2.md}`; `git show HEAD:<f> | sha256sum` per file
- `git archive HEAD | tar -x -C <scratch>/tree`; importlib-load committed `measure.py`; 18-case `probe.py` → `probe-out.txt`
- `git rev-parse <commit>:reports/round-71/measure.py` + `git cat-file blob` diffs for A1/A2 deltas
- Tool installs: none. Scratch `…/R71W2CounterClaim/` removed after this report.

Report: `.ufo/waves/round-71/w2/R71W2CounterClaim.md`
