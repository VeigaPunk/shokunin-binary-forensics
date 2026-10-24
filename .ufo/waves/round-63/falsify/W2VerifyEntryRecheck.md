# W2VerifyEntryRecheck

**Verdict: pass; no mismatch found.**

Target: `corpus/knowledge/round-63-zip-central-directory-evidence.md` at the lane tip.

## Recheck evidence

- Extracted the `### Code — readout.py (complete)` block from the entry verbatim into temporary `/tmp` scratch; its SHA-256 is `94f502cde75eb47ffd3d7d8a73de45ad8889337a5269b669d998126a063a4bac`, matching the entry's recorded script digest (§Reproduce, lines 266–273).
- Ran that code with Python 3 `-B`, the lane root as its repository-root argument, and the lane root as cwd. **Exit 0**, **17 stdout lines**, empty stderr. Stdout SHA-256: `02b0f495c1db8c50e22db835cd57e7a221dd0a9c82f09d442feea461de722ed4`, matching the entry header and §Reproduce (lines 4, 235–255). The actual stdout was byte-identical to the entry's reproduced 17-line stdout block.
- Re-ran each of the 17 `--fact` invocations from the Observation section. Every invocation exited 0 and its one-line stdout byte-matched the JSON line printed immediately after that command in the entry. No stderr, no value or byte mismatch.

Fact IDs checked: `archive`, `eocd`, `central_directory`, `spec_derived_field_offsets`, `member_cd[bin/checksum]`, `member_cd[README.txt]`, `member_local[bin/checksum]`, `member_local[README.txt]`, `truth_archive_level`, `truth_member[bin/checksum]`, `truth_member[README.txt]`, `truth_member_set_delta`, `truth_build_field`, `saved_record`, `saved_occurrence[bin/checksum]`, `saved_occurrence[README.txt]`, `saved_occurrence_set_delta`.

## Provenance result

All 17 printed fact-value records in the entry byte-match their individual recheck outputs; the reproduced aggregate stdout also matches byte-for-byte. **Mismatch located: none.** Evidence in the entry: individual command/output pairs at lines 21–183; aggregate stdout at lines 235–255; fact-command index at lines 661–681.

No tools installed. The extracted script was temporary `/tmp` scratch; no other repository files were changed.