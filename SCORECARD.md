# revenger scorecard — mint

Owned axes: depth, coverage, calibration. Scores remain unassigned without a
quality rubric; a row count is a measurement, not a score or verdict.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| depth | unmeasured | r3: `corpus/live/runs/20261012T164357Z/LEDGER.md` verifies three static relationships, command -> `True`; Evidence `ev_4a93276c886da96f0b37c490e395dc0761ac32225dd7297c600a51ce100c1c7e`; commit in r3 report | r3 static JS |
| coverage | unmeasured | r2: archive identity precision/recall 3/3; `corpus/live/runs/20261012T164246Z/LEDGER.md` independent Python comparison -> `True True`; r1 behavioral recall 0/6, precision N/A; `python3 -c "import json; d=json.load(open('.shokunin/revenger/corpus/live/runs/20261012T163909Z/artifact-inspection.json')); print(d['operation'],d['evidence_id'])"` -> `inspect_artifact ev_dd509246...`; native `provider_unavailable`; commit recorded in r1 report | r2 archive route |
| calibration | unmeasured | r4: `python3 .shokunin/revenger/corpus/verify_saved_evidence.py --self-test` -> 2 positive + 2 negative rejection, `corpus/live/runs/round-4-verification.md`; r1: independent `truth-score.md` defines six truth atoms; `python3 -c "from pathlib import Path; p=Path('.shokunin/revenger/corpus/live/runs/round-1/wave/truth-score.md'); print(sum(x.startswith('| T') for x in p.read_text().splitlines()))"` -> 6; artifact-only precision separated from behavioral precision N/A; commit recorded in r1 report | r4 full-unit proof |

planned: r4 full-unit saved-evidence verification landed (`corpus/live/runs/round-4-verification.md`); native session remains blocked until caller-supplied provider configured. Next claim must state a distinct question and ground-truth oracle.
retired: none.
