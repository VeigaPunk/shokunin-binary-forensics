# CriticR96 findings — round 96 w1 (fresh forgeries vs the frozen v5 counter, C02 entry audit)

Seat: CriticR96 (critic). Lane: revenger-shokunin. Candidate digest bound by this seat's
vote: `2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`
(re-derived from `corpus/knowledge/round-96-native-analysis-sessions.md`; raw file sha256
equals the normalized digest because the entry's status line is already `candidate`;
freeze-commit bytes at `ff767436feed32cf2f4074f05f938f8cea98e69a` equal the working-tree
bytes). Frozen predicate untouched: every forgery below ran against frozen
`reports/round-96/c1_k_admit_counter5.py` on fixture copies built by that counter's own
`_fixture` generator, driver `receipts/drv.py`, every invocation `python3 -B`,
`HYAKU_SCRATCH` pointed inside this seat's scratch. Per-forgery receipts:
`receipts/FG*.json` + `receipts/FG*.log`; aggregate `receipts/summary.json`.
Result line: `BATTERY_DONE forgeries=19 undecided=0 []` — 13 counter PASSES (findings
F1–F13), 6 kills (K1–K6). All findings route to r97; none changes the frozen C1/C2
predicate (claims.md kill rule: survivors are a miss, not a counter edit).

## A. Counter findings — forgeries that PASS `c1_k_admit_counter5.py --tree` (route to r97)

Command shape for every finding:
`PYTHONUTF8=1 python3 -B reports/round-96/c1_k_admit_counter5.py --tree <fixture-root>`
(run with cwd = lane root; fixture built by importing the counter module and calling its
own `_fixture(work)`; entry-mutating forgeries re-pin the three votes to the new digest —
the forger owns the tree, which is the counter's own threat model).

**F1 — C1_ADMITTED_UNION evaded by a decorated admitted line.**
Planted `corpus/knowledge/shadow-r96-decorated.md`, status line
`admission-status: admitted (round-96 gate, two reviewer votes)`.
The union regex `^\s*admission-status\s*:\s*admitted\s*$` demands the line END at
`admitted`; any suffix evades it. Counter output: `C1_ADMITTED_UNION=pass`,
`C1_VERDICT=pass`, rc 0 (`receipts/FG01-shadow-decorated-admitted.log`).
Smallest safe correction for r97: drop the `$` anchor (match
`^\s*admission-status\s*:\s*admitted\b`).

**F2 — union scan is non-recursive.**
Planted `corpus/knowledge/nested/shadow-r96-nested.md` with the exact canonical line
`admission-status: admitted`. `check_admitted_union` uses `kd.glob("*.md")` (top level
only) → shadow invisible. Output: `C1_ADMITTED_UNION=pass`, `C1_VERDICT=pass` (FG02).
Fix: `rglob("*.md")`.

**F3 — union scan is case-sensitive on the extension.**
Planted `corpus/knowledge/shadow-r96-caps.MD` (canonical admitted line). `glob("*.md")`
misses `.MD` on a case-sensitive fs. Output: `C1_ADMITTED_UNION=pass`,
`C1_VERDICT=pass` (FG03). Fix: suffix test lowercased.

**F4 — undecodable knowledge files are silently skipped by the union leg.**
Planted `corpus/knowledge/shadow-r96-latin1.md` with bytes ending in a lone `\xe9`
(invalid UTF-8) plus the canonical admitted line. `read_text` raises UnicodeError, the
leg `continue`s → shadow invisible. Output: `C1_ADMITTED_UNION=pass`, `C1_VERDICT=pass`
(FG04). Fix: scan bytes (e.g. regex over decoded-errors="replace" text), or fail the leg
on undecodable knowledge files.

**F5 — vote artifact may carry seat+digest ONLY inside an HTML comment.**
ReviewerGate's artifact replaced with
`<!-- wave round-96 evidence; seat ReviewerGate binds candidate 2f7d…d923; all
substantive content withheld -->` (sha re-pinned). The counter's containment checks are
raw substring tests over the bytes; comment-only content passes `is_file`, non-empty,
seat-in-bytes, digest-in-bytes, sha, distinctness. Output: `C1_VOTES=pass`,
`C1_VERDICT=pass` (FG05). Observation, not an evasion of the frozen rule's letter (the
rule says bytes must contain both strings) — routed as a calibration note: nothing
requires visible substantive evidence.

