# R67ReviewSkillRefresh — SHONEN box-1 evidence refresh on the CURRENT SKILL.md bytes

**Verdict: `[x]-ready YES`** — on the committed working bytes `SKILL.md` sha256
`d6e0798d9642a0fce847da3e2cfaaed6eddd4d7c188b53a69a2a38f20c00a5cf` (580 lines; the
round-66 refresh plus this round's `## Gate registry` row). Two non-blocking
refinements are listed at the end; neither misstates capability nor breaks a command.
The `[x]` flip itself stays a non-lane duty — this report only records lane evidence.

Reviewer: `revenger-r67.R67ReviewSkillRefresh` (reviewer seat; did not draft the bytes).
Prior signed state for comparison: `R64ReviewSkill` passed sha
`bfd92057e71541cc1d93a9812cb350d69fcb5524df57b24153364d6c11b0a9dd` (39098 bytes)
at round 64; the brief's `260ab2b4…` figure does not match the r64 report's recorded
hash — the r64 receipt itself (`bfd92057…`) is the baseline used here.
`SHONEN.md:5-6` currently reads `- [x] SKILL.md contains real decision tables, error
patterns, checklists, cited sources`; box text unchanged.

## Evidence — what was re-verified on THESE bytes

### §1 decision table (verifier credit table) — all four rows byte-checked, not just two

| row | claimed range | actual bytes |
|---|---|---|
| `verify_icon_languages.py` conjuncts | `:118-120` | :118 `def receipt_ok(receipt,command,expected_hash,evidence_id,raw_bytes):`, :119-120 the five-clause return — exact |
| forged controls | `:149-151` command / `:152-154` stdout / `:155-157` evidence / `:158-160` exit / `:161-163` fixture | each range opens `forged*=copy.deepcopy(receipt)` and closes `require(not receipt_ok(...), f'r{r}: forged receipt <field> accepted')`; the five `require` lines sit at :151/:154/:157/:160/:163 — exact, including the two round-66 C6-appended controls (exit, fixture) at the tail |
| `verify_multi_icon_states.py` conjuncts | `:121-123` | :121 `def receipt_ok(...)`, :122-123 the same five-clause return — exact |
| forged controls | `:148-150` command / `:151-153` stdout / `:154-156` evidence / `:157-159` exit / `:160-162` fixture | `require` lines at :150/:153/:156/:159/:162 — exact |
| `verify_icon_states.py` conjuncts | `:119-123` incl. "skipped when `round_id==36`" | :119 `def receipt_ok(receipt, expected_hash, evidence_id, raw_bytes, round_id):`, :120-121 exit/fixture/stdout asserts, :122-123 `if round_id != 36:` + evidence assert — exact |
| forged fixture control | `:151-158` → `forged receipt accepted` | :151-158 the try/except block closing `raise AssertionError(f'r{round_id}: forged receipt accepted')` — exact |
| `verify_named_multi_icon_states.py` conjuncts | `:16-17` incl. `duration_seconds` numeric `>=0` | :16 `def receipt_ok(receipt, command, digest, eid, raw):`, :17 single-line return with `isinstance(receipt['duration_seconds'],(float,int)) and receipt['duration_seconds']>=0` — exact |
| forged command control | `:76-78` → `forged receipt accepted` | :76-78 `forged=copy.deepcopy…` → `req(not receipt_ok(...), f'r{r}: forged receipt accepted')` — exact |

### §2 decision table (fixture authoring) — anchors spot-verified

`corpus/fixtures/firmware-r63/generator.py`: :17 `IMAGE_SIZE = 2048` (declare block
17-35), :39 `def decode_member` → :49 `return member_size, content`, :52
`def derive_regions` → :101 `return regions`, :113 `image = bytes(image)` in main
(build span 104-113), :131 `ZLIB_RUNTIME_VERSION`, :133 `platform.python_version()`,
:149-150 `IMAGE_PATH.write_bytes` / `TRUTH_PATH.write_text`. `apk-r65/generator.py`:
:197 `APK_PATH.write_bytes(apk)`, :226 `TRUTH_PATH.write_text(...)`. All land on the
claimed statements.

### §3 decision table (SOURCES tiers) — consistent with the contract it restates

Fleet contract `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`
exists; its lines 67-80 are byte-identical to the seven-command census block quoted in
both SKILL §6.2 and the checklists-half §4b. Tier rules (A sole-support-able inside
scope, B never sole, C never) match `corpus/SOURCES.md` restatement and Q01.

### §4 error patterns M33–M41 — nine rows, every named check exists

M33 (Q05+Q06+§2 pre-probe; `round-63.md:218`), M34 (non-author Q decisions +
`K_HELD_BACKED_STRICT` + committed-archive counting; `round-63.md:219`,
`reports/round-64/claims.md` §Counting), M35 (§1 credit rule + attributed-endswith;
`round-63.md:220`, `claims.md` §C2), M36 (`README_TOKEN_LEGEND_MISMATCH` vs frozen
ROW_OPS; `reports/round-64/claims.md` + `measure-before.log`), M37 (whole-file scan +
`STRICT_REJECT_WINDOW_SELFTEST`; `reports/round-65/claims.md`, `round-65.md:30`),
M38 (§2 byte-verify; `round-65.md:29`, `.ufo/waves/round-65/m38-red-before.log` — file
exists, 3498 bytes), M39 (Q11 verbatim check; `corpus/lessons/round-66.md:52` is the
M39 row, `.ufo/waves/round-65/R65ReviewEntryQ11.md` exists), M40 (located-quote rule +
SOURCES rule 2; `round-66.md:53` M40 row, S043/S044 registered), M41 (report-vs-spec
reconciliation; `round-66.md:54` M41 row). `corpus/lessons/round-66.md:48` is `##
Mistakes`; all cited pointers resolve.

### `## Gate registry` row vs `corpus/check_embedded_outputs.py` — matches on every field

Script sha256 `19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d`,
committed in `7668510`, working tree clean.

- name/kind/owner: `check_embedded_outputs`, gate (outside `verify_*` family), owner
  revenger — matches docstring :2-9 and `MARKER` :32.
- entry command: `python3 -B corpus/check_embedded_outputs.py --entry <knowledge.md>`
  cwd=lane root — matches `main()` :148-158 (`--entry` parses at :151).
- verdict map 0/1/2: exits at :155 (`0 if not problems else 1`) and :153
  (`could-not-evaluate … sys.exit(2)`); self-test `sys.exit(0)` :146 — exact.
- self-test spelling `--self-test`, hermetic `TemporaryDirectory(prefix="rev-r67-c7-
  selftest-")` :145; forged control `require(not ok(dproblems), MARKER)` :141 with
  marker `drifted entry output accepted` :32 — **executed**: `--self-test` printed
  `SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired`,
  exit 0.
- pinned-value path: sha256 `cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a`
  — **verified** against `corpus/knowledge/round-65-apk-axml-byte-evidence.md`
  (actual sha256 identical); entry:41 still carries the 15-byte drifted hex
  `4d616e696673742d56657273696f6e`. **Executed**:
  `--entry` over that file → `drift entry:41 embedded output line not in recheck
  stdout: {"cd_index": 2, … "payload_first16_hex": "4d616e696673742d…" …}`,
  `checked_blocks=15 problems=1`, exit 1 — exactly the pinned verdict.
- measured-against: `reports/round-67/measure.py` sha256
  `7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e` — actual file
  hashes identical.
- write scope "argv list, no shell": `subprocess.run([sys.executable, "-B", *argv[1:]], …)`
  :74 — argv list, no `shell=True`, confirmed.
- family note: `check_embedded_outputs.py` does **not** match the `verify_*.py` glob;
  the glob enumerates exactly 10 scripts (evm, icon_languages, icon_states,
  js_graph_delta, multi_icon_states, named_multi_icon_states, pe_resources,
  saved_evidence, semantic_trace, shape_evidence) — `HOLD_REPLAY=10/10` denominator
  untouched, consistent with claims.md §C2.

### §7 cited sources — existence sweep clean

43 paths tested (`test -e` loop): all knowledge entries incl.
`round-67-apk-axml-byte-evidence.md` (candidate) and the retained rejected r65 entry;
all lessons r1/r61/r62/r63/r65/r66; fixtures `firmware-r63/{generator.py,truth.json}`,
`apk-r65/{generator.py,truth.json,readout.py}`, `REPLAY.md`; `corpus/{README,QUALITY,
SOURCES}.md`; `SCORECARD.md`, `SHONEN.md`, `PROVINCE.md`; `reports/round-{64,65,66,67}/
{claims.md,measure.py,measure-before.log}`; `.ufo/waves/round-67/source-snapshots/
dex-format.html`; `corpus/check_embedded_outputs.py`; fleet contract + census script.
**Zero missing.** S-ids cited (S005,S006,S007,S009,S010,S014,S015,S032–S035,S038,
S041–S045) all exist in `corpus/SOURCES.md`; S045 row at :59 is `docs|A|mined` with the
snapshot sha `c0428612…f4` embedded. Census row count now **45** (44 + S045) — §6.2
commands unchanged. Counter sha256 claims in §7 verified: r64 `b8e68d32…9168`, r65
`8a2c69c4…0304`, r66 `a59914e9…f1da`, r67 `7933c060…c07e` — all four actual files
match. Red-before receipt claims verified against `reports/round-67/measure-before.log`:
`K_HELD=8/14`, `C7_GATE_PRESENT=no`, `C7_SELFTEST=n/a`, `C7_CONTROL_PASS=0/1`,
`C7_MUTANT_KILLED_ATTRIBUTED=0/1`, `C7_RED_ON_R65_CANDIDATE=no`, `HOLDS_OK_V5=no`.

## Non-blocking refinements (record, do not block)

1. Registry write-scope row says "`python3` first token only"; the actual allowlist at
   `check_embedded_outputs.py:72` is `("python3", "python", sys.executable)` — the gate
   also accepts `python` and the absolute interpreter path as first token. Direction of
   error is over-restrictive description, not a missing guard; tightening the wording
   to "a Python interpreter first token" would be byte-accurate.
2. §4 M39 row still parenthesizes "R65ReviewEntryQ02's proposed verbatim-diff gate is
   routed debt" — the debt is now discharged by the C2 gate registered two sections
   below; the named check itself (Q11 verbatim) is still real, so this is stale
   cross-referencing, not a false check.

## Residual risk

- §1 "unguarded" verdicts for `verify_icon_states.py` (exit/stdout/evidence) and
  `verify_named_multi_icon_states.py` (five clauses) remain source-reading judgments;
  the M35 debt stands until controls exist — unchanged by this refresh, correctly
  still stated as unguarded.
- The header `verified-at` (2026-10-24) describes the r66-era provenance split; the new
  registry section's own pins (r67 counter sha, r65-candidate sha) are byte-verified
  here, so the staleness is descriptive only.

## Verification gaps

- No `lsp` device is mounted (`xd://lsp` → "No such tool … mounted: ast_edit, debug");
  caller/definition checks used line-range reads, numbered greps and executions — no
  semantic cross-reference was available. This is a prose+script artifact, so the
  deficit is bounded.
- I did not run the mutant half of C7 (deleting the `drift(...)` call) — that is the
  mutation-tester seats' surface; I verified the *control wiring* exists at :141 and
  fires `MARKER`.
- No tools installed or updated this seat.

Report: .ufo/waves/round-67/R67ReviewSkillRefresh.md
