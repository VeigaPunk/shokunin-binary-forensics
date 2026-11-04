# ScoutR91Surfaces — surface map for the v3 + message-tree integration

**Verdict: MAP COMPLETE, no lane file edited.** 9 required edit sites across 4
files (+1 hazard site, 2 files that need no edit), each with `path:line` and a
per-class grep. Full map: `.ufo/waves/round-91/w1/ScoutR91Surfaces/surfaces.md`.
Read-only throughout; the only scratch tree lived under
`/fast/scratch/hyaku/revenger-r91/ScoutR91Surfaces` and was deleted.

## Edit-site count by file

| file | sites | what |
|---|---|---|
| `corpus/README.md` | 2 | index line for `self_assessment_check3.py` (line 30, **already landed by a sibling at recon close**); "Known gaps" sentence `:70-72` (open) |
| `SKILL.md` | 4 | v3 registry block; `message_tree_check` registry block (insert at `:325`); stale "registers exactly one committed gate" `:37-38`; placement before `## 7.` at `:470` |
| `SCORECARD.md` | 2 | capability row after `:169`; round-91 section after `:1670` |
| `LOG.md` | 1 | round entry after `:1289` (r90 bullet shape) |
| `SHONEN.md` | 0 | no `SM`/gate/registry token in 30 lines — and adding a digest/`[x]` would move SM3/SM4 |
| `corpus/QUALITY.md` | 0 | no criterion names the gate (Q17 names only `source_path_check`) |

## The two row formats (quoted verbatim in surfaces.md §2)

- Capabilities row — header `SCORECARD.md:165`: `| Capability | What it can now do | Evidence pointer | First-working round |`; rows `:167-169`; the admission rule `:171` ("Rows enter only through a round that demonstrates the capability running"). New row appends after `:169`.
- Gate-registry row — block form `| field | value |` / `|---|---|` + `name, kind, entry command, verdict map, self-test, [measured-against], what a green run does NOT establish, write scope, owner`, blank-line separated. `sed -n '/^## Gate registry/,/^## [^G]/p' SKILL.md | grep -cE '^\| name \|'` → **15** now, 17 after the two rows.

## What would break if v3 simply replaced v2

1. **README naming / SM2 — measured hard blocker (now closed).** v3 counts every top-level `corpus/*.py` (SM2, `self_assessment_check3.py:86`); with the README not naming it the full run read `SM2=1 SELF_MISMATCH=1 exit=1`, which fails C1's fourth leg (`c1_counter.py:111-115`). Scratch kill/restore control: line present → `SM2=0 SELF_MISMATCH=0 exit=0`; line removed → `SM2=1` again. At recon close a sibling had landed exactly that line and the live run reads `SELF_MISMATCH=0 exit=0`, `--self-test` exit 0.
2. **SCORECARD last-K-line rule.** SM6 v3 reads **cell index 2** of the *last* line containing `K_HELD_BACKED` (today `SCORECARD.md:693`, `8/15 → 8/15` → `SM6=0`). A new round-91 row that mentions the token outside cell 2, or states a wrong `N/D` there, flips `SM6=1` and kills the same leg. Safe: `K_HELD_BACKED 8/15 → 8/15` in cell 2, or omit the token (the `:1663` "held criteria (no claim)" pattern is invisible to SM6).
3. **C2 leg 4 is razor-thin.** In `7fab03f..refs/heads/main` (23 commits now, 21 at freeze) **no commit message contains a backtick**. Census: repo-relative path tokens 9 occurrences; `.log` filenames 8; extension-terminated filename tokens 23 occurrences / 21 distinct. `cap_probe.py:126` needs `cited=M ≥ 20`, so an instrument implementing only "backticked path + `.log`" reads M=8 and **fails**; it must also extract bare tokens (the claim's own "bare filenames resolve by suffix match" clause) to reach 21–23 — margin 1–3. Leg 4 ignores the instrument's exit code, so `misses=K>0` is tolerated by the counter but must be reported honestly.
4. **Flag spelling:** `cap_probe` calls `--selftest`, `c1_counter` calls `--self-test`.
5. **`sm6(root)` arity:** `c1_counter.py:70` calls `impl_mod.sm6(root)` with one positional arg; a `(root, lane)` signature dies before any case runs (v3 satisfies this: `:210`).
6. **v2 bytes are pinned** (`reports/round-90/instrument-pins.log:1`, sha `0e73a90b…0227`), and frozen historical counters `reports/round-70/measure.py`, `measure-a1.py`, `reports/round-71/measure.py` invoke `corpus/self_assessment_check.py` **by path** — never repoint them at v3.
7. **Registry-count drift:** `SKILL.md:37-38` already says "exactly one committed gate" (false at 15 rows); two new rows make it 17. Historical counts (`SCORECARD.md:871`, `LOG.md:1244`) are append-only.

## Tools

None installed or upgraded. Nothing written outside the two paths above.

Report: .ufo/waves/round-91/w1/ScoutR91Surfaces.md
