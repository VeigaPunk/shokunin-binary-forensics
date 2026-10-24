# R65ReviewEntryQ13 — criterion Q13 on the round-65 C05 candidate

PASS (Q13) — no `verify_*.py` script is credited anywhere in the entry and the entry's only recheck credit is its own readout, credited exactly for what its run shows (exit 0, 15 lines, stdout SHA-256), all three reproduced. One **blocking off-criterion defect** found while replaying the entry's commands: entry line 41 is not verbatim readout output (Q11/Q02, not Q13) — the entry is not admissible as written.

Reviewed bytes: commit `8214e4dd7289d5a96cc23c0b2bf6407a9a43dbe0`, blob `f02952afa622de99e3399fd098ad9db297083feb` for `corpus/knowledge/round-65-apk-axml-byte-evidence.md`, worktree file identical (`git diff --stat HEAD -- <path>` empty), sha256 `e173e6436e9b8cce2ddd9f318b914fde6fd9bdfaf18335f5a873ac60fa3cdfb7` (20754 bytes). Criterion text: `corpus/QUALITY.md:25` (Q13, mistake class M22). Assignment summary of Q13 matches the frozen text: credit only for clauses whose deletion the run is shown to detect, other clauses named unguarded.

## Q13 core check — negative for verifier credit

```
$ grep -c (pattern 'verify_' entry)              -> 0 occurrences
$ grep -oE 'verify_[A-Za-z0-9_]+\.py' entry      -> 0 matches
$ grep -n '^#' entry -> 9,13,119,123,129,133,137,154   (no ### headings)
```

