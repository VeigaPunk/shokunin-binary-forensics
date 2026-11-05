# ReviewerBlind report — revenger round 93, w1 (C08 blind-derivation vote)

Task: derive the C08 record's facts from primary bytes only, then compare the ScribeEntry draft's
statements against those blind derivations and emit the frozen-schema vote.

## Protocol and artifact order
1. Wrote scratch derive.py (`/fast/scratch/hyaku/revenger-r93/ReviewerBlind/derive.py`), reading
   ONLY index.html bytes, app.js bytes, and inspection.json bytes. Ran it first at 11:49:47
   local; the ScribeEntry draft did not exist until 12:07-12:08 (bounded wait, 29 checks x 30s,
   then 21 more x 30s → ~14.5 min total non-idle). Blind phase honoured.
2. Saved `blind-derivation.txt` (69 lines + 6-line addendum) in my wave dir BEFORE any entry read.
3. Read the entry draft (40551-byte final version) and produced `comparison.tsv`: 32 statements
   (every identity fact, digest, length, reconciliation status, volatile item, S496 quote) —
   32/32 match, 0 mismatches, 0 unsupported statements.
4. Wrote `evidence.md` first, then `vote.json` (required order).

## Independent verification actually executed
- Oracle re-run by me, twice: lane root AND an isolated scratch root containing only the oracle,
  truth.json, both fixture files, and the record — both exit 0, both end
  `ORACLE OK (17/17 checks)`, outputs byte-identical to each other.
- All 7 embedded `transcript` one-liner blocks replayed with shlex-parsed argv from the lane
  root; every output line matches its embedded block line-for-line (7/7).
- `git rev-parse 02050cb2a6758e3bd9cec696ff0e42df6f23511a^{commit}` → same id;
  `git diff --quiet <id> -- corpus` rc 0 (corpus byte-identity clause backed).
- S496 fetched MYSELF (curl, HTTP 200, 35462 B, sha256 ba8018bb02f360686cbff23304da8b6e21923a2e012ade273e3f9a2ce1e2fd64),
  byte-identical to ScoutRecord's saved body; 15-word quote located by me at norm-offset 2733;
  receipt span 3408-3526 legitimately binds quote to body (verified against the frozen
  audit-source-quoges verifier's own algorithm; no gate divergence with ReviewerGate at any point).
- Gates run as evidence (on the draft copy, never the L1 files): lint QMAP/Q14/Q15/HEADER all 0,
  exit 0; embedded-output gate checked_blocks=2 problems=0, exit 0; audit_source_quotes verify
  exit 0 with SUMMARY verified=1 unresolved=0.

## Candidate and artifact digests
- first derived candidate (draft bytes at 12:11 read, 40551 B): 6dc0c74ad61fbd837123c04fdc2dcfbf17c8202ab0451f686cab91fede82b5ea
- after two scribe edits the draft changed again (current 37729 B, mtime 12:14:32) (I was notified by the L1 (RevengerR93); I re-read the current bytes, re-verified the admission-status line is still exactly
  `candidate` (no normalisation substitution needed), re-ran all verifications on the current bytes
  (2/2 $ oracle blocks + 7/7 transcript blocks byte-identical on my own reruns, including the new
  receipt `duration_seconds`/`producer` lines), and re-ran both gates (lint rc 0, embedded rc 0).
- final bound vote.json: candidate_sha256 0db16a56fb0c2346d7109999dd6d98123403a52fa67d189112ba5597860593da
  (matches current READY), artifact_sha256 2a7609be0eb0f0630d4afc8b5a7b8207356828f7223c571cf5616b449d741958.

## Decision
Q01 Q02 Q03 Q04 Q06 Q07 Q09 Q10 Q11 Q13 Q14 Q15 Q16 Q17 = PASS (14);
Q05 n/a (no capability claim; item 21 of the entry refuses one explicitly);
Q08 n/a (superseded by Q11 per corpus/QUALITY.md);
Q12 n/a (no rejected row / no flip claim).

## Defects found: none.
The draft's edit cycle during my session (40471 -> 40551 bytes; admission-status was already
"candidate" in both versions; my final numbers were re-verified against the 40551-byte bytes)
introduced no factual drift. Every file, path and digest named by the entry resolves or re-derives.

## Tooling authorization
No tool installed or upgraded (nothing needed beyond stock python3/curl/git).

## Wave-dir files written
blind-derivation.txt, comparison.tsv, evidence.md, vote.json, S496.body (re-fetch evidence).
Scratch deleted before yield.

## Post-vote corrections (post-landing, same session)

Three L1-requested rebindings, each with a targeted re-derivation, blind data untouched:

1. Draft edited again after my first bound vote (40471 → 40551 → 37729 B). Re-read current bytes;
   admission-status verified still exactly `candidate`; re-verified 2/2 $ oracle blocks + 7/7
   transcript blocks on my own reruns (including new receipt `duration_seconds`/`producer` lines);
   gates re-run rc 0/0. Rebound: candidate 0db16a56fb0c2346d7109999dd6d98123403a52fa67d189112ba5597860593da.
2. Landed entry (corpus/knowledge/round-93-browser-cdp-runtime-evidence.md): two underived prose
   counts removed ("The stdout line count of the oracle block is 18."; "(15 words)"). I re-derived
   BOTH numbers myself on the same runs (18 lines = 17 check ok + 1 summary; quote = 15 words) —
   both were correct as facts but were prose without a deriving command, so removal is the right
   Q11/Q16 tightening. Rebound: candidate 53083246d5528eab8682f5938e4f1b0967683ae883499d15d702d9f671bd1fb1.
3. verified-at byte-identity clause re-scoped to corpus/live + corpus/fixtures (dropping the too-wide
   whole-corpus claim). I ran both scoped `git diff --quiet 02050cb2a… -- corpus/live` and
   `-- corpus/fixtures` myself: rc 0 silent. Final binding: candidate
   1304008c5a0aff9dbb9af09967e12caeef028b1ca52e14dac7b8fe0247e43647,
   artifact_sha256 b0d4e6466ae046d848dc11e24f07c0c6c40d9f89bdef239c26fadc462c3426ff.
   Gates on final landed bytes: lint rc 0, embedded rc 0; 9/9 embedded blocks byte-verified on my
   own reruns.

Defect verdict carried through all three states: none in blind-relevant content. The only wording
issues found across the session (underived counts; over-wide byte-identity claim) were caught and
removed by the L1 before final landing — both classes are exactly what my Q11/Q15/Q16 votes guard.
