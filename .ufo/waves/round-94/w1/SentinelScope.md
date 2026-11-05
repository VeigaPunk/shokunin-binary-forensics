# SentinelScope — round 94 w1 scope and host-safety findings (read-only)

Full evidence: `.ufo/waves/round-94/w1/SentinelScope/audit.md`.

## Result
Freeze intact. Host safety clean in the wave window: no sudo, pacman, sysctl, or ~/.local/bin activity. Scratch 129M, well under 500 MB. One minor bounds breach is attributable to no named seat: a gitignored bytecode file written into `corpus/` at 13:16:24. Two network items need receipts.

## Per-check
| Check | Verdict | Key evidence |
|---|---|---|
| Freeze bytes (reports/round-94 + round-72 entry) vs 060a8e8 | PASS | `git diff` empty; claims.md sha256 = freeze blob `c417e3d4…` |
| Lane tracked modifications | PASS | `git status`: only `?? .ufo/waves/round-94/` |
| Lane untracked writes outside wave dir | FAIL (minor) | F1: `corpus/__pycache__/audit_source_quotes.cpython-314.pyc` at 13:16:24, after spawn at 13:15:21; gitignored; writer unattributed |
| sudo in window | PASS | `journalctl _COMM=sudo --since 12:50` empty (pre-wave 09:02 entries are host disk-guard, not seats) |
| sysctl | PASS (file-level) | no changes in /etc/sysctl.d or /etc/sysctl.conf after Nov 5 00:00 |
| pacman | PASS | last pacman.log entry 2026-11-04 17:33 |
| service kills | UNVERIFIED | no kill trace; no failed units |
| ~/.local/bin, PATH dirs | PASS | nothing newer than 12:50 |
| Fleet-root strays | FLAG | F3–F6 below; no seat-attributable fleet-root write |
| Scratch size | PASS | 129M total; largest battery3 119M; nothing over 500 MB |
| Scratch naming | FLAG | F7: battery3/ and c1v3/ at scratch root (frozen-script hardcoded paths, pre-spawn) |
| Network: receipted fetches | PASS | S498 and S499 receipts: raw.githubusercontent.com/morluto/rea/main/{README.md,docs/installation.md} |
| Network: un-receipted fetches | FLAG | F8: `main-commit.json` from api.github.com/repos/morluto/rea (not a raw file); pinned-README/installation.md no receipt |
| Network: erratum URLs | PASS | no fetch evidence; appear only as text |
| Non-allowlisted URL strings | PASS | content of fetched rea docs and fixture copies, not fetches |
| /tmp hardcoding in committed freeze files | PASS | no hits |

## Flags and provenance (none is a proven seat bounds breach)
- **F1 (FAIL, minor):** `corpus/__pycache__/audit_source_quotes…pyc` written 13:16:24 in the lane's corpus. Candidates are ExecCensus, CriticR94, and ConnectorOverlap, all of which were active at 13:16. Remedy: delete the .pyc; require `-B` or `PYTHONDONTWRITEBYTECODE=1`.
- **F2 (pre-wave, orchestrator):** `reports/round-94/__pycache__/c1_k_admit_counter3…pyc` at 13:01:58, gitignored, inside the freeze dir. Tracked freeze bytes unchanged.
- **F3:** fleet-root `MANIFEST.json` rewritten 13:10:44, tracked commit `0ccd9d6` "rounds ledger: kaidoku r94 closure". Sibling-lane closure, not a revenger seat. Named only.
- **F4:** fleet `.scratch/run15-state.json` modified 13:12:14, uncommitted. Concurrent sibling closures. Named only.
- **F5:** other sibling-lane writes in window (kaidoku/kagi closure reports, prompts, dispatcher/disk-guard logs, kaidoku-shokunin lessons). Not this wave.
- **F6:** empty, untracked fleet-root dirs `counters/`, `exp-full/`, `history-recheck/`, `st2/`, `wt2/`, `tools/`, all pre-wave (05:20–11:12). Provenance unknown from metadata. Not deleted.
- **F7:** `battery3/` (119M) and `c1v3/` (8.5M) live at the scratch root. They are frozen-script output paths, created before spawn. Recommend L1 deletes them after landing.
- **F8:** three ScoutReopen fetches lack receipts. `main-commit.json` comes from api.github.com, which is outside the literal "raw files" allowlist. Remedy: record URL and time, or confirm the read was intended.
- **Self:** this seat's `git status` ran without `--no-optional-locks` and may have refreshed the lane `.git/index`. No tracked content changed.

## Recommended actions (orchestrator/L1; this seat changed nothing)
1. Delete the F1 .pyc. Enforce `-B` for seat Python.
2. Add receipts for the F8 fetches, or confirm them out of bounds.
3. After landing, delete scratch `battery3/` and `c1v3/`.

Freeze status for calibration: C1 and C2 freeze bytes are unchanged, so the frozen counters and claims are intact for the integrator.

Scratch `/fast/scratch/hyaku/revenger-r94/SentinelScope` removed on exit.
