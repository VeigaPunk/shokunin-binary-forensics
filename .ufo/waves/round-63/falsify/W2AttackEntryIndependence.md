# W2AttackEntryIndependence — C1 / Q03

Reviewer: `revenger-r63.W2AttackEntryIndependence` (independent leaf; not the candidate author/corrector).
Reviewed committed tip: `db55bd6488e24e956df5818ae34c2a043d7ddc12`.
Candidate: `corpus/knowledge/round-63-zip-central-directory-evidence.md`, SHA-256 `a0158e99d3fa4b3cec132e03f5738015c39ca3abb56437ae1bab81e88f2d1b53`.

## Axes and scoped result

- **Attack: C1 / Q03, coverage K. Independence HOLDS.** Fresh-seat Q03 pass recommendation: no expected archive value copied from the saved REA record was found. This is a finding about the committed derivation, not canonical admission or a claim to know the author's historical thought process.
- **Attack: C1 / Q11, coverage K, incidental defect.** One printed word-count output is wrong: candidate lines 291–292 report `8`, but the exact displayed command returns `7`. This needs a one-line correction before treating all Q criteria as satisfied. It is not evidence of record-derived expectations.
- C2/F and C3/calibration are outside this leaf's assignment. No K/F/C3 acceptance-counter verdict, admission, integration, or README flip is made here. Freshness and preserved-byte holds are not traded away.

## 1. Blind byte derivation, before either JSON input was opened

**Attack: C1 / Q03.** The first computation, tool cell `Deriving archive numbers independently`, decoded the ZIP directly from `git show db55bd6488e24e956df5818ae34c2a043d7ddc12:corpus/fixtures/archive-r2/fixture.zip`. It also checked that committed ZIP bytes equaled the working-tree file. The cell completed at `2026-10-24T02:59:59.422026+00:00`. Only afterward did I open the candidate, `truth.json`, or `artifact-inspection.json`.

My decoder used `struct`, `zlib`, and `hashlib`, not `zipfile`, the candidate script, the oracle, the saved record, or a producer. It located EOCD candidates by signature and required the declared comment to end exactly at EOF; required a single candidate; unpacked the EOCD, every complete central header, and every complete local header; compared their overlapping fields; inflated raw DEFLATE in memory; recomputed CRC-32 and SHA-256; and checked adjacent local-member spans and the central-directory endpoint. No member was executed or written to disk.

### Independently decoded archive and EOCD

| Value | Byte-derived result |
|---|---|
| Archive size | 2964 bytes |
| Archive SHA-256 | `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e` |
| EOCD signature bytes | `504b0506` |
| EOCD offset / bytes to EOF | 2942 / 22 |
| Current disk / central-start disk | 0 / 0 |
| Entries on disk / total entries | 2 / 2 |
| Central offset / size / end | 2828 / 114 / 2942 |
| Central half-open / inclusive span | `[2828,2942)` / `[2828,2941]` |
| Comment length / bytes | 0 / empty |
| EOCD end | 2964 |

### Independently decoded member fields

| Field | `bin/checksum` | `README.txt` |
|---|---:|---:|
| Index | 0 | 1 |
| Central-header offset | 2828 | 2886 |
| Central signature bytes | `504b0102` | `504b0102` |
| Version made by | 788 | 788 |
| Version needed | 20 | 20 |
| Flags | 0 | 0 |
| Compression method | 8 | 8 |
| DOS time | 27855 | 27987 |
| DOS date | 23884 | 23884 |
| CRC-32 decimal | 3017776807 | 1923438513 |
| CRC-32 hex, header and recomputed | `b3df9ea7` | `72a557b1` |
| Compressed size | 2668 | 78 |
| Uncompressed / inflated size | 16160 | 84 |
| Filename length | 12 | 10 |
| Extra length / comment length | 0 / 0 | 0 / 0 |
| Start disk / internal attributes | 0 / 0 | 0 / 0 |
| External attributes | 2179792896 | 25165824 |
| Local-header offset | 0 | 2710 |
| Local signature bytes | `504b0304` | `504b0304` |
| Local filename / extra lengths | 12 / 0 | 10 / 0 |
| Payload start / end | 42 / 2710 | 2750 / 2828 |
| Filename bytes hex | `62696e2f636865636b73756d` | `524541444d452e747874` |

