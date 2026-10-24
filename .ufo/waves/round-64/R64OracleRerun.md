# R64OracleRerun

- **Files changed:** `.ufo/waves/round-64/oracle-rerun.log` (captured oracle output, exit code, requested SHA-256 values, and frozen-base comparisons); this report.
- **Behavior/evidence:** `ORACLE OK`, exit code `0`. Region checks passed for padding at offsets 0, 591, and 1114, and zlib members at offsets 512 and 1024. Full captured output and hashes are retained in `oracle-rerun.log`.
- **Committed-byte confirmation:** `inspection.json`, `firmware-r63.bin`, `truth.json`, and `oracle_check.py` have the same SHA-256 in the working tree and frozen base commit `666ea84b6be2eec2b0359f556ba2429fc9044c36`. The saved record therefore still passes against those committed fixture bytes.
- **Risk/limitation:** This establishes correspondence with the authored fixture and saved record, not provenance or general firmware-format behavior.
- **Blockers/installations:** None; no tools installed.
