# W2FinalIndependent — independent final verification, round 63 falsify (attempt 1)

Seat: `revenger-r63.W2FinalIndependent` (leaf; no subagent dispatch). Date 2026-10-24.
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Target bytes: lane tip
`db55bd6488e24e956df5818ae34c2a043d7ddc12` (the integration commit carrying the C1
candidate entry, SOURCES S032/S033 and the round-63 lesson), extracted with
`git archive <tip> corpus` to `/tmp/revenger-r63-finalind`. Frozen counter
`reports/round-63/measure.py` sha256 `3b7fba2d5243bbe0b723a99a53085130ff97010e23c8a59a8027f5f8992c5908`;
frozen contract sha256 `aed53241c3e4445fab94e854e3185b235ab2ff45c921d6c95e6e60938c7d1e31`.
Machine receipt: `.ufo/waves/round-63/falsify/final-independent.json`.

## Verdicts

| Claim | Target | Observed on committed bytes | Verdict |
|---|---|---|---|
| C1 coverage K | `K_HELD` 7/14 and Q01–Q13 pass as committed | `K_HELD=6/14`, `K_ROW C06 status=partial`, `K_HELD_BACKED=6/14`; Q01 **FAIL** | **FALSIFIED** |
| C2 coverage F | `F_COVERAGE` 5/8 with a real-run envelope and byte-oracle agreement | `F_COVERAGE=5/8 score=6.2`, `F_FAMILIES` includes `firmware`; oracle `ORACLE OK` exit 0; envelope hashes agree | **MET** |
| C3 calibration | `C3_RECEIPT_KILLED_ATTRIBUTED` 2/2 | `C3_CONTROLS_PASS=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2`, both mutants killed with last line `… forged receipt accepted` | **MET** |

Probe exit `0`; `HOLDS_OK=yes`; `HOLD_CALIBRATION=4/4`; `HOLD_REPLAY=10/10`; `FRESH_ROWS=18/18`.
All 36 printed counter lines are recorded verbatim in `final-independent.json`.

## Attacks and evidence (each item names what it attacks)

### C1 — entry vs Q01–Q13 (attacks the admission condition)

- **Recheck reproducibility.** Extracted the `### Code — readout.py (complete)` block
  verbatim from `corpus/knowledge/round-63-zip-central-directory-evidence.md`, ran it in a
  fresh copy of the archive tree from the repo root: **exit 0, 17 stdout lines, SHA-256
  `02b0f495c1db8c50e22db835cd57e7a221dd0a9c82f09d442feea461de722ed4`** — equal to the
  entry's claimed stdout digest; **17/17 lines appear verbatim in the entry** (Q11 support
  for the readout itself; the separate word-count transcript failure is below).
  The printed paths are repo-relative, so the digest is extraction-root independent as claimed.
- **Source-row re-open (S032).** All **10** entry quotes are verbatim substrings of the
  whitespace-normalized pinned snapshot `.ufo/waves/round-63/source-snapshots/appnote.txt`
  (sha256 `0b99302…a50cd6`, 174585 bytes — re-hashed), and every quote is ≤24 words.
  S033's four digests reproduce at base `55bcb6e` (`git show <base>:<path> | sha256sum`) and
  in the working tree. Saved record is 7692 bytes as item 20 states.
- **Flip arithmetic (attacks the K target).** Applying the draft flip line
  (`R63ReadmeFlipDraft.md:23`) in `/tmp` only, the probe's K block prints
  `K_HELD=7/14` **and** `K_HELD_BACKED=7/14` (both knowledge paths resolve). So 7/14 is
  reachable; it is not licensed because of Q01 below.
