GRADE: PARTIAL — Q12 applied to rejected rows S024 and S025, plus S024's supersession of S008 (`corpus/SOURCES.md:38-39`, `:22`)

Seat `RevengerR61-2.W3SrcRejectRows`. I ran checks on `git archive ab580698212258a55e43e9bb9bf6ac78c91eae2a` extracted to `/tmp/revenger-r61w3-W3SrcRejectRows`. That archive's `SOURCES.md` is byte-identical to the live tree (`diff -q` printed SAME_AS_LIVE). Public pages were re-opened on 2026-10-21.

## S008 supersession under contract rule 2: HOLDS
- Observed: `git diff --stat cf02419..ab58069 -- corpus/SOURCES.md` printed `17 insertions(+)` and no deletions. The `+` rows are S016–S027 only.
- Observed: the S008 row's sha256 is `4896813e…7624fed` at cf02419, 0b6ddf0, 6e89c24 and ab58069. The only past edit is round 1's `recheck` change `—`→`on-release` (8df2fce), a field rule 2 allows to change in place.
- Observed: S024's `teaches` opens `supersedes S008 —`, which is the form required by `SOURCES-CONTRACT-v1.md:50-51`. `lessons/round-61.md:27` and `:68-69` record "S008 is not edited (rule 2)". `QUALITY.md:24` names "S008, superseded by S024". S008 keeps `status rejected`; the contract has no `superseded` status (census enum, `:76`).

## S024 under Q12: PARTIAL. The verdict stands; one flip branch can never fire, and the reason overstates the province.
- The quote is located and confirmed. I re-fetched `https://www.rfc-editor.org/rfc/rfc3227.txt`: HTTP 200, 18,468 B, sha256 `32e81a23…a6c5`, the same bytes as `build/ScoutSpotcheckIntake.md:13`. Lines 181-185 read "2.1 Order of Volatility … When collecting evidence you should proceed from the volatile to the less volatile." This matches `lessons/round-61.md:63`. Lines 8-11 give "BCP: 55 … February 2002", which matches the anchor.
- The "incident" part of the reason is grounded in the Abstract, which the anchor cites: lines 74-75, "System Administrators with guidelines on the collection and archiving of evidence relevant to such a security incident". That Abstract quote was recorded in round 1 (`lessons/round-1.md:77`). Round 61's Gate quote covers §2.1 only.
- Counterexample A: the successor branch of the flip can never change the verdict, which is the M21 failure class. The reason is about scope ("live-system incident collection ordering (§2.1) is outside this province's static shipped-artifact ledgers", `SOURCES.md:38`). A successor RFC or BCP would also be sysadmin incident guidance. It would get its own row, and RFC 3227 would stay rejected on the same scope reason. So "a successor RFC or BCP supersedes RFC 3227" cannot flip this row. The branch is a leftover from S008's age-based reason (`round-1.md:140`).
  - Q12 passes it literally, because `QUALITY.md:24` accepts any "change to the source (a successor or revision)". The reject-when column catches only flips that ask for content the row already credits.
  - Current state, observed: the `rfc-index.xml` entry for RFC3227 shows `obsoleted-by ABSENT`, `updated-by ABSENT`, `is-also BCP55`, `current-status BEST CURRENT PRACTICE`. No index entry obsoletes or updates RFC3227.
- Counterexample B: "static" contradicts the province text. `PROVINCE.md:3-5` owns "reverse engineering of shipped artifacts — … browser/Electron runtime evidence", and coverage-map row C08 "browser/Electron runtime evidence" is `frontier` (`corpus/README.md:34`, `:68`). The province is therefore not static-only.
  - The flip's second branch, "the province takes up live-system evidence collection", drops the reason's word "incident". Read plainly, the province already partly covers it through C08 runtime observation.
  - Inference: the verdict still holds on narrower ground. RFC 3227 §2.1 orders host incident surfaces (lines 188-201: registers, process table, memory, disk, …). The province owns no host incident response; C08 is "passive CDP observation of a declared local page".
- This is a wording and coherence defect. The row does not misstate what the source contains, so it does not void the admission. Impacted axes: coverage (source-record quality); the discernment trend. The K count is not impacted, because S024 is in no entry's `source:`.
- Smallest safe correction: append a new row superseding S024 (S024 itself stays unedited). Its reason: "host security-incident collection (Abstract l.74-75; §2.1 l.183-201) is outside `PROVINCE.md:3-5` shipped-artifact RE, including C08 passive runtime observation of a declared target". Its only flip: "the province takes up host incident-response collection". Optionally, extend Q12's reject-when with: "a source-change flip whose change leaves the reject reason true".

## S025 under Q12: HOLDS
- The quote is located and confirmed. I re-fetched `https://www.evm.codes/`: HTTP 200, 1,208,389 B, with `"buildId":"SnI4EiV4C4sZ8lujLV3M-"`, the same as the anchor (`SOURCES.md:39`). The raw HTML contains `"Mark a valid destination for ", … "JUMP" … " or " … "JUMPI" … ". This operation has no effect on machine` (compiled markup with links). Joined, that is the `lessons/round-61.md:64` quote; the opener's rendered-DOM match is at `build/SrcEvmCodesScreen.md:17,19`.
  - L1 never re-opened S025 (`lessons/round-61.md:64`). This seat has now re-opened it independently.
- "Undated" is grounded. The opener's rendered-DOM scan printed `2026 0`, `2025 0`, `last updated 0` (`SrcEvmCodesScreen.md:10`). My raw-HTML grep for `last updated|published|20(25|26)-MM-DD` matched nothing.
- "Adds nothing beyond S016/S017" is grounded for this row's scope. The quoted note restates S017's valid-destination concept (`lessons/round-61.md:56`). The opener's quotes for JUMPI and PUSH4 (`SrcEvmCodesScreen.md:15-16`) restate S016/S017 mechanics. The opener also confirms zero selector/ABI text (`:36`).
- The flip names a source change ("a dated, versioned snapshot") together with content the reason does not exclude ("an opcode fact the specs do not"). The row does not credit evm.codes with that content, so the flip is coherent.
- Tradeoff, not a defect: `community` is never tier A (`SOURCES-CONTRACT-v1.md:30`), and Q01 forbids tier-C sole support. So even if the flip fires, the row can only lift to a `queued` lead, never to entry support. That matches the S012 precedent (`SOURCES.md:27`).
  - Note: the opener recommended `queued`, not `rejected` (`SrcEvmCodesScreen.md:44`). L1 chose rejection, with the reason logged at `lessons/round-61.md:86`. That is a curation choice and violates no Q criterion.
  - Observed: the page carries per-fork text (raw counts Cancun 6, Shanghai 3, Osaka 1), but no dated snapshot, so the flip is not already met.

## Unknowns
- RFC 3227 errata state: not opened. It does not affect the quote or the verdict.
- The evm.codes deployed revision beyond buildId: the GitHub HEAD `4553021` is context only, per the opener's own note (`SrcEvmCodesScreen.md:10`).

VERDICT: The S008→S024 supersession holds: S008 is byte-unchanged since cf02419, and S024 opens with `supersedes S008 —`. S025 holds under Q12. S024 is PARTIAL: its quote is located, but its successor-RFC flip branch can never change a scope-based verdict, and "static shipped-artifact ledgers" contradicts `PROVINCE.md:5`. This does not void C1 admission, since neither row backs an entry.
Installs: none. curl, python3 and chromium were already present; chromium was not used.
