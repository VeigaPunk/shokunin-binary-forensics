Verdict: four exact deletions are safe (3 prose lines/sentences in the v6 entry, 1 dead default in the gate patch) and two non-deletion repairs are required — the gate docstring lost a round-67 provenance citation, and the working-tree `measure.py`/`claims.md` no longer match the pre-registration receipt shas. Nothing else should be dropped: every other surviving sentence carries a frozen repair or a Q-basis.

Seat: R71W1Simplify (leaf, advisory pre-gate). No edits made to lane source; deletions were proved on scratch copies under `/fast/scratch/hyaku/revenger-r71/R71W1Simplify/` (deleted before return). No source rows opened, so no new access dates/quotes.
Proof-method note: no `lsp` device is in this seat's toolset (read/bash/grep/edit/write only), so caller absence is proved by exhaustive in-repo text grep over `*.py` — recorded as the documented fallback, not as semantic proof.

## Baseline (unmodified tip `18200a4`, working tree)

| check | command | output |
|---|---|---|
| entry gate | `python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` | `checked_blocks=24 problems=0`, `GATE_EXIT=0` |
| lint | `python3 -B corpus/lint_entry.py --entry corpus/knowledge/round-71-apk-axml-byte-evidence.md` | `LINT_QMAP=0 / LINT_Q14=0 / LINT_Q15=0 / LINT_HEADER=0`, `LINT_EXIT=0` |
| self-test | `python3 -B corpus/check_embedded_outputs.py --self-test` | `SELFTEST OK: … pin and confinement checks passed, missing-entry and timeout legs passed`, exit 0 |
| missing-entry leg | CLI on nonexistent path | `could-not-evaluate: entry not found: …`, exit 2 |

C05 predicate floor is `>=17` blocks; tip already carries 24, so prose deletion cannot push it under the floor. Lint depends only on header keys, `§Q-map` rows, backticked-hex/byte-count pairs, and commit tokens — no candidate below touches any of those.

## Deletions that improve an axis and harm none (all proved on scratch copies)

| # | file:line | exact deletion | why harmless | proof |
|---|---|---|---|---|
| D1 | `corpus/knowledge/round-71-apk-axml-byte-evidence.md:12` | replace the 25-word line with `admission-status: candidate — wave-2 Q01–Q16 decisions pending` (removes “— round-71 sixth-pass candidate; repairs the four located round-70 prose failures without changing the fixture or embedded command/output blocks”) | second authority for repair scope, already stated verbatim at `:9` (`verified-at:`); the kill rule needs only a single-line `admission-status:` key with `candidate`, which survives | lint 4×0, gate 24/0 (below) |
| D2 | `…:51` | delete the whole line `Item 10's command prints the \`META-INF/MANIFEST.MF\` member's first line; item 16's command prints the general-purpose flags and compression method of every record.` | orphan forward reference placed after item 3's block; items 10 and 16 print their own `$` command above their own output, so it credits nothing and no Q-row cites it | lint 4×0, gate 24/0 |
| D3 | `…:285` | delete `The ZIP APPNOTE layouts are recorded from a snapshot; whether the upstream document has since changed is not checked.` | same disclaimer is already the S032 row's own scope clause (`:4`: “whether it still equals the upstream's current text is not claimed”); a row-scoped disclaimer is the correct authority, the Unknown bullet is the duplicate | lint 4×0, gate 24/0 |
| D4 | `corpus/check_embedded_outputs.py:102` | `def run_cmd(cmd, cwd, timeout=120):` → `def run_cmd(cmd, cwd, timeout):` | `timeout=120` is dead: the sole caller is `run_cmd(cmd, cwd, timeout=timeout)` at `:183` (grep over all `*.py` in the lane finds no second caller), so the default is a second place the frozen 120 lives; deleting it leaves `evaluate(..., timeout=120)` at `:158` as the one authority | self-test still `SELFTEST OK`; missing-entry leg still exit 2 |

Combined scratch proof (entry D1+D2+D3, gate D4), run from the lane root so `$` commands resolve:

```
lint rc= 0 | LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0
gate rc= 0 | checked_blocks=24 problems=0
selftest rc= 0 | SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired, pin and confinement checks passed, missing-entry and timeout legs passed
missing rc= 2 | could-not-evaluate: entry not found: corpus/knowledge/does-not-exist.md
```