- **Q01 FAIL (high).** `corpus/SOURCES.md:46` registers S032 with scope
  “central directory file header and end-of-central-directory record field layout … CRC-32
  and local-header offset” and anchors `§4.3.3, §4.3.12, §4.3.16, §4.4.7, §4.4.10-4.4.12,
  §4.4.16, §4.4.21-4.4.22` — **no §4.3.7**. The lesson Gate
  (`corpus/lessons/round-63.md:37-51`) declares the same narrower tier-A scope and records
  **9** quotes, none from §4.3.7. The entry's `source:` header instead attributes S032 with
  “the local file header, …” scope, and entry items 5, 8 and 9 derive the 30-byte local file
  header layout and the name/extra-length offsets 26/28 **from §4.3.7**; inference 17 rests
  on those local-header reads. Those load-bearing claims therefore rest on a row that is not
  tier A for their scope. Minimal repair (L1, not this seat): amend the S032 row scope+anchor
  and add the two §4.3.7 located quotes to the Gate; the entry text already cites the right
  sections and quotes.

- **Q11 transcript (high).** The entry's §Reproduce word-count block records `8` for
  `printf '%s\n' "local file header signature 4 bytes (0x04034b50)" | wc -w`; re-running
  that exact pipeline on the committed bytes prints **7**. All nine other recorded counts
  match (7, 21, 10, 8, 23, 24, 20, 12), and the 17 readout lines themselves reproduce
  verbatim with the claimed digest — but the entry carries one command output the command
  does not print, which is exactly what Q11 governs. Smallest correction: display `7`.

Named fresh-seat decisions: **Q01 FAIL and Q11 FAIL**; Q02 pass; Q03 pass; Q04 pass; Q05
n/a (no readiness claim); Q06 pass; Q07 n/a; Q08 superseded by Q11; Q09 pass; Q10 pass;
Q12 n/a; Q13 n/a by construction. Per `QUALITY.md` (“Admit only when no criterion fails”),
C06 must stay `partial`; K remains 6/14; **C1 falsified as committed**.

### C2 — firmware record envelope and oracle (attacks the F condition)

- (a) `corpus/live/runs/round-63/inspection.json` carries
  `evidence_id ev_aae7529f…0ed259` and `normalized_result.operation == inspect_firmware_regions`
  (keys `engine`, `input_size`, `regions`, `coverage`), input size 2048.
- (b) `receipt.json` carries the command
  `npx -y rea-agents@6.5.0 inspect-firmware-regions <fixture> --format json`, exit 0,
  duration 1.296587134, fixture SHA-256 `bdfe9f46…`, stdout SHA-256 `f6997835…`, and the
  same Evidence ID. `stdout.raw` and `inspection.json` are **byte-identical 3904-byte files**
  (both re-hashed to `f6997835…`); `stderr.txt` is 0 bytes. Raw layer carries
  `raw_result.execution` (binwalk `--search-all --threads 1`, `/tmp/rea-firmware-7rPoLl/…`)
  and `version_execution` stdout `binwalk 3.1.0`.
- (c) Both record regions match truth on offset and size (512/79, 1024/90) and their
  decompressed SHA-256 matches truth (`a5718481…`, `2d0d86aa…`). Independent `zlib`
  re-derivation over the committed fixture reproduces both digests and lengths (78, 97) and
  confirms the three padding spans are all-zero. `oracle_check.py` on the committed tree:
  five `OK` region lines, final line `ORACLE OK`, exit 0.
- Counter: `F_COVERAGE=5/8`, `F_FAMILIES` includes `firmware`.
- Note (low): the record reports **2** regions while truth lists **5** (three padding
  spans). Condition (c) is one-directional (“every region the record reports”), so this is
  not a falsification, but it is precision-of-reported-regions, not inventory equality;
  `oracle_check.py` encodes the asymmetry as `record=not-expected padding=OK`.

### C3 — attributed forged-receipt kills (attacks the calibration condition)

- Probe on committed bytes: `C3_CONTROLS_PASS=2/2`; mutant lines
  `verify_named_multi_icon_states.py c3 exit=1 killed :: AssertionError: r55: forged receipt accepted`
  and `verify_icon_states.py c3 exit=1 killed :: AssertionError: r36: forged receipt accepted`
  → attributed under the frozen rule (non-zero exit, last line contains `forged receipt`).
