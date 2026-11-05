# ScribeLesson findings — round 98, wave w1, seat `ScribeLesson`

Seat: `ScribeLesson` (scribe). Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`.
Scratch: `/fast/scratch/hyaku/revenger-r98/ScribeLesson/` (deleted before yield).
**Tools installed or upgraded: none.** No `pacman`, no `uv tool`, no `npx`, no binary download, no
`pacman` transaction of any kind.

## Files written

- `.ufo/waves/round-98/w1/ScribeLesson/round-98.md` (new) — the draft lesson for the L1 to copy into
  `corpus/lessons/round-98.md`. Sections: `## Gate`, `## Mistakes` (M11–M15), `## Frontier`,
  `## considerthese`. **The L1 copies it; I did not write into `corpus/`.**
- `.ufo/waves/round-98/w1/ScribeLesson.md` (this file).

Nothing else was written. `corpus/`, `reports/round-9[0-7]/`, `reports/round-98/claims.md`,
`reports/round-98/controls/`, `reports/round-98/quote-receipts/`, `SCORECARD.md`, `LOG.md`, `SKILL.md`
and `PROVINCE.md` were read only. No git mutation of any kind (no commit, stage, stash, reset,
checkout); `git log/show/diff/status/rev-parse` only. No `rea setup`; the only REA calls were
read-only (`rea --llms`, `rea doctor` was not run by me). Nothing was written to
`/home/vgpnk/Projects/shokuknow`.

## What the draft records (and how each fact was obtained)

Every count in the draft carries the command that produced it. The load-bearing ones, re-run and
confirmed:

| fact | command | observed |
|---|---|---|
| vote-binding digest | `python3 -c "import re,hashlib;t=open('corpus/knowledge/round-98-rea-host-readiness.md',encoding='utf-8').read();n=re.sub(r'(?im)^\s*admission-status\s*:.*$','admission-status: candidate',t);print(hashlib.sha256(n.encode()).hexdigest())"` | `6d27c129e6ec3bbd3699c84c0a06301d7aea88140e54a1ff8d8b34d5c0c5330f` |
| all three votes bind that digest | `python3 -c "import json;print(json.load(open('reports/round-98/votes/<Seat>.json'))['candidate_sha256'])"` | all three = `6d27c129…5330f` |
| critic FAILs | `python3 -c "import json;d=json.load(open('reports/round-98/votes/CriticR98.json'));[print(k,v) for k,v in d['decisions'].items() if v!='PASS']"` | Q11=FAIL, Q16=FAIL (6 n/a, 9 PASS) |
| ReviewerGate PASS notes are empty | `python3 -c "import json;d=json.load(open('reports/round-98/votes/ReviewerGate.json'));print({k:len(str(v).split()) for k,v in d['notes'].items()})"` | Q01–Q05, Q09, Q10 → 0 tokens |
| `ghidra-version 12.1.4` is not in the transcript | `grep -c "12\.1\.4" corpus/live/runs/round-98/host-probes-r98.txt` | **0** (and **17** in `rea-doctor-r98.txt`) |
| three installation paths | `sed -n '316p' corpus/live/runs/round-98/rea-doctor-r98.txt` → one `paths[3]:` line with three comma-separated paths (`tr ',' '\n' \| grep -c "bin/rea"` → 3); the row's own command `grep -c '^    paths\[3\]: '` → **1** | the number three is in the record; the recorded command counts lines |
| v6 checked used-by only for S502–S504 | `sed -n '54p' reports/round-97/c1_k_admit_counter6.py` → `NEW_ROW_IDS = ("S502", "S503", "S504")`; the loop at `:405`; the exclusivity check at `:428`; `grep -c S505 reports/round-97/c1_k_admit_counter6.py` → **0** | confirmed |
| no closure concept in either counter | `grep -c -i closure` on v6 → 1 (a docstring), on v7 → **0** | confirmed |
| the pending-closure note is digest-neutral only on the admission-status line | same digest script over two edited texts | same-line note → digest **unchanged** (`6d27c129…5330f`); separate-line note → digest **changes** (`740d43e1…d7894`) |
| S505 ungrounded count | `reports/round-98/controls/s505-ungrounded-count.txt` | 471 mined-with-used-by, 470 grounded, **1 ungrounded (S505)**; my own registry sweep over the freeze tree reproduced the same 1 |
| the v7 leg can fail on the base registry | `reports/round-98/controls/v7-dev/usedby-base34.log` | `C1_USEDBY_GROUNDED=fail`, why `S505 -> corpus/knowledge/round-96-native-analysis-sessions.md:entry does not cite row id`, exit 1; `pass` after the correction |
| C1 controls | `reports/round-98/controls/c1-v7/{do-nothing,junk-row,diag-landing}.log` | do-nothing 13/15 `fail`; junk-row 14/15 `fail`; diag-landing 14/15 but `C1_VERDICT=fail` (rc 1) on `C1_VOTES` and `C1_VOTE_NOTES` |
| C2 frozen run | `reports/round-98/controls/c2-v7-frozen.log` | `C2_ACCEPTED=0/5`, `C2_POSITIVE=pass`, `C2_POSITIVE2=pass`, `C2_STUB_SELFTEST=ok`, `C2_ROWSET_FR06/FR07` both contain `C1_ROWSET`, `C2_VERDICT=met`, rc 0 |
| fresh holdout | `.ufo/waves/round-98/w1/L1-holdout-v7/holdout98-v{6,7}-c02-parity.log`, `holdout98-v7-c14.log`, `holdout98-v7-c02.log` | c02 5/6 for **both** v6 and v7; c14 4/6; the unpatched c02 run shows 0/6 but its honest control is **BROKEN** (`C1_OWNWORK_PATHS`), so that 0 is not discrimination |
| SKILL registry count vs its own prose | `grep -c '^| name |' SKILL.md` → **31**; `SKILL.md:37` says "registers 17"; the same count was 17 at `d3f4e6c`, 28 at `85a2c7e` | the prose number and its own counting command disagree |
| r91 successors unregistered | `grep -c "c1_counter2\|cap_probe2" SKILL.md` → **0**; `grep -c cap_probe2 corpus/lessons/round-91.md` → 2 (the lesson names them unclaimed) | confirmed |
| census before / after append | `reports/round-98/controls/census-{round-start,after-append}.log` | exit 0, 21 × W01, 13 × W04, 0 E, both |
| registry rows | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | 507 (505 at base) |

