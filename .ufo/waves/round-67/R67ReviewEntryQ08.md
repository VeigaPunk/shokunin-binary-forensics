Q08 PASS — the entry's Q-map carries a Q08 row whose decision cell is exactly `superseded by Q11`, citing the correct supersession row.

# Evidence

- Entry under test: `corpus/knowledge/round-67-apk-axml-byte-evidence.md`, working-tree sha256 `170df17d82452fef310749e43d7d11661a943e2185594ad1de8c8446d33d968a`; committed at `7668510ffc49733daf023e40ff3300ef387ebde5` ("round-67: build — C05 v2 candidate …"); `git status --porcelain` on the entry and `corpus/QUALITY.md` is empty (committed bytes, unmodified).
- Q-map row, `corpus/knowledge/round-67-apk-axml-byte-evidence.md:151` (verbatim, raw read):
  `| Q08 | superseded by Q11 | QUALITY.md:23 — Q08 is historical; this map applies Q11 (applying Q08 instead would itself be a Q11 failure, round-66 adjudication table). |`
- Pointer check: `corpus/QUALITY.md:23` is indeed the Q11 criterion row and its first words are "Supersedes Q08." — the entry's `QUALITY.md:23` citation resolves to the correct supersession row.
- Q08 is not applied as a live criterion anywhere else in the entry: fixed-pattern grep for `Q08` over the file returns only two hits — the admission-status line `:8` ("…item-8 provenance sentence, item-9 dex spec row S045, Q08 Q-map row, dangling `### Code` pointer removed"), a repair manifest naming this very repair, and the Q-map row `:151` itself.
- The superseding criterion is actually applied: Q-map row `:154` marks `Q11 | pass |` with a derivation-and-output basis matching QUALITY.md:23's requirement — so the row is not merely decorative while Q08's old wording is enforced elsewhere.

# OFF-criterion observations

- OFF- The Q08 row's basis clause references a "round-66 adjudication table" by name only (no file:line pointer); harmless because the load-bearing pointer `QUALITY.md:23` resolves, but the secondary citation is unanchored.
- OFF- Display-length check only: all embedded JSON output lines verified complete (e.g. lines 85 and 183 end `…"offset": 272, "styleIndex": 0}`); apparent ellipses in some renders are truncation of long lines, not literal bytes. No defect.

No tools installed or upgraded; no installs needed for this read-only Q08 check.
