# Round 94 — ScoutErrata cite-back and erratum-pin sweep

Seat: `ScoutErrata` (role `scout`). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Tip under test: `060a8e87d6de6b31f91b58524ab0fcad88ae5431` (lane HEAD at sweep time).
Entry under test: `corpus/knowledge/round-72-tool-landscape.md`.
Read-only seat: no lane file, no git write command, no SOURCES.md edit.

Method (all facts below are observed, not inferred):

- S-ids collected from the **whole entry** with `re.findall(r"\bS\d{3,}\b", text)` — the same
  whole-file rule the v3 counter's `collect_sids` uses. **48 distinct S-ids** are cited:
  `S050,S051,S054–S095 (42 ids),S427,S428,S498,S499`.
- The task statement expects **46**; the 46 are the ids that have a row in `corpus/SOURCES.md`
  at the tip. The two extras, `S498`/`S499`, are this round's **new drift-check rows** — the
  frozen claims' §2b frontier step says the L1 appends them to `corpus/SOURCES.md` at landing,
  so at the freeze tip they are legitimately row-absent. They are listed below as
  `ROW-ABSENT`, not as drift.
- For each id with a row: the `used-by` cell is split on `,`; each pointer is resolved against
  the **committed** bytes at the tip (`git show HEAD:<pointer>`), and the pointer file is
  searched for the id with a word-bounded pattern `(?<![A-Za-z0-9])<SID>(?![A-Za-z0-9])`.
  A pointer whose committed bytes never name the id is `drift(<pointer>)` — the r86 sweep
  class M42. The v3 counter's `check_sources` only tests row **existence** and the
  `used-by` substring for the two new rows, so this cite-back-truth axis is not covered by
  the counter and is reported here only.
- Erratum rows were re-fetched at the URL/revision named in each row's anchor cell and the
  row's quote was located in the fetched bytes (exact substring, whitespace-preserving).

## 1. Cite-back sweep — 46 rows

| sid | used-by pointer (committed at tip) | row status | sid named in pointer file? | cite-back lines in pointer | verdict |
|---|---|---|---|---|---|
| S050 | corpus/training/bounty-triage/MODULE.md | mined | yes | :10, :43 | OK |
| S051 | corpus/training/bounty-triage/MODULE.md | mined | yes | :10, :43 | OK |
| S054 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :1, :6, :25 | OK |
| S055 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :26 | OK |
| S056 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :26 | OK |
| S057 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :26 | OK |
| S058 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :28 | OK |
| S059 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :28 | OK |
| S060 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :30 | OK |
| S061 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :29 | OK |
| S062 | corpus/knowledge/round-72-tool-landscape.md | rejected | yes | :26, :27 | OK |
| S063 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :30 | OK |
| S064 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :27 | OK |
| S065 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :26 | OK |
| S066 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :31 | OK |
| S067 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :29 | OK |
| S068 | corpus/knowledge/round-72-tool-landscape.md | rejected | yes | :29 | OK |
| S069 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :26, :27 | OK |
| S070 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :30 | OK |
| S071 | corpus/lessons/round-72.md | rejected | yes | :30, :62, :73, :98 | OK |
| S072 | corpus/lessons/round-72.md | rejected | yes | :31, :59, :62 | OK |
| S073 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :32 | OK |
| S074 | corpus/lessons/round-72.md | rejected | yes | :33, :58, :62 | OK |
| S075 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :2, :7, :38 | OK |
| S076 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :3, :39 | OK |
| S077 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :4, :32, :40, :69 | OK |
| S078 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :42 | OK |
| S079 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :42 | OK |
| S080 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :43 | OK |
| S081 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :44 | OK |
| S082 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :45, :89, :91 | OK |
| S083 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :45, :91 | OK |
| S084 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :45 | OK |
| S085 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :46 | OK |
| S086 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :47 | OK |
| S087 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :48 | OK |
| S088 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :48 | OK |
| S089 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :49 | OK |
| S090 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :49 | OK |
| S091 | corpus/lessons/round-72.md | rejected | yes | :50, :62 | OK |
| S092 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :49 | OK |
| S093 | corpus/lessons/round-72.md | rejected | yes | :52, :62 | OK |
| S094 | corpus/knowledge/round-72-tool-landscape.md | rejected | yes | :50 | OK |
| S095 | corpus/knowledge/round-72-tool-landscape.md | mined | yes | :5, :41 | OK |
| S427 | corpus/lessons/round-73.md | rejected | yes | :13, :17, :23 | OK |
| S428 | corpus/lessons/round-73.md | mined | yes | :14, :17, :23 | OK |

