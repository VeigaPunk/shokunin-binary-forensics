# ReviewerBlind — blind-derivation evidence for the C08 entry (round 93, w1)

Seat: ReviewerBlind (reviewer). Blind protocol honoured: I derived every fact from primary
bytes — `corpus/fixtures/browser-r77/{index.html,app.js,truth.json}` and
`corpus/live/runs/round-77/inspection.json` — and saved the derivations BEFORE opening the
ScribeEntry draft, the LEDGER, or any sources material. Artifact chain and byte sizes are at the
end; the derivation script lives at scratch `revenger-r93/ReviewerBlind/derive.py`.

## 1. Blind derivation (pre-entry)

`derive.py` parses only: index.html bytes, app.js bytes, inspection.json bytes.
Full verbatim output is committed beside this file as `blind-derivation.txt` (mtime
predates my first read of `entry-draft.md`; draft mtime 12:08:56, derivation written 11:49:47).
Key blind values (all re-derived by me, none copied from the entry):

- fixture digests: index.html 316 B, sha256 46e51761af28b05c4c382c8ee72f9d77fee6f20d0b904f69b1c7f9a2214deb45;
  app.js 101 B, sha256 fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593
- derived final title (static `<title> r77 probe page</title>` + inline JS literal `" [loaded]"`):
  `r77 probe page [loaded]` — equals the record's `target.title`
- record file: 10816 bytes, sha256 b045a4eecf2d77cfdee5de83e5864fcadbd6fd54e749f6985a04ecbeebaae868
- operation `inspect_web_page`; predicate_type `rea.web-page-inspection`
- provider.id `rea-cdp-browser` (name "REA Chrome DevTools Protocol observation provider", version "2")
- evidence_id `ev_a0134e6f482424baa278ec374f9bf0e984738a113106556b9933d2fd403918fd`, shape well-formed `ev_` + 64 lowercase hex (67 chars)
- target.url `http://127.0.0.1:8477/index.html`; target.origin `http://127.0.0.1:8477`
- metadata.dom_urls: exactly one entry, node_index 10, attribute src, url `http://127.0.0.1:8477/app.js`, destination_scope approved; excluded_dom_urls 0
- scripts.total 2; lengths 46 (inline, measured from index.html bytes between `<script>` tags, no src) and 101 (app.js committed bytes)
- cdp_hash inline `ee8e9624a274382bf825525637e2db30823eda881461276f6eed7e990b157783` == sha256(inline text from index.html bytes)
- cdp_hash app.js `fb079fa20d08a1309bed44c80743293d37ec8cd51c7ef7f9ee465e0d0d5aa593` == sha256(committed app.js bytes)
- resources: 1 entry; resource_key `res_0948976cb8f3ecdc1bafa5111ba86f55744db2803a8f1fc2a03cd66ee1b69548`;
  type `Script`; mime `text/javascript`; content_size 101; url `http://127.0.0.1:8477/app.js`
- script resource_reconciliation: app.js item `exact`; inline item `unmatched` (reason `no_exact_sanitized_url`)
- frames[0] frame_id == target_id == `F6A6B5C8E48625523BCEA0CE47F68B42`; url == page url
- completeness.status `policy_filtered`; browser.product `Chrome/156.0.8078.74`
- capture_window started_at 2026-11-01T06:59:28.999Z, ended_at 2026-11-01T06:59:29.701Z, observation_ms 500
- record confidence `observed`, authority `external-service`
- volatile fields (from authored `truth.json`): evidence_id (shape only), target_id/frame_id,
  script_key/cdp_hash per session, capture_window timestamps, completeness counters

## 2. Comparison (blind value vs entry statement)

Full table committed as `comparison.tsv` (fact, blind value, entry value, match): 32 statements
compared, 32 line up, 0 mismatches, 0 unsupported. Includes every oracle check name, every printed
digest, the derived title binding, the volatile list, the reconciliation statuses and the S496 quote.

## 3. Independent verification per criterion (no gate divergence with ReviewerGate)

- Q01 — every load-bearing fact is either a re-derived record fact (S495, tier-A own-work, opened
  today; oracle re-run by me: ORACLE OK 17/17, exit 0, byte-identical output to ScoutRecord's
  oracle.log) or the one external sentence about CDP (S496). No tier-C support. PASS.
- Q02 — header carries source:, verified-at: (02050cb2a6758e3bd9cec696ff0e42df6f23511a, resolved by
  me: `git rev-parse <sha>^{commit}` prints the same id; `git diff --quiet <sha> -- corpus` rc 0),
  recheck: (the oracle command, ends `ORACLE OK (17/17 checks)` — confirmed on my own run),
  coverage-map: C08, admission-status: candidate. No bare-homepage anchor. PASS.
