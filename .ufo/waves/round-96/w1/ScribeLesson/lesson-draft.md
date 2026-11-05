# Round 96 lesson — DRAFT for the L1 (ScribeLesson seat)

Seat: `ScribeLesson` (role `scribe`, registry `.ufo/waves/round-96/w1/swarm-registry.json`).
Lane: `/home/vgpnk/Projects/shokunin/revenger-shokunin`. Drafting only — this seat wrote no
lane file. Every byte below is traceable to a frozen byte or to a measured command in
`receipts/` (same dir). Every Python invocation used `python3 -B`; scratch
`/fast/scratch/hyaku/revenger-r96/ScribeLesson/` is deleted before yield.

---

## 1. `## Frontier` — DRAFT section for `corpus/lessons/round-96.md`

> Paste-ready. The L1 owns the landing write; the three bracketed `<…>` slots are the L1's
> to fill from the landing run (the frontier end-census, the round's own numbers). Everything
> else is measured and frozen.

```markdown
## Frontier and census

- Census round start (pre-freeze): `reports/round-96/controls/census-round-start.log` → exit 0,
  `revenger ok /home/vgpnk/Projects/shokunin/revenger-shokunin/corpus/SOURCES.md`; 0 E-codes,
  21 W01 + 13 W04 (W01 tier-C mined rows with a used-by; W04 duplicate URLs across scopes —
  status-neutral, per the round-95 spot-check §5 item 5). Driver command:
  `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin revenger`.
  Rows 501 at round start. The receipt's own last line is the `ok` marker (the r96 receipt
  carries no literal `rc=` line, unlike the r95 one); the exit code is the driver's own
  (`sources-census.sh` exits 1 on any E-code, 0 otherwise — `scripts/sources-census.sh:803-806`).
- Census round end: runs after landing — `<round-end census command and its exit code>`.
- Rows: 501 → 504 (S502, S503, S504 appended inside the `## Registry` section, after S501).
  Rows touched old→new: none (append-only; no status/recheck/used-by change in place).
- Rows added this round: **S502** (REA native-and-artifacts reference at revision `12f6e09`,
  tier A, `mined`, opened 2026-11-05) · **S503** (REA skill `SKILL.md` at revision `12f6e09`,
  tier A, `mined`, opened 2026-11-05) · **S504** (the saved round-96 native-session record
  `corpus/live/runs/round-96/`, tier A, `mined`, opened 2026-11-05) — all three with
  `used-by` = `knowledge/round-96-native-analysis-sessions.md`, the only entry that cites them.
- Tier histogram: A +3 (A=452 → 455); B and C unchanged. Status: mined +3 (465 → 468).
- Frontier row advanced: **C02 `partial` → `held`**. Its knowledge cell now names
  `knowledge/round-96-native-analysis-sessions.md` alone (the entry that carries the claim);
  the C02 cell's previous two names (`knowledge/seed.md` census,
  `knowledge/2026-10-12-rea-readiness-checklist.md`) leave that cell, and no other coverage
  row changes (the frozen counter's `C1_ONLY_C02` leg requires every other coverage row
  byte-identical to the base archive).
