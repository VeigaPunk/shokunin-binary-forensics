author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

# Round 75 — non-author verifier spot-check (revenger)

Closed against lane tip `5952d3cb27acdfbf81048992b455f2ac12294880` (branch `main`, pushed;
local = remote). Base `f29dc92b3adb4202195bc7fc25b4aa6a5b7a2563`. Every measurement below was
re-run by this verifier (non-author) on this host, 2026-11-01; scratch under
`scratch/revenger-r75/verify/` (judge copies, not lane artifacts). Index-free git only.

## Step-1 conformance

| check | result |
|---|---|
| Report committed in fleet repo by lane identity | PASS — `git log --format='%an <%ae> %H' -1 -- .ufo/reports/round-75/revenger.md` → `revenger-shokunin <revenger@shokunin.local> 2cf082485c049d1cde3141277b4241158834ca93` |
| `SHONEN` heading in committed report bytes | PASS — `## SHONEN` + one `[~]` line per box (4/4), pointers resolvable |
| Cited lane commits exist and are ancestors of `refs/heads/main` | PASS — `merge-base --is-ancestor` ok for `f29dc92b3adb` and `e783101f190e`; range `f29dc92b..5952d3cb` contains exactly the 2 cited commits, both authored `revenger-shokunin` |
| Lane tip pushed | PASS — `ls-remote origin refs/heads/main` = `5952d3cb27acdfbf81048992b455f2ac12294880` = local `refs/heads/main` |
| Report is a real report, not a marker | PASS — names work, evidence pointers, cited hashes; content checks out |

## Per-claim re-check (all re-measured by this verifier)

**C1 — coverage, criterion P revision (instrument P2).** Verdict: **improved, verifies.**

- Old probe genuinely PATH-only: `git show f29dc92:reports/round-74/province_probe.sh` line 33
  probes `command -v ghidra || command -v analyzeHeadless` only — no tools-dir or Program-Files
  fallback. The false "absent" record mechanism is real.
- Host facts re-derived: `command -v ghidra` and `command -v analyzeHeadless` both fail (off-PATH);
  `C:/Users/jpvei/tools/ghidra_12.1.4_PUBLIC/support/analyzeHeadless.bat` exists;
  `(Get-Item).CreationTime` → `Monday, October 26, 2026 11:14:22 PM` (= 2026-10-26 23:14, five
  days before the r74 probe ran, as reported).
- Judge red run (P2 from tip bytes against a fixture built from `git show f29dc92:PROVINCE.md`
  + `.git/` + bounty-module stub): exit 1, `P2_SURFACES_RESOLVED=10/11 UNRECORDED_ABSENT=0
  STALE_RECORDS=1 P2_SCORE=9.1`, `engine-ghidra STALE-RECORD` — matches `p2-before.log`.
- Judge green run (same P2 against tip PROVINCE.md): exit 0, `P2_SURFACES_RESOLVED=11/11
  UNRECORDED_ABSENT=0 STALE_RECORDS=0 P2_SCORE=10.0` — matches `p2-after.log` and the tip
  re-run in `tip-verification.log`.
- PROVINCE.md diff `f29dc92..5952d3cb` is exactly the one ghidra absent→present block; every
  other byte untouched (diff shown in full by the verifier).

**C2 — calibration, criterion N (record-vs-reality mismatch detection).** Verdict: **improved, verifies.**

- Judge re-run of `probe_negctl.sh` (tip bytes, complete fixture layout): exit 0 with all five
  lines byte-equal to `negctl-run.log` — `NEGCTL_V1_STALE_RECORD_FLAGGED=0/1`,
  `NEGCTL_V2_STALE_RECORD_FLAGGED=1/1` (attributed `engine-ghidra … STALE-RECORD`),
  `NEGCTL_V2_UNRECORDED_ABSENT_FLAGGED=1/1`, `NEGCTL_V2_POSITIVE_CONTROL=pass`,
  `NEGCTL_SELFTEST=pass`. The kill leg requires the specific line+token, not merely nonzero exit.
- Replication note (not a defect): the harness's positive control correctly fails if the fixture
  lane layout is incomplete (no `.git/` dir or no `corpus/training/bounty-triage/MODULE.md`
  stub) — future replicators must build both stubs; the probes are faithful to fixture state.

**Capability — ghidra-headless-recon.** Verdict: **verifies, fully re-measured end to end.**

- `sha256sum` over committed `corpus/fixtures/pe-r75-headless-smoke/fixture.exe` (extracted via
  `git show` from the tip) = `fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72`
  — matches truth.json and the report.
