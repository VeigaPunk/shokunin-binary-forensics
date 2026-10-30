# R73Source059 — round-73 v2 source audit (S059, iBotPeaches/Apktool)

Seat: R73Source059 · Role: reviewer (source audit) · Axes: coverage, source accuracy.
Scope: SOURCES.md row S059 only, with its round-72 lesson Gate row and linked entry
wording. No other source admission. Read-only lane; this report is the only write.

## Judgment: AGREE — disposition ADMIT tier A stands; no superseding row proposed

No quote defect, no scope drift, no tier mis-assignment, no rejection flip. S059 is not
one of the routed round-72 defect rows (S071/S082 in corpus/lessons/round-72-verifier-spotcheck.md),
so no append-only superseding row is proposed here.

## Located quote (verified this seat, access date 2026-10-30)

- Quote (15 words, ≤25 Gate): "It can decode resources to nearly original form and
  rebuild them after making some modifications"
- URL (pin reopened this seat):
  https://raw.githubusercontent.com/iBotPeaches/Apktool/0312d212c713c9ebc568b7d9295eec0f47858bfa/README.md
  (repo page cited by row: https://github.com/iBotPeaches/Apktool)
- Pinned fetch result: HTTP 200, text/plain, 3372 bytes, sha256 of fetched body
  a12dbea8be721e72124c45c4c96907375ef2b8e84d0f8386dcfd3a383454baaf.
- Control: same URL at bogus SHA 0000…0000 returned HTTP 404 — resolution is
  commit-SHA-sensitive, so the 200 is genuine pin resolution, not default-branch fallback.
  [observation]

## Verbatim and anchor

- [observation] Fetched pinned README line 7 reads in full: "Apktool is a tool for
  reverse engineering third-party, closed, binary, Android apps. It can decode resources
  to nearly original form and rebuild them after making some modifications; it makes it
  possible to debug smali code step-by-step. It also makes working with apps easier
  thanks to project-like file structure and automation of some repetitive tasks such as
  building apk, etc."
- [observation] The registry quote is a verbatim 15-word substring ending exactly before
  the semicolon; identical wording in the lesson Gate row (corpus/lessons/round-72.md
  line 18). Normalizing markup only; no wording difference.
- [observation] Anchor: the quote sits in the first paragraph directly under the
  `### Apktool` heading (line 1 of the file; locator "README.md 'Apktool'" does not
  claim a heading level, so the level-3 heading and preceding italic website note
  introduce no mismatch).

## Scope, tier, used-by, status

- [observation] Role (SOURCES.md line 73): "The repository's own stated Android
  resource/Smali decode and rebuild purpose; no APK correctness or permission claim."
  The pinned README's first sentence does state a reverse-engineering purpose; the row
  deliberately cites only the decode/rebuild clause, and the note adds "this entry does
  not claim the output is source-identical, install-valid, or appropriate for unlicensed
  modification." The README's own line 9 corroborates the boundary: "Apktool is **NOT**
  intended for piracy and other non-legal uses." Under-claiming relative to what the
  source permits — the safe direction. The "nearly original form" hedge is preserved
  inside the quote and never upgraded to "original".
- [observation] Tier A is correct: the cited text is the project's own README (primary).
- [observation] Status `mined`, accessed 2026-10-27 (original access; this audit re-accessed
  2026-10-30), cycle `on-release`; used-by corpus/knowledge/round-72-tool-landscape.md,
  and that entry's row "Need Android/APK output views" cites "JADX S058; Apktool S059"
  with boundary "Decompiled or rebuilt files are not the original source or proof of
  install validity. The lane must remain static/artifact-first; no package is installed
  here." Round-trip citation holds. claude-red-re-bridge.md line 36 lists S059 only as
  existing coverage ("likely redundant"), no new claim.
- [observation] Registry id unique: exactly one `| S059 ` row in corpus/SOURCES.md.

## Rejection-flip check

- [observation] Flip conditions tested: quote absent from pinned source (present, verbatim);
  claim beyond source (none — decode/rebuild only, disclaimers in place); wrong tier
  (primary README, tier A correct); source unreachable (reachable, HTTP 200 with 404
  control). [inference] No grounds to flip ADMIT tier A; the round-72 lesson Gate row's
  decision ("ADMIT, tier A for the README's stated decode/rebuild role, not install
  validity or permission to modify third-party apps") is confirmed.

## Non-blocking precision note (carried from round-72 CoreS059Review; unchanged)

- [observation] The README literally says "decode resources to nearly original form" and
  "it makes it possible to debug smali code step-by-step"; it does not literally say
  "decodes Smali". The row's "resource/Smali decode" role and the entry's "resource and
  Smali decoding and a rebuild path" are fair paraphrases (smali debugging presupposes
  decoded smali output), not inventions. Optional future tightening: quote the smali-debug
  clause or the README's explicit RE sentence. Does not touch the C10 predicate and does
  not change disposition.

## Network / source failures

- None. Both fetches succeeded (200 pinned, 404 bogus control). No rate-limit encountered
  on raw.githubusercontent.com this seat.

## Provenance, tools, hygiene

- No tool installs or updates this seat (curl/coreutils only; system tools). Pacman pause
  honored; no installs at all.
- No git/jj mutations; no target execution; no live-target requests beyond the two cited
  static fetches; no secrets touched. Fetched README text treated as untrusted data; no
  embedded instruction followed.
- Scratch /fast/scratch/hyaku/revenger-r73/R73Source059 removed after this report was
  written (fetched README hash recorded above).

## Unknowns / verification gaps

- [unknown] Commit author/date metadata not re-checked via GitHub API this seat (round-72
  review inferred timestamp from page metadata); not required for the quote/scope verdict.
- [unknown] Lane stores no pinned-README hash for S059; identity rests on verbatim quote
  match at the SHA-pinned URL plus the bogus-SHA 404 control.

Report: .ufo/waves/round-73/v2/R73Source059.md
