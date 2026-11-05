# ScribeEntry — round 93 C08 entry draft (revenger, attempt 1)

**Behaviour.** Drafted the C08 knowledge entry from the lane's saved round-77 CDP record. The draft is at
`.ufo/waves/round-93/w1/ScribeEntry/entry-draft.md`; the L1 lands it at
`corpus/knowledge/round-93-browser-cdp-runtime-evidence.md`. Nothing outside my wave dir was written except this
report; `corpus/**`, `reports/**` and the sibling repos were read only.

**Files written** (all under `.ufo/waves/round-93/w1/ScribeEntry/`):

| file | what it is |
|---|---|
| `entry-draft.md` | the entry draft, 37 729 bytes, 9 fenced blocks (2 `$ ` oracle blocks of 18 stdout lines each, 7 `transcript —` one-liner blocks of 4–11 stdout lines each) |
| `READY` | `sha256=0db16a56fb0c2346d7109999dd6d98123403a52fa67d189112ba5597860593da` — sha256 of the draft bytes with the `admission-status:` line normalised to `admission-status: candidate` (the counter's and voters' exact normalisation) |
| `sources-used.txt` | the two S-row texts used (S495, S496), quoted from the scout's `sources-draft.md` |
| `ScribeEntry.md` | this report |

**Digest check.** The READY digest recomputes: I re-read the landed bytes, applied the counter's
`re.sub(r"^admission-status: (candidate|admitted|rejected)$", "admission-status: candidate", text, flags=re.M)` and
`hashlib.sha256(norm.encode("utf-8"))`, and got the same value as the READY line. The raw file digest is identical
to it too, because the draft already carries `admission-status: candidate`.

**Gates run** (from the lane root, on the draft at its wave-dir path):

- `PYTHONUTF8=1 python3 -B corpus/lint_entry.py --entry .ufo/waves/round-93/w1/ScribeEntry/entry-draft.md --lane
  /home/vgpnk/Projects/shokunin/revenger-shokunin` → `LINT_QMAP=0 LINT_Q14=0 LINT_Q15=0 LINT_HEADER=0`, exit 0.
- `PYTHONUTF8=1 python3 -B corpus/check_embedded_outputs.py --entry .ufo/waves/round-93/w1/ScribeEntry/entry-draft.md`
  → `checked_blocks=2 problems=0`, exit 0.
- Both gates re-run against a copy of the draft at `corpus/knowledge/round-93-browser-cdp-runtime-evidence.md`
  inside a `git archive 02050cb2a…` materialisation of `corpus/` (the tree shape the frozen counter builds) →
  lint exit 0, embedded exit 0.

**Key numbers** (every one re-derived by a command inside the entry, output embedded verbatim):

- oracle `ORACLE OK (17/17 checks)`, exit 0 — 17 byte-derived checks over the committed fixture bytes.
- record `corpus/live/runs/round-77/inspection.json`: 10 816 bytes, sha256 `b045a4ee…ae868`, equal to the receipt's
  recorded `stdout_sha256`; receipt `exit_code` 0, `duration_seconds` 3.498.
- fixture `index.html` 316 bytes sha256 `46e51761…deb45`; `app.js` 101 bytes sha256 `fb079fa2…aa593`.
- script lengths 46 (inline, from the `index.html` bytes) and 101 (`app.js`), both equal to the record's
  `scripts.items[].length`.
- both `cdp_hash` values equal the sha256 of the corresponding authored script text
  (`fb079fa2…aa593` for `app.js`, `ee8e9624…b783` for the inline script) — verified `True` both sides.
- exactly one resource: `Script` / `text/javascript` / content_size 101; `app.js` reconciliation `exact`, inline
  reconciliation `unmatched`.
- target `http://127.0.0.1:8477/index.html`, origin `http://127.0.0.1:8477`, title `r77 probe page [loaded]`.
- `evidence_id` shape `ev_<64hex>` — the oracle checks the shape only; the value is reported as a record field.

**Header.** `source:` cites exactly S495 (own-work, tier A, opened 2026-11-05) and S496 (Chrome DevTools Protocol,
docs, tier A, opened 2026-11-05, opened 2026-11-05 by ScoutRecord), both quoted from
`.ufo/waves/round-93/w1/ScoutRecord/sources-draft.md` and copied into `sources-used.txt`. `verified-at:` names the
lane commit `02050cb2a6758e3bd9cec696ff0e42df6f23511a` with the two commands that derive it
(`git rev-parse …^{commit}` → the same sha; `git diff --quiet … -- corpus` silent — I ran both: the corpus tree is
byte-identical at that commit). `recheck:` is the one runnable oracle command, states the `ORACLE OK (17/17 checks)`
tail, and points at the unnumbered `## Reproduce` section. `coverage-map: C08`. `admission-status: candidate`.

