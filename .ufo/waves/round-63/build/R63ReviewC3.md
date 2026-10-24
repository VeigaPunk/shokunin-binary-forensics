# R63ReviewC3 — C3 patch review (revenger round 63, hyaku, attempt 1)

Reviewer: revenger-r63.R63ReviewC3 · 2026-10-23 · Frozen contract: `reports/round-63/claims.md` (C3 section, commit 54ab973) + frozen probe `reports/round-63/measure.py`. Baseline for all byte comparisons: `git show 55bcb6e:corpus/<script>`. The `verify_icon_states.py` patch landed mid-review; owner `R63C3IconPatch` confirmed the bytes final before this review was frozen. Lane files touched by this review: only this report. No tool installs (none needed); pacman untouched.

## Verdicts

| Script | Verdict |
|---|---|
| `corpus/verify_named_multi_icon_states.py` | **HOLDS** |
| `corpus/verify_icon_states.py` | **HOLDS** |

## Per-criterion evidence

### corpus/verify_named_multi_icon_states.py — HOLDS

Working-tree diff vs 55bcb6e: 8 added / 1 removed, all receipt-scoped; nothing else changed.

1. **Frozen conjunct byte-preserved, exactly once — PASS.** Claims froze the mutation target `receipt['command']==command`. The `receipt_ok` helper (line 17: ` return receipt['command']==command and …`) contains the full 7-conjunct chain **byte-identical** to the baseline `req(...)` argument (string-slice equality of the whole chain; 7 conjuncts vs 7: command, exit_code, fixture_sha256, evidence_id, stdout_sha256, `isinstance(duration_seconds,(float,int))`, `duration_seconds>=0`). Occurrence count of the frozen clause in the final file: 1 (baseline: 1) — the frozen probe's clause regex `receipt\['command'\]==command` (measure.py:119) hits exactly one site, so `mutate_c3` will not hit could-not-evaluate.
2. **Every pre-existing receipt conjunct survives — PASS.** The only removed line is the original receipt `req(...)` (line 72 at base); its conjunct chain moved verbatim into `receipt_ok` (proven byte-identical, criterion 1). The genuine-receipt check remains as `req(receipt_ok(receipt, command, digest, eid, raw),f'r{r} receipt')` (line 79) with the original message `f'r{r} receipt'` preserved. Helper/call signatures align: `def receipt_ok(receipt, command, digest, eid, raw)` called with the same values the inline check closed over.
3. **Exactly one new forged-receipt control — PASS.** Lines 75–78: `forged=copy.deepcopy(receipt)` / `forged['command'] += ' --forged'` / `req(not receipt_ok(forged, …), f'r{r}: forged receipt accepted')` — exactly the frozen forge field for this script; one control site (executed once per round 55/56/57); message contains `forged receipt`. Baseline contained zero `forged receipt` strings. Matches the frozen fix shape exactly.
4. **No saved-input assertion / EXPECT / PASS change — PASS.** `EXPECT={55:…,56:…,57:…}` bytes identical; the single `print('PASS: …')` literal identical; all 20 non-receipt assertion/`req(` lines identical (multiset compare). Diff hunks touch only the helper insertion and the receipt-line replacement.
5. **Self-test exit 0 from lane root — PASS.** `python3 -B corpus/verify_named_multi_icon_states.py --self-test` with cwd=lane root: exit 0, `PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size)…`.

### corpus/verify_icon_states.py — HOLDS

Working-tree diff vs 55bcb6e: 16 added / 4 removed, all receipt-scoped.

