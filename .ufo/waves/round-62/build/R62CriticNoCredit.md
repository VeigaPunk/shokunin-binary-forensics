RESULT: COMPLETE

# R62CriticNoCredit — no pre-credit / byte preservation for frozen C1

Scope: this report attacks the `claims.md` admission order only. It edits no production files and makes no admission.
I extracted frozen `a3498e25ad87bf756288812d0ea7c474b09433c7` with `git archive` to
`/fast/scratch/hyaku/revenger-r62/R62CriticNoCredit/frozen`, and ran every check with cwd=/ on copies of that archive.
The live repo HEAD is still `a3498e2`. Neither round-62 candidate path exists in the frozen tree, so both are genuinely new files.
Inputs I read: frozen `reports/round-62/claims.md` (sha256 `361605a9…1032`),
`corpus/lessons/round-61-verifier-spotcheck.md`, the K section of frozen `reports/round-61/measure.py`
(lines 22–34), README rows C04/C09, and QUALITY Q10–Q13.

## Counterexample 1 — the frozen K probe counts rejected files as coverage (verified)
`measure.py:32–33` counts a held row as backed whenever every `knowledge/*.md` path named in its knowledge cell exists as a file.
I ran the frozen K section verbatim (sha256 `1f1b9864…cb85`, 35 lines) against README mutants with `oracle/k_mutants.py`:
```text
M0 frozen baseline                                   K_HELD=4/14 K_HELD_BACKED=4/14
M1 C09 held, cell names OLD rejected evm file        K_HELD=5/14 K_HELD_BACKED=5/14
M2 C04+C09 held, cells name OLD rejected files       K_HELD=6/14 K_HELD_BACKED=6/14
M3 C09 status flip only, no knowledge path           K_HELD=5/14 K_HELD_BACKED=4/14
M4 C09 held, new path absent                         K_HELD=5/14 K_HELD_BACKED=4/14
M5 C09 held, new path = byte copy of rejected file   K_HELD=5/14 K_HELD_BACKED=5/14
M6 C09 held, new path = empty file                   K_HELD=5/14 K_HELD_BACKED=5/14
M7 C09 held, cell names new + OLD rejected           K_HELD=5/14 K_HELD_BACKED=5/14
```
Calling the old rejected files "superseded/accepted" and naming them in the README would therefore meet C1's ≥5/14 target on probe output alone.
The same holds for a re-headed copy or an empty stub.
`claims.md:41–44` already says the probe is existence-only, and the spot-check's routed item 3 (`round-61-verifier-spotcheck.md:215–216`) says the same. The probe must not change: claims.md uses it as the unchanged before/final command.
Impacted axes: coverage (false 5/14 or 6/14) and discernment.
Fix: add a separate necessary check, kept outside the probe and stated as not admission (see Proposed artifacts).

## Counterexample 2 — post-falsify edits need only a "focused" re-review (from the text)
`claims.md:47–50` says candidate defects "may be corrected … with changes and focused non-author-seat re-review".
Nothing ties a Q01–Q13 decision to the candidate's bytes. A fix to one derivation can change other printed values or prose that were already judged.
Round 61 shows the risk: the lane's initial Gate admits were overturned by the outside closure (`round-61-verifier-spotcheck.md:142–145`).
Fix: bind each per-candidate decision to a sha256. Any byte change after the attacked commit voids that file's whole Q01–Q13 table, which is then redone on the new bytes by a non-author seat that did not write the file's oracles.

## Counterexample 3 — self-grading and support from old entries (risk; no drafts exist yet)
No round-62 candidate draft exists yet in the repo or under `/fast/scratch/hyaku/revenger-r62/*`. I grepped peer scratch for the old slugs and for "supersed"; the only hits are frozen-tree copies.
So there is no violation yet. The remaining risks are below.
- (a) A new file that cites the old file or its Reproduce output as support. Claims line 50 forbids this; my checker flags such lines with `ADJUDICATE`.
- (b) L1 being both planner and integrator while writing the decisive lesson decisions. That lesson must contain per-row decisions signed by a non-author seat.
- (c) A `git mv` of the old file, or re-heading it as "superseded". Both void the byte-preservation hold (claims.md:59–60).

## Proposed artifacts (scratch only; none landed)
- `oracle/admission-order.md`: a 6-step candidate → attack → correct → decide → admit order. Candidates land with the header `admission-status: candidate` and README stays uncovered. The falsify wave names commit D and each file's sha256. Decisions are bound to a digest. At admission, the README knowledge cell names exactly the round-62 path. The old files stay only in the work-evidence column, byte-unchanged and never described as superseded.
- `oracle/nocredit_check.py` (sha256 `54258704…a42` after the addenda below): a necessary check that never admits anything. It covers preservation of 612 files (both rejected files, `lessons/round-61*.md`, `reports/round-61/**`, `.ufo/waves/round-61/**`, `corpus/live/**`, `corpus/fixtures/**`), byte-equality of the Q01–Q13 rows, 14 README rows with non-target rows unchanged, the draft stage (C04/C09 must stay uncovered), and the admission stage (exact new path, not a byte copy of a rejected file, not marked candidate/rejected).
- `oracle/preserve-manifest-a3498e2.sha256`: 612 lines, sha256 `b7fac91f…5a1e`; `sha256sum -c` on the frozen tree printed `self-check-ok`.
  Both rejected files are included: commonjs `690db9f1…a6f3` and evm `3e17b88f…9361`.

