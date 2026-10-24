# Round 64 — historical PASS-count non-reproduction receipt

Seat: R64ScoutHistory. Date: 2026-10-24.

Axes: current-output reproducibility; precise historical attribution; preservation of frozen evidence.

## Observed historical quotations

Literal search with the repository search tool (pattern `139`, case-sensitive, `gitignore=false`) over both `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-58/` and `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-59/` found:

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-58/reviewer.md:13`:

  ```text
  PASS: 139 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
  ```

  The historical command is at lines 7–10; line 14 records `exit_code=0`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-58/LEDGER.md:4` repeats that same `139 positive checks` result.
- No literal `139` match was found in the round-59 tree. A separate round-59 search for `139|142|verify_named_multi_icon_states|verify_icon_states` also returned no matches. Thus the routed “r58/59 139→142” wording must not be presented as proof that both reviewer files contain that quote. `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/live/runs/round-59/reviewer.md:17-38` records direct byte/UTF-16/resource checks, not that PASS-count summary. The separate devin-author ledger at line 36 reports `22 positive checks`, not 139.

## Fresh commands and exact stdout

Both explicitly assigned commands were run once, concurrently, with working directory `/`. Both Bash tool invocations completed successfully. The commands did not themselves print numeric exit-code lines.

```sh
python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_named_multi_icon_states.py --self-test
```

```text
PASS: 142 positive checks; 2/2 forged claims rejected (r56 candidate, r57 size). Limits: authored r55-r57 fixtures, not general PE validation.
```

```sh
python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_icon_states.py --self-test
```

```text
PASS: 4/4 source-decoded states, 3/3 one-byte deltas, one forged candidate REJECTED
```

**Observed conclusion:** the round-58 `139 positive checks` quotation is not reproduced by the current named-multi verifier: it now reports 142, a difference of three. The icon-state verifier prints state/delta counts, not a 142-positive-check summary; its observed output must not be relabeled as 142.

## Accounting evidence and inference

Literal source observations:

- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_named_multi_icon_states.py:10-14` increments `N` for each `req` call. Lines 76–78 contain the forged-command receipt rejection `req`; line 62 lists rounds 55, 56 and 57, and line 84 invokes `check` for each. Line 105 prints `N`.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/verify_icon_states.py:151-158` contains its forged fixture-hash receipt rejection. Its summary at line 178 remains the fixed 4/4-state, 3/3-delta text.
- `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure.py:168-171` explicitly identifies these two scripts as the C3 calibration hold.
- The already-saved red-before receipt `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/measure-before.log:22-27` records the same 142/state-summary control outputs with control exits 0 and C3 attributed kills 2/2. This is a citation of saved evidence, not a newly run mutation probe.

[INFERENCE] One additional named-multi `req` for each of three fixtures accounts for the +3 and is consistent with the registered C3 receipt controls. No historical script revision was executed or compared, so this is not an independently reconstructed historical patch diff.

Semantic tooling was unavailable: `read xd://lsp` returned `No such tool: xd://lsp. Mounted devices: ast_edit, debug.` No server request or cold-indexing result was available. The source observations above are literal-text evidence, not LSP definition/reference proof.

## Preservation, scope and remaining unknowns

`/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-64/claims.md:115-122` makes changed historical corpus/live or fixture bytes outside new round-64 paths a void condition. Lines 147–150 explicitly require these quotations to stay unedited, put the non-reproduction in the round-64 lesson, and assign re-derived counts to the next round touching those verifiers. Correct handling is this additive receipt, not rewriting old observations to match current software.

No historical file, verifier, fixture, registry, Git/JJ state or index was edited by this seat; no Git/JJ command, producer rerun or fixture execution was performed. Only the two assigned receipt/report paths were written. No installation, update or scratch artifact was needed.

Confidence: high for located quotations, absence of literal 139 in the searched round-59 tree, and fresh stdout; medium for historical causal attribution. Remaining unknown: the precise historical edit lineage, and which artifact the routed round-59 wording originally intended. Neither gap prevents recording the observed non-reproduction.
