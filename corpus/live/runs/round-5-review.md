# Round 5 independent fixture-replay review

Reviewer: independent LEAF non-author verifier. I read `/tmp/mission-revenger-standing.md`, the round-5 `REPLAY.md` and `replay_fixtures.py`, the r1 C source/README, the r2 truth manifest/ZIP, and `review-r1-r3.md`. All commands below ran from repository root; my new scratch directory was `.shokunin/revenger/corpus/live/runs/round-5-review-scratch/non-author-1488fd2e8b`. I did not execute either ELF, rerun REA, install an engine, commit, or spawn workers.

## Direct reproduction

- ZIP: `python3 .shokunin/revenger/corpus/fixtures/replay_fixtures.py .shokunin/revenger/corpus/live/runs/round-5-review-scratch/non-author-1488fd2e8b/fixture.zip` exited 0 and printed `sha256=857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e size=2964 expected_sha256=857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`. My independent read of the new file and committed `archive-r2/fixture.zip` found **exact byte equality**, SHA-256 `857989f5f2722fc00cd001387432b8bbcad55e3ed7d135fe1930df1e933be27e`, and size **2,964 bytes** for both, matching `archive-r2/truth.json`. The script consumes the committed r1 ELF and fixes README payload, member metadata/order, and compression; this validates deterministic replay from committed inputs, not independent generation of that source ELF.
- Native rebuild: `cc --version` reports `cc (GCC) 16.2.1 20260810`. `cc -std=c11 -O0 -g0 -fno-inline -o .shokunin/revenger/corpus/live/runs/round-5-review-scratch/non-author-1488fd2e8b/checksum .shokunin/revenger/corpus/fixtures/checksum-r1/checksum.c` exited 0. Source SHA-256 `aa75b4aca3ff535c8050c28db21433727f686102d62c526e294458537084b517` matches the r1 README; rebuilt output SHA-256 `f5ba069764ac66d5baa20224b0698a713823f45947a3364b67cfcb3f584897d0`, size **16,160 bytes**, exactly matches committed `checksum-r1/checksum` bytes and README digest/size. This is a rebuild with the stated toolchain on this host, not a portability guarantee. Neither executable was run.
- Saved-evidence test: `python3 .shokunin/revenger/corpus/verify_saved_evidence.py --self-test` exited 0 and printed:

```text
POSITIVE ev_cc681c2a03da4e9901275c1425fb1f726cca78bbdbec3defb13b6a0ac8ad156b ZIP root + 2 members: 3/3 identity units; formats, sizes, hashes, edges and fixture bytes match
POSITIVE ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e JS 2 imports + package main: 3/3 static inferred relationships match source/export and artifact digests
NEGATIVE ZIP REJECTED: ZIP: wrong root size/format
NEGATIVE JS REJECTED: JS: wrong package-main mapping
```

The positives compare the committed REA records to committed fixture bytes/source, with r2 ZIP root/two members and r3 three static inferred JS relationships; negative mutation tests reject changed in-memory ZIP root size and JS package-main mapping. These checks are stronger than the earlier ledger's limited `True` checks but do **not** authenticate REA's producer, independently rerun analysis, prove JS runtime behavior, or establish native session readiness.

## SHONEN reproducibility-box implication

The new recipe supports checking **instructions executable without oral context for fixture recreation and saved-evidence verification**, bounded to this repository, compiler/environment and committed inputs: an independent non-author followed the instructions and obtained byte-identical ZIP and ELF, plus passing saved-evidence self-tests. The r2 ZIP replay's ELF input is the committed binary, while the separate C build supplies independent source-to-ELF byte equality on this host. If the box instead requires an independent REA producer run, third-party artifact, portable builds, or native behavioral analysis, this review cannot satisfy it. Round-1 `provider_unavailable` remains unresolved; r2 inventory and r3 static relationships do not repair native coverage. Promotion authority, not this reviewer, decides or changes any SHONEN checkbox.
