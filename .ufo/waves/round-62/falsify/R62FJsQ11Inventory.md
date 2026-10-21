GRADE: PARTIAL — corpus/knowledge/round-62-commonjs-require-name-evidence.md (C04 candidate, admission-status: candidate)

Target: file SHA-256 `42096e9676d33e25c3b6092e60fbd0fdacd699435ed9dc9db59ce24a1ceaaba3` (37474 B), identical to `git show d97761952be256d145d298022de03091de91d358:corpus/knowledge/round-62-commonjs-require-name-evidence.md` (worktree == frozen, `git diff` empty).
Frozen candidate state `d97761952be256d145d298022de03091de91d358`; claim base `5bd4a90fc1a34caa94496601b60537b3aab12301`; pre-registration `a3498e25ad87bf756288812d0ea7c474b09433c7`. Entry's own corpus revision: `a3498e25…`.

Scratch: /fast/scratch/hyaku/revenger-r62/R62FJsQ11Inventory (TMPDIR=…/tmp). No live edits, no git index/history mutation, no producer/provider call, no fixture JS or EVM execution, no network except one read-only fetch of the cited public ECMA-262 page.

## Reproduced ground (all pass)

- Extracted `git -C <repo> archive a3498e25… | tar -x -C tree_a349` (also d9776195 tree). Ran the entry's own code block, extracted verbatim from the entry: sha256(readout.py as printed, with trailing NL, 6974 B) = `31dac2113f1b78967a635fbf65125ecedc7a7ab4924debad8ba3c4be77ee02ac` — matches entry L080.
- `python3 -B readout.py tree_a349` → exit 0, 25 stdout lines, sha256 `58b63dd9d7c7ae4a0311ff33f12317345f7e5b7c9e8f204cfb13d1d599f0c416` — matches header `recheck:` (L004) and L080. Same digest/25 lines on the d9776195 tree (corpus content identical).
- The entry's "Exact stdout" block is byte-identical to my run (block sha256 = `58b63dd9…`, 7547 B).
- Hand-checked spans against fixture bytes: js-r3 `require` at 28..50, pattern [6,25), assignment [6,50); js-r7-v2 18..40, [6,15), [6,40) — all match stdout. Require statement is physical line 1 of both fixtures at a349 (verified from bytes).
- Truncated aliases `92ef8e3d…`, `cd9f3f63…`, `8eec9ffb…`, `696c2496…` are correct prefixes of the printed digests. Record bytes/digests/Evidence IDs/operation/provider id+version, all edge fields, counts (3/2/1, 2/1/1) and both deltas match stdout exactly.
- Cited ECMA-262 page fetched read-only: sha256 = `06db92a8331aa452b0d4de8c8938f4b7559b72417769b57d0032002398f27d7f` — reproduces the S029 row digest; page header "Draft ECMA-262 / October 16, 2026". §14.3.3.3 KeyedBindingInitialization, production `SingleNameBinding : BindingIdentifier Initializeropt`, step 3: "Set value to ? GetV(value, propertyName)." — quote verbatim, referent correct.
- `corpus/README.md:33` C04 status = `uncovered`; `corpus/knowledge/commonjs-destructured-require-edges.md` unchanged a349→d977 (`git diff --stat`: only SOURCES.md and lessons/round-62.md changed); S029/S030 rows exist in corpus/SOURCES.md, tier A, `mined`, opened 2026-10-21.

## Concrete failures (each: path:line + exact output)