- Regen determinism: committed `gen_pe_r75.py` re-run to a fresh path → byte-identical
  (`cmp` clean, same sha256).
- Independent PE parse (`python -I`): PE32+ magic 0x20b, machine 0x8664, one section `.text`,
  image base 0x140000000, entry RVA 0x1000 → entry VA 0x140001000, entry file offset 0x200,
  entry bytes `B82A000000C3` = `mov eax,0x2A; ret`. All declared premises re-derive from the
  committed bytes.
- Live re-run by this verifier: committed `rev75_dump.java` via Ghidra 12.1.4 headless
  (`analyzeHeadless.bat` under cmd; project in `%TEMP%/rev75-judge`, `-deleteProject`) over the
  committed fixture → exit 0, tool line `REV75_DUMP wrote …: 1 functions, 1 decompiled
  (GhidraScript)`, output `// ==== FUNC entry @ 140001000 ====` with body `return 0x2a;` —
  matches the committed receipts (`ghidra-headless-recon.log`, `ghidra-headless-codeable.log`,
  `codeable-decompiled.c`). The capability claim rests on a real headless analysis and its
  receipts re-derive from committed bytes.
- pe-r53 leg (function_count=0, no decompile claim): consistent with the receipt's honesty
  boundary; not re-run (secondary leg, no claim rests on it).

**Carry-in — treecommit mode drift.** Verdict: **verified; note exists and is accurate.**

- `git ls-tree 85db6ab reports/round-74/measure.py` → `100755 blob 50f8aae00525fb94d4f0519d981e68bd4e8f055b`;
  same blob id at `f29dc92b` (base) and `5952d3cb` (tip) with mode `100644` — byte-identity is
  real (equal blob ids), mode 100755→100644 confirmed at both ends.
- `corpus/lessons/round-75.md` `## Mistakes` row 2 records the mode-correction note; LOG.md
  round-75 entry carries the same disclosure.
- treecommit helper code inspected: `update_tree` keeps `prev[0]` for existing blobs and pins
  `100644` for new blobs; the docstring's `<path>[:mode]` is not parsed anywhere in the code —
  "no treecommit invocation can produce 100755" is accurate. Operational impact none
  (invoked `python -B`), as disclosed.
- Carry-in item 2 (explicit file args, diff-stat verification): both round commits list explicit
  files; range diff-stat shows 21 files, +924/−1, zero unintended deletions.

**No-harm holds — all re-measured by this verifier.**

- K: extracted tip archive, `PYTHONUTF8=1 python -B reports/round-73/measure.py <tree>` →
  `K_HELD_BACKED=8/15`, `C10_STATUS=partial`, `C10_Q_VOTES=0/16`, exit 0 — matches
  `tip-verification.log`.
- F: SCORECARD F command over the committed tip tree → `COVERAGE 5 / 8 score= 6.25` with the
  identical family histogram — matches `holds.log`.
- FRESH_ROWS: committed-bytes grep → seed.md 12 + readiness checklist 6 = 18/18.
- Protected-path diff `f29dc92..5952d3cb` over `corpus/knowledge corpus/live corpus/README.md
  corpus/QUALITY.md SKILL.md SHONEN.md corpus/fixtures/pe-r53 corpus/fixtures/apk-r65` →
  0 bytes. No owned axis harmed.

## Spot-check table (step 3)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S443 (local Ghidra install, `application.properties` + `rea doctor`) | ADMIT (tier A own-host) | `C:/Users/jpvei/tools/ghidra_12.1.4_PUBLIC/Ghidra/application.properties`; `rea doctor` | **agree** | `application.version=12.1.4`, `application.revision.ghidra=8b6bbb857accdfa20dc5b2f5dea471178c2e9fbc`, doctor scope_check `name: ghidra / ok: true / classification: healthy / C:\Users\jpvei\tools\ghidra_12.1.4_PUBLIC` — all re-derive; quote located and ≤25 words |
| S444 (rea 6.8.0 manifest + doctor) | ADMIT (tier A own-host) | `rea --llms`; `rea doctor` | **agree, with a correction owed** | `cli_commands: 175` and `environment_healthy: false` re-derive; BUT the row's census sentence "`grep -cE 'inspect_'` over the full manifest prints 0" does NOT re-derive on the llms leg — verifier observes **2** (`inspect_macho`, `inspect_signature` inside two Hopper-wrapper descriptions); the doctor leg does print 0. Substance unaffected: all 14 frozen-F family operation names grep 0 in the manifest (verified), and the routed item (F counter revision) stands. The row/lesson phrase "zero `inspect_*`" needs a named correction entry next round |
| F-family coverage move (android/managed/browser-runtime) | REJECT (ruled out; S444) | `rea --llms` grep over the frozen counter's 14 family operation names | **agree** | 0 matches; a hand-authored 6.5-era-named record would be fabricated producer evidence; do-nothing control holds F 5/8 (re-measured). Note: 6.8.0 does carry hyphenated `inspect-*` CLI surfaces (`inspect-managed-artifact`, `inspect-macho`, …) under different names — this strengthens, not weakens, the routed need for a frozen counter-revision mapping table |
| K-map admissions (C05/C15/C10) | REJECT (ruled out; operator-blocked) | fleet `.ufo/state/` (empty — no dispatcher/seat surface); `.ufo/l0-questions.md` revenger r74 row still open | **agree** | no dispatch/Q-review surface on this host; L0 routed around, never treated as answered; C10 already disposed `rejected` by the r74 frozen kill rule |
| P-as-scored declaration (r74 instrument) | REJECT → revised instead (C1) | r74 `province_probe.sh:33` + judge P2 red run | **agree** | v1 is PATH-only (verified above); declaring P as scored would have rested on a defective instrument; the red-before on base bytes re-derives |