Both exit-2 legs are preserved by construction: D4 removes a default, not the `timeout` parameter, and the timeout message is an f-string over that parameter (`:114`), so the CLI (which goes through `evaluate`'s `timeout=120` default) still prints `could-not-evaluate: command timed out after 120s:`; the self-test's 1-second injected case still prints `… after 1s:` (asserted at `:285` and green above). Savings: 57 words + 3 lines in the entry, 12 characters in the gate.

## Rejected deletion candidates (and why)

- `evaluate`'s `entry not readable` branch (`check_embedded_outputs.py:161-166`) — looks redundant beside `is_file()`, but the registered SKILL.md row (`SKILL.md:288`) declares “unreadable/missing entry”, and the C2 claim makes that row the authority for the exact mappings. Deleting it would make the row false; folding it into one message cannot keep the literal `could-not-evaluate: entry not found:` the counter greps (`reports/round-71/measure.py:126`).
- The `return None, "", 2` sentinel paths (`:105-109`) and `if proc is None: return None, None` (`:184-185`) — a second no-evaluate mechanism beside `CannotEvaluate`, but `--self-test:268-269` asserts a hostile `python3 -c` entry yields `(None, None)`, and C2 holds confinement “unchanged”. Collapsing the two mechanisms would edit a frozen gate behavior for style.
- The new docstring sentence at `:18-19` (“A missing/unreadable entry and a command timeout are exit 2 …”) — duplicates the SKILL row, but at the call site it is the operator's one-glance contract and costs two lines. Keep.
- `## Reproduce`'s eight-flag enumeration (`:324`) — the only place the flag *names* sit in one list; deleting it trades operability for nothing (each item already prints its own command, so no criterion needs it, but no axis improves).
- The Observation bullet and Q13/Q16 rows — frozen repairs; deleting any clause restores a round-70 located defect.
- `admission-status`/`coverage-map`/`verified-at` `source:` rows — provenance; several are explicitly historical (round-65/69/70 mining dates). Out of scope by role.

## Two non-deletion findings for L1

1. **Provenance regression in the gate docstring (`18200a4`).** The reflow dropped the round-67 citation that justified keeping the file outside the `verify_*.py` glob: base `b7abcd8` read `… denominator stay untouched (reports/round-67/claims.md §C2).`; tip `:8-10` now reads `… denominator stay untouched.` The self-test docstring also lost its round-68/M45 parenthetical (kept only as the code comment at `:224`). Repair: restore the 12-word citation in the module docstring. Cost 1 line; it is the only in-file link between the filename decision and the frozen census denominator.
2. **Frozen counter and claims no longer match the receipt.** `reports/round-71/pre-registration.txt` records counter `d0d59b79…` and claims `1febae12…`; those are the `18200a4` blobs. The working tree is:
   ```
   39e92bab… reports/round-71/measure.py
   5b95d343… reports/round-71/claims.md
   ```
   `git diff` shows the vote channel was moved from committed per-seat JSON under `.ufo/waves/round-71/w2-votes/` to a single orchestrator `.ufo/waves/round-71/w2-results.json`, with the C1 predicate text edited to match (`claims.md:11`, `:13`, `:15`). Wave 1 has not scored, so re-freezing is still legal — but the receipt must be re-cut (or the base bytes restored) and both files committed before any wave-2 seat votes; otherwise `HOLDS_C1_V6` is scored by a counter whose sha the receipt does not name, which voids the calibration. Side note: `vote_pairs` (`measure.py:49-66`) requires `result.get('agent')=='reviewer'` and rejects duplicate names, so the four wave-2 seats must be dispatched as `reviewer` and land under exactly `R71W2Q01Q04`, `R71W2Q05Q08`, `R71W2Q09Q12`, `R71W2Q13Q16` (`:42-46`), or the predicate reads 0/16.

Tradeoff: D2/D3 remove navigation aids, not evidence — a reader who wants the MANIFEST.MF first line or the APPNOTE currency caveat reaches the same text one click in (item 10's block, S032's row). D1 concentrates repair-scope statements in `verified-at:`, which is where a later audit already looks.

Report: `.ufo/waves/round-71/w1/R71W1Simplify.md`
