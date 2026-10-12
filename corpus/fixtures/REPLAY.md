# Fixture replay (round 5)

From the repository root:

1. Create a **new empty scratch directory** under `.shokunin/revenger/corpus/live/runs/` (for example, `round-5-your-name/`).
2. Run `python3 .shokunin/revenger/corpus/fixtures/replay_fixtures.py .shokunin/revenger/corpus/live/runs/round-5-your-name/fixture.zip`. It refuses an existing output. The output SHA-256 and size must equal `archive-r2/truth.json` and the committed ZIP. It uses the committed r1 ELF bytes; it does not execute that ELF. Literal README payload, ZIP timestamps, Unix file modes, compression and member order are fixed in the script to reconstruct the original byte stream.
3. For the native source build, use `cc -std=c11 -O0 -g0 -fno-inline -o <new-scratch-path>/checksum .shokunin/revenger/corpus/fixtures/checksum-r1/checksum.c`, then `sha256sum <new-scratch-path>/checksum`. Round 1 recorded compiler `cc (GCC) 16.2.1 20260810` and SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`. A compiler rebuild may differ in build ID or bytes due to toolchain/environment; compare and report actual digest rather than asserting reproducibility without a match. **Do not run the executable.**
4. To replay saved REA results without re-analysis, run `python3 .shokunin/revenger/corpus/verify_saved_evidence.py --self-test` from the repo root. It reads the committed REA JSON and fixtures and rejects in-memory modified proof copies. It does not authenticate REA as a producer and is not a native session.

These steps recreate the known fixtures and verify saved results; they do not connect MCP, install a native engine, execute the target, or solve the round-1 `provider_unavailable` gap.