- Sourced claim: C1 rests on S502 and S503 (§2b.4) plus the own-work record S504.
```

**Facts behind this section** (all measured; receipts in `receipts/`):

| claim | source of truth |
|---|---|
| rows 501 at round start; tier A=452, B=21, C=28; mined 465 | `census-round-start.log` (round-start) and a live re-run of the same driver command: `revenger rows 501`, `revenger tier.A 452`, `revenger tier.B 21`, `revenger tier.C 28`, `revenger status.mined 465` |
| census exit 0 with 0 E-codes, 21 W01 + 13 W04 | `census-round-start.log` (21 `W01` + 13 `W04` + 1 `ok`); re-run reproduces rc=0 and the identical 21/13/1 profile — `receipts/census-roundstart-rerun.log` |
| exit-code semantics of the driver | `scripts/sources-census.sh:803-806` — `exit 1` on any E-code, else `exit 0`; the `ok` marker is emitted only when the lane has no E-code (`scripts/sources-census.sh:740-745`) |
| coverage map has 15 rows, C02 = `partial`, other 14 unchanged | `corpus/README.md` coverage table read directly; `C02` cell 2 currently names `knowledge/seed.md` (census) + `knowledge/2026-10-12-rea-readiness-checklist.md`; `C1_ONLY_C02` is a frozen leg of the counter |
| the new entry is not yet named in any coverage cell | direct read of all 15 rows' cells 2–3: `knowledge/round-96-native-analysis-sessions.md` appears in **no** coverage cell today, so C02's cell 2 is the only place it must land |
| the four other admitted entries keep their coverage names | `knowledge/round-72-tool-landscape.md` (C15), `round-92-managed-assembly-metadata-evidence.md` (C03), `round-93-browser-cdp-runtime-evidence.md` (C08), `round-95-evidence-ledger-discipline.md` (C10) — the frozen `C1_ADMITTED_UNION` leg requires every admitted knowledge file to be named in the coverage-row union, so those four must survive the C02 cell edit |

---

## 2. `## Gate` — DRAFT sources block for `corpus/lessons/round-96.md`

> House format follows the round-95 lesson (`corpus/lessons/round-95.md`, `## Gate` →
> "Opened THIS round, located quotes (≤25 words), access date 2026-11-05"). Every quote below
> is **verbatim from the frozen bytes**, with its location named precisely.

```markdown
### Source openings (CORPUS rule 1; access date 2026-11-05 for every row)

- **S502** — REA native-and-artifacts reference at revision `12f6e09`,
  `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/references/native-and-artifacts.md`,
  HTTP 200, 38167 bytes, sha256 `c818ee342477a2b1bf613f8b2074f284298edd5ab989ac15f97f728de563cc24`
  (receipt `reports/round-96/quote-receipts/S502.receipt.json`; body committed at
  `reports/round-96/quote-receipts/raw/S502.body`; fetch-log line in
  `reports/round-96/quote-receipts/fetch-log.md`).
  Quote (12 words), body chars 26309–26411, body line 425, section `## DOS MZ with Ghidra`
  (heading at body line 418): "rea decompile <path> --file-offset=0x... --provider ghidra`
  resolves the source byte offset internally".
  Teaches the CLI file-offset route: `--file-offset=0x…` on `rea decompile` is resolved to
  the source byte offset internally, so the caller passes the file offset rather than an
  analysis address.
- **S503** — REA skill `SKILL.md` at revision `12f6e09`,
  `https://raw.githubusercontent.com/morluto/rea/12f6e0974cc0db0b3a9b86246accc76556837222/.agents/skills/reverse-engineer-anything/SKILL.md`,
  HTTP 200, 35095 bytes, sha256 `b5f17fdff254804c723c8fa34a5b51180569e117437cddc7305dba2c59796ccc`
  (receipt `reports/round-96/quote-receipts/S503.receipt.json`; body committed at
  `reports/round-96/quote-receipts/raw/S503.body`; fetch-log line in
  `reports/round-96/quote-receipts/fetch-log.md`).
  Quote (17 words), body chars 257–389, body line 3, YAML frontmatter `description:` value:
  "Use shipped-artifact or requested runtime evidence to explain features, compare versions,
  decompile code, or guide a reconstruction."
  Teaches the skill's declared scope: decompiling code is one of the stated shipped-artifact
  uses, i.e. the scope the skill claims, not a demonstration that it ran.
- **S504** — saved round-96 native-session record — `corpus/live/runs/round-96/`
  (own-work; opened 2026-11-05; no fetch receipt, own-work rows carry none).
  Quote (6 words), `corpus/live/runs/round-96/codeable-decompiled.c` lines 6–10, the entry
  function block: "undefined8 entry(void) { return 0x2a; }".
  Teaches one demonstrated session on the committed authored fixture: the `entry` function at
  `140001000` decompiles to a body returning `0x2a`, matching the fixture's authored premise.
