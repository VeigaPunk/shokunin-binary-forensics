# R71W2Simplify — YAGNI review of the final v6 candidate and the C2 gate/counter patch

**VERDICT: nothing-to-drop at claim level. Exactly one safe source deletion exists (an unused `timeout=120` default at `corpus/check_embedded_outputs.py:102`), and one located instrument defect was found in the frozen C2 counter (`reports/round-71/measure.py:119-120`: its self-test conjunct is satisfied by the gate's own success banner, so a mutant with both new self-test legs deleted still scores `HOLDS_C2_V1=yes`). No source edit was made; every claim, target, threshold and kill rule is preserved by the deletion; the defect is reported, not repaired.**

Seat target: final candidate `4c1eeaee88fd07e442f1bd546faf77be3957d390`; measured archive `c6e284c6583fa3502754361f411b66646880ba02` (candidate + wave-2 dispatch/spec/registry files only). Lane HEAD moved mid-seat to `a16e6cbe24c51e6952e973d6b47560b49311420d`; `git diff --name-status c6e284c a16e6cb` = `M corpus/SOURCES.md`, `M corpus/lessons/round-71.md` only — the entry, gate and counter bytes are identical, so all findings below carry to the new tip. Gate `corpus/check_embedded_outputs.py` sha256 `05afff8b9f4a47d6705b6de17b7b4e38f28927ac7139dfb2748420a31cf938f8`; counter sha256 `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61` (= A2 binding).

## Axes named

- **coverage (C1)**: untouched — the candidate entry, its 24 embedded blocks, README C05 row, SKILL/Q-map and the 4 seat vote files are not in the deletion.
- **calibration (C2)**: the deletion cannot move either exit-2 leg or the self-test; the located defect is on the *instrument*, not on the landed source.
- **operability**: one authority for the production 120 s limit after the deletion (the CLI reaches `evaluate`'s default, which is the only caller's explicit argument today).
- **depth**: four call-site/dual-mechanism questions were walked to a proof (single caller, sentinel reachability, OSError reachability, import dependency on round-70 measure).
- **freshness/source closure**: no source change; S052/S053 `used-by` cells in `a16e6cb` were checked against the census receipt and do not stale it.

## Evidence (all runs in `/fast/scratch/hyaku/revenger-r71/R71W2Simplify/`, deleted after this report)

```
# 1. Candidate/source identity and frozen-counter binding
git rev-parse HEAD                     -> c6e284c (archive), later a16e6cb
sha256sum reports/round-71/measure.py  -> 718daa96…fcca61  (== A2)
sha256sum corpus/check_embedded_outputs.py -> 05afff8b…f938f8
git diff --name-status c6e284c a16e6cb -> M corpus/SOURCES.md; M corpus/lessons/round-71.md

# 2. Pristine detector on the landed bytes (scratch copy of `git archive c6e284c`)
python3 -B <tree>/corpus/check_embedded_outputs.py --self-test
  SELFTEST OK: … missing-entry and timeout legs passed / EXIT=0
python3 -B <tree>/corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md
  checked_blocks=24 problems=0 / EXIT=0

# 3. Safe-deletion probe (only `def run_cmd(cmd, cwd, timeout=120)` -> `(cmd, cwd, timeout)`)
del/corpus/check_embedded_outputs.py --self-test        -> SELFTEST OK / EXIT=0
del/corpus/check_embedded_outputs.py --entry <v6 entry> -> checked_blocks=24 problems=0 / EXIT=0

# 4. Instrument mutant (gate self-test lines 271-285 deleted, banner 286 kept)
mut/corpus/check_embedded_outputs.py --self-test
  SELFTEST OK: … missing-entry and timeout legs passed / EXIT=0
counter expression `'SELFTEST OK' in out and 'missing-entry' in out and 'timeout' in out` -> True
HYAKU_SCRATCH=<scratch> python3 -B reports/round-71/measure.py <mut tree>
  C1_GATE=checked_blocks=24 problems=0 exit=0 ok=yes
  C1_LINT=LINT_QMAP=0; LINT_Q14=0; LINT_Q15=0; LINT_HEADER=0 exit=0
  C1_W2_Q_VOTES=0/16
  C2_MISSING_ENTRY_EXIT2=1/1 rc=2 stderr_traceback=no
  C2_TIMEOUT_EXIT2=1/1 rc=2 stderr_traceback=no
  C2_GATE_SELFTEST=0 named_legs=1
  HOLDS_C2_V1=yes
  HOLDS_OK_V8=yes   (COUNTER_EXIT=0; HOLD_REPLAY=10/10; EMB_PIN_MUTANT_KILLED_ATTRIBUTED=1/1)
```

## Deletion candidate 1 (exact, verified, not applied)

- **Site**: `corpus/check_embedded_outputs.py:102` — `def run_cmd(cmd, cwd, timeout=120):` → `def run_cmd(cmd, cwd, timeout):`
- **Why it is dead**: `run_cmd` has exactly one call site, `:183`, which always passes `timeout=timeout` from `evaluate(..., timeout=120)` (`:158`). The default is never consumed. Fleet-wide literal search (the `lsp` device is not mounted on this host — recorded, so this is grep, not semantic proof): `grep -rn "run_cmd"` over `/home/vgpnk/Projects/shokunin` returns only unrelated same-named helpers in other lanes' historical artifacts and no import of this gate. The gate is a CLI script; no module imports it.
- **Duplicate authority removed**: the production 120 s limit is currently written twice in one file (default at `:102`, default at `:158`). After the deletion the CLI's only limit is `evaluate`'s, which is what the frozen predicate exercises (`command timed out after {timeout}s` at `:114` formats whatever the caller passed).
- **Preserved contract (probed, not asserted)**: missing-entry exit 2 + `could-not-evaluate: entry not found:`; timeout exit 2 + `…timed out after 120s:`; no traceback; `--self-test` exit 0 with both hermetic legs; the v6 entry still re-gates `checked_blocks=24 problems=0 exit=0`. The 1 s injected timeout in the self-test still selects the message via `evaluate(timeout=1)`.
- **Tradeoff**: the signature becomes one token longer and no longer self-documents a default. Value is small; it is the only YAGNI-mandated deletion and it is optional (zero-touch is also consistent with the frozen claims).

## Located instrument defect D1 (report only — do not repair after scoring)

- **Site**: `reports/round-71/measure.py:119-120`.
  `selftest_ok=grc==0 and 'SELFTEST OK' in gout and 'missing-entry' in gout and 'timeout' in gout`
  `print(f'C2_GATE_SELFTEST={grc} named_legs={int("missing-entry" in gout and "timeout" in gout)}')`
- **Defect**: both searched substrings are present in the gate's success banner itself (`corpus/check_embedded_outputs.py:286`: `… missing-entry and timeout legs passed`). The conjunct therefore tests the banner, not the legs. The only strings that discriminate the legs (`entry not found:` at `:275`, `command timed out after 1s:` at `:285`) are emitted only on failure, so no success-side discriminator exists.
- **Reproduction**: deleting the whole new leg block (`:271-285`) and keeping the banner yields `--self-test` exit 0 and the frozen counter prints `C2_GATE_SELFTEST=0 named_legs=1` / `HOLDS_C2_V1=yes` (log above). The C2 claim requires "`--self-test` exits 0 with fast hermetic cases for both behaviors"; this mutant has no such cases and still holds, so the third conjunct is unmeasured by the frozen instrument.
- **Scope of the finding**: the *landed bytes do contain both legs* (pristine self-test exit 0; W1 `R71W1GateMut` M1/M2 killed by those legs), so this is not a candidate defect and does not move `HOLDS_C2_V1` for the real tree — the two real CLI legs are strong and independent. It is a kill-rule power gap for the record; the counter is SHA-bound to A1/A2 (`718daa96…`), so any repair invalidates the amendment binding. A r72 repair would need per-leg success lines (e.g. `SELFTEST_LEG missing-entry OK`) and a counter match on those, plus a self-test shell-out for the `main()` handler that W1 already recorded as unobserved.
- **Operability note for L1**: `q_votes` fails closed on the *measured* archive (`return 0` when `TREE/.ufo/waves/round-71/w2-votes` is not a directory). That directory is absent at `c6e284c` and `a16e6cb`; the final archive must be taken after the four seat vote files are committed, otherwise C1 stays `0/16` by construction.

## Retention decisions — nothing else may be dropped

1. **v6 entry prose/blocks** (`corpus/knowledge/round-71-apk-axml-byte-evidence.md`): frozen bytes, gate 24/24, Q-map authority; deleting any locator/prose line narrows Q14/Q16 evidence.
2. **README C05 row** "sixth-pass candidate … wave-2 votes pending, no coverage credit": the landing order requires it to stay until adjudication; removing the row would hide the candidate, removing the note would pre-claim credit.
3. **SKILL.md exit-2 mapping appears twice** (verdict-map cell and the `round-71 exit-2 legs` row): predicate-bound — the claim requires the registered row to name both mappings, and the verdict map is the exit-code contract. Deleting either cell narrows a frozen registration; this duplicate authority is intentional, not stale.
4. **SOURCES S052/S053 rows** (incl. the rejected S053 and the rejected six-row C05 list in README): provenance + census 51→53; rejected rows are historical evidence and are never deletable.
5. **Counter bytes** (`reports/round-71/measure.py`): SHA-bound by A1 (`fbd81050…` → `718daa96…`) and A2; an edit silently un-binds both amendments.
6. **`evaluate`'s `(None, None)` sentinel + the CLI `if problems is None:` branch** (`:185`, `:301-302`): reachable and asserted — the self-test's hostile `python3 -c` entry must come back as the sentinel (`:267-269`). Folding it into `CannotEvaluate` would change the printed text for a refused command and break an asserted self-test behavior → harms calibration.
7. **`evaluate`'s `except OSError` → `entry not readable`** (`:164-166`): reachable under EACCES on an existing file; deleting it turns a permission error back into the traceback the claim forbids.
8. **`reports/round-70/measure.py`**: live dependency of the r71 counter (`importlib` load at `reports/round-71/measure.py:148-149`, `mod.self_check`); deleting/renaming it breaks the `SELF_MUTANTS_KILLED=6/6` leg.
9. **Round-71 receipts** (`controls/*`, `census-*`, `vote-parser-control.txt`, `sources-s05*/validate.log`, `w1*`): provenance for the frozen claims and the A2 parser control.
10. **`corpus/README.md` lessons-line wording** ("completed rounds when present"): already the simplification; re-adding round numbers would re-introduce drift.

## Preservation / scope statement

No lane source edit: `git status --porcelain` shows only peer/untracked wave-2 artifacts plus this report; the gate and counter hashes equal the recorded ones. No spawn, no route/config change, no commit, no install (no pacman transaction). Scratch `/fast/scratch/hyaku/revenger-r71/R71W2Simplify/` held the pristine archive, the `del` deletion probe, the `mut` leg-deletion mutant, `counter-mut.log` and `mut-selftest.out`; its contents are reproduced above and it was removed. Stop condition reached: the next deletion (items 1-10) would each harm coverage, calibration, provenance or the frozen instrument binding.

Report trailer: `.ufo/waves/round-71/w2/R71W2Simplify.md`
