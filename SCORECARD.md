# revenger scorecard — mint

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; a row count is a measurement, not a score or verdict.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | r3: `corpus/live/runs/20261012T164357Z/LEDGER.md` verifies three static relationships, command -> `True`; Evidence `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`; commit in r3 report | r3 static JS |
| coverage | unmeasured | r2: archive identity precision/recall 3/3; `corpus/live/runs/20261012T164246Z/LEDGER.md` independent Python comparison -> `True True`; r1 behavioral recall 0/6, precision N/A; `python3 -c "import json; d=json.load(open('.shokunin/revenger/corpus/live/runs/20261012T163909Z/artifact-inspection.json')); print(d['operation'],d['evidence_id'])"` -> `inspect_artifact ev_dd509246...`; native `provider_unavailable`; commit recorded in r1 report | r2 archive route |
| calibration | unmeasured | r8: `python3 .shokunin/revenger/corpus/verify_js_graph_delta.py --self-test` -> 1/1 saved-parent import delta + rejected mutation; non-author `corpus/live/runs/round-8/reviewer.md`; r7 comparison tool remains 0/1; r6: `corpus/live/runs/round-6/LEDGER.md` comparison -> five `True`, non-author `corpus/live/runs/round-6/reviewer.md` confirms 1/1 parent projection, IDs `ev_4a93276c...` → `ev_f315c466...`; r5: independent `corpus/live/runs/round-5-review.md` rebuilt ELF and ZIP byte-identically; `python3 .shokunin/revenger/corpus/verify_saved_evidence.py --self-test` -> 2 positives + 2 rejection controls; r4: `python3 .shokunin/revenger/corpus/verify_saved_evidence.py --self-test` -> 2 positive + 2 negative rejection, `corpus/live/runs/round-4-verification.md`; r1: independent `truth-score.md` defines six truth atoms; `python3 -c "from pathlib import Path; p=Path('.shokunin/revenger/corpus/live/runs/round-1/wave/truth-score.md'); print(sum(x.startswith('| T') for x in p.read_text().splitlines()))"` -> 6; artifact-only precision separated from behavioral precision N/A; commit recorded in r1 report | r8 parent graph delta |

planned: r8 saved-parent delta verified (`corpus/live/runs/round-8/reviewer.md`), distinct from r7 comparison-tool miss. Native session blocked until caller-supplied provider. Next claim must specify a distinct tool/result boundary and truth oracle.
retired: none.