```

### 2a. The located-quote basis, stated so no byte-level re-checker trips over it

The two receipt spans are **character** offsets into the decoded body, and the frozen verifier
`corpus/audit_source_quotes.py` slices the decoded string (`text[s:e]`,
`corpus/audit_source_quotes.py:103-107`) — so the receipt's basis is the basis the verifier
uses. Both bodies contain exactly one non-ASCII character (U+2013 EN DASH), which is why a
byte-offset reading lands two bytes off S502's quote:

| sid | body bytes / chars | non-ASCII | quote char span | quote byte span | `text[s:e] == quote` | `bytes[s:e] == quote` |
|---|---|---|---|---|---|---|
| S502 | 38167 / 38165 | U+2013 at char 11420 | 26309–26411 | 26311–26413 | **True** | False |
| S503 | 35095 / 35093 | U+2013 at char 21568 | 257–389 | 257–389 | **True** | True |

Both receipts verify green on the committed bytes:
`PYTHONUTF8=1 python3 -B corpus/audit_source_quotes.py verify --sources corpus/SOURCES.md --receipts reports/round-96/quote-receipts --sid S502 --sid S503` →
`S502 terminal=S502 state=verified (ok)`, `S503 terminal=S503 state=verified (ok)`,
`SUMMARY rows=2 verified=2 unreachable=0 unresolved=0`, exit 0.

**Location precision for each quote:**

| row | quote | located at | section / field |
|---|---|---|---|
| S502 | 12 words | body chars 26309–26411 = body line 425 | section `## DOS MZ with Ghidra` (heading at body line 418); the sentence begins "For Ghidra decompilation, `procedure_pseudo_code` also accepts `procedure: \"file-offset:0x...\"`; CLI " |
| S503 | 17 words | body chars 257–389 = body line 3 | YAML frontmatter `description:` value (the `description:` key spans body lines 3 only, at the pinned revision) |
| S504 | 6 words | `corpus/live/runs/round-96/codeable-decompiled.c` lines 6–10 | the `entry` function block; file header lines 1–4 give `program_name=fixture.exe`, `image_base=140000000`, `function_count=1`, `// ==== FUNC entry @ 140001000 ====`; line 14 gives `// decompiled_ok=1 of 1` |

Word counts use the lane's whitespace-split rule (the r95 lesson's `(13 words)` erratum,
`corpus/lessons/round-95.md` Corrections C-r95-1): S502 = 12, S503 = 17, S504 = 6 — all ≤ 25.

### 2b. A second S502 quote the entry's route table leans on (not yet in any receipt)

The entry's route table cites **two** S502 sections, but the S502 receipt pins **one** quote
(the CLI file-offset sentence). The other cited section, `## Native targets` (body line 285),
carries the boundary sentences the entry paraphrases. Located, verbatim, 20 words:

> body chars 17777–17942 = body lines 290–292, section `## Native targets`:
> "Addresses and recovered pseudocode are analysis observations, not original source. Provider
> unavailability and unsupported metadata remain unknown rather than false."

Two facts the L1 should decide on, not this seat:

1. **Whether to add a second receipt for that span.** The frozen `C1_RECEIPTS` leg iterates
   `RECEIPT_ROW_IDS = ("S502", "S503")` only (`reports/round-96/c1_k_admit_counter5.py:42`) and
   the frozen `C1_QUOTES` leg runs `audit_source_quotes.py verify --sid S502 --sid S503`
   (`reports/round-96/c1_k_admit_counter5.py:385-398`). A new receipt file for the same sid
   would be read by the *audit* tool's
   receipt loader (last-file-wins per sid) — the L1 must not add one casually. **Recommended:
   do not add a receipt; cite the span above in the Gate block as a located body span of the
   already-verified S502 body.** It is the same body, same revision, same sha256 — a second
   receipt for the same sid is the risky move, not a second span.