1. L056 (item 21) contradicts the entry's own stdout. Claim: "only the fields named in items 1-13 were read". The readout reads and prints `edge_id` for all five edges — 5 values `jag_edge_66e056c7…`, `jag_edge_b5c88eb6…`, `jag_edge_b6378db3…`, `jag_edge_2ff2c8d4…`, `jag_edge_7a0c9240…` — and the token `edge_id` appears nowhere in the entry prose (only inside the code block and the stdout block). `location.start_line`/`end_line` are likewise printed but never named in items 1-13. Inventory rows L264/L265 claim "all saved fields" while omitting `edge_id`. Round-62 lesson M27 requires auditing "claims that the block 'carries' a field, not just the printed values" — this block prints a field it neither carries nor disclaims.
2. L080 (§Reproduce): "The stdout carries no path, so the same bytes give the same 25 lines from any extraction directory." Literally false — the stdout carries relative paths: `"dir":"corpus/fixtures/js-r3"`, `"source_file":"corpus/fixtures/js-r3/index.js"`, `"path":"corpus/live/runs/20261012T164357Z/analysis.json"`, `files[].path`. The verified property is "carries no absolute path" (my two extraction dirs gave identical bytes; `grep -c "/fast\|/home/\|/tmp/" stdout` → 0).
3. L248 (§Sources S029): the quoted text is labelled "— 8 words". `"Set value to ? GetV(value, propertyName)."` = 6 whitespace tokens / 6 lexical words (Set, value, to, GetV, value, propertyName); the page's HTML-normalised form `"Set value to ? GetV ( value , propertyName )."` = 10 tokens, same 6 lexical words. No counting gives 8, and no in-entry command derives the count (Q11 requires counts to carry a derivation).
4. L068 (item 30) presents a non-verbatim string as a quote. corpus/lessons/round-62.md:29 reads `| ADJ-06 sibling arbitration | Operator-owned and unresolved; new entries do not declare ownership or a ruling. |`; the entry renders it with ":" instead of the cell separator, lower-cases "Operator-owned", and drops the final period.
5. L029 (item 6): "These are **recorded** fields of the saved files, not re-derived here" also covers `bytes` and the record `sha256`, which the command does derive (`len(record_bytes)`, `sha(record_bytes)`); only `evidence_id`, `operation`, `provider_id`, `provider_version` are literal copies. The entry's own L049 (item 17) and L249 (§Sources S030) draw the recorded/derived line correctly.
6. L037 (item 11) derivation gap: "the bytes read back at the saved columns are the texts above" — the code slices the *matched non-empty line* (`line[start:end]` in `import_edges`), never the file's saved line, and never compares the matched line with `location.start_line`; `line_number_1based` counts non-empty lines (7 for an 8-line split) and is a different coordinate from the saved line number. The correspondence holds on the data (both require statements are physical line 1; saved start_line=1) but the entry does not derive it.
7. L048 (item 16) labels the production "`SingleNameBinding : BindingIdentifier`"; the cited draft's heading is `SingleNameBinding : BindingIdentifier Initializeropt`. Referent and step are correct (matches S029's own "SingleNameBinding step3"); only the heading is elided.
8. L065 (item 27): "every value rests on the in-entry derivation of §Reproduce" overreaches for four attributed-not-derived values: the S029 page digest 06db92a8…, the ADJ-06 lessons quote, item 29's "byte-unchanged" repo-state claim, and item 26's "the one network access this round".

## Inference / unknown

- Inference: items 1-13 and 14-17 are fully carried by the reproduced output; the entry's substantive C04 content (names, spans, counts, deltas, recorded-vs-derived labels) does not depend on any of the 8 defects above.
- Unknown: the authoring round's process claims (item 26's network accounting, item 29's unstated "byte-unchanged" baseline) are not observable from the frozen tree; §16.2.1.7 Table 54 exists on the cited page but the entry does not rely on it, so its content was not audited.
- Not audited (out of scope): the EVM candidate, any admission, any held flip.

## Minimal correction (names only, no repair performed)

L056: state the read set accurately (edge_id and location.start_line/end_line are read) or list them as excluded; L080: "no absolute path"; L248: correct the quote's word count; L068: quote corpus/lessons/round-62.md:29 verbatim or mark it a paraphrase; L029: limit the "recorded, not re-derived" label to evidence_id/operation/provider id/version; L065: scope "every value" to §Reproduce-derived values.

VERDICT: PARTIAL — the entry's data and its reproduce section are byte-exact and independently re-runnable, so it is not BROKEN; but six in-entry factual claims are contradicted by the entry's own printed output or by cited text (items 21, 26-labelled wording, quote word count, ADJ-06 quote, item 6 label, item 27 scope) and two labels are imprecise (item 16 heading, item 11 line-coordinate derivation). The entry's self-declared QUALITY Q11 "pass" (L294) is therefore not fully supported; C04 must stay `uncovered`/candidate pending an independent focused re-review of the corrected bytes by an already-assigned fresh-wave seat (corpus/lessons/round-62.md, admission order). Recommendation only — no admission, no repair, no integration by this seat.

INSTALLS: none (no package installed or updated this run).
