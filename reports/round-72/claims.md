# Round 72 claim freeze — revenger

Author: RevengerR72. Base revision: `0027e3f62b60373f4dbc3937321ce9624f3ebdb4` (lane `main`). No source registry or knowledge changes were present at freeze. This is one coverage claim, on the lane's lowest-scored active axis. The claim is falsifiable from committed bytes and does not assert any tool was installed or run.

## C1 — coverage: documented RE tool landscape, frontier → core

**Before → target:** C15 is absent, so `C15_HELD_BACKED=0/1` and `C15_TOOL_ROWS=0/18`; after, exactly one new C15 coverage row is `held`, backed by the new knowledge entry and all 18 named direct-project source rows (`C15_HELD_BACKED=1/1`, `C15_TOOL_ROWS=18/18`). The entry is limited to each repository's own public statement of its purpose and explicit limitations, not correctness, performance, host readiness, execution, or actual provider availability. Source discovery catalogs are retained as C-tier rejection records, not load-bearing evidence. C03 managed assemblies is among the newly covered surfaces, but the claim's count is the deliberately narrower C15 tooling surface.

The one counting predicate is `reports/round-72/measure.py TREE`: C15 is backed only when its committed README row is held and points to `corpus/knowledge/round-72-tool-landscape.md`, the entry cites every required S054–S070 and S073 row, and those rows are mined and name that entry in `used-by`. `C15_TOOL_ROWS` independently counts those exact 18 citations. A C15 row flip, registry-only append, or empty/uncited entry cannot reach the target. No-op base and a status-flip-only control are required before integrating the source records.
Counter SHA-256 at freeze: `9559b10d49690c4247a4100516bef94c8607fcd198dd77d274c770bdb6df48b3`. Base archive receipt: `reports/round-72/controls/base.log`; status-flip-only control: `reports/round-72/controls/status-flip-only.log`. Both miss the frozen target.

The expected end state is a new coverage-map row C15 marked held, one new knowledge entry, 18 newly opened primary project repositories (S054–S070 and S073), and two newly opened secondary catalogs retained as rejected C-tier leads (S071–S072). Each source must have a located quote ≤25 words in the lesson Gate. C1 is not achieved by a source-row count alone.

## Kill rule

C1 passes only if the frozen counter reports `C15_HELD_BACKED=1/1`, `C15_TOOL_ROWS=18/18`, and exits 0 on the final committed lane tree. Any missing/malformed source row, absent/uncited entry, failure to source the C15 claims, or final counter miss falsifies C1; do not narrow the target after data. The selected counter labels, predicate and target stay unchanged.

## Round shape

One v2 wave of 64 distinct seats, if validated, with build/recon and attack work together; at least 25% attack roles. L1 is the planner seat (validator rejects planner). Seats are read-only and have unique report paths. No residual or second wave is predeclared; seat failures remain dead. The single wave is intended to re-open and independently scope-check the 20 operator-named repositories, verify the frozen counter and candidate evidence, and attack the exact C1 predicate and no-op controls.
The operator's additional short-link study is supplemental SOURCES curation, outside C1's 18-row numerator and its fixed required IDs; it cannot replace or narrow any of the 20 named repository targets. Screen each resolved destination for province fit and safety before deciding to add a row or knowledge claim. Preserve inaccessible/failed destinations as unresolved evidence, not source claims.

## Do-nothing controls

Before integration, run the counter on a committed archive of base `0027e3f62b60373f4dbc3937321ce9624f3ebdb4` and a scratch tree that changes only a C15 README status cell. Both must report `C15_HELD_BACKED=0/1`; the scratch control must also report `C15_TOOL_ROWS=0/18`. Receipts land in `reports/round-72/controls/`. If either reaches the target, revise the counter before source data is integrated; otherwise freeze the counter's SHA-256 in the round evidence.

## Exclusions

No calibration or freshness axis claim; no producer/tool readiness, installation, host availability, or dynamic-target activity claim; no changes to the APK candidate, C05, any calibration gate, existing coverage rows, or the province's prohibited work. Tool installs/updates are not planned.