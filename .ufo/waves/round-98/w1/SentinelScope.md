# SentinelScope — round 98, wave w1 (lane revenger-shokunin)

Seat: `SentinelScope` (sentinel). Scope of this sweep: credential material in the new round-98
records, registry-row hygiene for S506/S507, write-scope adherence (fleet-root misroot check),
and the candidate's scope sentences against `PROVINCE.md` / Q10.

Lane commit when the sweep ran: `cf8a9d4` (claims freeze `9d49002` + claims Amendment A).
All commands below were run from `/home/vgpnk/Projects/shokunin/revenger-shokunin` unless the
path says otherwise. Read-only; nothing in the lane was edited.

Raw receipts in this seat's dir: `SentinelScope/credential-scan.log`, `SentinelScope/census-now.txt`,
`SentinelScope/census-frozen.txt`.

---

## Item 1 — credential / secret scan of the new records

Trees scanned: `corpus/live/runs/round-98/` (3 files), `reports/round-98/` (all files present at
scan time, incl. `controls/`, `quote-receipts/`, `votes/`, `forgeries7/`, the v7 counter and
`forge_reach7.py`), plus the candidate entry `corpus/knowledge/round-98-rea-host-readiness.md`.

Commands (exit code in brackets; `1` = no match):

```
grep -rniE '(api[_-]?key|secret|token|password|passwd|bearer|authorization|auth[_-]?header|cookie|session[_-]?id|private[_-]?key|BEGIN [A-Z ]*PRIVATE KEY)' \
     corpus/live/runs/round-98/ reports/round-98/ corpus/knowledge/round-98-rea-host-readiness.md   [1]
grep -rnoiE '(npm_[A-Za-z0-9]{20,}|pypi-AgEI[A-Za-z0-9_-]{20,}|gh[pousr]_[A-Za-z0-9]{20,}|glpat-[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{30,}|sk-ant-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|Bearer[[:space:]]+[A-Za-z0-9._-]{15,})' \
     corpus/live/runs/round-98/ reports/round-98/ corpus/knowledge/round-98-rea-host-readiness.md   [1]
grep -rnoiE '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' corpus/live/runs/round-98/ reports/round-98/   [1]
grep -rniE '(mcpServers|"env"|"argv"|api_key|apiKey|client_id|client_secret)' \
     corpus/live/runs/round-98/ reports/round-98/ corpus/knowledge/round-98-rea-host-readiness.md   [1]
grep -rnoE '/(root|home/[a-z][a-z0-9_-]*|etc|var/lib|opt)/[A-Za-z0-9._/-]*' corpus/live/runs/round-98/ reports/round-98/ | grep -v '/home/vgpnk/'   [1]
grep -rnoE '/home/vgpnk/\.(ssh|aws|gnupg|config/gcloud|npmrc|netrc|docker|kube|azure)|/etc/(shadow|passwd)|\.netrc|\.npmrc|id_rsa|\.pem$|\.p12$|\.keystore' \
     corpus/live/runs/round-98/ reports/round-98/ corpus/knowledge/round-98-rea-host-readiness.md   [1]
```

**Hit counts: 0 credential material, 0 token values, 0 e-mail addresses, 0 config-file contents, 0
paths outside `/home/vgpnk`, 0 secret-dir paths.** The only keyword hits anywhere in the two trees are
the English word "token" in non-secret senses (`claims.md` "64-hex digest token"; the v7 counter's
`sid_tokens`/`digest token` code; `skip-work-table-r98.md` "sid token"). No hit line contains a value.

Long hex/base64 blobs in the records are all digests: the S506 body digest
`ce2d122b873fb84d98cdb56afd84a34ee8de362b65760855838dfb29c2282e50` (matches
`reports/round-98/quote-receipts/S506.receipt.json`), the fixture digest
`857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` (matches
`corpus/fixtures/archive-r2/truth.json`), the catalog digests in the doctor receipt, and the
Evidence/manifest/substep ids in the inspect-artifact receipt. `S506.body` (a public upstream
README) contains no credential string (`grep -c` = 0).

