RESULT: COMPLETE

Seat RevengerR61-2.R62DebtQ12Flip — Q12 / S024 successor-flip debt, frozen `a3498e25ad87bf756288812d0ea7c474b09433c7`. Frozen tree extracted with `git -C /home/vgpnk/Projects/shokunin/revenger-shokunin archive a3498e25… | tar -x` to /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62DebtQ12Flip. Checks ran on that tree or read-only public fetches. Only lane write: this report.

## 1. Frozen texts (opened this round)
- `QUALITY.md:24` Q12 pass: "its `flip` names a change to the source (a successor or revision) or a scope the reject reason does not exclude"; reject-when: "the flip asks for content the row already credits the source with, so it can never change the verdict (S008, superseded by S024)". `:4-5`: criteria are "superseded by new rows that name the row they replace, never rewritten".
- `SOURCES.md:38` S024: "supersedes S008 — REJECTED: live-system incident collection ordering (§2.1) is outside this province's static shipped-artifact ledgers; flip: a successor RFC or BCP supersedes RFC 3227, or the province takes up live-system evidence collection"; status `rejected`, `used-by —`.
- `SOURCES.md:22` S008 flip: "an entry needs its volatility-ordering primitive specifically".
- `PROVINCE.md:3-5` owns shipped artifacts (binaries, assemblies, Electron/JS packages, APKs, archives, firmware, browser/Electron runtime evidence); no host incident-response collection.
- `README.md:33,38` C04/C09 read `uncovered` — observed, unchanged; nothing admitted.

## 2. Why a successor RFC alone cannot negate the scope reason
R = "live-system incident collection ordering (§2.1) is outside this province's static shipped-artifact ledgers"; branch A = "a successor RFC or BCP supersedes RFC 3227"; branch B = "the province takes up live-system evidence collection".
- P1 (observed) R is a scope predicate over subject-versus-province; A changes the document's bibliographic status, not either term.
- P2 (observed) §2.1's subject is live-system volatile ordering: fetched rfc3227.txt (18,468 B, sha256 `32e81a23…a6c5`), lines 186-187 carry the quote and 190-200 list "registers, cache / routing table, arp cache, process table, kernel statistics, memory / temporary file systems / disk / remote logging"; intro 74-75 addresses "System Administrators … collection and archiving of evidence".
- P3 [INFERENCE] a successor in BCP 55's stream carries incident-collection guidance; and even a differently-scoped successor is a different source, which contract rule 1 requires to be opened and rowed on its own (`CORPUS.md:116-118` rule 2: corrections are new rows opening `supersedes S0NN —`), leaving §2.1's subject unchanged.
- P4 (observed) R never mentions RFC 3227's status.
=> Satisfying A leaves R true, so S024 stays rejected; A cannot change the verdict — the same rationale as Q12's reject-when ("can never change the verdict") through a mechanism it does not name (status change, not content the row already credits). Only B flips.
Today (fetched 2026-10-21): rfc3227.json `status "BEST CURRENT PRACTICE"`, `obsoleted_by []`, `updated_by []`, `pub_date "February 2002"`; info/bcp55 "BCP 55 subseries contains 1 RFC" — A is currently unrealizable too.

## 3. Q12 verdict and C1 impact
- S024's pass is correct and unchanged: branch B is "a scope the reject reason does not exclude", so the pass clause is met literally (consistent with `lessons/round-61.md:37`, `falsify-w3/W3QualityQ12Fail.md:13`). Q12 neither fails S024 nor credits branch A.
- The debt is record honesty of S024's `teaches` cell (an inert branch listed as a flip), not an admission defect: S024 `rejected`, `used-by —`; `grep -rn "S024\|S008" corpus/knowledge/` → no matches; both retained round-61 entries mark Q12 `n/a`.
- K / README: unchanged, C04/C09 uncovered; this seat admits nothing.

## 4. Proposed disposition (no QUALITY Q12 or S024 edit)
Scratch artifact `/fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62DebtQ12Flip/proposed-round-62-lesson-debt.md`:
1. Routed-debt row — deferred, no admission dependency; revisit trigger: `obsoleted_by` non-empty AND an in-province successor proposed → open it, row it separately; never edit S024. Cites `SOURCES.md:38`, `QUALITY.md:24`, the fetched metadata.
2. Reading note (interpretation only, no new gate): Q12's "can never change the verdict" rationale applied per branch — credit only branches whose satisfaction would make the reject reason false; a status-change branch leaving a scope reason true is recorded inert. Binds source-row records only; Q01–Q13 bytes unchanged; no effect on the two new entries.
3. Deferred option, not this round: supersede Q12 with a new criterion row naming Q12 (`QUALITY.md:4-5`) whose reject-when covers verdict-inert branches.

## 5. Pre-screen for the new entries (tested, read-only)
`python3 -B /fast/scratch/hyaku/revenger-r62/RevengerR61-2.R62DebtQ12Flip/q12_citation_check.py <tree> corpus/knowledge/round-62-evm-dispatch-byte-evidence.md corpus/knowledge/round-62-commonjs-require-name-evidence.md`
Expected PASS: every cited `S###` row `mined` and tier A. Tests: negative control on both retained rejected entries → `RESULT: PASS` exit 0 (12 cited rows: S002 S016-S019 S026 / S002 S020-S023 S027); `source: S024` + `support: S008` → FAIL exit 1; `source: S025` → FAIL exit 1 (tier C). Limitation: any `S\d{3}` mention counts as a citation, so a deliberate mention must be justified in the entry's Q12 cell; PASS is a pre-screen, not Q11 completeness.

## 6. Preservation and unknowns
- Live = frozen digests: `SOURCES.md` `aa7b07e1…ab58`, `QUALITY.md` `811ebf73…45d1`, retained entries `3e17b88f…9361` and `690db9f1…a6f3`; `git status --porcelain` shows only the new `.ufo/waves/round-62/` directory.
- Unknowns: (a) a future successor's content cannot be observed before publication; §2 is content-independent except the labeled P3 [INFERENCE]; (b) no LSP server answers for this markdown corpus — text grep used as the literal fallback and recorded, so row/Q12 evidence is literal file text, not semantic LSP proof; (c) census/measure reruns and entry drafting are outside this seat's scope.
- Installs/upgrades: none.