**Boundary discipline.** The entry states one fixture-scoped fact set: one provider operation
(`inspect_web_page`), one authored inert fixture of two static files, one saved round-77 record. No general Chrome /
CDP / Electron / browser claim (Q10); no producer-readiness claim — no producer was invoked, and the receipt's
fields are labelled **recorded** (Q05); no authenticity claim — every digest binds bytes only (Q09). Observation,
inference and unknown are separated into three sections, and 9 limitations are named (items 19–27), including which
side of each comparison is a byte reading.

**Defects / findings (reported, not hidden).**

1. **`python3 -c` one-liners cannot be `$ `-fenced blocks.** The frozen `corpus/check_embedded_outputs.py` confines
   a replayable command to `python3 [-B] <relative script inside the tree> [args]` and refuses `-c`/`-m`; a `-c` block
   makes the gate answer `could-not-evaluate` for the whole entry (I confirmed this: exit 2). The entry therefore
   quotes the seven one-liner transcripts under a `transcript —` marker (each block shows its exact command line and
   its verbatim stdout) and keeps only the oracle command in a `$ ` block, which the gate does replay. The entry
   states this openly in its reading rule and in limitation 26, so no reader mistakes a transcript for a replayed
   check. This is a formatting constraint of the frozen gate, not a weakening of the derivation discipline: every
   count still carries the command that derives it and that command's real output.
2. **Three oracle checks mix expectation sides.** `app.js script length == 101 and reconciliation exact`,
   `metadata.dom_urls == exactly the app.js src` and `resources == 1 app.js entry, content_size 101, text/javascript`
   each compare a byte-derived side against a fixed or literal side. Item 24 names them in neither column and says
   which side each part comes from. I read `corpus/fixtures/browser-r77/oracle_check.py` to confirm each part.
3. **r92 spot-check defect 2 (invented section numbers) avoided.** The r92 entry's `recheck:` cited a `§8` that did
   not exist; the sibling commands lived in the unnumbered `## Reproduce`. My `recheck:` points at `## Reproduce`, and
   the entry contains no numeric section reference at all (verified: `re.findall(r"§\d+", text)` is empty).
4. **The counter's `C1_SOURCES` leg only reads the first 15 lines.** I checked that the entry's head collects
   exactly `S495` and `S496` and nothing else, and that against the scout's row texts both rows satisfy the leg
   (11 cells, `status` `mined`, `opened` `2026-11-05`, `used-by` naming
   `corpus/knowledge/round-93-browser-cdp-runtime-evidence.md`). I also ran
   `corpus/audit_source_quotes.py verify --sid S496` against a scratch `SOURCES.md` copy carrying the two rows and the
   scout's receipts → `S496 terminal=S496 state=verified (ok)`, exit 0. The real rows land with the L1's
   `corpus/SOURCES.md` edit; the receipt directory the counter reads is `reports/round-93/quote-receipts/`, which the
   L1 must populate from the scout's `.ufo/waves/round-93/w1/ScoutRecord/quote-receipts/` (S495 is own-work and has
   no `http` in its source cell, so only S496 needs a receipt).
5. **`C1_ADMITTED` requires `admission-status: admitted` in the landed tree.** The counter's digest normalises
   candidate/admitted/rejected to `candidate`, so the digest above is stable across that flip — but the landed entry
   itself must carry `admission-status: admitted` for the leg to pass. That is the L1's landing edit; the digest in
   `READY` is the one the votes must bind.
6. **`C1_C08_CITES` needs the README row.** The C08 row of `corpus/README.md` must cite
   `knowledge/round-93-browser-cdp-runtime-evidence.md` and read `held`; `corpus/README.md` is not mine to edit.
7. **No tool was installed or upgraded this round**, so there is nothing to record on the tooling-authorisation
   channel.

**Verification honesty.** Every command quoted in the entry was run by me from the lane root, and its stdout was
spliced in by a generator (`/fast/scratch/hyaku/revenger-r93/ScribeEntry/build_entry.py`) rather than transcribed by
hand. I re-checked all 14 `check ok: …` lines the entry cites against the real oracle stdout (all present), the 17
bare oracle check names (all resolve to a real `check ok:` line), and 38 transcript field labels (all present as
stdout-line prefixes) — zero mismatches. I also verified the fixture is inert as the entry's limitation 19 states:
`grep -cE "fetch|XMLHttpRequest|localStorage|sessionStorage|document\.cookie|location\.|WebSocket|navigator\."`
over both fixture files returns 0 for both.

**Scratch.** `/fast/scratch/hyaku/revenger-r93/ScribeEntry/` held the generator, the template and the simulation
copies; it is removed before this seat yields.
