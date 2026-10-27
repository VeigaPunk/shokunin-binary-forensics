# R71W2Census — final registry census, round 71 wave 2

**VERDICT: CENSUS PASS (registry evidence only).** At the committed candidate `4c1eeae88fd07e442f1bd546faf77be3957d390` (wave-frozen HEAD `c6e284c`), `corpus/SOURCES.md` is clean under the frozen contract: `sources-census.sh validate` exits 0 with 6 W04 + 1 W01 warnings and zero E-codes; all seven frozen manual census commands exit 0; 53 rows, append-only +2 (S052/S053), no duplicate ID, enum/tier-inflation finding, or missing `used-by` path. This receipt decides no Q01–Q16 vote and no C1/C2 predicate.

- seat `R71W2Census` · date 2026-10-27 · measurements 16:04–16:07Z (13:04–13:07 local, UTC-3) · lane `/home/vgpnk/Projects/shokunin/revenger-shokunin`
- write scope: this report only. No source, config, route or git mutation by this seat.

## 1. Target and byte identity

| item | value |
|---|---|
| lane HEAD | `c6e284c6583fa3502754361f411b66646880ba02`, tree `cfae4cfc2cc8348f86df9de2662e27afeca8f055` |
| candidate/build commit | `4c1eeaee88fd07e442f1bd546faf77be3957d390` (HEAD adds only `.ufo/waves/round-71/w2-*`) |
| base commit | `b7abcd875c84f4e1d6c8df966b6bd20f4154c53f` |
| `corpus/SOURCES.md` blob | `79b4fb817f87278a062977d6b657424b0cc785d8` at HEAD **and** candidate — SAME |
| `corpus/SOURCES.md` sha256 | candidate/HEAD `a426f9d6c193399ebb19ab97ce8f992865db032dfc7cd8fbf7d4209caea9bdb0`; base `96df26f1aba6282874cf424756e96a3f772d91fb1436cf2036671eee6c266f1a` |
| v6 entry blob | `corpus/knowledge/round-71-apk-axml-byte-evidence.md` `036f8742b2c50b9df16fb5acfd90c7e1ab437c6a` at HEAD and candidate — SAME (39985 bytes) |
| lesson blob | `corpus/lessons/round-71.md` `705b50bb15492f2080b4bd03807fb27b2080d720` at HEAD and candidate — SAME |
| counter (context, not measured) | `reports/round-71/measure.py` sha256 `718daa96f34fa5c3435acdf031e2fe5099238e9092c36b845cb9258990fcca61` = A2 |
| census tool | `scripts/sources-census.sh` sha256 `3fb7261569f46423dd80ecc23e0a23789a7926f667c7a3fc559d2439d4a64e30` |

Row lines in the committed candidate: `corpus/SOURCES.md:66` (S052, `mined`/`90d`/used-by `corpus/knowledge/round-71-apk-axml-byte-evidence.md`) and `:67` (S053, `rejected`/`on-release`/used-by `—`).

## 2. Commands and exit codes

All commands run with absolute paths; lane reads only (`--out` never used).

```sh
# live lane (from fleet root)
bash /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger
# EXIT=0
revenger	W04	S024 duplicate url www.rfc-editor.org/rfc/rfc3227.txt across scopes
revenger	W04	S028 duplicate url github.com/ethereum/execution-specs/tree/v2.20.0/src/ethereum/forks/osaka/vm across scopes
revenger	W04	S029 duplicate url tc39.es/ecma262 across scopes
revenger	W04	S034 duplicate url pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT across scopes
revenger	W04	S048 duplicate url source.android.com/docs/core/runtime/dex-format across scopes
revenger	W01	S051 tierC mined used-by=corpus/training/bounty-triage/MODULE.md
revenger	W04	S053 duplicate url docs.python.org/3/library/zipfile.html across scopes
revenger	ok	/home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md
# stderr: empty · 7 warning lines · 0 E-lines
```

Re-derivation from `git archive` trees (independent of the dirty worktree):

