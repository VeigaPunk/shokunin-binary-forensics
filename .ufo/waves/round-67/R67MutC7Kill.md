# R67MutC7Kill — C2/C7 embedded-output gate mutant probe

FAIL — the frozen C7 mutant is killed (exit 1) but **unattributed**: last line is
`self-test: drifted entry not caught`, never the `drifted entry output accepted` marker
(measured `C7_MUTANT_KILLED_ATTRIBUTED=0/1` under measure.py's exact logic); the marker
control at `corpus/check_embedded_outputs.py:141` is structurally unreachable behind the
guard at `:131-134`, and two self-designed contract-defeating mutants survive the self-test.

- date: 2026-10-24 · seat: R67MutC7Kill (mutation-tester, round-67 v2 wave)
- probe under test: `/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/check_embedded_outputs.py`
  sha256 `19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d` (lane bytes, untouched)
- frozen contract: `/home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-67/claims.md`
  §C2 (`C7_MUTANT_KILLED_ATTRIBUTED=1/1` at :88, frozen mutant at :91-94)
- frozen counter: `reports/round-67/measure.py` sha256
  `7933c060db4d9b8db889830e2e0b6e1da1724d94854201aac9552e2a49cbc07e` (matches the pin)
- scratch tree: `/tmp/revenger-r67-mut-R67MutC7Kill` (full `cp -a` of `corpus/`, 501 files;
  lane tree never mutated)

## 1. Frozen mutant — applied exactly as pre-registered

Pristine clause match count was verified before mutation (must be exactly once):

```
$ python3 -B -c 're.findall(r"problems \+= drift\(lines, stdout_set, lineno\)", src)'
matches: 1
at 3576 line 101 'problems += drift(lines, stdout_set, lineno)'
```

Applied in the temp copy with `python re.sub(pat, "problems += []  # mutant: verbatim
comparison removed", src, count=1)` (`assert n == 1`):

```
$ cd /tmp/revenger-r67-mut-R67MutC7Kill
$ python3 -B corpus/check_embedded_outputs.py --self-test
self-test: drifted entry not caught
EXIT=1
LAST_LINE= 'self-test: drifted entry not caught'
ENDS_WITH_MARKER= False
mutated_sha256= 6335c6dbfd8a0c743f27e7622991f60b91780a394376d7e02e7f592ee6e32851
```

| requested check | expected | observed |
|---|---|---|
| self-test exit non-zero | killed | **exit=1 → killed** |
| last line ends `drifted entry output accepted` | attributed | **no — ends `self-test: drifted entry not caught`** |

**Verdict: killed, UNATTRIBUTED.** Under `measure.py:408`
(`c7_mut_attributed += rc != 0 and last.endswith(C7_MARKER)`, with `last` = last non-empty
line of stdout+stderr per `measure.py:127-131`), the frozen mutant scores `0/1`, so the frozen
predicate at `claims.md:88` (`C7_MUTANT_KILLED_ATTRIBUTED=1/1`) is not reachable on the landed
bytes. This is a calibration finding on the gate, reported as-is; I did not edit the contract or
the probe.

### Why attribution fails (structural, not flaky)

`corpus/check_embedded_outputs.py`:

- `:131-134` — guard: `require(dproblems is not None and dchecked == 1 and dproblems and
  dproblems[0].startswith("drift entry:"), "self-test: drifted entry not caught")`
- `:141` — forged control: `require(not ok(dproblems), MARKER)`

The control fires only when `ok(dproblems)` is true, i.e. `dproblems` **empty**; the guard at
`:131-134` already exits whenever `dproblems` is empty. The two conditions are mutually
exclusive, so `MARKER` (`:32`) cannot be printed on the landed bytes. Any mutant that empties
`dproblems` dies at `:134` with an unattributed message.

Diagnostic proof (temp copy; frozen mutant **plus** deletion of the `:131-134` guard only):

```
$ python3 -B corpus/check_embedded_outputs.py --self-test
drifted entry output accepted
EXIT=1
```

i.e. the marker is reachable only once the pre-guard is removed — it is dead code as landed.

## 2. Controls (pristine bytes, same detector)

```
$ python3 -B corpus/check_embedded_outputs.py --self-test
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
EXIT=0

$ python3 -B corpus/check_embedded_outputs.py --entry corpus/knowledge/round-65-apk-axml-byte-evidence.md
drift entry:41 embedded output line not in recheck stdout: {"cd_index": 2, "compressed_size": 69, "crc32": "e948d738", "crc32_matches": true, "crc32_recomputed": "e948d738", "fact": "member[META-INF/MANIFEST.MF]", "local_header_offset": 618, "payload_first16_hex": "4d616e696673742d56657273696f6e", "payload_offset": 668, "sha256": "2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49", "uncompressed_size": 69}
checked_blocks=15 problems=1
EXIT=1
```

Red-before on the retained r65 candidate holds exactly as claimed: exit 1, one problem, naming
`entry:41` (the 15-byte `4d616e696673742d…` transcription), 15/15 blocks checked.

## 3. Adversarial mutants (my design) — both SURVIVE

Fixture built in scratch only: `adv-two-line-drift.md` runs `python3 -B reader2.py` whose stdout
is two JSON lines; the block embeds line 1 correct and line 2 drifted (`"v": 9` vs `"v": 2`).
Pristine detector on it: `drift entry:4 … exit=1` (so the fixture is discriminating).

### Mutant A — `drift()` compares only the first embedded line

Candidate line `:81` (`for l, out_lineno in lines if l not in stdout_set]`) → `lines[:1]`.
sha256 `9c21e157f7059fbb81b78858fedbd9113e51a68294cce12c0df3b06fe079b0ec`.

```
--- A: self-test ---
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
EXIT=0
--- A: --entry adv-two-line-drift.md ---
checked_blocks=1 problems=0
EXIT=0
--- A: --entry r65 candidate ---
checked_blocks=15 problems=1   (exit=1)
```

**Verdict: SURVIVED** (self-test exit 0). It silently stops enforcing the docstring contract
("every following output line must appear verbatim", `:12-14`) for lines 2..N; the r65 red check
cannot discriminate it because that block is single-line.

### Mutant B — `evaluate()` skips blocks with >1 output line (phantom `checked`)

After the loop header at `:93`: `if len(lines) > 1: checked += 1; continue`.
sha256 `26aa63ef48309ec7a8246875062a1fc47dabb9555350b30d1e7aa7cbf04e6713`.

```
--- B: self-test ---
SELFTEST OK: clean exit 0, full-run exit 0, drifted caught, forged control fired
EXIT=0
--- B: --entry adv-two-line-drift.md ---
checked_blocks=1 problems=0
EXIT=0
```

**Verdict: SURVIVED** (self-test exit 0). Multi-output blocks are never evaluated yet are
counted as checked, so the self-test's only multi-line case (`full_entry`, all-correct,
`:126-127`) passes vacuously.

