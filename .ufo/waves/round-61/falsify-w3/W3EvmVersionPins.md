GRADE: HOLDS — C09 header/Limitations version claims (rea-agents@6.4.0 per ledgers; evmole-interface evmole@0.9.3 in records; run 2026-10-12; host skill now 6.7.0 per S002)

Attacked landed ab580698212258a55e43e9bb9bf6ac78c91eae2a. Entry `corpus/knowledge/evm-saved-interface-candidates.md` sha256 `ab9c48da93cc83da340f715423f796a86c0dd23dcee333b5e9965c90a137387b` (live == extracted archive at /tmp/revenger-r61w3-W3EvmVersionPins).

## Every record's own provider/version fields (python json load; 7/7 identical shape)

```text
round evidence_id(19)         provider.id       provider.version environment analysis_profile
19    ev_0ad0097eb137ff91    evmole-interface  evmole@0.9.3     null        null
21    ev_4810eda7b540fbf2    evmole-interface  evmole@0.9.3     null        null
22    ev_24fe0001213ec58a    evmole-interface  evmole@0.9.3     null        null
23    ev_296e7ed723c7356b    evmole-interface  evmole@0.9.3     null        null
24    ev_50d5ffb1fdbd17c4    evmole-interface  evmole@0.9.3     null        null
25    ev_23a9464bf2d8c3de    evmole-interface  evmole@0.9.3     null        null
26    ev_482e41e68b6c5f35    evmole-interface  evmole@0.9.3     null        null
```
Records also carry `provider.name="REA EVM interface adapter"`, `operation="inspect_evm_interface"`, `authority="shipped-artifact"`. `grep -c rea-agents` = 0 in each of the seven `inspection.json`; `grep -o 'evmole@[0-9.]*'` = exactly one hit per file, seven total.

## Findings

1. HOLDS — "`rea-agents@6.4.0` per the round ledgers" (entry:8-9). All seven `corpus/live/runs/round-{19,21,22,23,24,25,26}/LEDGER.md:5` literally read `` `npx -y rea-agents@6.4.0 inspect-evm-interface …` ``; `git log -L 5,5:<ledger>` shows each line introduced by its original 2026-10-12 commit (ca7653e, 2c1e6fc, de8094f, b804f89, dd0d49f, 7f8748c, a3cc3f2) and never edited. No other rea-agents version occurs in those seven ledgers.
2. HOLDS — "provider `evmole-interface` `evmole@0.9.3` inside the records" (entry:9). Exact equality with `provider.id`/`provider.version` in 7/7 records (table above). entry:170-171 states the split precisely: "Provider string `evmole@0.9.3` is read from the r19 record; `rea-agents@6.4.0` is recorded in the round ledgers only." Both halves verified against the artifacts; no record contains the producer version, so the entry does not overstate it.
3. HOLDS — "run 2026-10-12" (entry:82). `LOG.md` result headings for rounds 19, 21-26 are dated 2026-10-12 (`LOG.md:233,255,266,277,288,299,310`); the seven record commits are `2026-10-12 16:18:39` to `16:40:37 -0300` (`git log -- corpus/live/runs/round-N/inspection.json`). Caveat: no record carries a timestamp (`environment: null` 7/7), so the date is lane-log/commit evidence, not record content; the entry does not claim otherwise.
4. HOLDS — "the host skill now names `rea-agents@6.7.0`, S002" (entry:12). Installed `~/.agents/skills/reverse-engineer-anything/SKILL.md` (sha256 `fbcd39d6abe803cf7aa49c1880815bc8e22ba2af87a23681944f687bb7629eb1`) has `npx -y rea-agents@6.7.0` at lines 37, 51, 56 (also 71, 79) and `metadata.version: "42"`, `tool_count: 207` at 5-6. `corpus/SOURCES.md:16` (S002, tier A, docs, opened 2026-10-19) anchors "setup commands naming `rea-agents@6.7.0` (lines 37-56)", which the file contains.

## Adjacent observations (non-blocking; none contradicts a version claim)

- `SOURCES.md:16` S002 `used-by` lists only `corpus/knowledge/seed.md`, yet the C09 entry cites S002 at entry:12 and `lessons/round-61.md` records "Row changes old→new on pre-existing rows: none". Contract v1 defines `used-by` as "repo-relative paths of the knowledge entries or lessons citing the row" — registry bookkeeping gap, not a false claim. No Q01 problem: the entry's Q01 basis (entry:177) is S016/S017/S018/S019/S026, all opened 2026-10-21; S002 supports only the boundary clause.
- entry:181 Q05 row says "no current capability claim" while entry:12 is present-tense about the installed skill; S002's probe (2026-10-19) predates SKILL.md mtime 2026-10-20 13:35. The statement is true at the current bytes, and Q05 governs readiness/capability, not a documentation pin — a wording tension at most.
- entry:84 "locator paths point into an older checkout": all seven `parameters.path`/`locations` point under `/home/vgpnk/Projects/prymeagnt/revenger/.shokunin/revenger/…`, a separate repo (HEAD `568a68de`, 2026-10-13) whose `.shokunin/revenger` is now a symlink to the current lane; r19's saved record is byte-identical there (`cmp` clean, sha256 `e892dd18…f15948`). Historically accurate for the 2026-10-12 run.

## Re-derived checks

- Entry `## Reproduce` block run on the extracted archive: exit 0; output byte-identical to the entry's `## Provenance` (7 fixture lines, saved IDs and file_sha256 prefixes all match).
- `git diff --stat cf02419 ab58069 -- corpus/live corpus/fixtures` prints nothing; `git diff --stat e0a4b0c ab58069 -- …` likewise. No saved record or fixture changed, so no harm voids admission on this item.
- Entry base `e0a4b0c…` exists and is an ancestor of `ab58069` (`git merge-base --is-ancestor`, exit 0).

VERDICT: all four version claims are exactly supported by the ledgers, the records' own `provider` fields, the lane log/commits and S002; nothing contradicts them and no Q criterion fails on a load-bearing claim — HOLDS.
Installs/upgrades: none.
