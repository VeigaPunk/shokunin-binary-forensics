# ExecControlsR99 — findings (round 99, wave w1)

Seat: C1 control recipe and skip-work table. No landing tree built or scored. The control trees
carry no round-99 votes and the entry stays `candidate`, so no counter ran on a C14-held landing tree.

## Files written (repo)

- `reports/round-99/controls/make_c1_controls_r99.sh` (new, shellcheck-clean, chmod +x)
- `reports/round-99/controls/skip-work-table-r99.md` (new)
- receipts: `.ufo/waves/round-99/w1/ExecControlsR99/{accept,final,dryruns,c2routes,plumbing}/`

## Amendment A

L1 instruction mid-wave: build from `61e27feb4e8099af7f9bf41fbf69e223354f691e`, with the revision as
a script argument defaulting to it. Verified before editing: `git diff 7e6edd4d… 61e27feb… -- corpus/README.md`
is empty and the entry digest is unchanged.

Script signature: `make_c1_controls_r99.sh <counter> <work> [freeze-rev] [landing-rev]`. The optional
landing-diag tree is built but never scored by the script.

## Script behaviour

From the freeze rev it builds:
- `<work>/do-nothing/`: git archive, unchanged.
- `<work>/junk-row/`: identical, except `corpus/README.md` C14 status cell `partial -> held`. The script
  asserts the inter-tree diff is exactly that cell; observed: `exactly one changed cell (README line 61, C14 partial -> held)`.

It then runs `python3 -B <counter> --profile c14r99 --tree <tree> --work <work>/counter-run` on both,
writes full stdout plus `# rc=<n>` to `<work>/do-nothing.log` and `<work>/junk-row.log`, and prints
`C1_CONTROL_DONOTHING=<verdict>` and `C1_CONTROL_JUNKROW=<verdict>`.

Exit 0 iff both verdicts are `fail` (control-ok). Exit 1 on a passing or missing verdict
(control-BROKEN). Exit 2 on usage error. TMPDIR and HYAKU_SCRATCH are routed under `<work>`. The lane
checkout is only read.

## Acceptance (met, against the final v8 bytes)

Final WIP v8 `reports/round-99/c1_k_admit_counter8.py`, sha256
`620dfca9959572449638cab203485555c5d45f5a8e89c5b68121ffc2d3023581`. The author's last message
announced this as final, superseding `c7a9a2c2…`.

```
$ make_c1_controls_r99.sh reports/round-99/c1_k_admit_counter8.py <work>
C1_CONTROL_DONOTHING=fail        # counter rc=1
C1_CONTROL_JUNKROW=fail          # counter rc=1
control-ok (do-nothing rc=1, junk-row rc=1; both refused)   # script rc=0
do-nothing.log: C1_VERDICT=fail  # rc=1
junk-row.log:   C1_VERDICT=fail  # rc=1
junk-row.log:   C1_K_HELD_BACKED=pass  (14/15)
$ v8 --self-test   -> SELFTEST_C1V8=OK legs=98   (rc=0)
```

- do-nothing: 9 failing legs, including `C1_TARGET_CITES`, `C1_ADMITTED`, `C1_VOTES`, `C1_VOTES_GLOB`,
  `C1_K_HELD_BACKED`. K reads 13/15.
- junk-row: K passes at 14/15 and several other legs refuse. This is the designed demonstration that K
  alone is not a backstop against a bare row flip.
- The counter printed digest `36cc6ac2cd37d6866fe4ce0ad06c20d67d19fd2c7f0da08a2b63d277b948fce5` on both
  trees, independently re-deriving the frozen vote-binding digest.

Earlier WIP attempts, recorded for the audit trail:
- `c14r99` not yet accepted by argparse: counter rc=2 -> verdict `missing` -> script rc=1 (control-BROKEN),
  the designed missing-verdict path.
- Mid-wave bytes `c7a9a2c2…`: both controls `fail`, script rc=0. Superseded by the final bytes above.

## Skip-work dry-runs (observed rc; WHY strings in the skip-work table)

Seven C1 routes and four C2 routes were dry-run on scratch copies. Every route is refused by a named
leg or rule.

- Flip README only: refused by `C1_TARGET_CITES`, `C1_ADMITTED`, `C1_VOTES`. `C1_K_HELD_BACKED` alone would pass.
- Flip header only: inert. The failing-leg set is identical to the untouched baseline (v7-c14).
- Reuse round-98 votes: `vote digest mismatch for CriticR98 digest=36cc6ac2…` (v7-c14).
- Votes with re-pointed digest: `vote CriticR98 decision Q11='FAIL' not PASS/n-a` (v7-c14).
- Votes without matching artifacts: `artifact does not name the candidate digest` (v7-c14). The
  missing-file and sha-mismatch checks are code-named and were not reached in-run.
- PASS note copied between voters: `PASS note shared verbatim` on both voters (v7-c14).
- S506 receipt date drift: `C1_RECEIPTS` and `C1_VERIFIED_AT` both fire (v7-c14).
- Stub counter (forge_reach7): always-pass gives `C2_ACCEPTED=5/5`, not-met; always-fail gives `C2_POSITIVE=fail`.
- Builder edit (FR09 mutator no-op'd in a scratch harness copy): `VECTOR FR09 verdict=pass`,
  `C2_ACCEPTED=1/5`, `C2_STUB_SELFTEST=fail` (delta_applied), not-met.
- Dropped vector (FR10 removed in a scratch harness copy): `C2_ACCEPTED=0/4`, `C2_STUB_SELFTEST=fail`, not-met.
- Control-BROKEN run: `C2_POSITIVE=fail`, `C2_POSITIVE2=fail`, not-met (forge_reach7).

`forge_reach8` was not run by this seat; its 12-vector runs belong to ExecHarness8 and the L1.

## Tooling

No tools installed or upgraded. `shellcheck` was present at `/usr/bin/shellcheck` and reports the
script clean.

## Risks and open questions

- `C1_K_HELD_BACKED` passes on the junk-row tree. The control's refusal depends on
  `C1_TARGET_CITES`, `C1_ADMITTED` and `C1_VOTES*`. If a future landing tree satisfies those, K alone
  does not block a bare row flip.
- `C1_ONLY_TARGET` fails on any tree whose target row is byte-identical to base, including do-nothing.
  That is expected by construction.
- The control trees are built from the freeze rev and carry no round-99 votes. The L1 should score the
  landing tree only after the v8 freeze, as the claims ordering requires.
