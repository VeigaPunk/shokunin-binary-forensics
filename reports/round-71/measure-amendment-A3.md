# Round-71 counter amendment A3 — vote-tree file containment

Date: 2026-10-27, after W2 sentinel identified F2 and before the final counter/vote commit. This narrows malformed vote inputs; the C1 target, seat names, Q subsets and PASS/n/a rule do not change.

- Claims SHA remains `1febae1279fdeca323f5e8beffeb0a8ac2f26256158f7000bb0b2eff8321c3f5`.
- Counter SHA after A3: `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2` (`sha256sum reports/round-71/measure.py`).
- `q_votes(TREE)` now refuses a symlink or non-directory vote root, and refuses symlink/non-regular `*.json` members before reading. It also returns 0/16 for non-string seat names, duplicate JSON keys and non-object/malformed JSON. Exact per-seat stems/assigned Q sets, unique Q ownership and only `PASS`/`n/a` remain required.
- This addresses `R71W2Sentinel.md` F2 (a symlink vote member/root could point outside the measured archive) and F3 (unhashable seat could abort the counter). Probe receipt will show valid set=16; member symlink=0; root symlink=0; unhashable seat=0. No valid committed regular vote file's verdict changes.
- C1 remains not mechanically authenticated: structural vote files are evidence, not the judge. The frozen admission condition also requires the actual four fresh reviewer decisions/reports and independent closure; counter `HOLDS_C1_V6` alone never admits the candidate.
## A3 red-before receipt

`reports/round-71/measure-before.log` ran against the base archive with A3 counter SHA `82c817e1c2f7181cae759328fc884b8c38defbdba80dde4aad535d9c1f5f91b2`, exit 0. C1 remains 8/14 and 0/16 votes; C2 remains 0/1 on both base legs; `HOLDS_OK_V8=yes`; all ten HOLD rows are present. These labels match A2 because the base archive has no vote directory/symlink inputs.