**F6 — own-dir rule is a string prefix; a symlink resolves into a sibling's dir.**
Planted `…/w1/ReviewerBlind/planted-shared.md` (names BOTH seats + digest); made
`…/w1/ReviewerGate/link.md` a symlink to it; ReviewerGate's vote `artifact_path`
= `.ufo/waves/round-96/w1/ReviewerGate/link.md`. The prefix check passes; the resolve
check only requires containment in the WAVE dir, not the seat's own dir; sha is fresh
bytes so distinctness passes. Output: `C1_VOTES=pass`, `C1_VERDICT=pass` (FG06).
Fix: `resolved.is_relative_to((root / f"{WAVE_DIR}/w1/{seat}").resolve())`.

**F7 — sid citations with two spaces or lowercase are invisible to C1_SIDS/C1_SOURCES.**
Appended prose `Per S  0999 and s0888 the atlas approach generalizes.` (votes re-pinned).
Token regex `\bS\s?\d{2,}[a-z]?\b` allows at most one whitespace and is case-sensitive →
neither token collected → no unresolved-sid failure. Output: `C1_SIDS=pass`,
`C1_SOURCES=pass`, `C1_VERDICT=pass` (FG07). Fix: widen the token pattern
(`S\s*\d{2,}` case-folded) and normalize before lookup.

**F8 — loose `.pyc` files evade C1_PYCACHE (M5/M8 close matches only `__pycache__` dirs).**
Planted `corpus/lint_entry_r96.pyc` (no `__pycache__` directory anywhere).
`check_pycache` rglobs `__pycache__` only. Output: `C1_PYCACHE=pass`, `C1_VERDICT=pass`
(FG08). Same defect class as r94 M5 / r95 M8. Fix: flag `**/*.pyc` (and `**/*.pyo`)
under the audited surfaces. (Case variants of the directory name would evade rglob too.)

**F9 — receipt quote can anchor an irrelevant sentence; quote↔anchor-cell binding is
dead code.**
S502 receipt `quote`+`span` rewritten to the body's FIRST sentence
(`REA native-and-artifacts reference at the pinned revision, re-opened 2026-11-05.`,
span 0..len) while the body, fetch_sha256, fetch-log line and SOURCES row are untouched.
`check_verified` passes (quote IS in the body at its span); `check_receipts` passes
(re-hash unchanged). `audit_source_quotes.py` defines `anchor_quote` (last
double-quoted segment of the anchor cell) but `cmd_verify` never calls it, and the
counter never compares the receipt quote to the SOURCES anchor cell or to what the entry
cites. Output: `C1_RECEIPTS_WHY=ok`, `C1_QUOTES_WHY=ok`, `C1_VERDICT=pass` (FG09).
Smallest safe correction: in `cmd_verify`, assert
`norm(anchor_quote(row[6])) == norm(receipt["quote"])` — the helper already exists.
(For the honest lane data this binding HOLDS today: S502's receipt quote is the
file-offset CLI sentence the entry's route table actually cites; I verified
`norm(body[span]) == quote` for both receipts on the committed bytes.)

**F10 — SOURCES registry URL cell (col 1) is read by no leg.**
Replaced the S502 row's URL with `https://attacker.example/rea-native.md` (row stays
11 cells; used-by, status, tier, opened, quote cells intact). `check_sources` reads
cols 3/6/7/8/10 only; `check_receipts` validates the receipt's own `fetch_url` but
never cross-checks it against the row URL. Output: `C1_RECEIPTS_WHY=ok`,
`C1_QUOTES_WHY=ok`, `C1_VERDICT=pass` (FG10). Fix: assert row-URL == receipt
fetch_url (or same allowlisted host) for receipt-bearing rows.

