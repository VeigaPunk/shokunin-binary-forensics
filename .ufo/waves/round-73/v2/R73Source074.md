# R73Source074 — round-72 source audit, registry row S074 (Claude-Red root README)

Seat: R73Source074 (round-73 v2 wave, leaf reviewer; no subagent dispatch).
Claim context: frozen C10 coverage admission (target C10_HELD_BACKED=1/1). This seat is one of the 42 distinct round-72 source audits; it reports on assigned row S074 only and admits no new source.
Lane root: /home/vgpnk/Projects/shokunin/revenger-shokunin. Read-only besides this report; no corpus/shared/sibling/fleet writes.

## Disposition

**AGREE with the S074 source disposition (REJECTED, tier C, community).** The located quote is verbatim at the cited pin, the scope/tier/rejection wording matches the pinned bytes, the rejection ground holds at the pin, and the flip condition is explicit and unchanged. **No superseding row is proposed for S074** (none is needed: no quote defect, no scope drift). Old rows are never edited; had a defect existed, only a new superseding row would have been proposed here.

## Located quote (verbatim, ≤25 words), URL, access date

- Quote (17 words, em-dash U+2014, backticks as in source): "Offensive security skills for Claude — drop-in `SKILL.md` files that turn Claude into a context-aware red team operator."
- Exact locator: `README.md` line 7 at commit `a8de813edc9f66f60d44cfe42d47750e89d9930b` (inside the `<div align="center">` block directly under the `# claude-red` H1 at line 5).
- URL re-opened: `https://raw.githubusercontent.com/SnailSploit/Claude-Red/a8de813edc9f66f60d44cfe42d47750e89d9930b/README.md`
- This seat's re-access date: **2026-10-30** (row's recorded access date: 2026-10-27; both recorded, no conflict — row was opened 2026-10-27, this is a re-verification).

## Comparison against the registry row (corpus/SOURCES.md line 88, 11 cells)

| Check | Row content | Re-opened evidence | Result |
|---|---|---|---|
| Quote verbatim | cell 5: README.md introduction, commit a8de813…, accessed 2026-10-27; quote as above | Pinned README line 7 raw: `**Offensive security skills for Claude — drop-in \`SKILL.md\` files that turn Claude into a context-aware red team operator.**` — byte-identical after normalizing only the `**` bold markup | PASS (verbatim) |
| Quote length | ≤25 words | 17 whitespace-delimited words (em-dash not a word) | PASS |
| Pin validity | commit a8de813edc9f66f60d44cfe42d47750e89d9930b | GitHub API commit object exists: author "SnailSploit \| Kai Aizen", dated 2026-10-12T15:02:40Z, message "Update README.md", tree 527e68313597971d15d243514d884b19b49d9071, signature `verified: true`; raw fetch at pin HTTP 200, 20968 bytes, sha256 `82bb9daa054e003caa6a4c33a2f19209cb5c711bcc65e34707b54828ef3698c3` | PASS (pin resolves) |
| Scope | "The repository README's declared offensive-security skill collection only; not a source for reverse engineering or authorized bounty-triage procedure" | Pinned README: "claude-red is a curated library of offensive security skills… from SQL injection to shellcode, EDR evasion to ADCS abuse"; use cases "authorized red team engagements, bug bounty triage, security research, CTF preparation, operator training, and methodical attack surface exploration" | PASS (scope matches the README's own declaration) |
| Tier | community / C | Same repo class as S051 (community, tier C corroboration lead); the root page is a broad skill library, not a primary artifact source | PASS (consistent) |
| Rejection + flip | "REJECTED: broad offensive skill content exceeds this province's static artifact-first boundary; the already-curated S050/S051 support only policy/reporting scopes; flip: a narrowly scoped artifact-only source is separately identified, opened and passes PROVINCE/QUALITY" | Rejection ground holds at the pinned bytes (broad offensive procedure library). S050 (tier A, SECURITY.md intended-use/disclosure policy) and S051 (tier C, offensive-reporting SKILL.md, "never sole support for a load-bearing claim") exist and carry only policy/reporting scopes. Lesson Gate row (corpus/lessons/round-72.md line 33) flip: "flip if a separately identified artifact-only source fits PROVINCE/QUALITY" — same condition | PASS (row, lesson, and corpus support agree) |
| Status / opened / recheck / lesson link | rejected / 2026-10-27 / 90d / corpus/lessons/round-72.md | Lesson S074 row (line 33) decision "REJECT for revenger's province, tier C"; line 58 confirms S050/S051 remain the narrow support and "Do not write to kasegi's corpus" was honored; lesson line 62 lists S074 among rows "with located reject reasons and explicit flips" | PASS |
| Duplicate registry ids | S074 unique | `grep -n "S074" corpus/SOURCES.md` → one row (line 88) plus lesson/report mentions; no duplicate id | PASS |
| Superseding row | none for S074 | None exists; none needed (no defect found) | N/A |

## Prior spotcheck cross-reference

corpus/lessons/round-72-verifier-spotcheck.md line 75 records that the outside verifier re-opened "the extra README/catalog pages (S063, S073, S072, S074)" and found every checked quote ≤25 words. My independent re-fetch on 2026-10-30 confirms S074 specifically: verbatim, 17 words, pin valid. The two routed quote defects named in the round-73 brief (S071 registry paraphrase; S082 misattribution) do **not** extend to S074. Observation only: a superseding row S427 (supersedes S071) already exists in the committed corpus (SOURCES.md line 442, lesson corpus/lessons/round-73.md); S082 belongs to its own assigned seat and is not reported here. Per assignment, no other source admission and no other row's report is in scope.

## Evidence classification

- Observation: fetched README bytes at the pin (HTTP 200, sha256 above); API commit object; byte-level quote equality after `**` stripping; grep results for S074/S050/S051/S427; spotcheck lines cited.
- Inference: none material — the rejection ground ("broad red-team/exploit procedures outside the static artifact-first scope") is directly readable from the pinned README's own category text.
- Unknown: nothing blocking. (HEAD of the default branch was also live, HTTP 200, on 2026-10-30; the row is pin-bound so HEAD drift does not affect it.)

## Network / source failures

None. Both requests succeeded: raw.githubusercontent.com HTTP 200; api.github.com commit lookup returned the full verified commit object.

## Tooling record

No installs or updates this seat (nothing needed beyond curl/python3/sha256sum already present; pacman pause honored). No git/jj mutations, no builds/tests run, no child tasks, no background jobs. Scratch dir /fast/scratch/hyaku/revenger-r73/R73Source074/ (one clone-free download) cleaned after receipts were copied into this report.

## Judged axes note

- Coverage: assigned round-72 row S074 audited as scoped; report delivered.
- Source accuracy: located quote verified VERBATIM against the cited primary pin; agree with disposition; no superseding row required for S074.