Both local headers independently reproduce the corresponding central header's version-needed, flags, method, DOS time/date, CRC-32, compressed/uncompressed sizes, and filename. Central extra fields and comments are empty. Totals: 2746 compressed bytes, 16244 inflated bytes, 82 local-header/name bytes, and 114 central bytes; `2746 + 82 + 114 + 22 = 2964`.

Inflated payload digests:

- `bin/checksum`: `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`.
- `README.txt`: `7d8f6a8de39432f4119f0139c5ef5970c84c23520cfe6b40d19a3653081804d3`.

Compressed-payload digests, derived independently although not needed by the entry:

- `bin/checksum`: `4f97417595ef16aed9a674b040aa8e7c2c288c69de50c318c792f0ad04620a79`.
- `README.txt`: `1913a9f12ca815c3f821f92c66987bed5a8a4dc108a62b526f78b22d648bd34d`.

Decoder formats were `<4s4H2IH` (EOCD), `<4s6H3I5H2I` (central), and `<4s5H3I2H` (local). Expanding their types independently gives all field offsets/widths and fixed lengths 22, 46, and 30. These match the entry's complete `spec_derived_field_offsets` fact, not merely its selected prose offsets.

## 2. Comparison against the committed entry and source files

**Attack: C1 / Q03.** After the blind computation I extracted the candidate's complete Python code block from the pinned committed entry and ran it, unmodified, with `python3 -B -c CODE /home/vgpnk/Projects/shokunin/revenger-shokunin`. I also independently ran all 17 `--fact ID` selections. The working-tree entry and all four input files equaled their committed bytes. All four input files also equaled the base commit `55bcb6e1aeb4d42923a4e98db6580f67142b41ac`.

| Reexecuted measurement | Observed result |
|---|---|
| Full readout exit | 0 |
| Stdout line count (`wc -l`) | 17 |
| Stdout SHA-256 | `02b0f495c1db8c50e22db835cd57e7a221dd0a9c82f09d442feea461de722ed4` |
| Script line count (`wc -l`) | 328 |
| Script SHA-256 | `94f502cde75eb47ffd3d7d8a73de45ad8889337a5269b669d998126a063a4bac` |
| Full printed stdout versus rerun stdout | Byte-identical |
| Individually rerun facts versus full stdout | All 17 identical |
| Independent byte/spec fact groups compared | 8 |
| Top-level field comparisons, including whole nested offset/check maps | 119 |
| Disagreements against my independent decoder | 0 |

The eight groups are `archive`, `eocd`, `central_directory`, both `member_cd[...]`, both `member_local[...]`, and `spec_derived_field_offsets`. Every central-header field and every local-header fact was compared, not just the member-size/hash subset. `truth.json` separately agrees with my decoder on the archive digest/length, both member names, both compressed/uncompressed sizes, and both inflated digests.

Reopened new source rows: `corpus/SOURCES.md:46-47` (S032 and S033). I reopened the primary [PKWARE APPNOTE](https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT), including §4.3.3, §4.3.7, §4.3.12, §4.3.16 and §4.4.16, and the own-work ZIP, oracle, saved record, and ledger. The committed APPNOTE snapshot measures 174585 bytes and SHA-256 `0b993022a7d320a0bf704e6980bea36fafd17a6066ab994db0a0c16278a50cd6`, matching the entry.

Committed input hashes independently checked at base, review tip, and worktree:

- ZIP: `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`.
- Oracle: `7df773bf46b7c1273f8c3402b7825e7dacbb7f990c7d7ef41f30917c94726e68`.
- Saved record: `2fec924b5217885674149b6a516970f419a8e731c8e6e49eab178a4f065f3380`.
- Ledger: `05042a555f91511c9c191565d92f83527f54d1c9b14de331587f4cbffff9e6cb`.

## 3. Strongest attempted counterexample: poison the compared documents