**F11 — no leg validates any derivation-table value; a lying table passes green.**
Swapped one byte of `corpus/fixtures/pe-r75-headless-smoke/fixture.exe`; appended a
self-consistent embedded fence
(```sh\n$ python3 -B corpus/hash_fixture_r96.py\nsha256: <new-sha>\n```, helper added
under `corpus/`, python3-confined per round-70 F1) whose re-run output matches; votes
re-pinned to the new digest (93fafbf3…). The entry's derivation table still records the
STALE `fe060de1…` fixture sha. Output: `C1_EMBEDDED=pass`, `C1_EMBED_NONVACUOUS=pass`,
`C1_VOTES=pass`, `C1_VERDICT=pass` (FG11). Scope note for r97: the C1 counter verifies
admission MECHANICS (rows/votes/receipts/registry), not the entry's factual table; the
honest table rests on the non-author closure. Instrument gap, not a lane-data defect —
see §C (the real table verifies row by row today).

**F12 — negative result closing the suggested "tabs" digest-fork: digest normalization
is whitespace-invariant.**
Status line rewritten tab-indented (`\tadmission-status: admitted`). `digest()`'s
`(?im)^\s*admission-status\s*:.*$` absorbs the tab; `C1_ADMITTED`'s strip-compare
accepts it; the counter passes with the UNCHANGED frozen digest `2f7d4c1b…`
(`C1_VOTES=… digest=2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`)
(FG12). No digest fork exists via status-line whitespace; the pass is
content-equivalence, not evasion.

**F13 — extra §Q-map rows are unguarded (lint checks missing-only).**
Appended row `| Q18 | PASS | forged extra criterion row outside the pinned Q01-Q17 set |`.
`lint_qmap` returns only `want − have`; votes pin exactly Q01–Q17. Output:
`C1_LINT=pass`, `C1_VERDICT=pass` (FG15). Minor; fix only if exact-set equality is
intended.

**F14 (minor) — one fetch-log line can serve multiple receipts.**
Both log lines replaced by a single merged line carrying both sids and both shas;
`line_has` (sid AND sha on some line) passes for both receipts. Output: `C1_VERDICT=pass`
(FG19). Fix: one-line-per-sid with a per-line GET shape, if log granularity is meant to
be per-fetch.

## B. Kills — fresh forgeries the frozen counter REJECTS (recorded for coverage)

- **K1** status line moved below the 30-line head window → `C1_ADMITTED=fail` (FG13).
- **K2** `recheck:` header moved below the window → `C1_TRIO=fail` + `C1_LINT=fail`
  (lint header window is 40 lines) (FG14).
- **K3** NBSP inside the status line (`admission-status:\u00a0admitted`) → digest
  normalized (no fork) but `C1_ADMITTED=fail` (strip keeps the inner NBSP) (FG16).
- **K4** used-by path alias `./knowledge/round-96-native-analysis-sessions.md` →
  cite-back substring passes but strict set equality kills:
  `C1_SOURCES_WHY=S502:usedby-exclusivity:['./knowledge/round-96-native-analysis-sessions.md']`
  (FG18). The task-suggested used-by alias class is CLOSED by the v5 counter.
- **K5** prose mention of `admission-status:` anywhere in the entry → count=2 →
  `C1_ADMITTED=fail` (FG20). Brittleness note: the entry can never discuss its own
  status token in prose.
- **K6** = F12's other face: no digest fork via tab/whitespace/NBSP tricks (FG12/FG16).

## C. C02 entry audit (scope overreach / Q-map accuracy / derivation-table honesty)

Verified against committed bytes and host (read-only; re-fetch via the receipts' own
URLs, the only network use):

