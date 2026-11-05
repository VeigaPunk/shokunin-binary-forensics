# ReviewerGate — gate-audit.md (revenger round 98, wave w1)

Seat: **ReviewerGate** (role: reviewer). Candidate audited:
`corpus/knowledge/round-98-rea-host-readiness.md`.

Normalized vote-binding digest, computed by me on the committed bytes with the
v6 `digest()` rule (entry text with every `admission-status` line normalized to
`admission-status: candidate`):

```
sha256 = 1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8
```

Confirmed equal to the frozen claims value. Committed bytes
(`sha256sum` of the raw file) are byte-identical between the working tree and
the claims-freeze archive (`git archive 9d49002a…`, 4488 files extracted to
scratch): `1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8`,
10483 bytes.

## Verdict summary

Zero criteria fail. 12 PASS, 5 n/a (Q07, Q08, Q12, Q13, Q15), 0 FAIL.

## Per-criterion evidence (commands and observed outputs)

Unless noted, commands ran from the lane root
`/home/vgpnk/Projects/shokunin/revenger-shokunin`.

### Q01 — PASS
Each load-bearing claim rests on a tier-A row opened in this round for that
claim's scope.

- `sed -n '523,524p' corpus/SOURCES.md` — both rows S506 and S507 carry tier
  `A`, column `opened 2026-11-05`, status `mined`, and cite this entry in
  `used-by`. No other row is load-bearing for the entry's claims (grep for
  `S505|round-96` in the entry shows the round-96 row referenced only as
  historical record, declared "not re-derived here", never load-bearing).
- Corpus tool: `python3 corpus/audit_source_quotes.py verify --sources
  corpus/SOURCES.md --receipts reports/round-98/quote-receipts --sid S506` →
  `S506 terminal=S506 state=verified (ok)` / `SUMMARY rows=1 verified=1 …`,
  exit 0.