- No `could-not-evaluate (clause match count != 1)` line: each mutant matched exactly one
  site (the probe would otherwise set `evaluable=False` and exit 2).
- Red-before `measure-before.log`: `C3_CONTROLS_PASS=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=0/2`,
  both c3 mutants `exit=0`.
- Patch shape (`git diff 55bcb6e..db55bd6`): `receipt_ok` helper added to both files; the
  original conjunct chain moved verbatim (named) and the original assertions moved verbatim
  with the `round_id != 36` evidence-ID exemption preserved (`verify_icon_states.py:122`);
  forged deep-copy controls added (`command += ' --forged'`, `fixture_sha256 = '0'*64`); no
  existing assertion removed; named positive checks 139→142 (additive). Verifier census 10;
  `HOLD_REPLAY=10/10`, `HOLD_CALIBRATION=4/4`; C2 counters unchanged at 2/2.

## Findings by severity

1. **HIGH (C1).** Q01 scope/anchor mismatch — S032's registered scope (`SOURCES.md:46`) and
   the Gate (`lessons/round-63.md:37-51`) exclude §4.3.7 and local-file-header layout, while
   the entry's header claims that scope and items 5/8/9 depend on it. Blocks the C06 flip;
   C1 falsified at K 6/14.
2. **HIGH (C1).** Q11 transcript mismatch — the recorded `wc -w` output `8` for the local
   file header signature quote is `7` when the recorded pipeline is re-run; one wrong
   recorded command output. Single-character repair, but a criterion failure as committed.
3. **MEDIUM (C3).** The probe's `HOLDS_OK`/exit code does **not** include the two attribution
   counters: `PROBE_EXIT=0` would also be printed at C3 0/2. The C3 target must be read from
   `C3_RECEIPT_KILLED_ATTRIBUTED`, never inferred from exit 0.
4. **LOW (C2).** Record reports no padding regions (truth has 3 of 5 regions as padding);
   claim (c) is one-directional, so this is a framing risk, not a defect.
5. **INFO (C2).** Producer origin unprovable without executing the target (forbidden); the
   receipt/record byte identity is the available envelope evidence, and the ledger records it
   as U4 UNKNOWN.

## Residual risk

- If L1 reads the telegraphic S032 scope cell as non-exhaustive, Q01 could be recorded as
  pass-with-correction; the entry's own scope sentence still contradicts the registry bytes,
  so a row/Gate amendment is required either way before any flip. Even with Q01 resolved,
  Q11's recorded `8` must be corrected to `7` in the entry itself before admission.
- A forged-but-consistent C2 envelope cannot be excluded without re-running the producer.
- C3 numbers depend on the committed verifier bytes; any post-wave edit invalidates the
  receipt.

## Verification gaps

- No target execution (wave rule): the REA producer was not re-run.
- No `shokunin` CLI on PATH; the fleet's read-only `scripts/sources-census.sh` was used:
  `validate` **exit 0** with exactly the three disclosed W04s (S024/S028/S029); `census`
  **exit 0**: rows 33, tier A 31 / C 2, mined 28 / queued 1 / rejected 4, missing 0.
- Tool installs: **none**. Pacman untouched. Heavy scratch `/tmp/revenger-r63-finalind*`
  removed after this report landed. Lane tree, index, jj state and registry files unmodified.

## Reproduction (committed bytes only)

```
git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive db55bd6 corpus | tar -x -C /tmp/T
cd / && python3 -B /home/vgpnk/Projects/shokunin/revenger-shokunin/reports/round-63/measure.py /tmp/T
cd /tmp/T && python3 -B corpus/live/runs/round-63/oracle_check.py
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --today 2026-10-24 /home/vgpnk/Projects/shokunin/revenger-shokunin
/home/vgpnk/Projects/shokunin/scripts/sources-census.sh census /home/vgpnk/Projects/shokunin/revenger-shokunin
```
