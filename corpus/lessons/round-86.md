# Round 86 — the used-by pointer-drift class becomes machine-caught (orphan_sweep v7, per-source citation-sites accounting); SKILL.md gains the pointer-hygiene rules and the M42 signature

Base `d7fd9d93c522ccc6f2b8f46a56cb90231926c43e` (r85 tip + non-author
spot-check, pushed clean). Fresh-start round: r71/r72/r73 rejected
closures re-read (§Gate). Freeze
`231140083fe77739d4093be6fc6767733a1c8aae` (claims + sha-pinned v7
instrument + red pair over ONE pre-fix tree + selftest/mutant reds +
SKILL red greps + freshstart probes + dual round-start census receipts +
corrections.md correction 2, committed before any fix or after-run).
Landing `25041d95c04e3bb781db21b283874e8673bdbcaf` (six rule-2 used-by
pointer drops + S472 + SKILL.md §3/§4 rows; 3 files, 29 insertions,
6 deletions). Final measured revision = the adjudication commit carrying
this lesson. Two claims, distinct axes, causally separable, neither
exploratory: **C1 calibration** (orphan_sweep v7 change 10 — the r84
lesson's routed candidate vector 1, "per-source citation-sites
accounting"; red mismatch=6 → green mismatch=0 over the live tree) and
**C2 depth** (SKILL.md pointer-hygiene decision rows + the M42 named
error signature; reds 9/0/4 → greens 10/2).

## Gate

Fresh-start §7 (r71/r72/r73 rejected closures re-read at fleet
`.ufo/reports/round-7{1,2,3}/revenger.md`; common thread: all three are
K-admission claims whose deciding wave Q-review surface has never
settled on this host — r74 L0 re-read this round, unanswered; a
do-nothing control reaches each identically here; neither r86 claim
routes through K or any wave surface). Ruled out with fresh probes
(2026-11-02, receipt `reports/round-86/freshstart-probes.log`):
**coverage/K** (operator-blocked, L0 r74); **F android**
(`REA_JADX_MCP_JAR` UNSET, no jadx on PATH — S448 stands; F4's honest
exception stays 10/11); **M/A1/A1v2** (saturated 3/3, 3/3, 5/5; frozen
holds re-run over the landing archive at adjudication); **asset-catalog**
(macOS-gated; `rea capabilities` prints 7 unsupported_host groups this
round — 7 at r85, 8 at r84; the lane records the count it prints, not a
cause); **ghidra-headless repeat** (r75 capability row holds; r85
spot-check concurred); **criterion C repair / R full extension / N
attribution pair** (§9-sizing and r75–r85 lineage stay routed; this
round's calibration claim is the routed v7 vector instead). Lowest-axis
routing: coverage is the lowest non-retired axis (K 5.3 < saturation
line 7.0, so the stagnation nudge does NOT apply) — the obligation
routes on documented unreachability (probe 6 enumeration: every
reachable coverage surface saturated, hard-gated, or operator-blocked at
base), receipts cited, not on the nudge.

Carry-in first (r85 non-author closure, status-neutral, addressed before
claim work): item 1 → `reports/round-85/corrections.md` correction 2
(the mg_probe.py docstring prediction line vs the registered 0/3 red;
the conditional fix trigger documented — r86 does not touch mg_probe.py,
the verified sha pin `1840c30c…3ac03f` stays valid; the standing rule: a
docstring prediction line states the registration RULE, the registered
red receipt governs); item 2 → dual round-start census receipts landed
(`.ufo/waves/round-86/census-round-start-{sanctioned,literal}.log`;
sanctioned exit 0, 21 W01 + 10 W04, zero E; literal exit 2, the
disclosed r74–r85 lineage, routed around); item 4 → SHONEN non-author
re-confirmation stays operator-side, no box marked by the author; item 3
→ every r86 sweep receipt cites its basis line first.

Sources opened this round (row appended inside the Registry section,
directly after S471; census NF=13 checked at landing, 0 malformed):

| row | path/command | located quote (≤25 words) | decision |
|---|---|---|---|
| S472 | `reports/round-86/sweep7-red-prelanding.log` + `sweep7-v6-blind-prelanding.log` + `reports/round-86/freshstart-probes.log` probes 4-5 + the census contract (`CORPUS.md` used-by definition), opened 2026-11-02 | "repo-relative paths of the knowledge entries or lessons citing the row" (11 words) | ADMIT (tier A, own-work environment) |

Census: round start — sanctioned explicit-lane-dir form exit 0 (21 W01 +
10 W04, zero E, the same disclosed classes as r74–r85), receipts landed
in the freeze (`.ufo/waves/round-86/census-round-start-*.log`); literal
form exit 2, disclosed r74–r85 lineage, routed around (operator-side).
Round end — receipts in `reports/round-86/census-after.log`.

C1 evidence chain: S472 (the drift class, demonstrated live over one
tree) → v7 frozen at `2311400` (sha `f955cd7d…618`; v6 blob unchanged
`b2db45b0…f12b7` re-verified; declared exits 0/1/64 unchanged; change 10
non-gating by construction) → red pair over the SAME pre-fix tree:
`grep -c SWEEP_SRC` over the v6 summary → 0 (the class does not exist in
v6) vs `SWEEP_SRC registry=disk rows=451 sites=499 cited=493 mismatch=6
absent=0` with the six exception rows (S448 → reports/round-77/claims.md,
S449 → SKILL.md, S450 → reports/round-78/province_probe3.sh,
S451 → reports/round-79/claims.md, S453 → reports/round-79/claims.md,
S456 → reports/round-80/orphan-before.log); identical basis
`SWEEP_CORPUS fleet-reports=26 lessons=52 log=1` and gating
`CITED=1050 COMMITTED=988 LANDABLE_ORPHANS=0 ABSENT=62`, both exit 0 →
preprobe cross-check (`freshstart-probes.log` probes 4–5): per-pointer
`grep -cw` finds all six drift pointers at CITES=0 while each row's
OTHER pointer cites (4/1/1/5/7/1) — `mined` stays valid per CORPUS.md's
status contract ("cited by ≥1 path in used-by") → the fix: six rule-2
in-place used-by changes, each dropping exactly one non-citing pointer,
old→new logged (`reports/round-86/usedby-fix-log.txt`, each replacement
asserted unique in its row) → mutation check: selftest 25 legs + pass
exit 0 from the frozen bytes; ONE one-substitution sed mutant
(`USED_BY_ACCOUNTING = True` → `False`, exactly line 165, mutated sha
`0bfe69a0…8c3`) dies exit 1 attributed `selftest: used-by accounting
drifted (used-by class)` → green from the committed blob over the
adjudication tip (`sweep7-real-after.log`: mismatch=0, absent=0; the
intermediate landing-time state showed mismatch=0 with the one expected
S472→lesson absent row, disclosed). Separability: `c1-only.log`
(archive of base + C1 files only: the fixed SOURCES.md + v7; SWEEP_SRC
mismatch=0 present, SKILL greps at red values 9/0) and `c2-only.log`
(archive of base + C2 files only: the edited SKILL.md; M-rows 10 +
cite-back 2 with SOURCES.md at base, v7 absent). Noharm:
`noharm-diff.txt` (freeze..landing: 3 files, 29 insertions, 6 deletions
— SOURCES.md limited to the six used-by cells + the S472 append,
SKILL.md additions only; corpus/live, fixtures, knowledge/, README,
QUALITY.md and all standing verifiers byte-unchanged; frozen holds re-run
over the landing archive: M 3/3, F4 10/11, A1v2 5/5, A1 3/3).

C2 evidence chain: red greps over base bytes (`skill-red-greps.log`:
M-rows 9, cite-back 0, used-by 4) → the §3 rule table gains three rows
(cite-back rule with the six named specimens; placeholder semantics with
the em-dash parser class named; the census/sweep division of labor) and
§4 gains M42 (pointer-drift; what it looks like; the check that catches
it; the fix) → greens over the landing archive (`skill-green-greps.log`:
M-rows 10, cite-back 2, used-by 8). Boundary: C2's moved quantity is the skill's
decision ground for pointer hygiene — before this round, SKILL.md's
rule-2 row permitted pointers with no cite-back property at all (the
exact defect six live rows exhibit); after, a reader acting on SKILL.md
alone writes and audits pointers under the stated rules. C1 moves no
criterion score (same claim shape as r85 C2); the moved quantity is
pointer-truth: a used-by pointer that names a document which never cites
the row stops being invisible. No knowledge admission (K untouched,
operator-blocked); PROVINCE byte-unchanged; SHONEN boxes unchanged
([~], operator-side non-author confirmation routed).

Assimilation: `considerthese/` re-read this round (2026-10-20 through
2026-10-28; the same eight files r85 read — no new proposals landed
since; proposals 1–3 grounded out r83/r84, proposal 4 sits in the
§9-ruled criterion-C space, proposal 5 is the bot's own procedure, not
lane scope); adopted nothing — shokuknow unreachable. L2 floor: no
dispatch surface on this host (r74 L0 stands, re-read this round); every
verdict re-derives from committed bytes.

## Mistakes

| class | evidence pointer | captured-by | fix |
|---|---|---|---|
| placeholder-parse false positive: a used-by cell holding the em-dash placeholder (U+2014) parsed as a PATH in an ad-hoc probe that excluded only ASCII hyphens — 20 phantom no-disk rows (S007/S008/S012/S024/S025/S040/S043/S044/S415–S426) in the first preprobe output | the row-level cross-check (raw cell bytes `M-bM-^@M-^T` = U+2014 under `cat -A`; CORPUS.md's contract "`—`" form) — self-caught before any committed run | the cross-check habit (read the raw cell before trusting a parse); the probe was scratch-side, nothing committed | v7's `USED_BY_PLACEHOLDERS` covers em/en dash + ASCII hyphen forms with the selftest placeholder leg pinning both; SKILL.md §3 states the placeholder rule with this class as the named specimen; mined |
| probe parse desync (reference-parse re-derivation): a second probe build left the table id unstripped, so the cite-back regex searched the space-padded `" S016 "` form and printed 65 phantom no-cite rows (NO_CITEBACK=71 vs the frozen instrument's 6) | the two-implementation cross-check: sweep7-red said mismatch=6, the probe said 71 — a desync this large means a parse bug in one of them, and the committed instrument's parse is the reference | the cross-check habit (two parsers must agree before either is cited) | probes reuse the frozen instrument's parse (strip + placeholder set) instead of re-deriving it; probe v3 reproduced the instrument's 451/499/6 exactly; mined |
| frozen counting command vs first wording: the freeze pinned `grep -c 'cite-back' SKILL.md` green=2, but the first §3 edit wrote the rule without the literal term (green would have been 1) | running the frozen counting command BEFORE the landing commit (the green pre-check habit) — self-caught pre-commit | the frozen-command pre-check (measure what you pinned, before you pin the bytes) | wording aligned to the frozen command (row 1 now carries "passes cite-back"); landing greens 10/2 as pinned; rule: when a counting command is frozen, run it against the drafted bytes BEFORE committing the landing; mined |
| stale-index diff garbage recurrence: `git diff HEAD` printed 414 changed files / 68019 deletions against a working tree whose sampled blobs were byte-identical to HEAD (sha256 cross-check on three files, all equal) | the contract's standing rule (never trust git status/diff on this host) + the sha cross-check habit (compare `git show HEAD:<path>` digest vs on-disk digest) | the r78+ host-lineage discipline, re-applied on a new signature (this round it masqueraded as mass deletions, not just stat noise) | plumbing only for all round work (`git show`/`ls-tree`/`diff <base>..<new>` between real commits); byte-verify with sha256 when a diff surprises; no new treecommit variant occurred (10/10 and 3/3 numstat held) |
| shell-heredoc truncation recurrence: the multi-KB SCORECARD round-86 append via a bash heredoc was truncated mid-word and the terminator was never seen (the r84 mined class, second host recurrence) | the immediate post-write tail check (end-of-content check habit): the tail ended mid-word and the trailing marker lines were missing | the r84 lesson's own rule ("multi-KB content moves via files, never via shell heredocs; every append is followed by an end-of-content check") | SCORECARD.md restored from the committed bytes (`git show 25041d9:SCORECARD.md`, sha-verified `d6b68041…`) and the section re-appended from a Write-tool temp file with a passing tail check; corrections.md's shorter heredoc append was verified intact; the mined rule held — this row records the recurrence, not a new class |
| count-from-intent recurrence: the informational used-by green count was drafted as 7 by mental arithmetic (+3 §3 rows); the landing blob actually greps 8 (+3 §3 rows + the M42 row) | running the frozen greps against the landing blob before the adjudication commit (the same green pre-check that caught the cite-back wording) | the r83 count-from-intent class, re-caught by the pre-commit measurement | the three drafts (SCORECARD/LOG/lesson) corrected 7 → 8 before any of them landed; rule: every number in a draft is grepped against the bytes it names before the commit, never carried from arithmetic |

## Routed forward

- **Criterion R full extension** and **criterion N's mutation-killed
  attribution pair** — r75–r86 lineage; still open, not declared.
- **Criterion C repair** — §9 sizing, unchanged since r78.
- **v7 disposition ledger**: the accounting's absent-pointer class is
  empty after the fix (mismatch=0 absent=0 over the adjudication tip);
  no standing ledger needed operator-side. The remaining routed sweep
  candidate (none named this round) — the instrument's class space is
  currently closed: corpus, bare tokens, fleet resolution, LOG, and
  used-by pointers all have recorded, mutation-checked classes.
- **F android** — hard-gated on the caller-supplied `REA_JADX_MCP_JAR`
  (re-probed; S448 receipt stands). F4's honest exception stays 10/11;
  M/A1/A1v2 saturated; F4 is the only open coverage criterion number
  and its one missing family is operator-gated.
- **K** — blocked on the wave Q-review surface (r74 L0 unanswered,
  re-read this round).
- **Census literal form** — operator-side routing continues (r74–r86
  lineage; the r79 consolidation L0 line stands).
- **SHONEN box 1** — non-author re-confirmation of the CURRENT SKILL.md
  bytes stays operator-side (r69 spot-check V7 lineage; r85 closure
  item 4 re-recorded; SKILL.md changed this round, so the standing need
  now names the r86 bytes too).
- **treecommit discipline** — repo-relative args only; every arg exists
  on disk before the call; the landing diff counts one numstat row per
  arg (held this round: 10/10 freeze, 3/3 landing).