**Home-directory config paths — are any sensitive?** The doctor receipt prints 14 client-registration
config paths under `/home/vgpnk/`: `.claude.json`, `.codex/config.toml`, `.config/devin/mcp_config.json`,
`.config/opencode/opencode.json`, `.copilot/mcp-config.json`, `.cursor/mcp.json`,
`.gemini/config/mcp_config.json`, `.gemini/settings.json`, `.grokbot`, `.grok/config.toml`,
`.kimi-code/mcp.json`, `.omp/agent/mcp.json`, `.pi/agent/mcp.json`, `.zcode/cli/config.json`. These are
the paths `rea doctor` prints, with registration **states** and the command
`npx -y rea-agents@6.7.0 mcp` — no file content, no key, no cookie, no auth header, no env dump.
**None is sensitive as credential material.** They do disclose (a) the local user name `vgpnk`,
(b) which AI clients are configured on this host, and (c) for `grok_bot` only, that its connectors live
in a signed-in hosted account (that is the tool's own remediation text, and it explicitly advises
*not* to put credentials in the command). Two further non-home paths appear:
`/usr/lib/jvm/java-21-openjdk` and `/usr/bin/ghidra` (system paths), plus per-shell launcher paths
`/run/user/1000/fnm_multishells/<id>/bin/rea` (discloses uid 1000 and a shell id — not sensitive).
Precedent: the committed round-96 doctor record (`corpus/live/runs/round-96/rea-doctor-r96.txt`)
prints the same class of home config paths, so this is not a new disclosure category.
One path outside the home dir appears only in the fetched upstream body
(`/absolute/path/to/app`, `S506.body:198`) — example text from the upstream README, not a local path.

**Verdict item 1: PASS.** No credential material in the new records; no path beyond the
home-directory config paths that `rea doctor` prints; nothing sensitive in those paths.

---

## Item 2 — registry-row hygiene for S506 / S507

Rows live at `corpus/SOURCES.md:523` (S506) and `:524` (S507), inside the `## Registry` section
(headings: `## Registry` line 11, `## Paths` line 526), so no E12 "row outside Registry" applies.

**Column count.** The registry table header is `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`
(11 columns). For both new rows:

```
awk -F'|' 'NR==523{print NF}' corpus/SOURCES.md   -> 13     # NF-2 = 11 columns
awk -F'|' 'NR==524{print NF}' corpus/SOURCES.md   -> 13
sed -n '523,524p' corpus/SOURCES.md | grep -o '|' | wc -l   -> 24 total (12 per row)
```

NF = 13 means 11 content columns, exactly the SOURCES-CONTRACT-v1 shape the census enforces
(`E01 fields=%d` when `NF!=13`). A literal `|` inside any cell would have raised NF above 13 — it did
not. **11 columns confirmed for both rows.**

**No literal or escaped `|` in a cell.**

```
sed -n '523p' corpus/SOURCES.md | grep -o '\\|' | wc -l   -> 0
sed -n '524p' corpus/SOURCES.md | grep -o '\\|' | wc -l   -> 0
sed -n '523,524p' corpus/SOURCES.md | grep -cP '(?<!\\)\\\|' -> 0
```

Cell-by-cell split (`awk -F'|'`) of both rows shows the intended 11 fields with no embedded pipe and
no stray delimiter. **Confirmed.**

**Census.**

```
scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
```

exit code **0**. Output: 34 `W`-lines, **0 `E`-lines**, final line
`revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md`.
The output is **byte-identical** to the frozen control
`reports/round-98/controls/census-after-append.log` (after stripping that file's one `#` header
line): `diff` of the two is empty. Zero census lines mention S506 or S507 — the new rows raise no
warning and no error. The W-lines are the pre-existing duplicate-URL (W04) and tier-C-mined-used-by
(W01) warnings already present at the freeze.

**Grounding (the row-level hygiene the C1_USEDBY_GROUNDED leg will check).** S506 and S507 both carry
`used-by = corpus/knowledge/round-98-rea-host-readiness.md`, that file exists, and it cites both ids
as whole words: `grep -coE '\bS506\b'` → 15 lines, `grep -coE '\bS507\b'` → 5 lines. The candidate
entry cites neither S505 nor S504, so it does not create a second ungrounded pair. (The pre-existing
S505 ungrounded pair is out of this sweep's row set and is the subject of Amendment A2 /
`reports/round-98/controls/s505-usedby-fix.diff`; at freeze commit `9d49002` S505's used-by still
named `corpus/knowledge/round-96-native-analysis-sessions.md`, which cites S504 three times and S505
zero times.)

**Verdict item 2: PASS.** 11 columns on both rows, no literal or escaped `|` in any cell, census exit
0 with byte-identical output to the frozen after-append control.

