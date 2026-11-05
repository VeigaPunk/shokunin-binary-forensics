# MutationR98 — scoped findings (round 98, wave w1)

Role: mutation-tester (leaf seat). Axis: calibration. Milestone: port the mutation harness
to v7 and pre-register mutants for the eight new legs. Pre-registration:
`.ufo/waves/round-98/w1/MutationR98/preregistered.md` (written before the port first ran).

## Deliverables

- `reports/round-98/mutants/mutate7.py` (new; stdlib only; sha256
  `5f03c73ce8462f1302fb72a25a3401a5c69f076955fac1bf19713672847cf0a1`). Port of
  `reports/round-97/mutants/mutate.py` (read-only source, 372 ln) — same CLI
  (`--counter --out --kill-tree --selftest --label --jobs`) plus `--profile {c02|c14}`.
- Wave dir receipts: `v6r98-repro.out` / `.err` / `.rc` (full V6R98 detector run + exit
  code), `manifest-v6.json`, `v6-sites-table.out` (site-table-only run),
  `v7-dryrun-sites.out` (disclosed sites-only dry run on frozen v7),
  `iso-survivors/<mutant>/` (isolation self-test receipts for 3 of the 10 disputed
  mutants), `preregistered.md`.
- Tooling: nothing installed or upgraded (system `python3` only; git used read-only:
  `archive`, `log`, `show`, `rev-parse`).

## V6R98 reproduction on the frozen v6 counter (calibration of the port)

Counter `reports/round-97/c1_k_admit_counter6.py` sha256
`80c1f10b93ac9c3688c4dbd45286da7f08730b17b50930f5cb1d82dc4df3f2f4` (committed at the r97
v6 freeze `85a2c7e`, unchanged since — verified via `git log --follow`). Run:

    PYTHONUTF8=1 python3 -B reports/round-98/mutants/mutate7.py \
      --counter reports/round-97/c1_k_admit_counter6.py --out <scratch>/v6repro \
      --kill-tree <materialized git archive 7d380ce corpus reports .ufo> \
      --selftest --jobs 8 --label V6R98      # exit code 0

Against the recorded r97 run (`reports/round-97/controls/mutate-v6-kill.out`, label V6):

| metric | recorded (V6) | this run (V6R98) | verdict |
|---|---|---|---|
| site table (`MUTANT ` lines) | 140 | 140 | **byte-identical** (diff empty: names, classes, fns, lines, legs labels, edits) |
| `NO_SITE` / `EXCLUDED_MSG` | C1_TRIO; 7 (L345,L369,L429,L441,L460,L475,L501) | same | identical |
| `BASE_TREE` | rc=1 verdicts=22 | rc=1 verdicts=22 | identical |
| tree kills | `MUTANT_KILL_V6=107/140` | `MUTANT_KILL_V6R98=107/140` | identical; all 140 `KILL_TREE` lines byte-equal (diff empty) |
| `SURVIVORS_TREE` | 33 incl. `d-host` | same list | identical (d-host tree-survivor reproduced) |
| selftest kills | `MUTANT_SELFTEST_V6=137/140` | `MUTANT_SELFTEST_V6R98=127/140` | **10-kill difference, fully attributed below** |
| selftest survivors | m011, m029, m034 | m011, m029, m034 + 10 more | see below |

**The selftest difference is a recording artifact in the r97 control, not a port
difference.** Facts (all observed, quoted from both files):

- The recorded run has **91** `KILL_SELFTEST` lines with the crash signature
  `rc=1 killed=True timeout=False first=-` (process died with rc 1 and zero
  `SELFTEST FAIL:` lines — it never reached its own verdict print). The crash set is
  exactly the contiguous tail m049–m140 (except none survive there). This run has **0**
  such lines.
- The killed-set symmetric difference vs recorded is exactly 10 mutants:
  `d-host, m068-cmp-check_sources-L380, m070-cmp-check_sources-L384,
  m073-cmp-check_sources-L396, m090-if-check_embed_nonvacuous-L454,
  m115-if-evaluate-L538, m117-cmp-evaluate-L540, m130-if-evaluate-L587,
  m132-cmp-evaluate-L590, m133-cmp-evaluate-L590` — precisely mutants whose recorded
  kill was crash-only. 127 = 137 − 10.
- Isolation re-runs (fresh scratch, `--receipts-dir`) of three of them (d-host, m068,
  m115) all finish `rc=0`, zero `SELFTEST FAIL` lines, empty stderr, and every one of the
  33 EXPECT_FAIL deltas reports `decide=true` — the mutants genuinely pass v6's whole
  self-test battery. d-host surviving is the r96/r97 routed finding unchanged: V27
  (`fabricated-body-foreign-host`) still fails `C1_RECEIPTS`, via a non-host sub-check,
  so the allowlist removal is never the discriminator. m068/m070/m073/m090 and the five
  evaluate-internal mutants are **new real sub-check gaps of frozen v6** (coverage
  findings, not contract changes).
- Reading: the recorded 137/140 = 127 true delta kills + 10 crash-only kills; the
  recorded survivor list (3) understates v6's true selftest survivors (13). The spec's
  tree detector — 107/140 and the full survivor list — reproduces exactly.

Attribution note: v6 hard-codes a function→leg map; the port derives it (backward
data-flow from each `legs["L"] = ...` RHS through evaluate's bindings + call-graph
propagation + dict-key and evaluate-callsite rules). Verified lossless: the 140-line
site table is byte-identical, so the derivation reproduces the v6 map exactly. On v6 the
new operator classes find zero sites (no `C1_*`-keyed dicts, no new legs), so the
reproduction is within the same operator set, as required.

