# Round 79 claims — frozen before any after-run

Date 2026-11-01. Base `c205ef83ca3fa8e0c0e20488625d232cc3efc4c7` (r78 tip + non-author
spot-check, pushed). Two claims, distinct axes (coverage, calibration), causally
separable, neither exploratory. Instruments sha-pinned below; red-befores committed in
the same freeze. Kill rules are execute-as-frozen: a falsified claim keeps its evidence
bytes and takes no repair-and-revote in this round.

## §7 fresh-start duty (r71/r72/r73 rejected closures re-read and spot-checked)

All three rejected closures are the same class: K-admission claims (C05 sixth pass r71;
C15 tool landscape r72; C10 ledger-discipline entry r73) whose verdicts needed the wave
Q-review surface. On this host that surface does not exist (no `.ufo/state/` dispatcher,
no seat spawn; `/home/vgpnk` gone) and the r74 L0 asking for it stands unanswered
(re-checked in the fleet `.ufo/l0-questions.md` this round) — a do-nothing control
reaches the identical state, so none is declared. Their spot-checks:
r71 C05 falsified at Q09/Q16, C05 still `uncovered` (K 8/15 in every later counter); r72
C15 falsified / not admitted, candidate retained (K 8/15); r73 C1 unresolved, C10
disposed `rejected` by the frozen r74 kill rule (r74 SCORECARD + r74 spot-check).

Ruled out this round, and why (fresh probes, 2026-11-01):

- **F android** — `REA_JADX_MCP_JAR` UNSET, no jadx on PATH, no `~/tools/jadx*`; the
  committed r77 gate receipt (S448) stands. Hard-gated; a do-nothing control reaches the
  identical state.