**Tally: 46 OK, 0 drift.** No pointer's committed bytes fail to name its sid, so no r95
rule-2 pointer drop is proposed from this sweep.

### The two new rows (row-absent at the freeze tip — expected, not drift)

| sid | cited at entry line | row in `corpus/SOURCES.md` at tip | verdict |
|---|---|---|---|
| S498 | :6 (header `source:` line) | absent | ROW-ABSENT — pending L1 landing of the row |
| S499 | :7 (header `source:` line) | absent | ROW-ABSENT — pending L1 landing of the row |

Landing-time precondition for the v3 counter's `C1_SOURCES` leg (`NEW_ROW_IDS` check, frozen):
each new row must be `status=mined`, `tier=A`, `opened=2026-11-05`, and its `used-by` cell
must contain `knowledge/round-72-tool-landscape.md` (the counter's `ENTRY_REL` substring test).
Recorded here as a landing checklist item; the L1 owns `corpus/SOURCES.md`, this seat does not.

## 2. Erratum-pin sweep — 2 rows

### S427 — Awesome AI Reverse Engineering README at its pinned commit

- Anchor cell: `README introduction at 63900b2c9e2ae2dac61fc0db7553d4ce88ebb932`.
- Pinned URL fetched: `https://raw.githubusercontent.com/zhuyansen/awesome-ai-reverse-engineering/63900b2c9e2ae2dac61fc0db7553d4ce88ebb932/README.md`
  (39 590 bytes, fetched 2026-11-05).
- Row quote: `each one read and security-graded`.
- **Located: yes.** Line 5 of the pinned README:
  `Open-source **AI reverse engineering tools** for Claude Code, Codex and other agents: Ghidra MCP and IDA Pro MCP servers, jadx and Frida for mobile apps, reverse engineering skills, REA, and programs rebuilt with it. 118 repos, each one read and security-graded by [Agent Skills Hub (agentskillshub.top)](…)`
- Cross-check of the supersession the erratum claims: the **old** S071 anchored quote
  `Each repo is read and security-graded` is **not** a substring of the pinned README
  (verified absent) — consistent with the erratum's statement that S427 replaces S071's
  *paraphrased* quote with the verbatim one. The r73 erratum remains accurate.
- Verdict: **located yes** (line 5).

### S428 — LLM4Decompile abstract, arXiv v3

- Anchor cell: `v3 abstract opening sentence`; URL `https://arxiv.org/abs/2403.05286v3`.
- Pinned URL fetched (43 987 bytes, fetched 2026-11-05).
- Row quote: `traditional tools like Ghidra often produce results that are difficult to read and execute.`
- **Located: yes.** The abstract element at line 124 of the fetched abs page
  (`<span class="descriptor">Abstract:</span>Decompilation aims to convert binary code to
  high-level source code, but traditional tools like Ghidra often produce results that are
  difficult to read and execute. …`); also carried in the page's `og:description` /
  `twitter:description` meta at lines 30 and 34.
- Cross-check of the supersession the erratum claims: the **old** S082 anchored quote
  `The resulting code may appear readable or even compile successfully, yet still deviate from the behavior of the original binary.`
  is **not** a substring of the LLM4Decompile v3 abstract page (verified absent) — consistent
  with the erratum's statement that the behavioral-deviation sentence belongs to
  AutoDecompiler (S083), not to this paper, and that S428 supports only the stated
  readability/executability motivation. The r73 erratum remains accurate.
- Verdict: **located yes** (line 124).

### Erratum-section byte-identity

`## Round-73 source-attribution erratum` (the trailing section of the entry) is byte-identical
at the freeze tip `060a8e8` and at the round-93 base `9876cb38`: 771 bytes each, identical.
The section was introduced by commit `d4ab332` (`round-73: honest stop (attempt 2) …`) and has
not changed since. The frozen claim "the r73 erratum section stays byte-identical" holds as
observed.

## 3. Supplementary drift re-grounding for the two pending new rows (read-only)

Both `S498` and `S499` are declared as re-opens of `github.com/morluto/rea` for a scope drift
check. The URLs named in the entry header (`https://github.com/morluto/rea` README and
`docs/installation.md`) are within this seat's authorised network scope, so the two declared
scopes were re-checked at the pinned revision (S054's `0cd7ef45…`) and at `main`:

- S498 (root README, scope = "the project's own declared tool families"): the pinned README
  line 63 and `main` line 65 both carry
  `REA connects your agent to tools for inspecting native binaries, JavaScript and Electron apps, .NET assemblies, and websites. … Analysis runs locally, and results include the evidence and limitations behind each conclusion.`
  — the `native binaries` / `JavaScript` / `Electron` / `.NET` / `websites` /
  `evidence` / `limitation` scope tokens and the `How REA works` heading are all present at
  both revisions. **No scope drift observed** between the pinned revision and `main`.
- S499 (installation docs, scope = "the documented approval boundary"): `docs/installation.md`
  at `main` line 4 carries `Setup previews configuration changes and asks for approval before
  applying them.`, and the approval/plan semantics recur at lines 22, 48, 51, 54, 126–127,
  140–146. **No scope drift observed.**
- No entry byte was changed and no source row was created by this seat; these are
  observations for the L1's landing of S498/S499 and for the `C1_QUOTES` receipt leg
  (`reports/round-94/quote-receipts/` does not exist at the tip — the receipts are the
  L1/ExecReceipts deliverable).

## 4. Digest observed (for cross-seat binding)

The counter prints its digest even though the vote leg fails at the freeze tip:

```
$ PYTHONUTF8=1 python3 -B reports/round-94/c1_k_admit_counter3.py --rev 060a8e87d6de6b31f91b58524ab0fcad88ae5431
C1_VOTES=votes dir missing digest=01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3
```

Independently reproduced here: normalising every line matching
`^admission-status: (candidate|admitted|rejected)$` to `admission-status: candidate` and
sha256-ing the UTF-8 bytes of
`corpus/knowledge/round-72-tool-landscape.md` gives
`01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`
(identical for the worktree file and for `git show 060a8e8:corpus/knowledge/round-72-tool-landscape.md`;
the file carries exactly one `admission-status:` line, value `candidate`, at line 11 — inside
the 15-line header window). The same string is already in
`.ufo/waves/round-94/w1/ExecFrozen/freeze-state-digest.txt`.

**candidate_sha256 to carry in every vote file for this round:**
`01d51059fb29a5184342b2815e643695aa269b384c04d005f69556816f291bd3`

## 5. Findings summary

| # | finding | class | action |
|---|---|---|---|
| 1 | 46/46 cite-back pointers name their sid in committed bytes at the tip | no drift | none; no r95 rule-2 pointer drop proposed |
| 2 | S427 quote `each one read and security-graded` located at pinned README line 5 | erratum still accurate | none |
| 3 | S428 quote `traditional tools like Ghidra often produce results that are difficult to read and execute.` located at abs page line 124 | erratum still accurate | none |
| 4 | S071's old anchored quote is still absent from the pinned README; S082's old anchored quote is still absent from the LLM4Decompile v3 abstract page | both supersessions still needed | none (rows unchanged) |
| 5 | The entry's r73 erratum section is byte-identical at tip and at the round-93 base (771 bytes) | frozen claim holds | none |
| 6 | S498/S499 have no `corpus/SOURCES.md` row at the freeze tip; the counter's `C1_SOURCES` leg requires them `mined`/tier A/`opened=2026-11-05` with `used-by` containing `knowledge/round-72-tool-landscape.md` | landing precondition | reported to L1; not edited by this seat |
| 7 | `reports/round-94/quote-receipts/` does not exist at the tip, so the `C1_QUOTES` leg has no receipts to verify | landing precondition | reported to L1/ExecReceipts; not created by this seat |

No lane file was written. Scratch `/fast/scratch/hyaku/revenger-r94/ScoutErrata` was removed on
exit.