## Census (step 3)

- Contract's literal tail-arg form: `validate --root <fleet> revenger` → exit 2, `revenger
  missing …/shokunin/revenger-shokunin/corpus/SOURCES.md` — exactly the disclosed old-layout
  resolution; the r74 disclosure stands (status-neutral).
- Sanctioned explicit-lane-dir form: `validate --root <fleet> <lane-dir>` → **exit 0**, final
  line `ok … corpus/SOURCES.md`; warnings **31** (21 W01 tierC-mined used-by + 10 W04
  cross-scope duplicate-URL) — matches the report's 31→31 and the committed
  `census-after.log` classes. New rows S443/S444 added no warning.

## Trend verdicts (with evidence)

- **expansion — unchanged.** No knowledge entry admitted (protected `corpus/knowledge` diff = 0
  bytes, verified); K 8/15 (re-measured over tip), F 5/8 (re-measured); capability + registry
  growth are not admissions (r73/r74 precedent holds).
- **quality — improved.** A false province record is now true and dated (PROVINCE diff verified
  surgical); the defect class is instrumentally caught with attribution (negctl re-measured);
  the capability adds a demonstrated local producer route (live headless re-run by this
  verifier).
- **discernment — improved.** The round's own inherited instrument was the defect; falsified
  with a red-before on the lane's own committed bytes (re-derived here); mined as a mistake
  class; the superseded instrument's behavior on the fixed bytes is disclosed, not hidden
  (`NEGCTL_V1_ON_FIXED_OBSERVED=exit-1`, `v1-tip-exit=1` — both re-opened).

## Defects and routed items for next round

1. **(correction owed, status-neutral)** S444 + lesson/reports' "zero `inspect_*` operations /
   `grep -cE 'inspect_'` → 0" does not re-derive on the `rea --llms` leg (observed 2:
   `inspect_macho`, `inspect_signature` in Hopper-wrapper descriptions; the doctor leg re-derives
   0). Conclusion unaffected (all 14 frozen-F family names absent — verified). Land a named
   correction entry (new row or `used-by`/`teaches` logged change) per SOURCES contract rule 2.
2. **(routed, stands)** F counter revision needs a frozen 6.5→6.8 operation-name mapping table;
   6.8.0's hyphenated `inspect-*` surfaces make the mapping non-trivial (already routed in the
   lesson; confirmed here).
3. **(pre-existing, disclosed)** census literal tail-arg exits 2 on this host; explicit-lane-dir
   form is the sanctioned invocation (r74 disclosure stands).
4. **(observation)** negctl replication requires the `.git/` + bounty-module stubs in the
   fixture lane layout, else the positive control correctly fails — record for future
   replicators (behavior is correct, not a defect).
5. **(operator note)** All four SHONEN boxes remain `[~]` (lane-asserted); none carries `[x]`.
   Box 2 (end-to-end domain task) now has a fully re-derivable evidence chain (this verifier
   re-executed it end to end); the promotion review may check it — only a non-author may write
   `[x]`, and this verifier does not write SHONEN.md.

## Verdicts

| axis | verdict |
|---|---|
| coverage | improved (C1 re-measured) |
| calibration | improved (C2 re-measured) |
| depth | unchanged |
| operability | unchanged |
| freshness | unchanged (re-verification exercised; records stand) |
| adjacency | unchanged |

Status **ok**, admitted **true**: every declared claim verifies by re-measurement, no axis
harmed. The correction owed in defect 1 is status-neutral and does not bar admission.