- Q03 — expected values derive from committed fixture bytes or from pins fixed in the authored
  truth.json or literals in the oracle; the item-24 three-column partition table in the entry maps
  each check to its expectation side and I verified the partition against my own derivation (5
  byte-derived / 9 truth-pinned / 1 literal; 2 mixed checks named below the table — all correct). PASS.
- Q04 — tool credit names the oracle script, its 17 named checks, and the producer as record field
  source; lines print what I confirmed by running them myself. No tool credited with a result it
  did not output. PASS.
- Q05 — no capability/readiness claim is made; item 21 explicitly refuses one. n/a (no such claim).
- Q06 — the oracle re-hashes both fixture files against truth.json on every run (first two lines);
  my scratch-copy rerun reproduces those lines. PASS.
- Q07 — no pre-registered parser prediction in this entry; nothing was predicted. PASS (criterion
  does not hinder; nothing to pre-register).
- Q08 — superseded by Q11 (per QUALITY.md, Q11 is the operative re-derivation criterion). n/a.
- Q09 — receipts claimed only for the bytes hashed; item 22 explicitly disclaims
  origin/completeness/authenticity; digest comparisons labelled byte-identity only. PASS.
- Q10 — scope is one provider operation, one authored inert fixture, one saved record; the single
  external sentence does not generalize. PASS.
