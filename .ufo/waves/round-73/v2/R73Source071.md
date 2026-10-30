# R73Source071 — S071 quote-debt source audit (round 73, v2)

Seat: source audit, leaf member. Scope: SOURCES row **S071 only** — re-open the cited primary myself, compare the located quote verbatim (markup-normalized only), check scope, tier, used-by and rejection flip, and propose an append-only superseding row. Frozen bounds kept: read-only besides this report; no corpus/sibling/fleet writes; no installs; no git mutations; no scratch dir created (none needed, nothing to clean).

## Axes (godspeed)

- **source accuracy** — quote verbatim at the pinned locator.
- **coverage** — routed round-72 defect for S071 checked against ground truth, not against the lane's own audit.
- **auditability** — every claim carries locator + fetched text; observation vs inference labeled.

## Files read (all under /home/vgpnk/Projects/shokunin/revenger-shokunin)

- `corpus/SOURCES.md:85` — S071 row (11 cells).
- `corpus/lessons/round-72.md:30` — round-72 lesson Gate row for S071; `:97-100` erratum note re S427/S428.
- `corpus/lessons/round-72-verifier-spotcheck.md:71` — S071 spotcheck row; `:88` — routed defect #2.
- `reports/round-73/claims.md`, `reports/round-73/candidate-pin.json`, `reports/round-73/measure.py` (round preamble duty; counter not executed by this seat).

## Primary re-open (network, 2026-10-30)

1. `https://raw.githubusercontent.com/zhuyansen/awesome-ai-reverse-engineering/63900b2c9e2ae2dac61fc0db7553d4ce88ebb932/README.md` — HTTP 200, text/plain. The pinned commit resolves.
2. `https://api.github.com/repos/zhuyansen/awesome-ai-reverse-engineering` — HTTP 200 JSON (current HEAD record; `pushed_at` 2026-10-29T16:21:54Z).

**Network/source failures: none.** Both primary fetches succeeded on first attempt today (2026-10-30). No retries were needed; no source was unreachable.

## Findings

- **F1 [observation]** Old S071 located quote `Each repo is read and security-graded` is **not a substring** of the pinned README. The introduction reads: "…programs rebuilt with it. 118 repos, each one read and security-graded by [Agent Skills Hub (agentskillshub.top)](…)." The difference is "each one" vs the row's "Each repo" — a word-level paraphrase, not markup. The round-72 spotcheck's disagree-on-quote is confirmed on my own fetch.
- **F2 [observation]** Corrected quote `each one read and security-graded` **is verbatim** in the pinned README introduction. 5 words (≤25).
- **F3 [observation]** Live repo description today: "Open-source AI reverse engineering tools for coding agents: Ghidra MCP, IDA Pro MCP, jadx, Frida, skills and REA. 122 repos, each read and security-graded. EN + 中文." This matches the spotcheck's quoted description wording. Caution: the description is a moving HEAD surface (README at pin says "118 repos"; description now says "122 repos"); the pinned raw README is the stable evidence surface and should be the cited locator.
- **F4 [observation]** Round-72 lesson Gate row (`corpus/lessons/round-72.md:30`) quotes "Open-source AI reverse engineering tools for coding agents: Ghidra MCP, IDA Pro MCP, jadx, Frida, skills and REA." labeled "README overview". The text is verbatim the repo **description**'s first sentence; the README overview at the pin reads differently ("…for Claude Code, Codex and other agents: Ghidra MCP and IDA Pro MCP servers…"). Quote verbatim, locator label wrong.
- **F5 [observation]** Tier/scope check: tier C community catalog is right. The pinned README self-describes grading as catalog screening, not tool evidence: "The questions are answered by a decision model reading each README, not by hand." and "**Security** is the grade of the repo's README and install steps on Agent Skills Hub."
- **F6 [observation → agreement]** Disposition: **AGREE** with `REJECTED: its aggregate category/grade is not primary evidence for any tool function or safety`. The flip is checkable: "How a repo gets on the list" documents four admission rules, the decision-model process, and a misfile-issue channel, so a future scope evaluating the catalog's selection method with a reproducible sample can be checked against this README.
- **F7 [observation]** Used-by/status coherence: S071 row is `rejected | 2026-10-27 | 90d | corpus/lessons/round-72.md`; used-by matches the lesson that carries its Gate row. Consistent.
- **F8 [observation]** Old row not edited: `git diff` vs HEAD 74e1c3e shows 0 deletions and only 2 added lines in `corpus/SOURCES.md`; the S071 line is untouched. Append-only discipline currently holds.
- **F9 [observation]** A superseding row **already exists, uncommitted**: working tree `corpus/SOURCES.md:442` carries S427 (absent from HEAD; `git show HEAD:corpus/SOURCES.md | grep -c S427` → 0). S427's quote `each one read and security-graded` and locator "README introduction at 63900b2c…" match my independent re-open exactly. The second uncommitted added line was not identified by this seat (S428 exists in both HEAD and working tree; not this seat's row).
- **F10 [observation]** Spotcheck `round-72-verifier-spotcheck.md:71` verified on all three S071 points: decision agree; old registry quote not verbatim; pinned README "118 repos, each one read and security-graded" and description "122 repos, each read and security-graded". Routed defect #2 (`:88`) is satisfied by the corrected quote above.

