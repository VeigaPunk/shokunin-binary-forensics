GRADE: HOLDS — C09 header citation "S017 Yellow Paper Shanghai efc5f9a §9.4.3 eqs. (160)-(162), p.15" (`corpus/knowledge/evm-saved-interface-candidates.md:1`; `corpus/SOURCES.md:31`)

Target of attack: the S017 citation, re-fetched from the cited URL rather than trusted from the row. Lane under test: landed `ab580698212258a55e43e9bb9bf6ac78c91eae2a`. Scratch: `/tmp/revenger-r61w3-W3EvmYellowPaperCite`. No lane writes; no git/jj mutation (read-only `show`/`diff` only). No REA calls; no bytecode or fixture execution.

## Findings (observation)

1. **Fetch and byte identity.** `curl -sSL -o paper.pdf https://ethereum.github.io/yellowpaper/paper.pdf` → `HTTP 200 bytes=597589`; `sha256sum paper.pdf` → `d67c009c5d5a0542c8288aee3c4d470b3e2dbe6e664f72f00011543608477fa9`. That is character-for-character the digest recorded at `corpus/SOURCES.md:31` and `corpus/lessons/round-61.md:53`. HTTP `last-modified: Tue, 04 Feb 2025 14:03:41 GMT`, `pdfinfo` CreationDate `Tue Feb 4 11:02:58 2025 -03` (= 14:02:58Z). The cited row pins a mutable URL by digest and the pin still resolves.
2. **Revision.** PDF p.1, line 2 (`pdftotext -layout -f 1 -l 1`): "SHANGHAI VERSION efc5f9a – 2025-02-04" (en dash, U+2013). Matches the row's quoted title-page string exactly. `https://api.github.com/repos/ethereum/yellowpaper/commits/efc5f9a` → `efc5f9a1f356cba376c978eedb63cb0363c2aa85`, author date `2025-02-04T14:00:54Z`, message "🐞 fix: Correct 'form' to 'from' in withdrawal description (#923)". [INFERENCE] The 124 s gap commit→PDF build time is consistent with, but does not prove, a build from that commit.
3. **Section.** `pdftotext -layout -f 15 -l 15` page header reads "SHANGHAI VERSION 15" (printed page = PDF page 15). p.15 contains "9.4.2. Exceptional Halting" with eq. (158) and "9.4.3. Jump Destination Validity". §9.4.4 "Normal Halting" opens p.16 at eq. (163), so §9.4.3 ends on p.15. Citation section and page are exact.
4. **Equation numbers.** On p.15 only: `pdftotext -f 15 -l 15 paper.pdf - | grep -o '(1[5-6][0-9])' | sort -u` → `(150) (151) (152) (153) (154) (155) (156) (157) (158) (159) (160) (161) (162)`. Each of `(160)`, `(161)`, `(162)` occurs exactly once in the whole 42-page text (`grep -c` → 1, 1, 1; `(163)` → 1). (160) is `D(c) ≡ DJ(c, 0)`, (161) defines `DJ(c, i)` over `c[i] = JUMPDEST`, (162) defines `N(i, w)` skipping PUSH data ("if w ∈ [PUSH1, PUSH32]", "i+1 otherwise"). The cited range is the complete formal content of §9.4.3, not a loose span.
5. **Verbatim rule, quoted from the fetched PDF, §9.4.3 p.15:** "All such positions must be on valid instruction boundaries, rather than sitting in the data portion of PUSH operations" (19 words; full sentence continues "and must appear within the explicitly defined portion of the code …"). Same 19 words, same location, appear at `corpus/lessons/round-61.md:56`. The lesson's truncation ends at a clause boundary and omits the continuation without an ellipsis — a nit only, since every quoted word is contiguous and verbatim.
6. **Entry usage matches the source.** `evm-saved-interface-candidates.md:23-24` says only "S017 states the same rule for the Shanghai revision", i.e. the PUSH-data exclusion that S016 states; §9.4.3 states exactly that, and eq. (162) formalizes it. The entry does not attribute opcode byte values (0x63/0x14/0x57/0x5B) to S017; line 20 attributes them to S016 only. No overstatement.
7. **Row was opened in round 61, not inherited.** `git show cf02419…:corpus/SOURCES.md | grep S017` → no output (row absent at base). `git diff --stat cf02419… ab58069… -- corpus/SOURCES.md` → `1 file changed, 17 insertions(+)`; the added lines include the S017 row, the S025 rejection that names S017 as the tier-A comparator, and the S016→S017 reading path (`corpus/SOURCES.md:49`). Round-61 freshness condition satisfied.
8. **Tier-A scope is adequate for the cited use.** S017's declared scope is "the paper's definition of valid jump destinations and JUMP/JUMPI validity, Shanghai revision only" (`corpus/SOURCES.md:31`). Eq. (158) on p.15 carries the JUMP/JUMPI invalid-destination halting conditions; (160)-(162) carry the destination set and PUSH skip; `D(c)` recurses over the whole code with no reachability term, which supports the row's "whole-code candidate set, not reachability" summary. The entry rests only on the PUSH-data clause.

## Inference / limits

- The check proves the currently served bytes equal the pinned digest and that those bytes say what the row and entry claim; it does not independently prove the author fetched the same bytes on 2026-10-21 (only that the digest they recorded is reproducible today). [INFERENCE] provenance is consistent, not witnessed.
- `pdftotext` drops the brace/rule glyphs of the (161)/(162) cases, so equation bodies are legible but not layout-faithful; the equation *numbers* are unambiguous.
- Not checked: the LaTeX source at efc5f9a, and whether a later Yellow Paper build renumbers equations. Both are outside the pinned-digest contract the row uses.
- Possible wording nit, not a criterion failure: `evm-saved-interface-candidates.md:177` compresses the Q01 basis to "opcode values and the PUSH-data rule rest on S016/S017". Read as a pairing in order it is exact and line 20-24 disambiguates; read as a union it would over-credit S017 with opcode byte values, which live in Appendix H outside S017's declared scope. No load-bearing sentence depends on the union reading.
- Q01-Q11: nothing in this item contradicts an entry or source-row sentence. No changed saved record, no lost hold, no unopened row.

## Commands (reproducible)

`curl -sSL -o /tmp/revenger-r61w3-W3EvmYellowPaperCite/paper.pdf https://ethereum.github.io/yellowpaper/paper.pdf && sha256sum paper.pdf && pdfinfo paper.pdf`
`pdftotext -layout -f 1 -l 1 paper.pdf -` ; `pdftotext -layout -f 15 -l 15 paper.pdf -` ; `pdftotext -layout -f 16 -l 16 paper.pdf -`
`pdftotext -f 15 -l 15 paper.pdf - | grep -o '(1[5-6][0-9])' | sort -u`

## Installs

None. `pdftotext`/`pdfinfo` (poppler 26.08.0) already present at `/usr/bin`; `curl`, `python3` stdlib only. No pacman transaction attempted.

VERDICT: HOLDS — revision `efc5f9a`, section §9.4.3, equations (160)-(162), page 15 and the PUSH-data rule all match the C09 header and SOURCES row S017 byte-for-byte; S017 is a round-61 row (absent at base) and the entry does not exceed it.