**Attack: C1 / Q03, false provenance and identity/locator reuse.** I ran seven experiments concurrently in fresh Python subprocesses. Each executed the exact committed candidate code; an `open` hook supplied an in-memory map of committed input bytes with the listed substitutions. The hook refused any other path or non-`rb` access. The unchanged-input control produced byte-identical stdout to the direct command. Neither corpus files nor candidate code were mutated.

| Input experiment | Observed output | Independence result |
|---|---|---|
| Unchanged inputs | Exact original stdout | Baseline |
| Forge both members' saved declared/compressed sizes, all saved node sizes/digests, and saved subject digest | All 8 member size/digest correspondence booleans become false | All 8 independent fact groups unchanged |
| Rename both saved member paths to `forged/<original>` | Both independently named members reported absent; missing-set contains the two byte-derived names | All 8 independent fact groups unchanged |
| Swap the two saved member-to-node artifact links | Both node-size and both node-digest comparisons become false; occurrence sizes remain true | All 8 independent fact groups unchanged |
| Reverse saved node and occurrence arrays | Member comparisons unchanged | All 8 independent fact groups unchanged |
| Replace saved artifact IDs with arbitrary opaque labels, consistently in nodes and occurrences | Member comparisons unchanged | All 8 independent fact groups unchanged |
| Forge oracle archive/member sizes and digests | All 8 oracle size/digest correspondence booleans become false | All 8 independent fact groups unchanged |

All experiments exit 0 because this script prints observations; it is not a rejection verifier. A false printed comparison is the observed result, not a claimed deletion-sensitive guard or attributed kill.

Static dataflow confirms the experiment:

- Candidate lines 399–503 derive the archive, EOCD, central members, local payloads, inflated hashes and CRCs entirely from `zip_bytes` and specification constants.
- `truth.json` is first read at line 505, after those values exist. `inflated_sha` comes from the earlier byte-derived local facts at lines 507–508.
- Saved record bytes are first read at line 537. Lines 554–575 iterate `members` derived from ZIP bytes and compare record fields against those members and earlier inflated hashes.
- `by_path` is only a record-side locator. Expected member identity comes from ZIP filename bytes, not from the saved path. Saved artifact IDs locate saved nodes; they are not expected content identity. Relabeling and link-swap experiments distinguish those roles.
- Evidence IDs, provider id/version, operation, saved occurrence count, `executable`, `encrypted`, and `hash_status` are explicitly **recorded observations**, not independent expected archive values. Their appearance in the entry is not a hidden source for the expected side.

**Copied expected values found: none.** Smallest safe Q03 correction: none needed. This conclusion is limited to the committed one-fixture derivation; it does not establish record authenticity, parser generality, completeness, or an external history of oracle creation.

## 4. Incidental counterexample requiring a small correction

**Attack: C1 / Q11, coverage K.** Reexecuting all ten displayed word-count inputs yielded, in candidate command order:

```text
7, 21, 7, 10, 8, 23, 24, 20, 23, 12
```

The third command is candidate lines 291–292:

```sh
printf '%s\n' 'local file header signature 4 bytes (0x04034b50)' | wc -w
```

Actual output, independently exercised also as the literal shell pipeline:

```text
7
```

The entry prints `8`. The initial all-counts assertion therefore failed at that one item; inspecting the actual ten command results isolated it, and the remaining measurement commands were then completed. All other nine word counts agree and all quotes remain at most 25 words.

Smallest safe correction: change only the printed third word-count output from `8` to `7` at candidate line 292; do not weaken Q11, change the quote, or infer all-criteria admission from this Q03 finding. This is a fixable transcription defect, not a tradeoff and not an independently established Q03 failure. The defect was sent to L1 and `revenger-r63.W2AttackEntryQ11` for their scoped decision.

## Tooling and preservation

Python 3.14.8 standard library plus existing `git`, `wc`, and `sha256sum` only. No install/update or pacman transaction; no model arguments, producer call, target execution, other agent runtime, judge, admission, commit, git/jj mutation, or index change. No scratch files or directories were created, so there is no heavy scratch to remove. Only this named report path was written.
