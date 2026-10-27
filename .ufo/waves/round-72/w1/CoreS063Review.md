# CoreS063Review — x64dbg source and entry check

## Judgment: SUPPORT, with a minor citation/quotation correction

The S063 row is mined and names `corpus/knowledge/round-72-tool-landscape.md` in `used-by` (`corpus/SOURCES.md`, S063 row). The linked knowledge entry's process/debugging row does not claim x64dbg was installed or run, and its boundary says no target was run; it keeps platform and architecture claims per-project. Its Windows and 32-/64-bit scope is supported by the pinned README. No Linux/macOS capability is attributed to x64dbg.

## Exact source evidence

Pinned README: <https://raw.githubusercontent.com/x64dbg/x64dbg/ac4db12e133a3b2a91756fd2fbe864aa8dd1c453/README.md>

- Introduction: “An open-source binary debugger for Windows, aimed at malware analysis and reverse engineering of executables you do not have the source code for.” This matches the full quote in the round-72 lesson Gate (S063, `corpus/lessons/round-72.md`) verbatim; it is 23 words, within the 25-word limit.
- `Installation & Usage`, step 3: “You can now run `x32\\x32dbg.exe` if you want to debug a 32-bit executable or `x64\\x64dbg.exe` to debug a 64-bit executable!” It supports the entry's architecture-specific executable paths and scope. The README identifies `x96dbg.exe` as the optional architecture chooser; “x32/x64 launchers” in the knowledge entry is loose wording for the two debugger executables, not evidence of additional capability.
- The pinned commit page identifies `ac4db12e133a3b2a91756fd2fbe864aa8dd1c453`, title “Fix matrix contact URL,” and lists `README.md` as its sole changed file. The pinned `.patch` gives the commit date as `Thu, 16 Jul 2026 15:30:02 +0200`. The source row records this pin and access date 2026-10-27. The current `development` README and pinned README had identical SHA-256 (`66607f0df8c2e5f30bcfa00de99e4b1df059215e89ac43ac28bc0cc6fb166f47`; each 8,920 bytes) at review, so the checked content has not drifted there.

## Issue to correct

`corpus/SOURCES.md` S063 quotes: “An open-source binary debugger for Windows, aimed at malware analysis and reverse engineering.” The pinned README continues “of executables you do not have the source code for”; thus the row's closing period is not verbatim at that point in the sentence. The full sentence quoted by the lesson is exact. Revise the S063 source quote to use the full sentence (or omit the period from the excerpt) so the registry quote is exact and consistent with the lesson.

The knowledge entry calls this a “Windows user-mode debugger.” The phrase `user-mode` is absent from the pinned README, but the GitHub commit page's repository metadata (`meta-description`) states: “An open-source user mode debugger for Windows. Optimized for reverse engineering and malware analysis.” So this is supported by the repository's public description, not by the README locator currently named in the source row. To keep attribution precise, either add the repository description as a locator or drop “user-mode” from the README-based statement. This is a locator/attribution imprecision, not an unsupported platform claim.

## Limits

GitHub's commit API returned HTTP 403; commit date was confirmed from the public `.patch` endpoint instead. No tool execution, installation, or Windows-target activity was performed or inferred.