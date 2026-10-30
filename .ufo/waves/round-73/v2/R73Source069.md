# R73Source069 — S069 (Rizin) source audit

Seat: R73Source069 · wave round-73 v2 · assigned row: **S069 only** · read-only besides this report.
Access date for all re-opens below: **2026-10-30**. Network failures: **none** (all fetches HTTP 200; recorded inline).

## Assigned row S069 — re-open verdict: AGREE (admission sound)

**Primary source re-opened (exact cited pin):**
- URL: `https://raw.githubusercontent.com/rizinorg/rizin/470b1b1eb7338e7ee8bea581f3569b20321c7849/README.md` — HTTP 200, 4824 bytes, sha256 `b91344710837f17f14fa9c40a4a3ced5a48d7faec3b0ba325a9e83ff8c6818c0` (receipt copied here; scratch cleaned after write).
- Pin existence: GitHub API commit lookup `470b1b1eb7338e7ee8bea581f3569b20321c7849` → 200, committer-signed, dated 2026-03-17 ("rz-ar: add archive extraction utility (#6036)").
- "dev branch snapshot" claim: compare API `470b1b1e...527e0c8d` (current dev head) → `status: ahead, behind_by: 0, merge_base: 470b1b1e…` — pin is an ancestor of `dev`. Claim holds. [observation]
- Drift check: pinned README is byte-identical to today's dev-head README (`diff` empty). Quote stability confirmed at both pin and head. [observation]

**Located quote (registry row, verbatim, ≤25 words):**
> "Rizin is a reverse engineering framework, born as a fork of the radare2"

13 words. Substring match in the **raw** fetched bytes — verbatim with no normalization needed. [observation]

**Lesson Gate quote (`corpus/lessons/round-72.md` S069 row, verbatim after markup/whitespace-only normalization, ≤25 words):**
> "Rizin is a reverse engineering framework, born as a fork of the radare2, with a focus on usability, features and cleanliness."

21 words. Raw README wraps the sentence across lines (`"...radare2, with \na focus on..."` — trailing space + newline). With whitespace runs collapsed (markup-only normalization), the lesson quote is an exact substring; it is **not** a raw-byte substring solely due to the line wrap. This is the normalizing-markup-only case the seat spec allows. [observation]

**Scope cell** — "The project's own description of its framework/CLI surface, from the `dev` branch snapshot; no claim of parity with radare2":
Supported. README self-describes "Rizin is a reverse engineering framework…", "scriptable command-line hexadecimal editor", plus a `Tools` section (`rz-bin`, `rz-asm`, `rz-diff`, …). No parity-with-radare2 claim appears; the only radare2 mention is the fork-origin sentence itself. [observation]

**Decision cell** — "README documents its own fork history, command-line framework and listed architectures; this is not evidence of feature parity or upstream ownership":
Supported. Fork history: "born as a fork of the radare2". CLI/framework: see above. Architectures: `## Supported Architectures` lists i386 through "AMD Am29000" (~60 entries). The negative bound (no parity, no upstream ownership) is correctly stated — the README makes neither claim. [observation]

**Tier** `tool` / level `A`: correct — the project's own primary README at an exact commit pin; classic tier-A self-description. [observation]

**Used-by** `corpus/knowledge/round-72-tool-landscape.md`: present — row S069 is cited in the "Need native disassembly/decompilation and analysis" row and the "Need authored byte-level inspection and structure visualization" row (landscape lines 24–25). Entry wording "radare2/Rizin describe command-line binary analysis" and "radare2 and Rizin list hex/format and scriptable inspection capabilities" is a fair paraphrase of the README ("analyze binaries, disassemble code… scriptable command-line hexadecimal editor"); the entry's limits column ("do not infer feature parity, licensing, correct decompilation, or local provider readiness") matches the source and the row's own scope bound. [observation]

**Rejection flip:** N/A — S069 was admitted, not rejected; no flip wording exists or is needed. [observation]

**Access-date bookkeeping:** registry row records accessed 2026-10-27 (original open); this seat re-opened 2026-10-30 with identical bytes. No row field requires change; recheck policy `on-release` untouched (no release event observed). [observation]

## S071 / S082 routed defects — status check (no new row proposed by this seat)

The routed defects from `corpus/lessons/round-72-verifier-spotcheck.md` (S071 registry paraphrase; S082 quote misattributed to LLM4Decompile when it belongs to AutoDecompiler/S083) are **already discharged append-only** in the current registry and the round-73 lesson Gate: [observation]

- `S427` (`corpus/SOURCES.md` line 442, status `rejected`, 2026-10-30): supersedes S071 with verbatim pinned quote "each one read and security-graded" at commit `63900b2c9e2ae2dac61fc0db7553d4ce88ebb932` — exactly the fix the spot-check routed ("make the SOURCES.md quote verbatim").
- `S428` (line 443, status `mined`, 2026-10-30): supersedes S082 with the LLM4Decompile v3 abstract opening "traditional tools like Ghidra often produce results that are difficult to read and execute." and explicitly reassigns the behavioral-deviation quote to S083 — exactly the spot-check's re-pointing instruction.

Old S071/S082 rows are unedited (append-only discipline preserved); registry row count now 428 by the same `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` counting rule round-72 used (53 → 95 → 428, denominators distinguishable per the round-73 lesson). No further superseding row is required from this seat, and no other source admission or rejection is made or proposed. Registry cells for S071/S082 themselves were not independently re-fetched by this seat (out of assigned scope; S071/S082 belong to sibling audit seats).

## Failure disclosure

- Network/source failures: **none**. Every fetch (raw README, commit API, branch API, compare API, dev-head raw README) returned HTTP 200.
- Tooling: system `curl` and `python3` only; **no installs or updates performed** this seat (pacman pause honored; nothing needed installing).

## Receipts

- Fetched bytes: 4824; sha256 `b91344710837f17f14fa9c40a4a3ced5a48d7faec3b0ba325a9e83ff8c6818c0`; pinned README == dev-head README (diff empty).
- GitHub API: commit `470b1b1e…` exists (signed, 2026-03-17); `dev` head `527e0c8d…`; compare → `ahead`, `behind_by: 0`, merge-base = pin.
- Substring checks (mechanical, python): registry quote raw-hit = True; lesson quote raw-hit = False, normalized-hit = True (single line-wrap); word counts 13 and 21 (≤25 both).
- Registry citations: `corpus/SOURCES.md` line 83 (S069), lines 442–443 (S427/S428); `corpus/lessons/round-72.md` Gate S069 row; `corpus/knowledge/round-72-tool-landscape.md` lines 24–25.