- Q11 — every count, identifier and digest prints from a named command. I verified this by
  running the oracle twice myself (byte-identical full stdout, including in an isolated
  scratch root without the rest of the tree) and by replaying all 7 transcript one-liners with
  shlex-parsed argv from the lane root: every output line matches its embedded block
  line-for-line (my own re-runs, not the scribe's). PASS.
- Q12 — no source row is rejected or flipped in this entry. n/a.
- Q13 — item 26 names the clauses the recheck cannot detect (entry sentences, table rows) and
  notes the transcript blocks are deliberately not re-executed by the embedded gate (their
  `python3 -c` form is outside that gate's confinement, which I confirmed in the tool: only
  `python3 [-B] <script in tree>` replays). No clause-level guard credit. PASS.
- Q14 — no prose hex run carries a byte count; all hex values are fenced-block output lines.
  PASS (lint LINT_Q14=0 agrees).
- Q15 — the one git id is named with `git rev-parse <id>^{commit}`; I ran it, it resolves to that
  same id; the corpus byte-identity clause is backed by my own silent `git diff --quiet` (rc 0).
  PASS (lint LINT_Q15=0 agrees).
- Q16 — every printed line in the embedded blocks corresponds to real stdout of the named command
  (I re-ran the oracle and all 7 one-liners myself); the §5 provenance table maps each statement
  to the emitting line; the ORACLE summary line count (18 stdout lines for 17 checks + summary) is
  stated correctly and I confirmed it on my own output. PASS.
- Q17 — no artifact relocation in this round; every path named resolves in the tree at the pinned
  commit (byte-identity confirmed via git diff --quiet 02050cb2a6758e3bd9cec696ff0e42df6f23511a -- corpus). PASS.

## 4. External source (S496) — my own fetch, not the scribe's receipt

URL: https://chromedevtools.github.io/devtools-protocol/ (curl from the lane root, 2026-11-05).
HTTP 200, length 35462 bytes, sha256 ba8018bb02f360686cbff23304da8b6e21923a2e012ade273e3f9a2ce1e2fd64
— byte-identical to ScoutRecord's saved raw body. Raw saved as S496.body beside this file.
Located quote (norm-offset 2733 in my fetched text; 15 words):
"It allows tools to instrument, inspect, debug, and profile Chromium, Chrome, and other Blink-based browsers."
Span-check: quote appears within norm(text[3408:3526]) exactly as ScoutRecord's receipt binds.
No adjective stronger than the page's own words is introduced by the entry; every other statement
about CDP is excluded and the entry says so. tier A for that self-description is appropriate (Q01).

## 5. Gates (unchanged by me, run only as evidence)

- lint_entry.py on the draft: LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0, rc 0
- check_embedded_outputs.py on the draft: checked_blocks=2 problems=0, rc 0
- audit_source_quotes.py verify --sources <scratch copy of SOURCES.md + both new rows> --receipts
  ScribeEntry/quote-receipts --sid S496: S496 verified, SUMMARY rows=1 verified=1 unresolved=0, rc 0
  (again at receipts dir ScoutRecord/quote-receipts — identical result)

## 6. Candidate digest (recomputed by me from the bytes I read)

- READY (committed by ScribeEntry): `sha256=6dc0c74ad61fbd837123c04fdc2dcfbf17c8202ab0451f686cab91fede82b5ea`
- my recompute (admission-status line already normalised to `candidate` in the draft — verified,
  no substitution performed): sha256 = 6dc0c74ad61fbd837123c04fdc2dcfbf17c8202ab0451f686cab91fede82b5ea
  — byte-identical twice (second time over a byte-for-byte identical draft copy at scratch
  `spin0/hello.md`), headless, no editor repetition.
Note: draft was edited once (40471 -> 40551 -> 37729 bytes (final current read at 12:14:32 local), admission-status and §5 table additions after my
first read); my final re-read is of the current 37729-byte version; the admission-status line was verified still exactly `candidate` after BOTH subsequent scribe edits (no normalization substitution needed), and all numbers in this file were re-verified against that version (oracle 2/2 blocks, 7/7 transcripts, all gates re-run on current bytes). Recompute timestamps: first candidate 6dc0c74a… at 2026-11-05T12:11:29Z, current candidate 0db16a56… at 2026-11-05T12:15:03Z.

## 7. Artifact and vote binding

artifact_path: .ufo/waves/round-93/w1/ReviewerBlind/evidence.md (this file)
artifact_sha256: (computed at write time, same value written into vote.json)
No synthetic edits to the draft were made by me (I only read); no gate divergence with ReviewerGate
was introduced at any point.

Decisions Q01–Q17: Q01 PASS, Q02 PASS, Q03 PASS, Q04 PASS, Q05 n/a (no capability claim — item 21),
Q06 PASS, Q07 PASS, Q08 n/a (superseded by Q11, per QUALITY.md), Q09 PASS, Q10 PASS, Q11 PASS,
Q12 n/a (no rejected row, no flip), Q13 PASS, Q14 PASS, Q15 PASS, Q16 PASS, Q17 PASS.

## 8. Landed-entry re-check (post-removal corrections by RevengerR93, 2026-11-05 ~12:22 local)

Final landed bytes: corpus/knowledge/round-93-browser-cdp-runtime-evidence.md, 37668 bytes,
admission-status line reads exactly `admitted` (lands as `candidate` under the frozen counter's
normalisation — verified), normalized digest = 53083246d5528eab8682f5938e4f1b0967683ae883499d15d702d9f671bd1fb1
(recomputed twice on my side). Only two edits vs the draft I had just re-verified:
- removed the prose sentence "The stdout line count of the oracle block is 18." — I re-derived the
  number myself on the same oracle invocation (17 `check ok:` lines + 1 `ORACLE OK (17/17 checks)`
  summary = 18 stdout lines) BEFORE committing to the removal binding. The sentence was prose
  without a derivation command in the entry; its removal is a legitimate Q11 tightening under my Q11
  vote rationale, and the count remains re-derivable directly from the first block's own output.
- removed the parenthetical "(15 words)" beside the S496 quote. My blind derivation had counted the
  quote as 15 words (noted in §4 above); that too was underived prose (no entry command prints 15),
  so its removal is the same class of tightening.
No other content changed (verified by full-file diff against my verified 37729-byte draft: only
the two deleted spans and the admission-status line that always changes at landing). The 32-factor
blind comparison.tsv is unaffected (no row referenced those two prose fragments as entry-specific
values; both counts themselves re-derive from my blind data and remain correct as detached facts).
Gates on the LANDED bytes: lint rc 0; embedded rc 0 (checked_blocks=2, problems=0) — re-run by me.
The vote count bound to this landed entry is candidate_sha256 53083246… with artifact_sha256
(hashed over this evidence.md after this section was appended).

## 9. verified-at scoping re-check (second post-landing correction, 2026-11-05 ~12:25 local)

The landed byte-identity clause previously claimed the whole corpus tree byte-identical at commit
02050cb2a6758e3bd9cec696ff0e42df6f23511a. It now reads — scoped to what the byte-identity actually
backs: `git diff --quiet <id> -- corpus/live corpus/fixtures` is silent, and the corpus index and
registry files are explicitly NOT claimed identical. I re-ran both scoped invocations myself:
- `git diff --quiet 02050cb2a6758e3bd9cec696ff0e42df6f23511a -- corpus/live` → rc 0 (silent)
- `git diff --quiet 02050cb2a6758e3bd9cec696ff0e42df6f23511a -- corpus/fixtures` → rc 0 (silent)
and the combined two-path form the clause names (`-- corpus/live corpus/fixtures`) is the same
byte-identity, split across the two directories the entry actually reads — exactly my Q15 criterion
(a stated identity must be true under the command that names it; now it is, and it names only the
paths it covers). Recomputed candidate digest on the current landed bytes:
1304008c5a0aff9dbb9af09967e12caeef028b1ca52e14dac7b8fe0247e43647 — matches the L1's stated value.
Gates re-run on the current bytes: lint rc 0, embedded rc 0 (2 blocks, 0 problems).
The earlier 9-block byte-verification (2 $ oracle + 7 transcript) is unaffected by this one-sentence
edit (I diffed: only the verified-at line changed since digest 53083246…).

Vote re-bound: candidate_sha256 = 1304008c…47, artifact_sha256 = sha of this evidence.md as it now stands.