```sh
git -C … archive 4c1eeae | tar -x -C candidate-tree
git -C … archive b7abcd8 | tar -x -C base-tree
bash scripts/sources-census.sh validate --file /fast/scratch/hyaku/revenger-r71/R71W2Census/candidate-tree/corpus/SOURCES.md
# EXIT=0 — the same 7 lines above, prefix `file`, terminal `file ok <path>`
bash scripts/sources-census.sh validate --file /fast/scratch/hyaku/revenger-r71/R71W2Census/base-tree/corpus/SOURCES.md
# EXIT=0 — 6 warning lines: the same set minus `W04 S053`
bash scripts/sources-census.sh census --file …/candidate-tree/corpus/SOURCES.md
# EXIT=0 — file rows 53; tier.A 50; tier.C 3; status.mined 44; status.queued 4; status.rejected 5;
#          FLEET rows 53, tier.invalid 0, status.invalid 0, missing 0
TMPDIR=<scratch> bash scripts/sources-census.sh selftest
# EXIT=0 — 96 `killed` mutant lines, terminal `selftest ok`
```

Seven frozen manual commands, verbatim from `CORPUS.md:132-148`, run from lane root and again from each extracted tree (`LANE` = lane root / `candidate-tree` / `base-tree`):

```sh
grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; …}' corpus/SOURCES.md          # enum + tier-inflation
awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {s=$9; … print p}}' corpus/SOURCES.md | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done
```

| # | metric | lane root rc / out | candidate tree rc / out | base tree rc / out |
|---|---|---|---|---|
| 1 | rows | 0 / `53` | 0 / `53` | 0 / `51` |
| 2 | malformed NF!=13 | 0 / `0` | 0 / `0` | 0 / `0` |
| 3 | tier histogram | 0 / `A=50 C=3 ` | 0 / `A=50 C=3 ` | 0 / `A=48 C=3 ` |
| 4 | status histogram | 0 / `mined=44 queued=4 rejected=5 ` | 0 / `mined=44 queued=4 rejected=5 ` | 0 / `mined=43 queued=4 rejected=4 ` |
| 5 | duplicate ids | 0 / (empty) | 0 / (empty) | 0 / (empty) |
| 6 | enum / tier-inflation | 0 / (empty) | 0 / (empty) | 0 / (empty) |
| 7 | mined used-by missing | 0 / (empty) | 0 / (empty) | 0 / (empty) |

## 3. Before → after, and agreement with the frozen receipts

| label | `census-before.txt` | base re-derived here | `census-after.txt` | candidate re-derived here |
|---|---|---|---|---|
| rows | 51 (`git show b7abcd8:…` → 51, rc 0) | 51 | 53 | 53 |
| tier | A=48 C=3 | A=48 C=3 | A=50 C=3 | A=50 C=3 |
| status | mined=43 queued=4 rejected=4 | mined=43 queued=4 rejected=4 | mined=44 queued=4 rejected=5 | mined=44 queued=4 rejected=5 |
| validate | exit 0, 6 W (5 W04 + 1 W01) | exit 0, 6 W | exit 0, 7 W (6 W04 + 1 W01) | exit 0, 7 W |
| E-codes | 0 | 0 | 0 | 0 |
| duplicate ids / enums / missing | empty | empty | empty | empty |

`census-after.txt` (`sha256 ba050938…`, identical to its committed blob) is reproduced cell-for-cell; `census-before.txt`'s base row count is reproduced by its own recorded command. The whole registry delta is four added lines, zero removed (`git diff --numstat b7abcd8..HEAD -- corpus/SOURCES.md` = `4 0`; `grep -c '^-[^-]'` = 0): S052, S053, one `## Paths` chain line (`corpus/SOURCES.md:80`), one search-log line (`:103`).

## 4. Duplicates, enums, missing paths (independent checks)

