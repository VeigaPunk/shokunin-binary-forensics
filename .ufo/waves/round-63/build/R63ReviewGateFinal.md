# R63 build-wave integration gate — R63ReviewGateFinal (2026-10-23)

Scope: working tree at HEAD `54ab973` (claims frozen) reviewed while wave seats were landing (fixture/runs 23:22–23:26Z). Method: fresh file checks + frozen `reports/round-63/measure.py` run on an isolated copy of the working `corpus/` at `/tmp/revenger-r63-gate` (lane-owned scratch, `TMPDIR` inside it; repo untouched, no git/jj mutations, no `.ufo` spec/registry edits). No tools installed; no pacman (paused).

## Gate table

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | C06 candidate exists with Q01–Q13 self-check | **PENDING — FLAG** | Candidate absent at `corpus/knowledge/round-63-zip-central-directory-evidence.md` and at the seat target `/tmp/revenger-r63-entry/candidate.md` (only `readout.py`/`readout.stdout.txt` there). No R63EntryC06/R63ReviewC06Q report in `build/`. Premise artifacts DO exist: `build/zip-readout.out` + `build/zip-readout.py`, `source-snapshots/{appnote.txt,zipfile.html}`, readout stdout shows EOCD@2942 (2 entries), CD@2828 size 114, fixture sha `857989f5…` — premise only, not a candidate. |
| 2 | Firmware fixture + record + oracle present | **PASS** | `corpus/fixtures/firmware-r63/{firmware-r63.bin (2048 B, sha256 `bdfe9f46…8510be`), generator.py, truth.json}`; `corpus/live/runs/round-63/{inspection.json, stdout.raw, receipt.json, stderr.txt (empty), oracle_check.py}`. Receipt: real `npx -y rea-agents@6.5.0 inspect-firmware-regions … --format json`, exit 0, Evidence ID `ev_aae7529f…`. I recomputed: sha256(stdout.raw)=`f6997835…` == receipt.stdout_sha256; fixture sha == receipt.fixture_sha256; `stdout.raw` byte-identical to `inspection.json`; record has `operation=inspect_firmware_regions`. Byte oracle: `python3 -B corpus/live/runs/round-63/oracle_check.py` → `ORACLE OK`, exit 0 (zlib members 512/79 and 1024/90; decompressed sha `a5718481…`, `2d0d86aa…` match truth). Frozen counter on my isolated copy: `F_COVERAGE=5/8`, `inspect_firmware_regions: 1`. |
| 3 | Both C3 patches present and self-tested | **PASS** | `corpus/verify_named_multi_icon_states.py`: `receipt_ok()` L16 keeps `receipt['command']==command` (single match for the probe regex) + in-script control L76–79 (`forged['command'] += ' --forged'`, message `forged receipt accepted`). `corpus/verify_icon_states.py`: `receipt_ok()` L119–123 preserves the `round_id != 36` exemption + control L151–158 (`forged['fixture_sha256'] = '0'*64`). Frozen measure.py on the isolated copy: `C3_CONTROLS_PASS=2/2`, `C3_RECEIPT_KILLED_ATTRIBUTED=2/2` (named mutant → `AssertionError: r55: forged receipt accepted`; icon mutant → `r36: forged receipt accepted`), controls exit 0, `HOLD_CALIBRATION=4/4`, `HOLD_REPLAY=10/10`, `HOLDS_OK=yes`, `PROBE_EXIT=0`. Independent mutant transcripts: `/tmp/revenger-r63-mutc3/{work/,transcripts.json}`. |
| 4 | README NOT flipped yet | **PASS** | `corpus/README.md:35` C06 status still `partial` (fresh grep); `K_ROW C06 status=partial` in gate probe; `git status` shows corpus/README.md unmodified. |
| 5 | Source rows drafted and reviewed | **PENDING — FLAG** | `corpus/SOURCES.md` has no `S032`/`S033` rows (fresh count 0; last row S031 at L45). No R63SourceAppnote / R63SourceZipfileDocs / R63SourcesRows reports in `build/`. |
| 6 | Lesson drafted with M33 | **PENDING — FLAG** | No `corpus/lessons/round-63.md`; seat target `/tmp/revenger-r63-lesson/round-63.md` absent (only `probe/` pre-probe bins — the M33 evidence itself). No R63LessonDraft report in `build/`. |
| 7 | Preservation manifest present | **PASS (base)** | `.ufo/waves/round-63/build/preservation-base.sha256` — 455 sha256 records (443 `corpus/live`+`corpus/fixtures` files + 10 `verify_*.py` + README + SOURCES); `build/R63Preservation.md` records the clean-base guard, count reconciliation, capture command. `git status` ground truth: no modifications under `corpus/live`/`corpus/fixtures`; only new untracked `corpus/fixtures/firmware-r63/` and `corpus/live/runs/round-63/`. Final post-landing re-check remains L1's step. |
| 8 | No fleet-root stray files naming this round | **PASS** | `ls` of `/home/vgpnk/Projects/shokunin/` filtered `r63\|round-63\|revenger` → only the `revenger-shokunin` lane directory itself. (Sibling-lane kotoba-r63 scratch under `/tmp` is out of scope and not fleet-root.) |

## Flags for L1 (PENDING items claiming progress without evidence)

- **FLAG-1 (C1):** premise artifacts are not a candidate — no entry markdown, no Q01–Q13 self-check, no fresh-seat review decision exists. At this gate, C1 must not be claimed; K must land as 6/14 with C06 `partial`.
- **FLAG-2 (sources):** S032/S033 rows are the C1 sourced-claim prerequisite and are neither drafted-in-place nor reviewed; landing C1 before them would violate the admission order.
- **FLAG-3 (lesson):** `round-63.md` with `## Mistakes` M33, Gate quotes, search-log and routed-debt sections is a landing requirement and does not exist yet.

C2 needs no honest-absence report: fixture, real-run record, receipt and byte oracle are all present and green (item 2).

## Residual risk and verification gaps

- Seats landed mid-review; the gate probe ran on a copy taken ~23:26Z. The binding final numbers are L1's frozen counter on the committed archive (`reports/round-63/measure-after.log` on the tip, per round-62 routed debt (a)).
- `R63Preservation.md` notes requested baseline `55bcb6e` vs checkout HEAD `54ab973` with tracked-tree count reconciled (443); L1 should confirm this equals the claims-base tree when running the final preservation check.
- Named verifier PASS line now prints `142 positive checks` (was 139 at base): the added `receipt_ok` checks increment the computed counter; line template and all saved-input assertions unchanged (probe passes, controls exit 0). Consistent with the frozen fix shape; noted for transparency.
- Scratch `/tmp/revenger-r63-gate` (isolated copy + `probe.out`) is lane/round-owned under the sanctioned prefix; remove on landing with the other round scratch.