1. **Frozen conjunct byte-preserved, exactly once — PASS.** Claims froze `receipt['fixture_sha256'] == expected_hash`. It sits inside `receipt_ok` (line 120: `assert receipt['exit_code'] == 0 and receipt['fixture_sha256'] == expected_hash`) byte-identical to baseline; occurrence count in the final file: 1 (baseline: 1); probe regex `receipt\['fixture_sha256'\]\s*==\s*expected_hash` (measure.py:120) hits exactly one site.
2. **Every pre-existing receipt conjunct survives — PASS.** All four baseline receipt lines are byte-preserved inside `receipt_ok` (lines 119–123): exit_code + fixture_sha256 (120); `receipt.get('stdout_sha256', receipt.get('raw_output_sha256')) == sha(raw_bytes)` (121); the `round_id != 36` evidence-ID exemption (122, exactly 1 occurrence, as frozen) with `assert receipt['evidence_id'] == evidence_id` (123); check_saved calls `receipt_ok(receipt, expected_hash, evidence_id, raw_bytes, round_id)` (line 150) with the closure values in the helper's parameter order.
3. **Exactly one new forged-receipt control — PASS.** Lines 151–158: deepcopy, `forged['fixture_sha256'] = '0'*64` (the frozen forge field), `try: receipt_ok(forged, …) / except AssertionError: pass / else: raise AssertionError(f'r{round_id}: forged receipt accepted')` — one control site (runs once per round 36–39); rejection required, message contains `forged receipt`; baseline had zero such strings.
4. **No saved-input assertion / EXPECT / PASS change — PASS.** `EXPECTED = {…}` dict bytes identical (855 == 855); PASS print literal identical (`4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED`); all 27 non-receipt assertion lines identical; the pre-existing main() forged-candidate control is untouched.
5. **Self-test exit 0 from lane root — PASS.** `python3 -B corpus/verify_icon_states.py --self-test` with cwd=lane root: exit 0, PASS line as above.

## Mutant smoke (reviewer replication of frozen mutate_c3; scratch `/tmp/revenger-r63-review-c3-mutant`, removed after)

On a scratch copy of the working corpus, applying the frozen probe's exact `mutate_c3` (same clause regexes, same deletion order, measure.py:117–127):

- named: control exit 0; mutant compiles, exits 1, last line `AssertionError: r55: forged receipt accepted` → **attributed kill** (clause sits at head of the return chain; probe deletes `receipt['command']==command and ` via its second pattern).
- icon_states: control exit 0; mutant compiles, exits 1, last line `AssertionError: r36: forged receipt accepted` → **attributed kill** (clause sits at tail of the first assert; probe deletes ` and receipt['fixture_sha256'] == expected_hash` via its first pattern).

This replicates, but is not a substitute for, the frozen counter's own `C3_RECEIPT_KILLED_ATTRIBUTED` run on a committed archive (L1/falsify-wave owns that receipt).

## Notes (non-defects)

- Named PASS count rises 139→142 (+1 `req` per round for the mandated control). The PASS literal is unchanged; the increment is inherent to the frozen fix shape ("add one in-script control … require rejection").
- The icon control's `except AssertionError` catches only assertion-type rejections; a non-assertion error inside `receipt_ok(forged, …)` would crash uncaught (non-zero exit but unattributed). Unreachable in practice: `forged` is a deepcopy of an already-validated receipt, so no key can go missing. No action.
- Each control is one site executed once per round (3× / 4×) — consistent with the frozen "one in-script control per script".
- Ten-verifier census unchanged: no corpus files added/removed (`git status --porcelain`: only the two C3 files modified, plus untracked `.ufo/waves/round-63/`).

## Residual risk and verification gaps

- Both patches are uncommitted working-tree state; L1 reviews/commits. Byte evidence here is against the current frozen bytes (icon owner confirmed final).
- The frozen `measure.py` end-to-end (`C3_CONTROLS_PASS`, `C3_RECEIPT_KILLED_ATTRIBUTED 2/2`) on a committed `git archive` tree was not run by this reviewer — that is the falsify-wave/admission step; my smoke used the identical mutation logic on a scratch copy.
- Verification method note: caller/definition checks here are byte/text-level (git show + programmatic compares); no LSP server was consulted for these two scripts (none required — the affected surface is fully contained in the diffs shown).
