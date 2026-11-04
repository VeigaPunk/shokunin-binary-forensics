# ReviewerR91C2 — C2 attack report (round 91, attempt 1)

Target: `reports/round-91/message_tree_check.py` (commit-message↔tree
conformance) as scored by frozen `reports/round-91/cap_probe.py`. Method:
pre-registered falsification set (8 fixture cases on a protocol-compliant
throwaway repo + 5 sampled real commits hand-counted against frozen
claims.md §C2), run against the instrument's committed bytes. Full table,
commands, and raw outputs: `.ufo/waves/round-91/w1/ReviewerR91C2/receipt.md`
(expectations frozen pre-run in `expected-pre-registered.md`).

**C2_DISAGREE=6/13** (1 of 8 fixture cases + 5 of 5 real commits). Every
disagreement names its input and the instrument's exact output in the receipt.

## Findings by severity

**H1 — The frozen C2 predicate cannot be met by a spec-faithful instrument;
CAP_MESSAGE_TREE=pass is a false green as a claim-level result.**
claims.md §C2 scopes extraction to "every backticked repo-relative path and
every `.log` filename". Measured over the declared receipt range
`7fab03f..refs/heads/main`: 0 backtick characters in all 23 messages
(10,369 bytes, independently re-grepped) and exactly 8 `.log` tokens —
spec-faithful `cited` ceiling = 8, but frozen probe leg 4 requires
`cited ≥ 20`. The landed instrument resolves the tension by declaring (its
docstring) and implementing whole-message token extraction, where backticks
are mere delimiters. The probe cannot detect the swap: its owntest/planted-miss
fixtures cite backticked tokens, where both semantics coincide, and leg 4 only
checks thresholds. My own run: `CAP_MESSAGE_TREE=pass`, exit 0, with
`commits=23 cited=25 misses=9` — a pass that by construction certifies the
deviating contract, not the frozen one. Evidence: case (a) — a plain-prose
`missing/case-a.txt` with no backticks: spec-faithful count is 0 citations;
instrument prints `cited=1 misses=1 missing=missing/case-a.txt`, exit 1.

**H2 — The real-range conformance signal is false-positive-dominated: all 9
reported misses are non-defects.** The instrument exits 1 on the lane's own
history with `misses=9` over 6 commits. All nine name files that are not
actually absent: 8 exist in the citing commit's own tree under several
directories and are flagged only because bare-name suffix resolution requires
a *unique* match (claims.md ×30 — flagged on b13aac7, the very commit that
creates reports/round-91/claims.md; truth.json ×53; LEDGER.md ×72;
inspection.json ×31; receipt.json ×21; c1-only.log ×11; noharm-diff.txt ×13;
w1-results.json ×4); 1 (ufo-wave-policy.json in d509e98) is a fleet-root
orchestration file with 0 in-lane hits, reached only because prose tokens are
extracted. The capability's headline quantity — "how many commits cite paths
their tree does not carry" — is currently measuring ambiguity and cross-repo
prose, not the lane's commit-hygiene defect class C2 is meant to operationalize.

**M1 — Uniqueness-gated bare-suffix resolution turns existing files into
misses.** Any bare filename with ≥2 same-named in-tree files (up to 72
observed) is a guaranteed `missing=`. The frozen output grammar has no
`ambiguous` state (only `missing`/`bare`), so fixing this needs a contract
change, not a tweak. R2/R3/R4 are direct instances.

**M2 — Prose extraction contradicts the frozen spec sentence while satisfying
the frozen threshold.** Declared in the instrument's docstring, undeclared in
claims.md. Case (a) and R1 are the cleanly isolating instances (over-extraction
that also manufactures a miss); R3/R5 show cited-composition inflation even
when the outcome (miss count) happens to agree.

**INFO — What is sound (and honestly earned):** planted-miss kill, clean-range
clearance, own-tree basis pinned from both sides across a rename (cases f1/f2:
pre-rename hit, post-rename old-name miss), merge commits processed (case h),
`path:line` anchors, leading `./`, comma-in-token, directory citations,
command/flag exclusion (case g), per-commit dedupe, usage exit 2, honest
selftest (`MSG_TREE_SELFTEST=pass` exit 0). The instrument is a real,
working measure of a broader contract — not a stub; probe legs 1–3 are
genuinely passed, not gamed.

## Worst blind spot

Probe leg 4's `cited ≥ 20` threshold. It is unsatisfiable under the frozen
extraction spec on this history (ceiling 8, measured), so it structurally
forces and then rewards the extraction-scope swap, and no leg of the frozen
counter can distinguish a spec-faithful instrument (leg-4 fail) from the
landed token-based one (leg-4 pass).

## Does a blind spot make CAP_MESSAGE_TREE=pass a false green?

Yes, as a claim-level result. The probe's pass is honestly earned against the
probe's four legs, but the legs under-determine the frozen contract: legs 1–3
cannot see extraction scope, and leg 4 is only reachable *by* deviating from
it. Additionally the real-range number the capability lands on (misses=9,
exit 1) is 9/9 non-defects (H2). Recommended adjudication reading: C2's
capability exists and operates, but the round should record it as acquired
under a declared-deviation (token-based) contract with the spec-vs-threshold
inconsistency and the suffix-uniqueness false-positive class named — or as
not-verified-as-specified. Claims.md is frozen; the inconsistency is between
two frozen artefacts (spec sentence vs leg-4 threshold), not an
implementation bug alone. My verdict is a recommendation; adjudication is
Main's.

## Residual risk and verification gaps

- Hand-count rows use lenient suffix resolution (file exists ⇒ not a miss);
  under the instrument's strict-unique reading the spec-faithful miss count on
  the 5 samples would be 2 (45b2713's c1-only.log, noharm-diff.txt), not 0 —
  still files present in-tree; the over-extraction findings are independent of
  this reading. Disclosed, not hidden.
- The declared range is moving (21 commits at freeze, 23 now). Ceiling 8 and
  misses 9/9-non-defects are measured at d509e98; future landing commits could
  change both. The spec-vs-threshold inconsistency stands as measured today.
- I did not fuzz tokenization beyond the declared case set (e.g. unicode,
  very long tokens) and did not audit `--range` forms beyond `A..B` and `..B`;
  both are outside the frozen contract's words.
- Executor's "(f) post-rename hit" observation was not reproducible here
  because my F2 fixture cites both old and new names (old ⇒ miss, correctly);
  fixture difference, not a dispute.

## Tooling

No tools installed or upgraded (operator authorization noted; pacman pause
respected). Fixture and analysis scripts ran under
`/fast/scratch/hyaku/revenger-r91/ReviewerR91C2/` — removed before this
report; all evidence cited above is preserved in this directory.
