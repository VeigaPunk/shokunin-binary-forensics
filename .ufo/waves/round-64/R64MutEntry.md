# R64MutEntry — entry recheck mutation: C07 firmware byte-evidence derivation

Role: mutation-tester (attack seat). Round 64 / wave 1 seat `R64MutEntry`.
Scope of this report: mutate derived values the C07 entry claims, run the entry's
recheck on the mutated bytes, and record what the recheck catches and what it
does not (Q11 recheck-scope finding). No lane files were modified; all mutation
work happened in `/tmp/revenger-r64-mutentry-K9Q2` on copies.

## Dependency finding (recorded, does not block the probe)

`/tmp/revenger-r64-entry/candidate.md` **did not exist** at probe time
(01:18–01:21 host time; the directory then held `readout.py` 10018 bytes,
`all.txt` 6978 bytes, `err.txt` empty, and a `gen/` copy of the fixture
triple). The entry's candidate prose was therefore unavailable, so the recheck
was taken from the artifact that actually exists and that the entry will cite:
`/tmp/revenger-r64-entry/readout.py`, sha256
`2abe0c130ae29de27ae194511e3b4e5061364818cf94d8d8671c3019eafabae1`, together
with its canonical stdout `/tmp/revenger-r64-entry/all.txt`, sha256
`aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae`
(7 lines; `usage: readout.py <repo-root> [--fact <id>]`). The recheck command
extracted is therefore:

```
python3 -B readout.py <repo-root>
```

The prose-corruption probe (P5) uses a faithful simulation of the entry's
recorded `regions` fact because the candidate file itself was absent; that
limitation is stated with the result. This dependency is re-reported to L1 in
the final message, not routed as a blocker.

Baseline reproduction: running the same command on a byte-identical scratch
copy of `corpus/fixtures/firmware-r63/{firmware-r63.bin,truth.json,generator.py}`
and `corpus/live/runs/round-63/{inspection.json,LEDGER.md}`, cwd `/`, exits 0
and its 7 stdout lines are **byte-identical** to `all.txt`
(`cmp` clean; sha256 `aa3532…14ae`). Detector baseline is green; a later
failure is a mutant kill, not a baseline artifact.

Detector rules used (both are recorded because the entry must declare one):

- **R1 semantic** — a mutant is killed iff any printed `all_match` is `false`
  or a printed `derived`/`stated` check pair disagrees (the `oracle` and
  `record` facts emit their checks). The readout **always exits 0**
  (`main()` returns `None`, never `sys.exit(1)` for a mismatch); exit status is
  not a detector.
