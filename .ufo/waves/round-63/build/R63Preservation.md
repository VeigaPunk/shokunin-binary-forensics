# Round 63 preservation baseline

## Capture evidence

- Requested baseline: commit `55bcb6e` (`55bcb6e1aeb4d42923a4e98db6580f67142b41ac`). The lane checkout HEAD read after the capture was `54ab973c021cc62ca65dcbe2cbfabe3235d5ee38`.
- First ran `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin status --porcelain corpus/live corpus/fixtures`; it returned no output. No pre-existing modified or untracked files were found in either tree.
- Capture command: `find corpus/live corpus/fixtures -type f | sort | xargs -d '\n' sha256sum`.
- Counts at capture: `corpus/live` 345 files; `corpus/fixtures` 98 files; combined 443. The target commit's tracked tree count is also 443.
- Added 12 supplemental digest records: all 10 `corpus/verify_*.py` files plus `corpus/README.md` and `corpus/SOURCES.md`. The manifest therefore contains 455 SHA-256 records total; the first 443 are the sorted live/fixtures capture.
- Baseline manifest: `.ufo/waves/round-63/build/preservation-base.sha256`.

## Base-state reconciliation and guard scope

The tracked-path comparison against `55bcb6e` reported no changed `corpus/live` or `corpus/fixtures` paths. By the time of that comparison, `corpus/verify_icon_states.py` and `corpus/verify_named_multi_icon_states.py` were modified in the working tree. Their supplemental rows are anchored to the requested base: the `verify_icon_states.py` capture digest matched `git show 55bcb6e:corpus/verify_icon_states.py | sha256sum`; the `verify_named_multi_icon_states.py` row was corrected to the exact `git show 55bcb6e:corpus/verify_named_multi_icon_states.py | sha256sum` digest (`b62441d5e1fa9ce15be61686f6b0e0fe7b879d3aca3cb898edcd0c29894093a3`). No verifier source was changed by this seat.

For the final harms check, preserve every one of the 443 baseline live/fixtures paths byte-for-byte. New round-63 fixture and run files are permitted only in `corpus/fixtures/firmware-r63/` and `corpus/live/runs/round-63/`; all other additions or any changed, removed, or renamed baseline path are outside the allowance. The 10 verifier and README/SOURCES hashes are supplemental comparison references, not unconditional holds: C3 verifier edits and the authorized C06 README flip / SOURCES addition may change those files.

## Tooling and blockers

No tools were installed. No build, lint, test, or formatter was run. No blocker found. The only scoped outputs from this seat are this report and the baseline manifest.
