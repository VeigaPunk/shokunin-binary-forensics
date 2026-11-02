# round-87 verifier spot-check — revenger (closure judge, non-author)

author: hyaku closure (non-author integrator, zcode subagent (fresh session, non-author))

Round: revenger r87. Lane repo `fleet/shokunin-binary-forensics`, base
`1306ec9ac32a4d4477cc15049c1d09e326ecac5a` → tip
`1481f4907b370a32bc6543dfe831a3da30741d97`. Report
`.ufo/reports/round-87/revenger.md`. ONE declared claim (C1, calibration,
not exploratory, with counting commands). Every value below was re-run by
this session unless marked evidence-verified; commands were run against
committed blobs extracted with `git show` (never the git index).

## 1. Step-1 conformance — all pass

| check | result |
|---|---|
| report committed in fleet repo by lane identity | pass — `git log --format='%an %ae %H' -1 -- .ufo/reports/round-87/revenger.md` → `revenger-shokunin revenger@shokunin.local 5916d3ab7ae43813902815177a31ad8cdcc1a933` |
| `SHONEN` heading in report | pass — `## SHONEN` with four `[~]` lines, each with an evidence pointer; author marked no `[x]` |
| cited lane commits exist + ancestry | pass — `ea143a3a` (freeze), `1fa086d3` (landing), `1481f490` (adjudication) all `cat-file -e` OK and `merge-base --is-ancestor <h> refs/heads/main` OK |
| branch tip pushed | pass — `git ls-remote origin refs/heads/main` = `1481f4907b370a32bc6543dfe831a3da30741d97` = local `refs/heads/main` |
| round work within `1306ec9a..1481f490` | pass — `diff-tree -r` lists exactly 24 files, 966 insertions, 0 deletions (additions only) |
| dispatch/complete digest | pass — matches the contract's watchdog digest (launch 06:33:51-08:00, complete 07:58:58-08:00, head=1481f490 pushed=True) |

No marker-report condition: the report names real committed work with
checkable hashes and evidence pointers — a real report, not a marker.

## 2. Claim C1 re-check — re-measured, verifies

### 2a. Byte identity of the three instruments (all three shas match the claims.md pins)

```
sha256sum (git show <tip>:path > file, byte-preserving redirect)
eb5d1b54fa20421c09cd55e15d6a849af1379a822887b5a6ef60e0935c013fad  reports/round-75/probe_negctl.sh   (v1, = claims pin)
d70271464a437a6c0de598237a603cc50498458a14c94e37f8df2edf7e03070d  reports/round-87/probe_negctl2.sh  (v2, = claims pin)
ed0b328279133579a100d99f331ba752267782cd9b6764899c2082bfad4d87ed  reports/round-87/selftest_probe.sh (counting, = claims pin)
```
`diff-tree` freeze→tip over the three paths is empty — instruments
unchanged since the freeze `ea143a3a`, exactly as claimed.

### 2b. Red over the frozen v1 bytes (re-run by me)

```
$ bash reports/round-87/selftest_probe.sh reports/round-75/probe_negctl.sh
NEG_SELFTEST_MODE_PRESENT=0/1
NEG_SELFTEST_MUTANTS_KILLED_ATTRIBUTED=0/2
NEG_USAGE_EXIT64=0/1
RED_EXIT=1
```
Matches `negctl-red.log` exactly. v1 blindness markers re-grepped over the
committed blob: `usage:`=0, `NEGCTL_V2_SELFTEST`=0, `stale_flag_ok`=0,
`attribution guard`=0 — the blindness claim holds.

### 2c. Green over the committed v2 blob (re-run by me)

