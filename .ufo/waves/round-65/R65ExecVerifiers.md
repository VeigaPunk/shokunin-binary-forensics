PASS — all ten corpus verifier self-tests pass; calibration holds 4/4 and replay holds 10/10.

## Census C — current tree

Ran SCORECARD.md §C verbatim (lines 32–43) from `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Every verifier exited 0; exact last lines:

| Script | Exit | Last output line |
|---|---:|---|
| `verify_evm_evidence.py` | 0 | `NEGATIVE REJECTED candidate destination mismatch` |
| `verify_icon_languages.py` | 0 | `PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED` |
| `verify_icon_states.py` | 0 | `PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED` |
| `verify_js_graph_delta.py` | 0 | `NEGATIVE REJECTED saved graph disagrees with source truth` |
| `verify_multi_icon_states.py` | 0 | `PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED` |
| `verify_named_multi_icon_states.py` | 0 | `PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.` |
| `verify_pe_resources.py` | 0 | `NEGATIVE REJECTED payload relation mismatch` |
| `verify_saved_evidence.py` | 0 | `NEGATIVE JS REJECTED: JS: wrong package-main mapping` |
| `verify_semantic_trace.py` | 0 | `NEGATIVE REJECTED relation differs from source parent` |
| `verify_shape_evidence.py` | 0 | `NEGATIVE REJECTED changed-property evidence mismatch` |

Exact census summary: `CALIBRATION 4 / 4 score= 10.0`; `REPLAY 10 / 10`. The four calibration scripts are the SCORECARD C set (`verify_icon_states.py`, `verify_multi_icon_states.py`, `verify_icon_languages.py`, `verify_named_multi_icon_states.py`). Negative fixture lines above are expected self-test outcomes, not test failures.

## Frozen committed-tree counter

The measured revision was `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` (`git rev-parse HEAD`; no staged or unstaged tracked paths printed). Following `claims.md` lines 99–100, archived `corpus` from that commit into `/tmp/r65execverifiers.Aqf9nO`, then ran from `/`:

```sh
TMPDIR=/tmp/r65execverifiers.Aqf9nO python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-65/measure.py /tmp/r65execverifiers.Aqf9nO
```

Observed output: `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`, `HOLDS_OK_V2=yes`, `HOLDS_OK_V3=yes`, exit 0. The same run reports `C5_CONTROL_PRESENT=2/2`, `C5_CONTROLS_PASS=2/2`, `C5_RECEIPT_KILLED=2/2`, and `C5_RECEIPT_EVIDENCE_KILLED_ATTRIBUTED=2/2`. Mutant evidence: language script control exit 0, C5 mutant exit 1 with last line `AssertionError: r47: forged receipt evidence accepted`; multi-icon script control exit 0, C5 mutant exit 1 with last line `AssertionError: r42: forged receipt evidence accepted`. The registered window check also reports `STRICT_REJECT_WINDOW_SELFTEST=pass old_window_miss=True`.

C1 was not admitted in this measured revision: output remains `K_HELD=8/14`, `K_ROW C05 status=frontier`, matching the expected pre-adjudication state.

## C5 patch scope

The frozen claim names the two expected controls (`claims.md:33–48`); the counter enumerates exactly those two in `measure.py:259–263`. A read-only diff of `3eebcdd7ee7eb130b730a17fde1a0e40786c0f2f..8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0` over `corpus/verify_*.py` returned exactly:

- `corpus/verify_icon_languages.py`
- `corpus/verify_multi_icon_states.py`

The control insertions are at `verify_icon_languages.py:155–157` and `verify_multi_icon_states.py:154–156`, immediately after the forged-stdout checks. A search for the attribution marker across `corpus/verify_*.py` found only those two scripts. File SHA-256: language `64dc17ded0e32805c7a546e29e9f1e84dff30a68cb56df2c7d422c625bfbd93b`; multi-icon `320bf24ce25c01abce4732f02e97954c9596c690807fbc48e03194c957055818`.

## Risk / blocker

No blocker observed for this verifier assignment. The checks establish self-test/replay behavior and the frozen counter's registered mutation attribution only; they do not establish broader producer/runtime validity.