---

## Item 3 — write-scope adherence: fleet-root untracked files naming revenger round 98

Run at the end of the sweep, from the fleet root:

```
git -C /home/vgpnk/Projects/shokunin status --porcelain
 M .scratch/run15-kernel.py
 M .scratch/run15-state.json
 M .ufo/l0-questions.md
?? repofind-link
?? w4lines.txt
```

**Untracked fleet-root files: 2.** Neither names revenger round 98:

| file | content | revenger / r98 mentioned? | disposition |
|---|---|---|---|
| `w4lines.txt` (mtime 16:57, before wave start 17:55) | 25 bare line numbers (65 … 2490) | **no** (`grep -c` = 0) | not a revenger round-98 artifact; not created by this wave |
| `repofind-link` (mtime 18:11) | symlink → `/home/vgpnk/Projects/shokunin/m-rev-vs-rev.py`, a souji coverage-agreement instrument | **no** (`grep -c` = 0 in the target) | not a revenger round-98 artifact |

**Modified fleet-root tracked files: 3**, all dispatcher/hyaku-owned, none carrying revenger round-98
content: `.scratch/run15-kernel.py` and `.scratch/run15-state.json` (hyaku kernel/state) and
`.ufo/l0-questions.md`, whose diff adds only `kagi | round-45` and `kotodama | round-96` lines
(`git diff -- .ufo/l0-questions.md | grep '^+' | grep -i revenger` → no match).

**Conclusion: no untracked fleet-root file names revenger round 98 — no misroot by a seat of this
wave.** The only file anywhere under the fleet root that names revenger round 98 and is not tracked
is the git-ignored dispatcher log `.ufo/state/inline-dispatcher.log`
(`114308: l1 RevengerR98`, `114314: cap-defer …/revenger-shokunin/.ufo/waves/round-98/w1.ready`),
which is hyaku's own runtime log, not a seat artifact.

**Lane-side write scope.** `git -C revenger-shokunin status --porcelain` shows only
`?? .ufo/waves/round-98/` — no tracked file in the lane is modified except `reports/round-98/claims.md`,
which was amended by the L1 in commit `cf8a9d4` (authorized: the L1 decides amendments before the
v7 freeze). `git diff 9d49002 -- corpus/ reports/round-98/claims.md SCORECARD.md LOG.md SKILL.md
PROVINCE.md` lists **only** `reports/round-98/claims.md | 44 +++++` — the frozen corpus, the frozen
`reports/round-98/controls/` files that existed at `9d49002` and `reports/round-98/quote-receipts/`
are byte-unchanged. Nothing under `corpus/` was edited, so the two things seats must not touch are
untouched: `corpus/README.md` C14 is still `partial` and the candidate's `admission-status` is still
`candidate`.

**Verdict item 3: PASS.** No misroot; no seat wrote outside its lane or the fleet root outside
dispatcher-owned files.

---

## Item 4 — candidate's scope sentences against `PROVINCE.md` / Q10

Q10 (`corpus/QUALITY.md:22`, `SKILL.md:168`): *a finding is scoped to the observed family,
operation, version and input*; the failure mode is *one family's observation stated as a universal*.

**Is any scope sentence a general host claim? No — the candidate is host-and-date scoped and says so
twice.** Scope section, sentences 1–4:

- "This entry records what one host (this Linux host, `Linux 7.2.11-arch1-1 x86_64`) showed on
  2026-11-05 for the REA routes this lane uses …"
- "It does not claim readiness on any other host, date or REA version; it does not claim that any
  route other than the one exercised below produces correct results; and it treats no digest as
  authenticity or origin (Q09)."

Every route verdict in the decision table sits under the heading `## The host on 2026-11-05 (S507)`
with the column header `Observation on 2026-11-05`, so "not ready" (Hopper/IDA/Kuna), "the omp
registration is stale", "present, capability unprobed" etc. are table-scoped observations, not
universal readiness claims. `PROVINCE.md` places REA engine/registration readiness inside this lane's
domain ("server registration and engines are the lane's readiness domain"), and the entry covers
exactly the engines `PROVINCE.md` lists (Ghidra, IDA, JADX, Binwalk/Unblob, pwntools) — no scope
creep into another province, no cross-lane absorption. `PROVINCE.md`'s own host facts are dated
(2026-10-31 / 2026-11-01) and the entry is dated 2026-11-05, so the differing CLI version (6.8.0 in
PROVINCE vs 6.7.0 observed) and engine presence are not contradictions.