- **Duplicate URLs.** Independent regex enumeration (lowercased host, scheme stripped, trailing punctuation trimmed) finds exactly six same-URL groups: `zipfile` S040/S044/S053; execution-specs S016/S028; APPNOTE S032/S034; dex-format S045/S048; tc39 S022/S029; rfc3227 S008/S024. The tool reports exactly the expected newer row of each — W04 on S024, S028, S029, S034, S048, S053. For the zipfile trio, S040 and S044 carry byte-identical scope text (E04 exempt: S044's `teaches` opens `supersedes S040`), while S053's scope text differs → W04 only. Per `CORPUS.md:33`, W-codes never change lane status; exit stays 0.
- **IDs.** `S001`…`S053`, 53 rows, contiguous with no gap and no duplicate (`awk` sequence check plus `uniq -d` empty).
- **Enums.** Tiers observed `A=50`, `C=3` (no B, no invalid); statuses `mined|queued|rejected` only; kinds inside the nine-value enum; no `community` at tier A.
- **`used-by`.** All values repo-relative; no absolute or `../` path; every path resolves from the tree root, so command 7 prints nothing. In the committed candidate the single mined round-71 row S052 resolves to the existing v6 entry (`corpus/knowledge/round-71-apk-axml-byte-evidence.md`, blob `036f874…`); S053 is rejected with `—`.
- **Parser agreement.** No row is indented 4+ spaces, so the frozen column-zero commands and the maintained 0–3-space parser agree: 53 rows by both patterns. Tool selftest exits 0 with 96 mutants killed, including `W04-scope-sensitive-mutant`, `W04-does-not-fail-validation`, `E04-rejected-pair-exemption-mutant`, `E11-dangling-usedby`, `E12-row-outside-registry-exit-1`.

## 5. Located risk — post-freeze worktree drift (NOT the candidate)

Observed mid-wave, after the frozen candidate and after my first live run: `corpus/SOURCES.md` mtime `2026-10-27 13:05:39 -0300`, `corpus/lessons/round-71.md` mtime `13:06`. `git status` now shows `M corpus/SOURCES.md`, `M corpus/lessons/round-71.md` (plus untracked `.ufo/waves/round-71/w2.ready*`, `w2/R71W2SpotcheckDraft.md`, `__pycache__/`). Worktree `corpus/SOURCES.md` sha256 is now `dc2e5b22d648587b3dbaf797aaabcec65792ac0655736b196e28726dc0a5ed99` vs committed `a426f9d6…`.

Drift content (2 changed lines, both round-71 rows — no pre-existing row touched):
- `S052` `used-by`: `corpus/knowledge/round-71-apk-axml-byte-evidence.md` → `corpus/knowledge/round-71-apk-axml-byte-evidence.md, corpus/lessons/round-71.md`
- `S053` `teaches`: `format-layout claims` → `format/layout claims`; `used-by`: `—` → `corpus/lessons/round-71.md`

Measured effect: **none on this census.** The drifted worktree re-validates at EXIT=0 with the same 7 warning lines, and the seven manual outputs are byte-identical to the lane-root and candidate-tree runs (receipt hashes equal). `corpus/lessons/round-71.md` exists (11233 bytes), so `used-by` still resolves and E11 does not fire.

One internal inconsistency in the uncommitted worktree, surfaced for L1 (not a census failure, not in the committed candidate): `corpus/lessons/round-71.md:9` still describes S052's `used-by` as only `corpus/knowledge/round-71-apk-axml-byte-evidence.md`, while `:19` and `corpus/SOURCES.md:66` now list two paths. If the drift is committed, align line 9 and re-run this receipt (counts will not move). Adjudication must bind the committed candidate `4c1eeae`; this seat did not create, revert or repair the drift.

## 6. Limits of this receipt

- Registry-only evidence: it does not vote Q01–Q16, does not evaluate C1 gate/lint/vote-file conjuncts, and says nothing about the C2 exit-2 legs. No L0 question is answered here.
- No write outside this report; no pacman/tool install; no `agent://all` message; lane HEAD left at `c6e284c`.

## 7. Scratch receipts (deleted after this report was written)

`/fast/scratch/hyaku/revenger-r71/R71W2Census/` — `validate-live.out` and `validate-live-drift.out` (identical, `a0359715…`), `validate-candidate-tree.out` (`8b19a5d0…`), `validate-base-tree.out` (`1c47293c…`), `seven-live.out`/`seven-live-drift.out`/`seven-candidate.out` (identical, `8367609021…`), `seven-base.out` (`e8bc49df…`), `selftest.out` (`6f61744e…`), `sources-diff.txt` (`ceacc5d3…`), `ids.txt`, `rows-base-tree.tsv`/`rows-candidate-tree.tsv`, `changed-pre-existing.txt` (empty → `e3b0c442…`), `head.txt`, `seven.sh`. All outputs are inlined above; the directory is removed before returning.
