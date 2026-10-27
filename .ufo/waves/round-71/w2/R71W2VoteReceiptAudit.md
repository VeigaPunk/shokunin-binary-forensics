PASS on receipt integrity / FAIL on C1 binding — all four vote receipts are contract-clean, uniquely owned and agree with their reports, but two carry `FAIL` (Q09, Q16) with located defects I reproduced independently, so the A2 counter reads `C1_W2_Q_VOTES=0/16` and C1 cannot flip; the receipts are also still untracked, so the committed-TREE binding is 0/16 at HEAD `33fadb2`.

Seat `R71W2VoteReceiptAudit`, leaf, read-only. No source, routing, vote or report of another seat was modified. Audit window 2026-10-27T16:04Z–16:37Z. Lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`.

## Bound objects

| object | value |
|---|---|
| candidate | `4c1eeaee88fd07e442f1bd546faf77be3957d390` |
| HEAD at first check | `c6e284c6583fa3502754361f411b66646880ba02` |
| HEAD at intermediate checks | `a16e6cbe24c51e6952e973d6b47560b49311420d` |
| HEAD at final check | `33fadb25cdb260ee4a6ac2b0a2bb62c4c1bb8057` |
| entry bytes (candidate = worktree = HEAD) | `sha256 671f55fceb64af27f99c00106f58f9bc2c8b5dc9af6028382ff218655008f092` |

`git diff --stat 4c1eeae HEAD -- corpus/knowledge/round-71-apk-axml-byte-evidence.md` → empty; `git show 4c1eeae:<entry> | sha256sum`, `sha256sum <entry>` and `git show HEAD:<entry> | sha256sum` all printed the same digest above, so every receipt was cast on the frozen entry bytes, not a drifted copy.

## Receipts present (4/4, exact names)

`.ufo/waves/round-71/w2-votes/` contains exactly four files and nothing else:

| file | bytes | sha256 | seat | decisions |
|---|---|---|---|---|
| `R71W2Q01Q04.json` | 88 | `3b03a703aa2d05e5afb4b6222cd9e14b2cb2e0b70fe98d9cee0c7c66c3a50ca2` | `R71W2Q01Q04` | Q01 PASS, Q02 PASS, Q03 PASS, Q04 PASS |
| `R71W2Q05Q08.json` | 89 | `7bdb06cdffff7004b8f1613f82aa0ef7a2323137fd0d7789f516500e9dafc6b2` | `R71W2Q05Q08` | Q05 PASS, Q06 PASS, Q07 PASS, Q08 PASS |
| `R71W2Q09Q12.json` | 87 | `140ae8628a74b0df5ab2b8ca43fc80c062caa709b0990115b28fa13c91592bbc` | `R71W2Q09Q12` | Q09 **FAIL**, Q10 PASS, Q11 PASS, Q12 n/a |
| `R71W2Q13Q16.json` | 88 | `f486e464c3dc16f21f6b5456f2645438312e2061a51ee3320fe98b4a25938144` | `R71W2Q13Q16` | Q13 PASS, Q14 PASS, Q15 PASS, Q16 **FAIL** |

Raw bytes (single line each, no trailing newline, no BOM, no Markdown):

```
{"seat":"R71W2Q01Q04","decisions":{"Q01":"PASS","Q02":"PASS","Q03":"PASS","Q04":"PASS"}}
{"seat":"R71W2Q05Q08","decisions":{"Q05":"PASS","Q06":"PASS","Q07":"PASS","Q08":"PASS"}}
{"seat":"R71W2Q09Q12","decisions":{"Q09":"FAIL","Q10":"PASS","Q11":"PASS","Q12":"n/a"}}
{"seat":"R71W2Q13Q16","decisions":{"Q13":"PASS","Q14":"PASS","Q15":"PASS","Q16":"FAIL"}}
```

## Contract checks — all clean

Each file was downloaded through `json.loads(text, object_pairs_hook=<reject-duplicate-keys>)` and compared against the A2 `EXPECTED_VOTES` map:

- UTF-8 decodes, no `EF BB BF` prefix (`od -An -tx1 <file>` first row), no backticks anywhere.
- Root is a JSON object with exactly `seat` and `decisions` — no extra root keys.
- File stem equals `seat` for all four (`R71W2Q01Q04`, `R71W2Q05Q08`, `R71W2Q09Q12`, `R71W2Q13Q16`).
- `decisions` keys are exactly the assigned quadruple per seat; Q01–Q16 each owned by exactly one file; no duplicate Q key and no duplicate seat file.
- Values are inside `PASS | n/a | FAIL` only. `n/a` appears once (Q12) and is accepted by the A2 parser; no `FAIL` is hidden inside another key.
- No fifth `.json` and no non-JSON file exists in the directory, so no stray writer or shared file entered the `w2-votes` namespace.

## Counter parity (A2 `q_votes` port)

I re-implemented `measure.py:q_votes` byte-for-byte (`EXPECTED_VOTES` + `unique_object` + stem/seat/keyset/PASS-or-n/a rules) and ran it on the live directory and on `git archive HEAD` extraction:

- `COUNTER_Q_VOTES_LIVE=0/16` — 0 because two receipts carry `FAIL`, which A2 rejects by design. The receipts are structurally complete; the label is the kill signal, not a malformed-input result.
- `COUNTER_Q_VOTES_COMMITTED=0/16`, `git ls-tree -r --name-only HEAD .ufo/waves/round-71/w2-votes/` → 0 paths, `git status --porcelain .ufo/waves/round-71/w2-votes/` → `?? .ufo/waves/round-71/w2-votes/`. The directory is untracked at `33fadb2`, so the committed-TREE evidence A2 requires does not exist yet.

Harness calibration (synthetic receipts in `/fast/scratch/hyaku/revenger-r71/R71W2VoteReceiptAudit/`, never in the lane; my port vs the A2 semantics):

```
control: four valid PASS files            16
duplicate JSON key Q01                     0
non-object root                            0
stem != seat                               0
extra Q key in one seat                    0
Q12 n/a is accepted                       16
a FAIL vote scores 0 (kill)                0
UTF-8 BOM on one file                      0
```

The control row reproduces `vote-parser-control.txt` (16 for a valid four-seat PASS set), and every malformed shape collapses to 0, so the parity above is a calibrated reading rather than a bare assertion.

## Reports and outputs agree with the files

For each seat I matched the receipt JSON against the seat's own report (per-Q verdict tokens near the Q key, plus report first line):

| seat | report | first line | per-Q token agreement |
|---|---|---|---|
| `R71W2Q01Q04` | `w2/R71W2Q01Q04.md` | `PASS — Q01–Q04: …` | Q01–Q04 all PASS, matches file |
| `R71W2Q05Q08` | `w2/R71W2Q05Q08.md` | `PASS — Q05–Q08 hold on the final v6 entry: …` | Q05–Q08 all PASS, matches file |
| `R71W2Q09Q12` | `w2/R71W2Q09Q12.md` | `FAIL — Q09: the Q-map says an out-of-corpus builder is named as undigested, but the entry names no such script` | Q09 FAIL, Q10 PASS, Q11 PASS, Q12 n/a — matches file |
| `R71W2Q13Q16` | `w2/R71W2Q13Q16.md` | `FAIL — Q16 has a located output-overclaim: item 17 says it compares the AXML field offsets the readout uses, but its output compares only string-pool and attrExt subsets.` | Q13 PASS, Q14 PASS, Q15 PASS, Q16 FAIL — matches file |

No report contains a fenced JSON block pretending to be a vote.

**Located gap (not a receipt defect):** `.ufo/waves/round-71/w2-results.json` does not exist (`ls` → no such file) while `w1-results.json` does, so the "each mapped seat is a fresh reviewer in `w2-results.json`" and "output agrees with the vote file" legs cannot be proven from that artifact at this time. The mapping is otherwise supported: `w2/swarm-registry.json` lists all four seat ids with `kind=spawn`, `role=reviewer`; `W1_SEAT_REUSE=[]` (none of the four appears in `w1-results.json`, so no wave-1 seat voted); each seat wrote its own distinct file and its own distinct report. Registry `agentId` is `null` for all four members, so the registry itself carries no identity proof — consistent with A2's own statement that the per-seat files are structural receipts, not cryptographic identity proof.

Observation for L1's read, not a mismatch: the receipt says `Q08: PASS` while the entry's own Q-map row at line 306 marks Q08 `superseded`; the seat's report justifies the deference to Q11, and the A2 counter compares only against its fixed Q keysets, so the receipt is valid. `Q12: n/a` likewise matches the entry's Q12 row.

## Located defects forwarded (reproduced, not repaired)

**Q09** — entry line 307 states the Q09 basis as "…the builder script outside `corpus/` is named as undigested." Every script path printed in the entry is inside `corpus/` (`readout.py` 49+20, `entry_checks.py` 13+5, `generator.py` 5+1, `corpus/derive_axml_anchors.py` 3, `corpus/check_embedded_outputs.py` 1), and item 14 hashes the only named builder, `corpus/fixtures/apk-r65/generator.py` (line 225, `sha256 eaa9444c… 9599 bytes`). No outside-corpus builder exists to be "named as undigested", so the Q09 row overstates the entry's digest scope. The seat's `FAIL` stands.

**Q16** — entry line 251 (item 17) claims "The AXML field offsets the readout source uses, compared with sums of a second manual transcription of S038's struct widths". Reproduced: `python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout` exits 0 and prints 24 lines — 5 struct-width rows, 1 fixed-part note, 5 `ResStringPool_header` literal rows, 7 `attrExt` rows, 6 `attribute` rows. The comparison lists do not cover every offset the readout uses: `readout.py:189` reads `line = u32(axml, base + 8)` and `readout.py:197` reads `style_index = u16(axml, base + 34)`, and neither `base + 8` nor `base + 34` appears in the 24-line output. Item 17's universal wording is therefore wider than its printed evidence. The seat's `FAIL` stands.

Per the frozen contract these are located defects; reporting them does not license a repair or a re-gate after scoring.

## Consequence under the frozen rule

The four receipts exist and are structurally valid, but the vote conjunct is not satisfied for C1: two `FAIL` decisions make `C1_W2_Q_VOTES=0/16` under A2, and the receipts are still untracked so the committed-TREE measurement would also read 0/16. The frozen kill rule — any Q `FAIL` with a located defect keeps README uncovered, marks only the v6 `admission-status` line rejected, and reports C1 falsified/honest stop — applies on Q09 and Q16. I made no SCORECARD/LOG/README/entry change and flipped nothing; adjudication and integration belong to L1 alone.

Integration requirements if L1 proceeds to a measured tip: commit `.ufo/waves/round-71/w2-votes/` as bytes inside the archived TREE (A2 reads the directory under the measured `TREE`, not the live lane path), and materialize `w2-results.json` with all four seats as `reviewer` so the output-vs-file leg becomes provable.

## Exact commands used

```
git -C <lane> rev-parse HEAD                      → 33fadb25cdb260ee4a6ac2b0a2bb62c4c1bb8057
git -C <lane> ls-tree -r --name-only HEAD .ufo/waves/round-71/w2-votes/  → (0 paths)
git -C <lane> status --porcelain .ufo/waves/round-71/w2-votes/           → ?? .ufo/waves/round-71/w2-votes/
sha256sum .ufo/waves/round-71/w2-votes/*.json     → four digests as tabled above
git -C <lane> show 4c1eeae:corpus/knowledge/round-71-apk-axml-byte-evidence.md | sha256sum
sha256sum corpus/knowledge/round-71-apk-axml-byte-evidence.md
git -C <lane> show HEAD:corpus/knowledge/round-71-apk-axml-byte-evidence.md | sha256sum
                                                    → 671f55fc…f092 (identical three times)
python3 -B corpus/fixtures/apk-r65/entry_checks.py --axml-layout | cat -n   → 24 lines, exit 0
grep -oE "[A-Za-z0-9_/.-]+\.py" corpus/knowledge/round-71-apk-axml-byte-evidence.md | sort | uniq -c
grep -n "line = u32\|style_index = " corpus/fixtures/apk-r65/readout.py    → 189: base + 8, 197: base + 34
python3 <audit harness>                           → PROBLEMS: none
```

`audit.py` plus the mutant calibration ran from `/fast/scratch/hyaku/revenger-r71/R71W2VoteReceiptAudit/`; the directory was deleted after this report was written. No tool was installed (no `pacman` transaction), no routing or global config touched, no commit/push performed, nothing written outside this report.

Report: `.ufo/waves/round-71/w2/R71W2VoteReceiptAudit.md`