- **A macho/signature F-family route** — `rea capabilities` 2026-11-01:
  `inspect_macho`/`inspect_signature`/`inspect_plist`/`list_architectures` are
  `available: false`, `availability_code: unsupported_host` ("Native macOS utilities
  require macOS"). Not manufacturable on this host.
- **K admissions (C05/C10/C15)** — the wave Q-review surface is absent; the r74 L0
  stands unanswered (re-checked this round).
- **Criterion C repair** (the two failing replay verifiers, `r47: artifact` /
  `r55 artifact`) — repair means re-authoring the r47/r55–r57 old-host fixture chains;
  §9 sizing keeps it routed (unchanged from r78's ruling).
- **Census literal form** — operator-side; the consolidation L0 line naming the whole
  r74–r79 lineage landed this round (carry-in item 1); the sanctioned explicit-lane-dir
  form stays documented at SKILL.md §4a and is re-run at round start and end.

## r78 carry-in dispositions (addressed first, all status-neutral)

1. **Census literal-form host defect (r74–r78 lineage)** — both census forms re-run at
   round start (literal exit 2, sanctioned exit 0; receipts in the round report); the
   sanctioned form stays documented (SKILL.md §4a, already current for 2026-11-01); the
   requested L0 consolidation line naming the whole lineage landed in the fleet
   `.ufo/l0-questions.md` this round.
2. **Both new gates expose no self-test mode (routed debt)** — the "add" branch is
   executed: superseding instrument revisions v2 with §Gate-standard self-test modes
   (claim C2's substance). The "pin" branch would have re-recorded the debt per gate;
   supersession closes it instead.
3. **Criterion-instrument class question and criterion C repair** — both stay routed,
   re-pinned in `corpus/lessons/round-79.md` §Routed forward; no exemption claimed.

## C1 — coverage: a real producer record on a ninth F family (`native-authenticode`)

Falsifiable move: the frozen 8-family F mapping cannot see the
`inspect_pe_certificates` surface at all (its operation is in no family set); r79
registers the F2 mapping revision adding `native-authenticode:
{inspect_pe_certificates}` and lands one real producer record on an authored inert
native PE32 certificate-table fixture.

- Instrument (new, frozen): `reports/round-79/f_probe2.py` sha256
  `0be0d8b5ac131963f273e296c6c2822d277614d634db25b559256f4744e4cc12` — the eight
  round-1 families and predicate byte-equal to the frozen `reports/round-76/f_probe.py`
  (sha256 `e15a43af56f453479681b49e063741bb008245ed758af7fc2d685aa5e64f39ed`,
  unchanged), plus the one mapping entry; outputs renamed `F2_*`.
- Counting commands:
  - before (base archive `c205ef83`): `PYTHONUTF8=1 python -B reports/round-76/f_probe.py <base>/corpus`
    → `F_COVERAGE=7/8 score=8.75`; `PYTHONUTF8=1 python -B reports/round-79/f_probe2.py <base>/corpus`
    → `F2_COVERAGE=7/9 score=7.78` (native-authenticode absent). Receipt:
    `reports/round-79/f2-before.log`.
  - after (landing archive): same two commands → `F2_COVERAGE=8/9 score=8.89` with
    `native-authenticode` in `F2_FAMILIES`; v1 `F_COVERAGE=7/8` unchanged on the frozen
    eight (denominator disclosure, no v1 predicate change). Receipt:
    `reports/round-79/f2-after.log`.
- Fixture discipline (Q06): `corpus/fixtures/native-auth-r79/generator.py` builds a
  minimal native PE32 with one 8-aligned WIN_CERTIFICATE entry (PKCS#7 ContentInfo,
  structurally valid DER, cryptographically meaningless by construction — the producer
  declares it never verifies signatures/chains/digests); its self-check re-derives every
  premise from the built bytes before writing; `truth.json` pins byte-derived values;
  `oracle_check.py` compares the saved record against them. Regen byte-identical
  (`cmp` receipt). The scratch pre-probe that informed the expectations is captured in
  `reports/round-79/preprobe-cert-shape.log` (committed at freeze, before the run).
- Record discipline: one bounded static run
  `PYTHONUTF8=1 rea inspect-pe-certificates <lane>/corpus/fixtures/native-auth-r79/fixture.dll --format json`
  (rea 6.8.0, built-in provider `rea-pe-certificates`), exact stdout saved as
  `corpus/live/runs/round-79/inspection.json` with a `receipt.json` (command, exit,
  stdout sha256, fixture sha256) and `LEDGER.md` (observation/inference/unknown split).
- **C1 verifies iff**: (a) the saved record carries `evidence_id` and
  `normalized_result` with `operation == "inspect_pe_certificates"`; (b)
  `oracle_check.py` over the committed fixture, truth and record prints `ORACLE OK`
  with every check passing; (c) the committed fixture regenerates byte-identically and
  its sha256 equals the record's `subject.digest.sha256`; (d) the after counting
  commands print the stated values. **Kill rule**: any oracle mismatch, missing record
  field or regen drift → C1 falsified; the fixture and record stay as evidence; F2
  prints 7/9 on the final tree and the SCORECARD records the falsification.
- Grounding: the producer record (SOURCES row landed with the work) and the producer's
  declared capability surface (`rea capabilities` / `--llms`, SOURCES row landed with
  the work). §9: a do-nothing control cannot reach a new-family producer record — the
  fixture, the run and the mapping revision are all round work.

## C2 — calibration: §Gate-standard self-test modes for the two registered gates

Falsifiable move: the r78 registration recorded, honestly, that neither
`receipt_probe` (criterion R) nor `gate_probe` (criterion G) exposes the §Gate-standard
self-test mode (S452, the fleet PROTOCOL §Gate standard §Self-test clause: isolated
fixtures, asserting both the exit code and a stable expected finding-id, expected
values committed) nor a declared usage exit — both silently accept any argv and run
live legs. Superseding revisions v2 close the debt; v1 bytes stay frozen and their
registry rows stand.

- Instruments (new, frozen):
  - `reports/round-79/gate_probe2.sh` sha256
    `e2b71649faf34000ec0c2a777c07cf75dac1c92ca89561158093b73aa14caead` (plain mode
    value lines byte-identical to v1 `reports/round-77/gate_probe.sh` sha256
    `a594b57f58bcc5f401242d71a9ef50b14489b1dab142191bb8b96ec06c3ae84a`);
  - `reports/round-79/receipt_probe2.sh` sha256
    `076cdb67a4bb1dc5a5586cb23fd45d580703369a11b5baabc8e5ef12df2289d9` (plain mode
    byte-identical to v1 `reports/round-76/receipt_probe.sh` sha256
    `9315f8d8a2440feaca9d943b95b3eb7247a4635c0e113ee6c4101799d4bd5a11`);
  - counting instrument `reports/round-79/selftest_probe.sh` sha256
    `4126af12767d1968be1cd344c5795a3cb4c2f6cbc9f11e35556ebd6fb6722e1e`.
- Expected finding-ids (committed expectation, independent of the recomputation —
  also pinned in the SKILL.md registry rows landed with the work):
  - gate `--selftest`: `GATE_SELFTEST_COMPARATOR_EQUAL=ok`,
    `GATE_SELFTEST_COMPARATOR_MUTANT_FLAGGED=ok`,
    `GATE_SELFTEST_COMPARATOR_FIELD_MISSING_FLAGGED=ok`, last line
    `GATE_SELFTEST=pass`, exit 0.
  - receipt `--selftest`: `RECEIPT_SELFTEST_LLMS_VERDICT=ok`,
    `RECEIPT_SELFTEST_TOKEN_CHECK=ok`, `RECEIPT_SELFTEST_NEGCTL_LOGIC=ok`, last line
    `RECEIPT_SELFTEST=pass`, exit 0.
  - unrecognized form: usage line on stderr, exit 64.
- Frozen sed mutants (embedded verbatim in `selftest_probe.sh`; each mutant must be
  byte-different from its source and die with the attributed marker as the last line,
  exit 1):
  - gate: `s/sys.exit(0 if key(sys.argv\[1\]) == key(sys.argv\[2\]) else 1)/sys.exit(0)/`
    → `selftest: blind comparator accepted mutated receipt`
  - receipt: `s|^llms_ok() {.*|llms_ok() { return 0; }|` →
    `selftest: per-leg receipt verdict accepted any count`
- Counting command (same instrument both ends; the argument selects the revision):
  `bash reports/round-79/selftest_probe.sh <gate-script> <receipt-script>`
  - before (v1 pair, worktree bytes blob-identical to base — verified by the no-harm
    diff at adjudication): `SELFTEST_MODE_PRESENT=0/2`,
    `SELFTEST_MUTANT_KILLED_ATTRIBUTED=0/2`, `USAGE_EXIT64=0/2`, exit 1. Receipt:
    `reports/round-79/selftest-before.log`.
  - after (v2 pair): `SELFTEST_MODE_PRESENT=2/2`,
    `SELFTEST_MUTANT_KILLED_ATTRIBUTED=2/2`, `USAGE_EXIT64=2/2`, exit 0. Receipt:
    `reports/round-79/selftest-after.log`.
- Plain-mode no-drift receipt: `diff` of v1 vs v2 plain runs on the lane tree → empty
  twice, `GATE2_PLAIN_BYTES_EQUAL=yes` / `RECEIPT2_PLAIN_BYTES_EQUAL=yes`
  (`reports/round-79/plain-equal.log`). The criterion G/R verdict bytes do not move.
- **C2 verifies iff**: the after counters are full, the before counters are the red
  values above, both mutants are killed with the attributed last lines, usage exits 64
  on both, and the plain-mode diffs are empty. **Kill rule**: any short counter,
  unattributed kill (exit 1 with the wrong last line), plain-mode drift, or a
  selftest that needs the producer (PATH-strip leg fails) → C2 falsified; v1 stays the
  criterion instrument and the debt is re-recorded per gate.
- Grounding: S452 (fleet PROTOCOL §Gate standard, §Self-test + §Verdict clauses at the
  pinned r78 checkout, opened this round). §9: a do-nothing control leaves the routed
  debt standing (the r78 rows record it as not-satisfied); the v2 revisions, their
  hermetic fixtures and the attributed kills are round work.

## Boundary (honest)

- C1's score move is numerator+denominator together (7/8→7/9 before, 8/9 after): the
  mapping revision is registered at freeze and would LOWER the score to 7.78 had the
  record not landed — the moved quantity is the new in-province family with a real,
  oracle-checked record, not the 8.89 print. Android stays hard-gated (7→8 on the
  frozen eight is unreachable this round).
- C2 moves no criterion score (G 10.0, R 10.0 held over identical verdict bytes); the
  moved quantity is the closed routed debt (self-test clause + declared usage exit),
  with the kills attributed.
- v1 criterion instruments (f_probe, P2/P3, receipt/gate v1, r71 counter) stay
  byte-identical; the no-harm diff at adjudication proves it.

## Separability (to be receipted at adjudication)

- C1-only tree: base archive + fixture/record (no v2 scripts, no registry rows) →
  f_probe2 prints 8/9; selftest probe over the v1 pair stays red.
- C2-only tree: base archive + v2 scripts (no fixture, no record) → selftest probe
  2/2 ×3, exit 0; f_probe2 over that tree prints 7/9.