2. **Whether the Gate block's single S502 quote is enough to ground the `## Native targets`
   clauses.** It is not: the located quote grounds the CLI file-offset clause only. The
   `## Native targets` clauses are grounded by the span above. If the L1 wants the teaches
   sentence to carry both, the second span must be located too — which is why the teaches
   sentence above is written to claim **only** what the located quote grounds.

---

## 3. Per-row `teaches` review — is the teaches sentence inside what the quote and anchor ground?

One paragraph per row. Each reviews the **teaches cell** the row will carry (the `teaches`
column of `corpus/SOURCES.md`, `CORPUS.md` §Registry: "one grounded learner benefit"), against
that row's located quote and anchor, and flags any overreach.

**S502 — teaches: "the CLI file-offset route: `--file-offset=0x…` on `rea decompile` is
resolved to the source byte offset internally, so the caller passes the file offset rather
than an analysis address."** *Inside the ground.* The quote says exactly that, and the anchor
is precise (body chars 26309–26411, body line 425, `## DOS MZ with Ghidra`). The teaches
sentence adds no capability claim: it says the CLI *resolves* the offset, not that
decompilation succeeds, not that the route is available on this host, and not that any
provider other than ghidra behaves this way. One clause to watch — "so the caller passes the
file offset rather than an analysis address" is an inference from "resolves the source byte
offset internally", not a quotation; it is a fair reading, but if the L1 wants the cell to be
purely quotational, cut it to "…resolves the source byte offset internally" and stop there.
**Not an overreach:** the row claims nothing about `procedure_pseudo_code`'s file-offset
*selector* form, about the "existing symbols win" rule, or about the `inspect_native_load_image`
contract — all of which the same body states elsewhere (body lines 425 and 420) but which this
row's located quote does not cover. If the L1 wants the row's scope to mention them, the
corresponding spans must be located in the Gate block; the located quote alone does not ground
them.

**S503 — teaches: "the skill's declared scope: decompiling code is one of the stated
shipped-artifact uses, i.e. the scope the skill claims, not a demonstration that it ran."**
*Inside the ground, and the second clause is what keeps it there.* The quote is the frontmatter
`description:` value, and a frontmatter description is a statement of intent. The teaches
sentence therefore says "declared scope" and explicitly marks the row as **not** a
demonstration. This is the row where overreach is most tempting — "the skill can decompile
code" or "the skill supports native decompilation" would read the intent sentence as a
capability claim and would not be grounded by the located quote. **Flagged overreach to avoid:**
any phrasing that turns the frontmatter into a capability, a readiness, or an accuracy claim.
One further precision note: the pinned body at `12f6e09` declares `metadata.version: "49"`,
while the installed copy declares `metadata.version: "42"` (S002's row) — the row must cite the
**pinned** body (it does) and must not say "the installed skill declares …", because the
installed copy's bytes differ from the pinned ones (the entry's Unknown section discloses this;
the drift is material — 38167 vs 18911 B for S502's file, 35095 vs 23437 B for S503's).

**S504 — teaches: "one demonstrated session on the committed authored fixture: the `entry`
function at `140001000` decompiles to a body returning `0x2a`, matching the fixture's authored
premise."** *Inside the ground.* The quote is the decompiled body itself
(`codeable-decompiled.c` lines 6–10), so "the `entry` function … decompiles to a body returning
`0x2a`" is literally the quoted bytes. The clause "matching the fixture's authored premise" is
supported but is a *cross-reference*, not part of the quote: the premise is the committed
generator `corpus/fixtures/pe-r75-headless-smoke/gen_pe_r75.py` plus the fixture's
`truth.json`, and the entry's derivation table carries the byte-identity check
(`cmp` rc 0 on the regen). It is legitimate as long as the row does not present the
*fixture's* truth as the row's own evidence — the row's evidence is the saved record, and the
fixture is the subject. **Flagged overreach to avoid:** any generalization from this row to
"native analysis works on this host" or to other formats/providers — the entry's Limitations
section scopes it to one 1024-byte PE32+ fixture, one address, one host, one date, and the
doctor receipt's overall `healthy: false` (Hopper absent) must not be smoothed away by this
row. The `140001000` address and the `0x2a` return value are both in the record (file header
line 4 and line 9), so the sentence is re-derivable from the committed bytes.