```
$ bash reports/round-87/selftest_probe.sh reports/round-87/probe_negctl2.sh
NEG_SELFTEST_MODE_PRESENT=1/1
NEG_SELFTEST_MUTANTS_KILLED_ATTRIBUTED=2/2
NEG_USAGE_EXIT64=1/1
GREEN_EXIT=0
```
Matches `negctl-green.log` exactly. Direct hermetic selftest re-run:
`NEGCTL_SELFTEST_FALSEPASS_LOGIC=ok`, `NEGCTL_SELFTEST_ATTRIBUTION_GUARD=ok`,
`NEGCTL_SELFTEST_STALE_LOGIC=ok`, `NEGCTL_SELFTEST_UNRECORDED_LOGIC=ok`,
last line `NEGCTL_V2_SELFTEST=pass`, exit 0. Usage form: `usage:
probe_negctl2.sh [--selftest]` on stderr, exit 64.

### 2d. The mutation-killed attribution pair (re-derived by me from the committed blob)

| mutant | sed recipe applied | diff observed | mutated-copy sha | death observed |
|---|---|---|---|---|
| A (verdict blind) | `s^\|^stale_flag_ok() {.*\|stale_flag_ok() { return 0; }\|^` | exactly `35c35`, one line | `f70c0e9aceb72323550b4d3732edaa39013498fc2607b286f0adeddf49c79a99` (= pin) | exit 1, last line `selftest: stale-record verdict accepted a false-pass` (dies at ST1) |
| B (pattern `.*`) | `s\|'\^engine-ghidra \.\*STALE-RECORD'\|'.*'\|` | exactly `35c35`, one line | `ec29099cf02b9d10b4a9f15368e22d0ed0977d667b0e83969eedf1ffdce439cb` (= pin) | exit 1, last line `selftest: attribution guard accepted an unattributed kill` (passes ST1 `FALSEPASS_LOGIC=ok`, dies at ST2) |

Deterministic ST1→ST2 ordering confirmed: mutant A's blinded `return 0`
fires ST1; mutant B's `[ "$1" = "1" ]` guard still rejects exit-0 inputs so
it passes ST1 and dies at ST2 — each mutant gets its own attributed last
line, exactly as `negctl-mutant-kill-after.log` receipts.

### 2e. Plain-mode equality (re-run by me, diff empty)

Working-tree input files first byte-verified equal to the committed tip
(`sha256sum` of PROVINCE.md, round-74/province_probe.sh,
round-75/province_probe2.sh, round-75/probe_negctl.sh,
round-87/probe_negctl2.sh, round-87/selftest_probe.sh — all MATCH), then
both plain modes run over the real lane root:

```
v1 plain: NEGCTL_V1_STALE_RECORD_FLAGGED=0/1 … NEGCTL_SELFTEST=pass, V1_PLAIN_EXIT=0
v2 plain: identical six value lines,                  V2_PLAIN_EXIT=0
diff of probe outputs: empty (byte-identical value lines)
```
Matches `plain-equal.log` (both exits 0, diff empty, all six
`NEGCTL_*` lines verbatim).

Reproduction note (status-neutral, no defect): the same plain-mode pair
over a plain `git archive` tarball (no `.git` dir) fails leg 3 — P2 reads
the `lane-repo` surface as `UNRECORDED-ABSENT` and both probes exit 1 with
identical value lines. The receipts were captured over the real lane
checkout, which is what the registry row's entry command (`cwd = lane
root`) documents; the selftest mode — the part the claim rests on — has no
such dependency (hermetic, runs anywhere, verified from a bare blob
extraction).

### 2f. Registry row + S473 grounding (re-measured)

```
sed -n '/^## Gate registry/,/^## 7\./p' SKILL.md | grep -cE '^\| name \|'
  base 1306ec9a → 7 ; landing 1fa086d3 → 8 ; tip 1481f490 → 8   (7 → 8 confirmed)
