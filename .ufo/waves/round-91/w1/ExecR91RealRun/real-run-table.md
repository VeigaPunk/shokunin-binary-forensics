# C2 real-run miss table — ExecR91RealRun (round 91)

Range: `7fab03f..refs/heads/main` in /home/vgpnk/Projects/shokunin/revenger-shokunin.
Instrument: `reports/round-91/message_tree_check.py` sha256 4e45c2898b15b0170613a4725a2f3dfb243536c6a670faf7edaff42dc7a018be (stable across the run).
Summary line: `MESSAGE_TREE commits=23 cited=25 misses=9` (json and text modes agree on these bytes).

| # | commit | cited path (as reported) | verdict | proving read-only command (and observed output) |
|---|---|---|---|---|
| 1 | d509e98 | `ufo-wave-policy.json` | **genuine mismatch** | `git cat-file -e d509e98:ufo-wave-policy.json` -> fatal (absent); `git ls-tree -r --name-only d509e98 | grep -c 'ufo-wave-policy'` -> 0; `git cat-file -e d509e98^:ufo-wave-policy.json` -> fatal (absent in parent b13aac7); `git log --all --oneline -- '*ufo-wave-policy.json'` -> empty (never tracked in lane history; the file exists only at fleet-root scripts/hyaku/ufo-wave-policy.json, outside this repo) |
| 2 | b13aac7 | `claims.md` | ambiguous bare name (not a mismatch) | `git ls-tree -r --name-only b13aac7 | grep -c '/claims.md$'` -> 30 suffix candidates, so the instrument's unique-suffix rule cannot resolve it; intended `git cat-file -e b13aac7:reports/round-91/claims.md` -> present; `git diff --name-only b13aac7^ b13aac7 | grep claims.md` -> reports/round-91/claims.md (added by this commit) |
| 3 | b280719 | `w1-results.json` | ambiguous bare name (not a mismatch) | `git ls-tree -r --name-only b280719 | grep -c '/w1-results.json$'` -> 4 candidates; intended `git cat-file -e b280719:.ufo/waves/round-90/w1-results.json` -> present; `git diff --name-only b280719^ b280719 | grep w1-results` -> .ufo/waves/round-90/w1-results.json (added by this commit) |
| 4 | e0fbf2e | `truth.json` | ambiguous bare name (not a mismatch) | `git ls-tree -r --name-only e0fbf2e | grep -c '/truth.json$'` -> 53 candidates; intended `git cat-file -e e0fbf2e:corpus/fixtures/apk-r65/truth.json` -> present |
| 5 | 6ce41aa | `inspection.json` | ambiguous bare name (not a mismatch) | `git ls-tree -r --name-only 6ce41aa | grep -c '/inspection.json$'` -> 31 candidates; intended `git cat-file -e 6ce41aa:corpus/live/runs/round-89/inspection.json` -> present |
| 6 | 6ce41aa | `receipt.json` | ambiguous bare name (not a mismatch) | `git ls-tree -r --name-only 6ce41aa | grep -c '/receipt.json$'` -> 21 candidates; intended `git cat-file -e 6ce41aa:corpus/live/runs/round-89/receipt.json` -> present |
| 7 | 6ce41aa | `LEDGER.md` | ambiguous bare name (not a mismatch) | `git ls-tree -r --name-only 6ce41aa | grep -c '/LEDGER.md$'` -> 72 candidates; intended `git cat-file -e 6ce41aa:corpus/live/runs/round-89/LEDGER.md` -> present |
| 8 | 45b2713 | `c1-only.log` | ambiguous bare name (not a mismatch) | `git ls-tree -r --name-only 45b2713 | grep -c '/c1-only.log$'` -> 11 candidates; intended `git cat-file -e 45b2713:reports/round-88/c1-only.log` -> present; `git diff --name-only 45b2713^ 45b2713 | grep round-88/c1-only` -> reports/round-88/c1-only.log |
| 9 | 45b2713 | `noharm-diff.txt` | ambiguous bare name (not a mismatch) | `git ls-tree -r --name-only 45b2713 | grep -c '/noharm-diff.txt$'` -> 13 candidates; intended `git cat-file -e 45b2713:reports/round-88/noharm-diff.txt` -> present |

Genuine mismatches: **1** (d509e98 ufo-wave-policy.json). Renames/exists-in-parent in this pinned run: **0** —
the only such case (`bd575ca` citing `corpus/live/runs/round-89`, which its parent 6ce41aa carries and which
that commit renames to `reports/round-89/rejected-android-record/`) is no longer extracted by the current
bytes: it is an extensionless directory token, and the pinned run reports `bd575ca cited=0`.