Red/green run (`oracle/run_nocredit_mutants.sh`; output in `oracle/nocredit_mutants.out`):
```text
G0 frozen, draft                       exit=0 NO_VIOLATION
G1 new candidate file added, draft     exit=0 NO_VIOLATION
R1 held naming OLD file, admission     exit=1 cell not exactly round-62 path; new path absent
R2 byte copy of rejected as new path   exit=1 byte-equal to rejected; header admission-status='rejected …'
R3 held flip during draft              exit=1 README C09 status='held' before admission
R4 old file re-headed "superseded"     exit=1 PRESERVE changed …evm-saved-interface-candidates.md 3e17b88fff8c->f12ae51156cf
R5 git-mv old -> new path              exit=1 PRESERVE missing …evm-saved-interface-candidates.md
R6 Q11 wording weakened                exit=1 QUALITY Q01-Q13 rows differ from frozen
R7 cell names new+OLD, text cites OLD  exit=1 ADJUDICATE line 4; cell names both paths
R8 evm-r24 fixture.raw +1 byte         exit=1 PRESERVE changed corpus/fixtures/evm-r24/fixture.raw
R9 C04 -> partial during draft         exit=1 README C04 status='partial' before admission
G2 admitted header, exact new path     exit=0 NO_VIOLATION (necessary only)
```
G2 passes with an essentially empty entry, which shows the check is necessary but not sufficient. The Q01–Q13 record remains the admission condition.

Addendum (after `R62ReviewJsQ13` input): the check now also flags carried-over Q13 guard-credit wording for adjudication. On the frozen tree, `grep -n column` finds no `column` in either JS verifier, and `verify_saved_evidence.py` has 0 v2 references. The rejected wording is at `commonjs-destructured-require-edges.md:80–83,208` (not :74–77/:202). A new C04 file carrying those lines → `ADJUDICATE` lines 4 and 8. A "no verifier credit is taken" Q13 row is not flagged. The prior 12 cases give the same exits.
Second and third addenda: every block (a list item with its wrapped lines, a table row, or a paragraph) that mentions a verifier, a recheck, or "<verb> by …" prints `ADJUDICATE-VERIFIER`. It is tagged by whether its line citations stay within the deletion-detected lines `verify_js_graph_delta.py:58`/`verify_saved_evidence.py:115`, and ranked `priority`/`disclaimer-like` by the peer classifier. The rank never hides a block. The peer's first classifier (`b5989b70…`) gave OK on 12 of 13 adversarial coverage claims (`oracle/q13_adversarial.out`). Checker sha256 `54258704…a42`; the 12 earlier cases give the same exits.
Fourth addendum (peer classifier rebuilt, sha256 `2104ffb2…3e08`): I reproduced 27/27 on its tests, 0 misses on my 18-case battery, and a frozen sweep of 2 REVIEW / 37 OK / 915 SKIP. A second battery (`oracle/q13_adversarial_r2.out`) still gets OK on 13 of 16 coverage claims: passive voice ("names are guarded"), verbs outside its list (rejected by, catch, fails, relies on, escapes, safe under), "Coverage:", table cells, and double negation. Ranking only, as above.
Fifth addendum (peer classifier rebuilt again on value-word co-occurrence, sha256 `515199c2…a69c`): reproduced 41/41 on its tests, 0 misses on my first two batteries, and a sweep of 9 REVIEW / 181 OK / 764 SKIP. Round 3 (`oracle/q13_adversarial_r3.out`) gets OK on 8 of 12 coverage claims: pronouns ("covers them"), a claim split across sentences, value words outside its list (identifiers, offset, count, target, require site), "credited, but … does guard the names", "Q13: guarded (…)". It also puts priority on 1 of 3 clean disclaimers. Final peer version `456ad251…`: 41/41, 18/18, 16/16, 12/12 with 0 clean-case priority, and a sweep of 10/180/764. C04 `1e5d68d2…` and C09 `a097a599…` → my checker exits 0. Under my block grouping, 3 C04 blocks still get priority, all false positives: two §P section headers (944, 1763) and the Q13 disclaimer (2484). Ranking only; full non-author Q13 review remains the gate.
Real candidates, placed at their new paths in a frozen copy and checked at the draft stage: C04 `R62JsEntry/candidate.md` (sha256 `7869e354…`; the peer's `d413eb9c…` is older) and C09 `R62EvmEntry/candidate.md` (`067a6dea…`, re-checked at `a097a599…`) → exit 0 at both revisions. Both headers say candidate. The 4 old-file/"superseded" hits are disclaimers or the Q08 row. All 16 verifier blocks disclaim credit. The C04 out-of-set citations (`verify_saved_evidence.py:107-108`, `verify_js_graph_delta.py:41`, `verify_semantic_trace.py:76`) match the frozen sources and describe what the verifiers compare; they credit nothing.

## Verdict on claims.md order
Sound as written: new paths, no held flips before the fresh falsify wave, all-criteria admission, Q01–Q13 unchanged, rejected files byte-preserved, and the probe not treated as admission.
Gaps found: counterexample 1 (probe blind spot; needs the separate check), counterexample 2 (no digest binding for re-review), and counterexample 3b (who signs the decisions).
README remains uncovered for C04/C09. This report does not hold or admit any row.
Unknowns: candidate texts were checked only at the draft stage for no-credit and preservation (fourth addendum). Nothing here checks Q11 derivation completeness.

Installs: none. Tools used: Python 3.14.8 standard library, coreutils, git archive (read-only).
