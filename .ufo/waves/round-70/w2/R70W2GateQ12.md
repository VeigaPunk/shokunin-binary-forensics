PASS — Q12 is n/a for this entry: it writes no rejected-source row, every registry row it depends on is `mined` (none `rejected`), and the S048/S049 `teaches` cells open with the CORPUS.md rule-2 `supersedes S0NN —` wording.

Seat R70W2GateQ12 · 2026-10-25 · judged bytes: lane commit `17ee7f87ea8ee72a427af0fd8e7586d09bad99cd`, extracted via `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive 17ee7f87ea8ee72a427af0fd8e7586d09bad99cd | tar -x -C /tmp/revenger-r70-GateQ12` (all paths below are inside that extraction, i.e. the landed bytes). Criterion: `corpus/QUALITY.md:24` (Q12: a rejected source row states a reject reason grounded in a located quote, and its `flip` names a change to the source or a scope the reject reason does not exclude; reject when the flip asks for content the row already credits).

## Evidence

1. **The entry writes no rejected-source row.** `grep -n -i reject corpus/knowledge/round-70-apk-axml-byte-evidence.md` over the landed extraction returns exactly one hit: line 309, the entry's own §Q-map row `| Q12 | n/a | this entry writes no rejected-source row. |`. No `REJECTED:` text, no `flip:` text, no SOURCES-row proposal anywhere in the entry (`grep -n -i flip` same file → no hits). The `n/a` on line 309 is therefore itself correct; I did not take the entry's word for it — the byte-level grep above is the proof.

2. **Every source row the entry depends on is `mined`, none `rejected`.** `grep -o "S0[0-9][0-9]"` over the entry yields S032, S034, S038, S041, S043, S045, S046, S047, S048, S049; S043/S045/S046 appear only inside `supersedes` wording. `source:` header lines are entry lines 1-7 (S038, S049, S048, S032, S034, S047, S041). Registry status check (`awk -F'|'` field 9 of each matching `corpus/SOURCES.md` row): S032=mined, S034=mined, S038=mined, S041=mined, S043=queued, S045=mined, S046=mined, S047=mined, **S048=mined, S049=mined**. The registry's four `rejected` rows (S008 at SOURCES.md:22, S012 at :26, S024 at :38, S025 at :39) are cited nowhere by this entry.

3. **S048/S049 are `mined` with coherent used-by.** SOURCES.md:62 (S048) and :63 (S049) both carry `| mined | 2026-10-25 |` and `used-by` = `corpus/knowledge/round-70-apk-axml-byte-evidence.md`, matching the entry's `source:` lines 2-3 — satisfying CORPUS.md's `mined` definition ("cited by ≥1 path in `used-by`", fleet `CORPUS.md:107-108`).

4. **Supersession wording conforms to CORPUS.md rule 2** ("A correction is a new row whose `teaches` opens `supersedes S0NN —`", fleet `CORPUS.md:116-118`):
   - S048 teaches opens: `supersedes S045 — corrects its located-quote locator (S045 names "File layout" → \`header_item\` field table; the field table is under "Items and related structures" and ENDIAN_CONSTANT is under the constants heading); the four quoted phrases are unchanged`. Cross-checked against S045 (SOURCES.md:59): its anchor does quote from a `"File layout" → \`header_item\` field table` locator — the correction named is real and the wording is the required form.
   - S049 teaches opens: `supersedes S043 — adds the canonical URL (S043 names a repo path \`skills/...\` that returns HTTP 404 at the tag; the file lives under \`.agents/skills/\`); the located sentence is unchanged`. Cross-checked against S043 (SOURCES.md:57): it does name `skills/reverse-engineer-anything/references/android-applications.md` as a repo path — the correction named is real and the wording is the required form.

5. **The rows are honestly mined (snapshot pins re-derived).** `sha256sum corpus/snapshots/dex-format.html` → `c042861201d3530ff494d945cf4d6b42de14b7aaacd64496fa8cfed49691d9f4`, equal to the digest pinned in the S048 anchor cell; `sha256sum corpus/snapshots/rea-android-applications.md` → `412d9cb462d85b07f6fdbc2453dd741ca3da2c0dbba627867d5624df94afa74c`, equal to the digest pinned in the S049 anchor cell ("byte-identical to the committed snapshot"). Both commands run on the landed-commit extraction.

6. **Header status matches landing order step 1.** Entry line 11: `admission-status: candidate` — consistent with the frozen landing order (candidate + unflipped README until wave 2 decides); not part of my criterion, noted for coherence.

## Decision

Q12 = **n/a, confirmed** (the entry's §Q-map row at entry line 309 states n/a; my independent verification agrees via items 1-4). This is a PASS for the C1 kill-rule input: no located defect exists for this criterion on the landed bytes.

## Residual risk / notes (non-blocking, out of Q12 scope)

- The superseded rows S043 (`queued`), S045 (`mined`), S046 (`mined`) retain their pre-supersession statuses in the landed bytes, and no `corpus/lessons/round-70-*.md` exists at commit `17ee7f87` (`ls corpus/lessons | grep round-70` → empty), so no old→new status log exists yet. Per the frozen landing order step 4, the lesson and any status flips land only at admission; if the flip happens, rule 2 requires those old→new changes to be logged there. Registry housekeeping, not an entry defect.
- S048's anchor claims a live re-fetch (2026-10-25 21:28Z, 281161 bytes, sha256 `d72efc55…`) differing from the snapshot "only in the per-request CSP nonce and one devsite loader line". I did not re-fetch the live page (network content is not pinned and re-fetch can diverge); the committed-snapshot half of the claim is verified by item 5. A future recheck cycle (`180d`) covers the live half.