```
The `probe_negctl2` row carries every §Gate-standard field: kind (gate,
can fail), entry command, verdict map declaring 0/1/2/64, self-test clause
with the four committed finding-ids + both mutant attributions, pinned-value
path with both instrument shas + the two-evidences pair, write scope, owner.
S473: present at tip directly after S472, NF=13, tier A own-work, status
mined, opened 2026-11-02, used-by paths exist (`corpus/lessons/round-87.md`,
`reports/round-87/claims.md`). Located quote re-opened at base:
SCORECARD.md line 756 (r75 planned paragraph) reads verbatim "attribution
pair on the negctl harness itself, or retire/split P2 at saturation" —
matches the S473 quote character-for-character; ≤25 words holds (12 words
by whitespace, 13 counting the slash — the lane's "13" is within the bar
either way; status-neutral observation, not a defect). SOURCES census at
tip: 473 rows, 0 malformed (NF≠13), 0 duplicate ids.

### 2g. Fresh-start / holds / no-harm (receipts verified)

- Fresh-start probes re-run fresh by me: `REA_JADX_MCP_JAR=UNSET`, jadx
  not on PATH; L0 r74 question present at `.ufo/l0-questions.md` line 233
  and unanswered — agree with `freshstart-probes.log` probes 1 and 6b.
- Holds `holds-over-landing-archive.log`: evidence-verified, not
  re-executed (lane-owned probes; protocol bars executing a sibling's
  gate). All three probe blob pins re-hash-match (`mg_probe.py`
  `1840c30cf4f1cad0`, `f_probe4.py` `4d871971fa49131f`, `ag_probe2.py`
  `f9772ab1428ebe6e`); receipt internally consistent (M 3/3, F4 10/11,
  A1v2 5/5, A1 3/3, freshness 12+6=18 — the 12/6 split re-grepped by me
  over the committed knowledge bytes, K 8/15 carried).
- No-harm: protected-path scan re-run over the full range
  (`corpus/live corpus/fixtures corpus/knowledge corpus/README.md
  PROVINCE.md QUALITY.md SHONEN.md`) → empty; freeze..landing re-statted =
  2 files, 12 insertions, 0 deletions (SKILL.md additions only + the S473
  append) — matches `noharm-diff.txt`.
- Census: this session's own run — sanctioned explicit-lane-dir form exit
  0 with exactly 21 W01 + 10 W04, zero E (matches both round receipts);
  contract-literal form exit 2 (`revenger-shokunin/` not present under the
  fleet clone root — the disclosed standing operator-side defect, L0 r79
  lineage, routed around, nothing assumed answered).
- Separability `c1-only.log`: evidence-verified (single-claim round;
  instruments read only their own bytes + frozen fixture inputs; receipt
  shows base-state markers 7 rows / no S473 with green values identical).

## 3. Per-axis verdicts (spot-check table agrees with the closure JSON)

| axis | verdict | basis |
|---|---|---|
| calibration | improved | C1 re-derived end-to-end by this session (red/green/mutants/plain/registry all as receipted) |
| coverage | unchanged | lowest non-retired axis routed on documented unreachability with fresh receipts (K L0 r74 unanswered, F android gated, M/A1/A1v2 saturated, asset-catalog sentinel unchanged); F4 10/11 and K 8/15 held |
| freshness | unchanged | 18/18 stored-assertion proxy re-grepped over committed knowledge bytes; knowledge untouched in range |
| depth | unchanged | additions-only registry row (r79 precedent shape); no engine-readiness claim; trigger for the r86 conditioned depth row unmet |
| operability | unchanged | no verifier byte changed; protected paths empty; standing instruments byte-unchanged (blob pins match) |
| adjacency | unchanged | PROVINCE.md byte-unchanged; ADJ-06 remains reported, not absorbed |

No axis harmed. The single claim verifies → the round is admissible.

## 4. Discernment spot-check (re-opened sources)

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S473 source row (own-work, tier A, the criterion-N instrument-blindness evidence) | admit | re-opened: v1 bytes sha-re-derived, `negctl-v1-baseline.log` vs `negctl-red.log` contrast re-run by me (legs green / conformance red over the SAME committed bytes), quote re-read at SCORECARD.md:756 base | agree | tier A is correct for the lane's own re-runnable gate output per the CORPUS.md contract; every evidence component in the row re-derives; quote verbatim, located, ≤25 words |
| C1 claim (the pair lands + first registry row for the criterion-N instrument) | admit | re-derived in full by this session (§2a–2f) | agree | red 0/1·0/2·0/1 exit 1 and green 1/1·2/2·1/1 exit 0 reproduce exactly from committed bytes; both mutants die attributed with pin-matching shas; plain mode byte-identical; registry 7→8; the moved quantity is honestly the instrument's self-conformance + visibility, not the held 10.0 score |
| considerthese 2026-10-28 item 4 (Q16 claimed-coverage-set checker) — NOT adopted | reject | re-opened `considerthese/2026-10-28.md` item 4 ("Claimed-coverage-set check for open candidates") | agree | its natural consumers are the C05 re-gate surface, which is operator-blocked on this host (L0 r74 unanswered; r71's falsification was Q09/Q16 on exactly that surface), and it is a larger instrument than one bounded round; routing it forward (it stays in Routed-forward) is the honest disposition, not an evasion |
| fresh-start rejects: coverage/K and coverage/F android ruled out | reject (of those claims) | re-ran probes 1 and 6b fresh: `REA_JADX_MCP_JAR=UNSET`, no jadx on PATH, L0 r74 unanswered at line 233 | agree | both routes are genuinely unreachable on this host; declaring either would have been a do-nothing-control-reachable claim |

## 5. Trend verdicts (verified, agree with the report)

- **expansion: unchanged** — no knowledge admission (corpus/knowledge
  absent from the round diff), no new capability row (SCORECARD capabilities
  untouched; v2 supersedes the existing criterion-N instrument); denominators
  held (holds receipt + my freshness re-grep). Evidence: diff-tree range,
  `holds-over-landing-archive.log`, `noharm-diff.txt`.
- **quality: improved** — the twelve-round routed criterion-N debt became
  machine-caught: hermetic selftest + declared usage contract + two
  mutation-checked switches with per-mutant attribution + first registry
  row, no axis harmed (holds green, no-harm clean, additions only). Evidence:
  my §2 re-runs, SKILL.md registry diff.
- **discernment: improved** — five mistake rows mined with evidence
  pointers, four caught before any committed byte could mislead. Spot-verified:
  `mutants-prelanding.log` really carries the unapplied mutant B
  (`MUTB_EXIT=0`, no diff lines) that the over-escaping row mines;
  `freshstart-probes.log` really carries both the loose 31 (probe 3) and
  the registered 7 (probe 6); the committed `selftest_probe.sh` STRIPPED
  line matches the r79 bytes (no spurious quote — the bash -n row's fix
  landed). The honest red state (legs-green/conformance-red over the same
  bytes) is real and is the round's central evidence.

## 6. Routed items / notes for the operator (all status-neutral; nothing bars admission)

1. SHONEN boxes 2 and 3 look fully checkable by a non-author from this
   round's evidence (the evidence-ledger task is logged in the LOG.md
   round-87 block and re-derived by this session; the frozen counting
   commands and both mutant recipes were executed verbatim with exits
   matching the claims pins). Per protocol only a non-author may write
   `[x]`; this judge does not write SHONEN.md — the operator may
   re-confirm boxes 1–4 on the r87 bytes.
2. The census contract-literal form exit 2 persists (operator-side
   lineage, L0 r79) — dual receipts landed again; routed around.
3. SHONEN box 1 non-author re-confirmation stays operator-side and now
   names the r87 SKILL.md bytes (the registry row changed SKILL.md again).
4. Plain-mode reproduction environment note: over a plain archive
   extraction (no `.git`) leg 3 fails on the `lane-repo` surface; the
   receipts' documented environment (`cwd = lane root`, a git checkout)
   reproduces them exactly. Optional future hardening: name the
   git-checkout dependency in the registry row's write-scope cell.
   Status-neutral; the claim's selftest evidence has no such dependency.
5. S473 quote is 12 words by whitespace splitting (the lane says 13,
   counting `retire/split` as two); ≤25 holds under any convention.
   Status-neutral observation, recorded for precision only.

Verdict: **admitted** — the single claim verifies from committed bytes
re-measured by this session, no axis is harmed, and no material defect was
found.
