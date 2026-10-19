# Mutation probe — repaired PE ledger verifiers (2026-10-19)

The dispatched mutation-tester L2 (`W2RoundRevenger.RevMutation-2`) failed at
start: `resource_exhausted: Reached free model rate limit` (its transcript,
`history://W2RoundRevenger.RevMutation-2`). L1 ran the same specified probe
itself, so this is **author-side** evidence, not non-author review.

Method: copy the working-tree `corpus/` into `mktemp -d /var/tmp/rev-mut-XXXX`,
apply one mutant per fresh copy, run the verifier with `cwd=/`, record exit and
last line; temp tree removed. Lane files were never edited.

| mutant | file | exit | finding | result |
|---|---|---|---|---|
| a artifact check uses current path | verify_icon_languages.py | 1 | `AssertionError: r47: artifact` | killed |
| b receipt command clause deleted | verify_icon_languages.py | 0 | `PASS: 3/3 group-language states…` | survived |
| c HIST points at copy root | verify_icon_languages.py | 1 | `AssertionError: r47: artifact` | killed |
| d1 saved `artifact.path` → current path | verify_icon_languages.py | 1 | `AssertionError: r47: artifact` | killed |
| d2 receipt command forged | verify_icon_languages.py | 1 | `AssertionError: r47: receipt` | killed |
| d3 semantic field flipped (`resources[0]` id) | verify_icon_languages.py | 1 | `AssertionError: r47: resources` | killed |
| a artifact check uses current path | verify_multi_icon_states.py | 1 | `AssertionError: r42: artifact` | killed |
| b receipt command clause deleted | verify_multi_icon_states.py | 0 | `PASS: 4/4 two-image states…` | survived |
| c HIST points at copy root | verify_multi_icon_states.py | 1 | `AssertionError: r42: artifact` | killed |
| d1 saved `artifact.path` → current path | verify_multi_icon_states.py | 1 | `AssertionError: r42: artifact` | killed |
| d2 receipt command forged | verify_multi_icon_states.py | 1 | `AssertionError: r42: receipt` | killed |
| d3 semantic field flipped (`resources[0]` id) | verify_multi_icon_states.py | 1 | `AssertionError: r42: resources` | killed |

KILLED 10 / 12 — `grep -cE '^\| .*\| killed \|$' .ufo/waves/kaika-r1/mutation-post.md` → 10.

Every data forgery (d1–d3) is rejected, and every code mutant that reverts the
repair (a, c) is caught. The two survivors (b) are a **coverage gap, not a
regression**: the receipt-command clause is new this round and neither script
carries an in-script forged-receipt control, so deleting the clause is invisible
to the script's own run. The data probe d2 shows the clause works while present.
The named ledger has the equivalent control in its external battery
(`reports/round-1/replay_scenarios.py`, N2); these two do not. Next-round
candidate: add an in-memory forged-receipt-command rejection to both scripts.