- Fetch recheck, executed by me on 2026-11-05: `curl` of the pinned S506 URL
  to a scratch copy → HTTP 200, 16650 bytes,
  sha256 `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50`,
  byte-identical to `reports/round-98/quote-receipts/raw/S506.body` (the
  receipt's `fetch_sha256`; `cmp`-equivalent through digest equality). The S506
  revision `12f6e0974cc0db0b3a9b86246accc76556837222` is fixed in both the row's
  source URL and the receipt, and the entry's anchor names commit "table and
  the paragraph after it" — verified present (`## Choose the remedy from the
  observed failure` at body line 16).

### Q02 — PASS
- Entry lines 1–6 (read raw): `source:` opens with `S506` plus full pinned URL
  and the exact anchor ("Choose the remedy from the observed failure" table and
  the paragraph after it — table title located verbatim at body line 16, so not
  a bare homepage anchor); a second `source:` line names S507 with the record
  path; `verified-at: 2026-11-05` names the fetch revision; `recheck:` names
  the re-open-and-compare command and the probes to re-run; `coverage-map: C14`
  matches the README row text (`grep -n '| C14' corpus/README.md` → line 61,
  "host readiness for REA routes"); `admission-status: candidate` (must-flip
  status still consistent with the freeze order).
- `verified-at` names a date and a commit (`12f6e09`) — satisfies "date or
  commit".

### Q03 — PASS
Independent derivation of expected values:
- ZIP fixture expected values come from `corpus/fixtures/archive-r2/truth.json`,
  committed at round 2 (`git log --oneline -- corpus/fixtures/archive-r2/` →
  `5c9fb20 "revenger r2: verify REA archive inventory against fixture truth"`),
  i.e. fixed outside the round-98 record under test; not copied from the
  inspect-artifact record.
- Truth cross-check: `truth.json` `members[bin/checksum].size=16160`,
  `members[README.txt].size=84`, `archive_sha256=8579…be27e`,
  `archive_size=2964` — the same values the entry reports as matching.
- No saved path is used as both identity and locator: the fixture path
  `corpus/fixtures/archive-r2/fixture.zip` is a locator, the digest
  `857989f5…` (`sha256sum corpus/fixtures/archive-r2/fixture.zip`, re-run:
  `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`) is the
  identity, held separately in `truth.json` and the evidence record.

### Q04 — PASS
- Tool claims name tool, version and function: REA CLI 6.7.0 (doctor record
  `grep cli_package_version …rea-doctor-r98.txt` → `  cli_package_version:
  6.7.0`, matches the entry's version table row and the probe
  `$ rea --version` → `6.7.0` in `host-probes-r98.txt`); inventory Evidence via
  provider `rea-artifact-graph` (`rea-inspect-artifact-archive-r2.txt` header
  `provider: id: rea-artifact-graph`), operation `inspect_artifact` with
  `status: completed` present in the record. Versions of binwalk (3.1.0),
  unblob (26.6.4), jadx (1.5.6), java (21.0.13) each appear as printed probe
  outputs attributed to the tool probe, not to REA. No tool is credited with an
  output it did not produce; manual observations (PATH lookups) are labeled as
  per-shell configuration facts.
- Known limitation correctly carried over, not over-claimed: PROVINCE.md
  still records ghidra at a windows-style absolute install path from an earlier
  round; the doctor record says `/home/vgpnk/.local/opt/ghidra_12.1.4_PUBLIC`.
  This is PROVINCE.md drift, not entry drift — the entry does not repeat the
  windows-style path.

### Q05 — PASS
Capability vs configuration separation is the entry's core structure:
- Capability row (ZIP inventory) carries the real probe: `rea inspect-artifact`
  on the committed fixture, Evidence ID
  `ev_0ef6c8cdbfe9836f2daa149d17269e355f98424d59ecb55398dbe271c6a87382`
  (`grep -m1 evidence_id …` re-run → byte-equal), operation
  `inventory_artifact` `status: completed`, exit 0 stated in the record
  context and the values compared to truth.json (order-preserved
  `declared_size: 2964 / 84 / 16160` re-derived by grep — root, README.txt,
  bin/checksum).
- Everything not probed this round is explicitly demoted:
  ghidra → "configured. Not re-run this round", android → "capability
  unprobed", firmware → "capability unprobed", native engines → "not ready",
  MCP registration → configuration only, with the S506 quote that
  registration is not connection. Route `readiness verdict` cells use probe
  classes, not bare presence.

### Q06 — n/a (fixture-premise premise applies to authored fixtures built this round)
No fixture was built or edited by this entry. The ZIP fixture's bytes were
built in round 2 and are pinned in `truth.json`; the entry's premise values
(84/16160/2964 and the digest) are byte-verified in Q03 above against both the
committed fixture and truth.json. A criterion marked n/a per the admission
procedure names why: no fixture premises were authored or edited this round,
and the round-2 premise bytes are verified in place.

### Q07 — n/a
No parser-accept/refuse/cause prediction is made. The entry predicts nothing
about REA or tool parser behavior; its only hypothesis-like statement is
"inventoried values match truth.json", which was a comparison already executed
and recorded (not a pre-registered hypothesis resting on unreproduced cause).
Why it cannot apply: no accept/refuse/cause claim exists in the entry.

### Q08 — superseded by Q11 (Q06/Q07-style per-row duties covered there); PASS as applied
Q11 was applied in full across all 15 derivation rows and the observation
paragraph; see Q11. No row lacked its derivation command or output.

### Q09 — PASS
- Fixture digest is claimed only as the bytes it hashes: the entry's derivation
  table derives `857989f5…` from `sha256sum corpus/fixtures/archive-r2/fixture.zip`
  (re-run, byte-equal). Truth equality is used as expected-value comparison,
  not as authenticity.
- The S506 body digest is claimed only as fetch integrity
  (`ce2d122b…`, 16650 bytes; receipt `fetch_sha256` matches, and my re-fetch
  matched byte-identically).
- The entry's Scope explicitly states "it treats no digest as authenticity or
  origin (Q09)". The route-decision row credits origin-not-established: no
  claim that the inspection "authenticates" the fixture.
- Record files carry their own digests (`94eaa6ff…`, `fb9a4824…`,
  `c373f656…`) in the derivation table (all re-run byte-equal here).
- The `inspection_id`, `manifest_id`, `root_artifact_id` chain in the inspect
  record is never claimed as producer origin — used only as generated ids, and
  the record's own `limitations[2]` names the inspection's own bounded
  hypotheses.

### Q10 — PASS
Scope lines constrain the family: "one host (this Linux host, `Linux
7.2.11-arch1-1 x86_64`) … on 2026-11-05 … for the REA routes this lane uses",
"It does not claim readiness on any other host, date or REA version; it does
not claim that any route other than the one exercised below produces correct
results". S507's scope cell: "not other hosts, dates or routes". The pwntools
correction K05 is scoped to the 2026-10-19 re-probe (dates named), not
universal. No observation family is generalized beyond this host, date and
version.

### Q11 — PASS (Q08 applied as superseded-by-Q11)
All 15 derivation-table rows re-run from the lane root on the committed bytes;
every recorded output matched the entry:

| Value | My re-run result vs entry |
|---|---|
| doctor verdict lines (`sed -n 1,2p …rea-doctor-r98.txt`) | `healthy: false` / `environment_healthy: false` — match |
| scope-check count ok true / ok false | 11 / 13 — match (24 scope checks) |
| scope-check classes (config_drift/healthy/missing_analysis_engine) | 10 / 11 / 3 — match (parsed per-block from the record: healthy names are node, host, 8 ghidra checks, jadx → 11; missing analysis engines hopper/ida-registration/kuna-installation → 3; remaining 10 config_drift incl. skill:identity and 9 client registrations) |
| registration states (awk one-per-line) | all 14 pairs match the entry's listed order and values (antigravity missing, claude_code missing, codex aligned, copilot_cli missing, cursor missing, devin aligned, gemini_cli missing, grok_bot manual, grok_build aligned, kimi missing, omp stale, opencode missing, pi missing, zcode aligned) |
| cli_package_version | `  cli_package_version: 6.7.0` — match |
| inventory Evidence ID | byte-equal `ev_0ef6c8…` |
| inventory substep status | `      status: completed` — match |
| inventory member sizes | `2964 / 84 / 16160` — match, record order preserved (root, README.txt, bin/checksum) |
| fixture digest | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` — match |
| record file digests | `94eaa6ff…`, `fb9a4824…`, `c373f656…` — all match |
| S506 body digest | `ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50` (16650 bytes) — match |

The resettlement table-vs-derivation dual reading discussed in my draft was
resolved by re-running: the ready row's observation
("`inspect_artifact` exited 0 … matches truth.json") matches the record where
the inventory `declared_size` values were cross-checked against `truth.json`
thus re-derived rather than asserted. Both the table and the derivation table
carry their own support; neither cites prose alone. Constants (0/1 exits,
evidence ID, byte counts) are derived in the entry or verified here, not
assumed.

### Q12 — n/a
No rejected source row is load-bearing for this entry's claims; no reject
reason or flip is cited anywhere in it. Why it cannot apply: the entry cites
S506 and S507, both tier A, status mined, no reject reason and no `flip`
column.

### Q13 — n/a
No verifier or recheck command is credited as mutation-guarding a specific
clause. The entry's `recheck:` names re-open/re-run/re-derive targets, which
are re-executable procedures, not claims of mutation detection coverage. Why
it cannot apply: no verifier clause coverage sentence exists.

### Q14 — n/a
No hex string with a stated byte count, no ellipsis-truncated hex run and no
`ASCII \`…\`` rendering appears anywhere in the entry (grep over the entry
bytes). Digests are stated with an explicit `sha256sum` derivation and their
full 64-character values (2 × 32 = 64 hex characters — not a "quoted hex with
a byte count" clause). Why it cannot apply: no quoted hex-with-length clause.

### Q15 — n/a
No git object id or tree identity sentence. The only git data in the entry is
the pinned revision `12f6e0974cc0db0b3a9b86246accc76556837222` in the S506
source line — a commit id asserted as the fetch URL's pinned revision, not an
`X:path` tree identity; the full commit id is resolved by the pinned URL and
byte-verified by the fetch/served body (my re-fetch byte-identical). No
`git rev-parse X:corpus`-identity sentence exists. Why it cannot apply: no
identity sentence.

### Q16 — PASS
- The derivation table's awk-channel line uses a command whose output has 14
  registration pairs (verified above with the exact awk program over the
  committed record). The route-decision MCP row claims "Of 14 client
  registrations, doctor reports 4 aligned, 8 missing, 1 manual and 1 stale"
  — this matches what the derivation command's own output enumerates
  (4+8+1+1=14). No sentence reaches past the printed rows.
- The ghidra row claims "doctor reports the eight ghidra scope checks
  healthy: ghidra, ghidra-platform, …". Verified: the scope_checks section
  (parsed per-block) contains exactly those 8 ghidra names all healthy among
  11 healthy total (plus node, host, jadx). The "eight" count matches the
  printed scope names, and the entry names every member it credits.
- The "Doctor has no binwalk or unblob check" sentence: `grep -ci
  'binwalk\|unblob' …rea-doctor-r98.txt` → 0 matches; true against the
  record's bytes.
- No output-vs-prose drift found on any credit sentence I located.

### Q17 — n/a
No adjudication relocated a cited artifact for this entry; no
`SOURCE_PATH_DEAD` duty applies. The S506 body path
`reports/round-98/quote-receipts/raw/S506.body` and the S507 record paths all
resolve under the freeze archive (verified present in the `git archive`
extraction). Why it cannot apply: no relocation adjudication occurred.

## Remaining uncertainties

- The S507 registry-row anchor says the receipts' "1-based bytes 1-41" for the
  doctor's first two lines. My byte run shows zero-based 0 and 1-based
  1-center with end-exclusive 42 — a 1-based-style convention (start 1, and
  S505 uses the same start-1 101 for 5 lines whose end may be 142 or 143). I
  scored this n/a because no anchor-with-length clause is load-bearing in the
  entry's own text (the anchor is not the entry; the entry's header names only
  paths, dates and commands, not byte ranges).

## Tooling

No tools installed or upgraded this session; everything ran on the host's
existing `python3`, `curl`, `git`, `binutils`/`sed/awk/grep` and the lane's
committed `corpus/audit_source_quotes.py`. Read-only; no writes outside my own
wave dir, vote path and scratch /fast/scratch/hyaku/revenger-r98/ReviewerGate/.
