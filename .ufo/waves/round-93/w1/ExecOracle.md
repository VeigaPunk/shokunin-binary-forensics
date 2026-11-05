# ExecOracle — round 93, wave 1 — independent re-derivation (C1 support)

Lane HEAD = freeze commit `02050cb2a6758e3bd9cec696ff0e42df6f23511a`. Only my wave dir is written; the lane shows no other change (`git status`: `?? .ufo/waves/round-93/`). No installs. No mutating git. Scratch removed.

## Results

| Check | Result |
|---|---|
| Oracle re-run (`oracle-rerun.log`) | `ORACLE OK (17/17 checks)`, exit 0. Record sha256 `b045a4ee…e868`; `index.html` `46e51761…deb45` (316 B); `app.js` `fb079fa2…aa593` (101 B) |
| Independent derivations (`derivations.txt`) | 18 commands, all exit 0. Every LEDGER identity fact re-derived from raw record JSON and fixture bytes |
| LEDGER cross-check (`ledger-check.tsv`) | 26 rows: **25 yes, 1 NO** (LC26) |
| Draft embedded commands (`embedded-recheck.tsv`) | Draft located at READY digest `921563694da4…1a73d`; 9 command blocks, **9 yes, 0 no**, all exit 0. Wait: READY at check 15, no timeout |
| K arithmetic (`k-arithmetic.txt`) | 15 rows; 9 held at base (C01 C03 C04 C06 C07 C09 C11 C12 C13); C08 `uncovered`; flip → **10/15**. Worktree `corpus/README.md` byte-equal to freeze blob. Entry absent at freeze and now (pre-landing, expected) |

## Defects

**D1 (blocks C1_EMBEDDED as drafted): the frozen checker cannot evaluate the draft.**
`corpus/check_embedded_outputs.py --entry …/entry-draft.md` → `could-not-evaluate: no $ cmd blocks or unsupported command`, exit 2 (`checker-on-draft.log`). The checker only parses fences whose first line starts with `$ `; the draft has **zero** such lines (`grep '^\$ '` → no matches). The counter's `C1_EMBEDDED` leg requires exit 0, so it fails.

**D2 (blocks C1_EMBEDDED even with `$` prefixes added): `python3 -B -c` is refused.**
Seven of the nine draft commands are `python3 -B -c '…'`. The checker's confinement refuses `-c` (its self-test asserts `not confined(["python3","-c",…])`), and any refused command makes the whole entry could-not-evaluate. The fix is a committed file-based command (a script under `corpus/`), not a prefix change. This is for the scribe/L1 to route; I did not edit the draft.

**D3 (frozen counter gap, not a draft defect): `C1_EMBED_NONVACUOUS` passes vacuously on an entry with no `$` fences.**
The non-vacuity guard inspects only blocks whose first line starts with `$`. An entry that omits the prefix is never checked by it. In this draft, `C1_EMBEDDED` still kills the entry through D1, so the verdict is unaffected today. Reported only; the counter is frozen.

**D4 (LEDGER overstatement, minor, auxiliary): `list_browser_targets` "(exit 0)" is not in the committed bytes.**
LEDGER says discovery ran `(exit 0)`. `receipt.json` records `exit_code: 0` for the `inspect-web-page` leg only; the target-listing leg has `target_listing_stdout_sha256` and no exit-code field. Unsupported from committed bytes (LC26). The stdout hash itself re-derives (`6954848b…bbb8`).

## Notes (verified, no defect)

- `ORACLE OK (17/17)` re-derived by my own driver, not by reusing `oracle_check.py`: fixture hashes, operation/provider, `ev_<64hex>` shape, url/origin (== `run_pin`), title `r77 probe page [loaded]` (static `<title>` + the inline script's `" [loaded]"` literal), 2 scripts (101 / 46 B), `cdp_hash` == sha256 of `app.js` bytes and of the inline text, one resource (101 B, `text/javascript`, reconciliation `exact`).
- Inline script reconciliation is `unmatched` (`no_exact_sanitized_url`); the LEDGER claims exact only for `app.js`, and the record agrees.
- `completeness.conditions` = `attach_limited, policy_filtered`; both `source.included` = false, consistent with the LEDGER's "source text not retained".
- `list_browser_targets` appears in no family set of the frozen `reports/round-81/f_probe4.py`; `inspect_web_page` is in `browser-runtime`.
- Frozen `reports/round-93/` and `reports/round-92/` untouched.

## Commands the main agent should re-run

- `python3 -B .ufo/waves/round-93/w1/ExecOracle/drive_derivations.py` (run from the lane root; regenerates the three tables)
- `python3 -B corpus/check_embedded_outputs.py --entry <landed entry>` once the draft is reformatted (expect exit 0 only after D1/D2 are fixed)

## Files (all under `.ufo/waves/round-93/w1/ExecOracle/`)

`oracle-rerun.log`, `derivations.txt`, `ledger-check.tsv`, `k-arithmetic.txt`, `embedded-recheck.tsv`, `embedded-recheck-meta.tsv`, `embedded-recheck-mismatches.txt` (absent: zero mismatches), `checker-on-draft.log`, `drive_derivations.py`, `recheck_draft.py`.

## Blockers

None for my assignment. D1/D2 mean the current draft would fail C1_EMBEDDED at landing; C1 verdict is not established by this seat.
