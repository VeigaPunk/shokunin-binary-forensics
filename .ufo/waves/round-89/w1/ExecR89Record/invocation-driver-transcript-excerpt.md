# Invocation-driver transcript excerpt — the two producer invocations (ExecR89Record)

Verbatim copy of the single bash tool call that performed both exit-0 producer
invocations, preserved from the ExecR89Record session transcript (also live at
`history://ExecR89Record`). One shell loop = two `rea` subprocess calls; stdout
and stderr captured to separate files per run. The driver's overall exit code
was 1 — that comes from `cmp` on the two differing stdout files, not from
either `rea` invocation. This evidence contains no PIDs and no UTC stamps
(only `date +%s.%N`-derived wall deltas); none were reconstructed.

## Driver command (verbatim)

```sh
cd /home/vgpnk/Projects/shokunin/revenger-shokunin && S=/fast/scratch/hyaku/revenger-r89/ExecR89Record && export TMPDIR=$S && echo "bash REA_JADX_MCP_JAR=[$REA_JADX_MCP_JAR]" && ls -l /home/vgpnk/.local/opt/jadx-headless-mcp/ && for n in 1 2; do t0=$(date +%s.%N); rea inspect-android-package corpus/fixtures/apk-r65/fixture.apk --format json > $S/run$n.json 2> $S/run$n.stderr; rc=$?; t1=$(date +%s.%N); awk -v a=$t0 -v b=$t1 -v n=$n -v r=$rc 'BEGIN{printf "run%s exit=%d wall=%.3fs\n", n, r, b-a}'; done; echo "--- sha256 stdout"; sha256sum $S/run1.json $S/run2.json; echo "--- stderr sizes"; wc -c $S/run1.stderr $S/run2.stderr; cat $S/run1.stderr $S/run2.stderr; echo "--- cmp"; cmp $S/run1.json $S/run2.json && echo CMP_IDENTICAL
```

## Captured output (verbatim)

```text
bash REA_JADX_MCP_JAR=[/home/vgpnk/.local/opt/jadx-headless-mcp/jadx-headless-mcp-0.7.1-all.jar]
total 41624
-rw-r--r-- 1 vgpnk vgpnk 42619858 Oct 13 13:54 jadx-headless-mcp-0.7.1-all.jar
run1 exit=0 wall=2.464s
run2 exit=0 wall=2.276s
--- sha256 stdout
01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76  /fast/scratch/hyaku/revenger-r89/ExecR89Record/run1.json
5bbdd189cd19dd1b181b4850b95fe07d077bc4031c70b25fec5006ca0d72ce00  /fast/scratch/hyaku/revenger-r89/ExecR89Record/run2.json
--- stderr sizes
0 /fast/scratch/hyaku/revenger-r89/ExecR89Record/run1.stderr
0 /fast/scratch/hyaku/revenger-r89/ExecR89Record/run2.stderr
0 total
--- cmp
/fast/scratch/hyaku/revenger-r89/ExecR89Record/run1.json /fast/scratch/hyaku/revenger-r89/ExecR89Record/run2.json differ: char 20, line 1
```

## Retained bytes cross-check

The preserved `run1.json`/`run2.json` in this directory hash to exactly the two
sha256 values printed by the driver above (re-verified after copy:
`01af3141d79027a3bae53b6482779d3e9c89446ab6ca09b408a6cb266f321c76` /
`5bbdd189cd19dd1b181b4850b95fe07d077bc4031c70b25fec5006ca0d72ce00`), and both
retained stderr files are 0 bytes, matching the driver's `wc -c`.

## Context: the earlier failed attempt pair (NOT the record runs)

Before the two exit-0 runs, an attempt pair in a non-interactive exec
environment with `REA_JADX_MCP_JAR` unset produced the producer's
`capability_unavailable` payload (exit 1, 686 bytes, sha256
`4d0e6ea59823c97242bfa75b009952dfe8c1e9c63bc1793c09308d6482167330`, both
attempts identical). Those bytes are not retained and are not part of the
record; the full story is in `corpus/live/runs/round-89/LEDGER.md`.
