# C2 forged-receipt control safety review

## Finding — Medium: receipt-command mutation currently survives each verifier

- **Exploit path:** delete the command-equality conjunct (mutant b); forge only a receipt's `command` in memory; the verifier's existing unrelated forged-selection control still passes and the script exits successfully.
- **Evidence:** `reports/round-61/claims.md:42-54` records the surviving mutant and required control. `corpus/verify_icon_languages.py:143-145` and `corpus/verify_multi_icon_states.py:142-144` check saved receipt command, but their current `main()` controls at `verify_icon_languages.py:156-163` and `verify_multi_icon_states.py:155-163` forge only semantic selection fields. `.ufo/waves/kaika-r1/mutation-post.md:15,21,29-36` records mutant b exiting 0 in both.
- **Impact:** the verifier does not self-detect loss of this receipt-identity assertion; calibration claim C2 is not satisfied unless both scripts detect the forged command.
- **Smallest remediation:** for each script, exercise its actual receipt-validation path with an in-memory copy of a valid loaded receipt whose command alone is changed. Treat acceptance as a hard assertion failure.

## Final-diff rejection criteria for the integrator

1. **Mutation-sensitive control:** the forged copy must pass through the same production validation path as the saved receipt. Reject a duplicate, test-only command comparison: deleting the one production command conjunct must make the script exit nonzero because the forged receipt is then accepted. There must be exactly one `receipt['command']==<expr>` conjunct in each file, as required by `claims.md:50-55`.
2. **Preserve the saved object:** copy the JSON-loaded receipt (deep copy is already imported in both scripts at line 5), alter only the copy's top-level `command`, and leave the original saved receipt object untouched for its normal validation/use. Do not alter saved records or fixtures.
3. **Narrow expected rejection:** catch only the expected `AssertionError`, and only around the production validator call for the forged copy; if that call returns, raise an `AssertionError` outside the `try`. Reject `except Exception`, a `try` covering `main()`/the whole run, or any handler that suppresses ordinary verifier failures.
4. **No side effects:** the control must be purely in-memory. Reject writes, temp files, subprocesses, network/client calls, package invocation, or any other external mutation/access added for this test.
5. **HIST is identity text only:** use `str(hist)` only to construct/compare the expected command. Reject `.exists()`, `stat`, opening, resolving through the filesystem, or otherwise conditioning the control on whether the historical path exists. Existing comments state that HIST is for saved-path/receipt identity only: both scripts line 9; path construction is at `verify_icon_languages.py:121` and `verify_multi_icon_states.py:124`.
6. **Normal run remains authoritative:** the control must run during each script's ordinary invocation (or an explicitly supported self-test invocation), while the original receipt and all existing checks still fail normally on real errors. No broad exception or altered fixture/receipt contents may turn a failure into a pass.

No source files changed. No checks or probes run; this is a read-only review of the preregistration and current verifier code.

VERDICT: Require the six diff checks above in both verifiers; current code has the documented calibration blind spot.
Installs: none.
