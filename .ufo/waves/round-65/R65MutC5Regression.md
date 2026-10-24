PASS — foreign-real and fabricated evidence IDs are both rejected by pristine `receipt_ok`; the frozen conjunct-deletion mutant accepts both and is killed with the exact attribution marker on both scripts; scratch bytes restored to lane hashes.

# R65MutC5Regression — second C5 mutant path (foreign-real + fabricated evidence id)

Seat scope: read-only mutation probe. No lane file edited; single write is this report.
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin` @ HEAD `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` (target scripts clean in `git status --porcelain`).
Scratch: `/tmp/r65-c5reg-k97jtvzg` (master copy + per-variant copies; restored, see §5).

## 1. Transplant direction verified independently (not trusted from the authored literal)

Driver imported both modules and compared each authored control literal against the OTHER module's `EXPECTED` evidence id, rather than asserting the claims.md text.

| receiving script | control site | authored literal | other script's real id | match |
|---|---|---|---|---|
| `corpus/verify_multi_icon_states.py` | line 155 | `ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421` | `verify_icon_languages.py:108` (`EXPECTED[47]`) | True |
| `corpus/verify_icon_languages.py` | line 156 | `ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d` | `verify_multi_icon_states.py:108` (`EXPECTED[42]`) | True |

Probe output (`python3 -B probe.py master/corpus`):
```
[verify_multi_icon_states.py r42] authored_control_literal_is_foreign_real=True
  foreign_real=ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421
  authored_literal=ev_8ed889836291b900a28c7e3816167392cc5042301e069cb2a647b6a98e8d4421
[verify_icon_languages.py r47] authored_control_literal_is_foreign_real=True
  foreign_real=ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d
  authored_literal=ev_6e055332b6fc4cb1a047db769eb5896c73aff9d1ce1bad18105e6559b152dc3d
```
Cross-count (`grep -c`): `ev_6e05…` occurs 1× per script (own real id at multi:108, control at languages:156); `ev_8ed8…` 1× per script (own real id at languages:108, control at multi:155). Each transplanted value is therefore foreign to the receiving script's own `EXPECTED` set. `grep -rn deadbeef corpus/*.py` → no matches (the fabricated id is nowhere in the corpus).

Detector surface: `receipt_ok` at `verify_icon_languages.py:118-120` and `verify_multi_icon_states.py:121-123`; control require at `:157` / `:156` respectively, message `forged receipt evidence accepted`.

## 2. Run 1 — foreign real id (`ev_8ed8…` into multi, `ev_6e05…` into languages)

Baseline receipt built exactly as `check()` does: round-42 (multi) / round-47 (languages) `producer-receipt.json`, expected hash and id from `EXPECTED`, command `npx -y rea-agents@6.4.0 inspect-pe-resources <HIST>/fixtures/pe-r<R>/fixture.exe --format json`, stdout bytes from `inspection.raw.json`.

| bytes | multi `receipt_ok(foreign)` | languages `receipt_ok(foreign)` | expected |
|---|---|---|---|
| pristine | `False` | `False` | rejected |
| mutant (§4) | `True` | `True` | accepted → mutant is caught by the control |
| restored | `False` | `False` | rejected |

## 3. Run 2 — fabricated ids (`ev_deadbeef`, and 64-hex `ev_deadbeefdeadbeef…`)

| bytes | multi short | multi 64-hex | languages short | languages 64-hex |
|---|---|---|---|---|
| pristine | `False` | `False` | `False` | `False` |
| mutant | `True` | `True` | `True` | `True` |
| restored | `False` | `False` | `False` | `False` |

`baseline_receipt_ok=True` in every table row's tree (the genuine receipt still passes), so the rejections/acceptions are attributable to the id field alone.

Pristine full runs (`python3 -B <script> --self-test`):
```
verify_icon_languages.py rc=0 last=PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
verify_multi_icon_states.py rc=0 last=PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
```

## 4. Frozen mutant — exact shape, isolated per script

Mutation applied with the contract's own regex `receipt\['evidence_id'\]\s*==\s*evidence_id` (identical to `reports/round-65/measure.py:261`), `clause_matches=1` per script, deleting `\s*and\s+receipt['evidence_id']==evidence_id`; `diff -u` shows exactly the one-conjunct removal and line join, nothing else. Mutant sha256:
```
90ad7fc6ea955626cc6c26883af71e6d76d1a98b3b898c234a857c8e7196c275  verify_icon_languages.py
876aef179d7d7a86642ea8296fc185c0ddf2cbf8d145a5482265c9dfaed168f0  verify_multi_icon_states.py
```
Isolated runs (one mutant per tree; sibling left pristine as the determinism control):

| tree | script | rc | last line | ends `forged receipt evidence accepted` |
|---|---|---|---|---|
| mut_lang | `verify_icon_languages.py` (mutant) | 1 | `AssertionError: r47: forged receipt evidence accepted` | True |
| mut_lang | `verify_multi_icon_states.py` (unmutated) | 0 | `PASS: 4/4 …` | False |
| mut_multi | `verify_multi_icon_states.py` (mutant) | 1 | `AssertionError: r42: forged receipt evidence accepted` | True |
| mut_multi | `verify_icon_languages.py` (unmutated) | 0 | `PASS: 3/3 …` | False |

Verdict: **killed and attributed 2/2** under the frozen rule (non-zero exit ∧ last line ends with the marker). The unmutated sibling in each tree still exits 0, so the kill is caused by the deleted conjunct, not by the copy or the driver.

## 5. Restoration evidence

All scratch copies rebuilt from `master`; every copy now hashes equal to the lane bytes:

```
64dc17ded0e32805c7a546e29e9f1e84dff30a68cb56df2c7d422c625bfbd93b  {master,work,mut_lang,mut_multi,restored}/corpus/verify_icon_languages.py
320bf24ce25c01abce4732f02e97954c9596c690807fbc48e03194c957055818  {master,work,mut_lang,mut_multi,restored}/corpus/verify_multi_icon_states.py
```
Lane files re-hashed unchanged:
```
64dc17de…bfbd93b  /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_icon_languages.py
320bf24c…055818  /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_multi_icon_states.py
```
Restored bytes re-run: probe → foreign/fabricated `False`, `baseline_receipt_ok=True`; both self-tests `rc=0`. `git status --porcelain` before and after the probe showed only two sibling seat reports (untracked), no `corpus/` change.

## 6. Coverage observations (non-blocking; no contract change proposed)

1. The authored control covers only the **foreign-real** class. The fabricated class (`ev_deadbeef`, non-existent id) is not asserted by any landed control, yet it is accepted identically by the frozen mutant (`receipt_ok=True`, §3) — both classes die to the same deleted conjunct today, so C2 is not weakened. It becomes a coverage hole only if a future mutant switches the id guard to a weaker predicate (e.g. regex/prefix or membership in a registry) that a real foreign id could satisfy differently from a fabricated one.
2. `receipt_ok` performs no format validation of `evidence_id` (equality only); the control's rejection is therefore purely the conjunct under test. Any future hardening that adds shape validation would need the control to keep the foreign-real value (both classes must still be `not receipt_ok`).
3. The scripts ignore `sys.argv` — the counter's `--self-test` argument is inert, so `main()`/controls run unconditionally. A future `argparse` gate could silently skip the controls; not a defect at this revision.

Tooling: no installs, no pacman/jj/git mutations. Only writes were `/tmp/r65-c5reg-k97jtvzg/**` (scratch) and this report.
