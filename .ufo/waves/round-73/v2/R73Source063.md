# Round-73 source audit — seat R73Source063 — row S063

Seat: R73Source063 · Date: 2026-10-30 · Lane: /home/vgpnk/Projects/shokunin/revenger-shokunin
Read-only production: no corpus/shared/sibling/fleet writes. Sole write: this report.
Scratch: /fast/scratch/hyaku/revenger-r73/r73source063/ (cleaned after receipts copied).
Tooling: no installs or updates this seat (curl/python3/sha256sum already present; pacman paused host-wide, not needed).

## Assigned registry row (verbatim, corpus/SOURCES.md:77)

| S063 | x64dbg — https://github.com/x64dbg/x64dbg | tool | A | The repository's Windows user-mode debugger description and architecture-specific launch paths; not execution on a Windows target | README.md introduction and "Installation & Usage", commit ac4db12e133a3b2a91756fd2fbe864aa8dd1c453, accessed 2026-10-27; "An open-source binary debugger for Windows, aimed at malware analysis and reverse engineering." | Its docs distinguish x32 and x64 debugger executables; that declared platform scope is not generalized to Linux/macOS | mined | 2026-10-27 | on-release | corpus/knowledge/round-72-tool-landscape.md |

## Round-72 lesson and entry wording

- Lesson Gate row (corpus/lessons/round-72.md:22):
  `S063 | https://github.com/x64dbg/x64dbg | 2026-10-27 | README introduction: "An open-source binary debugger for Windows, aimed at malware analysis and reverse engineering of executables you do not have the source code for." | ADMIT, tier A for the Windows user-mode scope; no Windows target was used.`
- Used-by entry (corpus/knowledge/round-72-tool-landscape.md:28): row "Need process instrumentation or debugging" cites "Frida S060; x64dbg S063; RAD Debugger S070" and states: "x64dbg describes a Windows user-mode debugger and x32/x64 launchers."
- Round-72 lesson (corpus/lessons/round-72.md:59): S063 destination re-surfaced via the shorteners; "Canonical URLs match the rows newly added this round; no duplicate source rows were added."

## Re-opened primary source (this seat, access date 2026-10-30)

- Cited URL/pin: https://github.com/x64dbg/x64dbg @ commit ac4db12e133a3b2a91756fd2fbe864aa8dd1c453
- Re-opened bytes: `https://raw.githubusercontent.com/x64dbg/x64dbg/ac4db12e133a3b2a91756fd2fbe864aa8dd1c453/README.md` → HTTP 200, 8920 bytes, sha256 `66607f0df8c2e5f30bcfa00de99e4b1df059215e89ac43ac28bc0cc6fb166f47`.
- Commit identity (GitHub API, HTTP 200): sha ac4db12e133a3b2a91756fd2fbe864aa8dd1c453, committer date 2026-07-16T13:30:11Z, message "Fix matrix contact URL". Pin resolves; the raw 200 independently proves the commit exists in this repo.
- Repo description metadata (GitHub API, HTTP 200): "An open-source user mode debugger for Windows. Optimized for reverse engineering and malware analysis."

## Located-quote verification (verbatim, markup normalized only)

Pinned README line 9 (introduction, first prose paragraph after the badge block; single occurrence in file):

`An open-source binary debugger for Windows, aimed at malware analysis and reverse engineering of executables you do not have the source code for. There are many features available and a comprehensive [plugin system](...) to add your own. ...`

1. **Registry located quote** — "An open-source binary debugger for Windows, aimed at malware analysis and reverse engineering." — **PRESENT, verbatim**, line 9, contiguous strict prefix of the full sentence. 13 words ≤ 25. ✓
2. **Lesson Gate quote** — "An open-source binary debugger for Windows, aimed at malware analysis and reverse engineering of executables you do not have the source code for." — **PRESENT, verbatim**, line 9, complete sentence. 18 words ≤ 25. ✓
3. **Anchor sections** — "Installation & Usage" section present (line 20); architecture-specific launch paths at line 24: "You can now run `x32\x32dbg.exe` if you want to debug a 32-bit executable or `x64\x64dbg.exe` to debug a 64-bit executable! If you are unsure you can always run `x96dbg.exe` and choose your architecture there." Both anchor claims in the row hold. ✓

## Scope, tier, used-by, rejection flip

- **Scope** ("Windows user-mode debugger description and architecture-specific launch paths; not execution on a Windows target"): README says "binary debugger for Windows" (line 9); "user mode" wording is the repo's own description metadata, corroborated above. x32/x64 launch paths verbatim at line 24. No Linux/macOS generalization anywhere in the README; "not generalized to Linux/macOS" (teaches cell) is accurate. This seat performed only static source reads; no target execution. **Agree.**
- **Tier A** (project's own README, primary self-description): appropriate; the row makes no version-specific or correctness claim beyond the project's own words. **Agree.**
- **Used-by** (round-72-tool-landscape.md:28): "x64dbg describes a Windows user-mode debugger and x32/x64 launchers" — both halves verified against the pinned README ("debugger for Windows" line 9; x32/x64 launchers line 24). "User-mode" modifier per repo description metadata, not the README sentence; corroborated, minor imprecision at most. **Agree.**
- **Rejection flip**: none. Status `mined` (admitted), consistent with the lesson Gate ADMIT, tier A. Round-72 verifier spotcheck (corpus/lessons/round-72-verifier-spotcheck.md:75) re-opened S063 among the extra README/catalog pages and recorded every checked quote ≤ 25 words, with no defect for S063. Disposition stands.

## Seat return values

- Located quote (≤25 words, verbatim): **"An open-source binary debugger for Windows, aimed at malware analysis and reverse engineering of executables you do not have the source code for."**
- Access date: **2026-10-30**
- URL: **https://github.com/x64dbg/x64dbg** (pinned README at commit ac4db12e133a3b2a91756fd2fbe864aa8dd1c453)
- **Agree** with the source disposition: keep S063 `mined`, tier A, used-by as recorded. No superseding row proposed for S063 (no quote defect found; registry quote is a verbatim prefix, lesson quote is the verbatim full sentence).

## S071/S082 context (recorded, not acted on)

Corpus/lessons/round-72-verifier-spotcheck.md:71-72,87-88 confirms routed quote defects for S071 (registry quote paraphrase; pinned README says "each one read and security-graded") and S082 (quote verbatim in S083's source, absent from S082's). Per claims.md, resolution is append-only superseding rows by the seats that own those rows; this seat owns S063 only and proposes **no** new row, consistent with "no other source admission; report only your assigned row."

## Network/source failures

None. All three fetches (pinned raw README, repo API, commit API) returned HTTP 200. No unreachable results treated as anything but verified-present.

## Evidence classification

- Observation: fetch receipts (HTTP 200, 8920 B, sha256 66607f0d…), line-9 verbatim matches for both quotes, line 20/24 anchor sections, commit metadata, API description string.
- Inference: "user-mode" scope modifier sourced from repo description metadata rather than the README sentence itself (corroborated, not contradicted).
- Unknown: nothing material to this row; historical GitHub shortener hops (round-72.md:59) were not re-traced this round beyond the canonical-URL note.
