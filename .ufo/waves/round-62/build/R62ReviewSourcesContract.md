RESULT: COMPLETE

# Round-62 CORPUS sources-v1 review of the reserved S028–S031 design

Scope: contract compliance of the reserved source-row design only. No corpus file edited; no
README/map row touched; README stays uncovered per the round claim. Frozen base
`a3498e25ad87bf756288812d0ea7c474b09433c7` (`git -C … archive a3498e2 | tar -x -C frozen`);
`corpus/SOURCES.md` sha256 `aa7b07e12107ab9ef8f0933efd44cd7fcded2f7e5b3e186b2eee55e65bfaab58` (live =
frozen). Scratch `…/R62ReviewSourcesContract/`. Baseline census: `census --root … revenger` → rows 27 ·
tier.A 25 tier.C 2 · status.mined 22 queued 1 rejected 4; `validate … revenger` → `W04 S024 duplicate
url www.rfc-editor.org/rfc/rfc3227.txt across scopes`, `revenger ok`, exit 0 — one W04 (same RFC URL,
two scopes) is pre-existing.

**Contract facts, each measured on scratch copies.**
1. The duplicate-URL check keys on `url+scope`: same URL + *different* scope ⇒ W04, exit 0; same URL
   + *identical* scope ⇒ **E04, exit 1** (both measured). Every new row needs a scope string no live
   row uses; copying one is an exit-1 defect, not a style issue.
2. Fragment anchors are not a new URL: `…/ecma262/#sec-getvalue` normalizes to `tc39.es/ecma262` (same
   key as S022) — measured, still W04. Only a distinct scope string avoids the clash; `teaches` opening
   `supersedes S0NN` is the sole E04 escape and is wrong here (S016/S022 stay mined and cited).
3. Rows must sit inside `## Registry`; a row-shaped line after `## Paths` is `E12 … row outside
   Registry section`, exit 1 (measured). 11 cells per row (NF=13); a 10-cell row is `E01 fields=10`,
   exit 1 (measured).
4. used-by is existence-checked (E11): a `mined` row naming an absent file is `E11 missing used-by`,
   exit 1 — measured with the round-62 entry file absent. Those files do not exist at the frozen
   base, so either land them first, or land rows `queued` + used-by `—` and flip status/used-by
   afterwards (both flips rule-2 legal, each old→new logged in the lesson). `queued`+`—` is the
   existing S007 precedent; `W03 mined but unused` is warning-only.
5. Rule 2 append-only: only `status`/`recheck`/`used-by` change in place; `scope`/`anchor`/`teaches`/
   `kind`/`tier` are immutable ⇒ new scope ⇒ new row. Rule 4: a short registry beats a long one.

**Per-ID verdict.**
- **S028 (execution-specs v2.20.0, tier A for byte boundaries) — MINT.** S016's scope names only
  PUSH4/EQ/JUMPI/JUMPDEST + the jumpdest scan; the PUSH family, POP, STOP and the immediate-length rule
  are new ground for C09. Scope excludes PUSH4 by name so disjointness is explicit (else E04). Same URL ⇒
  one extra W04, exit 0.
- **S029 (ECMA-262, tier A for language semantics) — DO NOT MINT as reserved.** S022's scope already is
  "evaluation of destructuring binding patterns and the separation of ImportDeclaration from scripts,
  this draft only" (§14.3.1.3, §14.3.3.3, §16.2.2, quote "Set value to ? GetV(value,
  propertyName)."). A second row at that URL for that ground is a rule-4 duplicate plus a third W04.
  Instead re-open the draft this round, re-match the quote in the round-62 Gate (round-61 did this for
  S016–S019) and append the C04 entry to **S022's** used-by; the lesson should record that the
  reserved id went unused.
- **S030 (own-work, js-r3/js-r7-v2) — MINT, RESCOPED to authored source only.** The saved-graph half
  duplicates S027 (the two saved `analyze_javascript_application` outputs for js-r3/js-r7-v2); S027
  keeps that and takes a used-by append. S030's distinct ground is the **authored fixture source
  bytes** — destructuring names, call spans, manifests — which no live row covers (0 live rows mention
  `corpus/fixtures`). own-work kind with a repo path keeps it out of the URL-duplicate check.
- **S031 (own-work, seven EVM fixtures) — MINT, RESCOPED to authored bytes.** S026 keeps the seven
  saved `inspect_evm_interface` outputs (+ used-by append); S031's distinct ground is the authored
  bytes plus carrier-vs-decoded digests and recorded offsets. `truth.json` offsets are *recorded*;
  teaches says the bytes are what a scan is checked against, preserving the recorded-vs-derived line
  (Q11).

**Recommended end state (measured).** rows 30 · tier.A 28 tier.C 2 · status.mined 25 queued 1
rejected 4 · W04 = S024 (pre-existing) + S028 → validate exit 0, "ok". The contract's own seven census
commands on the same file: 0 malformed, 0 dup ids, 0 enum violations, 0 missing used-by paths. With
S029 added: rows 31, tier.A 29, W04 3, exit 0 — lawful but a rule-4 duplicate, so not recommended.

**Proposed rows, in-place used-by old→new pairs, ordering constraint, and Gate-quote candidates**
(URL, ≤25-word quote, location, digests I re-derived) are in
`/fast/scratch/hyaku/revenger-r62/R62ReviewSourcesContract/proposed-SOURCES-rows.md` — a scratch
artifact, **not** landed; L1 owns the `corpus/SOURCES.md` write. Two quote traps found there: the
ECMA §14.3.3.3 quote's `?` is followed by U+00A0 (ASCII-space variant 0 hits, NBSP 4 hits — a
space-typed quote cannot byte-match; the round-61 lesson recorded the ASCII form at
`corpus/lessons/round-61.md:56`), and the live ECMA page exposes no "last modified" string, so S022's
anchor claim "last-modified 2026-10-19" is not re-derivable from the fetched bytes — anchor on the
draft date actually read (`October 16, 2026`). `https://tc39.es/ecma262/2026/` is a different, older
draft ("March 31, 2026") and `…/multipage/` a smaller rendering of the same October draft; neither may
replace the URL S022 cites.

**Unknowns and limits.** I fetched the two raw execution-specs files at tag and commit (byte-identical,
`cmp` clean); the tree URL is a revision anchor, not a page I read, so the opener must confirm it.
Whether the C04/C09 entries cite S016/S022 is L1's call; the used-by appends are conditioned on that.
Q11 completeness of the entries is out of scope. Cross-lane sharing: grep of all 21 lane
`corpus/SOURCES.md` files finds `tc39.es/ecma262` and the execution-specs tree URL in revenger only.

**No admissions claimed.** No entry admitted, no README map row flipped, no gate claimed. The two
round-62 candidate files are absent, so no used-by path may name them yet (E11). No claim about C04/C09
admission. Installs: none — nothing installed or updated in this lane.