**Two advisory observations (Q10-adjacent, both in S506-derived material, not host claims):**

- **O1 — over-generalised tool claim in the S506 registry cell and the entry's boundary table.**
  The quoted source sentence is "Static JavaScript and ordinary ZIP inventory need neither Hopper nor
  Ghidra." The S506 `teaches` cell generalises it to "**a missing native engine** does not block ZIP or
  static JavaScript routes", and the entry's boundary table repeats "A missing native engine does not
  block the static JavaScript or ZIP-inventory routes." The source names two engines; the cell states
  a rule about any engine, and drops "ordinary" from "ordinary ZIP inventory". The scope cell
  ("not provider execution or route correctness on any host") does not re-scope that sentence.
  Smallest remediation: narrow the cell to the two named engines, or cite the doc's own wording.
- **O2 — a host-scoped observation carrying a general conclusion.** The S507 `teaches` cell reads
  "On this host an unhealthy overall doctor verdict coexists with a working ZIP-inventory route, so
  the overall verdict is not a route verdict", and the entry's Inference paragraph ends with
  "**A failing overall doctor verdict is therefore not a readiness verdict for a given route.**" — the
  sentence drops the host/date qualifier its antecedent carries. It is supported in substance by
  S506's own sentence ("Doctor checks registration; it cannot establish the current agent's
  connection"), so it is not a bare one-host generalization, but the sentence as written is not
  host-scoped.
- Also noted: the entry marks its third boundary row as a paraphrase and locates it at "body lines
  35–37"; that is correct (body lines 35–37 carry "Native decompilation, Android analysis and
  firmware extraction have their own bring-your-own prerequisites"), but the paraphrase adds "each"
  to the source's collective "have their own". It is explicitly labelled a paraphrase, so this is
  acceptable.

**Verdict item 4: PASS on the question asked** (no general *host* claim; scope sentences are
host/date/route-scoped and explicitly disclaim other hosts, dates and versions), **with O1 and O2
recorded as advisory observations for the L1 to weigh before the v7 freeze.**

---

## Additional findings on the candidate (outside the four numbered items, for the L1)

These are recorded because they touch the coverage claim's correctness. They are **not** votes and do
not change the vote-binding digest; they are inputs to whatever the L1 decides.

**F1 (medium) — two asserted exit codes are not in any committed byte.** The entry states
"`rea doctor` … The run exited 1" and "`rea inspect-artifact corpus/fixtures/archive-r2/fixture.zip`,
which exited 0", and the S507 `scope` cell says "the `rea doctor` receipt (CLI 6.7.0, exit 1)".
No committed round-98 byte records either exit code: `corpus/live/runs/round-98/rea-doctor-r98.txt`
and `…/rea-inspect-artifact-archive-r2.txt` contain no exit/rc marker, and
`…/host-probes-r98.txt` covers 13 probes (`rea --version`, `command -v rea`, `node`, `npm`,
`binwalk`, `unblob`, `jadx`, `java`, `command -v analyzeHeadless`, `command -v ghidra`,
`command -v idat64`, `command -v hopper`, `python3 -c 'import pwn'`) — **neither `rea doctor` nor
`rea inspect-artifact` is among them**. The entry's own derivation table states "Every value above was
derived from the saved record by the command shown", so these two prose values breach the entry's own
derivation contract; `exited 1` is at best inferable from `healthy: false`, and `exited 0` is not
inferable from the record at all. Every other derivation-table row re-derives cleanly from the
committed bytes (scope-check count `11`/`13` of 24; classes `10 config_drift` / `11 healthy` /
`3 missing_analysis_engine`; the 14 registration states and their 4 aligned / 8 missing / 1 manual /
1 stale split; `cli_package_version: 6.7.0`; evidence id `ev_0ef6c8cd…`; `status: completed`;
`declared_size: 2964 / 84 / 16160`; fixture digest `857989f5…`; record-file digests `94eaa6ff…` /
`fb9a4824…` / `c373f656…`; S506 body digest `ce2d122b…` = 16650 bytes). Smallest remediation: add the
two exit codes to `host-probes-r98.txt` and the derivation table, or soften the prose to what the
record carries.