Every script named in the entry is one of its own four fixture files, cited as source S041 (entry:3): `fixture.apk`, `truth.json`, `generator.py`, `readout.py`. No `corpus/verify_icon_languages.py` / `verify_multi_icon_states.py` (this round's C2 surfaces) and no other verifier is named or credited. The two occurrences of the word "verifier"/"verification" are disclaimers: entry:6 "Not covered: install/signature verification" and entry:11 "no verifier source is read".

Recheck credit scope (entry:5, entry:162) is `python3 -B corpus/fixtures/apk-r65/readout.py` -> "exits 0 and prints 15 stdout lines whose SHA-256 is `507d79f8...`". Reproduced on a committed archive at two different extraction roots:

```
$ git -C <lane> archive HEAD corpus/fixtures/apk-r65 | tar -x -C /tmp/q13a
$ cd /tmp/q13a && python3 -B corpus/fixtures/apk-r65/readout.py > /tmp/q13a.out; echo exit=$?
exit=0
$ wc -l < /tmp/q13a.out ; sha256sum /tmp/q13a.out
15
507d79f8362b2c48640c1f0f9343dd3de2497c406df91de7c1ef0a1596dad247
$ (same archive at /tmp/q13b/deeper/nest) -> sha256 identical; cmp -> STDOUT_IDENTICAL_ACROSS_ROOTS
```

So the "repo-relative paths, root-independent" wording at entry:5 holds (`readout.py:47` hardcodes `path="corpus/fixtures/apk-r65/fixture.apk"`; it never prints `Path(__file__)`). The credit is not stretched: the recheck is **not** credited for the oracle comparison, for regeneration, or for any per-value clause. Q13's reject condition ("cites a verifier as guarding a value whose check survives deletion") is not met. §Q13 row (entry:152) uses the same "n/a by construction" convention as admitted `round-62-commonjs-require-name-evidence.md` and `round-63-zip-central-directory-evidence.md`.

## Findings by severity

### B1 — BLOCKING (off-criterion: Q11/Q02, not Q13) — entry:41 mis-transcribes its own readout output

Entry line 41 (committed blob, not a worktree artifact) prints:

```
{"cd_index": 2, ..., "payload_first16_hex": "4d616e696673742d56657273696f6e", ...}
```

Rerunning the exact command on the committed archive (`--fact 'member[META-INF/MANIFEST.MF]'`, readout sha256 `92e347c3...`, matching the entry's declared script digest at entry:162) prints `"payload_first16_hex": "4d616e69666573742d56657273696f6e"`. Field-level diff over the parsed JSON: exactly one differing field, `payload_first16_hex` (`4d616e696673742d...` = 15 bytes, "Manifst-Version"; actual 16 bytes). Independent byte check: payload at offset 668 begins `4d616e69666573742d56657273696f6e` = `b'Manifest-Version: 1.'`, sha256 `2e5da2495f3d231eb0e9107fafea4f7a0b8e0f6b4bc603d588c8acec403c0a49`, all consistent with the rest of the line.

Replaying **all 15** cited commands from the entry against the committed archive output: `checked_commands=15 mismatches=1` (this one). Consequence: entry:15's promise "The command is given with the output it printed" is false for line 41, and the entry's own stdout-hash credit cannot catch it (the hash covers the script's real output, not the entry's transcription). Recommendation: correct line 41 to `4d616e69666573742d56657273696f6e` and re-run Q11 on the entry; do not admit on this blob.

### M1 — minor (Q02/Q11 adjacencies) — dangling `### Code` pointer and absent "full 15-line stdout"

Entry:15 says "the script is the `### Code` block of that section ... and the same lines appear in the full 15-line stdout reproduced there", but the entry contains **0** `^###` headings and §Reproduce (entry:154-162) gives only the command, exit status, line count and hash — no code block and no 15-line listing. Admitted precedent has the block: `round-63-zip-central-directory-evidence.md:330` `### Code — readout.py (complete)`, and `round-62-commonjs-require-name-evidence.md:5` advertises "full code and exact stdout in §Reproduce". The pointer is non-resolving. It does not change the Q13 decision — the hash credit is true — but it is a template carry-over regression.

### M2 — minor (Q13-adjacent, literal over-claim in §Q13 row) — regeneration credited with no shown run

Entry:4 (`verified-at:`) and entry:121 (§Comparison) credit a `generator.py` run: "Regenerating the fixture from `generator.py` ... reproduced `fixture.apk` byte-for-byte and `truth.json` up to its embedded `python_version` field". No command and no output for that run appear in the entry; entry:152 nevertheless states "no ... comparison tool ... is credited". I reproduced the claim independently, and it is **true**:

```
$ cp <lane>/corpus/fixtures/apk-r65/generator.py /tmp/q13gen/ && cd /tmp/q13gen && python3 -B generator.py   # exit 0
$ sha256sum /tmp/q13gen/fixture.apk -> 05d2280f847497cf4dc9f5dbf9237721fedf1c928d8e7abe67cbe007afe7d03e  (947 bytes, identical)
$ sha256sum /tmp/q13gen/truth.json  -> 27303baeab02e771264421cfe4bbc2f0ef0aade3a8732de43b22c0e15b4f8173  (byte-identical)
```

So the credit is honest but unshown, and the §Q13 row's wording is literally inaccurate for that one sentence. Admitted precedent shows the run instead: `round-64-firmware-region-byte-evidence.md:58-59` (`$ cp ... generator.py /tmp/...`, `$ cd /tmp/... && python3 -B generator.py`) with its sha256 output. This is not a guard credit over any entry value, so Q13 stays pass; either show the two commands in §Reproduce or mark the sentence "not shown here".

## Residual risk and verification gaps

- No `lsp` device exists in this leaf's toolset (available: read, bash, edit, eval, glob, grep, task, wait, web_search, write, yield), so the credit scan is literal grep, not semantic reference resolution. Compensating check: I replayed every cited command and diffed output, which is the stronger instrument for this criterion. A cold/empty LSP absence is therefore not being recorded as evidence of absence by a semantic server; the negative is a literal substring/regex scan over the reviewed blob.
- Spoof surface of the scan: a verifier credit phrased without the `verify_` token would evade the grep. I also scanned for `recheck|self-test|self_test|probe|checker|automatic|comparison tool|guarded` — only the disclaimers above match.
- Off-criterion claims I spot-checked, none of which turned up a defect beyond B1: entry:121's oracle agreement is true for every group it names — `truth.json` `image.sha256/size` == readout `archive`, all three `members[]` shared fields (compressed_size, crc32, local_header_offset, sha256, uncompressed_size) diff-free, `axml_declared.strings` == `axml_string_pool.strings`, `axml_declared.resource_ids` == `axml_resource_map.ids`, and the three `axml_declared.attributes` rows agree with `axml_start_element` on `data_type`/`name_idx`/`ns_idx`/`raw_value_idx`. `truth.json` has no dex block and the entry claims none, so item 9's self-consistency result is correctly oracle-free.
- I did not run `reports/round-65/measure.py` and did not measure any counter: Q13 requires no counter movement, and measurement belongs to committed trees with the frozen probe (assigned to other seats).
- Read-only seat: no file other than this report was written; lane git/jj state untouched. `/tmp/q13a`, `/tmp/q13b`, `/tmp/q13gen` are outside the repo. No tools installed or upgraded, so no install record is due.
