# ReviewerBlind — round 96 w1 report (blind derivation vote)

Verdict: **no value, scope, or boundary mismatch found** between the candidate entry
`corpus/knowledge/round-96-native-analysis-sessions.md` and independent derivations made
before reading it. Vote cast: `.ufo/waves/round-96/w1/ReviewerBlind/vote.json`
(11 PASS, 6 n/a with cross-referenced notes) binding the normalized candidate digest
`2f7d4c1b754d812102563869b511a746c7c49750d8cc42859b2a6466d776d923`; artifact
`.ufo/waves/round-96/w1/ReviewerBlind/blind-evidence.md`
(sha256 `020a2a7a805f850e98dd36a0974cd0df367ccfc4e4819973d378d8a1a9df20ca`).

## Preconditions verified

- Candidate digest re-derived from the working tree with the task's normalization
  one-liner (`python3 -B`): equals the frozen digest exactly.
- Working-tree entry bytes == freeze commit ff767436 bytes (both sha256
  `2f7d4c1b…d923`; the file's single `admission-status: candidate` line makes
  normalization a no-op on these bytes).
- Pinned receipt bodies: S502 38167 B `c818ee34…cc24`, S503 35095 B `b5f17fdf…6ccc` —
  equal to the frozen claim values; quote anchors ("Native targets", "DOS MZ with
  Ghidra", the file-offset CLI sentence, "analysis observations, not original source",
  S503 frontmatter "decompile code") all found verbatim.

## Blind derivations that matched the entry (all rows checked)

fixture sha256 `fe060de1…afd72`; entry bytes `B82A000000C3` = `mov eax, 0x2A; ret` per the
generator's own asserts (12 hex digits = 2 × 6, entry RVA 0x1000, base 0x140000000);
regen byte-identical (re-run, cmp clean, 1024 bytes); Evidence
`ev_cc0b9d88200afef1e7bf90e77f4d52faa20a049f85f1db1a7bf4a531282ffefe`; provider
ghidra/Ghidra/12.1.4; function_count=1; entry line `// ==== FUNC entry @ 140001000 ====`;
body `undefined8 entry(void){ return 0x2a; }`, `decompiled_ok=1 of 1`; 6 REPORT lines in
the headless log; all four record digests (`d717b491…`, `6ce217fa…`, `2fba7fbf…`,
`6a1d18c3…`); all eight ghidra* doctor scope checks healthy (platform linux, arch x64,
version 12.1.4, java 21.0.13); receipt line 1 literal `healthy: false`; Hopper and
ida-registration both `missing_analysis_engine`; REA CLI 6.7.0 derived from the doctor
receipt (`cli_package_version: 6.7.0`, L307) plus installed SKILL.md (S002, version "42",
`npx rea-agents@6.7.0`) vs pinned body `version: "49"` — the entry's era/byte-difference
disclosure is accurate.

## Findings (disclosed, non-blocking)

1. **Q16 dangling clause (cosmetic).** The entry's Q16 row cites "the doctor's
   healthy-line count" and its producing grep — no such derivation row exists in the
   entry (the only `grep -c` row is the headless receipt). Substance of Q16 held for every
   actually-present derivation row.
2. **Doctor causation not exhaustive (precision).** Item 3 attributes `healthy: false`
   to the absent Hopper engine alone; the receipt shows a second missing engine
   (`ida-registration`). The entry's Scope discloses both, so no internal contradiction.
3. **"No IDA is installed"** paraphrases the receipt's "IDA MCP registration is not
   configured" (classification `missing_analysis_engine` supports it).

## Verification gaps (consistent with the record, not byte-derivable from it)

- `rea decompile` exit 0, `analyzeHeadless` exit 0, `rea doctor` exit 1: none of the three
  saved receipts records its own process exit code; the claims are consistent with the
  receipts' content (complete Evidence, `Import succeeded`, `healthy: false`) but rest on
  run observation.
- The headless run executed a scratch copy of `rev75_dump.java`
  (`/fast/scratch/hyaku/revenger-r96/l1/rev75_dump.java` per the log); the committed
  original exists at `reports/round-75/rev75_dump.java`, but byte-identity of the run-time
  copy to the committed bytes is not evidenced inside the record.

## Bounds compliance

Writes: `.ufo/waves/round-96/w1/ReviewerBlind/blind-evidence.md`,
`.ufo/waves/round-96/w1/ReviewerBlind/vote.json`, this report. Scratch
`/fast/scratch/hyaku/revenger-r96/ReviewerBlind/` deleted before yield (fixture-regen
receipt quoted in the artifact). All Python invocations used `python3 -B`. No lane files,
no git writes (only read-only `git show`), no subagents, no network.