- **R2 pinned-stdout** — a mutant is killed iff the 7-line stdout SHA-256
  differs from the pinned `aa3532…14ae` (the round-63 entry form: "prints N
  stdout lines whose SHA-256 is …").

## Results

| Mutant | Corrupted value | Expected detector | Observed | R1 | R2 |
|---|---|---|---|---|---|
| M1 | `truth.json` → `regions[1].decompressed_member.sha256` last hex digit `6→7` (member at 512) | derived digest ≠ stated digest | exit 0; `oracle.all_match=false`; failing check `zlib@512.decompressed_sha256` (derived `a571…7b86`, stated `a571…7b87`) | **KILLED** | killed (stdout `fbec7cc62e3a…`) |
| M2 | fixture byte at offset 700 (`0x00→0x01`, inside padding span `[591,1024)`) | image digest + padding derivation ≠ oracle | exit 0; `oracle.all_match=false`, `record.all_match=false`; failing checks `image.sha256` (derived `602b7f43…d56d`), region re-derivation (`region_count 6`, padding split at 701), `subject.digest.sha256` | **KILLED** | killed (stdout `71c5bcc55a0f…`) |
| M3 | `truth.json` → `build_recipe.compression.level` `9→8` (recorded provenance the oracle states) | semantic check on the level | exit 0; `oracle.all_match=true`, `record.all_match=true`; **no check, no printed fact, and no `--fact` output mentions `compression.level`** | **SURVIVED** | change-only trip (stdout `3613bd960237…` differs only in the `digests` fact) — see hole H2 |
| M4 | `inspection.json` → `evidence_id` last hex digit `9→0` (recorded identity the entry cites) | derived Evidence-ID binding | exit 0; `oracle.all_match=true`, `record.all_match=true`; `evidence_id` occurs **0 times** in readout output | **SURVIVED** | change-only trip (stdout `40d823d6d56b…`, `digests` fact only) — hole H3 |
| P5 | entry prose: `regions` fact transcribed with `decompressed_sha256` `a571…7b86→a571…7b80` (simulated candidate block, `entry.md` sha256 `0a31dc83…2559`) | recheck compares entry text to derived bytes | readout exit 0; **stdout byte-identical to canon** (`aa3532…14ae`, `cmp` clean); the entry states `…7b80` while bytes give `…7b86` | **SURVIVED (blind)** | **SURVIVED** — identical stdout, pin matches |

Mutation/restoration hashes (each mutant made on its own copy; predecessor and
successor measured):

- M1 `corpus/fixtures/firmware-r63/truth.json`: before `9663f90b2b9f29c5…65e6`
  → mutated `ef236f32403801d9…4c2f8f` → restored `9663f90b2b9f29c5…65e6`
  (`restored_equal=true`)
- M2 `corpus/fixtures/firmware-r63/firmware-r63.bin`: before `bdfe9f46e8f21371…10be`
  → mutated `602b7f43156a8ca3…ad56d` → restored `bdfe9f46e8f21371…10be`
  (`restored_equal=true`)
- M3 `truth.json`: before `9663f90b…65e6` → mutated `f712d6b3852e1897…23d8`
  → restored `9663f90b…65e6` (`restored_equal=true`)
- M4 `inspection.json`: before `f69978355e2897fb…71f9` → mutated `01383b419869a2c8…e683`
  → restored `f69978355e2897fb…71f9` (`restored_equal=true`)
- Post-restore: all probe corpora `diff -rq`-equal to the pristine snapshot, and
  a final baseline run reproduces `aa3532…14ae` byte-for-byte, exit 0.
- The lane's own corpus bytes were re-hashed after the probe and are unchanged:
  fixture `bdfe9f46…10be`, `truth.json` `9663f90b…65e6`,
  `inspection.json` `f6997835…71f9`, `LEDGER.md` `25a4a18b…e1a6`.

## The hole (Q11 recheck scope), stated honestly

**H1 — the recheck never reads the entry.** `readout.py` opens exactly four
files (`FIXTURE`, `ORACLE`, `RECORD`, `LEDGER`); no `.md` is read. P5 shows the
consequence: a transcription defect in the entry's own stated values leaves the
canonical stdout **byte-identical** and the pin matching, so "the recheck
passes" says nothing about the entry's text. This reproduces, for C07, the
round-63 entry's own limitation sentence ("The recheck command reproduces the
observations; it does not detect the deletion of any clause"). A fresh-seat
reviewer must diff the entry's recorded block against a live run; the recheck
command alone cannot do it.

**H2 — recorded oracle provenance is semantically unguarded, and the level is
not byte-derivable.** `build_recipe.compression.level` is never read by any
`--fact`; M3 keeps every semantic check green. Worse, the value is **not
recoverable from the fixture bytes** for this fixture: recompressing both
payloads with `zlib.compress` at levels 7, 8 and 9 yields byte-identical
compressed slices (79 and 90 bytes, `bytes_equal_fixture_slice=True` for all
three levels; FLG `flevel` bits = 3 in every case), so levels 7–9 are
indistinguishable here even by regeneration. The oracle's `level: 9` is a
recorded build-recipe value, not a derived one; the entry must not present it
as byte-checked. Under R2 the only thing that reacts is the `digests` fact
(whole-file `truth.json` hash), i.e. a change tripwire — re-running the readout
and re-pinning the new stdout (the normal update path for any legitimate oracle
edit) makes the mutant green without any check ever having examined the level.

**H3 — the saved record's identity field is outside the recheck.** M4 mutates
`evidence_id` and every semantic check stays green; the string `evidence_id`
does not occur anywhere in readout output (`record` fact echoes only
`coverage`, `confidence`, `authority`, `region_kinds` and a fixed check list).
If the entry cites the record's Evidence ID — the round-63 C06 entry did cite
its record's ID — that citation is unchecked, and no Evidence-ID derivation
exists in-tree. This is exactly routed debt item 4 of
`reports/round-64/claims.md` ("Evidence-ID transplant corollary"); this probe
confirms it applies to the C07 recheck, not just to receipt binding.

**Why M1/M2 kills are real but narrow.** M1 is caught by the one conjunct that
compares a recomputed digest against the oracle for the mutated field. M2 is
caught four ways (image digest, region re-derivation, subject digest, padding
run length) because the fixture's whole-image hash is pinned in the oracle;
note the derivation *structurally* re-derives regions, so an inserted
non-zero byte splits a padding run (`region_count 6`, new span at 701) rather
than merely changing a hash. Both are honest kills. Neither establishes
coverage of any value outside the check list above.

## Verdict

- M1 **killed attributed** to `zlib@512.decompressed_sha256` (R1); R2 also trips.
- M2 **killed attributed** to `image.sha256` with region re-derivation and
  `subject.digest.sha256` as corroborating checks (R1); R2 also trips.
- M3 **survived** under R1 (no check exists); under R2 it trips only the
  `digests` tripwire, and a re-pin restores green — coverage finding H2.
- M4 **survived** under R1 (no check exists); same R2 caveat — coverage
  finding H3.
- P5 **survived both rules** — recheck is blind to the entry text (H1).

This is a coverage finding against the candidate's recheck scope, not a
falsification of C1's byte claims: every derived value the readout *does*
compare held on pristine bytes. Recommended for the candidate entry: declare
the recheck's detection rule explicitly (pinned stdout vs `all_match`), state
that recorded provenance fields (`build_recipe.compression.level`,
`python_version`, `determinism`) and the saved record's Evidence ID are
recorded-not-derived and outside the recheck, and have a non-author seat diff
the entry prose against a live run.

## Evidence locations

- Scratch (lane-owned, not part of the tree): `/tmp/revenger-r64-mutentry-K9Q2`
  — `readout.py` (copy of the entry recheck),
  `snapshot/corpus/**` (pristine copy), `probe_*`/`r1…r4` mutant copies
  (restored), `harness_entry.py`, `harness_stage2.py`,
  `results-entry.json`, `results-stage2.json`, `post-restore.out`.
- Entry artifacts probed: `/tmp/revenger-r64-entry/readout.py`,
  `/tmp/revenger-r64-entry/all.txt` (hashes above).
- No git/jj operation, no commit, no push; no lane file written by this seat
  except this report. No tool installed or upgraded (nothing needed; pacman
  untouched).

## Re-probe against the landed entry (final bytes, 2026-10-24)

Landed entry: `corpus/knowledge/round-64-firmware-region-byte-evidence.md`,
sha256 `9bf21e5057b77f17a8406af9d006fb4594dd2da54c6d0920f4ca842cfa3e0ebf`,
53098 bytes. Its `recheck:` line names the command
`python3 -B readout.py <repo-root>` with pinned 7-line stdout
`aa353251f7529a00c4336f9bf8cae6634838b8d10bd20e24b7340d94cf1314ae`
(the same pin as the pre-landing artifact). The `### Code` block was extracted
from the landed text verbatim (10018 bytes, sha256
`2abe0c130ae29de27ae194511e3b4e5061364818cf94d8d8671c3019eafabae1`) and is
**byte-identical** to the readout probed above (`cmp` clean). Run on a
byte-identical scratch copy of the six corpus files, cwd `/`: exit 0, stdout
**byte-identical** to the pin (`cmp` clean). Baseline green.

### Digest-flip kill on the landed text

M1 re-probe: `truth.json` → `regions[1].decompressed_member.sha256` last hex
digit `6→7` (`9663f90b…65e6` → `ef236f32403801d9…4c2f8f`). Run: exit 0,
`oracle.all_match=false`, failing check **`zlib@512.decompressed_sha256`**
(derived `a571…7b86`, stated `a571…7b87`), stdout `fbec7cc62e3a…` ≠ pin.
**KILLED attributed under both rules** (R1 semantic check; R2 pinned stdout).
Restored to `9663f90b…65e6`, `restored_equal=true`, copy `diff -rq`-equal to
the pristine snapshot. The landed entry's derivation does catch a flipped
decompressed digest.

### Do items 10–11 close H1 / H3? Honest verdict

**H1 (recheck blind to entry text) — NOT closed.** The readout still opens
exactly four files (`FIXTURE`, `ORACLE`, `RECORD`, `LEDGER`); no `.md` is read.
Items 10–11 add in-entry commands with their outputs (Q11 reproducibility), but
those commands are one-off shell/python invocations, **not** part of the
`readout.py` 7-line stdout, and nothing compares the entry's prose to a live
run. Probe: flipping item 10's `receipt.json` digest inside a copy of the
landed entry (`…b94d→…b94e`) leaves the recheck stdout **byte-identical to the
pin** (`aa3532…14ae`, exit 0, `all_match` true). A reviewer who reruns item 10's
`sha256sum` would see the disk hash, but only if they choose to run and compare
it; the recheck itself remains blind. Q13's own wording ("reproducibility aid,
not a gate") is accurate and must not be upgraded.

**H3 (saved-record identity unguarded) — instance closed by omission, gap
structural.** The landed entry cites **no** `evidence_id` (0 matches for
`evidence_id` / `ev_[0-9a-f]` in the text), so the round-63-style unguarded
identity citation is gone. Item 11 does not check identity: its command prints
only region count/keys, `names_present`, `decompressed_digest_present`,
`extractions`, and the `unblob` counts; `evidence_id` is not in its output
either. Item 11's own command replays exactly as printed (verified) and its
absence claims hold (`names_present=False`, `decompressed_digest_present=False`,
`extractions={}`, `unblob_lower=0`, `unblob_upper=1`). So H3 is closed for this
entry by not claiming the value, not by a check.

**New surviving mutant class opened by item 10 — the claimed surface now
exceeds the recheck.** Items 10–11 claim values for `generator.py`,
`receipt.json` and the S036 snapshot, none of which the readout reads. Two
probes on the landed code:

- M5: mutate `receipt.json` (claimed sha256 `e930a549…b94d` in item 10, the
  S037 header and the item-2 table) → `e930a549…b94d` → `fcb5831491fe…9c01`.
  Recheck stdout **identical to the pin** (`aa3532…14ae`, exit 0,
  `oracle`/`record` `all_match` true). **SURVIVED both rules.**
- M6: mutate `generator.py` (`level=9`→`level=8`, i.e. the item-3 replay basis;
  claimed sha256 `4e5d5975…d3b4`) → `76540971f577…326c`. Recheck stdout
  **identical to the pin**, `all_match` true. **SURVIVED both rules.**

Both copies were restored (`restored_equal=true`, `diff -rq` clean). This is a
coverage finding, not a contract break: item 10's `wc -c` + `sha256sum`
commands do catch these values **when rerun**, and the entry correctly claims no
guard credit. The residual risk is a reviewer treating the green 7-line pin as
covering item 10 — it does not; the pin covers only fixture, oracle, record and
ledger. Recommended wording for the entry (author's call, not a contract
change): state in §Reproduce that the 7-line pin covers the four read files
only, and that item 10's sizes/digests are verified by rerunning its own
commands.

Lane bytes after the re-probe are unchanged: fixture `bdfe9f46…10be`,
`truth.json` `9663f90b…65e6`, `generator.py` `4e5d5975…d3b4`,
`inspection.json` `f6997835…71f9`, `receipt.json` `e930a549…b94d`,
`LEDGER.md` `25a4a18b…e1a6`, entry `9bf21e50…0ebf`. Scratch:
`/tmp/revenger-r64-mutentry-LD` (`readout-landed.py`, `snapshot/`,
`reprobe-results.json`, mutant copies restored). No installs.
