PASS — SCORECARD census C completed; probe exit 0, ten verifier exits recorded, and all four calibration scripts exit 0.

Axes: census completion; calibration replay; probe/constituent exit separation.

Evidence

- Contract read first: `reports/round-65/claims.md` (full frozen admission order and criteria; lines 110–123). Census command and its non-propagating child-exit reporting are in `SCORECARD.md:32–42`.
- Ran from `/home/vgpnk/Projects/shokunin/revenger-shokunin` the SCORECARD C command verbatim (`python3 -B -c '…'` from `SCORECARD.md:35–42`), then recorded its shell status as `CENSUS_PROBE_EXIT`.
- Actual output:

```text
verify_evm_evidence.py exit=0 NEGATIVE REJECTED candidate destination mismatch
verify_icon_languages.py exit=0 PASS: 3/3 group-language states, 2/2 exact one-byte deltas, two icon candidates retained, forged selection REJECTED
verify_icon_states.py exit=0 PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
verify_js_graph_delta.py exit=0 NEGATIVE REJECTED saved graph disagrees with source truth
verify_multi_icon_states.py exit=0 PASS: 4/4 two-image states, 3/3 exact one-byte deltas, first link stable, forged second match REJECTED
verify_named_multi_icon_states.py exit=0 PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
verify_pe_resources.py exit=0 NEGATIVE REJECTED payload relation mismatch
verify_saved_evidence.py exit=0 NEGATIVE JS REJECTED: JS: wrong package-main mapping
verify_semantic_trace.py exit=0 NEGATIVE REJECTED relation differs from source parent
verify_shape_evidence.py exit=0 NEGATIVE REJECTED changed-property evidence mismatch
CALIBRATION 4 / 4 score= 10.0
REPLAY 10 / 10
CENSUS_PROBE_EXIT=0
```

The observed child exit codes are all zero. `NEGATIVE REJECTED` lines are verifier output for rejected negative cases, not nonzero process exits. The census command prints child return codes and counts successful returns; it does not set its own status from a child return code (`SCORECARD.md:37–42`).

Blockers/risks: none observed. No tools installed or updated.