## Verdict (required fields)

- **Located quote (verbatim, markup-normalized; 5 words):** `each one read and security-graded`
- **Access date:** 2026-10-30
- **URL:** https://raw.githubusercontent.com/zhuyansen/awesome-ai-reverse-engineering/63900b2c9e2ae2dac61fc0db7553d4ce88ebb932/README.md (introduction paragraph)
- **Agree/disagree with source disposition:** AGREE — REJECT as primary tool-function/safety evidence, tier C, catalog screening only; flip (reproducible methodology evaluation) is checkable. AGREE with the round-72 spotcheck that the S071 registry quote was a paraphrase; the quote above is the verbatim fix.

## Proposed NEW superseding row (append-only; S071 must never be edited)

```
| S4xx | Awesome AI Reverse Engineering — https://github.com/zhuyansen/awesome-ai-reverse-engineering | community | C | Correction of S071's paraphrased catalog-screening quote; its own screening description only, never evidence for any listed tool | raw README.md introduction at commit 63900b2c9e2ae2dac61fc0db7553d4ce88ebb932, https://raw.githubusercontent.com/zhuyansen/awesome-ai-reverse-engineering/63900b2c9e2ae2dac61fc0db7553d4ce88ebb932/README.md, accessed 2026-10-30; "each one read and security-graded" | supersedes S071 — REJECTED: catalog screening by a decision model is not primary evidence for any tool function or safety; flip: a future scope evaluates the catalog's selection method with a reproducible sample | rejected | 2026-10-30 | 90d | corpus/lessons/round-73.md |
```

**Collision note (F9):** the lane's own S427 (uncommitted, `corpus/SOURCES.md:442`, Gate row in `corpus/lessons/round-73.md:13`) already carries exactly this correction and passes my independent verbatim check. **Adopt S427; do not append this proposal in addition** — `measure.py` flags duplicate S-ids as a defect. This proposal stands as this seat's independent row should the integrator discard S427; id left as `S4xx` for the integrator.

## Bounds record

- Writes: this report only. No scratch dir created or left behind. No tool installs (none needed — record: none, no version/channel to log). No pacman transactions (pause trivially observed). No secrets accessed.
- Git: read-only queries only (`status`, `log`, `show`, `diff`, `rev-parse`); no mutations, commits, pushes, child tasks, or background jobs.
- Not checked (out of seat scope): S082/S428 substance, the C10 candidate entry, vote files, counter execution; no target execution or live-target requests were made.