**Cross-row note (all three rows).** The `used-by` cell of S502/S503/S504 is what the frozen
counter's `C1_SOURCES` leg checks, and it must be exactly `{knowledge/round-96-native-analysis-sessions.md}`
— the corpus-relative form, matching `ENTRY_REL` in the frozen counter
(`reports/round-96/c1_k_admit_counter5.py:34-35`, `:374-383`). The **census** resolves the same
cell against the **lane root** (`scripts/sources-census.sh:560-569`, `:452-497`), so the
lane-root-relative form `corpus/knowledge/round-96-native-analysis-sessions.md` is what the
census's E11 leg needs on disk. The two forms are **not** interchangeable: measured both
directions on the frozen counter's own fixture tree, the bare form passes `C1_SOURCES` and
fails the census with 3× E11, while the prefixed form fails `C1_SOURCES` (set-equality on the
used-by cell) — see `receipts/usedby-form-conflict.log`. Every one of the lane's 501 existing
rows uses the lane-root-relative `corpus/…` form, and the census is green on all of them
today; the frozen counter's own fixture writes the bare form. **This is a real, unreported
conflict between two authoritative instruments, and the L1 must resolve it before landing.**
This seat does not decide it (the counter is frozen; the census lives outside the lane). It is
routed to the L1 as finding F-S1 below.

---

## 4. Findings — for the L1's integration decision

### F-S1 (blocking, material): the frozen counter and the census disagree on the `used-by` cell form for the three new rows

The frozen `C1_SOURCES` leg requires the new rows' `used-by` cell to be **exactly**
`knowledge/round-96-native-analysis-sessions.md` (corpus-relative). The fleet census's E11 leg
resolves `used-by` against the **lane root**, so on disk the path must be
`corpus/knowledge/round-96-native-analysis-sessions.md`. Measured, both directions, on the
counter's own fixture tree (`receipts/usedby-form-conflict.log`):

| used-by cell | frozen counter `C1_SOURCES` | census `validate` |
|---|---|---|
| `knowledge/round-96-native-analysis-sessions.md` | **pass** (`C1_VERDICT=pass`, rc 0) | **rc 1** — 3× E11 `missing used-by knowledge/…` |
| `corpus/knowledge/round-96-native-analysis-sessions.md` | **fail** — `C1_SOURCES_WHY=S502:usedby-exclusivity:[…]` → `C1_VERDICT=fail`, rc 1 | **rc 0**, 0 E-codes |

A third possibility is excluded by measurement: the rows must also sit **inside** the
`## Registry` section (appended at file end they draw 3× E12 `row outside Registry section`
from the census), and the counter reads the registry regardless of section.

The counter's own self-test fixture (`reports/round-96/c1_k_admit_counter5.py:628-641`, the
`add.append(...)` row builder at `:639-641`) writes the **bare** form, so the counter's positive
control and the lane's 501-row convention
point opposite ways. The L1 must pick one and record it (a used-by form that satisfies the
frozen counter leaves the census red; one that satisfies the census fails the frozen
predicate). This seat's draft assumes the counter wins for the **predicate** (it is the frozen
claim instrument and the kill rule is explicit: "Any leg fails ⇒ C1 not verified") and the
census consequence is recorded as the Frontier census line; **the L1 may decide the other way**
— the alternative makes `C1_VERDICT=fail`, which is a recorded miss under the kill rule.
Either way the round-96 lesson must record the form actually landed and the instrument that
went red.