**F2 (low-medium) — the checklist the entry supersedes is described by a stale re-probe.** The
entry's scope says it supersedes "the pre-contract 2026-10-12 checklist
(`knowledge/2026-10-12-rea-readiness-checklist.md`, re-probed 2026-10-19)" and its pwntools row says
"This corrects the 2026-10-19 re-probe row K05, which recorded the import as failing". But that same
file has a later section, `## Re-verification 2026-11-04 (Linux host, this machine)` (line 48), whose
K05 row already reads "pwntools imports | STALE -> all four present" — i.e. the correction the entry
claims to make was already made on this same host on 2026-11-04, and the file's most recent re-probe is
2026-11-04, not 2026-10-19. The entry's description of the artifact it supersedes is one re-probe
cycle behind. Smallest remediation: cite the 2026-11-04 section as the superseded state (and drop or
re-scope the "corrects K05" claim).

**F3 (low) — anchor-byte convention in the S506 row.** The S506 `anchor` cell says
"… (body bytes 7126-7202)". The receipt's `span` is `{start: 7126, end: 7202}` in the committed
auditor's 0-based half-open slice semantics (`corpus/audit_source_quotes.py:103-107`,
`text[s:e] != quote`), and
`python3 -B corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts reports/round-98/quote-receipts --sid S506`
returns `S506 terminal=S506 state=verified (ok)`, exit 0. Under a 1-based inclusive reading — the
convention the sibling rows use explicitly ("1-based bytes 101-142" for S505, "1-based bytes 1-41" for
S507, both of which I byte-verified) — 7126–7102 spans 77 bytes and includes the newline before the
quote; the quote's own 1-based range is 7127–7202. The receipt is internally consistent and verifies;
only the registry cell's wording is ambiguous. Smallest remediation: label the span
"(0-based half-open, as in the receipt)" or write the 1-based range 7127-7202.

**F4 (informational) — everything else I re-derived from the record matched.** Scope-check totals
(24 checks, 11 ok / 13 not-ok), the eight `ghidra*` scope checks, the nine stale/missing client
registrations plus the stale installed skill identity, the three `missing_analysis_engine` engines,
the three `fnm_multishells` installation paths with `state: multiple`, the `grok_bot` remediation
text, `expected_skill_version "42"` vs `installed_version "42"` with `state: stale`, the
`evidence_id`/`inspection_id`/`manifest_id`/`artifact_id` chain, the fixture members against
`corpus/fixtures/archive-r2/truth.json` (`README.txt` 84 B, `bin/checksum` 16160 B, root 2964 B,
digest `857989f5…`), and the entry digest itself:
recomputing the v6 `digest()` rule (admission-status lines normalized to `admission-status: candidate`)
over `corpus/knowledge/round-98-rea-host-readiness.md` gives
`1ea9260c812947d3e2c61161c22a1e143df432168e7b9b5bc4c1a90c0b1527b8` — **identical to the frozen
vote-binding digest in `reports/round-98/claims.md`**. The vote-binding digest therefore still binds
the committed entry bytes; no seat has edited the entry.

---

## Tooling

No tool was installed or upgraded for this sweep; nothing was written outside this seat's wave dir
and scratch. `pacman` was not invoked. The `pacman` guard (all transactions paused host-wide) was
therefore not engaged.

## Scratch

Scratch root `/fast/scratch/hyaku/revenger-r98/SentinelScope/` held only the census and scan receipts
above; they were copied into `.ufo/waves/round-98/w1/SentinelScope/` and the scratch dir was deleted
before this report was written. (Note for the fleet: `ConnectorScope-23` reported deleting the parent
`/fast/scratch/hyaku/kake-r97` and its siblings; this seat's scratch lives under
`/fast/scratch/hyaku/revenger-r98/` and was not affected — verified present and intact throughout.)

## Open questions for RevengerR98

1. F1 — do the two asserted exit codes (`rea doctor` 1, `rea inspect-artifact` 0) get added to the
   record, or does the prose get narrowed to what the committed bytes carry? (Would touch the entry
   bytes and hence the vote-binding digest, so it must be decided before the votes are relied on.)
2. F2 — should the entry cite the checklist's 2026-11-04 Linux-host re-verification as the superseded
   state instead of the 2026-10-19 row?
3. O1/O2 — narrow the S506 `teaches` cell to the engines the source names, and re-scope the
   "overall verdict is not a route verdict" sentences to the host/date they were observed on?
4. F3 — label the S506 anchor byte span unambiguously.