## Findings the L1 must act on

1. **C1 is NOT VERIFIED, and it is blocked by two independent things, not one.** The counter's own
   landing diagnostic fails `C1_VOTES` (critic Q11/Q16 FAIL) **and** `C1_VOTE_NOTES` (ReviewerGate's
   seven PASS notes are empty strings; ReviewerBlind's Q17 PASS note is n/a-style). Fixing the two
   critic FAILs alone would not turn `C1_VERDICT` to pass. The draft says so explicitly.
2. **The pending-closure note has a digest constraint.** If M12's fix is applied to the entry, the
   note must ride on the `admission-status:` line itself: on that line the digest is unchanged
   (`6d27c129…5330f`), on a separate line the digest changes (`740d43e1…d7894`) and every vote is
   invalidated again. Measured on the committed bytes; the L1 should write it on that line.
3. **The S505 correction form is fixed by Amendment A2** (`status mined→queued`, `used-by → —`).
   Measured side effect, for the L1's awareness: with S505 `queued`, the v6/v7 `C1_SOURCES`
   supersedes chain resolves S504 → S505 and fails with `S504:terminal-mined-expected:S505:queued`
   (my runs on scratch copies of the claims-freeze tree: v6 rc 1, v7 c02 rc 1). The v7 c14 profile
   is unaffected (`C1_SOURCES=pass` there), and the v7 leg the fix installs,
   `C1_USEDBY_GROUNDED`, passes on the corrected tree. The correction is therefore safe for the c14
   target it is made for, but the c02 profile sees the supersedes side effect. Flagged, not
   resolved — the claims are frozen and the L1 decides.
4. **`SKILL.md:37` says "registers 17 instrument blocks" but its own command prints 31.** The count
   was 17 at `d3f4e6c`, 28 at the r97 freeze `85a2c7e`, 31 now. This is the drift the
   `considerthese` proposal 5 names, and it is already visible in the lane's own bytes.
5. **The C2 positive-control wording in claims A1 is conditional.** A1 states the c02 landing run
   "cannot pass by construction" and is reported as a diagnostic under a no-harm rule. The draft
   follows A1 and reports the c02 result from the frozen harness run (`c2-v7-frozen.log`, which is
   the holdout fixture set, `C2_ACCEPTED=0/5`). The draft does **not** claim a c02 landing-tree
   verdict; the fresh-holdout c02 diagnostic is reported as its own line, including that the
   unpatched run's 0/6 is a broken control, not discrimination.

## Out of scope for this seat (not attempted)

- No landing tree was built or scored by me, and no counter was run on any tree with C14 held. The
  only counter runs I made were on **scratch copies of the claims-freeze archive** with C14 still
  `partial` (the base tree, the freeze tree and three one-cell S505 variants), i.e. the disclosed
  development set, plus `--self-test`. Receipts stayed in scratch and were deleted; the counts they
  produced are quoted above with their commands so the L1 can re-run them.
- I did not write the SCORECARD round-98 section, `corpus/lessons/round-98.md`, `LOG.md` or
  `corpus/SOURCES.md`; those are the L1's landing edits.

## Note on an out-of-lane incident (not this lane's)

`ConnectorScope-23` (kake r97) reported at ~18:14Z that it had run `rm -rf /fast/scratch/hyaku/kake-r97`,
deleting sibling seats' scratch trees in the **kake** round-97 lane. My seat's scratch
(`/fast/scratch/hyaku/revenger-r98/ScribeLesson`) is in a different root and was unaffected; I
re-created and re-verified it after the message and re-derived every transient artefact from the
frozen instruments and controls. Nothing in the revenger lane tree was touched by that incident.