### F-S2 (advisory): the S502 receipt pins one quote; the entry's route table cites two sections

The entry's route table cites `## Native targets` **and** `## DOS MZ with Ghidra` under S502,
but the S502 receipt's `quote` field pins only the CLI file-offset sentence from the latter
(`body chars 26309–26411`). The `## Native targets` clauses the entry paraphrases are grounded
by body chars 17777–17942 (body lines 290–292, 20 words, quoted in §2b above). The draft's
S502 `teaches` sentence is written to claim only what the pinned quote grounds; the L1 may
widen it if it also locates the second span in the Gate block. Adding a *second receipt* for
the same sid is the risky move (the audit tool loads one receipt per sid) — **not recommended**.

### F-S3 (advisory, precision): the census round-start receipt carries no literal `rc=` line

`reports/round-96/controls/census-round-start.log` ends with the driver's `revenger ok …`
marker and 0 E-codes; it has no literal `rc=0` line, unlike the r95 receipt
(`reports/round-95/controls/census-round-start.log`, last line `rc=0`). The exit code is
therefore an inference from the driver's semantics (`scripts/sources-census.sh:803-806`) plus
the absence of any E-code, not a quoted line. The draft's Frontier says "exit 0" and names the
`ok` marker; a live re-run of the identical command returns rc 0 with the identical
21 W01 + 13 W04 profile (`receipts/census-roundstart-rerun.log`). If the L1 prefers a literal
rc in the receipt, that is a control-log edit at the L1's discretion — this seat did not touch
the frozen receipt.

### F-S4 (advisory): the `used-by` exclusivity leg also constrains the *existing* S500/S501 rows

`check_sources` enforces set-equality `{ENTRY_REL}` only for `NEW_ROW_IDS = ("S502","S503","S504")`
(`reports/round-96/c1_k_admit_counter5.py:41`, `:374-383`), so the 501 existing rows' used-by
cells are not re-checked for that form. The landing edit therefore touches **only** the three
new rows' used-by cells — the other 498 mined rows keep their `corpus/…` pointers untouched,
consistent with the append-only rule (`CORPUS.md` rule 2: only `status`, `recheck` and
`used-by` change in place, each logged old→new in the round lesson). The draft's Frontier
records "Rows touched old→new: none", which is correct for this round: no existing row's
used-by changes.

---

## 5. What this seat did NOT do (explicitly out of scope)

- Did not write, edit or delete **any** lane file — not `corpus/`, not `reports/round-96/`, not
  `corpus/SOURCES.md`, not `corpus/README.md`, not `corpus/lessons/round-96.md`, not
  `SCORECARD.md` / `LOG.md` / `SKILL.md` / `README.md` / `PROVINCE.md`. The L1 lands.
- Did not run any `git`/`jj` write command; ran only read-only `git show`/`git status` for
  provenance.
- Did not touch `.ufo/state`, `.ufo/watchdog.log`, the fleet repo, sibling lanes, or
  `shokuknow`.
- Did not run the frozen counter as a *claim* check on the lane tree (it would need the votes
  and the landing rows, which do not exist yet); the counter runs in §4/F-S1 were against
  **scratch fixture trees built by the counter's own `_fixture()`**, read-only, in scratch.
- Wrote no `vote.json` — the frozen vote-file shape is scoped to ReviewerGate / ReviewerBlind /
  CriticR96; this seat is `scribe` and has no vote.
- Did not install any tool; used only the pre-installed `python3` and `bash`/`awk`/`grep`/
  `sha256sum`/`sed`.
- Left no `__pycache__`/`.pyc` under `corpus/`, `reports/round-93..96`, or
  `.ufo/waves/round-95..96` (verified empty after the run — every invocation used `python3 -B`).
- Did not fetch anything over the network. The only network use in this round's receipts
  (ScoutReopen's re-fetch) belongs to that seat; this seat re-verified the committed bodies
  from disk only.