## Port on frozen v7 (disclosed dry run, sites only)

Frozen v7 `reports/round-98/c1_k_admit_counter7.py` sha256
`59c9930ae864ce826e9f468b4b76bdef33de7ae5e6760eda4d88db4eab2e8548` (committed at the v7
freeze `5d9b087` during this seat's window). Dry run (no detectors, no counter
execution — only the AST site pass and mutant-file writing):

    PYTHONUTF8=1 python3 -B reports/round-98/mutants/mutate7.py \
      --counter reports/round-98/c1_k_admit_counter7.py --out <scratch>/v7dry \
      --label V7R98-DRY                                     # exit code 0

- Anchors all match: LANE pin (`parents[2]`, L13), exactly one d-host pair
  (`if host not in HOST_ALLOWLIST:` + `:host` fails.append), `--profile` flag detected →
  detector runs will pass `--profile` to the counter; `SELFTEST_C1V7` regex matches.
- `MUTANTS_WRITTEN=249` = 233 carried-class + 16 new-class. `NO_SITE leg=C1_TRIO`;
  `EXCLUDED_MSG=7` (L356,L380,L440,L452,L471,L485,L511).
- All eight new legs bound (`NEWLEG` lines): every leg has `del-leg=1 drop-why=1`;
  `widen-re`: C1_HEADER_POSITION=2, C1_VOTE_NOTES=2, C1_QUOTE_BYTES=1,
  C1_USEDBY_GROUNDED=2 (one is the shared `parse_sources` helper), and **0** for
  C1_ROWSET (inline tuple comparison, no regex), C1_ENTRY_BYTES, C1_VERIFIED_AT,
  C1_OWNWORK_PATHS — those decide without `re.match` calls (disclosed limitation, as
  pre-registered). inv-cmp coverage for every new leg exists as the carried
  cmp/not/if mutants inside the leg-attributed check functions (e.g.
  `m107-cmp-check_entry_bytes-L534 legs=C1_ENTRY_BYTES`).
- Implementation deltas vs the pre-registration text (same semantics, v7's real
  structure): v7 stores the new legs as a checks-dict returned by `new_checks()`, so
  **del-leg** deletes the dict entry (leg never decided — the `C1_L` verdict line
  vanishes → tree-detector kill on any tree); **drop-why** resolves the generic
  `print(f"{name}_WHY={why}")` loop to the eight dict keys (one statement governs all
  eight legs — one mutant, legs=all eight; still the pre-registered expected survivor);
  **widen-re** widens any first-argument expression of `re.match/fullmatch/search`
  (v7 builds patterns by concatenation, e.g. `r"\b" + re.escape(sid) + r"\b"`).
- Disclosed denominator note: v7 renamed its self-test fixture builders
  (`edit_source_row`, `_new_delta`) and carries `configure(profile)`; v6 excluded the
  `_set_*`-era names, the port's prefix rules don't match the new names, so 21 sites are
  included and labeled `legs=UNATTRIBUTED` in the manifest (2 configure + 19
  fixture-side). Kept deliberately: configure is real counter behavior (profile gating);
  the fixture-side ones only inflate the denominator and are visible per-row. The L1 can
  read them off the manifest.

## Commands for the L1 (also sent inline)

    D=<scratch>/freeze9d49002a && mkdir -p "$D" && git -C <lane> archive --format=tar \
      9d49002a3804de48d365b7d32849ada06745d64f -- corpus reports .ufo | tar -x -C "$D"
    PYTHONUTF8=1 python3 -B reports/round-98/mutants/mutate7.py \
      --counter reports/round-98/c1_k_admit_counter7.py --out <scratch>/v7-c02 \
      --kill-tree "$D" --selftest --jobs 8 --label V7 --profile c02
    PYTHONUTF8=1 python3 -B reports/round-98/mutants/mutate7.py \
      --counter reports/round-98/c1_k_admit_counter7.py --out <scratch>/v7-c14 \
      --kill-tree "$D" --selftest --jobs 8 --label V7 --profile c14

Exit codes: 0 completed, 2 malformed anchor, 3 selftest baseline failed. The tree
detector kills on verdict-set or rc difference vs the unmutated run on the same tree
(timeout counts as killed; WHY-text-only changes are `message-only`, not kills).

## Open items for the L1

1. The 10-mutant selftest discrepancy vs the recorded r97 control is explained above; if
   the recorded control is ever re-run on a healthy-scratch host, expect 127/140 and the
   13-mutant survivor list, not 137/140 and 3.
2. Frozen v6 carries nine real selftest sub-check gaps (the 10 above minus d-host which
   was already routed; plus the tree-survivor set already recorded in r97). They are
   findings against v6, not v7; v7's new-leg deltas (seen in
   `controls/v7-dev/selftest-cases/`) are exactly the kind of per-leg discriminators
   that close this class.
3. drop-why mutants are pre-registered expected survivors on v7 (WHY text is not
   instrumented by either detector); do not read them as counter defects.

## Hygiene

No lane file edited outside my named artifacts (`reports/round-98/mutants/mutate7.py`,
wave dir). No counter was run on any landing tree or on any tree with C14 held (the v7
dry run executes no counter at all). Frozen bytes untouched (v6 counter sha verified
before and after). Scratch `/fast/scratch/hyaku/revenger-r98/MutationR98/` deleted after
receipts were copied. No git mutation; read-only git only. One incident ack sent to
ConnectorScope-23 (their kake-r97 scratch deletion could not touch my
`revenger-r98` scratch root).