- fixture sha256 = `fe060de1bc5106f30dec532270fc634426484e4e2ef186e5b7617443950afd72` ✓
  (table + truth.json agree); bytes at file offset 0x200 are `b8 2a 00 00 00 c3` ✓
  (entry-point claim, Q14's `2 × 6 hex characters` phrasing); regen via
  `python3 -B corpus/fixtures/pe-r75-headless-smoke/gen_pe_r75.py` is byte-identical
  (`cmp` rc 0) ✓.
- record digests d717b491… / 6ce217fa… / 2fba7fbf… / 6a1d18c3… ✓; `evidence_id:
  ev_cc0b9d88…` ✓; provider block id ghidra / 12.1.4 ✓; headless
  `function_count=1`, `FUNC entry @ 140001000`, body `return 0x2a;` ✓;
  `INFO  REPORT` count = 6 ✓; `140001000` = image base 0x140000000 + RVA 0x1000 ✓.
- doctor receipt: `healthy: false` present, ghidra scope classifications healthy,
  Hopper block present (absent-engine claim) ✓; `cli_package_version: 6.7.0` grounds
  Q04's "rea 6.7.0" (host `rea --version` = 6.7.0) ✓; Ghidra install path exists ✓.
- Non-author re-fetch at the pinned revision: S502 HTTP 200, 38167 B, sha256
  == `c818ee34…`; S503 HTTP 200, 35095 B, sha256 == `b5f17fdff…` ✓. Receipt spans
  verify: `norm(body[span]) == norm(quote)` for both ✓. Installed skill copy DIFFERS
  from the pinned body, exactly as the entry's Unknown section discloses ✓.
- Q-map: all PASS rows spot-verified true; all six n/a rows verified genuinely n/a
  (no parser prediction; Q08 superseded; no rejected row load-bearing — consistent with
  the counter's empty REJECTED_OK; no mutation-guarded clause; lint Q15 clean, no
  git-identity sentence; no adjudication relocation). Q14: the table's truncated
  digests (`d717b491…`) carry no length claims — consistent with the row's own text ✓.

Minor entry observations (do not change any decision):

1. **E-1 (exit codes are prose-only).** `rea-decompile.raw.txt` carries no
   exit/returncode line; Q05's "exit 0 / exit 0 / exit 1" integers are session
   observations consistent with the committed markers (`Import succeeded`,
   `healthy: false`) but are not re-derivable from committed bytes. The derivation
   table honestly omits them (its scope is counts/ids/offsets/digests); Q05/Q11 readers
   should treat the exit integers as session-recorded, not record-recorded.
2. **E-2 ("6.7.0-era" tag).** The installed SKILL.md frontmatter declares
   `metadata.version: "42"`; the S002 registry row records that honestly. The entry's
   "installed 6.7.0-era skill copy" phrasing rests on the CLI package version
   (doctor line 307 + `rea --version`), not the frontmatter number — defensible, but a
   reader can conflate the two; a parenthetical would remove the ambiguity.
3. **E-3 (located quotes land with the L1).** The ≤25-word located quotes are not yet
   in the tree (round-96 lesson `## Gate` lands at landing, per claims.md frontier).
   The receipts' quotes ARE the sentences the entry's route table relies on, so when
   the lesson lands, the Gate quotes should be checked to equal the receipts' `quote`
   fields — see F9 (that equality is otherwise unenforced by any instrument).

No scope overreach found: the entry's claims stay inside the demonstrated fixture,
versions, host and date; missing engines are recorded as absent; digests bind bytes
only; the installed-vs-pinned drift is disclosed.

## D. Bounds

Writes: this wave dir only (`findings.md`, `receipts/*`, `vote.json`) + scratch
`/fast/scratch/hyaku/revenger-r96/CriticR96/` (deleted before yield; receipts copied
here first). Lane files, fleet repo, sibling lanes, `.ufo/state`, watchdog log: read
only (plus read-only `git show`/`git cat-file` used by the frozen instruments and the
digest verification). Installs: none. Subagent dispatch: none (leaf). Every Python
invocation used `python3 -B`; the counter's own temp dirs were redirected into this
seat's scratch via `HYAKU_SCRATCH`. Network: only the two receipt URLs under
raw.githubusercontent.com/morluto/rea.