### Why both escape — coverage gap in the self-test

`_self_test` has exactly three drift-sensitive cases: clean (1 line), drifted (1 line, `:122-125`),
full-run (2 lines, all **correct**, `:126-127`). There is **no multi-line drifted case**, so the
self-test cannot distinguish per-line comparison (A) from first-line-only, nor block evaluation
(B) from block skipping. The frozen control at `:141` also cannot see them — it is dead code
(§1). An escaped mutant here is a coverage finding, not a licence to change the contract.

## 4. Restoration evidence

Every probe state was restored from the lane file and re-hashed:

| state | sha256 of `corpus/check_embedded_outputs.py` | self-test |
|---|---|---|
| lane (start and end) | `19007beb…e697d` | exit 0 |
| frozen mutant | `6335c6db…e32851` | exit 1, unattributed |
| mutant A | `9c21e157…b0ec` | exit 0 (survived) |
| mutant B | `26aa63ef…e6713` | exit 0 (survived) |
| scratch after restore | `19007beb…e697d` | `SELFTEST OK …` exit 0 |

Lane tree writes: **none**. Final lane hashes:
`corpus/check_embedded_outputs.py` = `19007bebeb4d60dafd826df108584933ebb3f2b1e6ab112925ea6c6cab3e697d`,
`corpus/knowledge/round-65-apk-axml-byte-evidence.md` =
`cf42cc2059e454027685a59a2a35a190f6ba981f95645f41e407c47c01c4d05a` (unchanged since round 65).
All mutation happened under `/tmp/revenger-r67-mut-R67MutC7Kill`; the only report-side write is
this file.

## 5. Consequence for the wave (finding, not a decision)

- `C7_MUTANT_KILLED=1/1` (detection exists) but `C7_MUTANT_KILLED_ATTRIBUTED=0/1`, simulated with
  byte-exact copies of `measure.py:127-131` and `:363-373` on the pristine scratch corpus:

  ```
  MUTANT check_embedded_outputs.py control exit=0 pass :: SELFTEST OK: ...
  MUTANT check_embedded_outputs.py c7 exit=1 killed :: self-test: drifted entry not caught
  C7_MUTANT_KILLED=1/1
  C7_MUTANT_KILLED_ATTRIBUTED=0/1
  ```

  Therefore the §C2 frozen predicate cannot reach `1/1` as landed; per `claims.md` the attributed
  calibration target (C7 1/1) is unmet → C2's fail branch applies unless the L1/adjudication
  rules otherwise. This is a calibration observation from the frozen mutant, not a contract edit.
- Attribution target is unsatisfiable **by construction** (`:131-134` vs `:141`), so it is not a
  flake: re-running the same probe on the same bytes cannot change the result.
- Self-test coverage gap (no multi-line drifted case) is the root cause for both escaped mutants;
  it is independent of the frozen mutant, so a repaired marker alone would not close it.

## 6. Tooling

No tool installed or updated (none needed): Python 3 stdlib only (`re`, `shutil`, `subprocess`,
`tempfile`); no pacman/uv/npm transaction. No network fetch was required for this seat.
